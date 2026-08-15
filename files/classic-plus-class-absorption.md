# Classic+ Class Absorption: New Archetypes as Trees, Not Classes

**Version 1.2 | August 2026**

*Revision 1.4 adds two candidate original trees, Dreamer and Radiance, in Sections 9.10 and 9.11, and establishes in 7.9 the distinction between absorbed and original trees that the document did not start with. Revision 1.3 added Chronomancer as an eighth tree, in Sections 7.8 and 9.9, and corrected the twenty-point arithmetic in 9.1. Revision 1.2 added Section 9, which builds the trees row by row. That pass produced one correction to 7.1: no absorbed tree should import a new resource bar, and each uses a local mechanic layered on the host's existing resource instead. It also establishes the two-signature-talent structure, a twenty-point mark for hybrids and a thirty-one point capstone for the archetype, which is the structural answer to Section 6. All seven trees are also maintained as structured data in trees.json, whose worldAnchors field joins to the world document's zones, since every tree is acquired by going somewhere. The Bladedancer tree also forks on equipped weapon, so one tree presents as either the duelist or the martial artist without a talent point spent on the choice.*

*Revision 1.1 expands Section 8 from a short note into the document's central argument: these archetypes are acquired rather than innate, they were Warcraft III heroes, and the acquisition verb should differ per tree. Also revises 7.4 to carry the monk fantasy explicitly through fist weapons and vanilla's vestigial unarmed skill.*

*Companion document to the Classic+ living world design proposal. That document concerns world texture and is almost entirely additive and post-launch. This one is the opposite: it is the most revisionary proposal in either document and belongs to a fresh realm by definition. The two share a method and a tier vocabulary, and nothing here depends on anything there.*

---

## 0. Status and Scope

Classic+ remains unconfirmed as of July 2026. This is a design proposal rather than a prediction, and it assumes nothing about what Blizzard intends.

It also assumes two things that are not in vanilla and are commonly discussed for Classic+: paladin available to the Horde and shaman available to the Alliance. Without that, several proposals below break on faction availability rather than on design. With it, the faction problem disappears entirely and can be set aside.

The scope is the roughly two decades of class design that came after vanilla: Death Knight, Demon Hunter, Monk, Evoker, and the archetypes that arrived as specs rather than classes. The question is not whether that material is good. Much of it is. The question is what shape it should take in a game built on 51 points and three trees.

---

## 1. The Proposal

Do not add classes. Add trees.

Every post-vanilla class is decomposed into the fantasies it actually contains, and each fantasy is placed on the vanilla class that can already reach it. Death Knight becomes a fourth paladin tree. Metamorphosis returns to warlock. Necromancer becomes the shadow school mage never had. The specs that existed only because a class needs three are merged or dropped.

The unit of design is the archetype, not the class. Blizzard bundled Havoc and Vengeance into one class because a class needs specs, not because a glaive-throwing duelist and a demon-form tank are the same idea. Once that bundling is undone, most of this material has an obvious home.

**Three claims follow from it, and each is argued below:**

1. New classes are expensive in ways trees are not, and most of the expense buys nothing.
2. The game has already done this repeatedly, including once in a Classic context.
3. Fourteen specs across four post-vanilla classes reduce to roughly seven trees, and the ones that vanish are the ones that existed for structural reasons. An eighth tree, Chronomancer, reduces nothing and exists because the fantasy is available and its host needs it.

A fifth claim emerged while building the trees in Section 9: none of these needs a new resource bar, which removes the last technical objection. A fourth claim emerged while writing Section 8 and is arguably the most important: these archetypes are all things a character *becomes* rather than things a character *is*, which means they should be acquired through the world rather than granted in the talent pane, and that single decision solves most of the objections to the rest.

---

## 2. What a New Class Costs

The case against new classes is not that they are hard to balance, though they are. It is that a class is a bundle of commitments and most of them are unrelated to the fantasy anyone actually wanted.

**A class needs three specs whether or not it has three ideas.** This is the central problem. Death Knight needed a tank, and got Blood. It also needed two more, so Frost and Unholy were built to fill slots. Both are good, but neither was demanded by the fantasy, and Unholy in particular is a necromancer wearing plate because there was a slot to fill rather than because the Scourge fantasy required a pet build.

**A class needs a starting experience.** Death Knight got Acherus and one of the best introductory sequences Blizzard has ever built. Demon Hunter got Mardum. These are expensive, they are played once, and they are content that cannot be patched in incrementally.

**A class needs an itemization lane.** Every tier, every dungeon, every quest reward table has to account for it. In vanilla's design, where itemization is thin and hand-built, this is a heavier tax than it is in a modern expansion.

**A class needs faction and race decisions** that constrain the world permanently.

**A class cannot be shipped in a patch.** A tree can. In the layering terms used in the companion document, a class is a launch decision and a tree is a content update. That difference is the practical argument, and for a game whose whole premise is a long slow additive cadence, it is decisive.

A tree needs none of that. It needs talents, a resource decision, and a reason to exist.

---

## 3. Four Precedents

This is not a new idea, and three of the four precedents are Blizzard's own.

### 3.1 Druid is the proof of concept and it shipped in 2004

Druid is one class containing three roles, three armor-relevant forms, and three separate resources. Bear tanks on rage. Cat does melee damage on energy. Caster heals or nukes on mana.

If a rage-driven melee tank and a mana-driven healer can live under one class banner in vanilla, the claim that any modern class needs to be its own class is much weaker than it appears. Druid also demonstrates the exact technology this proposal depends on, which is a form that changes resource, animation set, and role without changing class.

### 3.2 Metamorphosis was a talent before it was a class

The strongest single piece of evidence. Metamorphosis is adapted from the Warcraft III Demon Hunter ability and is visually based on Illidan's demon form. Blizzard implemented it as a Demonology warlock talent in Wrath of the Lich King, at the bottom of the tree, where it sat for three expansions as the defining ability of that spec [1][2].

It was removed from warlocks in patch 7.0.3, specifically because the Demon Hunter class was being introduced [1][2].

So the direction of travel is the reverse of what people assume. The demon hunter fantasy lived inside an existing class first, worked there for years, and was taken out to make room for a class. This proposal is not inventing anything. It is declining to make that trade.

### 3.3 Season of Discovery already did this in a Classic context

The closest precedent and the most recent. Season of Discovery's rune system gave vanilla classes roles they never had. Warlocks became tanks through the Metamorphosis rune, which grants a permanent demon form with a large armor multiplier, converts Shadow Bolt into Shadow Cleave, and multiplies threat [3][4]. Rogues and shaman also gained tanking, and mages gained healing [3][5].

Two things matter here. First, it worked, in the sense that warlock tanking was viable and popular rather than a novelty. Second, and more important for this document, Blizzard chose to deliver those roles by modifying existing classes rather than by adding new ones, in exactly the design context this proposal is about.

Season of Discovery also demonstrates the delivery mechanism. The Metamorphosis rune was gated behind a long multi-stage quest chain running through Redridge, Darkshore, the Barrens, Shadowfang Keep, Blackfathom Deeps, and a summoning ritual at Demon Fall Ridge in Ashenvale [6]. That is how an archetype should be acquired, and Section 8 returns to it.

### 3.4 Blizzard arrived here themselves, twenty years later

The War Within introduced hero talents: subtrees layered onto existing classes, each shared by two specs, selected at level 71 and filled out by 80 [7][8].

The content of those trees is the tell. San'layn, Rider of the Apocalypse, Deathbringer, Dark Ranger, Slayer, Mountain Thane, Colossus, Lightsmith. These are Warcraft archetypes that in an earlier era would have been argued about as candidate classes, and Blizzard shipped them as subtrees on classes that already existed. Their own framing describes them as functioning like subclasses [9].

The relevant detail for this proposal is that each hero tree is shared between two specs rather than owned by one. That is the fluid model argued for in Section 6, arrived at independently.

---

## 4. The Test

A quick test sorts most candidates, and it asks three questions. Does the archetype need a resource the host class cannot reach? An armor class the host does not wear? A role the host cannot fill?

One of those is a tree. Two is difficult. All three is a genuine class.

- **Demon Hunter on warlock.** Role is new (tank). Resource and armor are reachable, and the form precedent exists. One. Tree.
- **Necromancer on mage.** Nothing is new except a pet and a school. Zero. Tree.
- **Death Knight on paladin.** Plate, melee, self-sustain, all present. Runic power is the only gap, and runes are a talent-tree resource in the same way energy is a form resource for druids. One. Tree.
- **Evoker on shaman.** Mail, ranged caster, healer, elemental theme. Zero. Tree, and an easy one.
- **Monk.** Needs an energy melee DPS, a tank with a unique mitigation model, and a healer built on an inverted damage loop. Three roles across two armor types with a resource nothing else uses. Three. This is a real class, and it is the only one on the list.

The test's value is that it fails honestly. It does not conclude that everything can be absorbed. It concludes that Monk mostly cannot, which is worth knowing.

---

## 5. Absorb Mechanics, Not Identities

The most important rule in this document, and the one that resolves the awkward placements.

When a fantasy moves onto a host class, take the mechanics and leave the name. A rogue tree with glaives, fel-flavored mobility, a double jump, and a forward cleave is not a demon hunter, and should not claim to be. It is a rogue tree about mobility and cleave, and it is better for not claiming otherwise.

This matters for three reasons.

**It removes the lore burden.** A rogue does not have to explain demonic corruption, an Illidari initiation, or burning out their own eyes. The mechanics were the good part. The origin story was the part that needed a starting zone.

**It prevents the comparison.** If a tree is called Demon Hunter, every player measures it against the retail class and finds it incomplete. If it is called something else and simply plays well, there is nothing to measure against.

**It respects what the host class already is.** Warrior's defining trait in vanilla is having no magic. A tree that gives warrior an enchanted weapon is a small, careful step. A tree that makes warrior a spellcaster is a different class wearing warrior's name.

The corollary is that the name should come from Warcraft's own vocabulary rather than from the retail class. Warcraft III and vanilla lore are full of unclaimed archetype names, and using them is the same method the companion document uses everywhere: build on what the world already asserts.

---

## 6. Fluid Trees

Vanilla has no specs. It has 51 points across three additive trees, and nothing stops a player putting 20 in one and 31 in another. This is the strongest objection to the whole proposal, because a fourth tree is not an identity a player assumes, it is an option they splash.

The wrong answer is exclusivity. Locking a tree, or making it consume the character, imports a modern design convention into a game whose talent system is defined by not having one. It would be the single most un-Classic change in this document.

The right answer is to build the trees so partial investment is a legitimate outcome rather than a failure state.

**What that means in practice:**

- **The tree's identity concentrates at the bottom.** A player at 20 points gets real, useful, thematically consistent benefits. A player at 31 gets the capstone that defines the archetype. This is exactly how vanilla's existing deep talents work, and Metamorphosis at the bottom of Demonology is the model [1].
- **Capstones are transformative, not incremental.** Metamorphosis, a permanent rune blade, a raised undead servant. These are things a character either has or does not, which means the deep investment reads as a commitment without any rule enforcing it.
- **Splashing produces hybrids, and hybrids are correct.** A paladin with 20 points in the death tree is a knight touched by something cold. That is a character concept, not a broken build. Vanilla is full of these and they are one of the reasons people still play it.
- **No tree may be mandatory for its host class's existing role.** If protection paladins end up needing 15 points in the death tree, the tree has failed. Each new tree must be an alternative to the existing three, never a tax on them.

The result is that the new trees behave exactly like the old ones. That is the whole point, and it is why the fluidity is a feature rather than a problem to solve.

---

## 7. Class by Class

Each entry gives the archetype, the mechanical case, the lore case, and what is deliberately left behind.

### 7.1 Paladin absorbs Death Knight

**The archetype.** The fallen knight. Plate melee with a dark self-sustain engine, disease, and command over the dead in a limited, personal way.

**The mechanical case.** Paladin already wears plate, fights in melee, and is built around self-sustain. The death tree inverts each of these rather than adding new categories: healing becomes leeching, blessings become presences that cannot be shared, the paladin's aura becomes something that harms rather than helps. Runic power is the resource gap, and it should be handled the way vanilla handles druid energy, as something the deep tree grants rather than something the class has from level one.

Blood's core loop translates cleanly. A strike that heals for a portion of damage dealt, shields built from overhealing, and diseases that pay out on other abilities. None of that requires machinery vanilla lacks.

**The lore case.** This is the strongest thematic placement available, and the game already made the argument. Arthas was a paladin. The Death Knight fantasy is not adjacent to the paladin fantasy, it is the paladin fantasy corrupted, and Warcraft III spends an entire campaign on the transition. A player who has taken a paladin to 60 and then invests in the death tree is retracing the most famous character arc in the setting.

The Light and the Scourge are also mechanically opposed in vanilla's own fiction, which gives the tree a natural set of restrictions. A paladin deep in the death tree losing access to certain Light abilities is a flavor consequence rather than an exclusivity rule.

**What is left behind.** Frost as a separate identity, and the Ebon Blade organization. This tree is a paladin who fell, not a member of an order with a floating necropolis.

**Tier 3, fresh realm.**

### 7.2 Mage absorbs Necromancer

**The archetype.** The shadow scholar. A caster who raises disposable dead, spreads plague, and drains.

**The mechanical case.** Vanilla mage is organized by school: arcane, fire, frost. Shadow is the conspicuous absence, and adding it as a fourth tree is structurally identical to what already exists rather than a new kind of thing.

The pet question is where this earns its place. Vanilla mage has no pet at all, so nothing is taken from anyone, and the necromancer's dead are mechanically distinct from the warlock's demon in every way that matters. The warlock's pet is singular, permanent, bonded, and named. The necromancer's are plural, disposable, expiring, and anonymous. One is a relationship. The other is ammunition. That difference is large enough to sit on separate classes without the two feeling redundant.

The rest of the kit is a caster with damage over time, which mage lacks and which gives the tree a distinct rhythm from the burst-oriented existing trees.

**The lore case.** Necromancy in Warcraft is explicitly taught, not innate. Kel'Thuzad was a Dalaran mage and a member of the Kirin Tor before founding the Cult of the Damned, and Scholomance exists in vanilla as a school where necromancy is taught to students. The path from mage to necromancer is the best documented magical career change in the setting, and both endpoints are already in the game.

Scholomance also solves acquisition, discussed in Section 8.

**What is left behind.** Unholy Death Knight's plate melee framing entirely. This is the necromancer as Warcraft III presented it, a robed caster who commands rather than fights.

**Tier 3, fresh realm.**

### 7.3 Warlock reabsorbs Metamorphosis

**The archetype.** The demon-form bruiser. A caster who becomes the thing they summon.

**The mechanical case.** This is the easiest placement in the document because it already existed and worked [1][2], and because Season of Discovery has since demonstrated it specifically as a tanking spec in a Classic ruleset [3][4]. The form technology is druid's. The fel magic is warlock's. The threat model is solved.

The SoD implementation is a reasonable starting point: permanent form rather than a cooldown, a large armor multiplier, Shadow Bolt converting to a cleave, and a threat multiplier on everything [4]. Where this proposal would differ is in making it a talent capstone rather than a rune, so that it obeys the same investment logic as everything else.

**The lore case.** Warlocks and demon hunters draw on the same power from opposite directions. The warlock enslaves demons and risks becoming one. The demon hunter takes fel power deliberately and fights what it came from. In a talent tree that reads as a warlock who went too far, the difference is a matter of intent, which is a better story than a separate class and matches how vanilla warlock quests already talk about the risk.

**What is left behind.** The Illidari, and the demon hunter as an organization or a night elf tradition. This is a warlock's own transformation.

**Tier 3, fresh realm.**

### 7.4 Rogue absorbs the duelist and the martial artist, merged

**The archetype.** Mobile melee flow. Leaps, rolls, sustained movement, and damage spread across several targets rather than concentrated in a burst on one.

**The mechanical case.** Havoc Demon Hunter and Windwalker Monk are the same shape. Both are leather, both run on energy or an energy analogue, both are built on mobility and multi-target melee, and both have a gap closer. Kept separate on the same host they would compete for the same points and the same players. Merged, they are one coherent alternative to vanilla rogue's single-target burst identity, and they give rogue the thing it most lacks, which is a reason to be in a fight with more than one target.

Combo points carry the design without new machinery. Build on movement and single strikes, spend on a spinning multi-target finisher rather than a single-target one.

**Preserving the monk feel specifically.** Monk does not need to be a class and it does not need three specs, but the thing that made Windwalker distinctive was never its spec count. It was rhythm and unarmed martial tradition, and both survive the merge if they are protected deliberately.

- **Fist weapons.** Vanilla rogues can already use them and almost nobody does, because nothing rewards it. This tree should. That is a weapon type already in the game, already itemized at several levels, currently vestigial.
- **The Unarmed weapon skill.** Vanilla has one. It exists, it can be levelled, and it is functionally pointless. Making it viable inside exactly one tree is the cheapest possible way to give that tree an identity nothing else in the game has, and it is the same method the companion document uses everywhere: make something the game already contains actually mean something.
- **A roll, not a sprint.** Rogue has Sprint. What it lacks is a short directional tumble on a low cooldown, which is what makes the monk fantasy read as flow rather than speed.
- **A spinning finisher and a sweeping control effect.** Rogue has Kidney Shot for one target. A combo-point AoE stun and a spin finisher complete the kit without inventing a resource.
- **Rhythm over burst.** Vanilla rogue is stealth, opener, burst, vanish. This tree should be the opposite: no opener dependency, continuous uptime, damage that comes from never stopping. That is a genuinely different way to play a rogue and it is the actual monk contribution.

**The lore case.** This is the placement that most needs Section 5's rule, applied twice. Do not call it a demon hunter and do not call it a monk. Warcraft has an unclaimed melee duelist tradition available in the Blademaster and the Aldrachi glaivemasters, and the Pandaren Brewmaster was a hireable Warcraft III hero rather than a race requirement [10][11].

That last point matters. Building this as a pandaren tradition would import a race, a homeland, and a whole expansion's worth of material. Building it as a martial tradition imports a fighting style, which is all that was ever needed.

**What is left behind.** The demon identity entirely, along with spectral sight and fel corruption. From monk: chi as a separate resource, Brewmaster, Mistweaver, and any pandaren framing.

**Tier 3, fresh realm.**

### 7.5 Shaman absorbs Evoker

**The archetype.** The ranged elemental caster with empowered casts and a group-support role.

**The mechanical case.** Almost nothing here is new to shaman. Mail, ranged casting, healing, and elemental damage are the class's existing description. Evoker's distinguishing mechanic is empowerment, where a spell's strength scales with how long it is held, and that is a clean fit for a class whose identity is channeling forces rather than commanding them.

Augmentation deserves particular attention, because it is the one genuinely novel role in modern WoW and it is closer to shaman than to anything else. A support spec that buffs allies rather than dealing damage directly is the totem fantasy aimed at a person instead of at the ground. Shaman is the only vanilla class where that reads as an extension rather than an import.

**The lore case.** Dragonflight-era Evoker lore does not exist in a Classic timeframe and should not be imported. What does exist is the shaman's relationship with the elements and, if a dragon connection is wanted, the black and red dragonflights' presence in vanilla. The safer read is to drop the dragon framing entirely and build the tree as elemental empowerment, which is what the mechanics actually are.

**What is left behind.** Dracthyr, the visage form, Dragon Isles lore, and the flight mechanics. All of it is post-Classic and none of it is load-bearing.

**Tier 3, fresh realm.**

### 7.6 Warrior absorbs the runeblade, narrowly

**The archetype.** A warrior whose weapon is enchanted with cold. Not a caster.

**The mechanical case.** This is the most restrained entry and it should stay that way. Frost Death Knight's translatable core is a weapon that carries an effect: strikes that slow, a weapon enchantment that procs, damage that lands as frost rather than physical. Rage remains the resource. No runes, no diseases, no raised dead, no magic school.

**The lore case.** Warrior's identity in vanilla is defined negatively. It is the class with no magic, and that absence is the point. A runeblade tree respects this because the magic belongs to the weapon rather than to the character, which is how enchanted weapons already work for everyone.

Vanilla supports the framing directly. Runeblades are forged objects in Warcraft lore, and a warrior who carries one has acquired an item rather than a power.

**What is left behind.** Everything else about Death Knight. This tree is deliberately smaller in ambition than the others, and any attempt to grow it into a full DK on warrior should be refused.

**Tier 3, fresh realm.**

### 7.7 Hunter absorbs melee Survival

**The archetype.** The close-range trapper. A hunter who fights beside the pet rather than behind it.

**The mechanical case.** This is the least disruptive entry in the document because the tree already exists in name. Vanilla's Survival tree is a partial version of this idea, full of traps, melee-adjacent talents, and defensive utility, and it is generally considered the weakest of the three precisely because it never committed.

Committing means mail, melee weapons, and a kit built around traps used offensively rather than as escapes, with the pet as a coordinated partner. The 2016 Survival rework is the reference, though the vanilla version should be considerably simpler.

**The lore case.** No import needed. Rexxar exists in Warcraft III and in vanilla, fights in melee alongside Misha, and is the archetype fully realized. A hunter tree that produces Rexxar is a tree that produces something the setting already contains.

**What is left behind.** Nothing significant, which makes this the cleanest entry on the list.

**Tier 2, and arguably shippable outside a fresh realm**, since it is a rework of an existing underperforming tree rather than an addition. This is the only entry in Section 7 with that property.

### 7.8 Mage also absorbs the chronomancer

**The archetype.** The time mage. A healer who does not add health but returns a target to health they previously had.

**The mechanical case.** The absorption test in Section 4 asks for a resource the host cannot reach, an armor type the host does not wear, and a role the host cannot fill. Chronomancer needs one of the three. Mana is already the resource and cloth is already the armor. Only the role is new, which is the same result the test gave for Demon Hunter on warlock and Evoker on shaman.

It also gives mage two absorbed trees and five in total, which no other host has. That asymmetry is deliberate and the reason is not symmetry but the talent audit. **Mage has the healthiest talent trees in the game and the most repetitive gameplay.** Fire forces eight of the thirty points to its capstone onto flat modifiers, the lowest figure of any tree, and Frost is described in its own guides as spam Frostbolt. The talent document says plainly that its rework is necessary and not sufficient, and names mage as the proof: what constrains a vanilla mage is that the spell book holds three damage spells. A second absorbed tree addresses exactly the problem the talent rework cannot, on the class where that problem is worst.

The healing model is what keeps this from being a priest in different colours. The local mechanic is Echo, a recorded snapshot of an ally's health that the tree spends to restore them to it. That produces a healer whose curve is the inverse of a priest's: strongest immediately after a spike because the record is still high, weakest under sustained damage because the record degrades with the target, and useless on someone who has been low for a while because there is nothing good to return them to. A priest is proactive and sustaining. A chronomancer is retroactive and burst-corrective. They are bad at different things, which is the test a fourth healing archetype has to pass.

**The lore case.** This is the best-anchored tree in the document and none of it needs inventing. Anachronos, child and heir of Nozdormu, has stood at the Caverns of Time in Tanaris since patch 1.9, gating access behind Brood of Nozdormu reputation. His questline sends a mortal to a Crystalline Tear in Silithus to watch the sealing of Ahn'Qiraj play out, in quests named Long Forgotten Memories and A Pawn on the Eternal Board.

Vanilla already contains a bronze dragon whose function is showing chosen mortals events that already happened, in a named place, behind a reputation gate, with a quest titled after remembering. The acquisition is recognising that one of the memories he shows you is yours.

**What is left behind.** All of it, deliberately. No travel to past zones, no bronze dragon form, no altering of events. The tree is time magic used on a health bar, which is small enough to sit inside a talent tree and large enough to be its own role.

**Tier 3, fresh realm.**

### 7.9 Two kinds of tree, and the distinction this document did not start with

Everything above absorbs something. A post-vanilla class or spec exists, the fantasy is good, the host can carry it, and the tree is the vehicle.

Chronomancer is not that. It has no retail source. It exists because the Bronze Dragonflight is in vanilla, because Anachronos gates a questline in Tanaris, and because mage needed something. Two further proposals in Section 9 are the same shape.

So the document now holds two categories and should say so rather than letting a reader discover it:

**Absorbed trees** take a fantasy that already shipped elsewhere and find it a vanilla home. Blackguard, Necromancy, Metamorphosis, Bladedancer, Conduit, Runeblade, and Survival. Seven.

**Original trees** take a fantasy vanilla asserts and never shows, and build it from nothing. Chronomancer, and the two candidates below. No retail source, no spec being reduced, and a much heavier burden of proof, because there is no shipped version to point at as evidence that it works.

That distinction matters for how each is argued. An absorbed tree's case is that the fantasy is proven and the host can hold it. An original tree's case has to be that vanilla already built the door and left it shut, which is a higher bar and one that only a few candidates clear.

### 7.10 Priest and Druid absorb nothing, which is not the same as needing nothing

Worth stating explicitly.

**Priest** already spans holy and shadow, already has the discipline framing, and already covers the ground that Mistweaver and modern priest specs occupy. The only genuinely distinct modern idea in its neighborhood is fistweaving, healing through melee attacks, and that is a talent rather than a tree.

**Druid** is the proof of concept, not a recipient. It already ships three roles, three resources, and three forms. Adding a fourth tree to the class that demonstrates the whole thesis would be a strange use of the idea.

---

**A correction to the above, added later.** Everything in this section is about *absorption*, and it holds: neither class has a post-vanilla spec worth importing. Mistweaver on priest is a talent at most, and druid already covers every role vanilla has.

That is not the same as saying neither could carry an original tree, and two candidates now exist.

Druid's case is the strongest lore case anywhere in this document. Vanilla built four portals to the Emerald Dream, at Twilight Grove, Seradane, Dream Bough, and Bough Shadow, put a corrupted dragon at each, dropped an object that quests to Keeper Remulos and proves to be Malfurion's ring, told the player he is inside fighting the Nightmare, and left every door shut. The argument in 7.9 about original trees needing a higher bar is met here more completely than anywhere else.

Priest's case is narrower and rests on one spell. Holy Nova has healed allies and damaged enemies in a single cast since launch, sits unused in the Holy tree, and has never had anything built around it.

Both are worked up in Section 9 as **candidates rather than commitments**, and the reasoning above is why: the role argument that excluded them was about absorption, and these are not absorptions.

---

## 8. Acquisition

This section grew because it turns out to be the load-bearing one. The acquisition method is not packaging around the trees. It is the thing that makes them coherent, and it resolves problems Sections 5 and 6 could only work around.

### 8.1 These are things you become, not things you are

Notice what every archetype in Section 7 has in common. Not one of them is a starting condition.

Arthas was a paladin, and then he took Frostmourne. Kel'Thuzad was a Kirin Tor mage, and then he studied necromancy and founded the Cult of the Damned. Illidan was a night elf sorcerer, and then he drank from the Skull of Gul'dan. Every one of these is a second act. The character existed, was already something, and then sought out or was subjected to a transformation.

That is not true of the vanilla classes. A warrior is a warrior at level one. Nobody becomes a rogue in a cutscene. The vanilla twelve are starting conditions, and their talent trees are refinements of what the character already was.

So the two kinds of tree are genuinely different in fiction, and they should be different in acquisition. A vanilla tree needs no quest because it describes what you have been doing since level one. An absorbed tree needs a quest because it describes something that happened to you.

This resolves the Section 6 problem more elegantly than any rule about points. The reason a fourth tree is not just a splash target is not that a rule forbids it. It is that the tree does not exist on your character until you go and get it.

### 8.2 The Warcraft III pattern

The lore support for this is stronger than it first looks, because almost every archetype in this document was a Warcraft III hero.

The faction rosters include the Death Knight, the Blademaster, the Demon Hunter, the Warden, the Lich, and the Dark Ranger. The neutral roster hired from taverns includes the Beastmaster, the Pandaren Brewmaster, the Naga Sea Witch, the Firelord, the Goblin Tinker, and the Goblin Alchemist [10][11]. The Necromancer was an Undead unit rather than a hero, but the archetype sits in the same body of material.

The relevant point is structural rather than a list. In Warcraft III, heroes are not unit types you train in bulk. They are individuals, recruited or risen, and the campaigns are largely about specific people becoming something they were not at the start. Arthas is the whole thesis: he begins the campaign as the Paladin hero and ends it as the Death Knight hero, and the transition is the story.

Absorbed trees acquired by quest reproduce exactly that structure. Vanilla classes are the units. The trees are what a unit becomes when something happens to it.

### 8.3 Seven ways to acquire, because they should not all be the same

The temptation is one formula: a long chain, an item at the end, done. That would make eight trees feel like eight copies of one quest. The better approach is to let the acquisition verb differ, because in the fiction it already does.

**Forged.** The runeblade. This is an object, not a power, which is the whole reason warrior can have it without becoming a spellcaster. The chain should produce a weapon and require someone who can make one.

**Taught.** The shadow tree. Necromancy in Warcraft is explicitly curriculum. Somebody teaches it, in a building, to students. The chain should be an apprenticeship with a named instructor, and Scholomance is sitting in the game already.

**Taken.** Metamorphosis. Nobody grants this and nobody teaches it. The warlock performs a ritual on themselves and it works or it does not. Season of Discovery's chain, ending in a summoning at Demon Fall Ridge, is already the right shape [6].

**Fallen.** The death tree. The only one that should be done to the character rather than by them, and the only one that should carry a real cost. A paladin does not apply to become a death knight.

**Earned.** The melee hunter tree. A master, a trial, and a demonstration. Rexxar is the archetype and the Beastmaster was a hero you hired rather than one you built.

**Granted.** The shaman tree. The elements agree or they do not, so the chain is a petition rather than a conquest, and it should be possible to be refused and have to return.

**Copied.** The duelist tree. The rogue watches someone fight and learns it by imitation, which is both the least mystical acquisition on the list and the most in character for a rogue.

**Remembered.** The chronomancer tree, and the only verb on the list that is not an event. Anachronos does not teach the chain and does not grant it. He shows a mortal something that already happened, which vanilla's Long Forgotten Memories quest already does literally. Learning it is recognising it.

**Dreamt.** The Dreamer candidate, and the only passive verb. You enter a Barrow Den, you sleep, and you do not wake for a long time. Naralex in Wailing Caverns is the cautionary version: a druid who did exactly this and woke into the Nightmare instead.

**Recanted.** The Radiance candidate. You publicly renounced the doctrine and the Light did not leave you. The chain is a trial rather than a lesson, and it is the only acquisition on the list where the character is tested and nothing is taken away.

Nine verbs across ten trees, with no two chains structurally alike. That variety is worth more than any individual chain's length.

### 8.4 Profession and social gates

The runeblade case suggests something the others should borrow. A warrior seeking a runeblade needs a blacksmith, and the interesting version of that requirement is not that the warrior must be a blacksmith. It is that the warrior needs **access to one**.

That distinction matters enormously.

A hard profession requirement is a tax. It forces a player to drop a profession they chose, it punishes people for a decision made at level ten, and it will be resented. A soft requirement is a reason to talk to someone. The warrior needs a smith of sufficient skill, and either has one or knows one or pays one, exactly as vanilla already handles crafted gear, weapon enchants, and summoning.

Vanilla is full of this and it is one of the reasons the game feels populated. Warlocks summon. Mages make portals and food. Blacksmiths make things you cannot make. The Sulfuron Hammer and Thunderfury both require a smith at the anvil. A tree acquired partly through another player's profession is not a new kind of thing, it is the same kind of thing at a larger scale.

Sensible pairings, with the same soft framing throughout:

- **Runeblade.** Blacksmithing, at high skill, ideally with the Weaponsmith specialization that vanilla already gates behind its own quest.
- **Shadow tree.** Alchemy for the plague components, since Scholomance is as much a laboratory as a school.
- **Metamorphosis.** Tailoring, which fits the Season of Discovery precedent of cloth built for tanking, and enchanting for the ritual components.
- **Duelist tree.** Leatherworking for the glaives and the harness.
- **Death tree.** Deliberately none. The whole point of the fallen verb is that nothing is prepared and nothing is chosen.

The rule is that no gate may require the player to hold the profession personally. Every one must be satisfiable by another player, and each one that is satisfiable that way is a small ongoing reason for two people to talk.

### 8.5 Cost

Two of these should cost something permanent, and the rest should not.

The death tree is the obvious one. A paladin who takes it should lose access to some part of the Light, not as a balance lever but because the fiction demands it and because a transformation with no cost is a purchase rather than a transformation. This is not exclusivity in Section 6's sense; nothing prevents the player from spending points wherever they like. It is a consequence attached to a specific act.

Metamorphosis is the second. The warlock who takes fel into themselves should be marked by it in some visible, permanent, mechanically minor way.

The others should cost nothing beyond the effort of the chain. Applying a cost to every tree would turn a meaningful consequence into a formula, which is the same failure mode as making every chain alike. Chronomancer is the exception that earns one: a healer who cannot be resurrected by others is a real raid cost.

### 8.6 Pacing

The trees do not have to unlock at once, and they should not. One tree per content patch, each with its own chain and its own moment, is a content cadence rather than a launch feature.

It also allows the game to test the argument cheaply. Ship one, watch what happens to warlock representation or paladin build diversity, and adjust before shipping the second.

---

## 9. The Trees

Sections 1 through 8 argue that these archetypes belong on existing classes and describe how a player would acquire them. This section builds them.

### 9.1 Structural rules

Vanilla's talent trees have a fixed shape and the absorbed trees must obey it or they will read as imports regardless of how good the talents are.

**Seven rows.** Row one is available immediately, and each subsequent row requires five more points spent in the tree. Row seven unlocks at thirty points, which is why a capstone costs thirty-one.

**Roughly twenty talents totalling fifty to sixty available points**, so the tree cannot be fully filled and the player is choosing what to leave behind.

That number is a hard constraint rather than a style note, and the first draft of Section 9 failed it. Each tree offered under thirty points across rows one through six, which made every capstone unreachable, since row seven requires thirty already spent. The trees as built now carry fifty-seven to sixty-four points in rows one through six, leaving roughly half of each tree on the table in any given build. Half a tree unspent is not waste, it is the choice.

**Fifty-one points total across four trees now instead of three, and five for mage.** A thirty-one point capstone leaves twenty.

An earlier draft read that twenty as reaching the twenty-point mark. It does not. A gate is points *already invested*, so owning a talent at tier N costs 5(N-1) plus one, and the twenty-point mark therefore costs twenty-one. Twenty points reaches tier four.

The shapes the budget actually produces are 31/20, a capstone plus a shallow second tree, or 30/21 and 26/25, two deep talents and no capstone at all. **Both canonical vanilla warlock raid builds take the second shape and own no thirty-one point talent**, and warlock is the only vanilla class with two competing viable raid builds. That is the strongest available evidence that giving up a capstone for two mid-tree talents is a real decision rather than a mistake, and the absorbed trees should be tuned so it stays one.

Three rules specific to the absorbed trees:

**No new resource bars.** This is a correction to what 7.1 suggested. Runic power, chi, and their kin should not be imported, and the tree should run on whatever the host class already spends. Vanilla's one exception is druid, where the resource changes because the *form* changes, and only one of these seven trees is a form.

What each tree gets instead is a **local mechanic**: something only its talents generate and consume, layered on the host's existing resource. Combo points are the model, and so are soul shards. A disease that several talents pay out against is a resource in every way that matters and costs nothing architecturally.

**Two signature talents, not one.** This is the structural answer to Section 6's fluidity problem.

- The **twenty-point mark** is the hybrid's prize. It is a real, usable, identity-carrying ability that works without deep investment, and it is what a player gets for splashing. A paladin with twenty points here is a knight touched by something cold, which is a character concept rather than a broken build.
- The **thirty-one point capstone** is transformative. It is a thing a character either has or does not, and it is what makes deep investment read as a commitment without any rule enforcing one.

The gap between those two is what makes the tree fluid rather than exclusive. Nothing forbids splashing. The splash is simply a different character than the capstone.

**No absorbed tree may be mandatory for its host's existing roles.** If protection paladins end up needing fifteen points in Blackguard, the tree has failed and should be retuned. Each of these is an alternative to the existing three, never a tax on them.

### 9.2 Blackguard (Paladin)

*The Light turned inward. Self-sustain becomes leeching, blessings become presences that cannot be shared, and the aura harms instead of helps.*

**Local mechanic: Blight, a disease applied by Blackguard strikes that roughly a third of the tree pays out against.**

Acquired by the **fallen** verb. The only tree that should be done to the character rather than by them. A paladin does not apply to become a death knight.

Profession gate: none. Deliberately none. The whole point of the fallen verb is that nothing is prepared and nothing is chosen.

Rows one through six offer 57 points against the thirty needed to reach row seven, so roughly half the tree is left behind in any build.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Unholy Vigor* (5): Your melee strikes apply Blight. Blight applied this way stacks twice. It cannot be dispelled. It spreads to a nearby enemy on death. A target at full Blight takes double damage from your next strike.
- *Grave Cold* (3): Your Blackguard abilities cost health instead of mana while a target near you carries Blight. Spending health this way applies a stack. Below 30% health they cost nothing.
- *Deathward* (5): Shadow damage taken is reduced. Frost damage taken is also reduced. Absorbed damage returns as a shield. The shield discharges as Shadow damage on your next strike. A fully absorbed spell prevents a killing blow once every 3 min.

**Row 2 (5 pts, 11 available)**
- *Plague Strike* (1): Instant melee strike dealing weapon damage and applying Blight for 15 sec. The tree's enabler.
- *Deathchill* (2): Your strikes chill what they touch and the chill deepens with each blow. A chilled target cannot escape you.
- *Rotting Flesh* (3): Your Blight reduces the target's armor. It stacks with Sunder Armor rather than replacing it. At full stacks the reduction applies to your party.
- *Morbid Strength* (5): Your attack power scales with Blight stacks on your current target. The scaling persists 6 sec after the target dies. It carries to your next target. Blight you did not apply also counts. At full stacks your strikes cannot be parried.

**Row 3 (10 pts, 10 available)**
- *Leeching Blade* (5): Your strikes against a Blighted target heal you. The healing scales with stacks held. Healing beyond full becomes a shield. The shield discharges as Shadow damage on your next strike. A killing blow on a Blighted target heals your party.
- *Spreading Corruption* (2): Your Blight spreads to a nearby enemy on its own and spreads faster at full stacks. A target that dies passes every stack to whatever is closest.
- *Chilblain* (3): Your Blight slows attack speed. It cannot be dispelled below 20% target health. It spreads on death.

**Row 4 (15 pts, 9 available)**
- *Presence of the Grave* (1): An aura that reduces damage taken and generates threat on everything nearby. Enemies striking you while it is active are slowed.
- *Chill of the Grave* (3): Blight reduces healing received by its target. The reduction cannot be dispelled. At full stacks the target cannot be healed above 50%.
- *Necrotic Aura* (3): Enemies within 8 yards take Shadow damage every 3 sec. The damage applies Blight. Enemies killed by it rise as a servant for 20 sec.
- *Vile Contagion* (2): Blight no longer expires while its target is in combat. Blight spreads to everything within 8 yards when its target dies.

**Row 5 (20 pts, 8 available)**
- *Blood Rite* (1): Your next strike heals you for the damage it deals, cannot be avoided, and spends every Blight stack on the target as immediate damage. Healing beyond full is added to the strike.
- *Unyielding Dead* (3): You cannot be critically struck by an enemy you have struck in the last 3 sec. The window extends to 6 sec. Surviving a killing blow once every 3 min heals you for the damage prevented.
- *Corpsefeeder* (2): Blood Rite also removes one poison or disease from you. Its overhealing is added to your next strike.
- *Damnation* (2): *(subtraction)* Your Blight never expires and cannot be dispelled, and every point of healing you would receive is converted into damage on your next strike. You may no longer be healed by another player.

**Row 6 (25 pts, 8 available)**
- *Frozen Heart* (3): Presence of the Grave converts damage taken into Blight on your attackers. It cannot be dispelled while you are below 50% health. Leaving it applies its accumulated Blight to everything nearby.
- *Reaping* (2): Killing a Blighted enemy grants attack speed. Your strikes below twenty percent target health spend Blight for damage.
- *Death's Advance* (3): You cannot be slowed below base speed while in combat. Closing to melee removes one movement-impairing effect every 10 sec. Snares on you are shortened.

**Row 7 (30 pts, 1 available)**
- *Damnation* (1): Your Blight never expires and cannot be dispelled, and every point of healing you would receive is converted into damage on your next strike. You may no longer be healed by another player.

<!-- END GENERATED -->

Lay on Hands inverted. An emergency heal that requires you to have poisoned somebody first, which is a complete character in one talent.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Unholy Vigor* (5): Your melee strikes apply Blight. Blight applied this way stacks twice. It cannot be dispelled. It spreads to a nearby enemy on death. A target at full Blight takes double damage from your next strike.
- *Grave Cold* (3): Your Blackguard abilities cost health instead of mana while a target near you carries Blight. Spending health this way applies a stack. Below 30% health they cost nothing.
- *Deathward* (5): Shadow damage taken is reduced. Frost damage taken is also reduced. Absorbed damage returns as a shield. The shield discharges as Shadow damage on your next strike. A fully absorbed spell prevents a killing blow once every 3 min.

**Row 2 (5 pts, 11 available)**
- *Plague Strike* (1): Instant melee strike dealing weapon damage and applying Blight for 15 sec. The tree's enabler.
- *Deathchill* (2): Your strikes chill what they touch and the chill deepens with each blow. A chilled target cannot escape you.
- *Rotting Flesh* (3): Your Blight reduces the target's armor. It stacks with Sunder Armor rather than replacing it. At full stacks the reduction applies to your party.
- *Morbid Strength* (5): Your attack power scales with Blight stacks on your current target. The scaling persists 6 sec after the target dies. It carries to your next target. Blight you did not apply also counts. At full stacks your strikes cannot be parried.

**Row 3 (10 pts, 10 available)**
- *Leeching Blade* (5): Your strikes against a Blighted target heal you. The healing scales with stacks held. Healing beyond full becomes a shield. The shield discharges as Shadow damage on your next strike. A killing blow on a Blighted target heals your party.
- *Spreading Corruption* (2): Your Blight spreads to a nearby enemy on its own and spreads faster at full stacks. A target that dies passes every stack to whatever is closest.
- *Chilblain* (3): Your Blight slows attack speed. It cannot be dispelled below 20% target health. It spreads on death.

**Row 4 (15 pts, 9 available)**
- *Presence of the Grave* (1): An aura that reduces damage taken and generates threat on everything nearby. Enemies striking you while it is active are slowed.
- *Chill of the Grave* (3): Blight reduces healing received by its target. The reduction cannot be dispelled. At full stacks the target cannot be healed above 50%.
- *Necrotic Aura* (3): Enemies within 8 yards take Shadow damage every 3 sec. The damage applies Blight. Enemies killed by it rise as a servant for 20 sec.
- *Vile Contagion* (2): Blight no longer expires while its target is in combat. Blight spreads to everything within 8 yards when its target dies.

**Row 5 (20 pts, 8 available)**
- *Blood Rite* (1): Your next strike heals you for the damage it deals, cannot be avoided, and spends every Blight stack on the target as immediate damage. Healing beyond full is added to the strike.
- *Unyielding Dead* (3): You cannot be critically struck by an enemy you have struck in the last 3 sec. The window extends to 6 sec. Surviving a killing blow once every 3 min heals you for the damage prevented.
- *Corpsefeeder* (2): Blood Rite also removes one poison or disease from you. Its overhealing is added to your next strike.
- *Damnation* (2): *(subtraction)* Your Blight never expires and cannot be dispelled, and every point of healing you would receive is converted into damage on your next strike. You may no longer be healed by another player.

**Row 6 (25 pts, 8 available)**
- *Frozen Heart* (3): Presence of the Grave converts damage taken into Blight on your attackers. It cannot be dispelled while you are below 50% health. Leaving it applies its accumulated Blight to everything nearby.
- *Reaping* (2): Killing a Blighted enemy grants attack speed. Your strikes below twenty percent target health spend Blight for damage.
- *Death's Advance* (3): You cannot be slowed below base speed while in combat. Closing to melee removes one movement-impairing effect every 10 sec. Snares on you are shortened.

**Row 7 (30 pts, 1 available)**
- *Damnation* (1): Your Blight never expires and cannot be dispelled, and every point of healing you would receive is converted into damage on your next strike. You may no longer be healed by another player.

<!-- END GENERATED -->

Acquisition runs through Scholomance, Scarlet Monastery, Western Plaguelands, Eastern Plaguelands. Those are live join points to the world document, since each is a named location that appears in its own proposals.

Lore anchor: Arthas was a paladin. The Death Knight fantasy is the paladin fantasy corrupted, and Warcraft III spends an entire campaign on the transition.


### 9.3 Necromancy (Mage)

*The fourth school. A caster who raises the disposable dead, spreads plague, and drains.*

**Local mechanic: The Risen, skeletal minions raised from corpses, plural and expiring.**

Acquired by the **taught** verb. Necromancy in Warcraft is explicitly curriculum. Somebody teaches it, in a building, to students.

Profession gate: Alchemy. For the plague components. Scholomance is as much a laboratory as a school. Satisfiable by another player, never required personally.

Rows one through six offer 57 points against the thirty needed to reach row seven, so roughly half the tree is left behind in any build.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Shadow Focus* (5): Your Necromancy spells cannot be partially resisted. A full resist raises one Risen. Your Risen cannot be resisted. Resisted spells refund their mana. A resist grants your next spell a free cast.
- *Grave Robbing* (3): Your Necromancy spells cost health instead of mana while a Risen is active. Spending health this way heals your Risen. A Risen dying refunds the health spent.
- *Deathchill Focus* (5): Your Risen inherit your resistances. They cannot be dispelled. They persist through your death. They rise at full strength rather than building. A Risen that dies raises another once per fight.

**Row 2 (5 pts, 11 available)**
- *Wither* (1): A shadow damage over time effect. Mage's first real DoT and the tree's rhythm-setter.
- *Bone Chill* (2): Your Frost spells slow what they touch and the slow deepens with each application. It cannot be dispelled.
- *Rotting Touch* (3): Your Risen strike hardest when newly raised. For the first twenty seconds after you enter combat your Shadow damage and your Risen's damage are increased, and the bonus does not fall off early if a Risen dies. Raising a Risen outside combat starts the window on the pull.
- *Dark Intellect* (5): Your spell damage scales with the number of Risen you control. A Risen consumed by Death Pact returns the scaling for 12 sec. Risen raised from a killing blow count double. The scaling persists 6 sec after all Risen die. At full Risen your spells cannot be interrupted.

**Row 3 (10 pts, 10 available)**
- *Siphon Life* (5): Wither heals you for a portion of its damage. All your Shadow damage over time heals you. The healing doubles below 10% of your own health. The threshold rises to 20%. It also heals your Risen.
- *Corpse Harvest* (2): Your Risen accumulate on you rather than on the field. They persist through a target's death, between pulls, and out of combat, and you may hold up to three.
- *Sepulchral Study* (3): Your summoning spells are instant. They may be cast before combat. A Risen dying refreshes the cooldown.

**Row 4 (15 pts, 9 available)**
- *Bone Armor* (1): Surrounds you with bone fragments absorbing damage. Each absorb consumes a fragment, so the shield visibly depletes.
- *Contagion* (3): Your damage over time effects cannot be dispelled. They spread to a nearby enemy on death. They tick faster below 20% target health.
- *Boneyard* (3): Raise every Risen you can hold at once, on a 3 min cooldown. They rise immediately and at full strength. The cooldown falls to 2 min.
- *Withering Cold* (2): Your Frost spells apply decay and the decay stacks. At full stacks the target takes your Shadow damage as Frost.

**Row 5 (20 pts, 8 available)**
- *Raise Skeleton* (1): Consumes a corpse to raise a skeletal minion for 60 sec. One at a time.
- *Grave Chill* (3): Bone Armor reduces the attack speed of melee attackers. It applies Blight to them. It cannot be stripped by their attacks.
- *Necrotic Aptitude* (2): Your Risen do not expire while in combat. A Risen at expiry detonates for Shadow damage rather than vanishing.
- *Grave Bargain* (2): *(subtraction)* Your Risen are permanent and rise at full strength. You may no longer cast any spell that does not raise or command them.

**Row 6 (25 pts, 8 available)**
- *Unstable Dead* (3): Your Risen explode on expiry, dealing damage scaled to how long they were held, and the explosion applies decay. A Risen killed by an enemy explodes for double. You may detonate them yourself.
- *Dark Command* (2): Your pet and any summoned servant attack the target you last damaged without command. They inherit your critical strike chance.
- *Death Pact* (3): Consuming a Risen heals you. Its remaining duration is added to your next spell as damage. It also removes one harmful effect.

**Row 7 (30 pts, 1 available)**
- *Command the Damned* (1): Your Risen no longer expire and answer from anywhere. They strike alongside you while you move, and every second strike they land sweeps through two enemies.

<!-- END GENERATED -->

The largest mark in the document, because vanilla mage has no pet at all. The corpse requirement keeps it tied to combat that already happened.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Shadow Focus* (5): Your Necromancy spells cannot be partially resisted. A full resist raises one Risen. Your Risen cannot be resisted. Resisted spells refund their mana. A resist grants your next spell a free cast.
- *Grave Robbing* (3): Your Necromancy spells cost health instead of mana while a Risen is active. Spending health this way heals your Risen. A Risen dying refunds the health spent.
- *Deathchill Focus* (5): Your Risen inherit your resistances. They cannot be dispelled. They persist through your death. They rise at full strength rather than building. A Risen that dies raises another once per fight.

**Row 2 (5 pts, 11 available)**
- *Wither* (1): A shadow damage over time effect. Mage's first real DoT and the tree's rhythm-setter.
- *Bone Chill* (2): Your Frost spells slow what they touch and the slow deepens with each application. It cannot be dispelled.
- *Rotting Touch* (3): Your Risen strike hardest when newly raised. For the first twenty seconds after you enter combat your Shadow damage and your Risen's damage are increased, and the bonus does not fall off early if a Risen dies. Raising a Risen outside combat starts the window on the pull.
- *Dark Intellect* (5): Your spell damage scales with the number of Risen you control. A Risen consumed by Death Pact returns the scaling for 12 sec. Risen raised from a killing blow count double. The scaling persists 6 sec after all Risen die. At full Risen your spells cannot be interrupted.

**Row 3 (10 pts, 10 available)**
- *Siphon Life* (5): Wither heals you for a portion of its damage. All your Shadow damage over time heals you. The healing doubles below 10% of your own health. The threshold rises to 20%. It also heals your Risen.
- *Corpse Harvest* (2): Your Risen accumulate on you rather than on the field. They persist through a target's death, between pulls, and out of combat, and you may hold up to three.
- *Sepulchral Study* (3): Your summoning spells are instant. They may be cast before combat. A Risen dying refreshes the cooldown.

**Row 4 (15 pts, 9 available)**
- *Bone Armor* (1): Surrounds you with bone fragments absorbing damage. Each absorb consumes a fragment, so the shield visibly depletes.
- *Contagion* (3): Your damage over time effects cannot be dispelled. They spread to a nearby enemy on death. They tick faster below 20% target health.
- *Boneyard* (3): Raise every Risen you can hold at once, on a 3 min cooldown. They rise immediately and at full strength. The cooldown falls to 2 min.
- *Withering Cold* (2): Your Frost spells apply decay and the decay stacks. At full stacks the target takes your Shadow damage as Frost.

**Row 5 (20 pts, 8 available)**
- *Raise Skeleton* (1): Consumes a corpse to raise a skeletal minion for 60 sec. One at a time.
- *Grave Chill* (3): Bone Armor reduces the attack speed of melee attackers. It applies Blight to them. It cannot be stripped by their attacks.
- *Necrotic Aptitude* (2): Your Risen do not expire while in combat. A Risen at expiry detonates for Shadow damage rather than vanishing.
- *Grave Bargain* (2): *(subtraction)* Your Risen are permanent and rise at full strength. You may no longer cast any spell that does not raise or command them.

**Row 6 (25 pts, 8 available)**
- *Unstable Dead* (3): Your Risen explode on expiry, dealing damage scaled to how long they were held, and the explosion applies decay. A Risen killed by an enemy explodes for double. You may detonate them yourself.
- *Dark Command* (2): Your pet and any summoned servant attack the target you last damaged without command. They inherit your critical strike chance.
- *Death Pact* (3): Consuming a Risen heals you. Its remaining duration is added to your next spell as damage. It also removes one harmful effect.

**Row 7 (30 pts, 1 available)**
- *Command the Damned* (1): Your Risen no longer expire and answer from anywhere. They strike alongside you while you move, and every second strike they land sweeps through two enemies.

<!-- END GENERATED -->

The expiry is the identity, not a balance lever. Warlocks have a companion. Necromancers have ammunition.

Acquisition runs through Scholomance, Western Plaguelands. Those are live join points to the world document, since each is a named location that appears in its own proposals.

Lore anchor: Kel'Thuzad was a Dalaran mage and a member of the Kirin Tor before founding the Cult of the Damned. Both endpoints of that career change are already in the game.


### 9.4 Metamorphosis (Warlock)

*The caster who becomes the thing they summon.*

**Local mechanic: Fel corruption, a self-applied stacking state, plus the form itself at the bottom.**

Acquired by the **taken** verb. Nobody grants this and nobody teaches it. The warlock performs a ritual on themselves and it works or it does not.

Profession gate: Tailoring, Enchanting. Tailoring fits the Season of Discovery precedent of cloth built for tanking. Enchanting for the ritual components.

Rows one through six offer 57 points against the thirty needed to reach row seven, so roughly half the tree is left behind in any build.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Fel Vigor* (5): Your Fire and Shadow damage applies fel Corruption. Corruption applied this way stacks twice. It does not decay in combat. It spreads on the target's death. At full stacks your next spell cannot be resisted.
- *Demonic Hide* (3): Your armor scales with Corruption stacks held. The scaling persists through form changes. Corruption on you converts physical damage to Fire once per fight.
- *Fel Concentration* (5): Your channelled spells cannot be interrupted by damage. Pushback is capped at once per channel. A channel completed while corrupted grants two stacks. Interruption converts to Corruption instead. You may channel while in the form.

**Row 2 (5 pts, 11 available)**
- *Shadow Cleave* (1): A short-range shadow attack striking up to three enemies in front of you. Works out of form, better in it.
- *Fel Stamina* (2): Your maximum health scales with Corruption stacks held. Corruption spent on an ability heals you for a portion.
- *Cruel Intent* (3): Shadow Cleave applies two stacks of Corruption. It strikes behind you. It spends stacks for damage.
- *Demonic Bulwark* (5): Blocking applies Corruption to the attacker. Corruption on an attacker raises your block value. A full block spends its Corruption for damage. Blocking while at full Corruption refreshes Fel Aegis. You may block while in the form.

**Row 3 (10 pts, 10 available)**
- *Demonic Aegis* (5): Corruption stacks reduce physical damage taken. They convert magic damage to Fel. At full stacks they absorb a killing blow once per fight. Absorbed damage feeds the form. Breaking the absorb applies Corruption to everything nearby.
- *Soul Link* (2): A portion of damage taken is redirected to your demon. The redirected share doubles.
- *Master Summoner* (3): Summoning is instant while Corruption is on you. Summoning does not break your current cast. A demon summoned at full Corruption arrives enraged.

**Row 4 (15 pts, 9 available)**
- *Immolation Aura* (1): Deals periodic fire damage to nearby enemies and generates threat.
- *Fel Resilience* (3): Stun and snare durations on you are reduced. You cannot be feared while in the form. Control effects that would be resisted are shortened instead.
- *Unholy Sacrifice* (3): Sacrificing your demon grants Corruption stacks equal to its remaining health. The stacks arrive immediately and at full value. They do not decay.
- *Fel Ferocity* (2): Corruption stacks raise Shadow Cleave's critical strike chance. A critical Shadow Cleave applies two stacks.

**Row 5 (20 pts, 8 available)**
- *Fel Aegis* (1): Partial transformation for 20 sec on a 3 minute cooldown. Large armor bonus, increased threat, cheaper Shadow Cleave.
- *Demonic Knowledge* (3): Your spell damage scales with Corruption stacks held. Corruption on your demon counts toward the scaling. Spending Corruption grants the scaling for 12 sec regardless.
- *Warding Fel* (2): Magic damage taken is reduced. Absorbing magic damage lengthens the caster's next cast.
- *Irreversible* (2): *(subtraction)* Your Corruption stacks never decay and the form's bonuses double. You may no longer leave the form or summon a demon.

**Row 6 (25 pts, 8 available)**
- *Unending Fel* (3): Fel Aegis has no cooldown while you are at full Corruption. Using it spends all stacks and deals their value as Shadow damage. The damage strikes every enemy around you.
- *Demonic Fury* (2): Your Shadow Cleave draws attention well beyond its damage. The attention holds through your demon's death.
- *Fel Domination* (3): Summoning is instant and costs no shard. It may be used while in the form. The summoned demon arrives with your Corruption stacks.

**Row 7 (30 pts, 1 available)**
- *Metamorphosis* (1): Permanent demon form. Armor multiplied substantially, Shadow Bolt replaced by Shadow Cleave, all threat multiplied. You look like this now.

<!-- END GENERATED -->

This is Wrath's Metamorphosis, which was a three minute cooldown. The capstone is Season of Discovery's, which is permanent. Splitting them across the two slots is not a compromise between the versions, it is both of them in the order they were built.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Fel Vigor* (5): Your Fire and Shadow damage applies fel Corruption. Corruption applied this way stacks twice. It does not decay in combat. It spreads on the target's death. At full stacks your next spell cannot be resisted.
- *Demonic Hide* (3): Your armor scales with Corruption stacks held. The scaling persists through form changes. Corruption on you converts physical damage to Fire once per fight.
- *Fel Concentration* (5): Your channelled spells cannot be interrupted by damage. Pushback is capped at once per channel. A channel completed while corrupted grants two stacks. Interruption converts to Corruption instead. You may channel while in the form.

**Row 2 (5 pts, 11 available)**
- *Shadow Cleave* (1): A short-range shadow attack striking up to three enemies in front of you. Works out of form, better in it.
- *Fel Stamina* (2): Your maximum health scales with Corruption stacks held. Corruption spent on an ability heals you for a portion.
- *Cruel Intent* (3): Shadow Cleave applies two stacks of Corruption. It strikes behind you. It spends stacks for damage.
- *Demonic Bulwark* (5): Blocking applies Corruption to the attacker. Corruption on an attacker raises your block value. A full block spends its Corruption for damage. Blocking while at full Corruption refreshes Fel Aegis. You may block while in the form.

**Row 3 (10 pts, 10 available)**
- *Demonic Aegis* (5): Corruption stacks reduce physical damage taken. They convert magic damage to Fel. At full stacks they absorb a killing blow once per fight. Absorbed damage feeds the form. Breaking the absorb applies Corruption to everything nearby.
- *Soul Link* (2): A portion of damage taken is redirected to your demon. The redirected share doubles.
- *Master Summoner* (3): Summoning is instant while Corruption is on you. Summoning does not break your current cast. A demon summoned at full Corruption arrives enraged.

**Row 4 (15 pts, 9 available)**
- *Immolation Aura* (1): Deals periodic fire damage to nearby enemies and generates threat.
- *Fel Resilience* (3): Stun and snare durations on you are reduced. You cannot be feared while in the form. Control effects that would be resisted are shortened instead.
- *Unholy Sacrifice* (3): Sacrificing your demon grants Corruption stacks equal to its remaining health. The stacks arrive immediately and at full value. They do not decay.
- *Fel Ferocity* (2): Corruption stacks raise Shadow Cleave's critical strike chance. A critical Shadow Cleave applies two stacks.

**Row 5 (20 pts, 8 available)**
- *Fel Aegis* (1): Partial transformation for 20 sec on a 3 minute cooldown. Large armor bonus, increased threat, cheaper Shadow Cleave.
- *Demonic Knowledge* (3): Your spell damage scales with Corruption stacks held. Corruption on your demon counts toward the scaling. Spending Corruption grants the scaling for 12 sec regardless.
- *Warding Fel* (2): Magic damage taken is reduced. Absorbing magic damage lengthens the caster's next cast.
- *Irreversible* (2): *(subtraction)* Your Corruption stacks never decay and the form's bonuses double. You may no longer leave the form or summon a demon.

**Row 6 (25 pts, 8 available)**
- *Unending Fel* (3): Fel Aegis has no cooldown while you are at full Corruption. Using it spends all stacks and deals their value as Shadow damage. The damage strikes every enemy around you.
- *Demonic Fury* (2): Your Shadow Cleave draws attention well beyond its damage. The attention holds through your demon's death.
- *Fel Domination* (3): Summoning is instant and costs no shard. It may be used while in the form. The summoned demon arrives with your Corruption stacks.

**Row 7 (30 pts, 1 available)**
- *Metamorphosis* (1): Permanent demon form. Armor multiplied substantially, Shadow Bolt replaced by Shadow Cleave, all threat multiplied. You look like this now.

<!-- END GENERATED -->

Acquisition runs through Redridge Mountains, Darkshore, The Barrens, Shadowfang Keep, Blackfathom Deeps, Ashenvale. Those are live join points to the world document, since each is a named location that appears in its own proposals.

Lore anchor: Metamorphosis is adapted from the Warcraft III Demon Hunter ability, visually based on Illidan, and was removed from warlocks in patch 7.0.3 specifically to make room for the Demon Hunter class.


### 9.5 Bladedancer (Rogue)

*Mobile melee flow. Glaives, fists, and open hands, spread across several targets rather than concentrated on one.*

**Local mechanic: Momentum, a stacking state gained by moving and by striking new targets, lost by standing still. Combo points remain the spend..**

Acquired by the **copied** verb. The rogue watches someone fight and learns it by imitation. The least mystical acquisition on the list and the most in character.

Profession gate: Leatherworking. For the glaives and the harness.

Rows one through six offer 63 points against the thirty needed to reach row seven, so roughly half the tree is left behind in any build.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 12 available)**
- *Flowing Form* (5): Your fist and unarmed strikes build Momentum. Momentum built this way does not decay while moving. Strikes at full Momentum cannot be dodged. A killing blow refunds all Momentum. Momentum persists through Tumble.
- *Fleet Footed* (2): Momentum grants movement speed while it lasts, and snares are shortened per stack held. At full Momentum you cannot be rooted.
- *Deft Hands* (5): Your attack speed scales with Momentum held. The scaling persists 4 sec after Momentum ends. Momentum is not lost on a miss. Two strikes in a row build double. At full Momentum your off-hand strikes with the main.

**Row 2 (5 pts, 10 available)**
- *Tumble* (1): A short directional roll. Not a Sprint. The thing that makes the fantasy read as flow instead of speed.
- *Open Hand* (2): Your unarmed attacks use your Fist Weapon skill. They scale as a weapon.
- *Lithe* (3): Tumble builds Momentum rather than spending it. It may be used while rooted. It refreshes Momentum's duration.
- *Sinew* (4): Your critical strike chance scales with Momentum held, and criticals build an extra stack. Momentum is not lost when you change target. Spending Momentum refreshes your poisons. At full Momentum criticals cannot be resisted.

**Row 3 (10 pts, 10 available)**
- *Momentum* (5): Moving in combat builds Momentum. Each stack drives your strikes harder. Momentum holds three stacks. The cap rises to five. Standing still sheds it one stack at a time instead of all at once.
- *No Opening Needed* (2): Your openers no longer require stealth, though they strike softer used openly. At full rank they strike as though you had never been seen.
- *Redirection* (3): Changing targets no longer clears combo points. Combo points persist 10 sec out of combat. A killing blow transfers them to your next target.

**Row 4 (15 pts, 9 available)**
- *Sweeping Kick* (1): A combo point spender that briefly stuns all enemies within melee range. Rogue's first multi-target control.
- *Blade Harmony* (3): Attacking a target you have not hit in the last 6 sec grants Momentum. The bonus doubles against a target no ally has struck. It cannot be dodged.
- *Precision Footwork* (3): Your strikes cannot miss while Momentum is at full stacks. A miss builds Momentum instead. Momentum spent on a miss is refunded.
- *Second Wind* (2): Being stunned or rooted builds Momentum. The effect breaks the control once every 30 sec.

**Row 5 (20 pts, 8 available)**
- *Whirling Blades* (1): A finisher dealing damage to multiple enemies, scaling with combo points.
- *Unbroken Rhythm* (3): Whirling Blades spends Momentum for damage rather than energy. It refreshes Momentum on a killing blow. It may be used while moving.
- *Evasive* (2): Momentum stacks grant dodge. Dodging builds a stack rather than spending one.
- *Perpetual Motion* (2): *(subtraction)* Momentum never decays and starts at full. You may no longer use any ability that costs energy.

**Row 6 (25 pts, 14 available)**
- *Edged Discipline* (3): Whirling Blades may be used at range with a bladed weapon. It returns to you, striking again. It cannot be resisted on the return.
- *Flowing Palm* (3): With a fist weapon or bare hands, Whirling Blades refunds a combo point for every four targets struck. The refund comes every three targets. It comes every two.
- *Relentless* (3): Whirling Blades refunds a combo point per target struck. The refund is not capped by your maximum. A full refund makes your next finisher free.
- *Uninterrupted* (2): Momentum stacks decay two at a time rather than clearing. The decay slows to one stack at a time.
- *Killing Flow* (3): Killing an enemy grants two Momentum stacks. It refreshes Momentum's duration. A killing blow at full Momentum grants a free ability.

**Row 7 (30 pts, 1 available)**
- *Unending Dance* (1): Momentum behaves differently by weapon. Your whirling Blades no longer costs a full finisher below three targets.

<!-- END GENERATED -->

Vanilla ships an Unarmed weapon skill that exists, can be levelled, and is pointless. One talent makes it real in exactly one tree.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 12 available)**
- *Flowing Form* (5): Your fist and unarmed strikes build Momentum. Momentum built this way does not decay while moving. Strikes at full Momentum cannot be dodged. A killing blow refunds all Momentum. Momentum persists through Tumble.
- *Fleet Footed* (2): Momentum grants movement speed while it lasts, and snares are shortened per stack held. At full Momentum you cannot be rooted.
- *Deft Hands* (5): Your attack speed scales with Momentum held. The scaling persists 4 sec after Momentum ends. Momentum is not lost on a miss. Two strikes in a row build double. At full Momentum your off-hand strikes with the main.

**Row 2 (5 pts, 10 available)**
- *Tumble* (1): A short directional roll. Not a Sprint. The thing that makes the fantasy read as flow instead of speed.
- *Open Hand* (2): Your unarmed attacks use your Fist Weapon skill. They scale as a weapon.
- *Lithe* (3): Tumble builds Momentum rather than spending it. It may be used while rooted. It refreshes Momentum's duration.
- *Sinew* (4): Your critical strike chance scales with Momentum held, and criticals build an extra stack. Momentum is not lost when you change target. Spending Momentum refreshes your poisons. At full Momentum criticals cannot be resisted.

**Row 3 (10 pts, 10 available)**
- *Momentum* (5): Moving in combat builds Momentum. Each stack drives your strikes harder. Momentum holds three stacks. The cap rises to five. Standing still sheds it one stack at a time instead of all at once.
- *No Opening Needed* (2): Your openers no longer require stealth, though they strike softer used openly. At full rank they strike as though you had never been seen.
- *Redirection* (3): Changing targets no longer clears combo points. Combo points persist 10 sec out of combat. A killing blow transfers them to your next target.

**Row 4 (15 pts, 9 available)**
- *Sweeping Kick* (1): A combo point spender that briefly stuns all enemies within melee range. Rogue's first multi-target control.
- *Blade Harmony* (3): Attacking a target you have not hit in the last 6 sec grants Momentum. The bonus doubles against a target no ally has struck. It cannot be dodged.
- *Precision Footwork* (3): Your strikes cannot miss while Momentum is at full stacks. A miss builds Momentum instead. Momentum spent on a miss is refunded.
- *Second Wind* (2): Being stunned or rooted builds Momentum. The effect breaks the control once every 30 sec.

**Row 5 (20 pts, 8 available)**
- *Whirling Blades* (1): A finisher dealing damage to multiple enemies, scaling with combo points.
- *Unbroken Rhythm* (3): Whirling Blades spends Momentum for damage rather than energy. It refreshes Momentum on a killing blow. It may be used while moving.
- *Evasive* (2): Momentum stacks grant dodge. Dodging builds a stack rather than spending one.
- *Perpetual Motion* (2): *(subtraction)* Momentum never decays and starts at full. You may no longer use any ability that costs energy.

**Row 6 (25 pts, 14 available)**
- *Edged Discipline* (3): Whirling Blades may be used at range with a bladed weapon. It returns to you, striking again. It cannot be resisted on the return.
- *Flowing Palm* (3): With a fist weapon or bare hands, Whirling Blades refunds a combo point for every four targets struck. The refund comes every three targets. It comes every two.
- *Relentless* (3): Whirling Blades refunds a combo point per target struck. The refund is not capped by your maximum. A full refund makes your next finisher free.
- *Uninterrupted* (2): Momentum stacks decay two at a time rather than clearing. The decay slows to one stack at a time.
- *Killing Flow* (3): Killing an enemy grants two Momentum stacks. It refreshes Momentum's duration. A killing blow at full Momentum grants a free ability.

**Row 7 (30 pts, 1 available)**
- *Unending Dance* (1): Momentum behaves differently by weapon. Your whirling Blades no longer costs a full finisher below three targets.

<!-- END GENERATED -->

Rogue's entire vanilla identity is single-target burst from stealth. A multi-target finisher is the largest thing twenty points could buy.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 12 available)**
- *Flowing Form* (5): Your fist and unarmed strikes build Momentum. Momentum built this way does not decay while moving. Strikes at full Momentum cannot be dodged. A killing blow refunds all Momentum. Momentum persists through Tumble.
- *Fleet Footed* (2): Momentum grants movement speed while it lasts, and snares are shortened per stack held. At full Momentum you cannot be rooted.
- *Deft Hands* (5): Your attack speed scales with Momentum held. The scaling persists 4 sec after Momentum ends. Momentum is not lost on a miss. Two strikes in a row build double. At full Momentum your off-hand strikes with the main.

**Row 2 (5 pts, 10 available)**
- *Tumble* (1): A short directional roll. Not a Sprint. The thing that makes the fantasy read as flow instead of speed.
- *Open Hand* (2): Your unarmed attacks use your Fist Weapon skill. They scale as a weapon.
- *Lithe* (3): Tumble builds Momentum rather than spending it. It may be used while rooted. It refreshes Momentum's duration.
- *Sinew* (4): Your critical strike chance scales with Momentum held, and criticals build an extra stack. Momentum is not lost when you change target. Spending Momentum refreshes your poisons. At full Momentum criticals cannot be resisted.

**Row 3 (10 pts, 10 available)**
- *Momentum* (5): Moving in combat builds Momentum. Each stack drives your strikes harder. Momentum holds three stacks. The cap rises to five. Standing still sheds it one stack at a time instead of all at once.
- *No Opening Needed* (2): Your openers no longer require stealth, though they strike softer used openly. At full rank they strike as though you had never been seen.
- *Redirection* (3): Changing targets no longer clears combo points. Combo points persist 10 sec out of combat. A killing blow transfers them to your next target.

**Row 4 (15 pts, 9 available)**
- *Sweeping Kick* (1): A combo point spender that briefly stuns all enemies within melee range. Rogue's first multi-target control.
- *Blade Harmony* (3): Attacking a target you have not hit in the last 6 sec grants Momentum. The bonus doubles against a target no ally has struck. It cannot be dodged.
- *Precision Footwork* (3): Your strikes cannot miss while Momentum is at full stacks. A miss builds Momentum instead. Momentum spent on a miss is refunded.
- *Second Wind* (2): Being stunned or rooted builds Momentum. The effect breaks the control once every 30 sec.

**Row 5 (20 pts, 8 available)**
- *Whirling Blades* (1): A finisher dealing damage to multiple enemies, scaling with combo points.
- *Unbroken Rhythm* (3): Whirling Blades spends Momentum for damage rather than energy. It refreshes Momentum on a killing blow. It may be used while moving.
- *Evasive* (2): Momentum stacks grant dodge. Dodging builds a stack rather than spending one.
- *Perpetual Motion* (2): *(subtraction)* Momentum never decays and starts at full. You may no longer use any ability that costs energy.

**Row 6 (25 pts, 14 available)**
- *Edged Discipline* (3): Whirling Blades may be used at range with a bladed weapon. It returns to you, striking again. It cannot be resisted on the return.
- *Flowing Palm* (3): With a fist weapon or bare hands, Whirling Blades refunds a combo point for every four targets struck. The refund comes every three targets. It comes every two.
- *Relentless* (3): Whirling Blades refunds a combo point per target struck. The refund is not capped by your maximum. A full refund makes your next finisher free.
- *Uninterrupted* (2): Momentum stacks decay two at a time rather than clearing. The decay slows to one stack at a time.
- *Killing Flow* (3): Killing an enemy grants two Momentum stacks. It refreshes Momentum's duration. A killing blow at full Momentum grants a free ability.

**Row 7 (30 pts, 1 available)**
- *Unending Dance* (1): Momentum behaves differently by weapon. Your whirling Blades no longer costs a full finisher below three targets.

<!-- END GENERATED -->

The duelist builds and spends. The martial artist accumulates and never stops. That is the difference between the two fantasies stated mechanically; everything else is presentation.

**Open item.** Unspecified. Section 8.6 names chains for Blackguard, Necromancy, Metamorphosis, and Runeblade only. This is an open item.

Lore anchor: The Blademaster and the Aldrachi glaive tradition are both available as naming material without importing the Illidari. The Pandaren Brewmaster was a hireable Warcraft III neutral hero, not a race requirement.

#### The weapon fork

The merge in 7.4 raises a fair objection: if Havoc and Windwalker are folded together, does the result feel like neither? It does not have to, and the fix costs no talent points. **The tree does not ask which one you are. Your main hand answers.**

The tree does not ask which fantasy you are. Your main hand answers. Vanilla already gates Backstab and Ambush on daggers and carries per-weapon specialization talents in Combat, so this is the existing rule rather than a new one.

**Bladed main hand.** One-handed swords, axes, daggers. Forward, thrown, burst. Reads as the duelist.

**Fist weapons or unarmed.** Fist weapons or unarmed. Around you, sustained, continuous. Reads as the martial artist.

| Ability | Bladed | Fist or unarmed |
|---|---|---|
| *Tumble* (row 2) | A 15 yard forward leap on a 20 sec cooldown. A gap closer. | An 8 yard roll in any direction on an 8 sec cooldown. Repositioning. |
| *Whirling Blades* (row 5) | An arc striking enemies in a cone in front of you at up to 8 yards. | A spin striking every enemy within melee range around you. |
| *Unending Dance* (row 7) | Momentum is consumed by your next finisher for a large burst, then resets. | Momentum has no cap and does not decay while you keep moving. |

The capstone row is the real distinction, and it states the difference between the two fantasies mechanically. The duelist builds and spends. The martial artist accumulates and never stops. Everything else is presentation.

Row six carries one talent per path, and points spent on the wrong one do nothing, exactly as Sword Specialization does nothing while holding daggers. That is not a trap, it is the existing rule.

Swapping weapons swaps the style in the field, so a player carrying both is carrying two builds at the cost of a weapon swap rather than a respec. It also gives fist weapons a reason to exist, which vanilla's thin fist itemization currently does not provide.

It also settles the naming problem from Section 5 without a naming decision. The tree is never called Demon Hunter or Monk. A player who wants to be one equips for it, and the game agrees without ever making the claim.


### 9.6 Conduit (Shaman)

*Elemental power held rather than thrown, and given to a person rather than to the ground.*

**Local mechanic: Empowerment, where certain spells may be held while casting to advance through charge stages.**

Acquired by the **granted** verb. The elements agree or they do not, so the chain is a petition rather than a conquest. It should be possible to be refused and have to return.

Profession gate: none. None. Nothing is crafted and nothing is bought.

Rows one through six offer 57 points against the thirty needed to reach row seven, so roughly half the tree is left behind in any build.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Elemental Focus* (5): Casting Lightning Bolt may leave you Clearcast, halving the cost of your next spell. Casting any elemental spell may trigger it. The next spell instead costs nothing. Clearcasting also reduces the next spell's pushback. The pushback is removed entirely.
- *Steady Channel* (3): Empowering cannot be pushed back. Damage taken while empowering adds a stage instead. An interrupted empowerment releases at its current stage rather than failing.
- *Elemental Warding* (5): Fire, Frost, and Nature damage taken adds an empowerment stage. The stage cannot be resisted. Absorbing such damage grants a free cast. Empowerment on you converts magic damage to healing once per fight. At full empowerment you cannot be interrupted.

**Row 2 (5 pts, 11 available)**
- *Empowered Lightning* (1): Your Lightning Bolt may be held to charge through three stages.
- *Grounding* (2): Empowered spells cost health instead of mana above half health. You enter combat with a charge already held, and for the first twenty seconds your spells empower faster and hit harder.
- *Tidal Focus* (3): Your heals cannot be overhealed on a target below 30% health. Overhealing becomes an absorb. The absorb persists 10 sec.
- *Ancestral Insight* (5): Your spell damage and healing scale with empowerment stages held. Stages persist through a target change. Releasing early keeps the scaling for 6 sec. Two empowerments in a row grant a free stage. At full stages your next cast is instant.

**Row 3 (10 pts, 10 available)**
- *Living Current* (5): Empowered Lightning Bolt at full charge restores mana. Any empowered spell at full charge restores mana. At full charge the surplus discharges as damage. A bonded ally gains half the mana restored. The bonded ally gains the full amount.
- *Empowered Healing* (2): Your Healing Wave may be held to charge, and each stage raises its effect and its radius. At full charge it cannot be overhealed.
- *Storm Reach* (3): Your spells reach further. At maximum range they ignore line of sight. Range no longer reduces their effect.

**Row 4 (15 pts, 9 available)**
- *Totemic Reach* (1): Your totems reach twice as far and follow you between them. A totem out of range still counts as placed.
- *Elemental Grace* (3): Empowerment reaches full charge faster. Movement no longer slows the charge. Releasing early keeps one stage.
- *Restorative Current* (3): Empowered Healing at full charge heals a second ally. The second heal cannot overheal. It carries the first heal's element.
- *Earthen Footing* (2): You cannot be interrupted while casting. Being struck while casting shortens your next cast instead.

**Row 5 (20 pts, 8 available)**
- *Elemental Bond* (1): Places one active totem's effect on a single ally rather than on the ground. The effect follows them and persists while they remain in your party.
- *Elemental Devotion* (3): Elemental Bond does not expire while you are empowering. It transfers to a second ally at half effect. Breaking it releases its remaining duration as healing.
- *Surge* (2): Empowered spells at full charge may release without consuming their charge. A held charge released early deals its accumulated value at once.
- *Unbroken Current* (2): *(subtraction)* Your empowered casts cannot be interrupted or pushed back. You may no longer cast anything instantly.

**Row 6 (25 pts, 8 available)**
- *Conductive* (3): Empowered spells at full charge strike a second target. The second strike carries the full element. It cannot be resisted.
- *Deep Bond* (2): Elemental Bond binds harder and to a second ally. The bond does not break when either of you dies.
- *Wellspring* (3): Living Current restores mana to bonded allies. The restoration scales with charge held. A bonded ally at full mana gains an absorb instead.

**Row 7 (30 pts, 1 available)**
- *Confluence* (1): Your elemental Bond may be active on up to three allies at once, and fully empowered spells grant a brief share of their effect to everyone you are bonded to.

<!-- END GENERATED -->

Augmentation translated into vanilla's vocabulary with no invention required. Shaman's defining contribution is already a buff placed on the ground; placing it on a person is one talent.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Elemental Focus* (5): Casting Lightning Bolt may leave you Clearcast, halving the cost of your next spell. Casting any elemental spell may trigger it. The next spell instead costs nothing. Clearcasting also reduces the next spell's pushback. The pushback is removed entirely.
- *Steady Channel* (3): Empowering cannot be pushed back. Damage taken while empowering adds a stage instead. An interrupted empowerment releases at its current stage rather than failing.
- *Elemental Warding* (5): Fire, Frost, and Nature damage taken adds an empowerment stage. The stage cannot be resisted. Absorbing such damage grants a free cast. Empowerment on you converts magic damage to healing once per fight. At full empowerment you cannot be interrupted.

**Row 2 (5 pts, 11 available)**
- *Empowered Lightning* (1): Your Lightning Bolt may be held to charge through three stages.
- *Grounding* (2): Empowered spells cost health instead of mana above half health. You enter combat with a charge already held, and for the first twenty seconds your spells empower faster and hit harder.
- *Tidal Focus* (3): Your heals cannot be overhealed on a target below 30% health. Overhealing becomes an absorb. The absorb persists 10 sec.
- *Ancestral Insight* (5): Your spell damage and healing scale with empowerment stages held. Stages persist through a target change. Releasing early keeps the scaling for 6 sec. Two empowerments in a row grant a free stage. At full stages your next cast is instant.

**Row 3 (10 pts, 10 available)**
- *Living Current* (5): Empowered Lightning Bolt at full charge restores mana. Any empowered spell at full charge restores mana. At full charge the surplus discharges as damage. A bonded ally gains half the mana restored. The bonded ally gains the full amount.
- *Empowered Healing* (2): Your Healing Wave may be held to charge, and each stage raises its effect and its radius. At full charge it cannot be overhealed.
- *Storm Reach* (3): Your spells reach further. At maximum range they ignore line of sight. Range no longer reduces their effect.

**Row 4 (15 pts, 9 available)**
- *Totemic Reach* (1): Your totems reach twice as far and follow you between them. A totem out of range still counts as placed.
- *Elemental Grace* (3): Empowerment reaches full charge faster. Movement no longer slows the charge. Releasing early keeps one stage.
- *Restorative Current* (3): Empowered Healing at full charge heals a second ally. The second heal cannot overheal. It carries the first heal's element.
- *Earthen Footing* (2): You cannot be interrupted while casting. Being struck while casting shortens your next cast instead.

**Row 5 (20 pts, 8 available)**
- *Elemental Bond* (1): Places one active totem's effect on a single ally rather than on the ground. The effect follows them and persists while they remain in your party.
- *Elemental Devotion* (3): Elemental Bond does not expire while you are empowering. It transfers to a second ally at half effect. Breaking it releases its remaining duration as healing.
- *Surge* (2): Empowered spells at full charge may release without consuming their charge. A held charge released early deals its accumulated value at once.
- *Unbroken Current* (2): *(subtraction)* Your empowered casts cannot be interrupted or pushed back. You may no longer cast anything instantly.

**Row 6 (25 pts, 8 available)**
- *Conductive* (3): Empowered spells at full charge strike a second target. The second strike carries the full element. It cannot be resisted.
- *Deep Bond* (2): Elemental Bond binds harder and to a second ally. The bond does not break when either of you dies.
- *Wellspring* (3): Living Current restores mana to bonded allies. The restoration scales with charge held. A bonded ally at full mana gains an absorb instead.

**Row 7 (30 pts, 1 available)**
- *Confluence* (1): Your elemental Bond may be active on up to three allies at once, and fully empowered spells grant a brief share of their effect to everyone you are bonded to.

<!-- END GENERATED -->

**Open item.** Unspecified. Elemental sites would be the obvious home but Section 8.6 does not name them. Open item.

Lore anchor: Dragonflight-era Evoker lore does not exist in a Classic timeframe and should not be imported. The shaman's existing relationship with the elements carries the whole tree.


### 9.7 Runeblade (Warrior)

*A warrior whose weapon is enchanted with cold. Not a caster, and deliberately smaller in ambition than the other six.*

**Local mechanic: Rune charges accumulated on the weapon and spent on effects. The magic belongs to the object throughout..**

Acquired by the **forged** verb. An object, not a power, which is the whole reason warrior can have it without becoming a spellcaster. The chain produces a weapon and requires someone who can make one.

Profession gate: Blacksmithing, ideally Weaponsmith. The model for the rest. Not that the warrior must be a smith, but that they need access to one. Same as Thunderfury and the Sulfuron Hammer.

Rows one through six offer 59 points against the thirty needed to reach row seven, so roughly half the tree is left behind in any build.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Cold Iron* (5): Your weapon holds its charge between fights. You enter combat with one charge already held. You enter combat with two charges already held. You enter combat fully charged. For the first twenty seconds your weapon strikes deal increased damage.
- *Frostbitten* (3): Frost damage taken is reduced. Absorbing Frost damage heals you. At full absorption you are immune to Frost for 4 sec.
- *Iron Discipline* (5): Your strikes cannot miss while the weapon holds charges. A miss grants a Charge instead. Charges are not spent on a dodge or parry. Two strikes in a row grant an extra Charge. At full charges your strikes cannot be avoided.

**Row 2 (5 pts, 13 available)**
- *Rime* (2): Your melee strikes may chill what they touch, and the chill deepens on a critical. A chilled target cannot outrun you.
- *Weighted Edge* (3): Slowed targets grant an extra Charge when struck. Charges spent on a slowed target deal double. Slowing a target refreshes the weapon's charges.
- *Glacial Edge* (3): Rime does not expire while the weapon holds charges. Rime spends a Charge to refresh itself. A Charge spent under Rime applies a slow.
- *Tempered* (5): Your weapon damage scales with charges held. The scaling persists 6 sec after spending. Charges are not lost on death. Spending all charges at once doubles the effect. At full charges your weapon strikes a second target.

**Row 3 (10 pts, 10 available)**
- *Rune Charge* (5): One charge held on your weapon adds frost damage to every swing. A second charge adds its frost damage. A third charge adds its frost damage. Every charge held adds its frost damage. The charges do not bleed away between fights.
- *Cold Endurance* (2): Below 35% health you take reduced damage. Damage absorbed this way heals you for a portion.
- *Cold Blood* (3): Your next strike is a guaranteed critical. Used on a finisher it adds two combo points to those spent. The finisher doubles the combo points spent instead.

**Row 4 (15 pts, 9 available)**
- *Shattering Blow* (1): Consumes all rune charges to deal frost damage scaled to the number consumed.
- *Killing Frost* (3): Critical strikes against slowed targets restore rune charges. A killing blow restores all charges. Charges restored this way do not decay.
- *Chillguard* (3): Slowed enemies deal reduced damage to you. Their attacks cannot be critical. A slowed attacker is briefly rooted after striking you.
- *Frost Reserve* (2): Rune charges build faster and build while sheathed. Two charges may be banked beyond the maximum.

**Row 5 (20 pts, 8 available)**
- *Hoarfrost* (1): For 20 sec every swing deals additional frost damage and applies Rime automatically. Two minute cooldown.
- *Numbing Cold* (3): Rime reduces the target's attack speed. It cannot be dispelled. It spreads to a nearby enemy on death.
- *Deep Freeze* (2): Shattering Blow spends every Charge held and scales with the number spent. It applies Rime for each Charge spent.
- *Bound Blade* (2): *(subtraction)* Your weapon holds twice as many charges. It never loses them, and you may no longer change weapons.

**Row 6 (25 pts, 8 available)**
- *Permafrost* (3): Rune charges no longer decay out of combat. They persist through death. They are not lost on a weapon swap.
- *Bitter Cold* (2): Shattering Blow chills everything nearby. While your weapon holds charges every third strike you land sweeps through two enemies beside your target.
- *Unbreakable Rime* (3): Rime cannot be dispelled. Its slow is not reduced by the target's effects. It refreshes when you spend a Charge.

**Row 7 (30 pts, 1 available)**
- *The Runeblade* (1): Requires an equipped runeblade. Your weapon permanently deals frost damage on every swing, your strikes always apply Rime, and killing blows restore rage.

<!-- END GENERATED -->

The only capstone in the document gated on an item rather than on points. It exists to close the loop with the forged verb: the capstone should not function without the thing that was forged.

Acquisition runs through Blackrock Depths, Searing Gorge, Burning Steppes. Those are live join points to the world document, since each is a named location that appears in its own proposals.

Lore anchor: Runeblades are forged objects in Warcraft lore, so a warrior who carries one has acquired an item rather than a power. Warrior's identity in vanilla is defined negatively, as the class with no magic, and this respects that.


### 9.8 Survival (Hunter, reworked)

*The close-range trapper. A hunter who fights beside the pet rather than behind it.*

The only entry that reworks an existing tree rather than adding a fourth, which is why it is Tier 2 and does not need a fresh realm. Vanilla's Survival is already full of traps and melee-adjacent talents and is the weakest of the three precisely because it never committed to either.

**Local mechanic: Traps used offensively rather than defensively.**

Acquired by the **earned** verb. A master, a trial, and a demonstration. The Beastmaster was a hero you hired rather than one you built.

Profession gate: none. None.

Rows one through six offer 57 points against the thirty needed to reach row seven, so roughly half the tree is left behind in any build.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Savage Strikes* (5): Your melee strikes arm your nearest trap. Traps armed this way trigger without being stepped on. A strike at a trapped target triggers it immediately. Killing a trapped target rearms the trap. At full traps your strikes cannot be dodged.
- *Trap Mastery* (3): Traps deal damage instead of only controlling. They apply Serpent Sting. Explosive Trap knocks back.
- *Hunter's Guile* (5): Your traps scale with your ranged attack power. Traps cannot be resisted. They arm instantly. Two may be active at once. A trap that is broken early refunds its cooldown.

**Row 2 (5 pts, 11 available)**
- *Combat Trapping* (1): Your traps may be laid in combat and laying one costs no global cooldown. A trap laid before the pull arms at full strength, and for the first twenty seconds of an encounter your traps and strikes deal increased damage.
- *Deflection* (2): Parrying an attack grants you a short damage reduction. Parrying also refreshes Deterrence.
- *Improved Traps* (3): Trap cooldowns are shared rather than separate. Triggering one resets another. Traps may be laid in combat.
- *Thick Hide* (5): Armor from items is increased. Damage taken is reduced while standing still. Below 35% health you cannot be critically struck. Absorbed damage heals you. A killing blow grants a short damage reduction.

**Row 3 (10 pts, 10 available)**
- *Close Quarters* (5): Your ranged shots do not suffer at melee range. Raptor Strike does not consume your ranged swing. Melee strikes refresh Serpent Sting. A melee critical grants focus. At melee range you cannot be disarmed.
- *Snare Expert* (2): Traps arm faster and their snare cannot be dispelled. A snared target draws nearby enemies toward the trap.
- *Surefooted* (3): You cannot be slowed below base speed. Snares on you are shortened. Movement-impairing effects cannot be reapplied for 4 sec.

**Row 4 (15 pts, 9 available)**
- *Harpoon* (1): Throw a line to an enemy within 25 yards and pull yourself to them. A melee hunter without a gap closer is not a melee hunter.
- *Wyvern Venom* (3): Melee strikes against trapped targets apply a lingering poison. The poison prevents the target regaining health. It spreads when the trap is triggered again.
- *Killer Instinct* (3): Critical strikes arm a trap. A trap triggered by a critical deals double damage. Traps benefit from your critical strike chance.
- *Entrapment* (2): Your traps root what they catch and the root holds longer. The root cannot be broken by your own damage.

**Row 5 (20 pts, 8 available)**
- *Coordinated Assault* (1): Your melee strikes command your pet to strike the same target for bonus damage. Off the global cooldown.
- *Resourcefulness* (3): Melee abilities cost no mana while a trap of yours is armed. Using one arms a trap. Below 30% mana traps arm themselves.
- *Bestial Discipline* (2): Your pet arms traps it walks over. Your pet cannot trigger your own traps.
- *Sole Survivor* (2): *(subtraction)* Your traps arm instantly and cannot be resisted. You may no longer have a pet active.

**Row 6 (25 pts, 8 available)**
- *Pack Instinct* (3): Your pet gains a share of your attack power. It also gains your critical strike chance. It cannot be slowed while a trap of yours is armed.
- *Trapper's Cunning* (2): Traps rearm themselves once after triggering. A rearmed trap costs no cooldown.
- *Ferocious Bond* (3): Coordinated Assault heals your pet. It also removes one harmful effect from it. Your pet cannot die while it is active.

**Row 7 (30 pts, 1 available)**
- *Hunt as One* (1): You and your pet share a single threat pool and a single target. Your coordinated Assault triggers automatically on every third melee strike, and your pet's abilities are usable off your own cooldowns.

<!-- END GENERATED -->

This one talent is the rework. Vanilla traps require leaving combat, which is why the tree never worked, and it is the difference between a defensive tool and an offensive one.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1 (0 pts, 13 available)**
- *Savage Strikes* (5): Your melee strikes arm your nearest trap. Traps armed this way trigger without being stepped on. A strike at a trapped target triggers it immediately. Killing a trapped target rearms the trap. At full traps your strikes cannot be dodged.
- *Trap Mastery* (3): Traps deal damage instead of only controlling. They apply Serpent Sting. Explosive Trap knocks back.
- *Hunter's Guile* (5): Your traps scale with your ranged attack power. Traps cannot be resisted. They arm instantly. Two may be active at once. A trap that is broken early refunds its cooldown.

**Row 2 (5 pts, 11 available)**
- *Combat Trapping* (1): Your traps may be laid in combat and laying one costs no global cooldown. A trap laid before the pull arms at full strength, and for the first twenty seconds of an encounter your traps and strikes deal increased damage.
- *Deflection* (2): Parrying an attack grants you a short damage reduction. Parrying also refreshes Deterrence.
- *Improved Traps* (3): Trap cooldowns are shared rather than separate. Triggering one resets another. Traps may be laid in combat.
- *Thick Hide* (5): Armor from items is increased. Damage taken is reduced while standing still. Below 35% health you cannot be critically struck. Absorbed damage heals you. A killing blow grants a short damage reduction.

**Row 3 (10 pts, 10 available)**
- *Close Quarters* (5): Your ranged shots do not suffer at melee range. Raptor Strike does not consume your ranged swing. Melee strikes refresh Serpent Sting. A melee critical grants focus. At melee range you cannot be disarmed.
- *Snare Expert* (2): Traps arm faster and their snare cannot be dispelled. A snared target draws nearby enemies toward the trap.
- *Surefooted* (3): You cannot be slowed below base speed. Snares on you are shortened. Movement-impairing effects cannot be reapplied for 4 sec.

**Row 4 (15 pts, 9 available)**
- *Harpoon* (1): Throw a line to an enemy within 25 yards and pull yourself to them. A melee hunter without a gap closer is not a melee hunter.
- *Wyvern Venom* (3): Melee strikes against trapped targets apply a lingering poison. The poison prevents the target regaining health. It spreads when the trap is triggered again.
- *Killer Instinct* (3): Critical strikes arm a trap. A trap triggered by a critical deals double damage. Traps benefit from your critical strike chance.
- *Entrapment* (2): Your traps root what they catch and the root holds longer. The root cannot be broken by your own damage.

**Row 5 (20 pts, 8 available)**
- *Coordinated Assault* (1): Your melee strikes command your pet to strike the same target for bonus damage. Off the global cooldown.
- *Resourcefulness* (3): Melee abilities cost no mana while a trap of yours is armed. Using one arms a trap. Below 30% mana traps arm themselves.
- *Bestial Discipline* (2): Your pet arms traps it walks over. Your pet cannot trigger your own traps.
- *Sole Survivor* (2): *(subtraction)* Your traps arm instantly and cannot be resisted. You may no longer have a pet active.

**Row 6 (25 pts, 8 available)**
- *Pack Instinct* (3): Your pet gains a share of your attack power. It also gains your critical strike chance. It cannot be slowed while a trap of yours is armed.
- *Trapper's Cunning* (2): Traps rearm themselves once after triggering. A rearmed trap costs no cooldown.
- *Ferocious Bond* (3): Coordinated Assault heals your pet. It also removes one harmful effect from it. Your pet cannot die while it is active.

**Row 7 (30 pts, 1 available)**
- *Hunt as One* (1): You and your pet share a single threat pool and a single target. Your coordinated Assault triggers automatically on every third melee strike, and your pet's abilities are usable off your own cooldowns.

<!-- END GENERATED -->

**Open item.** Unspecified. Open item.

Lore anchor: Rexxar exists in Warcraft III and in vanilla, fights in melee alongside Misha, and is the archetype fully realized. A hunter tree that produces Rexxar is a tree that produces something the setting already contains.
### 9.9 Chronomancer (Mage)

**Concept.** Healing as reversion. The tree records what an ally used to be and spends the record to put them back.

**Local mechanic.** Echo, a snapshot of an ally's health taken by your spells. It lives on the target rather than in a new resource bar, per the rule in 9.1. Forty-six of the tree's fifty-eight points reference it, which is the highest mechanic coverage of any tree here.

**Verb.** Remembered. **Profession gate.** Enchanting, on the soft-gate rule: access to an enchanter rather than being one, since binding a moment into an object is what enchanting already does.

**Permanent cost.** Cannot be resurrected by another player. Returns unaided after a delay, at a position held earlier in the fight. For a healer, who is a priority resurrection target, that is a real raid cost rather than a flavour line.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1, gate 0, 10 points**

- *Recollection* (5): Your spells record an Echo of an ally's health. Echoes persist through your own death. An Echo taken above 90% health is worth more. Two Echoes may be held per ally. Echoes do not expire while you remain in combat.
- *Borrowed Time* (5): Your heals may be cast before they are needed, landing three seconds later. The delay may be cancelled. A delayed heal landing on a full ally becomes an absorb. Two may be in flight. A delayed heal whose target dies first returns to you as mana.

**Row 2, gate 5, 12 points**

- *Accelerate* (5): Spending an Echo hastens the ally's next action. Their attack speed. Shortens their next cooldown. Extends to anyone else you Echoed recently. Shortens their global cooldown once.
- *Sand in the Glass* (4): Time spent not casting banks mana. The bank may be spent as a burst. It may be shared with an ally you Echoed. It is not lost on taking damage.
- *Dilation* (3): Blink leaves an Echo of your position. Returning to it restores the mana you held. The health, and an ally may trigger the return.

**Row 3, gate 10, 9 points**

- *Temporal Anomaly* (1): Place a stationary field in which healing over time ticks at twice the rate.
- *Regression* (5): Spending an Echo also removes one recently applied debuff. Returns the ally's threat to its recorded value. Restores mana as well as health. Doubles below 20% health. Is not consumed if the ally already sits at the Echo's value.
- *Foresight* (3): You see damage already in flight. A shield cast on an ally with incoming damage absorbs more. The shield's unspent remainder becomes an Echo.

**Row 4, gate 15, 10 points**

- *Stasis* (1): Suspend an ally in time. They take no damage, cannot act, and cannot be healed. Ends on command.
- *Paradox* (5): Two Echoes on one ally may be merged. Merging heals for the difference. A merged Echo cannot be dispelled. Merging refunds mana. A merged Echo may be moved to another ally.
- *Unwind* (4): Your damage spells slow an enemy's casting. The slow holds their cooldown recovery as well. It may be spent to hasten an ally. A slowed enemy's damage arrives late rather than not at all.

**Row 5, gate 20, 8 points**

- *Chronal Bond* (1): The twenty-point mark. Your Echoes are shared with a second ally near the first.
- *Arcane Continuum* (3): *(cross-tree)* Arcane Missiles apply an Echo to the lowest-health party member. Evocation restores an ally's mana as well as your own. Your Presence of Mind applies to your next heal.
- *Frozen Moment* (2): *(cross-tree)* Your Frost Nova applies Stasis to allies caught in it rather than rooting them. Ice Block leaves an Echo where you stood.
- *Fixed Point* (2): *(subtraction)* Your Echoes never expire and always hold their ally's highest value this fight. You may no longer cast any damaging spell.

**Row 6, gate 25, 8 points**

- *Timeless* (5): Your heals cannot be interrupted. cannot be dispelled. Refresh your Echoes on completion. Take a fresh Echo on a critical heal. May record an Echo from an ally's shield value.
- *Second Sunrise* (3): An ally you Echo gains an absorb equal to the gap between their current and recorded health. The absorb decays over time rather than vanishing at once. It refreshes when the Echo does.

**Row 7, gate 30, 1 points**

- *Rewind* (1): Return an ally to the state they held ten seconds ago: their health, and one debuff removed. If they died inside that window, they return at that health. Five minute cooldown.

<!-- END GENERATED -->

**Fifty-eight available points.** Gate twenty carries eight, matching the standard applied across the rebuilt vanilla trees. No node is a pure numeric modifier.

*Rewind is the strongest single effect proposed in either document and the first thing to cut if the tree tunes badly. The tree does not depend on it.*

### 9.10 Dreamer (Druid), candidate

**Status: candidate, not committed.** Argued in `two-trees.md` and measured there against every other tree in the suite. Included here so the two categories in 7.9 can be read side by side, not because the decision is made.

**Concept.** The druid who does not visit the Emerald Dream but brings a piece of it here and holds ground with it.

**Local mechanic.** Threshold, a large persistent piece of the Dream planted on the ground. One at a time. Inside it the world behaves as it does in the Dream, and the Nightmare is the same mechanic inverted.

**Verb.** Dreamt. The ninth verb and the only passive one. You enter a Barrow Den, you sleep, and you do not wake for a long time. Naralex in Wailing Caverns is the cautionary version: a druid who did exactly this and woke into the Nightmare.

**Profession gate.** Herbalism. Access to a herbalist rather than being one. The chain needs living things gathered from all four portal groves, which is what herbalism already does.

**Permanent cost.** You never fully wake. Sleep and fear effects that would be resisted take hold instead, and effects that break on damage do not break for you.

**Lore anchor.** Vanilla has four portals to the Emerald Dream, at Twilight Grove in Duskwood, Seradane in the Hinterlands, Dream Bough in Feralas, and Bough Shadow in Ashenvale. All four are inactive. The Dragons of Nightmare guarding them drop an object that quests to Keeper Remulos and proves to be Malfurion's ring, telling the player he is inside fighting the Nightmare. Four doors, bosses at each, a named person on the other side, and no way through. Nothing in vanilla asserts something and refuses to show it more completely.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1, gate 0, 10 points**

- *Threshold* (1): Plant a large, persistent piece of the Emerald Dream on the ground. Your only one may exist at a time.
- *Rooted Ground* (5): Allies in your Threshold regenerate. Their heals over time tick faster. Their bleeds do not. They cannot be dazed. Leaving carries the regeneration for six seconds.
- *Verdance* (4): Your Nature spells cause plants to take root where they land. Allies who stand among them are healed. The effect grows over time. It spreads along your Entangling Roots.

**Row 2, gate 5, 12 points**

- *Nightmare* (1): You may plant the corrupted version of your Threshold instead, which weakens what stands in it rather than strengthening it.
- *Dread* (5): Enemies in a Nightmare are slowed. They heal for less. Their casts are pushed back. They cannot regain stealth. Their periodic damage runs twice as fast.
- *Wakefulness* (6): You may move your Threshold rather than replanting it. It follows you slowly. Your moving does not interrupt you. Two may exist briefly during a move. Your moving costs no mana. It may snap to an ally instead.

**Row 3, gate 10, 9 points**

- *Lucid* (1): You see stealth and invisibility within thirty yards. What you see, your party sees.
- *Communion* (5): *(subtraction)* Allies within thirty yards share a portion of your spell power. Your critical strike chance and your armor. One of your active buffs. Your Nature's Swiftness. Doubled for anyone standing in your Threshold.
- *Overgrowth* (3): Your Nature spells leave briars where they land, damaging enemies who cross them. Rooting them briefly. The root cannot be dispelled.

**Row 4, gate 15, 10 points**

- *Emerald Vigor* (1): An ally who holds position for five seconds gains an absorb, doubled if they are inside your Threshold.
- *Terror* (5): Your Entangling Roots frighten rather than rooting a target already afraid. The fear is graded rather than binary, reducing damage dealt against immune targets. It spreads on death. It does not break on your damage. The target cannot be healed briefly.
- *Tending* (4): Your Threshold is not destroyed by area damage. It cannot be dispelled. It persists fully through your death. It refreshes when an ally dies inside it.

**Row 5, gate 20, 8 points**

- *Grove of Ysera* (1): *(the mark)* Your Threshold heals for a portion of all damage dealt inside it, by anyone, to anyone.
- *Dreamwalk* (3): *(cross-tree)* Rejuvenation lands at full effect anywhere inside your Threshold regardless of range. Regrowth does as well. Your Moonfire refreshes on enemies standing in a Nightmare.
- *Wildseed* (2): *(cross-tree)* Your Feral forms gain your Threshold's regeneration. They cannot be rooted inside it.
- *Deep Slumber* (2): *(subtraction)* Your Threshold is permanent and cannot be moved or destroyed. You may not leave it.

**Row 6, gate 25, 8 points**

- *The Waking World* (5): Your Threshold's effects reach the whole raid at half strength. Your party at full. Apply Dream and Nightmare simultaneously to the correct targets. Resurrect an ally who dies inside it once per fight. Double its size.
- *Ysera's Regard* (3): Allies who leave your Threshold keep its effects for ten seconds. The duration rises to twenty seconds. The effects hold until they enter combat elsewhere.

**Row 7, gate 30, 1 points**

- *Open the Way* (1): Your Threshold becomes a portal for twenty seconds. Your allies may step through and are untargetable, healed, and cleansed while inside, returning where they entered. You cannot enter it yourself.

<!-- END GENERATED -->

**58 available points, gate 20 carries 8, no node is a pure numeric modifier.** Mechanic coverage 77%, inside the 40 to 80 band established after the first version measured 100% and was judged brittle.

### 9.11 Radiance (Priest), candidate

**Status: candidate, not committed.** Argued in `two-trees.md` and measured there against every other tree in the suite. Included here so the two categories in 7.9 can be read side by side, not because the decision is made.

**Concept.** The heretical Light. Healing and harm are one act, and the priest cannot do either alone.

**Local mechanic.** Corona. Your healing emits outward and damages what stands near its target; your damage emits outward and heals what stands near its. Nothing you cast affects only one thing.

**Verb.** Recanted. The tenth verb. You publicly renounced the doctrine and the Light did not leave you. The chain is a trial rather than a lesson, and the only acquisition on the list where the character is tested and nothing is taken away.

**Profession gate.** Enchanting. Access to an enchanter. The trial requires a focus that survives being told it is heresy, which is a disenchanting problem.

**Permanent cost.** You can no longer cast Power Word: Shield or any absorb. You do not prevent.

**Lore anchor.** Holy Nova has damaged enemies and healed allies in one cast since launch, sits in the Holy tree, is famously weak, and is taken by nobody. The fantasy of the Light as an act that comforts and sears at once has existed in the game since launch as a single bad spell with nothing built around it.

<!-- GENERATED: tree rows, source talent-data.json, do not hand edit -->

**Row 1, gate 0, 10 points**

- *Corona* (1): Healing emits outward and damages nearby enemies. Your damage emits outward and heals nearby allies.
- *Effulgence* (5): The emission reaches further. It cannot be resisted. It ignores line of sight. It prefers wounded allies and healthy enemies. It strikes a second ring at half effect.
- *Kindling* (4): Your heals build a stack. At five your next emission doubles. Your stacks persist through target changes. Overhealing builds two.

**Row 2, gate 5, 12 points**

- *Searing Mercy* (5): The damage half of your emission scales with the healing the cast did. With overhealing specifically. Applies Holy Fire's burn. Cannot be reflected. Refreshes when the enemy takes further damage.
- *Sanctuary* (4): The healing half of your emission scales with damage done. It reaches your whole party. It heals for the excess when an enemy dies inside it. It cleanses one effect.
- *Holy Nova* (3): Holy Nova costs less than a heal of the same rank. It emits a Corona at full value. It refreshes Kindling.

**Row 3, gate 10, 9 points**

- *Revelation* (1): Brand a target. Your emissions centre on the brand rather than on your cast.
- *Doctrine* (5): Your emission may be aimed. Split between two points. Held for one global cooldown and released. Centred on an ally instead of yourself. Centred on a corpse.
- *Unbroken* (3): Your casts cannot be pushed back while any ally is below half health. While any enemy is branded. At all during Absolution.

**Row 4, gate 15, 10 points**

- *Conflagrant Grace* (1): For ten seconds your healing lands at full value on allies and full damage on enemies with no falloff.
- *Zealotry* (5): *(subtraction)* Critical heals critically damage, and the reverse. A critical builds two Kindling. Your criticals cannot be resisted. A critical on a branded target resets Revelation. Two criticals in a row make your next cast instant.
- *Penitence* (4): Healing yourself damages what is attacking you. It strikes everything nearby as well. It applies your brand. It heals your attackers' targets.

**Row 5, gate 20, 8 points**

- *Congregation* (1): *(the mark)* Your emissions also emit from every ally you healed in the last three seconds.
- *Radiant Word* (3): *(cross-tree)* Smite carries a full emission. Holy Fire carries a full emission as well. Renew's ticks each emit at reduced value.
- *Shadow's Mirror* (2): *(cross-tree)* Shadow Word: Pain's ticks emit healing. Mind Blast emits at full value.
- *Apostasy* (2): *(subtraction)* Your emissions double in size and effect. You may no longer target allies with any spell, so all of your healing is emission and none of it is aimed.

**Row 6, gate 25, 8 points**

- *The Unquiet Light* (5): Your emission persists on the ground for three seconds. Follows the branded target. Leaves a trail as you move. Triggers again when the brand expires. Applies to everything your party heals.
- *Litany* (3): *(the mark)* Your Holy damage rises with each ally your healing has touched. The count does not reset on death. Holy Nova counts every ally it reaches.

**Row 7, gate 30, 1 points**

- *Absolution* (1): For twelve seconds every point of healing you do is dealt again as holy damage to every enemy in range, and every point of damage you deal is healed again to every ally in range, with no falloff and no cap on targets.

<!-- END GENERATED -->

**58 available points, gate 20 carries 8, no node is a pure numeric modifier.** Mechanic coverage 70%. Fingerprints at 0.97 against vanilla Holy priest, which resolves once the Holy rebuild removes its Smite and Holy Fire content.

### 9.12 What the point math produces

Fifty-one points, four trees. Some builds worth naming, because they demonstrate that the fluid model produces characters rather than mistakes.

- **31 Blackguard / 20 Protection.** A death knight who still tanks. Damnation plus enough Protection for defensive fundamentals.
- **20 Blackguard / 31 Retribution.** A paladin who dabbled. Blood Rite as an emergency button in an otherwise Light-driven build, and the Blessings still work because Damnation was never taken.
- **31 Necromancy / 20 Frost.** A caster with three Risen and enough Frost for control.
- **20 Necromancy / 31 Arcane.** A mage with a temporary skeleton and a real burst spec.
- **31 Bladedancer / 20 Combat.** Sustained multi-target melee.
- **20 Conduit / 31 Restoration.** A healer who bonds a totem to the tank. Probably the most immediately popular build on this list.

The pattern in every case is that twenty points is a flavor and thirty-one is an identity, and both are legitimate. That is what Section 6 asked for and it is the reason no exclusivity rule is needed anywhere.

---

## 10. Open Items

Three acquisition chains are unspecified. Section 8.6 names locations for Blackguard, Necromancy, Metamorphosis, and Runeblade. Bladedancer, Conduit, and Survival have verbs but no route. Bladedancer's is **copied**, so it wants somebody worth watching fight. Conduit's is **granted**, so it wants an elemental site willing to refuse. Survival's is **earned**, so it wants a master, and Rexxar is already in the game.

Fist weapon itemization is thin in vanilla, and the Bladedancer fork depends on it. Filling that lane in is additive Tier 1 work but it is a prerequisite rather than a nice-to-have, since half the tree is unplayable without weapons to play it with.

---

## 11. What This Costs, Honestly

Three problems, stated plainly.

**Talent points do not stretch.** Fifty-one points across four trees is different from fifty-one across three, and every existing build becomes a comparison against a new option. Some existing deep specs will lose players not because they got worse but because something new is adjacent. That is a real cost and there is no way to avoid it.

**Balance does not become easy, only smaller.** A tree is easier to tune than a class because it shares gear, resource, and baseline abilities with something already balanced. It is not easy. Warlock with a viable tank tree is a different balance problem than warlock without one.

**Some of this is worse than the original.** Frost DK as a warrior runeblade tree is a shadow of Frost DK. Anyone who loved that spec will find this version thin. The argument for it is that it costs a fraction as much and fits the game it is being added to, not that it is better.

The counter to all three is the one from Section 2. Every item here ships in a content patch, can be revised in the next one, and does not commit the game to a starting zone, a faction decision, or an itemization lane. In a project whose entire premise is a long additive cadence, that is worth a great deal.

---

## Appendix A: Summary Table

| Host | Tree | Retail source | Local mechanic | 20-point mark | 31-point capstone |
|---|---|---|---|---|---|
| Paladin | Blackguard | Death Knight, Blood plus core identity | Blight | Blood Rite | Damnation |
| Mage | Necromancy | Necromancer, Unholy's caster half | The Risen | Raise Skeleton | Command the Damned |
| Warlock | Metamorphosis | Demon Hunter, Vengeance | Fel corruption | Fel Aegis | Metamorphosis |
| Rogue | Bladedancer | Havoc plus Windwalker | Momentum, forked by weapon | Whirling Blades | Unending Dance |
| Shaman | Conduit | Evoker, all three specs | Empowerment | Elemental Bond | Confluence |
| Warrior | Runeblade | Death Knight, Frost only | Rune charges | Hoarfrost | The Runeblade |
| Hunter | Survival, reworked | Survival, 2016 version | Offensive traps | Coordinated Assault | Hunt as One |
| Mage | Chronomancer | None; Bronze Dragonflight fiction | Echo | Chronal Bond | Rewind |
| Druid | Dreamer, candidate | None; the four inactive Dream portals | Threshold | Grove of Ysera | Open the Way |
| Priest | Radiance, candidate | None; Holy Nova, unused since launch | Corona | Congregation | Absolution |
| Priest | Absorbs nothing | Mistweaver as a talent at most | | | |
| Druid | Absorbs nothing | | | | |

Acquisition verbs, deployment, and tier per tree:

| Tree | Verb | Profession gate | Tier |
|---|---|---|---|
| Blackguard | Fallen | None, deliberately | 3, fresh realm |
| Necromancy | Taught | Alchemy | 3, fresh realm |
| Metamorphosis | Taken | Tailoring, Enchanting | 3, fresh realm |
| Bladedancer | Copied | Leatherworking | 3, fresh realm |
| Conduit | Granted | None | 3, fresh realm |
| Runeblade | Forged | Blacksmithing, Weaponsmith | 3, fresh realm |
| Survival | Earned | None | 2, no fresh realm needed |
| Chronomancer | Remembered | Enchanting | 3, fresh realm |
| Dreamer | Dreamt | Herbalism | 3, fresh realm |
| Radiance | Recanted | Enchanting | 3, fresh realm |

## Appendix B: Specs That Do Not Survive

Fourteen specs across four post-vanilla classes reduce to seven trees. Chronomancer is the eighth and reduces nothing: it has no retail source and exists because the fantasy is available and the host needs it. What follows is what is lost and why it is not a loss.

- **Blood and Frost DK merge**, split across paladin and warrior. They were separate because a class needs three specs.
- **Unholy DK splits.** Its necromancy goes to mage. Its plate melee framing is dropped.
- **Havoc and Vengeance DH separate.** They were never one idea, only one class.
- **Brewmaster Monk is dropped.** Druid bear is already the leather tank with active mitigation, and stagger is a variation on frenzied regeneration rather than a distinct concept.
- **Mistweaver Monk is dropped as a tree** and survives as a priest talent at most.
- **Windwalker merges with Havoc** on rogue, keeping the rhythm, the fist weapons, and the vestigial unarmed skill, and dropping chi and the pandaren framing. The merge is not a flattening: the weapon fork in 9.5 lets one tree present as either fantasy depending on what is equipped, so nothing was actually lost except two separate talent trees. Monk is the one modern class this document concludes did not need to exist at all; one spec of it survives, and it survives as a way of playing rather than as a class.
- **Devastation and Preservation Evoker merge**, since the split served the three-spec requirement.
- **Augmentation survives** as the most novel idea in the set.

The pattern is the argument. Every spec that disappears is one that existed because a class needs three, not because a fantasy needed a home.

---

## Sources

[1] "Metamorphosis (warlock ability)," Warcraft Wiki. https://warcraft.wiki.gg/wiki/Metamorphosis_(warlock_ability)

[2] "Metamorphosis (warlock ability)," Wowpedia. https://wowpedia.fandom.com/wiki/Metamorphosis_(warlock_ability)

[3] "New Class and Role Combinations in Season of Discovery," WowCarry. https://wowcarry.com/blog/wow-classic/unlocking-new-class-role-combinations-embrace-the-season-of-discovery

[4] "Season of Discovery Demonology Warlock Tank Guide," Icy Veins. https://www.icy-veins.com/wow-classic/demonology-warlock-tank-season-of-discovery-pve-guide

[5] "Warlock Tank Guide and Best Runes," Warcraft Tavern. https://www.warcrafttavern.com/wow-classic-sod/guides/warlock-tank/

[6] "WoW Season of Discovery: How To Get Metamorphosis," Game Rant. https://gamerant.com/wow-season-of-discovery-warlock-metamorphosis-unlock-rune-guide-sod/

[7] "Get an Early Look at Hero Talents in The War Within," Blizzard News. https://news.blizzard.com/en-us/article/24038519/get-an-early-look-at-hero-talents-in-the-war-within

[8] "WoW The War Within: Hero Talents Explained," GameLeap. https://www.gameleap.com/articles/wow-the-war-within-hero-talents-explained

[9] "World of Warcraft: The War Within Hero Talents explained," Dexerto. https://www.dexerto.com/world-of-warcraft/world-of-warcraft-the-war-within-hero-talents-explained-2438284/

[10] "Warcraft III heroes," Warcraft Wiki. https://warcraft.wiki.gg/wiki/Warcraft_III_heroes

[11] "Warcraft III hero units," WoWWiki. https://wowwiki-archive.fandom.com/wiki/Warcraft_III_hero_units
