# Absorbed Trees: Revisions

**August 2026**

*Executes REG-25. Companion to `absorbed-audit.md`, which established that the seven trees need a pass rather than a rebuild. Two of them turned out to need more than a pass.*

*Scope note: these revisions cover the original seven trees. Chronomancer was written to the finished rule set and needs none of them.*

---

## 1. Two findings that changed the scope

### 1.1 No cross-tree conditional exists anywhere in the seven trees

Class Absorption's fluid-trees argument establishes a twenty-point mark so that partial investment is a legitimate outcome. Checked against the data, that mark is a good talent sitting at gate 20. **Not one talent in any of the seven trees is conditioned on investment in a host tree.** Zero, across 414 points.

So the trees are splashable in the sense that stopping early leaves you something. They are not splashable in the sense Section 5.6 means, where a 26/25 build is a specific character because talents on each side read the other.

That is the largest single gap between the two documents, and it is the one REG-03 explicitly asked for: absorbed trees participating in cross-tree conditionals in both directions. Every tree below gains one at gate 20.

### 1.2 Metamorphosis does not contain its own mechanic

Each tree declares a local mechanic. Measured against the talents that actually reference it:

| Tree | Mechanic | Nodes engaging it | Points |
|---|---|---|---|
| Conduit | Empowerment | 12 | 30 / 58 |
| Blackguard | Blight | 10 | 22 / 58 |
| Survival | Offensive traps | 7 | 16 / 58 |
| Bladedancer | Momentum | 5 | 13 / 64 |
| Necromancy | The Risen | 6 | 12 / 58 |
| Runeblade | Rune charges | 4 | 11 / 60 |
| **Metamorphosis** | **Fel corruption** | **0** | **0 / 58** |

Metamorphosis declares a self-applied stacking corruption state and no talent in the tree applies it, spends it, or refers to it. What the tree actually contains is fifty-two points of Fel-prefixed percentages ending in a form.

That is Demonology's premise failure exactly, and the Section 9 treatment applies without modification: the tree has to be about the thing it is named for before anything else is worth doing to it.

Conduit at 30 of 58 is the model. Blackguard at 22 is acceptable. The bottom four need their mechanic pushed into more of the tree, and Metamorphosis needs it introduced.

---

## 2. Metamorphosis, rebuilt

Fel corruption becomes real: a stack applied by the warlock's own damage, spent by the tree, and the thing the form runs on.

- **Gate 0, 10.** *Corruption's Price* (5): your Shadow damage applies a stack of fel corruption, then stacks persist through form changes, then a stack is spent to make your next spell unresistable, then corruption ticks for damage at five stacks, then stacks do not decay in combat. *Fel Concentration* (5), kept.
- **Gate 5, 11.** *Shadow Cleave* (1), kept. *Cruel Intent* (5): Shadow Cleave applies two stacks, then strikes behind you, then spends stacks for damage, then refreshes Immolation Aura, then cannot be dodged at full stacks. *Sacrificial Pact* (5): your health is spendable as a resource, then spending it applies corruption, then Health Funnel channels while you attack, then Life Tap applies corruption, then your demon's death grants full stacks.
- **Gate 10, 10.** *Soul Link* (2), kept. *Demonic Aegis* (5) reworked: corruption stacks reduce damage taken, then convert magic damage to fel, then a full stack absorbs a killing blow once per fight, then absorbed damage feeds the form, then breaking absorbs applies corruption to attackers. *Master Summoner* (3) reworked to summoning behavior.
- **Gate 15, 9.** *Immolation Aura* (1), kept. *Unholy Sacrifice* (3), kept. *Fel Ferocity* (5): corruption stacks raise Shadow Cleave's critical chance, then criticals apply two stacks, then a critical at full stacks resets Fel Aegis, then criticals spread corruption to nearby enemies, then a spread refunds a shard.
- **Gate 20, 8, hybrid seat.** *Fel Aegis* (1), kept. *Demonic Knowledge* (2), kept. **Cross-tree, new:** *Ruinous Corruption* (3): your Immolate and Corruption apply fel stacks; Conflagrate spends them for damage; Shadow Bolt applies two. Every warlock has all three spells, so it stands alone per Section 5.7, and it is worth most to an Affliction or Destruction main at 26/25. **Subtraction, new:** *Irreversible* (2): your corruption stacks never decay and the form's bonuses double. You may no longer leave the form or summon a demon.
- **Gate 25, 8.** *Unending Fel* (3), kept. *Demonic Fury* (5): the form's abilities spend corruption rather than mana, then generate it, then a full stack empowers the next, then the form's damage scales with stacks held, then leaving the form banks them.
- **Gate 31, 1.** *Metamorphosis* (1), kept.

57 points. Fel Vigor, Demonic Hide, Fel Stamina, Demonic Bulwark, Fel Resilience, Warding Fel, and Fel Domination deleted, their budget into corruption scaling per REG-05.

*Irreversible is also the subtraction node Metamorphosis was missing, and it is the natural one: the fantasy of a warlock who went too far should be purchasable.*

## 3. Survival, replaced

Absorbed Survival is 71% flat and inherits vanilla Survival's content under the same names, including Deflection, Savage Strikes, Thick Hide, Killer Instinct, and Trap Mastery. Sixteen of its fifty-eight points touch traps, which is its stated mechanic.

**It should take the Section 17.2 rebuild of vanilla Survival rather than carrying the original forward.** That rebuild already makes traps work in both modes per Section 5.8, already grows gate 20 to eight, and already carries a subtraction node in Lone Wolf.

Three changes to that rebuild for the absorbed context:

- Lone Wolf is wrong here, since this tree is built around a pet through Coordinated Assault and Hunt as One. Replace with *Sole Survivor* (1): your traps arm instantly and cannot be resisted; you may no longer have a pet active.
- Coordinated Assault stays at gate 20 as the twenty-point mark, alongside a new cross-tree node, *Marked Prey* (3): your traps apply Hunter's Mark, your melee strikes benefit from your ranged attack power, Raptor Strike refreshes Serpent Sting. Stands alone for any hunter.
- Hunt as One stays as the capstone.

## 4. The other five

**Conduit** is the healthiest of the seven and needs only the standard pass. Gate 20 from six to eight, absorbing a new cross-tree node *Stormbound* (2): your Empowerment stages carry into Chain Heal and Chain Lightning, and a fully held cast grants Clearcasting. Subtraction node, new: *Unbroken Current* (1): your empowered casts cannot be interrupted or pushed back, and you may no longer cast anything instantly. Elemental Focus, Elemental Warding, Grounding, and Steady Channel's flat halves go to the local mechanic.

**Blackguard** keeps Blight and its two subtraction-shaped nodes. Gate 20 to eight with a cross-tree node, *Unholy Devotion* (2): your Blight benefits from your healing bonus, and Judgement spreads it. Unholy Vigor, Grave Cold, Deathward, and Morbid Strength deleted into Blight scaling. Damnation is restated as a toggleable form in the manner of Shadowform, with permanence moved to the acquisition chain, phrased identically in both documents.

**Necromancy** is the second healthiest. Gate 20 to eight with *Grave Bond* (2): your Risen benefit from your spell critical chance and Frost spells slow anything attacking them. Shadow Focus, Grave Robbing, Deathchill Focus, and Dark Intellect deleted into The Risen scaling, which at 12 of 58 needs the budget.

**Bladedancer** keeps the weapon fork, which is now a shared component across six trees. Gate 20 to eight with *Shadow Momentum* (2): Momentum is gained from stealth openers and spent by finishers. Flowing Form, Fleet Footed, Deft Hands, and Lithe deleted into Momentum scaling, which at 13 of 64 is the thinnest mechanic coverage of any tree with a working mechanic.

**Runeblade** keeps its two subtraction nodes. Gate 20 to eight with *Tempered Steel* (2): rune charges are spent by Sunder Armor and Shield Slam, and Mortal Strike consumes all charges for damage. Cold Iron, Iron Discipline, and Weighted Edge deleted into rune charge scaling, at 11 of 60 the thinnest of all seven.

---

## 5. What changed, in summary

| Change | Trees |
|---|---|
| Cross-tree conditional added at gate 20 | all seven |
| Gate 20 from six to eight | all seven |
| Flat nodes deleted, budget into the local mechanic | all seven |
| Subtraction node added | Metamorphosis, Conduit, Survival |
| Full rebuild, premise failure | Metamorphosis |
| Replaced by the Section 17.2 rebuild | Survival |
| Damnation phrasing aligned across documents | Blackguard |

The two documents now share a rule set. What they do not yet share is a verification pass on the vanilla side's cross-tree talents, which is the same Section 5.7 check applied in reverse, and that is the last outstanding consistency item between them.
