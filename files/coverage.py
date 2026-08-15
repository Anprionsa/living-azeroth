#!/usr/bin/env python3
"""Which authored effects does anything actually read?

Every bug this project has found in the last several passes has the same shape: an
effect exists in the data and no consumer looks at it. This enumerates every op and
stat combination in use and reports whether sim, tank or heal reads it.
"""
import json, re
from collections import Counter
D=json.load(open("/mnt/user-data/outputs/talent-data.json"))
SRC={n:open(f"/home/claude/{n}.py").read() for n in ("sim","tank","heal")}

def reads(op, stat):
    """A consumer reads a combination if its source mentions both the op and the stat."""
    hits=[]
    for n,s in SRC.items():
        opq = f'"{op}"' in s or f"'{op}'" in s
        stq = stat is None or f'"{stat}"' in s or f"'{stat}'" in s
        if opq and stq: hits.append(n)
    return hits

if __name__=="__main__":
    combos=Counter()
    for t in D["trees"]:
        for r in t["rows"]:
            for x in r["talents"]:
                for e in x.get("effects",[]):
                    if e.get("source")!="authored": continue
                    combos[(e["op"], e.get("stat") or e.get("flag"))]+=1
    unread=[]; partial=[]
    print(f"{'op':10} {'stat/flag':22} {'count':>6}  read by")
    for (op,stat),c in sorted(combos.items(), key=lambda kv:-kv[1]):
        h=reads(op,stat)
        mark = ",".join(h) if h else "NOTHING"
        if not h: unread.append((op,stat,c))
        print(f"  {op:10} {str(stat):22} {c:5}  {mark}")
    print()
    print(f"combinations in use: {len(combos)} | total effects: {sum(combos.values())}")
    print(f"read by nothing: {len(unread)} combinations, {sum(c for _,_,c in unread)} effects")
    for op,stat,c in sorted(unread, key=lambda z:-z[2]):
        print(f"    {op} / {stat}   x{c}")
