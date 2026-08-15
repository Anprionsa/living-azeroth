#!/usr/bin/env python3
"""Measure every talent a build actually takes, across every core tree.

A talent worth exactly zero is not a weak talent, it is a talent that does nothing.
Four were found by accident in the Warrior sweep; this looks everywhere.
"""
import json, copy, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim
P="/mnt/user-data/outputs/talent-data.json"
BASE=json.load(open(P))
# healing and tank trees are measured by the wrong instrument here and every talent in
# them reads zero. They need heal.py and tank.py and are excluded rather than reported.
WRONG_INSTRUMENT={"priest-holy-rebuilt","priest-discipline-rebuilt","druid-restoration-rebuilt",
 "shaman-restoration-rebuilt","paladin-holy-rebuilt","warrior-protection-rebuilt","paladin-protection-rebuilt"}
HOST={"warrior-arms-rebuilt":"warrior-fury-rebuilt","warrior-fury-rebuilt":"warrior-arms-rebuilt",
 "rogue-combat-rebuilt":"rogue-assassination-rebuilt",
 "rogue-assassination-rebuilt":"rogue-subtlety-rebuilt","rogue-subtlety-rebuilt":"rogue-combat-rebuilt",
 "mage-fire-rebuilt":"mage-frost-rebuilt","mage-frost-rebuilt":"mage-fire-rebuilt","mage-arcane-rebuilt":"mage-fire-rebuilt",
 "warlock-affliction-rebuilt":"warlock-destruction-rebuilt","warlock-destruction-rebuilt":"warlock-demonology-rebuilt",
 "warlock-demonology-rebuilt":"warlock-destruction-rebuilt","priest-shadow-rebuilt":"priest-discipline-rebuilt",
 "priest-discipline-rebuilt":"priest-shadow-rebuilt","priest-holy-rebuilt":"priest-discipline-rebuilt",
 "shaman-elemental-rebuilt":"shaman-enhancement-rebuilt","shaman-enhancement-rebuilt":"shaman-elemental-rebuilt",
 "shaman-restoration-rebuilt":"shaman-elemental-rebuilt","druid-balance-rebuilt":"druid-feral-combat-rebuilt",
 "druid-feral-combat-rebuilt":"druid-balance-rebuilt","druid-restoration-rebuilt":"druid-balance-rebuilt",
 "paladin-retribution-rebuilt":"paladin-holy-rebuilt","paladin-holy-rebuilt":"paladin-protection-rebuilt",
 "paladin-protection-rebuilt":"paladin-retribution-rebuilt","hunter-marksmanship-rebuilt":"hunter-beast-mastery-rebuilt",
 "hunter-beast-mastery-rebuilt":"hunter-marksmanship-rebuilt","hunter-survival-rebuilt":"hunter-marksmanship-rebuilt"}
CLS={t["id"]:t.get("class") for t in BASE["trees"]}

def sweep(n=12):
    out=[]
    for tid,host in HOST.items():
        cls=CLS.get(tid)
        if not cls or cls not in sim.GEAR or tid in WRONG_INSTRUMENT: continue
        importlib.reload(sim)
        taken=sim.build(tid,31,forceCapstone=True)[0]
        base=statistics.mean([sim.run(cls,[(tid,31),(host,20)],seed=s)[0] for s in range(1,n+1)])
        if base<=0: continue
        for name in list(taken):
            D=copy.deepcopy(BASE)
            for t in D["trees"]:
                if t["id"]!=tid: continue
                for r in t["rows"]:
                    for x in r["talents"]:
                        # strip everything including grants. Keeping the grant means an
                        # ability-granting talent measures as worth nothing, because the
                        # thing that makes it worth something is still there.
                        if x["name"]==name:
                            x["effects"]=[]; x["grants"]=[]
            json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)
            importlib.reload(sim)
            v=statistics.mean([sim.run(cls,[(tid,31),(host,20)],seed=s)[0] for s in range(1,n+1)])
            out.append((tid,name,100*(base-v)/base if base else 0.0))
        json.dump(BASE,open(P,"w"),indent=1,ensure_ascii=False)
        importlib.reload(sim)
    return out

if __name__=="__main__":
    r=sweep()
    zero=[x for x in r if abs(x[2])<0.05]
    print(f"talents measured: {len(r)} | worth exactly zero: {len(zero)}")
    from collections import Counter
    c=Counter(t for t,_,_ in zero)
    print()
    for tid,k in c.most_common():
        names=[n for t,n,_ in zero if t==tid]
        print(f"  {tid.replace('-rebuilt',''):28} {k}  {', '.join(names)}")
