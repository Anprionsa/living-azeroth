# Full Test Run

**August 2026**

*After the methodology correction, the maintenance buff fix, and the Auto Shot fix.*

---

## 1. Three more bugs this run

**Cooldowns only ever applied damage and critical strike chance.** A cooldown whose effect was resource regeneration or haste did nothing, which is why **Adrenaline Rush measured as worthless despite doubling energy for fifteen seconds**. With `resourceRate` read, Rogue Combat went from 0.0% to +12.4% before tuning.

**Trueshot was scoped to the wrong stat.** It read as a cooldown reduction across all ranged abilities rather than removing Aimed Shot's cast time. Corrected, Hunter Marksmanship went from 0.0% to a measurable result.

**Eight core pairs are now testable where six were.** Rogue Combat and Hunter Marksmanship had both read exactly 0.0% across every scenario since the project began.

## 2. Core

| Pair | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Warrior Arms + Fury | +1.3% | -3.7% | +1.3% | **-6.7%** | +2.5% |
| Warrior Fury + Protection | +6.6% | +6.3% | +6.6% | -2.4% | +6.9% |
| Rogue Combat + Assassination | +3.2% | **+19.1%** | +3.2% | +3.2% | +3.2% |
| Mage Fire + Frost | +1.6% | +4.3% | +1.8% | +1.6% | +1.6% |
| Mage Arcane + Fire | +3.5% | **+10.9%** | +2.4% | +3.5% | +3.5% |
| Warlock Affliction + Destruction | -1.1% | -3.6% | -1.1% | -0.9% | -1.2% |
| Warlock Destruction + Demonology | +1.0% | +2.0% | +1.4% | +0.7% | +0.5% |
| Priest Shadow + Discipline | +4.7% | +2.4% | +4.3% | +4.7% | +4.8% |
| Hunter Marksmanship + Beast Mastery | -2.4% | **+9.3%** | -2.2% | -0.7% | -1.7% |

| Scenario | mean | median | within 5% |
|---|---|---|---|
| patchwerk | +2.1% | +2.4% | **7/8** |
| movement | +2.0% | +2.1% | **7/8** |
| cleave | +0.7% | +2.4% | 5/6 |
| burst | +6.3% | +5.3% | 4/8 |

**Sustained, movement and cleave are all healthy. Burst is the outlier and the reason is structural.**

Three capstones exceed +9% on burst and all three are cooldowns: Adrenaline Rush, Arcane Power, and Trueshot's interaction with Aimed Shot. **A cooldown is a larger share of a forty-five second fight than of a five minute one, and that is correct behaviour rather than a tuning fault.** Tuning it away would make those capstones worse than mid-tree talents in every other scenario.

The honest reading is that **the burst column should be judged against a different band than the sustained columns**, in the same way a ramping tree is correctly negative there.

## 3. Expanded

| Tree | patchwerk | burst | movement | cleave | switching |
|---|---|---|---|---|---|
| Blackguard | +4.2% | +1.5% | +4.2% | +4.2% | +3.4% |
| Necromancy | +5.0% | -3.5% | -2.4% | +5.0% | +6.0% |
| Bladedancer | +0.1% | +6.2% | +0.1% | +1.1% | +0.1% |
| Conduit | +3.9% | -3.2% | +3.9% | +4.0% | +4.0% |
| Runeblade | +4.2% | +3.1% | +4.2% | +3.5% | +4.9% |
| Survival | +5.3% | -2.0% | +5.7% | +7.4% | +5.9% |

**Thirty cells: worst -3.5%, best +7.4%, twenty-four inside five percent, none below the floor.**

## 4. Tanking

| Build | TPS | DTPS | EHP | Crit immune | Gap |
|---|---|---|---|---|---|
| Warrior Prot | 802 | 374 | 41,923 | yes | +4.6% |
| Paladin Prot | 825 | 331 | 36,118 | no | +7.2% |
| Druid bear | 504 | 431 | 43,437 | no | +9.4% |
| Metamorphosis | 932 | 339 | 36,186 | no | +11.1% |

Warrior is in band where it was +14.2% two passes ago. **Metamorphosis's 30/21 build loses 11,000 effective health and takes 43% more damage**, which is the clearest tank result in the suite: the capstone is the mitigation.

## 5. Healing

Unchanged and stable. **Restoration shaman holds +3.3% healing per second and -24.2% per mana across all three damage patterns**, the sixth consecutive run with that shape.

Overheal separates correctly: shaman 37 to 49%, druid and paladin 0 to 5%.

## 6. What remains

**Two pairs still read 0.0%: Rogue Assassination plus Subtlety, and Paladin Retribution plus Holy.** Their capstones are Master Poisoner and Repentance. Repentance is a stun and carries `simulable: false`, which is correct. Master Poisoner makes poisons apply instantly at full stacks, and the simulator does not model poison application at all.

**That is the last known gap and it is a modelling one rather than a design one.**
