import json, re
"""
RULE: a talent `reads` a category only if its effect would automatically extend to a
NEW member of that category. That is the only thing a tag conversion can exploit.

  "Your Fire spells cannot be pushed back"  -> reads fire.  A converted Frostbolt gains it.
  "Fireball applies a burn stack"           -> reads nothing. It names one spell.
  "Your bleeds ignore armor"                -> reads bleed.
  "Rend ignores armor"                      -> reads nothing.

So generic plurals and category words count; named abilities do not.
"""
GENERIC = {
 "fire":   r"\byour Fire\b|\bFire spells?\b|\bFire damage\b|\bfire damage over time\b",
 "frost":  r"\byour Frost\b|\bFrost spells?\b|\bFrost damage\b|\bChill effects?\b",
 "arcane": r"\byour Arcane\b|\bArcane spells?\b|\bArcane damage\b",
 "shadow": r"\byour Shadow\b|\bShadow spells?\b|\bshadow damage\b",
 "holy":   r"\byour Holy\b|\bHoly spells?\b|\bholy damage\b",
 "nature": r"\byour Nature\b|\bNature spells?\b|\bnature damage\b",
 "bleed":  r"\byour bleeds?\b|\bbleeding\b|\bbleed effects?\b|\ball bleeds\b",
 "poison": r"\byour poisons?\b|\bpoisons\b(?! Improved)",
 "curse":  r"\byour curses?\b|\bcurses\b",
 "disease":r"\byour diseases?\b|\bdiseases\b",
 "periodic":r"\bperiodic\b|\bdamage over time effects?\b|\bheals? over time\b|\byour damage-over-time\b",
 "melee":  r"\byour melee attacks?\b|\bmelee attacks?\b(?! stops)|\byour attacks\b",
 "ranged": r"\byour ranged attacks?\b|\branged attacks?\b",
 "spell":  r"\byour spells\b|\ball spells\b|\byour casts\b|\byour damage spells\b|\byour healing spells\b",
 "heal":   r"\byour heals?\b(?! Touch)|\byour healing\b|\bheals? you cast\b|\bany heal\b",
 "absorb": r"\byour shields?\b|\babsorbs?\b|\bshield value\b",
 "threat": r"\bthreat you generate\b|\byour threat\b|\ball threat\b",
 "pet":    r"\byour pet's\b|\byour demon's\b|\byour minions?\b|\byour Risen\b",
 "totem":  r"\byour totems?\b|\btotems you\b|\bbuff totems\b",
 "trap":   r"\byour traps?\b|\btraps\b",
 "stealth":r"\bstealth\b|\bProwl\b",
 "physical":r"\byour physical\b|\bphysical damage\b",
}
D=json.load(open("/mnt/user-data/outputs/rebuilt-trees.json"))
prop=0; total=0
for t in D["trees"]:
    for r in t["rows"]:
        for x in r["talents"]:
            total+=1
            txt=x["name"]+". "+x["text"]
            reads=sorted(k for k,p in GENERIC.items() if re.search(p,txt))
            x["reads"]=reads
            if reads: prop+=1
json.dump(D,open("/mnt/user-data/outputs/rebuilt-trees.json","w"),indent=1,ensure_ascii=False)
print(f"talents: {total} | proposed a category for: {prop} ({100*prop//total}%) | read nothing: {total-prop}")
from collections import Counter
c=Counter(k for t in D["trees"] for r in t["rows"] for x in r["talents"] for k in x["reads"])
print("\ncategory frequency:")
for k,v in c.most_common(): print(f"  {k:10} {v}")
