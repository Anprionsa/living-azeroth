# Band Neutrality, Run

**August 2026**

*The tuning pass the protocol described and nobody had executed.*

---

## 1. The lever, built

`depthCoefficient`, one scalar per tree, read by the simulator at the point output is returned. **No talent edits, no ability changes, no rebalancing of anything inside a tree.**

That is what makes this cheap: vanilla never had this dial, and every correction it needed meant editing talents other specs also used.

## 2. Strict neutrality first, to check the lever works

Targeting each class's logged share exactly:

| Class | Logged | Achieved | Coefficient |
|---|---|---|---|
| Warrior | 100.0% | 99.7% | 1.000 |
| Rogue | 84.2% | 83.6% | 0.884 |
| Mage | 74.8% | 76.0% | 0.906 |
| Warlock | 64.4% | 65.0% | 0.778 |
| Hunter | 60.8% | 61.8% | 0.904 |
| Druid | 60.5% | 60.6% | 1.024 |
| Shaman | 51.8% | 50.3% | 1.000 |
| Priest | 42.4% | 43.1% | 0.912 |
| Paladin | 39.1% | 37.1% | 1.000 |

Nine classes, all within two points, in four iterations.

## 3. Then a measurement error worth recording

Widening to a floor of 50 produced targets summing to 578, the same as logged, and the result came back at 632. Renormalising every class by the same factor changed nothing at all.

**Share sums are the wrong measure.** Shares are relative to the top spec, so scaling every class equally leaves them identical while the raid's actual output falls. Two configurations can have identical shares and different totals.

**Band neutrality has to be checked on absolute output**, which is total raid damage with one of each class.

## 4. Measured properly, and it works

Logged raid total, one of each class: **7,958 damage per second.**

| Configuration | Floor | Raid total | Against logged |
|---|---|---|---|
| Band neutral | 37% | 8,027 | 100.9% |
| **Floor 50** | 48% | 8,014 | 100.7% |
| **Floor 55** | 54% | 8,035 | 101.0% |
| **Floor 60** | 58% | 8,032 | 100.9% |

**All four hold total raid output within one percent of logged while the floor moves from 37% to 58%.**

That is band neutrality doing exactly what it promises. The raid does the same damage; it is distributed differently.

## 5. And compression costs no build diversity

| Configuration | Builds within 7 points of their class best |
|---|---|
| Band neutral | 95 of 320 |
| Floor 50 | 95 of 320 |
| Floor 55 | 95 of 320 |
| Floor 60 | 95 of 320 |

**Identical at every floor.**

The reason is structural: the depth coefficient scales a whole tree and leaves the relative worth of talents inside it untouched. **Compressing the ladder between classes does not compress the choices within one.**

That is the strongest argument for this lever over any other. Every alternative way to raise Paladin, editing its talents or its abilities, would have changed which Paladin builds are worth taking.

## 6. Committed at floor 55

| Class | Logged | Before | After |
|---|---|---|---|
| Warrior | 100.0% | 100.0% | 100.7% |
| Rogue | 84.2% | 94.8% | **88.1%** |
| Mage | 74.8% | 83.7% | **81.2%** |
| Warlock | 64.4% | 82.6% | **73.1%** |
| Hunter | 60.8% | 68.6% | 70.5% |
| Druid | 60.5% | 58.9% | **70.0%** |
| Shaman | 51.8% | 50.1% | **63.1%** |
| Priest | 42.4% | 47.5% | **56.3%** |
| Paladin | 39.1% | 37.6% | **54.3%** |

**Paladin goes from 37.6% to 54.3% and Warlock comes down from 82.6% to 73.1%.** The classes that were inflated give back and the classes that were stranded gain.

**The floor is 54% of the top spec against vanilla's 31.6%**, which is the difference between a spec that gets a raid slot and one that does not.

## 7. Why 55 rather than 50 or 60

Fifty leaves Paladin at 48%, which is better than vanilla and still low enough that a guild optimising a roster would cut it.

Sixty puts Paladin at 58% and Warrior at 100%, compressing the top four into a fourteen point band. That starts to look like the saturation shape rather than a ladder.

**Fifty-five puts the bottom spec at roughly half the top and keeps a 46 point spread**, which is a ladder a player can see and a floor a guild can accept.

**Widening further is available and reversible.** Every configuration is one number per tree, the snapshots are kept, and moving between them is a single pass.
