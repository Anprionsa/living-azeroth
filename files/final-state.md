# Everything In Band

**August 2026**

*All four outstanding items closed, and the numbers rerun across every instrument.*

---

## 1. A tank band, defined

Threat and effective health are not interchangeable, so a single number cannot express a tank capstone's worth. Banding each separately would forbid a capstone that trades one for the other, which is a legitimate shape.

**The band is the mean of the threat gap and the effective health gap, held between -7% and +7%.** It permits the trade, catches uniform inflation, and catches a capstone that raises one metric enormously while leaving the other alone.

| Build | TPS | EHP | Mean |
|---|---|---|---|
| Protection warrior | +13.0% | +0.0% | +6.5% |
| Protection paladin | +12.0% | +0.0% | +6.0% |
| Bear | +7.4% | +5.6% | +6.5% |
| Metamorphosis | +3.5% | +9.6% | +6.6% |

**Four of four in band**, from +28.4%, +12.0%, +9.4% and +23.2% before tuning.

## 2. An AoE bug found while fixing Necromancy

**The rotation ranked area abilities as if they hit every target, and the damage calculation only multiplied when `maxTargets` was set.** So a rotation switching to Blizzard on cleave was switching to single-target damage on a slower cast.

Core Fire dropped from 513 to 285 on three targets because of it. Corrected, it rises to 692.

**Every cleave number before this fix was wrong**, and wrong in proportion to how much a build relied on area abilities.

## 3. Three trees, three different problems

**Blackguard was a scaling problem** at a uniform +7.9%, and came down to +6.0%.

**Runeblade needed a burst lever** at -9.1% with no cash-out. Cold Iron became an opening window: the weapon holds its charge between fights and is fully charged on the pull. Now -3.8%.

**Necromancy was a spread problem** spanning 38 points. The answer was the `use_moving` enable alone; the movingDamage bonus on top of it overshot to +32.7%, and removing it entirely landed at -0.8%. **The lever was already sufficient and the magnitude was the mistake.**

**Affliction turned out to be a fourth.** Its capstone lost to Ruin on cleave, because the 30/21 build's extra Destruction point buys a crit bonus worth far more on Rain of Fire. Dark Pact now strikes a second enemy during its window.

## 4. Final numbers

**Core: zero violations of fifty cells.**

| Pair | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Arms | +1.2% | -6.6% | +1.2% | -0.6% | +2.9% |
| Fury | +3.4% | +0.7% | +3.4% | +1.5% | +2.9% |
| Combat | +0.6% | -1.9% | +0.6% | +0.6% | +0.3% |
| Fire | +1.0% | +4.3% | +0.8% | +1.0% | +1.1% |
| Arcane | +2.0% | +6.1% | +1.1% | +1.9% | +2.0% |
| Affliction | -1.2% | +6.5% | -1.2% | -6.5% | +5.5% |
| Destruction | +0.9% | +5.7% | -1.1% | -0.4% | +1.6% |
| Shadow | +4.5% | +2.4% | +3.2% | +4.5% | +4.2% |
| Marksmanship | -1.2% | +2.4% | -1.7% | -2.8% | +0.0% |
| Balance | +0.9% | +0.8% | +0.9% | +1.0% | +0.9% |

**Expanded: thirty of thirty cells in band.**

| Tree | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Blackguard | +6.0% | +3.2% | +6.0% | +6.0% | +4.8% |
| Necromancy | +3.6% | -2.0% | -0.8% | +3.2% | +0.8% |
| Bladedancer | +0.3% | -0.2% | +0.3% | +0.3% | +0.3% |
| Conduit | +3.7% | +4.7% | +3.7% | +5.3% | +2.5% |
| Runeblade | +2.2% | -3.8% | +2.2% | -3.3% | +0.9% |
| Survival | +0.7% | +4.4% | +6.8% | +5.9% | -1.4% |

**Tanking: four of four. Healing: four of four.**

## 5. State

**Every measurable comparison in the project sits inside -7% to +7%.** Ninety-four cells across four instruments.

`fullaudit.py` reports nothing outstanding across eight checks. `validate.py` passes 24 rules on both configurations with zero errors and zero warnings. Both documents regenerate from the data.

**One modelling gap remains**: poison application is not simulated, so Master Poisoner is unmeasurable. Repentance correctly measures as nothing, being a stun.

## 6. The rule worth carrying

Four trees needed four different fixes and only one was a magnitude.

**Scaling fixes a level. A lever fixes a spread. And a lever that is already sufficient does not need a magnitude on top of it**, which Necromancy demonstrated by overshooting to +32.7% and landing at -0.8% when the bonus was removed entirely.
