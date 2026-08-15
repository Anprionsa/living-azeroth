# Two Candidate Trees: Dreamer and Radiance

**August 2026**

*Worked up for a decision. Both are built to the finished rule set. Neither is in `trees.json` yet. The priest tree is a second draft; the first, a melee zealot, is discarded in 2.1 for reading as a paladin.*

---

## 0. What changed in the druid concept, and why

The first version was that a druid exists in two places, with a dream-self persisting where you were. On reflection that is astral projection rather than the Emerald Dream, and worse, it overlaps Chronomancer: delayed resolution and a second version of a thing are already that tree's territory.

The Emerald Dream is not a copy of you. **It is a copy of the world**, concurrent rather than past, showing Azeroth as it would be unspoiled. So the mechanic should be territorial, not personal.

And vanilla hands you the image directly. There are four portals to the Dream in the game, at Twilight Grove in Duskwood, Seradane in the Hinterlands, Dream Bough in Feralas, and Bough Shadow in Ashenvale. **All four are inactive.** You can walk to a door, kill the corrupted dragon guarding it, loot an object that quests to Keeper Remulos and turns out to be Malfurion's ring, be told he is inside fighting the Nightmare, and never open the door.

The tree is about learning to open one.

---

## 1. Dreamer (Druid)

**Fantasy.** The druid who does not visit the Dream but brings a piece of it here.

**Local mechanic: Threshold.** You plant a piece of the Dream on the ground. It is large, it persists, and only one may exist at a time. Inside it the world behaves as it does in the Dream: wounds close on their own, corruption is visible, and things that are not truly there lose their hold. The tree is about what happens inside your Threshold and what it costs to hold one.

The Nightmare is the same mechanic inverted. Talents let you plant the corrupted version instead, which weakens what stands in it rather than strengthening it.

**The shape.** Support and zone control, not trinity. Your own output is modest and your value is what happens to everyone standing in your ground. That is the augmentation shape, which Conduit already establishes as legitimate, and it is the only role druid does not already fill.

**Why it does not duplicate.** Balance is a ranged caster, Restoration is a direct healer, Feral is both melee and tank. None of them is territorial. Chronomancer is time; this is place. The two never touch.

**Verb: dreamt.** The ninth verb and the only passive one. You go into a Barrow Den, you sleep, and you do not wake for a long time. Nobody teaches you and nobody grants it. Moonglade and Keeper Remulos are the frame, and Naralex in Wailing Caverns is the cautionary version: a druid who did exactly this and woke into the Nightmare instead.

**Anchors.** Moonglade, Duskwood, Ashenvale, Feralas, the Hinterlands, and Wailing Caverns in the Barrens.

**Permanent cost.** You never fully wake. Sleep and fear effects that would be resisted take hold instead, and effects that break on damage do not break for you.

### The tree

**Gate 0, 10.** *Threshold* (1), the mechanic itself. *Rooted Ground* (5): allies in your Threshold regenerate, then their heals over time tick faster, then their bleeds do not, then they cannot be dazed, then leaving carries the regeneration for 6 seconds. *Verdance* (4): your Threshold grows over time, then heals what plants itself in it, then spreads along your Entangling Roots, then survives your death for 20 seconds.

**Gate 5, 12.** *Nightmare* (1): you may plant the corrupted version instead. *Dread* (5): enemies in a Nightmare are slowed, then heal for less, then their casts are pushed back, then they cannot regain stealth, then they suffer their own damage over time twice as fast. *Wakefulness* (6): you may move your Threshold rather than replanting, then it follows you slowly, then moving it does not interrupt you, then two may exist briefly during a move, then moving costs no mana, then it snaps to an ally instead.

**Gate 10, 9.** *Lucid* (1): you see through the Dream, revealing stealth and invisibility inside your Threshold. *Communion* (5): allies in your Threshold share a portion of your spell power, then your critical strikes, then your armor, then one of your active buffs, then your Nature's Swiftness. *Overgrowth* (3): your Threshold's edge damages enemies crossing it.

**Gate 15, 10.** *Emerald Vigor* (1): a stationary ally in your Threshold for 5 seconds gains an absorb. *Terror* (5): Nightmare talents that escalate fear into a genuine control tool with graded fallbacks for immune targets. *Tending* (4): your Threshold is not destroyed by area damage, then cannot be dispelled, then persists through your death fully, then refreshes when an ally dies in it.

**Gate 20, 8, the mark.** *Grove of Ysera* (1): your Threshold heals for a portion of all damage dealt inside it, to anyone. *Dreamwalk* (3), cross-tree: your Rejuvenation and Regrowth land at full effect anywhere inside your Threshold regardless of range; Moonfire refreshes on enemies standing in a Nightmare. Every druid has all three. *Wildseed* (2), cross-tree: your Feral forms gain your Threshold's regeneration and cannot be rooted inside it. *Deep Slumber* (2), subtraction: your Threshold is permanent and cannot be moved or destroyed. You may not leave it.

**Gate 25, 8.** *The Waking World* (5): your Threshold's effects apply at half strength to everyone in the raid, then at full strength to your party, then it applies both the Dream and the Nightmare at once to the correct targets, then allies who die inside it are resurrected weakened once per fight, then it doubles in size.

**Gate 31, 1.** *Open the Way* (1). Your Threshold becomes a portal for 20 seconds. Allies may step through, and while inside they are untargetable, healed, and cleansed, returning where they entered. You cannot enter it yourself.

**58 points, gate 20 at eight, no flat nodes, 44 of 58 referencing Threshold.**

### Risks

**Totem overlap.** A planted thing that affects an area is what a shaman does. The differences are that a Threshold is one large transformation of ground rather than four small emitters, that it affects enemies as well as allies, and that it is contested rather than incidental. That is defensible and it is also the first thing a critic will say.

**Zone control in raids is awkward** because encounters move. Wakefulness at gate 5 exists to answer that and it costs six points to solve a problem the mechanic creates, which is a real tax.

**Open the Way is enormous** and is the first thing to cut, in the same way Rewind is for Chronomancer.

---

## 2. Radiance (Priest), replacing the Zealot

### 2.1 Why the first version failed

The Zealot was close-range holy damage with self-sustain that scaled off being hurt. That is Retribution paladin, and the separations offered for it, cloth instead of plate and no blessings, are cosmetic. A priest doing melee holy damage reads as a paladin with worse armour no matter what the talents say.

It also sat too near Discipline in flavour space. Discipline is already the Light used as force rather than comfort, and two trees competing for that register is worse than one.

### 2.2 The heretical Light, and the spell vanilla already wrote

A better frame is the Light as something the Church would forbid, mirroring Shadow rather than duplicating a paladin.

Shadow's structural signature is Vampiric Embrace: **the priest deals damage and their allies are healed by it.** One act, two effects, in a direction the Light supposedly owns. Shadow is generous, which is the joke.

The mirror is the direction nobody built. **The priest heals, and the healing burns.** Not two spells, one. You cannot comfort without harming, and that is the heresy: the Church teaches that the Light soothes, and this tree knows it also sears, because it is the same act seen from two sides.

Vanilla wrote the spell and then buried it. **Holy Nova damages enemies and heals allies simultaneously**, it sits in the Holy tree, it is famously weak, and nobody takes it. The fantasy has existed in the game since launch as a single bad spell with nothing built around it. That is the project's method exactly: something the game already asserts and never develops.

### 2.3 The tree

**Local mechanic: Corona.** Your healing spells emit outward and damage what stands near their target. Your damaging spells emit outward and heal what stands near theirs. Nothing you cast affects only one thing. Talents govern what the emission carries and how far it reaches.

**The shape.** Not a healer and not a caster. Both, at once, each at reduced efficiency alone, competitive because they happen in the same global cooldown. Your positioning is the skill, because everything you do lands on two sets of people at the same time.

**Why it does not read as Discipline.** Discipline prevents damage before it arrives. Radiance prevents nothing and cannot shield. It heals what is already hurt and burns what caused it, in one motion. Opposite methods for opposite moments.

**Why it does not read as a paladin.** No melee, no plate, no blessings, no judgement, and paladins never heal and damage in the same cast. Retribution is a melee damage spec with a heal attached. This is a caster whose healing and damage are the same number applied twice.

**Why it does not read as Shadow.** It is the inversion, deliberately, and the two are mutually exclusive in exactly the way Shadowform already establishes.

**Verb: recanted.** You publicly renounced the doctrine and the Light did not leave you. The chain is a trial rather than a lesson, and the proof is that you were not abandoned. That is the only acquisition on the list where the character is tested and nothing is taken away, which is what makes it heresy rather than corruption.

**Anchors.** Tirisfal Glades, Western and Eastern Plaguelands, Stratholme, and the Scarlet Monastery Cathedral and Library.

**Permanent cost.** You can no longer cast Power Word: Shield or any absorb. You do not prevent, and the Church's chief mercy is closed to you.

### 2.4 The tree

**Gate 0, 10.** *Corona* (1), the mechanic. *Effulgence* (5): the emission reaches further, then it cannot be resisted, then it ignores line of sight, then it prefers wounded allies and healthy enemies, then it strikes a second ring at half effect. *Kindling* (4): your heals build a stack; at five your next emission doubles; stacks persist through target changes; overhealing builds two.

**Gate 5, 12.** *Searing Mercy* (5): the damage half of your emission scales with how much healing the cast did, then with overhealing specifically, then it applies your Holy Fire's burn, then it cannot be reflected, then it refreshes on the enemy taking further damage. *Sanctuary* (4): the healing half of your emission scales with damage done, then reaches your whole party, then heals for the excess when an enemy dies inside it, then cleanses one effect. *Holy Nova* (3): rebuilt from vanilla's dead spell into the tree's rotational core rather than a curiosity.

**Gate 10, 9.** *Revelation* (1): brand a target; your emissions centre on the brand rather than on your cast. *Doctrine* (5): your emission may be aimed, then split between two points, then held for one global cooldown and released, then centred on an ally rather than yourself, then centred on a corpse. *Unbroken* (3): your casts cannot be pushed back while any ally is below 50% health.

**Gate 15, 10.** *Conflagrant Grace* (1): for 10 seconds your healing lands at full value on allies and full damage on enemies with no falloff. *Zealotry* (5): critical heals critically damage; the reverse also holds; a critical emission builds two Kindling; criticals cannot be resisted; a critical on a branded target resets Revelation. *Penitence* (4): healing yourself damages what is attacking you.

**Gate 20, 8, the mark.** *Communion* (1): your emissions from any source now also emit from every ally you healed in the last 3 seconds. *Divine Fury* (3), cross-tree: Smite and Holy Fire carry a full emission; Renew's ticks each emit at reduced value. Every priest has all three. *Shadow's Mirror* (2), cross-tree: Shadow Word: Pain's ticks emit healing; Mind Blast emits at full value. *Apostasy* (2), subtraction: your emissions double in size and effect. You may no longer target allies with any spell, so all of your healing is emission and none of it is aimed.

**Gate 25, 8.** *The Unquiet Light* (5): your emission persists on the ground for 3 seconds, then follows the branded target, then leaves a trail as you move, then triggers again when the brand expires, then applies to everything your party heals as well.

**Gate 31, 1.** *Absolution* (1). For 12 seconds every point of healing you do is dealt again as holy damage to every enemy in range, and every point of damage you deal is healed again to every ally in range, with no falloff and no cap on targets. Three minute cooldown.

**58 points, gate 20 at eight, no flat nodes, 47 of 58 referencing Corona.**

### 2.5 Risks

**Emission is an area effect on every cast**, which means it breaks crowd control constantly. That is a real raid problem in vanilla, where sheep and sap hold pulls together, and it needs either a suppression toggle or an accepted reputation for being disruptive. Possibly both, and the second is more interesting.

**Both halves at reduced efficiency is the classic bad hybrid.** The spec only works if doing both in one global cooldown beats doing either alone, and that is a tuning knife edge rather than a design guarantee.

**Losing Power Word: Shield is severe.** It is the priest's signature and arguably the best spell in vanilla. Removing it is what makes the tree heretical rather than decorative, and it is also the single most likely thing to make the spec unplayable.

**Apostasy at gate 20 may be the whole spec rather than an option.** A subtraction node that removes targeted healing entirely is close to a second capstone, and if it turns out to be mandatory then it is not a choice, it is the design.

## 3. How they compare

| | Dreamer | Radiance |
|---|---|---|
| Fantasy vanilla asserts and never shows | four inactive Dream portals, Malfurion inside | Holy Nova, a heal and a strike in one cast, dead since launch |
| Mechanic | Threshold, territorial | Corona, every cast emits both ways |
| Shape | support and zone control | healer and caster simultaneously, neither alone |
| Nearest existing thing | shaman totems | Shadow's Vampiric Embrace, inverted |
| Distance from it | large; one big contested area, affects enemies | it is the deliberate mirror, and mutually exclusive by design |
| Reads as another class | no | no; no melee, no plate, no blessings, no absorbs |
| Fills a shape the host lacks | yes, druid has no support role | yes, priest has no spec that does two things at once |
| Biggest risk | zone control in moving encounters | breaks crowd control on every cast |
| Verb | dreamt | recanted |

**If only one gets built, it is the Dreamer**, because the four inactive portals are the single clearest case in the entire suite of vanilla asserting something and refusing to show it, and because druid is the only class with no support shape while priest at least has two casters.

**If the concern is mechanical risk, it is the Dreamer as well**, which is a change from the first draft. Corona emitting on every cast makes Radiance the more disruptive of the two in an actual raid, because it breaks crowd control constantly and vanilla pulls depend on sheep and sap holding. Threshold's problem is that encounters move, which is solvable with points. Radiance's problem is social.

---

## 4. Tested against the other 35 trees

Both were built into `trees.json` and measured with the same code that produced the vanilla audit and the absorbed audit. Thirty-seven trees compared.

| Tree | Points | Flat share | Forced flat to capstone | Gate 20 | Mechanic coverage |
|---|---|---|---|---|---|
| **Dreamer** | 58 | 0% | 0 / 30 | 8 | **100%** |
| **Radiance** | 58 | 0% | 0 / 30 | 8 | 84% |
| Chronomancer | 58 | 0% | 0 / 30 | 8 | 79% |
| Blackguard | 58 | 50% | 5 / 30 | 6 | 37% |
| Necromancy | 58 | 43% | 5 / 30 | 6 | 20% |
| Bladedancer | 64 | 45% | 7 / 30 | 6 | 20% |
| Mage Fire, best vanilla | 46 | 50% | 8 / 30 | 4 | none |
| Conduit | 58 | 50% | 9 / 30 | 6 | 51% |
| Metamorphosis | 58 | 65% | 11 / 30 | 6 | 0% |
| Shaman Enhancement, worst vanilla | 52 | 94% | 28 / 30 | 6 | none |

The three trees written to the finished rule set are the only three at zero percent flat, and they lead on every measure. That is expected rather than impressive: they were written after the rules and the others were not.

### 4.1 The finding worth acting on: concentration risk

Dreamer measures 100% mechanic coverage. Every talent in the tree references Threshold or Nightmare.

The REG-27 check was written as a floor, because Metamorphosis declared a mechanic and contained none of it. Applied as a floor, 100% looks like a perfect score. It is not, and the reason is specific.

**A tree at 100% coverage has no fallback.** If Threshold turns out not to work, nothing in the tree works. Not a portion of it, all of it. Compare Blackguard at 37% or Conduit at 51%, where a player who dislikes the mechanic still finds usable talents and where a tuning failure in the mechanic leaves most of the tree standing.

That matters most for Dreamer specifically, because Threshold is also the riskiest mechanic proposed anywhere in the suite. Zone control breaks when encounters move, and vanilla encounters move. **The tree with the highest concentration is built on the mechanic most likely to fail**, which is the worst possible pairing of those two properties.

Radiance at 84% has the same shape with a milder failure mode, since Corona does not depend on a planted object holding position.

One thing softens this. Both mechanics are single-point nodes at gate 0, so a player splashing 21 or 26 points gets the mechanic with their first point and every subsequent talent works. Partial investment is still legitimate, which is what Class Absorption's fluid trees argument requires. The risk is not to splashers, it is to the tree as a whole if the mechanic is bad.

**So REG-27 needs restating as a band rather than a floor.** Roughly 40 to 80 percent looks right on this evidence: enough that the tree is about its own subject, not so much that the subject is the only thing in it. Metamorphosis at 0% is broken. Dreamer at 100% is brittle. Conduit at 51% is the model and always was.

### 4.2 What that changes

Dreamer should shed some concentration deliberately. The candidates are the talents that are already only loosely territorial: Communion at gate 10 sharing your stats with allies, Lucid revealing stealth, and Terror's fear content could all be rewritten to work without a Threshold planted, which would bring coverage to roughly 70% and give the tree a floor to stand on if the mechanic tunes badly.

That is a real edit rather than a cosmetic one, and it is worth doing before either tree is committed to.

### 4.3 Revised recommendation

The earlier draft recommended Dreamer on both fantasy strength and mechanical risk. The second half of that no longer holds.

**Fantasy: Dreamer, clearly.** Four inactive doors with Malfurion behind them is unmatched anywhere in the suite.

**Risk: Radiance.** Its failure mode is social, that it breaks crowd control, which is a tuning and etiquette problem. Dreamer's failure mode is structural, that a moving encounter voids a mechanic the whole tree depends on.

If both ship, Dreamer needs the 4.2 edit first. If one ships, the choice is genuinely between the better story and the safer build, and this document cannot make that call for you.

---

## 5. Second round of testing

Three checks that had not been run on anything: capstone reachability, row distribution, and overlap against every other tree in the suite.

### 5.1 Reachability, clean

To buy at a gate you need that many points already spent below it. Across all 37 trees, **no gate is unreachable.** The bug that shipped in the first draft of Class Absorption's Section 9, where trees offered under thirty points in rows one through six and made every capstone impossible, does not exist anywhere now.

### 5.2 The original seven share a row template

| Tree | g0 | g5 | g10 | g15 | g20 | g25 | g31 |
|---|---|---|---|---|---|---|---|
| Blackguard | 13 | 11 | 10 | 9 | 6 | 8 | 1 |
| Necromancy | 13 | 11 | 10 | 9 | 6 | 8 | 1 |
| Metamorphosis | 13 | 11 | 10 | 9 | 6 | 8 | 1 |
| Conduit | 13 | 11 | 10 | 9 | 6 | 8 | 1 |
| Survival | 13 | 11 | 10 | 9 | 6 | 8 | 1 |
| Bladedancer | 13 | 11 | 10 | 9 | 6 | 14 | 1 |
| Runeblade | 13 | 13 | 10 | 9 | 6 | 8 | 1 |
| Chronomancer | 10 | 12 | 9 | 10 | 8 | 8 | 1 |
| Dreamer | 10 | 12 | 9 | 10 | 8 | 8 | 1 |
| Radiance | 10 | 12 | 9 | 10 | 8 | 8 | 1 |

Five of the original seven are byte-identical in shape, and the other two differ in one row each. Vanilla's trees vary enormously by comparison, from three points at gate 20 in Feral to sixteen in Combat rogue.

**A row shape repeated seven times is a template, not a design.** It is also the specific shape REG-18 identifies as the most common structural fault in the game: front-loaded, declining to a starved gate 20. The absorbed trees inherited the fault by construction rather than by accident.

The three newer trees are flatter, with a spread of four points between their heaviest and lightest rows against seven or eight for the originals. That is a better shape and it should become the target when the seven are revised per `absorbed-revisions.md`.

### 5.3 Overlap, and the one result that matters

Each tree was given a fingerprint across twelve systems, healing, damage, absorb, threat, resource, mobility, control, pet, stealth, area, periodic, and death, then compared against every other tree.

**Radiance scores 0.97 against vanilla Holy priest.** That is the highest similarity between any two trees in the suite, and it lands on precisely the concern raised about this tree: that it must be distinct from what the priest already has.

Two things need saying about it, in order.

**First, the metric cannot see the distinguishing feature.** It measures which systems a tree touches, not how. Radiance and vanilla Holy both touch healing, damage, and area, so they fingerprint alike. What separates them is that Radiance does all three in one cast and cannot do otherwise, which no fingerprint of this kind will ever detect. A 0.97 here is a warning rather than a verdict.

**Second, and more usefully, the overlap has already been removed by other work.** The comparison is against *vanilla* Holy priest. Section 15 of the talent document rebuilds that tree and deletes exactly the content that creates the overlap: Divine Fury, Holy Reach, and Searing Light, nine points of Smite and Holy Fire improvements, on the grounds that a raid healer's tree should not be paying for damage spells. Rebuilt Holy is healing only.

So the two pieces of work happen to fit. The Holy rebuild cleared the damage content out of the priest's healing tree, and Radiance is the tree that picks it up and makes it a thesis instead of a footnote. That was not planned and it is the strongest argument yet that Radiance belongs to this class.

**Dreamer's nearest neighbour is Chronomancer at 0.80**, which is lower than any of Radiance's top five, and no shaman tree appears in its top five at all. That partly clears the totem-overlap objection raised in section 1: whatever else is true of Threshold, it does not occupy the same system space as Restoration or Enhancement shaman.

### 5.4 Splash reachability

Every tree in the file, old and new, puts 84 to 85 percent of its points at gate 20 or below, so gates 25 and 31 hold roughly nine points between them. Deep investment buys a capstone and very little volume.

That is defensible, since a capstone is meant to be qualitative rather than large, and the uniformity across ten trees suggests it is deliberate. It does mean the marginal value of points 26 through 31 rests entirely on the capstone being good, which is a heavier load than it looks.

### 5.5 Where this leaves the two

Nothing in this round changes the fantasy case. Dreamer still has the better story.

Radiance gained ground on risk. Its worst measured result, the 0.97 against Holy, dissolves once you notice the Holy rebuild already removed the overlapping content, and the two pieces of work turn out to reinforce each other. Dreamer's concentration problem from section 4.1 is unaddressed and still needs the edit.

**On the evidence so far, Radiance is the safer build and Dreamer is the better idea**, which is the same conclusion as section 4.3 arrived at by a different route.
