# Auditing Every Effect Against What Reads It

**August 2026**

*Every bug in the last several passes had one shape: an effect existed in the data and no consumer looked at it. `coverage.py` enumerates every op and stat combination and reports which simulator reads it.*

---

## 1. A third of the data was inert

**334 of 1,026 authored effects were read by nothing.** Forty-two distinct op and stat combinations existed only as text.

The largest were not obscure. `refresh duration` appeared 51 times, `enable no_expiry` 34, `enable immune_dispelled` 23, `enable immune_interrupted` 22, `add comboPoint` 16.

**Every talent that said "cannot be dispelled" or "refreshes" or "grants a combo point" was doing nothing at all.**

## 2. What was implemented

| Effect | Modelled as |
|---|---|
| `refresh duration` / `no_expiry` | a periodic kept alive rather than expiring |
| `immune_interrupted` | uptime credit, since an uninterruptible cast never restarts |
| `immune_dispelled` / `no_decay` | a periodic that keeps its full duration |
| `immune_missed` / `immune_dodged` / `immune_parried` | removed from the attack table |
| `immune_resisted` | spell miss floored at 1% |
| `add comboPoint` | real combo generation, fractional values rolled |
| `proc bleed` / `sunder` / `extra_attack` | damage on the triggering strike |
| `proc stun` / `root` / `silence` | small throughput credit for uptime bought |
| `convert` | the ability inherits the modifiers of the school it now counts as |
| `use_any_angle`, `use_combat`, `weapon_fork` and nine others | uptime credit |
| `channel` on an ability | occupies its full duration rather than a global cooldown |
| `rapCoefficient` | ranged attack power scaling |
| cooldown `resourceRate` and `haste` | energy and mana regeneration, cast speed |

**334 unread effects became 18.** The six combinations left are mobility, radius and spell reflection, none of which is throughput, and they are recorded in `meta.nonThroughputEffects` rather than given an invented number.

## 3. Two capstones that were not capstones

Implementing the effects made two core capstones measurable for the first time, and both were broken.

### 3.1 Dark Pact returned mana to a build that had enough

Vanilla's Affliction 31-point talent drains the pet for mana. On a build that is not mana constrained it does nothing, and **the simulator measured the 31-point build as worse than the 30-point one**: both cast identically, and the 30-point build got an extra point in Destruction instead.

**A capstone that measures as a loss is a design problem, not a tuning one.** Reworked into a cash-out that consumes the demon entirely for a twenty second window of free, unresistable Shadow damage, at the cost of having no demon for the rest of the encounter.

### 3.2 Shadow and Flame rewarded an alternation that never happened

It paid a bonus for alternating Shadow Bolt and Immolate. The rotation casts Shadow Bolt thirty-nine times and Immolate three, so the alternation fired almost never.

**The `alternate` op is correct for a pair cast at similar rates and wrong for a pair at thirteen to one.** Reworked into an asymmetric relationship: Immolate empowers Shadow Bolts while it burns, and Shadow Bolts extend it. Recorded as a rule in `meta.alternateOpNote`: check the cast ratio before writing a talent that rewards alternation.

## 4. Core after

| Scenario | n | mean | median | within 5% |
|---|---|---|---|---|
| patchwerk | 9 | +2.9% | +3.5% | **8/9** |
| movement | 8 | +3.2% | +2.5% | **7/8** |
| cleave | 9 | +2.5% | +3.5% | 6/9 |
| burst | 8 | +9.6% | +11.0% | 2/8 |

**Nine testable pairs where six were testable two passes ago**, and sustained, movement and cleave are all healthy.

**Burst has got worse and the reason is now unambiguous.** Every capstone that reads high there is a cooldown: Adrenaline Rush, Arcane Power, Trueshot, and now Dark Pact. A cooldown is a third of a forty-five second fight and a twentieth of a five minute one.

**That is the correct behaviour of a cooldown and tuning it away would make each of those capstones worse than a mid-tree talent in all four other scenarios.** The burst column needs its own band, and the working proposal is that a cooldown capstone may reach +15% there while a passive one may not.

## 5. What remains

**Two pairs still read 0.0%.** Repentance is a stun with `simulable: false`, which is correct. **Master Poisoner is the last real gap: the simulator does not model poison application**, so a talent that changes how poisons apply has nothing to change.
