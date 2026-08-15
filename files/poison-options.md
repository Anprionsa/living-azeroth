# Modelling Poisons

**August 2026**

*Master Poisoner is unmeasurable because poisons are not modelled. It turns out to be nine talents, not one.*

---

## 1. What the audit found

A new check asks whether an effect is scoped to a tag any ability actually carries. **Nine talents across all three rogue trees modify `poison`, and no ability carries that tag.**

Envenom, Toxicology, Blade Venom, Master Poisoner, Vitality, Cutthroat and Deadened Nerves are all modifying nothing. **This is the same shape as the unread effects and the unreachable abilities, in a place nothing had looked.**

What those nine promise, collectively: poisons stack and the stacks matter, they apply from strikes and finishers and off-hand attacks and openers, they can be spent by a finisher for damage, and they can be made uncleansable.

## 2. Four options

### Option A: model poisons properly

Four abilities, applied on weapon swings at a proc chance, with Deadly Poison stacking to five. Poison damage becomes a real stream that the nine talents modify.

**Catches:** all nine talents, including Master Poisoner's specific change, which is skipping the stack ramp. Makes Assassination measurable as the poison tree it is meant to be.

**Costs:** four abilities with proc rates, a stack counter per target, application from three different sources, and a spend interaction with finishers. It is the largest single modelling addition since pets.

**Risk:** poisons are roughly a third of a vanilla rogue's damage, so getting the rate wrong moves every rogue number. Rogue is currently the best-behaved class in the suite at +0.6% across four scenarios.

### Option B: poison as a damage stream

A flat contribution proportional to weapon swings, scaled by whatever modifies the poison tag. No stacks, no application sources.

**Catches:** seven of nine talents, since most are damage percentages on the tag.

**Misses:** Master Poisoner, exactly. Its whole change is to the ramp, and a stream has no ramp. Also misses Blade Venom's spend and Deadened Nerves's opener interaction.

**Costs:** small. An hour of work.

**This option does not solve the problem that prompted it.**

### Option C: model the ramp only

A single stack counter that builds on swings and caps at five, with poison damage proportional to stacks. Master Poisoner sets it to full immediately.

**Catches:** Master Poisoner, Envenom and Toxicology's higher maximum, and Blade Venom's faster application. Four of nine.

**Costs:** moderate. A counter and a stack-to-damage curve, no separate abilities.

**This is the minimum that makes the talent that prompted the question measurable**, and it is honest about being a partial model.

### Option D: leave it

Mark all nine `simulable: false` and argue them.

**Costs:** nothing, and it is what the project already does for Repentance.

**But Repentance is a stun and genuinely has no throughput. Poisons are damage.** Marking a damage mechanic unsimulable because it has not been built is a different act from marking a stun unsimulable because it cannot be.

## 3. Recommendation

**Option C**, with a note that it is partial.

Option A is correct and I would not start it without a reason beyond one talent. **Rogue is currently the best-behaved class in the suite, and a third of a rogue's damage arriving as a new stream would move every rogue number in the project.** That is a large risk to take for measurement fidelity on a tree that is already in band.

Option C makes Master Poisoner measurable, catches four of the nine, and leaves the numbers where they are because a ramp that starts at zero and ends at full averages out close to the flat value the sim currently has implicitly.

**Option B is the one to avoid.** It looks like progress, costs the least, and specifically fails to measure the talent that prompted the work.

## 4. What I would want before committing to A

The question is whether the other rogue talents are correct, and there is a cheaper way to find out than building the model: **check whether Assassination's nine poison talents leave it inside the band at all.** It currently reads +0.6% with those nine doing nothing, which means the tree is in band without them.

**If a tree is balanced while a third of its mechanics are inert, adding them will unbalance it.** That is worth knowing before choosing, and it is one measurement rather than a build.

---

## 5. The measurement, taken

**Assassination plus Subtlety reads exactly 0.0% on every scenario.** Its capstone is Master Poisoner, which modifies a tag no ability carries, so the comparison is between two identical characters.

That is not a tree that is in band. **It is a tree that is unmeasured**, and the +0.6% figure reported for rogue in earlier passes came from Combat, not Assassination.

This changes the recommendation. **Option C is no longer the minimum, it is the requirement**, because without some poison model Assassination has no measurable capstone at all and one of the thirteen core pairs is permanently blank.

It also raises the value of Option A. If Assassination is entirely unmeasured, there is no in-band result to protect, and the risk that made Option A unattractive largely disappears.

**Revised recommendation: Option C now, Option A when the rest of the suite is stable.** C makes the pair measurable and catches four of nine talents. A is the correct model and can be built against a tree that C has already brought into the light, rather than against one nobody has ever measured.
