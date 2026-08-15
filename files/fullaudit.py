#!/usr/bin/env python3
"""Every completeness check in one place.

Every pass for the last several rounds found a field that existed and nothing read.
This checks all of them at once so the next gap surfaces here rather than as a
suspicious number three passes later.
"""
import json, re, sys
from collections import defaultdict
D=json.load(open("/mnt/user-data/outputs/talent-data.json"))
A={a["id"]:a for a in D["abilities"]}
SRC={n:open(f"/home/claude/{n}.py").read() for n in ("sim","tank","heal")}
ALL="".join(SRC.values())
findings=defaultdict(list)

def add(k,v): findings[k].append(v)

# 1. effects nobody reads
NT=set(D["meta"].get("nonThroughputEffects",{}).get("flags",[]))|set(D["meta"].get("nonThroughputEffects",{}).get("stats",[]))
for t in D["trees"]:
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                if e.get("source")!="authored": continue
                op=e["op"]; st=e.get("stat") or e.get("flag")
                if st in NT: continue
                if not (f'"{op}"' in ALL or f"'{op}'" in ALL): add("effect op unread",f"{op}")
                elif st and not (f'"{st}"' in ALL or f"'{st}'" in ALL): add("effect stat unread",f"{op}/{st}")

# 2. abilities granted but unreachable
inrot=set()
for cls,rot in D["rotations"].items():
    for k in ("priority","healingPriority","feralPriority"):
        for e in rot.get(k,[]): inrot.add(e["ability"] if isinstance(e,dict) else e)
cds=set(D.get("cooldowns",{}))
for t in D["trees"]:
    for r in t["rows"]:
        for x in r["talents"]:
            ids=set(x.get("grants",[]))|{e["scope"]["ability"] for e in x.get("effects",[])
                 if e["op"]=="grant" and e.get("scope",{}).get("ability")}
            for i in ids:
                if i not in A: add("granted ability missing", i)
                elif i not in inrot and i not in cds and (A[i].get("baseDamage") or A[i].get("baseHealing")):
                    add("granted but never cast", i)

# 3. abilities cast without the data needed
for i in inrot:
    a=A.get(i)
    if not a: add("in rotation, not in table", i); continue
    off=(a.get("baseDamage") or a.get("baseHealing") or a.get("spCoefficient")
         or a.get("apCoefficient") or a.get("rapCoefficient"))
    if not off and "pet" not in a.get("tags",[]) and not a.get("grantsSelf") and not a.get("grantsTarget"):
        add("cast but does nothing", i)
    if off and not (a.get("spCoefficient") or a.get("apCoefficient") or a.get("rapCoefficient") or a.get("weaponMultiple")):
        add("no scaling coefficient", i)
    if a.get("gcd") is None: add("no gcd", i)
    if a.get("costType")=="mana" and a.get("cost") is None: add("no cost", i)

# 3b. effects scoped to a tag no ability carries
TAGS=set()
for a in A.values(): TAGS|=set(a.get("tags",[]))
for t in D["trees"]:
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                tg=e.get("scope",{}).get("tag")
                if tg and tg not in TAGS: add("effect scoped to a tag no ability carries", tg)
                for tg2 in e.get("addTags",[]) or []:
                    if tg2 not in TAGS: add("convert adds a tag no ability carries", tg2)

# 4. effects referencing abilities that do not exist
for t in D["trees"]:
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                i=e.get("scope",{}).get("ability")
                if i and i not in A: add("effect names unknown ability", i)

# 5. text still vanilla or broken
for t in D["trees"]:
    if t["kind"]=="vanilla": continue
    for r in t["rows"]:
        for x in r["talents"]:
            if re.search(r"\bYour this\b|\bthis this\b|\bby N%|\bN sec\b|\bby N \b", x["text"]):
                add("placeholder text", f"{t['name']}/{x['name']}")
            if not x["text"].strip(): add("empty text", f"{t['name']}/{x['name']}")

# 6. talents with no authored effect and not classified
for t in D["trees"]:
    if t["kind"]=="vanilla": continue
    for r in t["rows"]:
        for x in r["talents"]:
            if x.get("simulable") is False: continue
            if not any(e.get("source")=="authored" for e in x.get("effects",[])):
                add("no authored effect", f"{t['name']}/{x['name']}")

# 7. rotations missing a class, or classes missing a rotation
for t in D["trees"]:
    c=t.get("class") or t.get("host")
    if c and c not in D["rotations"]: add("class has no rotation", c)

# 8. cooldowns whose effect key nothing reads
for k,v in D.get("cooldowns",{}).items():
    for st in v.get("effect",{}):
        if not (f'"{st}"' in ALL or f"'{st}'" in ALL): add("cooldown effect unread", f"{k}/{st}")

if __name__=="__main__":
    total=sum(len(v) for v in findings.values())
    print(f"FULL AUDIT: {total} findings across {len(findings)} categories\n")
    for k in sorted(findings, key=lambda k:-len(findings[k])):
        v=sorted(set(findings[k]))
        print(f"  {k:30} {len(v)}")
        for i in v[:10]: print(f"      {i}")
    if not findings: print("  nothing outstanding")
