#!/usr/bin/env python3
"""Calibrate the gear blocks against logged Naxxramas output.

The blocks were invented and never checked against each other, so cross-class comparison
was meaningless. This scales each class's primary stat until its canonical build lands on
its logged number, which is what sim-baseline-protocol.md meant by "the control is
something you download".

After this the sim can answer a question it could not before: how far apart do the specs
sit under the rework, against how far apart they sit in the logs.
"""
import json, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim, logcompare as LC
P="/mnt/user-data/outputs/talent-data.json"

def scale_gear(cls, f):
    D=json.load(open(P))
    g=D["gear"][cls]
    for k in ("attackPower","spellDamage","weaponDamage","healingBonus"):
        if g.get(k): g[k]=round(g[k]*f,1)
    D["gear"][cls]=g
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)

def calibrate(rounds=9, n=22):
    # a class appears more than once; calibrate on its highest logged spec
    primary={}
    for k,v in LC.CONTROL.items():
        cls=LC.MAP[k][0]
        if cls not in primary or v>LC.CONTROL[primary[cls]]: primary[cls]=k
    for cls,key in sorted(primary.items()):
        target=LC.CONTROL[key]
        for i in range(rounds):
            importlib.reload(sim)
            c,build=LC.MAP[key]
            got=statistics.mean([sim.run(c,build,seed=s)[0] for s in range(1,n+1)])
            if abs(got-target)/target<=0.04: break
            scale_gear(cls, max(0.5,min(2.2,(target/max(1,got))**0.75)))
        importlib.reload(sim)
        got=statistics.mean([sim.run(c,build,seed=s)[0] for s in range(1,n+1)])
        print(f"  {cls:9} {key:22} target {target:5} got {got:5.0f}  {100*(got-target)/target:+5.1f}%")

if __name__=="__main__":
    print("calibrating gear to logged output:")
    calibrate()
