# Fixing the Burst Hole

**August 2026**

*Four trees read -7.8% to -18.7% on a forty-five second fight, below the -5% floor. Three are fixed. One is not, and the reason matters.*

---

## 1. Four simulator gaps found, each larger than the tuning

**The ramp had no cash-out.** Every one of the four trees describes one in its own text and none was authored as damage. Unstable Dead detonates Risen, Unending Fel spends Corruption, Surge releases a held charge, Blood Rite spends Blight. The value accumulated and never converted.

**A cash-out is a cooldown, not a passive.** Authored as a flat `consume` it raised sustained output as much as burst, and Conduit went from -8.3% burst to +11.3% sustained. Moved into the cooldown table, it fires once in a forty-five second fight and is a third of the output, twice in five minutes and is a twentieth. **That weighting is the entire point and a passive cannot produce it.**

**Pets dealt no damage at all.** Raise Skeleton was cast and the skeleton stood there. Necromancy, Demonology and Beast Mastery all depend on pets and none of them had one that fought.

**Pet summons were excluded from every rotation**, because the rotation builder required an ability to deal direct damage and a summon deals none. So a pet class summoned nothing even after pets could fight.

**Periodics were applied with seconds left in the fight.** Nobody refreshes an eighteen second effect at forty seconds into a forty-five second fight, and modelling it that way made every periodic tree weak in short fights for a reason that was not the design.

## 2. Result

| Tree | Burst before | Burst after | Patchwerk |
|---|---|---|---|
| Blackguard | -7.8% | **-1.3%** | +5.0% |
| Conduit | -8.3% | **-2.0%** | +5.1% |
| Metamorphosis | -13.9% | **-5.9%** | tank, see below |
| Necromancy | -18.7% | -21.5% | +6.0% |

**Three of four are now at or near the floor.** Blackguard and Conduit sit inside it.

**Metamorphosis is a tank and should not be tuned on damage at all.** Its -5.9% is a damage simulator measuring a mitigation tree, which is the same category error as running Chronomancer through it. Its real numbers are 749 threat per second and 36,186 effective health, both competitive.

## 3. Necromancy cannot reach the floor without ceasing to be Necromancy

It sits at -21.5% and every lever has been tried: the cash-out cooldown shortened to forty seconds, pets given damage, summons moved pre-pull, periodics stopped from being wasted.

The reason is visible in the cast list. **In a forty-five second fight Necromancy spends four of nineteen casts on Wither and Raise Skeleton while core Fire spends all eighteen on nukes.** A fifth of a short fight goes to setup that pays out after the fight has ended.

That is not a bug and it is not a magnitude. **It is what a tree built on raising the dead and applying a disease does in a fight that ends before either matters.**

Three options, and this is a design decision rather than a tuning one:

**Accept it.** Necromancy is a sustained tree and a forty-five second fight is its worst case. Every other scenario is in band. Vanilla had specs like this and players chose accordingly.

**Give it a front-loaded tool.** A talent that makes the first Risen arrive instantly at full strength, or Wither deal its full duration's damage immediately when applied below a health threshold. That is new design, not tuning.

**Change the band for ramping trees.** A -5% floor may be the wrong rule for a tree whose mechanic is accumulation, in the way that a burst cooldown correctly exceeds +10% on burst.

## 4. Where the rest sit

| Tree | patchwerk | verdict |
|---|---|---|
| Runeblade | +4.3% | in band |
| Survival | +0.0% | in band |
| Blackguard | +5.0% | top of acceptable |
| Conduit | +5.1% | top of acceptable |
| Bladedancer | +6.0% | above, cleave at +9.8% |
| Necromancy | +6.0% | above, no specialisation |

Four sit at the top of the acceptable band rather than in the target. Pushing them lower is possible but each round of scaling now moves them by under a point, because a meaningful share of their output comes from the twenty points spent in the host tree rather than from themselves.

**That is a real ceiling on this method: a tuner can only move what belongs to the tree it is tuning.**
