#!/usr/bin/env python3
"""Data for the scenario-band decision.

The open question is whether a capstone may exceed the band in the scenario its shape
suits. Rather than argue it, this measures what each of three policies would require.
"""
import json, copy, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim
P="/mnt/user-data/outputs/talent-data.json"
BASE=json.load(open(P))
SCN=["patchwerk","burst","movement","cleave","switching"]
PAIRS=[("Warrior","warrior-arms-rebuilt","warrior-fury-rebuilt","Arms","periodic cleave"),
 ("Warrior","warrior-fury-rebuilt","warrior-protection-rebuilt","Fury","strike + heal"),
 ("Rogue","rogue-combat-rebuilt","rogue-assassination-rebuilt","Combat","cooldown"),
 ("Mage","mage-fire-rebuilt","mage-frost-rebuilt","Fire","cooldown"),
 ("Mage","mage-arcane-rebuilt","mage-fire-rebuilt","Arcane","cooldown"),
 ("Warlock","warlock-affliction-rebuilt","warlock-destruction-rebuilt","Affliction","cooldown"),
 ("Warlock","warlock-destruction-rebuilt","warlock-demonology-rebuilt","Destruction","passive"),
 ("Priest","priest-shadow-rebuilt","priest-discipline-rebuilt","Shadow","passive"),
 ("Hunter","hunter-marksmanship-rebuilt","hunter-beast-mastery-rebuilt","Marksmanship","cast time"),
 ("Druid","druid-balance-rebuilt","druid-feral-combat-rebuilt","Balance","form")]
def gaps(cls,a,b,n=45):
    out={}
    for scn in SCN:
        x=statistics.mean([sim.run(cls,[(a,31),(b,20)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
        y=statistics.mean([sim.run(cls,[(a,30),(b,21)],seed=s,scenario=scn)[0] for s in range(1,n+1)])
        out[scn]=100*(x-y)/y if y else 0.0
    return out
if __name__=="__main__":
    importlib.reload(sim)
    print(f"  {'pair':14} {'shape':16}" + "".join(f"{s[:9]:>10}" for s in SCN))
    rows=[]
    for cls,a,b,lbl,shape in PAIRS:
        g=gaps(cls,a,b); rows.append((lbl,shape,g))
        print(f"  {lbl:14} {shape:16}" + "".join(f"{g[s]:+9.1f}%" for s in SCN))
    print()
    # policy 1: one band everywhere
    def viol(g,lo,hi,scn=None):
        ks=[scn] if scn else SCN
        return sum(1 for k in ks if not (lo<=g[k]<=hi))
    for lo,hi,name in [(-5,5,"one band, -5 to +5"),(-6,6,"one band, -6 to +6"),
                       (-7,7,"one band, -7 to +7"),(-8,8,"one band, -8 to +8")]:
        bad=[(l,k,g[k]) for l,_,g in rows for k in SCN if not (lo<=g[k]<=hi)]
        print(f"  {name:24} {len(bad):2} violations of {len(rows)*len(SCN)} cells   " +
              ", ".join(f"{l}/{k[:5]} {v:+.0f}%" for l,k,v in bad[:6]))
    # policy 2: sustained band tight, signature scenario loose
    SIG={"cooldown":"burst","periodic cleave":"cleave","form":"cleave","cast time":"movement","passive":None,"strike + heal":None}
    v=0
    for lbl,shape,g in rows:
        sig=SIG.get(shape)
        for s in SCN:
            lo,hi=(-15,20) if s==sig else (-5,5)
            if not (lo<=g[s]<=hi): v+=1
    print(f"  {'signature scenario exempt, -15 to +20':38} {v} violations of {len(rows)*len(SCN)} cells")
    # policy 3: judged on sustained only
    v=sum(1 for _,_,g in rows if not (-5<=g['patchwerk']<=5))
    print(f"  {'judged on patchwerk alone':38} {v} violations of {len(rows)} pairs")
