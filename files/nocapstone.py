#!/usr/bin/env python3
"""What can a build do without a capstone?

51 points, no tree above 30, so no capstone is reachable. Enumerates two and three tree
splits and measures each against the class's best capstone build.
"""
import json, importlib, statistics, sys, itertools
sys.path.insert(0,"/home/claude")
import sim
D=sim.D
SCN=["patchwerk","burst","cleave"]

def trees_for(cls):
    return [t["id"] for t in D["trees"] if t.get("class")==cls and "core" in t.get("configurations",[])]

def splits(n=51, cap=30, step=5):
    """The shapes worth testing rather than every arithmetic possibility.

    A one point difference in a split almost never changes which talents are taken, so
    stepping by five covers the real design space at a fraction of the cost. Gate
    boundaries are included exactly because they are where builds actually change.
    """
    out=set()
    marks=sorted({cap, 26, 25, 21, 20, 16, 15, 11, 10, 6, 5} | set(range(5, cap+1, step)))
    for a in marks:
        if a>cap: continue
        b=n-a
        if 0 < b <= cap: out.add((a,b))
        for b2 in marks:
            if b2>min(cap,b) or b2>a: continue
            c=n-a-b2
            if 0 < c <= b2 <= cap: out.add((a,b2,c))
    return sorted(out, reverse=True)

def run(cls, assign, n=30, scn="patchwerk"):
    return statistics.mean([sim.run(cls, assign, seed=s, scenario=scn)[0] for s in range(1,n+1)])

def best_capstone(cls, n=30, scn="patchwerk"):
    ts=trees_for(cls); best=None
    for a in ts:
        for b in ts:
            if a==b: continue
            v=statistics.mean([sim.run(cls,[(a,31),(b,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
            if best is None or v>best[0]: best=(v,f"{a.split('-',1)[1].replace('-rebuilt','')} 31 / {b.split('-',1)[1].replace('-rebuilt','')} 20")
    return best

def sweep(cls, top=14, n=25):
    ts=trees_for(cls)
    ref,refname=best_capstone(cls,n=n)
    rows=[]
    seen=set()
    for sp in splits():
        for combo in itertools.permutations(ts, len(sp)):
            key=tuple(sorted(zip(combo,sp)))
            if key in seen: continue
            seen.add(key)
            assign=list(zip(combo,sp))
            v=run(cls,assign,n=n)
            rows.append((100*(v-ref)/ref, assign, v))
    rows.sort(key=lambda r:-r[0])
    return rows, ref, refname
