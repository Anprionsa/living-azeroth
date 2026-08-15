# What Is Left

**August 2026**

*An honest state of the work after adopting the -7% to +7% band.*

---

## 1. Done and holding

**Core.** All ten measurable pairs sit inside -7% to +7% in all five scenarios. Zero violations of fifty cells.

**Healing.** All four healers inside the band. Restoration shaman's +3.3% throughput against -24.2% efficiency has now held across seven runs, two authoring passes and a behaviour repair.

**Data completeness.** `fullaudit.py` reports nothing outstanding across eight checks. `validate.py` passes 24 rules on both configurations with zero errors and zero warnings. Both documents regenerate from the data.

## 2. Found while checking, and it invalidated earlier tuning

**The expanded baseline was not always a real build.** For Runeblade the comparison was `arms 31 + arms 20`, which is fifty-one points in one tree. `tune.gaps` now refuses a baseline that duplicates either the tree under test or its host.

With the correct baseline, **21 of 30 expanded cells were out of band**, where the previous measurement had shown four. Everything tuned against that comparison was tuned against a partly fictional opponent.

**Two tuner gaps found in the same pass.** Cost, cooldown and cast time discounts were untunable, so Conduit's entire advantage was mana efficiency the tuner could not reach. And burst levers were protected unconditionally, so a tree whose only authored magnitudes were burst levers could not be tuned at all. Protection now applies when burst alone is the outlier, not when the tree is out everywhere.

## 3. Expanded: 23 of 30 cells in band, three trees outstanding

| Tree | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Bladedancer | +0.4% | -0.5% | +0.4% | +0.4% | +0.4% |
| Conduit | +3.9% | +5.0% | +3.9% | +5.2% | +2.7% |
| Survival | +0.7% | +5.5% | +6.4% | +6.0% | -1.0% |
| Runeblade | +2.0% | **-9.1%** | +2.0% | -2.5% | +1.3% |
| Blackguard | **+7.9%** | +4.9% | **+7.9%** | **+7.9%** | +6.9% |
| Necromancy | -6.4% | -2.5% | **-10.9%** | **+27.4%** | **-9.4%** |

**Blackguard is a scaling problem.** It sits uniformly at +7.9%, one point over, and resists further scaling. Ordinary tuning work.

**Runeblade needs a burst lever.** It is fine everywhere except burst at -9.1%, and it has no cash-out or opening window. The candidate test says an opening window is the efficient shape.

**Necromancy is a spread problem, not a magnitude problem.** It spans 38 points between movement and cleave, and scaling moves the whole range without narrowing it. Pets strike independently, so a pet tree is inherently a cleave tree, and the fix has to be a lever that pays only on movement, not more or less power overall.

**That distinction is the useful one: scaling fixes a level, a lever fixes a spread.** Three attempts at scaling Necromancy produced three different placements of the same 38 point range.

## 4. Tanking has no band and needs one

| Build | TPS gap | EHP gap |
|---|---|---|
| Warrior Protection | +28.4% | +0.0% |
| Paladin Protection | +12.0% | +0.0% |
| Druid bear | +9.4% | +7.2% |
| Metamorphosis | +3.5% | +42.9% |

**None of these has ever been tuned to a band, because the band was defined for damage.**

Threat and effective health are not interchangeable, so a single number cannot express a tank capstone's worth. Metamorphosis trades +3.5% threat for +42.9% effective health, which is a coherent capstone; the warrior's +28.4% threat at no survivability cost is probably not.

**Deciding what a tank band means is the next real decision**, and it is a design question rather than a tuning one.

## 5. Two things still unmeasurable

**Master Poisoner**, because poison application is not modelled. It is the only known modelling gap.

**Repentance**, correctly, because it is a stun and carries `simulable: false`.

## 6. Order I would take it in

1. **Define a tank band.** Four capstones are untuned and the instrument has been ready for several passes.
2. **Blackguard down one point.** Smallest item on the list.
3. **A burst lever for Runeblade**, using the opening window shape the candidate test established.
4. **A movement lever for Necromancy**, which is the only one requiring new design rather than tuning.
5. **Poison modelling**, which unlocks the last unmeasurable talent.
