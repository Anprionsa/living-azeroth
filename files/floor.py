"""Minimum flat spend forced by tree structure.

You do not need to know a build to measure forced filler. To reach a talent at
gate G you must spend G points in that tree first. How many of those points can
possibly buy behavior is fixed by the tree. The remainder is filler you have no
choice about.
"""
import json
D = json.load(open("talents-classified.json"))["classes"]

def flat_floor(talents, target):
    """Greedily reach `target` points preferring behavior. Returns (flat, behavior)."""
    taken = {n: 0 for n in talents}
    flat = beh = 0
    while flat + beh < target:
        avail = []
        for n, t in talents.items():
            if taken[n] >= t["maxRank"]: continue
            if t["reqPoints"] > flat + beh: continue
            pre = t.get("prereq")
            if pre and pre in talents and taken[pre] < talents[pre]["maxRank"]: continue
            avail.append((t["buys"], n))
        if not avail: return None, None            # tree cannot reach target
        pick = next((n for b, n in avail if b == "behavior"), None)
        if pick: taken[pick] += 1; beh += 1
        else:    taken[avail[0][1]] += 1; flat += 1
    return flat, beh

print(f"{'class':9} {'tree':15} {'to reach capstone (30 pts)':>28}")
print(f"{'':9} {'':15} {'forced flat':>12} {'best case behavior':>19}")
rows = []
for cls, trees in D.items():
    for tree, talents in trees.items():
        f, b = flat_floor(talents, 30)
        rows.append((cls, tree, f, b))
rows.sort(key=lambda r: -(r[2] if r[2] is not None else -1))
for cls, tree, f, b in rows:
    if f is None: print(f"{cls:9} {tree:15} {'unreachable':>12}"); continue
    print(f"{cls:9} {tree:15} {f:8} /30 {b:15} /30")
