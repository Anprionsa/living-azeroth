# Prose Pass

**August 2026**

*A second read of all 696 talents, looking for what makes text flat rather than what makes it wrong.*

---

## 1. Build advice was written into fifteen tooltips

The worst finding, and the one no rule was looking for.

> Your Rejuvenation and Regrowth benefit from your spell critical chance. Healing a target grants them your next Moonfire's damage as absorb. **Every druid heals, so it stands alone, worth most to a Restoration main at 26/25.**

That last sentence is design-doc reasoning about where a talent sits in the point economy, sitting in text a player reads in game. Fifteen talents carried it, all in the cross-tree nodes where the rationale had been written alongside the effect and never separated.

**A player reading a tooltip should learn what the talent does, not which point split it suits.** Removed from all fifteen.

One was worse: Restoration's Wild Growth **ended mid-sentence on a colon**, its text having been truncated where the commentary was cut from a source document.

## 2. Seven talents still opened with raw vanilla tooltip phrasing

> Places a Blessing on the friendly target, reducing damage dealt from all sources by up to 10 for 5 min.

> Gives the Paladin a chance to deal Holy damage equal to 70% of normal weapon damage.

Blessing of Kings, Blessing of Sanctuary, Seal of Command, Elemental Fury, Amplify Curse, Ruin and Subtlety. Rewritten in the established voice:

> Your Blessing turns a share of the damage its target takes back on the attacker. Blocking returns more. It holds on you while you tank.

## 3. Three talents referenced the design rather than the game

> Effect determined by your equipped weapons rather than **by the node**, using **the same fork as Arms, Enhancement, Combat rogue, and Bladedancer**.

A tooltip cannot refer to a node, and a player cannot see other classes' trees. Rewritten to describe the weapons.

## 4. And one N placeholder survived two passes

`Improved Enrage` read *"The Enrage ability now instantly generates N Rage"* through both the previous reading pass and the widened rule, because the rule looks for `N%` and this one had a bare `N`.

## 5. The repetition problem

**"Cannot be" appeared in 164 of 696 talents**, nearly a quarter. Every instance is individually correct, since resisted, dispelled and interrupted are real vanilla concepts, but a quarter of a tree reading the same negative construction is a checklist rather than prose.

Varied where the phrase closes a clause and a synonym is safe: *always lands*, *resists dispel*, *shrugs off fear*, *holds through interruption*, *is never dodged*.

**A first attempt substituted blindly and produced "Healing spells finishes whatever interrupts it by damage."** Reverted, and the second pass only substitutes where the phrase is followed by a full stop or comma, so the replacement cannot collide with what follows.

**164 to 117.** Deliberately not to zero: the phrase is correct vanilla usage and removing it entirely would be its own kind of uniformity.

## 6. What was checked and left alone

**Length.** Median 23 words, range 9 to 53. Twenty-five run over 42 words and all are multi-rank talents describing three or five distinct effects, which is the convention working rather than failing.

**Repeated openings.** "Your heals" opens 14, "Your Fire" 12, "When activated" 12. That is a tree's subject matter showing through and reads correctly.

## 7. Totals

| | Count |
|---|---|
| Build advice removed from tooltips | 15 |
| Rewritten outright | 29 |
| "Cannot be" varied | 53 |
| **Talents touched** | **97** |

Both documents regenerate with zero stale text. Zero N placeholders, zero slash notation, zero build advice, zero vanilla openings, zero em dashes. Both configurations pass 24 rules clean and the audit reports nothing outstanding.
