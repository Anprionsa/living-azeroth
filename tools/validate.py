#!/usr/bin/env python3
"""Every accumulated project rule, as a suite. Rules live here, not in prose."""
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, re, sys
CONFIG=(sys.argv[1] if len(sys.argv)>1 else "expanded")
D=json.load(open(_ROOT + "/data/talent-data.json"))
D["trees"]=[t for t in D["trees"] if t["kind"]=="vanilla" or CONFIG in t.get("configurations",[])]
for t in D["trees"]:
    for r in t["rows"]:
        r["talents"]=[x for x in r["talents"] if x.get("availableIn") is None or CONFIG in x["availableIn"]]
    t["availablePoints"]=sum(x["ranks"] for r in t["rows"] for x in r["talents"])
VOCAB=set(D["meta"]["vocabulary"])
R=[]
def rule(name, sev, kinds):
    def deco(fn):
        R.append((name,sev,set(kinds),fn)); return fn
    return deco

@rule("gate-arithmetic","error",["vanilla","rebuilt","absorbed","original"])
def r1(t):
    return [f"row {r['row']} gate {r['gate']} should be {5*(r['row']-1)}"
            for r in t["rows"] if r["gate"] != 5*(r["row"]-1)]

@rule("reachability","error",["vanilla","rebuilt","absorbed","original"])
def r2(t):
    cum=0; bad=[]
    for r in sorted(t["rows"],key=lambda x:x["gate"]):
        if r["gate"]>cum: bad.append(f"gate {r['gate']} needs {r['gate']}, only {cum} below")
        cum+=sum(x["ranks"] for x in r["talents"])
    return bad

@rule("hybrid-seat-weight","warn",["rebuilt","absorbed","original"])
def r3(t):
    g=sum(x["ranks"] for r in t["rows"] if r["gate"]==20 for x in r["talents"])
    return [f"gate 20 carries {g}, want >=8"] if g<8 else []

@rule("no-numbers","warn",["rebuilt","absorbed","original"])
def r4(t):
    n=[x["name"] for r in t["rows"] for x in r["talents"] if x["buys"]=="number"]
    return [f"{len(n)} numeric talents: {', '.join(n[:4])}"] if n else []

@rule("subtraction-present","warn",["rebuilt","absorbed","original"])
def r5(t):
    return [] if any("subtraction" in x["flags"] for r in t["rows"] for x in r["talents"]) else ["no subtraction node"]

@rule("cross-tree-stands-alone","error",["vanilla","rebuilt","absorbed","original"])
def r6(t):
    return [f"{x['name']} does not stand alone" for r in t["rows"] for x in r["talents"]
            if x["crossTree"] and x["crossTree"]["standsAlone"] is False]

@rule("one-capstone","error",["rebuilt","absorbed","original"])
def r16(t):
    c=[x["name"] for r in t["rows"] if r["gate"]>=30 for x in r["talents"]]
    return [f"{len(c)} capstones: {', '.join(c)}"] if len(c)!=1 else []

@rule("no-passive-aura-capstone","warn",["rebuilt","absorbed","original"])
def r7(t):
    return [f"{x['name']} is a passive aura at the capstone" for r in t["rows"] if r["gate"]>=30
            for x in r["talents"] if "aura" in x["flags"] and x["buys"]!="ability"]

@rule("mechanic-coverage-band","warn",["absorbed","original"])
def r8(t):
    if not t["mechanic"]: return []
    ws=[w.lower() for w in re.findall(r"[A-Za-z]{4,}", t["mechanic"]["name"])]
    stems=[(w[:-4] if w.endswith("ment") else (w[:-1] if w.endswith("s") else w)) for w in ws]
    key="|".join(re.escape(x) for x in stems) or "zzzz"
    m=sum(x["ranks"] for r in t["rows"] for x in r["talents"] if re.search(key,x["name"]+" "+x["text"],re.I))
    share=100*m//t["availablePoints"]
    return [f"mechanic coverage {share}%, band is 40-80"] if not 40<=share<=80 else []

@rule("tree-size-band","warn",["vanilla","rebuilt","absorbed","original"])
def r9(t):
    p=t["availablePoints"]
    return [f"{p} available points, band is 45-64"] if not 45<=p<=64 else []

@rule("vocabulary","error",["vanilla","rebuilt","absorbed","original"])
def r10(t):
    bad=set()
    for r in t["rows"]:
        for x in r["talents"]: bad|= set(x["reads"])-VOCAB
    return [f"unknown categories: {sorted(bad)}"] if bad else []

@rule("no-permissions","warn",["rebuilt"])
def r11(t):
    return [f"{x['name']} is a permission" for r in t["rows"] for x in r["talents"]
            if re.match(r"^Allows you to use|^Gives a chance to parry",x["text"])]

@rule("text-complete","warn",["rebuilt","absorbed","original"])
def r13(t):
    n=[x["name"] for r in t["rows"] for x in r["talents"] if "text-incomplete" in x["flags"]]
    return [f"{len(n)} talents lack a stated effect: {', '.join(n[:3])}"] if n else []

VOICE=re.compile(r"^(Your|You|Increases|Reduces|Decreases|Gives|Allows|Causes|Grants|Instantly|When|While|After|At |Each|All |A |An |Two|Three|Transforms|Puts|Places|Absorbing|Dodging|Blocking|Parrying|Cleansing|Healing|Spending|Shifting|Being|Critical|Shadowform|Blessing|Damage|Enemies|Allies|Dropping|Windfury|Dodged|Its|It )")
BADSTYLE=re.compile(r";|\bthen\b|^(From |Kept|Reworked|Replacing|Moved|Unchanged|Sideways|Subtraction|Cross-tree|The (sideways|subtraction))", re.I)
@rule("vanilla-voice","warn",["rebuilt","absorbed","original"])
def r14(t):
    ABIL={a["name"] for a in D.get("abilities",[]) if a["class"]==t["class"]}
    bad=[x["name"] for r in t["rows"] for x in r["talents"] if BADSTYLE.search(x["text"])]
    off=[x["name"] for r in t["rows"] for x in r["talents"] if not re.match(r"^[A-Z]", x["text"])]
    out=[]
    if bad: out.append(f"{len(bad)} talents use design-doc style: {', '.join(bad[:3])}")
    if len(off)>len([x for r in t["rows"] for x in r["talents"]])*0.45:
        out.append(f"{len(off)} talents do not open in vanilla voice")
    return out

@rule("ranks-match-effects","warn",["rebuilt","absorbed","original"])
def r15(t):
    bad=[x["name"] for r in t["rows"] for x in r["talents"] if x["ranks"]>=3
         and len([s for s in re.split(r"(?<=\.)\s+",x["text"]) if len(s.split())>2])<2]
    return [f"{len(bad)} multi-rank talents describe one effect: {', '.join(bad[:3])}"] if bad else []

@rule("sim-readiness","warn",["rebuilt"])
def r17(t):
    tal=[x for r in t["rows"] for x in r["talents"]]
    try: scope={n.split("/",1)[1] for n in json.load(open(_ROOT + "/files/sim-authoring-scope.json")) if n.startswith(t["name"]+"/")}
    except Exception: scope=set()
    if not scope: return []
    missing=[x["name"] for x in tal if x["name"] in scope and not any(e.get("source")=="authored" for e in x.get("effects",[]))]
    return [f"{len(missing)} of {len(scope)} scope talents lack authored effects: {', '.join(missing[:3])}"] if missing else []

@rule("effect-vocabulary","error",["rebuilt","absorbed","original"])
def r18(t):
    V=D["meta"].get("effectVocabulary")
    if not V: return []
    bad=set()
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                if e["op"] not in V["ops"]: bad.add(e["op"])
                if e["op"]=="enable" and e.get("flag") not in V["flags"]: bad.add(str(e.get("flag")))
                if e["op"]=="proc" and e.get("stat") not in V["procs"]: bad.add(str(e.get("stat")))
                if e["op"] in ("add","multiply","ignore","refresh") and e.get("stat") and e["stat"] not in V["stats"]: bad.add(e["stat"])
    return [f"outside the closed vocabulary: {sorted(bad)[:5]}"] if bad else []

@rule("effect-references","error",["rebuilt","absorbed","original"])
def r19(t):
    abil={a["id"] for a in D.get("abilities",[])}
    bad=set()
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                a=e.get("scope",{}).get("ability")
                if a and a not in abil: bad.add(a)
    return [f"effects point at unknown abilities: {sorted(bad)[:4]}"] if bad else []

@rule("effect-magnitudes","warn",["rebuilt","absorbed","original"])
def r20(t):
    V=D["meta"].get("effectVocabulary",{}).get("magnitudeRequired")
    if not V: return []
    req=set(V["required"]); bad=[]
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                if e.get("source")=="authored" and e["op"] in req and e.get("magnitude") is None:
                    bad.append(x["name"])
    return [f"{len(bad)} authored effects need a magnitude: {', '.join(sorted(set(bad))[:3])}"] if bad else []

@rule("no-broad-zeroing","error",["rebuilt","absorbed","original"])
def r21(t):
    bad=[]
    for r in t["rows"]:
        for x in r["talents"]:
            for e in x.get("effects",[]):
                if e.get("source")!="authored": continue
                sc=e.get("scope",{})
                if (e["op"]=="multiply" and e.get("magnitude")==0.0
                    and e.get("stat") in ("cooldown","cost","castTime")
                    and (sc.get("all") or sc.get("tag"))):
                    bad.append(f"{x['name']} zeroes {e['stat']} across {sc}")
    return bad

@rule("band-recorded","warn",["rebuilt"])
def r24(t):
    b=D["meta"].get("band")
    if not b: return ["no band recorded in meta"]
    return []

@rule("no-vanilla-tooltip","error",["rebuilt","absorbed","original"])
def r25(t):
    import re as _re
    pat=_re.compile(r"^(Increases|Reduces|Decreases|Gives|Places|Allows|Causes|Grants|Deals|Restores|Heals|Summons|When activated,)\b.{0,90}?\b(\d+%|\d+ sec|\d+ min|by \d+|instant cast spell)")
    bad=[x["name"] for r in t["rows"] for x in r["talents"] if pat.search(x["text"])]
    return [f"raw vanilla tooltip phrasing: {', '.join(bad[:3])}"] if bad else []

@rule("no-placeholder-text","error",["rebuilt","absorbed","original"])
def r23(t):
    import re as _re
    bad=[x["name"] for r in t["rows"] for x in r["talents"]
         if _re.search(r"\bYour this\b|\bthis this\b|\bN%|\bby N\b|\bN sec\b", x["text"])]
    return [f"vanilla placeholder or broken text: {', '.join(bad[:3])}"] if bad else []

@rule("percentage-drift","warn",["rebuilt","absorbed","original"])
def r22(t):
    tal=[x for r in t["rows"] for x in r["talents"]]
    # only a POSITIVE multiplier across a whole tag is the flat modifier 5.2 deleted.
    # a penalty is the cost of a subtraction node, and a single-ability buff is specific.
    def drift(e):
        return (e.get("source")=="authored" and e["op"]=="multiply"
                and e.get("stat") in ("damage","healing","effect")
                and (e.get("magnitude") or 1.0) > 1.0
                and not e.get("scope",{}).get("ability"))
    pct=[x["name"] for x in tal if any(drift(e) for e in x.get("effects",[]))]
    if len(pct) > len(tal)*0.20:
        return [f"{len(pct)}/{len(tal)} talents express their effect as a percentage, which is what 5.2 deleted"]
    return []

@rule("mechanic-present","error",["absorbed","original"])
def r12(t):
    return [] if t["mechanic"] else ["no local mechanic declared"]

# an ability a talent grants must be reachable, or the talent grants nothing
_A={a["id"]:a for a in D.get("abilities",[])}
_rot=set()
for _r in D.get("rotations",{}).values():
    for _k in ("priority","healingPriority","feralPriority"):
        for _e in _r.get(_k,[]): _rot.add(_e["ability"] if isinstance(_e,dict) else _e)
_cds=set(D.get("cooldowns",{}))
_gr=set()
for _t in D.get("trees",[]):
    for _rw in _t["rows"]:
        for _x in _rw["talents"]:
            _gr|=set(_x.get("grants",[]))
            for _e in _x.get("effects",[]):
                if _e["op"]=="grant" and _e.get("scope",{}).get("ability"): _gr.add(_e["scope"]["ability"])
_unreach=sorted(i for i in _gr if i not in _rot and i not in _cds
                and (_A.get(i,{}).get("baseDamage") or _A.get(i,{}).get("baseHealing")))
if _unreach: print(f"  FAIL  grant-reachability          {len(_unreach)}: {_unreach[:4]}")
else: print(f"  PASS  grant-reachability          0 finding(s)")

# rotations reference abilities that must exist
_abil={a["id"] for a in D.get("abilities",[])}
_rotbad=sorted({a for r in D.get("rotations",{}).values() for k in ("priority","healingPriority","feralPriority") for a in [(e["ability"] if isinstance(e,dict) else e) for e in r.get(k,[])] if a not in _abil})
if _rotbad: print(f"  FAIL  rotation-references          {len(_rotbad)}: {_rotbad[:4]}")
else: print(f"  PASS  rotation-references          0 finding(s)")

errs=warns=0; report={}
for t in D["trees"]:
    for name,sev,kinds,fn in R:
        if t["kind"] not in kinds: continue
        for msg in fn(t):
            report.setdefault(name,[]).append((sev,t["name"],t["kind"],msg))
            if sev=="error": errs+=1
            else: warns+=1
print(f"CONFIGURATION: {CONFIG}\n{len(D['trees'])} trees, {sum(len(r['talents']) for t in D['trees'] for r in t['rows'])} talents, {len(R)} rules\n")
for name,sev,kinds,fn in R:
    hits=report.get(name,[])
    mark="PASS" if not hits else ("FAIL" if hits[0][0]=="error" else "WARN")
    print(f"  {mark}  {name:28} {len(hits)} finding(s)")
    for sev,tn,kind,msg in hits[:4]:
        print(f"          {tn} ({kind}): {msg}")
    if len(hits)>4: print(f"          ... and {len(hits)-4} more")
print(f"\nerrors {errs} | warnings {warns}")
sys.exit(1 if errs else 0)
