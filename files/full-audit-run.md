# Full Audit and Test Run

**August 2026**

*Every completeness check consolidated into one script, then a full run.*

---

## 1. One audit instead of finding gaps one at a time

Every pass for five rounds found the same shape in a different place: a field existed, nothing read it, and the resulting number looked like a finding. `fullaudit.py` now runs all eight checks at once:

- effects whose op or stat no simulator reads
- abilities a talent grants that appear in no rotation
- abilities cast without damage, scaling, cost or a global cooldown
- effects naming an ability that does not exist
- talent text still carrying vanilla placeholders
- talents with no authored effect and no `simulable: false`
- classes with no rotation
- cooldown effect keys nothing reads

**It found two things and both are now closed.** Repentance had empty text, and `immune_slowed` was unread and is mobility rather than throughput, so it is classified rather than modelled.

**The audit now reports nothing outstanding.**

## 2. Three fixes the run produced

**The converger was flattening the burst levers it had just been given.** Cash-out cooldowns are burst-weighted by design, and scaling them alongside sustained output undoes exactly the asymmetry they exist to provide. `SCALE_COOLDOWNS` is now off, joining `openingDamage` and `frontload` in the protected set.

**Survival had no burst lever at all** and read -11.0% there. Combat Trapping became an opening window, which the candidate test established as the most efficient shape available.

**The build selector did not value opening windows**, so it never took the talent. A burst lever the build will not pick is worthless. `openingDamage`, `frontload`, `comboPoint`, `attackSpeed`, `rage` and `energy` are now in the selector's `DPS_STATS`.

**Survival went -11.0% to +0.1% on burst. Conduit went -12.0% to -4.0%.**

## 3. Core

| Scenario | n | mean | median | within 5% |
|---|---|---|---|---|
| patchwerk | 7 | +4.1% | +3.7% | 6/7 |
| movement | 8 | +2.7% | +2.2% | 7/8 |
| cleave | 6 | -1.0% | +2.6% | 5/6 |
| burst | 7 | +8.5% | +4.3% | 4/7 |

## 4. Expanded

| Tree | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Blackguard | +6.8% | +5.0% | +6.8% | +6.8% | +6.3% |
| Necromancy | +5.8% | +1.8% | +2.3% | +17.5% | +5.9% |
| Bladedancer | +4.8% | +5.3% | +4.8% | +4.8% | +4.8% |
| Conduit | +3.4% | -4.0% | +3.4% | +3.9% | +2.7% |
| Runeblade | +1.5% | -2.1% | +1.5% | -6.5% | -0.8% |
| Survival | +3.9% | +0.1% | +10.7% | +8.1% | +3.5% |

**No tree is below -6.5% anywhere and four are inside the target band on sustained.**

## 5. The three cells that should stay where they are

**Warrior Arms at -16.8% on cleave.** Mortal Strike strikes one target; the 30/21 build takes Death Wish, a universal damage cooldown. A single-target capstone is worth less on three targets and that is what it means to be single-target.

**Warlock Affliction at +17.7% on burst.** Dark Pact is a cooldown that consumes the demon for a twenty second window. A cooldown is a third of a forty-five second fight.

**Necromancy at +17.5% on cleave.** Risen strike independently, so more targets means more of them contributing. A pet tree is a cleave tree.

**All three are the capstone's own shape showing up in the scenario that suits it.** Flattening any of them would make that capstone worse everywhere else, which is the argument the burst column has been making for four passes and which now applies in both directions.

## 6. Standing position

The instrument is complete in the sense that nothing in the data is unread. **What remains is judgment about which scenario a capstone should be judged in**, and the working rule is that a capstone may exceed the band in the scenario its shape suits and must sit inside it everywhere else.

Two pairs still measure nothing: Repentance because it is a stun, and Master Poisoner because poison application is not modelled. **The second is the only known modelling gap left.**
