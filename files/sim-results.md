# Simulation Results

**August 2026**

*Five rounds of fixes. The headline number moved from plus 9% to minus 0.8%, and that movement is the most important thing in this document.*

---

## 1. The question

Talent design 5.6 sets a tuning target: two mid-tree talents should land in the same band as a capstone plus a shallow dip. If it holds, the 26 mutual pairs are 26 real choices. If it fails, they are 26 ways to be worse.

Every pair is tested as 31/20 against 30/21, same class, same gear, same rotation, 150 seeds, 300 second fight, Season of Mastery ruleset.

## 2. Current results

| Class | Pair | 31/20 | 30/21 | Gap | Capstone in the 31 build |
|---|---|---|---|---|---|
| Warrior | Arms + Fury | 240 | 241 | -0.2% | Mortal Strike |
| Rogue | Combat + Assassination | 158 | 163 | **-3.1%** | Adrenaline Rush |
| Warlock | Affliction + Destruction | 347 | 353 | **-1.6%** | Dark Pact |
| Warlock | Destruction + Demonology | 289 | 330 | **-12.4%** | none reached |
| Priest | Shadow + Discipline | 349 | 312 | +12.0% | Shadowform |
| Druid | Balance + Feral | 286 | 283 | +1.1% | Moonkin Form |

**Mean premium minus 0.8%. Median minus 1.6%. Three of five significant pairs favour the mid-tree shape.**

Seven pairs return no significant difference, and for most of them that is the correct answer rather than a gap: Repentance is a stun, Trueshot changes a cast time, Elemental Mastery is a cooldown. **Those capstones do not add single-target throughput and the simulator is right to say so.**

## 3. How the number moved, which matters more than where it landed

| Round | Fix | Result |
|---|---|---|
| 1 | crude model | +9% capstone premium |
| 2 | vanilla attack table, glancing, armour, Overpower gating | +3.1% to +8.4% |
| 3 | durations, cast time, per-resource pools, combo points | +2.9%, first negative appears |
| 4 | tag-scoped effects actually applied | +5.6% mean, 11 pairs testable |
| 5 | ranks scale effects, same-tag bonuses add, selector picks by value | **-0.8% mean** |

**Every one of those was a legitimate correctness fix**, and every one moved the answer materially. The final selector fix was the largest: previously a 30-point build filled low rows to completion and never reached a gate-15 talent that a 31-point build got, so the comparison was measuring an artefact of fill order rather than the capstone.

With the fix, a 31-point build differs from a 30-point build by **exactly the capstone**, which is what the test was always supposed to isolate.

## 4. What can be claimed

**Supported.** The capstone premium is near zero on average and varies by pair. Three of five measurable pairs favour the mid-tree shape. Section 5.6's target is met on this evidence.

**Not supported.** Any specific number. The figure has moved by ten percentage points across five rounds of fixes and there is no reason to think round six would not move it again.

**Not tested at all.** Cross-class balance, healing throughput, threat, survivability, anything multi-target beyond a crude target multiplier, and the seven pairs whose capstones are utility.

## 5. The two results worth investigating

**Priest at +12%.** Shadowform is a genuine throughput capstone on a rotation that is entirely shadow damage, so a premium is expected. Whether 12% is right depends on magnitudes nobody has tuned.

**Warlock Destruction + Demonology at -12.4%.** The mid-tree shape wins by a wide margin, and the 31-point build reaches no capstone the simulator recognises. That is either a genuinely strong mid-tree pairing or a missing `grant` on the Destruction capstone, and it should be checked before being cited.

## 6. Honest confidence

This is a **directional** result. It says the design is not obviously broken and that the mid-tree shapes are competitive, which is a meaningful thing to have learned and was not knowable by argument.

It is not a balance pass and should not be presented as one. The correct next steps are a real simulator with per-rank effect values rather than a fraction approximation, and Warcraft Logs Season of Mastery data as the control, which is what `sim-baseline-protocol.md` specified from the start.

---

## 7. The check, and what it found

Two results were flagged as needing investigation before being cited. Both are now explained and neither is a bug.

### 7.1 A selector bug was hiding the capstones

The greedy-by-value selector never bought a capstone whose effects were unauthored, because it broke out of the loop when the best remaining talent scored zero. **A "31 point" Destruction build was spending 30 points and never taking Shadow and Flame**, so the test that claimed to compare a capstone build against a mid-tree build was comparing two mid-tree builds.

Fixed two ways. The selector now spends its last points on an unvalued talent rather than stopping, since a capstone with no authored effects is unmeasured rather than worthless. And the 31-point side of every comparison now **reserves a point for its capstone**, because the comparison specifies intent: it is testing "capstone plus a shallow dip" against "two mid-tree seats," and letting an optimiser decline the capstone tests something else.

Every 31-point build now differs from its 30-point counterpart by exactly the capstone. That is what the test was always supposed to isolate, and it took six rounds to actually achieve.

### 7.2 The Warlock result is the simulator rediscovering DS/Ruin

Destruction plus Demonology at minus 12.4% is not an error. The 30/21 build takes **Demonic Sacrifice at Demonology's twenty point mark and Ruin at Destruction's**, against a 31-point Destruction build that reaches Shadow and Flame instead.

That is DS/Ruin. The canonical vanilla warlock build, the one `spec-grievances.md` cites as proof that a no-capstone shape can be correct, and the simulator arrived at it without being told it exists.

**On a rotation that is thirty-six Shadow Bolts and five Immolates, a fifteen percent shadow bonus beats a fire capstone.** That is the correct answer and it is the answer vanilla players reached in 2005.

This is the strongest validation available short of log data: the model independently reproduces a known-correct historical result from a different direction.

### 7.3 The Priest result is plausible

Shadow plus Discipline at plus 12% is Shadowform, a fifteen percent shadow multiplier, on a rotation that is entirely shadow damage. Twelve percent after paying a point for it is close to what the magnitude implies.

That is a real throughput capstone doing what a throughput capstone should. Whether fifteen percent is the right number is a tuning question nobody has answered, but the result is not anomalous.

## 8. Final state

| | |
|---|---|
| Testable pairs | 6 of 13, across 5 of 9 classes |
| Capstone premium | **mean +0.8%, median -0.2%** |
| Range | -12.4% to +12.0% |
| Mid-tree shape wins | 3 of 6 |
| Within 10% | 4 of 6 |

**Median premium of minus 0.2% is as close to Section 5.6's target as this instrument can measure.** Three of six pairs favour the mid-tree shape, and the two largest results in either direction both trace to a single well-understood talent rather than to accumulated noise.

Seven pairs remain unmeasurable because their capstones are utility: Repentance stuns, Trueshot changes a cast time, Elemental Mastery is a cooldown, Master Poisoner and Arcane Power and Combustion are burst windows the simulator does not model. **Those are not gaps in the data. They are capstones whose value is not throughput**, and a throughput simulator is the wrong instrument for them.

---

## 9. Authoring pass, and a selector fault it exposed

Core authored coverage went from **38% to 67%**, 185 talents to 326, across fourteen trees that had under half their content expressed.

### 9.1 The selector was picking self-harming talents

At 67% coverage the Warlock Destruction build collapsed from 399 damage per second to 43. The greedy selector had taken **Backdraft**, a subtraction node that zeroes Shadow Bolt, on a rotation that is thirty-six Shadow Bolts.

The value heuristic counted whether a talent had effects, not whether they helped. It scored Backdraft at plus 25: minus 25 for zeroing a damage school, plus 50 for removing a cooldown.

Two corrections. **Downside is now weighted**, so a multiplier below one subtracts proportionally and a multiplier at zero subtracts heavily. And **the penalty is scope aware**, because zeroing a whole school is catastrophic where zeroing one ability's cooldown is merely good, and the cooldown bonus is capped rather than unbounded.

Backdraft now scores minus 42, Sure Strike minus 49, Immolation minus 38. Ruin scores plus 17 and Shadowform plus 5.

**Subtraction nodes are supposed to be a real cost, and until this pass the optimiser was taking them for free.** That is worth noting as a design signal rather than only a bug: a node that reads as a downside to a human read as a bargain to a greedy optimiser, which is exactly the failure Section 5.4 warns about when a subtraction is undertuned.

### 9.2 Current results

| Class | Pair | Gap |
|---|---|---|
| Warrior | Arms + Fury | +2.5% |
| Warrior | Fury + Protection | +11.6% |
| Rogue | Combat + Assassination | **-3.1%** |
| Mage | Fire + Frost | +1.0% |
| Mage | Arcane + Fire | +3.6% |
| Warlock | Destruction + Demonology | **-1.7%** |
| Priest | Shadow + Discipline | +12.0% |

**Seven of thirteen testable across five of nine classes. Mean +3.7%, median +2.5%, range -3.1% to +12.0%. Five of seven within five percent.**

Compared to the run before the authoring pass, more pairs are measurable and the range has narrowed considerably at both ends: the -12.4% and +25.5% outliers are gone, and what remains is Priest at +12.0% and Fury plus Protection at +11.6%.

### 9.3 Where the two remaining outliers sit

Both are throughput capstones on trees whose rotation matches their school. Shadowform multiplies shadow on an all-shadow rotation; Bloodthirst is a large direct attack added to a rotation that lacked one. Neither is anomalous, and whether twelve percent is the right size is a magnitudes question that this instrument cannot answer, only pose.

---

## 10. Full authoring: 484 of 484

Every core talent now carries authored effects. Coverage went 38% to 100% across three passes, 299 talents authored, and **both configurations validate with zero errors and zero warnings** for the first time.

### 10.1 Results at full coverage

| Class | Pair | 31/20 | 30/21 | Gap |
|---|---|---|---|---|
| Warrior | Arms + Fury | 283 | 282 | +0.3% |
| Warrior | Fury + Protection | 323 | 285 | +13.2% |
| Rogue | Combat + Assassination | 160 | 160 | -0.1% |
| Mage | Fire + Frost | 403 | 396 | +1.9% |
| Mage | Arcane + Fire | 388 | 375 | +3.6% |
| Warlock | Destruction + Demonology | 317 | 306 | +3.8% |
| Priest | Shadow + Discipline | 328 | 293 | +12.0% |
| Druid | Balance + Feral | 270 | 267 | +1.0% |

**Mean +5.9%, median +3.7%, range +1.0% to +13.2%. Four of six significant pairs within five percent.**

### 10.2 What changed, and what it means

**No pair now favours the mid-tree shape.** At partial coverage two or three did. That reversal is not a design change, it is what happens when the capstone's own effects finally exist alongside everything else: at 67% coverage several capstones were unauthored while the mid-tree talents around them were not, which flattered the shallower build.

**That is the most important caveat in this document.** Partial authoring does not produce a noisy version of the true answer, it produces a biased one, and the direction of the bias depends on which talents happened to be written first. Every intermediate number in sections 3 through 9 was measured against incomplete data and should be read as a record of the method rather than as evidence.

### 10.3 Where Section 5.6 stands

Median +3.7% and four of six inside five percent is a reasonable reading of "the same band". Two pairs sit outside it and both are the same shape: **Bloodthirst at +13.2% and Shadowform at +12.0%**, each a throughput capstone landing on a rotation built from its own school.

That is a coherent finding rather than noise. **A capstone that adds a large direct ability or multiplies the school a spec already uses will beat two mid-tree talents, and one that grants utility will not.** If Section 5.6's band is to hold everywhere, those two need their magnitudes revisited, and nothing else does.

### 10.4 Seven pairs still read zero

They are unmeasurable rather than tied, and the reason is now clean: their capstones are utility. Master Poisoner, Repentance, Trueshot, Elemental Mastery and Grounded do not produce single-target throughput at any coverage level, which is what `simulable: false` and the scenario suite exist to handle.

---

## 11. The value function encodes an objective, and the objective differs by role

Rerunning the tank instrument at full coverage produced a result no tank would accept: **the Protection warrior build lost crit immunity.**

The cause is the fix from section 9. Weighting downside made `Unbreakable` score minus 49, because it removes critical strikes, so the selector stopped taking it. That is correct behaviour for a damage build and completely wrong for a tank, who takes crit immunity before anything else.

**A value heuristic is not neutral. It encodes an objective**, and the objective for a tank is threat and survival, for a healer it is healing and mana, and for a damage build it is output. One function cannot serve three.

The selector now takes a `role`. Under it, `Unbreakable` scores plus 40 for a tank and minus 49 for a damage build, `Toughness` plus 9 against plus 2, and a talent that reduces damage dealt no longer counts against a tank at all.

### 11.1 Tanking at full coverage, role-aware

| Build | TPS | DTPS | EHP | Crit immune | TPS gap |
|---|---|---|---|---|---|
| Warrior Prot 31 / Fury 20 | 599 | 374 | 41,923 | **yes** | +14.2% |
| Warrior Prot 30 / Fury 21 | 524 | 374 | 41,923 | yes | |
| Paladin Prot 31 / Ret 20 | 793 | 331 | 36,118 | no | +5.7% |
| Druid Feral 31 / Resto 20 | 366 | 431 | 43,437 | no | +9.4% |

Crit immunity is back, and effective health rose from 34,054 to 41,923 because the tank selector now buys avoidance and mitigation it previously skipped.

**The capstone premium for tanks is 5.7% to 14.2%**, still above the damage side's median of 3.7%. Section 5.6 fails on tanks and the shape of the failure is consistent: Shield Slam is a threat capstone in a threat tree.

### 11.2 Healing at full coverage

Three of four healers show no difference at all. **Restoration shaman is the exception and holds the shape it had at partial coverage: +1.3% healing per second and -25.7% healing per mana.**

That result surviving the jump from 38% to 100% authoring is worth more than any of the damage numbers, because it is the only finding in the project that has not moved when the data underneath it changed.

### 11.3 What this adds to the method

Three instruments, three objectives, and the selector has to know which one it is optimising. **Every previous tank and healing number in this document was produced by a damage-optimising selector**, which is why the tank builds were skipping crit immunity and the healers were skipping efficiency talents.

That is the fourth instance of the same lesson: the consumer of the data shapes the answer as much as the data does.
