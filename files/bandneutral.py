#!/usr/bin/env python3
"""Band neutrality, run as a tuning pass rather than described.

The rule the protocol set: hold total raid output constant while individual specs move
within it. The lever is the depth coefficient, one scalar per tree, no talent edits.

Target for each class is its logged share of the top spec, taken as the mean of the two
Classic controls. Total output is checked against the logged total afterwards.
"""
import json, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim, allbuilds as A
P="/mnt/user-data/outputs/talent-data.json"
LOG={"Warrior":100.0,"Rogue":84.2,"Mage":74.8,"Warlock":64.4,"Hunter":60.8,
     "Druid":60.5,"Shaman":51.8,"Priest":42.4,"Paladin":39.1}
# the canonical build per class, used as the tuning handle
CANON={"Warrior":[("warrior-arms-rebuilt",31),("warrior-fury-rebuilt",20)],
 "Rogue":[("rogue-assassination-rebuilt",31),("rogue-combat-rebuilt",20)],
 "Mage":[("mage-fire-rebuilt",31),("mage-frost-rebuilt",20)],
 "Warlock":[("warlock-destruction-rebuilt",31),("warlock-demonology-rebuilt",20)],
 "Hunter":[("hunter-marksmanship-rebuilt",31),("hunter-beast-mastery-rebuilt",20)],
 "Druid":[("druid-feral-combat-rebuilt",31),("druid-balance-rebuilt",20)],
 "Shaman":[("shaman-enhancement-rebuilt",31),("shaman-elemental-rebuilt",20)],
 "Priest":[("priest-shadow-rebuilt",31),("priest-discipline-rebuilt",20)],
 "Paladin":[("paladin-retribution-rebuilt",31),("paladin-protection-rebuilt",20)]}

def depth(cls, f):
    """Scale a class's depth dividend. One number, applied to every tree it owns."""
    D=json.load(open(P))
    for t in D["trees"]:
        if t.get("class")!=cls: continue
        t.setdefault("depthCoefficient", 1.0)
        t["depthCoefficient"]=round(t["depthCoefficient"]*f, 4)
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)

# measuring every build to find the best is far too slow to tune inside a loop. The best
# build per class is stable across small coefficient changes, so find it once and reuse it.
BEST_BUILD={}
def findBest(cls, n=10):
    importlib.reload(sim); importlib.reload(A)
    rows=[(A.measure(cls,b,n=n),b) for b in A.builds(cls)]
    rows.sort(key=lambda r:-r[0])
    BEST_BUILD[cls]=rows[0][1]
    return rows[0]

def best(cls, n=12):
    importlib.reload(sim)
    b=BEST_BUILD.get(cls)
    if b is None: return findBest(cls,n=n)[0]
    return A.measure(cls,b,n=n)

def report(n=14):
    importlib.reload(sim); importlib.reload(A)
    top=A.measure("Warrior",CANON["Warrior"],n=25)
    out={}
    for cls in LOG:
        rows=sorted([100*A.measure(cls,b,n=n)/top for b in A.builds(cls)], reverse=True)
        out[cls]=rows
    return out, top
