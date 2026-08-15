#!/usr/bin/env python3
"""Tune a tank capstone to the tank band: the mean of its threat and effective health
gaps, held between -7% and +7%."""
import json, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim, tank
P="/mnt/user-data/outputs/talent-data.json"
LO,HI=-7.0,7.0
def gaps(cls,a,b,n=25):
    r1=[tank.run_tank(cls,[(a,31),(b,20)],seed=s) for s in range(1,n+1)]
    r2=[tank.run_tank(cls,[(a,30),(b,21)],seed=s) for s in range(1,n+1)]
    m=lambda r,k: statistics.mean(x[k] for x in r)
    t=100*(m(r1,"tps")-m(r2,"tps"))/m(r2,"tps")
    e=100*(m(r1,"ehp")-m(r2,"ehp"))/max(1,m(r2,"ehp"))
    return t,e,(t+e)/2
def scale_cap(tid,f):
    D=json.load(open(P)); t=next(x for x in D["trees"] if x["id"]==tid)
    cap=max(t["rows"], key=lambda r:r["gate"]); ids=set()
    for x in cap["talents"]:
        ids|=set(x.get("grants",[]))
        for e in x.get("effects",[]):
            m=e.get("magnitude")
            if m is None or e.get("source")!="authored": continue
            st=e.get("stat")
            if e["op"]=="multiply" and st=="threat" and m>1.0: e["magnitude"]=round(1+(m-1)*f,4)
            elif e["op"]=="multiply" and st=="damageTaken" and m<1.0: e["magnitude"]=round(min(0.999,1-(1-m)*f),4)
            elif e["op"]=="add" and st in ("threat","dodge","parry","blockChance","blockValue","health","selfHeal"):
                e["magnitude"]=round(m*f,4)
            elif e["op"] in ("debuff","consume","proc"): e["magnitude"]=round(m*f,4)
    for k,v in D.get("cooldowns",{}).items():
        if k not in ids: continue
        for st in ("damage","critChance"):
            if st in v["effect"]:
                b=v["effect"][st]; v["effect"][st]=round(1+(b-1)*f,4) if b>1.0 else round(b*f,4)
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)
def fit(cls,a,b,label,rounds=7):
    for i in range(rounds):
        importlib.reload(sim); importlib.reload(tank)
        t,e,m = gaps(cls,a,b)
        if LO<=m<=HI: break
        scale_cap(a, max(0.35,min(2.2,((100+2.0)/(100+m))**2.2)))
    importlib.reload(sim); importlib.reload(tank)
    return gaps(cls,a,b)
if __name__=="__main__":
    for cls,a,b,lbl in [("Warrior","warrior-protection-rebuilt","warrior-fury-rebuilt","Prot warrior"),
     ("Paladin","paladin-protection-rebuilt","paladin-retribution-rebuilt","Prot paladin"),
     ("Druid","druid-feral-combat-rebuilt","druid-restoration-rebuilt","bear"),
     ("Warlock","metamorphosis","warlock-destruction-rebuilt","Metamorphosis")]:
        t,e,m=fit(cls,a,b,lbl)
        print(f"  {lbl:14} TPS {t:+6.1f}%  EHP {e:+6.1f}%  mean {m:+6.1f}%   {'in band' if LO<=m<=HI else 'OUT'}")
