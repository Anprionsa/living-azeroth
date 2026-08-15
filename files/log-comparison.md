# Against Real Logs

**August 2026**

*The comparison `sim-baseline-protocol.md` specified in section 2 and which had never been done.*

---

## 1. The control, downloaded rather than simulated

Warcraft Tavern's Phase 6 Naxxramas rankings, January 2026, derived from Warcraft Logs Classic Fresh. Twelve specs, median parse, real players in real Naxxramas gear.

<cite index="11-1">Warriors sit at the top at 1,411 with Rogues at 1,151, which is 81.64% of the top</cite>. The full ladder runs to Frost mage at 446, or 31.6%.

## 2. The first attempt failed, and the reason was worth finding

Run against the sim as it stood, the comparison was nonsense: Rogue read 100% and Warrior 35%, an inversion of the logged order.

**The gear blocks were invented per class and hardcoded in the simulator rather than held in the data, and had never been checked against each other.** Within a class the 31 versus 30 comparison was always valid, because both builds wear the same invented gear. Across classes the absolute numbers meant nothing at all.

That is the reason the blocks are now in `talent-data.json` where they can be seen, and the reason a comparison like this one had to come before any claim about cross-class balance.

## 3. Calibrated

Each class scaled on its highest logged spec until the canonical build lands within 4% of the logged number. Nine classes, nine targets, all inside 3.2%.

| Spec | Logged | Log share | Sim | Sim share | Gap |
|---|---|---|---|---|---|
| Warrior DPS | 1,411 | 100.0% | 1,390 | 100.0% | +0.0 |
| Rogue DPS | 1,151 | 81.6% | 1,186 | 85.4% | +3.8 |
| Mage Fire | 1,019 | 72.2% | 1,001 | 72.0% | -0.2 |
| Warlock DPS | 887 | 62.9% | 871 | 62.7% | -0.2 |
| Hunter Marksmanship | 856 | 60.7% | 825 | 59.4% | -1.3 |
| Druid Feral | 839 | 59.5% | 825 | 59.3% | -0.1 |
| Shaman Enhancement | 687 | 48.7% | 674 | 48.5% | -0.2 |
| **Shaman Elemental** | 675 | 47.8% | 697 | 50.2% | **+2.3** |
| Priest Shadow | 596 | 42.2% | 583 | 42.0% | -0.3 |
| Paladin Retribution | 524 | 37.1% | 512 | 36.9% | -0.3 |
| **Druid Balance** | 503 | 35.6% | 496 | 35.7% | **+0.1** |
| **Mage Frost** | 446 | 31.6% | 1,081 | 77.8% | **+46.2** |

## 4. Three of these are real tests and nine are not

**A calibration target cannot fail.** Nine specs were what the gear was fitted to, so their agreement proves nothing.

**The three second-specs are free tests.** Their gear was set by a different spec in the same class, and their output is whatever the reworked trees produce.

**Shaman Elemental lands +2.3 points off its logged share. Druid Balance lands +0.1.** Two independent predictions, both inside three points on a 68 point ladder. That is the strongest evidence in the project that the trees behave like the game rather than like a spreadsheet.

## 5. And one enormous deviation, which is the design working

**Mage Frost sits at 31.6% in the logs, last of twelve, and 77.8% under the rework.**

Vanilla Frost is not raid-viable. It has no scaling talents worth the points, its damage coefficients are poor, and it exists as a levelling and PvP spec that people abandon at 60. The rework rebuilt the tree.

**So the number is not a measurement error, it is the thing the rework was for.** Frost now sits roughly level with Fire.

**Whether level with Fire is right is a design decision rather than a measurement one.** Two readings are available. A spec that is dead last at a third of the top spec should not stay there, and parity with its sibling school is a defensible target. Or the rework has overshot and Frost should land somewhere in the sixties, below Fire but clearly playable.

**I would take the second.** Frost and Fire being interchangeable removes a choice rather than adding one, and the case for the rework is stronger if it can say Frost went from unplayable to competitive than if it says Frost and Fire are now the same.

## 6. Does the spread hold

| | Spread | Standard deviation |
|---|---|---|
| Logged | 68.4 | 19.6 |
| Sim, patchwerk | 64.1 | 19.1 |
| Sim, burst | 63.3 | 18.3 |
| Sim, cleave | 83.9 | 22.2 |

**Sustained and burst both sit slightly tighter than the logs**, which is what band neutrality predicts: the same ladder, marginally compressed.

**Cleave is 15 points wider and that is expected.** Several reworked trees carry periodic cleave levers added during the tuning passes, and the logged control is Patchwerk-style single target. A wider cleave spread means the classes that should be good on multiple targets now are.

## 7. What this does not establish

**The calibration fits nine classes to nine numbers, which any nine-parameter fit would do.** The claim rests entirely on the three free tests, and one of those three is a deliberate change. So the honest count is **two independent predictions, both correct within three points.**

That is meaningful but thin. Adding Season of Mastery and Season of Discovery as further controls would give more free tests, since specs shifted between those versions and the trees did not.
