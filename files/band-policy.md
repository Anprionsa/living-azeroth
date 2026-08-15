# Arms Cleave, and Data for the Band Decision

**August 2026**

---

## 1. The Arms fix, and why the obvious version does not work

Arms read -16.7% on three targets. **Making Mortal Strike itself hit more targets barely helped**: hitting two gained one point, hitting three gained two. It is cast too rarely to matter.

**A periodic cleave on every strike gained 18.8 points at zero cost on one target.**

| Candidate | Cleave | Patchwerk | Gain | Cost |
|---|---|---|---|---|
| Baseline | -16.7% | +1.2% | | |
| Every 3rd strike cleaves 2 | **+2.2%** | +1.2% | +18.8 | **0.0** |
| Every 2nd strike cleaves 1 | -0.0% | +1.2% | +16.7 | 0.0 |
| Every 3rd strike cleaves 1 | -5.4% | +1.2% | +11.2 | 0.0 |
| Every 4th strike cleaves 1 | -8.2% | +1.2% | +8.5 | 0.0 |
| Mortal Strike hits 3 | -14.7% | +1.2% | +2.0 | 0.0 |
| Wound spreads through bleeds | -16.7% | +1.2% | 0.0 | 0.0 |

**Zero cost on every one of them, because cleaving is worth nothing when there is nothing to cleave into.** That is the cleanest lever shape found anywhere in this project: it moves one scenario and touches no other.

Adopted, at every third strike sweeping two:

> A vicious strike that wounds, halving the healing its target receives. While the wound holds, every third strike you land sweeps through two nearby enemies and carries the wound with it. A wounded target that dies passes the wound to the nearest enemy.

Arms now reads **+1.2% patchwerk, +2.2% cleave, +1.2% movement, +2.9% switching**, and -6.6% on burst, which is the remaining cell.

## 2. Data for the band decision

Ten pairs, five scenarios, with each capstone's shape recorded.

| Pair | Shape | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|---|
| Arms | periodic cleave | +1.2% | -6.6% | +1.2% | +2.2% | +2.9% |
| Fury | strike + heal | +3.4% | +0.7% | +3.4% | +1.5% | +2.9% |
| Combat | cooldown | +0.6% | -1.9% | +0.6% | +0.6% | +0.3% |
| Fire | cooldown | +1.0% | +4.3% | +0.8% | +0.9% | +1.1% |
| Arcane | cooldown | +3.7% | **+10.9%** | +1.7% | +3.3% | +3.7% |
| Affliction | cooldown | +5.8% | **+17.7%** | +5.8% | +1.8% | **+13.4%** |
| Destruction | passive | +4.5% | **+11.0%** | +2.4% | +1.8% | +5.2% |
| Shadow | passive | +4.5% | +2.4% | +3.2% | +4.5% | +4.2% |
| Marksmanship | cast time | -1.2% | +2.4% | -1.7% | -2.8% | +0.0% |
| Balance | form | +0.9% | +0.8% | +0.9% | +1.0% | +0.9% |

### 2.1 What each policy would cost

| Policy | Violations |
|---|---|
| One band, -5 to +5, every scenario | **8 of 50 cells** |
| One band, -8 to +8, every scenario | **4 of 50 cells** |
| Signature scenario exempt at -15 to +20 | 6 of 50 cells |
| Judged on sustained alone | **1 of 10 pairs** |

**The exemption policy performs worse than simply widening the band**, which was not the expected result. It fails six cells against four, because it licenses a cooldown to exceed on burst while still failing Affliction's +13.4% on switching, which is not its signature scenario.

### 2.2 What the data actually says

**The cooldown shape does not reliably run high on burst.** Combat reads -1.9% and Fire +4.3%, both cooldowns. Only Arcane and Affliction exceed, and Affliction exceeds on switching too.

**So "cooldowns are correctly high on burst" is not supported as a general rule.** It holds for two capstones and not for two others of the same shape. The likelier explanation is that **Arcane Power and Dark Pact are individually overtuned**, not that their shape entitles them.

That reverses the position taken in the last four passes, and the data is the reason.

### 2.3 The recommendation

**A single band of -8 to +8 across every scenario.** Four violations, all in two capstones, and both are tunable rather than structural.

The alternative worth considering is **judging on sustained alone**, which passes nine of ten pairs immediately. It is defensible if the view is that scenario spread is desirable variety rather than imbalance, and it is much less work. **It also gives up the ability to notice a capstone that is useless in a whole category of encounter**, which is exactly what the Arms cleave gap was.

## 3. What running the alternatives showed

Every candidate tested for both Necromancy's burst and Arms's cleave had the same property: **the levers that work are the ones that only pay in one scenario.**

Opening windows scored 4.8 burst per point of sustained. Periodic cleave scored infinite, gaining 18.8 cleave points for nothing. Pet amplifiers scored 2.4 and making a capstone hit more targets scored almost nothing.

**A lever that pays everywhere is a buff. A lever that pays in one place is a fix.**

---

## 4. Adopted: a single band of -7% to +7%, every scenario

Tighter than the -8 to +8 recommendation, and it cost nothing to tighten: **both bands failed the same four cells**, so -7 is free.

| Band | Violations before tuning | After |
|---|---|---|
| -5 to +5 | 8 of 50 | 4 of 50 |
| -6 to +6 | 5 of 50 | 3 of 50 |
| **-7 to +7** | 4 of 50 | **0 of 50** |
| -8 to +8 | 4 of 50 | 0 of 50 |

**Every core pair now sits inside -7% to +7% in all five scenarios.**

| Pair | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Arms | +1.2% | -6.6% | +1.2% | +2.2% | +2.9% |
| Fury | +3.4% | +0.7% | +3.4% | +1.5% | +2.9% |
| Combat | +0.6% | -1.9% | +0.6% | +0.6% | +0.3% |
| Fire | +1.0% | +4.3% | +0.8% | +0.9% | +1.1% |
| Arcane | +2.0% | +6.1% | +1.1% | +2.0% | +2.0% |
| Affliction | -1.6% | +7.0% | -1.6% | -4.3% | +4.5% |
| Destruction | +0.9% | +5.7% | -1.1% | -0.4% | +1.6% |
| Shadow | +4.5% | +2.4% | +3.2% | +4.5% | +4.2% |
| Marksmanship | -1.2% | +2.4% | -1.7% | -2.8% | +0.0% |
| Balance | +0.9% | +0.8% | +0.9% | +1.0% | +0.9% |

### 4.1 Three capstones needed tuning and one needed diagnosis

Arcane Power and Shadow and Flame came down through their cooldown entries, which lowers their burst share without touching sustained value.

**Dark Pact needed diagnosis rather than tuning.** Its cooldown was scaled to 1.011, effectively nothing, and **the switching gap did not move at all**. The driver was its `consume` effect, worth twenty percent of shadow damage: on target switching the periodics are cleared, the rotation becomes more Shadow Bolt, and a shadow multiplier is worth more.

**Tuning the obvious lever three times without checking which lever it was would have gutted the capstone and left the outlier in place.**

### 4.2 What the tuner learned

`tune_band.py` targets the worst cell rather than the sustained one. **Converging on patchwerk alone produces a capstone that is fine sustained and wrong in one scenario**, which is how three of these got out of band while reading correctly on the number being watched.

It also distinguishes a capstone that overshoots everywhere from one that overshoots in a single scenario: the first is scaled through the tree, the second through the cooldown table alone. And it never touches `openingDamage`, `frontload` or `cleaveEvery`, which are scenario levers rather than power.
