#!/usr/bin/env python3
"""Magnitude pass against stated bands.

  above +10%   unacceptable
  +5 to +10%   acceptable only if the tree excels in another scenario
  0 to +5%     the target
  -5 to 0%     acceptable
  below -5%    unacceptable

Scales a tree's behaviour magnitudes and re-measures until it lands in band. Only
magnitudes move; no talent changes what it does.
"""
import json, statistics, importlib, sys
import sim
D=sim.D
P="/mnt/user-data/outputs/talent-data.json"
SCN=["patchwerk","burst","movement","cleave","switching"]
BEST={"Paladin":("paladin-retribution-rebuilt","paladin-holy-rebuilt"),
 "Mage":("mage-fire-rebuilt","mage-frost-rebuilt"),
 "Warlock":("warlock-affliction-rebuilt","warlock-destruction-rebuilt"),
 "Rogue":("rogue-combat-rebuilt","rogue-assassination-rebuilt"),
 "Shaman":("shaman-elemental-rebuilt","shaman-enhancement-rebuilt"),
 "Warrior":("warrior-arms-rebuilt","warrior-fury-rebuilt"),
 "Hunter":("hunter-marksmanship-rebuilt","hunter-beast-mastery-rebuilt")}
TUNABLE={"debuff","consume","proc"}
# openingDamage and frontload are deliberately excluded. They are burst-weighted levers,
# and scaling them alongside sustained output undoes the thing they were added to fix.
TUNABLE_STATS={"damage","effect","vulnerability","stack","critChance","attackSpeed"}
BURST_LEVERS={"openingDamage","frontload","movingDamage","cleaveEvery"}
SCALE_COOLDOWNS=False   # a cash-out cooldown is a burst lever, not sustained output

def gaps(cls, tid, host, n=60):
    """Hold the twenty point half constant so the comparison isolates the deep tree.

    Measuring necromancy31+frost20 against fire31+frost20 is a fair test of the deep tree.
    Measuring blackguard31+retribution20 against retribution31+holy20 is not: the shallow
    half differs too, so part of the gap belongs to the host rather than to the tree.
    """
    ca,cb=BEST[cls]
    # the baseline must be a real build: a different deep tree from the one under test,
    # and a different tree from the shallow half. Comparing arms31+arms20 is 51 points
    # in one tree and not a build at all.
    # the baseline must also be a damage tree. Falling through to a healing tree makes
    # every comparison against it meaningless, and Blackguard read +71% on burst against
    # Holy paladin measured by a damage simulator.
    HEALING={"priest-holy-rebuilt","priest-discipline-rebuilt","druid-restoration-rebuilt",
             "shaman-restoration-rebuilt","paladin-holy-rebuilt","warrior-protection-rebuilt",
             "paladin-protection-rebuilt"}
    _dmg=[t["id"] for t in D["trees"] if t.get("class")==cls and t["kind"]=="rebuilt"
          and t["id"] not in HEALING]
    _shallow=host
    if ca in (tid,host): ca=next((x for x in _dmg if x not in (tid,host)), None)
    if ca is None or ca in HEALING:
        # the class has only one core damage tree besides the host, so the host cannot be
        # held constant. Compare the best real damage build instead and accept that the
        # shallow half differs, which is stated rather than hidden.
        ca=next((x for x in _dmg if x!=tid), cb)
        _shallow=next((t["id"] for t in D["trees"] if t.get("class")==cls and t["kind"]=="rebuilt"
                       and t["id"] not in (tid,ca)), host)
    out={}
    for scn in SCN:
        a=statistics.mean([sim.run(cls,[(tid,31),(host,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
        c=statistics.mean([sim.run(cls,[(ca,31),(_shallow,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
        out[scn]=100*(a-c)/c if c else 0.0
    return out

def verdict(g):
    p=g["patchwerk"]; best=max(g.values())
    if p>10: return "TOO STRONG"
    if p<-5: return "TOO WEAK"
    if p>5: return "high, acceptable" if best>=p+8 else "high, no specialisation"
    return "in band"

def scale_tree(D, tid, factor, includeBurstLevers=False):
    """Scale the behaviour magnitudes that carry a tree's output.

    Also scales the base values of abilities the tree grants. A tree's output can sit
    entirely in an ability it introduces rather than in any talent magnitude, and
    Necromancy's whole advantage was Wither's base damage.
    """
    t=next(x for x in D["trees"] if x["id"]==tid); n=0
    granted={g for r in t["rows"] for x in r["talents"] for g in x.get("grants",[])}
    granted|={e["scope"]["ability"] for r in t["rows"] for x in r["talents"] for e in x.get("effects",[])
              if e["op"]=="grant" and e.get("scope",{}).get("ability")}
    # cooldown effects live in their own table and were unreachable, so a tree whose
    # output sat in a cash-out cooldown reported as untunable while the tuner gutted
    # everything else trying to move it.
    # cooldowns are burst levers. Scaling them alongside sustained output undoes the
    # asymmetry they exist to provide, in the same way scaling an opening window does.
    # A tree brought into band on patchwerk should keep the burst it was given.
    if SCALE_COOLDOWNS or includeBurstLevers:
        for k,v in D.get("cooldowns",{}).items():
            if k not in granted: continue
            for stat in ("damage","critChance"):
                if stat in v["effect"]:
                    base=v["effect"][stat]
                    v["effect"][stat]=round(1.0+(base-1.0)*factor,4) if base>1.0 else round(base*factor,4)
                    n+=1
    for a in D["abilities"]:
        if a["id"] not in granted: continue
        for k in ("baseDamage","baseHealing"):
            if a.get(k): a[k]=round(a[k]*factor,1); n+=1
        for k in ("spCoefficient","apCoefficient","rapCoefficient"):
            if a.get(k): a[k]=round(a[k]*factor,4); n+=1
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                if e.get("source")!="authored": continue
                m=e.get("magnitude")
                if m is None: continue
                if includeBurstLevers and e["op"]=="add" and e.get("stat") in BURST_LEVERS and m is not None:
                    e["magnitude"]=round(max(0.02, m*factor),4); n+=1
                elif e["op"] in TUNABLE and e.get("stat") in TUNABLE_STATS:
                    e["magnitude"]=round(max(0.01, m*factor),4); n+=1
                elif e["op"]=="multiply" and e.get("stat") in ("damage","effect") and m>1.0:
                    e["magnitude"]=round(1.0+(m-1.0)*factor,4); n+=1
                elif e["op"]=="multiply" and e.get("stat") in ("cost","cooldown","castTime") and m<1.0:
                    # a discount is worth less as it approaches one. Scaling the discount
                    # rather than the multiplier is what makes efficiency tunable at all.
                    e["magnitude"]=round(min(0.999, 1.0-(1.0-m)*factor),4); n+=1
                elif e["op"]=="add" and e.get("stat")=="damage":
                    e["magnitude"]=round(m*factor,4); n+=1
    return n

if __name__=="__main__":
    CASES=[("Paladin","blackguard","paladin-retribution-rebuilt"),
     ("Mage","necromancy","mage-frost-rebuilt"),
     ("Rogue","bladedancer","rogue-combat-rebuilt"),
     ("Shaman","conduit","shaman-elemental-rebuilt"),
     ("Warrior","runeblade","warrior-arms-rebuilt"),
     ("Hunter","survival","hunter-marksmanship-rebuilt")]
    print(f"{'tree':14}" + "".join(f"{s[:9]:>10}" for s in SCN) + "   verdict")
    for cls,tid,host in CASES:
        g=gaps(cls,tid,host)
        print(f"  {tid:14}" + "".join(f"{g[s]:+9.1f}%" for s in SCN) + f"   {verdict(g)}")
