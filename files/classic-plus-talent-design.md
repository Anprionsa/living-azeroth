# Classic+ Talent Design: Behavior Over Numbers

**Version 1.0 | August 2026**

*Third document in the Classic+ suite. "A Living Azeroth" covers world texture. "Class Absorption" argues that post-vanilla classes should arrive as talent trees rather than as classes. This one sits upstream of that: it concerns what a talent point should buy in the first place. The eight trees proposed in Class Absorption should be built to the rules set out here, and where they are not, this document is the one that wins.*

---

## 0. Scope and constraints

Five constraints, accepted before any design work.

The tree structure stays. Three trees per class, seven rows, five points per row to advance, 51 points at level 60, a capstone at row 7. None of that is the problem and none of it changes.

This is not a departure. A player who last logged out in 2006 should open the talent panel and recognize it immediately. The shape is identical. What changes is what the nodes contain.

Points buy behavior, never numbers. No talent should exist whose entire text is a percentage.

Flat stats do not disappear from the game, they stop being purchased. Where a number is still wanted, it is granted automatically for depth in a tree rather than bought with a point. Fifteen points in Fury gives you the Fury stat curve regardless of which fifteen.

Power stays where it is, at the level of the raid rather than the individual spec. **Band neutrality is the settled position:** total raid output is held constant while individual specs may move within it. That keeps the claim that matters, which is that this is not a power increase, while allowing the worst gaps to be closed. Strict per-spec neutrality was rejected because it would reproduce vanilla's imbalance exactly.

---

## 1. The problem, measured

The complaint is usually stated as a feeling. It is worth turning into a number first, because the number is worse than the feeling.

Take the vanilla Arms warrior tree at 1.12. Eighteen nodes, 59 available points.

| Category | Points | Share |
|---|---|---|
| Buys a number (damage, cost, cooldown, crit, parry) | 36 | 61% |
| Buys a new effect or technique | 21 | 36% |
| Buys a new button | 2 | 3% |

Two points out of 59 give you something to press. Sweeping Strikes and Mortal Strike. Everything else either changes a number or, at best, attaches a proc to a number.

Weapon specialization is the clearest offender. Axe, Mace, Sword, and Polearm hold 20 of the tree's 59 points between them, and they are mutually exclusive in practice. You are not choosing a playstyle there, you are declaring which weapon you happened to loot.

The generous reading is that 39% of the tree buys behavior. The strict reading is 3%. Both are indefensible for the system that is supposed to be the primary expression of a character.

Arms is not special. All 27 vanilla trees have since been parsed from client-accurate data and classified node by node, then hand-reviewed: 1,352 available points across the game, 991 of which buy a number. Seventy-three percent.

A harder measure exists and it needs no opinion about builds. To own a talent gated at 30 points you must first spend 30 in that tree, and the gates constrain the order. Take every behavior talent the moment it becomes legal, fill with flat only when nothing else is, and count. That is the minimum filler the tree forces on you.

Enhancement shaman and Warlock Demonology tie at 28 of 30, meaning two points of the entire climb can buy behavior. Feral druid forces 26, Retribution paladin 24, and Marksmanship hunter 23. At the other end Fire mage forces 8 and Shadow priest 11. Specs with poor community reputations average 22.7; specs with good reputations average 14.4.

The full audit, including what players actually complain about per class and which complaints this document cannot fix, is in `spec-grievances.md`. Three of its findings are load-bearing enough to change the argument here, and they appear in 1.2, 5.3, and 8.

### 1.1 The second problem: sealed trees

Arms does not know Fury exists. Every talent in Arms modifies an Arms ability or a baseline warrior ability. Nothing in it reads the Fury tree, and nothing in Fury reads Arms.

The result is that hybrid builds are compromises rather than designs. You give up a capstone and receive twenty points of filler. The community solved this years ago by simply not doing it, which is why vanilla build diversity collapses to about three specs per class.

There is a structural irony sitting underneath this. The 51-point budget already encodes a hybrid:

- Row 7 requires 30 points in a tree, plus 1 for the capstone itself. That is 31.
- 51 minus 31 leaves 20.
- Tier 5 of a second tree gates at 20 invested, so owning a tier 5 talent costs 21.

A tier gate is points already invested, so owning one talent at tier N costs 5(N-1) + 1. Tier 7 costs 31, which is where the familiar 31-point capstone comes from. Tier 6 costs 26 and tier 5 costs 21.

An earlier draft of this document got the next step wrong. It read 51 minus 31 as 20 and called 20 the row 5 gate, concluding that the budget natively produces a capstone plus a row 5 talent. It does not. Twenty points reaches tier 4, because buying at tier 5 costs 21.

What the budget actually produces is more interesting:

| Split | Reaches | Shape |
|---|---|---|
| 31/20 | tier 7 + tier 4 | a capstone and a shallow second tree |
| 30/21 | tier 6 + tier 5 | no capstone, two deep talents |
| 26/25 | tier 6 + tier 5 | no capstone, balanced |
| 21/21/9 | tier 5 + tier 5 + tier 2 | three-way |

Taking a capstone costs 31 of 51, and what remains buys almost nothing. Skipping it buys two genuinely deep talents instead. That is a real decision and vanilla already contains the proof that it is a good one.

Both canonical warlock raid builds skip the capstone. SM/Ruin is 30 in Affliction for Shadow Mastery, a tier 6 talent, plus 21 in Destruction for Ruin, a tier 5. DS/Ruin is 21 in Demonology for Demonic Sacrifice plus 30 in Destruction. Verified against gate data, and neither owns a 31-point talent.

Warlock is also the one vanilla class with two competing viable raid builds. The class that skips its capstones is the class with build diversity, which is the single most useful fact in this document.

### 1.2 The third problem: talents that are dead, not boring

A category the first draft of this document missed entirely, because auditing one tree cannot reveal it.

Some vanilla talents are not weak modifiers. They are modifiers to things the game no longer asks you to do.

Protection paladin tanking guides state that roughly 95% of a raid protection paladin's threat comes from casting Greater Blessing of Kings on party members, and that the One-Handed Weapon Specialization talent sitting in the Protection tree is useless because paladin melee damage is never relied on for threat. That is a node in a tank tree that is dead on arrival for tanks.

A vanilla-era priest post makes the same complaint about the entire Holy tree: in Molten Core you are not casting Greater Heal, Heal, or Prayer of Healing, so every talent buffing them is wasted. The talents work exactly as written. The encounter design moved and they did not.

These need deleting, not rewriting. Section 5.2 converts a flat rank into a discrete effect, which is the right treatment for a talent that does something small. It is the wrong treatment for a talent that does nothing, because an interesting version of a useless talent is still useless.

**The category is much smaller than it first appears, and the sweep that established that is worth recording.** All 27 trees were screened for effects that cannot apply to a raid boss, effects conditional on creature type, and effects that only matter against players. Twenty-eight nodes were flagged. Hand review kept one.

Almost everything the screen caught was one of two things. Either the flagged clause was a rider on a talent whose real effect is something else, as with Death Wish, where 20% physical damage is the point and fear immunity is a bonus. Or it was alive in a context the screen could not see, as with Repentance and Unbreakable Will, which are dead on a boss and load-bearing in a battleground.

So the honest statement of the category is narrower:

> A talent is dead when the thing it modifies is something the spec no longer does **in any context it is played in.** A talent that is useless in raids and useful in PvP is not dead. It is evidence of the PvE and PvP split, which is a different problem and not one this document solves.

The clearest universally dead node found is paladin One-Handed Weapon Specialization in the Protection tree: protection paladin threat comes from casting blessings rather than from melee, and protection paladin has no PvP context in which melee damage matters instead. Improved Scorpid Sting and the Holy priest heal talents are dead in raids only.

The practical consequence for a rebuild is that dead nodes free almost no points. The rewrite budget in Section 5.2 does not get smaller. What the sweep did produce is a cleaner way to talk about the second category, because a tree carrying several PvP-only nodes is not full of filler, it is carrying content for a mode its raiding players never enter, and that is a scoping decision rather than a design error.

---

## 2. What four eras of WoW talent design taught

Four systems in twenty years is a lot of iteration to learn from, and each one traded something away.

**The original trees (vanilla through Wrath).** Deep, sprawling, and full of the filler measured above. What they got right was the sense of a long road: you could see the capstone from level 10 and spend forty levels walking toward it. <cite index="28-1">Blizzard's own retrospective before Dragonflight acknowledged that things were lost in the shift away from this model.</cite> The Wrath version is the one most often cited as the peak, mostly because the trees had accumulated enough genuine talents to dilute the filler.

**Cataclysm.** Trimmed the trees and locked you into a specialization. <cite index="30-1">The result was a much smaller set of viable builds, the loss of true hybrid specs, and talent choices that mattered less because once the important talents were secured the remaining points had little impact.</cite> The lesson is that trimming filler without replacing it with real choices just produces a shorter list of obligations.

**Mists of Pandaria.** <cite index="32-1">Talent trees removed entirely, replaced by six tiers of three choices each, with each row focused on a gameplay element and easy swapping between them.</cite> This is the era that solved the flat-stat problem completely, and it is worth being honest about that: MoP talents are all behavior. The reason it is still remembered badly is that it removed progression. Every character of a spec was identical except for eighteen binary choices, and you stopped feeling like you were building anything.

The lesson from MoP is precise and it is the one this document takes: behavior-only talents work, but they cannot be the whole system, because they leave nothing to accumulate.

**Dragonflight and after.** <cite index="27-1">Two trees, one class-wide and one spec-specific, with a point granted each level alternating between them, plus saved and shareable loadouts.</cite> This is the modern answer and most of it is good. What is not portable to Classic is the loadout system, which turns talents into an encounter-by-encounter equipment slot. That is directly contrary to Classic's respec cost being a real decision.

The synthesis across all four: vanilla had progression without meaningful choice, MoP had choice without progression, Dragonflight got both and paid for it with permanence. Classic+ should take progression from vanilla, behavior-only content from MoP, and leave the loadouts alone.

---

## 3. Diablo 4, Lord of Hatred

Lord of Hatred shipped April 28, 2026 and it is the most relevant single case study available, because it is a game that had exactly this problem and just finished fixing it.

What they did:

<cite index="20-1">Every dedicated passive node was eliminated from every class skill tree, including the Key Passive capstones. The stated reasoning was that legacy passive nodes provided unearned flat damage and generic power boosts that diluted combat engagement.</cite>

<cite index="25-1">Raw stat growth was stripped off the Paragon board entirely and relocated to itemization, including the small additive damage nodes players routinely pathed through to reach something better.</cite>

<cite index="22-1">The design principle stated openly: items and Paragon handle raw power scaling, while the skill tree governs how skills function rather than how much damage they deal. The rebalancing of responsibilities also gave designers freedom to write genuinely impactful nodes without breaking global power balance.</cite>

<cite index="24-1">Each active skill now carries seven upgrades. Three change the skill fundamentally, the other four adjust specific aspects of it.</cite> <cite index="23-1">The third branch of each skill offers variants that can change the skill's category outright, creating synergy with gear that references those categories.</cite>

Three things translate directly.

**Separation of concerns is the whole trick.** Each system gets exactly one job. In Classic terms: gear carries the numbers, tree depth carries the passive curve, talent points carry behavior. Vanilla currently has all three doing all three jobs, which is why none of them feels decisive.

**Removing flat nodes buys you design freedom.** The reason vanilla talents are boring is partly that they are load-bearing for balance. If Two-Handed Weapon Specialization is 5% of a warrior's damage, it cannot be replaced with something interesting without a tuning pass on the whole class. Move that 5% somewhere structural and the node is free to become anything.

**The 3-and-4 split is a usable template.** Three transformative options, four adjustments. That maps cleanly onto a seven-row tree and is a reasonable target ratio for how many nodes per tree should genuinely change how you play.

**A fourth thing, recorded late and as a correction.** The three above are hygiene. They make a tree cleaner and not one of them produces a build.

The mechanism that actually generates build variety in Lord of Hatred is tag conversion: skill variants change a skill's elemental and mechanical tags outright, and the Paragon board reads those tags, so a frost-converted Hydra stops benefiting from Fire nodes and starts benefiting from Frost ones. A build there is a declared set of tags and everything in the game that reads them.

Vanilla has the tags already, in damage schools, bleeds, poisons, curses, diseases, melee, ranged, and spells, and no vanilla talent moves anything between them. That is why two trees of one class rarely combine: a Fire talent has no way to notice a Frost spell exists.

This document saw the mechanism, quoted it, and took only the hygiene. `tag-conversion.md` works it out properly, including the reason it is safer here than there: Section 5.1 already deleted the flat nodes, so a conversion catches behaviours rather than damage percentages and cannot spiral the way it does in an ARPG.

One thing that does not translate: D4 raised the level cap and handed out more points to fill bigger trees. Classic+ should hold the 51-point budget fixed. Power neutrality is the entire political case for this rework and giving out more points forfeits it.

---

## 4. Three other games worth stealing from

**Grim Dawn: the mastery bar, and modifiers that cross the boundary.**

<cite index="36-1">Grim Dawn's mastery bar is divided into nine tiers. Filling it to a tier unlocks the skills of that tier, and each point invested in the bar also grants an increase in base attributes. A second mastery is chosen at level 10 to create a dual-class character.</cite>

Two separate ideas here and both are useful. The bar itself is the closest existing implementation of "depth grants stats," although Grim Dawn still makes you spend points on it. The version proposed in 5.1 is cleaner: grant it free.

The more important idea is the modifier system. <cite index="36-1">Modifiers alter the behavior of active and passive skills by adding additional effects.</cite> In a dual-class character these routinely cross the mastery boundary, so your second mastery's passives reshape your first mastery's abilities. That is the exact mechanism vanilla lacks, and it requires no new interface. It only requires writing talents that point sideways.

**Path of Exile: subtraction as a design tool.**

Keystones in Path of Exile take something away. Resolute Technique removes your ability to critically strike and in exchange your attacks never miss. Chaos Inoculation sets your life to 1 and makes you immune to chaos damage. Blood Magic removes your mana pool and pays for everything with health.

These are the most build-defining nodes in that game, and the reason is that they close doors. A talent that only adds is a talent everyone eventually takes. A talent that subtracts is a talent that produces two different characters.

Vanilla has almost none of these. The one clean example is Shadowform, which increases shadow damage and reduces physical damage taken at the cost of being unable to cast Holy spells. That precedent matters, because it means the design space is already established in the era and does not need to be argued for from scratch.

**Last Epoch: the tree below the tree.**

<cite index="44-1">Investing passive points into a mastery tree unlocks skills unique to that mastery, and points can be placed in the other mastery trees up to half the tree.</cite> More relevant is what Last Epoch does one level down: each specialized active skill gets its own tree, and its nodes transform the skill rather than scaling it. A fireball becomes a wall of flame, or a projectile that seeks, or a totem.

This is almost certainly too much system for Classic+ and it is not proposed here. It is worth noting as the endpoint of the direction, and as the reason to hold back: the further you push toward per-ability trees, the less the result resembles the game.

---

## 5. The proposals

### 5.1 The depth dividend

Every point spent in a tree grants an automatic passive appropriate to that tree. Not purchased. Granted for depth, regardless of which talents were taken to get there.

Fifteen points in Fury gives you the Fury curve. Thirty-one points gives you roughly twice it. Which fifteen is irrelevant.

This is where every flat bonus currently sitting in the trees goes. Deflection, Divine Strength, Divine Intellect, Ancestral Knowledge, Arcane Focus, Lethal Shots, Two-Handed Weapon Specialization, Malice, Suppression, Convection. All deleted as nodes, all returned as curve.

The tuning method that makes this defensible: take a canonical raid build for each spec, sum every flat bonus it currently takes, and set the depth coefficient so a 31-point investment delivers approximately that sum. The character ends up with the same numbers. The difference is that the sixteen or so points which used to buy them are now free to buy something else.

Some illustrative shapes, with coefficients as placeholders pending simulation:

- Arms: melee critical strike chance and armor penetration, rising per point.
- Fury: attack speed and rage generation.
- Protection: armor, block value, and threat.
- Fire mage: spell critical strike and fire damage.
- Restoration druid: healing done and mana efficiency.

Two consequences worth stating plainly. First, this makes the first point in a tree meaningful, which it currently is not. Second, it removes the "trap build" problem for new players, because you can no longer accidentally skip the mandatory stat nodes.

There is a third, and the cross-class audit is what surfaced it. Rogue has among the healthiest trees in the game by forced filler, and real vanilla rogue builds are stacked with Malice, Lethality, Precision, Lightning Reflexes, and Deflection anyway. All pure numbers, none of them forced, taken because they are simply stronger than the alternatives.

So restructuring a tree does not fix a tree. Rogues would keep those builds through any amount of node redesign, because the problem is not what the tree permits, it is what the spec sheet rewards. The depth dividend is the only proposal here that changes that outcome, because deleting the flat nodes and returning their value as a curve makes the interesting path the only path at identical power.

That makes 5.1 the load-bearing proposal in this document and 5.2 the supporting one, which is the reverse of how they were originally weighted.

### 5.2 Ranks stack effects, they do not scale numbers

Multi-rank talents stay. Five-rank nodes stay. What changes is what a rank does.

A rank should add a discrete effect rather than increase a number. The vanilla node:

> **Improved Rend.** Increases the damage of your Rend ability by 15%, 25%, 35%.

becomes:

> **Bloodletting.**
> Rank 1: Rend ignores armor.
> Rank 2: Overpower refreshes Rend's duration.
> Rank 3: When a target affected by Rend falls below 20% health, Rend deals all of its remaining damage at once.

Same node, same three ranks, same position in the tree. Rank 3 changes the rotation. Rank 2 creates a reason to keep Overpower in it. Nothing scales.

This is more design work per node than writing a percentage, and that cost should be acknowledged rather than hidden. It is roughly 150 nodes across nine classes. It is the single largest line item in this document.

The 3-and-4 ratio from Lord of Hatred is a reasonable target: per tree, about three nodes should transform how a spec plays and about four should adjust it. The rest can be modest.

### 5.3 Tier 5 is the hybrid seat

This is the structural fix for sealed trees, and it costs nothing to implement because the arithmetic already exists.

The budget offers two honest shapes: 31/20 buys a capstone and a shallow second tree, or 30/21 and 26/25 skip the capstone and buy two deep talents. The second shape is the one vanilla warlock actually uses.

So tier 5 of every tree becomes the designated cross-tree seat, reachable at 21 points. It holds at least one talent whose value is highest for a character whose main investment is elsewhere.

An Arms tier 5 example, reachable at 21 points and worth taking by anyone who swings a weapon:

> **Mortal Cleave (2 ranks).**
> Rank 1: Your Cleave and Whirlwind apply Mortal Strike's healing reduction.
> Rank 2: The healing reduction persists for 4 seconds after the target leaves your melee range.

Cleave and Whirlwind are baseline, so this is worth its points to any warrior, which is what Section 5.7's rule requires. It is worth *most* to a Fury warrior, whose rotation leans on both, and it hands a Protection warrior a real off-tank tool.

The rule generalizes: a sideways talent sits in tree A and is worth more to a tree B main than to a tree A main, because tree B's rotation uses it harder. It must never be worth *nothing* without tree B, which is the trap Section 5.7 closes.

This is not a new idea, and it is not untested. Vanilla warlock already does it in both directions, and it is the only vanilla class with two competing viable raid builds. Section 1.1 has the corrected arithmetic: the seat is tier 5 at 21 points, not 20, and the builds that use it skip the capstone entirely. Any objection that a mid-tree seat would go unused has a counterexample that shipped in 2004.

It is also not new in this project. The seven trees in Class Absorption were already built around a twenty-point mark and a thirty-one point capstone, described there as the two-signature structure and justified on the grounds that partial investment should be a legitimate outcome rather than a failure state. Two documents reaching the same conclusion from opposite directions is strong evidence that the mid-tree seat is real. Note that both used the twenty-point figure, and Section 1.1's correction applies to both: the seat costs 21.

One risk worth naming now rather than discovering later. This creates optimal hybrid builds where none existed, and simulation will find them within a week. That is acceptable if the mid-tree seats are tuned as lateral rather than superior, but it does mean the 30/21 and 26/25 splits need as much tuning attention as the pure builds, which vanilla never gave them.

### 5.4 Subtraction talents

A small number of nodes should close a door.

Two per tree at most, and they should be optional nodes rather than capstones, because a forced subtraction on a capstone reads as a nerf while an optional one reads as a choice.

The Shadowform precedent is the one to cite in any public discussion of this, because it establishes that vanilla already shipped a talent that takes something away in exchange for an identity. That argument is much harder to dismiss than an appeal to Path of Exile.

Examples:

> **Sure Strike (Arms, tier 5, 1 rank).** Your melee attacks can no longer be dodged, parried, or miss. Your melee attacks can no longer critically strike.

That is a Resolute Technique port and it is a genuinely hard decision for a warrior, because giving up critical strikes also gives up Deep Wounds, Flurry, and most of the depth dividend. It is strong in PvP against high-avoidance targets and weak in raids. That is exactly the shape a keystone should have.

> **Vow of Silence (Priest, Discipline, tier 5, 1 rank).** Your healing spells cost no mana when cast on a target below 30% health. You can no longer cast Power Word: Shield.

These are also the nodes most likely to break something, so they should be the last thing designed and the first thing cut if the budget runs out.

### 5.5 World-facing depth rewards

This is the part that makes the system Classic+ rather than a generic ARPG rework, and it is the join to the living world document.

Talents that do not help you fight are never taken. That is a solved problem in every game that has tried it. So world-facing effects should not be talents at all. They should ride on the depth dividend, granted free at investment thresholds.

At 15 and 30 points in a tree, alongside the stat curve, a character gains a world-facing capability tied to what that tree is about:

- Beast Mastery hunter at 15: you can read tracks well enough to see where a zone's beasts have moved with the season. This is the player-facing surface of seasonal fauna, Living Azeroth section 10.4.
- Subtlety rogue at 15: caravan drivers and their cargo become valid pickpocket targets. Ties to cart and caravan routes, section 2.
- Restoration druid at 15: herbs in the zone you are standing in show their remaining season to you. Ties to per-species herb calendars, section 10.3.
- Elemental shaman at 15: you can read the coming weather in a zone before it arrives. Ties to the weather system, section 10.9.
- Holy priest at 30: the recently dead in a zone can be questioned, in the same register as the hidden lore NPCs in section 1.7.

Each of these is small. None of them affects combat. All of them make a spec choice visible outside of a raid instance, which is something vanilla talents never once managed.

The scoping note matters: this list should stay short and should be cut entirely if the world systems it depends on do not ship. A depth reward that reads seasonal herb data is worthless on a realm with no seasons.

### 5.6 Unconventional builds, and what the curve shape decides

Settled: the goal is that going deep should carry an edge without making anything else a mistake. Nobody should be pigeonholed, and a player who splits should end up with a character rather than a compromise.

Three levers control this and they need setting deliberately rather than falling out of tuning.

**The dividend curve is linear.** A superlinear curve, where later points in a tree are worth more than earlier ones, rewards depth twice: once through the capstone and again through accelerating stats. That is the pigeonhole. A sublinear curve punishes depth and pushes everyone into spreading, which is the same failure inverted. Linear is the only shape that leaves the decision to the talents.

The consequence is worth stating plainly: **spreading points costs you no stats.** A 26/25 build and a 31/20 build receive the same dividend total. What differs is entirely what talents they own. That is the correct place for the difference to live.

**Depth is rewarded by discrete talents, not by the curve.** The capstone is the reward for going all the way, and it should be strong enough that going all the way is attractive. It should not be so strong that not going all the way is a mistake, which is what vanilla currently gets wrong through back-loading almost all of a tree's power into its last rows.

The checkable rule: **two tier-5 seats plus a tier-2 talent should be worth roughly one capstone plus one tier-4 talent.** If a 21/21/9 build and a 31/20 build land in the same band, the budget is doing its job. If they do not, the mid-tree talents are underweight and that is a tuning target rather than a structural one.

**Interdependency is what makes a split build an identity.** A build that is merely stat-neutral is not interesting, it is just permitted. What makes 26/25 a character rather than a hedge is talents in one tree that change what talents in another tree do.

Section 5.3 puts one cross-tree seat at tier 5. That was too narrow. The corrected arithmetic in Section 1.1 shows the budget supports tier 6 plus tier 5, so cross-tree conditionals belong at both, and a small number should sit lower for three-way splits. Design them as a set rather than one per tree:

- Tier 5, reachable at 21, the common seat. Modifies a sibling tree's abilities.
- Tier 6, reachable at 26, for the deep-but-no-capstone shape. Should be strong enough to compete with a capstone in combination with a second tier 5 or 6.
- Tier 2 or 3, cheap, for the third tree in a 21/21/9. Small, and mostly about enabling rather than power.

**Absorbed trees participate, with one caveat that needs settling.** Class Absorption's trees should carry cross-tree conditionals in both directions: their talents modifying host abilities, and host talents modifying theirs. A paladin at 26 Blackguard and 25 Holy should be a specific character rather than a bad healer.

The caveat is a conflict with a decision already made. Section 20.3 gives absorbed trees no stat curve, on the correct reasoning that there is no vanilla baseline to calibrate against. But if vanilla trees grant a dividend and absorbed trees do not, then splashing an absorbed tree costs stats that splashing a vanilla tree does not, which is a direct disincentive against exactly the builds this section wants.

The resolution is that an absorbed tree's local mechanic must scale with depth strongly enough to be worth what a stat curve would have been. Blight, rune charges, momentum, and the rest already scale in principle. They now have a tuning target: parity with the dividend a vanilla tree of the same depth would have granted. That is a constraint on the absorbed trees, recorded here because it did not exist when they were built.

### 5.7 Revealing interdependencies

The proposal is that cross-tree interdependencies are found rather than read, and that the game tells you about them somewhere other than a tooltip.

An earlier draft of this section objected on respec cost and that objection was wrong. Vanilla's first talent reset is 1 gold and the second is 2, escalating to 5, 10, and eventually 50, with anything above 10 decaying back down at 5 gold per month. Three or four experiments are genuinely cheap, and Classic players respec routinely for raid nights and battlegrounds anyway. Experimentation is affordable. The objection is withdrawn.

Two real constraints remain, and neither argues against the idea.

**Nothing stays secret past launch week.** Talent calculators and datamined tables will publish every conditional in the game within days. So the design cannot depend on secrecy holding, and there is no point building anything whose value evaporates once it is known.

What that rules out is a system where knowing the interdependency is the advantage. What it permits, and what is worth building, is a system where the *fiction* of learning is the reward: the game has an in-world answer to how anyone found this out, and a player who engages with the world gets to feel like they discovered something even on a server where everyone already knows.

**A player must never be able to build wrong by not knowing.** This is the constraint that actually matters, and it resolves with a single rule:

> A cross-tree conditional may never be the reason to take the talent it sits on. The talent has to be worth its points on its own. The conditional is upside.

With that rule, ignorance costs a player some upside and never costs them correctness. A hunter who takes Pack Tactics without knowing it does anything extra at 26 points in Beast Mastery has still bought a good talent. The player who knows gets more out of the same points, and the player who does not has not been punished for it.

**Where the telling happens.** Not the tooltip. A trainer who mentions what their old students used to do. A book in the Ironforge Library or Scholomance. Someone in a tavern describing a warrior they fought beside who moved strangely. The living world document's whole method is that the world already asserts things it never shows, and a talent interdependency is an unusually good candidate: somebody, in the fiction, worked this out first, and the game currently has no answer for who.

This costs almost nothing to build. The trainers, the books, and the tavern NPCs already exist. It fails gracefully, because a player who never talks to anyone loses only flavor. And it puts the discovery in the place this project keeps saying discovery belongs, which is out in the world rather than in an interface panel.

The tree itself can show the condition or not; with the rule above in force, that becomes a presentation choice rather than a fairness question. The recommendation is to show that a condition exists without describing the payoff, in the same way vanilla's prerequisite arrows already indicate a dependency without explaining the result.

### 5.8 One set of talents for both modes

Settled: a reworked tree serves PvE and PvP from a single set of talents. No PvP-only nodes, no PvP branch, and no assumption that gear will bridge the gap.

That last clause is the constraint with teeth. Vanilla has PvP gear and Classic+ would presumably have more, but writing a talent that only pays off once some future itemization exists is designing on credit. Every talent has to justify its points with the game as it is.

What this rules out is the pattern vanilla uses constantly: an effect that is binary against a target type. A stun is applied or resisted, and raid bosses resist. A talent whose whole value is a stun is a PvP talent wearing a raid tree's colors, and it is exactly what a raider reads as filler.

**The general rule: prefer graded effects to binary ones.** A slow, an armor reduction, a healing reduction, a damage reduction all work on a boss at reduced relevance rather than at zero. A stun, a fear, a polymorph work at zero. Graded effects are mode-agnostic by construction, and they are also more interesting to tune.

Where a binary effect is the right fantasy and should be kept, it needs a second clause that lands on an immune target. Less elegant than one clause, and honest about the game having two modes.

Three checks for any rewritten talent:

1. Does it change how you play, rather than what you are effective against?
2. Does it land in both modes with the game as it currently is, no gear assumed?
3. If it carries a binary clause, does it have a graded fallback?

Applied to the audit, this is a smaller cleanup than expected. Warrior Protection carries the most mode-locked content at three nodes. Most trees carry one or none. Notably Enhancement shaman, the flattest tree in the game at 94%, carries none at all, which means that figure is not inflated by PvP content and the tree is simply flat.

---

## 6. Worked example: Arms rebuilt

One tree, in full, to show the method produces something recognizable.

Arms is the wrong tree to rebuild first and this section survives only as a worked method. At 12 of 30 forced filler it is one of the healthier trees in the game, and that figure did not move in the classifier review. Enhancement shaman and Demonology at 28, Feral Combat at 26, and Retribution at 24 all have far stronger claims. Arms is here because it is the tree this project audited first, not because it is broken.

Row assignments below are illustrative and have not been checked against a talent calculator. Vanilla's own Arms rows do not sit where they are commonly remembered: Impale is tier 4, reachable at 17 points invested, which is the entire reason the canonical Fury build spends exactly 17 in Arms. Any build of this tree needs its gates verified before the point math means anything.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 8 points**

- *Bloodletting* (3). Critical strikes cause bleeding. The bleed does not fall off early. A bleeding target takes every third blow as though it were two enemies.
- *Poise* (5). Dodged and parried attacks refund their Rage. Overpower's cooldown resets on a dodge. You cannot be disarmed in Battle Stance. Hamstring's slow cannot be dispelled. Your rage does not decay while a target you struck recently is still alive.

**Gate 5, 10 points**

- *Concussion* (3). Thunder Clap also slows casting. It spreads Rend to targets already bleeding. It becomes usable in any stance.
- *Headlong* (2). Charge usable in combat when no enemy is within 8 yards. Charge interrupts spellcasting.
- *Tactical Mastery* (5). Swapping to Battle Stance retains your Rage. Swapping to Berserker Stance retains it. Swapping to Defensive Stance retains it. Stance swapping has no cooldown. Swapping stances reopens Overpower's window.

**Gate 10, 6 points**

- *Riposte Reading* (2). Your Overpower cannot be dodged or parried. Overpower's window opens on any miss rather than only a dodge.
- *Deep Wounds* (3). Your critical strikes cause bleeding. Refreshing carries remaining damage forward rather than overwriting. The bleed jumps to a nearby enemy on death.
- *Battle Trance* (1). Three consecutive attacks without a miss makes your next Overpower or Execute free.

**Gate 15, 8 points**

- *Sweeping Strikes* (1). Your next 5 melee attacks strike an additional nearby opponent.
- *Weapon Mastery* (5). The effect follows your equipped weapon, and swords grant a chance at an extra attack. Maces stun the target. Fists reduce the target's attack speed. Daggers allow Backstab from any angle. The effect extends to your off-hand and to Blade Flurry, cannot be avoided at full stacks, and a killing blow refreshes it.
- *Opportunist* (2). Sweeping Strikes copies your Overpower, and the copies wound as the original does. Your strikes from behind may be used from any angle.

**Gate 20, 10 points. The hybrid seat, reachable at 21 points invested**

- *Rupture Line* (3). Your Execute refreshes your bleeds. Your bleeds on a target below 20% tick twice as fast. A target dying while bleeding refunds the Rage spent on Execute.
- *Mortal Cleave* (2). *(cross-tree)* Your Cleave and Whirlwind apply Mortal Strike's healing reduction. The reduction persists for 4 seconds after the target leaves your melee range.
- *Sure Strike* (1). *(subtraction node)* Your melee attacks can no longer be dodged, parried, or miss. Your melee attacks can no longer critically strike.
- *Second Wind* (2). Your being stunned or rooted generates Rage. The second rank breaks the effect once per 30 seconds.
- *Guarded Stance* (2). *(reciprocal)* Your Overpower may be used in Defensive Stance. Your Sunder Armor applies from Mortal Strike.

**Gate 25, 9 points**

- *Crippling Grip* (3). Your Hamstring roots rather than slows. The root holds through your own damage. Every third strike you land while a target is rooted sweeps through two enemies beside it.
- *Death Sentence* (3). Execute refunds its Rage on a kill. Usable below 35% against targets you have Rent. A kill by Execute resets Overpower.
- *Unyielding* (3). Reduces the duration of stuns used against you. Reduces the duration of disarms. You continue attacking for 2 seconds after a fear begins.

**Gate 30, 1 points**

- *Mortal Strike* (1). A vicious strike that wounds, halving the healing its target receives. While the wound holds, every third strike you land sweeps through two nearby enemies and carries the wound with it. A wounded target that dies passes the wound to the nearest enemy.

<!-- END GENERATED -->

Tactical Mastery survives almost intact because it was already behavioral. Only its ranks change from numeric to discrete.
This is the row that fixes vanilla's 18-point weapon specialization block. Four nodes and 20 points collapse into one node and 5, and the choice moves from the talent panel to the weapon in your hand.

**What was deleted.** Deflection is gone. Its parry now arrives through the depth dividend.

Totals: 50 available points against vanilla's 59, across the same seven rows. That sits just under the 57 to 64 band the Class Absorption trees use, and closing the gap is a matter of adding one more node to rows 5 and 6 rather than a structural issue.

Points that buy a new button: 2, the same as vanilla. Points that buy behavior: all of them.

---

## 7. First real rebuild: Marksmanship

Arms in Section 6 shows the method on a healthy tree. This is the method applied where it is actually needed.

Marksmanship earns first place on the tiebreak rather than the raw number. At 23 of 30 forced flat and 87% flat overall it is firmly in the worst group, though the classifier review put Enhancement shaman and Demonology above it at 28. What separates it is that unlike either of those, it is its class's mandatory raid spec, so every raiding hunter in the game walks this exact path.

Vanilla Marksmanship, for reference: 14 nodes, 52 points, three behavior nodes total. Two of those three are the only active abilities in the tree.

### 7.1 The capstone problem

Trueshot Aura sits at gate 30. It grants party members within 45 yards a flat 50 attack power.

It is a flat number, it is the capstone of the tree, and it is given to other people. It is also the entire reason the spec is mandatory: guides state plainly that Beast Mastery loses Trueshot Aura and therefore hurts the whole party's damage.

So the tree's final point, the one a hunter spends 30 points climbing toward, buys somebody else a stat. That is the third failure mode and the flat-talent problem meeting at the single most visible node in the class.

Deleting it takes the hunter's raid slot. Keeping it flat breaks the rules this document sets. The resolution is to move it rather than change it: **Trueshot Aura becomes part of the depth dividend, granted automatically at 30 points in Marksmanship.** The raid keeps the aura, the hunter keeps the slot, and the capstone is freed to be something the hunter does.

That is the clearest single demonstration of what Section 5.1 is for. The dividend is not only a place to put filler. It is where a spec's obligations to other people belong, so that purchased talents can be about the player.

### 7.2 The tree

Row point totals held close to vanilla's own so the shape on screen is unchanged. Gates are the real ones from client data.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Steady Aim* (5). Arcane Shot no longer clips your Auto Shot. Multi-Shot no longer clips it either. Movement does not reset your swing timer. Aimed Shot becomes castable while moving. Auto Shot continues firing during Aimed Shot's cast.
- *Marked Quarry* (5). Hunter's Mark shows the target's health to your party. Your Auto Shots on a marked target cannot be dodged. The mark jumps to the nearest enemy on death. Marking no longer breaks Feign Death. A marked target shows on your minimap at any range.

**Gate 5, 10 points**

- *Ranger's Cadence* (5). Arcane Shot refunds its cooldown on a critical strike. Multi-Shot applies Serpent Sting to everything it hits. Arcane Shot removes one magic effect. Multi-Shot gains a fourth target. Arcane Shot and Multi-Shot stop sharing a cooldown.
- *Hawk Eye* (3). Concussive Shot and Scatter Shot gain your full ranged range. Holding position for 3 seconds extends your range further. You can fire on a marked target you cannot see.
- *Bullseye* (2). Your Hawk Eye adds range to every shot. At maximum range your shots cannot be dodged.

**Gate 10, 9 points**

- *Aimed Shot* (1). An Aimed Shot that increases ranged damage by 70.
- *Killing Instinct* (5). Your Aimed Shot refreshes Hunter's Mark. It cannot be dodged or parried. It does not break your own trap. A killing blow with it refunds its mana. It resets Scatter Shot.
- *Distracting Fire* (3). Your shots may stun. The stun cannot be resisted. Your ranged attacks lose no damage while you are moving.

**Gate 15, 10 points**

- *Venomshot* (5). Serpent Sting ticks twice as fast below 20% health. It cannot be dispelled. It spreads on death. It applies through immunities to poison. Refreshing carries remaining damage forward.
- *Ranger's Focus* (5). Standing still builds Focus stacks that empower your next Aimed Shot. Your stacks persist through one movement. They are not lost on a miss. They double during Rapid Fire. A full stack makes the next Aimed Shot instant.

**Gate 20, 10 points. The hybrid seat, reachable at 21 points invested**

- *Scatter Shot* (1). A short range shot that deals 50% wepon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used.
- *Pack Tactics* (3). *(cross-tree)* Your pet strikes alongside you. It strikes more often. Every third shot you land strikes a second target.
- *Sure Shot* (1). *(subtraction node)* Your ranged attacks can no longer miss or be resisted. Your ranged attacks can no longer critically strike.
- *Volley Discipline* (3). Your Volley may be channelled while moving. It marks everything it touches. A target already marked takes it harder.
- *Trapline* (2). *(reciprocal)* Your traps root what they catch and reach an additional enemy. Every third shot you land strikes a second target.

**Gate 25, 5 points**

- *Rapid Killing* (5). Rapid Fire's cooldown drops on a killing blow. It no longer costs mana. It extends when you critically strike. It grants your party your Auto Shot speed for 5 seconds. Using it resets Aimed Shot.

**Gate 30, 1 points**

- *Trueshot* (1). Your Aimed Shot loses its cast time entirely, but can only be fired after three consecutive Auto Shots have landed.

<!-- END GENERATED -->

Steady Aim is the important one. Shot weaving against the auto shot timer is the single most complained-about mechanical problem in the spec, to the point that hunters prefer slower weapons purely for more forgiving windows. Five ranks that dismantle that problem step by step is worth more than any damage percentage in the original tree.
Raw range moves to the dividend. Hawk Eye becomes about what range lets you do rather than how much of it you have.
*Rewritten under Section 5.7's rule.* The first draft made rank 3 read "Bestial Wrath also grants you its damage bonus," which is worth nothing to a hunter without the Beast Mastery capstone and therefore made the talent a trap for anyone who did not know the interdependency. All three ranks now work for any hunter with a pet, which is every hunter. What a Beast Mastery main gets is more out of the same three points, because their pet is doing far more of their damage.

**What was deleted.** Efficiency is deleted. Its mana reduction goes to the dividend. Improved Hunter's Mark is deleted as a flat attack power number and its node becomes Marked Quarry. Improved Arcane Shot is deleted as a cooldown number, absorbed into Ranger's Cadence. Mortal Shots is deleted entirely. Its critical strike damage goes to the dividend, which is exactly what Section 5.1 exists for. Pack Tactics is the node a Beast Mastery hunter crosses for, reachable at 21 points invested. Note the shape that actually reaches it: not 31/20, which stops at tier 4, but 30/21 or 26/25, both of which give up the Beast Mastery capstone. That is the trade, and per Section 5.6 it should be a real one. Improved Scorpid Sting is deleted rather than rewritten: reducing a target's Stamina does nothing to a raid boss, which makes it dead rather than boring, per Section 1.2. Ranged Weapon Specialization is deleted. Flat ranged damage goes to the dividend.

The aura is gone from this slot and now arrives free with depth. What replaces it converts the spec's worst mechanical friction into its payoff: Aimed Shot stops being a cast that fights the swing timer and becomes the reward for a clean rotation.

### 7.3 What the numbers look like after

52 available points across the same seven rows, against vanilla's 52. Fourteen nodes against vanilla's fourteen. Two points buy a new active ability, the same as vanilla.

Forced flat on the way to the capstone: zero, because there are no flat nodes left to force. Vanilla's figure is 23 of 30.

Deleted rather than rewritten: Improved Scorpid Sting. Deleted and returned as dividend: Efficiency, Improved Hunter's Mark, Lethal Shots, Improved Arcane Shot, Improved Serpent Sting, Mortal Shots, Barrage, Ranged Weapon Specialization, Hawk Eye's raw range, and Trueshot Aura's party attack power.

None of that changes the hunter's output by design. Section 5.1's tuning method sets the dividend coefficients to reproduce exactly what those nodes delivered to a canonical build.

And to be clear about what this does not do, per Section 22: it does not fix hunters falling off as gear scales. That is a scaling problem, it is the actual reason hunter raid slots shrink after Molten Core, and no amount of talent redesign touches it.

---

## 8. Second rebuild: Enhancement shaman

Tied with Demonology for the worst tree in the game at 28 of 30 forced flat, and the flattest tree anywhere at 94%. Nineteen of the first twenty points must buy numbers, so an Enhancement splash is very close to pure filler.

### 8.1 Two of its three real talents are permissions

Vanilla Enhancement has 16 nodes and 52 points. Three nodes buy behavior. Read them:

- *Two-Handed Axes and Maces.* Allows you to use two-handed axes and maces.
- *Parry.* Gives a chance to parry enemy melee attacks.
- *Stormstrike.* The capstone.

Two of the three are not talents. They are permissions to do things other melee classes do without asking. A warrior parries at level one. Spending a talent point to be allowed to hold a two-handed axe is the clearest statement in the game that a tree has nothing to sell you.

**Both should be baseline, and the two points they occupied do not come back as talents.** A permission converted into a talent is still a permission; it just costs more. Enhancement gets two-handers and parry for free, and the tree is rebuilt at 50 available points rather than 52.

The dead node sweep in Section 1.2 found almost nothing across 27 trees. This is the closest thing to a second finding: not nodes that do nothing, but nodes that undo an artificial restriction. Worth checking the other trees for the same shape.

### 8.2 What the tree should be about

The grievance record says shamans are called totem bots, and that the argument about it is unusually well matched on both sides. One position is that existing to make other people parse well is not engaging. The other is that reading what the group needs, weaving Earthbind for a runner, dropping Tremor before a fear lands, and reassessing which air totem is correct is real decision-making.

Both are right, and the disagreement points at the fix. The decisions exist. What is missing is any talent that engages with them. Sixteen nodes and not one of them is about totem play.

So the rebuilt tree is about three things Enhancement actually does and vanilla never talents: Windfury proc manipulation, totem handling, and shock weaving.

### 8.3 The tree

Gates are the real ones. Row totals held near vanilla's own, minus the two permission points.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Stormbringer* (5). Windfury can proc from an extra attack once per swing. Its proc rate stops scaling down with weapon speed. A proc refreshes your weapon imbue duration. Two procs in a row make your next Shock free. A proc grants a stack that increases the next one's damage.
- *Totemic Focus* (5). Dropping a totem no longer resets your swing timer. Your totems inherit your weapon imbue's element. A totem destroyed by an enemy refunds its mana. You may drop two totems on one global cooldown. Your buff totems follow you within 20 yards.

**Gate 5, 12 points**

- *Elemental Cadence* (5). Earth Shock leaves the Flame and Frost Shock cooldown alone. A Shock within 3 seconds of a Windfury proc costs no mana. Frost Shock also slows attack speed. Your Flame Shock spreads to a second target on your next proc. Shocks no longer clip your swing.
- *Charged* (3). Lightning Shield orbs are consumed by your attacks as well as by being hit. Losing an orb refunds mana. At full orbs your next Shock chains to a second target.
- *Guardian Totems* (2). Stoneskin also shortens movement-impairing effects. Windwall reflects one ranged attack every 10 seconds.
- *Improved Ghost Wolf* (2). Ghost Wolf is instant and may be entered in combat. It sheds movement-impairing effects on the shift.

**Gate 10, 8 points**

- *Weapon Mastery* (5). Your equipped weapon determines the effect: swords grant a chance at an extra attack, maces stun, fists reduce the target's attack speed, and daggers allow Backstab from any angle. The effect also applies to your off-hand. It triggers from Blade Flurry. At full stacks it cannot be avoided. A killing blow refreshes it.
- *Enhancing Totems* (3). Strength of Earth and Grace of Air persist for 10 seconds after leaving their radius. They scale with your weapon imbue. Recasting one does not clear its buff from anyone still in range.

**Gate 15, 10 points**

- *Static Charge* (5). Your critical strikes add an orb to Lightning Shield. Orbs beyond maximum become damage. Crits refresh your weapon imbue. At full orbs a crit discharges one at a nearby enemy. A crit within 3 seconds of a Windfury proc grants another proc.
- *Ancestral Guidance* (5). Healing Wave no longer stops your swing. Your Lesser Healing Wave may be cast while moving. Healing a target grants them your Lightning Shield's next discharge. Your heals generate no threat while a totem of yours is active. Overhealing becomes attack power for 6 seconds.

**Gate 20, 10 points. The hybrid seat, reachable at 21 points invested**

- *Elemental Weapons* (3). *(cross-tree)* Your weapon imbues add spell damage as well as their own effect. Flame and Frost Shock scale with it. Lightning Bolt may be cast without stopping your swing.
- *Improved Weapon Totems* (4). Your Windfury Totem also grants its attack power to you while you are within range of it. Its proc can trigger from an extra attack. Your Flametongue Totem applies your weapon imbue to the party. A totem you drop refreshes the imbue on everyone in range.
- *Earthbound* (1). *(subtraction node)* Your totems become immune to damage and last twice as long. You may have only one totem active at a time.
- *Ancestral Strength* (2). *(reciprocal)* Your Healing Wave may be cast without stopping your swing. A heal you cast refreshes your weapon imbue.

**Gate 25, 5 points**

- *Windfury Mastery* (5). Windfury's extra attacks use your main hand's full damage. They can critically strike. They generate no threat. They refresh Flame Shock. A proc during Stormstrike's window adds a third attack.

**Gate 30, 1 points**

- *Stormstrike* (1). Gives you an extra attack. In addition, the next 2 sources of Nature damage dealt to the target are increased by 20%. Lasts 12 sec.

<!-- END GENERATED -->

The last rank of Totemic Focus is the single highest-value line in this rebuild. Recasting long-duration buff totems every time a raid advances is the specific thing players complain about, the suggestion has been circulating in the community for years, and it costs one talent.

**What was deleted.** Ancestral Knowledge and Shield Specialization are deleted, their mana and block returned as dividend. Thundering Strikes and Improved Lightning Shield are deleted, crit and orb damage returned as dividend. Anticipation is deleted, dodge returned as dividend. The two permission nodes are gone. Flurry and Toughness are deleted, haste and armor returned as dividend. Static Charge is what replaces Flurry: the crit-driven feedback loop stays, but it feeds a mechanic instead of a percentage.

### 8.4 After

50 available points across seven tiers against vanilla's 52, with two points returned to baseline as permissions. Sixteen nodes against vanilla's sixteen. One point buys a new active ability, against vanilla's one.

Forced flat to the capstone: zero. Vanilla's figure is 28 of 30, and 19 of 20 to the hybrid seat.

Deleted and returned as dividend: Ancestral Knowledge, Shield Specialization, Thundering Strikes, Improved Lightning Shield, Anticipation, Flurry, Toughness, Weapon Mastery's raw damage. Returned to baseline: Two-Handed Axes and Maces, Parry.

What this does not fix, per Section 10: Enhancement's raid slot still exists because of Windfury Totem rather than because of the shaman holding it. Improved Weapon Totems now at least lets the shaman benefit from the totem they are carrying for everyone else, which is a small correction to the third failure mode rather than a solution to it.

---

## 9. Third rebuild: Demonology

Tied with Enhancement for the worst tree in the game at 28 of 30 forced flat. Unlike Enhancement, this one also fails at the thing it is named after.

### 9.1 The tree does not believe in demons

Fifty-two points across 17 nodes. Thirty-eight of those points are percentages applied to a pet: Improved Imp, Improved Voidwalker, Improved Succubus, Fel Intellect, Fel Stamina, Unholy Power, Demonic Embrace. Another six are applied to consumable stones, which have nothing to do with demons at all. Improved Spellstone sits at gate 30, alongside the capstone, and increases the amount of damage a stone absorbs.

Not one node in the tree is about commanding a demon. Which one you summon, when you swap, what you tell it to do, and what you give up to keep it are all decisions a warlock makes constantly, and the tree that is supposedly about the demon has nothing to say about any of them.

Then the finding from the audit, which is worth restating because it is the sharpest single fact in this document. Nobody specs deep Demonology. The two canonical raid builds are SM/Ruin and DS/Ruin, and DS/Ruin takes exactly 21 points here to reach Demonic Sacrifice at gate 20, **a talent that kills the demon in exchange for a damage buff.**

The tree's most-used talent deletes the thing the tree is about. That is not a flatness problem, it is a premise failure, and no amount of rank rewriting fixes it. The rebuild has to give the tree a reason to exist first.

### 9.2 The thesis

Demonology is about which demon you have and when you change it, not about how much stat each demon carries.

Vanilla already gestures at this twice and develops neither. Fel Domination makes a summon instant, which is only interesting if swapping mid-fight is a thing you do. Master Demonologist gives a different effect per demon, which is the one node in the tree that treats the four demons as different rather than as one pet with different art.

Everything below builds on those two.

### 9.3 The tree

Gates are the real ones. Improved Spellstone is deleted outright rather than rewritten, so the tree rebuilds at 50 points.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Bound Servant* (5). Your demon inherits your resistances. It inherits your armor as well. A demon that dies returns after a minute at 30% health. The wait shortens to thirty seconds. Summoning costs no shard.
- *Familiar* (3). Your Imp's Firebolt applies Corruption. Your Voidwalker's Torment scales with your spell power. Your demon's attacks benefit from your own hit chance.
- *Soulcraft* (2). Healthstones can be used while silenced. Creating one below 30% health costs no shard.

**Gate 5, 10 points**

- *Soul Tether* (5). Health Funnel channels while you cast. Your demon's damage returns health to you. A demon at full health funnels back to you instead. Your Health Funnel on a full demon becomes damage against its target. Your demon's regeneration applies to you while it is idle.
- *Demonic Resilience* (3). Your demon takes reduced damage from area effects. It cannot be feared. When it attacks, it breaks roots on you.
- *Guardian* (2). Voidwalker's Sacrifice absorbs based on your health rather than the Voidwalker's. Consuming Shadows can be cast on you.

**Gate 10, 9 points**

- *Fel Domination* (1). Your next Imp, Voidwalker, Succubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its mana cost reduced by 50%.
- *Swift Binding* (5). Fel Domination's cooldown drops. It applies to Enslave Demon. A demon summoned under it arrives at full health. Swapping demons carries your active buffs across. Fel Domination holds two charges.
- *Cruelty* (3). Succubus's Lash of Pain reduces healing received. Felhunter's Spell Lock silences longer against a target mid-cast. Imp's Fire Shield reflects to a second attacker.

**Gate 15, 7 points**

- *Master Summoner* (2). Summoning is instant if your previous demon died within 10 seconds. Summoning does not break your current cast.
- *Demonic Empowerment* (5). Your Imp gains a command you can trigger. It becomes a charge you spend. The Voidwalker gains one and taunts. The Succubus gains one and breaks a caster. The Felhunter gains one and drains.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Demonic Sacrifice* (1). Sacrificing your demon grants you an effect that holds for the rest of the encounter, shaped by which demon you spent. Summoning another ends it.
- *Shadow Bond* (3). *(cross-tree)* Your demon's damage benefits from your curses. Your Corruption refreshes on any target your demon damages. Your demon's critical strikes extend Siphon Life.
- *Ashen Pact* (3). *(cross-tree)* Your demon's attacks apply your Immolate's fire damage. Your Conflagrate does not consume Immolate while your demon is on the target. Searing Pain from you draws no threat if your demon is attacking.
- *Unbound* (1). *(subtraction node)* You may have two demons active at once. Neither may be sacrificed, and both answer your commands.

**Gate 25, 5 points**

- *Master Demonologist* (5). Your demon grows stronger the longer it stands beside you. The bonus builds twice as fast. It persists through your demon's death. Your demon's threat is reduced. It draws no threat of its own.

**Gate 30, 1 points**

- *Soul Link* (1). Links you with your demon so that 30% of damage dealt to you is instead taken by it. Lasts as long as your demon lives and persists through your death.

<!-- END GENERATED -->

Swift Binding is where the thesis lands. Five ranks that make swapping demons mid-fight fast, cheap, and lossless turn a pre-fight checkbox into a live decision, and none of them is a number.
Demonic Empowerment is the node that answers "the demon just autoattacks." Four demons, four buttons, and which one you brought now decides what you can do rather than what percentage you get.
Unbound is the deliberate answer to 9.1. The tree whose signature talent deletes your demon now also offers a talent that gives you a second one, at a real cost, and the two sit in the same tier so the choice is explicit.

**What was deleted.** Demonic Embrace and Improved Imp are deleted, stamina and Imp damage returned as dividend. Fel Intellect is deleted, pet mana returned as dividend. Fel Stamina is deleted. Improved Succubus becomes part of Cruelty. Unholy Power is deleted, pet damage returned as dividend. Improved Enslave Demon and Improved Firestone are deleted.

### 9.4 After

50 available points across seven tiers against vanilla's 52. Sixteen nodes against seventeen. Forced flat to the capstone: zero, against vanilla's 28 of 30.

Deleted and returned as dividend: Demonic Embrace, Improved Imp, Fel Intellect, Fel Stamina, Unholy Power. Deleted outright: Improved Spellstone, Improved Firestone, Improved Enslave Demon.

The test the rebuild has to pass is not the floor figure. It is whether a warlock would now spend 26 points here on purpose. The old tree's answer was no, and the proof is that the two builds everyone runs either skip it entirely or dip in exactly far enough to kill the demon.

---

## 10. Fourth rebuild: Feral Combat

Twenty-six of thirty forced flat, and a hybrid seat figure of 19 of 20 that is the worst in the game.

### 10.1 Two roles, and the smallest tree in the game

Forty-five points, tied with Holy and Retribution paladin for the least content anywhere. Combat rogue carries 62 for one role. Feral carries 45 for two, because bear tanking and cat damage share a tree.

That is roughly twenty points of relevant content per role, and it is the structural reason the tree feels thin from either side. **The rebuild grows it to 55, and the growth is the finding rather than a liberty taken.** A tree serving two roles at 72% of the size of a tree serving one is underinvested, and no amount of rewriting fixes a shortage of nodes.

Gate 20 holds three points in vanilla: Faerie Fire in forms, and two ranks of Savage Fury. That is why reaching the hybrid seat costs 19 flat points out of 20. The seat is not badly designed, it is nearly empty.

### 10.2 The undocumented technique

The grievance record notes that feral damage depends on power-shifting, dropping cat form and re-entering it to trigger Furor's energy. The interface does not teach it, no tooltip describes it, and it is mandatory.

A spec whose optimal play is a community discovery is a design failure regardless of its numbers, and it is exactly the kind of thing this project's method says to fix: the game already does this, so let the game say so. The rebuilt tree makes shifting an explicit subject with its own node rather than an exploit that happens to work.

### 10.3 The tree

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Savage Instinct* (5). Shifting no longer resets your swing timer. Combo points persist 10 seconds after leaving cat form. Shifting clears movement-impairing effects. You may shift while stunned once every 30 seconds. Returning to a form you left within 6 seconds costs no mana.
- *Feral Aggression* (5). Demoralizing Roar also reduces armor. It applies behind you. It cannot be dispelled. It refreshes your bleeds on everything it hits. A target that resists it takes bleed damage instead.

**Gate 5, 12 points**

- *Bloodletting* (5). Your critical strikes cause bleeding. The bleed does not fall off early. A bleeding target takes every fifth blow as though it were two enemies. The interval tightens to every fourth blow. It tightens to every third.
- *Menace* (5). Your Swipe generates threat on targets it misses. Maul's threat applies within 5 yards. Your threat does not decay in bear form. Taunt has no cooldown against a target already on you. Your damage taken in bear form generates threat.
- *Brutal Impact* (2). Bash and Pounce interrupt regardless of stun immunity. Your Pounce reaches 15 yards from Prowl.

**Gate 10, 9 points**

- *Feral Charge* (1). You charge an enemy, rooting it and cutting off whatever it was casting. It may be used in combat and while rooted yourself.
- *Stalker* (2). Prowl loses its movement penalty. You may Prowl in combat once every 60 seconds.
- *Rend and Tear* (3). Shred works from the front against a bleeding target. Your Shred refreshes Rake. A critical Shred reduces Ferocious Bite's cost.
- *Primal Fury* (3). Your critical strikes grant an extra combo point. Crits in bear form grant rage. A crit at 5 combo points refunds the finisher.

**Gate 15, 10 points**

- *Blood Frenzy* (2). Your critical strikes with Claw grant an additional combo point. This extends to all Cat Form abilities that add combo points.
- *Opportunist* (2). Your Shred refreshes Rake's duration. Your strikes from behind may be used from any angle.
- *Wild Aspect* (3). Cat abilities benefit from your bear armor. Bear abilities benefit from your cat critical strike chance. One active buff carries across a shift.
- *Savage Fury* (3). Claw and Rake apply a bleed. Maul and Swipe reduce the target's armor. All four cost less energy or rage while the target is losing blood.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Faerie Fire (Feral)* (1). Decrease the armor of the target by 175 for 40 sec. While affected, the target cannot stealth or turn invisible.
- *Nature's Grip* (3). *(cross-tree)* Your Entangling Roots may be cast in form. Your Moonfire may be cast in form at reduced damage. Your bleeds scale with your spell critical strike chance.
- *Wildheart* (3). *(cross-tree)* Your Healing Touch may be cast in form. Your heals in form cost rage or energy instead of mana. Overhealing becomes attack power for 6 seconds.
- *Unshifted* (1). *(subtraction node)* You may cast any spell while in form. Your form's armor and attack power bonuses are halved.

**Gate 25, 5 points**

- *Heart of the Wild* (5). In Bear Form your health scales with your Intellect. In Cat Form your energy regeneration scales with it as well. Your forms inherit your Intellect rather than converting it. They inherit your Spirit. They inherit all your caster statistics.

**Gate 30, 1 points**

- *Apex Predator* (1). Your combo points persist through form changes and through target changes.

<!-- END GENERATED -->

Vanilla's three-point tier becomes eight, and the two sideways nodes are what make a druid who does two things a character rather than a compromise.

**What was deleted.** Ferocity is deleted, its energy and rage cost reduction returned as dividend. The fifth rank of Savage Instinct is the power-shifting fix: the technique becomes cheap and stated rather than an undocumented mana burn. Thick Hide and Feral Instinct are deleted, armor and threat percentage returned as dividend. Menace is the tanking half of the tree finally having something to say. Feline Swiftness and Sharpened Claws are deleted, movement speed and crit returned as dividend. Predatory Strikes and Improved Shred are deleted, attack power and energy cost returned as dividend. Wild Aspect is the node that treats the two roles as one character rather than two.

Leader of the Pack moves to the depth dividend at 30 points, on exactly the reasoning applied to Trueshot Aura in Section 7.1. It is a flat aura given to other people sitting in the capstone slot, and the capstone should buy the druid something.

**Note.** That is the third capstone in this document to be a party buff, after Trueshot Aura and alongside Sanctity Aura in Retribution. The rule, in its final form after Discipline forced a distinction in Section 13.1: **a passive aura never belongs at a capstone, because it is an obligation rather than a reward. An active cooldown aimed at an ally does, because choosing when and on whom to spend it is a decision.** Trueshot Aura, Leader of the Pack, and Sanctity Aura move to the dividend. Power Infusion and Innervate stay where they are.

### 10.4 After

55 points against vanilla's 45, the growth justified by two roles in one tree. Sixteen nodes. Forced flat to the capstone: zero, against 26 of 30. Hybrid seat: zero against 19 of 20.

---

## 11. Fifth rebuild: Retribution

Twenty-four of thirty forced flat, 84% flat overall, and the only tree in this document whose worst problem is not in the tree.

### 11.1 The rotation is empty on purpose

Guides describe Retribution as running on auto attacks and passive procs, and then defend that emptiness on the grounds that it leaves the paladin free to distribute blessings. The spec has nothing to press because its actual job is buff maintenance, and forty raid members need rebuffing every five minutes.

So the tree being 84% numbers is the second problem. The first is that the paladin has no room to use anything anyway.

That points the rebuild somewhere unusual. **The most valuable thing this tree can buy is time.** A talent that cuts blessing overhead does more for how Retribution feels to play than any damage node, because it converts a spec that cannot afford a rotation into one that can.

### 11.2 The tree

Vanilla row totals are 10/10/11/4/4/5/1. Gates 15 and 20 hold four points each, which is why the middle of this tree feels like a corridor. The rebuild redistributes toward the middle and grows to 52, matching Enhancement and Marksmanship rather than staying at the 45 shared with Feral and Holy paladin.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Sanctified Blessings* (5). Greater Blessings last twice as long. They may be cast on any raid member rather than only your party. Recasting one does not clear it from others. They persist through the target's death. One cast applies to an entire party.
- *Crusader's Word* (5). Your Blessing of Might also grants you its attack power. Blessing of Wisdom returns mana on your critical strikes. Your Blessing of Freedom may be cast on yourself while stunned. Blessing of Sacrifice transfers threat as well as damage. A blessing you cast refreshes your current Seal.

**Gate 5, 10 points**

- *Seal Mastery* (5). Your Seal persists through weapon swaps. Judging does not consume it. A Seal refreshes when you Judge. Two Seals may be active at once. Your Seal applies to your first attack after leaving combat.
- *Improved Judgement* (3). Judgement's cooldown drops. It may be cast while moving. It applies your Seal to a second nearby target.
- *Vindication* (2). Your melee strikes weaken what they hit, reducing the damage it deals. The weakness stacks and cannot be dispelled.

**Gate 10, 11 points**

- *Seal of Command* (1). Your Seal strikes a second time for Holy damage. The second strike carries your Judgement. It cannot be dodged.
- *Righteous Fury* (5). Consecration ticks faster on targets you have Judged. Your holy damage you deal refreshes Judgement. Your Judgement debuff cannot be overwritten by another paladin. Judging a target already Judged by you extends both. Consecration follows you for its first 3 seconds.
- *Pursuit of Justice* (2). You cannot be slowed below your base speed, mounted or otherwise. You close faster on a target you have Judged.
- *Eye for an Eye* (3). Spell criticals against you return damage to the caster. The return cannot be resisted. It ignores absorption.

**Gate 15, 10 points**

- *Vengeance* (5). A critical strike opens a window. Inside it your next Judgement is free. Consecration costs no mana. The window extends on each critical. It may be opened by your Seal's proc rather than only by your own critical.
- *Zeal* (5). Your critical strikes with a two-handed weapon apply a healing reduction. Slow weapons make Seal of Command proc harder. Your first attack from more than 8 yards cannot be dodged or parried. It cannot miss. Judgement resets your swing timer favourably.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Hammer of Wrath* (1). Instantly hurls a hammer at a target below 20% health, dealing Holy damage. Usable in any Seal and off the global cooldown.
- *Sanctified Light* (3). *(cross-tree)* Your Holy Light and Flash of Light may be cast while your Seal is active without breaking it. Your heals extend your Judgement. Healing a target below 30% refreshes your Seal.
- *Bulwark of Faith* (3). *(cross-tree)* Blessing of Sanctuary's block damage scales with your attack power. Your Holy Shield may be maintained while a two-handed weapon is equipped. Your damage you block refreshes your Seal.
- *Zealotry* (1). *(subtraction node)* Your Seals never expire and cannot be dispelled. You may no longer benefit from any blessing cast by another paladin. Sanctity Aura moves to the depth dividend at 20 points, on the same reasoning as Trueshot Aura and Leader of the Pack.

**Gate 25, 5 points**

- *Crusade* (5). Your Judgement applies to everything your Consecration touches. Seal of Command chains to a second target. Your judging refreshes every blessing you have cast on your party. Your Seal procs cannot be resisted. A Judgement that kills its target has no cooldown.

**Gate 30, 1 points**

- *Repentance* (1). Puts an enemy into a penitent trance for six seconds, ending on any damage. Against an enemy immune to incapacitation it instead removes one enrage or haste effect and prevents another for the duration. Two minute cooldown.

<!-- END GENERATED -->

**What was deleted.** Benediction and Improved Blessing of Might are deleted, mana cost and attack power returned as dividend. Sanctified Blessings is the point of the rebuild: five ranks that hand the paladin back the global cooldowns their rotation was traded away for. Deflection and Improved Seal of the Crusader are deleted, parry and attack power returned as dividend. Seal Mastery makes seals a system rather than a pre-pull toggle. Conviction is deleted, critical strike chance returned as dividend. Improved Retribution Aura and Two-Handed Weapon Specialization are deleted. Sanctity Aura moves to the depth dividend at 20 points, on the same reasoning as Trueshot Aura and Leader of the Pack. Improved Enslave-style filler is gone.

### 11.3 After

52 points against vanilla's 45. Sixteen nodes against fifteen. Forced flat to the capstone: zero, against 24 of 30.

What this does not fix, and it is the important part: Retribution's raid damage. The rebuild gives the spec a rotation it can actually run and hands back the global cooldowns that blessing maintenance was eating, which addresses the complaint that the spec is boring. It does not address the complaint that it is weak, and per Section 22 that needs the depth coefficient set deliberately under band neutrality rather than any talent in this list.

---

## 12. Sixth rebuild: Protection paladin

Twenty-three of thirty forced flat, and the only tank tree in the game whose threat comes from buffing.

### 12.1 The tree is coherent, and that is the problem

Blessing of Kings sits at gate 10, Blessing of Sanctuary at gate 20. Both are buffs cast on other people, inside a tank tree. That looks like misplacement until you read the tanking guides, which state that Greater Blessing of Kings cast on party members is roughly 95% of a protection paladin's raid threat.

So the tree is not confused. It is internally consistent with a threat model where the tank's rotation is buffing the raid. The buffs are in the tree because the buffs *are* the rotation.

That is the thing to fix, and no rank rewriting reaches it. **A protection paladin needs threat that comes from tanking.** Everything below follows from that.

One-Handed Weapon Specialization at gate 25 is the single universally dead node found by the Section 1.2 sweep: paladin melee damage never carries threat, and protection paladin has no PvP context where it would. Deleted, not rewritten.

### 12.2 The tree

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Righteous Defense* (5). Your damage you take generates threat on its source. On everything within 8 yards. Blocked damage generates double. Your threat you generate does not decay while you hold aggro. A target that switches off you takes holy damage.
- *Redoubt* (5). Blocking refreshes your Seal. Consecutive blocks raise your block value for 6 seconds. A block below 30% health grants a charge of Holy Shield. Blocking a critical strike stuns nothing but refunds mana. Blocks generate threat on the whole encounter.

**Gate 5, 10 points**

- *Guardian's Favor* (2). Blessing of Protection's cooldown drops. It may be cast on yourself while silenced.
- *Anvil* (5). Your Consecration generates threat on targets that resist it. It follows you for 3 seconds. It refreshes when you block. It applies your Judgement debuff. It cannot be outranged by a target inside its original radius.
- *Improved Righteous Fury* (3). Righteous Fury also converts healing received into threat. It persists through death. It applies to your Consecration.

**Gate 10, 12 points**

- *Blessing of Kings* (1). Your Blessing raises every attribute rather than one. It persists through death and cannot be dispelled by a player.
- *Reckoning* (5). Being critically struck grants you an extra attack. The attack carries your Seal. It generates threat as though it were a Judgement. Extra attacks bank to four. It also triggers on a block.
- *Shield Specialization* (3). Your shield's absorb applies to your party's next hit. Absorbed damage generates threat. Your block value scales with your Blessing of Sanctuary.
- *Bulwark* (3). Shield Block covers an extra attack. It may be used while stunned. It refreshes on a parry.

**Gate 15, 6 points**

- *Improved Hammer of Justice* (3). Hammer of Justice's cooldown drops. It may be cast at range. Against stun-immune targets it instead reduces their damage dealt for its duration.
- *Aura Mastery* (3). Your aura applies to the whole raid instead of your party. You may run two auras at once. Switching auras costs no global cooldown.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Blessing of Sanctuary* (1). Your Blessing turns part of the damage its target takes back on the attacker. Blocking returns more. It holds on you while you tank.
- *Hand of Light* (3). *(cross-tree)* Your Holy Light and Flash of Light generate no threat on a target you are tanking. Healing yourself refreshes Righteous Fury. Your heals scale with your block value.
- *Crusader's Resolve* (3). *(cross-tree)* Your Seal damage generates threat as though doubled. Your Seal of Command may proc from a block. Your Judgement applies to everything striking you.
- *Immovable* (1). *(subtraction node)* You cannot be moved, feared, stunned, or knocked back. Your movement speed is reduced by 30% at all times.

**Gate 25, 5 points**

- *Ardent Defender* (5). Below 35% health, damage taken is reduced. A killing blow is survived once every 3 minutes. Survival grants a full Holy Shield. It heals you for the overkill. It resets Lay on Hands.

**Gate 30, 1 points**

- *Holy Shield* (1). For a short time your blocks strike back for Holy damage and draw far more attention than the damage warrants. Each block spends a charge, and the shield holds four.

<!-- END GENERATED -->

**What was deleted.** Improved Devotion Aura is deleted, armor returned as dividend. Righteous Defense is the replacement threat engine: it scales with being hit, which is what a tank does. Precision and Toughness are deleted, hit and armor returned as dividend. Anticipation is deleted, defense skill returned as dividend. Improved Concentration Aura is deleted as mode-locked content per Section 5.8, folded into Aura Mastery. One-Handed Weapon Specialization deleted outright.

50 points, 16 nodes, forced flat zero against 23 of 30.

---

## 13. Seventh rebuild: Discipline

Twenty-three of thirty forced flat, and five of its forty-eight points buy wand damage.

### 13.1 What is in it

Wand Specialization takes five points at gate 0, over a tenth of a healing tree, to improve a weapon a raid healer fires between casts. Unbreakable Will takes five more on stun and fear resistance, which is mode-locked content per Section 5.8. Mental Strength, Force of Will, Mental Agility, Improved Inner Fire, and Improved Mana Burn are all percentages.

Two nodes give something to someone else: Divine Spirit at gate 20 and Power Infusion at gate 30.

**A refinement to the rule from Section 10.3 is needed here.** Power Infusion is an active cooldown the priest chooses when to spend and on whom. That is a decision, and decisions belong at a capstone. Trueshot Aura, Leader of the Pack, and Sanctity Aura are passive and permanent, which makes them obligations. The rule is therefore narrower than first stated: **a passive aura never belongs at a capstone. An active cooldown aimed at an ally is fine.** Power Infusion stays.

### 13.2 The tree

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Silent Resolve* (5). Your first heal on a target generates no threat. Overhealing generates none. Healing a target below 30% generates none. Your threat you would generate transfers to the tank. Your shields generate none.
- *Inner Focus* (1). Your next spell costs nothing and strikes critically more often. It cannot be interrupted.
- *Improved Power Word: Shield* (4). Your the shield does not break on your own damage. It may be cast on a target already shielded, refreshing rather than failing. Its expiry heals for what it did not absorb. A shield that absorbs its full value refunds its mana.

**Gate 5, 12 points**

- *Meditation* (3). Your mana regeneration continues while casting. It also continues for 5 sec after being interrupted. A cast completed at full mana banks a portion for later.
- *Martyrdom* (2). Being critically struck may leave you unable to be interrupted for a time. It also refunds the interrupted cast.
- *Improved Power Word: Fortitude* (2). Your fortitude applies to the raid rather than the party. It persists through death.
- *Absolution* (5). Dispel Magic removes one additional effect. It may be cast while casting. Dispelling grants the target a shield. Dispelling an enemy buff damages them. Failed dispels refund mana.

**Gate 10, 8 points**

- *Focused Will* (5). Casting is not interrupted by damage below a threshold. Pushback is capped at once per cast. A completed heal under fire grants Focused Casting. Interruption instead extends your next cast's power. You may cast while silenced once every 45 seconds.
- *Reflective Shield* (3). Power Word: Shield returns a portion of absorbed damage. The return scales with your spell damage. It applies to everything attacking the shielded target.

**Gate 15, 10 points**

- *Mental Agility* (5). Instant spells do not trigger the global cooldown when cast on a target below 20%. Your Renew may be applied to two targets. Shield and Renew share a cast. Instants refresh Inner Fire. Your next instant after a Greater Heal is free.
- *Improved Inner Fire* (2). Inner Fire is not consumed by damage. It grants spell damage as well as armor.
- *Mana Burn* (3). *(subtraction node)* Mana Burn no longer has a cast time against a target below half mana. The cast time is removed entirely. Against a target with no mana it instead deals Shadow damage equal to the amount it would have burned.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Divine Spirit* (1). Holy power infuses the target, increasing their Spirit by 17 for 30 min.
- *Grace* (3). *(cross-tree)* Your Renew benefits from your shield's absorb value. Prayer of Healing gains the same benefit. Healing a shielded target extends the shield.
- *Shadow Affinity* (3). *(cross-tree)* Your Shadow Word: Pain refreshes when you shield its target. Mind Blast generates no threat while a shield of yours is active. Your shields benefit from your shadow damage.
- *Ascetic* (1). *(subtraction node)* Healing is increased substantially. You may no longer cast Power Word: Shield. The original draft named it Vow of Silence and gave it a mana clause. This version trades the class's signature spell for throughpu.

**Gate 25, 5 points**

- *Power of the Word* (5). Your shields chain to a second target. Power Infusion's cooldown drops. Your shields cannot be dispelled. A shield that expires unspent grants a charge. A full charge makes your next Greater Heal instant.

**Gate 30, 1 points**

- *Power Infusion* (1). Infuses the target with power, increasing their spell damage and healing by 20%. Lasts 15 sec.

<!-- END GENERATED -->

Wand Specialization and Unbreakable Will are both deleted. Wand damage returns as dividend; the resistances go with the mode-locked content.
*Ascetic is the Section 5.4 example rewritten. The original draft named it Vow of Silence and gave it a mana clause; this version trades the class's signature spell for throughput, which is a harder and more interesting choice.*

**What was deleted.** Force of Will and Mental Strength are deleted, spell damage and mana returned as dividend.

52 points against 48, growth per REG-17. Forced flat zero against 23 of 30.

---

## 14. Eighth rebuild: Elemental

Twenty-three of thirty forced flat, and a gate-20 tier holding three points, the second-sparsest hybrid seat in the game after Feral.

### 14.1 A tree about one spell

Concussion, Convection, Call of Thunder, Reverberation, and Lightning Mastery all modify Lightning Bolt and Chain Lightning. Twenty-three of forty-six points make one spell cheaper, faster, harder, and more likely to crit.

Three more, Call of Flame, Earth's Grasp, and Improved Fire Totems, modify totems nobody drops. That is the same totem neglect found in Enhancement, from the other direction: Enhancement had no totem talents at all, Elemental has three that nobody takes.

The grievance record adds that Elemental runs out of mana and does not put out enough. The second is a tuning problem for the depth coefficient under band neutrality. The first is a tree problem and the tree should own it.

### 14.2 The tree

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Convection* (5). Critical strikes with Lightning Bolt restore mana. All your Nature criticals gain the refund. Your Nature spells deal increased damage for the first 10 seconds of an encounter. The effect extends to all your spells. The window extends to 20 seconds.
- *Storm Reach* (2). Your Lightning spells reach further and chain further. Every third spell you cast strikes a second enemy.
- *Elemental Warding* (3). Fire, Frost, and Nature damage taken is reduced. The reduction also applies to your totems. A resisted spell grants you a shield.

**Gate 5, 8 points**

- *Call of Flame* (3). Fire totems inherit your spell critical chance. Fire Nova arms instantly when an enemy enters its radius. Magma Totem pulses on a target that flees.
- *Earth's Grasp* (2). Stoneclaw taunts on a delay instead of instantly. Earthbind slows casting as well as movement.
- *Static Field* (3). Your Lightning Shield orbs are shared with your totems. Your totems struck discharge an orb. A discharged orb refreshes Flame Shock.

**Gate 10, 11 points**

- *Elemental Focus* (1). Casting an elemental spell may leave you Clearcast, so the next costs nothing. Clearcasting also removes its pushback.
- *Reverberation* (5). Shocks no longer share a cooldown with each other. A Shock refreshes on a critical strike. Earth Shock interrupts through immunity. Your Frost Shock's slow applies to attack speed. A Shock cast during Clearcasting costs nothing and does not consume the proc.
- *Storm Caller* (5). Your Lightning Bolt may be cast while moving at reduced damage. Your Chain Lightning cannot be resisted on its first target. A critical Lightning Bolt shortens Chain Lightning's cooldown. Overloads cannot draw threat. Chain Lightning bounces back to its origin.

**Gate 15, 8 points**

- *Elemental Devastation* (3). Your offensive spell criticals grant you melee critical strike chance. The effect stacks. It persists through a weapon swap.
- *Eye of the Storm* (3). Being struck while casting may leave you unable to be interrupted for a time. Any strike triggers it. It also refunds the interrupted cast.
- *Improved Fire Totems* (2). Fire Nova's delay is removed entirely. A Fire totem that dies detonates.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Elemental Fury* (1). Your fire totems strike harder and their criticals hit for double. A totem that dies discharges its remaining damage.
- *Stormstrike Affinity* (3). *(cross-tree)* Your Flame and Frost Shock scale with your attack power as well as your spell damage. Your weapon imbue adds to your spell damage. Melee critical strikes grant Clearcasting.
- *Tidal Mastery* (3). *(cross-tree)* Your Chain Lightning's jump logic applies to Chain Heal. Healing a target grants them your next Lightning Shield discharge. Your clearcasting applies to your heals.
- *Grounded* (1). *(subtraction node)* Your spells cannot be resisted or interrupted. You may no longer critically strike with them.

**Gate 25, 5 points**

- *Lightning Mastery* (5). Your Lightning Bolt gains a chance to overload and cast a free second copy. Overloads can chain. They apply Flame Shock. Chain Lightning can overload. An overload refunds the original spell's mana.

**Gate 30, 1 points**

- *Elemental Mastery* (1). Your next elemental spell is a guaranteed critical and costs nothing. Its cooldown returns on a killing blow.

<!-- END GENERATED -->

Vanilla's three-point tier becomes eight, matching the Feral fix.

**What was deleted.** Concussion is deleted, spell damage returned as dividend. Call of Thunder is deleted, critical strike chance returned as dividend.

50 points against 46. Forced flat zero against 23 of 30.

---

## 15. Ninth rebuild: Holy priest

Twenty of thirty forced flat, and the tree with the best-documented complaint in the whole audit.

### 15.1 Built for a game the encounters do not run

A vanilla-era forum post, quoted in the grievance record, says the holy tree is mostly worthless because in Molten Core you are not casting Greater Heal, Heal, or Prayer of Healing, so every talent buffing them is wasted.

The tree confirms it. Improved Healing takes three points on the mana cost of Lesser Heal, Heal, and Greater Heal. Improved Prayer of Healing takes two more on a spell raid healers rarely cast. Divine Fury spends five on cast time for Greater Heal alongside two damage spells.

Then the second problem, which is the mirror of Discipline's wand node. Divine Fury, Holy Reach, and Searing Light spend nine points improving Smite and Holy Fire, offensive spells inside the tree a raid healer specialises into.

And the capstone is Lightwell, which asks other players to click a well and which they famously do not.

So roughly a fifth of the tree buffs spells raids do not cast, another fifth buffs spells a healer does not cast, and the capstone depends on other people doing something they will not do. **This tree does not need rank rewriting. It needs its subject changed from specific spells to healing behavior**, so that a shift in encounter design cannot strand it again.

### 15.2 The tree

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Healing Focus* (2). Your healing spells may resist interruption from damage. They resist it entirely while you are below half health.
- *Renewal* (5). Renew ticks once immediately. A target at full health banks the tick. Renew's remaining duration is added when refreshed. Renew on a target below 30% heals double and ends. Your Renew spreads to a nearby ally when its target dies.
- *Holy Concentration* (3). Your critical heals refund mana. Reduce your next heal's cast time. Grant the target 10% of the overheal as a shield.

**Gate 5, 10 points**

- *Attunement* (5). Your talents scale with what a heal does, not with which heal it is. Any heal cast on a target below 50% is faster. Any heal that lands on a target at full health becomes a shield. Any overheal is banked toward your next cast. Any heal may spend the bank.
- *Spell Warding* (5). Reduces Fire damage taken. Reduces Frost damage taken. Reduces Shadow damage taken. While a Renew of yours is active on you it also reduces Physical damage taken. Any heal of yours active on you maintains the Physical reduction.

**Gate 10, 7 points**

- *Holy Nova* (1). Causes an explosion of holy light around the caster, causing 29 to 34 Holy damageto all enemy targets within 10 yards and healing all party members within 10 yards for 54 to 63. These effects cause no threat.
- *Blessed Recovery* (3). After a critical hit you heal over 6 sec. The heal cannot be interrupted. It also triggers on a block.
- *Inspiration* (3). A critical heal grants the target armor. It also grants damage reduction. The effect applies to everyone the heal touched.

**Gate 15, 7 points**

- *Circle of Healing* (1). Heals all party members within 15 yards for a moderate amount. It cannot be overhealed and prefers the lowest-health target.
- *Improved Healing* (3). Your area heals prioritise the lowest-health target. They cannot overheal. They refund mana per target already at full health.
- *Holy Reach* (3). Your heals reach further. Your area heals apply to anyone within your Holy Nova radius. Range no longer reduces their effect.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Spirit of Redemption* (1). Upon death, the priest becomes the Spirit of Redemption for 10 sec. Your the Spirit of Redemption cannot move, attack, be attacked or targeted any spells or effects. While in this form the priest can cast any healing spell free of cost. When the effect ends, the pri.
- *Spiritual Guidance* (3). Your spell damage and healing scale with your Spirit. Spirit also reduces your heals' mana cost. Spirit continues to regenerate mana while casting.
- *Empowered Shield* (3). *(cross-tree)* Your heals on a shielded target extend the shield. A shield that breaks while you are casting refunds its mana. Power Word: Shield benefits from your healing bonus.
- *Martyr* (1). *(subtraction node)* Healing is increased while you are below 50% health. You may no longer heal yourself.

**Gate 25, 5 points**

- *Spiritual Healing* (5). Your heals on a target you have healed in the last 6 seconds chain to a second ally. The chain carries Renew. It cannot overheal. It prefers a target with no heal-over-time active. A full chain refunds a portion of the cast.

**Gate 30, 1 points**

- *Guardian Spirit* (1). Place a spirit on an ally that heals them over 10 sec and once prevents a killing blow. Three minute cooldown.

<!-- END GENERATED -->

**What was deleted.** Holy Specialization and Improved Renew are deleted, critical chance and Renew percentage returned as dividend. Divine Fury is deleted. Smite and Holy Fire content leaves the tree entirely; a raid healer's tree should not be paying for damage spells. Searing Light is deleted. Improved Prayer of Healing is deleted.

52 points against 48. Forced flat zero against 20 of 30.

---

## 16. Tenth rebuild: Balance

Nineteen of thirty forced flat, and a gate-5 tier holding sixteen points against a gate-20 tier holding four.

### 16.1 Three spells and a sparse middle

Improved Wrath, Improved Moonfire, Improved Starfire, Vengeance, Moonfury, and Moonglow spend twenty-eight of fifty-two points modifying Wrath, Starfire, and Moonfire. That is the Elemental disease with three spells instead of two.

The distribution is the other problem. Sixteen points sit at gate 5 and four at gate 20, so the tree front-loads its content and then thins out exactly where the hybrid seat is. Third tree in this document with a near-empty gate 20, after Feral at three and Elemental at three.

**One thing here works and is worth protecting.** Omen of Clarity at gate 10 is the most-splashed talent in the class: feral druids spend points in Balance specifically to reach it, which is a functioning cross-tree draw that arose without anyone designing one. Section 5.3's hybrid seat is trying to produce deliberately what Omen of Clarity produces by accident, and it should not be disturbed.

Moonkin Form is a capstone carrying a party spell critical aura. Per the rule in Section 13.1, the form stays because transforming is a real capstone and changes how you play; **the aura portion moves to the depth dividend**, as with Trueshot Aura.

### 16.2 The tree

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Gate 0, 10 points**

- *Nature's Grasp* (1). Nature's Grasp roots attackers and cannot be resisted. While it holds, your Nature spells reach a second target.
- *Starlight* (5). Your Starfire deals more damage. Wrath deals more damage as well. Starfire cannot be resisted. Wrath is instant below 10% target health. The threshold rises to 20%.
- *Improved Nature's Grasp* (4). Nature's Grasp cannot be resisted. It holds through your own damage. While you are moving your Nature spells lose no damage. This extends to all your spells.

**Gate 5, 10 points**

- *Moonfire* (5). Moonfire's periodic damage refreshes when you cast Starfire. A critical Moonfire extends its duration. It spreads to a second target on the target's death. It may be cast while shapeshifted. Its initial damage scales with time remaining on the previous application.
- *Improved Entangling Roots* (3). Entangling Roots cannot be interrupted by damage. It may be cast while shapeshifted. Its root does not break on your Moonfire.
- *Natural Shapeshifter* (2). Shifting costs less and may be done while rooted. For the first twenty seconds of an encounter your spells deal increased damage.

**Gate 10, 8 points**

- *Omen of Clarity* (1). Your damage and healing spells have a chance to grant Clearcasting, making the next spell of any school free.
- *Nature's Reach* (2). Your Balance spells reach further, and at maximum range they ignore line of sight. Moonfire cast at range does not break your own crowd control.
- *Improved Thorns* (3). Your Thorns damage generates no threat. It applies to your party. It refreshes when its target is critically hit.
- *Celestial Focus* (2). Starfire's pushback is halved. A critical Starfire cannot be pushed back at all.

**Gate 15, 10 points**

- *Improved Starfire* (5). Starfire stuns the first target it strikes. Against stun-immune targets it instead reduces their damage dealt. Starfire's cast cannot be pushed back. A killing blow with Starfire resets it. Starfire applies Moonfire.
- *Vengeance* (5). A critical strike increases the range of your next spell. It also grants Clearcasting. Your critical strikes cannot be resisted. Two criticals in a row make your next Starfire instant. A critical Moonfire tick counts toward the chain.

**Gate 20, 8 points. The hybrid seat, reachable at 21 points invested**

- *Nature's Grace* (1). All spell criticals grace you with the blessing of nature, reducing the casting time of your next spell by 0.5 sec.
- *Moonglow* (2). Your Balance and healing spells cost less. A spell that critically strikes costs nothing at all.
- *Wild Growth* (3). *(cross-tree)* Your Rejuvenation and Regrowth benefit from your spell critical chance. Healing a target grants them your next Moonfire's damage as absorb. Nature's Swiftness also affects Starfire.
- *Eclipse* (1). *(cross-tree)* Your bleeds in cat and bear form scale with your spell damage.
- *Solstice* (1). *(subtraction node)* Your Starfire and Wrath deal substantially more damage. You may no longer shapeshift.

**Gate 25, 5 points**

- *Moonfury* (5). Casting Starfire empowers your next Wrath. Casting Wrath empowers your next Starfire as well. The bonus persists through a Moonfire. It doubles at full stacks. It applies to Hurricane.

**Gate 30, 1 points**

- *Moonkin Form* (1). Transforms you into Moonkin Form. While in this form your armor from items is increased and your spell critical strikes restore mana. Your party's spell critical strike aura is granted by depth in this tree rather than by this talent.

<!-- END GENERATED -->

Vanilla's four-point tier becomes eight. Solstice is the druid trade stated plainly: commit to being a caster and give up the flexibility that defines the class.

**What was deleted.** Improved Wrath is deleted, cast time returned as dividend. Natural Weapons is deleted, physical damage in forms returned as dividend. Vanilla's sixteen-point tier becomes ten, and the six points move down to where the tree was starving.

52 points, unchanged. Forced flat zero against 19 of 30.

---

## 17. The 18-band, rebuilt

Five trees at 18 of 30 forced flat. None is severe, all share a shape: a spine of real mechanics buried under stat modifiers to the same handful of abilities. The method from Sections 7 through 16 applies without modification, so these are recorded more briefly.

### 17.1 Beast Mastery

Eleven of sixteen nodes are pet statistics: health, armor, damage, critical strike, focus regeneration, movement speed. Demonology's disease, one class over, and with the same consequence: the four pet families are one pet with different art.

The spine that survives is Frenzy, Intimidation, Spirit Bond, and Bestial Wrath, all of which are about the pet doing something rather than having more of something.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Improved Aspect of the Hawk* (5). Aspect of the Hawk's ranged haste triggers on any shot rather than only on auto shot. It cannot be dispelled. Swapping aspects does not clear it. It persists 6 sec after swapping. Two aspects may be active at once. *Kindred* (5). Your pet inherits your resistances. Your critical strike chance. Your Hunter's Mark bonus. It holds threat through your Feign Death. It attacks a target you Scatter Shot without breaking it.
- **Gate 5, 12.** *Improved Revive Pet* (2). Reviving your pet is instant, costs no mana, and may be done in combat. A pet revived this way returns at full health. *Pack Leader* (5). Your pet's family ability gains a second effect that differs by family. The ability costs no focus while your pet holds aggro. It may be used while your pet is moving. It triggers automatically when your pet is critically hit. It applies your Hunter's Mark. *Bestial Bond* (5). Your pet's damage feeds your focus. Your critical strikes. Your traps arm faster while it holds aggro. Commands cost no global cooldown. It executes one queued command after dying.
- **Gate 10, 8.** *Unleashed Fury* (5). Your pet's family ability costs no focus while it holds aggro. It may be used while your pet is moving. It triggers automatically when your pet is critically hit. It applies your Hunter's Mark. Using it grants your pet your own critical strike chance for 6 seconds. *Pathfinding* (3). Your pet keeps pace with you mounted. Closes through crowd control. Reaches a target you cannot see.
- **Gate 15, 7.** *Ferocity* (5). Your pet's critical strikes cause its target to bleed. The bleed spreads on the target's death. Your pet's criticals refresh your Hunter's Mark. At full health your pet's criticals cannot miss. Your pet's criticals grant it focus. *Improved Mend Pet* (2). Mend Pet also cleanses a curse, disease, magic or poison from your pet. It cleanses one more and may be cast while your pet is feared.
- **Gate 20, 10, hybrid seat.** *Intimidation* (1). Command your pet to intimidate the target on the next successful melee attack, causing a high amount of threat and stunning the target for 3 sec. *Spirit Bond* (2). You and your pet regenerate health while it is active. The regeneration continues out of combat. *Marksman's Bond* (4). *(cross-tree)* Your pet's critical strikes apply your Hunter's Mark. All of its attacks apply it. Your Aimed Shot refreshes its focus. Its criticals reduce your Rapid Fire cooldown. *Blood Bond* (1). *(subtraction node)* Your health and your pet's become a single shared pool, and damage to either reduces both. *Pack Hunter* (2). *(reciprocal)* Your pet's attacks arm a trap it is standing on. Your pet cannot trigger your own traps.
- **Gate 25, 5.** *Frenzy* (5). Your pet gains attack speed after a critical strike. The effect stacks. It does not fall off when the pet changes target. It also triggers on your own critical strikes. At full stacks your pet's next attack cannot miss.
- **Gate 30, 1.** *Bestial Wrath* (1). Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be prevented unless killed.

<!-- END GENERATED -->

48 points, unchanged. Endurance Training, Thick Hide, Bestial Swiftness, and Bestial Discipline are deleted to dividend.

### 17.2 Survival

The one tree in the game whose own class guides call it the worst and advise against playing it. Its content is traps and defence, neither of which vanilla raids reward, and it carries the most mode-locked nodes after Protection warrior.

Two things make it the most interesting salvage in the document. Traps are a mechanic no other class has, and Section 5.8's rule means they now need to work in both modes rather than being written off as PvP content.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 11.** *Trapper* (5). Traps arm instantly. May be laid in combat. Two may be active at once. They persist through your death. Laying one does not break stealth-equivalent positioning. *Quarry* (6). Your damage against a creature type you have Tracked is increased. Track may be swapped in combat. Tracking a type reveals it on your minimap at any range. A tracked target cannot restealth. Tracked targets take increased damage from your traps. Track persists through your death.
- **Gate 5, 12.** *Entrapment* (5). Your Frost Trap roots what it catches. Every trap roots what it catches. The root holds longer. It holds through your own periodic damage. It holds through all damage you deal. *Improved Wing Clip* (5). Wing Clip may root instead of slow. Against a target immune to roots it slows harder instead. The slow rises to twice as hard. The root holds through your periodic damage. It holds through all damage you deal. *Savage Strikes* (2). Your Raptor Strike does not consume your ranged swing timer. It applies Serpent Sting, and a critical strike with it arms your nearest trap.
- **Gate 10, 8.** *Deterrence* (1). For a short time you turn aside almost everything aimed at you. Attacks you deflect return a shot of your own. *Clever Traps* (3). Your trap effects cannot be dispelled. They scale with your ranged attack power. A broken trap refunds its cooldown. *Survivalist* (4). Damage taken below 35% health arms your nearest trap. It also grants you a short damage reduction. A trap armed this way costs no cooldown. Below 20% health it arms every trap you have set.
- **Gate 15, 7.** *Improved Feign Death* (2). Feign Death cannot be resisted. Feigning drops all your damage-over-time effects rather than breaking them, and they resume when you rise. *Trap Mastery* (5). Traps deal damage rather than only controlling. They apply Serpent Sting. Explosive Trap knocks back. Freezing Trap slows a stun-immune target. Triggering one resets another.
- **Gate 20, 8, hybrid seat.** *Counterattack* (1). A strike that becomes available after you parry. It cannot be dodged or parried in turn, and it roots the target where it stands. *Snare Mastery* (3). *(cross-tree)* Your Concussive Shot and Wing Clip share their slow. Your Explosive and Immolation Traps benefit from your ranged critical chance. Every trap benefits from it. *Melee Cadence* (3). *(cross-tree)* Raptor Strike does not consume your ranged swing timer. Mongoose Bite triggers on a dodge as well as a parry. A melee strike refreshes Serpent Sting. *Lone Wolf* (1). *(subtraction node)* You gain substantial damage while no pet is active, and you may not summon one.
- **Gate 25, 5.** *Lightning Reflexes* (5). Dodging an attack refreshes the cooldown of Riposte. Dodging grants a combo point. A full dodge chain refreshes Evasion. Avoidance cannot be reduced below its base. Riposte cannot be avoided.
- **Gate 30, 1.** *Wyvern Sting* (1). Puts the target to sleep and applies Serpent Sting when the sleep breaks. Against targets immune to sleep it instead reduces their damage dealt by 20% for the same duration.

<!-- END GENERATED -->

52 points against 48. Surefooted and Killer Instinct deleted to dividend.

### 17.3 Restoration shaman

Twenty of fifty-two points are mana cost and healing percentage on one spell family. Gate 20 holds four points, the sparse-tier problem from REG-18 for the fifth time.

The spine is Nature's Swiftness, Healing Way, Totemic Mastery, and Mana Tide Totem. Three of those four are totem content, which makes this the one shaman tree that already knows what the class is about.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Tidal Focus* (5). A Healing Wave that overheals refunds mana. All your heals gain the refund. The overhealed portion of a critical heal chains to a second target. Any overheal chains. It banks toward your next cast. *Ancestral Healing* (5). Your heal grants armor. It reduces damage taken as well. It applies to everyone the heal touched. It persists 10 seconds after the heal. It cannot be dispelled.
- **Gate 5, 7.** *Improved Reincarnation* (2). Reincarnation's cooldown drops. You return with full mana as well as health. *Chain Mastery* (5). Chain Heal jumps further. Prefers the lowest-health target. Does not lose effect per jump against targets below 30%. Can bounce back to its origin. Jumps to a target with no heal-over-time first.
- **Gate 10, 12.** *Healing Focus* (5). Your Healing Wave may resist interruption from damage. Lesser Healing Wave and Chain Heal gain the effect. All your healing spells gain it. They resist it entirely while you are below one quarter health. The threshold rises to half your health. *Totemic Mastery* (1). The radius of your totems that affect friendly targets is increased to 30 yd. *Totemic Reach* (3). Your totems reach twice as far. They follow you between them. A totem out of range still counts as placed. *Healing Grace* (3). Healing generates less threat. Threat you do generate transfers to the target after 6 sec. Overhealing generates none at all.
- **Gate 15, 10.** *Restorative Totems* (5). Mana Spring and Healing Stream Totem reach your whole raid. They persist 10 sec after being destroyed. They cannot be targeted by enemies. They scale with your healing bonus. Dropping one refreshes the other. *Tidal Mastery* (5). A critical Healing Wave chains to a second ally at one third value. The chain seeks an injured ally. The effect extends to your other heals. The chain's value rises to half. The chain cannot overheal.
- **Gate 20, 10, hybrid seat.** *Nature's Swiftness* (1). Your next Nature spell is instant. It may be used while silenced, and using it does not break your own crowd control. *Healing Way* (3). Healing Wave leaves the target more receptive to your next. The effect stacks. It does not fall off between fights. *Elemental Communion* (3). *(cross-tree)* Your Lightning Shield discharges heal instead of damage while Healing Stream Totem is active. Any healing totem maintains the effect. Your Chain Lightning uses Chain Heal's jump logic. *Ancestor's Vigil* (1). *(subtraction node)* Your totems heal continuously and cannot be destroyed. You may not cast direct heals. *Stoneskin Discipline* (2). *(reciprocal)* Your Earth Shield-style effects persist through your own melee damage. Healing a target grants them a portion of your weapon imbue's effect.
- **Gate 25, 5.** *Purification* (5). Cleansing a poison heals the target. Cleansing a disease does as well. Your Cure Poison removes one additional effect. Cure Disease removes one additional effect. They share no cooldown.
- **Gate 30, 1.** *Mana Tide Totem* (1). A totem that returns mana to your party over its life. It restores more as its own health falls, and it cannot be attacked below half.

<!-- END GENERATED -->

56 points against 52. Improved Healing Wave, Totemic Focus, and Nature's Guidance deleted to dividend.

### 17.4 Affliction

Seventeen nodes, and five of them modify curses that a raid warlock casts once. Improved Curse of Exhaustion takes four points at gate 20, in the hybrid seat, on a movement slow.

The spine is Nightfall, Siphon Life, Dark Pact, Improved Drain Soul, and Shadow Mastery. Affliction is in better shape than its floor suggests because those five are genuinely good; the problem is what sits between them.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Suppression* (5). Your damage-over-time effects cannot be dispelled. They cannot be resisted on application. They do not break on damage. They persist through your death. They spread to a nearby enemy when their target dies. *Improved Corruption* (5). Your Corruption applies instantly at rank 1. Refreshes on your Shadow Bolt. Ticks faster below 20%. Spreads on death. Carries remaining damage forward when refreshed.
- **Gate 5, 12.** *Improved Drain Soul* (2). Drain Soul restores mana while it channels. It restores more on a killing blow, and the mana persists through death. *Siphon* (5). Drain Life and Drain Mana channel while you move. They do not break on damage. They benefit from your shadow damage. They apply Corruption. They refund a shard on a killing blow. *Curse Mastery* (5). Two curses may be active at once. Curses cannot be dispelled. A curse refreshes on your damage-over-time ticks. Amplify Curse has no cooldown. Curses apply to everything Corruption is on.
- **Gate 10, 9.** *Fel Concentration* (5). Your channelled spells cannot be interrupted by damage. Pushback is capped at once per channel. A channel completed under fire grants a soul shard. Interruption refunds the mana spent. You may channel while silenced once every 45 sec. *Amplify Curse* (1). Your next Curse lands at doubled strength and cannot be dispelled. Amplifying a Curse of Agony makes it tick from the first second. *Grim Reach* (3). Your Affliction effects gain range. Reapplying one at maximum range does not break your current cast. Your curses reach as far as your damage-over-time effects.
- **Gate 15, 6.** *Nightfall* (2). Corruption and Drain Life may make your next Shadow Bolt instant. Nightfall also refunds its mana. *Improved Drain Mana* (2). The mana your Drain Mana takes also burns the target. It burns harder against a target already out of mana. *Shadow Embrace* (2). Your periodic effects make a target vulnerable to Shadow, and the vulnerability stacks. While Dark Pact holds, your periodics also afflict one nearby enemy.
- **Gate 20, 8, hybrid seat.** *Siphon Life* (1). Transfers 15 health from the target to the caster every 3 sec. Lasts 30 sec. *Soul Siphon* (3). *(cross-tree)* Your Shadow Bolt refreshes Corruption. Your Immolate benefits from your shadow damage. Conflagrate does not consume Immolate on a target affected by Corruption. *Malediction* (2). *(cross-tree)* Your Curses last longer and cannot be dispelled. They afflict one nearby enemy as well. *Unstable Affliction* (2). *(subtraction node)* Your damage-over-time effects deal substantially more damage and detonate when dispelled. You may no longer cast Shadow Bolt.
- **Gate 25, 5.** *Shadow Mastery* (5). Your Shadow spells ignore a portion of the target's resistance. They cannot be reflected. Shadow damage over time ticks faster below 20% target health. Your Shadow spells apply Curse of Shadow's vulnerability. A Shadow critical refreshes Corruption.
- **Gate 30, 1.** *Dark Pact* (1). Your demon's life becomes yours to spend. Consuming it restores your health and mana in full and leaves your Shadow damage raised for the rest of the encounter. For twenty seconds your Shadow spells cost nothing and strike a second enemy. You may not summon another demon.

<!-- END GENERATED -->

49 points, unchanged. Improved Curse of Weakness, Improved Curse of Agony, Curse of Exhaustion, and Improved Curse of Exhaustion deleted, their effects folded into Curse Mastery.

### 17.5 Fury

Sixty points, the second largest tree in the game, and 78% of them flat. Nothing structural is wrong: gate 20 holds eight points and the distribution is even. It is simply a large tree full of percentages.

The spine is Unbridled Wrath, Blood Craze, Piercing Howl, Death Wish, Improved Berserker Rage, and Bloodthirst.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Booming Voice* (5). Shouts affect the raid. Persist through death. Refresh on a killing blow. Cost no rage below 20 rage. Apply to targets instead of allies as a debuff. *Bloodletting* (5). Your critical strikes cause bleeding. The bleed does not fall off early. A bleeding target takes each fifth blow as though it were two enemies. The interval tightens to each fourth blow. It tightens to every third.
- **Gate 5, 10.** *Unbridled Wrath* (5). Your strikes generate rage more freely. A critical strike generates it twice. You generate rage faster still for the first ten seconds of an encounter. The window extends to fifteen seconds. It extends to twenty. *Improved Demoralizing Shout* (5). Demoralizing Shout also reduces the target's critical strike chance. It applies to targets behind you. It cannot be dispelled. It refreshes when a target you have shouted at strikes you. A target that resists it is slowed instead.
- **Gate 10, 12.** *Blood Craze* (3). Being critically struck regenerates health over 6 sec. The regeneration cannot be interrupted. It also triggers on a block. *Piercing Howl* (1). A howl that dazes everything near you. It cannot be resisted, and a dazed target cannot mount. *Improved Cleave* (3). Your Cleave hits a third target. Applies your last special attack's effect. Costs no rage while enraged. *Rampage* (5). A killing blow grants attack speed. The effect stacks. It persists 10 seconds out of combat. It triggers on a critical strike. It carries across targets.
- **Gate 15, 12.** *Enrage* (5). While enraged your Heroic Strike costs no rage. Your shouts cost none. All your abilities cost none. Being enraged prevents fear. Taking a critical hit refreshes its duration. *Dual Wield Specialization* (5). While enraged your off-hand strikes for its full weight rather than half. It strikes for its full weight at all times. Two one-handers strike faster together than either alone. A critical strike with your main hand readies your off-hand. A critical strike with either hand readies the other. *Improved Execute* (2). Execute costs less rage. It costs none against a target below 10% health.
- **Gate 20, 10, hybrid seat.** *Death Wish* (1). You deal more damage and take more, and cannot be feared. It may be used while feared and while enraged, and it does not break your own crowd control. *Improved Intercept* (2). Intercept's cooldown drops and it may be used in any stance. It removes movement-impairing effects on arrival. *Sundering Blows* (4). *(cross-tree)* Your Sunder Armor applies from Cleave. It also applies from Whirlwind. Your Overpower benefits from your off-hand. Shield Slam may be used without a shield at reduced effect. *Reckless* (1). *(subtraction node)* Your critical strike chance is greatly increased. You cannot dodge, parry, or block. *Shieldbreaker* (2). *(reciprocal)* Your Cleave and Whirlwind ignore a portion of block value. Bloodthirst heals for more against a target you are tanking.
- **Gate 25, 7.** *Improved Berserker Rage* (2). Berserker Rage generates rage on use and cannot be prevented. For the first twenty seconds of an encounter your strikes deal increased damage. *Flurry* (5). A critical strike hastens your next swings. The effect does not fall off on a miss. It also hastens your shout casts. It stacks to two applications. While active your attacks cannot be dodged.
- **Gate 30, 1.** *Bloodthirst* (1). An instant strike that draws blood. Each of your next five melee hits returns health, and against a bleeding target the strike hits everything in front of you.

<!-- END GENERATED -->

60 points, unchanged. Improved Battle Shout and Improved Slam deleted to dividend.

---

## 18. The 15 and 16 band

Seven trees between 15 and 16 forced flat. Recorded briefly, since none needs a new diagnosis. Two of them carry the sharpest single examples in the audit and are given more room.

### 18.1 Holy paladin

Forty-five points, the third of the underweight trees from REG-17 and the last one outstanding. Gate 20 holds four points, sparse-tier again.

It also opens with the purest offenders in the game. **Divine Strength and Divine Intellect take ten of forty-five points, and their entire text is "increases your Strength" and "increases your Intellect."** No condition, no interaction, no spell named. If Section 5.1 needed a single illustration, it is these two nodes: they exist only because the tree needed something at gate 0, and under the depth dividend they are precisely what a curve is for.

The spine is Illumination, Spiritual Focus, Divine Favor, Consecration, and Holy Shock.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Sanctified Word* (5). Your first heal on a target cannot be interrupted. It cannot be overhealed. It refreshes your Seal. It grants the target your aura at double effect. It applies to everyone within 8 yards of them. *Beacon* (5). A target you heal is marked. Your heals on others echo to them. The mark persists through your death. It transfers your Judgement. Two may be active.
- **Gate 5, 10.** *Spiritual Focus* (5). Your heals cannot lose casting time when you take damage. Pushback is capped at once per cast. A heal completed under fire refreshes your Seal. Interruption instead reduces your next heal's cost. You may heal while silenced once every 45 sec. *Improved Seal of Righteousness* (5). Your Seal persists through a weapon swap. Your judging does not consume it. It refreshes when you cast a heal. It applies to the first target struck after leaving combat. Two Seals may be active at once.
- **Gate 10, 8.** *Consecration* (1). Consecrates the land beneath the Paladin, doing 64 Holy damage over 8 sec to enemies who enter the area. *Improved Lay on Hands* (2). Lay on Hands leaves the target armored for a time and does not empty your own mana. Used on yourself it grants the armor to your party instead. *Healing Light* (5). A heal cast on a target below 30% health cannot be overhealed. It refreshes your Seal. It removes one harmful effect. It grants the target your aura at double effect. It reduces your next heal's cost.
- **Gate 15, 7.** *Illumination* (5). A critical heal refunds its mana. It also refunds the mana of your previous cast. A critical heal grants the target your aura at double effect. Two criticals in a row make your next heal instant. A critical heal cannot be overhealed. *Improved Blessing of Wisdom* (2). Your Blessing of Wisdom restores mana when the target takes damage as well as over time. It persists through death.
- **Gate 20, 10, hybrid seat.** *Divine Favor* (1). Your next heal is a guaranteed critical. A Divine Favor heal that would overheal shields instead. *Judgement of Light* (3). Your Judgement heals whoever strikes the target. Scales with your healing bonus. Cannot be overwritten. *Righteous Shield* (3). *(cross-tree)* Your Blessing of Sanctuary scales with your healing bonus. Holy Shield may be maintained while healing. Damage you block refreshes your Seal. *Devotion* (1). *(subtraction node)* Your heals cost no mana while above 50% health. Below 50% you cannot heal at all. *Sanctified Judgement* (2). *(reciprocal)* Your Judgement's cooldown drops when you critically heal. Healing a target refreshes the Judgement on whatever struck them.
- **Gate 25, 5.** *Holy Power* (5). A critical Holy Light grants the target armor for 15 sec. A critical Flash of Light grants it as well. Any critical heal grants it. A critical heal on a target below 20% health also removes one harmful effect. The threshold rises to 30%.
- **Gate 30, 1.** *Holy Shock* (1). Blasts the target with Holy energy, causing 204 to 220 Holy damage to an enemy, or 204 to 220 healing to an ally.

<!-- END GENERATED -->

52 points against 45, per REG-17. Unyielding Faith deleted as mode-locked.

### 18.2 Combat rogue

The inverse of every sparse-tier tree in this document. **Gate 20 holds sixteen points, and all sixteen are weapon specialization: Fist, Mace, and Sword at five each, plus Blade Flurry.** Add Dagger Specialization at gate 15 and Weapon Expertise at gate 25 and the tree spends twenty-seven of sixty-two points on which weapon you happened to loot.

This is the Arms problem at twice the scale, and the fix is the same weapon fork used in Arms, Enhancement, Fury, and Bladedancer. Five nodes and twenty-seven points collapse to one node and five, and the choice moves from the talent panel to your hands.

That reclaims twenty-two points, which is why this tree does not grow: it redistributes.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Improved Gouge* (3). Gouge lasts longer and does not break on your periodic damage. It may be used from any angle. A target coming out of Gouge is slowed. *Improved Sinister Strike* (2). Your Sinister Strike grants an additional combo point on a critical strike. It may be used from any angle without penalty. *Opportunist* (5). Your Sinister Strike may be used from any angle. Sinister Strike refreshes your Slice and Dice. Your Backstab may be used from any angle. Your Ambush may be as well. Every strike from behind loses its positional requirement.
- **Gate 5, 13.** *Riposte* (1). A strike that becomes available after you parry, disarming the target briefly. It cannot be dodged and it refunds its energy on a critical strike. *Bladework* (5). Parrying grants a combo point. Dodging does too. Avoidance refreshes Riposte. A parry refunds energy. Your Riposte cannot be avoided. *Improved Backstab* (3). Your Backstab may be used from the side as well as from behind. Against a bleeding target it may be used from the front. It refreshes Rupture. *Endurance* (4). Sprint and Evasion share no cooldown. Sprint removes movement-impairing effects. Evasion also reduces ranged damage taken. Both may be used while rooted.
- **Gate 10, 8.** *Improved Sprint* (2). Sprint removes movement-impairing effects on use. Against effects that cannot be removed it instead halves their remaining duration. *Adrenaline* (6). Energy regeneration increases below 20 energy. A finisher refunds energy. Your Evasion grants energy. Energy caps higher during Blade Flurry. Abilities cost no energy for 3 seconds after a killing blow. Your Sprint costs energy instead of a cooldown.
- **Gate 15, 12.** *Weapon Mastery* (5). Your equipped weapon determines the effect: swords grant a chance at an extra attack, maces stun, fists reduce the target's attack speed, and daggers allow Backstab from any angle. The effect also applies to your off-hand. It triggers from Blade Flurry. At full stacks it cannot be avoided. A killing blow refreshes it. *Improved Kick* (2). Kick may silence what it interrupts. The silence lasts longer against a caster mid-cast. *Vitality* (5). Your poisons persist through weapon swaps. They deal increased damage. They apply from Blade Flurry. They spread to everything it strikes. A poison application refreshes Slice and Dice.
- **Gate 20, 8, hybrid seat.** *Blade Flurry* (1). Your attacks come faster and strike a second enemy beside your target. The extra strikes carry your poisons. *Killing Spree* (3). *(cross-tree)* Your Backstab and Ambush benefit from your off-hand weapon. Cheap Shot applies your Expose Armor. Openers refresh Slice and Dice. *Cutthroat* (3). *(cross-tree)* Your poisons benefit from your critical strike damage bonus. Eviscerate consumes poison stacks for damage rather than letting them fall off. Every finishing move does the same. *Duellist* (1). *(subtraction node)* You deal substantially more damage from the front and none at all from behind.
- **Gate 25, 5.** *Aggression* (5). Your finishing moves cost less energy. Below 10% target health they consume one fewer combo point. The threshold rises to 20%. A finisher that kills its target refunds a combo point. It refunds every combo point spent.
- **Gate 30, 1.** *Adrenaline Rush* (1). Your energy returns at double pace for a short time. Finishers used during it cost nothing.

<!-- END GENERATED -->

62 points, unchanged. Lightning Reflexes, Deflection, Dagger Specialization, Fist and Mace and Sword Specialization, and Weapon Expertise all deleted or folded into the fork.

### 18.3 Frost mage

Gate 20 holds four points. The tree is otherwise healthy and its spine, Shatter, Winter's Chill, Ice Block, Cold Snap, and Ice Barrier, is among the best in the game.

The Winter's Chill note from Section 5.4 belongs here: the frost group build trades roughly 5 to 10% of the mage's own damage for the whole group's, which is a subtraction talent that shipped in vanilla and the better of the two precedents this document cites.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Improved Frostbolt* (5). Your Frostbolt applies two stacks of Chill. Cannot be resisted against a Chilled target. Reduces its own cast time per consecutive cast. Refreshes Winter's Chill. A critical hit resets Frost Nova. *Frost Warding* (2). Your Armor spells absorb elemental damage as well as physical. Absorbing damage restores mana instead of merely preventing it. *Elemental Precision* (3). Your Frost and Fire spells cannot be partially resisted. A full resist refunds their mana. A resisted spell reduces the target's resistance to your next cast.
- **Gate 5, 13.** *Frostbite* (3). Your Chill effects freeze the target in place. The freeze cannot be resisted. A frozen target takes increased damage from your other schools. *Improved Frost Nova* (2). Frost Nova's cooldown drops and its root does not break on your own periodic damage. A target freed from it is Chilled for the remainder. *Permafrost* (3). Your Chill effects also slow the target's attack speed. They cannot be dispelled. A Chilled target takes increased damage from your Fire and Arcane spells. *Deep Freeze* (5). Chilled targets take increased damage from your other schools. Frost Nova's break threshold rises. Your chill spreads on death. Your Blizzard applies Frostbite. A frozen target's Shatter bonus applies to your party.
- **Gate 10, 7.** *Cold Snap* (1). Your Frost cooldowns are finished at once. Cold Snap does not finish its own. *Improved Blizzard* (3). Blizzard Chills what it touches and the Chill deepens with each tick. It follows a target you have marked. It does not break your own crowd control. *Piercing Ice* (3). Your Chill effects reduce the target's casting speed as well as their movement. Your chill cannot be dispelled. A Chilled target takes increased damage from your other schools.
- **Gate 15, 8.** *Shatter* (1). Your spells strike frozen targets with certainty rather than chance. A frozen target takes your criticals as a matter of course, and shattering one spreads the Chill. *Arctic Reach* (2). Your Frost spells reach further and their area effects cover more ground. At maximum range Frostbolt cannot be resisted. *Frost Channeling* (5). Channelled spells cannot be pushed back. Blizzard follows your target. Your Evocation may be used in combat once. Channels benefit from Clearcasting. A broken channel refunds its mana.
- **Gate 20, 10, hybrid seat.** *Ice Block* (1). You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot, move or cast spells. *Improved Cone of Cold* (2). Cone of Cold strikes in a full circle instead of an arc. Its Chill cannot be dispelled. *Frostfire* (3). *(cross-tree)* Your Fire spells apply Chill. Frostbolt benefits from Ignite. Blast Wave applies Frostbite. *Absolute Zero* (2). *(subtraction node)* Your Frost spells always apply their full Chill and cannot be resisted. They can no longer critically strike. *Arcane Frost* (2). *(reciprocal)* Your Presence of Mind does not consume itself on a Frost spell that is resisted. Your Arcane Explosion applies Chill.
- **Gate 25, 5.** *Winter's Chill* (5). Your Frostbolt leaves the target vulnerable to your Frost criticals. All your Frost spells apply it. The vulnerability stacks. It does not fall off while you keep casting. It applies to your party's Frost criticals as well.
- **Gate 30, 1.** *Ice Barrier* (1). Instantly sheilds you, absorbing 455 damage. Lasts 1 min. While the shield holds, spells will not be interrupted.

<!-- END GENERATED -->

52 points against 46.

### 18.4 Assassination

Gate 20 holds four points. The tree is the least flat in the game at 67% and its spine, Seal Fate, Relentless Strikes, Cold Blood, Ruthlessness, and Improved Kidney Shot, is a genuine combo point engine.

**The capstone is Vigor, which increases maximum energy by 10.** A 31-point talent whose entire text is a flat number, and the only capstone in the game that buys nothing but a stat. Deleted to dividend, and the slot needs a real capstone: *Master Poisoner* (1), your poisons apply instantly at full stacks and cannot be cleansed.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Remorseless Attacks* (2). Killing a target raises the critical strike chance of your next opener. The bonus holds through two openers. *Improved Eviscerate* (3). Eviscerate refunds one combo point on a critical strike. It consumes any bleed on the target for additional damage. A killing blow with it refreshes Slice and Dice. *Opportunity* (5). Your Ambush and Garrote deal increased damage. Cheap Shot gains the bonus. The bonus lasts 15 seconds. Your first strikes of an encounter gain it as well. The bonus holds until you leave combat.
- **Gate 5, 8.** *Ruthlessness* (3). A finishing move that critically strikes returns a combo point. Every finishing move returns one. Your strikes lose no damage while you are moving. *Improved Slice and Dice* (3). Your Slice and Dice refreshes rather than overwriting when reapplied. It persists 10 seconds after leaving combat. It is not lost when you Vanish. *Find Weakness* (2). Your finishers reduce the target's armor for 12 seconds, stacking with Expose Armor rather than replacing it. The reduction applies to your whole party.
- **Gate 10, 6.** *Relentless Strikes* (1). Finishing moves restore energy, and every third strike you land sweeps through a second enemy. *Puncturing Wounds* (5). A critical finisher applies a bleed scaling with combo points spent. The bleed cannot be dispelled. It spreads on the target's death. It ticks twice as fast below 20% health. Refreshing it carries remaining damage forward.
- **Gate 15, 10.** *Envenom* (5). Your poisons stack one higher than their maximum. They stack a second point higher. Eviscerate applies them. Every finishing move applies them. A finisher landed at full stacks refreshes their duration. *Toxicology* (5). Your poisons deal increased damage. They stack one higher than their maximum. Eviscerate applies them. Every finishing move applies them. They cannot be cleansed.
- **Gate 20, 10, hybrid seat.** *Cold Blood* (1). Your next strike is a guaranteed critical. Used on a finisher it doubles the combo points spent. *Improved Kidney Shot* (3). A target you have Kidney Shot takes more damage from you. The effect lasts beyond the stun. It cannot be dispelled. *Shadow Focus* (3). *(cross-tree)* Your stealth abilities cost less energy while Slice and Dice is active. Premeditation feeds Seal Fate. Openers from stealth cannot be resisted. *Blood Price* (1). *(subtraction node)* Your finishers deal substantially more damage and cost health as well as energy. *Blade Venom* (2). *(reciprocal)* Your poisons apply from off-hand attacks at full rate. A finishing move spends a poison stack for immediate damage.
- **Gate 25, 5.** *Seal Fate* (5). Your critical strikes from abilities that add combo points add an additional one. The extra point is not lost on a miss. Two criticals in a row grant a third. Seal Fate triggers from poisons. A finisher spent at five points refreshes it.
- **Gate 30, 1.** *Master Poisoner* (1). Your poisons apply instantly at full stacks rather than building, and cannot be cleansed by any means. A target that dies while poisoned passes your stacks to the nearest enemy.

<!-- END GENERATED -->

52 points against 46.

### 18.5 Subtlety, Destruction, Protection warrior

Three trees needing no new argument.

**Subtlety** (47 points, 15 forced flat) is a PvP tree with no raid application, which under Section 5.8 is the problem rather than a description. Its stealth and positioning content becomes mode-agnostic: Opportunity and Initiative reworked so opening from stealth matters in a raid pull, Preparation kept, Ghostly Strike kept, Master of Deception and Camouflage folded into a single stealth node, Improved Sap given a graded fallback. Gate 20 grows from six to eight with a sideways node keyed to poisons and a subtraction node, *Silent Death*: your openers cannot be dodged or resisted and generate no threat, and you deal no damage from the front. That is the deliberate mirror of Combat's Duellist, so the two rogue trees close opposite doors.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Master of Deception* (5). Stealth is harder to detect. It does not break on ambient damage. It may be entered in combat once every three minutes. The cooldown drops to two minutes. It drops to one minute. *Opportunity* (5). Your Ambush and Garrote deal increased damage. Cheap Shot gains the bonus. The bonus lasts 15 seconds. Your first strikes of an encounter gain it as well. The bonus holds until you leave combat.
- **Gate 5, 11.** *Initiative* (3). Your Cheap Shot grants an additional combo point. Ambush and Garrote grant one as well. The effect works on a raid pull rather than only from stealth. *Camouflage* (5). Stealth movement speed rises. It reaches your normal speed. Movement-impairing effects cannot slow you while stealthed. Your Sprint does not break stealth. Vanish resets it. *Improved Sap* (3). Your Sap lasts longer. Against Sap-immune targets it instead reduces the damage they deal in melee. The reduction extends to all damage they deal.
- **Gate 10, 6.** *Ghostly Strike* (1). A strike that deals 125% weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. *Serrated Blades* (5). Eviscerate reduces the target's armor. Every finishing move reduces it. Eviscerate also applies a bleed. Every finisher applies the bleed. The bleed scales with combo points spent.
- **Gate 15, 9.** *Setup* (3). Avoiding an attack grants a combo point. Your Riposte does. A full dodge chain refreshes Evasion. *Elusiveness* (2). Vanish and Blind cooldowns drop. Vanish removes damage over time effects. *Hemorrhage* (4). A strike that marks the target, increasing your party's Physical damage against it. The mark stacks three times. It persists through your death. It transfers on target death.
- **Gate 20, 10, hybrid seat.** *Preparation* (1). Your Rogue cooldowns are finished at once. Preparation does not finish its own. *Deadened Nerves* (4). *(cross-tree)* Your Ambush applies your active poison at full stacks. Backstab applies it as well. A poison applied from stealth strikes for its full duration at once. Your poisons deal increased damage and cannot be cleansed. *Silent Death* (3). *(subtraction node)* Your openers cannot be dodged or resisted. They generate no threat. You deal no damage from the front. *Shadow Dance* (2). *(reciprocal)* Your Blade Flurry does not break stealth openers. Your Ghostly Strike refreshes Slice and Dice.
- **Gate 25, 5.** *Premeditation* (5). Grants combo points before an opener. They persist through a target change. They cannot be lost. Premeditation resets on a killing blow. It grants an extra finisher point.
- **Gate 30, 1.** *Shadowstrike* (1). A strike from stealth that does not break stealth, usable once per Vanish.

<!-- END GENERATED -->

**Destruction** (53 points, 15 forced flat, gate 20 at eight) is the healthiest warlock tree and needs the least. Devastation, Improved Immolate, Improved Searing Pain, Cataclysm, and Bane are flat and go to dividend; Shadowburn, Conflagrate, Ruin, Pyroclasm, and Improved Shadow Bolt are the spine and stay. The rebuilt nodes are about Immolate and Conflagrate interacting rather than about either being larger. Subtraction node at gate 20, *Backdraft*: Conflagrate loses its cooldown and you may no longer cast Shadow Bolt.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Improved Shadow Bolt* (5). Your Shadow Bolt applies a vulnerability consumed by the next attacker. The vulnerability stacks. It does not expire. It applies on cast rather than on hit. It spreads on death. *Aftermath* (5). Your Destruction spells may daze the target. A dazed target casts more slowly. Your Rain of Fire applies Immolate's burn at reduced value. Your direct Fire spells do as well. Every Destruction spell applies it.
- **Gate 5, 10.** *Improved Immolate* (5). Immolate's direct half scales with its remaining periodic damage. It refreshes on Shadow Bolt. It cannot be dispelled. It ticks faster below 20% health. It detonates on expiry. *Intensity* (2). Your Destruction spells cannot be pushed back. A spell that would have been pushed back instead finishes early. *Destructive Reach* (3). Range increases. Your threat is reduced. Rain of Fire follows a marked target.
- **Gate 10, 8.** *Shadowburn* (1). Instantly blasts the target for 91 to 104 Shadow damage. If the target dies within 5 sec of Shadowburn, and yields experience or honor, the caster gains a Soul Shard. *Improved Searing Pain* (5). Searing Pain draws no threat. It consumes Immolate for burst. It applies Immolate. It refreshes Conflagrate. Two casts in a row are free. *Pyroclasm* (2). Your Fire spells may stun. For the first twenty seconds of an encounter they deal increased damage.
- **Gate 15, 9.** *Devastation* (5). A critical Destruction spell refreshes Immolate on its target. It grants a soul shard. It applies Aftermath. It cannot be resisted. Two in a row make your next Destruction spell instant. *Emberstorm* (4). Your direct Fire spells consume Immolate stacks for damage. Your Rain of Fire applies Immolate. Every Fire spell you cast consumes stacks. Your Hellfire does not damage you while Immolate is active.
- **Gate 20, 8, hybrid seat.** *Ruin* (1). Your Destruction criticals strike for double rather than half again. A critical that kills refunds its shard. *Cataclysm* (3). *(cross-tree)* Your Immolate counts as a curse. Your Corruption refreshes it. Curse of Agony benefits from your fire damage. *Nether Protection* (2). *(cross-tree)* Your demon's attacks apply Immolate. Soul Link shares your fire damage bonus. *Backdraft* (2). *(subtraction node)* Conflagrate loses its cooldown. You may no longer cast Shadow Bolt.
- **Gate 25, 5.** *Conflagrate* (5). Conflagrate no longer consumes Immolate. It extends it. It hits a second target. It cannot be resisted. It resets on a killing blow.
- **Gate 30, 1.** *Shadow and Flame* (1). Immolate empowers your Shadow Bolts while it burns, and each Shadow Bolt extends it. A Shadow Bolt cast into your own Immolate cannot be resisted, and Immolate's remaining damage is added to the killing blow.

<!-- END GENERATED -->

**Protection warrior** (53 points, 15 forced flat) is the tree this document originally called the healthiest in the game, before the classifier review moved it from 7 to 15. It carries the most mode-locked content of any tree at three nodes: Iron Will, Improved Disarm, and Improved Revenge's stun. All three get graded fallbacks per Section 5.8 rather than deletion. Gate 20 grows from five to eight, including the subtraction node *Unbreakable*: you cannot be critically struck, and you can no longer critically strike. Shield Slam, Last Stand, Concussion Blow, and Shield Specialization's rage interaction are the spine and stay.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Shield Specialization* (5). Blocking generates rage. Refreshes Shield Block. A block grants a stacking damage reduction. Blocked damage generates threat. Two blocks in a row reset Revenge. *Anticipation* (5). A dodge refreshes Revenge. A parry does as well. A dodge grants rage. A parry grants it too. Reduces Shield Slam's cooldown.
- **Gate 5, 12.** *Improved Bloodrage* (2). Your Bloodrage generates threat. It may be used while stunned. *Toughness* (5). Damage you take refreshes Battle Shout. It refreshes Demoralizing Shout as well. It refreshes any active shout. It generates threat. Reduces the next hit. *Iron Will* (5). The duration of stuns against you is reduced. The duration of charms is reduced. A stun from an immune source instead generates rage. A charm from an immune source does as well. The rage granted is doubled.
- **Gate 10, 12.** *Last Stand* (1). You gain a share of your maximum health for twenty seconds. When it ends the health drains away rather than vanishing. *Improved Shield Block* (3). Shield Block covers an additional attack. It may be used while stunned. It refreshes on a parry. *Improved Revenge* (3). Revenge stuns the target. Against stun-immune targets it instead reduces their damage dealt. Revenge may be used without having blocked, dodged, or parried. *Defiance* (5). Your threat decays more slowly while you hold aggro. It does not decay at all. It holds against everything in melee range. A share of it transfers on Taunt. Taunt transfers it in full.
- **Gate 15, 8.** *Improved Sunder Armor* (3). Your Sunder Armor costs less rage. Applies from Cleave. Does not fall off while you are in melee range. *Improved Disarm* (3). Your Disarm lasts longer. Against disarm-immune targets it instead reduces their damage. The reduction matches a full disarm. *Improved Taunt* (2). Taunt's cooldown drops. Taunt works on an already-taunted target.
- **Gate 20, 8, hybrid seat.** *Concussion Blow* (1). A blow that stuns. It cannot be resisted, and a stunned target takes your next strike as a critical. *Sword and Board* (3). *(cross-tree)* Your Overpower may be used with a shield equipped. Your Deep Wounds applies from Shield Slam. Mortal Strike's healing reduction applies from Revenge. *Bulwark* (3). *(cross-tree)* Your Cleave generates block value. Your Whirlwind does as well. Bloodthirst heals for your block value. *Unbreakable* (1). *(subtraction node)* You cannot be critically struck. You can no longer critically strike.
- **Gate 25, 5.** *Shield Discipline* (5). Your Shield Slam refreshes Shield Block. It dispels one magic effect. It applies Sunder Armor. It cannot miss. It resets Last Stand below 20% health.
- **Gate 30, 1.** *Shield Slam* (1). Slam the target with your shield, causing 225 to 236 damage, modified by your Shield Block value, and has a 50% chance of dispelling 1 magic effect on the target. Also causes a high amount of threat.

<!-- END GENERATED -->

---

## 19. The last five

Arcane at 14, Restoration druid at 13, Arms at 12, Shadow at 11, Fire at 8. The healthy end of the audit, and two of them raise questions the rest did not.

### 19.1 Arcane

Fourteen forced flat, gate 20 at six. Arcane Focus, Arcane Subtlety, Magic Absorption, Arcane Resilience, Magic Attunement, Improved Mana Shield, Arcane Mind, and Arcane Instability are all percentages, and Wand Specialization reappears for the third time in the document after Discipline and Combat rogue.

The spine is Arcane Concentration, Presence of Mind, Improved Counterspell, Arcane Meditation, and Arcane Power. That is a real spec, and it is the reason Arcane is a splash tree rather than a main one: the good nodes are cheap and the deep ones are stats.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Improved Arcane Missiles* (5). Arcane Missiles cannot be interrupted by damage. It may be channelled while moving. Its channel does not break when the target dies, retargeting instead. A full channel grants Clearcasting. It applies your Chill or Ignite depending on your last cast. *Arcane Subtlety* (5). Your spells ignore a portion of the target's resistance. They cannot be reflected. A resisted spell refunds its mana. Partial resists are removed entirely. A resist grants Clearcasting.
- **Gate 5, 10.** *Arcane Concentration* (5). Your Arcane damage spells may leave you Clearcast, so the next spell costs half its mana. The next spell costs nothing instead. Fire and Frost damage spells may trigger Clearcasting as well. Clearcasting removes half the next spell's cast time. It removes the cast time entirely. *Magic Absorption* (5). Your Wards restore mana equal to a portion of the spell damage they absorb. Your Mana Shield and Ice Barrier do the same. Any absorption protecting you restores mana as well. Absorbing a spell grants a stack that empowers your next damage spell. The stack empowers a cast of any kind.
- **Gate 10, 8.** *Improved Counterspell* (2). Counterspell may silence what it interrupts. The silence cannot be resisted. *Arcane Shielding* (6). Mana Shield converts damage at a better rate. Does not break on control effects. May be cast on an ally. Refreshes on a critical strike. Absorbs magic as well as physical. Its expiry deals arcane damage.
- **Gate 15, 8.** *Arcane Meditation* (3). Your mana regeneration continues while casting. It also continues through Evocation's cooldown. Casting a spell at full mana banks a portion for later. *Temporal Flux* (5). Your next spell after a Blink is instant. Blink removes roots. Presence of Mind's cooldown drops on a critical strike. Your Evocation may be channelled while moving. Blink resets Frost Nova.
- **Gate 20, 8, hybrid seat.** *Presence of Mind* (1). Your next spell is instant however long it would have taken. It may be used while silenced. *Arcane Potency* (3). *(cross-tree)* Your Fire and Frost spells benefit from Clearcasting without consuming it. Arcane Missiles applies an Ignite or a Chill depending on your last cast. Presence of Mind applies to your next two spells. *Spellsteal* (3). *(cross-tree)* Counterspell removes one beneficial magic effect from the target. The effect is granted to you for 30 sec. Counterspell's cooldown drops when it steals. *Mana Burn* (1). *(subtraction node)* Your spell damage is greatly increased and your mana pool is halved.
- **Gate 25, 5.** *Arcane Instability* (5). Clearcasting does not break when an Arcane spell is resisted. It holds through a resist on any school. Three Clearcasting procs in a row make your next Arcane spell instant. Two procs in a row suffice. The instant cast applies to a spell of any school.
- **Gate 30, 1.** *Arcane Power* (1). For a short time your spells are cast with everything you have: they deal substantially more damage, cost substantially more mana, and cannot be interrupted or resisted.

<!-- END GENERATED -->

52 points against 47. Wand Specialization, Arcane Mind, Arcane Resilience, and Magic Attunement deleted to dividend.

### 19.2 Restoration druid

Thirteen forced flat, gate 20 at eight, and the only tree in this document whose complaint the floor cannot see.

The grievance record found it: the Restoration points are set with no real choice, and the spare Balance points are the only decision a resto druid gets. **The tree is not full of filler. It is full of talents so obviously mandatory that there is nothing to decide.** That is a fourth failure mode, and the rework as specified in Section 5.2 does not address it, because making a mandatory talent more interesting leaves it mandatory.

The fix is Section 5.4, not 5.2. A tree with no choices needs talents that trade against each other, which means subtraction nodes and mutually exclusive paths rather than better versions of the same obligations.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Furor* (5). Shifting into Cat Form grants energy and shifting into Bear Form grants rage. The amount is not reduced by shifting recently. Shifting also clears movement-impairing effects. Shifting does not break your Rejuvenation. Returning to a form you left within 6 sec costs no mana. *Improved Mark of the Wild* (5). Your Mark of the Wild applies to your whole party in one cast. It reaches a raid member outside your party. It persists through the target's death. It grants its bonus to your pet or your Feral form as well. Recasting it does not clear it from anyone still in range.
- **Gate 5, 12.** *Nature's Focus* (5). Healing spells cannot be interrupted by damage below a threshold. Pushback is capped at once per cast. A heal completed under fire refreshes Rejuvenation. Interruption instead empowers your next heal. You may cast while silenced once every 45 sec. *Improved Enrage* (2). Enrage generates rage the moment it is used rather than over its duration. It may be used while feared. *Regrowth* (5). Regrowth's direct and periodic halves may be split across two targets. The periodic half refreshes on your Rejuvenation. A critical direct half doubles the periodic. It may be cast while moving. It cannot be dispelled.
- **Gate 10, 9.** *Insect Swarm* (1). The enemy is swarmed by insects, decreasing their chance to hit by 2% and causing 66 Nature damage over 12 sec. *Reflection* (3). Your mana regeneration continues while casting. It also continues for 5 sec after taking damage. Casting a heal on a target at full health refunds its mana. *Subtlety* (5). Your heals over time draw less attention. All your healing does. The attention it does draw transfers to the tank you are healing. A heal that would pull aggro is silent instead once every 60 sec. Every such heal is silent.
- **Gate 15, 8.** *Improved Rejuvenation* (3). Rejuvenation may be applied twice to one target, the second stacking rather than overwriting. Its remaining duration carries forward when refreshed. A target at full health banks its ticks until they are needed. *Living Seed* (5). A critical heal leaves a seed that blooms when the target is next struck. The seed persists through your death. Two may be active. Blooming refunds mana. A bloom applies Rejuvenation.
- **Gate 20, 13, hybrid seat.** *Nature's Swiftness* (1). Your next Nature spell is instant. It may be used while silenced, and using it does not break your own crowd control. *Gift of Nature* (3). Your heals cannot be overhealed on a target below 30% health. A heal that would overheal instead shields for the excess. The shield persists 10 sec. *Wild Growth* (3). *(cross-tree)* Your heals over time benefit from your spell critical chance. Moonfire refreshes Rejuvenation. A critical heal over time seeds the next one. *Grove* (1). *(subtraction node)* Your heals over time cannot be dispelled and tick faster. Your direct heals cost double. *Torrent* (1). *(subtraction node)* Your direct heals critically strike far more often. Your heals over time no longer stack. *Communion* (1). *(subtraction node)* Your heals split between two targets at reduced effect. You may not single-target heal. *Nature's Bounty* (3). *(reciprocal)* Your Rejuvenation may be cast while shapeshifted. Its remaining duration is preserved through a shift. Healing a target in a Feral form refunds a portion of its cost.
- **Gate 25, 5.** *Improved Regrowth* (5). Regrowth's direct half cannot be resisted. A critical Regrowth doubles its periodic half. Regrowth may be cast while moving. Its periodic half refreshes on your Rejuvenation. Regrowth cannot be dispelled.
- **Gate 30, 1.** *Swiftmend* (1). Consumes a Rejuvenation or Regrowth effect on a friendly target to instantly heal them an amount equal to 12 sec. of Rejuvenation or 18 sec. of Regrowth.

<!-- END GENERATED -->

55 points against 53. Tranquil Spirit and Improved Tranquility deleted to dividend.

### 19.3 Shadow

Eleven forced flat, and the tree this document has repeatedly used as its example of a healthy structure attached to a weak spec. That remains true and the rebuild does not change it.

Improved Mind Blast, Shadow Focus, Shadow Reach, Improved Fade, Improved Psychic Scream, Improved Shadow Word: Pain, Shadow Affinity, and Darkness are the flat content, and most of them are small. Blackout, Spirit Tap, Mind Flay, Shadow Weaving, Silence, Vampiric Embrace, and Shadowform are the spine, and it is a good one.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Spirit Tap* (5). Killing a target that yields experience or honor restores your Spirit. Half your mana regeneration continues while casting during the effect. Any killing blow triggers it. Your full regeneration continues while casting. The effect persists through your next death. *Blackout* (5). Your Shadow spells stun on a critical strike. Against stun-immune targets they instead reduce damage dealt for the same duration. The effect cannot be resisted. It applies Shadow Weaving at full stacks. A stunned target's next hit on you is absorbed.
- **Gate 5, 10.** *Shadow Affinity* (3). Your Shadow Word: Pain refreshes when you shield its target. Mind Blast generates no threat while a shield of yours is active. Your shields benefit from your shadow damage. *Shadow Focus* (5). Your Shadow spells generate reduced threat. Shadow Word: Pain cannot be resisted. Mind Blast cannot be resisted. Mind Flay cannot be resisted. Your other Shadow spells cannot be resisted. *Improved Shadow Word: Pain* (2). Shadow Word: Pain refreshes when you cast Mind Blast on its target. It cannot be dispelled below 20% target health.
- **Gate 10, 8.** *Mind Flay* (1). Assault the target's mind with Shadow energy, causing 75 Shadow damage over 3 sec and slowing their movement speed by 50%. *Improved Mind Blast* (5). Your Mind Blast refreshes Shadow Word: Pain. Generates no threat. Applies Shadow Weaving at full stacks. Its cooldown resets on a killing blow. It consumes Shadow Word: Pain for burst. *Improved Psychic Scream* (2). Psychic Scream's cooldown drops and it breaks on a smaller amount of damage. Against fear-immune targets it instead reduces their movement speed and damage dealt for its duration.
- **Gate 15, 10.** *Shadow Weaving* (5). Your direct Shadow spells leave the target vulnerable to Shadow. The vulnerability stacks twice. Your periodic Shadow damage also applies it. It stacks five times. Anyone's Shadow damage benefits. *Mind Melt* (5). Your periodic shadow damage refreshes on Mind Flay. Your Mind Flay may be cast while moving. It does not break on damage. It applies Vampiric Embrace's healing. A full channel resets Mind Blast.
- **Gate 20, 8, hybrid seat.** *Vampiric Embrace* (1). Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 1 min. *Improved Vampiric Embrace* (2). Vampiric Embrace returns more health. The returned health may exceed full and becomes a shield. *Silence* (1). Silences the target, preventing them from casting spells for 5 sec. *Inner Light* (3). *(cross-tree)* Your Renew benefits from your Shadow damage. Your heals extend Vampiric Embrace. Power Word: Shield does not break Shadowform. *Void* (1). *(subtraction node)* Your shadow damage is greatly increased and you may not be healed by anyone but yourself.
- **Gate 25, 5.** *Darkness* (5). Shadowform no longer prevents you from casting Power Word: Shield on yourself while below half health. The restriction is removed entirely. Being critically struck in Shadowform generates a stack of Shadow Weaving. Damage beyond a tenth of your health generates a stack. Any damage you take in Shadowform generates a stack.
- **Gate 30, 1.** *Shadowform* (1). Assume a Shadowform, increasing your Shadow damage by 15% and reducing Physical damage done to you by 15%. However, you may not cast Holy spells while in this form.

<!-- END GENERATED -->

52 points against 48. Shadow Reach and Improved Fade deleted to dividend.

### 19.4 Fire

Eight forced flat, the healthiest tree in the game, and the one that argues against this document.

Impact, Ignite, Burning Soul, Pyroblast, Improved Fire Ward, Improved Scorch, Master of Elements, Blast Wave, and Combustion are all behavior. Only Improved Fireball, Flame Throwing, Improved Fire Blast, Improved Flamestrike, Incinerate, Critical Mass, and Fire Power are flat, and several are two or three ranks rather than five.

**So the rebuild is small, and that is the finding.** Improved Fireball, Critical Mass, and Fire Power go to the dividend. Flame Throwing and Improved Fire Blast get discrete ranks. Gate 20 grows from four to eight with a sideways node keyed to Frost and a subtraction node. Everything else stays as written.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

- **Gate 0, 10.** *Improved Fireball* (5). Fireball casts faster. It cannot be resisted. It leaves the target vulnerable to your next Fireball. The vulnerability applies to all your Fire spells. It stacks. *Impact* (5). Your Fire spells stun the target on a critical strike. Against stun-immune targets they instead reduce damage dealt for the same duration. The effect cannot be resisted. It applies Ignite at full value. A stunned target's next hit on you is absorbed.
- **Gate 5, 10.** *Ignite* (5). Your Fire criticals burn the target over time. The burn stacks. It spreads on death. It refreshes on any Fire cast. It cannot be dispelled. *Flame Throwing* (2). Fire spells reach further. Your Scorch may be cast while moving. *Improved Fire Blast* (3). Your Fire Blast refreshes Ignite. It may be cast while casting. A critical resets its cooldown.
- **Gate 10, 8.** *Incinerate* (2). Fire Blast consumes Ignite for burst damage. Scorch does as well. *Improved Flamestrike* (3). Flamestrike leaves burning ground. It applies Ignite. It follows a marked target. *Pyroblast* (1). Hurls an immense fiery boulder that causes 141 to 188 Fire damage and an additional 56 Fire damage over 12 sec. *Burning Soul* (2). Your fire spells cannot be pushed back. Your threat from Fire is reduced.
- **Gate 15, 9.** *Improved Scorch* (3). Your Scorch applies a stacking fire vulnerability. The stack persists through target death. At full stacks Scorch is free. *Master of Elements* (3). Your Fire criticals refund part of the spell's mana. The refund grows to the full cost. A Fire critical grants Clearcasting as well. *Critical Mass* (3). Your Fire criticals apply Ignite at double value and refund mana. They cannot be resisted, and two in a row make your next Fire spell instant. A critical on a burning target spreads the burn.
- **Gate 20, 10, hybrid seat.** *Blast Wave* (1). A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 187 Fire damage, and dazing them for 6 sec. *Frostfire* (3). *(cross-tree)* Your Fire spells apply Chill. Frostbolt benefits from Ignite. Blast Wave applies Frostbite. *Fire and Ice* (2). *(cross-tree)* Your Fireball applies Chill to targets already burning. All your Fire spells do the same. *Immolation* (2). *(subtraction node)* Your Fire damage over time effects deal double damage. Your direct Fire spells can no longer critically strike. *Arcane Kindling* (2). *(reciprocal)* Your clearcasting does not break when a Fire spell is resisted. Your Arcane Missiles applies Ignite at reduced value.
- **Gate 25, 5.** *Fire Power* (5). Ignite ticks faster. It spreads further. It applies to Blast Wave. It cannot be outpaced by healing. It detonates on expiry.
- **Gate 30, 1.** *Combustion* (1). Your Fire spells build heat as they land, each critical strike making the next more likely, until one of them consumes the accumulated heat entirely.

<!-- END GENERATED -->

The tree needed about a quarter of the work the others did, and per Section 21 the class that owns it still has the most repetitive rotation in the game. Fire mage is the proof that a good tree and good gameplay are separate problems, and it should be read alongside its own rebuild rather than instead of it.

### 19.5 Arms, redone

Section 6 predates the tier arithmetic correction, the classifier review, the aura rule, the sparse-tier finding, the weapon fork as a shared component, and Section 5.7's cross-tree rule. Its worked example was written to demonstrate a method that has since changed in six places.

Rather than rewrite Section 6, it stays as the record of how the method started, with this note attached. The current-rules Arms is:

Weapon specialization collapses into the shared fork, as in Combat rogue, Enhancement, and Fury. Deflection, Two-Handed Weapon Specialization, Improved Overpower, Impale, and Improved Heroic Strike go to the dividend. Gate 20 is checked against REG-18; Arms holds twelve points there, which is healthy, so it needs no rebalancing. Mortal Cleave passes Section 5.7's rule and stays. Sure Strike stays as the Resolute Technique port. Mortal Strike stays as the capstone. Tactical Mastery, Deep Wounds, and Sweeping Strikes were already behavior and are unchanged.

**Twenty-seven of 27 trees complete.**

### 19.6 Compliance audit

The rules in Section 5 did not all exist when the first rebuilds were written. Section 6 predates six of them. So every rebuild was audited against the final rule set, and three kinds of gap were found and closed.

**Five trees had no subtraction node.** Balance, Beast Mastery, Subtlety, Destruction, and Protection warrior. All five now have one, and two of them turned out better for the delay: Subtlety's *Silent Death* deals no damage from the front, which is the exact mirror of Combat's *Duellist*, so the two rogue trees close opposite doors. That symmetry would not have occurred to anyone writing them separately.

**Five gate-20 tiers were still under eight points** after their own rebuilds: Marksmanship at seven, Enhancement, Protection paladin, Discipline, and Affliction at six. Given that REG-18 identified starved hybrid tiers as the most common structural fault in vanilla, leaving five rebuilt trees with the same fault would have been an obvious inconsistency. All five are now at eight.

**Every rebuild carries at least one sideways node and one subtraction node**, and no capstone is a passive aura. The three that were, Trueshot Aura, Leader of the Pack, and Sanctity Aura, are in the dividend; Power Infusion and Innervate stayed because pressing them is a decision.

The audit is worth recording rather than quietly fixing, because it is the same failure that produced every other correction in this project: a rule was established, the passage that prompted it was fixed, and the rest of the document was not swept.

---

## 20. The absorbed trees

Class Absorption proposes seven new trees, one per host class, with priest and druid deliberately left empty. Those trees are downstream of this document, so this section states which rules they already satisfy, which they do not, and where the two documents actually conflict.

| Host | Tree | Local mechanic | 20-point mark | 31-point capstone | Verb |
|---|---|---|---|---|---|
| Paladin | Blackguard | Blight | Blood Rite | Damnation | Fallen |
| Mage | Necromancy | The Risen | Raise Skeleton | Command the Damned | Taught |
| Warlock | Metamorphosis | Fel corruption | Fel Aegis | Metamorphosis | Taken |
| Rogue | Bladedancer | Momentum | Whirling Blades | Unending Dance | Copied |
| Shaman | Conduit | Empowerment | Elemental Bond | Confluence | Granted |
| Warrior | Runeblade | Rune charges | Hoarfrost | The Runeblade | Forged |
| Hunter | Survival, reworked | Offensive traps | Coordinated Assault | Hunt as One | Earned |

Each is a fourth tree alongside the host's existing three, splashable rather than exclusive, carrying 57 to 64 available points across rows one through six.

### 20.1 They found the mid-tree seat first

Class Absorption's fluid trees argument establishes a twenty-point mark and a thirty-one point capstone as the two-signature structure of every absorbed tree, on the reasoning that a player at 20 points should get something real and thematically consistent rather than a consolation prize.

That is Section 5.3's hybrid seat, reached from the other side. This document arrived at it through arithmetic on the point budget. That document arrived at it through the problem of what a splashed tree owes a player who does not commit. Same conclusion, different route, and neither was written with the other in view. Both stated the seat as twenty points and both are off by one, per Section 1.1.

The practical consequence is that the absorbed trees are already compliant with the hardest of the five rules, and the vanilla trees are the ones that need to catch up.

### 20.2 What they already satisfy

Points buy behavior, mostly. Every local mechanic in the table above is a behavioral system rather than a stat curve. Blight, rune charges, momentum, and offensive traps all change what a character does. None of them is a percentage.

No new resource bars. Each tree layers its mechanic onto the host's existing resource rather than importing a new one. That decision was made for engineering reasons but it happens to be the same instinct as Section 3's separation of concerns.

Tree shape is unchanged. Seven rows, standard row gates, 57 to 64 available points with roughly half left behind in any build. That matches the target this document sets for rebuilt vanilla trees, which means the two sets will sit side by side without one looking foreign.

### 20.3 Where the two documents conflict

One real conflict, and it is load-bearing.

**The depth dividend does not calibrate against an absorbed tree.** Section 5.1's entire defensibility rests on a tuning method: sum the flat bonuses a canonical vanilla build already buys, and hand that sum back as a curve. Net power unchanged.

An absorbed tree has no canonical vanilla build, because it never existed. There is nothing to sum. So either the absorbed trees receive no depth dividend at all, or their curve gets set by feel, which forfeits the power neutrality that is the whole political case for Section 5.1.

The recommendation is the first option. Absorbed trees grant no stat curve. Points in them buy behavior, and the local mechanic is the reward for depth.

That is not a compromise, it is the better answer anyway, because it protects Class Absorption's own rule that no tree may be mandatory for its host class's existing role. A free stat curve attached to a fourth tree is precisely the mechanism by which that tree becomes a tax. A protection paladin who gains armor for fifteen points in Blackguard will take fifteen points in Blackguard, and the tree has failed on its own terms.

The asymmetry needs stating plainly in both documents, because a player looking at four trees where three grant a passive curve and one does not will read it as an oversight unless it is explained.

### 20.4 What still needs a pass

**Rank structures.** Section 5.2 requires that a rank add a discrete effect rather than scale a number. The absorbed trees were built before that rule existed and almost certainly contain multi-rank nodes that scale. Every tree needs the same audit run on it that Section 1 runs on Arms.

**Damnation and the subtraction rule.** Damnation has already been flagged as needing to become toggleable in the manner of Shadowform, with permanence moved into the acquisition chain rather than sitting in the mechanical capstone. That is the same Shadowform precedent Section 5.4 leans on for subtraction talents. These are one idea rather than two, and both documents should cite it the same way.

**World-facing rewards do not apply here.** Section 5.5 attaches world-facing capabilities to depth in vanilla trees. The absorbed trees should not also get them. They are already world-anchored through acquisition, since every one of them is obtained by going somewhere specific and doing something specific. Adding depth-granted world effects on top would be double-dipping and would blur the cleanest distinction between the two sets of trees: vanilla trees reach into the world through depth, absorbed trees reach into it through the chain that grants them.

**Fist weapon itemization.** Already an open item in Class Absorption, and Section 6's Weapon Mastery node makes it slightly worse. If equipped weapon type drives talent behavior in rebuilt vanilla trees as well as in Bladedancer, then vanilla's thin fist weapon lane is now blocking two systems rather than one.

### 20.5 For the visualization

Three notes for Claude Design, since both documents feed the same build.

The talent rework adds a classification axis that did not exist before. Every node in every tree, vanilla or absorbed, can be tagged as buying a number, buying an effect, or buying a button. That is renderable, and it makes Section 1's audit visual rather than tabular. Vanilla Arms colored by what each node buys is almost entirely one color, and it is a more persuasive argument than the table.

A before and after toggle on the Arms tree is the single most demonstrable idea in this document, in the same way the Bladedancer weapon fork is the most demonstrable idea in Class Absorption. One control, two states, same seven rows. It shows the claim rather than asserting it.

Tiers 5 and 6 should be emphasized across every tree in the build, not just the absorbed ones. Both documents treat the mid-tree as the hybrid seat, so it is shared vocabulary across the whole class dataset and should read as a band rather than as per-tree decoration.

---

## 21. What does not change

Worth stating explicitly, because a proposal this large invites the assumption that everything is on the table.

51 points at level 60. Three trees. Seven rows. Five points per row to advance. A single capstone at row 7. Respec cost that escalates and decays, with no loadouts and no free swapping. Talent trainers in cities. The talent panel's visual structure and the arrows between prerequisite nodes.

Nothing here touches abilities learned from trainers, and nothing here changes gear.

---

## 22. What this does not fix

The cross-class audit produced one result that argues against this document, and it belongs here rather than buried.

Mage has the healthiest talent trees in the game. Fire forces 8 of 30, second lowest anywhere, and both Fire and Arcane reach the mid-tree having spent very few points on numbers. Mage gameplay is also the most repetitive in the game, described in its own guides as spam Frostbolt.

Good trees do not produce good gameplay. What constrains a vanilla mage is that the spell book holds three damage spells and the resource model is a mana bar with an eight minute Evocation. No amount of talent redesign touches either.

So the honest scope of this document is narrower than its length implies. It fixes what a talent point buys. It does not fix rotations, spell books, resource models, threat generation, or encounter design, and every one of those is a larger contributor to how a spec feels than its talent tree is.

Three specific things it will not fix, named so nobody expects otherwise:

**Numerically weak specs.** Shadow priest forces 11 of 30, among the best figures in the game, and still cannot hold a vanilla raid slot. Its problems are output and mana. A spec that is weak needs tuning or a role, not more interesting talents, and Section 5.1's depth coefficient is the right dial for that rather than anything in 5.2.

**Specs valued for what they give other people.** Enhancement shaman exists in raids for Windfury Totem. Marksmanship hunter for Trueshot Aura. Retribution paladin for blessings. Their logged personal output understates their value, and any rebalance driven by damage meters will overcorrect all three. This is a composition problem and it needs flagging before tuning, not after.

**Empty rotations.** Retribution paladin runs on auto attacks and passive procs, and guides defend that emptiness on the grounds that it leaves time to maintain blessings. Fixing the tree leaves a paladin with interesting talents and still nothing to press.

Where both a tree problem and one of these apply, fix the tree and tune separately, and do not let either claim credit for the other.

---

## 23. Open items

Honest gaps, in the order they need answering.

**The depth coefficients are unset.** Every number in 5.1 is a placeholder. Setting them requires simming a canonical build per spec, and that work has to happen before any of this can be evaluated for balance rather than for feel.

**Nine classes at roughly 150 nodes is the real cost.** Section 5.2 is a rewrite of nearly every talent in the game. This document shows the method on one tree. The remaining 26 are not sketched and should not be assumed easy.

**Hybrid tuning is a new obligation.** Section 5.3 creates 30/21 and 26/25 builds that need balancing. Vanilla never balanced hybrids because nobody played them. That changes here, and the tuning surface roughly doubles.

**Does the depth dividend apply to points in a third tree?** A 31/15/5 build gets three partial curves. Whether that should be additive, or whether the curve should be superlinear to discourage spreading, is unresolved and matters more than it sounds. Section 20.3 answers the related question for absorbed trees, which get no curve at all.

**The absorbed trees have not been audited against Section 5.2.** Seven trees, roughly 150 talents, built before the rank rule existed. That audit is a prerequisite to publishing the two documents as a set, because a reader who checks will find vanilla trees rebuilt to a standard the new trees do not meet.

**Leveling feel is untested.** The depth dividend front-loads stat gain smoothly, but a level 12 warrior with Bloodletting rank 1 and nothing else may feel weaker than a vanilla warrior with 2/5 Deflection. Early levels need a separate pass.

**Subtraction talents may not survive contact.** Section 5.4 is the most likely part of this to be cut, and the document should not depend on it. Two vanilla precedents now exist rather than one: Shadowform, and the Winter's Chill frost mage variant that raises the whole frost group's damage at the cost of roughly 5 to 10% of the mage's own. The second is the better citation, because it trades personal output for group output rather than trading one personal stat for another.

**Dead nodes need sorting from boring ones before any rebuild.** Section 1.2 establishes the category. Nobody has swept the 27 trees for it, and the sweep should happen before 5.2's rewrite budget gets estimated, since dead nodes free their points instead of consuming design effort.

**The rebuild order, revised after the classifier review.** Enhancement shaman and Demonology tied at 28, Feral Combat at 26, Retribution at 24, then Marksmanship, Protection paladin, Discipline, and Elemental at 23. Marksmanship was done first because it is the only tree on that list that is also its class's mandatory raid spec, which is still the right tiebreak. Enhancement shaman is the strongest remaining claim: tied worst on the floor, 94% flat overall, and 19 of the first 20 points forced, which makes an Enhancement splash almost pure filler.

---

## 24. Tier and rollout

Tier 3 throughout, using the vocabulary from the living world document. This changes how every character in the game is built, it cannot be retrofitted onto a realm with established characters without a global respec, and it is a launch decision for a fresh realm.

There is no Tier 1 version of this. Unlike seasons, which has a cosmetic-only subset that ships alone, a talent rework has no cheap partial. The one thing that could ship independently is the depth dividend in 5.1 without the node rewrites, which would leave every existing talent in place and simply hand out the stat curve for free. That would be strictly a power increase and is not recommended, but it is the only separable piece.

The precedent to cite is Season of Discovery, which already established that a Classic realm can carry substantially reworked class mechanics without being treated as a different game.

---

---

## Appendix: Provenance

Where every idea in this document came from. The point of recording it is partly honesty and partly usefulness: an idea taken whole from a shipped game carries evidence that it works, and an idea original to this project does not, and a reader is entitled to know which is which before deciding how much to trust it.

Six labels, used consistently here and in the other documents in this suite.

| Label | Meaning |
|---|---|
| **Taken** | Lifted essentially whole from a named source. The source did the design work. |
| **Adapted** | The mechanism is someone else's, changed to fit vanilla's constraints. |
| **Inspired by** | The principle is someone else's, the implementation here is different. |
| **Vanilla precedent** | Already exists somewhere in vanilla. This document systematizes it. |
| **Brendan** | Specified by the author in conversation, not derived from a source. |
| **Derived here** | Follows from analysis performed in this project. |
| **Original** | No known source. Treat with the least confidence. |

### The proposals

| Idea | Provenance | Detail |
|---|---|---|
| Separation of concerns: gear carries numbers, tree carries behavior | **Taken**, Diablo 4 Lord of Hatred | Stated openly in its design notes. Raw stat growth was stripped off the Paragon board and moved to itemization; the skill tree governs how skills function rather than how much damage they deal. |
| Depth grants numbers, points buy behavior (5.1) | **Brendan** | Specified directly in the brief: if stat increases stay, they should be passive for that level of the tree rather than purchased. |
| Depth as a per-tree stat curve, mechanically | **Adapted**, Grim Dawn | Grim Dawn's mastery bar grants base attributes per point and unlocks tiers. This version removes the purchase and grants the curve free, which Grim Dawn does not do. |
| Deleting flat nodes buys design freedom | **Taken**, Diablo 4 Lord of Hatred | Every dedicated passive node was removed, including the Key Passive capstones, on the stated grounds that they diluted engagement. |
| Tag conversion as the source of build variety | **Taken**, Diablo 4 Lord of Hatred, and taken late | Recorded in Section 3 as a correction. The mechanism was quoted in the original research and only the hygiene lessons were carried across. Worked out in `tag-conversion.md`. |
| Ranks stack discrete effects rather than scaling numbers (5.2) | **Brendan**, with the ratio **taken** from Lord of Hatred | The instruction to pull out flat damage and timer increases is Brendan's. The three-transformative-plus-four-adjustment ratio is D4's. |
| The mid-tree hybrid seat, the arithmetic (5.3) | **Derived here**, and corrected twice | First stated as 31/20 reaching tier 5, which was wrong: a gate is points already invested, so tier 5 costs 21. The corrected shapes are 31/20 for a capstone plus tier 4, or 30/21 and 26/25 for two deep talents and no capstone. |
| The mid-tree hybrid seat, the evidence | **Vanilla precedent**, warlock | Both canonical warlock raid builds are a tier 6 talent plus a tier 5 talent and neither takes a capstone. Warlock is the only vanilla class with two competing viable raid builds. Found during the cross-class audit, after the arithmetic. |
| Sideways modifiers: talents in one tree modifying another tree's abilities | **Adapted**, Grim Dawn | Grim Dawn's modifier system routinely crosses the dual-mastery boundary. Requires no new interface, only talents written to point sideways. |
| Subtraction talents (5.4) | **Taken**, Path of Exile | Keystones. Resolute Technique, Chaos Inoculation, Blood Magic. Sure Strike in Sections 6 and 7 is a direct Resolute Technique port. |
| Subtraction talents, the argument for a Classic audience | **Vanilla precedent** | Shadowform, and the Winter's Chill frost mage variant that raises the whole frost group's damage at the cost of 5 to 10% of the mage's own. The second is the better citation. |
| World-facing depth rewards (5.5) | **Original** | The join to the living world document. No known source and the weakest-supported proposal here. |
| Weapon Mastery as an equipped-weapon fork | **Taken**, this project | The Bladedancer weapon fork from Class Absorption, reused. |
| Trueshot Aura moved from capstone to depth reward (7.1) | **Derived here** | Follows from 5.1 plus the audit finding that the mandatory raid spec's capstone is a flat buff given to other people. |
| Talents that are dead rather than boring (1.2) | **Derived here** | From the cross-class audit. Grounded in a protection paladin tanking guide and a vanilla-era priest forum post, neither of which framed it as a category. |
| The forced-flat floor measure | **Original** | Computed from client-accurate tree data, then hand-reviewed. No known prior work applying it to vanilla trees. Section 13 of `spec-grievances.md` records the review, which changed the rebuild order. |
| Keeping the 51-point budget fixed while D4 raised its cap | **Derived here** | Power neutrality is the political case for the rework, and handing out more points forfeits it. |

### What was rejected, and from where

| Idea | Source | Why not |
|---|---|---|
| Loadouts and free talent swapping | Dragonflight | Turns talents into an encounter-by-encounter equipment slot, contrary to respec cost being a real decision. |
| Per-ability skill trees | Last Epoch | The endpoint of this direction. The further you push toward it, the less the result resembles the game. |
| Behavior-only talents as the whole system | Mists of Pandaria | Solved the flat-stat problem completely and removed progression with it. Every character of a spec became identical. |
| Trimming filler without replacing it | Cataclysm | Produces a shorter list of obligations rather than more choices. |

### The findings that changed the document after it was written

All **derived here**, from the cross-class audit in `spec-grievances.md`, and each one reversed or narrowed a claim in the first draft.

- The floor is a lower bound rather than a prediction. Rogue has healthy trees and flat builds anyway, which made 5.1 the load-bearing proposal and 5.2 the supporting one, the reverse of the original weighting.
- Good trees do not produce good gameplay. Mage has the healthiest trees and the most repetitive rotation, which is why Section 10 exists.
- Some talents are dead rather than boring, which added 1.2.
- Arms was the wrong tree to rebuild first, which is why Section 7 exists and Section 6 now says so.
