# The Healing Instrument

**August 2026**

*Filling the last gap named in `sim-tanking.md`. Four healing trees were unmeasurable by both existing instruments.*

---

## 1. Healing is not damage aimed at a friend

A damage simulator measures output against a boss health bar. A healer's output is bounded by **how much damage arrives**, not by how much they can produce, and a heal landing on a full-health target is worth nothing.

So the instrument needs an incoming damage pattern, and its metrics are different:

- **Effective healing per second**, excluding overheal
- **Healing per mana**, which is the binding constraint over five minutes
- **Overheal share**
- **Time to out of mana**

Three patterns, in `talent-data.json` under `healModel.damagePatterns`:

| Pattern | Shape | Rewards |
|---|---|---|
| `steady` | constant tank damage, light raid chip | efficiency |
| `spiky` | a 3,000 hit on one target every twelve seconds | fast direct heals over efficient ones |
| `aoe` | heavy raid-wide damage | group heals and heals over time |

## 2. Two modelling decisions that mattered more than the talents

**Downranking and skipping.** The first version cast the largest available heal on the lowest-health target every global cooldown. Every healer went out of mana at 34 to 44 seconds, which is arithmetically correct and completely unlike how anyone plays: 710 mana every three seconds against 66 a second of regeneration empties a 7,200 pool in 42 seconds.

The model now picks the heal whose size best matches the hole, preferring the cheapest per point healed, and does not cast into a target missing under 400 health. **That is downranking and triage, and it is the difference between measuring throughput and measuring healing.**

**Scope on cost effects.** Omen of Clarity was authored as `multiply cost 0.0` scoped to all spells, so a Restoration druid healed for free and reported healing per mana of 129,422. It is a ten percent proc for one free spell. **A proc-based cost reduction has to be authored at expected value**, and it now reads 0.90.

## 3. The healing trees were as unauthored as the tank trees

| Tree | Authored before |
|---|---|
| Holy priest | 4 of 18 |
| Discipline | 4 of 18 |
| Restoration druid | 4 of 20 |
| Restoration shaman | 2 of 18 |
| Holy paladin | 4 of 17 |

Twenty-three healing talents now authored, plus Circle of Healing and Swiftmend added as abilities because talents granted them and they did not exist.

**That is the third time an instrument has been built and found nothing to read.** The pattern is consistent enough to state: authoring follows the instrument, because until something consumes a field nobody notices it is empty.

## 4. Results

| Pattern | Class | HPS gap | HPM gap |
|---|---|---|---|
| steady | Restoration shaman | +1.5% | **-28.0%** |
| spiky | Restoration shaman | +8.3% | -22.9% |
| aoe | Restoration shaman | +8.5% | -22.0% |
| steady | Restoration druid | -1.1% | -0.9% |
| all | Holy priest, Discipline, Holy paladin | ~0% | ~0% |

**The shaman result is the only interesting one and it is interesting in the right way.** The 31-point build heals more per second and dramatically less per mana. That is a real trade rather than a strict improvement, and it is exactly the shape a capstone choice should have: **more throughput, worse sustain, and the fight length decides.**

Three classes show no difference at all, which reflects how little of their trees is authored rather than a finding.

## 5. What healing exposes that damage did not

**Healing per mana and healing per second point in opposite directions.** On the damage side more of one meant more of the other. Here a build can be better and worse at once, which means **a single number cannot rank healing builds** and any future balance pass has to state a fight length before it can state a winner.

Every healer except the paladin runs dry between 40 and 53 seconds under the steady pattern. That is short, and it is the model saying that vanilla healing is mana-bound rather than throughput-bound, which matches the era. Whether the profiles are tuned right is unverified and marked so.

## 6. Instruments now built

| Instrument | Measures | Covers |
|---|---|---|
| `sim.py` scenarios | damage per second across five fight profiles | damage trees |
| `tank.py` | threat per second, damage taken, effective health, crit immunity | three tank trees |
| `heal.py` | effective healing, healing per mana, overheal, time to out of mana | five healing trees |

**All twenty-seven core trees are now measurable by at least one instrument**, which was not true an hour ago. What remains is authoring: most trees still have under a quarter of their talents expressed as effects, and every instrument built so far has found that out the hard way.
