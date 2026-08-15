# Poisons, One Talent at a Time

**August 2026**

*Option C implemented: a stack ramp rather than a full poison system. Nine talents, fixed individually.*

---

## 1. What was built

One poison carrying the `poison` tag, applied on weapon swings at a chance, stacking to a maximum, dealing damage proportional to stacks held. Recorded in `meta.poisonModel` with what is and is not modelled.

**Deliberately partial.** Four separate poisons, off-hand application rates, weapon swap persistence and cleanse mechanics are Option A and are not built.

## 2. Three simulator bugs found while wiring the first talent

**The generic `enable` handler swallowed every flag before the specific ones could see it.** `poison_instant` was dispatched after it and never fired. Specific flags now dispatch first and the generic handler stays last.

**There was no general `add damage` handler.** Only the pet tag had one, so **every `add damage` effect scoped to any other tag fell through the chain and did nothing.** That is not a poison problem: it affected `bleed`, `weapon`, `ranged` and every other tag across the whole project.

**Stack counts were truncated with `int()`**, so a partially ranked talent granting two stacks at 40% ranks contributed zero rather than one.

## 3. A selector gap

Envenom read +0.0% and was not in the build at all, because `_value` did not score `poisonStacks`. **A talent the selector will not take cannot be measured**, which is the same finding as the opening window two passes ago and now has a second instance.

## 4. The nine, measured individually

`talent_worth.py` removes a talent's effects and re-runs, which is the only way to see a mid-tree talent: the 31-versus-30 comparison moves only for a capstone.

| Talent | Tree | Worth |
|---|---|---|
| Envenom | Assassination | **+11.0%** |
| Toxicology | Assassination | +8.1% |
| Master Poisoner | Assassination | +6.4% |
| Deadened Nerves | Subtlety | +3.7% |
| Blade Venom | Assassination | +3.1% |
| Vitality | Combat | +2.6% |
| Cutthroat | Combat | not taken |

**Eight of nine now contribute.** Cutthroat is authored but the selector does not take it, which is a build-choice outcome rather than an inert talent.

## 5. Assassination, measured for the first time

It had read **exactly 0.0% on every scenario** since the project began, because its capstone modified a tag no ability carried.

| | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Assassination | +0.7% | +7.0% | +0.7% | +0.7% | +0.7% |
| Combat | -0.1% | -0.7% | -0.1% | -0.1% | +0.5% |
| Subtlety | +1.6% | +6.0% | +1.6% | +1.6% | +1.7% |

**All three rogue trees in band.**

### 5.1 The burst problem, and how it was solved without gutting the capstone

Master Poisoner's whole change is skipping the ramp, so it is **inherently worth most in a short fight**. It read +14.2% on burst.

Scaling its damage share brought sustained to +1.1% and left burst at +10.1%, because the instant is not a damage number, it is a timing change.

**The fix was to make the natural ramp faster.** Raising the poison application rate from 30% to 60% means an ordinary rogue reaches full stacks in roughly twenty seconds rather than forty, so skipping the ramp is worth half as much in a forty-five second fight. Burst fell to +7.0% with the capstone untouched.

**That is a lever on the baseline rather than on the talent**, and it is a shape worth remembering: when a capstone's advantage comes from avoiding a cost, reducing the cost reduces the advantage without touching the capstone.

## 6. State

**Core: zero violations of fifty cells at -7% to +7%.** All thirteen pairs now measurable, where two read blank before this work.

`fullaudit.py` reports nothing outstanding across nine checks, including the new one for effects scoped to a tag no ability carries. `validate.py` passes 24 rules on both configurations.

**Option A remains open** and is now cheaper to judge: Assassination is measured, so building the full poison model can be validated against a known number rather than against a blank.
