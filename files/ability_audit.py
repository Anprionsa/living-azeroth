#!/usr/bin/env python3
"""Ability-side coverage. An ability that is never cast, or cast without the data the
simulator needs, is a hole in exactly the way an unread effect is."""
import json
from collections import defaultdict
D=json.load(open("/mnt/user-data/outputs/talent-data.json"))
A={a["id"]:a for a in D["abilities"]}
inrot=set()
for cls,rot in D["rotations"].items():
    for k in ("priority","healingPriority","feralPriority"):
        for e in rot.get(k,[]): inrot.add(e["ability"] if isinstance(e,dict) else e)
granted=set()
for t in D["trees"]:
    for r in t["rows"]:
        for x in r["talents"]:
            granted|=set(x.get("grants",[]))
            for e in x.get("effects",[]):
                if e["op"]=="grant" and e.get("scope",{}).get("ability"): granted.add(e["scope"]["ability"])
referenced=set()
for t in D["trees"]:
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                a=e.get("scope",{}).get("ability")
                if a: referenced.add(a)
cds={k for k in D.get("cooldowns",{})}

def issues(a):
    out=[]
    # an ability whose damage is entirely coefficient-based has base zero and is fine
    off = (a.get("baseDamage") or a.get("baseHealing")
           or a.get("spCoefficient") or a.get("apCoefficient") or a.get("rapCoefficient"))
    if a["id"] in inrot:
        if off is None and "pet" not in a.get("tags",[]) and not a.get("grantsSelf") and not a.get("grantsTarget"):
            out.append("in rotation, no value")
        if off and not (a.get("spCoefficient") or a.get("apCoefficient") or a.get("rapCoefficient") or a.get("weaponMultiple")):
            out.append("no scaling coefficient")
        if a.get("cost") is None: out.append("no cost")
        if a.get("gcd") is None: out.append("no gcd")
    return out

if __name__=="__main__":
    never = sorted(i for i in A if i not in inrot and i not in cds)
    unreach = sorted(i for i in (granted|referenced) if i not in inrot and i not in cds and (A.get(i,{}).get("baseDamage") or A.get(i,{}).get("baseHealing")))
    print(f"abilities: {len(A)} | in a rotation: {len(inrot)} | cooldown table: {len(cds)}")
    print(f"never cast and not a cooldown: {len(never)}")
    print()
    print(f"GRANTED OR REFERENCED, deals damage or healing, but never cast: {len(unreach)}")
    for i in unreach: print(f"    {i:34} {A[i].get('baseDamage') or A[i].get('baseHealing')}")
    print()
    bad=defaultdict(list)
    for i in inrot:
        a=A.get(i)
        if not a: bad["missing from table"].append(i); continue
        for z in issues(a): bad[z].append(i)
    print("PROBLEMS WITH ABILITIES THAT ARE CAST:")
    for k,v in sorted(bad.items(), key=lambda kv:-len(kv[1])):
        print(f"  {k:26} {len(v)}")
        for i in sorted(v)[:8]: print(f"      {i}")
