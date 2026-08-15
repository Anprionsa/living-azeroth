# First Simulation Run: What the Data Can and Cannot Tell Us

**August 2026**

*A minimal priority-loop simulator reading `talent-data.json`. The purpose was to find out whether the data produces numbers, not to produce trustworthy numbers.*

---

## 1. It runs, and the numbers separate

Warrior, six build shapes, twenty seeds each, 300 second fight, fixed gear.

| Build | Mean | Standard deviation | Range |
|---|---|---|---|
| Arms 31 / Fury 20 | 307 | 6.9 | 295 to 317 |
| Arms 30 / Fury 21 | 282 | 6.6 | 271 to 294 |
| Arms 26 / Fury 25 | 282 | 6.6 | 271 to 294 |
| Fury 31 / Arms 20 | 230 | 3.0 | 225 to 234 |
| Fury 30 / Arms 21 | 210 | 2.1 | 206 to 215 |
| Fury 26 / Arms 25 | 210 | 2.1 | 206 to 215 |

**Spread across shapes is 47%. Run-to-run noise is 2.7%.** The shapes are separable, which is the minimum condition for the exercise to be worth continuing.

## 2. Three bugs the run found that no amount of reading would have

**Talent-granted abilities were available to every build.** The rotation names Mortal Strike and Bloodthirst; the sim happily cast both regardless of whether the build owned the talent. A five-point Arms build was casting Mortal Strike. **This is the single most important finding**, because it means every earlier reasoning-based claim about what a build does was made against an assumption nobody had checked.

The fix reads two sources: authored `grant` effects, which cover 16 abilities, and the `grants` field derived from name matching, which covers 94. Using only the authored effects would have left 78 capstones freely available to builds that had not paid for them.

**The build selector never reached a capstone.** A greedy top-down fill spends 31 points on the first three rows. Real builds spend the minimum to open the deepest gate they can afford, and the selector now does that. Before the fix, an "Arms 31" build did not contain Mortal Strike.

**Execute had no health gate**, so it fired 177 times in a 300 second fight as the highest-priority free ability. Now gated to the last 20% of the fight.

## 3. What the numbers do not mean

**The absolute values are meaningless.** Roughly 300 damage per second against a Naxxramas-geared warrior's real output is off by an order of magnitude. The gear block is invented, Overpower has no dodge requirement, rage generation is approximated from one formula, and there is no armour, no boss resistance, and no raid buffs.

**Only Warrior is testable.** The other eight classes have rotations and abilities but too few authored effects for their builds to differ.

**Single target only.** Section 5.2 deliberately built talents around cleave, spreading, and target switching. `Opportunist` and the addTarget effects contribute nothing here, so any build whose advantage is multi-target reads as flat.

**The 30/21 and 26/25 shapes returned identical means.** That is correct rather than a bug: both reach gate 25 in the deep tree and gate 20 in the second, so the same talents are taken. It confirms the point math from Section 1.1 and means the two shapes are the same build described two ways.

## 4. What it says about the actual question

On this evidence, for warrior, **the capstone shapes beat the mid-tree shapes by roughly 9%**: 307 against 282 for Arms, 230 against 210 for Fury.

That is a real signal in the direction that matters, and it is bad news for Section 5.6. The tuning rule says two mid-tree seats should land in the same band as a capstone plus a shallow dip. **They do not, at least not for warrior in single target with the current magnitudes.**

Three readings, and the honest answer is that this run cannot separate them:

- The mid-tree talents are undertuned and need their magnitudes raised.
- The comparison is unfair because the mid-tree advantages are multi-target and this is a single-target test.
- The capstone is doing exactly what a capstone should and 9% is the correct premium.

**The third would be a good outcome and the first two are fixable.** What matters is that the question is now empirical rather than rhetorical.

## 5. What to do next

**Add a cleave scenario.** Two and four targets, same builds. If the mid-tree shapes close the gap there, reading two is correct and the design is fine.

**Author effects for one more class**, ideally Mage, where Frostfire is the clearest tag conversion and Fire and Frost is a genuine mutual pair. One class is an anecdote.

**Fix Overpower**, which currently has no dodge gate and dominates every warrior rotation at 86 to 116 casts. It is the largest single distortion in the numbers.

**Do not chase absolute accuracy.** The control is Warcraft Logs, per the protocol, and the comparison is relative. Effort spent making 307 into a realistic 1,400 buys nothing that effort spent on the cleave scenario does not buy better.

---

## 6. Second run, with the documented vanilla combat model

The first run used an invented combat model. This one implements what the era's own testing established: a single-roll attack table resolving miss, dodge, parry, block, glancing, crit, hit in that order; 40% glancing on white swings only against a level 63 boss, at 65% damage with 300 weapon skill; a 9% hit cap; armour mitigation against 3,731 boss armour; vanilla rage generation; 200% melee crits and **150% spell crits, not 200%**; and Overpower requiring an actual dodge rather than firing on cooldown.

**200 seeds, 300 second fight, single target.**

| Build | Mean | sd | Standard error |
|---|---|---|---|
| Arms 31 / Fury 20 | 292.2 | 14.4 | 1.02 |
| Arms 30 / Fury 21 | 283.4 | 12.2 | 0.86 |
| Fury 31 / Arms 20 | 251.1 | 17.2 | 1.21 |
| Fury 30 / Arms 21 | 231.4 | 13.1 | 0.92 |

**Arms: the capstone shape leads by 3.1%, z = 6.6. Fury: by 8.5%, z = 12.9.** Both significant, and both smaller than the 9% the crude model reported.

### 6.1 The combat model mattered more than the talents

The gap for Arms fell from 9% to 3.1% purely by modelling combat correctly. Two terms did most of that work.

**Overpower requiring a dodge.** In the first run it fired 96 to 116 times per fight as an off-cooldown filler. It now fires 24 times, gated on a 5.6% dodge chance. It had been the single largest distortion.

**Glancing blows and armour.** Forty percent of white damage arriving at 65%, and everything physical reduced by 38% from armour, compresses the distance between builds whose difference is a handful of special attacks.

**That is a general lesson rather than a warrior one.** A model that flatters one term will exaggerate whichever build uses it most, and the direction of the error is not predictable in advance.

### 6.2 Where this leaves Section 5.6

The tuning rule wants two mid-tree seats to land in the same band as a capstone plus a shallow dip. **Arms at 3.1% is arguably inside a band. Fury at 8.5% is not.**

Three targets changes little: 2.1% and 4.3%. The multi-target explanation for the gap does not survive, which removes one of the three readings from section 4.

So the remaining question is narrower and better posed: **is a 3% capstone premium correct and an 8.5% one too large, or should both be nearer zero?** That is a tuning decision about magnitudes, not a structural one about the design, and it is exactly the kind of question the dividend coefficient exists to answer.

### 6.3 Still not fixed

Rend at 66 casts is too many; it has no duration tracking, so it is refreshed constantly. Deep Wounds, Flurry, and every proc in the `procs` list are collected and never applied. Only warrior has enough authored effects to test. And the absolute numbers remain roughly a fifth of a real Naxxramas warrior's output, which is fine for a relative comparison and useless for anything else.

---

## 7. Third run: all nine classes, five fixes in

Five legitimate fixes since the last run, each found by the simulator disagreeing with itself.

**Duration tracking.** Maintenance spells were occupying every global cooldown: Rend at 66 casts, Scorch at 189. Rotation entries are now objects carrying `maintain` and `duration`, and 22 abilities are marked. Rend now fires 11 times and Scorch 11.

**Cast time.** Only the global cooldown gated casting, so a three second Frostbolt cost the same as an instant. Casters now spend their real cast time.

**Per-resource pools.** The model had one resource and a binary physical-or-caster split. **Druid, Paladin, Shaman and Hunter cast literally nothing**, because they held rage they could not spend on mana abilities. Rage, energy and mana are now tracked separately and each ability is paid from the one it costs. Rogue's energy also regenerates properly at 20 per two seconds rather than not at all.

**Combo points.** Finishers fired at any time, so Eviscerate spammed 55 times and Sinister Strike never appeared. Builders now add points, finishers require five and scale with what they spend. Rogue now opens with 67 Sinister Strikes.

**Seal of Command as a white-swing proc**, which is where Retribution's damage actually lives.

### 7.1 Results

| Class | Pair | 31/20 | 30/21 | Gap | Significant |
|---|---|---|---|---|---|
| Warrior | Arms + Fury | 277 | 270 | +2.9% | yes |
| Warrior | Fury + Protection | 244 | 225 | +8.4% | yes |
| Mage | Fire + Frost | 281 | 294 | **-4.2%** | yes |
| Mage | Arcane + Fire | 305 | 294 | +4.0% | yes |
| Warlock | Destruction + Demonology | 284 | 267 | +6.2% | yes |
| Rogue, Priest, Shaman, Druid, Paladin, Hunter | 8 pairs | | | 0.0% | no |

**Five of thirteen pairs are now testable across three classes, and every rotation casts something.** No pair returns zero casts.

### 7.2 The first result that supports the design

**Mage Fire plus Frost returns minus 4.2%: the mid-tree shape beats the capstone shape.**

That is the first evidence in the project that Section 5.6's tuning rule can hold. Across the five measurable pairs the premium runs from minus 4.2% to plus 8.4%, mean plus 3.5%, and one of five favours the mid-tree build.

That is a much better answer than "capstones always win," which is what the first two runs implied. **The premium is not a constant, it is a property of the specific pair**, which is what a working design should look like.

### 7.3 What the eight zeroes mean

They are not ties. Those pairs differ by six to eight talents each, and almost none of those talents have authored effects, so the simulator sees two identical characters. The set includes Shadow Mastery, Ruin, Dark Pact, Adrenaline Rush and Cold Blood.

**This is the 157 outstanding talents from the scope correction, and it is now the only thing standing between five testable pairs and thirteen.**

### 7.4 Honest state

Three classes give real numbers. Six do not, and the reason is data rather than modelling. The simulator now handles the vanilla attack table, glancing, armour, cast time, three resources, durations, periodic damage, combo points and talent-gated abilities.

**That is enough machinery. What it lacks is effects on the talents it is being asked to compare.**

---

## 8. Fourth run: eleven of thirteen pairs, eight of nine classes

Fifty-two more talents authored, and one further simulator bug that had been silencing most of the work.

### 8.1 Tag-scoped effects were collected and never applied

The modifier lookup checked the ability id and then fell back to `all`. **It never checked the ability's own tags**, and most authored effects are tag-scoped: Shadow Mastery multiplies damage on `shadow`, Ruin on `fire`, Moonfury on `arcane` and `nature`.

So five pairs read as exactly 0.0% while every one of their differing talents was authored. The data was fine and the consumer was ignoring it. Fixing the lookup to check ability, then tags, then all took eleven of thirteen pairs from six.

**That is the third time in this project that data was correct and the thing reading it was not.** The pattern is worth naming: when a measurement returns exactly zero, suspect the reader before the data.

### 8.2 Results

| Class | Pair | 31/20 | 30/21 | Gap |
|---|---|---|---|---|
| Warrior | Arms + Fury | 279 | 270 | +3.2% |
| Warrior | Fury + Protection | 244 | 226 | +7.9% |
| Rogue | Combat + Assassination | 156 | 159 | **-2.0%** |
| Mage | Fire + Frost | 343 | 293 | +17.3% |
| Mage | Arcane + Fire | 304 | 293 | +4.1% |
| Warlock | Affliction + Destruction | 320 | 316 | +1.3% |
| Warlock | Destruction + Demonology | 283 | 295 | **-4.0%** |
| Priest | Shadow + Discipline | 330 | 249 | +32.6% |
| Druid | Balance + Feral | 280 | 283 | **-1.1%** |
| Paladin | Retribution + Holy | 173 | 177 | **-1.9%** |
| Hunter | Marksmanship + Beast Mastery | 209 | 201 | +3.6% |

**Eleven of thirteen pairs testable across eight of nine classes. Mean premium +5.6%, median +3.2%, range -4.0% to +32.6%. Four of eleven favour the mid-tree shape and eight of eleven sit within five percent.**

### 8.3 What this says about Section 5.6

The tuning rule wanted two mid-tree seats to land in the same band as a capstone plus a shallow dip. **On eight of eleven pairs it does, and on four the mid-tree shape is ahead.**

That is a genuinely good result and it is the first time the design has been supported rather than questioned by evidence.

**Two outliers need attention rather than celebration.**

Priest at +32.6% is not credible. Shadowform, Shadow Weaving and Darkness each multiply shadow damage, and the sim stacks them multiplicatively on a rotation that is entirely shadow. That is a magnitudes problem in the authored effects, not a design finding.

Mage at +17.3% has the same shape: Fire and Frost both multiply a damage school and the 31-point build reaches Combustion.

**Both are the same failure: several talents multiplying the same tag compound, and nobody checked the product.** That is exactly the kind of thing the dividend coefficient work will have to police, and it is now visible rather than theoretical.

### 8.4 Remaining

Rogue Assassination plus Subtlety and Shaman Elemental plus Enhancement still read zero. Their differing talents are authored, so the cause is that their effects are of kinds the simulator collects but does not yet act on: procs, `addTarget` on single target, and resource changes that do not bind.

That is a simulator gap rather than a data gap, and it is the smallest remaining item.
