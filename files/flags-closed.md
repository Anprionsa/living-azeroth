# The Two Flags, Closed

**August 2026**

---

## 1. The healing and tank trees, swept with their own instruments

Never done before. My first attempt used the damage simulator and reported every talent in them as worth zero, which is why they had been excluded rather than reported.

| | Measured | Worth zero |
|---|---|---|
| Tank trees | 47 | **4** |
| Healing trees, before fixes | 51 | 24 |
| Healing trees, after | 51 | **14** |

**The tank instrument was healthy.** Four zeros, all in Protection paladin, and all four are buffs or utility a threat-and-survival model correctly cannot see.

**The healing instrument was not.** It read a fraction of the vocabulary the damage one does.

## 2. Four gaps in the healing model

**No grant gating at all.** Every ability in a healing rotation was castable regardless of whether the build had taken the talent granting it. Swiftmend, Holy Shock, Circle of Healing and Guardian Spirit were all free.

**No cooldowns.** **Guardian Spirit, a three minute ability, was cast 110 times in a five minute fight.** Then the fix did not work either, because the loop variable leaked and the cooldown was recorded against whichever ability the selection loop happened to end on.

**No per-ability multipliers.** Only tag-wide effects were read, so every talent of the "Improved Regrowth" shape was invisible.

**No cast time changes**, so a talent that makes a heal faster changed nothing about how many landed.

## 3. And then the real cause, which was the scenario

With all four fixed, the count moved 24 to 23.

**A healer doing 404 healing per second against a pattern delivering 440 damage per second is already covering it**, so every extra point of throughput became overheal and every throughput talent measured as worth nothing.

**The instrument could not see its own subject.** The damage patterns were sized for a healer working alone rather than a raid healer covering a share of a much larger stream.

Raised so a single healer covers roughly a third to a half of the incoming damage. Overheal fell from 65% to 5% for a druid, healers began using their full kit rather than one spell, and **23 zeros became 14.**

Every remaining Druid zero is now a genuinely non-healing talent: Improved Enrage and Reflection are rage and mana in forms, Insect Swarm is damage.

## 4. Healers still band

| Class | HPS gap | HPM gap |
|---|---|---|
| Priest | -0.1% | -0.1% |
| Druid | +2.1% | +1.6% |
| Paladin | +0.0% | +0.0% |
| Shaman | +5.3% | tuned from +27.9% |

Restoration shaman moved from +3.3% to +27.9% under the heavier patterns, which is the correct direction: its capstone is throughput and the old pattern could not show it. Tuned back to +5.3%.

## 5. The capstone-free results, rerun

Both predated the school preference, the pet summons, the crit fix and the rotation selection.

| Class | Before | After |
|---|---|---|
| Rogue best free build | +6.7% | **+5.3%** |
| Rogue within 7% | 56 of 114 | 54 of 114 |
| Rogue beating capstone | 6 | 5 |
| Rogue distinct results | 80 | 81 |
| Druid median | -34.4% | -34.8% |
| Druid distinct results | 15 | **18** |

**Both findings survive.** Rogue's three-tree split still beats the capstone and is still the widest design space in the game. Druid is still the most capstone-dependent class measured.

That the numbers barely moved across four structural fixes is the useful part: **these two findings are the most stable results in the project**, which was not true of anything on the damage side.

## 6. State

Core zero violations of fifty. Expanded thirty of thirty. Tanking four of four. Healing four of four.

`fullaudit.py` reports nothing outstanding. Both configurations pass 24 rules with zero errors and zero warnings.
