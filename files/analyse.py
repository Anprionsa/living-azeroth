#!/usr/bin/env python3
"""Queries that used to be hand-built maps. All read talent-data.json."""
import json
from collections import defaultdict
D=json.load(open("/mnt/user-data/outputs/talent-data.json"))
idx={t["id"]:t for t in D["trees"]}

def cross_edges():
    e=[]
    for t in D["trees"]:
        for r in t["rows"]:
            for x in r["talents"]:
                ct=x.get("crossTree")
                if ct and ct.get("target"): e.append((t["id"],x["name"],ct["target"]))
    return e

def mutual_pairs():
    out=defaultdict(set)
    for a,_,b in cross_edges(): out[a].add(b)
    return sorted({tuple(sorted([a,b])) for a in out for b in out[a] if a in out.get(b,())})

def one_way():
    out=defaultdict(set)
    for a,_,b in cross_edges(): out[a].add(b)
    return [(a,b) for a in out for b in out[a] if a not in out.get(b,())]

if __name__=="__main__":
    e=cross_edges(); m=mutual_pairs(); o=one_way()
    print(f"cross-tree edges: {len(e)} | mutual pairs: {len(m)} | one-way: {len(o)}\n")
    print("MUTUAL PAIRS, these are the predicted named builds:")
    for a,b in m: print(f"  {idx[a]['name']:26} <-> {idx[b]['name']}")
    print("\nONE-WAY, a tree reaches toward one that does not reach back:")
    byclass=defaultdict(list)
    for a,b in o: byclass[idx[a]['class']].append(f"{idx[a]['name']} -> {idx[b]['name']}")
    for c in sorted(byclass):
        print(f"  {c}: " + "; ".join(byclass[c]))
    print("\nCLASSES WITH NO MUTUAL PAIR:")
    have={idx[a]['class'] for a,b in m}
    print("  " + (", ".join(sorted({t['class'] for t in D['trees']}-have)) or "none"))
