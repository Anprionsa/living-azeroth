# Builds Without a Capstone

**August 2026**

*51 points, no tree above 30. 114 shapes per class, each measured against that class's best capstone build.*

---

## 1. The result varies enormously by class

| Class | Best capstone-free | Within 7% | Beating the capstone | Distinct results |
|---|---|---|---|---|
| **Rogue** | **+6.7%** | **56 of 114** | **6** | 80 of 114 |
| Hunter | +8.9% | 24 of 114 | 1 | 26 of 114 |
| Druid | -0.7% | **99 of 114** | 0 | **7 of 114** |
| Mage | -2.0% | 13 of 114 | 0 | 32 of 114 |
| Warlock | -3.8% | 6 of 114 | 0 | 37 of 114 |
| Warrior | -0.0% | 6 of 114 | 0 | 22 of 114 |

**Rogue and Druid are opposites, and both are informative.**

## 2. Rogue: the capstone-free build is genuinely competitive

**Six builds beat the best capstone build, and the best is a three-tree split**: Assassination 25 / Subtlety 20 / Combat 6 at +6.7%.

The reason is the poison work. **Poison talents exist in all three rogue trees**, so a build that spreads collects Envenom, Toxicology, Vitality, Cutthroat and Deadened Nerves rather than choosing between them. Eighty of 114 shapes produce distinct results, which is the highest in the class list by a wide margin.

**A mechanic that appears in every tree makes spreading a real strategy.** That is what the nine poison talents bought, and it was invisible until they were modelled.

## 3. Druid: 99 of 114 within 7%, and only 7 distinct results

Nearly every capstone-free shape performs the same, and nearly all of them match the capstone build.

**That is not flexibility, it is indifference.** Seven distinct results from 114 shapes means the point split barely determines what the build does. A Druid can spend 51 points almost any way and get the same output.

**This is the failure mode Section 5.6 was written against**, and it is the opposite of the one anyone was watching for. The concern was that capstones would dominate. The Druid problem is that nothing matters.

## 4. Warrior: many splits, few builds

Five different splits tie at exactly 434 damage per second: 30/21, 26/25, 26/21/4, 25/25/1 and 25/21/5.

They are **not** the same build. 30/21 takes Death Sentence, 26/25 takes Sundering Blows. Measured individually, **Death Sentence, Sundering Blows, Crippling Grip and Shieldbreaker are each worth exactly 0.0%.**

Four Warrior talents contribute nothing, so the splits that differ only by which of them is taken produce identical output. **Twenty-two distinct results from 114 shapes.**

## 5. Hunter: one build beats the capstone, and it is a two-tree split

Marksmanship 30 / Survival 21 at +8.9%. The lowest count of distinct results outside Druid at 26 of 114, so the Hunter design space is narrow, but the one shape that works is strongly ahead.

**A +8.9% capstone-free build is out of band** by the standard applied to everything else, and it is the same finding in a different direction: the Marksmanship capstone is not worth its point against a deeper Survival investment.

## 6. What this says about the design

**The original question was whether a hybrid is a real build.** The answer differs by class, and the difference is diagnostic rather than incidental.

**Where a mechanic spans trees, spreading works and the design space is large.** Rogue with poisons is the clearest case in the project.

**Where talents are tree-specific, spreading is a strict loss**, and Warlock at 6 of 114 within 7% is the extreme.

**Where too many talents are worth nothing, the split stops mattering at all**, which is Druid at 7 distinct results and Warrior at 22.

## 7. Two items this generates

**Four Warrior talents are worth exactly zero** and should be rewritten or replaced. `talent_worth.py` can find the rest across every tree, which has not been run as a sweep.

**Druid needs the same treatment.** Seven distinct results from 114 shapes is a stronger signal than any single talent measurement, and it says the Balance and Feral trees are not making choices that matter.
