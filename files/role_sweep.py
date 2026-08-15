#!/usr/bin/env python3
"""Talent worth in healing and tank trees, measured with their own instruments.

The damage sweep excludes these trees because measuring them with sim.py reports every
talent in them as worth zero. This measures healing with heal.py and tanks with tank.py.
"""
import json, copy, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim, heal, tank
P="/mnt/user-data/outputs/talent-data.json"
BASE=json.load(open(P))
HEAL=[("Priest","priest-holy-rebuilt","priest-discipline-rebuilt"),
      ("Priest","priest-discipline-rebuilt","priest-holy-rebuilt"),
      ("Druid","druid-restoration-rebuilt","druid-balance-rebuilt"),
      ("Shaman","shaman-restoration-rebuilt","shaman-elemental-rebuilt"),
      ("Paladin","paladin-holy-rebuilt","paladin-protection-rebuilt")]
TANK=[("Warrior","warrior-protection-rebuilt","warrior-fury-rebuilt"),
      ("Paladin","paladin-protection-rebuilt","paladin-retribution-rebuilt"),
      ("Druid","druid-feral-combat-rebuilt","druid-restoration-rebuilt"),
      ("Warlock","metamorphosis","warlock-destruction-rebuilt")]

def strip(tid,name):
    D=copy.deepcopy(BASE)
    for t in D["trees"]:
        if t["id"]!=tid: continue
        for r in t["rows"]:
            for x in r["talents"]:
                if x["name"]==name: x["effects"]=[]; x["grants"]=[]
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)

def restore():
    json.dump(BASE,open(P,"w"),indent=1,ensure_ascii=False)

def heal_val(cls,tid,host,n=14):
    r=[heal.run_heal(cls,[(tid,31),(host,20)],seed=s) for s in range(1,n+1)]
    return statistics.mean(x["hps"] for x in r), statistics.mean(x["hpm"] for x in r)

def tank_val(cls,tid,host,n=16):
    r=[tank.run_tank(cls,[(tid,31),(host,20)],seed=s) for s in range(1,n+1)]
    return statistics.mean(x["tps"] for x in r), statistics.mean(x["ehp"] for x in r)

def sweep(kind="heal"):
    out=[]
    cases = HEAL if kind=="heal" else TANK
    val = heal_val if kind=="heal" else tank_val
    for cls,tid,host in cases:
        importlib.reload(sim); importlib.reload(heal); importlib.reload(tank)
        taken=sim.build(tid,31,forceCapstone=True,role=("heal" if kind=="heal" else "tank"))[0]
        a0,b0=val(cls,tid,host)
        for name in list(taken):
            strip(tid,name)
            importlib.reload(sim); importlib.reload(heal); importlib.reload(tank)
            a,b=val(cls,tid,host)
            out.append((tid,name,100*(a0-a)/a0 if a0 else 0.0, 100*(b0-b)/b0 if b0 else 0.0))
        restore(); importlib.reload(sim); importlib.reload(heal); importlib.reload(tank)
    return out

if __name__=="__main__":
    for kind,m1,m2 in (("heal","HPS","HPM"),("tank","TPS","EHP")):
        r=sweep(kind)
        zero=[x for x in r if abs(x[2])<0.05 and abs(x[3])<0.05]
        print(f"{kind.upper()}: {len(r)} measured, {len(zero)} worth zero on both {m1} and {m2}")
        from collections import Counter
        for tid,k in Counter(t for t,_,_,_ in zero).most_common():
            print(f"  {tid.replace('-rebuilt',''):28} {k}  {', '.join(n for t,n,_,_ in zero if t==tid)}")
        print()
