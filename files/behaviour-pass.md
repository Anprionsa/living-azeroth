# The Behaviour Repair

**August 2026**

*Re-expressing percentage-authored talents as the behaviour their own text already describes. Not a redesign.*

---

## 1. What the problem turned out to be

Thirty percent of authored talents expressed their effect as `multiply damage`, which is exactly the flat modifier Section 5.2 deleted from the trees.

Reading them showed the repair is smaller than the finding implied. **In almost every case the talent's text already describes behaviour and only the effect was written as a percentage.**

Improved Shadow Bolt reads *"Your Shadow Bolt applies a vulnerability consumed by the next attacker and it stacks. It does not expire."* That is a debuff mechanic. It was authored `multiply damage 1.10`.

So this is completing the authoring correctly rather than changing what any tree does.

## 2. Three ops added, because the vocabulary could not say what the text said

| Op | Expresses |
|---|---|
| `debuff` | a stacking vulnerability that ramps, with a stack count |
| `consume` | spending a stack or effect for burst, scoped to what benefits and naming what it spends |
| `alternate` | a bonus for alternating two abilities rather than repeating one |

Shadow and Flame reads *"your Shadow Bolt and Immolate each empower the other, so alternating them is stronger than repeating either."* No previous op could say that, which is why it had been flattened to `multiply damage 1.08`.

**A vocabulary that cannot express a design will quietly convert it into one it can.**

## 3. The conversion standard

Recorded in `meta.behaviourStandard`. A talent may use `multiply damage` only if its text states a percentage. Everything else converts to the op its text names:

| Text says | Op |
|---|---|
| applies a vulnerability, stacks | `debuff` |
| consumes X for damage | `consume`, scoped to the beneficiary |
| each empowers the other | `alternate` |
| hits a second target, spreads, chains | `addTarget` |
| cannot be resisted, dispelled, interrupted | `enable` with an immune flag |
| refreshes, extends, does not expire | `refresh` or `no_expiry` |
| counts as, becomes | `convert` |
| costs less, cooldown drops, instant | `multiply` on cost, cooldown or castTime |

**Cost, cooldown and cast time multipliers stay.** Changing how often you act is behaviour. Scaling what an action does is not.

## 4. Result

| | Before | After |
|---|---|---|
| Talents expressing a percentage | 214 of 696, 30% | **101 of 696, 14%** |
| Of those, text genuinely states a percentage | | 36, legitimate |
| Behaviour described, effect still a percentage | 214 | 65 |
| Primary-school multiplier band | 1.00 to 1.58 | 1.00 to 1.50 |
| Median primary-school multiplier | 1.10 | **1.00** |

**The median tree now has no primary-school damage percentage at all**, which is what Section 5.2 asked for. Arms, Combat, Retribution, Fire and Affliction all sit at 1.00 and get their damage from behaviour.

Two trees remain high. Destruction at 1.50 is almost entirely Ruin, whose vanilla text genuinely states a percentage and which should keep it. Shadow at 1.30 is Shadowform and Shadow Weaving, both of which state percentages in vanilla too.

## 5. Two rules earned their place during the pass

**`no-broad-zeroing` caught the converter producing exactly the error it was written for.** The instant-cast cue emitted `multiply castTime 0.0` scoped to the arcane tag, which would have made every arcane spell instant. The rule failed the build immediately.

**`percentage-drift` was tightened from 40% to 20%** once the first pass brought the worst trees under the old threshold. It now flags one core tree and seven expanded trees, which is the honest remaining list rather than a clean bill.

## 6. What is left

**Sixty-five talents describe behaviour and are still authored as percentages.** They are the ones whose text uses phrasing the converter's cues do not match, and they need reading individually rather than another regex pass.

That is the correct next step and it should not be automated further. **The converter got from 30% to 14% and each widening of its cues produced more false conversions**, including the one the zeroing rule caught. The remaining sixty-five are a hand-authoring job.

---

## 7. Finished, one by one

The automated pass got from 30% to 14% and then started producing false conversions, including one the `no-broad-zeroing` rule caught. The rest was done by reading each talent.

### 7.1 The rule was counting the wrong things

Before doing the work, the list needed to be honest. Of the effects the rule flagged:

| Kind | Count | Verdict |
|---|---|---|
| Magnitude below 1 | 16 | **The cost of a subtraction node.** Legitimate. |
| Scoped to one named ability | 13 | A specific buff. Acceptable. |
| Positive across a whole tag | **81** | The flat modifier 5.2 deleted. |

Only the third kind is the problem. A penalty is not a flat modifier, it is a price, and Sure Strike trading criticals for accuracy is the design working. The rule now counts only positive tag-wide multipliers, which raised the real number from 65 to 81 and made it worth fixing.

### 7.2 Result

**Tag-wide positive damage percentages: 80 to 6.**

Seventy-two rewritten by hand across three passes. The six that remain state a percentage in their own vanilla text: Shadowform's fifteen, Ruin's hundred, Death Wish's twenty, Amplify Curse's fifty, Deep Bond's thirty and Metamorphosis's form multiplier.

**A talent whose vanilla wording is a percentage should keep it.** Section 5.2 deleted percentages that existed *instead of* a mechanic, not percentages that *are* the mechanic.

### 7.3 The final band

| Tree | Primary school | Before | After |
|---|---|---|---|
| Warrior Arms | melee | 1.00 | 1.00 |
| Rogue Combat | melee | 1.00 | 1.00 |
| Paladin Retribution | melee | 1.21 | **1.00** |
| Mage Fire | fire | 1.10 | **1.00** |
| Warlock Affliction | shadow | 1.10 | **1.00** |
| Druid Balance | arcane | 1.18 | **1.00** |
| Priest Shadow | shadow | 1.40 | **1.15** |
| Warlock Destruction | fire | 1.58 | 1.50 |
| Blackguard | melee | 1.56 | **1.00** |
| Bladedancer | melee | 1.44 | **1.00** |
| Runeblade | weapon | 1.47 | **1.00** |

**Median 1.10 to 1.00. Eleven of thirteen trees now have no primary-school damage percentage at all.**

Destruction stays at 1.50 because that is Ruin, and Shadow at 1.15 because that is Shadowform. Both are vanilla talents whose entire text is a percentage.

### 7.4 What replaced them

The rewrites use the ops the texts already named: `debuff` for stacking vulnerabilities, `consume` for spending Blight, Charges, Momentum, Echoes and Kindling, `addTarget` for emissions and Thresholds and Chain Heal, `enable` with `immune_overheal` for the healing trees, `convert` for Open Hand making unarmed count as a weapon and The Runeblade making a weapon count as frost.

**Every one of those is a mechanic the tree already claimed to have and the data did not.**
