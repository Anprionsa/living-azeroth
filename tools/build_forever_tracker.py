"""Assemble data/forever-tracker.json from an export of the Forever tracker's store.

The live tracker is a hosted working copy with a shared database; that store is
canonical. This script turns a per-document export of it (one JSON file per
document, in <export>/<collection>/<id>.json) into the single snapshot the
site's forever.html reads.

    python tools/build_forever_tracker.py <export-dir> [--date YYYY-MM-DD]
"""
import argparse
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "forever-tracker.json")
COLLECTIONS = ("issues", "goals", "team", "premise")


def load(dirpath):
    docs = []
    if not os.path.isdir(dirpath):
        return docs
    for name in sorted(os.listdir(dirpath)):
        if name.endswith(".json"):
            with open(os.path.join(dirpath, name), encoding="utf-8") as f:
                docs.append({"id": name[:-5], **json.load(f)})
    return docs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()

    snap = {c: load(os.path.join(a.export, c)) for c in COLLECTIONS}
    meta = {m["id"]: m for m in load(os.path.join(a.export, "meta"))}
    about = meta.get("about", {})
    team_meta = meta.get("team", {})

    for c in ("goals", "premise"):
        snap[c].sort(key=lambda d: d.get("order", 99))
    snap["team"].sort(key=lambda d: d.get("order", 99))

    ids = {i["id"] for i in snap["issues"]}
    refs = ({l["id"] for p in snap["team"] for l in p.get("likelyIssues", [])} |
            {r for g in snap["goals"] for r in g.get("relatedIssueIds", [])} |
            {u["id"] for u in team_meta.get("unowned", [])})
    missing = sorted(refs - ids)
    if missing:
        sys.exit(f"references to unknown issues: {', '.join(missing)}")

    snap["source"] = {"title": about.get("sourceTitle", ""), "seededOn": about.get("seededOn", "")}
    snap["gaps"] = team_meta.get("gaps", [])
    snap["unowned"] = team_meta.get("unowned", [])
    snap["exported"] = a.date

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"{OUT}: {len(snap['issues'])} issues, {len(snap['goals'])} goals, "
          f"{len(snap['team'])} people, {len(snap['premise'])} premise quotes")


if __name__ == "__main__":
    main()
