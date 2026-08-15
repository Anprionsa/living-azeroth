# Absorbed Trees: Compliance Audit

**August 2026**

*Closes REG-12 and REG-05. The seven trees in `trees.json` were built before most of the rules in `classic-plus-talent-design.md` Section 5 existed. This runs the same measurements on them that produced the vanilla audit, and records what needs changing.*

*Scope note: this audit measured the original seven trees. Chronomancer was added afterwards, built to the rules this audit established, and its figures are in `chronomancer.md` section 5. It requires none of the changes listed here.*

---

## 1. They are in much better shape than vanilla

| Tree | Host | Points | Flat share | Forced flat to capstone | Gate 20 |
|---|---|---|---|---|---|
| Blackguard | Paladin | 58 | 50% | 5 / 30 | 6 |
| Necromancy | Mage | 58 | 43% | 5 / 30 | 6 |
| Bladedancer | Rogue | 64 | 45% | 7 / 30 | 6 |
| Runeblade | Warrior | 60 | 57% | 8 / 30 | 6 |
| Conduit | Shaman | 58 | 50% | 9 / 30 | 6 |
| Metamorphosis | Warlock | 58 | 66% | 11 / 30 | 6 |
| Survival | Hunter | 58 | 71% | 15 / 30 | 6 |

Across all seven: 225 flat of 414 points, 54%. Vanilla before the rework was 73%.

Mean forced flat to a capstone is 8.6 of 30, against a vanilla mean of 17.4 and a vanilla worst-five mean of 26.2. **Five of the seven would rank in the healthiest third of vanilla trees, and Blackguard and Necromancy at 5 would be the two healthiest trees in the game**, ahead of Fire mage at 8.

That is a real result and it should be said plainly before the criticism: whoever built these was already designing to most of the principles this document arrived at later.

## 2. What needs changing

### 2.1 The flat content is smaller but it is still there

Section 5.2 is absolute: points buy behavior, never numbers. Fifty-four percent is better than seventy-three and it is not zero.

The pure-modifier nodes, counted per tree, are 26 points in Blackguard, 25 in Necromancy, 29 each in Bladedancer and Conduit, 34 in Runeblade, 41 in Survival, and 44 in Metamorphosis. They read exactly like vanilla's: Unholy Vigor increases melee damage by 1 through 5%, Grave Cold reduces mana cost by 5 through 15%, Fel Vigor and Fel Stamina and Demonic Hide are stat percentages, Deflection reappears in absorbed Survival under its own name.

All of it goes to the depth dividend, with the caveat in 2.4.

### 2.2 Two trees are notably flatter than the rest

**Metamorphosis at 66% and absorbed Survival at 71%** sit where a middling vanilla tree sits. Survival is the worse case, because it is 41 points of pure modifiers out of 58 and it carries Deflection, Savage Strikes, and Trap Mastery under the same names and roughly the same text as the vanilla Survival tree it replaces.

That is worth naming precisely: **the absorbed Survival tree inherited its predecessor's flatness along with its content.** Section 17.2 of the design document rebuilds vanilla Survival around traps working in both modes. The absorbed version should take that rebuild rather than the original.

Metamorphosis has the opposite problem. Its thirteen modifier nodes are all Fel-prefixed stat percentages feeding a form that arrives at the bottom, which is Demonology's shape: a tree of pet statistics ending in the thing you actually wanted. The Section 9 treatment applies.

### 2.3 Gate 20 is six points in all seven trees

REG-18 found starved hybrid tiers in eleven of twenty-seven vanilla trees and called it the most common structural fault in the game. All twenty-seven rebuilds were standardised to eight points at gate 20.

Every absorbed tree is at six. Consistent with each other, and consistent with the fault. All seven need the same two points, and they should come from an overweight lower tier rather than being added.

This matters more here than in vanilla, because these trees are splashed by design. Class Absorption's own fluid-trees argument says partial investment must be a legitimate outcome, and gate 20 is where partial investment lands.

### 2.4 REG-05: the dividend conflict, and how it resolves

Section 20.3 gives absorbed trees no stat curve, because there is no vanilla baseline to calibrate one against. That decision stands.

But it creates the problem REG-05 recorded: if a vanilla tree grants a dividend and an absorbed tree does not, splashing an absorbed tree costs stats that splashing a vanilla tree does not, which discourages exactly the builds Section 5.6 wants.

The audit resolves it. Every absorbed tree has a local mechanic that already scales with depth: Blight, The Risen, fel corruption, Momentum, Empowerment, rune charges, offensive traps. **Those mechanics take the deleted flat content's budget.** When Unholy Vigor's 5% melee damage is removed, its value goes into Blight scaling harder with points invested, not into a stat curve and not into thin air.

That keeps the absorbed trees behavior-only, keeps them competitive to splash, and gives their local mechanics the tuning target REG-05 asked for. It also means the deleted points are not lost, which is the answer to the obvious objection.

### 2.5 Subtraction nodes: four of seven have none

Blackguard, Necromancy, Bladedancer, and Runeblade carry subtraction-shaped talents. **Metamorphosis, Conduit, and absorbed Survival carry none.**

Metamorphosis is the surprising gap, since a self-inflicted demonic transformation is the most natural subtraction fantasy in the game. It should have one and it does not.

Note also that Damnation is already flagged for conversion to a toggleable form in the manner of Shadowform, with permanence moved to the acquisition chain. That is the same Shadowform precedent Section 5.4 cites, so both documents should state it identically.

### 2.6 Cross-tree conditionals need the REG-07 check

Metamorphosis and Conduit have six and five talents respectively worded against host-tree content. None has been checked against Section 5.7's rule: **a cross-tree conditional may never be the reason to take the talent it sits on.**

That rule caught a real trap in Marksmanship's Pack Tactics, whose rank 3 was worthless without the Beast Mastery capstone. The same check has not been run here and should be, node by node, before either document is published.

## 3. Summary of required changes

| Change | Trees affected |
|---|---|
| Delete flat nodes, budget into the local mechanic | all seven |
| Gate 20 from six to eight | all seven |
| Take the Section 17.2 rebuild rather than vanilla Survival's content | Survival |
| Apply the Section 9 treatment for stat-percentage trees ending in a form | Metamorphosis |
| Add a subtraction node | Metamorphosis, Conduit, Survival |
| Run the Section 5.7 check on every cross-tree talent | Metamorphosis, Conduit, Blackguard, Runeblade |
| State the Damnation and Shadowform precedent identically in both documents | Blackguard |

None of this is structural. The seven trees were built to a compatible philosophy and need a pass, not a rebuild, which is the opposite of what the twenty-seven vanilla trees needed.
