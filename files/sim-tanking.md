# The Threat and Survivability Instrument

**August 2026**

*Filling the gap named in `sim-instruments.md`: a third of the rebuilt trees were invisible to every damage scenario.*

---

## 1. What was missing

Protection warrior, Protection paladin, and every tanking talent in Feral generate almost no damage and were therefore unmeasurable by five scenarios that all report damage per second. **A damage simulator is the wrong instrument for a tank the same way it is the wrong instrument for Repentance.**

## 2. What was built

**A threat model.** Damage generates threat one for one before modifiers, healing generates half a point per point healed. Defensive Stance multiplies a warrior's threat by 1.3, Righteous Fury multiplies a paladin's Holy threat by 1.6. Recorded in `talent-data.json` under `threatModel`.

**A boss profile.** Naxxramas-tier melee: 2,400 per swing on a two second timer, a 4,000 damage special every fifteen seconds, level 63. A level 63 attacker cannot land crushing blows on a level 60 player, since crushing requires a four level gap, so the player-side attack table is miss, dodge, parry, block, crit, hit.

**Three tank profiles.** Warrior, Paladin and bear Druid, each with health, armour, defence, dodge, parry, block chance and block value.

**Metrics that are not damage.** Threat per second, damage taken per second, effective health, block rate, and whether the build reaches crit immunity at 440 defence.

## 3. The tank trees had almost nothing authored

Protection warrior carried authored effects on **three of nineteen talents**. Protection paladin on two of eighteen. The instrument worked immediately and had nothing to read: every build returned identical damage taken and identical effective health.

Twenty-six tank talents are now authored against six new stats, `dodge`, `parry`, `blockChance`, `blockValue`, `health`, `damageTaken` and `defense`, added to the closed vocabulary.

## 4. Results

| Build | TPS | DTPS | EHP | Crit immune | TPS gap |
|---|---|---|---|---|---|
| Warrior Prot 31 / Fury 20 | 446 | 361 | 34,054 | yes | **+17.2%** |
| Warrior Prot 30 / Fury 21 | 380 | 361 | 34,054 | yes | |
| Warrior Prot 31 / Arms 20 | 533 | 361 | 34,054 | yes | **+19.5%** |
| Warrior Prot 30 / Arms 21 | 446 | 361 | 34,054 | yes | |
| Paladin Prot 31 / Ret 20 | 408 | 351 | 33,951 | no | +9.4% |
| Paladin Prot 31 / Holy 20 | 498 | 351 | 33,951 | no | +13.3% |
| Druid Feral 31 / Resto 20 | 296 | 432 | 43,437 | no | +9.4% |

**The capstone premium for tanks is much larger than for damage: 9 to 20 percent against a median of minus 0.2 percent on the damage side.**

That is a real finding and it points at a design problem rather than a modelling one. Shield Slam is a threat capstone on a tree whose entire purpose is threat, so a 31-point Protection build is straightforwardly better at its job than a 30-point one. **Section 5.6's tuning rule is met on the damage trees and clearly failed on the tank trees**, and nobody would have known because the tank trees were never measured.

## 5. Four sanity checks against known truths

| Check | Result |
|---|---|
| Bear has the largest effective health | yes, 43,437 against 34,054 and 33,951 |
| Warrior generates the most threat | yes, 458 against 390 and 281 |
| Bear cannot block | yes, block rate 0.00 |
| Protection warrior reaches crit immunity | yes, via Unbreakable |

All four are things a Classic player would state without hesitation, and the model reproduces them from talent data rather than being told.

## 6. What this instrument still does not cover

**Healing.** No throughput number exists for Holy priest, Restoration druid, Restoration shaman or Holy paladin, and their trees are as large as anyone's. Healing needs its own instrument: healing per second, mana efficiency, and overheal, measured against an incoming damage pattern rather than against a boss health bar.

**Threat as a competition.** The model reports a tank's threat in isolation. What actually matters is the tank's threat against the raid's damage, which needs both simulated at once.

**Cooldown survivability.** Last Stand and Ardent Defender are authored as flat health and mitigation, which understates a cooldown whose value is surviving one specific spike.

Naming these is the point. **Three instruments now exist where one did, and the gap that remains is healing.**
