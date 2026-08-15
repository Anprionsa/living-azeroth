#!/usr/bin/env python3
"""Candidate fixes for the Arms cleave gap, measured on both axes.

The measure is cleave gained per point of sustained inflated. A candidate that lifts
both equally has not given the capstone cleave relevance, it has just made it stronger.
"""
import json, copy, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim
P="/mnt/user-data/outputs/talent-data.json"
BASE=json.load(open(P))
def E(op,stat=None,sc=None,mag=None,**kw):
    e={"op":op,"scope":sc or {"all":True},"magnitude":mag,"source":"authored"}
    if stat: e["flag" if op=="enable" else "stat"]=stat
    e.update(kw); return e

CANDIDATES={
 "H. every 3rd cleaves 1, wound spreads": [E("add","cleaveEvery",{"all":True},3,extraTargets=1),
                                           E("addTarget",None,{"tag":"bleed"},1.0)],
 "I. every 4th cleaves 1":         [E("add","cleaveEvery",{"all":True},4,extraTargets=1)],
 "J. every 5th cleaves 2":         [E("add","cleaveEvery",{"all":True},5,extraTargets=2)],
 "A. every 3rd strike cleaves 1":   [E("add","cleaveEvery",{"all":True},3,extraTargets=1)],
 "B. every 2nd strike cleaves 1":   [E("add","cleaveEvery",{"all":True},2,extraTargets=1)],
 "C. every 3rd strike cleaves 2":   [E("add","cleaveEvery",{"all":True},3,extraTargets=2)],
 "D. every 4th strike cleaves 2":   [E("add","cleaveEvery",{"all":True},4,extraTargets=2)],
 "E. Mortal Strike hits 2":         [E("addTarget",None,{"ability":"warrior-mortal-strike"},1.0)],
 "F. Mortal Strike hits 3":         [E("addTarget",None,{"ability":"warrior-mortal-strike"},2.0)],
 "G. wound spreads through bleeds": [E("addTarget",None,{"tag":"bleed"},2.0)],
}
def apply(eff):
    D=copy.deepcopy(BASE)
    for t in D["trees"]:
        if t["id"]!="warrior-arms-rebuilt": continue
        for r in t["rows"]:
            for x in r["talents"]:
                if x["name"]=="Mortal Strike":
                    x["effects"]=[e for e in x["effects"] if e["op"]=="grant"]+eff+[
                        {"op":"add","scope":{"tag":"melee"},"stat":"healingReduction","magnitude":0.35,"source":"authored"}]
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)
def gap(scn,n=45):
    a=statistics.mean([sim.run("Warrior",[("warrior-arms-rebuilt",31),("warrior-fury-rebuilt",20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
    b=statistics.mean([sim.run("Warrior",[("warrior-arms-rebuilt",30),("warrior-fury-rebuilt",21)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
    return 100*(a-b)/b if b else 0.0
if __name__=="__main__":
    importlib.reload(sim)
    bc,bp=gap("cleave"),gap("patchwerk")
    print(f"  {'candidate':32} {'cleave':>8} {'patch':>8} {'gain':>7} {'cost':>7} {'ratio':>7}")
    print(f"  {'baseline':32} {bc:+7.1f}% {bp:+7.1f}%")
    for name,eff in CANDIDATES.items():
        apply(eff); importlib.reload(sim)
        c,pk=gap("cleave"),gap("patchwerk")
        gain=c-bc; cost=pk-bp
        ratio=gain/cost if cost>0.2 else float("inf")
        print(f"  {name:32} {c:+7.1f}% {pk:+7.1f}% {gain:+6.1f} {cost:+6.1f} {ratio:7.1f}")
    json.dump(BASE,open(P,"w"),indent=1,ensure_ascii=False)
    print("\n  data restored to baseline")
