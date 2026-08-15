# After the Worth Fixes

**August 2026**

---

## 1. Everything back in band

**Core: zero violations of fifty cells.** Expanded: **thirty of thirty.** Tanking four of four, healing four of four.

The audit reports nothing outstanding across nine checks. Both configurations pass 24 rules clean. Both documents regenerate.

## 2. Four structural bugs, each larger than the talents they hid

**A spec did not cast its own school.** A Fire mage cast only Frostbolt, because raw throughput scored marginally higher, so **all eight Fire talents read exactly zero.** A spec now prefers its own school by thirty percent, applied after the mana blend rather than before it, or the blend dilutes it away.

It needed a second correction: the Fire tree references frost through Frostfire and Fire and Ice, so **counting any mention made both schools its own.** Using the dominant school fixed it.

**One rotation per class.** Druid had a feral list that had never been used, so a Feral build was measured casting Wrath and Starfire. Fixed, it reads **440 against the 290 it read as a caster** and ten Feral talents went from zero to contributing. Shaman, Priest and Paladin had unused healing lists too.

**Warlock and Hunter never summoned a pet**, though both hold a permanent one in vanilla. Seventeen pet talents were inert.

**A crit-conditional multiplier applied on every cast.** Ruin says it doubles the critical strike bonus, which at eighteen percent crit is worth about nine percent. Encoded as a flat multiply it paid fifty percent on every hit, so **a one point talent was worth half a tree.** The simulator now reads `when: event.critical` on multipliers.

## 3. A baseline that was not a build

For Blackguard the comparison fell through to **Holy paladin measured by a damage simulator**, and Blackguard read +70.6% on burst against it.

Paladin has only one core damage tree besides the host, so the host cannot be held constant. The baseline picker now excludes healing and tank trees, and where no valid baseline exists it compares against the best real damage build and states that the shallow half differs rather than hiding it.

## 4. What the levers taught

**A lever placed mid-tree lifts both the 31 and 30 builds and closes nothing.** I placed three cleave levers that way and none moved its gap. **A lever meant to close a capstone gap has to sit on the capstone**, because that is the only talent that differs.

**And a lever is sized against the scenario, not the tree.** Necromancy's movement bonus needed sixty percent to close a six point hole, because the movement scenario is only thirty percent movement, so the lever pays on less than a third of the fight.

## 5. Zero-worth talents

**89 to 73**, and the composition changed more than the count. Roughly a third of what remains is control, survivability or utility that a damage simulator correctly cannot see.

Fifteen genuinely inert talents were rewritten as scenario levers: opening windows for Unbridled Wrath, Improved Berserker Rage, Opportunity, Pyroclasm, Natural Shapeshifter and Convection; movement bonuses for Ruthlessness, Distracting Fire and Improved Nature's Grasp; periodic cleave for Crippling Grip, Relentless Strikes, Trapline and Storm Reach.

## 6. What is still open

**The remaining 73 are dominated by three causes**, and only the third is a design problem: an ability the build does not cast, an effect the damage simulator correctly cannot see, and a talent that genuinely does nothing.

**The healing and tank trees have never been swept with their own instruments.** My first attempt measured them with the damage simulator and reported every talent in them as worth zero, which is why they are excluded rather than reported. That sweep is the largest remaining piece of measurement work.

**The capstone-free results predate all of this.** Rogue at +6.7% and Druid at -34.4% were measured before the school preference, the pet summons, the crit fix and the rotation selection. **Both need rerunning before either is cited.**
