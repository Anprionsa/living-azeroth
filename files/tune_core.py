#!/usr/bin/env python3
"""Converge a core pair's capstone premium. Only the capstone seat moves, since the
gap between a 31 and a 30 point build IS the capstone."""
import json, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim
P="/mnt/user-data/outputs/talent-data.json"
def pair(cls,a,b,n=45,scn="patchwerk"):
    r1=statistics.mean([sim.run(cls,[(a,31),(b,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
    r2=statistics.mean([sim.run(cls,[(a,30),(b,21)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
    return 100*(r1-r2)/r2 if r2 else 0.0
def scale_cap(tid,f):
    D=json.load(open(P)); t=next(x for x in D["trees"] if x["id"]==tid)
    cap=max(t["rows"], key=lambda r:r["gate"]); ids=set()
    for x in cap["talents"]:
        ids|=set(x.get("grants",[]))
        for e in x.get("effects",[]):
            m=e.get("magnitude")
            if m is None or e.get("source")!="authored": continue
            if e["op"]=="multiply" and e.get("stat") in ("damage","effect") and m>1.0: e["magnitude"]=round(1+(m-1)*f,4)
            elif e["op"] in ("debuff","consume","proc","add") and e.get("stat") not in ("openingDamage","frontload"):
                e["magnitude"]=round(m*f,4)
    for k,v in D.get("cooldowns",{}).items():
        if k not in ids: continue
        for st in ("damage","critChance","resourceRate","haste"):
            if st in v["effect"]:
                b=v["effect"][st]; v["effect"][st]=round(1+(b-1)*f,4) if b>1.0 else round(b*f,4)
    for a in D["abilities"]:
        if a["id"] not in ids: continue
        for k in ("baseDamage","baseHealing","spCoefficient","apCoefficient","rapCoefficient"):
            if a.get(k): a[k]=round(a[k]*f,4)
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)
def converge(cls,a,b,label,target=2.5,tol=2.5,rounds=6):
    for i in range(rounds):
        importlib.reload(sim); g=pair(cls,a,b)
        if abs(g-target)<=tol: break
        scale_cap(a, max(0.35,min(2.4,((100+target)/(100+g))**3.0)))
    importlib.reload(sim)
    return pair(cls,a,b)
if __name__=="__main__":
    CASES=[("Warrior","warrior-arms-rebuilt","warrior-fury-rebuilt","Arms"),
     ("Warrior","warrior-fury-rebuilt","warrior-protection-rebuilt","Fury"),
     ("Warlock","warlock-affliction-rebuilt","warlock-destruction-rebuilt","Affliction"),
     ("Warlock","warlock-destruction-rebuilt","warlock-demonology-rebuilt","Destruction"),
     ("Hunter","hunter-marksmanship-rebuilt","hunter-beast-mastery-rebuilt","Marksmanship")]
    for cls,a,b,lbl in CASES:
        print(f"  {lbl:14} {converge(cls,a,b,lbl):+.1f}%")
