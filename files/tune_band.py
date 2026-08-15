#!/usr/bin/env python3
"""Tune a capstone until every scenario sits inside the band.

Converging on patchwerk alone leaves a capstone that is fine sustained and wrong in
one scenario. This targets the worst cell instead.
"""
import json, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim
P="/mnt/user-data/outputs/talent-data.json"
SCN=["patchwerk","burst","movement","cleave","switching"]
LO,HI=-7.0,7.0

def gaps(cls,a,b,n=40):
    out={}
    for scn in SCN:
        x=statistics.mean([sim.run(cls,[(a,31),(b,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
        y=statistics.mean([sim.run(cls,[(a,30),(b,21)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
        out[scn]=100*(x-y)/y if y else 0.0
    return out

def scale_cap(tid,f,cooldownsOnly=False):
    D=json.load(open(P)); t=next(x for x in D["trees"] if x["id"]==tid)
    cap=max(t["rows"], key=lambda r:r["gate"]); ids=set()
    for x in cap["talents"]:
        ids|=set(x.get("grants",[]))
        if cooldownsOnly: continue
        for e in x.get("effects",[]):
            m=e.get("magnitude")
            if m is None or e.get("source")!="authored": continue
            if e.get("stat") in ("openingDamage","frontload","cleaveEvery"): continue
            if e["op"]=="multiply" and e.get("stat") in ("damage","effect") and m>1.0: e["magnitude"]=round(1+(m-1)*f,4)
            elif e["op"] in ("debuff","consume","proc","add"): e["magnitude"]=round(m*f,4)
    for k,v in D.get("cooldowns",{}).items():
        if k not in ids: continue
        for st in ("damage","critChance","resourceRate","haste"):
            if st in v["effect"]:
                b=v["effect"][st]; v["effect"][st]=round(1+(b-1)*f,4) if b>1.0 else round(b*f,4)
    if not cooldownsOnly:
        for a in D["abilities"]:
            if a["id"] not in ids: continue
            for k in ("baseDamage","baseHealing","spCoefficient","apCoefficient","rapCoefficient"):
                if a.get(k): a[k]=round(a[k]*f,4)
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)

def fit(cls,a,b,label,rounds=7):
    """Bring the worst offending cell inside the band."""
    for i in range(rounds):
        importlib.reload(sim)
        g=gaps(cls,a,b)
        hi=max(g.values()); lo=min(g.values())
        if lo>=LO and hi<=HI: return g
        # a cooldown that only overshoots in one scenario is tuned through the cooldown
        # table alone, so its sustained value is left where it belongs
        over=hi-HI; under=LO-lo
        if over>=under:
            spread=hi-statistics.median(list(g.values()))
            f=max(0.45,min(1.0,(HI+100)/(hi+100)))**(3.0 if spread>4 else 2.0)
            scale_cap(a,f,cooldownsOnly=(spread>4))
        else:
            scale_cap(a, min(2.0,((LO+100)/(lo+100))**-2.0))
    importlib.reload(sim)
    return gaps(cls,a,b)

if __name__=="__main__":
    CASES=[("Mage","mage-arcane-rebuilt","mage-fire-rebuilt","Arcane"),
     ("Warlock","warlock-affliction-rebuilt","warlock-destruction-rebuilt","Affliction"),
     ("Warlock","warlock-destruction-rebuilt","warlock-demonology-rebuilt","Destruction"),
     ("Warrior","warrior-arms-rebuilt","warrior-fury-rebuilt","Arms")]
    for cls,a,b,lbl in CASES:
        g=fit(cls,a,b,lbl)
        ok="in band" if min(g.values())>=LO and max(g.values())<=HI else "OUT"
        print(f"  {lbl:12} " + " ".join(f"{k[:4]} {v:+6.1f}%" for k,v in g.items()) + f"   {ok}")
