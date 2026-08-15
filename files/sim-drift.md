# Two Corrections and One Finding About My Own Authoring

**August 2026**

---

## 1. Blackguard is not a tank, and I measured it as one

Class absorption 7.1 describes Blackguard as **plate melee with a dark self-sustain engine**. Paladin already has Protection. It is a melee damage tree competing with Retribution.

When it read -15% on damage I added self-healing to the tank model and ran it through `tank.py`. **That was reaching for a kinder instrument to rescue a bad number**, which is the failure mode the instrument work exists to prevent rather than an application of it. Role assignments for all ten new trees are now recorded in `meta.roleAssignments` so the question cannot be fudged again.

**Metamorphosis is a tank and had no tank profile at all**, so it was only ever measured by the damage simulator. Given one, it reads 564 threat per second against 599 for a Protection warrior and 34,015 effective health against 41,923. Competitive, not the -23% the damage run suggested.

## 2. Talent damage multipliers never applied to autoattacks

The white swing calculated weapon damage, applied the attack table and armour, and **skipped every talent modifier**. For a class whose damage is mostly autoattack this meant most of a melee tree did nothing.

Blackguard had a 1.56 melee multiplier reaching 23 Plague Strikes and no white swings. Fixing it moved Blackguard from -15.0% to +8.3% with no change to the tree at all.

**Every melee number in this project before this fix was wrong**, and wrong in a direction that penalised melee trees in proportion to how much of their damage was autoattack.

## 3. The finding: my authoring reintroduced what Section 5.2 deleted

With the fix in place the melee trees separated wildly: Bladedancer +45.7%, Runeblade +15.7%, Survival +16.9%. The obvious reading was that the new trees were authored too generously.

Measuring the multipliers says something worse.

| Tree | Primary school multiplier |
|---|---|
| Warrior Arms | **1.00** |
| Rogue Combat | **1.00** |
| Druid Feral | **1.00** |
| Mage Frost | 1.08 |
| Warlock Affliction | 1.10 |
| Paladin Retribution | 1.21 |
| Priest Shadow | 1.40 |
| Warlock Destruction | **1.58** |

**Core trees that are meant to be balanced range from 1.00 to 1.58.**

The trees at 1.00 are not broken. **They are the ones honouring the design.** Arms deals damage through Mortal Strike, bleeds and Overpower resets, which is behaviour. Destruction reads 1.58 because I authored Improved Shadow Bolt, Aftermath, Emberstorm, Devastation and Shadow and Flame as percentage multipliers.

**Thirty percent of all authored talents express their effect as a percentage.** Section 5.2's entire method was deleting exactly that from the trees.

### 3.1 Why it happened

The effect DSL makes `multiply damage 1.10` the easiest thing to write and a behaviour the hardest. Authoring 696 talents under that gradient drifted toward percentages under its own gravity, and nothing checked for it because the vocabulary permits it and the validator had no rule against it.

**A tool shapes what gets built with it.** The DSL was designed to express behaviour and it made percentages cheaper, so percentages is what it got.

### 3.2 What not to do about it

The tempting fix is to normalise every tree to a common multiplier, around 1.20. **That would entrench the drift rather than repair it**, by giving the three trees that correctly have none a percentage they were designed not to have.

The correct repair is to re-express the percentage talents as behaviour: Improved Shadow Bolt as a vulnerability the next attacker consumes rather than as ten percent, Emberstorm as Immolate stacks consumed for damage rather than as eight. That is a second authoring pass and it is design work, not tuning.

A `percentage-drift` rule now flags any tree where more than 40% of talents express a percentage. Six core trees and ten expanded trees trip it.

## 4. Smaller fixes in the same pass

**Coordinated Assault had no cooldown**, so it occupied every global cooldown and was 175 of Survival's 192 casts. Gated at six seconds.

**New trees were authored more generously than core trees.** Blackguard, Bladedancer and Runeblade sat at 1.56 to 1.69 against a core median of 1.10, and were scaled to 1.22. That was a real imbalance independent of the drift, since the new trees compete directly with the core ones.

## 5. Where this leaves the numbers

**Every damage figure produced before section 2's fix is void for melee specs.** The tank and healing figures are unaffected.

The percentage drift means the current damage numbers measure a version of the design that partially reverted to vanilla's method. **They are not wrong as measurements. They are measuring the wrong thing**, and the gap between those two statements is the whole reason the finding matters.
