#!/usr/bin/env python3
"""Render a tree's rows from talent-data.json. The document should quote this, not restate it."""
import json, sys
D=json.load(open("/mnt/user-data/outputs/talent-data.json"))
def render(tid, config="core"):
    t=next(x for x in D["trees"] if x["id"]==tid)
    out=[f"**{t['name']}** ({t['availablePoints']} points)"]
    for r in sorted(t["rows"], key=lambda r:r["gate"]):
        tal=[x for x in r["talents"] if x.get("availableIn") is None or config in x["availableIn"]]
        if not tal: continue
        pts=sum(x["ranks"] for x in tal)
        out.append(f"\n**Gate {r['gate']}, {pts} points**\n")
        for x in tal:
            tags=[]
            if "subtraction" in x["flags"]: tags.append("subtraction")
            if "reciprocal" in x["flags"]: tags.append("reciprocal")
            if x["crossTree"] and x["crossTree"]["target"]: tags.append("cross-tree")
            suffix=f"  *[{', '.join(tags)}]*" if tags else ""
            out.append(f"- *{x['name']}* ({x['ranks']}). {x['text']}{suffix}")
    return "\n".join(out)
if __name__=="__main__":
    print(render(sys.argv[1] if len(sys.argv)>1 else "warrior-arms-rebuilt"))
