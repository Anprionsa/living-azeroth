#!/usr/bin/env python3
"""Compare the reworked trees against real Naxxramas logs.

The control is downloaded, not simulated, exactly as sim-baseline-protocol.md section 2
specified. Source: Warcraft Tavern's Phase 6 Anniversary rankings, January 2026, derived
from Warcraft Logs Classic Fresh Naxxramas.

The comparison that matters is SPREAD, not absolute numbers. The sim's gear blocks are
invented, so its absolute output means nothing; what can be compared is how far apart the
specs sit, which is the thing the rework claims to change.
"""
import json, importlib, statistics, sys
sys.path.insert(0,"/home/claude")
import sim

# Warcraft Tavern, Phase 6 Naxxramas, Anniversary realms. January 2026.
CONTROL={
 "Warrior DPS":1411, "Rogue DPS":1151, "Mage Fire":1019, "Warlock DPS":887,
 "Hunter Marksmanship":856, "Druid Feral":839, "Shaman Enhancement":687,
 "Shaman Elemental":675, "Priest Shadow":596, "Paladin Retribution":524,
 "Druid Balance":503, "Mage Frost":446,
}
# the reworked build closest to each logged spec
MAP={
 "Warrior DPS":("Warrior",[("warrior-arms-rebuilt",31),("warrior-fury-rebuilt",20)]),
 "Rogue DPS":("Rogue",[("rogue-combat-rebuilt",31),("rogue-assassination-rebuilt",20)]),
 "Mage Fire":("Mage",[("mage-fire-rebuilt",31),("mage-frost-rebuilt",20)]),
 "Warlock DPS":("Warlock",[("warlock-destruction-rebuilt",31),("warlock-demonology-rebuilt",20)]),
 "Hunter Marksmanship":("Hunter",[("hunter-marksmanship-rebuilt",31),("hunter-beast-mastery-rebuilt",20)]),
 "Druid Feral":("Druid",[("druid-feral-combat-rebuilt",31),("druid-balance-rebuilt",20)]),
 "Shaman Enhancement":("Shaman",[("shaman-enhancement-rebuilt",31),("shaman-elemental-rebuilt",20)]),
 "Shaman Elemental":("Shaman",[("shaman-elemental-rebuilt",31),("shaman-enhancement-rebuilt",20)]),
 "Priest Shadow":("Priest",[("priest-shadow-rebuilt",31),("priest-discipline-rebuilt",20)]),
 "Paladin Retribution":("Paladin",[("paladin-retribution-rebuilt",31),("paladin-protection-rebuilt",20)]),
 "Druid Balance":("Druid",[("druid-balance-rebuilt",31),("druid-feral-combat-rebuilt",20)]),
 "Mage Frost":("Mage",[("mage-frost-rebuilt",31),("mage-fire-rebuilt",20)]),
}
def measure(n=30, scenario="patchwerk"):
    importlib.reload(sim)
    out={}
    for k,(cls,build) in MAP.items():
        out[k]=statistics.mean([sim.run(cls,build,seed=s,scenario=scenario)[0] for s in range(1,n+1)])
    return out

def spread(d):
    v=list(d.values()); top=max(v)
    return {k: 100.0*x/top for k,x in d.items()}

if __name__=="__main__":
    got=measure()
    cs, ss = spread(CONTROL), spread(got)
    print(f"{'spec':22} {'logged':>7} {'log %':>7} {'sim':>7} {'sim %':>7} {'gap':>7}")
    gaps=[]
    for k in CONTROL:
        g=ss[k]-cs[k]; gaps.append((k,g))
        print(f"  {k:22} {CONTROL[k]:7} {cs[k]:6.1f}% {got[k]:7.0f} {ss[k]:6.1f}% {g:+6.1f}")
    print()
    cv=list(cs.values()); sv=list(ss.values())
    print(f"  logged spread, top to bottom : {max(cv)-min(cv):.1f} points")
    print(f"  sim spread,    top to bottom : {max(sv)-min(sv):.1f} points")
    print(f"  logged stdev {statistics.pstdev(cv):.1f}  sim stdev {statistics.pstdev(sv):.1f}")
