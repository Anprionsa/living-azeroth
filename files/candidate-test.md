# Testing Candidates Against Both Axes

**August 2026**

*Which talent shapes close a burst gap without inflating sustained output.*

---

## 1. The measure

A candidate that lifts burst and sustained equally has changed nothing about the tree's shape. So the number that matters is **burst gained per point of sustained inflated**, and `candidates.py` reports it.

Each candidate is applied to Necromancy in isolation against a saved baseline, measured across all five scenarios, then reverted.

## 2. Results

Baseline: burst -13.9%, patchwerk +5.2%.

| Candidate | Burst | Patchwerk | Gain | Cost | **Ratio** |
|---|---|---|---|---|---|
| Opening window +25% / 15s | -6.5% | +6.7% | +7.4 | +1.5 | **4.8** |
| Opening window +40% / 10s | -5.8% | +6.9% | +8.1 | +1.7 | **4.8** |
| Opening window +30% / 20s | -3.1% | +7.4% | +10.8 | +2.3 | **4.8** |
| Pet amplifier 3min / 25s +30% | -0.3% | +10.7% | +13.6 | +5.6 | 2.5 |
| Pet amplifier 3min / 20s +55% | +5.9% | +13.5% | +19.8 | +8.3 | 2.4 |
| Pet amplifier 90s / 15s +30% | -5.0% | +11.6% | +8.9 | +6.4 | 1.4 |
| Boneyard amplifies its own army | +4.3% | +14.9% | +18.2 | +9.8 | 1.9 |

**An opening window is twice as efficient as a pet amplifier, and the ratio is flat at 4.8 across three different magnitudes and durations.**

That flatness is the useful part. It says the shape is what matters and the size is a free parameter, so the window can be tuned to whatever the band requires without changing how efficiently it trades.

## 3. Why the pet amplifier loses

It was the obvious candidate, because it is what Unholy uses and the prior art pointed straight at it. It works: the strongest version takes burst from -13.9% to +5.9%.

But a three minute cooldown fires **once in a forty-five second fight and twice in a five minute one**. Two firings in five minutes is not rare enough to be burst-only, so it lifts sustained output substantially. The ratio is 2.4 whichever way it is tuned.

**An opening window fires exactly once per fight regardless of length.** That is the whole difference: its share of a short fight is large and of a long fight is small, automatically, with no cooldown arithmetic to get wrong.

## 4. What was adopted

`Rotting Touch` becomes the opening window:

> Your Risen strike hardest when newly raised. For the first twenty seconds after you enter combat your Shadow damage and your Risen's damage are increased, and the bonus does not fall off early if a Risen dies. Raising a Risen outside combat starts the window on the pull.

**It reads correctly, which matters as much as the number.** The dead answer fastest when first called, and an army loses momentum as a fight wears on. That is a better sentence than "your minions deal thirty percent more damage for twenty seconds on a three minute cooldown."

Set at 42%, Necromancy reads **burst -2.6%, patchwerk +5.5%**. First time it has been inside the floor.

## 5. A tuner correction the test forced

The tuner scaled the opening window along with everything else, which undid the fix it had just been given. `openingDamage` and `frontload` are now in a `BURST_LEVERS` set that the tuner does not touch.

**A tuner that treats every magnitude as interchangeable will flatten exactly the asymmetry you added on purpose.**

## 6. Where every expanded tree now sits

| Tree | patchwerk | burst | worst cell |
|---|---|---|---|
| Blackguard | +5.0% | -1.3% | -1.3% |
| Necromancy | +5.5% | -2.6% | -2.6% |
| Bladedancer | +6.0% | +8.4% | +6.0% |
| Conduit | +5.1% | -2.0% | -2.0% |
| Runeblade | +4.3% | +4.0% | +2.2% |
| Survival | +0.0% | +0.0% | +0.0% |

**Worst single cell across all six trees and all five scenarios: -2.6%.** No tree is below the -5% floor anywhere.

Four sit at +5 to +6% on sustained, which is the top of the acceptable band rather than the target. That remains the known ceiling: a meaningful share of each tree's output comes from the twenty points spent in its host tree, and a tuner can only move what belongs to the tree it is tuning.

## 7. What did not work

**Front-loading a periodic** registered no change at all across three magnitudes. Wither is eight casts of a nineteen cast fight, so moving half its damage earlier moves too little to see. The mechanism is sound and the vehicle was wrong.

---

## 8. The ceiling was a methodology error

Section 6 recorded four trees stuck at +5 to +6% and blamed a ceiling: that a tuner can only move what belongs to the tree it is tuning. **That was wrong, and checking it found four more bugs.**

### 8.1 The comparison was not isolating the tree

Necromancy was measured as `necromancy 31 + frost 20` against `fire 31 + frost 20`, which is fair. **Blackguard was measured as `blackguard 31 + retribution 20` against `retribution 31 + holy 20`**, which is not: the shallow half differs too, so part of every gap belonged to the host rather than to the tree.

With the host held constant the real numbers appeared: **Blackguard +18.9%, not +5.0%. Bladedancer +15.0%, not +6.0%.** Weeks of tuning had been chasing a moving baseline.

### 8.2 Slice and Dice granted nothing

Four maintained buffs occupied a global cooldown and did nothing in the model: Slice and Dice, Sunder Armor, Hunter's Mark, Insect Swarm.

**A build that maintains a buff was paying its cost and receiving none of its benefit**, which flattered every tree that skips maintenance. Bladedancer read +13.1% largely because its finisher deals damage while the baseline's buff dealt none. Given its real 30% attack speed, **Bladedancer fell to +0.2%** with no change to the tree.

### 8.3 Auto Shot consumed every global cooldown

Listed as a rotation entry with a 1.5 second global cooldown, Auto Shot was cast 171 times and a hunter cast nothing else. That is why **every hunter comparison read exactly 0.0%** across every scenario for the entire project. It is now a continuous ranged attack on its own timer, like a melee swing.

Hunters now cast Arcane Shot, Aimed Shot, Multi-Shot, Serpent Sting and Coordinated Assault.

## 9. Final state

| Tree | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Blackguard | +4.5% | +1.7% | +4.5% | +4.5% | +3.9% |
| Necromancy | +5.0% | -3.4% | -2.4% | +5.0% | +6.0% |
| Bladedancer | +0.3% | +6.3% | +0.3% | +1.2% | +0.3% |
| Conduit | +4.1% | -2.9% | +4.1% | +4.2% | +4.3% |
| Runeblade | +4.6% | +3.7% | +4.6% | +3.7% | +5.4% |
| Survival | +5.2% | -1.8% | +5.5% | +7.3% | +5.7% |

**Thirty cells. Worst -3.4%, best +7.3%, twenty-one inside five percent, and none below the -5% floor.**

Four trees are fully in band. Necromancy and Survival sit at +5 to +6% on sustained, which is the top of the acceptable range rather than the target, and both are now genuinely close rather than stuck behind a broken measurement.
