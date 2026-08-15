# Ready for Design

**August 2026**

*What the simulation work settled, what it changed, and what it cannot answer.*

---

## 1. Yes, with two caveats worth reading first

Everything checkable is clean. **484 of 484 core talents and 212 of 212 expanded talents authored. Both configurations pass 24 rules with zero errors and zero warnings. Nine completeness checks report nothing outstanding. Both documents regenerate from the data with zero stale text.**

Two things were not ready when the question was asked and are now: **four talents had drifted out of the talent document** during tuning, and **41 of 90 files were missing from the manifest**, which is the file a reader opens first.

## 2. What it settled

**Talent design 5.6's tuning rule holds.** Every core pair sits inside -7% to +7% against its mid-tree alternative across all five scenarios. Fifty cells, zero violations.

**Hybrids are real builds.** Every class has a capstone-free build within 6.3% of its best capstone build, and four of six have one that beats it. Rogue's is a three-tree split.

**The band was chosen on evidence.** Three policies were priced against fifty cells. A signature-scenario exemption, which I had argued for across four passes, **performed worse than simply widening the band** and was dropped.

## 3. What it changed about the design

Eleven talents were rewritten because measurement showed they did not work.

**Dark Pact** returned mana to a build that had enough, and the 31-point build measured as worse than the 30-point one. **Shadow and Flame** paid for alternating two spells cast thirty-nine and three times. **Unbound** said *"you may have two demons active at once"* and was authored as a damage percentage, so the talent that makes a Demonology splash worth taking did not do the thing it describes. **Death Wish** carried both a permanent bonus and a cooldown, which made one point worth ten percent and left Warrior with a single viable hybrid.

**Nine rogue talents modified a `poison` tag no ability carried**, so Assassination read exactly 0.0% on every scenario since the project began.

**Thirty percent of authored talents had drifted into percentages**, which is what Section 5.2 deleted. The repair took it to a median tree with no primary-school damage percentage at all.

## 4. The reusable result

**Scenario levers.** A periodic cleave gained 18.8 points on three targets at **zero cost on one**. An opening window gained 4.8 points of burst per point of sustained. A pet amplifier gained 2.4.

**A lever that pays everywhere is a buff. A lever that pays in one place is a fix.** And it must sit on the talent that differs between the two builds, or it lifts both and closes nothing, which I got wrong three times before writing it down.

## 5. What it cannot answer

**Absolute numbers.** The figures are relative and the gear blocks are invented. A real balance pass needs Warcraft Logs Season of Mastery data as the control, which `sim-baseline-protocol.md` specified from the start and which has never been done.

**Anything not throughput, threat or healing.** Twelve talents carry `simulable: false`. Repentance is a stun and no damage simulator will ever measure it. Six effect combinations remain unread and are mobility, radius and spell reflection.

**Whether the design is fun.** The instrument says a hybrid is within six percent. It cannot say whether anyone wants to play one.

## 6. Where design should pick up

**The eleven rewritten talents need reading as prose**, not as numbers. They were rewritten to satisfy a measurement and their text should be checked against the voice of the trees around them.

**Warrior's narrowness is a design decision rather than a fault.** One capstone-free shape within seven percent, because its third tree is Protection and a damage build correctly gets nothing from it. Hunter has the same structure and reaches 28 because Beast Mastery still hands a damage build a pet. **Whether Warrior should have a third damage-relevant tree is a design question the simulator surfaced and cannot settle.**

**Dreamer and Radiance remain candidates.** They were authored, validated and simulated, but the decision to include them was never made.
