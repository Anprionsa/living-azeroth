#!/usr/bin/env python3
"""What is one talent worth? Measured by removing its effects and re-running.

The 31-versus-30 comparison only moves for a capstone, so it cannot show whether a
mid-tree talent does anything at all. This can.
"""
import json, copy, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim
P="/mnt/user-data/outputs/talent-data.json"
def worth(cls, tid, host, name, n=35, scn="patchwerk"):
    BASE=json.load(open(P))
    with_it=statistics.mean([sim.run(cls,[(tid,31),(host,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
    D=copy.deepcopy(BASE)
    for t in D["trees"]:
        if t["id"]!=tid: continue
        for r in t["rows"]:
            for x in r["talents"]:
                if x["name"]==name: x["effects"]=[e for e in x.get("effects",[]) if e["op"]=="grant"]
    json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)
    importlib.reload(sim)
    without=statistics.mean([sim.run(cls,[(tid,31),(host,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
    json.dump(BASE,open(P,"w"),indent=1,ensure_ascii=False)
    importlib.reload(sim)
    return 100*(with_it-without)/without if without else 0.0
