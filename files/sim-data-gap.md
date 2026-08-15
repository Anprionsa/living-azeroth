# What the Classes Still Need Before Build Diversity Can Be Simulated

**August 2026**

*Answering a specific question: what data would let a simulator decide whether 30/21 is competitive with 31/20. Measured against `talent-data.json` rather than guessed.*

---

## 1. The problem we created on purpose

Section 5.2 deleted every percentage from the trees and replaced it with discrete behaviour. That was correct and it is the whole design. It also means **only 21% of core talents state a magnitude at all.**

Measured across 484 core talents, what they express:

| Shape | Talents | Share |
|---|---|---|
| refresh or extend a duration | 135 | 27% |
| a magnitude | 104 | 21% |
| a resource change | 83 | 17% |
| a proc on an event | 63 | 13% |
| ignore or bypass a defence | 59 | 12% |
| a threshold condition | 55 | 11% |
| enable an otherwise disallowed action | 49 | 10% |
| add a target | 30 | 6% |
| convert a tag | 18 | 3% |

A simulator can read "increases Fire damage by 5%". It cannot read "Rend ignores armor. Overpower refreshes it. Below 20% health it dumps its remaining damage at once."

So the gap is not that we removed numbers. It is that we replaced them with prose, and prose is not a data type.

## 2. Four additions, in dependency order

### 2.1 An effect DSL, so behaviour is machine-readable

Added to the schema as `effects` on every talent. Nine operations cover the shapes above:

`add`, `multiply`, `ignore`, `enable`, `grant`, `convert`, `proc`, `refresh`, `addTarget`

Each carries a `scope` of one ability, one tag, or everything, an optional `when` condition, and a `magnitude`.

Bloodletting, which reads as three sentences, becomes three effects:

```
ignore   armor          on warrior-rend                       1.0
refresh  duration       on warrior-rend    when Overpower     null
multiply tickRate       on tag:bleed       when hp<0.2        2.0
```

**The `convert` op is the one that matters most for this question**, because tag conversion is the mechanism the whole build-diversity argument rests on, and it becomes a one-line effect: add `fire` to Frostbolt's tags, and every talent whose `reads` includes `fire` applies automatically. That is a set operation the sim already knows how to do.

**Cost.** Roughly 1,200 effects across 484 core talents. It is authoring, not design, but it is the largest single item remaining.

### 2.2 Ability baselines, because talents modify things that need values

`castTime`, `cooldown`, `cost`, `costType`, `baseDamage`, the spell power or attack power coefficient, `gcd`, and where relevant `duration`, `tickInterval`, and `maxTargets`.

Fifteen of 204 are authored as a worked sample. The rest carry the fields as null.

**Cost.** 204 abilities times roughly eight fields. This is transcription of public vanilla values, not design, and it is the cheapest large item on the list.

### 2.3 The dividend curve, which is currently a placeholder

`dividend.stats` is empty on all 64 trees. Section 5.1's method is stated but no coefficient exists.

This is the one item with a chicken-and-egg problem: the curve is meant to reproduce what a canonical build's flat talents used to deliver, which requires knowing what those were worth, which requires a sim. **The resolution is to propose a curve from the vanilla ledger and let the sim validate it rather than derive it**, which is what the ledger work in `specs-baseline.json` was for.

### 2.4 A rotation priority per canonical build

A sim cannot infer what order to press things. Every build being tested needs an ordered priority list.

This is genuinely design work rather than transcription, because the rotation is part of what the rebuild claims to have changed. Marksmanship's Steady Aim is only worth its five points if the rotation stops fighting the swing timer, and that has to be expressed as a priority before it can be measured.

## 3. What is not needed, which bounds the work

**The question is relative, not absolute.** Nobody needs to know a Fury warrior's exact damage. The question is whether 30/21 lands inside the same band as 31/20 for the same class in the same gear. That means:

- **No encounter model beyond fight length and target count.** Movement, mechanics, and positioning cancel out when comparing two builds of one class.
- **No cross-class balance pass yet.** Band neutrality is per raid, and the within-class comparison comes first because it is the one this document's argument depends on.
- **No gear optimisation.** One Naxxramas gear set per class, held constant. The control is Warcraft Logs rather than a simulated baseline, which was settled in `sim-baseline-protocol.md`.

That reduces the sim to: one class, one gear set, three builds, fixed fight length, and a comparison of the resulting numbers against each other rather than against a target.

## 4. The order to do it in

1. **Ability baselines.** Cheapest, unblocks everything, and it is transcription.
2. **Effect DSL on the talents that appear in the 26 named pairs.** Bounded, and it is exactly the set the question is about.
3. **Rotation priorities for those builds.**
4. **A proposed dividend curve**, to be validated rather than derived.
5. **Everything else**, only if the first four leave the question open.

## 5. The honest risk

Some talents may not be simulable at any level of detail. "Your threat does not decay while you hold aggro" needs a threat model that vanilla simulators mostly do not have. "Your buff totems follow you within 20 yards" is a quality-of-life change whose value is real and does not appear in a damage number.

**Those talents are not failures, they are the part of the design that a simulator cannot judge.** The right response is to mark them `simulable: false` and evaluate them by argument rather than pretending a number exists. What must not happen is quietly dropping them so the model looks complete.
