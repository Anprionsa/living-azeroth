# Full Pass: Core and Hybrid

**August 2026**

---

## 1. Core: zero violations of fifty cells

| Pair | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Arms | +3.0% | -3.1% | +3.0% | -0.3% | +5.2% |
| Fury | +0.6% | +1.4% | +0.6% | +0.2% | +1.2% |
| Combat | -0.7% | -2.3% | -0.5% | -0.9% | -0.7% |
| Assassination | -0.2% | +5.6% | -0.2% | -0.1% | -0.2% |
| Subtlety | +1.3% | +4.7% | +1.3% | +1.3% | +1.2% |
| Fire | +1.9% | +4.3% | +2.3% | +1.1% | +1.9% |
| Arcane | +2.0% | +6.5% | +1.1% | +1.9% | +2.0% |
| Affliction | -2.2% | +3.8% | -2.2% | -4.5% | -0.2% |
| Destruction | +4.3% | +6.6% | +4.1% | +2.4% | -5.1% |
| Shadow | +5.6% | +2.6% | +5.6% | +5.6% | +5.6% |
| Marksmanship | -2.1% | +0.9% | -2.5% | +6.6% | -0.3% |
| Balance | +0.9% | +0.9% | +1.0% | +1.0% | +0.9% |

## 2. Hybrid

| Class | Best capstone-free build | Gap | Within 7% | Beating | Distinct |
|---|---|---|---|---|---|
| Rogue | Assassination 25 / Subtlety 20 / Combat 6 | +6.3% | 41 of 114 | 1 | 75 |
| Hunter | Marksmanship 30 / Survival 21 | +4.9% | 28 | 8 | 61 |
| Warlock | Affliction 26 / Destruction 25 | +4.8% | 21 | 7 | 71 |
| Mage | Frost 26 / Arcane 25 | +3.4% | 31 | 1 | 48 |
| Warrior | Arms 30 / Fury 21 | +0.5% | 1 | 1 | 34 |
| Druid | Feral 30 / Balance 21 | +0.0% | 25 | 0 | 18 |

**Every class has a capstone-free build within 6.3% of its best capstone build**, and four of six have one that beats it.

## 3. Three findings this pass

### 3.1 Death Wish was a cliff

A one point talent at gate 20 carrying **both a permanent ten percent and a cooldown**. Every warrior build had to reach exactly twenty-one points in Fury, and the design space collapsed: **Warrior had one capstone-free shape within seven percent** and the next best was ten percent behind it.

Removing the permanent half entirely swung it to **zero** shapes, because the talent stopped being worth its point and the capstone ran away. Raising the cooldown from 1.45 to 2.00 recovered less than two points, because a cooldown is a small share of a five minute fight.

**Settled at a small permanent share plus the cooldown.** The problem was the size, not the combination: seven percent works where ten was a cliff.

### 3.2 The Rogue lever runs backwards

Rogue read **+10.0% with sixteen shapes beating the capstone**, because poison talents exist in all three trees and spreading collects them.

**Weakening poison made it worse**, to +13.2% with forty-four shapes beating. The capstone is Master Poisoner, whose entire value is skipping the poison ramp, so cutting poison cut the capstone harder than the spread.

Raising poison from 36 to 60 base brought it to **+5.8% with one shape beating.** The lever pointed the opposite way to intuition and only measurement would have shown that.

### 3.3 Warrior remains narrow and it is structural

One shape within seven percent, and it is the obvious one. Warrior's third tree is Protection, which contributes nothing to a damage build, so the class has four real shapes rather than 114.

Hunter has the same structure and reaches 28, because Beast Mastery still gives a damage build a pet. **Protection gives a damage build nothing, and that is correct.**

Warrior's narrowness is a property of having one tank tree and two damage trees, not a fault in the two.

## 4. State

Core zero of fifty. Both configurations pass 24 rules with zero errors and zero warnings. `fullaudit.py` reports nothing outstanding across nine checks.
