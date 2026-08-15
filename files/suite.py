#!/usr/bin/env python3
"""Full suite. Every pair, every scenario, all three instruments, with confidence
intervals rather than point estimates."""
import importlib, statistics, math, json, sys
import sim, tank, heal
for m in (sim,tank,heal): importlib.reload(m)

N=int(sys.argv[1]) if len(sys.argv)>1 else 200
def ci(vals):
    m=statistics.mean(vals); se=statistics.pstdev(vals)/math.sqrt(len(vals))
    return m, 1.96*se

def compare(runner, cls, A, B, **kw):
    a=[runner(cls,A,seed=s,**kw)[0] if not isinstance(runner(cls,A,seed=1,**kw),dict) else runner(cls,A,seed=s,**kw) for s in range(1,N+1)]
    return a

CORE=[("Warrior","warrior-arms-rebuilt","warrior-fury-rebuilt"),
 ("Warrior","warrior-fury-rebuilt","warrior-protection-rebuilt"),
 ("Rogue","rogue-combat-rebuilt","rogue-assassination-rebuilt"),
 ("Rogue","rogue-assassination-rebuilt","rogue-subtlety-rebuilt"),
 ("Mage","mage-fire-rebuilt","mage-frost-rebuilt"),
 ("Mage","mage-arcane-rebuilt","mage-fire-rebuilt"),
 ("Warlock","warlock-affliction-rebuilt","warlock-destruction-rebuilt"),
 ("Warlock","warlock-destruction-rebuilt","warlock-demonology-rebuilt"),
 ("Priest","priest-shadow-rebuilt","priest-discipline-rebuilt"),
 ("Shaman","shaman-elemental-rebuilt","shaman-enhancement-rebuilt"),
 ("Druid","druid-balance-rebuilt","druid-feral-combat-rebuilt"),
 ("Paladin","paladin-retribution-rebuilt","paladin-holy-rebuilt"),
 ("Hunter","hunter-marksmanship-rebuilt","hunter-beast-mastery-rebuilt")]
EXP=[("Paladin","blackguard","paladin-retribution-rebuilt"),
 ("Mage","necromancy","mage-frost-rebuilt"),
 ("Warlock","metamorphosis","warlock-destruction-rebuilt"),
 ("Rogue","bladedancer","rogue-combat-rebuilt"),
 ("Shaman","conduit","shaman-elemental-rebuilt"),
 ("Warrior","runeblade","warrior-arms-rebuilt"),
 ("Hunter","survival","hunter-marksmanship-rebuilt")]
SCN=["patchwerk","burst","movement","cleave","switching"]

def dmg_pair(cls,a,b,scn):
    r1=[sim.run(cls,[(a,31),(b,20)],seed=s,scenario=scn)[0] for s in range(1,N+1)]
    r2=[sim.run(cls,[(a,30),(b,21)],seed=s,scenario=scn)[0] for s in range(1,N+1)]
    m1,h1=ci(r1); m2,h2=ci(r2)
    gap=100*(m1-m2)/m2 if m2 else 0
    sig=abs(m1-m2) > (h1+h2)
    return m1,m2,gap,sig

if __name__=="__main__":
    print(f"FULL SUITE, {N} seeds per cell, 95% confidence\n")
    print("="*78)
    print("1. CORE, capstone shape against mid-tree shape, by scenario")
    print("="*78)
    print(f"  {'pair':32}" + "".join(f"{s[:9]:>10}" for s in SCN))
    allg={s:[] for s in SCN}
    for cls,a,b in CORE:
        row=[]
        for scn in SCN:
            m1,m2,gap,sig=dmg_pair(cls,a,b,scn)
            if sig: allg[scn].append(gap)
            row.append(f"{gap:+.1f}%"+("*" if sig else " "))
        nm=f"{cls} {a.split('-',1)[1].replace('-rebuilt','')[:9]}+{b.split('-',1)[1].replace('-rebuilt','')[:9]}"
        print(f"  {nm[:32]:32}" + "".join(f"{c:>10}" for c in row))
    print()
    for scn in SCN:
        g=allg[scn]
        if g: print(f"  {scn:11} n={len(g):2}  mean {statistics.mean(g):+5.1f}%  median {statistics.median(g):+5.1f}%  within 5%: {sum(1 for x in g if abs(x)<=5)}/{len(g)}")

    print()
    print("="*78)
    print("2. EXPANDED, new tree against its class's best core build")
    print("="*78)
    BEST={"Paladin":("paladin-retribution-rebuilt","paladin-holy-rebuilt"),
     "Mage":("mage-fire-rebuilt","mage-frost-rebuilt"),"Warlock":("warlock-affliction-rebuilt","warlock-destruction-rebuilt"),
     "Rogue":("rogue-combat-rebuilt","rogue-assassination-rebuilt"),"Shaman":("shaman-elemental-rebuilt","shaman-enhancement-rebuilt"),
     "Warrior":("warrior-arms-rebuilt","warrior-fury-rebuilt"),"Hunter":("hunter-marksmanship-rebuilt","hunter-beast-mastery-rebuilt")}
    print(f"  {'tree':16}" + "".join(f"{s[:9]:>10}" for s in SCN))
    vs={s:[] for s in SCN}
    for cls,a,b in EXP:
        ca,cb=BEST[cls]; row=[]
        for scn in SCN:
            m1,h1=ci([sim.run(cls,[(a,31),(b,20)],seed=s,scenario=scn)[0] for s in range(1,N+1)])
            mc,hc=ci([sim.run(cls,[(ca,31),(cb,20)],seed=s,scenario=scn)[0] for s in range(1,N+1)])
            g=100*(m1-mc)/mc; vs[scn].append(g)
            row.append(f"{g:+.1f}%"+("*" if abs(m1-mc)>(h1+hc) else " "))
        print(f"  {a:16}" + "".join(f"{c:>10}" for c in row))
    print()
    for scn in SCN:
        g=vs[scn]
        print(f"  {scn:11} mean {statistics.mean(g):+5.1f}%  median {statistics.median(g):+5.1f}%  within 10%: {sum(1 for x in g if abs(x)<=10)}/{len(g)}")

    print()
    print("="*78)
    print("3. TANKING")
    print("="*78)
    print(f"  {'build':26} {'TPS':>6} {'DTPS':>6} {'EHP':>7} {'critImm':>8}  gap")
    for cls,a,b in [("Warrior","warrior-protection-rebuilt","warrior-fury-rebuilt"),
                    ("Paladin","paladin-protection-rebuilt","paladin-retribution-rebuilt"),
                    ("Druid","druid-feral-combat-rebuilt","druid-restoration-rebuilt")]:
        res={}
        for lbl,pa,pb in (("31/20",31,20),("30/21",30,21)):
            r=[tank.run_tank(cls,[(a,pa),(b,pb)],seed=s) for s in range(1,max(30,N//4))]
            res[lbl]=(statistics.mean(x["tps"] for x in r), statistics.mean(x["dtps"] for x in r),
                      statistics.mean(x["ehp"] for x in r), r[0]["critImmune"])
        for lbl in ("31/20","30/21"):
            t_,d_,e_,c_=res[lbl]
            g=f"{100*(res['31/20'][0]-res['30/21'][0])/res['30/21'][0]:+.1f}%" if lbl=="31/20" else ""
            print(f"  {cls+' '+lbl:26} {t_:6.0f} {d_:6.0f} {e_:7.0f} {str(c_):>8}  {g}")

    print()
    print("="*78)
    print("4. HEALING, three damage patterns")
    print("="*78)
    for pat in ("steady","spiky","aoe"):
        print(f"  {pat}")
        for cls,a,b in [("Priest","priest-holy-rebuilt","priest-discipline-rebuilt"),
                        ("Druid","druid-restoration-rebuilt","druid-balance-rebuilt"),
                        ("Shaman","shaman-restoration-rebuilt","shaman-elemental-rebuilt"),
                        ("Paladin","paladin-holy-rebuilt","paladin-protection-rebuilt")]:
            o={}
            for lbl,pa,pb in (("31/20",31,20),("30/21",30,21)):
                r=[heal.run_heal(cls,[(a,pa),(b,pb)],pattern=pat,seed=s) for s in range(1,max(20,N//6))]
                o[lbl]=(statistics.mean(x["hps"] for x in r), statistics.mean(x["hpm"] for x in r),
                        statistics.mean(x["overheal"] for x in r))
            gh=100*(o["31/20"][0]-o["30/21"][0])/o["30/21"][0]
            gm=100*(o["31/20"][1]-o["30/21"][1])/o["30/21"][1]
            print(f"    {cls:8} HPS {o['31/20'][0]:4.0f} ({gh:+5.1f}%)   HPM {o['31/20'][1]:5.2f} ({gm:+6.1f}%)   overheal {o['31/20'][2]*100:3.0f}%")
