# Three Instruments, Not One

**August 2026**

*Answering a specific question: what measures a capstone whose value is not throughput.*

---

## 1. Seven capstones read zero, for three different reasons

A single-target damage simulator returned no significant difference for seven of thirteen pairs. That looked like a data gap. It was three separate problems wearing the same result.

**Burst cooldowns.** Combustion, Arcane Power, Elemental Mastery and Adrenaline Rush produce throughput, concentrated into a window. On a 300 second fight a 15 second window is 5% of the time and vanishes into the average. **The instrument was right and the fight length was wrong.**

**Uptime and ramp.** Trueshot removes Aimed Shot's cast time; Master Poisoner makes poisons apply instantly. Neither adds damage on a stationary five minute fight against one target. Both matter when you move or when the target dies.

**Control.** Repentance is a stun. It has no throughput value at any fight length, on any target count, under any movement pattern. **No damage simulator will ever measure it, and building one that appears to would be worse than admitting the gap.**

## 2. What was built

### 2.1 A scenario suite

Five profiles in `talent-data.json` under `scenarios`:

| Scenario | Shape | What it exposes |
|---|---|---|
| `patchwerk` | 300s, one target, no movement | raw throughput. The default, and the wrong instrument for everything else |
| `burst` | 45s, one target | cooldowns, which are a large share of a short fight |
| `movement` | 300s, 30% unable to hard cast | instant casts, cast-while-moving, mobility |
| `cleave` | 300s, three targets | addTarget and spread effects |
| `switching` | 300s, new target every 30s | ramp, periodic effects, instant application |

**A talent's value is its profile across scenarios, not one number.**

### 2.2 A cooldown table

Activated abilities that modify subsequent casts rather than dealing damage. Six defined, each with duration, cooldown and effect. The simulator fires them when available and applies their modifier while active.

### 2.3 An explicit non-throughput classification

Twelve talents now carry `simulable: false`, including every subtraction node and Repentance. **They are argued rather than measured**, and the note in `meta.instrumentNote` says so, because the failure mode to avoid is producing a number for them that looks like evidence.

## 3. What it found

| Capstone | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Arcane Power | +3.6% | **+13.0%** | +2.3% | +3.6% | +3.6% |
| Combustion | +1.2% | **+4.5%** | +0.6% | +1.2% | +1.3% |
| Bloodthirst | +9.9% | +7.7% | +9.9% | +9.1% | +8.7% |
| Shadowform | +12.0% | +12.0% | +12.0% | +12.0% | +12.0% |
| Shadow and Flame | -12.4% | -11.7% | -12.1% | -12.4% | **-12.5%** |
| Dark Pact | -1.6% | -3.3% | -2.3% | -1.6% | -1.3% |
| Adrenaline Rush | -3.1% | -3.3% | -3.1% | -3.1% | -3.1% |

**Arcane Power goes from +3.6% to +13.0% between patchwerk and burst.** That is the whole argument for the suite in one line: the same talent, the same build, measured correctly instead of measured conveniently.

Capstones measurable in at least one scenario went from six to seven, and two that read near zero on patchwerk now show real value on burst.

## 4. What is still not measurable, and should not be

**Trueshot, Master Poisoner, Elemental Mastery, Mortal Strike and Moonkin Form** still read flat everywhere.

For Elemental Mastery that is a data problem: it grants an ability now, but the shaman rotation does not weight a single crit window heavily enough for 15 seconds in 45 to register. For Trueshot and Master Poisoner the authored effects do not yet express what the scenarios test, which is a 197-talent authoring problem rather than an instrument one.

**Repentance should never register**, and the right response is the `simulable: false` flag rather than a fourth scenario invented to make a stun look like damage.

## 5. The instrument that does not exist

Nothing here measures **survivability, threat, or crowd control**, and those are where a third of the rebuilt trees live. Protection warrior, Protection paladin, and every tanking talent in Feral are invisible to all five scenarios.

A threat and damage-taken model is the obvious next instrument, and it is a larger build than the scenario suite because it needs an attacking boss, an armour and avoidance model on the player side, and a threat table. **It is worth naming as absent rather than leaving the impression that a damage simulator covers the design.**
