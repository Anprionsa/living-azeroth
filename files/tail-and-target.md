# The Tail, and What the Target Should Be

**August 2026**

---

## 1. I was wrong about SoD and the error was selection

Last pass I reported SoD's spread as 13.2 points against Classic's 68.4 and read it as a deliberate near-parity design worth considering as an alternative target.

**Both halves were wrong.**

The 13.2 came from taking the twelve SoD specs that matched the Classic list and dropping nine. **The full twenty-one spread 92.9 points, which is wider than Classic, not narrower.**

| SoD, all 21 specs | Share of top |
|---|---|
| Top sixteen | 86.8% to 100% |
| Beast Mastery hunter | 83% |
| Combat rogue | 71% |
| Demonology warlock | 67% |
| **Arms warrior** | **34%** |
| **Arcane mage** | **7%** |

**SoD is not flat. It is sixteen specs bunched at a ceiling and five abandoned below it.**

**Selecting the overlapping subset selected the specs near the ceiling and dropped the tail**, which inverted the finding. Any future control has to be compared on its full spec list or not at all.

## 2. And the compression is saturation, not balance

The sixteen at the top sit inside 1.15x with **no adjacent gap above 2.6 points.**

Classic's adjacent gaps run 18.4, 10.8, 9.4. A ladder where nobody is more than 2.6 points from their neighbour is not a ladder that was tuned; it is a ladder where the content stopped distinguishing between them.

**Content tuned too easy compresses everything that clears the bar and strands everything that does not**, which produces a flat middle and a long tail at the same time. That is exactly the shape SoD has.

**So SoD cannot be used to judge class balance in either direction**, and the alternative target I described last pass does not exist.

## 3. What the rework actually does, measured properly

| Spec | CLASSIC | WOWTBC | Rework |
|---|---|---|---|
| Warrior | 100.0% | 100.0% | 100.0% |
| Rogue | 81.6% | 86.7% | 85.6% |
| Mage Fire | 72.2% | 77.5% | 72.3% |
| Warlock | 62.9% | 66.0% | 63.8% |
| Hunter MM | 60.7% | 60.9% | 59.7% |
| Druid Feral | 59.5% | 61.5% | 59.4% |
| Shaman Enh | 48.7% | 48.8% | 48.6% |
| Shaman Ele | 47.8% | 55.8% | 50.3% |
| Priest Shadow | 42.2% | 42.5% | 42.1% |
| Paladin Ret | 37.1% | 41.0% | 36.9% |
| Druid Balance | 35.6% | 39.3% | 35.6% |
| Mage Frost | 31.6% | 53.2% | 78.1% |

| | Bottom spec | Bottom three mean | Top to bottom |
|---|---|---|---|
| Classic, median | 31.6% | 34.8% | 3.16x |
| Classic, top 10% | 39.3% | 40.9% | 2.54x |
| **Rework** | **35.6%** | **38.2%** | **2.81x** |

**The rework preserves the ladder and has not lifted the tail.** Balance druid sits at 35.6% in both. Retribution at 36.9% against 37.1%.

That is strict neutrality in practice, which is not what `sim-baseline-protocol.md` recommended. **Band neutrality was chosen and what got delivered is closer to strict.**

## 4. Which is a real finding about the design rather than the measurement

The rework's claim is that talents buy behaviour instead of numbers, and that spending points differently produces different builds. **Both are true and neither raises a floor.**

Checking each bottom spec's best reworked build rather than its canonical one:

| Spec | Canonical | Best reworked build | Gain |
|---|---|---|---|
| Priest Shadow | 42.1% | **47.7%** via Shadow 26 / Discipline 25 | +5.6 |
| Shaman Elemental | 50.3% | 50.1% | 0.0 |
| Paladin Retribution | 36.9% | 37.3% via Ret 26 / Holy 25 | +0.4 |
| Druid Balance | 35.6% | 35.8% | +0.2 |

**Shadow priest gains 5.6 points from a hybrid that vanilla does not reward. Balance druid gains nothing.**

So the rework has delivered build variety without delivering a floor, and those are separate promises. A player who wants Balance druid to be raid-viable is not helped by Balance druid having three viable ways to be 35% of a warrior.

## 5. What this establishes about the target

**Three positions, and the middle one is now clearly the project's.**

**Strict neutrality**, which is what the numbers currently show. Defensible and provable, and it leaves Balance druid where vanilla left it.

**Band neutrality**, which is what was chosen on paper: hold total raid output constant, move individual specs within it. **This has not actually been done.** Doing it means deciding what the bottom of the ladder should be and moving the depth coefficients to reach it, which is one number per tree and no talent edits.

**Parity**, which SoD does not demonstrate and which nothing in the control data supports as a target.

**The question that needs answering before any more tuning is what the bottom of the ladder should be.** Classic's median puts it at 31.6% and its top parses at 39.3%. Something in the fifties would make every spec raid-viable without flattening the ladder, and it is reachable with the depth coefficient alone.

**That is a design decision and I am not going to make it by tuning toward whatever the sim currently reads.**
