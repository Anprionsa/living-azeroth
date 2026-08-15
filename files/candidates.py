#!/usr/bin/env python3
"""A/B test candidate designs for closing a burst gap.

The measure that matters is not how much burst a candidate adds but how much it adds
PER POINT of sustained output it inflates. A candidate that lifts both equally has
changed nothing about the tree's shape.
"""
import json, copy, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim, tune
P="/mnt/user-data/outputs/talent-data.json"
BASE=json.load(open(P))

def E(op,stat=None,sc=None,mag=None,**kw):
    e={"op":op,"scope":sc or {"all":True},"magnitude":mag,"source":"authored"}
    if stat: e["flag" if op=="enable" else "stat"]=stat
    e.update(kw); return e

CANDIDATES={
 "A. pet amplifier, 3min/20s":{"talent":"Dark Command","cooldown":("mage-dark-command",
   {"class":"Mage","duration":20,"cooldown":180,"effect":{"damage":1.55},"tags":["pet","shadow"]})},
 "B. pet amplifier, 90s/15s":{"talent":"Dark Command","cooldown":("mage-dark-command",
   {"class":"Mage","duration":15,"cooldown":90,"effect":{"damage":1.30},"tags":["pet","shadow"]})},
 "C. Wither front-loads 50%":{"talent":"Wither","effects":[E("add","frontload",{"ability":"mage-wither"},0.50)]},
 "D. opening window +25%/15s":{"talent":"Wither","effects":[E("add","openingDamage",{"all":True},0.25,window=15.0)]},
 "E. opening window +40%/10s":{"talent":"Wither","effects":[E("add","openingDamage",{"all":True},0.40,window=10.0)]},
 "G. pet amp 3min/20s, +35%":{"talent":"Dark Command","cooldown":("mage-dark-command",
   {"class":"Mage","duration":20,"cooldown":180,"effect":{"damage":1.35},"tags":["pet","shadow"]})},
 "H. pet amp 3min/25s, +30%":{"talent":"Dark Command","cooldown":("mage-dark-command",
   {"class":"Mage","duration":25,"cooldown":180,"effect":{"damage":1.30},"tags":["pet","shadow"]})},
 "I. opening +30%/20s":{"talent":"Wither","effects":[E("add","openingDamage",{"all":True},0.30,window=20.0)]},
 "F. Boneyard amplifies its own army":{"talent":None,"cooldown":("mage-boneyard-amp",
   {"class":"Mage","duration":25,"cooldown":120,"effect":{"damage":1.40},"tags":["pet"]}),"grantOn":"Boneyard"},
}

def apply(name, spec):
    D=copy.deepcopy(BASE)
    if spec.get("cooldown"):
        aid,cd=spec["cooldown"]
        D["cooldowns"][aid]=cd
        if not any(a["id"]==aid for a in D["abilities"]):
            D["abilities"].append({"id":aid,"class":cd["class"],"name":aid.split("-",1)[1].replace("-"," ").title(),
              "tags":cd["tags"],"scalesWith":[],"coefficient":None,"castTime":0,"cooldown":cd["cooldown"],
              "cost":0,"costType":None,"baseDamage":0,"gcd":0,"duration":cd["duration"],"confidence":"candidate"})
        host=spec.get("grantOn") or spec["talent"]
        for t in D["trees"]:
            if t["id"]!="necromancy": continue
            for r in t["rows"]:
                for x in r["talents"]:
                    if x["name"]==host: x.setdefault("grants",[]).append(aid)
    if spec.get("effects"):
        for t in D["trees"]:
            if t["id"]!="necromancy": continue
            for r in t["rows"]:
                for x in r["talents"]:
                    if x["name"]==spec["talent"]: x["effects"]=x.get("effects",[])+spec["effects"]
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)

if __name__=="__main__":
    importlib.reload(sim); importlib.reload(tune)
    base=tune.gaps("Mage","necromancy","mage-frost-rebuilt",n=40)
    print(f"  {'candidate':34} {'burst':>8} {'patch':>8} {'gain':>7} {'cost':>7} {'ratio':>7}")
    print(f"  {'baseline':34} {base['burst']:+7.1f}% {base['patchwerk']:+7.1f}%")
    for name,spec in CANDIDATES.items():
        apply(name,spec)
        importlib.reload(sim); importlib.reload(tune)
        g=tune.gaps("Mage","necromancy","mage-frost-rebuilt",n=40)
        gain=g["burst"]-base["burst"]; cost=g["patchwerk"]-base["patchwerk"]
        ratio=gain/cost if cost>0.15 else float("inf")
        print(f"  {name:34} {g['burst']:+7.1f}% {g['patchwerk']:+7.1f}% {gain:+6.1f} {cost:+6.1f} {ratio:7.1f}")
    json.dump(BASE,open(P,"w"),indent=1,ensure_ascii=False)
    print("\n  data restored to baseline")
