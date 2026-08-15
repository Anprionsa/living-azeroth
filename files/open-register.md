# Open Register: Classic+ Design Suite

**Version 1.1 | August 2026**

*Tracking document for the whole suite. Everything unresolved, everything blocked, everything already decided that should not be re-litigated. Items carry stable IDs so they can be referenced from any document or conversation.*

**How to use this.** Update it when something closes rather than remembering that it closed. Section 6 is the most valuable part of the file, because settled decisions are what get accidentally reopened after a gap.

---

## 0. Version state: resolved, fast-forward not merge

**REG-00. CLOSED.** Investigated rather than assumed, and the answer was simpler than the problem looked.

The two copies are not siblings needing reconciliation. The copy held elsewhere is a direct descendant of this one and a strict superset:

- Its Section 10 extends this one's 10.1 through 10.7 with 10.8 and 10.9, adding the holiday calendar snap and the weather rules.
- Its `proposals.json` carries 74 proposals against 33 here, on a six-axis schema (tier, cost, deployment, ptrReason, layer, change) against two axes here.
- Every seasons proposal in this copy has a counterpart there under a different id. `seasonal-cycle`, `seasonal-flora`, `seasonal-fauna`, and `seasonal-quest-scaling` became `full-seasonal-turn`, `herb-calendars`, `season-quest-scaling`, and related. Renamed, not lost.
- It also carries sections 6.9 to 6.11, 12, and 13, which do not exist here at all.

**Action: discard this container's `classic-plus-living-world-design.md` and `proposals.json`. Do not merge them.** Merging would reintroduce the older seasons text and downgrade the schema.

**One thing to port forward.** Appendix D, the provenance appendix, was written in this thread and does not exist in the canonical copy. A portable version updated for the newer structure is in `appendix-d-portable.md`. Append it to the canonical document. It already covers weather, the holiday calendar, art direction, inward zones, and world-state architecture, all of which are sections this copy does not have.

*Everything else in this register was written against this container's files and should be re-checked once the canonical copy is in hand, but no item below depended on the living world document's contents.*

---

## 1. Blocking decisions

Only Brendan can settle these, and work downstream of each is stopped until he does.

**REG-01. CLOSED. Band neutrality.**
Total raid output held constant, individual specs may move within it. Keeps the claim that this is not a power increase while allowing the worst gaps to close. Recorded in talent design section 0.

**REG-02. REASSIGNED, not blocked.** Depth coefficients get set per tree as each tree is rebuilt, since the ledger is per tree anyway. No longer a standing blocker; it is a step in REG-10.

**REG-03. CLOSED. Unconventional builds are a goal, and the curve is linear.**
Depth carries an edge through discrete talents, never through an accelerating stat curve, so spreading points costs no stats and the difference lives entirely in which talents you own. Cross-tree conditionals at tier 6 and tier 5, with a few cheap ones lower for three-way splits. Absorbed trees participate in both directions. Interdependencies are told in the world rather than in tooltips. Recorded in talent design 5.6 and 5.7.

**REG-07. NEW, and it constrains every tree rebuild from here.**
A cross-tree conditional may never be the reason to take the talent it sits on. The talent must be worth its points alone; the conditional is upside. This is what makes it safe to describe interdependencies in the world rather than in the interface, because ignorance then costs a player upside and never correctness. **Checked.** Mortal Cleave passes: Cleave and Whirlwind are baseline, so it is worth its points to any warrior. Pack Tactics failed and was rewritten; its rank 3 read "Bestial Wrath also grants you its damage bonus," which is worth nothing without the Beast Mastery capstone. Every future cross-tree talent gets this check before it is written down.

**REG-05. NEW. Absorbed tree local mechanics need a scaling target.**
Follows from REG-03. Section 8.3 gives absorbed trees no stat curve, so splashing one costs stats that splashing a vanilla tree does not, which discourages exactly the builds REG-03 wants. Their local mechanics must scale with depth to parity with the dividend a vanilla tree of the same depth would grant. A constraint on the absorbed trees that did not exist when they were built.

**REG-24. NEW, and it should be run again after any future rule change.**
A compliance audit of all 27 rebuilds against the final rule set found five trees with no subtraction node and five gate-20 tiers still under eight points. All closed, recorded in talent design 19.6. This is the fourth instance of the same failure: a rule lands, the prompting passage gets fixed, the rest of the document does not get swept. **Treat a rule change as a document-wide operation by default.**

**REG-06. Mid-tree talents need weighting against capstones.**
The checkable rule from 5.6: two tier-5 seats plus a tier-2 should land in the same band as a capstone plus a tier-4. Vanilla back-loads almost all tree power into its last rows, so this is a real tuning target rather than a formality.

---

## 2. Queued work, not blocked

**REG-10. CLOSED. All 27 trees rebuilt.**
Done, in order of severity: Enhancement and Demonology at 28, Feral Combat at 26, Retribution at 24, Marksmanship, Protection paladin, Discipline and Elemental at 23, Holy priest at 20, Balance at 19, then the five-tree 18-band (Beast Mastery, Survival, Restoration shaman, Affliction, Fury). Arms is done but was the wrong tree and survives only as method.

**REG-10 COMPLETE. All 27 trees rebuilt.** Section 6 (Arms) is retained as the record of how the method started, with a current-rules note attached in Section 19.5 rather than being rewritten.

What the rebuild pass produced that the floor measure did not predict, all now recorded in the design document: permission nodes (Enhancement), premise failure (Demonology), structural underweight (Feral, Retribution, Holy paladin), sparse hybrid tiers in eleven trees, the weapon fork as a shared component across five, capstones that buy only a stat (Assassination), talents keyed to named spells (Holy priest), pet stat multipliers (Demonology and Beast Mastery), and the no-choice tree (Restoration druid). Note from REG-11: dead nodes free almost no points, so the rewrite budget does not shrink.

**REG-12b. NEW, generalised from Demonology.** A tree can fail its premise rather than merely being flat. Demonology's most-used talent kills the demon; the tree named for a thing contains nothing about doing that thing. Before rebuilding any remaining tree, ask what decisions the spec actually makes and check whether the tree addresses any of them. Flatness is measurable and this is not, so it needs asking deliberately rather than falling out of the floor figure.

**REG-09. CLOSED. Permission sweep run across all 27 trees.** Exactly two permission nodes exist in the game, Two-Handed Axes and Maces and Parry, both in Enhancement shaman, both already handled. Improved Shield Block matched the screen but improves an existing ability rather than granting one. The pattern is confined to a single tree.

**REG-16. RULE, refined once. A passive aura never belongs at a capstone; an active ally cooldown does.**
Trueshot Aura, Leader of the Pack, and Sanctity Aura are passive and permanent, which makes them obligations, and all three move to the depth dividend. Power Infusion forced the distinction: it targets an ally but the priest chooses when and on whom, which is a decision, so it stays at Discipline's capstone. Innervate is the same shape. Recorded in talent design 10.3 and 13.1.

**REG-17. Three trees are structurally underweight at 45 points.**
Feral Combat, Holy paladin, and Retribution, against 62 for Combat rogue. Feral is worst because it carries two roles at 45. Feral and Retribution grew to 55 and 52. Holy paladin is the one left. Growth in available points is not a power increase under band neutrality, since 51 points to spend is unchanged, but it should be stated rather than slipped in.

**REG-18. Seen eleven times. Sparse hybrid tiers.**
Gate 20 holds three points in Feral and Elemental, four in Balance, Survival, and Restoration shaman, four in Holy paladin, Frost, and Assassination, five in Protection warrior, and six in Protection paladin, Discipline, Affliction, and Subtlety, against ten or more at gate 5 or 10. Eleven of 27 trees. This is the most common structural fault in the game and every rebuild has had to correct it. That is why those trees score badly on the hybrid seat measure: the seat is not badly designed, it is nearly empty. Every remaining rebuild should check its gate-20 weight before anything else, and rebalance downward from an overweight gate 5 rather than adding points.

**REG-21b. NEW. The weapon fork now applies to five trees.**
Arms, Enhancement, Fury, Combat rogue, and Bladedancer in Class Absorption all collapse a weapon specialization block into one node whose effect reads the equipped weapon. Combat rogue is the largest case: 27 of 62 points across five nodes become one node and five points. This is now the single most reused pattern in the rework and should be stated as a shared component rather than reinvented per tree.

**REG-23b. NEW. The no-choice tree needs 5.4, not 5.2.**
Restoration druid is 13 of 30, one of the healthiest floors in the game, and players still complain. The tree is not full of filler, it is full of talents so obviously mandatory that nothing is decided. Making a mandatory talent more interesting leaves it mandatory. The fix applied was three mutually exclusive one-point paths at the hybrid seat. Check every rebuilt tree for the same shape: a low floor plus a locked build means the choices are missing rather than the content.

**REG-22b. Two capstones buy nothing but a stat.**
Assassination's Vigor increases maximum energy by 10 and nothing else, the only capstone in the game whose whole text is a number. Replaced. Worth confirming no absorbed tree capstone has the same shape.

**REG-20. Pet trees are the same disease twice.**
Demonology and Beast Mastery are both dominated by pet stat multipliers, eleven of sixteen nodes in Beast Mastery's case, with the same consequence: the pet families become one pet with different art. Both rebuilds fixed it the same way, by giving each family a distinct ability rather than a distinct percentage. If any absorbed tree carries a pet, it inherits this problem.

**REG-19. Talents keyed to named spells strand when encounter design moves.**
Holy priest is the case: Improved Healing, Improved Prayer of Healing, and part of Divine Fury buff spells vanilla raids do not cast. The fix applied there was to change the subject from specific spells to healing behavior, so that a talent reads "any heal that lands on a full-health target" rather than "Greater Heal." Worth applying wherever a talent names a spell rather than a situation.

**REG-11. CLOSED. Dead node sweep run across all 27 trees.**
Screened for boss-immune effects, creature-type conditionals, and PvP-only effects. Twenty-eight nodes flagged, one kept: paladin One-Handed Weapon Specialization in the Protection tree. Two more are dead in raids only. The rest were riders on talents whose real effect is something else, or alive in a context the screen could not see.

**The definition tightened as a result:** a talent is dead only when the thing it modifies is something the spec no longer does in *any* context it is played in. Useless in raids and useful in PvP is not dead. Recorded in talent design 1.2.

**Consequence: dead nodes free almost no points, so the Section 5.2 rewrite budget does not shrink.** That assumption in REG-10 was wrong and is corrected.

**REG-08. CLOSED. One set of talents serves both modes.**
No PvP-only nodes, no PvP branch, and explicitly no assumption that gear will bridge the gap. Prefer graded effects to binary ones, since a slow or an armor reduction works on a boss at reduced relevance while a stun works at zero. Binary effects that are worth keeping need a graded fallback. Recorded in talent design 5.8. Smaller cleanup than expected: Warrior Protection carries the most mode-locked content at three nodes, most trees carry one or none, and Enhancement carries none.
*Source: talent design 1.2.*

**REG-12. CLOSED. Absorbed trees audited.** `trees.json` received and measured with the same method as the 27 vanilla trees. Result: 54% flat against vanilla's 73%, mean forced flat 8.6 of 30 against vanilla's 17.4. Blackguard and Necromancy at 5 would be the two healthiest trees in the game. They need a pass, not a rebuild. Full findings and the change list in `absorbed-audit.md`.

**REG-25. CLOSED. Absorbed tree revisions written to `absorbed-revisions.md`.**
All seven get a cross-tree conditional at gate 20, gate 20 grown from six to eight, and their flat nodes deleted into local-mechanic scaling. Metamorphosis fully rebuilt, Survival replaced by the Section 17.2 rebuild, subtraction nodes added to Metamorphosis, Conduit, and Survival, Damnation phrasing aligned.

**Two findings expanded the scope beyond a pass:**

**REG-26. Zero cross-tree conditionals existed in any of the seven trees.** The twenty-point mark is a good talent at gate 20, not a talent that reads the host's other trees. Across 414 points, no talent is conditioned on host-tree investment. That is the gap REG-03 explicitly asked to close and it was total rather than partial.

**REG-29. CLOSED. Chronomancer added and integrated.**
An eighth absorbed tree, a mage healing spec built on Echo, a recorded snapshot of an ally's health spent to return them to it. Written to the finished rule set: 58 points, gate 20 at eight, no pure-modifier nodes, one subtraction, two cross-tree that both stand alone, and 46 of 58 points referencing its own mechanic, which is the highest coverage of any tree in the suite.

Integrated into `classic-plus-class-absorption.md` as Sections 7.8 and 9.9, added to `trees.json`, and the suite swept for the references it made wrong. **The integration also carried REG-C10's tier arithmetic correction into the class document, where Section 9.1 still claimed twenty points reaches the twenty-point mark.** Fifth instance of the same propagation failure; see REG-24.

Mage now has five trees against four for every other host. Justified from the audit rather than from symmetry: mage has the healthiest trees and the most repetitive gameplay, so a second absorbed tree addresses the problem the talent rework explicitly cannot.

**REG-44. NEW. Four fields authored, three confirmed blocked.**
Filled: `crossTree.target` on 47 talents, `crossTree.standsAlone` on the same, `flags.subtraction` from a curated list, and `reads` across the absorbed and original trees. Left empty deliberately: `reads` on vanilla trees, since vanilla is being replaced. Genuinely blocked: `modifies` and `grants` need the abilities table, `dividend.stats` needs simulation per REG-02.

**REG-45. NEW. The build prediction was wrong by hand and is now a query.**
`analyse.py` derives cross-tree edges from the data: **48 edges, 15 mutual pairs, 16 one-way, and every class now has at least one mutual pair.** The hand count in `partial-builds.md` found 11 and claimed mage and warlock had none. Mage's Fire tree was one of the four written out later; warlock's pairs came from the gate-20 rebalancing that postdated the analysis. Warrior Protection reaching toward both Arms and Fury was missed entirely. **Every analysis built by reading prose in this project has needed correcting at least once; every analysis built against structured data has held.**

**REG-50. NEW. Canonical source declared, because the divergence recurred in reverse.**
Twelve reciprocal nodes were authored directly into `talent-data.json` and appear in no document. That is the same data-versus-prose split the schema was built to prevent, running the other way. **Rule now recorded in `meta.canonicalSource`: the data is canonical for WHAT a talent does, the documents are canonical for WHY.** Tree listings in the documents are a rendering of the data and should be regenerated by `render.py` rather than hand-maintained. Hand-editing either side is what produced every divergence in this project.

**REG-67. NEW. The simulator runs, the shapes separate, and it found three bugs reading never would have.**
Warrior, six shapes, twenty seeds: **47% spread across shapes against 2.7% run-to-run noise.** Separable, which is the minimum condition for continuing.

**The most important finding is a modelling bug with implications beyond the sim.** Talent-granted abilities were available to every build regardless of whether it owned the talent: a five-point Arms build was casting Mortal Strike. Every earlier reasoning-based claim about what a build does was made against that unchecked assumption. The fix reads authored `grant` effects, which cover 16 abilities, plus the `grants` field from name matching, which covers 94. Authored effects alone would have left 78 capstones free to builds that never paid for them.

Also found: the build selector never reached a capstone, because a greedy top-down fill spends 31 points on the first three rows, so "Arms 31" contained no Mortal Strike. And Execute had no health gate and fired 177 times as the top-priority free ability.

**REG-111. CLOSED. Arms cleave fixed by periodic cleave, and it is the cleanest lever shape found in the project.**
Arms read -16.7% on three targets. **Making Mortal Strike itself hit more targets barely helped**, gaining one point at two targets and two at three, because it is cast too rarely to matter. **A periodic cleave on every strike gained 18.8 points at zero cost on one target**, and every variant tested had zero cost, because cleaving is worth nothing when there is nothing to cleave into.

Adopted at every third strike sweeping two, carrying the wound. **Arms now reads +1.2% patchwerk, +2.2% cleave, +1.2% movement, +2.9% switching.** Burst at -6.6% is the remaining cell.

**REG-141. ERROR, mine. Every build analysis for several passes excluded the expanded trees.**
Recorded in `expanded-builds.md`. `A.builds(cls)` defaults `withExpanded=False` and every call used the default, so **the 320-build comparison, the 69 hybrids, the build names and the band-neutral targets were all core only.** Two smaller faults in the same map: **it held one tree per class so Chronomancer was silently dropped**, and Druid and Priest had no entry rather than an empty one.

**The tuning itself is intact.** The band-neutral pass scaled by class rather than tree, so expanded trees took their class coefficient correctly: Blackguard at Paladin's 1.2711, Necromancy and Chronomancer at Mage's 0.8527.

**Four of nine classes have an expanded tree in their best build.** Warrior Fury 31 / Runeblade 20 at **+17.3%**, Rogue Assassination 21 / Bladedancer 20 / Combat 10 at **+21.0%**, Shaman Elemental 26 / Conduit 25 at +8.4%, Paladin Blackguard 31 / Retribution 20 at +4.1%.

**The five unchanged are the more interesting half.** Druid and Priest expected, since Dreamer and Radiance are held out. **But Mage, Warlock and Hunter have Necromancy, Chronomancer, Metamorphosis and Survival available and none beats their best core build.** That is the absorption proposal working: an absorbed tree that beat every core build would make the core trees obsolete, which is the failure the whole argument was avoiding.

**Warrior's +17.3% is defensible and Rogue's +21.0% is not.** Warrior's gain is Protection being useless to a damage build, so Runeblade fixes a structural gap; **Rogue already had three usable damage trees, so Bladedancer beating all of them means it is simply stronger.** Bladedancer sits at 0.8169, the same as the core rogue trees, so the pass never treated it separately. One number fixes it.

**REG-140. CLOSED. Band neutrality run.**
Recorded in `band-neutral-pass.md`. Lever is `depthCoefficient`, **one scalar per tree, no talent edits.** Strict neutrality first, to check it works: nine classes within two points in four iterations.

**A measurement error worth recording: share sums are the wrong measure.** Widening to a floor of 50 gave targets summing to 578 and a result of 632, and renormalising every class equally changed nothing. **Shares are relative to the top spec, so scaling everything leaves them identical while the raid total falls. Band neutrality has to be checked on absolute output.**

**Measured properly it works. Logged raid total 7,958 dps; band neutral 8,027, floor 50 at 8,014, floor 55 at 8,035, floor 60 at 8,032.** All within one percent while the floor moves 37% to 58%.

**And compression costs no build diversity: 95 of 320 builds within seven points of their class best, identical at every floor.** The depth coefficient scales a whole tree and leaves the relative worth of talents inside it untouched, so **compressing the ladder between classes does not compress the choices within one.** Every alternative way to raise Paladin would have changed which Paladin builds are worth taking.

**Committed at floor 55. Paladin 37.6% to 54.3%, Priest 47.5% to 56.3%, Shaman 50.1% to 63.1%, Druid 58.9% to 70.0%; Warlock down 82.6% to 73.1% and Rogue 94.8% to 88.1%.** The floor is 54% against vanilla's 31.6%.

**Fifty leaves Paladin at 48%, low enough that a roster-optimising guild cuts it. Sixty compresses the top four into fourteen points, which is the saturation shape.** Fifty-five keeps a 46 point spread. **All four configurations are saved and moving between them is one pass.**

**REG-139. All 320 reworked damage builds against the averaged Classic ladder.**
Recorded in `all-builds-vs-classic.md`. Reference is the mean of the two Classic controls. Builds whose deepest tree is a healing or tank tree are excluded rather than reported as zeros.

**The order is intact**: Warrior, Rogue, Mage, Warlock, Hunter, Druid, Shaman, Priest, Paladin, exactly as logged. **But the five classes that exceed their logged best are the top five**: Rogue +10.6, Warlock +18.2, Mage +8.9. **That is not band neutrality; total raid output has risen rather than staying flat.**

**Not one of the bottom four classes can reach its own logged output with any available build.** Druid 58.9% against 60.5%, Shaman 50.1% against 51.8%, Paladin 37.6% against 39.1%. **Paladin's sixteen builds span 37.1% to 37.6%, half a point.**

**Five of nine classes have a hybrid as their best build**, which is the rework's central claim landing: Warlock at Affliction 26/25, Priest at Shadow 26/25, Paladin at Retribution 26/25, Hunter at MM 30/21, Shaman at Elemental 30/21. In vanilla the answer is always the 31-point build.

**The clearest measure of the problem is the medians. Rogue's median build is 84.3%, which is its logged best; Druid's is 40.1% against a logged 60.5%.** The classes that were strong got a wide band of good options and the classes that were weak got a narrow band of poor ones.

**This reframes the open question.** The bottom has not moved and the top has, so raising the bottom widens total output further. **Lowering the top is the band-neutral answer and has not been attempted.** The depth coefficient reaches both, one number per tree with no talent edits, and can pull the top three down while pushing the bottom three up until total output matches the logged total. **That is a single tuning pass, the one the protocol described, unrun because the target was never set.**

**REG-137. CORRECTION. The SoD reading was wrong and the error was selection.**
Recorded in `tail-and-target.md`. I reported SoD's spread as 13.2 points against Classic's 68.4 and read it as deliberate near-parity worth considering as a target. **The 13.2 came from taking the twelve SoD specs that matched the Classic list and dropping nine. The full twenty-one spread 92.9 points.** SoD is **sixteen specs bunched at a ceiling and five abandoned below it**: Beast Mastery 83%, Combat 71%, Demonology 67%, **Arms warrior 34%, Arcane mage 7%**.

**Selecting the overlapping subset selected the specs near the ceiling and dropped the tail**, which inverted the finding. Any future control must be compared on its full spec list or not at all.

**And the compression is saturation, not balance.** The top sixteen sit inside 1.15x with **no adjacent gap above 2.6 points**, where Classic's gaps run 18.4, 10.8, 9.4. **Content tuned too easy compresses everything that clears the bar and strands everything that does not**, which is a flat middle and a long tail at once. **SoD cannot be used to judge class balance in either direction, and the alternative target I described does not exist.**

**REG-138. NEW. Band neutrality was chosen on paper and strict neutrality is what got delivered.**
| | Bottom spec | Bottom three | Top to bottom |
|---|---|---|---|
| Classic median | 31.6% | 34.8% | 3.16x |
| Classic top 10% | 39.3% | 40.9% | 2.54x |
| **Rework** | **35.6%** | **38.2%** | **2.81x** |

**The rework preserves the ladder and has not lifted the tail.** Balance druid is 35.6% in both.

**Build variety and a floor are separate promises and only one was delivered.** Checking each bottom spec's best reworked build rather than its canonical one: **Shadow priest gains 5.6 points from a hybrid vanilla does not reward; Balance druid gains 0.2.** A player who wants Balance raid-viable is not helped by it having three viable ways to be 35% of a warrior.

**What needs deciding before any more tuning is what the bottom of the ladder should be.** Classic's median puts it at 31.6% and its top parses at 39.3%; **something in the fifties would make every spec raid-viable without flattening the ladder, and it is reachable with the depth coefficient alone**, one number per tree and no talent edits. **That is a design decision and I am not making it by tuning toward whatever the sim currently reads.**

**REG-136. CLOSED. Three controls established, and the decisive number is how far apart the published ladders are from each other.**
Recorded in `controls-established.md`. Added **wowtbc.gg Phase 6 Naxxramas**, twelve specs at top 10% parses rather than medians, which makes it an independent second reading of the same game. Added **Season of Discovery Phase 7**, twenty-one specs.

**The two Classic controls disagree with each other by a mean of 4.4 points of share and 21.6 at the extreme.** That is the noise floor. **The sim sits 4.6 from one and 4.2 from the other, so it is as close to each published ladder as they are to each other**, which is the strongest form the claim can take and also its ceiling. Excluding Mage Frost the errors fall to **0.8 and 2.3 points**.

**Six free tests where there were three.** Shaman Elemental +2.4 and -5.6, Druid Balance -0.0 and -3.7.

**Frost reads differently against the second control and it changes the recommendation.** It is 31.6% at median and **53.2% at top 10%**, the largest disagreement between the sources. **A spec whose good players parse enormously higher than its median players is hard rather than weak**, so the rework is lifting it from somewhere between the two, and 77.8% is an overshoot of about twenty-five points rather than forty-six.

**SoD is not a validation target and saying why matters**: runes changed every class while the trees did not, so agreement would be coincidence. It is worth having for a different reason. **SoD's spread is 13.2 points against vanilla Classic's 68.4**, and the rework sits at 64.3. **That is vanilla's shape, not SoD's**: the ladder preserved and individual specs fixed within it, which is band neutrality doing what the protocol said. **It is a position rather than a default, and the alternative was available**: if the goal were every spec viable, SoD shows the target is thirteen points.

**Still not established: a nine-parameter fit to nine numbers proves nothing**, and free tests are limited to the three classes with two logged damage specs. **A fourth control needs a version where specs shift while talents stay comparable**, which is Season of Mastery, whose per-spec numbers are not readily published.

**REG-135. CLOSED. Compared against real Naxxramas logs.**
Recorded in `log-comparison.md`. Control downloaded rather than simulated, per `sim-baseline-protocol.md` section 2: Warcraft Tavern Phase 6 Naxxramas rankings, January 2026, from Warcraft Logs Classic Fresh, twelve specs.

**The first attempt was nonsense: Rogue read 100% and Warrior 35%, inverting the logged order.** The cause is that **the gear blocks were invented per class, hardcoded in the simulator rather than held in the data, and never checked against each other.** Within a class the 31 versus 30 comparison was always valid since both builds wear the same invented gear; **across classes the absolute numbers meant nothing.** Blocks moved into `talent-data.json` and calibrated: nine classes, all within 3.2% of their logged spec.

**Nine of the twelve are calibration targets and cannot fail. Three are free tests**, being the second spec of a class whose gear was fitted to its first. **Shaman Elemental lands +2.3 points off its logged share, Druid Balance +0.1.** Two independent predictions inside three points on a 68 point ladder, which is the strongest evidence in the project that the trees behave like the game.

**Mage Frost is the third and it is off by +46.2, from 31.6% logged to 77.8%.** That is the rework doing its job rather than an error: vanilla Frost is last of twelve and not raid-viable. **Whether parity with Fire is the right landing is a design decision. I would say no**: Frost and Fire being interchangeable removes a choice rather than adding one, and the case is stronger saying Frost went from unplayable to competitive than saying the two are now the same. Sixties rather than seventy-eight.

**Spread holds. Logged 68.4 with stdev 19.6; sim patchwerk 64.1 / 19.1 and burst 63.3 / 18.3**, slightly tighter, which is what band neutrality predicts. **Cleave is 83.9, fifteen points wider, and that is expected**: the reworked trees carry periodic cleave levers and the logged control is single target.

**What it does not establish: a nine-parameter fit to nine numbers proves nothing.** The claim rests on two free tests. **Adding Season of Mastery and Season of Discovery would give more**, since specs shifted between versions and the trees did not.

**REG-134. CORRECTION. The variation pass was a mistake and has been reverted entirely.**
Recorded in `voice-correction.md`. Prompted by the edits reading as machine-written, and the example given was a **comma splice**: "The health does not fall away when the effect ends, it drains." A negation followed by a comma and a corrective clause is the specific construction that reads as generated.

**Two passes ago I found "cannot be" in 164 of 696 talents and called it a checklist. That judgement was wrong and the fix was worse.** **Wrong because vanilla repeats it freely**: resisted, dispelled, interrupted and dodged are the game's own vocabulary for what a talent removes, and a player reading them across a tree reads consistency rather than repetition. **Worse because the substitution produced grammar errors in three separate rounds**: "Healing spells finishes whatever interrupts it by damage", then "your attacks is never dodged", then nineteen more including "Your Seal procs always lands" and "They always lands" after a fix that covered a fixed noun list and missed the rest. **Reverted on all 53 talents, back to 162 instances.**

**"Rather than" at 57 uses was a real tic and did come from me**, reduced to 46. That substitution also went wrong: **"instead of" takes a noun phrase, and before a preposition or gerund the correct choice is "rather than"**, so seventeen were reverted. **Bullseye had drifted into abstraction**, describing a talent's purpose rather than its effect.

**The lesson: "if nothing is wrong, don't fix it" was applied to structure but not to register.** The consistency pass correctly left a three-word talent and twenty-five long ones alone, while the pass before it had already changed 53 talents on a judgement that repetition reads flat, which was taste presented as a fault. **A repeated phrase the source material also repeats is a house style, not a defect.**

**REG-133. CLOSED. Consistency pass. 27 talents fixed, 27 flagged and correctly left alone.**
Recorded in `consistency-pass.md`. **Three number-agreement errors from the previous pass's own substitution**: varying "cannot be" without checking the subject's number produced "your attacks is never dodged" and "your spells shrugs off interruption".

**Twenty-two raw vanilla tooltips the rules were not catching**, and it took two widenings. **Nine opened with a verb the pattern did not list**, since it required "Increases the" and these read "Increases chance to block by 30% for 10 sec". **Thirteen more opened with "When activated,"**, vanilla's other stock construction, which was in no pattern at all. A `no-vanilla-tooltip` rule now covers both.

**Two things were flagged and left alone after reading them.** `Destructive Reach` opens "Range increases.", which matched a fragment check and **is not a fault**: the established voice does exactly this, as in "Shouts affect the raid. Persist through death." And **twenty-five talents over 42 words are all five-rank talents describing five effects**, where compressing them would break a rule that matters more.

**Why this kept recurring: three passes each found vanilla survivors, and each time the rule matched a narrower pattern than the fault.** `by N%` missed `a N% chance`; `Increases the` missed `Increases chance`; neither covered `When activated,`. **A rule written from the examples in front of you catches those examples**, so the pattern now matches the category rather than the phrasings.

**REG-132. CLOSED. Prose pass. 97 talents touched, and build advice was sitting inside fifteen tooltips.**
Recorded in `prose-pass.md`. The worst finding and the one no rule was watching for: **fifteen talents had design-doc reasoning written into their text**, as in "Every druid heals, so it stands alone, worth most to a Restoration main at 26/25." **A player reading a tooltip should learn what the talent does, not which point split it suits.** One was worse: Restoration's Wild Growth **ended mid-sentence on a colon** where the commentary had been cut from a source document.

**Seven talents still opened with raw vanilla tooltip phrasing**, including "Places a Blessing on the friendly target" and "Gives the Paladin a chance to". **Three referenced the design rather than the game**, one of them describing "the same fork as Arms, Enhancement, Combat rogue, and Bladedancer", which a player cannot see. **And one N placeholder survived two passes** because the rule looks for `N%` and Improved Enrage had a bare `N`.

**"Cannot be" appeared in 164 of 696 talents.** Every instance individually correct, a quarter of the trees reading as a checklist. **A first attempt substituted blindly and produced "Healing spells finishes whatever interrupts it by damage"**; reverted, and the second pass substitutes only where the phrase closes a clause. **164 to 117, deliberately not zero**, since the phrase is correct vanilla usage.

**Checked and left alone: length**, median 23 words with the 25 longest all being multi-rank talents describing three or five effects, and **repeated openings**, which are a tree's subject matter showing through.

**REG-129. CLOSED. Reading pass. 42 talents rewritten, and the placeholder rule was passing on nineteen it existed to catch.**
Recorded in `reading-pass.md`. **The established voice is bare declarative sentences, one per rank, with no rank markers**: "Shouts affect the raid. Persist through death. Refresh on a killing blow." **Sixteen talents used an "At two ranks... At three..." construction and every one was written during the tuning passes.** That is design-doc voice explaining a mechanism from outside the game. Dark Pact used a colon introducing a list and Envenom stated a number where the convention states a behaviour.

**The pass also found nineteen talents still carrying raw vanilla text with N placeholders.** The `no-placeholder-text` rule matched `by N%` and `N sec` and missed `a N% chance`, which is the more common phrasing, **so it was passing on nineteen talents it existed to catch.** Widened and all nineteen rewritten.

**42 talents rewritten. Both documents regenerate with zero stale text, `vanilla-voice` and `no-placeholder-text` both pass, zero em dashes.**

**REG-130. CLOSED. Warrior's narrowness is an argument for the expanded configuration, not a fault in the core one.**
The one-shape result was measured on core, where the third tree is Protection and a damage build correctly gets nothing from it. **With Runeblade available the capstone-free space goes from 1 shape within seven percent to 79, with Runeblade in 66 of them.** The clearest case in the project of an absorbed tree solving a structural problem rather than adding content. Runeblade retuned to +5.2% sustained after the Death Wish and tie-break changes, cleave lever sized to every fourth strike.

**REG-131. Dreamer and Radiance moved to a third configuration, `candidate`.**
**Held out rather than deleted.** Both remain authored and validated to the same standard; switching them on is a configuration change rather than rework. Expanded is now 27 rebuilt plus 7 absorbed plus Chronomancer, and both configurations validate clean.

**REG-128. CLOSED. The simulation work is ready to hand back to design, and two things were not ready when asked.**
Recorded in `handoff.md`. **Four talents had drifted out of the talent document** during tuning and **41 of 90 files were missing from the manifest**, which is the file a reader opens first. Both fixed; documents regenerate with zero stale text and the manifest covers all 90 files including the eleven simulation scripts and twenty-nine records.

**Settled: 5.6's tuning rule holds** at zero violations of fifty cells, **hybrids are real builds** with every class within 6.3% and four of six beating the capstone, and **the band was chosen on evidence** with the signature-scenario exemption I argued for across four passes dropped because it priced worse than simply widening.

**Changed: eleven talents rewritten because measurement showed they did not work.** Dark Pact, Shadow and Flame, Unbound, Death Wish and seven others. **Nine rogue talents modified a tag no ability carried.** Thirty percent of authored talents had drifted into percentages and were repaired.

**Cannot answer: absolute numbers**, which need Warcraft Logs as the control per `sim-baseline-protocol.md` and have never been validated; **anything not throughput, threat or healing**, which is what `simulable: false` marks; and **whether any of it is fun.**

**For design to pick up: the eleven rewritten talents need reading as prose** rather than as numbers, since they were written to satisfy a measurement. **Warrior's single viable hybrid is a design question the simulator surfaced and cannot settle** ,  whether a class whose third tree is a tank tree should have a third damage-relevant one. **Dreamer and Radiance remain candidates** whose inclusion was never decided.

**REG-127. CLOSED. Full pass on core and hybrid. Core zero of fifty, and every class has a capstone-free build within 6.3% of its best.**
Recorded in `full-pass.md`. Rogue +6.3%, Hunter +4.9%, Warlock +4.8%, Mage +3.4%, Warrior +0.5%, Druid +0.0%. **Four of six have a capstone-free build that beats the capstone.**

**Death Wish was a cliff.** A one point gate-20 talent carrying **both a permanent ten percent and a cooldown**, so every warrior build had to reach exactly twenty-one Fury and **Warrior had one capstone-free shape within seven percent** with the next ten points behind. Removing the permanent half swung it to **zero** shapes, and raising the cooldown from 1.45 to 2.00 recovered under two points because a cooldown is a small share of five minutes. **Settled at seven percent permanent plus the cooldown: the problem was the size, not the combination.**

**The Rogue lever runs backwards.** Rogue read +10.0% with sixteen shapes beating the capstone, and **weakening poison made it worse**, to +13.2% with forty-four beating, because Master Poisoner's entire value is skipping the poison ramp so cutting poison cuts the capstone harder than the spread. **Raising poison 36 to 60 base brought it to +5.8% with one beating.** Only measurement would have shown the direction.

**Warrior stays narrow at 1 of 114 and it is structural.** Its third tree is Protection, which correctly gives a damage build nothing, so the class has four real shapes. Hunter has the same structure and reaches 28 because Beast Mastery still gives a damage build a pet.

**REG-126. CLOSED. The Warlock gap was Demonology being worth nothing as a partner, and it is now 9 shapes to 19.**
Recorded in `warlock-chase.md`. **Every viable Warlock build was Affliction plus Destruction and Demonology appeared in none**, so the class effectively had two trees to combine. Mage's weakest tree appears in 14 of its 31 working shapes.

**Twenty-one points in Demonology bought no damage modifiers at all.** Two causes. **A caster's pet was scaled off attack power it does not have**: the base read `attackPower` with a 700 default for any class lacking it, so a warlock's demon contributed 31 damage per second. Pets now scale off spell power for casters and a demon reaches about a fifth of output. And **Unbound was authored as a percentage**: its text reads "you may have two demons active at once" and its effect was `add damage 0.3`, so **the talent that makes a Demonology splash worth taking did not do the thing it describes.**

**A selector fault the fix exposed: on a tie the selector preferred the shallower talent**, so Unbound had the highest value at its gate and was still not taken, and the last points never reached the deep rows. Players build deep; ties now go to the deeper talent. That moved every class.

**Warlock 9 of 114 to 19, Demonology appearances 0 to 4, the partner gap 144 points to 90.** Still the weakest of the three, so narrowed rather than closed. **The residue is that Destruction 21 reaches Ruin and Demonology 21 reaches Unbound, and a second demon is worth less than doubling critical damage.** Forcing those level would make Demonology the default splash for every warlock, which is the same failure in reverse.

**REG-125. CORRECTION. The capstone-free median is not a measure of design health, and I reported it as one twice.**
Recorded in `reading-the-number.md`. Druid's -34.8% is the middle of 114 shapes **most of which put points in Restoration**, a healing tree where a damage build's points do nothing. Split out: **every Feral plus Balance shape sits between 0 and -8%; every Feral plus Restoration shape falls to -27% or worse.** That is correct, not a fault.

**Restricted to damage trees only, the picture inverts.** Druid reaches -18.4% on 2 of 4 shapes, Warrior -3.7% on 2 of 4, Hunter -1.5% on 4 of 4. **Rogue's 55 of 114 against Druid's 25 is not better design, it is three damage trees against two**, and a class with two only has four shapes to have.

**The one real finding: Warlock has three damage trees and only 9 of 114 within seven percent**, against Mage's 31 on the same structure. That gap is worth pursuing and nothing else here is.

**I reported the Druid median twice, first as "nothing matters" and then as "strongly capstone-dependent". Both took the median of a population that is mostly off-role builds.** The number to watch is the best capstone-free shape and how many cluster near it, restricted to trees the build can use.

**Corrected headline: every class has a capstone-free build within four percent of its best capstone build.** Rogue +5.3%, Mage +3.3%, Druid +0.0%, Warrior -0.1%, Hunter -1.5%, Warlock -3.8%. **That is a better answer to the original question than any median I quoted.**

**REG-123. CLOSED. Healing and tank trees swept with their own instruments for the first time, and the healing model could not see its own subject.**
Recorded in `flags-closed.md`. **Tank trees were healthy at 4 zeros of 47**, all buffs or utility a threat-and-survival model correctly cannot see. **Healing was not: 24 of 51.**

**Four gaps in `heal.py`.** **No grant gating at all**, so every ability was castable regardless of the build. **No cooldowns**, so Guardian Spirit was cast 110 times in five minutes, and the first fix failed because the loop variable leaked and recorded the cooldown against the wrong ability. **No per-ability multipliers**, so every "Improved Regrowth" shape was invisible. **No cast time changes.**

**With all four fixed the count moved 24 to 23, because the real cause was the scenario.** A healer doing 404 per second against a pattern delivering 440 is already covering it, so every extra point of throughput became overheal. **The instrument could not see its own subject.** Patterns raised so one healer covers a third to a half of the stream: druid overheal fell 65% to 5%, healers began using their full kit rather than one spell, and **23 zeros became 14**. Every remaining Druid zero is now genuinely non-healing.

**Restoration shaman moved +3.3% to +27.9% under the heavier patterns**, which is the correct direction since its capstone is throughput and the old pattern could not show it. Tuned to +5.3%.

**REG-124. The capstone-free findings survive four structural fixes and are the most stable results in the project.**
Rerun after the school preference, pet summons, crit fix and rotation selection. **Rogue's best free build +6.7% to +5.3%, still a three-tree split, still beating the capstone on five shapes, distinct results 80 to 81. Druid median -34.4% to -34.8%, distinct 15 to 18.** That the numbers barely moved is the useful part: **nothing on the damage side has been this stable.**

**REG-122. CLOSED. All fixes in and everything back in band.**
Recorded in `state-after-worth-fixes.md`.

**Four structural bugs, each larger than the talents they hid.** **A spec did not cast its own school**: a Fire mage cast only Frostbolt because raw throughput scored marginally higher, so **all eight Fire talents read exactly zero**. The school preference had to be applied after the mana blend or the blend diluted it, and had to use the tree's **dominant** school, since Fire references frost through Frostfire and made both its own. **One rotation per class** meant a Feral druid was measured casting Wrath; fixed, it reads 440 against 290. **Warlock and Hunter never summoned a pet** despite holding permanent ones, leaving seventeen talents inert. And **a crit-conditional multiplier applied on every cast**: Ruin doubles the critical strike bonus, worth about nine percent at eighteen percent crit, and paid fifty percent on every hit, so **a one point talent was worth half a tree**.

**A baseline that was not a build.** For Blackguard the comparison fell through to **Holy paladin measured by a damage simulator** and read +70.6% on burst. The picker now excludes healing and tank trees, and where no valid baseline exists it states that the shallow half differs rather than hiding it.

**Two rules about levers, learned by getting both wrong.** **A lever placed mid-tree lifts both builds and closes nothing**; it must sit on the capstone, the only talent that differs. And **a lever is sized against its scenario, not the tree**: Necromancy's movement bonus needed sixty percent to close six points, because movement is only thirty percent of that fight.

**Zero-worth talents 89 to 73**, with fifteen rewritten as scenario levers.

**Still open: the healing and tank trees have never been swept with their own instruments**, and **the capstone-free results predate all of these fixes** and need rerunning before Rogue's +6.7% or Druid's -34.4% is cited.

**REG-120. The worth sweep found 89 zero-value talents, and the largest cause was one rotation per class.**
Recommendations in `worth-findings.md`. **My first sweep reported 176 of 277 and was wrong twice**: it kept `grant` effects when stripping a talent, so an ability-granting talent measured as worth nothing, and it measured healing and tank trees with the damage simulator. Corrected to 89 of 206.

**The simulator used one rotation per class. Druid has a feral list that had never been used**, so a Feral build was measured casting Wrath and Starfire. Feral now casts Ferocious Bite, Shred and Rip and reads **440 against the 290 it read as a caster**. Ten Feral talents went from zero to contributing. Shaman, Priest and Paladin all had unused healing lists too.

**The remaining 89 classified: pet talents in builds with no pet are the largest group**, ten in Warlock Demonology and seven in Hunter Beast Mastery. Both classes have a permanent pet in vanilla and neither summons one. **One line per class makes seventeen talents measurable.**

**Ability-scoped talents in builds that do not cast that ability are correct and should not be fixed**, but `_value` takes them anyway because it scores effects rather than usefulness. **The selector should score an ability-scoped effect at zero when the build does not cast that ability.**

**Thirteen are genuinely inert** and should be rewritten as scenario levers, the shape proven twice: periodic cleave gained 18.8 points at zero sustained cost.

**REG-121. CORRECTION. The Druid finding in REG-119 was an artefact of the same broken rotation.**
Rerun after the fix: **7 distinct results became 15, and 99 within 7% became 19.** Druid is not indifferent, it is **strongly capstone-dependent**, with a median capstone-free build at **-34.4%**, the worst of any class. **Both the finding and its opposite came from measuring a Feral build with a caster rotation.** The Druid conclusion in `nocapstone-results.md` is wrong and is corrected in `worth-findings.md`.

**REG-119. Capstone-free builds swept, 114 shapes per class, and the answer differs enormously by class.**
Recorded in `nocapstone-results.md`. 51 points, no tree above 30, measured against each class's best capstone build.

| Class | Best free build | Within 7% | Beating | Distinct results |
|---|---|---|---|---|
| Rogue | **+6.7%** | **56/114** | **6** | 80/114 |
| Hunter | +8.9% | 24/114 | 1 | 26/114 |
| Druid | -0.7% | **99/114** | 0 | **7/114** |
| Mage | -2.0% | 13/114 | 0 | 32/114 |
| Warlock | -3.8% | 6/114 | 0 | 37/114 |
| Warrior | -0.0% | 6/114 | 0 | 22/114 |

**Rogue's best capstone-free build is a three-tree split, Assassination 25 / Subtlety 20 / Combat 6, and six builds beat the capstone.** The reason is the poison work: **poison talents exist in all three rogue trees**, so spreading collects Envenom, Toxicology, Vitality, Cutthroat and Deadened Nerves rather than choosing between them. **A mechanic that appears in every tree makes spreading a real strategy**, and it was invisible until those nine talents were modelled.

**Druid is the opposite and it is a problem. 99 of 114 within 7% but only 7 distinct results.** That is not flexibility, it is indifference: the point split barely determines what the build does. **This is the failure mode Section 5.6 was written against, arriving from the direction nobody was watching.** The concern was capstones dominating; the Druid problem is that nothing matters.

**Warrior: five splits tie at exactly 434 dps and they are not the same build.** 30/21 takes Death Sentence, 26/25 takes Sundering Blows, and **Death Sentence, Sundering Blows, Crippling Grip and Shieldbreaker are each worth exactly 0.0%.**

**Two items generated.** Four Warrior talents are worth zero and need rewriting; `talent_worth.py` has never been run as a sweep across every tree. And **Druid needs the same treatment**, since 7 distinct results from 114 shapes is a stronger signal than any single measurement.

**REG-118. CLOSED. Poison modelled at Option C, all nine talents fixed, and Assassination is measurable for the first time.**
Recorded in `poison-model.md`. One poison carrying the tag, applied on swings at a chance, stacking to a maximum, damage proportional to stacks. **Deliberately partial**; four poisons and off-hand rates remain Option A.

**Three simulator bugs found wiring the first talent.** **The generic `enable` handler swallowed every flag before the specific ones could see it**, so `poison_instant` never fired. **There was no general `add damage` handler at all**: only the pet tag had one, so every `add damage` effect scoped to any other tag fell through and did nothing, across `bleed`, `weapon`, `ranged` and the whole project. And **stack counts were truncated with `int()`**, so a partially ranked talent granting two stacks contributed zero.

**A selector gap, second instance.** Envenom read +0.0% and was not in the build, because `_value` did not score `poisonStacks`. **A talent the selector will not take cannot be measured.**

**Eight of nine talents now contribute**, measured individually with `talent_worth.py`, which removes a talent's effects and reruns: Envenom +11.0%, Toxicology +8.1%, Master Poisoner +6.4%, Deadened Nerves +3.7%, Blade Venom +3.1%, Vitality +2.6%.

**Assassination read exactly 0.0% on every scenario since the project began** and now reads +0.7% sustained. All three rogue trees in band.

**The burst problem was solved without touching the capstone.** Master Poisoner skips a ramp, so it is inherently worth most in a short fight and read +14.2%. Scaling its damage left burst at +10.1%, because the instant is a timing change rather than a number. **Raising the natural poison application rate from 30% to 60% halved what skipping the ramp is worth**, and burst fell to +7.0% with the capstone unchanged. **When a capstone's advantage comes from avoiding a cost, reduce the cost rather than the capstone.**

**REG-117. Master Poisoner is nine talents, not one, and Assassination has never been measured.**
A new audit check asks whether an effect is scoped to a tag any ability carries. **Nine talents across all three rogue trees modify `poison` and no ability carries that tag.** Envenom, Toxicology, Blade Venom, Master Poisoner, Vitality, Cutthroat and Deadened Nerves are all modifying nothing. **Same shape as the unread effects and unreachable abilities, in a place nothing had looked.**

**Assassination plus Subtlety reads exactly 0.0% on every scenario**, because its capstone modifies a tag that does not exist and the comparison is between two identical characters. **That is not a tree in band, it is a tree unmeasured**, and the +0.6% reported for rogue in earlier passes came from Combat.

Four options in `poison-options.md`. **Option B, poison as a flat damage stream, is the one to avoid**: it looks like progress, costs least, and specifically cannot measure the talent that prompted the work, since Master Poisoner's whole change is to a ramp a stream does not have.

**Recommendation: Option C, a stack ramp, now; Option A, full poison abilities, when the suite is stable.** C makes the pair measurable and catches four of nine. **The risk that made A unattractive was unbalancing a rogue that reads +0.6%, and that figure turns out to belong to a different pair**, so there is less to protect than it appeared.

**REG-116. CLOSED. Everything is in band. Ninety-four cells across four instruments, all inside -7% to +7%.**
Recorded in `final-state.md`. **Core zero violations of fifty cells. Expanded thirty of thirty. Tanking four of four. Healing four of four.**

**A tank band is defined: the mean of the threat gap and the effective health gap.** Threat and effective health are not interchangeable, so banding each separately would forbid a capstone that trades one for the other. The mean permits the trade, catches uniform inflation, and catches a capstone that raises one metric enormously while leaving the other alone. **Four tanks came from +28.4%, +12.0%, +9.4% and +23.2% to +6.5%, +6.0%, +6.5% and +6.6%.**

**An AoE bug found while fixing Necromancy. The rotation ranked area abilities as if they hit every target and the damage only multiplied when `maxTargets` was set**, so a rotation switching to Blizzard on cleave was switching to single-target damage on a slower cast. Core Fire read 285 on three targets and now reads 692. **Every cleave number before this fix was wrong**, in proportion to how much a build relied on area abilities.

**Four trees, four different problems, and only one was a magnitude.** Blackguard was scaling, at a uniform +7.9% down to +6.0%. Runeblade needed a burst lever and Cold Iron became an opening window. **Necromancy was a spread, and the answer was the `use_moving` enable alone: adding a movingDamage bonus on top overshot to +32.7% and removing it entirely landed at -0.8%.** Affliction turned out to be a fourth kind, losing to Ruin on cleave because the shallower build's extra Destruction point buys a crit bonus worth far more on Rain of Fire; Dark Pact now strikes a second enemy during its window.

**Rule worth carrying: scaling fixes a level, a lever fixes a spread, and a lever that is already sufficient does not need a magnitude on top of it.**

**REG-114. The expanded baseline was not always a real build, and it invalidated the tuning done against it.**
For Runeblade the comparison was `arms 31 + arms 20`, **fifty-one points in one tree**. `tune.gaps` now refuses a baseline duplicating the tree under test or its host. With the correct baseline **21 of 30 expanded cells were out of band** where the previous measurement showed four.

**Two tuner gaps found in the same pass.** Cost, cooldown and cast time discounts were untunable, so **Conduit's entire advantage was mana efficiency the tuner could not reach**. And burst levers were protected unconditionally, so a tree whose only authored magnitudes were burst levers could not be tuned at all; protection now applies when burst alone is the outlier.

**Expanded now 23 of 30 cells in band.** Bladedancer, Conduit and Survival fully in. Three outstanding, and they are three different kinds of problem: **Blackguard is a scaling problem** at a uniform +7.9%, **Runeblade needs a burst lever** at -9.1% with no cash-out, and **Necromancy is a spread problem** spanning 38 points between movement and cleave.

**The distinction is the useful one: scaling fixes a level, a lever fixes a spread.** Three attempts at scaling Necromancy produced three placements of the same 38 point range.

**REG-115. NEW. Tanking has no band and needs one, and it is a design decision rather than tuning.**
Warrior Protection +28.4% threat at no survivability cost, Paladin +12.0%, bear +9.4%, Metamorphosis +3.5% threat for **+42.9% effective health**. **None has ever been tuned, because the band was defined for damage.** Threat and effective health are not interchangeable so a single number cannot express a tank capstone's worth. Metamorphosis's trade looks coherent; the warrior's does not.

**REG-113. CLOSED. Band adopted at -7% to +7% in every scenario, and every core pair is inside it. Zero violations of fifty cells.**
Tighter than the -8 recommendation and **it cost nothing to tighten**: both bands failed the same four cells before tuning and both reach zero after. Recorded in `meta.band` with the rejected alternatives and why.

**Three capstones needed tuning and one needed diagnosis.** Arcane Power and Shadow and Flame came down through their cooldown entries, which lowers burst share without touching sustained value. **Dark Pact's cooldown was scaled to 1.011, effectively nothing, and the switching gap did not move at all.** The driver was its `consume` effect at twenty percent of shadow damage: on switching the periodics clear, the rotation becomes more Shadow Bolt, and a shadow multiplier is worth more. **Tuning the obvious lever three times without checking which lever it was would have gutted the capstone and left the outlier in place.**

**`tune_band.py` targets the worst cell rather than the sustained one.** Converging on patchwerk alone produces a capstone that is fine sustained and wrong in one scenario, which is how three of these got out of band while reading correctly on the number being watched. It scales a capstone that overshoots everywhere through the tree and one that overshoots in a single scenario through the cooldown table alone, and never touches `openingDamage`, `frontload` or `cleaveEvery`.

**REG-112. It reverses the position of the last four passes. "Cooldowns are correctly high on burst" is not supported by the data.**
`band_study.py` measures ten pairs against five scenarios with each capstone's shape recorded, then prices three policies.

| Policy | Violations |
|---|---|
| One band -5 to +5 everywhere | 8 of 50 cells |
| **One band -8 to +8 everywhere** | **4 of 50 cells** |
| Signature scenario exempt, -15 to +20 | 6 of 50 cells |
| Judged on sustained alone | 1 of 10 pairs |

**The exemption policy performs worse than simply widening the band**, failing six cells against four, because it licenses a cooldown on burst while still failing Affliction's +13.4% on switching.

**The cooldown shape does not reliably run high on burst.** Combat reads -1.9% and Fire +4.3%, both cooldowns; only Arcane and Affliction exceed. **The likelier explanation is that Arcane Power and Dark Pact are individually overtuned, not that their shape entitles them.** I argued the opposite for four passes and the data does not support it.

**Recommendation: a single band of -8 to +8 across every scenario**, four violations, both in tunable capstones. The alternative is judging on sustained alone, which passes nine of ten immediately but **gives up the ability to notice a capstone useless in a whole category of encounter, which is exactly what the Arms cleave gap was.**

**Standing observation from running alternatives twice: the levers that work are the ones that only pay in one scenario.** Opening windows scored 4.8 burst per point of sustained, periodic cleave scored infinite, pet amplifiers 2.4, and making a capstone hit more targets almost nothing. **A lever that pays everywhere is a buff. A lever that pays in one place is a fix.**

**REG-110. CLOSED. Every completeness check consolidated, and the audit now reports nothing outstanding.**
`fullaudit.py` runs eight checks at once: unread effect ops and stats, granted-but-unreachable abilities, abilities cast without the data they need, effects naming unknown abilities, placeholder text, unauthored talents, classes without rotations, and unread cooldown effect keys. **Every pass for five rounds had found the same shape in a different place; this finds all of them together.** It flagged two, both closed: Repentance's empty text and `immune_slowed`, which is mobility and is classified rather than modelled.

**Three fixes the run produced.** **The converger was flattening the burst levers it had just been given** since cash-out cooldowns are burst-weighted by design; `SCALE_COOLDOWNS` is now off, joining `openingDamage` and `frontload` in the protected set. **Survival had no burst lever at all** at -11.0%, so Combat Trapping became an opening window. And **the selector did not value opening windows so it never took the talent** ,  a burst lever the build will not pick is worthless. **Survival went -11.0% to +0.1% on burst, Conduit -12.0% to -4.0%.**

**Core: patchwerk 6/7, movement 7/8, cleave 5/6. Expanded: no tree below -6.5% anywhere, four inside the target band on sustained.**

**Three cells should stay where they are, and they now run in both directions.** Warrior Arms **-16.8% on cleave** because Mortal Strike strikes one target while the 30/21 build takes a universal cooldown. Warlock Affliction **+17.7% on burst** because Dark Pact is a cooldown. Necromancy **+17.5% on cleave** because Risen strike independently and a pet tree is a cleave tree. **All three are the capstone's own shape showing up in the scenario that suits it**, and flattening any would make that capstone worse everywhere else.

**Nothing in the data is unread. What remains is judgment about which scenario a capstone is judged in.** Master Poisoner is the only known modelling gap left, since poison application is not simulated.

**REG-109. CLOSED. Twenty-two talents were never rebuilt, and a resource-blind rotation made a capstone a liability.**
Chasing the Hunter outlier led to Mortal Strike, which turned out to be **unmodified vanilla text in a capstone slot**. Bloodthirst read "Your this effect lasts 8 sec", a broken string from an incomplete automated rewrite. A scan found **twenty-two talents still carrying vanilla wording with `N%` and `N sec` placeholders**, including Shatter, Arcane Power, Combustion, Vindication and Heart of the Wild. **Every one is a talent the project claims to have rebuilt.** All rewritten; a `no-placeholder-text` rule now fails the build on them.

**The Hunter answer was resource pacing, not the talent.** Trueshot makes Aimed Shot instant and measured as **16.4% worse** on switching, because **a rotation ranked purely on damage per second is correct only when the resource is free**: the freed globals went to cheap Arcane Shots that burned the mana Aimed Shot needed. Priority now blends throughput with efficiency in proportion to how constrained the resource is, and **a caster below thirty percent mana falls back to efficient spells** rather than spending freely then idling. **Hunter went -16.4% to +0.4% and is inside five percent on all five scenarios**, with Aimed Shot rising from twelve casts to thirty-seven.

**Warrior Fury cleave went -14.4% to +3.7% with no tuning**, because Bloodthirst's rewritten text gave it reach against a bleeding target and the effect now matches the words. **Arms stays at -13.3%: the 30/21 build takes Death Wish, and a universal damage cooldown beats a single-target strike on three targets.** A genuine design trade, same shape as a cooldown capstone exceeding the band on burst.

**Core: patchwerk 7/7 within five percent, movement 8/8, cleave 4/5.**

**Standing note: three of the last five passes found the same thing in a different place.** A field existed, nothing read it, and the number that resulted looked like a finding. Unread effects, unreachable abilities, unrewritten text. `grant-reachability`, `no-placeholder-text`, `no-broad-zeroing` and `percentage-drift` each exist because something got that far uncaught.

**REG-108. CLOSED. Ability-side audit. Eighteen granted abilities were never cast and a fixed priority list was measuring itself.**
Recorded in `ability-coverage.md`. **Eighteen abilities granted by talents and dealing real damage appeared in no rotation**, including Shield Slam, Ambush, Riposte, Blizzard, Flamestrike, Rain of Fire and Guardian Spirit. **Every talent granting one was measuring as worthless.** A `grant-reachability` rule now fails the build if it recurs.

**Sixteen area abilities had no target gate** and either never entered a rotation or displaced single-target casts; `minTargets` now gates them, and situational singles like Revenge carry a `condition` instead.

**Twelve abilities being cast had no scaling coefficient at all.** Bloodthirst is the one that mattered: its vanilla damage is entirely attack-power-based with a base of zero, so it dealt nothing. Giving it 0.45 took the Fury capstone from noise to +20.9%, then tuned to +4.6%.

**The fix that mattered most: rotation priority is not fixed.** A single ordered list regardless of target count meant **a single-target capstone displaced area abilities on cleave**, so the comparison measured the rotation's stubbornness rather than the talent. Priority is now computed per scenario by damage times targets hit; a warrior on three targets opens with Cleave 55 times rather than Heroic Strike 73, and the Arms cleave gap went **-16.6% to -5.5%**. **Any simulator with a hand-authored priority list is measuring the list as much as the build.**

**Core: patchwerk 8/8 within five percent, movement 8/8.**

**Two columns should not be flattened.** Burst runs high because its leading capstones are cooldowns; **cleave runs low for warriors because Mortal Strike and Bloodthirst both strike one target.** Same argument in reverse and equally correct. **Each scenario needs its own band, and a capstone should be judged against the scenario its shape suits.**

**Largest cell left: Hunter Marksmanship -16.4% on switching**, where Trueshot's cast-time removal is worth least. Uninvestigated.

**REG-106. CLOSED. A third of the authored data was inert. 334 unread effects became 18.**
`coverage.py` enumerates every op and stat combination against what any simulator reads. **334 of 1,026 authored effects were read by nothing**, across 42 combinations. The largest were not obscure: `refresh duration` 51 times, `no_expiry` 34, `immune_dispelled` 23, `immune_interrupted` 22, `add comboPoint` 16. **Every talent saying "cannot be dispelled" or "refreshes" or "grants a combo point" was doing nothing at all.**

Implemented: refresh and no_expiry keeping periodics alive, immunities removed from the attack table, combo generation, bleed and extra-attack procs as damage, control as small uptime credit, `convert` inheriting a school's modifiers, `channel` occupying its full duration, `rapCoefficient`, and cooldown `resourceRate` and `haste`. **The six combinations left are mobility, radius and reflection**, recorded in `meta.nonThroughputEffects` rather than given an invented number.

**REG-107. NEW. Two core capstones were not capstones, and only became visible once the effects worked.**
**Dark Pact** returns pet mana on a build that is not mana constrained, and **the simulator measured the 31-point build as worse than the 30-point one** because both cast identically while the shallower build got an extra Destruction point. **A capstone that measures as a loss is a design problem, not a tuning one.** Reworked into a cash-out consuming the demon entirely.

**Shadow and Flame** paid for alternating Shadow Bolt and Immolate, which are cast thirty-nine and three times. **The `alternate` op is correct for a pair cast at similar rates and wrong at thirteen to one.** Reworked asymmetric. Rule recorded: check the cast ratio before writing a talent that rewards alternation.

**Core: nine testable pairs where six were two passes ago. Patchwerk 8/9 within five percent, movement 7/8, cleave 6/9.**

**Burst is 2/8 and every capstone reading high there is a cooldown.** Adrenaline Rush, Arcane Power, Trueshot, Dark Pact. **Tuning it away would make each of them worse than a mid-tree talent in all four other scenarios. The burst column needs its own band**, and the working proposal is that a cooldown capstone may reach +15% there while a passive one may not.

**REG-105. Full run. Eight core pairs testable where six were, and burst is now the only unhealthy column.**
Recorded in `final-suite.md`. **Cooldowns only ever applied damage and critical strike chance**, so a cooldown whose effect was resource regeneration or haste did nothing; **Adrenaline Rush measured as worthless despite doubling energy for fifteen seconds**, and Rogue Combat had read 0.0% across every scenario since the project began. **Trueshot was scoped to cooldown rather than cast time**, so Hunter Marksmanship had too.

**Core: patchwerk 7/8 within five percent, movement 7/8, cleave 5/6. Burst 4/8 and it is structural.** Three capstones exceed +9% on burst and all three are cooldowns: Adrenaline Rush, Arcane Power, Trueshot. **A cooldown is a larger share of a 45 second fight than of a five minute one, which is correct rather than a fault**, and tuning it away would make those capstones worse than mid-tree talents everywhere else. **The burst column should be judged against a different band**, the same way a ramping tree is correctly negative there.

**Expanded: 30 cells, worst -3.5%, best +7.4%, 24 inside five percent, none below the floor.**

**Tanking: warrior +4.6%, in band where it was +14.2% two passes ago.** Metamorphosis's 30/21 build **loses 11,000 effective health and takes 43% more damage**, the clearest tank result in the suite.

**Healing unchanged. Restoration shaman holds +3.3% HPS and -24.2% HPM for the sixth consecutive run.**

**Two pairs still read 0.0% and one is correct.** Repentance is a stun with `simulable: false`. **Master Poisoner is the last real gap: the simulator does not model poison application at all.**

**REG-104. CLOSED. The "ceiling" was a methodology error, and checking it found three more bugs.**
REG-103 recorded four trees stuck at +5 to +6% and blamed a ceiling. **That was wrong.**

**The comparison was not isolating the tree.** Blackguard was measured as `blackguard 31 + retribution 20` against `retribution 31 + holy 20`, so the shallow half differed too and part of every gap belonged to the host. With the host held constant: **Blackguard +18.9%, not +5.0%. Bladedancer +15.0%, not +6.0%.** The tuning had been chasing a moving baseline.

**Slice and Dice granted nothing**, along with Sunder Armor, Hunter's Mark and Insect Swarm. A build maintaining a buff paid its global cooldown and received no benefit, which flattered every tree that skips maintenance. Given its real 30% attack speed, **Bladedancer fell +13.1% to +0.2% with no change to the tree.**

**Auto Shot consumed every global cooldown.** Listed as a rotation entry it was cast 171 times and a hunter cast nothing else, which is why **every hunter comparison read exactly 0.0% across every scenario for the entire project.** Now a continuous ranged attack on its own timer.

**Final: 30 cells across six trees and five scenarios. Worst -3.4%, best +7.3%, twenty-one inside five percent, none below the -5% floor.** Four trees fully in band; Necromancy and Survival at the top of the acceptable range.

**REG-103. CLOSED. Candidate testing found a better shape than the prior art suggested, and every expanded tree is now above the floor.**
`candidates.py` applies each candidate in isolation and measures **burst gained per point of sustained inflated**, because a candidate that lifts both equally has changed nothing about the tree's shape.

**An opening window scores 4.8 against a pet amplifier's 2.4, and the ratio is flat at 4.8 across three magnitudes and durations.** That flatness is the useful finding: the shape is what matters and the size is a free parameter.

**The pet amplifier was the obvious candidate and it loses.** A three minute cooldown fires once in a 45 second fight and twice in a five minute one, and twice is not rare enough to be burst-only. **An opening window fires exactly once per fight regardless of length**, so its share of a short fight is large and of a long fight small, automatically.

`Rotting Touch` is now the opening window, and it reads correctly: the dead answer fastest when first called. **Necromancy reads burst -2.6%, patchwerk +5.5%.**

**Worst single cell across all six expanded trees and all five scenarios: -2.6%. No tree is below the -5% floor anywhere.**

**A tuner correction the test forced:** the tuner scaled the opening window along with everything else, undoing the fix it had just been given. `openingDamage` and `frontload` are now in a `BURST_LEVERS` set it does not touch. **A tuner that treats every magnitude as interchangeable will flatten exactly the asymmetry you added on purpose.**

**Front-loading a periodic did nothing** across three magnitudes: Wither is eight casts of nineteen, so moving half its damage earlier moves too little to see. Sound mechanism, wrong vehicle.

**REG-102. The ramp problem is solved elsewhere, and the prior art gives four mechanisms. Necromancy -21.5% to -13.4%.**
Researched in `ramp-prior-art.md`. Affliction warlock has had this exact problem for years and the community named the rule: **a ramp is not bad, a ramp that buys nothing is.** Affliction started slow and purchased no advantage later.

**Four mechanisms, all with prior art.** **Move the stacks from the target to the player**, which is Unholy's Midnight rework replacing Festering Wounds with Lesser Ghouls; a stack on the target must be rebuilt per target and dies with it, a stack on the player is built once and carried in. **Enter the burst window already stacked.** **An instant multi-summon**, which is Apocalypse bringing four ghouls whole rather than building them. **A spender that converts a stack to damage now**, which is Putrefy, making the stack a currency rather than a timer. And the simplest: **reduce the setup**, which is how both Unholy and Demonology became top specs in Midnight.

**Applied to Necromancy.** Corpse Harvest stacks Risen on the caster and persists them between pulls. Sepulchral Study makes summoning instant and pre-combat. Boneyard raises the whole army at once. Unstable Dead already detonated them.

**It exposed a simulator gap: pre-pull summons were applied at t=0 and then cast again during the fight**, so the ramp was paid twice. Fixing that alone took burst -25.6% to -10.6%.

**Still -13.4% and outside the floor.** The remaining gap is that core Fire enters a short fight with Combustion while Necromancy enters with skeletons accruing at a fixed rate. **Prior art says the missing piece is a pet-damage amplifier aligned with the summon**, which is Dark Transformation; Unholy's whole single-target identity is aligning Apocalypse with it, and Necromancy has only the first half. That is a real talent rather than a magnitude, and it is the next design step.

**REG-101. Burst hole fixed on three of four, and four more simulator gaps found doing it.**
**Blackguard -7.8% to -1.3%, Conduit -8.3% to -2.0%, Metamorphosis -13.9% to -5.9%.** Recorded in `burst-fix.md`.

**Four gaps, each larger than the tuning.** The ramp had **no cash-out**, and all four trees described one in their own text that was never authored as damage. **A cash-out is a cooldown, not a passive**: authored flat it raised sustained as much as burst and pushed Conduit to +11.3%; in the cooldown table it fires once in 45 seconds as a third of the output and once in 300 as a twentieth. **Pets dealt no damage at all**, so Raise Skeleton summoned a skeleton that stood there. **Pet summons were excluded from every rotation** because the builder required direct damage. And **periodics were applied with seconds left**, which nobody does.

**Necromancy stays at -21.5% and cannot reach the floor without ceasing to be Necromancy.** In a 45 second fight it spends four of nineteen casts on Wither and Raise Skeleton while core Fire spends all eighteen on nukes. **A fifth of a short fight goes to setup that pays out after the fight has ended.** Three options, all design decisions: accept it as the tree's worst case, give it a front-loaded tool, or accept that a -5% floor is the wrong rule for a tree whose mechanic is accumulation.

**Metamorphosis should not be tuned on damage at all.** It is a tank; 749 TPS and 36,186 effective health are its real numbers.

**Four trees sit at the top of the acceptable band and resist further scaling**, because a meaningful share of their output comes from the twenty points in the host tree. **A tuner can only move what belongs to the tree it is tuning.**

**REG-100. CLOSED. Magnitude pass complete. Every measurable core pair is in band and five of six expanded trees are too.**
**Core: patchwerk median +1.6%, 7/7 within 5%. Movement 7/7, switching 6/6.** Section 5.6's tuning rule is met. Bloodthirst tuned +13.3% to +3.8% and Shadowform +15.0% to +4.7%, both scaled rather than redesigned.

**Three bugs found while tuning, each worth more than the tuning.** **Pyroblast sat above Fireball** while dealing 234 per second of cast time against 342, so Necromancy read +19.8% because **the baseline was casting its worst filler ten times a fight**; fillers now order by throughput and Necromancy fell to +0.9% untouched. **Twenty-nine melee abilities had no weapon scaling**, so Mortal Strike read as 160 damage against Heroic Strike's 157 and **taking the capstone measured as a loss**. **Heroic Strike and Cleave are on-next-swing**, replacing the autoattack at no global cooldown, and modelling them as casts made them free damage; Heroic Strike reached 88 casts a fight.

**Each made a capstone look worse than a rage dump. Tuning against them would have entrenched three errors as design.**

**Blackguard went -15.2% to +0.5% without a single talent changing what it does.** Bladedancer sits at +6.2% single and +10.0% cleave and resists scaling because much of its output comes from its host tree; it falls in the "above 5% but excels elsewhere" band.

**Four of six expanded trees are strongly negative on burst**, and that is a coherent pattern rather than six coincidences: all of them ramp. **A tree built on a stacking mechanic should be weak in short fights**, and before the behaviour repair those mechanics were flat percentages that paid instantly.

**The tuner needed extending twice**, to the base values of granted abilities and then to coefficients. **A tuner that cannot reach a tree's actual source of output will report that the tree is untunable**, which it said about Necromancy for four rounds.

**REG-99. Full suite after the behaviour repair, and the repair improved the design's own numbers.**
**`tank.py` and `heal.py` could not read the ops the repair introduced**, so eighteen effects in healing and tank trees were invisible to their own instruments. Both now read `debuff`, `consume`, `addTarget` and `immune_overheal`. **Fifth time a consumer failed to keep up with the data, and the first time it was caught before the numbers were reported.**

**Core: patchwerk median +1.9%, seven testable pairs where five were testable before.** The behaviour ops give the simulator something to read on talents that previously carried only a percentage. **Warlock Affliction plus Destruction now favours the mid-tree shape at -1.9%**, which it did not before, and that pair is SM/Ruin's neighbour.

**Warrior tank capstone premium fell +14.2% to +1.4%.** Shield Discipline's flat threat percentage became a stacking vulnerability the mid-tree build also benefits from. **Section 5.6 now holds on warrior tanking where it clearly failed**, achieved through the correctness repair rather than through tuning.

**Overheal separated sensibly for the first time**: shaman 37 to 49%, druid and paladin 0 to 5%. Chain Heal into a raid overheals and targeted heals do not, which was invisible while `immune_overheal` went unread.

**One thing needs fixing before more simming. Necromancy is now +19.8% sustained and +30.9% on burst**, because its flat shadow percentage became a vulnerability that ramps with the number of Risen, and a ramp beats a flat bonus on any fight long enough to build it. **The repair made the tree stronger rather than only differently expressed**, which is a tuning consequence of a correctness fix.

**Restoration shaman holds +3.3% HPS and -24.2% HPM across all three patterns.** Fifth run, surviving an authoring pass from 38% to 100% and a repair that rewrote a fifth of the project.

**REG-98. CLOSED. The behaviour repair is complete. Tag-wide positive damage percentages went 80 to 6.**
The automated pass reached 14% and then began producing false conversions, one of which `no-broad-zeroing` caught. The remaining seventy-two were rewritten by hand.

**The rule had been counting the wrong things.** Of the flagged effects, 16 were magnitudes below 1, which is **the cost of a subtraction node and legitimate**, and 13 were scoped to a single named ability. Only positive tag-wide multipliers are the flat modifier 5.2 deleted. Correcting the rule raised the real count from 65 to 81 and made it worth fixing.

**Median primary-school multiplier 1.10 to 1.00. Eleven of thirteen trees now carry no primary-school damage percentage at all**, including Retribution 1.21 to 1.00, Balance 1.18 to 1.00, Blackguard 1.56 to 1.00, Bladedancer 1.44 to 1.00 and Runeblade 1.47 to 1.00.

**The six that remain state a percentage in their own vanilla text**: Shadowform's fifteen, Ruin's hundred, Death Wish's twenty, Amplify Curse's fifty, Deep Bond's thirty, Metamorphosis's form multiplier. **Section 5.2 deleted percentages that existed instead of a mechanic, not percentages that are the mechanic.**

Replacements use ops the texts already named: `debuff` for stacking vulnerabilities, `consume` for spending Blight, Charges, Momentum, Echoes and Kindling, `addTarget` for emissions and Thresholds, `immune_overheal` across the healing trees, `convert` for Open Hand and The Runeblade. **Every one is a mechanic the tree already claimed to have and the data did not.**
The repair was smaller than the finding implied: **in almost every case the talent's text already described behaviour and only the effect was a percentage.** Improved Shadow Bolt reads "applies a vulnerability consumed by the next attacker and it stacks", which is a debuff mechanic, and was authored `multiply damage 1.10`.

**Three ops added because the vocabulary could not say what the text said:** `debuff` for a stacking vulnerability, `consume` for spending a stack for burst, `alternate` for a bonus on alternating two abilities. Shadow and Flame's "each empowers the other" had no op and was flattened to a percentage. **A vocabulary that cannot express a design will quietly convert it into one it can.**

**Primary-school multiplier band 1.00 to 1.58 becomes 1.00 to 1.50, median 1.10 becomes 1.00.** Arms, Combat, Retribution, Fire and Affliction now sit at 1.00 and get their damage from behaviour. Destruction at 1.50 is Ruin and Shadow at 1.30 is Shadowform, both of which state percentages in vanilla and should keep them.

**Cost, cooldown and cast time multipliers stay.** Changing how often you act is behaviour; scaling what an action does is not.

**`no-broad-zeroing` caught the converter producing the exact error it was written for**, an instant-cast cue emitting `multiply castTime 0.0` across the arcane tag. **`percentage-drift` tightened from 40% to 20%**, now flagging one core and seven expanded trees.

**Sixty-five talents remain.** Their text uses phrasing the cues do not match and they need reading individually. **Each widening of the converter produced more false conversions**, so the rest is hand authoring rather than another regex pass.

**REG-95. Thirty percent of talents express their effect as a percentage, which is what Section 5.2 deleted.**
Primary-school multipliers across core trees range **1.00 to 1.58**. Arms, Combat and Feral sit at 1.00 because their damage genuinely comes from behaviour; Destruction reads 1.58 and Shadow 1.40 because I authored their talents as percentage multipliers.

**The trees at 1.00 are the ones honouring the design.** Normalising everything to a common multiplier would entrench the drift rather than repair it. The correct fix is to re-express percentage talents as behaviour, which is a second authoring pass and design work rather than tuning.

**Why it happened: the effect DSL makes `multiply damage 1.10` the easiest thing to write and a behaviour the hardest.** Authoring 696 talents under that gradient drifted toward percentages under its own gravity. **A tool shapes what gets built with it.** A `percentage-drift` rule now flags any tree above 40%; six core and ten expanded trees trip it.

**REG-96. NEW. Talent damage multipliers never applied to autoattacks.**
The white swing applied the attack table and armour and skipped every talent modifier, so for a class whose damage is mostly autoattack most of a melee tree did nothing. Blackguard's 1.56 melee multiplier reached 23 Plague Strikes and no white swings. **Fixing it moved Blackguard from -15.0% to +8.3% with no change to the tree.** Every melee damage figure before this fix is void.

**REG-97. CLOSED. Blackguard is melee damage, not a tank, and I measured it wrong.**
Class absorption 7.1 says plate melee with a self-sustain engine, and paladin already has Protection. When it read -15% I added self-healing to the tank model and ran it through `tank.py`. **That was reaching for a kinder instrument to rescue a bad number**, which is the failure the instrument work exists to prevent. Role assignments for all ten new trees are now in `meta.roleAssignments`.

**Metamorphosis is a tank and had no tank profile**, so it was only ever damage-tested. Given one it reads 564 TPS against a Protection warrior's 599 and 34,015 effective health against 41,923. Competitive, not the -23% the damage run showed.

**REG-94. Full suite run, and the expanded trees turn out to be balanced on patchwerk and specialised everywhere else.**
`suite.py` runs every pair against every scenario across all three instruments, 120 seeds per cell at 95% confidence. Recorded in `suite-results.md`.

**The expanded table is the most informative result the project has produced.** Six of seven trees land within ten percent of their class's best core build on patchwerk and only three of seven on burst, because each has a distinct scenario identity: **Necromancy +29.4% on burst and level on patchwerk. Metamorphosis +20.9% on cleave and -23.4% on burst. Survival +9.4% sustained and -18.2% on burst. Bladedancer +21.8% on cleave.** A set that measures alike on a stationary single target and diverges under different fight shapes is what a designer wants and is not what homogenisation produces.

**Runeblade is flat at +8 to +10 in every scenario**, which is the profile of a tree with no scenario identity. Design question rather than a tuning one.

**Blackguard is the one genuine outlier: -14.4% to -21.0% everywhere.** Every other tree wins somewhere. A tree weak in one scenario is specialised; a tree weak in all of them is weak. Its damage sits in Blight and self-healing, so `tank.py` decides whether it is undertuned or mismeasured.

**Section 5.6 holds on damage and fails on tanks**, median +3.7% against 5.7% to 14.2%. **Burst is the worst scenario for it and the reason is Arcane Power**, +3.6% patchwerk to +13.0% burst, which is correct behaviour for a cooldown capstone rather than a fault.

**Restoration shaman has now held +1.3% HPS and -25.7% HPM across four runs and an authoring pass from 38% to 100%.** Most stable finding in the project.

**REG-93. The expanded trees measure well against core, and finding that out took three bug fixes.**
First simulation of the seven absorbed and three original trees. **Mean +1.2%, median +0.9%, range -15.0% to +9.5% against each class's best core build. Six of seven within ten percent**, which is better than the core capstone work produced and was not designed for.

**Three bugs, each invisible without running it.** The rotations contained **no absorbed-tree abilities** at all, so Plague Strike, Shadow Cleave, Whirling Blades and Shattering Blow were granted and never cast; four of seven trees read exactly 0.0% for that reason. **Every one of the ten new trees had its capstone at gate 31 rather than 30**, so `forceCapstone` never fired, and the gate-arithmetic rule allowed both as a tolerance so it never fired either. And **Tactical Mastery zeroed every cooldown in the build**, because it removes the stance-swap cooldown and was scoped to `all`; Shattering Blow fired 88 times against a 12 second cooldown and Runeblade read +26.7% against core rather than +9.2%.

The gate tolerance is removed. A new rule **`no-broad-zeroing`** rejects any effect multiplying a cooldown, cost or cast time to zero across a tag or across everything; nine talents were flagged, seven rescoped to a named ability and two rescaled.

**Conduit's -20.0% capstone gap is the clearest case yet for the support instrument that does not exist.** Confluence spreads Elemental Bond across three allies and a single-character damage simulator cannot see raid support at all. **Blackguard at -15.0%** is likely undervalued the same way, since its damage is spread across Blight and self-healing.

**REG-92. CLOSED. Authoring is complete across the entire project. 696 of 696.**
The expanded configuration went 0 to 100% in three passes: Blackguard, Necromancy and Metamorphosis first, then Bladedancer, Conduit, Runeblade and Survival, then the three original trees. **212 of 212 expanded talents authored, 484 of 484 core, 972 authored effects, 231 abilities.**

Twenty-one abilities were added along the way because talents granted things that did not exist: Plague Strike, Wither, Bone Armor, Raise Skeleton, Shadow Cleave, Immolation Aura, Fel Aegis, Metamorphosis, Tumble, Sweeping Kick, Whirling Blades, Elemental Bond, Shattering Blow, Hoarfrost, Harpoon, Coordinated Assault, Rewind, Threshold, Open the Way, Corona and Absolution. **The `effect-references` rule caught every one**, which is the whole reason it exists.

**Both configurations pass all 21 rules with zero errors and zero warnings. Both documents regenerate with zero stale text and zero missing talents. Zero em dashes across the suite.**

Every subtraction node carries its cost as a real effect: Fixed Point trades all damage for 25% healing, Sole Survivor trades the pet for 40% trap damage, Irreversible trades the demon for 25% shadow, Perpetual Motion triples energy cost for 25% damage. **The selector will price those correctly now that downside is weighted, which it would not have done two passes ago.**

**REG-90. CLOSED. The class document was 131 of 212 talents stale and is now generated.**
Checking rather than assuming found that **the entire Phase 2 flat-node rewrite never reached the class document**: Unholy Vigor still read "Increases melee damage by 1/2/3/4/5%" in prose while the data held the rewritten behaviour. Nine talents were also missing outright.

Seventeen row blocks wrapped across two formats, since the seven absorbed trees use `**Row N (X pts)**` and the three original trees use `**Row N, gate G, X points**`. `render_class.py` regenerates all of them, matching blocks to trees by talent names rather than headings. **Stale text 131 to 0, missing talents 9 to 0, argument prose lost 0 of 421 sentences.**

Both documents are now rendered from the data. The divergence is structurally closed on both sides.

**REG-91. CLOSED. The manifest describes the arrangement that actually exists.**
It described a document-first project; the data has been canonical since the schema work. Rewritten to lead with `talent-data.json` and `SCHEMA.md`, cover all 49 files including the superseded ones with a do-not-edit warning, and state where the work stands: **core complete at 484 of 484 authored, expanded structurally complete and 0 of 212 authored.**

Section 6 records the five lessons worth carrying: data is canonical and documents are rendered; a derived set must be recomputed by its consumer; a measurement of exactly zero means suspect the consumer; partial authoring biases rather than adds noise; and a value heuristic encodes an objective, so it must know its role.

**REG-89. The value function encodes an objective, and it has to know which role it is optimising.**
Rerunning the tank instrument at full coverage produced a build with **no crit immunity**, which no tank would accept. The section 9 downside fix made `Unbreakable` score minus 49 for removing critical strikes, correct for damage and wrong for a tank.

`build()` now takes a `role`. `Unbreakable` scores plus 40 for a tank and minus 49 for damage; `Toughness` plus 9 against plus 2; a talent reducing damage dealt no longer counts against a tank. Crit immunity is back and effective health rose 34,054 to 41,923 because the tank selector now buys mitigation it was skipping.

**Every previous tank and healing number in this project was produced by a damage-optimising selector.** Fourth instance of the same lesson: the consumer shapes the answer as much as the data does.

**Tanking at full coverage: premium 5.7% to 14.2%**, still above the damage median of 3.7%. Section 5.6 fails on tanks and the shape is consistent, Shield Slam being a threat capstone in a threat tree.

**Healing: Restoration shaman holds +1.3% HPS and -25.7% HPM**, the same shape it had at 38% authoring. **That is the only finding in the project that has not moved when the data underneath it changed**, which makes it the most trustworthy result produced so far.

**REG-88. CLOSED. Core authoring is complete at 484 of 484, and both configurations validate clean.**
Coverage 38% to 100% across three passes, 299 talents authored. **Zero errors and zero warnings on both `validate.py core` and `validate.py expanded` for the first time in the project.**

**Results at full coverage: mean +5.9%, median +3.7%, range +1.0% to +13.2%, four of six significant pairs within five percent.**

**No pair now favours the mid-tree shape, where two or three did at partial coverage.** That reversal is the finding: at 67% several capstones were unauthored while the mid-tree talents around them were not, which flattered the shallower build.

**Partial authoring does not produce a noisy version of the true answer, it produces a biased one**, and the direction depends on which talents happened to be written first. Every intermediate number in `sim-results.md` sections 3 through 9 was measured against incomplete data and is now labelled a record of method rather than evidence.

**Section 5.6 holds on four of six pairs.** The two outside are Bloodthirst at +13.2% and Shadowform at +12.0%, both throughput capstones landing on rotations built from their own school. **A capstone that adds a large direct ability or multiplies a school the spec already uses beats two mid-tree talents; one that grants utility does not.** If the band is to hold everywhere those two magnitudes need revisiting and nothing else does.

**REG-87. Authoring 38% to 67%, and the selector was taking subtraction nodes for free.**
141 talents authored across fourteen trees. At 67% coverage the Warlock Destruction build collapsed 399 to 43 damage per second: the greedy selector had taken **Backdraft**, which zeroes Shadow Bolt, on a rotation that is thirty-six Shadow Bolts. The heuristic counted whether a talent had effects, not whether they helped, and scored it plus 25.

Fixed twice: **downside is now weighted proportionally**, and **the penalty is scope aware**, since zeroing a whole school is catastrophic where zeroing one ability's cooldown is merely good. Backdraft now scores minus 42, Sure Strike minus 49, Ruin plus 17.

**Worth reading as a design signal, not only a bug.** A node that reads as a downside to a human read as a bargain to an optimiser, which is the exact failure Section 5.4 warns about when a subtraction is undertuned.

**Results: 7 of 13 testable across 5 of 9 classes, mean +3.7%, median +2.5%, range -3.1% to +12.0%, five of seven within five percent.** Both former outliers, -12.4% and +25.5%, are gone. What remains is Shadowform at +12.0% and Bloodthirst at +11.6%, both throughput capstones on rotations that match their school.

**REG-85. CLOSED. The healing instrument is built, and all 27 core trees are now measurable.**
`heal.py` measures effective healing per second, healing per mana, overheal share and time to out of mana against three incoming damage patterns. **Healing is bounded by damage arriving, not by what a healer can produce**, so a boss health bar is the wrong reference and a heal on a full target is worth nothing.

**Two modelling decisions mattered more than the talents.** Casting the largest heal every global cooldown emptied every mana pool in 34 to 44 seconds, which is arithmetically right and unlike how anyone plays; the model now downranks to match the hole and skips targets missing under 400. And Omen of Clarity was authored as `multiply cost 0.0` across all spells, so a druid healed for free and reported 129,422 healing per mana. **A proc-based cost reduction must be authored at expected value.**

**Third instrument, third time it found nothing to read.** Healing trees were authored at 2 to 4 talents of 17 to 20. Twenty-three now authored, plus Circle of Healing and Swiftmend added as abilities. **Authoring follows the instrument, because until something consumes a field nobody notices it is empty.**

**REG-86. NEW. Healing exposes a ranking problem damage did not.**
Restoration shaman's 31-point build heals **+8.3% per second and -22.9% per mana**. Better and worse at once. On the damage side more of one meant more of the other; here **a single number cannot rank healing builds**, and any balance pass must state a fight length before it can state a winner. That is the correct shape for a capstone choice and it is the only interesting healing result so far.

**REG-83. It found a real design failure nobody could have seen. The tank trees fail Section 5.6.**
`tank.py` implements threat and survivability: vanilla threat coefficients, Defensive Stance at 1.3 and Righteous Fury at 1.6, a Naxxramas boss profile, three tank profiles, and metrics that are not damage. Six new defensive stats added to the closed vocabulary.

**The tank trees carried authored effects on three of nineteen talents for Protection warrior and two of eighteen for Protection paladin.** The instrument worked immediately and had nothing to read. Twenty-six tank talents now authored.

**Capstone premium for tanks is 9 to 20 percent, against a median of minus 0.2 percent on the damage side.** Shield Slam is a threat capstone on a tree whose whole purpose is threat, so a 31-point Protection build is simply better at its job. **Section 5.6's rule is met on the damage trees and clearly failed on the tank trees, and nobody would have known because the tank trees were never measured.**

**Four sanity checks pass against things a Classic player would state flatly:** bear has the largest effective health, warrior generates the most threat, bear cannot block, and Protection warrior reaches crit immunity through Unbreakable. All four reproduced from talent data rather than asserted.

**REG-84. NEW. The remaining gap is healing.**
No throughput number exists for Holy priest, Restoration druid, Restoration shaman or Holy paladin, and their trees are as large as anyone's. Healing needs healing per second, mana efficiency and overheal measured against an incoming damage pattern rather than a boss health bar. Also missing: threat as a competition against raid damage rather than in isolation, and cooldown survivability, since Last Stand and Ardent Defender are authored as flat values which understates a cooldown whose worth is surviving one spike.

**REG-81. Three instruments, because the seven unmeasurable capstones fail for three different reasons.**
Built: a **scenario suite** of five fight profiles (patchwerk, burst, movement, cleave, switching), a **cooldown table** for activated abilities that modify subsequent casts, and an explicit **`simulable: false`** classification for talents whose value is control or survivability.

**Arcane Power reads +3.6% on patchwerk and +13.0% on burst.** Same talent, same build, measured correctly instead of conveniently. That is the argument for the suite in one line. Combustion moves +1.2% to +4.5%. Capstones measurable in at least one scenario went six to seven.

**A talent's value is its profile across scenarios, not one number.**

Three fixes were needed to get there: two cooldown abilities did not exist so nothing granted them, the `grants` field was derived by name-matching before those abilities were added and was stale, and two passives had been wrongly placed in the cooldown table.

**REG-82. NEW. The missing instrument is threat and survivability, and it should be named rather than implied.**
Nothing built measures threat, damage taken, or crowd control, and **a third of the rebuilt trees live there**: Protection warrior, Protection paladin, and every tanking talent in Feral are invisible to all five scenarios. Repentance reading zero is correct and gets `simulable: false` rather than a fourth scenario invented to make a stun look like damage. A threat model needs an attacking boss, player-side avoidance, and a threat table; it is a larger build than the scenario suite.

**REG-79. It is the strongest validation the project has. The simulator independently rediscovered DS/Ruin.**
The Warlock minus 12.4% flagged for checking is not an error. The 30/21 build takes **Demonic Sacrifice at Demonology's twenty point mark and Ruin at Destruction's**, beating a 31-point Destruction build that reaches Shadow and Flame. That is DS/Ruin, the canonical vanilla build `spec-grievances.md` cites as proof a no-capstone shape can be correct, and the model arrived at it without being told it exists. On a rotation of thirty-six Shadow Bolts and five Immolates, a fifteen percent shadow bonus beats a fire capstone. **That is the answer vanilla players reached in 2005.**

Priest at plus 12% is also fine: Shadowform's fifteen percent on an all-shadow rotation. A real throughput capstone doing what one should.

**REG-80. NEW. A selector bug was hiding every unvalued capstone.**
The greedy selector broke out when the best remaining talent scored zero, so a "31 point" Destruction build spent 30 and never took Shadow and Flame. The comparison claiming to test a capstone build was testing two mid-tree builds. Fixed twice over: the selector now spends its last points on an unvalued talent, and **the 31-point side reserves a point for its capstone**, because the test specifies intent and letting an optimiser decline the capstone tests something else. Every 31-point build now differs from its 30-point counterpart by exactly the capstone. Six rounds to achieve what the test always claimed to do.

**Final: mean premium +0.8%, median -0.2%, 6 of 13 pairs testable across 5 of 9 classes, mid-tree winning 3 of 6.** Seven pairs are unmeasurable because their capstones are utility rather than throughput, which is not a data gap.

**REG-78. Round five, and the capstone premium is now near zero. Section 5.6's target is met on current evidence.**
**Mean minus 0.8%, median minus 1.6%, three of five significant pairs favouring the mid-tree shape.** Consolidated in `sim-results.md`.

Three fixes this round, all correctness rather than tuning. Effects now **scale with ranks actually purchased**, since Shadow Weaving at 2 of 5 ranks was delivering its full 15%. Same-tag damage bonuses now **add rather than compound**, as vanilla stacks them. And the **build selector is greedy by value under gate constraints** rather than filling low rows to completion, which was the largest error: a 30-point build never reached a gate-15 talent a 31-point build got, so the comparison was measuring fill order rather than the capstone. With the fix a 31-point build differs from a 30-point build by exactly the capstone.

**The movement matters more than the landing.** The headline went +9%, then +3 to +8%, then +2.9%, then +5.6%, now -0.8%, across five rounds of legitimate fixes. **No specific number should be quoted.** What can be claimed is directional: the design is not obviously broken and mid-tree shapes are competitive.

Seven pairs show no significant difference and for most that is correct rather than missing: Repentance is a stun, Trueshot changes a cast time, Elemental Mastery is a cooldown. Those capstones do not add single-target throughput.

**Two to check before citing.** Priest at +12% is a real throughput capstone on an all-shadow rotation, magnitude untuned. Warlock Destruction plus Demonology at -12.4% reaches no capstone the simulator recognises, which may be a missing `grant`.

**REG-76. Eleven of thirteen pairs testable, and the design holds on eight of them.**
52 more talents authored plus one simulator fix. **Mean capstone premium +5.6%, median +3.2%, range -4.0% to +32.6%. Four of eleven pairs favour the mid-tree shape and eight of eleven sit within five percent.** Section 5.6's tuning rule wanted exactly that band, and this is the first evidence supporting the design rather than questioning it.

**Two outliers are magnitude errors, not findings.** Priest at +32.6% stacks Shadowform, Shadow Weaving and Darkness multiplicatively on an all-shadow rotation. Mage at +17.3% has the same shape. **Several talents multiplying the same tag compound, and nobody checked the product.** That is what the dividend coefficient work will have to police and it is now visible rather than theoretical.

**REG-77. NEW. Tag-scoped effects were collected and never applied.**
The modifier lookup checked ability id then fell back to `all`, never checking the ability's own tags, and most authored effects are tag-scoped. Five pairs read exactly 0.0% while every differing talent was authored. Fixing the lookup took testable pairs from six to eleven.

**Third time in this project that the data was correct and the reader was not.** Standing rule: **when a measurement returns exactly zero, suspect the consumer before the data.**

**REG-74. It is the first result that supports the design. The capstone premium is not a constant.**
Five fixes in: duration tracking, cast time, per-resource pools, combo points, and Seal of Command as a white-swing proc. **Five of thirteen pairs now testable across three classes, and no rotation casts zero.**

**Mage Fire plus Frost returns minus 4.2%: the mid-tree shape beats the capstone shape.** First evidence in the project that Section 5.6's tuning rule can hold. Across the five measurable pairs the premium runs minus 4.2% to plus 8.4%, mean plus 3.5%, one of five favouring mid-tree. **A premium that varies by pair is what a working design looks like; a constant premium would have meant the capstone is simply overtuned everywhere.**

**REG-75. NEW. Four classes were casting literally nothing and it was invisible in the aggregate.**
Druid, Paladin, Shaman and Hunter all returned roughly 151 dps, which read as a tie and was pure autoattack. The model had one resource pool and a binary physical-or-caster split, so hybrids held rage they could not spend on mana abilities. Rogue's energy never regenerated and its finishers fired without combo points, so Eviscerate spammed 55 times while Sinister Strike never appeared.

**Numbers that agree across classes for different reasons look like a result.** Checking cast counts, not damage, is what exposed it.

**REG-71. It invalidates REG-62. The 69-talent scope was measured against a build selector the simulator does not use.**
The scope was computed with a greedy top-down fill. The simulator uses a deepest-affordable-gate selector, adopted later when the first run showed an "Arms 31" build containing no Mortal Strike. Different selectors, different builds, different differing talents.

**Scope under the selector actually in use is 197, not 69. Overlap by name is 33. Thirty-six authored talents are no longer in scope and 157 still need effects.** Just over half the authoring went to talents the simulator never compares.

**It surfaced only because all nine classes were run.** Seven of thirteen pairs returned exactly 0.0%, and the differing talents included Shadow Mastery, Ruin, Dark Pact, Adrenaline Rush and Cold Blood with no authored effects between them. Warrior worked because Arms was hand-authored as the reference and was covered under either selector, so a single-class test could not have caught it.

**Standing fix: a derived set should be recomputed by whatever consumes it, not stored.** `sim-authoring-scope.json` is now regenerated from the simulator's own selector so the two cannot drift again.

**REG-72. NEW. No duration tracking, so every maintenance spell spams.**
Scorch is cast 189 times in 300 seconds and every Mage build collapses to Scorch spam, which is why two different Mage pairs returned identical numbers. Rend at 66 casts on Warrior is the same bug. **Any rotation containing a maintenance effect is meaningless until the simulator tracks durations**, and that is now the highest-value fix to the simulator itself.

**REG-73. One class is an anecdote.** REG-70's 3 to 8 percent capstone premium holds for Warrior only and should not be generalised until at least three classes are testable.

**REG-70. With the real vanilla combat model the gap halves, and the combat model mattered more than the talents.**
Implemented from the era's documented testing: single-roll attack table, 40% glancing on white only at 65% damage against a level 63 boss, 9% hit cap, armour mitigation against 3,731, vanilla rage generation, **150% spell crits rather than 200%**, and Overpower gated on an actual dodge.

**Arms capstone shape now leads by 3.1% (z=6.6), Fury by 8.5% (z=12.9), across 200 seeds.** Down from 9% under the crude model. Overpower alone accounted for much of it: it fired 96 to 116 times per fight as an off-cooldown filler and now fires 24.

**Three targets changes little, 2.1% and 4.3%, which kills the multi-target explanation** and removes one of the three readings from REG-68. The remaining question is narrower: is a 3% capstone premium correct and 8.5% too large, or should both be near zero? That is a magnitudes decision, not a structural one.

**General lesson worth keeping: a model that flatters one term exaggerates whichever build leans on it, and the direction of that error is not predictable in advance.**

**REG-68. It is bad news for Section 5.6. Capstone shapes beat mid-tree shapes by roughly 9%.**
307 against 282 for Arms, 230 against 210 for Fury. The tuning rule says two mid-tree seats should land in the same band as a capstone plus a shallow dip. On this evidence they do not.

Three readings and this run cannot separate them: the mid-tree talents are undertuned, or the test is unfair because their advantages are multi-target and this is single-target, or 9% is the correct capstone premium. **The third would be a good outcome and the first two are fixable.** Next step is a cleave scenario, which decides between them. Recorded in `sim-first-results.md`.

**REG-69. NEW. The 30/21 and 26/25 shapes are the same build.**
Both reach gate 25 in the deep tree and gate 20 in the second, so they take identical talents and returned identical means. Not a bug: it confirms the point math and means the two shapes are one build described two ways. The build table in `build-diversity.md` overstates the distinct shapes by listing both.

**REG-65. CLOSED. The dividend is not a simulation blocker, and never was.**
The curve is linear per REG-03, so a 31/20 build and a 30/21 build both spend 51 points and receive an identical dividend total. **It cancels out of the comparison entirely.** That removes `dividend.stats` from the critical path for the build-diversity question, where it had been carried as a blocker since the sim protocol was written. It is still needed for cross-class balance, which is a different question.

**REG-66. CLOSED. Effects, baselines and rotations are complete for the scope.**
All 90 authored effects that require a magnitude have one, with 2 flagged `magnitudeSource: op default, needs tuning` rather than left null. `magnitudeRequired` now records that grant, enable, convert, refresh and addTarget are binary or definitional, so a null on those is correct rather than missing; the count had been overstating the gap by 24.

Ability baselines went 76 to 88 of 205, bounded the same way the talents were: **only the 34 abilities that authored effects actually touch needed them, and 12 were missing.**

**Rotations defined for all nine classes** as priority lists the sim walks top down, with separate healing and feral lists where a class has two or three rotations. A rotation belongs to the class rather than the build, which is what keeps the 31/20 against 30/21 comparison fair. A `rotation-references` check confirms every ability named exists; it caught `hunter-hunters-mark` against the actual `hunter-hunter-s-mark` and three abilities that existed in the rotations and not in the table.

**REG-64. CLOSED. The 69-talent authoring scope is complete.**
All 69 talents that differ between a 31/20 and a 30/21 build across the 26 core pairs now carry authored effects. **87 talents authored in total, 166 effects, and both configurations pass 20 rules with zero errors and zero warnings.**

Two new rules earned their place immediately. `effect-references` caught an authored effect pointing at `paladin-hammer-of-wrath`, an ability that did not exist because the talent grants it and nothing had added it to the table. `effect-vocabulary` caught `immune_disarmed` against the closed set's `immune_disarm`, a mismatch between my hand authoring and the extractor's output that would otherwise have silently split one flag into two.

**`sim-readiness` was also rescoped.** It measured every talent, which permanently reported 26 warnings for work REG-62 established was unnecessary. It now measures the authoring scope, which is the set the question actually depends on, and reports clean.

**REG-62. The authoring scope is 69 talents, not 484.**
To decide whether 30/21 beats 31/20 for a pair, a simulator only needs the talents that **differ** between the two builds, not every talent in both trees. Across all 26 core pairs that set is **69 talents**. The rest can stay drafted or empty without blocking the question. Listed in `sim-authoring-scope.json`.

**REG-63. NEW. The effect vocabulary is closed, and closing it was the real fix.**
Hand-authoring Warrior Arms produced flag names invented on the spot: `rageNoDecay`, `procOnAnyMiss`, `executeThreshold35`. No extractor could guess them and no simulator could implement them. **The extractor's 27% recall was measuring vocabulary disagreement, not extraction failure.**

`meta.effectVocabulary` now closes all five sets: 9 ops, 28 stats, 31 flags, 10 procs, 17 condition forms. An `effect-vocabulary` rule rejects anything outside them, exactly as the reads categories work. Arms was re-authored against it and both configurations validate clean.

**Recall only moved to 31% after closing the vocabulary**, which settles the question: the extractor is a drafting aid, not an author. Authoring requires judgment about what a sentence means mechanically, and regex does not have it. 363 talents now carry drafts marked `source: proposed`; the `sim-readiness` rule counts only `authored`.

**REG-60. CLOSED. Season of Mastery is the ruleset basis, with one refinement to world buffs.**
`classic-plus` now inherits SoM: world buffs suppressed in raid instances, no buff or debuff limit, boss health tuned to compensate. **The refinement is that world buffs are suppressed on entering a raid or instanced battleground and restored on leaving, rather than lost.** That differs from SoM, which suppresses without restoring, and from Classic Era's Chronoboon, which banks them manually. The intent is that world buffs reward world activity and never become a raid or arena prerequisite, which was the specific failure that made them unpopular rather than the buffs themselves.

**REG-61. NEW, and the honest number is low. Effect authoring is the largest remaining item.**
An extractor proposes structured effects from talent text. It covered 45% of non-vanilla talents on the first pass, and **hand-authoring Warrior Arms as a reference tree showed roughly a third of those proposals were wrong**: phrases matched from a later sentence and attributed to the wrong scope, conditions parsed into nonsense like `state.a`, and whole effects missed. Bloodletting parsed perfectly; Poise and Deep Wounds did not.

So proposals are marked `source: proposed` and the `sim-readiness` rule counts only `source: authored`. Current state: **20 of 484 core talents authored, 223 proposed but unreviewed, 241 with nothing.** 355 effects exist, 164 of which lack a magnitude.

Warrior Arms is the reference: 20 talents, 53 effects, every one authored. Reviewing a proposal is faster than writing from scratch, so the extractor still earns its place, but its output is a draft and must not be counted as data.

**REG-58. Rulesets are now an explicit axis, and Season of Mastery is the right control.**
Six encoded in `meta.rulesets` with their environmental parameters: vanilla, classic-era, som, anniversary, sod, classic-plus. **Three are usable as controls and SoM is the best of them**, because world buffs are disabled in raid instances and the debuff limit is removed, which eliminates two of the three confounds `sim-baseline-protocol.md` names. Boss health was raised to compensate, so absolute numbers differ from Classic Era while relative comparisons hold.

**SoD is explicitly not a control.** Runes grant abilities outside the talent system, so a SoD parse measures runes plus talents plus gear and cannot be decomposed. It is a precedent for how far a rework can go and still be Classic, which is a scope argument rather than a balance baseline.

**Where Classic Era and SoM disagree, the disagreement is itself the measurement** of how much world buffs distort the class ranking, which is worth knowing before any band neutrality target is set.

**REG-59. NEW. Sim readiness is now measurable and the number is low.**
A `sim-readiness` rule reports it: **7 of 484 core talents carry structured effects, 75 of 204 abilities carry baseline values, zero trees have a dividend curve, zero builds have a rotation priority.** All 75 ability baselines are rank-60 vanilla values transcribed from era knowledge and every one carries `confidence: verify against a database before simming`. Utility abilities with no damage or healing component are deliberately null rather than guessed.

That 1% on effects is the real distance to a sim, and it is authoring rather than design.

**REG-57. Four data additions stand between the current state and a simulated answer on build diversity.**
Measured: **only 21% of core talents state a magnitude at all.** The rest express duration refreshes, resource changes, procs, bypasses, thresholds, enables, added targets, and tag conversions, all in prose. Removing the percentages was correct; replacing them with prose was the part that blocks simulation.

Added to the schema: an **effect DSL** with nine ops (`add`, `multiply`, `ignore`, `enable`, `grant`, `convert`, `proc`, `refresh`, `addTarget`), each with scope, condition, and magnitude, plus **ability baseline fields** for cast time, cooldown, cost, base value, and coefficient. Seven talents and fifteen abilities authored as worked samples.

**The `convert` op is the one that matters most**, because it turns tag conversion into a set operation: add `fire` to Frostbolt's tags and every talent whose `reads` includes `fire` applies automatically.

**Scope is bounded by the question being relative rather than absolute.** Whether 30/21 matches 31/20 for one class in one gear set needs no encounter model, no cross-class pass, and no gear optimisation. Order: ability baselines first since they are transcription, then the DSL on the talents in the 26 named pairs, then rotation priorities, then a proposed dividend curve to be validated rather than derived. Recorded in `sim-data-gap.md`.

**Known limit.** Some talents are not simulable at any detail. Threat decay needs a threat model most vanilla sims lack; totems following the shaman is real value that appears in no damage number. Those get marked `simulable: false` and argued rather than measured. Quietly dropping them to make the model look complete is the failure mode to avoid.

**REG-56. CLOSED. Phase 2 complete. The expansion now meets core's standard.**

**All 67 flat nodes across the seven absorbed trees are gone**, 233 points of percentages rewritten into behaviour that engages each tree's own mechanic. That single pass closed five warning categories at once, which is why it went first.

Added: seven subtraction nodes, one per absorbed tree, placed at gate 20 so they fix the seat weight at the same time. Seven reciprocal nodes in core trees, closing REG-48 and the Metamorphosis gap found afterwards. **No absorbed or original tree is now unreached.**

**`validate.py expanded` passes all sixteen rules with zero errors and zero warnings**, matching core. Cross-tree graph: core 53 edges and 26 mutual pairs, expanded 73 edges and 32 mutual pairs.

**Three measurement bugs surfaced and were fixed in the validator rather than worked around in the data.** Mechanic coverage matched only the first word of the mechanic name, so Conduit read 35% because its text says "empowered" while its mechanic was called "Empowerment", and Runeblade read 32% because its mechanic name was a full sentence. Mechanic names are now the mechanic word and matching uses stems of every word in the name. The vanilla-voice rule was also too narrow: it flagged 150 perfectly good openings like "Traps deal damage" and "Consecrates the land", because vanilla opens with verbs, plural nouns, and ability names, not a fixed list. Widened to require a capital letter, which is what vanilla actually does.

It still earned its place: narrowing it exposed seven genuine artifacts, including two talents whose text began with a bare period.

**REG-55. CLOSED. Phase 1 complete. All 27 core tree listings are generated from the data.**

**Done.** The eleven full rebuild sections had 52 paragraphs interleaved *between* their gate blocks, which is why a naive splice was impossible. Those were relocated: deletion notes merged into a single "What was deleted" paragraph per section, design commentary moved below the tree. Sentence count held at 1,341 across the move, and 36 of 37 deletion-note phrases verified present afterwards, the 37th being a duplicate already stated twice elsewhere.

Gate sequences are now wrapped in `<!-- GENERATED -->` markers and `render_doc.py` regenerates all eleven from `talent-data.json`. **All 195 talents in those sections match the data exactly, with zero stale text and zero em dashes.**

**The batch sections needed a second format.** Sections 17 to 19 hold their trees as inline bullets, one per gate, so the renderer emits two shapes: full gate blocks for the eleven detailed rebuilds and compact bullets for the sixteen batch ones. Four trees, Mage Fire and the Subtlety, Destruction, and Protection warrior trio, had no listing at all and now have one.

**The renderer identifies blocks by the talent names inside them rather than by heading**, so the document can be restructured without breaking regeneration. That was needed because four blocks had no heading to key on, and it removed a whole class of fragility.

**Verified.** All 477 core talents present, zero stale text, zero em dashes, 27 generated blocks, and the regenerator is byte-idempotent from a settled state. **Argument prose lost across the whole phase: zero.** A diff initially reported 14 losses; each was checked and each was present, the diff having caught sentence-boundary shifts from the deletion-note merge rather than real removals.

**Standing property.** Editing a talent in `talent-data.json` and running `render_doc.py` now updates the document. The divergence that recurred four times is structurally closed for core.

**REG-54. CLOSED. Verification pass on things the rules did not check.**
Re-running the existing rules would only have confirmed what they already said, so the pass tested duplicate names and ids, cross-class references, capstone counts, text truncation, and whether rank counts match the number of effects described. **Six real problems found, all now fixed.**

- **273 duplicate talent ids.** Vanilla and rebuilt trees generated identical slugs, so `druid-balance-nature-s-grasp` existed twice. Namespaced by tree id; 1,114 talents now have 1,114 unique ids.
- **Warrior Arms had four talents duplicated into gate 5.** The extractor read "Row 5 (20 points)" as gate 5, and I later added the gate-20 row by hand, leaving both.
- **Warlock Demonology's rebuilt capstone was missing entirely.** Gate 30 existed and was empty. Soul Link restored.
- **Two talents had text truncated at the 280-character extraction cap**, ending mid-sentence.
- **Sixty-eight multi-rank talents described a single effect**, which contradicts Section 5.2's whole method: a five-rank talent should state five discrete effects. Most were "kept from vanilla" talents backfilled with vanilla's scaling text, so they still read "Increases the chance of your Nature's Grasp to entangle an enemy by X%." All 68 rewritten.
- **Eighteen style regressions** in text I hand-wrote *after* the restyle pass ran, so it never touched them.

Two new rules added, `ranks-match-effects` and `one-capstone`. **Core now passes sixteen rules with zero errors and zero warnings.** The 85 remaining rank/effect mismatches are entirely in the absorbed and original trees, which is expansion debt already tracked under REG-25.

**REG-53. CLOSED. Style pass to vanilla tooltip voice.**
Measured against vanilla's own *behaviour* talents rather than all of vanilla, since the flat talents we deleted skewed the first comparison. Before: 41% semicolons, 21% "then" chaining, 36% carrying an artifact prefix from my own earlier cleanup, 11% opening in vanilla voice. After: **zero semicolons, zero "then" chains, zero artifacts, 69% opening in vanilla voice against vanilla's 70%.**

Fixed along the way: 79 talents carrying design metadata like "Sideways node." in their tooltip text, which belongs in `flags`; 82 instances of a "Your a critical" bug I introduced in the first restyle pass; 26 sentences of document commentary that had leaked into tooltips; 21 single-word fragments from collapsed comma lists; markdown bold surviving extraction; and ability names lowercased, restored using the abilities table. A `vanilla-voice` rule now guards it.

**Rendering caught what metrics missed.** The percentages read clean while the actual output said "Your rend ignores armor. Deflection is gone. Its parry now arrives th." Reading the rendered trees is the check that works.

**REG-51. CLOSED. Every core talent now states an effect.**
Of the 72 flagged, 52 were flagged only for starting lowercase and had real content; 20 were genuinely unwritten and are now authored, plus 6 more found on a second pass. Shortest core description is now 96 characters against a median of 129. `validate.py core` passes all thirteen rules with zero errors and zero warnings, and `render.py` produces readable trees from the data.

**The core configuration is finished as authoring work.** The only remaining empty fields are `dividend.stats` and ability `coefficient`, both blocked on simulation rather than on writing.
Rendering the data exposed that the batch-written trees in document sections 17 to 19 summarised rather than specified: text like "reworked to threat behaviour" instead of what the talent does. 204 were recoverable by stripping connectives; **72 are genuinely unwritten** and now carry a `text-incomplete` flag with a `text-complete` rule watching them. Worst are Assassination at 10 and Combat at 9. **The dataset cannot drive a simulator or a renderer until these are authored.**

**REG-52. CLOSED. `modifies` and `grants` filled.**
403 talents across the suite reference a named ability, 245 of them in core; 93 talents share a name with an ability and are treated as granting it. Derived by matching the authoritative ability list rather than by keyword guessing.

**REG-49. Core is structurally complete and validates clean.**
Twelve rules, **zero errors and zero warnings** on `validate.py core`. 54 cross-tree edges, **26 mutual pairs, zero one-way**, after twelve reciprocal nodes closed every unanswered edge. Eight of nine classes have all three possible pairs. **188 abilities authored** with tags and scalesWith, bounded by what core talents actually reference. Coefficients null pending simulation, which is the only blocked field left.

**Priest Holy and Shadow is left unwired deliberately** and recorded in `meta.deliberateGaps`: Shadowform forbids casting Holy spells, so the class already rules the pair out and wiring it would be symmetry against the game.

**The ability tags share the talent `reads` vocabulary**, so a tag conversion is now a set intersection rather than a text search. That is the fix for the question that produced three wrong answers before the data existed.

**REG-47. It restructures how the work is presented. Two configurations.**
**Core, "Fixing Classic"**, is the 27 rebuilt vanilla trees alone. **Expanded, "Expanding on it"**, adds the seven absorbed and three original trees. Encoded as `meta.configurations` with `configurations` on each tree and `availableIn` on each talent; `validate.py core` and `validate.py expanded` run the suite against either.

**Core stands alone and it is now checkable that it does.** Zero errors, five warnings, 42 edges, 15 mutual pairs, all nine classes covered, and not one of its pairs touches a tree that might never ship. **Twenty-six of expanded's thirty-one warnings are the seven absorbed trees**, so the expansion's debt is confined to the expansion.

Core ships first and is defensible on the audit alone. Expanded is a second argument that depends on accepting the first.

**REG-46. CLOSED by REG-47's reciprocal nodes.** Seven added to core trees, expanded-only, producing six new mutual pairs: Chronomancer with Arcane and Frost, Dreamer with Feral and Restoration, Radiance with Holy and Shadow. **The first draft of all seven failed REG-07** by doing nothing without the new tree, and the validator caught it on the run immediately after the rule was encoded. Rewritten with a base effect plus the new-tree interaction as upside.

**REG-48. NEW. Six absorbed trees are still unreached.**
Necromancy, Metamorphosis, Bladedancer, Conduit, Runeblade, and absorbed Survival have no core tree pointing at them. One reciprocal node each and the expansion is symmetric.
Chronomancer, Dreamer, and Radiance each carry two cross-tree nodes and no vanilla tree points at them. Structurally understandable, since a vanilla tree cannot reference one that may never ship, but it means splashing an original tree is a one-way relationship. Decide deliberately rather than by omission.

**REG-43. One schema, one dataset, one validation suite.**
`SCHEMA.md` defines four entities: tree, row, talent, ability. `talent-data.json` holds all 64 trees and 1,091 talents in it, built by `migrate.py` from the three previous files. `validate.py` encodes the twelve rules that had accumulated as prose and runs them as a suite. **Zero errors, 32 warnings on first run.**

**The suite independently rediscovered REG-25** without being told it existed: every finding on numeric talents, missing subtraction nodes, starved gate 20, and mechanic coverage lands on the seven absorbed trees and matches the hand-written change list. Rules that reproduce a known answer are worth trusting.

**The abilities table is empty by design and is the gear socket.** Gear effectiveness is a question about abilities, not talents, and cannot be answered until abilities exist with declared `tags` and `scalesWith`. Leaving the table out would mean editing every talent later.

**Authoring debt is now recorded in the data**, under `meta.authoringDebt`: `standsAlone` unset on 37 talents, `flags` partly inferred, `reads` authored for rebuilt trees only, `abilities` empty. An inferred field that looks authored is worse than an empty one, which is the same lesson as the reads field one turn earlier.

**REG-42. It narrows REG-38 sharply. Conversion is worth building for three classes, not nine.**
Measured against the authored `reads` field: Mage 58%, Warlock 27%, Priest 26%, everything else at 14% or below and five classes catching a single talent. **Only 143 of 454 talents read any category at all**, because the rebuilds replaced percentages with discrete effects on *named abilities*, and a named ability is what a conversion cannot reach. The hygiene work that made conversion safe also made it thin. Option A applies to Mage, Warlock, and Priest; the other twenty-four trees keep their gate-20 sideways node. Three rewrites, not twenty-seven.

**Every prior ranking of this question was wrong, including the reasoned one.** Vanilla data said Hunter highest; keyword matching on rebuilt data agreed; authored data says Hunter catches one talent worth one point. The section 6 reasoning called Shaman a clear yes (it catches three points) and Priest a no (it is third strongest). Recorded in `conversion-framing.md` section 7.1 rather than quietly corrected.

**REG-41. CLOSED. The reads field is authored across all 454 talents.**
Rule: a talent reads a category only if its effect would automatically extend to a new member of it. 142 talents whose rebuild text was "kept" or "unchanged" were backfilled from vanilla descriptions first; 8 remain without usable text and are the known gap.

**REG-39. CLOSED. The 27 rebuilt trees are now structured data.**
`rebuilt-trees.json`, 27 trees and 1,408 points, matching the `trees.json` schema. Twenty-three parsed from the document, seven matching their stated totals exactly and the rest within five points. Four existed only as prose and were written out by hand: Mage Fire, Rogue Subtlety, Warlock Destruction, Warrior Protection. Point totals approximate, talent text abbreviated, category membership reliable. Every future measurement runs against this rather than `talents-classified.json`, which holds vanilla only.

**REG-40. NEW. Conversion placement is per class, not global.**
Measured by how much of the destination tree reads the new category, then corrected for the rebuilds. Clear yes: Mage, Shaman. Arguable: Warlock, Rogue, Druid, Paladin. No: Priest, Hunter, Warrior. Gate 20 stays the crossing point in every tree; what sits there is whichever mechanism the class supports. **Third time symmetry has been the wrong instinct**, after one absorbed tree per class and one second tree per host, so treat "one per class" as a hypothesis to test rather than a design.

**REG-38. The largest outstanding design item. Tag conversion.**
The talent document cites Lord of Hatred three times and takes only hygiene lessons: separation of concerns, flat-node deletion, and the 3-and-4 ratio. None of those produces a build. **The mechanism that generates build variety in that game is tag conversion**, which the original research quoted and the document never used. Vanilla has the tags and no talent moves anything between them, which is why two trees of one class rarely combine.

Nine conversions proposed, one per class, in `tag-conversion.md`. Safer here than in the source, because Section 5.1 already deleted the flat nodes, so a conversion catches behaviours rather than damage multipliers and cannot spiral.

**First open question withdrawn.** Conversions do not need an internal downside. Shadow Mastery and Ruin are purely additive with no downside and produce vanilla's only two named builds; the choice was never in the talent, it was in the thirty points needed to reach it. Recorded in `conversion-framing.md`.

**Placement is the design.** A conversion lives in the **destination** tree, never the source, so reaching it costs the source tree's capstone. "Frostbolt counts as Fire" in the Fire tree means 30/21 and giving up Ice Barrier. The cost appears by itself.

**Second open question, still open, three options in `conversion-framing.md` section 4.** A: conversion replaces the sideways node at gate 20, cleanest, rewrites 27 gate-20 tiers. B: conversion at gate 20, sideways node drops to gate 15. C: both at gate 20, tier grows to ten or eleven points. Recommendation is A, decision is Brendan's.

**REG-36. Four classes have one-way cross-tree wiring and produce no named hybrid.**
All 34 cross-tree nodes in the 27 rebuilds were mapped to the tree they reach toward. Eleven pairs are mutual and will produce named builds. Twelve edges are one-way. **Mage has no mutual pair at all**, which is notable because it is the class with the healthiest trees and the most repetitive gameplay. **Warlock is a chain flowing one way into Destruction**, which is a poor result for the one vanilla class that already had two competing named builds. Rogue Combat and Hunter Survival are likewise unpartnered. Fix is one node each in Fire, Destruction, Assassination or Subtlety, and Marksmanship or Beast Mastery. Four nodes takes the prediction from eleven named builds to fifteen. Recorded in `partial-builds.md`.

**REG-37. NEW. Build naming follows talent pairs, not point splits.**
Vanilla names SM/Ruin and DS/Ruin after two talents and leaves 17/34/0 unnamed, because the warrior split has no pair. One signature talent gives a spec name players already have; two from different trees give a build name they do not. That makes cross-tree conditionals name generators and is the strongest practical argument for them found so far.

**REG-34. It reframes the class document. Two kinds of tree exist.**
**Absorbed trees** take a fantasy that shipped elsewhere and find it a vanilla home: the original seven. **Original trees** take a fantasy vanilla asserts and never shows and build it from nothing: Chronomancer, Dreamer, Radiance. The second kind carries a higher burden of proof, because there is no shipped version to point at as evidence it works. Recorded in class absorption 7.9, and it corrects Section 7.10, which said priest and druid need nothing when what it established was that neither *absorbs* anything.

**REG-35. NEW. Dreamer and Radiance folded in as candidates, not commitments.**
Both in `trees.json` with a `status` field distinguishing candidate from committed and a `source` field distinguishing original from absorbed. Both in class absorption as 9.10 and 9.11, marked candidate in their own headings. The decision between them, or for both, is open. Dreamer's concentration edit is applied: coverage 100% to 77%, and Radiance trimmed 84% to 70%, both now inside REG-31's band.

**REG-32. The original seven absorbed trees share a row template.**
Five of the seven are byte-identical in row distribution at 13/11/10/9/6/8/1, and the other two differ in one row each. Vanilla varies from three points at gate 20 to sixteen. A shape repeated seven times is a template rather than a design, and it is specifically the front-loaded shape REG-18 names as the most common structural fault in the game. The three newer trees run 10/12/9/10/8/8/1, a spread of four against seven or eight. Use the newer shape as the target when revising the seven.

**REG-33. NEW. Overlap testing added, with a known blind spot.**
Trees can now be fingerprinted across twelve systems and compared pairwise. Radiance scores 0.97 against vanilla Holy priest, the highest in the suite. The metric measures which systems a tree touches, not how, so it cannot see that Radiance does healing and damage in one mandatory cast. Treat a high score as a prompt to look, not a verdict. The Radiance case resolved favourably: the Holy rebuild in talent design Section 15 already deleted the nine points of Smite and Holy Fire content that create the overlap.

**REG-31. REG-27 should be a band, not a floor.**
Mechanic coverage was written as a floor after Metamorphosis declared a mechanic and contained none of it. Dreamer measures 100%, which scores perfectly against a floor and is brittle: a tree where every talent needs the mechanic has no fallback if the mechanic fails. Proposed band is roughly 40 to 80 percent. Conduit at 51% is the model. Metamorphosis at 0% is broken, Dreamer at 100% is concentrated. Dreamer needs an edit shedding roughly 30 points of coverage before it is committed.

**REG-30. Five trees on one host has no second instance.**
If Chronomancer works, the question of a second absorbed tree for the other eight hosts arrives immediately, and nothing in the suite answers it. Either the asymmetry is permanent and justified per host, or eight more trees are implied. Decide before publishing rather than after someone asks.

**REG-27. Metamorphosis did not contain its own declared mechanic.** Fel corruption is named as the local mechanic and zero of its 58 points apply, spend, or reference it. Demonology's premise failure exactly. Mechanic coverage measured across all seven: Conduit 30/58, Blackguard 22/58, Survival 16/58, Bladedancer 13/64, Necromancy 12/58, Runeblade 11/60, Metamorphosis 0/58. **Worth measuring on any future tree: does the tree contain the thing it is named for?**

**REG-13. Fill the remaining spec ledgers.**
Thirteen specs need talent-level allocations rather than X/Y/Z splits. `ledger.py` computes the ledger and validates gates once an allocation exists.

**REG-14. Leveling feel pass.**
The dividend front-loads stat gain smoothly, but a level 12 warrior with one rank of one talent may feel worse than a vanilla warrior with 2/5 Deflection. Untested and needs its own pass.

**REG-15. Hybrid tuning.**
Row 5 as a real seat creates 31/20 builds that need balancing. Vanilla never balanced hybrids because nobody played them. The tuning surface roughly doubles.

---

## 3. Verification debt

Things currently asserted that have not been checked. Each is a candidate for the same class of error as REG-C4.

**REG-20. Eleven of thirteen canonical builds are unconfirmed.**
`specs-baseline.json` marks one verified, one likely, eleven `needs-check`. Confirm against a talent calculator before any sim run.

**REG-21. CLOSED. Classifier hand-reviewed across all 27 trees.**
Twenty-five corrections, twenty-three to flat and two to behavior, from two systematic errors: triggered numbers read as new effects, and compound descriptions read as behavior on the word "and". Revised totals 991 flat of 1,352, 73%. The review changed conclusions: Enhancement shaman 18 to 28 and now tied worst, Protection warrior 7 to 15 and no longer the healthiest tree, Holy priest out of the worst five, rebuild order changed. Recorded in `spec-grievances.md` section 13.

**REG-23. Tier arithmetic correction did not propagate on first pass.**
The REG-C10 fix was applied to Section 1.1 but fourteen other places in the talent document still carried the old 31/20 claim, found only when starting REG-07. All fourteen corrected. **Standing lesson: when a correction lands, grep the whole suite for the old claim rather than fixing the passage that prompted it.**

**REG-22. Arms rebuild row assignments are unverified.**
Talent design section 6 states this in its own text. The gates in that rebuild have not been checked against a calculator, which is precisely the error class that produced REG-C4 and REG-C10.

**REG-23. Font licensing.**
MORPHEUS.TTF and FRIZQT__ are commercial faces. Verify before any public-facing build ships. Free substitutes noted in the art direction revision.

**REG-24. Image permissions.**
ChromedDragon Classic zone mockups are used on assumed permission, with per-image attribution required. Confirm the permission is actual rather than assumed.

---

## 4. Build and visualization

**REG-30. Four InterlockSpine rendering bugs, unfixed.**
Edge weight hardcoded to 1px regardless of downstream reach, so the most load-bearing nodes draw thinnest. Label halos stippling departing edges through paint order. Fixed canvas at 1364 by 1152 with no downscale, caused by tier imbalance. A stray band divider rule and one odd cargo label.
*The talent-tree top-to-bottom layout from the art direction revision is the intended structural fix for the third.*

**REG-31. Apply the art direction revision.**
Talent-tree spine, item-quality tier colors, tooltip cards, quest-log body, client palette.

**REG-32. New render axis available.**
Every node in all 27 trees now carries a flat/behavior/active tag in `talents-classified.json`. Colouring a tree by what each node buys makes the audit visual, and a before-and-after toggle on a rebuilt tree is the most demonstrable single idea in the talent document.

---

## 5. Documentation debt

**REG-40. Provenance appendix not yet applied everywhere.**
Done: `classic-plus-talent-design.md`, `spec-grievances.md`, `classic-plus-living-world-design.md`. Outstanding: `classic-plus-class-absorption.md`, the three Claude Design briefs, `art-direction-revision.md`, `sim-baseline-protocol.md`.
*Blocked by REG-00 for the class document and briefs.*

**REG-41. Class Absorption needs a reciprocal pointer.**
The talent document declares itself upstream of the absorbed trees. That document does not yet say so.
*Blocked by: REG-00.*

---

## 6. Closed, do not reopen

The most useful section in this file. Each of these was genuinely settled, with the reason, so it does not get argued again after a context gap.

**REG-C1. Absorbed trees get no depth dividend.**
Points in them buy behavior only; the local mechanic is the reward for depth. Reason: 5.1's tuning method sums what a canonical vanilla build already buys, and an absorbed tree has no canonical vanilla build to sum. Also protects Class Absorption's own rule that no tree may tax its host's existing role.
*Recorded in talent design 8.3.*

**REG-C2. Row 5 is the hybrid seat.**
51 minus a 31-point capstone leaves 20, and row 5's gate is exactly 20. Confirmed as a vanilla precedent rather than a proposal: both canonical warlock raid builds are a row 5 talent plus a deep tree, and warlock is the only vanilla class with two competing viable raid builds.

**REG-C3. 5.1 is load-bearing, 5.2 is supporting.**
Reversed from the first draft. Reason: rogue has healthy trees and flat builds anyway, because the flat talents are simply stronger. Restructuring a tree does not fix a tree. Only removing the flat nodes and returning their value as a curve changes that outcome.

**REG-C10. A tier gate is points already invested, so owning a tier-N talent costs 5(N-1) + 1.**
Tier 7 costs 31, tier 6 costs 26, tier 5 costs 21. An earlier draft read 51 minus 31 as 20 and called that the tier 5 seat. Twenty points reaches tier 4. The correction improved the argument: the real shapes are 31/20 for a capstone plus a shallow second tree, or 30/21 and 26/25 for no capstone and two deep talents. **Both canonical warlock builds take the second shape and own no 31-point talent**, which is why warlock is the class with build diversity.

**REG-C4. Impale sits at tier 4 behind a 15-point gate.**
Not tier 5. Fifteen plus two ranks is 17, which is why the canonical Fury build is 17/34/0. An earlier draft had this wrong and it would have made the canonical build impossible. **The general rule that came out of it: confirm gates before filling any ledger, because a wrong gate does not throw an error, it produces a plausible ledger with the wrong contents.**

**REG-C5. Seasons follow latitude, not two hemispheres flipping.**
Azeroth's warm band sits south on both continents, so one rule works everywhere without per-zone exceptions.

**REG-C6. The forced-flat floor is a lower bound, not a prediction.**
A low floor means the tree permits an interesting path, not that anyone walks it. Where the floor is low and builds are flat anyway, the fix is making behavior talents worth taking, not restructuring.

**REG-C7. Good trees do not produce good gameplay.**
Mage has the healthiest trees in the game and the most repetitive rotation. The talent rework is necessary and not sufficient, and the document says so in its own voice in section 10.

**REG-C8. Trueshot Aura moves to the depth dividend rather than being deleted or kept.**
The raid keeps the aura, the hunter keeps the raid slot, and the capstone is freed for something the hunter does. Generalizes: the dividend is where a spec's obligations to other people belong.

**REG-C9. Arms was the wrong tree to rebuild first.**
At 12 of 30 forced flat it is one of the healthier trees. Marksmanship went first instead, being both the flattest tree in the game and its class's mandatory raid spec. Section 6 now says this in its own text.

---

## 7. Counts

| | Count |
|---|---|
| Blocking decisions | 0 |
| Queued work items | 24 |
| Verification debt | 5 |
| Build and visualization | 3 |
| Documentation debt | 2 |
| Closed | 30 |

No blocking decisions remain. Everything left is work.

All 27 vanilla trees are rebuilt, the seven original absorbed trees are audited and revised, an eighth has been added and integrated, and the documents share a rule set.

Outstanding, none of it design: **REG-28**, run the Section 5.7 cross-tree check on the vanilla side's sideways talents, which is the last consistency item between the documents. Then REG-13 on the ledgers, REG-06 on mid-tree weighting, REG-14 on leveling feel, REG-15 on hybrid tuning, and REG-02 folding coefficient-setting into each tree. All of the remainder needs simulation or talent-level builds rather than design decisions.
Cheapest open action: append `appendix-d-portable.md` to the canonical living world document.
