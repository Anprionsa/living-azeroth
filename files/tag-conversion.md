# Tag Conversion: The Diablo Lesson We Did Not Take

**August 2026**

*A correction to Section 3 of the talent document, and the most likely fix for the one-way wiring found in `partial-builds.md`.*

---

## 1. We took the hygiene and left the engine

Section 3 of the talent document takes three things from Lord of Hatred: separation of concerns, deletion of flat nodes, and the three-transformative-plus-four-adjustment ratio.

All three are hygiene. They make a tree cleaner. **Not one of them produces a build.**

The thing that actually generates build variety in Diablo 4 is the mechanism we noted in passing and never used. From the same source material: skill variants can change a skill's elemental and mechanical tags outright, and the Paragon board reacts to those tags directly, so a frost-converted Hydra stops benefiting from Fire damage nodes and starts benefiting from Frost ones. The variants exist specifically so that converting a tag makes a different set of existing effects apply.

**That is the engine.** A build in Diablo is not a set of chosen nodes, it is a declared set of tags and everything in the game that reads those tags. Choosing to convert one thing rewires what a dozen other things do.

Vanilla has the tags already and never converts them.

## 2. Vanilla is full of tags and no talent moves anything between them

Vanilla talents reference tags constantly. Shadow Mastery increases Shadow damage. Fire Power increases Fire damage. Piercing Ice increases Frost damage. Talents reference bleeds, poisons, curses, diseases, melee attacks, ranged attacks, spells, and periodic effects.

Every one of those is a category with talents pointing at it. **No talent in vanilla moves an ability from one category to another.** Frostbolt is Frost forever. Rend is a bleed forever. There is no conversion, so the categories never interact and half your class's talents are permanently irrelevant to the other half.

That is why two trees of the same class rarely combine into anything. Not because the talents are weak, but because a Fire talent has no way to notice a Frost spell exists.

## 3. What conversion looks like in vanilla's own vocabulary

One conversion node per class, placed in the mid-tree where hybrids reach. Each makes an ability count as something it is not, and every talent that reads the new category immediately applies.

| Class | Conversion | What it lights up |
|---|---|---|
| Mage | Frostbolt counts as a Fire spell as well as Frost | Ignite, Critical Mass, Fire Power, Master of Elements |
| Priest | Your Holy spells count as Shadow for stacking purposes | Shadow Weaving, Darkness, Shadow Affinity |
| Warlock | Immolate counts as a curse | every curse talent in Affliction |
| Rogue | Your bleeds count as poisons | Improved Poisons, Vile Poisons, Envenom |
| Warrior | Rend counts as a physical periodic effect Deep Wounds can refresh | Deep Wounds, Impale's crit chain, Bloodletting |
| Druid | Moonfire counts as a bleed | every Feral bleed talent, and Rip's refresh |
| Shaman | Your weapon imbue counts as a spell | Elemental's spell damage and Clearcasting |
| Paladin | Seal damage counts as a melee attack | Retribution's melee chain and Protection's threat |
| Hunter | Traps count as ranged attacks | Marksmanship's shot talents |

Every one of those is a single node. Every one of them turns a tree pair from two half-builds into one build, because the second tree's talents suddenly have something to act on.

## 4. Why this is safer here than in the game we took it from

Diablo has to tune tag conversion constantly, because tags there catch **damage multipliers**. Convert everything to one element, stack that element's percentages, and the build spirals. That is the standard ARPG failure and it is why their Paragon board needed stripping in the first place.

Our system cannot do that, and the reason is a decision already made for other purposes. **Section 5.1 deleted every flat node and moved its value to the depth dividend.** So there are no damage percentages left in the trees for a conversion to catch. A converted Frostbolt does not pick up "+5% Fire damage" because that talent no longer exists. It picks up Ignite, which is a behaviour.

**Conversion in our system produces new interactions rather than new multipliers.** That is a much smaller blast radius, and it means the mechanism that is dangerous in Diablo is comparatively safe here, as a direct consequence of the hygiene work we did take.

That is worth stating plainly because it inverts the usual objection. The reason to be nervous about copying an ARPG mechanic is number spiral, and we removed the numbers first.

## 5. It fixes the one-way wiring more cleanly than adding nodes

`partial-builds.md` found that mage, warlock, rogue Combat, and hunter Survival all reach toward other trees that do not reach back, so those classes produce no named hybrid. The fix proposed there was four new sideways nodes.

Conversion does it better in at least two of the four cases.

**Mage.** Frostbolt counting as Fire is not a sideways node bolted on, it is the whole Fire tree becoming reachable from Frost. One node, and Fire/Frost becomes a build with a name rather than a split with a number. That is a better answer than giving Fire a node that reaches toward Frost, because it makes the existing talents do the work.

**Rogue.** Bleeds counting as poisons connects Assassination to Combat and Subtlety at once, since all three produce bleeds and only one has the poison talents.

**Warlock** is the interesting failure. Immolate counting as a curse points Destruction toward Affliction, which reverses the one-way chain. Whether it produces a build depends on whether the curse talents are worth it, which after the Affliction rebuild folded five curse nodes into one Curse Mastery, is less certain than it was.

**Hunter** does not resolve as neatly, because Survival's problem is that it sits next to the class rather than inside it, and traps counting as ranged shots is a smaller bridge than the others.

## 6. Risks

**Conversion nodes are strictly additive and therefore always correct to take.** If Frostbolt counting as Fire has no downside, every frost mage takes it and it stops being a choice. Each conversion needs either a cost, so that Frostbolt counting as Fire also means it can be resisted as Fire, or a subtraction framing, so that it counts as Fire *instead of* Frost and gives up the Frost talents in exchange. The second is better and matches Section 5.4.

**It multiplies the tuning surface.** Every conversion means a set of talents now applies to something they were not written for, and each of those combinations needs checking. Nine conversions is not nine tests, it is nine times however many talents read the target category.

**It can trivialise the cross-tree seat.** If conversion connects trees more effectively than the sideways nodes at gate 20 do, the sideways nodes become redundant. That is arguably fine and arguably means gate 20 should hold the conversions rather than the sideways nodes, which would be a real restructuring of what has already been built.

## 7. What this changes in the documents

Section 3 of the talent document should gain a fourth item, stated as a correction: the variety mechanism was available, we saw it, and we recorded only the hygiene. The provenance table entry becomes **Taken**, Diablo 4 Lord of Hatred, rather than the omission it currently is.

Section 5 needs a subsection for conversion, and it belongs next to 5.3 because it is doing the same job by a better method.

The nine conversions above need to be placed, costed, and given their subtraction framing before any of this is more than an argument.
