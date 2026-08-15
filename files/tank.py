#!/usr/bin/env python3
"""Threat and survivability model. Reports TPS and DTPS rather than DPS, because a
tank talent's value is threat generated and damage avoided, and no damage simulator
measures either."""
import json, random, statistics
import sim
D=sim.D
TM=D["threatModel"]; BOSS=D["bossProfile"]; TANKS=D["tankProfiles"]

def mitigation(prof):
    """Armor reduction against a level 63 attacker."""
    a=prof["armor"]; return a/(a+400+85*BOSS["level"])

def run_tank(cls, splits, seconds=300, seed=1):
    rng=random.Random(seed)
    prof=dict(TANKS[cls])
    taken={}
    for i,(tid,pts) in enumerate(splits):
        taken.update(sim.build(tid,pts,forceCapstone=(i==0 and pts>=31),role="tank")[0])
    mods=sim.modifiers(taken)

    # collect defensive and threat effects, scaled by ranks bought
    threatMult=TM["stanceMultiplier"].get(prof.get("stance"),1.0)
    if prof.get("righteousFury"): threatMult*=TM["righteousFury"]
    dtMult=1.0; threatAdd=0.0; selfHeal=0.0
    for val in taken.values():
        x, ranks = val if isinstance(val,tuple) else (val, val["ranks"])
        frac=ranks/max(1,x["ranks"])
        for e in x.get("effects",[]):
            if e.get("source")!="authored": continue
            op,st,v = e["op"], e.get("stat"), e.get("magnitude")
            if v is None: 
                if op=="enable" and e.get("flag")=="immune_crit": prof["defense"]=max(prof["defense"],440)
                continue
            if op=="multiply" and st=="threat": threatMult*= 1.0+(v-1.0)*frac
            elif op=="add" and st=="threat": threatAdd+= v*frac
            elif op=="multiply" and st=="damageTaken": dtMult*= 1.0-(1.0-v)*frac
            elif op=="add" and st=="dodge": prof["dodge"]+= v*frac
            elif op=="add" and st=="parry": prof["parry"]+= v*frac
            elif op=="add" and st=="blockChance": prof["block"]+= v*frac
            elif op=="add" and st=="blockValue": prof["blockValue"]+= v*frac
            elif op=="add" and st=="health": prof["health"]*= 1.0+v*frac
            elif op=="add" and st=="selfHeal": selfHeal+= v*frac
            elif op=="debuff" and st in ("vulnerability","stack"):
                threatMult*= 1.0 + v*min(4,e.get("stacks",1))*frac
            elif op=="consume":
                if e.get("spends")=="heal": selfHeal+= v*200*frac
                else: threatMult*= 1.0 + v*frac
            elif op=="enable" and e.get("flag")=="immune_crit": prof["defense"]=max(prof["defense"],440)
    threatMult*=(1.0+threatAdd)

    dr=mitigation(prof)
    avoid=min(0.75, prof["dodge"]+prof["parry"])
    critChance=max(0.0, TM["bossCritVsPlayer"] - max(0,prof["defense"]-315)*0.0004)
    avoid=prof["dodge"]+prof["parry"]
    t=0.0; swing=0.0; special=0.0; taken_dmg=0.0; threat=0.0; blocked=0; hits=0
    # the tank's own damage feeds threat; reuse the damage sim for output
    dps,_,_ = sim.run(cls, splits, seconds=seconds, seed=seed)
    while t<seconds:
        if t>=swing:
            r=rng.random(); dmg=BOSS["baseSwingDamage"]
            if r<0.05: dmg=0                                  # boss miss
            elif r<0.05+avoid: dmg=0                          # dodge or parry
            elif r<0.05+avoid+prof["block"]:
                dmg=max(0,dmg*(1-dr)-prof["blockValue"]); blocked+=1
            elif r<0.05+avoid+prof["block"]+critChance: dmg=dmg*2*(1-dr)
            else: dmg=dmg*(1-dr)
            taken_dmg+=dmg*dtMult; hits+=1; swing=t+BOSS["swingSpeed"]
        if t>=special:
            taken_dmg+=BOSS["specialDamage"]*(1-dr)*dtMult; special=t+BOSS["specialEvery"]
        t+=0.1
    avoid=min(0.75, prof["dodge"]+prof["parry"])
    # self-healing is mitigation. A tank that heals itself takes less net damage, and a
    # model that ignores it understates every leeching tree by exactly what it does.
    hps = selfHeal * (1.0/BOSS["swingSpeed"])
    net = max(0.0, taken_dmg/seconds - hps)
    return {"tps":dps*TM["damageToThreat"]*threatMult, "dtps":net, "grossDtps":taken_dmg/seconds,
            "selfHps":hps,
            "ehp":prof["health"]/(1-dr)/max(0.25,1-avoid)/dtMult*(1.0+hps/max(1.0,taken_dmg/seconds)),
            "critImmune":prof["defense"]>=440,
            "blockRate":blocked/max(1,hits), "threatMult":threatMult, "dps":dps}

if __name__=="__main__":
    CASES=[("Warrior","warrior-protection-rebuilt","warrior-fury-rebuilt","Prot 31 / Fury 20"),
           ("Warrior","warrior-protection-rebuilt","warrior-fury-rebuilt","Prot 30 / Fury 21"),
           ("Paladin","paladin-protection-rebuilt","paladin-retribution-rebuilt","Prot 31 / Ret 20"),
           ("Paladin","paladin-protection-rebuilt","paladin-retribution-rebuilt","Prot 30 / Ret 21"),
           ("Druid","druid-feral-combat-rebuilt","druid-restoration-rebuilt","Feral 31 / Resto 20"),
           ("Druid","druid-feral-combat-rebuilt","druid-restoration-rebuilt","Feral 30 / Resto 21")]
    print(f"{'build':24} {'TPS':>7} {'DTPS':>7} {'selfHPS':>8} {'EHP':>7} {'critImm':>8}")
    for i,(cls,a,b,label) in enumerate(CASES):
        pts=(31,20) if "31" in label.split("/")[0] else (30,21)
        r=[run_tank(cls,[(a,pts[0]),(b,pts[1])],seed=s) for s in range(1,40)]
        m=lambda k: statistics.mean(x[k] for x in r)
        print(f"  {label:24} {m('tps'):7.0f} {m('dtps'):7.0f} {m('ehp'):7.0f} {m('blockRate'):6.2f} {str(r[0]['critImmune']):>8}")
