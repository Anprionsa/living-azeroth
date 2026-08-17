#!/usr/bin/env python3
"""Apply a talent patch file to a copy of talent-data.json, with safety gates.

Usage: apply_patch.py <patch.json> [<patch.json> ...] --out <merged.json>
       [--in <data.json>]

Gates enforced per patched talent:
- authored effects are frozen: same multiset before and after, ignoring an
  added integer `rank` key (sim.py reads only source:"authored"; rank is
  display-only)
- every effect uses the closed vocabulary (ops/stats from meta.effectVocabulary,
  flags from meta.effectVocabulary plus fx-norms)
- source is one of authored (pre-existing only), reviewed, drafted
- rank keys are integers in 1..ranks
- a replaced text is non-empty, ends in [.!?], has no em dash or exclamation
  point, and for multi-rank talents decomposes into exactly `ranks` clauses
  under the calculator's splitter
"""
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, re, sys, copy

IN = _ROOT + r"/data/talent-data.json"
NORMS = _ROOT + r"/data/fx-norms.json"
args = sys.argv[1:]
if "--in" in args:
    i = args.index("--in"); IN = args[i + 1]; del args[i:i + 2]
out = None
if "--out" in args:
    i = args.index("--out"); out = args[i + 1]; del args[i:i + 2]
ALLOW_AUTHORED = "--allow-authored" in args
if ALLOW_AUTHORED: args.remove("--allow-authored")
patch_paths = args

def clauses(text):
    t = re.sub(r"\s+", " ", str(text or "")).strip()
    parts = []
    for sent in re.findall(r"[^.!?]+[.!?]?", t):
        for c in re.split(r",?\s+then\s+", sent, flags=re.I):
            c = c.strip()
            if c:
                parts.append(c)
    return parts

def authored_key(e):
    k = {a: b for a, b in e.items() if a != "rank"}
    return json.dumps(k, sort_keys=True)

d = json.load(open(IN, encoding="utf-8"))
vocab = d["meta"]["effectVocabulary"]
norms = json.load(open(NORMS, encoding="utf-8"))
OPS = set(vocab["ops"])
# proc-type effects carry their proc name in the stat field throughout the
# authored data, so the gate accepts stats and procs alike
STATS = set(vocab["stats"]) | set(vocab.get("procs", []))
FLAGS = set(vocab.get("flags", [])) | set(norms.get("flags", []))

byid = {}
for t in d["trees"]:
    for r in t.get("rows", []):
        for tal in r["talents"]:
            byid[tal["id"]] = tal

errors, applied = [], 0
for pp in patch_paths:
    patch = json.load(open(pp, encoding="utf-8"))
    for tid, ch in patch.get("talents", {}).items():
        tal = byid.get(tid)
        if tal is None:
            errors.append(f"{pp}: unknown talent id {tid}")
            continue
        e = []
        if "effects" in ch:
            new_fx = ch["effects"]
            before = sorted(authored_key(x) for x in tal.get("effects", [])
                            if x.get("source") == "authored")
            after = sorted(authored_key(x) for x in new_fx
                           if x.get("source") == "authored")
            if before != after and not ALLOW_AUTHORED:
                e.append("authored effects changed (only adding `rank` to them is allowed)")
            for fx in new_fx:
                if fx.get("op") not in OPS:
                    e.append(f"op {fx.get('op')!r} not in vocabulary")
                if fx.get("stat") is not None and fx["stat"] not in STATS:
                    e.append(f"stat {fx.get('stat')!r} not in vocabulary")
                if fx.get("flag") is not None and fx["flag"] not in FLAGS:
                    e.append(f"flag {fx.get('flag')!r} not in vocabulary")
                if fx.get("source") not in ("authored", "reviewed", "drafted"):
                    e.append(f"source {fx.get('source')!r} invalid")
                rk = fx.get("rank")
                if rk is not None and not (isinstance(rk, int) and 1 <= rk <= tal["ranks"]):
                    e.append(f"rank {rk!r} outside 1..{tal['ranks']}")
                sc = fx.get("scope")
                if not (isinstance(sc, dict) and (("ability" in sc) or ("tag" in sc) or sc.get("all"))):
                    e.append(f"scope {sc!r} invalid")
        if "text" in ch:
            tx = str(ch["text"]).strip()
            if not tx or not re.search(r"[.!?]$", tx):
                e.append("text empty or missing terminal punctuation")
            if "\u2014" in tx or "!" in tx:
                e.append("text contains em dash or exclamation point")
            if tal["ranks"] >= 2 and len(clauses(tx)) != tal["ranks"]:
                e.append(f"text decomposes into {len(clauses(tx))} clauses, needs {tal['ranks']}")
        if "requires" in ch and ch["requires"] is not None:
            rq = ch["requires"]
            tree_of = {}
            for t in d["trees"]:
                for r in t.get("rows", []):
                    for x in r["talents"]:
                        tree_of[x["id"]] = (t["id"], r["row"], x)
            if not (isinstance(rq, dict) and isinstance(rq.get("talent"), str)):
                e.append("requires must be {talent, ranks}")
            else:
                tgt = tree_of.get(rq["talent"]); me = tree_of.get(tid)
                if not tgt: e.append(f"requires unknown talent {rq['talent']}")
                elif tgt[0] != me[0]: e.append("requires a talent in another tree")
                elif tgt[1] > me[1]: e.append("requires a talent in a later row")
                elif rq["talent"] == tid: e.append("requires itself")
                else:
                    rk = rq.get("ranks", tgt[2]["ranks"])
                    if not (isinstance(rk, int) and 1 <= rk <= tgt[2]["ranks"]): e.append(f"requires ranks {rk!r} outside 1..{tgt[2]['ranks']}")
        if e:
            errors.append(f"{tid}: " + "; ".join(e))
            continue
        if "col" in ch:
            c = ch["col"]
            if c is None: tal.pop("col", None)
            elif isinstance(c, int) and 0 <= c <= 3: tal["col"] = c
            else: errors.append(f"{tid}: col {c!r} outside 0..3")
        if "requires" in ch:
            if ch["requires"] is None: tal.pop("requires", None)
            else: tal["requires"] = {"talent": ch["requires"]["talent"], "ranks": ch["requires"].get("ranks", tree_of[ch["requires"]["talent"]][2]["ranks"])}
        if "text" in ch:
            tal["text"] = str(ch["text"]).strip()
        if "effects" in ch:
            tal["effects"] = ch["effects"]
        applied += 1

print(f"applied {applied} talent patches, {len(errors)} rejected")
for x in errors:
    print("  REJECT", x)
if out:
    json.dump(d, open(out, "w", encoding="utf-8"))
    print("wrote", out)
sys.exit(1 if errors else 0)
