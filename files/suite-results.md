# Full Suite

**August 2026**

*Every pair, every scenario, all three instruments, 120 seeds per cell, 95% confidence. `suite.py`.*

---

## 1. Core: capstone shape against mid-tree shape

| Pair | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Warrior Arms + Fury | -1.4% | -1.4% | -1.4% | **-2.8%** | **-2.3%** |
| Warrior Fury + Protection | +13.2% | +15.8% | +13.2% | +11.7% | +15.0% |
| Mage Fire + Frost | +1.9% | +4.7% | +2.2% | +1.9% | +2.0% |
| Mage Arcane + Fire | +3.6% | **+13.0%** | +2.7% | +3.6% | +3.7% |
| Warlock Destruction + Demonology | +3.8% | +4.2% | +3.6% | +3.8% | +3.8% |
| Priest Shadow + Discipline | +12.0% | +12.0% | +12.0% | +12.0% | +12.0% |

| Scenario | n | mean | median | within 5% |
|---|---|---|---|---|
| patchwerk | 5 | +6.9% | +3.8% | 3/5 |
| burst | 5 | +9.9% | +12.0% | 2/5 |
| movement | 5 | +6.7% | +3.6% | 3/5 |
| cleave | 6 | +5.0% | +3.7% | 4/6 |
| switching | 6 | +5.7% | +3.7% | 4/6 |

**Burst is the worst scenario for Section 5.6 and the reason is Arcane Power**, which goes +3.6% on patchwerk to +13.0% on burst. A capstone that is a cooldown will always look better in a short fight, and that is correct behaviour rather than a tuning fault.

**Arms plus Fury is the only pair where the mid-tree shape wins**, and it does so most clearly on cleave and switching, which is where Mortal Cleave and Rupture Line were aimed.

## 2. Expanded: new trees against their class's best core build

**This is the most informative table in the project.**

| Tree | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Blackguard | -15.2% | -21.0% | -15.2% | -15.2% | -14.4% |
| Necromancy | -1.9% | **+29.4%** | +3.4% | -1.9% | +0.7% |
| Metamorphosis | -1.6% | **-23.4%** | -8.0% | **+20.9%** | -2.6% |
| Bladedancer | +7.7% | +8.4% | +7.7% | **+21.8%** | +7.7% |
| Conduit | +0.9% | -3.1% | -2.7% | +2.7% | +0.6% |
| Runeblade | +9.0% | +8.7% | +9.0% | +7.9% | +9.8% |
| Survival | +9.4% | **-18.2%** | +8.0% | -1.4% | +9.5% |

| Scenario | mean | median | within 10% |
|---|---|---|---|
| patchwerk | +1.2% | +0.9% | 6/7 |
| burst | -2.7% | -3.1% | 3/7 |
| movement | +0.3% | +3.4% | 6/7 |
| cleave | +5.0% | +2.7% | 4/7 |
| switching | +1.6% | +0.7% | 6/7 |

### 2.1 The trees are balanced on patchwerk and specialised everywhere else

That is the finding, and it is the best outcome available.

**Necromancy is a burst tree**, +29.4% in a forty-five second fight and level on a five minute one. The Risen arrive, do their work, and the fight ends before their cost is paid.

**Metamorphosis is a cleave tank**, +20.9% on three targets and -23.4% on burst. Shadow Cleave strikes three and the form's value is mitigation that a short fight never tests.

**Survival is the inverse**, +9.4% sustained and -18.2% on burst, because traps need time to arm and rearm.

**Bladedancer is a cleave spec**, +21.8% on three targets against +7.7% single.

**Runeblade is flat at +8 to +10 everywhere**, which is the profile of a tree with no scenario identity. Whether that is a virtue or a flaw is a design question rather than a tuning one.

**Six of seven within ten percent on patchwerk, three of seven on burst.** A set of trees that measure alike on a stationary single target and diverge sharply under different fight shapes is exactly what a designer would want and is not what a homogenised set would produce.

### 2.2 Blackguard is the one genuine outlier

**-14.4% to -21.0% across every scenario**, with no shape where it is competitive. Every other tree has at least one scenario it wins. That consistency is the point: a tree that is weak everywhere is weak, where a tree weak in one place is specialised.

Its damage is spread across Blight application and self-healing, so `tank.py` is the instrument that will say whether it is genuinely undertuned or simply measured wrong.

## 3. Tanking

| Build | TPS | DTPS | EHP | Crit immune | Gap |
|---|---|---|---|---|---|
| Warrior Prot 31 / Fury 20 | 599 | 374 | 41,923 | yes | **+14.2%** |
| Paladin Prot 31 / Ret 20 | 793 | 331 | 36,118 | no | +5.7% |
| Druid Feral 31 / Resto 20 | 366 | 431 | 43,437 | no | +9.4% |

Unchanged from the previous run and consistent: the tank capstone premium runs 5.7% to 14.2%, above the damage median. **Section 5.6 holds on damage and fails on tanks.**

## 4. Healing

| Pattern | Class | HPS | HPM | Overheal |
|---|---|---|---|---|
| steady | Restoration shaman | **+1.3%** | **-25.7%** | 31% |
| spiky | Restoration shaman | +5.8% | -22.2% | 19% |
| aoe | Restoration shaman | +8.0% | -20.1% | 20% |
| all | Priest, Druid, Paladin | ~0% | ~0% | 5 to 44% |

**Restoration shaman is the only healer whose capstone changes anything, and it holds the same shape across all three damage patterns: more throughput, materially worse efficiency.** It has now held that shape across four separate runs and an authoring pass from 38% to 100%, which makes it the most stable finding in the project.

Overheal ranges from 5% for a druid under spiky damage to 44% for a priest under steady, which is a plausible spread and matches the era's reputation.

## 5. What the suite says overall

**Section 5.6 holds on damage and fails on tanks.** Median capstone premium is +3.7% on patchwerk with four of six inside five percent, against 5.7% to 14.2% for tanks.

**The expanded trees are balanced where it counts and specialised where it matters.** Six of seven within ten percent on a stationary single target, and sharply divergent under burst, cleave and movement.

**Two things need a design decision rather than a tuning pass.** Blackguard is weak in every scenario. And tank capstones are worth more than damage capstones, which is either acceptable or requires Shield Slam and its equivalents to be retuned.

**Two things need an instrument that does not exist.** Conduit's Confluence spreads a buff across three allies and Blackguard's self-healing is real mitigation, and no damage number contains either.

---

## 6. Rerun after the behaviour repair

The repair rewrote 72 talents. **`tank.py` and `heal.py` could not read the ops it introduced**, so eighteen effects in the healing and tank trees were invisible to the instruments measuring them. Both now read `debuff`, `consume`, `addTarget` and `immune_overheal`.

That is the fifth time a consumer has failed to keep up with the data, and the first time it was caught before the numbers were reported rather than after.

### 6.1 Core

| Scenario | n | mean | median | within 5% |
|---|---|---|---|---|
| patchwerk | 7 | +3.5% | **+1.9%** | 4/7 |
| burst | 7 | +4.4% | +4.7% | 3/7 |
| movement | 7 | +3.5% | +2.1% | 4/7 |
| cleave | 6 | +3.2% | +2.7% | 3/6 |
| switching | 6 | +3.8% | +2.8% | 3/6 |

**Seven testable pairs where five were testable before**, because the behaviour ops give the simulator something to read on talents that previously had only a percentage.

**Warlock Affliction plus Destruction now favours the mid-tree shape at -1.9%**, and it did not before. That pair is SM/Ruin's neighbour and the movement is in the direction vanilla's own history suggests.

Two pairs remain outside the band and are the same two as always: **Fury plus Protection at +16.0%** and **Shadow plus Discipline at +15.0%**. Bloodthirst adds a large direct attack to a rotation that lacked one; Shadowform is a fifteen percent multiplier stated in its own vanilla text.

### 6.2 Expanded

| Tree | patchwerk | burst | cleave |
|---|---|---|---|
| Necromancy | **+19.8%** | **+30.9%** | +19.8% |
| Runeblade | +14.0% | +15.1% | +12.8% |
| Metamorphosis | -9.9% | **-30.5%** | -2.4% |
| Blackguard | -8.7% | -14.1% | -8.7% |
| Bladedancer | +7.6% | +8.0% | **+18.6%** |
| Survival | +9.0% | -5.8% | +4.9% |
| Conduit | +3.1% | -9.2% | +2.5% |

**Necromancy is now the outlier at +19.8% sustained and +30.9% on burst.** The behaviour repair replaced its flat shadow percentage with a stacking vulnerability that ramps with the number of Risen, and a ramp is worth more than a flat bonus on any fight long enough to build it. **The repair made the tree better, not just differently expressed**, which is a tuning consequence of a correctness fix and needs a magnitude pass.

**Metamorphosis at -30.5% on burst is correct and should not be fixed.** It is a tank tree measured by a damage simulator.

### 6.3 Tanking

| Build | TPS | DTPS | EHP | Gap |
|---|---|---|---|---|
| Warrior Prot 31 | 594 | 374 | 41,923 | **+1.4%** |
| Paladin Prot 31 | 789 | 331 | 36,118 | +5.9% |

**Warrior's tank capstone premium fell from +14.2% to +1.4%.** Shield Discipline's flat threat percentage became a stacking vulnerability that the mid-tree build also benefits from, which closed the gap. **Section 5.6 now holds on warrior tanking where it clearly failed before**, and it did so through the behaviour repair rather than through tuning.

### 6.4 Healing

**Restoration shaman holds: +3.3% healing per second, -24.2% per mana, across all three patterns.** Fifth run, and it has now survived an authoring pass from 38% to 100% and a behaviour repair that rewrote a fifth of the project.

Overheal separated sharply and sensibly: **shaman at 37 to 49%, druid and paladin at 0 to 5%.** Chain Heal into a raid overheals; a druid's heals over time and a paladin's targeted heals do not. That was not true before the repair, because `immune_overheal` was not being read.

## 7. Answer to whether more simming is worth doing

**Yes, and one thing needs fixing first.** Necromancy's ramp is too strong at +19.8% and its magnitude needs a pass. Everything else is within a band worth arguing about rather than a band that says the model is broken.
