#!/usr/bin/env python3
"""Every reworked build against the averaged Classic Naxxramas ladder.

The comparison so far used one canonical build per spec. The rework's whole claim is that
other builds are viable, so the honest comparison is every build a class can make against
the logged number for that class's specs.

Reference is the mean of the two Classic controls, since neither is authoritative and they
disagree by 4.4 points.
"""
import importlib, itertools, statistics, sys
sys.path.insert(0,"/home/claude")
import sim, controls as C

def reference():
    top_c, top_w = max(C.CLASSIC.values()), max(C.WOWTBC.values())
    out={}
    for k in C.CLASSIC:
        v=[100*C.CLASSIC[k]/top_c]
        if k in C.WOWTBC: v.append(100*C.WOWTBC[k]/top_w)
        out[k]=statistics.mean(v)
    return out

CORE={"Warrior":["warrior-arms-rebuilt","warrior-fury-rebuilt","warrior-protection-rebuilt"],
 "Rogue":["rogue-combat-rebuilt","rogue-assassination-rebuilt","rogue-subtlety-rebuilt"],
 "Mage":["mage-fire-rebuilt","mage-frost-rebuilt","mage-arcane-rebuilt"],
 "Warlock":["warlock-destruction-rebuilt","warlock-affliction-rebuilt","warlock-demonology-rebuilt"],
 "Hunter":["hunter-marksmanship-rebuilt","hunter-beast-mastery-rebuilt","hunter-survival-rebuilt"],
 "Druid":["druid-feral-combat-rebuilt","druid-balance-rebuilt","druid-restoration-rebuilt"],
 "Shaman":["shaman-enhancement-rebuilt","shaman-elemental-rebuilt","shaman-restoration-rebuilt"],
 "Priest":["priest-shadow-rebuilt","priest-discipline-rebuilt","priest-holy-rebuilt"],
 "Paladin":["paladin-retribution-rebuilt","paladin-protection-rebuilt","paladin-holy-rebuilt"]}
EXPANDED={"Warrior":["runeblade"],"Rogue":["bladedancer"],"Mage":["necromancy","chronomancer"],
 "Warlock":["metamorphosis"],"Hunter":["survival"],"Shaman":["conduit"],"Paladin":["blackguard"],
 "Druid":[],"Priest":[]}   # Dreamer and Radiance are candidates, held out of the default set
SPLITS=[(31,20),(30,21),(26,25),(31,15,5),(30,16,5),(26,20,5),(25,21,5),(21,20,10)]

# a build with no damage tree deep is a healer or a tank, and comparing it on damage is
# not a finding. Excluded rather than reported as a zero.
HEALING={"priest-discipline-rebuilt","priest-holy-rebuilt","druid-restoration-rebuilt",
 "shaman-restoration-rebuilt","paladin-holy-rebuilt","paladin-protection-rebuilt",
 "warrior-protection-rebuilt"}

def isDamage(assign):
    deep=max(assign, key=lambda z:z[1])[0]
    return deep not in HEALING

def builds(cls, withExpanded=False):
    ts=list(CORE[cls])
    if withExpanded: ts += EXPANDED.get(cls, [])
    seen=set(); out=[]
    for sp in SPLITS:
        for combo in itertools.permutations(ts, len(sp)):
            key=tuple(sorted(zip(combo,sp)))
            if key in seen: continue
            a=list(zip(combo,sp))
            seen.add(key)
            if isDamage(a): out.append(a)
    return out

def measure(cls, assign, n=14):
    return statistics.mean([sim.run(cls, assign, seed=s)[0] for s in range(1,n+1)])

def label(a):
    f=lambda t:(t.split("-",1)[1] if "-" in t else t).replace("-rebuilt","")[:9]
    return " / ".join(f"{f(t)} {p}" for t,p in a)
