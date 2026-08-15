# Consistency Pass

**August 2026**

*A verification read with the bar set at "genuinely inconsistent" rather than "I would have written it differently."*

---

## 1. What was checked and found clean

**Structure.** Zero multi-rank talents describing a single effect. Zero doubled words, zero double spaces, zero trailing colons, zero fragments that are not deliberate rank statements. Length median 23 words, range 9 to 53, and every talent over 42 words is a five-rank talent describing five effects.

**Terminology.** Zero slash notation, zero build advice, zero design-doc rank markers, zero cross-tree references, zero em dashes.

**Two things were flagged by a check and left alone after reading them.**

`Destructive Reach` opens *"Range increases."* Three words, and it matched a fragment check. **It is not a fault.** The established voice does exactly this: *"Shouts affect the raid. Persist through death. Refresh on a killing blow."* A terse rank statement is the convention working.

**Twenty-five talents run over 42 words.** Every one is a five-rank talent, and the alternative would be compressing five distinct effects into fewer sentences than there are ranks, which breaks a rule that matters more.

## 2. What was genuinely wrong

### 2.1 Three number-agreement errors, from my own substitution

> While active your attacks **is never** dodged.

> At full Risen your spells **shrugs off** interruption.

The previous pass varied "cannot be" without checking the subject's number. Three instances, all in talents where the phrase followed a plural subject. Fixed, and the mirror error checked for and absent.

### 2.2 Twenty-two raw vanilla tooltips the rules were not catching

The larger finding, and it took two widenings to reach.

**Nine opened with a verb the rule did not list**, because the pattern required *"Increases the"* and these read *"Increases chance to block by 30% for 10 sec"*. Holy Shield, Blade Flurry, Adrenaline Rush, Feral Charge, Improved Wing Clip, Elemental Focus, Mana Tide Totem, Improved Drain Mana, Piercing Howl.

**Thirteen more opened with "When activated,"**, which is vanilla's other stock construction and was in no pattern at all:

> When activated, increases your Dodge and Parry chance by 25% for 10 sec.

> When activated, this ability temporarily grants you 30% of your maximum hit points for 20 seconds.

All rewritten:

> For a short time you turn aside almost everything aimed at you. Attacks you deflect return a shot of your own.

> You gain a share of your maximum health for a short time. The health does not fall away when the effect ends, it drains.

**A `no-vanilla-tooltip` rule now covers both openings**, so the category cannot slip a fourth time.

## 3. Why this kept recurring

Three passes each found vanilla survivors, and each time the rule was matching a narrower pattern than the fault. `by N%` missed `a N% chance`. `Increases the` missed `Increases chance`. Neither covered `When activated,`.

**A rule written from the examples in front of you catches those examples.** The fix each time was to widen the pattern from what the fault looks like to what the *category* looks like, which is why this rule now matches on twelve opening verbs plus a number-and-duration pattern rather than on specific phrasings.

## 4. Totals

| | Count |
|---|---|
| Number agreement fixed | 3 |
| Vanilla tooltips rewritten, first widening | 10 |
| Vanilla tooltips rewritten, second widening | 14 |
| **Talents touched** | **27** |
| Flagged and correctly left alone | 27 |

Both documents regenerate with zero stale text. Both configurations pass 25 rules with zero errors and zero warnings. The audit reports nothing outstanding.
