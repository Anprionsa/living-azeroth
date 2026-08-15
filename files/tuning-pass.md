# Magnitude Pass

**August 2026**

*Tuning to stated bands: above +10% unacceptable, +5 to +10% acceptable only with a specialisation, 0 to +5% the target, 0 to -5% acceptable, below -5% unacceptable.*

---

## 1. Three bugs found while tuning, each worth more than the tuning

**Pyroblast sat above Fireball in the mage rotation** while dealing 234 damage per second of cast time against 342. Necromancy read +19.8% against core Fire not because Necromancy was strong but because **the baseline was casting its worst filler ten times a fight**. Rotation fillers are now ordered by throughput rather than by hand, and Necromancy fell to +0.9% with no change to the tree.

**Twenty-nine melee abilities had no weapon scaling.** Vanilla melee specials are weapon damage plus a flat amount and only the flat amount was in the data, so **Mortal Strike read as 160 damage against Heroic Strike's 157 and taking the capstone measured as a loss.** A `weaponMultiple` field now records how many swings' worth an ability deals.

**Heroic Strike and Cleave are on-next-swing abilities.** They replace the autoattack and cost no global cooldown, and modelling them as normal casts made them free damage occupying no time. Heroic Strike reached 88 casts a fight. They now queue against the swing timer and replace the swing rather than adding to it.

**Each of these made a capstone look worse than a rage dump.** No amount of magnitude tuning would have fixed that, and tuning against them would have entrenched three errors as design.

## 2. Core, after

| Scenario | mean | median | within 5% |
|---|---|---|---|
| patchwerk | +1.4% | +1.6% | **7/7** |
| burst | +1.9% | +2.6% | 4/7 |
| movement | +1.3% | +1.9% | **7/7** |
| cleave | -1.0% | +0.0% | 5/6 |
| switching | +1.2% | +2.5% | **6/6** |

**Every measurable core pair is inside the target band on patchwerk, movement and switching.** Section 5.6's tuning rule is met.

Two capstones were tuned to get there: **Bloodthirst from +13.3% to +3.8%** and **Shadowform from +15.0% to +4.7%**. Both were scaled rather than redesigned, and both remain the strongest single seat in their tree.

Burst is the weakest scenario at 4 of 7, and the reason is unchanged: **Arcane Power is a cooldown, and a cooldown is worth more in a forty-five second fight.** That is correct behaviour and should not be tuned away.

## 3. Expanded, after

| Tree | patchwerk | burst | cleave | Verdict |
|---|---|---|---|---|
| Blackguard | +0.5% | -7.8% | +0.5% | in band |
| Necromancy | +4.7% | -18.7% | +4.7% | in band |
| Conduit | +3.8% | -8.3% | +3.4% | in band |
| Runeblade | +4.4% | +3.9% | +2.3% | in band |
| Survival | +0.0% | +0.0% | +0.0% | in band |
| Bladedancer | +6.2% | +8.5% | **+10.0%** | high, cleave-specialised |

**Five of six inside the target band.** Blackguard went from -15.2% before the melee fixes to +0.5%, without a single talent changing what it does.

**Bladedancer sits at +6.2% single target and +10.0% on cleave** and resists further scaling, because a meaningful share of its output comes from the twenty points in its host tree rather than from itself. It falls in the "above 5% but excels elsewhere" band by the stated rule. Whether a cleave specialisation justifies six percent on single target is a design call rather than a tuning one.

## 4. What the burst column says

Four of six expanded trees are strongly negative on burst: Necromancy -18.7%, Conduit -8.3%, Blackguard -7.8%, Metamorphosis -13.9%.

**That is a coherent pattern rather than six coincidences.** Every one of them ramps: Risen accumulate, Empowerment charges, Blight stacks, Corruption stacks. A forty-five second fight ends before a ramp pays for itself.

The behaviour repair caused this and it is the correct outcome. **A tree built on a stacking mechanic should be weak in short fights**, and before the repair those mechanics were flat percentages that paid instantly.

## 5. Method note

The tuner scales magnitudes and re-measures until a tree lands in band, and it needed extending twice during the pass: first to the **base values of abilities a tree grants**, because Necromancy's whole advantage sat in Wither rather than in any talent, and then to **coefficients**, because Bloodthirst's damage is entirely `apCoefficient` and scaling base damage moved nothing.

**A tuner that cannot reach a tree's actual source of output will report that the tree is untunable.** It said exactly that about Necromancy for four rounds.
