#!/usr/bin/env python3
"""Compute a flat ledger for a build.

Usage:
    python3 ledger.py Warrior "Arms:Improved Heroic Strike=3,Tactical Mastery=5,..." 

Or import build_ledger(cls, {tree: {talent: rank}}).
Validates gates: a talent is only legal if points already in that tree >= reqPoints.
"""
import json, sys

D = json.load(open("talents-classified.json"))["classes"]

def build_ledger(cls, alloc):
    trees = D[cls]
    out = {"class": cls, "trees": {}, "totalSpent": 0,
           "flatPoints": 0, "behaviorPoints": 0, "illegal": []}
    for tree, picks in alloc.items():
        spent = sum(picks.values())
        entries = []
        for name, rank in picks.items():
            t = trees[tree][name]
            if rank > t["maxRank"]:
                out["illegal"].append(f"{tree}/{name}: rank {rank} > max {t['maxRank']}")
            if spent < t["reqPoints"] + rank:
                out["illegal"].append(
                    f"{tree}/{name}: needs {t['reqPoints']} invested, build has {spent} in tree")
            entries.append({"talent": name, "ranks": rank, "buys": t["buys"],
                            "gate": t["reqPoints"], "effect": t["description"][:110]})
            out["flatPoints" if t["buys"]=="flat" else "behaviorPoints"] += rank
        out["trees"][tree] = {"spent": spent, "entries": entries}
        out["totalSpent"] += spent
    out["freedPoints"] = out["flatPoints"]
    out["dividendTarget"] = ("sum the effect column of every flat entry; that is what the depth "
                             "curve must reproduce at this build's point investment")
    return out

if __name__ == "__main__":
    # demo: the verified 17 point Arms portion of the canonical Fury build
    demo = {"Arms": {"Improved Heroic Strike": 3, "Improved Rend": 3, "Tactical Mastery": 5,
                     "Deep Wounds": 3, "Impale": 2, "Anger Management": 1}}
    r = build_ledger("Warrior", demo)
    print(json.dumps({k: v for k, v in r.items() if k != "trees"}, indent=2))
    for e in r["trees"]["Arms"]["entries"]:
        print(f"  {e['buys']:9} {e['ranks']}x {e['talent']:28} gate {e['gate']:2}")
