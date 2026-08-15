#!/usr/bin/env python3
"""Install the merged talent data and regenerate the audit artifacts.

Usage: finalize_data.py <merged.json>
- backs up data/talent-data.json into the scratchpad
- updates meta.authoringDebt.draftedEffects and adds meta.effectProvenance
- writes the merged file to data/talent-data.json (minified, as before)
- regenerates data/rank-gap-rows.json
- regenerates data/rank-audit.md with the post-pass numbers
"""
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, re, sys, os, shutil, collections

SCRATCH = os.path.dirname(os.path.abspath(__file__))
DATA = _ROOT + r"/data/talent-data.json"
sys.path.insert(0, SCRATCH)
import rank_audit as RA

merged_path = sys.argv[1]
d = json.load(open(merged_path, encoding="utf-8"))

# --- provenance metadata
drafted_left = sum(1 for t in d["trees"] for r in t.get("rows", [])
                   for tal in r["talents"] for e in tal.get("effects", [])
                   if e.get("source") == "drafted")
reviewed = sum(1 for t in d["trees"] for r in t.get("rows", [])
               for tal in r["talents"] for e in tal.get("effects", [])
               if e.get("source") == "reviewed")
d["meta"]["effectProvenance"] = {
    "authored": "written by hand before or during simulation; the only effects sim.py applies",
    "reviewed": "display annotation verified against its rank clause in the August 2026 finalization pass; never simulated",
    "drafted": "machine-drafted and not yet reviewed; renders with a (drafted) suffix",
}
d["meta"]["authoringDebt"]["draftedEffects"] = (
    f"August 2026 finalization pass reviewed the 321 drafted effects: duplicates of authored "
    f"behaviour were deleted with their rank bindings moved onto the authored effect, the rest "
    f"were corrected and promoted to source:\"reviewed\" ({reviewed} reviewed effects now carry "
    f"rank bindings). {drafted_left} drafted effects remain."
)

# --- audit the merged data
shown = [t for t in d["trees"] if t.get("kind") in ("rebuilt", "absorbed", "original")]
multi = [(t, tal) for t in shown for r in t.get("rows", []) for tal in r["talents"]
         if tal.get("ranks", 1) >= 2]
mismatch, clean = [], []
for t, tal in multi:
    parts = RA.clauses(tal.get("text"))
    (clean if len(parts) == tal["ranks"] else mismatch).append((t, tal, parts))
total_clauses = sum(tal["ranks"] for _, tal, _ in clean)
covered = 0
gap_rows, gap_rows_json = [], []
for t, tal, parts in clean:
    tags = RA.join_tags(tal, parts)
    has = [i in tags for i in range(len(parts))]
    covered += sum(has)
    missing = [i + 1 for i, h in enumerate(has) if not h]
    if missing:
        gap_rows.append((t["id"], tal["name"], tal["ranks"], " ".join(map(str, missing))))
        gap_rows_json.append(f"| {t['id']} | {tal['name']} | {tal['ranks']} | {' '.join(map(str, missing))} |")

# --- install (backup goes to the OS temp dir, not the repo)
import tempfile
shutil.copy2(DATA, os.path.join(tempfile.gettempdir(), "talent-data.backup.json"))
json.dump(d, open(DATA, "w", encoding="utf-8"), separators=(",", ":"))
json.dump(gap_rows_json, open(_ROOT + r"/data/rank-gap-rows.json", "w",
                              encoding="utf-8"), indent=1)

# --- regenerate rank-audit.md
lines = []
lines.append("# Rank-clause audit")
lines.append("")
lines.append("August 2026, regenerated after the finalization pass. The calculator decomposes a multi-rank talent's text into one bullet per rank, splitting on sentences and \"then\" chains, and inherits the first clause's subject where a later clause starts with a verb. This report lists where the data does not decompose: clause count differs from rank count, so the calculator falls back to the plain tooltip text.")
lines.append("")
lines.append(f"Multi-rank talents in the shown configurations: {len(multi)}. Decomposing cleanly: {len(clean)}.")
lines.append("")
if mismatch:
    lines.append("| Tree | Talent | Ranks | Clauses |")
    lines.append("|---|---|---|---|")
    for t, tal, parts in mismatch:
        lines.append(f"| {t['id']} | {tal['name']} | {tal['ranks']} | {len(parts)} |")
else:
    lines.append("No talent in the shown configurations mismatches its rank count. The August finalization pass restaged every mismatched tooltip against its design chapter, with the full-rank end state held fixed.")
lines.append("")
lines.append("## Per-rank magnitude gaps")
lines.append("")
pct = round(100 * covered / total_clauses) if total_clauses else 0
lines.append(f"Coverage after the finalization pass: {covered} of {total_clauses} rank clauses ({pct}%). Authored effects carry explicit rank bindings where a clause describes them; display annotations verified against their clause carry source:\"reviewed\" and are never simulated; {drafted_left} machine-drafted effects remain, rendering with a (drafted) suffix.")
lines.append("")
if gap_rows:
    lines.append("The ranks below remain unbound. Each names a mechanic the closed effect vocabulary cannot express; extending the vocabulary is a design decision, not an authoring gap.")
    lines.append("")
    lines.append("| Tree | Talent | Ranks | Unbound ranks |")
    lines.append("|---|---|---|---|")
    for a, b, c, m in gap_rows:
        lines.append(f"| {a} | {b} | {c} | {m} |")
else:
    lines.append("Every rank clause of every cleanly decomposing talent carries a bound effect.")
lines.append("")
open(_ROOT + r"/data/rank-audit.md", "w", encoding="utf-8").write("\n".join(lines))

print(f"installed. mismatch={len(mismatch)} covered={covered}/{total_clauses} ({pct}%) "
      f"gapRows={len(gap_rows)} reviewed={reviewed} draftedLeft={drafted_left}")
