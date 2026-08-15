# Chasing the Warlock Gap

**August 2026**

*Nine of 114 capstone-free shapes within seven percent, against Mage's 31 on the same three-damage-tree structure.*

---

## 1. The diagnosis was one line of the distribution

Listing which trees appear in the shapes that work:

| Class | Shapes within 7% | Trees used |
|---|---|---|
| Mage | 31 | frost 31, fire 16, arcane 14 |
| Warlock | 9 | affliction 9, destruction 9, **demonology 0** |

**Every viable Warlock build was Affliction plus Destruction. Demonology appeared in none of them.**

Mage's weakest tree still appears in 14 of its 31 working shapes. Warlock's appeared in zero, so the class effectively had two trees to combine rather than three, which is exactly the shape of a class with two.

## 2. Why Demonology was worth nothing as a partner

Twenty-one points bought **no damage modifiers at all.** Every talent in the tree is pet-scoped, and:

**A caster's pet was scaled off attack power it does not have.** The pet base read `attackPower` with a default of 700 for any class lacking it, so a warlock's demon contributed 31 damage per second. Pets now scale off spell power where the owner is a caster, and a warlock's demon reaches roughly a fifth of the build's output, which is where a vanilla demon sits.

**And Unbound was authored as a percentage.** Its text reads *"You may have two demons active at once"* and its effect was `add damage 0.3`. **The talent that makes a Demonology splash worth taking did not do the thing it describes.** Reworked to `addTarget pet`, and it now grants a second demon.

Familiar, Demonic Empowerment and Master Demonologist had the same problem in smaller form and were rewritten alongside it.

## 3. A selector fault the fix exposed

Unbound had the highest value at its gate and was still not taken. **On a tie the selector preferred the shallower talent**, so a strong talent at gate 20 lost to an equal one at gate 5 and the last points never reached the deep rows.

Players build deep. The tie now goes to the deeper talent, and that change moved every class, not just Warlock.

## 4. Result

| | Before | After |
|---|---|---|
| Warlock shapes within 7% | 9 of 114 | **19 of 114** |
| Demonology appearances | 0 | **4** |
| Affliction 30 / Demonology 21 | 476 | 497 |
| Gap to the Destruction partner | 144 | **90** |

**Demonology is now a tree a build can splash into**, which it was not. It is still the weakest of the three, and 19 against Mage's 31 says the gap is narrowed rather than closed.

## 5. What is left of it

The remaining 90 point gap is that **Destruction 21 reaches Ruin and Demonology 21 reaches Unbound**, and a second demon is worth less than doubling critical strike damage.

Whether that should be equal is a design question rather than a tuning one. **A pet tree splashed for one talent is reasonably worth less than a damage tree splashed for one talent**, and forcing them level would make Demonology the default splash for every warlock, which is the failure it was suffering in reverse.

## 6. State

Core zero violations of fifty cells. Both configurations pass 24 rules clean. The audit reports nothing outstanding.

Destruction needed retuning after the tie-break change, since its capstone reached talents it previously could not, and now reads +4.3% sustained and +6.6% on burst.
