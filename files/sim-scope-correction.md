# The Authoring Scope Was Measured Against the Wrong Build Model

**August 2026**

*A correction, found by running the simulator on all nine classes instead of one.*

---

## 1. What happened

REG-62 established that a simulator comparing 31/20 against 30/21 only needs the talents that **differ** between the two builds, and computed that set at 69 talents. All 69 were authored. That number was reported as the minimum viable scope and used to declare the work tractable.

The set was computed with a greedy build selector that fills talents top down. **The simulator uses a different selector**, one that spends the minimum to reach the deepest affordable gate and then fills upward, because a greedy fill never reaches a capstone. That fix was made later, when the first run showed an "Arms 31" build containing no Mortal Strike.

Two different selectors produce two different builds, which produce two different sets of differing talents.

| | Talents |
|---|---|
| Scope under the greedy selector | 69 |
| Scope under the selector the simulator actually uses | **197** |
| Overlap between them, by name | 33 |
| Authored, and no longer in scope | 36 |
| Authored and still in scope | 40 |
| **Still needing effects** | **157** |

**Just over half the authoring work went to talents the simulator never compares.**

## 2. How it surfaced

Running all nine classes returned exactly 0.0% for seven of thirteen pairs. The builds were not identical: rogue Combat against Assassination differed by eight talents, warlock Affliction against Destruction by eight.

But of those sixteen differing talents, **two had authored effects.** The rest were empty, so the simulator saw two identical characters. And the fourteen empties included Shadow Mastery, Ruin, Dark Pact, Adrenaline Rush, and Cold Blood, which is to say the signature talents the whole build-diversity argument is named after.

A single-class test could not have caught this. Warrior worked because Warrior Arms was hand-authored as the reference tree, so its talents were covered whichever selector picked them.

## 3. The second bug, which is smaller but blocks Mage

Mage returned +52.2% for two different pairs with identical numbers, which is the signature of a result that does not depend on the input.

The cause is that Scorch sits first in the Mage rotation and is cast 189 times in a 300 second fight. It is a maintenance spell whose value is a stacking debuff, and the simulator has no duration tracking, so it never falls off and never yields priority. Every Mage build reduces to Scorch spam.

**This is the same class of bug as Rend at 66 casts on Warrior.** Any rotation containing a maintenance effect is currently meaningless without duration tracking, which is now the single highest-value fix to the simulator itself.

## 4. What this says about the method rather than the data

Three findings in this project have now come from running something rather than reading it: the renderer exposed 72 talents with no stated effect, the validator rediscovered REG-25 unprompted, and the simulator has now found that a scope calculation everyone accepted was measuring the wrong thing.

The common shape is that **a derived number inherits every assumption of the thing that derived it**, and those assumptions are invisible until something downstream disagrees. The 69 was correct arithmetic on a build model that was replaced eleven steps later, and nothing rechecked it because nothing had to.

The fix that generalises: **any derived set should be recomputed by whatever consumes it, not stored.** `sim-authoring-scope.json` is now regenerated from the simulator's own selector rather than from a separate calculation, so the two cannot drift again.

## 5. Where this leaves the numbers

Warrior remains the only class whose results mean anything: capstone shapes lead by 3.5% for Arms and Fury, significant across 200 seeds, and three targets does not change it.

**One class is an anecdote.** The claim in REG-70 that the capstone premium is 3 to 8 percent stands only for Warrior, and should not be generalised until at least three classes are testable.

Order of work: duration tracking in the simulator first, because it blocks Mage and distorts Warrior; then the 157 talents; then rerun all nine.
