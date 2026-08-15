#!/usr/bin/env python3
"""Regenerate the GENERATED row blocks in classic-plus-class-absorption.md.

Same contract as render_doc.py: blocks are matched to trees by the talent names
they contain, so the document can be restructured without breaking regeneration.
"""
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, re
P=_ROOT + "/data/talent-data.json"
D=json.load(open(P))
EXP=[t for t in D["trees"] if t["kind"] in ("absorbed","original")]

def block(tid, config="expanded", style="pts"):
    t=next(x for x in D["trees"] if x["id"]==tid); t=dict(t); t["_rowStyle"]=style; out=[]
    for r in sorted(t["rows"], key=lambda r:r["gate"]):
        tal=[x for x in r["talents"] if x.get("availableIn") is None or config in x["availableIn"]]
        if not tal: continue
        pts=sum(x.get("ranks",1) for x in tal)
        style=t.get("_rowStyle","pts")
        if style=="gate": out.append(f"**Row {r['row']}, gate {r['gate']}, {pts} points**"); out.append("")
        else: out.append(f"**Row {r['row']} ({r['gate']} pts, {pts} available)**")
        for x in tal:
            tags=[]
            if "subtraction" in x.get("flags",[]): tags.append("subtraction")
            if "reciprocal" in x.get("flags",[]): tags.append("reciprocal")
            elif x.get("crossTree") and x["crossTree"].get("target"): tags.append("cross-tree")
            if "mark" in x.get("flags",[]): tags.append("the mark")
            suf=f" *({', '.join(tags)})*" if tags else ""
            out.append(f"- *{x['name']}* ({x.get('ranks',1)}):{suf} {x['text']}")
        out.append("")
    return "\n".join(out).rstrip()

def identify(blk):
    names=set(re.findall(r"\*([A-Z][^*\n]{2,42}?)\*\s*\(\d+\)", blk))
    best=None; score=0
    for t in EXP:
        tn={x["name"] for r in t["rows"] for x in r["talents"]}
        s=len(names & tn)
        if s>score: score,best=s,t["id"]
    return best if score>=2 else None

if __name__=="__main__":
    p=_ROOT + "/files/classic-plus-class-absorption.md"
    T=open(p,encoding="utf-8").read()
    PAT=re.compile(r"<!-- GENERATED:[^>]*-->\s*(.*?)\s*<!-- END GENERATED -->", re.S)
    done=[]; miss=[]
    def rep(m):
        tid=identify(m.group(1))
        if not tid: miss.append(m.group(1)[:50]); return m.group(0)
        done.append(tid)
        style="gate" if "gate" in m.group(1)[:80] else "pts"
        return ("<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->\n\n"
                + block(tid, style=style) + "\n\n<!-- END GENERATED -->")
    open(p,"w",encoding="utf-8").write(PAT.sub(rep,T))
    print(f"blocks regenerated: {len(done)} | unidentified: {len(miss)} | distinct trees: {len(set(done))}")
    if miss: print("  ", miss)
