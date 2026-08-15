# Cross-Tree Synergy and Build Diversity: Where We Actually Are

**August 2026**

*Answerable from `talent-data.json` rather than from opinion. Derived with `analyse.py`.*

---

## 1. The numbers

| | Core | Expanded |
|---|---|---|
| Cross-tree edges | 53 | 73 |
| Mutual pairs, both trees reaching toward each other | 26 | 32 |
| One-way edges | 0 | 0 |
| Classes with at least one pair | 9 of 9 | 9 of 9 |
| Classes with every possible pair | 8 of 9 | 8 of 9 |

Vanilla, measured the same way, has effectively one: warlock. Everything else is a spec with points parked somewhere.

The ninth class is priest, and Holy plus Shadow is left unwired on purpose because Shadowform forbids casting Holy spells. The class already rules that pair out and wiring it would be symmetry against the game.

## 2. The method reproduces a real name, which is the strongest evidence available

Take the mutual pairs, apply the 30/21 split, and read off the deepest talent owned in each tree. For warlock Affliction and Destruction that returns:

> **Shadow Mastery / Ruin**

That is SM/Ruin. Vanilla's actual, player-invented, still-used name for that build, produced by machinery that was not told it existed.

The same procedure on the other warlock pair returns Master Demonologist / Ruin and Conflagrate / Demonic Sacrifice, which is DS/Ruin's territory. **The naming rule established earlier, that builds are named after signature talent pairs rather than point splits, holds up when run backwards.**

## 3. The shapes, and what each buys

Three splits are reachable with 51 points, and they are genuinely different characters rather than three ways to say the same thing.

| Shape | Deep tree reaches | Second tree reaches |
|---|---|---|
| 31/20 | the capstone | gate 15 |
| 30/21 | gate 25 | gate 20, the mark |
| 26/25 | gate 25 | gate 20, the mark |

Worked on five pairs:

| Pair | 31/20 | 30/21 | 21/30 |
|---|---|---|---|
| Affliction + Destruction | Dark Pact / Devastation | **Shadow Mastery / Ruin** | Siphon Life / Conflagrate |
| Arms + Fury | Mortal Strike / Enrage | Crippling Grip / Death Wish | Rupture Line / Improved Berserker Rage |
| Fire + Frost | Combustion / Shatter | Fire Power / Ice Block | Blast Wave / Winter's Chill |
| Discipline + Shadow | Power Infusion / Shadow Weaving | Power of the Word / Vampiric Embrace | Divine Spirit / Darkness |
| Elemental + Enhancement | Elemental Mastery / Static Charge | Lightning Mastery / Elemental Weapons | Elemental Fury / Windfury Mastery |

**Combustion / Shatter** is a mage who crits into crits from both directions. **Power Infusion / Shadow Weaving** is a discipline priest who spends their cooldown on a shadow priest's ramp. **Mortal Strike / Enrage** is the arms warrior who took the capstone and paid for it with a shallow Fury dip. Those are three different characters, and a player would recognise each.

## 4. The honest part: wiring a pair is necessary and not sufficient

Twenty-six pairs times two directions is fifty-two possible builds per configuration. **They will not all become named builds, and claiming otherwise would be the same overreach as claiming nine classes needed a conversion.**

A pair gets named when both signature talents are memorable. Shadow Mastery and Ruin are. **Crippling Grip and Improved Berserker Rage are not**, and no amount of wiring makes them so. That is not a flaw in the structure, it is the difference between what a system permits and what a community adopts, and only the first is in our control.

What the data can say is where the raw material is good. The pairs whose signatures are capstones or gate-20 marks are the ones most likely to stick: Mortal Strike / Enrage, Combustion / Shatter, Elemental Mastery / Static Charge, Power Infusion / Shadow Weaving, Dark Pact / Devastation.

The pairs whose signatures are ordinary multi-rank talents will probably stay unnamed and be described by their numbers, which is exactly what happened to 17/34/0 in vanilla.

## 5. What actually changed against vanilla

**Vanilla:** one class had a named hybrid. Every other split was a spec with filler attached, because nothing in tree A referenced tree B, so there was no reason to cross and nothing to call it.

**Core:** every class has at least one pair, eight have all three, and every crossing point is a talent that reads the other tree rather than a percentage. Zero one-way edges, so no tree reaches toward one that ignores it.

**Expanded:** thirty-two pairs, and every absorbed and original tree is reached by a core tree rather than only reaching outward.

**What is still unproven.** Whether any of these are *competitive* is untested and depends entirely on the tuning rule from Section 5.6: two tier-five seats plus a tier-two should land in the same band as a capstone plus a tier-four. That is a target, not a result. If it holds, fifty-two builds are viable and a dozen get named. If it does not, they are fifty-two ways to be worse, and players will name them and then not play them.

**That is the single largest open risk in the project**, and it is the thing the simulation handoff in Phase 3.1 exists to resolve.
