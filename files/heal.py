#!/usr/bin/env python3
"""Healing model. Reports effective healing per second, healing per mana, overheal
share and time to out of mana, measured against an incoming damage pattern.

Healing is not damage aimed at a friendly target. Over a five minute fight mana binds
before throughput does, and a heal landing on a full-health target is worth nothing."""
import json, random, statistics
import sim
D=sim.D
HM=D["healModel"]; PROF=D["healerProfiles"]

def heal_rotation(cls):
    r=D["rotations"].get(cls,{})
    lst=r.get("healingPriority") or r.get("priority") or []
    return [e if isinstance(e,dict) else {"ability":e} for e in lst]

def run_heal(cls, splits, pattern="steady", seconds=300, seed=1):
    rng=random.Random(seed)
    g=dict(PROF[cls]); pat=HM["damagePatterns"][pattern]
    taken={}
    for i,(tid,pts) in enumerate(splits):
        taken.update(sim.build(tid,pts,forceCapstone=(i==0 and pts>=31),role="heal")[0])
    mods=sim.modifiers(taken)
    # healing talents move throughput, cost and crit
    healMult=1.0; costMult=1.0; critAdd=0.0; manaBack=0.0; extraTargets=0; noOverheal=False
    perAbility={}     # multipliers scoped to one healing spell
    castMult={}       # cast time changes, which decide how many heals land
    granted=set()     # abilities this build actually has
    interruptGuard=0.0
    for val in taken.values():
        x,ranks = val if isinstance(val,tuple) else (val,val["ranks"])
        frac=ranks/max(1,x["ranks"])
        for _gr in x.get("grants",[]): granted.add(_gr)
        for e in x.get("effects",[]):
            if e.get("source")!="authored": continue
            op,st,v=e["op"],e.get("stat"),e.get("magnitude")
            if v is None and not (e["op"]=="enable" and e.get("flag")=="immune_overheal"): continue
            if v is None: v=1.0
            sc=e.get("scope",{}); tag=sc.get("tag"); allsc=sc.get("all"); ab=sc.get("ability")
            if e["op"]=="grant" and ab: granted.add(ab)
            if ab:
                # a multiplier on one healing spell was invisible: only tag-wide effects
                # were read, so every "Improved Regrowth" style talent measured as zero
                if e["op"]=="multiply" and st in ("healing","effect") and v is not None:
                    perAbility[ab]=perAbility.get(ab,1.0)*(1+(v-1)*frac)
                elif e["op"]=="multiply" and st=="castTime" and v is not None:
                    castMult[ab]=castMult.get(ab,1.0)*(1-(1-v)*frac)
                elif e["op"] in ("add","debuff") and st in ("stack","healing") and v is not None:
                    perAbility[ab]=perAbility.get(ab,1.0)*(1+v*frac)
                continue
            if e["op"]=="enable" and e.get("flag")=="immune_interrupted":
                interruptGuard=min(0.06, interruptGuard+0.02)
            # scope matters: a talent that makes one ability free must not zero every cost
            broad = allsc or tag in ("heal","holy","nature","spell")
            if e["op"]=="enable" and e.get("flag")=="immune_overheal" and broad: noOverheal=True
            if op=="multiply" and st in ("healing","effect") and tag=="heal": healMult*=1+(v-1)*frac
            elif op=="multiply" and st=="cost" and broad: costMult*=1-(1-v)*frac
            elif op=="add" and st=="critChance" and broad: critAdd+=v*frac
            elif op=="add" and st=="mana" and broad: manaBack+=min(v,300)*frac
            # behaviour ops the repair introduced. Without these a healing tree's rewritten
            # talents are invisible to the instrument that measures it.
            elif op=="debuff" and st in ("vulnerability","stack") and broad:
                healMult*= 1.0 + v*min(4,e.get("stacks",1))*frac
            elif op=="consume" and broad: healMult*= 1.0 + v*frac
            elif op=="addTarget" and broad: extraTargets+= int(v or 1)*frac
    raid=[10000.0]*HM["raidSize"]; maxhp=[10000.0]*HM["raidSize"]
    for i in range(HM["tankTargets"]): raid[i]=maxhp[i]=16000.0
    rot=heal_rotation(cls)
    mana=g["manaPool"]; t=0.0; gcd=0.0; eff=0.0; over=0.0; spent=0.0; oom=None; casts={}
    cd={}   # cooldowns were never tracked, so a three minute ability was cast 110 times
    spike=0.0
    while t<seconds:
        # incoming damage
        for i in range(HM["tankTargets"]): raid[i]=max(0,raid[i]-pat["tankDPS"]*0.1/HM["tankTargets"])
        for i in range(HM["raidSize"]): raid[i]=max(0,raid[i]-pat["raidDPS"]*0.1/HM["raidSize"])
        if pat["spikeEvery"] and t>=spike:
            v=rng.randrange(HM["raidSize"]); raid[v]=max(0,raid[v]-pat["spikeDamage"]); spike=t+pat["spikeEvery"]
        if t>=gcd:
            tgt=min(range(HM["raidSize"]), key=lambda i: raid[i]/maxhp[i])
            missing=maxhp[tgt]-raid[tgt]
            # a real healer does not cast into a nearly full target, and downranks so the
            # heal roughly matches the hole. Spamming the largest heal is maximum throughput
            # and minimum efficiency, which is not how anyone plays a five minute fight.
            if missing>400:
                best=None
                for ent in rot:
                    a=sim.ABIL.get(ent["ability"])
                    if not a or not a.get("baseHealing"): continue
                    # an ability a talent grants is not available unless the build took it
                    if ent["ability"] in sim.TALENT_GRANTED and ent["ability"] not in granted: continue
                    if t < cd.get(ent["ability"],0.0): continue
                    cost=(a.get("cost") or 0)*costMult
                    if cost>mana: continue
                    amt=(a["baseHealing"]+g["healingBonus"]*(a.get("spCoefficient") or 0.5))*healMult
                    amt*= perAbility.get(ent["ability"],1.0)*(1.0+interruptGuard)
                    waste=max(0, amt-missing)
                    urgent = missing > maxhp[tgt]*0.45
                    score=((waste/max(1,amt))*(0.3 if urgent else 1.0),
                           (cost/max(1,amt))*(0.3 if urgent else 1.0),
                           -amt if urgent else 0)
                    if best is None or score<best[0]: best=(score,a,cost,amt,ent["ability"])
                if best:
                    _,a,cost,amt,_aid=best
                    if rng.random()<g["critChance"]+critAdd: amt*=1.5
                    if noOverheal: amt=min(amt,missing)
                    e=min(amt,missing); eff+=e; over+=amt-e
                    raid[tgt]=min(maxhp[tgt], raid[tgt]+amt)
                    # a heal that reaches extra targets does real work on them
                    for _ in range(int(extraTargets)):
                        o=min(range(HM["raidSize"]), key=lambda i: raid[i]/maxhp[i])
                        if o==tgt: continue
                        m2=maxhp[o]-raid[o]; e2=min(amt*0.5,m2)
                        eff+=e2; over+=max(0,amt*0.5-e2); raid[o]=min(maxhp[o],raid[o]+amt*0.5)
                    mana-=cost; spent+=cost
                    if a.get("cooldown"): cd[_aid]=t+a["cooldown"]
                    casts[a["name"]]=casts.get(a["name"],0)+1
                    gcd=t+max((a.get("castTime") or 0)*castMult.get(_aid,1.0), a.get("gcd") or 1.5)
                else: gcd=t+0.5
            else: gcd=t+0.5
        mana=min(g["manaPool"], mana+0.1*(g["mp5"]+manaBack)/5.0)
        if mana<200 and oom is None: oom=t
        t+=0.1
    return {"hps":eff/seconds,"hpm":eff/max(1,spent),"overheal":over/max(1,eff+over),
            "oom":oom or seconds,"totalEff":eff,"casts":casts}

if __name__=="__main__":
    CASES=[("Priest","priest-holy-rebuilt","priest-discipline-rebuilt"),
           ("Priest","priest-discipline-rebuilt","priest-holy-rebuilt"),
           ("Druid","druid-restoration-rebuilt","druid-balance-rebuilt"),
           ("Shaman","shaman-restoration-rebuilt","shaman-elemental-rebuilt"),
           ("Paladin","paladin-holy-rebuilt","paladin-protection-rebuilt")]
    for pat in ("steady","spiky","aoe"):
        print(f"\n=== {pat}")
        print(f"  {'build':34} {'HPS':>6} {'HPM':>6} {'overheal':>9} {'OOM at':>7}")
        for cls,a,b in CASES:
            for lbl,pa,pb in (("31/20",31,20),("30/21",30,21)):
                r=[run_heal(cls,[(a,pa),(b,pb)],pattern=pat,seed=s) for s in range(1,25)]
                m=lambda k: statistics.mean(x[k] for x in r)
                nm=f"{cls} {a.split('-',1)[1].replace('-rebuilt','')} {lbl}"
                print(f"  {nm[:34]:34} {m('hps'):6.0f} {m('hpm'):6.2f} {m('overheal')*100:8.0f}% {m('oom'):6.0f}s")
