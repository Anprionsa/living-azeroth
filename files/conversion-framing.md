# Tag Conversion: Better Framing

**August 2026**

*Replaces the two open questions at the end of `tag-conversion.md`. The first was posed wrongly. The second has three answers and needs a choice.*

---

## 1. The additive question was wrong

I asked whether conversions need a downside, on the reasoning that a purely additive talent is always correct to take and therefore not a choice.

Vanilla refutes this directly. **Shadow Mastery increases Shadow damage by 10% and has no downside whatsoever. Ruin increases critical damage by 100% and has no downside whatsoever.** They are the two most purely additive talents in the game, and between them they produce SM/Ruin and DS/Ruin, which are the only two named builds vanilla has.

Nobody has ever complained that Shadow Mastery is not a choice, because that was never where the choice was. **The choice is whether to spend thirty points in Affliction to reach it.**

So a conversion does not need an internal cost. It needs to be expensive to reach.

## 2. Which means placement is the whole design

If "Frostbolt counts as Fire" sits in the Frost tree, a frost mage passes gate 20 in Frost on the way to their capstone and collects it for free. Then the objection is correct and the talent is not a choice.

**Put it in the tree it converts toward, and the cost appears by itself.**

"Frostbolt counts as Fire" belongs in the Fire tree at gate 20. Now a frost mage has to spend twenty-one points in Fire to get it, which means going 30/21 instead of 31/20, which means **giving up Ice Barrier**. That is a real decision, it produces a hybrid by construction, and no artificial downside was needed.

The rule: **a conversion lives in the destination tree, never the source.** It is the destination tree's offer to abilities it did not previously recognise.

## 3. Five worked examples

Each is one node at gate 20 in the destination tree. The cost in every case is the source tree's capstone, because 31/20 does not reach gate 20 in a second tree and 30/21 does.

**Mage. Frostfire.** In the Fire tree: your Frostbolt counts as a Fire spell as well as Frost.
Build is 30 Frost / 21 Fire. You give up Ice Barrier. You gain Ignite, Critical Mass, Fire Power, and Master of Elements all reading your Frostbolt, which is the spell you cast a hundred times a fight. That is a rotation that plays differently rather than a rotation that hits harder.

**Warrior. Bloodwhirl.** In the Arms tree: your Bloodthirst and Whirlwind count as bleeds for the purposes of your Arms talents.
Build is 30 Fury / 21 Arms. You give up Bloodthirst's capstone slot, and in exchange Bloodletting, Deep Wounds, and Rupture Line all apply to a Fury rotation that previously had no bleed content at all. Fury becomes a bleed spec without ceasing to be Fury.

**Rogue. Bleedvenom.** In the Assassination tree: your bleeds count as poisons.
Build is 30 Combat / 21 Assassination. You give up Adrenaline Rush. Rupture and Garrote start reading Improved Poisons, Vile Poisons, and Envenom, so a Combat rogue's finisher becomes a poison delivery system.

**Druid. Thornmoon.** In the Feral tree: your Moonfire and Insect Swarm count as bleeds.
Build is 30 Balance / 21 Feral. You give up Moonkin Form. Bloodletting and Rend and Tear apply to a caster's periodic damage, and the druid's two halves finally share a category.

**Shaman. Stormcaller.** In the Elemental tree: your weapon imbues count as spells.
Build is 30 Enhancement / 21 Elemental. You give up Stormstrike. Windfury and Flametongue start reading Elemental's spell talents, and Clearcasting begins proccing off melee.

In all five the sacrifice is the capstone and the gain is that an entire tree's worth of existing talents starts noticing what you already do. That is a much larger effect per node than any sideways talent written so far, from one point of investment more.

## 4. The placement question, with three real options

Gate 20 currently holds a sideways node in every rebuilt tree. If it also holds a conversion, something has to give.

**Option A. The conversion replaces the sideways node.**
Cleanest and most defensible. They do the same job and the conversion does it better: a sideways node crosses one specific effect, a conversion crosses everything the destination tree can read. Gate 20 stays at eight points.
Cost: rewriting the gate-20 tier of all 27 rebuilt trees, and the sideways nodes were the answer to REG-03 so this reopens that.

**Option B. Conversion at gate 20, sideways node drops to gate 15.**
Preserves both. Gate 15 costs sixteen points, so a light splash gets the surgical crossing and a committed splash gets the broad one, which is a sensible escalation.
Cost: the sideways nodes were designed as the hybrid seat's signature, and demoting them to a tier reachable by 31/16/4 makes them incidental.

**Option C. Both at gate 20, tier grows to ten or eleven points.**
Smallest edit. Gate 20 becomes the heaviest tier in the tree, which inverts REG-18's finding that vanilla starves it.
Cost: a ten-point gate 20 in a 58-point tree means seventeen percent of the tree sits in one tier, and a splasher taking both spends most of their twenty-one points there. That is close to gate 20 being the only reason to splash, which is not obviously bad and is definitely a different design.

**My read is A**, on the grounds that two mechanisms doing one job is worse than one doing it well, and that the sideways nodes exist because conversion had not been thought of yet. But it is the most expensive option and it undoes finished work, so it should be your call rather than mine.

## 5. What is still genuinely open

**Whether nine conversions is too many.** One per class is symmetrical and symmetry has been the wrong instinct twice in this project already. Mage and warrior have obvious ones. Hunter's is thin, as noted before. It may be that four or five classes have a real conversion and the rest do not, which is the same conclusion the fifth-tree question reached.

**Whether a conversion can be reversed.** If Frostbolt counts as Fire, does it stop counting as Frost? Section 3 says it counts as both, which is additive in the way section 1 argues is fine. A version where it counts as Fire instead would be a subtraction node and a different, harder talent. Both are buildable and they are not the same talent.

**Whether the sim collapses it.** Nine conversions across nine classes is nine new optimal builds for a simulator to find, and if one conversion is clearly best per class then the outcome is nine new mandatory splashes rather than nine new choices. That is the same risk named in talent design 5.3 and it is now larger.

---

## 6. Should it be A everywhere, or A in some places

No, and the reason is not taste.

A conversion is only worth its slot if the destination tree actually has content that reads the new category. That is measurable, so it was measured: for each proposed conversion, how much of the destination tree references the category the conversion would create.

| Conversion | Destination | Share of that tree reading it |
|---|---|---|
| traps count as ranged attacks | Marksmanship | 84% |
| Frostbolt counts as Fire | Fire | 82% |
| weapon imbue counts as a spell | Elemental | 71% |
| Holy spells count as Shadow | Shadow | 64% |
| Shadow Bolt counts as periodic | Affliction | 63% |
| Seal damage counts as melee | Retribution | 42% |
| bleeds count as poisons | Assassination | 21% |
| Moonfire counts as a bleed | Feral Combat | 20% |
| Bloodthirst and Whirlwind count as bleeds | Arms | 10% |

That table contradicts my own ranking in three places. Hunter came out highest and I had called it thin. Warrior came out lowest and I had called it strong.

### 6.1 The table measures the wrong trees

Every number above is computed against **vanilla** talent data, because that is the only version of the 27 trees that exists as data. The rebuilds exist as prose.

That matters enormously, and Hunter is the clearest case. Marksmanship scores 84% because most of its vanilla tree references ranged weapons, and most of those references are flat nodes: Lethal Shots, Mortal Shots, Ranged Weapon Specialization. **Section 7 deleted every one of them into the depth dividend.** What remains in rebuilt Marksmanship is Steady Aim, Ranger's Cadence, and Ranger's Focus, all of which are about Auto Shot timing and Aimed Shot, and none of which a trap would sensibly benefit from. Post-rebuild, Hunter's conversion is close to worthless.

Warrior moves the other way. Vanilla Arms holds six points of bleed content; rebuilt Arms holds Bloodletting, Deep Wounds, and Rupture Line, which is more, though still not much.

Reasoning about the rebuilt versions instead:

**Clear yes.** Mage and Shaman. Fire's behavioural content is Ignite, Master of Elements, Improved Scorch, and Combustion, all of which a converted Frostbolt genuinely triggers. Elemental's is Clearcasting, overload, and Elemental Devastation, all of which a converted weapon imbue genuinely triggers.

**Arguable.** Warlock, Rogue, Druid, Paladin. Real interactions exist but each lights up two or three talents rather than a tree.

**No.** Priest, Hunter, Warrior. Priest's categories do not cross naturally, since two of its three trees are healing. Hunter's collapses once the flat nodes are gone. Warrior's was thin to begin with.

### 6.2 So the answer

**Option A where a conversion earns the slot, and the existing sideways node stays where it does not.** Two classes clearly, four arguably, three not at all.

That is not inconsistency for its own sake. Gate 20 remains the crossing point in every tree, and what sits there is whichever mechanism the class can support. A player learns one rule, that gate 20 is where trees meet, and the specific talent varies as every talent does.

**And this is the third time symmetry has been the wrong instinct in this project**, after one absorbed tree per class and one second tree per host. The pattern is consistent enough to be worth stating as a habit: propose per class, then check which classes actually support it, and expect roughly half to fail.

### 6.3 The blocker underneath all of this

The decision above cannot be made properly yet, because **the 27 rebuilt trees exist only as prose.**

Every measurement in this project runs against `talents-classified.json`, which is vanilla. The rebuilds changed what talents exist, what categories they read, and which nodes are behaviour rather than numbers, and none of that is queryable. The table in section 6 is the second time that has produced a misleading answer, after the classifier review.

Until the rebuilds are structured the same way vanilla is, every question of this kind gets answered against a version of the game the rework has already replaced.

---

## 7. Measured properly, and the answer changed again

The `reads` field is now authored across all 454 talents in `rebuilt-trees.json`, under one rule:

> A talent reads a category only if its effect would automatically extend to a **new member** of that category. That is the only thing a tag conversion can exploit.
>
> "Your Fire spells cannot be pushed back" reads fire. "Fireball applies a burn stack" reads nothing, because it names one spell.

**Only 143 of 454 talents read any category at all.** The other 311 name specific abilities.

That number is the finding. **The rebuilds made talents more specific, which makes tag conversion less useful than when the idea was proposed.** Section 5.2's whole method was replacing "increases Fireball damage by 5%" with a discrete effect on a named ability, and a named ability is exactly what a conversion cannot reach. The hygiene work that made conversion *safe*, by deleting the multipliers, also made it *thin*, by pointing what remained at specific spells.

Measured against the authored field:

| Class | Conversion | Destination reads it | Verdict |
|---|---|---|---|
| Mage | Frostbolt counts as Fire | 12 nodes, 58% | **STRONG** |
| Warlock | Shadow Bolt counts as periodic | 4 nodes, 27% | **STRONG** |
| Priest | Holy spells count as Shadow | 6 nodes, 26% | **STRONG** |
| Druid | Moonfire counts as a bleed | 2 nodes, 14% | moderate |
| Rogue | bleeds count as poisons | 1 node, 10% | weak |
| Warrior | Bloodthirst counts as a bleed | 1 node, 6% | weak |
| Shaman | weapon imbue counts as a spell | 1 node, 5% | weak |
| Paladin | Seal damage counts as melee | 1 node, 3% | weak |
| Hunter | traps count as ranged attacks | 1 node, 1% | weak |

**Three classes, not nine.** Mage, Warlock, Priest.

### 7.1 Every previous ranking was wrong, including the reasoned one

This is the third answer to the same question and the first one with evidence behind it.

Vanilla data said Hunter highest at 84%. Rebuilt data with keyword matching said Hunter 94%. Both were artefacts. Authored data says Hunter catches exactly one talent, Sure Shot, worth one point.

More uncomfortably, my reasoned correction in section 6 was also wrong. It called **Shaman a clear yes** and Shaman turns out to catch one node worth three points, because rebuilt Elemental talks about Lightning Bolt and Chain Lightning by name rather than about spells as a class. It called **Priest a no** and Priest is one of the three strongest, because rebuilt Shadow genuinely does read shadow as a category through Shadow Weaving, Mind Melt, Shadow Embrace, and Shadowform.

Reasoning about a system this size is not a substitute for measuring it, and I made that mistake after arguing the opposite.

### 7.2 What to build

**Mage.** Frostbolt counting as Fire lights up Impact, Ignite, Burning Soul, Master of Elements, Critical Mass, Combustion, and more, at 58% of the destination tree. This is the case the whole idea was built on and it survives contact. Build it.

**Warlock.** Shadow Bolt counting as a periodic effect catches Suppression, Curse Mastery, Shadow Embrace, and Unstable Affliction. It also fixes the one-way chain into Destruction found in `partial-builds.md`. Build it.

**Priest.** Holy spells counting as Shadow for stacking catches six nodes including Shadowform and Vampiric Embrace. Worth building, and it is the one that most needs a subtraction framing, since a holy priest building shadow stacks they cannot spend is a trap rather than a build.

**The other six.** Leave the gate-20 sideways node where it is. It does the job that a conversion cannot do in those trees, precisely because those trees talk about abilities rather than categories.

### 7.3 So Option A applies to three classes

The placement question from section 4 resolves. Option A, conversion replacing the sideways node at gate 20, applies to Mage, Warlock, and Priest. The remaining twenty-four trees keep what they have.

Three rewrites rather than twenty-seven, which makes this the cheapest of the three options rather than the most expensive, and it became so only after the data existed to narrow it.
