# The Expanded Trees, Measured

**August 2026**

*First simulation of the seven absorbed and three original trees. This comparison has never been run.*

---

## 1. The question the core work could not answer

Core asks whether a capstone build beats a mid-tree build within one class. Expanded asks something the core configuration structurally cannot: **is a new tree balanced against the trees it sits beside?**

A fourth tree that beats every existing tree by twenty percent is not an option, it is a replacement. One that trails by twenty is a trap.

## 2. Results

Each new tree at 31 points, paired with a host core tree at 20, against that class's strongest core build at the same shape.

| Class | New tree | DPS | 31 vs 30 | vs best core build |
|---|---|---|---|---|
| Paladin | Blackguard | 188 | -3.0% | **-15.0%** |
| Mage | Necromancy | 396 | +0.0% | -1.8% |
| Warlock | Metamorphosis | 392 | +9.2% | -1.8% |
| Rogue | Bladedancer | 172 | +0.7% | +7.4% |
| Shaman | Conduit | 266 | **-20.0%** | +0.9% |
| Warrior | Runeblade | 307 | +0.0% | +9.2% |
| Hunter | Survival | 223 | -0.5% | +9.5% |
| Mage | Chronomancer | 294 | -23.1% | -27.2% |

**Mean +1.2%, median +0.9%, range -15.0% to +9.5%. Six of seven land within ten percent of their class's best core build.**

Chronomancer is excluded from those figures. **It is a healing tree and a damage simulator is the wrong instrument for it**, exactly as it is for Repentance. Its -27.2% is not a balance finding.

## 3. Three bugs the run found

**The rotations contained no absorbed-tree abilities.** Plague Strike, Shadow Cleave, Whirling Blades, Shattering Blow and seventeen others existed as abilities, were granted by talents, and were never cast because no rotation named them. Four of seven trees read exactly 0.0% for that reason alone. Granted abilities are now inserted into their host rotation and gated on the talent, so a build without it never casts them.

**Every one of the ten new trees had its capstone at gate 31 rather than 30**, so `forceCapstone` never fired for any of them: the check requires `points >= gate + 1` and 31 points cannot reach a gate of 31. The gate-arithmetic rule allowed both 30 and 31 as a tolerance, which is why it never fired either. The tolerance is removed and the rule now requires exactly `5 * (row - 1)`.

**Tactical Mastery zeroed every cooldown in the build.** It removes the *stance swap* cooldown and was authored scoped to `all`, so Shattering Blow fired 88 times against a twelve second cooldown and Runeblade read +26.7% against core. Rescoped, it fires 21 times and Runeblade reads +9.2%.

That last one is the same error as Omen of Clarity zeroing every spell's cost. **A new rule, `no-broad-zeroing`, now rejects any effect that multiplies a cooldown, cost or cast time to zero across a tag or across everything.** Nine talents were flagged; seven were rescoped to a named ability and two were rescaled rather than zeroed.

## 4. What the numbers say about the expansion

**Six of seven within ten percent is a better result than the core capstone work produced**, and it was not designed for. The absorbed trees were built to a rule set, not to a damage target, and they land near their class's existing best without tuning.

Two sit outside and both are informative rather than alarming.

**Blackguard at -15.0%** is the weakest. Its damage is spread across Blight application and self-healing, and a damage simulator counts none of the sustain. It is the tree most likely to be undervalued by this instrument rather than genuinely weak, and it should be checked with `tank.py` before anything is changed.

**Conduit's -20.0% capstone gap** is the largest internal spread in the project. The 31-point build takes Confluence and loses to the 30-point build by a fifth. Confluence spreads Elemental Bond across three allies, which is a raid-support effect that a single-character damage simulator cannot see at all. **It is the clearest case yet for the support instrument that does not exist.**

## 5. What is still not measured

Chronomancer, Dreamer and Radiance are healing trees. Two of the three have never been run through `heal.py`, and the numbers above should not be read as saying anything about them.

Blackguard's sustain, Metamorphosis's mitigation and Conduit's raid support are all real value that no damage number contains. **Three instruments exist and the expansion needs all three pointed at it**, which is the next piece of work rather than a caveat on this one.
