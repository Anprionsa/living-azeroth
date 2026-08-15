# Placeholder Text and Resource Pacing

**August 2026**

---

## 1. Twenty-two talents were never rebuilt

Chasing the Hunter switching outlier led to Mortal Strike, and Mortal Strike turned out to be **unmodified vanilla text sitting in a capstone slot**. Bloodthirst read *"Your this effect lasts 8 sec"*, which is a broken string from an automated rewrite that never completed.

A scan found **twenty-two talents still carrying vanilla wording**, most with `N%` and `N sec` placeholders: Shatter, Arcane Power, Combustion, Frost Warding, Improved Blizzard, Arctic Reach, Vindication, Pursuit of Justice, Heart of the Wild and thirteen others.

**Every one of them is a talent the project claims to have rebuilt.** They are now written in the same idiom as the rest, and a `no-placeholder-text` rule fails the build on `N%`, `N sec`, or a broken `Your this` construction.

Both documents regenerated: 27 core blocks and 17 expanded blocks, zero unidentified.

## 2. The resource fix, which was the actual Hunter answer

Trueshot makes Aimed Shot instant. Measured, it made the hunter **worse** by 16.4% on target switching.

The reason was not the talent. **A rotation ranked purely on damage per second is correct only when the resource is free.** Removing a cast time freed global cooldowns, the hunter filled them with cheap Arcane Shots, and those burned the mana Aimed Shot needed. The capstone made the build spend faster on worse spells.

Two changes:

**Priority now blends throughput with efficiency** in proportion to how constrained the resource is over the fight, computed per scenario rather than authored.

**A caster low on mana stops casting its expensive spells.** Below thirty percent of pool it falls back to efficient ones. Spending the pool freely and then idling is not what anyone does, and it was what the simulator did.

**Hunter Marksmanship went from -16.4% to +0.4% on switching and is now inside five percent on all five scenarios.** Aimed Shot went from twelve casts to thirty-seven and became the hunter's primary, which is what a marksman should be doing.

## 3. And the warrior cleave gap halved on its own

Fury plus Protection went from **-14.4% to +3.7%** on cleave with no tuning, because Bloodthirst's rewritten text gave it reach against a bleeding target and the effect now matches the words.

Arms remains at -13.3%. Mortal Strike's wound now spreads through Cleave and Whirlwind, which helped, but the 30/21 build takes Death Wish instead and a universal damage cooldown beats a single-target strike on three targets.

**That one is a genuine design trade rather than a bug**, and it is the same shape as a cooldown capstone exceeding the band on burst.

## 4. Core

| Scenario | n | mean | median | within 5% |
|---|---|---|---|---|
| patchwerk | 7 | +4.0% | +4.5% | **7/7** |
| movement | 8 | +2.6% | +2.8% | **8/8** |
| cleave | 5 | -1.5% | +1.8% | 4/5 |
| burst | 7 | +6.2% | +4.3% | 4/7 |

## 5. Standing note

Three of the last five passes found the same thing in a different place: **a field existed, nothing read it, and the number that resulted looked like a finding.**

Unread effects, unreachable abilities, and now unrewritten text. The rules added in response are `grant-reachability`, `no-placeholder-text`, `no-broad-zeroing` and `percentage-drift`, and each one exists because something got that far without being caught.
