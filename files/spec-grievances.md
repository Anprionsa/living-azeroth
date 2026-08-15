# Spec Grievances: Why People Are Annoyed, With Numbers

**Version 1.0 | August 2026**

*Companion to classic-plus-talent-design.md. Documents the complaints that actually exist about vanilla specs, separates the ones the talent rework can fix from the ones it cannot, and attaches a computed number to each where one applies. Classes in alphabetical order.*

---

## 1. The measure

The obvious way to audit a tree is to count how many of its points buy numbers. That is useful but soft, because a player never takes a whole tree. They take a path through it.

A harder measure is available and it needs no opinion about builds.

To own a talent gated at 30 points you must first spend 30 points in that tree. Which 30 is partly your choice, but the tree constrains it: at any moment you can only buy talents whose gate you have already passed. So there is a floor. Take every behavior talent the moment it becomes available, fill with flat only when nothing else is legal, and count. That number is the minimum filler the tree forces on you to reach its capstone. No build, no preference, no argument.

Run across all 27 trees, the result:

| Forced flat, of the 30 points to a capstone | Trees |
|---|---|
| 23 to 28 | Enhancement, Demonology, Feral Combat, Retribution, Marksmanship, Protection paladin, Discipline, Elemental |
| 15 to 20 | Holy priest, Balance, Beast Mastery, Survival, Restoration shaman, Affliction, Fury, Holy paladin, Combat, Frost, Assassination, Subtlety, Destruction, Protection warrior |
| 8 to 14 | Arcane, Restoration druid, Arms, Shadow, Fire |

Enhancement shaman and Demonology warlock tie at the extreme. Twenty-eight of the thirty points on the way to either capstone must buy a number. Best case, across the entire climb, two points buy behavior.

The correlation with reputation holds. Specs with poor reputations average 22.7 forced flat points. Specs with good reputations average 14.4.

**These figures were revised after a hand review of the classifier.** The first pass was validated on Warrior Arms only and was wrong in 25 places across the 27 trees, in both directions. Section 13 records what changed and why, because two of the corrections moved conclusions rather than decimal places.

It is a correlation, not a law, and the exceptions are the useful part.

## 2. Two different failure modes

The floor separates two complaints that get voiced identically and need opposite fixes.

**Structurally boring.** The tree forces you to spend your climb on numbers. Retribution, Marksmanship, Feral, Demonology. A player here is bored on the way up and has no build to speak of when they arrive. This is what the talent rework fixes, and it fixes it completely.

**Numerically weak.** The spec does not put out enough. Shadow priest sits at 11 forced flat, which is among the best figures in the game, and still has a poor reputation. Its tree is fine. Its problem is output, mana, and in vanilla the debuff slot competition. Elemental shaman is similar.

The rework does nothing for the second category, and pretending otherwise is how a design document loses credibility. A spec that is weak needs tuning or a role, not more interesting talents. Where both apply, fix the tree and tune separately, and do not let one claim credit for the other.

**A limit on the floor, found while auditing Rogue.** The floor measures what a tree forces, not what a spec sheet forces. A tree can offer behavior talents at every gate and still see every player take the flat ones, because the flat ones are simply stronger. Rogue is the case: Combat's floor is 11 of 30, among the best in the game, while real vanilla rogue builds are stacked with Malice, Lethality, Precision, Lightning Reflexes, and Deflection, all pure numbers, taken freely.

So the floor is a lower bound on filler, not a prediction of builds. A low floor means the tree permits an interesting path. It does not mean anyone walks it. Where the floor is low and the builds are flat anyway, the fix is not restructuring the tree, it is making the behavior talents worth taking.

**Third mode, which neither fixes: valued for what you give other people.** Several specs hold raid slots for an aura or a totem rather than for anything they do. Their logged output understates their value and any rebalance driven by personal numbers will overcorrect them. This is a composition problem, not a talent problem, and it should be flagged before tuning rather than discovered after.

---

## 3. Druid

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Balance | 52 | 77% | 19 / 30 | 11 / 20 |
| Feral Combat | 45 | 84% | 26 / 30 | 19 / 20 |
| Restoration | 53 | 66% | 13 / 30 | 4 / 20 |

Feral Combat is the third worst tree in the game by forced filler, and the row 5 figure is worse than the capstone figure in a way nothing else matches. Seventeen of the first twenty points must buy numbers. A feral druid splashing twenty points, which is the single most common thing a druid does with a second tree, spends 85% of that investment on modifiers.

**The complaint that shows up everywhere: all three specs are valued for what they hand other people.** Balance is brought for the Moonkin spell crit aura. Feral cat is brought for Leader of the Pack, a 3% melee crit buff to the group. Restoration brings innervate and battle resurrection. The personal output in every case is acknowledged as below the class that specialises in that role.

**Restoration's main tree is locked and the choice lives in the off-tree.** Guides state this outright: the Restoration points are essentially set with little room for personal choice, while the spare Balance points are open. That is exactly backwards from how a talent system should feel. The tree you care about is a checklist, and your only real decision is what to do with the leftovers.

That complaint is not visible in the flat share. Restoration's 13 of 30 is one of the better figures in the game. The tree is not full of filler, it is full of talents so obviously mandatory that there is no decision. Worth recording as its own failure mode: **no filler, no choice either.**

**Feral DPS depends on power-shifting.** The standard rotation involves shifting out of and back into cat form to trigger Furor's energy, which is a technique the interface does not teach and the tooltips do not describe. It is effectively a community-discovered exploit that became mandatory. A spec whose optimal play is undocumented is a design failure regardless of its numbers.

**Balance runs out of mana.** Named repeatedly alongside Feral and Elemental shaman as the specs whose abilities cost more than their damage justifies.

What the rework fixes: Feral Combat's forced filler, decisively, and the same for Balance. What it does not fix: mana economy, the aura-slot problem, or Restoration's mandatory-talent problem, which needs talents that trade against each other rather than talents that are merely more interesting.

---

## 4. Hunter

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Beast Mastery | 48 | 62% | 18 / 30 | 11 / 20 |
| Marksmanship | 52 | 87% | 23 / 30 | 14 / 20 |
| Survival | 48 | 73% | 18 / 30 | 9 / 20 |

Marksmanship is the flattest tree in the game at 87%. Forty-five of its fifty-two points buy a number.

This matters more than the raw figure suggests, because Marksmanship is not an option. It is the raid spec. Guides state that most guilds expect a 20/31/0 or similar Marksmanship build, that Beast Mastery loses Trueshot Aura and therefore hurts the whole party, and that Survival is the worst of the three and should not be played if you want to be optimal.

So the hunter's situation is the sharpest case in the document. The class has three trees. One is mandatory for raiding, and it is the flattest tree in the game. The other two are the interesting ones and taking them costs your raid slot. That is a worse outcome than having one tree.

**Hunters fall off as gear scales.** Competitive in Molten Core and Onyxia at low gear levels, then out-scaled by warriors, rogues, mages, and warlocks in later phases. An optimised late raid brings one to three, largely for Tranquilizing Shot and pet pulling.

That is a numerical problem, not a tree problem, and it is the clearest example in the document of why the two need separating. Fixing Marksmanship's 87% would make hunters much more interesting to play and would not move their position on a Naxxramas damage ranking by a single place.

**Utility slot.** The reason to bring one is Trueshot Aura and Tranquilizing Shot. Personal damage is not the argument. Same third failure mode as druid, and the same warning applies to any rebalance driven by logged output.

**Class-level irritants outside the trees.** The dead zone, the range band where a hunter can neither shoot nor melee, with no tool to escape it. Mana drain from aspect management. Hunter-specific itemization being thin. Aimed Shot timing against the auto shot swing, where slower weapons are preferred purely because they give more forgiving windows.

None of those are talent problems and none of them are in scope, but they belong in the record, because a hunter reading a talent proposal that ignores the dead zone will not believe the author plays the class.

---

## 5. Mage

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Arcane | 47 | 64% | 14 / 30 | 5 / 20 |
| Fire | 46 | 50% | 8 / 30 | 2 / 20 |
| Frost | 46 | 65% | 15 / 30 | 11 / 20 |

Mage has the healthiest trees in the game. Fire's 8 of 30 is the second lowest forced filler anywhere, and both Arcane and Fire let you reach row 5 having spent only two points on numbers.

And mage gameplay is the most repetitive in the game. Frost is described in its own guides as one of the simplest rotations available, which is to say spam Frostbolt.

That combination is the single most useful data point in this document, because it falsifies the tidy version of the argument. Good trees do not produce good gameplay. The talent rework in Section 5 of the design document is necessary and it is nowhere near sufficient, and any claim that fixing talents fixes how a class feels to play is refuted by the class with the best talents.

What actually constrains mage is elsewhere. The spell book is three damage spells. The resource model is a mana bar and an eight minute Evocation. Neither is a talent problem.

**Spec choice is dictated by boss immunity, not preference.** Frost is mandatory for Molten Core and Blackwing Lair because most bosses there carry fire immunity or heavy fire resistance. A fire mage in those raids is not a build choice being outperformed, it is a build choice that does nothing. Combined with vanilla's escalating respec cost, this is a tax on playing the tree you like.

This is worth carrying into the Classic+ discussion because it is fixable without touching talents. Immunity as a wall is a blunt instrument, and resistance as a curve would let a fire mage be worse in Molten Core rather than absent from it.

**One genuine trade-off already exists here and should be noticed.** The Winter's Chill variant of the frost build improves the whole frost mage group's damage at the cost of roughly 5 to 10% of the mage's own. That is a subtraction talent in everything but name, it shipped in vanilla, and it is a second precedent alongside Shadowform for Section 5.4. Worth citing, because it is a trade of personal output for group output rather than a trade of one personal stat for another.

---

## 6. Paladin

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Holy | 45 | 67% | 16 / 30 | 7 / 20 |
| Protection | 50 | 84% | 23 / 30 | 19 / 20 |
| Retribution | 45 | 84% | 24 / 30 | 14 / 20 |

Retribution is the second worst tree in the game by forced filler and the second flattest overall. Twenty-four of the thirty points to its capstone must buy a number.

The complaint is not subtle and it is not new. There are threads on Blizzard's own Classic forums titled around Retribution having no viable DPS option and around Protection and Retribution both being non-viable in PvE. Community diagnosis is that the vanilla paladin has one real raid role, which is healing.

**The rotation problem is worse than the tree problem, and the two are connected in a way that is genuinely bleak.** Guides describe Retribution as relying on auto attacks and passive procs for the bulk of its damage, and then justify that emptiness on the grounds that it leaves the paladin free to distribute blessings. The spec has nothing to press because its actual job is buff maintenance.

So the tree is 84% numbers and the rotation is deliberately empty, and each is defended by pointing at the other. That is the clearest case in the document of a spec that needs both fixes at once, and fixing only the tree would leave a paladin with interesting talents and still nothing to do.

**Protection generates threat by buffing.** Tanking guides state that Greater Blessing of Kings is the source of roughly 95% of a protection paladin's raid threat, cast on party members rather than at the boss. The same guides note that the One-Handed Weapon Specialization talent in the tree is useless because paladin melee damage is never relied on for threat.

That is a talent sitting in a tank tree that is dead on arrival for tanks. It is the most concrete single example anywhere in this audit of a node that exists to occupy a slot.

**Faction lock.** Paladin is Alliance-only in vanilla, so every paladin complaint is invisible to half the playerbase. The Class Absorption document already assumes paladin for Horde and shaman for Alliance, and that assumption matters here too: a Retribution rework only reaches the whole game if the class does.

What the rework fixes: Retribution's and Protection's forced filler. What it does not fix: threat generation, the empty rotation, or the fact that a tank's primary threat button is a raid buff.

---

## 7. Priest

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Discipline | 48 | 83% | 23 / 30 | 14 / 20 |
| Holy | 48 | 77% | 20 / 30 | 11 / 20 |
| Shadow | 48 | 56% | 11 / 30 | 4 / 20 |

Priest is the cleanest demonstration in the document that the two failure modes are separate, because it has one tree of each.

**Holy is structurally boring and its talents buff spells nobody casts.** Twenty-three of thirty forced flat, fifth worst in the game. But the sharper complaint is older and more specific. A vanilla-era forum post puts it directly: the holy tree is mostly worthless, a heavily Discipline specced priest heals more efficiently, and in Molten Core you are not casting Greater Heal, Heal, or Prayer of Healing, so every talent that buffs them is wasted.

That is a failure mode the floor cannot see. The talents are not merely flat, they are flat modifiers to spells the encounter design has made irrelevant. Vanilla raid healing ran on efficiency and downranked fast heals, and the Holy tree was built for a different game.

It is worth noticing that the tree the period complaint recommends instead, Discipline, also has the better floor: 18 against 23. Not proof of anything, but the two measures agree.

**Shadow is numerically weak with a perfectly good tree.** Eleven of thirty forced flat, among the best figures anywhere, and Shadow still cannot hold a raid slot in vanilla. Its problems are output, mana, and in the original debuff-limited game, competition for slots. Period advice was blunt: level as Shadow, respec Holy at 60, and expect groups to take a dim view of standing in Shadowform and doing damage.

The rework will make Holy interesting. It will do nothing whatsoever for Shadow, and Shadow is the spec people actually want to play. Anyone reading a talent proposal as a fix for Shadow priest should be told plainly that it is not one.

**Shadow's raid value, where it exists, is Vampiric Embrace.** Healing the raid as a side effect of doing damage, which lets other healers relax. Third failure mode again, and the same warning about tuning from logged personal output.

---

## 8. Rogue

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Assassination | 46 | 67% | 15 / 30 | 14 / 20 |
| Combat | 62 | 74% | 16 / 30 | 16 / 20 |
| Subtlety | 47 | 66% | 15 / 30 | 11 / 20 |

Rogue has no tree in the worst third and Assassination at 67% is on the better side of average. It is also the class people complain about least.

The original version of this section claimed rogue had the least flat tree in the game and among the lowest floors anywhere. Both figures moved on review, Combat from 11 to 16 and Assassination from 9 to 15, so the claim is softened rather than withdrawn. Rogue is comfortably healthy, not exceptional.

Combat's 62 available points is the largest tree in the game, which matters for a reason unrelated to flatness: more points available against the same 51 to spend means more left on the table, which is the slack that makes a tree feel like a choice rather than a checklist. Compare Retribution and Holy paladin at 45.

**And yet real rogue builds are stacked with numbers.** Period builds show Malice 5/5, Lethality 5/5, Precision 5/5, Lightning Reflexes 5/5, Deflection 5/5, Improved Sinister Strike, Improved Eviscerate. That is the discovery recorded in Section 2: the tree permits an interesting path and nobody takes it, because the flat talents are stronger.

Rogue is therefore the strongest argument for the depth dividend specifically rather than for the rework generally. Restructuring Combat would not change these builds. Removing the flat talents as purchasable nodes and returning their value as a curve would, because it makes the interesting path the only path, at identical power.

**The narrower complaints.** Subtlety is a PvP tree with no raid application, so a third of the class's talent content is invisible to raiders. Weapon choice is heavily constrained: swords dominate, reinforced on Alliance by the Human sword skill racial, which means the weapon specialization nodes function as a race tax rather than a build choice.

**No real utility.** A rogue brings damage. That makes rogues clean to tune and gives them nothing to fall back on when their damage is not needed, which is the flip side of the third failure mode rather than an escape from it.

---

## 9. Shaman

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Elemental | 46 | 83% | 23 / 30 | 14 / 20 |
| Enhancement | 52 | 94% | 28 / 30 | 19 / 20 |
| Restoration | 52 | 75% | 18 / 30 | 12 / 20 |

Enhancement is now tied for the worst tree in the game at 28 of 30, and at 94% flat it is the flattest tree anywhere by a clear margin. Nineteen of the first twenty points must buy numbers, which means an Enhancement splash is almost pure filler. Elemental at 23 is not much better.

The first version of this document put all three shaman trees in the middle band and said nothing here was catastrophic. That was a classifier error, corrected in Section 13. The revised picture matches the complaint far better than the original did: shaman players say the class has no role of its own, and it turns out the trees have very little in them either.

**Every tree is valued for what it gives the group.** Windfury Totem is stated outright as the reason Enhancement holds raid spots, with raids bringing roughly one shaman per five-man group. Guides describe the class as the toolbox's toolbox, acknowledging in the same breath that shamans do not put out the biggest damage or the biggest heals. That is the third failure mode in its purest form, and shaman is the class where it defines all three specs at once rather than one.

The community shorthand is totem bot, and the arguments about it are worth reading because both sides are right. One position: it is not engaging to exist so that other people parse well. The other: reading what the group needs, weaving Earthbind for a runner, dropping Tremor before a fear lands, and reassessing which air totem is correct is real decision-making. The disagreement is not about whether shamans make decisions. It is about whether decisions that only show up on someone else's meter feel like playing.

**Totem management is an interface problem masquerading as a class problem.** Vanilla has no totem bar. Each totem is dropped individually, they do not move with you, and long-duration group buffs have to be recast every time the raid advances. A period suggestion that keeps recurring is simply letting buff totems follow the shaman. None of that is a talent problem, and a talent rework that ignores it will not change how the class feels for a single player.

**Horde only in vanilla,** the mirror of paladin. Same caveat about the Class Absorption assumption applies.

What the rework fixes: the middle-band filler, modestly. What it does not fix: the role problem, which is the actual complaint, and which needs the class to have something that is its own rather than everyone else's.

---

## 10. Warlock

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Affliction | 49 | 73% | 18 / 30 | 9 / 20 |
| Demonology | 52 | 85% | 28 / 30 | 19 / 20 |
| Destruction | 53 | 70% | 15 / 30 | 7 / 20 |

Demonology is the worst tree in the game and it is not close. Twenty-six of the thirty points to its capstone must buy a number. Across the entire climb, four points can buy behavior.

Look at what fills it: Improved Imp, Fel Intellect, Improved Voidwalker, Fel Stamina, Improved Succubus, Unholy Power, Improved Enslave Demon, Improved Firestone, Improved Spellstone, Improved Healthstone, Improved Health Funnel. Eleven nodes, every one of them a percentage applied to a pet or a consumable.

**And then the punchline.** Nobody specs deep Demonology in vanilla. The two canonical raid builds are SM/Ruin and DS/Ruin, and DS/Ruin takes exactly 21 points in Demonology to reach Demonic Sacrifice at gate 20, a talent that kills your demon in exchange for a damage buff.

The demon tree's most-used talent deletes the demon. That is the single best example in this audit of a tree that failed at its own premise, and it needs no interpretation to land.

**Warlock also validates the row 5 argument better than anything else in the game.** Both canonical builds are a row 5 talent plus a deep tree:

- SM/Ruin: 30 in Affliction for Shadow Mastery at gate 25, 21 in Destruction for Ruin at gate 20.
- DS/Ruin: 21 in Demonology for Demonic Sacrifice at gate 20, 30 in Destruction.

That is Section 5.3's hybrid seat, shipped in 2004, on the one class that has two competing viable raid builds instead of one. The design document argues that vanilla never put anything at row 5 worth crossing for. Warlock is the exception, and the exception has the build diversity to show for it.

That is worth promoting from a footnote to the main argument. The claim is no longer "this would probably work." It is "this worked, once, and the class it worked on is the one with two specs."

---

## 11. Warrior

| Tree | Available | Flat share | Forced flat to capstone | Forced flat to row 5 |
|---|---|---|---|---|
| Arms | 59 | 61% | 12 / 30 | 12 / 20 |
| Fury | 60 | 78% | 18 / 30 | 11 / 20 |
| Protection | 53 | 70% | 15 / 30 | 8 / 20 |

Protection sits at 15 of 30, mid-table. An earlier version of this document had it at 7, the lowest in the game, and drew a conclusion from the fact that the mandatory raid tank spec also had the healthiest tree. That was a classifier error and the conclusion is withdrawn. Section 13 has the detail.

What survives is narrower and still worth noting: no warrior tree is in the bad half, and the class that dominates vanilla has no tree above 18.

Warrior also has the two largest trees after Combat rogue, at 59 and 60 available points against Retribution and Holy paladin's 45. More slack, more left on the table, more that feels like a choice.

**The complaints are about gear, not talents.** Warriors are rage-starved and weak in poor gear, and scale harder than anything else as gear improves, which is why hunters are competitive in Molten Core and irrelevant by Naxxramas. The practical consequence is guilds funnelling weapons to warriors, which is a loot politics problem that no talent change touches.

**The tanking monopoly.** Vanilla raid tanking is warriors. Feral druids and protection paladins can off-tank, and the paladin threat model described in Section 6 shows how far from viable the alternative actually is. That is a problem about the other classes, not about warriors, and it is worth recording here because a Classic+ conversation about tank diversity starts by admitting the monopoly exists.

**Arms is a PvP tree.** Twelve of thirty forced flat is a good figure, and the tree is largely irrelevant to raiding except as the 17 points a Fury warrior spends to reach Impale. Section 6 of the design document rebuilds Arms specifically because it is the tree this project has audited most closely, not because it is the most broken one. Fury at 18 and Demonology at 26 both have stronger claims on the first rebuild.

---

## 12. Summary

Ranked by forced filler on the way to a capstone, worst first:

| Rank | Tree | Forced flat | Failure mode |
|---|---|---|---|
| 1 | Shaman Enhancement | 28 / 30 | structural, and 94% flat overall |
| 1 | Warlock Demonology | 28 / 30 | structural, and the tree fails its own premise |
| 3 | Druid Feral Combat | 26 / 30 | structural |
| 4 | Paladin Retribution | 24 / 30 | structural plus empty rotation |
| 5 | Hunter Marksmanship | 23 / 30 | structural, and it is the mandatory raid spec |
| 5 | Paladin Protection | 23 / 30 | structural |
| 5 | Priest Discipline | 23 / 30 | structural |
| 5 | Shaman Elemental | 23 / 30 | structural plus numerically weak |
| ... | middle band, 13 to 20 | | mixed |
| 26 | Priest Shadow | 11 / 30 | numerically weak, tree is healthy |
| 27 | Mage Fire | 8 / 30 | none, but the rotation is one button |

Four things this audit established that the design document did not know when it was written.

The floor is a lower bound, not a prediction. Rogue proves a healthy tree can still produce flat builds when the flat talents are simply stronger.

Good trees do not produce good gameplay. Mage proves it. The rework is necessary and not sufficient, and the document should say so in its own voice rather than waiting to be told.

Some talents are dead rather than boring. Paladin's One-Handed Weapon Specialization in a tank tree, and every Holy priest talent that buffs a spell raids do not cast. Those need deleting, not rewriting.

Row 5 already worked once. Warlock's two canonical builds are both a row 5 talent plus a deep tree, and warlock is the class with two viable raid specs. That moves Section 5.3 from proposal to precedent.


---

## 13. Classifier review record

The floor figures in this document were revised after a hand review of every tree. The first pass was validated against Warrior Arms only, where it matched an independent audit exactly, and that turned out not to generalise.

Twenty-five corrections across 27 trees, twenty-three moving a node to flat and two to behavior. Two systematic errors caused nearly all of them.

**Triggered numbers were being read as new effects.** Flurry, on both shaman and warrior, increases attack speed after a critical strike. The trigger is new, the effect is a percentage. Same for Anticipation, Precision, Iron Will, Improved Disarm, Brutal Impact, and Permafrost. The rule now applied: flat if the entire effect is a numeric modifier to something that already exists, however it is triggered.

**Compound descriptions were being read as behavior on the word "and".** Monster Slaying increases damage and increases critical damage. Vile Poisons increases poison damage and increases dispel resistance. Two numbers is still two numbers.

Left alone after review: Improved Starfire and Mace Specialization, where the second clause is a stun that did not previously exist. Holy Shield and Shield Specialization, an active ability and a rage interaction respectively. Trueshot Aura is a genuinely ambiguous case, an active whose entire effect is a flat stat handed to other people, and it is kept flat because that ambiguity is exactly the point made about it in the design document.

**What moved conclusions rather than decimals:**

- Enhancement shaman went from 18 to 28 and is now tied for worst. It had been described here as unremarkable.
- Protection warrior went from 7 to 15 and is no longer the healthiest tree in the game. A conclusion drawn from that has been withdrawn.
- Holy priest went from 23 to 20 and left the worst five.
- The rebuild order changed. Holy priest is out, Enhancement shaman is in at the top.
- The reputation correlation weakened from 20.4 against 10.6 to 22.7 against 14.4. Still present, less dramatic.

**What survived unchanged:** Demonology, Feral Combat, Retribution, and Marksmanship all stayed in the worst five. Mage Fire stayed the healthiest tree at 8. Priest Shadow stayed at 11, so the numerically-weak-with-a-healthy-tree finding holds. Arms stayed at 12, so it remains the wrong tree to have rebuilt first.

---

## Appendix: Provenance

Labels as defined in `classic-plus-talent-design.md`.

| Element | Provenance | Detail |
|---|---|---|
| The forced-flat floor measure | **Original** | Greedy walk of a tree preferring behavior at every gate, counting what flat spend remains unavoidable. No known prior application to vanilla trees. |
| Client-accurate tree data for all 27 trees | **Taken**, maladr0it/classic-talent-calculator | Parsed from `src/trees/*/data.ts`. Validated against an independent hand audit of Arms and against the 17-point Impale gate behind the canonical Fury build. |
| Flat versus behavior classification | **Derived here** | Heuristic on description text. Validated on Arms only, where it matches a hand audit exactly. Expect low single-digit errors per tree elsewhere. |
| The three failure modes | **Derived here** | Structurally boring, numerically weak, and valued for what you give others. Fell out of the floor data disagreeing with reputation on Shadow priest and Enhancement shaman. |
| The floor is a lower bound, not a prediction | **Derived here** | Found while auditing Rogue, whose healthy trees produce flat builds anyway. |
| Good trees do not produce good gameplay | **Derived here** | Found while auditing Mage. |
| Talents that are dead rather than boring | **Derived here**, grounded in community sources | A protection paladin tanking guide on One-Handed Weapon Specialization, and a vanilla-era priest post on the Holy tree buffing spells raids do not cast. Neither framed it as a category. |
| Per-class grievances | **Taken**, community sources | Class guides, Blizzard forum threads, and period forum posts, cited inline per class. The document contributes the sorting, not the complaints. |