# Chronomancer: An Eighth Absorbed Tree

**August 2026**

*Proposal for a mage healing tree. Written to the current rule set in `classic-plus-talent-design.md`, added to `trees.json` as tree eight, and audited against the same checks applied to the other seven in `absorbed-audit.md`.*

---

## 1. It passes the absorption test

Class Absorption's own test asks whether a fantasy needs a resource the host cannot reach, an armor type the host does not wear, and a role the host cannot fill. One of those is a spec. All three is a class.

Chronomancer needs one. Mana is already the resource. Cloth is already the armor. Only the role is new.

That is the same result the test gave for Demon Hunter on warlock and Evoker on shaman, both of which the document accepted. It is a spec.

## 2. The five-tree question, answered from the audit rather than from symmetry

Mage would carry five trees against four for every other host. That is asymmetric, and it is worth being direct about why it is acceptable here rather than waving at the ceiling.

It is not a power question. Under the fluid-tree model a character still has 51 points regardless of how many trees they can spend them in, so a fifth tree adds options and adds nothing to a ceiling.

It is a content question, and the audit answers it. **Mage has the healthiest talent trees in the game and the most repetitive gameplay.** Fire forces 8 of 30, the lowest figure anywhere. Frost is described in its own guides as spam Frostbolt. Section 22 of the talent document says plainly that the rework is necessary and not sufficient, and names mage as the proof: what constrains a vanilla mage is that the spell book holds three damage spells, and no amount of talent redesign touches that.

A second absorbed tree is a fix for exactly the problem the talent rework explicitly cannot solve, on exactly the class where that problem is worst. That is a better argument than "five is the maximum," and it means the asymmetry is pointed at the right class rather than being an accident.

The honest cost: mage becomes the class with the most to learn. Whether that is a problem depends on whether the other eight hosts also eventually get a second tree, which would remove the asymmetry and is not proposed here.

## 3. It is not a priest

The obvious objection is that the game already has a cloth healer and this is that healer with different art. The answer is in the mechanic.

**A chronomancer does not add health. It returns a target to health they previously had.**

The local mechanic is Echo: a recorded snapshot of an ally's health, taken by your spells and spent to restore them to it. It lives on the target rather than in a new resource bar, per Class Absorption's rule that no absorbed tree imports one.

That produces a healer whose curve is the inverse of a priest's:

- Strongest immediately after a damage spike, because the recorded value is still high.
- Weakest during sustained damage, because the record degrades with the target.
- Useless on someone who has been low for a while, since there is nothing good to return them to.
- Rewarding of attention, because the record is only as good as your recent casting.

A priest is proactive, shields, and sustains. A chronomancer is retroactive and burst-corrective. The two are bad at different things, which is the test a fourth healing archetype has to pass.

The capstone is the fantasy stated plainly. **Rewind** returns an ally to the state they held ten seconds ago, and if they died inside that window, they return.

## 4. The verb is remembered, and vanilla already wrote it

Six verbs exist across the seven trees: forged, taught, taken, fallen, earned, granted, copied. Chronomancer takes a seventh, and it is the only one that is not an event.

Anachronos has stood at the Caverns of Time in Tanaris since patch 1.9, gating access behind Brood of Nozdormu reputation. His questline sends a mortal to a Crystalline Tear in Silithus to watch the sealing of Ahn'Qiraj play out, in quests named Long Forgotten Memories and A Pawn on the Eternal Board.

So vanilla already contains a bronze dragon whose function is showing chosen mortals events that already happened, in a place, with a reputation gate, and with a quest literally titled after remembering. Nothing needs inventing. The acquisition is recognising that one of the memories he shows you is yours.

Anchors are Tanaris, Silithus, and Un'goro Crater. Profession gate is Enchanting, on the soft-gate rule: access to an enchanter rather than being one, since binding a moment into an object is what enchanting already does.

Permanent cost: **you cannot be resurrected by another player.** You return unaided after a delay, at a position you held earlier in the fight. For a healer, who is a priority resurrection target, that is a real raid cost and not a flavor line.

## 5. Compliance

Audited against every rule the other seven were:

| Check | Result |
|---|---|
| Available points | 58, matching five of the other seven |
| Gate 20 weight | 8, the standard set across all 27 vanilla rebuilds |
| Pure-modifier nodes | none |
| Cross-tree conditionals | two, Arcane Continuum and Frozen Moment |
| Section 5.7 rule, does each stand alone | yes; every mage has Arcane Missiles, Evocation, Presence of Mind, Frost Nova, and Ice Block |
| Subtraction node | Fixed Point |
| Capstone is not a passive aura | Rewind is an active with a five minute cooldown |
| Mechanic coverage, REG-27 | **46 of 58 points reference Echo** |

That last figure is the highest of any tree in the suite. Conduit was previously best at 30 of 58, and Metamorphosis was at zero, which is what triggered its rebuild.

## 6. Risks worth recording now

**Rewind resurrecting inside a ten second window is the strongest single effect proposed anywhere in this suite.** It needs the long cooldown to survive contact, and it is the first thing to cut if the tree tunes badly. The tree does not depend on it.

**Echo asks the interface for something vanilla does not display.** Knowing a target's recorded value requires showing it, and vanilla unit frames do not. That is an addon-shaped problem in the original game and a real cost here.

**A healer who cannot be resurrected changes raid behavior**, and not only for the chronomancer. Guilds will assign someone to keep them alive differently. That is interesting rather than broken, but it should be tested before it is assumed.

**Five trees on one host has no precedent and no second instance.** If it works, the question of a second tree for the other eight hosts arrives immediately and this document does not answer it.
