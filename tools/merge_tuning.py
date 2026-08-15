#!/usr/bin/env python3
"""Merge a tuned talent-data.json (from a staging copy) into the canonical data.

Usage: merge_tuning.py <tuned.json> --trees blackguard,necromancy,... [--apply]

Tuning legitimately changes authored effects (magnitudes, new levers) and may
change tooltip text on the tuned trees, so this bypasses apply_patch's
frozen-authored gate. It is guarded instead by scope: only talents inside the
named trees may differ; any difference outside them is reported and refused.
meta differences are listed; only keys named with --meta are carried over.
Without --apply it is a dry run.
"""
import os as _os, sys, json
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
CANON = _ROOT + "/data/talent-data.json"

args = sys.argv[1:]
tuned_path = args[0]
trees = set()
meta_keys = set()
apply = "--apply" in args
if "--trees" in args:
    trees = set(args[args.index("--trees") + 1].split(","))
if "--meta" in args:
    meta_keys = set(args[args.index("--meta") + 1].split(","))

canon = json.load(open(CANON, encoding="utf-8"))
tuned = json.load(open(tuned_path, encoding="utf-8"))

def talents(d):
    out = {}
    for t in d["trees"]:
        for r in t.get("rows", []):
            for tal in r["talents"]:
                out[tal["id"]] = (t["id"], tal)
    return out

C, T = talents(canon), talents(tuned)
in_scope, out_of_scope, text_changed = [], [], []
for tid, (tree, ttal) in T.items():
    ctree, ctal = C.get(tid, (None, None))
    if ctal is None:
        out_of_scope.append(f"{tid} (new talent, tree {tree})")
        continue
    if json.dumps(ctal, sort_keys=True) == json.dumps(ttal, sort_keys=True):
        continue
    if tree in trees:
        in_scope.append(tid)
        if ctal.get("text") != ttal.get("text"):
            text_changed.append(tid)
    else:
        out_of_scope.append(f"{tid} (tree {tree})")
for tid in C:
    if tid not in T:
        out_of_scope.append(f"{tid} (removed in tuned)")

# tree-level fields (dividend, mechanic, lore, status) inside scope
tree_level = []
ct = {t["id"]: t for t in canon["trees"]}
for t in tuned["trees"]:
    c = ct.get(t["id"])
    if not c:
        out_of_scope.append(f"tree {t['id']} new"); continue
    a = {k: v for k, v in c.items() if k != "rows"}
    b = {k: v for k, v in t.items() if k != "rows"}
    if a != b:
        (tree_level if t["id"] in trees else out_of_scope).append(t["id"] + " (tree-level fields)")

meta_diff = [k for k in set(canon["meta"]) | set(tuned["meta"])
             if json.dumps(canon["meta"].get(k), sort_keys=True) != json.dumps(tuned["meta"].get(k), sort_keys=True)]
top_diff = [k for k in set(canon) | set(tuned) if k not in ("trees", "meta")
            and json.dumps(canon.get(k), sort_keys=True) != json.dumps(tuned.get(k), sort_keys=True)]

print(f"in-scope talent changes: {len(in_scope)}  (text changed on {len(text_changed)})")
for x in in_scope: print("   ", x, "(text)" if x in text_changed else "")
print(f"tree-level changes in scope: {tree_level}")
print(f"OUT-OF-SCOPE differences: {len(out_of_scope)}")
for x in out_of_scope[:40]: print("   !!", x)
print(f"meta keys differing: {sorted(meta_diff)}  (carrying: {sorted(meta_keys & set(meta_diff))})")
print(f"other top-level keys differing: {sorted(top_diff)}  (NOT carried; abilities/rotations/gear changes need review)")

if out_of_scope:
    print("REFUSED: out-of-scope differences present"); sys.exit(2)
if not apply:
    print("dry run; pass --apply to write"); sys.exit(0)

# apply: replace in-scope talents and tree-level fields, carry named meta keys
tuned_talents = T
for t in canon["trees"]:
    if t["id"] in trees:
        src = next(x for x in tuned["trees"] if x["id"] == t["id"])
        for k, v in src.items():
            if k != "rows":
                t[k] = v
        for r in t.get("rows", []):
            for i, tal in enumerate(r["talents"]):
                if tal["id"] in tuned_talents:
                    r["talents"][i] = tuned_talents[tal["id"]][1]
for k in meta_keys & set(meta_diff):
    canon["meta"][k] = tuned["meta"][k]
json.dump(canon, open(CANON, "w", encoding="utf-8"), separators=(",", ":"))
print("applied to", CANON)
