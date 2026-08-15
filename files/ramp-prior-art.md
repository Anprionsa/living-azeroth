# How Other Games Solved the Ramp Problem

**August 2026**

*Research prompted by Necromancy reading -21.5% on a forty-five second fight. This is a solved problem elsewhere.*

---

## 1. The diagnosis is not new

Affliction warlock has had this exact problem for years, and the community named it precisely: <cite index="9-1">damage comparable to several other specs over an extended period, with no way to get the damage profile out quickly and meaningfully, and a weakness that isn't made up for with any benefit</cite>.

**That last clause is the design rule.** A ramp is not automatically bad. A ramp that buys nothing is. Affliction's problem was never that it started slow, it was that starting slow purchased no advantage later.

<cite index="12-1">The stated expectation was that Affliction starts slowly and ends on top if the target lives long enough, and players noticed when the sims showed it lowest in both</cite>.

## 2. Four mechanisms, all with prior art

### 2.1 Move the stacks from the target to the player

The most transferable finding. Unholy death knight's Midnight rework <cite index="19-1">replaced Festering Wounds with Lesser Ghouls stacked through Festering Strike, changing where the resource lives</cite>, and <cite index="21-1">the wounds became ghouls that stack on the player rather than on the target</cite>.

**A stack on the target must be rebuilt for every target and dies with it. A stack on the player is built once, survives the pull, and can be carried in.** That single relocation removes most of a ramp without removing the ramp.

### 2.2 Enter the burst window already stacked

Icy Veins states it as rotation advice: <cite index="23-1">enter the Dark Transformation window with high stacks of Lesser Ghoul, six to eight, so more of the window is spent summoning rather than building</cite>.

**The ramp is paid before the timer starts.** This only works if 2.1 is true.

### 2.3 An instant multi-summon

<cite index="19-1">Apocalypse summons four army ghouls at once, and aligned with a pet-damage cooldown produces roughly a twenty second window in which single-target damage triples</cite>.

Not a ramp at all. The army arrives whole.

### 2.4 A spender that converts a stack to damage now

<cite index="23-1">Putrefy summons and sacrifices a Lesser Ghoul to strike the target and then explode</cite>. **The stack is a currency rather than a timer**, which means holding it is a choice and spending it early is available when the fight is short.

### 2.5 And the simplest one: reduce the setup

Blizzard's own summary of the rework is that <cite index="21-1">the rotation now has significantly less setup, with cooldowns dropping from four or five to two</cite>. The Midnight tier list credits this directly: <cite index="10-1">the rework fixed a lot of the annoying ramp issues for Unholy DK</cite>, and separately that Demonology's <cite index="10-1">ramp is much lighter than before</cite>.

**Two of the strongest specs in the current expansion got there by having their ramps shortened.**

## 3. What was applied to Necromancy

**Corpse Harvest** now stacks Risen on the caster rather than on the field: they persist through a target's death, between pulls, and out of combat, up to three. That is 2.1.

**Sepulchral Study** makes summoning instant and castable before combat. That is 2.2.

**Boneyard** raises every Risen at once, immediately and at full strength, on a two minute cooldown. That is 2.3, and it is Apocalypse.

**Unstable Dead** already detonated Risen for damage, which is 2.4 and was authored earlier.

### 3.1 The simulator gap it exposed

Pre-pull summons were being applied at t=0 **and then cast again during the fight**, so the ramp was paid twice. Fixing that took burst from -25.6% to -10.6% on its own.

| | Before research | After |
|---|---|---|
| Burst | -21.5% | **-13.4%** |
| Patchwerk | +6.0% | +5.3% |
| Movement | +3.2% | +0.3% |

## 4. Honest assessment

**-13.4% is better and still outside the -5% floor.**

The remaining gap is that core Fire enters a forty-five second fight with Combustion, a cooldown worth a third of the fight, while Necromancy enters with three skeletons whose damage accrues at a fixed rate. **Prior art says the answer is a pet-damage amplifier aligned with the summon**, which is Dark Transformation, and Necromancy does not have one.

That is the next design step and it is a real talent rather than a magnitude: a cooldown that multiplies Risen damage for a window, taken alongside Boneyard so the army arrives and is immediately amplified. Unholy's entire single-target identity is <cite index="19-1">aligning Apocalypse with Dark Transformation</cite>, and Necromancy currently has the first half.

**The alternative remains accepting -13.4% as the tree's worst case.** Vanilla was full of specs that were bad in short fights, and a design that says "raising the dead takes a moment" is defensible in a way that a design saying "your damage is fifteen percent lower for no reason" is not.
