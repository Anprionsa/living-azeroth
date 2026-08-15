# Ability Coverage

**August 2026**

*The same audit applied to abilities that `coverage.py` applied to effects: which exist, which are reachable, and which carry the data the simulator needs.*

---

## 1. Eighteen granted abilities were never cast

A talent that grants an ability which appears in no rotation grants nothing. **Eighteen abilities dealing real damage were in that state**, including Shield Slam, Ambush, Riposte, Ghostly Strike, Blast Wave, Blizzard, Flamestrike, Rain of Fire, Guardian Spirit and Raptor Strike.

**Every talent granting one of those was measuring as worthless.** They are now added to their class rotations and ordered by throughput, and a `grant-reachability` rule fails the build if it recurs.

## 2. Area abilities had no target gate

Blizzard, Flamestrike, Rain of Fire, Thunder Clap, Hellfire and eleven others are a loss on one target and a gain on several. Without a `minTargets` field they either never entered a rotation or displaced single-target casts on Patchwerk.

Sixteen abilities now carry `minTargets` and the simulator skips them below it. A handful of situational singles carry a `condition` instead: Revenge only after a dodge, Hamstring and Wing Clip never in a damage rotation.

## 3. Twelve abilities that were cast had no scaling at all

Rip, Arcane Shot, Serpent Sting, Eviscerate, Rupture, Hammer of Wrath, Exorcism, Swiftmend, Insect Swarm, Ferocious Bite, Bloodthirst and Bone Armor were all being cast with a flat value and **no attack power or spell power coefficient**, so they did not grow with gear at all.

**Bloodthirst is the one that mattered.** Its damage in vanilla is entirely attack-power-based and its base is zero, so it was dealing nothing. Giving it 0.45 attack power took the Fury capstone from measuring as noise to +20.9%, which then needed tuning back to +4.6%.

## 4. The fix that mattered most: priority is not fixed

A rotation was a single ordered list regardless of how many targets were present, so **a single-target capstone displaced area abilities on cleave** and the comparison measured the rotation's stubbornness rather than the talent.

Priority is now computed per scenario, weighting each ability by damage times the number of targets it hits. On three targets a warrior now opens with Cleave 55 times rather than Heroic Strike 73 times, and the Arms cleave gap went from **-16.6% to -5.5%**.

**Any simulator with a hand-authored priority list is measuring the list as much as the build.**

## 5. Core after

| Scenario | n | mean | median | within 5% |
|---|---|---|---|---|
| patchwerk | 8 | +3.0% | +4.6% | **8/8** |
| movement | 8 | +2.6% | +3.3% | **8/8** |
| cleave | 5 | -3.9% | +1.3% | 3/5 |
| burst | 7 | +6.2% | +4.3% | 4/7 |

**Every measurable pair is inside five percent on sustained and on movement.**

## 6. Two columns that should not be flattened

**Burst runs high because the capstones that lead it are cooldowns.** Arcane Power, Adrenaline Rush, Dark Pact. A cooldown is a third of a forty-five second fight and a twentieth of a five minute one.

**Cleave runs low for warriors because their capstones are single-target abilities.** Mortal Strike and Bloodthirst both strike one target, so on three targets a point spent elsewhere buys more. That is the same argument in reverse and it is equally correct.

The working proposal stands: **each scenario needs its own band, and a capstone should be judged against the scenario its own shape suits.** A cooldown capstone may exceed the sustained band on burst; a single-target capstone may fall below it on cleave.

## 7. What remains

**Hunter Marksmanship at -16.4% on switching.** Trueshot removes Aimed Shot's cast time, and target switching is where Aimed Shot is worth least. Same category as the warrior cleave result and probably correct, but it is the largest single cell left and has not been investigated.

**Master Poisoner is still unmeasurable** because poison application is not modelled, and Repentance correctly measures as nothing because it is a stun.
