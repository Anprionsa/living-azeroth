#!/usr/bin/env python3
"""Reproduce rank-audit.md's numbers from data/talent-data.json.

Mirrors the calculator's v2RankList clause split and v2Join effect-to-rank
mapping from DocumentPage.dc.html so the authoring pass has a mechanical
acceptance check. Targets: 548 multi-rank, 397 clean, 151 mismatch,
coverage 609/1359, 357 unauthored rows.
"""
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, re, sys, collections

DATA = _ROOT + r"/data/talent-data.json"
if "--data" in sys.argv:
    DATA = sys.argv[sys.argv.index("--data") + 1]

def clauses(text):
    """v2RankList split: sentences, then ',? then ' chains."""
    t = re.sub(r"\s+", " ", str(text or "")).strip()
    parts = []
    for sent in re.findall(r"[^.!?]+[.!?]?", t):
        for c in re.split(r",?\s+then\s+", sent, flags=re.I):
            c = c.strip()
            if c:
                parts.append(c)
    return parts

def effect_words(fx):
    strong, weak = [], []
    if fx.get("stat"):
        strong += re.sub(r"([A-Z])", r" \1", str(fx["stat"])).lower().split()
    if fx.get("flag"):
        strong += str(fx["flag"]).split("_")
    sc = fx.get("scope") or {}
    if sc.get("ability"):
        strong += str(sc["ability"]).split("-")[1:]
    if sc.get("tag"):
        strong.append(sc["tag"])
    if fx.get("when"):
        w = re.sub(r"[^a-z<>=.]", " ", str(fx["when"]), flags=re.I).lower()
        weak += [x for x in re.split(r"[\s.]+", w)
                 if len(x) > 3 and not re.search(r"event|target|ability|health|self", x)]
    return ([w for w in strong if len(w) > 2], [w for w in weak if len(w) > 2])

def join_tags(talent, parts):
    """v2Join: effect index -> rank index (0-based) or None."""
    tags = []
    for fx in talent.get("effects", []):
        rank = fx.get("rank")
        if isinstance(rank, (int, float)) and 1 <= rank <= len(parts):
            tags.append(int(rank) - 1)
            continue
        sW, wW = effect_words(fx)
        if not sW and not wW:
            tags.append(None)
            continue
        scores = []
        for p in parts:
            pl = p.lower()
            scores.append(sum(3 for w in sW if w in pl) + sum(1 for w in wW if w in pl))
        best = max(scores)
        if best == 0 or scores.count(best) != 1:
            tags.append(None)
        else:
            tags.append(scores.index(best))
    return tags

def main():
    d = json.load(open(DATA, encoding="utf-8"))
    shown = [t for t in d["trees"] if t.get("kind") in ("rebuilt", "absorbed", "original")]
    multi = []
    for t in shown:
        for r in t.get("rows", []):
            for tal in r["talents"]:
                if tal.get("ranks", 1) >= 2:
                    multi.append((t, tal))
    mismatch, clean = [], []
    for t, tal in multi:
        parts = clauses(tal.get("text"))
        (clean if len(parts) == tal["ranks"] else mismatch).append((t, tal, parts))

    total_clauses = sum(tal["ranks"] for _, tal, _ in clean)
    covered = 0
    unauthored_rows = []
    subjectless = 0
    for t, tal, parts in clean:
        tags = join_tags(tal, parts)
        has = [i in tags for i in range(len(parts))]
        covered += sum(has)
        missing = [i + 1 for i, h in enumerate(has) if not h]
        if missing:
            unauthored_rows.append((t["id"], tal["name"], tal["ranks"],
                                    " ".join(map(str, missing))))

    drafted = sum(1 for t in d["trees"] for r in t.get("rows", [])
                  for tal in r["talents"] for e in tal.get("effects", [])
                  if e.get("source") == "drafted")

    print(f"shown trees: {len(shown)}")
    print(f"multi-rank talents: {len(multi)}  (target 548)")
    print(f"decompose cleanly: {len(clean)}  (target 397)")
    print(f"clause mismatch: {len(mismatch)}  (target 151)")
    print(f"rank clauses: {total_clauses}  (target 1359)")
    print(f"covered: {covered}  (target 609)")
    print(f"unauthored rows: {len(unauthored_rows)}  (target 357)")
    print(f"drafted effects: {drafted}  (target 321)")

    if "--dump" in sys.argv:
        out = {
            "mismatch": [
                {"tree": t["id"], "talent": tal["name"], "ranks": tal["ranks"],
                 "clauses": len(parts), "text": tal["text"], "id": tal["id"]}
                for t, tal, parts in mismatch
            ],
            "unauthored": [
                {"tree": a, "talent": b, "ranks": c, "missing": m}
                for a, b, c, m in unauthored_rows
            ],
        }
        json.dump(out, open(sys.argv[sys.argv.index("--dump") + 1], "w",
                            encoding="utf-8"), indent=1)
        print("dumped worklists")

if __name__ == "__main__":
    main()
