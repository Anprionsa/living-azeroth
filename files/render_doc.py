#!/usr/bin/env python3
"""Regenerate every GENERATED tree-row block in a design document from talent-data.json.

Blocks are matched to trees by the talent names they contain, not by heading, so the
document can be restructured freely without breaking regeneration.
"""
import json, re, sys
DATA="/mnt/user-data/outputs/talent-data.json"
D=json.load(open(DATA)); BY={t["id"]:t for t in D["trees"]}

def rows_of(t, config):
    for r in sorted(t["rows"], key=lambda r:r["gate"]):
        tal=[x for x in r["talents"] if x.get("availableIn") is None or config in x["availableIn"]]
        if tal: yield r, tal, sum(x["ranks"] for x in tal)

def full(tid, config="core"):
    out=[]
    for r,tal,pts in rows_of(BY[tid],config):
        seat=". The hybrid seat, reachable at 21 points invested" if r["gate"]==20 else ""
        out += [f"**Gate {r['gate']}, {pts} points{seat}**",""]
        for x in tal: out.append(f"- *{x['name']}* ({x['ranks']}).{tags(x)} {x['text']}")
        out.append("")
    return "\n".join(out).rstrip()

def compact(tid, config="core"):
    out=[]
    for r,tal,pts in rows_of(BY[tid],config):
        seat=", hybrid seat" if r["gate"]==20 else ""
        body=" ".join(f"*{x['name']}* ({x['ranks']}).{tags(x)} {x['text']}" for x in tal)
        out.append(f"- **Gate {r['gate']}, {pts}{seat}.** {body}")
    return "\n".join(out)

def tags(x):
    t=[]
    if "subtraction" in x["flags"]: t.append("subtraction node")
    if "reciprocal" in x["flags"]: t.append("reciprocal")
    elif x["crossTree"] and x["crossTree"].get("target"): t.append("cross-tree")
    if "mark" in x["flags"]: t.append("the mark")
    return f" *({', '.join(t)})*" if t else ""

def identify(block):
    """Which tree does this block belong to? Match on talent names present."""
    names=set(re.findall(r"\*([A-Z][^*\n]{2,42}?)\*\s*\(\d+\)", block))
    best=None; score=0
    for t in D["trees"]:
        if "core" not in t.get("configurations",[]): continue
        tn={x["name"] for r in t["rows"] for x in r["talents"]}
        s=len(names & tn)
        if s>score: score, best = s, t["id"]
    return best if score>=3 else None

if __name__=="__main__":
    p="/mnt/user-data/outputs/classic-plus-talent-design.md"
    T=open(p,encoding="utf-8").read()
    PAT=re.compile(r"<!-- GENERATED:[^>]*-->\s*(.*?)\s*<!-- END GENERATED -->", re.S)
    done=[]; miss=[]
    def rep(m):
        blk=m.group(1); tid=identify(blk)
        if not tid: miss.append(blk[:60]); return m.group(0)
        style = compact if blk.lstrip().startswith("- **Gate") else full
        done.append(tid)
        return ("<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->\n\n"
                + style(tid) + "\n\n<!-- END GENERATED -->")
    T2=PAT.sub(rep,T)
    open(p,"w",encoding="utf-8").write(T2)
    print(f"blocks regenerated: {len(done)} | unidentified: {len(miss)}")
    if miss: print("  ", miss)
    print(f"distinct trees covered: {len(set(done))}")
