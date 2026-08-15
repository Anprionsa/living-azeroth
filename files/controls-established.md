# Three Controls

**August 2026**

*Two free tests was thin. This establishes what the comparison can and cannot show.*

---

## 1. What was added

**wowtbc.gg Phase 6 Naxxramas**, twelve specs, <cite index="28-1">comparing top 10% parses rather than medians, with Fury warrior at 1274, Combat rogue at 1105 and Fire mage at 987</cite>.

A different site, a different percentile, the same game. That makes it an independent second reading rather than more of the same data.

**Season of Discovery Phase 7 Naxxramas**, twenty-one specs, <cite index="29-1">led by Fire mage at 22,277 with Melee hunter at 99.31% and Balance druid at 99.12%</cite>.

## 2. The most useful number is how far apart the two Classic controls are

**They disagree with each other by a mean of 4.4 points of share, and by 21.6 at the extreme.**

That is the noise floor. Two published ladders, same game, same raid, same phase, differing because one takes medians and the other takes top parses.

| | Mean error against the sim |
|---|---|
| CLASSIC (median) | 4.6 points |
| WOWTBC (top 10%) | 4.2 points |
| **The two controls against each other** | **4.4 points** |

**The simulator sits as close to each published ladder as they sit to each other.** That is the strongest form the claim can take, and it is also its ceiling: no amount of further tuning can do better than the sources agree.

Excluding Mage Frost, which is a deliberate change, the errors fall to **0.8 and 2.3 points**.

## 3. The free tests, now doubled

| Free test | vs CLASSIC | vs WOWTBC |
|---|---|---|
| Shaman Elemental | +2.4 | -5.6 |
| Druid Balance | -0.0 | -3.7 |
| Mage Frost | +46.4 | +24.8 |

**Six independent measurements where there were three.** Elemental and Balance land inside the noise floor against the median ladder and just outside it against the top-parse one.

**And Frost is instructive against the second control.** It reads 31.6% at median and **53.2% at top 10%**, a 21.6 point gap, by far the largest disagreement between the two sources. A spec whose good players parse enormously higher than its median players is a spec that is hard rather than weak.

That changes the reading of the rework's Frost number. It is not lifting a spec from 31.6% but from something between 31.6% and 53.2%, which makes 77.8% an overshoot of roughly twenty-five points rather than forty-six.

## 4. Season of Discovery is not a validation target, and saying why matters

SoD runes changed every class. The reworked trees did not. **Agreement between them would be a coincidence and disagreement is the expected result**, so scoring against it would be meaningless.

It is worth having for a different reason. **SoD's spread is 13.2 points top to bottom against vanilla Classic's 68.4.**

| Ladder | Spread | Standard deviation |
|---|---|---|
| Classic, median | 68.4 | 19.6 |
| Classic, top 10% | 60.7 | 18.1 |
| **This rework** | **64.3** | **19.1** |
| Season of Discovery | 13.2 | 3.9 |

**That is the design decision the project has been implicitly making, shown as a number.** SoD chose near-parity: twenty-one specs inside thirteen points, where the twelfth-best spec does 87% of the first. Vanilla Classic has the twelfth at 32%.

**The rework sits at 64.3, which is vanilla's shape, not SoD's.** It preserves the ladder and fixes individual specs within it. That is band neutrality doing exactly what `sim-baseline-protocol.md` said it would, and it is a defensible position, but it is a position rather than a default.

**The alternative was available and was not taken.** If the goal were every spec viable, SoD demonstrates the target is thirteen points rather than sixty-four.

## 5. What is now established

**The simulator tracks the vanilla ladder to within the disagreement between published sources.** Six free tests, four of them within the noise floor, one deliberate change, one that is smaller than it looked.

**What it still cannot establish:** the calibration fits nine classes to nine numbers, and no amount of control data changes that. The free tests are limited to classes with two logged damage specs, which is three of nine.

**A fourth control would need a version where a class's specs shift relative to each other while the underlying talents stay comparable.** Season of Mastery is the obvious candidate: same talents, no world buffs, longer fights. Warcraft Logs holds it under the Vanilla site's SoM filters, but the published per-spec numbers are not readily available in the way the two Classic ladders are.
