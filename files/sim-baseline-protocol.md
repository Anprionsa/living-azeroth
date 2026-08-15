# Sim Baseline Protocol

**Version 0.1 | August 2026**

*Companion to classic-plus-talent-design.md. Establishes the control set against which the talent rework gets measured. Gear assumption is Naxxramas best in slot exactly as it exists in Classic, unchanged.*

---

## 1. The fork, which has to be settled before any of this means anything

Section 5.1 of the talent document promises power neutrality: sum what a canonical build already buys in flat bonuses, hand it back as an automatic depth curve, net change zero. That promise is the entire political case for the rework. It is what lets you tell a Classic audience that this is a redistribution rather than a buff.

Vanilla Naxxramas is not balanced. Warriors dominate melee, hunters fall off as gear scales, and several specs hold raid slots for a totem or a buff rather than for their own output.

Those two facts are in direct tension. If every spec targets its own current number, the rework reproduces vanilla's imbalance exactly and the sim confirms it to four decimal places. You will have done a large amount of work to arrive at the same tier list.

Three ways out.

**Strict neutrality.** Every spec targets its own logged number. The rework is provably not a power change and the argument is airtight. Warriors still dominate. Choose this if the goal is to make talents interesting and you consider balance a separate project.

**Band neutrality.** Total raid output is held constant while individual specs move within it. Some gain, some lose, the sum is flat. You can still say the rework is not a power increase, which is the claim that actually matters, and you get to fix the worst gaps.

**Explicit rebalance.** Set a target band and move every spec into it. This is a real power change and has to be argued on its own merits rather than smuggled in under a neutrality claim.

Band neutrality is the recommendation, and the reason it is even available is new.

The depth dividend is a per-tree scalar. One number. You can raise or lower a spec's output without touching a single talent, without redesigning an ability, and without a tuning pass that breaks four other things. Vanilla never had a dial like that, which is part of why its balance never got fixed: every correction required editing talents that other specs also used.

That makes the depth coefficient the most valuable thing in the whole rework, and it argues for setting it deliberately rather than mechanically. Deriving it from each spec's current flat sum is the safe default. Deriving it from a target band is the better outcome, and it costs you the ability to claim strict neutrality.

Pick before the ledgers get filled in, because the choice determines what the target column contains.

---

## 2. You do not need to sim the control

Worth saying early because it removes a large amount of work.

Warcraft Logs carries Naxxramas rankings for Classic by spec. Real players, real Naxx gear, real fights. Median and 95th percentile per spec is a better control than any sim would produce, because it includes execution variance, real fight lengths, and movement, none of which a sim models honestly.

So the control is not something you build. It is something you download.

What needs simming is the reworked system, in the same gear, against those numbers. One sim target instead of two, and the baseline stops being an assumption.

---

## 3. The four steps

**Fix the build.** One canonical build per spec, written down, not revisited. `specs-baseline.json` holds these. Most are marked `needs-check` and should be confirmed against a talent calculator before use, for the reason in section 4.

**Extract the flat ledger.** For each build, list every talent taken, its rank count, and whether it buys a number or a behavior. Sum the flat side. That sum is what the depth curve has to reproduce.

**Set the depth coefficient.** Under strict neutrality it is the ledger sum divided by points invested in the main tree. Under band neutrality it is that number adjusted toward the target band.

**Sim the rework and compare.** Same gear, same fight profile, against the logged control.

---

## 4. Confirm every talent gate before trusting a ledger

This is not a formality. It already caught an error in the talent document.

Impale, in vanilla Arms, sits at tier 4 behind a 15 point gate. Two ranks at 2 points brings the total to 17, and that is the entire reason the canonical Fury build is 17/34/0 rather than some rounder number. The talent document originally placed Impale at tier 5, which would have made the canonical build impossible and quietly changed which talents every warrior build could reach.

A wrong gate does not throw an error. It produces a plausible ledger with the wrong contents. Confirm gates first, per tree, before any ledger is filled in.

The worked example in `specs-baseline.json` under `warrior-fury` shows the shape. Seventeen points in Arms, roughly nine of which buy a number, and the entire investment exists to reach one flat talent that increases critical strike damage. Under the rework those seventeen points return as curve and the player gets seventeen points to spend on behavior. That is the argument in miniature, and it is the only ledger in the file currently backed by verified data.

---

## 5. Confounds that will wreck the comparison if unrecorded

**World buffs.** The largest problem by far. Classic Naxxramas logs are saturated with world buffs, and they do not scale every spec equally. A world-buffed fire mage gains more than a world-buffed resto shaman. If the control is pulled from buffed parses and the sim runs unbuffed, the comparison is meaningless. Record the buff state on every control number and hold it constant. The `worldBuffed` field exists for this.

**Debuff slots.** The anniversary realms removed the debuff limit, which materially changed warlock and shadow priest viability. Whichever ruleset the control comes from has to match the ruleset the sim assumes, and it should be stated in the meta block rather than inferred.

**Raid buffs and composition.** Vanilla output is heavily group-dependent. Windfury Totem alone reorders the melee list. A spec simmed solo and compared against a logged parse from a windfury group is not being measured, it is being flattered.

**Specs brought for utility.** Enhancement shaman and marksmanship hunter both hold raid slots partly for what they give other people. Their control number understates their value and a rebalance driven purely by personal output will overcorrect them. Flag these before tuning, not after.

---

## 6. What to measure per role

DPS wants sustained single target as the primary number, plus one cleave case, because Section 6's Sweeping Strikes and Weapon Mastery changes only show up when a second target exists.

Tanks want threat per second and effective health. Threat is the one that constrains raid DPS in vanilla, so it is the number that actually matters for balance.

Healers want throughput and healing per mana. Vanilla healing is mana-limited rather than throughput-limited, so a rework that improves raw output without touching efficiency will look like a buff in the sim and change nothing in a raid.

---

## 7. State of the dataset

Thirteen specs in `specs-baseline.json`. One build verified in session, one likely, eleven needing confirmation. One ledger partially worked, twelve pending.

The builds are the least valuable part of the file and the part most likely to be wrong, since anyone who plays these classes can correct a point split in under a minute. The schema and the target column are the parts worth keeping.

Filling the remaining twelve ledgers requires rank-by-rank tree data per class. That is mechanical work but it is not work worth doing from memory, for the reason in section 4.
