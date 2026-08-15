# Reading Pass

**August 2026**

*Checking the rewritten talents against the voice of the trees around them.*

---

## 1. The established voice, read off the untouched talents

> Shouts affect the raid. Persist through death. Refresh on a killing blow. Cost no rage below 20 rage.

> Your demon inherits your resistances and your armor. It returns at 30% health thirty seconds after dying.

> Demoralizing Shout also reduces the target's critical strike chance. It applies to targets behind you. It cannot be dispelled.

**Bare declarative sentences, one per rank, no rank markers.** The reader infers that each sentence is a rank because the sentences arrive in order.

## 2. What the simulation work introduced

**Sixteen talents used an "At two ranks... At three..." construction.** Every one of them was written during the tuning passes. None of the original text does this.

> Critical strikes cause bleeding. **At two ranks** the bleed does not fall off early. **At three** a bleeding target takes every third blow as though it were two enemies.

That is design-doc voice explaining a mechanism to a reader outside the game. Rewritten:

> Critical strikes cause bleeding. The bleed does not fall off early. A bleeding target takes every third blow as though it were two enemies.

**Dark Pact used a colon introducing a list**, which is the same fault in a different shape, and **Envenom said "stack two higher than their maximum"**, which states a number where the convention states a behaviour.

## 3. And the reading pass found something the rules had missed

**Nineteen talents were still carrying raw vanilla text with N placeholders.**

> Gives you a **N%** chance of entering a Clearcasting state after any damage spell hits a target.

> After killing a target that yields experience or honor, gives you a **N%** increased critical strike chance on your next Ambush, Garrote or Cheap Shot.

The `no-placeholder-text` rule had been matching `by N%` and `N sec` and missed `a N% chance`, which is the more common phrasing. **The rule was passing on nineteen talents it existed to catch.**

Widened, and all nineteen rewritten:

> Damage spells may leave you Clearcast, so the next costs nothing. Clearcasting also removes the next spell's cast time.

> Killing a target raises the critical strike chance of your next opener. The bonus holds through two openers.

## 4. Totals

| | Count |
|---|---|
| Rewritten to the established voice | 19 |
| Raw vanilla placeholders rewritten | 20 |
| Final voice fixes, colon list and stated number | 3 |
| **Total talents rewritten this pass** | **42** |

Both documents regenerate with zero stale text. `vanilla-voice` and `no-placeholder-text` both pass. Zero em dashes.

## 5. On Warrior and Runeblade

**Correct, and the effect is larger than expected.** Warrior's narrowness at one capstone-free shape was measured on the core configuration, where its third tree is Protection and a damage build gets nothing from it.

With Runeblade available the class has three damage-relevant trees, and the capstone-free space goes from **1 shape within seven percent to 79**, with Runeblade appearing in 66 of them.

**That makes Warrior's core narrowness an argument for the expanded configuration rather than a fault in the core one.** It is the clearest case in the project of an absorbed tree solving a structural problem rather than adding content.

Runeblade needed retuning to sit in band after the Death Wish and tie-break changes, and now reads +5.2% sustained with its cleave lever sized to every fourth strike.

## 6. Dreamer and Radiance

Moved to a third configuration, `candidate`. **Held out rather than deleted**: the data is whole, both trees remain authored and validated to the same standard as everything else, and switching them on is a configuration change rather than rework.

`validate.py core` and `validate.py expanded` both pass clean with them excluded. The expanded set is now 27 rebuilt plus 7 absorbed plus Chronomancer.
