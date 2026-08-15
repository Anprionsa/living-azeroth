#!/usr/bin/env python3
"""Convert percentage-authored talents into the behaviour their own text describes.

Not a redesign. In nearly every case the talent's text already names a behaviour and
only the effect was written as `multiply damage`. This reads the text and proposes the
op it names, per meta.behaviourStandard.
"""
import json, re
P="/mnt/user-data/outputs/talent-data.json"
D=json.load(open(P))
STD=D["meta"]["behaviourStandard"]

CUES=[
 (r"\bsubstantially more damage\b|\bgreatly increased\b", lambda m,sc: {"op":"debuff","stat":"vulnerability","scope":sc,"magnitude":0.10,"stacks":3}),
 (r"\bignore[sd]? armou?r\b|\bignores? a portion of the target'?s? armou?r\b", lambda m,sc: {"op":"ignore","stat":"armor","scope":sc,"magnitude":0.10}),
 (r"\bcannot be (dodged|parried|avoided|missed)\b", lambda m,sc: {"op":"enable","flag":"immune_dodged","scope":sc,"magnitude":1.0}),
 (r"\bscales? with\b|\bbenefits? from\b|\bgains? your\b|\binherits? your\b", lambda m,sc: {"op":"debuff","stat":"vulnerability","scope":sc,"magnitude":0.07,"stacks":2}),
 (r"\bmay be (cast|used) while\b|\bwithout stopping\b|\bwhile moving\b", lambda m,sc: {"op":"enable","flag":"use_moving","scope":sc,"magnitude":1.0}),
 (r"\bcosts? (no|less)\b|\brefunds?\b", lambda m,sc: {"op":"multiply","stat":"cost","scope":sc,"magnitude":0.85}),
 (r"\bcooldown drops?\b|\bno cooldown\b|\bcooldown .* reduced\b", lambda m,sc: {"op":"multiply","stat":"cooldown","scope":sc,"magnitude":0.80}),
 (r"\binstant\b|\bloses its cast time\b", lambda m,sc: {"op":"multiply","stat":"castTime","scope":sc,"magnitude":(0.0 if sc.get("ability") else 0.85)}),
 (r"cannot be (dispelled|resisted|interrupted|reflected)", lambda m,sc: {"op":"enable","flag":"immune_"+m.group(1),"scope":sc,"magnitude":1.0}),
 (r"\bdoes not expire\b|\bno longer expires\b|\bpersists?\b", lambda m,sc: {"op":"enable","flag":"no_expiry","scope":sc,"magnitude":1.0}),
 (r"\bhits? a second\b|\bstrikes? a second\b|\bspreads?\b|\bchains?\b|\breaches? .* party\b|\bapplies to your (party|raid)\b",
   lambda m,sc: {"op":"addTarget","scope":sc,"magnitude":1.0}),
 (r"\bcounts? as\b|\bbecomes? a\b", lambda m,sc: {"op":"convert","scope":sc,"magnitude":None}),
 (r"\bconsumes?\b .*\bfor (damage|burst)\b|\bspends? .* stacks?\b", lambda m,sc: {"op":"consume","stat":"stack","scope":sc,"magnitude":0.20}),
 (r"\bvulnerab\w+|\bstacking .* (mark|debuff)\b|\bstacks?\b(?!.*energy)", lambda m,sc: {"op":"debuff","stat":"vulnerability","scope":sc,"magnitude":0.06,"stacks":3}),
 (r"\brefreshes?\b|\bextends?\b|\bresets?\b", lambda m,sc: {"op":"refresh","stat":"duration","scope":sc,"magnitude":None}),
 (r"\bchance to\b", lambda m,sc: {"op":"proc","stat":"damage","scope":sc,"magnitude":0.25}),
 (r"\bignores?\b .*armou?r", lambda m,sc: {"op":"ignore","stat":"armor","scope":sc,"magnitude":0.08}),
 (r"\beach empowers? the other\b|\balternating\b", lambda m,sc: {"op":"alternate","stat":"damage","scope":{"all":True},"magnitude":0.15}),
]

def convert(x, tree):
    """Replace percentage damage effects with the behaviour the text names."""
    pct=[e for e in x.get("effects",[]) if e.get("source")=="authored"
         and e["op"]=="multiply" and e.get("stat") in ("damage","healing","effect")]
    if not pct: return None
    # a talent whose own text states a percentage keeps it
    if re.search(r"\bby \d+%|\bby N%|\b\d+/\d+/\d+%|\bdouble", x["text"]): return None
    keep=[e for e in x["effects"] if e not in pct]
    scopes=[e.get("scope",{}) for e in pct]
    sc=scopes[0] if scopes else {"all":True}
    new=[]
    for pat,fn in CUES:
        m=re.search(pat, x["text"], re.I)
        if not m: continue
        e=fn(m,sc); e["source"]="authored"
        if not any(z["op"]==e["op"] and z.get("stat")==e.get("stat") for z in keep+new): new.append(e)
        if len(new)>=2: break
    if not new: return None
    return keep+new

if __name__=="__main__":
    import sys
    changed=0; skipped=0
    for t in D["trees"]:
        if t["kind"]=="vanilla": continue
        for r in t["rows"]:
            for x in r["talents"]:
                out=convert(x,t)
                if out is None: skipped+=1; continue
                x["effects"]=out; changed+=1
    if "--apply" in sys.argv:
        json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)
    print(f"talents converted to behaviour: {changed}")
    pct=sum(1 for t in D["trees"] if t["kind"]!="vanilla" for r in t["rows"] for x in r["talents"]
            if any(e.get("source")=="authored" and e["op"]=="multiply" and e.get("stat") in ("damage","healing","effect") for e in x.get("effects",[])))
    tot=sum(len(r["talents"]) for t in D["trees"] if t["kind"]!="vanilla" for r in t["rows"])
    print(f"percentage talents remaining: {pct}/{tot} = {100*pct//tot}%  (was 30%)")
