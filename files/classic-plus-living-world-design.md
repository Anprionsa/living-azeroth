# A Living Azeroth
## Design Notes for WoW Classic+ World Systems

**Version 1.2 | July 2026**

*Revision 1.2 replaces the binary in 10.2 (a zone either turns or it does not) with three tiers of seasonal response, and works all forty-plus zones of both continents individually against them. That pass corrected the latitude model in 10.1, which predicts temperature but not moisture, and sorted the arrested zones into residue, active, and held. Also adds 4.6, creatures reacting to corpses, and folds nine previously unused lore anchors into the sections they serve: 1.8, 2.8, 3.5, 4.6, 4.7, 5, 6.8, 8.12, 9.5, and 10.8. Adds 7.7 and 8.13 on reagent legibility, the rule being to add texture to materials without adding item slots. Adds Section 12 on art direction, which is also the first proposal whose risk tier and cost diverge, and whose 12.3 extends material sourcing from an art question into a world-logic one. Adds 11.3 to 11.6, which reframe the document for a shipped game: an additive versus revisionary distinction, a four-layer dependency ordering, the argument that hooks are the only thing that cannot be retrofitted, and 11.7 to 11.8 sorting every proposal into live, PTR, or fresh realm. Adds Section 13 on adding to the world, which argues for inward additions through doors vanilla already drew. Adds 6.9 to 6.11 and a sixth design constraint, settling the world-state architecture: cyclical by default, permanent only when additive, phasing effectively never. Adds 4.8 and 10.9 on weather, with the rule that weather changes what is available rather than what a player is capable of. Resolves the three open questions in 10.5: counts are visible, they move under accepted quests with progress held proportionally, and scope is derived from whether the world moved the thing being asked for.*

*Companion document: a separate proposal covers absorbing post-vanilla classes as talent trees rather than classes. It shares this document's tier vocabulary but is fresh-realm-only by nature, and nothing here depends on it.*

*Revision 1.1 closes five gaps in 1.0: the two trainer proposals referenced in Appendix A had no body text (now 8.10 and 8.11), caravan robbery had no stated cost (2.6), realm ruleset was unaddressed (2.7), the trade network was never mechanically connected to vendor stock (9.4), and flare-ups had no protection against destroying quest content (6.7).*

---

## 0. Status and Scope

As of July 2026, Blizzard has not announced a product called "Classic+." What is on the record is narrower: at the State of Azeroth stream on January 29, 2026, Blizzard said that clarity on Classic's future and Anniversary realm progression would come at BlizzCon 2026, which is confirmed for September 12 and 13 in Anaheim [1]. Everything else is community inference built on a real but ambiguous evidence base: the "Project Camelot" datamine, a sustained run of encrypted internal builds tagged around version 1.60, private server takedowns, and a May 2026 creator summit at Blizzard's Irvine campus that pulled in Xaryu, Esfand, Guzu, Savix, and sodapoppin under NDA [2][3][4].

Season of Discovery is the closest thing to a stated precedent. It demonstrated that Blizzard is willing to break vanilla's rules (healing mages, tanking warlocks) on a sandboxed realm, and that a meaningful audience shows up for a Classic that deviates from the 2004 design rather than recreating it [5][6].

This document assumes nothing about what Blizzard is actually building. It is a design proposal, not a prediction.

### What this document is about

Most Classic+ speculation concentrates on the loud stuff: new classes, new raids, new zones, itemization overhauls. This document deliberately covers the opposite category. It is about world texture, the systems that determine whether Azeroth reads as an inhabited place or a static diorama with mobs standing in assigned boxes.

The unifying observation is that vanilla WoW is full of lore that the game world never actually depicts. Quest text tells you the Kolkar centaur are breaking through Horde lines. Zone descriptions tell you the Venture Company is stripping Stonetalon bare. Faction pages tell you the Steamwheedle Cartel and the Venture Company are in open commercial war. None of this is visible in the world itself. The camps face each other and nothing happens.

Almost every proposal here follows the same method: find something the existing lore already asserts, and make the world show it.

### Design constraints applied throughout

1. **Specificity over abstraction.** Every proposal is anchored to a named vanilla location, faction, or NPC. "Add wandering merchants" is not a design. "Run a Venture Company ore wagon down the Talondeep Path into the Barrens" is.
2. **Vanilla-appropriate, not expansion-appropriate.** Systems imported from The Burning Crusade forward get rebuilt around vanilla's mechanics rather than transplanted. Gem sockets do not exist in Classic, so jewelcrafting cannot be a socket profession.
3. **Discovery over checklists.** Rare content should be rare enough that deliberate farming is inefficient. The target player reaction is "I got the weirdest drop," not "here is the wiki page telling you where to camp it."
4. **Not everything needs a mechanic.** A meaningful share of these proposals have no interaction hook at all. They exist to be seen from a road, heard over a ridge, or glimpsed from a zeppelin.
5. **Implementation cost is a first-class design input.** Section 11 sorts every proposal into three tiers by how deeply it touches the game's architecture, because that determines whether something can be patched in later or has to be a launch decision.
6. **World-indexed change, not player-indexed change.** The world changes on its own schedule and the player happens to be present for it. It does not change because of what the player did or what level they are. This is the sharpest fork in the road for any living-world proposal and 6.9 argues it at length, because the obvious alternative is phasing and phasing is the single most un-Classic technology available.

---

## 1. Ambient Life: NPCs Doing Their Jobs

The cheapest immersion win in the game is idle animation variety tied to what a faction actually does for a living. Not combat behavior. Not quest hooks. Just work, rest, and downtime.

### 1.1 Grave robbing and the Duskwood cemeteries

Duskwood's two graveyards, Tranquil Gardens Cemetery southeast of Darkshire and Raven Hill Cemetery to the west, are the zone's thematic core [7]. The hostile humanoids and undead scattered around them currently stand still.

Give them a job. Figures working the Tranquil Gardens plots should cycle: kneel and dig, pry at a lid, straighten up, move to the next plot. A rare variant has two of them shoving each other over something found in a grave, which sells "criminals" rather than "sentries." Because Duskwood's tone is horror rather than action, an occasional nervous glance up the road toward the Rotting Orchard adds dread at zero mechanical cost.

Duskwood already has a grave robbing narrative baked in. Abercrombie, the hermit northeast of Raven Hill Cemetery, has the player gathering grave moss and body parts, and his stitched creation eventually walks the road to Darkshire. The ambient behavior around the cemeteries should look like the same world that produced Abercrombie.

### 1.2 Bloodsail Buccaneers on downtime

The Bloodsail camps along the Stranglethorn coast are currently patrol grids. They should be camps. A cluster sitting on crates around a low fire, a dice or cards animation, one standing to stretch or drink, another watching the water. Because the Bloodsail's defining relationship in vanilla is their rivalry with Booty Bay and the Blackwater Raiders who protect it [8], the occasional gesture toward the coastline reinforces their identity as blockade runners without adding a single quest.

### 1.3 Venture Company logging crews, Windshear Crag

Windshear Crag in the Stonetalon Mountains has been clear-cut by Venture Company logging, with the surrounding air fouled by soot and the water spoiled by oil and waste, and the local operation runs under the leprous gnome Gerenzo Wrenchwhistle [9]. That is a described industrial operation, and the zone shows almost none of it in motion.

Build the work chain visibly:
- A chopper crew felling a marked tree
- A shredder hauling the log to a stacking yard
- A foreman with a clipboard checking loads between hauls

This connects directly to the cart network in Section 2. The stacked lumber is the cargo.

### 1.4 Dark Iron crews near Ironforge

Loch Modan already carries a Dark Iron sabotage plot: Chief Engineer Hinderweir VII at Stonewrought Dam has the player investigating Dark Iron explosive charges planted at the dam, and the trail leads north to Dun Modr in the Wetlands [10]. There is also a standing "WANTED: The Dark Iron Spy" bounty in the zone.

Make the encroachment visible. A working crew rather than a set of identical pickaxe-swingers: one or two chipping at a face, a hauler moving an ore cart toward a stockpile, a foreman inspecting the load. A scout at a tunnel mouth watching the road toward Ironforge sells "they are probing our defenses," which is what the quest chain already claims is happening.

### 1.5 Booty Bay docks

Booty Bay is a functioning port in fiction and a static backdrop in practice. Goblin dockworkers moving crates off ships and stacking them near the harbor, with the occasional dropped crate cracking open, gives the town its trade identity. Layering a Bloodsail scout at the pier's edge, periodically shooed off by a bruiser, dramatizes a rivalry that currently exists only as an inverse reputation relationship in a menu [8].

### 1.6 City density with routines, not just headcount

Adding NPCs without adding behavior produces a crowd of statues. The routines matter more than the numbers.

**Stormwind.** The orphanage and its matron already exist. Children playing near the Cathedral steps during the day and being called inside at dusk extends NPCs the game already has.

**Ironforge.** Bruuk's Corner in the Military Ward is an established drinking spot. Patrons stumbling out on a bark cycle, and miners actually traveling the road out toward Gol'Bolar Quarry instead of standing at a fixed post, uses mining lore the zone already establishes.

**Orgrimmar.** The Ring of Valor sits in the Valley of Strength. Grunts sparring there on a cycle, and guard patrols visibly rotating between the Valley of Strength and the Valley of Wisdom, dramatizes the militarized city that Orgrimmar's design implies but never shows.

**Booty Bay.** Already the chaos city by design. It should be the densest and the most visibly transactional of the four.

### 1.7 Hard-to-reach NPCs with a lore payoff

Vanilla exploration culture is built around reaching places the designers did not obviously intend. Reward it, sparingly, with content rather than a copy-pasted mob.

- **Ironforge's exterior mountain ledges.** A dwarven hermit with dialogue touching Titan-forged lore, a body of story vanilla barely gestures at.
- **Blackrock Mountain's outer cliffs.** An orc lorekeeper or a Dark Iron captive, connecting the surface world to a storyline otherwise locked behind two dungeons and a raid.
- **Un'goro Crater's plateaus.** A Cenarion Circle researcher working alone above Marshal's Refuge, with notes that reference the zone's druidic and Emerald Dream themes.

None of these should be quest-critical. The payoff is that the lore exists at all, in a place most players will never stand.

### 1.8 The Park district and the guild that stopped working

Stormwind's Park district is unfinished, and the reason is standing in the keep. The Stonemasons Guild rebuilt the city after the Second War and was not paid, both sides manipulated by Lady Katrana Prestor, and when Edwin VanCleef demanded restitution the House of Nobles ordered the guild disbanded [31][32][33].

None of that needs narrating. It needs dressing. Idle masons with nothing to do, unfinished stonework, tools and cut blocks left where a crew walked off. A player who has run the Deadmines and then notices the Park has assembled the connection themselves, which is worth more than any quest text saying it.

Scope note: the Prestor material is genuinely vanilla and surfaces through the Marshal Windsor chain and the Onyxia attunement, but the fullest version of the Stonemasons backstory comes from supplementary material. Build on what a Classic player can reach in the client and let the rest sit behind it. The consequence for Westfall's supply lines is in 9.5.

---

## 2. Roads and Traffic

### 2.1 The core proposal

Carts and wagons that travel real roads on real routes, which players can ride, escort, rob, or simply watch go past. This is the load-bearing feature of the whole document because it connects the ambient layer (Section 1) to the economic layer (Section 9).

Vanilla already contains every component. It has escort quests with NPCs pathing long distances under attack, including the Loch Modan run where Miran is escorted to Ironband's Excavation and ambushed by Dark Iron dwarves partway [10], and the Barrens run where Gilthares Firebough is escorted from Northwatch Hold all the way back to Ratchet [11]. It has NPCs that run circuits between named locations, notably the Defias Messenger, whose scouted route between Moonbrook, the Gold Coast Quarry, and the Jangolode Mine is the object of a Westfall quest [12]. What it does not have is that behavior as standing world furniture rather than as a quest object.

### 2.2 Kalimdor routes

**The Gold Road, Crossroads to Camp Taurajo.** The Barrens already frames the Kolkar centaur as an active military problem: Regthar Deathgate holds a fortified camp west of the Crossroads specifically to stop the centaur from breaking through Horde defenses [11]. A supply wagon running the Gold Road with a small grunt escort, subject to Kolkar raids, does not invent a conflict. It stages one the zone already asserts.

Note also that the Barrens description says the large predators tend to avoid the Gold Road [11], which is a small piece of existing ecological reasoning worth preserving and building on (see Section 6).

**Talondeep Path, Windshear Crag down into the Barrens.** Venture Company lumber and ore leaving Stonetalon. This gives the logging crews in Section 1.3 an output and gives the cargo a specific identity: it is a resource shipment cutting through contested ground, which supplies a motive for anyone who attacks it.

**Thousand Needles to Gadgetzan.** A second Venture Company route running south through the Shimmering Flats toward Tanaris, which positions Venture as supplier and Steamwheedle as buyer. More on why that matters in Section 3.

### 2.3 Eastern Kingdoms routes

**Ironforge to Menethil Harbor through Loch Modan and Dun Algaz.** Loch Modan is explicitly framed as the source of Ironforge's mercantile strength, and Dun Algaz is the sieged choke point between it and the Wetlands [10][13]. A standing dwarven supply road along that corridor, subject to interference from the Mo'grosh ogres in Loch Modan and from the Dragonmaw presence in the Wetlands, is the most obviously justified route in the game.

**Lakeshire to Darkshire.** Big Will's roadside camp already sits on this route. A cart running it, with the odds of an ambush scaling against how many guards are riding, reuses existing NPCs rather than inventing a new threat.

**Undercity through Silverpine to the Sepulcher.** Forsaken logistics rather than commerce: blight barrels, apothecary supplies, plague research materials. Silverpine's real vanilla antagonists are the Dalaran wizards holding Ambermill, the Rot Hide gnolls on Fenris Isle under Thule Ravenclaw, the worgen curse around Pyrewood, and Alliance incursions coming north out of Southshore [14]. Any of those can hit the wagon. (The Scarlet Crusade presence on Fenris Isle is a much later retcon and should not be used as a vanilla anchor. See Appendix B.)

**Southshore and Tarren Mill.** The oldest standing world PvP flashpoint in the game. Running an Alliance supply wagon toward Menethil and a Forsaken wagon toward Undercity through the same contested ground makes that conflict read as disruption of real logistics rather than two towns that dislike each other.

### 2.4 Why Eastern Kingdoms should feel older

Kalimdor's trade web should read as opportunistic and recent. The goblin cartels are prospecting, the Horde presence is a few years old, and the routes look improvised.

Eastern Kingdoms should read as centuries deep. The dwarf-human alliance is old, Loch Modan is described as among the most peaceful regions on the continent behind Algaz Gate [13], and the Deeprun Tram physically connects two capitals. Its routes should feel worn: standing checkpoints, established schedules, roads with names. The contrast is worth designing for deliberately rather than treating all trade the same.

### 2.5 Interactive versus observational

Not every route should be reachable. Three visibility tiers:

**Walkable and interactive.** Roads players already travel. The Gold Road, the Loch Modan corridor, Lakeshire to Darkshire. Ridable, escortable, robbable.

**Visible but not reachable.** Ships leaving Menethil Harbor on a schedule. The zeppelin network is the strongest case here: from the Orgrimmar, Undercity, and Grom'gol towers, a player at altitude can be shown a Bloodsail action on the Stranglethorn coast or a centaur skirmish on the Barrens plain, entirely unreachable from the platform. This is a genuinely different kind of witnessing than walking past something.

**Geographically impossible.** The Badlands and Searing Gorge canyons make this easy. A Dark Iron cart moving along a ledge across an unreachable ravine, between Kargath and the Blackrock approaches, exists purely to be wondered about.

### 2.6 The cost of robbery

Section 2.1 says players can rob these carts and does not say what that costs. The answer is already sitting in vanilla's reputation system and does not require inventing a penalty.

Steamwheedle Cartel reputation is a single shared bar across all four cities. Booty Bay, Ratchet, Gadgetzan, and Everlook read from it together, so dropping far enough makes the bruisers hostile in all four at once and costs auction house access at three of them [8][21]. That is already among the harshest self-inflicted penalties available in vanilla, and it is the reason the Bloodsail grind has the reputation it does.

The gradient falls out of existing faction standings:

**Venture Company wagons.** Already hostile, so no cost and no decision. This is the entry-level target and it should stay that way. It gives a new player somewhere to learn the mechanic without a trap attached to it.

**Steamwheedle wagons.** Real reputation loss across four cities, recoverable but slow. This is the only version of the mechanic with an actual decision inside it, and it should be the one the design points at.

**Own-faction wagons.** Not attackable, same as any other friendly NPC.

**Opposing-faction wagons.** An act of war under normal PvP rules, with no reputation cost attached. See 2.7.

The part worth building deliberately is the Bloodsail inverse. Steamwheedle and Bloodsail standing already move against each other in vanilla [8][21]. Repeatedly hitting cartel cargo should raise Bloodsail reputation, which turns that grind from killing Booty Bay bruisers until they hate you into actually behaving like a blockade runner. Same reputation system, same numbers, pointed at behavior that matches the fiction instead of at a farming loop.

### 2.7 Realm ruleset

Routes inherit the ruleset of whatever zone they cross. That produces a difficulty gradient for free, without a single new rule, and in at least one case it produces one that agrees with the lore.

The Ironforge to Menethil corridor is the clean example. Loch Modan is Alliance territory and the Wetlands is contested, so an Alliance driver is safe until Dun Algaz and exposed after it. That is precisely what the fiction already says Algaz Gate is: the frontier, with the peaceful country behind it [13]. Nobody has to design that curve. It is a consequence of where the road goes.

Southshore and Tarren Mill is the opposite case and the sharpest one. Both wagons run the same contested corridor, which makes them competing objectives in the oldest world PvP flashpoint in the game rather than two towns that dislike each other.

Two consequences worth stating rather than discovering later:

**PvE realms lose an entire threat category.** With no opposing players, the NPC threats carry the whole load. That is workable, but it means the predator behavior in 4.5 and the flare-ups in Section 6 are doing more work on a PvE realm than on a PvP one, and they need to be tuned twice rather than once.

**Wagons must not become a griefing engine.** Nothing about destroying a wagon should reward camping one. The cargo is the reward, it is finite per wagon, and the destruction itself carries no kill credit, no honor, and no bonus. A level sixty parked on the Gold Road killing every caravan that passes should be wasting an afternoon for nothing.

### 2.8 Route funneling and the chokepoints the map already has

Routes matter far more when they funnel. A caravan system with traffic spread evenly across the map is scenery; one where a few crossings carry nearly everything has geography with stakes.

The chokepoints already exist and cost nothing to use. Every crossing between the continents runs through a boat, which on the Eastern Kingdoms side means Menethil Harbor. The land route from Arathi into the Wetlands crosses the Thandol Span, one damaged dwarven bridge. Dun Algaz is the only pass from the Wetlands toward Loch Modan, which 2.7 already leans on for its safe-corridor argument.

Weight the routes accordingly and Menethil becomes the most valuable point on the continent, the Thandol Span becomes worth watching, and the robbery economics in 2.6 change depending on where a player chooses to sit. This is a route authoring decision rather than a new system, which puts it at Tier 1.

---

## 3. The Trade Network

### 3.1 The rivalry the game already has

The Steamwheedle Cartel controls four cities in Classic: Booty Bay, Ratchet, Gadgetzan, and Everlook. It is neutral by policy, profitable because of that neutrality, and it is in direct commercial competition with the Venture Company, another goblin cartel, with neither side above sabotage or murder [8].

That is a fully formed economic conflict sitting unused. The Venture Company appears in-game only as hostile mobs at work sites. The Steamwheedle cities appear only as auction house stops. Nothing connects them.

### 3.2 The Kalimdor web

**Supply side: Venture Company.** Windshear Crag lumber and ore moving south and east. Their Thousand Needles operations feeding a second route toward Gadgetzan. Venture is the extraction arm.

**Demand side: Steamwheedle.** Ratchet, Gadgetzan, Booty Bay, and Everlook as buyers and redistributors. Give each an arriving-and-departing traffic pattern: a quartermaster logging a wagon in at the Ratchet dock, a ship departing for Booty Bay, crates moving in Gadgetzan. Ratchet already runs a boat to Booty Bay in vanilla [11], so the sea link is not an invention.

**The friction point.** A Steamwheedle shipment moving between Ratchet and Booty Bay can be harassed by Bloodsail raiders along the Stranglethorn coast. That turns the Bloodsail from a static reputation grind into a visible commercial threat, which is exactly what they are in fiction.

**Everlook is Steamwheedle, not Venture.** Worth stating plainly because it is commonly misremembered. Everlook is one of the four cartel cities [8]. If a Winterspring route is wanted, the interesting version is a hard, high-level Steamwheedle supply run down through Felwood, not a Venture-controlled corridor.

### 3.3 The Eastern Kingdoms spine

Deliberately kept separate from the goblin web. The Ironforge-to-Menethil corridor and the Undercity-to-Sepulcher run are domestic Alliance and Forsaken logistics, not cartel trade. Keeping them isolated makes a worldbuilding point: the factions run their own internal supply, and the goblins run the cross-continent commercial layer that both sides use and neither controls.

### 3.4 What this buys

Once routes exist, three other systems get load-bearing:

- Predators and raiders gain targets that matter (Section 6.5)
- Regional vendor stock gains a physical explanation (Section 9)
- The Venture and Steamwheedle rivalry gains a visible battleground

### 3.5 Why the goblins need this and nobody else does

The strongest argument for the whole trade network is not mechanical, and the document has so far made only the mechanical case. It is that the Steamwheedle cities physically cannot supply themselves, and the map has been saying so since 2004.

All four sit where nobody else wanted to be. Booty Bay is built into a cliff face in hostile jungle. Ratchet is a landing on a barren coast. Gadgetzan is in the middle of a desert. Everlook is in a frozen valley above a cloud bank, reachable on foot only through a furbolg tunnel. Everlook cannot produce what Everlook sells. Neither can Gadgetzan. The goblins are neutral traders in part because they chose sites that leave them no other option.

So the caravan system is not something being added to the world. It is something the world has implied for twenty years and never drawn. Every wagon on the Winterspring road exists because there is no other way that vendor has stock.

This also gives the NPC-to-player supply ratio in 9.4 a natural per-city variation rather than one global number. Booty Bay is a port with sea access. Everlook is a dead end at the top of a mountain. They should not resupply at the same rate, and the map already tells you which is which.

---

## 4. Wildlife and Ecology

Vanilla's beasts are combat units with animal models. Every one of them notices you at the same radius, approaches the same way, and stands in the same place until it does.

### 4.1 Pack structure

Timber wolves in Elwynn and Ashenvale spawn in loose clusters that behave as individuals. A real pack has one or two members stalking at a distance, low, before the group commits together. Bears are solitary in nature and should stay solitary in game, but with a wide patrol between a den and a feeding site rather than a fixed spawn point. Two different behavior models on adjacent creatures is worth more than either one alone.

### 4.2 Rest cycles

This is the proposal with the largest gameplay consequence in the section. A pack can bed down near a den for a real window, non-aggressive or aggro-immune at range, waking only if physically disturbed. That creates a live decision: sneak past, or wake the den deliberately because you want the kills. Weather-linked denning (bears holing up during rain) gives the same idea a smaller, more frequent expression.

### 4.3 Concealment and the art dependency

This is the one part of the section that requires art changes rather than behavior changes. Ambush predators should be hard to see. Cats curled in tall grass under low branches in Duskwood or Ashenvale, rather than standing in a clearing.

That requires denser underbrush placed intentionally near predator spawns, functioning as camouflage rather than as decoration. It is the single highest-cost item in this section and should be scoped as a per-zone art pass, not a global one.

### 4.4 Species-specific behavior

- **Boars.** Rooting at the ground rather than standing idle. Pure animation loop, near-zero cost.
- **Raptors.** Fan out to flank instead of queueing single file. An alpha that postures or screeches before the group commits gives a half-second tell, which is what a real pack hunter telegraphs.
- **Crocolisks.** Ambush predators, so mostly submerged and invisible, breaching when something approaches the bank. Currently they stand fully visible in shallow water, which undersells the "stay out of the rivers" reputation the Wetlands and Redridge quest text establishes.
- **Spiders.** Web-anchored rather than roaming. A spider sitting in a web strung between two trees, emerging to strike what gets caught, is a behavior model nothing else in the game uses.
- **Turtles.** Retreat into the shell or flee toward water instead of fighting. Passive creatures should have a passive identity rather than being aggressive creatures with lower numbers.
- **Devilsaurs.** Apex predators holding a defended territory. A devilsaur driving off a diretiger that wanders too close is a fight players stumble onto rather than start. Young sticking near an adult reads as a family unit rather than a same-tier spawn cluster.
- **Elementals.** Not real-world creatures, but the same principle applies. Fire elementals in the Searing Gorge or the Charred Vale being more active under some environmental conditions and dormant under others is a first step toward creatures that respond to their surroundings rather than being permanently switched on.

### 4.5 Where ecology meets the trade network

The ecosystem stops being a separate system the moment it can threaten cargo.

- **Draft animals as targets.** Hyena and lion packs going after a Barrens caravan's oxen rather than its guards produces a completely different failure mode: the cargo is lost because the team bolted, not because it was stolen.
- **Rest cycles setting departure times.** If wolf packs den during a known window, a Lakeshire-to-Darkshire cart timed to pass Big Will's camp during that window reads as drivers who know the woods. No schedule UI required.
- **Fixed-point ambush versus mobile raid.** Crocolisks at a river crossing on the Wetlands road are a hazard tied to one location. Ogres out of Grim Batol are a hazard that comes to you. A route with both feels like a road with real geography rather than one repeated encounter.
- **Territory as narrative.** If the Un'goro devilsaur's defended ground sits near the Cenarion researcher from Section 1.7, the researcher's notes should say so.

### 4.6 Creatures reacting to the dead

Death in Azeroth is inert. A corpse greys out and despawns and nothing in the world registers that it was ever there. This proposal makes corpses attractants, so the act of killing something occasionally sets off a reaction the player did not stage and mostly was not looking for.

**The delay is the whole thing.** Scavengers must never spawn onto a fresh kill. There is a real lag, on the order of thirty seconds to a couple of minutes, before anything arrives. Instant scavenging reads as a mechanic aimed at the player. A delay reads as the world noticing a body on its own schedule, which is the difference between a feature and a place that happens to be alive. The common case is that the player has already moved on and never sees it, and that is correct.

**Three inputs decide whether a corpse gets noticed and how it reads:** what died, where it died, and what is nearby to care. The same system produces mundane ecology in one place and dread in another with no change to the underlying logic.

- A beast carcass in a temperate zone is food. A wolf drifts in, or a couple of carrion birds land. Common, quiet, unremarkable, and it should stay that way. This is the ecological baseline and it is allowed to be boring.
- A humanoid corpse in an atmospheric zone is a different event. A ghoul shuffling out of the Duskwood tree line toward a body, or a worg coming in low, is horror rather than nature. Rare, weighted toward zones whose tone already supports it, and never the default reading of a death.

**Feeding behavior differs by scavenger,** the way the swallowed-remains loot in 7.4 differs by predator. The animation is the storytelling.

- **Ghouls and feral undead.** Crouch and feed in place. The Duskwood and Tirisfal cases.
- **Carrion birds.** Land and pick. Westfall's fields already establish the infestation [12].
- **Spiders.** Do not feed in place at all. They wrap the corpse and haul it back toward the web, which is the most unsettling one to catch mid-happening and the only scavenger that removes the body rather than sitting on it.
- **Oozes.** Flow over and dissolve rather than chew, consistent with the corrosion framing in 7.5.

**The ominous version is the exception, and it is dynamic.** Baseline beast scavenging stays common and quiet. The undead-and-ambush-predator version reacting to humanoid corpses is rare by default, but it responds to accumulated death in an area using the same hidden-condition engine as the Section 6 flare-ups. No counter, no announcement, nothing the player can read directly.

A stretch of road or a chokepoint where players keep dying, a bad pull, a contested graveyard, a corpse run everyone botches, silently accrues attention. Below threshold, normal quiet scavenging. Past it, the place starts to feel wrong: more carrion birds circling than the zone should carry, a ghoul that wandered in from further out than its normal range. In fiction, the feeding has been good there lately, and the scavengers have thickened to match.

**Attention decays.** If the dying stops, it bleeds off and the area goes quiet again. This is what keeps it from becoming a farm or a campable spawn. A player cannot manufacture it without a lot of other players actually dying in the same place, which is the same sustained-coordination cost that makes the vendor manipulation in 9.3 unprofitable. It is tied to what has been happening, not to a timer.

The payoff is that it becomes a readable signal without a line of text. A veteran rides down a road, notices the birds are heavier than they should be, and understands that people have been dying here. That is the world telling the player something true about itself, which is the entire thesis of this document expressed as circling crows.

**Tuning philosophy matches 7.6.** The goal is not that players can trigger the eerie version. It is that the overwhelming majority who ever witness it were not trying to, and could not reliably do it again if they wanted to.

This is Tier 2. The baseline scavenging is close to Tier 1 behavior work, but the accumulation trigger, its decay, and the density response are new logic in the same family as the flare-up conditions, and they should be built alongside them rather than separately.

The Kodo Graveyard in Desolace is the one place this system should not accumulate. It is a canonical location where kodo go to die, so scavenger presence there should be permanent and heavy from the start rather than building on the attention mechanic, which assumes deaths are unusual and here they are the entire premise.

The consequence is stranger than it sounds. Desolace does not turn, does not green, and is still being drained by Theradras beneath Maraudon, and yet one place inside it is unmistakably alive with the business of death. That should make the zone read as more wrong rather than less. An arrested zone with one functioning system in it is more unsettling than an empty one.

### 4.7 Corruption as a visible process

The world contains matched pairs of the same species on either side of a line, and in at least two cases the transformation is still happening rather than finished. The Timbermaw are the last uncorrupted furbolg tribe; the Deadwood in Felwood were taken by fel and the Winterfall in Winterspring by the demon Xandivious. The vanilla quest chain around Falling to Corruption has the player finding a flask and a cauldron and tracking evidence of dealings between the two tribes, with Winterfall runners moving through Timbermaw territory [34][35]. Silverpine's Rot Hide gnolls are the same shape: Thule Ravenclaw is making them, currently, on Fenris Isle.

Right now this is carried entirely by faction tags. It could be carried by the models. Show fel progression that varies by individual, with the least affected at the edges of Deadwood territory and the worst near the cauldron, so the gradient is a thing a player reads off the ground rather than off a nameplate. Put the runners on the route the quest text already describes, actually running it, so transmission is something you can watch.

The geography is a gift on top of that. Timbermaw Hold is the tunnel junction of Felwood, Winterspring, and Moonglade, which under 10.2 are an arrested zone, a muted zone, and the only zone in the world held permanently into life. The last uncorrupted furbolgs live at the meeting point of the three most extreme seasonal states in the world, and every player passing to Winterspring walks through it. That is not something to explain.

Tier 1 for the visual gradient, Tier 2 for runners and progression.

### 4.8 Behavior that answers the weather

4.2 puts creatures on a daily clock and Section 10 puts zones on a yearly one. Weather is the third clock, it already exists in the client as a purely cosmetic system, and it is the cheapest of the three to hang behavior on because it needs no new state at all.

The proposals are small and each one is a single conditional on an existing spawn or movement rule:

- Murlocs along the Elwynn and Westfall waterways range further and move faster in rain, so a shoreline that was safe on a clear day is not.
- Goats and other prey in Loch Modan shelter under overhangs and treelines when it rains, which is the daily-cycle denning from 4.2 triggered by weather instead of by hour.
- Harpies in Durotar and Stonetalon ground themselves in a dust storm, ranging less but hitting harder with wind-based attacks when they do engage.
- Lashers and other plant creatures appear in the Wetlands during and shortly after heavy rain, and are simply absent otherwise.

The last one is the template for everything in this area, because it is purely additive. Nothing is taken away on a clear day. Something is present on a wet one.

Tier 1 for movement and shelter changes, Tier 2 for weather-conditional spawns.

---

## 5. The Middle Tier: Gnolls, Murlocs, Kobolds, Harpies, Quilboar

There is a behavioral gap between beasts and civilized factions that vanilla never dramatizes. These creatures have camps, hierarchy, tools, and territory, but they are not the Defias or the Scarlet Crusade. They should read as neither.

**Gnolls.** The Riverpaw pack in Elwynn, Westfall, and Redridge, and the Mosshide gnolls in the Wetlands. Their design basis is clearly hyena social structure, so show a crude hierarchy: a larger named model eating first or holding the better sleeping spot, smaller ones squabbling over what is left. Unlike wolves, gnolls should visibly use tools and hold loot. Stolen goods piled in a camp rather than existing only in a drop table, given that the Riverpaw are canonically raiding Westfall farms alongside the Defias [12].

**Murlocs.** The best "just above animal" case in the game, because their identity is a screeching alarm network rather than individuals. Keep the swarm alert as the defining mechanic. Add non-combat behavior around it: spear fishing at tide pools, shiny objects hoarded near huts, which finally explains why their loot tables are full of unexplained trinkets.

**Kobolds.** Already partial comic relief in vanilla, and worth leaning into. They should be visibly the weakest of this tier: skittish, and prone to breaking as a group when their strongest member dies rather than fighting to the last. Note that Westfall's Jangolode Mine kobolds are described as having connections to the Defias [12], which makes them a good candidate for showing a subordinate relationship between two hostile groups.

**Harpies.** Airborne and nest-based rather than ground-camp based. The Stonetalon Mountains are their traditional homeland [9], they hold perches atop the mesas of the northern Barrens [11], and the Roguefeather harpies are a standing nuisance in Thousand Needles [15]. They should perch on cliff edges and dead trees and dive at what passes below, with nests tucked into cliffside terrain holding eggs and stolen shinies.

**Quilboar.** Razormane and Bristleback in the Barrens, with the Razorfen complexes as their center of gravity. The lore here is stronger than any other race in this tier and it points somewhere specific. Agamaggan was an Ancient Guardian killed during the War of the Ancients, and where his blood fell, thorn-ridden vines rose from the ground; the largest cluster became the Razorfen, which the quilboar revere as his resting place and are held to descend from [27][28]. This is in the vanilla client rather than supplementary material, as the Razorfen Kraul dungeon description and the Spirit of Agamaggan inside it.

Note it is his blood and not his quills, which changes the image. The Razorfen is not a carcass the quilboar live inside. It is what the soil did afterward.

That reframes the race. Quilboar do not build, they tend. A quilboar camp should read as horticulture rather than construction: thorn walls grown and trained rather than assembled, quilboar working the vines the way the Venture Company works timber in 1.3, and no cut ends anywhere in the structure. Whatever the largest thorn mass in a camp is, that is what they are maintaining, and everything else radiates out from it.

It also hands Section 4 something it otherwise lacks, a plant that behaves like a creature. Razorfen thorns with their own slow growth response, thickening where quilboar tend them and receding where they have been driven off, are the clearest possible readout of who currently holds a piece of ground, with no text at all. Quilboar defend ground. Gnolls raid it. That distinction should be legible without reading a single quest. Tier 1 for camp art and animation, Tier 2 for responsive thorn growth.

---

## 6. Emergent Conflict

### 6.1 The design requirement

The thing that ruins an event is a visible timer. If players can schedule around it, it stops being the world's business and becomes content queued up for them.

The proposal is that flare-ups are driven by conditions the player cannot see and cannot directly read, accumulating quietly in the background. No counter, no bar, no announcement. Most of the time nothing happens. Occasionally something does, and there is a good chance you are not close enough to participate.

### 6.2 Riverpaw gnolls raiding Defias holdings, Westfall

Westfall is the strongest candidate because both factions are already there and already hostile. The Defias hold Moonbrook, the Gold Coast Quarry, the Dead Acre, the Dagger Hills, and Klaven's Tower; the Riverpaw hold camps in the southern plains; and Captain Danuvin at Sentinel Hill is specifically working the gnoll problem alongside Gryan Stoutmantle's Defias problem [12].

The trigger should be invisible and indirect. Something like tracking recent Defias deaths in an area as a proxy for "the gang looks weak right now." Past a threshold, a one-time raid spawns: gnolls assaulting a Defias camp, both sides fighting each other rather than the player.

If you are nearby, you see it. If you are not, you arrive later to find gnoll and Defias corpses tangled together and have to work out what happened. The second outcome is arguably the better one, and it will be the common one.

### 6.3 Murloc surges, heard before seen

On a coastal road, murloc screeching audible from over a ridge well before anything is visible. Most of the time it fades and nothing comes of it; the camp was reacting to something else. Rarely it escalates into a surge toward the road, which a player may watch from a distance without ever being close enough to intervene, cart included.

### 6.4 Territorial flare-ups on the Barrens and Thousand Needles border

Quilboar and centaur territory abut each other. A dispute can start because one side's patrol drifted slightly outside its normal range, with no warning at all. A player on the Gold Road catches the tail end of a skirmish already in progress, off in the grass, with nothing to click on.

### 6.5 Harpy nests above the Stonetalon logging camp

Harpies nest on the Stonetalon cliffs. Venture Company shredders work the crag below. A falling tree or shredder noise disturbing a nest, sending harpies down onto the logging crew, is almost entirely an audio-visual event: a commotion overhead that most players glance at and keep walking past.

### 6.6 Centaur clan war in Desolace

This one deserves special attention because vanilla already built the mechanic and then hid it in a reputation grind. Desolace's centaur clans are mortal enemies by design. The player picks a side: killing Gelkis raises Magram reputation with Warug outside Magram Village, killing Magram raises Gelkis reputation with Uthek the Wise outside Gelkis Village, and each kill moves the opposing bar in the other direction [16][17][18].

The feud is fully specified and completely invisible in the world. Desolace is a desert. Staging periodic Kolkar, Magram, and Gelkis war parties clashing over a contested water source dramatizes an existing system using an existing motive, and it does it without a single line of new lore.

### 6.7 Flare-ups and quest integrity

A flare-up that eats a quest objective is a bug wearing a feature's clothes, and it is the most likely way this section ships broken. Four rules contain it.

**Named NPCs are never casualties.** Quest givers, quest objectives, and rare spawns are excluded from flare-up losses outright. The Riverpaw can overrun a Defias camp without Klaven Mortwake dying inside it.

**Casualties come from generic spawns only**, capped as a fraction of the camp rather than as a flat number. A thinly populated camp should not get erased because the same subtraction was written for a dense one.

**Respawn accelerates rather than pauses.** A camp cleared by a flare-up refills faster than one cleared by players, not slower. The event is allowed to change what a camp looks like for twenty minutes. It is not allowed to make the zone emptier for an hour, because the player who arrives afterward did not opt into the event and should not pay for it.

**A flare-up cannot fire on a camp with players in combat inside it.** This blocks three failure modes at once: the event stealing kills, a second hostile faction landing on someone mid-pull, and the case where a player's own farming triggers the condition that then interrupts the farming.

That last rule is load-bearing for the trigger design in 6.2. If recent Defias deaths are the hidden condition, the player generating that condition is by definition standing right there, so the event has to wait for them to leave. Which is also the better outcome narratively. They walk away, come back an hour later, and find the aftermath.

### 6.8 Blackrock Mountain, and reading a war from outside it

Section 6 so far proposes small flare-ups. The world already contains one conflict big enough to anchor the system, and the game was largely built around it.

Blackrock Mountain is a volcano created when Dagran Thaurissan accidentally summoned Ragnaros, and the blast shattered a section of the Redridge Mountains into what are now the Searing Gorge and the Burning Steppes. Inside, Ragnaros and the enslaved Dark Iron hold the lower reaches while Nefarian and the Dark Horde under Rend Blackhand hold the upper, and the two sides are in open war with each other [29][30].

That first detail matters for Section 10 as well. Those two zones are not arrested zones that happen to sit near a volcano. They are its blast radius. Their existence and their stillness have the same cause, which is what puts them in the active-arrest category in 10.2.

The proposal is to run the 6.1 engine on a much longer clock with a single hidden state: who currently holds more of the mountain. The surface is the only readout. Dark Iron patrols pushing further out of the Gorge in one state, Blackrock orc and dragonspawn activity thickening on the Steppes side in another, with the density and the reach of each shifting over weeks rather than hours.

The restraints from 6.1 apply with more force here, not less. No visible timer, no announcement, no dependency on raid progress. A player who works both zones over months should learn to read the surface as a symptom of something underground that they never see directly. This is weather, not a world event. Tier 2.

### 6.9 Three kinds of world state, and which one to use

Everything in this section, and in Sections 4 and 10, depends on an architectural question that should be answered explicitly rather than assumed: when the world changes, who sees it, and does it change back?

There are three available answers and only two of them belong in this game.

**Cyclical state. The default, at every level, everywhere.** The zone has two or more states and moves between them on hidden conditions, then moves back. Seasons work this way. Flare-ups work this way. Scavenger attention in 4.6 works this way, and the decay rule there exists specifically to keep it cyclical.

Cyclical state is the answer to the hardest objection against a living world, which is that a game with a continuous supply of new players cannot ratchet. Anything permanent is a door that closes behind the people who were there. A cycle closes no doors. A player who arrives in Westfall during a heavy Defias occupation and a player who arrives after Stormwind has pushed them back are both seeing a real Westfall, both have full content, and neither has missed anything, because it will come around again.

It also produces a kind of knowledge no static world can. A veteran who says the Defias are worse than they were is describing something true and checkable, and that is only possible if the statement can be false at other times.

**One-way additive events. Rare, server-wide, and permitted only when nothing is removed.** The gates of Ahn'Qiraj are vanilla's proof that a realm can change permanently and it can be one of the best things that ever happens on it.

The useful lesson from AQ is not that permanent change is for max level. It is that permanent change must be **additive**. AQ opened access to content that did not previously exist and removed nothing; no leveling path broke, no quest became uncompletable, and a player who rolled a character the following year lost nothing by having missed the event itself.

That reframes the level question entirely. The Lakeshire bridge in Redridge is unfinished in vanilla and never gets finished, which is an unpaid promise sitting in the game. Completing it as a one-time server-wide event would be safe at any level, because a finished bridge takes nothing away. A player who arrives afterward sees a bridge, which is fine. Worlds are allowed to have history that happened before you got there.

The inverse fails for the same reason. Driving the Defias out of Westfall permanently would remove the zone's content for everyone who comes later, and no amount of narrative payoff is worth that.

So the rule is: **additive changes may be permanent, subtractive changes must be cyclical.**

**Phasing. Almost never.** Phasing gives each player a private copy of world state, and it is the specific technology that made the modern game's world feel lonely. Two players stand in the same place and see different places. They cannot group on it, cannot point at it, and cannot tell each other where to go.

Everything in this document depends on the opposite property. A flare-up matters because the person you tell about it can go and see it. A heavier ring of carrion birds is a signal only if it is the same signal for everybody. Shared reference is most of what the word world is doing in the phrase living world.

The narrow exception is scale. Phasing a single room, a cave, or a quest interior breaks nothing and nobody notices. The line to hold: **never phase anything two players might reasonably need to stand in together.** No hubs, no roads, no zones.

### 6.10 Player action with server-wide effect

There is a real appetite behind the phasing idea that the three-state model above does not by itself satisfy: the wish to have done something and see the world respond.

Vanilla already solved this and the solution is sitting in Onyxia's Lair. A guild kills Onyxia, someone carries the head to a capital, the whole realm gets an announcement and a buff, and it wears off. Player action, server-wide visible effect, temporary, repeatable.

That pattern generalizes to almost every idea phasing is usually reached for. Clearing Stonewatch Keep in Redridge could shift the zone toward a garrisoned state for a period, visible to everyone, decaying afterward. World PvP in Ashenvale could build or burn faction camps, with the state persisting for the realm rather than the participant. In each case the player who acted gets the satisfaction of having changed something, and everyone else gets to see it, which is strictly better than a private phase where the accomplishment is invisible to the only people whose opinion of it matters.

The constraint from 6.7 carries over unchanged. Named NPCs survive, quest givers persist, and no state may make a quest uncompletable.

### 6.11 Threats that appear later

A smaller idea worth separating out, because it is cheap and does not need any of the above.

Some things should exist in a zone only for players who have outgrown it. A Defias assassin working the roads around Goldshire, or a kobold who has taken over as something like a candle-king in the Jangolode Mine. These are absent at the levels the zone is built for, because they would wreck the questing, and present for anyone who comes back later.

Mechanically this is a conditional spawn rather than a state system, which puts it far below anything else in this section in cost. What it buys is that a zone a player thinks they have finished has something in it they have never seen, and that a level sixty passing through Elwynn has a reason to look around rather than ride through.

It also pairs with 8.11's guard hints and 7.6's tuning philosophy, since the right way to hear about the assassin is from another player or a guard rather than from a spawn timer.

---

## 7. Loot Logic

### 7.1 The problem

A timber wolf in Ashenvale drops silver coins. Nothing in the fiction explains this, and it breaks immersion at a rate of several times per minute during leveling.

### 7.2 Coin by creature type

**Beasts: no coin, ever.** Wolves, bears, boars, cats, raptors drop pelts, fangs, claws, and meat. The lost value gets pushed into slightly better vendor prices on those materials rather than disappearing.

**Bandit humanoids: the primary gold source.** The Defias, the Syndicate in Hillsbrad and Alterac, the Bloodsail, the Southsea pirates around Lost Rigger Cove in Tanaris [8]. These are written as organized criminal enterprises, so they should be where money physically is. Faction-flavored junk reinforces identity: lockpicks and stolen deeds on Defias, pilfered goblin hardware on Bloodsail.

**Military humanoids: coin plus rank-scaled equipment.** A Scarlet Crusade footman drops a common blade; a centurion drops officer-tier gear and more coin. This gives players a reason to target higher-rank mobs rather than farming whichever variant is easiest.

**Cultists: reagents, minimal coin.** Twilight's Hammer in Silithus, Burning Blade in Durotar and Blackrock. Fanatics, not looters. Ritual components, robes, corrupted trinkets.

**Constructs, elementals, ghosts: no coin, no conventional gear.** Elementals drop elemental materials only. Ghosts drop nothing physical beyond an occasional memento tied to their own backstory, which Duskwood and Tirisfal already have the narrative infrastructure for.

### 7.3 Coin by zone

Creature-type logic is not sufficient on its own. Zones should have economic character.

**Westfall.** The entire zone premise is agricultural collapse and banditry. Non-Defias drops should be poor across the board, reinforcing a depressed region rather than a farming ground.

**Un'goro Crater.** Prehistoric wildlife isolated from civilization. No coin at any level, no exceptions. Hide, meat, and crater-specific reagents only. Nothing in Un'goro's fiction explains a raptor carrying money.

**Stranglethorn and Booty Bay.** The deliberate contrast zone. Goblins and pirates are literally about commerce and plunder, so coin should be conspicuously plentiful here, to make Westfall and Un'goro read as intentional rather than stingy.

### 7.4 Swallowed remains

The exception that makes the rule work.

A very low chance, rarer than a standard rare drop, for a predator to yield an item framed as something it ate rather than something it owned. Bent and tooth-marked. Partly digested. The flavor text does the storytelling and no quest is attached.

Examples anchored to specific fiction:
- A Duskwood wolf yielding a gnawed silver coin or a tarnished ring, implying someone did not make it to Darkshire
- A devilsaur yielding scorched research notes, implying a Cenarion researcher's satchel went down with its owner
- A Thousand Needles predator yielding Bloodhoof-marked jewelry, which quietly implicates the Grimtotem at Darkcloud Pinnacle, who are already suspected of murdering and abducting Freewind Post tauren [15]

### 7.5 The same idea across other creature types

The mechanic generalizes, but the flavor should differ by how the creature actually feeds.

- **Oozes.** Corrosion, not gnawing. A half-dissolved dwarven pick near Dun Modr. A pitted Dark Iron insignia near Blackrock. Etched and eaten away rather than chewed.
- **Carrion birds.** Collectors, not diners. Westfall's fields are already described as infested with carrion birds [12]. A bird carries something because it glinted: a bauble, a torn scrap of a supply manifest that connects to a caravan route.
- **Crocolisks.** Targeted ambush, not scavenging. Soggy, algae-covered items. A fisherman's ring. Something with a quartermaster's mark on it.
- **Spiders.** Storage, not digestion. A silk-wrapped bundle still attached to the corpse, containing something small.

### 7.6 Tuning philosophy

These should not be findable on purpose in any efficient way. If a player wants to grind for one, that is allowed and it should be a bad idea. The design target is that the overwhelming majority of players who ever see one were not looking.

### 7.7 Anatomy that reads from the outside

7.4 and 7.5 are about what a creature has eaten. This is about what a creature is, and it is the same argument pointed inward.

Vanilla's materials divide into legible and illegible, and the split has gone unremarked because the legible ones are the vast majority. Herbs are legible: you see the plant, you pick the plant, you get the plant. Ore is legible. Leather is legible because everything has skin. Cloth is legible because humanoids wear clothes. In each case the source is visible from outside the creature or the node.

Venom sacs are not, and neither are flame sacs, ichor, glands, or hearts. These are internal anatomy, and nothing about the outside of a creature tells you whether it has one. The Small Venom Sac is the clearest case: it drops from scattered spiders across Tirisfal, Silverpine, Stonetalon, Redridge, Loch Modan, and Durotar, with no stated reason why those spiders and not others [36]. The item is the only evidence that the anatomy exists at all.

So the fix is not primarily flavor text. It is making the outside of the creature honest about the inside.

**The behavioral tell.** The strongest version costs almost nothing, because the information is already in the combat log. If a creature envenoms you, it has a venom sac. If it does not, it does not. Tighten that correlation until it holds without exception and every poison debuff a player has ever taken becomes a drop-table lesson they learned without being taught. The same rule extends to flame sacs and anything that breathes fire. This is the shape argued for in 7.6 and again in 8.12: knowledge a player accumulates by paying attention rather than by looking up.

**The constraint that governs all of it.** The instinct with an undifferentiated reagent is to differentiate it, splitting venom into spider, scorpid, and serpent variants with distinct properties. Do not. Bag space is the real currency of the vanilla leveling experience, sixteen slots for most of sixty levels, and every new material item is a tax on it. Fragmenting one reagent into five spends the player's scarcest resource to buy texture, and it will be resented rather than enjoyed.

The rule to write down: **add texture to materials without adding item slots.** Naming, flavor, visual tells, behavioral tells, and source logic are all free. New item IDs are expensive.

**The game already did this once by accident.** Scorpids in Tanaris, the Blasted Lands, and the Burning Steppes drop an Empty Venom Sac [37]. That name tells a story: the thing spent its venom, and it spent it on you. Nobody followed through on it. Every item in this family could carry that much implication for the cost of a string.

**One voice for the whole set.** If these items get flavor text it should read as a single naturalist's field notes distributed across dozens of anatomy items, so that reading tooltips becomes reading one person's work rather than forty disconnected jokes. This is text only, which makes it the cheapest proposal in the document.

And the author already exists. 1.7 puts a Cenarion Circle researcher alone on the Un'goro plateaus, and 7.4 has a devilsaur yielding their scorched satchel. Make them the person who wrote the anatomy notes and they have a body of work sitting in every player's bags before anyone ever finds them, and a reason the notes stop at the point where their fieldwork did. Tier 1 throughout, except the behavioral tell audit, which is Tier 2 because it touches spell tables.

---

## 8. Professions

### 8.1 Jewelcrafting without sockets

Jewelcrafting is the most-discussed profession addition, and it shows up in the leaked feature lists as a mining-paired profession producing jewelry and trinkets rather than gems [19]. That framing is correct for vanilla, and the reason is mechanical: gem sockets do not exist in Classic. They arrived with The Burning Crusade.

So jewelcrafting has to be a finished-goods profession. Rings, necklaces, and trinkets crafted whole, with fixed stats, competing directly against dungeon and quest reward jewelry rather than augmenting existing gear. This is not a downgrade. Classic's rings and necks are already stat sticks with nothing to slot into, and a full vanilla-era recipe progression along these lines already exists in later-added content as a reference point: copper wire and simple settings at the bottom, worked bands and pendants through the middle, high-tier stones at the top [20].

**Material sourcing tied to exploration.** Pair it to mining as expected, but differentiate it by having raw gems appear disproportionately in rare or hard-to-reach veins. This connects the profession to Section 1.7: a truesilver deposit tucked onto an awkward ledge occasionally yielding a cuttable stone makes jewelcrafting materials feel earned rather than farmed.

### 8.2 Inscription without glyphs

Retail inscription is built around glyphs modifying spells, which presupposes a talent and spell system far more granular than vanilla's. Transplanting it directly would be the wrong shape.

A vanilla-appropriate scribe produces consumables and equipment instead: scrolls granting temporary stat buffs in the same family as alchemy's flasks, and the physical books and codices that casters use as offhands. That keeps it additive and keeps it away from the talent system entirely.

### 8.3 Woodcutting

Retail's lumber gathering is resource-management heavy. A vanilla version should be simpler and should serve the rest of this document.

A woodcutting gathering skill harvesting from forest zones like Ashenvale and Stonetalon, feeding recipes for wagon components, bows, hafts, and furnishing-style goods. This does three things at once: it gives lumber an economic identity instead of leaving it as Venture Company backstory, it supplies the cart network with a crafted input, and it creates direct competitive friction with the Venture Company operation in Windshear Crag, since players and goblins would be stripping the same forests.

### 8.4 Regional cooking

Cooking exists in vanilla but is thin and universal. Tying recipes to geography gives it identity: a Booty Bay dish requiring goblin spices sold only there, a Mulgore dish built on plains game. This also gives the trade network something to carry.

### 8.5 Trapping

A secondary skill open to all classes, placing snares near dens and along the movement paths established in Section 4. It yields small-creature materials that feed leatherworking and tailoring: specific pelts, feathers, and the like.

The value here is that it is the only proposal in this document that interacts with the wildlife systems without killing anything. Everything else in Sections 4 through 7 is kill-and-loot.

### 8.6 Relic hunting

A stripped-down archaeology precursor. Disturbed-earth dig spots, mostly yielding lore fragments and cosmetic trinkets. Explicitly no power progression, so it never competes with the real profession economy, and it exists mainly to give the hidden content in Section 1.7 something to connect to.

### 8.7 Cross-tier materials: keeping low-level goods valuable

This addresses one of vanilla's real structural weaknesses. Peacebloom becomes economically worthless the moment a player outlevels Elwynn, even though it keeps growing there forever, and the same is true of copper, linen, and every other entry-tier material.

Three approaches, usable together:

**Blended recipes.** A high-end recipe requires a small quantity of a rare current-tier material plus a bulk quantity of an early-game one. This mirrors how real formulation works, where expensive components are cut with cheap bases rather than used at full purity.

**Dual crafting paths.** The same output available two ways: fast and expensive using only current-tier materials, or slower and cheaper substituting a larger volume of low-level materials. A level 60 alchemist going back to farm silverleaf because it is the cost-effective route, not because a quest sent them, is the goal state.

**Extension beyond alchemy.** Blacksmithing folding copper or tin into a high-tier weapon as a tempering component. Tailoring requiring linen or wool as a lining under runecloth or mageweave. Real construction is layered, not monolithic, and the crafting system can say so.

### 8.8 Cross-profession dependencies

Vanilla professions are mostly self-contained gathering-and-crafting pairs. Herbalism feeds alchemy. Mining feeds blacksmithing. Very little moves sideways.

**Fishing into alchemy.** Currently fishing feeds cooking and almost nothing else. Specific fish, catchable only in particular bodies of water, should be legitimate alchemy reagents. This turns Loch Modan's lake or a Wetlands pool into a destination for alchemists rather than only for anglers, and it is well-precedented by real-world folk pharmacology.

**Jewelcrafting into enchanting.** Crushed low-tier gems as a dust component gives two crafting professions a direct reason to trade with each other.

### 8.9 Vendor trade goods should be craftable

Right now a set of universally required materials are bought from NPC vendors and produced by no player: coarse thread, weak flux, empty vials. Every one of those transactions is a dead gold sink that bypasses the player economy entirely.

- **Coarse thread** from linen scraps via a first-tier tailoring recipe, which makes low-level tailors producers of something every other profession consumes
- **Weak flux** from low-grade processed stone, giving miners a reason to sell to blacksmiths beyond raw ore
- **Empty vials** through a simple glassblowing-adjacent recipe using sand or silica, most naturally folded into mining

Vials are the clearest case. Alchemists buy a vial for every potion they make, forever, from a vendor. Notably, vanilla already treats crystal vials as a tradeable commodity of some standing: the Ratchet reputation turn-in is built on linen cloth and crystal vials, exactly as the Booty Bay turn-in is built on silk and dye [21]. The game already knows these are goods. It just does not let players make them.

These should remain purchasable. The point is not to force crafting, it is to stop the vendor from being the only source.

### 8.10 Wandering profession trainers

Vanilla already establishes that the trainers worth finding are not in cities. Every leatherworking specialization master sits in a wilderness camp: Peter Galen above the Ruins of Eldarath in Azshara, Sarah Tanner at the Tanner Camp in Searing Gorge, Caryssia Moonhunter at Thalanaar, Thorkaf Dragoneye in the Badlands, Brumn Winterhoof north of Stromgarde Keep, Se'Jib south of Grom'gol [22]. The pattern is already in the game. It is just nailed to the ground.

The proposal is a small number of trainers who travel instead of holding a post, teaching regional recipes no city trainer offers. They path the routes from Section 2, sit at a settlement for a day or two, and move on. Their recipes should not be stronger than city recipes. They should be different, and they should smell like where they came from: a Thelsamar smoking recipe, a Booty Bay cure that uses goblin spices, something out of Feralas that a Stormwind trainer would never have heard of.

This is as much a Section 1 proposal as a Section 8 one, because a wandering trainer is a traveler first and a trainer second. She makes camp, eats, packs, leaves. A player who happens to be in Thelsamar the week she is there gets something. A player who was there last week does not, and finds out from a guard that he missed her.

Tier 1. Everything it needs already exists: NPC pathing, gossip, trainer flags. It is a scheduling problem, not an engineering one.

### 8.11 Finding them, and the honest problem with hidden content

Vanilla city guards already answer questions. Asking a Stormwind guard where the auction house is flags it on the minimap, and players already use this. Extend the same system rather than building a new one: guards, innkeepers, and flight masters can be asked about a wandering trainer and answer with a region and a staleness, never a coordinate. She came through here about a week back, said she was headed up toward Thelsamar. No marker, no arrow, and the information is allowed to be out of date.

The honest problem is that constraint 3 of this document asks for content rare enough that deliberate farming is inefficient, and a wandering trainer on a fixed route fails that test inside a week. It gets datamined, the circuit gets posted, and the guard system becomes decoration on top of a wiki page.

The fix is that the route is not fixed. The trainer picks each next stop from a small weighted set rather than running a loop, so the community can learn her territory without being able to predict tomorrow. That is the correct target anyway. The goal was never that players cannot find her. It is that finding her is a thing you do in the world, using the world, rather than in a browser tab.

Tier 2, and it lands there for one reason: the guard gossip has to read a live NPC position, degrade it into a region, and attach an age to it. That is new logic. Everything else in the pair is existing systems pointed somewhere new.

### 8.12 Kobolds and ore

Vanilla never states this and the client demonstrates it everywhere: kobold camps and mineral veins occupy the same ground, from Elwynn to the Badlands.

Make the correlation causal rather than incidental and mining gains a reading skill for free. Kobold density predicts vein density. No tooltip says so, no quest explains it, and miners simply learn it, with the ones who learn it earlier doing better. That is the shape 7.6 argues for: knowledge that rewards attention rather than lookup, and that a player can be taught by another player rather than by a website.

It gives 8.11's guard hint system something concrete to point at, and it gives Section 6 a consequence with teeth. Clear a kobold warren and the veins in that pocket are easier to work for a while, until the kobolds come back, which they should. Tier 2.

### 8.13 Anti-Venom, and the counter found on the threat

First Aid past bandages is close to dead content in vanilla, and Anti-Venom is the reason to look at why. The problem is not the craft. It is that you do not know you need it until you are already poisoned, at which point you are not at a trainer and not at a bank.

But the reagent drops off the thing that poisons you. The counter is found on the threat. That loop is already sitting in the game and has never once been signposted.

Closing it takes two changes and no new items. Make poison actually bite in the zones where venomous creatures are dense, enough that a player notices the debuff as a problem rather than as chip damage. Then hold the 7.7 rule that anything which envenoms you carries a sac. A player who dies to spider poison in Loch Modan and then loots a venom sac off the spider has been handed the entire lesson in one death, without a quest, and First Aid acquires a purpose past the leveling grind.

There is a distribution problem to fix alongside it, and it is an old complaint rather than a theoretical one: the reliable Small Venom Sac sources skew heavily toward Alliance-accessible zones, which has sent Horde players on long detours for a basic First Aid reagent since vanilla [36]. Applying the 7.7 tell honestly fixes this by itself, because venomous creatures are distributed across both factions' leveling paths even though the current drop assignments are not.

This is also the cleanest test case for 8.9, since Anti-Venom is exactly the kind of consumable that should be craftable rather than only purchasable. Tier 1 for the drop-table and tuning work.

---

## 9. Economy: Vendors as Supply Nodes

### 9.1 The proposal

Selling to an NPC vendor stocks that vendor's inventory rather than deleting the item and conjuring gold from nowhere. Vendor shelves reflect what has actually been sold locally, and they can run dry.

### 9.2 What this produces

**Regional shortages that are real.** If nobody has been supplying flux in Ironforge, Ironforge runs low on flux. A player who notices can import from somewhere with surplus. This is emergent commerce created by nothing more than a stock counter.

**A reason for the trade network to be load-bearing.** Section 2 and Section 3 become economically necessary rather than decorative the moment goods have to physically move to rebalance supply. This is the single strongest argument for building the cart network at all.

**A functioning floor under the player economy.** The auction house stays where it belongs, handling finished and rare goods where price discovery matters: jewelry, weapons, enchants, consumables. Raw and semi-processed materials route through vendors, so a new or crafting-focused player has a baseline supply even on a server with a thin auction house.

### 9.3 The obvious failure mode

A large guild or a gold farmer floods one vendor to crash local prices, or starves one to manufacture a shortage they profit from.

The mitigation is a soft cap: a vendor pays well for the first N of an item per day, then its buy price drops sharply. That makes mass dumping unprofitable without penalizing a normal player offloading crafting byproducts. It also means the manipulation strategy requires sustained coordination rather than one afternoon, which raises the cost above the likely reward.

This should be tuned per item category, not globally. Raw ore and a finished weapon do not have the same abuse profile.

### 9.4 Where the stock actually comes from

Section 3 moves goods and Section 9 holds them, and until now this document has implied the connection without stating it. State it plainly: a wagon that completes its route credits stock to the destination's vendor pool. A wagon that does not arrive does not.

That single sentence is the payoff for building the cart network at all, and it makes three things true at once.

**Robbery acquires a world consequence.** An intercepted Ironforge shipment means Ironforge is short on flux the following week. Nothing announces it. It is simply true, and it is noticeable to whoever went to buy flux. This is the first mechanic in the document where one player's action changes what a different player finds on a shelf, without either of them knowing about the other.

**The manipulation problem in 9.3 partly solves itself.** That failure mode assumes players are the only source of supply. They are not. NPC traffic sets a floor that a guild cannot starve without also interdicting the route, and interdiction is a sustained, visible, contested operation rather than one afternoon of dumping items at a counter. The soft cap handles the flooding case. Route traffic handles the starving case.

**Regional character stops being arbitrary.** A vendor's stock becomes downstream of what its region produces and what physically reached it, so Booty Bay carrying goblin goods and Thelsamar carrying dwarven ones reads as a consequence rather than as a table somebody wrote.

The number this opens up is the ratio of NPC-supplied to player-supplied stock, and it is the most important tuning value in Section 9. Weighted too far toward NPC supply and selling to vendors stops mattering. Too far toward players and a low-population realm has empty shelves and no way to fix them. It should be tunable per realm rather than fixed globally, because a dead realm and a full one need different answers.

### 9.5 Interdiction, and the one the lore already ran

The systems in 9.4 imply their own inverse. If completed deliveries credit vendor stock, then stock can be starved by stopping deliveries, and the world has already done this once.

From the shadows, Onyxia continued using her position as Lady Prestor to cut off supplies and support to Westfall, deliberately, to keep the Defias enraged [31][33]. Westfall's poverty is canonically a supply interdiction plot, which means Sections 2, 3, and 9 have a ready-made use case sitting in the game's own backstory.

What the player sees: wagons that should reach Sentinel Hill and do not, and a Sentinel Hill vendor whose stock stays thinner than any comparable settlement's for reasons observable on the road rather than stated in quest text. The Stormwind half of the story is in 1.8.

This is also the honest answer to a question 9.3 raises. If players can manipulate supply, so can the world, and a zone that is being starved on purpose is more interesting than a zone that is simply poor. Tier 1 for the dressing, Tier 3 for the supply consequence, since it depends on 9.4 existing.

---

## 10. Seasons

Azeroth's zones have fixed weather. Elwynn is always late spring, Winterspring is always deep winter, Tanaris is always noon in a desert. The world has climate but no calendar, which means it has no sense of time passing at any scale larger than a day.

### 10.1 The core proposal

The world runs a year. Not a cosmetic reskin on a timer, an actual clock that flora, fauna, quest requirements, and vendor stock all read from.

The instinct is two hemispheres flipping the way Earth's do. Azeroth's map does not support that cleanly, and forcing it would mean bending geography to fit the system. What the map does support is latitude, because the warm band sits in the south on both continents. Stranglethorn Vale and the Blasted Lands are at the bottom of the Eastern Kingdoms; Un'goro Crater, Tanaris, and Silithus are at the bottom of Kalimdor. The cold sits north on both: Tirisfal Glades and the Alterac range on one, Winterspring, Felwood, Darkshore, and Teldrassil on the other.

So the model is a growing season that marches by latitude rather than two halves swapping. In the northern summer the productive band pushes all the way up into Tirisfal and Silverpine. In the northern winter it retreats south toward the tropics, which barely slow down because they are jungle year-round.

One correction to that, found while working Kalimdor zone by zone in 10.2. Latitude gives temperature and it does not give moisture. The rule predicts that the bottom of both continents is warm, which is correct, and it predicts that the bottom of both continents is productive, which is wrong: Tanaris and Silithus sit at the same latitude as Un'goro and they are desert. So the model is latitude for temperature plus a per-zone moisture value, and the moisture value is what decides whether a warm zone is jungle or sand.

That is still one rule applied everywhere rather than a pile of per-zone exceptions, which is what makes it buildable. It is just two dials instead of one.

### 10.2 How much each zone responds

The instinct is a binary: a zone either turns or it sits out. That is wrong, because nothing in the world actually sits still. Weather does not stop at a zone border and neither does the sun. A zone whose flora never changes is still lit differently in midwinter than at midsummer. And a zone held frozen by magic is being held against something, which means there has to be a something for it to be held against.

So three tiers instead of two.

**Full turn.** The zone runs the whole cycle. Foliage, ground cover, snow, herb windows, beast density, ambient audio, light. This is the temperate belt and it is where the calendar is actually felt.

**Muted pulse.** The zone's defining climate never changes, but the year still moves through it. Sun angle, day length, storm frequency and severity, ambient audio, ice and water at the margins. Dun Morogh never greens. It still breathes.

**Arrest.** No response at all. Not slowed, not muted, flat. Reserved for zones killed or held by magic.

The third tier only works because the second one exists. If every unchanging zone were flat, flatness would just be what unchanging zones look like and it would carry no meaning. Give Dun Morogh and Stranglethorn a faint pulse and the Plaguelands become the only ground in Azeroth not doing the thing that every other place does, including the frozen places and the deserts. Dead stillness reads as wrong when it is an exception rather than a category.

There is also a cost argument for the middle tier. Muted pulse is lighting, weather tables, and audio with no gameplay hooks attached, which is the Tier 1 cosmetic pass described in 10.7. It ships with the art work and needs none of the spawn or node plumbing. Arrest costs nothing at all, since it means doing nothing. Only the full turn is Tier 3.

#### Eastern Kingdoms, north to south

**Tirisfal Glades. Partial, and only downward.** Tirisfal is not blighted the way the Plaguelands are, but the ground is soured and vanilla paints it permanently autumnal. That gives the honest answer: the zone can go down but not up. Winter takes it hard, snow over the orange canopy, Brill's fields bare, Deathknell genuinely bleak. Then spring arrives everywhere else and Tirisfal returns to autumn rather than to green. A zone whose best season is October is a more specific kind of wrong than a zone that is simply dead.

**Silverpine Forest. Full turn, expressed sideways.** Silverpine is conifer, so leaf color is not the lever. Snow depth, understory, fog density, and the worgen and wolf packs around the Sepulcher are. A full turn here looks like accumulation rather than color change, which is exactly right for a pine forest and cheaper to author than a deciduous repaint.

**Western and Eastern Plaguelands. Arrest.** The Scourge killed the ground. Nothing here reads the clock, and once the rest of the world visibly does, that is the whole statement.

**Alterac Mountains. Muted, with a moving snowline.** The high ground stays white year-round. The lower valleys toward the Hillsbrad border should thaw in summer and take snow again in autumn, so the boundary between Alterac and Hillsbrad migrates up and down the slope across the year. A snowline that moves is the single cheapest way to show altitude and season interacting.

**Hillsbrad Foothills. Full turn, and the best argument for the system.** Hillsbrad is farmland. Southshore and Tarren Mill are working settlements with fields around them. Crops that are green in spring, gold in late summer, cut in autumn, and bare under snow in winter make the calendar legible without a word of explanation, and they make the contested-zone tension worse in the good way, since both sides are fighting over ground that visibly produces something.

**Arathi Highlands. Full turn.** Open grassland goes green, then gold, then brown, then white. Wide sightlines mean the season is visible from anywhere in the zone. Stromgarde's ruins read differently in each one.

**The Hinterlands. Full turn, the most dramatic in the game.** The Hinterlands are deciduous, primarily oak and maple, and lore explicitly notes it is remarkable they thrive so close to the wasted Plaguelands. That is the case handed to us: put a genuine New England autumn in the Hinterlands, and the border with the Plaguelands becomes the sharpest visual argument in the world. Living forest on one side of the line turning red and gold, dead ground on the other side doing nothing, in the same week.

**Wetlands. Full turn on the water axis.** Temperature matters less here than water level. A wet season floods the lowlands, widens the channels, and pushes the murlocs and crocolisks inland; a dry season pulls the water back and exposes ground that was under it. Menethil's dock waterline is a free gauge. This also gives 6.4's murloc surges a seasonal reason to exist rather than a purely hidden trigger.

**Dun Morogh. Muted pulse.** Alpine, snowed year-round, and it should stay that way. What moves is sun angle, day length, storm frequency, and the ice on the ponds around Kharanos thickening in deep winter and going thin and dark at the edges in high summer. Coldridge Valley in July should feel like the same place in a different month, not a different zone. This is the reference implementation of the middle tier.

**Loch Modan. Full turn, anchored to the loch.** Temperate, wooded, and built around a body of water and a dam. Ice at the loch margins in winter, full green around Thelsamar in summer, and the Stonewrought Dam as a fixed structure the changing water reads against.

**Badlands. Muted, loud.** Arid canyon with no vegetation to lose, so there is no full turn available. But deserts have the most violent seasons on Earth, and the sky is the whole zone here. Dust storms, monsoon cells, flash flood channels running and then dry, temperature swing sold through light and audio. Badlands is barren, not dead, and the difference should be audible.

**Searing Gorge and Burning Steppes. Arrest, but a loud arrest.** These are held by an active forcing function, Ragnaros beneath and the Dark Iron and black dragonflight above, and elemental fire overwhelms any calendar. Worth distinguishing from the Plaguelands in kind: the Plaguelands are arrested into silence, the Steppes are arrested into noise. Both fail to turn. Only one of them is quiet about it.

**Elwynn Forest. Full turn, flagship.** Deciduous, farmed, and the first zone most Alliance players ever see. Goldshire under snow is the screenshot that sells the entire system. Elwynn is also where the herb migration in 10.3 is most felt, since its briarthorn going dormant is what sends people south.

**Westfall. Full turn, and it does thematic work.** Westfall is an abandoned breadbasket. Making the fields still turn with the year while nobody harvests them is a better statement of that than any quest text: the land is fine, the people left. Harvest golems standing in wheat that goes gold and then rots in place. Dust in high summer, which the zone art already leans toward.

**Redridge Mountains. Full turn.** Temperate and wooded around Lake Everstill, with enough elevation that winter should bite harder than in Elwynn next door. The lake freezing at the edges gives Lakeshire a seasonal identity.

**Duskwood. Full turn under permanent darkness.** This is the interesting one. The curse from Medivh's death fixes the light, so Duskwood never gets a day. But the forest is described as dying, not dead, and things clearly still live in it. So the season moves through Duskwood without ever touching the sky. Fog thickens and thins, the spiders around the Yorgen Farmstead den in winter, the understory changes, snow settles on gnarled trees under a black sky. That last image is worth building for its own sake, and it makes Duskwood distinct from both the living zones and the arrested ones instead of getting lumped in with either.

**Deadwind Pass. Arrest.** Petrified leafless trees and a wind that never stops, with Karazhan leaking into the ground. Nothing here should register the year.

**Swamp of Sorrows. Muted, warm.** Subtropical wetland with no cold season to speak of. What moves is water level, insect and ambient audio density, and rain frequency. It slows in what passes for its dry months rather than stopping.

**Stranglethorn Vale. Muted, at the top of the tier.** Tropical, so temperature is not the axis, but the tropics have a real seasonal cycle and it is wet against dry. Monsoon rain that actually changes visibility and audio for a stretch of the year, then a drier stretch. Stranglethorn sits closest to full turn of anything in the muted tier, which suits its role in 10.3 as the shelf-stable pantry: it keeps producing because its season is a rain cycle rather than a growing one.

**Blasted Lands. Arrest.** The Dark Portal did this and the zone is the evidence.

#### Kalimdor, north to south

Kalimdor does not sort as cleanly as the Eastern Kingdoms, and the reason is worth stating before the list. A dry band runs across the whole middle of the continent, Durotar and the Barrens and Thousand Needles and on down into Tanaris, at exactly the latitudes where the Eastern Kingdoms is temperate farmland. Latitude alone cannot explain that. What can is moisture: the wet ground is coastal and northwestern, Darkshore and Ashenvale and Feralas, and the central mountains stand between the ocean and the interior. Stonetalon and the western wall of the Barrens catch the rain and the interior sits in the lee of it. Feralas stays lush because it is coastal and exposed on the southwest side, not because it is far south.

This matters mechanically, because it means the dry zones of Kalimdor are dry for ordinary reasons and should therefore still have a real seasonal cycle. It is just a wet and dry cycle rather than a warm and cold one.

**Teldrassil. Muted, on the tree's terms.** Teldrassil is a World Tree grown after the Third War and the zone is its canopy. The palette is warm gold by the tree's own vitality, not by the month, so it should not go bare in winter. What moves is weather through the branches, light, and the sound of the canopy. A grown thing that keeps its own color is a different statement from a static one.

**Darkshore. Full turn, and the storms are the point.** Exposed western coastline, temperate, already wet and grey. Winter here should be genuinely hostile: sea storms off the water, heavy surf, poor visibility along the Auberdine road. Then a real summer that makes the ruined coast almost pleasant. Darkshore has the largest gap between its best and worst month of anywhere on the continent, which is a good use of a low-level zone people otherwise pass through once.

**Felwood. Arrest, with one deliberate exception.** Felwood was northern Ashenvale before Tichondrius and the Skull of Gul'dan corrupted it, and the healing has been slow. So it does not turn. But the Emerald Sanctuary is in vanilla, and Greta Mosshoof is there working to cleanse the taint. Give the ground immediately around the Sanctuary the faint pulse of a Tier 2 zone while the rest of Felwood stays flat. That reads as an effort that is working in a small radius and losing everywhere else, which is exactly what the quest text says, and it costs one localized art state.

**Ashenvale. Full turn, and it does the strongest border work in the game.** Ashenvale should carry the full cycle, and the Felwood border then becomes a sharper version of the Hinterlands argument in the Eastern Kingdoms, because Ashenvale and Felwood were literally the same forest. One half turning red and gold while the other half does nothing, along a line that exists only because of something that happened in living memory. The Warsong logging in Section 1 gains from this too: clear-cut ground reads differently in each season.

**Winterspring. Muted, with a rare exception that lore hands us.** Winterspring is alpine, above the cloud bank that separates it from Moonglade, and perpetually snowed. Normal years get the Dun Morogh treatment: sun angle, day length, storm severity, ice on Lake Kel'Theril. But Warcraft III put the valley in a rare snowless spring during Reign of Chaos, which is an explicit canonical statement that Winterspring can thaw and almost never does. So build that. Once every several in-game years, on a long cycle nobody can predict from a calendar addon, Winterspring greens. That is the single best seasonal event available anywhere in the world and the lore already granted permission for it.

**Moonglade. Arrest into life.** The lore is explicit: Moonglade sits under perpetual night, the moon stays high, and the land never suffers extremes of weather, holding in a warm endless summer evening. So it is arrested, and it is the only pleasant arrest in the world. This pairs against Duskwood deliberately. Both are permanently dark, one by curse and one by holiness, and the seasons behave in opposite directions: Duskwood's forest still turns under a black sky, Moonglade's refuses to. Two zones with the same lighting and inverse relationships to the calendar is a better argument for the whole system than either one alone.

**Azshara. Muted, high in the tier.** Coastal, temperate by latitude, and permanently gold and violet in a way that reads as arcane residue from the Highborne rather than as autumn. Keep the canopy. Move the weather hard, since it is an exposed eastern coast, and move the fauna, which Azshara has in unusual density. Close to Teldrassil in treatment, for a different reason.

**Stonetalon Mountains. Full turn with altitude.** Mixed forest on real elevation, so snow on the high ground in winter while the lower reaches stay green longer, and the same moving snowline proposed for Alterac. Stonetalon is also the zone that catches the rain the Barrens does not get, so a visibly wetter Stonetalon in the wet season is the in-world explanation for the dry zone next door.

**Durotar. Muted, with a wet season.** Hot, red, and dry, but coastal, and dry coastal regions get violent rain when they get any. Storms off the water past the Echo Isles, wadis that run and then go dry, dust in the long hot months. No green, but a lot of sky.

**The Barrens. Full turn on the moisture axis, and the highest-value zone on this list.** Savannas have the most dramatic wet and dry cycle of any grassland on Earth, and the Barrens is a savanna. So it gets a genuine turn: grass greening after the rains and going gold and then brittle, the oases swelling and shrinking, plainstrider and zhevra density shifting with it. The Barrens is also the most-traveled zone in Classic and the one players hold the strongest memory of. A wet-season Barrens would be felt by more people than any other single piece of this document.

**Mulgore. Full turn.** Open fertile plain, green to gold to brown to bare, with sightlines from Thunder Bluff that show the whole zone's state at once. Kodo grazing patterns and the herds around Bloodhoof Village give it a fauna component for free.

**Desolace. Arrest, and still being drained.** Desolace was Mashan'she, fertile grassland, until the tauren shaman woke Princess Theradras and she consumed the land's energies to rebuild herself. She is still down there, in Maraudon, at the edge of the zone. That makes Desolace an active drain rather than old residue, closer to the Burning Steppes than to the Plaguelands in kind. Note for scope: the Cenarion Wildlands regrowth is a Cataclysm change and has no place in a Classic-era proposal, so unlike Felwood there is no healing exception to carve out here.

**Dustwallow Marsh. Muted, warm.** Subtropical wetland with no cold season. Water level, insect and ambient density, rain frequency. Same treatment as the Swamp of Sorrows, and the Theramore waterline is a free gauge the way Menethil's is.

**Thousand Needles. Muted, loud, with one good detail.** Mesa desert where wind is the zone's whole signature. But the Shimmering Flats is a dry lake bed, and dry lake beds take shallow water in the wet season. Let it flood, thinly, for a stretch of the year. The goblins built the Mirage Raceway on a seasonal lakebed and have to deal with it periodically, which is both funny and completely in character for Steamwheedle.

**Feralas. Full turn on the moisture axis.** Coastal rainforest in the southwest, so temperature is not the lever and monsoon is. Rain that genuinely changes visibility and audio for a stretch of the year, then a drier stretch. Feralas is also the richest herb zone in the level range and Thalanaar sits on its eastern edge, so the 10.3 migration and the 8.10 wandering trainers both have business here.

**Tanaris. Muted, loud.** True desert. No flora to lose, so it runs on sky: sandstorm frequency, the extreme swing between day and night heat sold through light and audio, haze. Gadgetzan is the reference point everything is measured against.

**Un'goro Crater. Muted, sealed.** The crater wall is the whole climate argument. Un'goro is thermally and hydrologically cut off from the desert around it, so it holds its own jungle regardless of what Tanaris and Silithus are doing. Very slight pulse: light across the rim, storm cells that get trapped inside and sit. The devilsaur territory work in 4.5 and the 1.7 Cenarion researcher both live here, and a crater that stays lush while everything around it turns is a better frame for both.

**Silithus. Arrest.** C'Thun beneath and the qiraji above, and the sandstorm never lets up. The newest of the arrested zones in Classic terms, since it was rebuilt in 1.9, and the flattest.

Mount Hyjal is out of scope; there is no playable Hyjal in the Classic client to give a season to.

#### What the pattern says

Work both continents and the classification stops feeling like a judgment call. Almost every zone sorts itself off two facts the game already established, where it sits and what happened to it.

The full-turn zones are the ordinary ones: a temperate belt from Silverpine to Westfall in the Eastern Kingdoms, and on Kalimdor a wet northwest from Darkshore through Ashenvale and Stonetalon plus the grasslands and savanna of Mulgore, the Barrens, and Feralas. Note that the Kalimdor list turns on moisture at least as often as on temperature, which is the correction folded back into 10.1.

The muted zones are the natural extremes, and there are more of them on Kalimdor than in the Eastern Kingdoms: alpine at Dun Morogh, Winterspring, and the high ground of Alterac and Stonetalon; desert at Tanaris, Thousand Needles, Durotar, and the Badlands; tropical and swamp at Stranglethorn, Dustwallow, and the Swamp of Sorrows; and three zones held to their own palette by something growing or lingering in them, Teldrassil, Azshara, and Un'goro.

The arrested zones cluster tightly around catastrophes the lore already names, and they divide into three kinds rather than one:

- **Residue.** The event is over and the damage remains. Western and Eastern Plaguelands, Blasted Lands, Deadwind Pass, Felwood.
- **Active.** Something is still doing it, right now, from inside the zone. Searing Gorge and the Burning Steppes with Ragnaros beneath, Desolace with Theradras in Maraudon, Silithus with C'Thun.
- **Held.** Arrested deliberately, and into life rather than out of it. Moonglade, alone.

That last category having exactly one member is the shape of the argument. Moonglade is arrested for the same mechanical reason the Plaguelands are, and the effect is the opposite, and a player who has seen both understands something about Azeroth that no quest text tells them.

The two hybrids are worth keeping visible because they are the cases a simpler model would have flattened. Tirisfal can go down but not up, so it winters hard and then returns to autumn instead of to spring. Duskwood turns fully under a sky that never changes. Both come straight out of lore that was already on the page.

That is the method this whole document runs on. The lore already says which parts of Azeroth are healthy, which are wounded, and which are being held. Seasons is the first system here that lets a player see all three from the road.

### 10.3 Flora

Herbs should not run on a generic winter switch. Each herb gets its own calendar, the way a real crop does.

Hardy species run nearly year-round. Silverleaf and earthroot behave like weeds and should stay findable in almost any season a zone is not frozen. Delicate species get real windows: a spring-blooming mageroyal, a late-summer liferoot, present for a stretch and then gone until the next cycle.

The rule that keeps this from being punishing is that nothing leaves the world, it migrates. When Elwynn's briarthorn goes dormant in the northern winter, briarthorn is still coming up in the warmer south. The reagent is available. It is further away and it costs more to get, which is a different thing from being unavailable.

This makes the tropics quietly load-bearing. Stranglethorn and Un'goro become the shelf-stable pantry, always producing something, while the temperate belt is where the calendar is actually felt.

### 10.4 Fauna

Beast density follows the same clock. Packs thin out and den during a zone's winter and thicken during its growing season, so skinning and the hunt migrate alongside the herbs instead of running on separate rules.

Never to zero. These are quest zones and leveling grounds before they are ecosystems. A winter Elwynn has fewer wolves, not no wolves.

This layers onto the rest cycles proposed in 4.2 rather than duplicating them. That proposal already builds denning as a behavior on a daily cycle. Seasons runs the same machinery on a yearly one.

### 10.5 Quests that breathe

This is the piece that can quietly break things, and it is now resolved.

If a quest asks for eight wolf pelts and the wolves have thinned for the winter, the quest is broken. Not impossible, just slower and more tedious than it was tuned to be, which is the worst kind of broken because almost nobody reports it. They just remember that the zone felt bad.

So gathering and kill requirements scale against current density. The winter version asks for five, the summer version asks for eight, and the reward scales with it, so completion time stays roughly flat across the calendar. Three decisions govern how.

**Visible, not silent.** The count shown to the player is the real count. No hidden drop-rate flexing behind a fixed number.

The argument for hiding it is that nobody is ever confused. The argument against is stronger: a system the player cannot perceive is a system that cannot be learned, and everything else in this document is built on the player learning to read the world. A quest that asks for five in winter and eight in summer teaches the seasonal model in one sentence, for free, to everyone who levels through the zone twice.

This carries a concrete authoring constraint that is easy to miss. **Quest prose may not contain the number.** Write "thin the pack" and "bring me what hides you can," never "slay ten of them." The objective counter renders from a field and updates itself; the flavor text does not. This also means vanilla's existing quest text needs an audit for hardcoded numerals in any quest that would flex, which makes this the one part of Section 10 that is revisionary under 11.4 rather than additive.

**The requirement moves, including under an accepted quest.** Locking at acceptance is safer and it is wrong. The whole premise is that the number reflects what the world currently is, and a locked number is a number that has stopped reflecting anything. A player who accepted a quest in autumn and returns in winter should find that the request has changed, because the situation has.

The sharp edge is progress. A player sitting at four of five who watches the requirement rise to eight has just gone backwards, which is the worst feeling any progress bar can produce. Two rules remove it without reintroducing the lock:

- **Kill counters scale proportionally.** Progress is held as a position rather than an absolute. Four of five becomes six of eight. The number moved, the player did not lose ground, and both facts are true at once.
- **Item counts never rise on an accepted quest.** Physical drops are already in the bag and cannot be retroactively added to, so a rising requirement would genuinely take something away. These move down freely and are capped at the accepted value going up.

The asymmetry is not arbitrary. It falls directly out of the difference between an abstract counter and objects a player is carrying.

**Scope is derived, not chosen.** A quest's requirement moves if and only if the thing it asks for has moved. That single rule settles every case without a list:

- Kill quests for a species whose density changed with the season: yes.
- Gather-from-corpse quests where the drop is the bottleneck: yes.
- Herb and gathering quests in a zone where the flora migrated under 10.3: yes.
- Kill one named NPC: no. One is one in every season.
- Deliver, escort, explore, and talk-to quests: no. Nothing the world did affects them.

**Flare-ups do not flex quests.** Worth stating because the rule above looks like it would sweep them in. Seasonal density is a sustained baseline shift lasting months, which is why quests should track it. A flare-up under Section 6 is transient and measured in hours, and 6.7's protections exist precisely so quests do not have to respond to it. Requirements track the baseline, never the spike.

**On the obvious exploit.** A player could bank quests and complete them in the cheap season. This neutralizes itself, because the reward scales with the count, so waiting for the smaller requirement also means waiting for the smaller payout. What is left is a player who chose to hold a quest for several months in exchange for nothing, which is not a problem worth engineering against.

### 10.6 What this does to the economy

Seasons give the work in Sections 3, 8, and 9 something none of it currently has: a reason for prices to move that is not player behavior.

**Stockpiling becomes a skill.** An alchemist who knows liferoot comes in late summer buys deep and sits on it. The vanilla economy never rewarded that kind of planning because nothing in it was ever scarce on a schedule.

**Caravans get real cargo.** The carts in Section 2 and the trade network in Section 3 have been hauling goods largely for their own sake. Seasonal scarcity means a midwinter shipment of southern herbs going north is worth something specific to somebody.

**Vendor stock swings with the calendar.** The restock model in Section 9 can read the season directly rather than needing its own logic.

And it partially solves a vanilla problem nothing else in this document touches: low-level zones die the moment you outlevel them. If Elwynn's summer bloom is genuinely the cheapest source of a reagent for three months of the year, a level sixty alchemist has a concrete reason to go back there. Cross-tier materials in 8.7 pushes the same direction by making low-level goods matter. Seasons puts them on a schedule.

### 10.7 Cost and separability

This is Tier 3 and it is the largest single item in the document. It touches spawn tables, resource nodes, quest requirements, and zone art simultaneously, and it cannot be retrofitted onto an established economy without real disruption. It is a launch decision.

The visual pass is the exception and should be scoped separately. Foliage tint, snow cover, ambient audio, and lighting on a yearly cycle with no gameplay hooks attached is Tier 1 work. It ships alone, it costs a fraction of the full system, and it gets the art tested a long time before anything reads from the clock. If seasons never make it past cosmetic, that version is still worth having.

### 10.8 Snapping to the calendar the game already runs

Vanilla already has a year: Winter Veil, the Lunar Festival, Midsummer, Hallow's End, on real dates, already implemented.

The seasonal clock should snap to these rather than run beside them. If the two disagree, both feel arbitrary. If Winter Veil lands in the deepest part of the seasonal winter and Midsummer at the peak of the growing season, each confirms the other and neither needs explaining. It also gives 10.6's demand spikes fixed anchor dates that players already plan around.

The Lunar Festival is the sharpest case, because it is held in Moonglade, which 10.2 classifies as the only zone in the world held permanently in a warm summer evening. A midwinter festival in the one place that never has winter is a better joke than anything we would write, and it already shipped. Tier 1.

### 10.9 What weather is allowed to do

Once seasons exist, weather stops being decoration and the question of what to hang on it becomes live. It needs a rule, because the obvious ideas divide sharply into ones that work and ones that quietly teach players to log off.

**The rule: weather changes what is available, not what you are capable of.**

Lashers appearing in the rain changes what is available. A five percent hit penalty during a sandstorm changes what you are capable of. Both make weather matter. Only the first gives anyone a reason to be outside while it is happening, and the second actively teaches that the correct response to weather is to wait it out somewhere safe, which is the opposite of everything this document is for.

Three anti-patterns worth naming, because each one sounds like flavor and is not.

**Never put weather in the combat math.** Frost spells hitting harder during a snowstorm reads as atmosphere and functions as balance. A five to ten percent swing on a school is enormous, the community solves it within a week, and afterwards people are scheduling around the forecast and stacking classes by condition. That is Constraint 3 failing exactly as written: the world stops being discovered and starts being managed.

**Never make a penalty invisible.** Nobody can perceive five percent hit. They miss more, feel vaguely worse, and never connect it to the dust. If a penalty exists at all it has to be legible in the moment, something a player can see and point at, like obscured vision or reduced movement.

**Never tie a penalty to race or class.** Frost damage in Dun Morogh for anyone who is not a dwarf or gnome is not a weather system, it is a tax on a character creation choice made ninety seconds earlier in Coldridge Valley.

**Weather-conditional gathering, which is the version worth building.** A herb that grows only during rain and withers a few hours after the rain begins, regardless of when it is picked, is the best available use of the whole system. It is additive, since nothing is removed on a dry day. It cannot be farmed on demand, which satisfies 7.6. It is self-limiting by construction. And the way a player finds out is somebody saying it is raining in the Wetlands, which makes it social in the same way flare-ups are.

This runs on the same machinery as the seasonal herb windows in 10.3, just at a scale of hours instead of months.

**The gating limit.** Vanilla already gates crafting on world state: Mooncloth must be purified at a moonwell and sits behind a four-day cooldown [44][45]. That works because a cooldown is predictable, so it is planning. Weather is not predictable, so gating anything required behind it converts planning into waiting, and the cost falls hardest on players with fixed play windows. Weather may gate a bonus. It may not gate a prerequisite.

Tier 1 for the gathering windows and the audio and lighting work. Tier 2 for anything that touches spawns.

---

## 11. Implementation Tiers and Rollout

### 11.1 Why this section exists

These proposals are not equally expensive, and more importantly they are not equally reversible. A live-service game can patch in animation work indefinitely. It cannot casually retrofit a new economic model onto a server that has been running for eight months on the old one.

### Tier 1: Cosmetic and behavioral

Animation states, pathing, spawn logic, bark cycles. Nothing touches drop tables, itemization, or the economy.

Includes: all NPC routines and idle behavior (Section 1), city density and shift rotation, wandering profession trainers, creature pack behavior and rest cycles, species-specific animation, concealment art passes.

**Deployment: patchable at any time, incrementally, zone by zone.** This tier does not need to be announced as a system change. It is the ongoing content cadence.

The one caveat inside Tier 1 is the vegetation and concealment work in Section 4.3, which is an art pass rather than a scripting pass. It is still additive and still safe to patch, but it should be scoped per zone and budgeted accordingly.

### Tier 2: Contained new systems

New spawn logic, trigger conditions, pathing infrastructure, and new content that does not require rebalancing anything that already exists.

Includes: the cart and caravan network as a traversal feature, wandering rares, the swallowed-remains rare loot family, unscripted faction flare-ups and their hidden trigger conditions, the guard-hint system for locating trainers, and all new professions (jewelcrafting, inscription, woodcutting, trapping, relic hunting).

New professions land here rather than Tier 3 because adding a profession does not require touching the ones that already exist.

**Deployment: post-launch content, but planned. These need engineering, not just assets.**

### Tier 3: Architectural

Changes to how gold and materials flow for the entire playerbase.

Includes: the vendor restock economy (Section 9), cross-tier material requirements (Section 8.7), and the global loot and coin rebalance (Section 7) if it is intended as a genuine repricing of leveling income rather than a flavor pass.

Loot logic is the borderline case. Removing coin from beasts as flavor is close to Tier 2. Removing coin from beasts as a deliberate reduction in leveling gold income is Tier 3, because it changes mount timing, respec affordability, and consumable access for every player in the game.

**Deployment: launch decisions. Retrofitting these onto an established economy is disruptive in ways that are difficult to communicate and impossible to reverse cleanly.**

### 11.2 Rollout strategy

The fresh-realm-as-testbed model resolves the Tier 3 problem cleanly, and Blizzard has already run the play. Season of Discovery served as a sandbox for rule-bending that would have been unacceptable as a permanent change to Era realms [5][6].

The proposal:

1. Launch Tier 3 changes only on a new realm, with the new ruleset present from the first day. Nobody's established gold or market position is disrupted, because there is no established position. Everyone starts even.
2. Run Tier 1 and Tier 2 as ongoing content on that realm and, where compatible, on existing realms.
3. Fold forward what works. Successful Tier 3 systems become the default for subsequent fresh realms, with backporting to existing realms as an opt-in per-realm decision.

The industry pattern already supports this. Fresh realms launch regularly, which means there is a recurring natural window to introduce an architectural change without asking any existing player to accept it. And the resulting decision is backed by real player data rather than a design argument.

The important constraint on step 3 is that folding forward should require player appetite on the originating realm, not just internal enthusiasm. A system that works mechanically but that its own playerbase does not want is not a success.

### 11.3 Assuming the game has already shipped

The tiers above are written as pre-launch advice, and Tier 3 is defined as launch decisions. That framing has a problem: if Classic+ is already built and running, Tier 3 stops meaning risky and starts meaning too late, which quietly writes off a large share of this document.

So the rest of Section 11 assumes the game shipped and asks a different question. Not how risky is this, but what can be added to a live world, in what order, and what does each addition require to already be there.

The tiers still hold. They measure reversibility and they were never wrong. What they do not give is a sequence.

### 11.4 Additive versus revisionary

The distinction that matters in a live game is not cost. It is whether a change invalidates something players have already learned.

**Additive** changes put something in the world that was not there. New animations, new NPCs, new camps, new drops, new flavor text. A player who knew the old world is not wrong about anything, they simply have not seen the new part yet. These can ship to live realms indefinitely, in any order, with no announcement.

**Revisionary** changes alter something that already exists and is already known. Moving a drop source, rebuilding a familiar town, repricing loot, changing what a zone looks like in a given month. These are not necessarily expensive and they are not necessarily risky in an engineering sense. They are expensive in player trust, because someone learned that thing and now their knowledge is stale.

This cuts across the tiers rather than aligning with them, and it produces at least one result the tier system gets wrong. The behavioral tell audit in 7.7 is Tier 2 by engineering risk and nearly harmless in isolation, but it relocates drop sources that players have had memorized for twenty years. Post-launch, it is one of the more disruptive things in this document. Conversely 12.3's material camps are new locations that take nothing away, so despite touching the world map they are as safe as an animation pass.

The working rule: **on live realms, ship additive freely and treat revisionary as a fresh-realm item regardless of tier.**

### 11.5 The layers

The sequence below is ordered by dependency rather than by cost, because the ordering is not only about safety. Each layer is what makes the next one legible. Material chains do not parse if every settlement still looks alike, since there is no way to tell where the timber went. Seasons do not land without ambient life to react to them. Corpse scavenging is invisible without the creature behavior that frames it. Shipping a later layer first does not break anything, it just wastes it.

**Layer 1. The world in motion.** Purely additive, no dependencies, unlimited runway. NPC work routines and city shift rotation (Section 1), creature pack structure, rest cycles, and species behavior (4.1 to 4.4), the swallowed-remains loot family (7.4, 7.5), the naturalist flavor voice across anatomy items (7.7), the Park district dressing (1.8), Kodo Graveyard scavenger presence (4.6), the Stormwind quarry and other material origins (12.3), and settlement differentiation (Section 12) proceeding one town at a time forever.

This layer is the ongoing content cadence. It never has to end and it never needs a patch note framing it as a system.

**Layer 2. The world reacting.** Contained systems built on Layer 1 being visible. Faction flare-ups and their hidden conditions (Section 6), corpse scavenging with the attention mechanic (4.6), the corruption gradient and runners (4.7), responsive Razorfen thorn growth (Section 5), wandering trainers and the guard hint system (8.10, 8.11), kobold and ore correlation (8.12), and contestable material sources (12.3).

These need engineering rather than assets, and each one needs its Layer 1 groundwork present or players will not read the reaction as a reaction.

**Layer 3. The world circulating.** Carts and routes as a traversal and supply feature (Sections 2 and 3), vendor stock as a supply consequence (Section 9), Westfall interdiction (9.5), and the material chains in 12.3 as functioning freight rather than set dressing.

Layer 3 is where additive stops being sufficient, because vendor stock becoming variable is revisionary by definition. Fresh realm.

**Layer 4. The world on a clock.** Seasons (Section 10), which 10.7 already argues is separable. The muted-pulse tier from 10.2 is lighting and weather and can ride along in Layer 1; the full turn and everything hanging off it belongs here, last, because it is the only proposal that depends on nearly all the others to be worth its cost.

### 11.6 What the fresh-realm cadence is actually for

11.2 proposes fresh realms as the testbed for architectural change. Under the post-launch framing that role gets sharper: **every fresh realm is another launch, and therefore another chance to reserve hooks.**

The thing that cannot be retrofitted is not a system, it is a hook. A per-zone climate state, a route and cargo entity, vendor stock stored as a variable rather than a constant, a hidden-condition engine that flare-ups and scavenging and seasons can all read from. Any of these can ship inert, doing nothing visible, costing almost nothing. What they buy is that Layers 3 and 4 remain possible later without a rebuild.

So the recommendation for any subsequent realm launch is to ship the hooks even when the systems are years out, and to ship them switched off. That is the cheapest decision in this entire document and the only one that expires.

### 11.7 What ships where

Three deployment paths on a live game, sorted by what actually forces the difference. The dividing question is not how big a change is. It is what could go wrong that reasoning alone will not catch.

**Straight to live realms.** New content with no new logic, no server load at scale, and nothing to exploit. Failure mode is a visual bug, which is a hotfix.

- Flavor text across anatomy items and the naturalist voice (7.7)
- The swallowed-remains loot family (7.4, 7.5), since the rates are deliberately negligible and nothing is removed
- New static locations: the Stormwind quarry, material camps and their approach roads (12.3), the Park district dressing and idle masons (1.8)
- Permanent scavenger presence at the Kodo Graveyard (4.6), which is a static spawn rather than the attention system
- Localized work animations: the Venture logging crew at Windshear Crag, Bloodsail downtime, Dark Iron crews near Ironforge, the Booty Bay docks (1.2 to 1.5)
- Hard-to-reach lore NPCs (1.7)
- Settlement dressing where it is new construction rather than a rebuild

**Needs a PTR.** Four distinct reasons, and it is worth knowing which one applies, because they need different test plans.

*Server load.* City-scale NPC routines and shift rotation (1.6) and the creature behavior pass (4.1 to 4.4) touch thousands of entities. Neither is risky by design, both are risky by volume, and no amount of reasoning substitutes for watching Stormwind at peak population.

*Exploitability.* Flare-ups (Section 6), the scavenging attention mechanic (4.6), and the guard hint system (8.11) all have hidden conditions, and hidden conditions get datamined and farmed. 6.7 and the decay rule in 4.6 exist because of this, and both are tuning claims that need a live population to falsify.

*Player knowledge going stale.* The behavioral tell audit (7.7) and the Anti-Venom sourcing fix (8.13) relocate drop sources people have memorized. Technically small, socially expensive, and the PTR here is as much about giving notice as about finding bugs.

*Taste.* Settlement differentiation of existing towns (12.2) and the muted seasonal pulse (10.2) are revisionary and visual. Nothing breaks. The question is whether people like it, and that is not answerable internally.

Also here: new professions (8.1 to 8.6), wandering trainers (8.10), the corruption gradient and runners (4.7), kobold and ore correlation (8.12), responsive thorn growth (Section 5), and carts running as observable traffic without cargo consequences (2.5).

**Fresh realm, then backport by opt-in.** Anything that changes how gold and materials flow for everyone. These are not more likely to fail; they are harder to reverse and impossible to introduce fairly to players with established positions.

- Vendor restock as a supply consequence (Section 9) including wagon delivery crediting stock (9.4) and Westfall interdiction (9.5)
- Cross-tier material requirements (8.7)
- The loot and coin repricing (7.2, 7.3) where it is a genuine change to leveling income rather than flavor
- Caravan robbery and its reputation costs (2.6), since it prices an existing faction currency
- The full seasonal turn and everything hanging off it (10.2 to 10.6)
- Material chains operating as real freight (12.3)

Backport per 11.2: fold forward only with demonstrated appetite on the originating realm, as an opt-in per-realm decision.

### 11.8 The proposals that split, and why that is the strategy

Several items appear in more than one bucket above, and that is not indecision. The same shape recurs: **the visible half can ship to live now, the consequential half needs a fresh realm.** That turns out to be an advantage rather than a compromise.

- **Carts.** As traffic on the roads, they are scenery and go through PTR to live. As the thing that determines vendor stock, they are fresh realm.
- **Seasons.** The muted pulse in 10.2 is lighting, weather, and audio, and can ship to live realms. The full turn, with herb migration and beast density and price movement, is fresh realm.
- **Material sourcing.** Placing the camps and quarries is additive and ships now. Making them actually feed settlements is fresh realm.
- **Loot logic.** Flavor and rare story drops ship now. Repricing leveling income does not.

Shipping the visible half first is the right order regardless of the constraint. By the time the consequential version launches on a fresh realm, players have spent months seeing wagons on the roads and camps beside them, so the system arrives already legible instead of needing to teach itself. The visual language gets established on live realms at no risk, and the fresh realm inherits an audience that already knows how to read it.

It also produces a useful test. If the visible half ships and nobody notices or cares about the wagons for a year, that is real evidence against building the consequential half at all, and it was collected cheaply.

---

## 12. Art Direction

Every other section in this document proposes a system. This one proposes a stance, because the systems will be built by someone with an art budget and the way that budget gets spent will decide whether any of it looks like Classic.

### 12.1 Variety, not fidelity

The concern is that a Classic+ art pass follows retail: higher resolution textures, normal maps, re-lit interiors, denser geometry. That would be a mistake, and not for nostalgic reasons.

Retail's problem was never polygon count. It is that higher fidelity pushes everything toward a single house style, because detailed assets are expensive and expensive assets get reused. Classic reads as characterful partly because the art had to carry meaning through silhouette and color rather than surface detail, and silhouette is what actually reads at distance across a zone.

So the rule: **spend the art budget on variety, not fidelity.** Same texture resolution, same polygon budget, more distinct assets. This is both cheaper than a fidelity pass and more faithful to the original, and it is the same shape as the constraint in 7.7, where the expensive axis and the good axis turn out to be different axes.

Explicit anti-goals, worth stating because they are what a well-meaning team does by default:

- No normal or specular pass over the existing kit
- No re-lighting of interiors that currently read by flat color
- No replacement of iconic silhouettes, however dated they look in isolation
- No detail that only resolves at a distance the player never stands at

### 12.2 The four things that make buildings differ within one culture

Southshore and Darkshire are both human and should feel almost nothing alike. What separates real buildings inside a single culture is not taste, it is four practical constraints, and vanilla has all four available and unused.

**Materials, meaning whatever is within hauling distance.** Southshore is coastal farmland, so timber, fieldstone, and lime wash. Lakeshire has a working lumber mill, so it should look overbuilt in heavy timber, because wood is the cheap thing there and people overuse whatever is cheap. Menethil Harbor is a port with no forest behind it, so stone. Sentinel Hill is farm country stripped of its farmers, so salvage.

**Climate, which mostly means roof pitch.** Steep roofs shed snow and heavy rain. Shallow roofs with wide eaves suit places where the problem is sun. A Westfall farmhouse and a Hillsbrad farmhouse should not share a roofline. This connects directly to Section 10: once seasons exist, a player can watch the steep roofs in Hillsbrad doing the job they were shaped for, and the argument closes itself.

**Threat, which is the most legible of the four.** Darkshire boards its windows and keeps the Night Watch on patrol because of what is in the trees. Sentinel Hill is built around a fortified tower because of the Defias. Goldshire has no defenses at all, and that is information too. A player should be able to guess how dangerous a region is from the buildings before meeting anything in it.

**Age.** 2.4 already argues the Eastern Kingdoms should feel older than Kalimdor, and buildings are the cheapest place to show it: additions in mismatched materials, patched roofing, a stone foundation under a timber upper floor that was obviously added later. Kalimdor's Horde settlements should look built rather than accumulated, because they were.

### 12.3 Where the material comes from

12.2 says a settlement should be built from what is within hauling distance. The stronger version is that the hauling distance should be on the map. Every settlement's material ought to have a findable origin, and finding it should be possible on foot.

**The game already did this once, completely.** Durotar has no forests. Orgrimmar is built from timber. The Warsong clan logs Ashenvale, where the forest is described from the orc side as a cache of building planks, and the route is already drawn: the Warsong Lumber Camp and Labor Camp in eastern Ashenvale, Mor'shan Base Camp at the northern end of the Barrens, then the road south [38][39]. Warsong Gulch is a battleground fought over construction material. The Silverwing Sentinels are defending a forest and the Outriders are defending a supply line.

Nothing in this document needs to invent that. It needs to notice that vanilla built one complete material chain, made a battleground out of it, and then never applied the idea to a single other settlement.

**The Westfall case, and the rule it produces.** Sentinel Hill needs timber and Westfall has almost none. Two options present themselves: put a logging camp near the Duskwood bridge in the southeast so the source is visibly external, or add trees to the southern hills so the zone can supply itself.

The first is correct and the second is a trap. Westfall's treelessness is not an oversight, it is the zone's entire character: a stripped farm country that cannot provide for itself. Adding a local timber supply solves a problem the zone exists to have. The external camp does the opposite, making the dependency visible and giving 9.5's interdiction something concrete to cut.

The rule generalizes: **when a zone's poverty is the point, the material source must be external.** Where a zone is meant to read as self-sufficient, put the source inside it.

There is a second payoff in the Westfall case that comes free. Timber crossing the Duskwood bridge is timber from a cursed forest, and Darkshire is already built from it. A hard-up settlement building with wood nobody else wants is a better explanation of Sentinel Hill's character than any amount of art direction.

**The constraint on terrain.** Prefer adding a camp, a road, or a structure over reshaping ground. Classic players know this terrain intimately and edits to it are the most conspicuous change available. Reshape only where the existing terrain already nearly supports the read, and treat any terrain edit as Tier 3 regardless of how small it looks.

**The inverse is also a statement.** A settlement built from something not locally available means somebody paid to haul it, and that is worth showing. Stormwind is cut stone in quantity, which implies a quarry that supplied the rebuild. Put it in the hills, worked out and abandoned, with mason marks still on the faces. 1.8 already has the guild that cut it walking off the job; the quarry is where they were working when they stopped.

Ironforge is the opposite extreme, carved from the mountain it occupies and importing nothing structural, which is worth making legible precisely because no other settlement can say it. Thunder Bluff is a third case: everything it is built from arrived by lift.

**What this buys the rest of the document.** Three things, none of them cosmetic.

- **Cargo becomes specific.** The wagons in Sections 2 and 3 currently carry goods in the abstract. Material chains give them named freight with a known origin and destination, which makes 2.6's robbery decisions concrete rather than generic.
- **Sources become contestable.** A logging camp or quarry is a place that can be pressured, which hands Section 6 flare-ups a target with consequences a player can trace to a settlement.
- **8.3 gains a reason to exist.** Woodcutting is more interesting when the world already agrees that timber is worth fighting over, and Ashenvale proves it does.

Tier 1 to place camps and quarries and dress settlements to match. Tier 2 to make sources contestable. Tier 3 for any terrain change, which should mostly be declined.

### 12.4 Shared grammar, different sentences

What keeps these recognizably human is a shared grammar rather than shared models. Same window proportions, same door and lintel logic, same way a roofline meets a wall, same chimney placement and construction. Shared vocabulary, different sentences.

This is what makes the proposal affordable. A kit of parts with consistent rules generates far more distinct buildings than a set of finished models, and it is the technique the original art was already halfway using.

The same applies per race rather than only to humans. Orc construction is lashed hide and timber over a frame; the question is what the Crossroads has that Razor Hill does not, given one is a supply junction and the other is a defensive outpost. Tauren structures are portable in origin, so Camp Taurajo should read as a camp that stayed and Thunder Bluff as the one that never had to move. Dwarven work is cut stone, so the interesting variable is how finished the cutting is, with Ironforge worked and Thelsamar rough.

### 12.5 The limit, and the thing variety costs

There is a real cost here and the document should be honest about it. The repeated kit is why a player can walk into an unfamiliar town and locate the inn in four seconds. Lose that and you have traded navigation for texture, which is a bad trade at any level of prettiness.

The fix is to vary the fabric while keeping the function legible. Whatever an inn is built from, it keeps the sign, the warm window light, and a recognizable mass. **Vary what a building is made of, not what it obviously does.**

This is also the honest limit on 12.2. A town whose buildings are so distinct that the town no longer reads as human has overshot.

### 12.6 Vanilla had the instinct and applied it unevenly

The pitch is not that variety is missing. It is that vanilla already did this in places and did not carry it through, which is a much easier argument to make and fits the method used everywhere else in this document.

Darkshire genuinely is more angular and dour than Goldshire. Lakeshire uses its water rather than sitting beside it. Menethil is built like a port. Then a great many other settlements share a layout for no reason the fiction supports. So the work is finishing something that was started, not importing a new aesthetic.

### 12.7 Where this breaks the tier system

Worth flagging, because this is the first proposal in the document where the tier system gives a misleading answer.

By risk, this is Tier 1. It is pure art, it ships whenever, it breaks nothing, and it can be patched in piecemeal one settlement at a time. By cost, it is closer to Tier 3, because it is a large number of art hours with no way to shortcut them.

The tiers as defined in Section 11 measure architectural risk and say nothing about budget. For everything else in this document those two roughly track each other. Here they diverge hard, and any team reading Section 11 as a rough cost ordering would badly underestimate this section. The tier stays 1, with the cost noted separately.

The practical consequence is that this is the most incremental proposal here. There is no minimum viable version and no launch dependency. One town at a time, indefinitely, starting with whichever pair of settlements most embarrasses the current kit.

---

## 13. Adding to the World

Everything above concerns the world as it exists. This section concerns adding to it, because the question will come up and because the way expansions answered it is the reason retail's world feels smaller than Classic's despite being many times larger.

### 13.1 Why expansion zones die

The world grows and gets smaller. That is the whole problem in one sentence, and the mechanism is not mysterious.

**Zones ship in batches tied to a level bracket.** Seven or eight arrive at once, are consumed in sequence over a few weeks, and then expire together the moment the bracket is cleared. A zone built for 60 to 70 has a defined lifespan by construction.

**They are placed outside the existing world.** A new continent inherits no traffic. Nobody passes through it on the way to anywhere, because there is nowhere on the other side.

**Their content is one-time.** Quest chains do not repeat. When the chain is done the zone has nothing left to offer, and a zone whose only offering is quests is a zone with an expiry date printed on it.

**The next expansion invalidates the last.** Gear resets, so the raids die. Reputations complete, so the hubs empty.

The result is a world where the active portion is always the newest slice, and everything behind it is scenery you fly over.

### 13.2 What keeps a zone alive, per vanilla's own evidence

Vanilla accidentally ran the experiment. Some of its zones die when you outlevel them and some never do, and the difference is consistent.

Un'goro stays busy because of herbs, devilsaur leather, and crystals. Winterspring stays busy because of Everlook, Black Lotus, and high-end reagents. Silithus has Cenarion rep and the war effort. The Eastern Plaguelands have the Argent Dawn, Stratholme, and Naxxramas. Stranglethorn has fishing, Zul'Gurub, Booty Bay's neutral auction house, and open-world conflict. The Burning Steppes and Searing Gorge have Blackrock Mountain.

Meanwhile Loch Modan, Redridge, Darkshore, Stonetalon, and Thousand Needles are ghost towns above level 30.

The rule falls out cleanly: **a zone survives if it has a reason that is not leveling.** A raid entrance, a profession material that stays valuable, a faction hub, or a neutral market. One is usually enough. None is fatal.

This is also the strongest argument for most of this document. Seasons in 10.6 gives low-level zones a reason to be visited at sixty. Cross-tier materials in 8.7 does the same. Material chains in 12.3 give ordinary zones a permanent industrial reason to exist. Every one of those is an anti-death mechanism applied to zones that already have the death problem, and the same mechanisms applied to a new zone are what would keep it from acquiring the problem in the first place.

### 13.3 Add inward, not outward

Expansions add outward because they are sold as products. A box price demands eight zones, so eight zones get built, so each one gets a fraction of the attention and none of them can be small. That constraint is real and it is not Classic+'s constraint.

A patch can add one zone. One zone, added well, lands harder than eight added at once, because it is not competing with seven siblings for the player's attention in the same month.

More importantly, it can be added **inward**. The vanilla map is full of gaps, closed gates, and places the world points at and never lets you reach. Filling those has properties that a new continent can never have:

- It inherits the existing road network, so people arrive on foot through 2.8's chokepoints rather than by portal.
- It has no clean level bracket, because it borders zones of several different levels, which makes bracket-based death harder to arrange.
- It is purely additive in 11.4's sense. Nothing existing changes, no player knowledge goes stale, and a player who never goes there is not wrong about anything.
- It is already promised. The wall, the gate, and the locked door are all in the game, and the world has been asserting for twenty years that something is behind them.

That last point is this document's method applied at the largest possible scale. Everywhere else the argument is to show what the lore already asserts. Here the lore asserts a place, and the map draws its front door.

### 13.4 The doors already in the world

An inventory, roughly by how ready each one is.

**Karazhan, from Deadwind Pass.** The clearest case in the game. The tower is modeled and standing, and Deadwind Pass has essentially no vanilla content of its own; the quests it does have arrived with The Burning Crusade and concern Karazhan [40]. Karazhan was intended for vanilla and cut for time [40]. So this is not an import from another expansion so much as the delivery of something vanilla was already building. Medivh, the Guardian, and the opening of the Dark Portal are all vanilla backstory. Deadwind Pass is also an arrested zone under 10.2, which makes it the right kind of quiet approach.

**The Emerald Dream, from four portals that already exist.** Patch 1.8 placed Dream Gates at Twilight Grove in Duskwood, Seradane in the Hinterlands, Dream Bough in Feralas, and Bough Shadow in Ashenvale, each guarded by one of the Dragons of Nightmare [41][42]. The portals are in the game. They are guarded. They lead nowhere. Four doors already distributed across two continents at four different level ranges is a better foundation for a zone than any expansion has ever started with, and the multiple-entrance structure defeats bracket death by construction. Ysera and the green flight are established vanilla lore, and the Nightmare corruption is already the reason the guardians are hostile.

**Gilneas, from the Greymane Wall.** A closed gate in Silverpine with a nation behind it, and the worgen thread is already running through the zone by way of Pyrewood Village and Shadowfang Keep.

**Grim Batol, from the Wetlands.** The fortress is visible and unreachable, and its Dark Iron and dragonflight associations connect directly to Blackrock content in 6.8.

**Quel'Thalas, from the Eastern Plaguelands.** The Thalassian Pass is blocked. High elf survivors are already present at Quel'Lithien Lodge in the Plaguelands and Quel'Danil Lodge in the Hinterlands, and Arthas's march through Quel'Thalas is vanilla backstory rather than an import. This one is the largest and should be treated with the most caution, since it comes with a race and a capital rather than a location.

**Hyjal, from Winterspring.** A blocked path at the top of the zone with a mountain behind it that Warcraft III already made significant. Worth noting the risk: the version that eventually shipped bore little resemblance to what the closed path implied, which is an argument for building it small rather than as a capstone.

**Azshara, from Azshara.** Not a closed door but an unfinished room, and the most commonly cited candidate for a zone that vanilla started and abandoned. Filling it in is the cheapest entry here because the terrain exists and the surrounding lore is settled.

**The Amani thread, from the Hinterlands.** Jintha'alor, the Vilebranch, and the Witherbark are already there, and the forest troll material is the most developed unfinished faction story in the Eastern Kingdoms.

**Uldum and the Caverns of Time, from Tanaris.** Both are later additions in a desert vanilla already established as full of titan and time-related strangeness. Lower priority than the others because neither has a door drawn in the vanilla client, so both would be additions rather than deliveries.

### 13.5 How to add one so it does not die

The inventory is the easy half. The rule from 13.2 is the hard half, and it should be applied deliberately rather than hoped for.

**Give it a non-leveling reason before giving it quests.** A profession material, a faction hub, a market, or a raid entrance. Karazhan is a raid, which solves it immediately. The Emerald Dream would need a material or a reagent that nothing else supplies. Gilneas would need a reason to enter it at sixty.

**Do not build it as a level bracket.** An inward addition borders several brackets at once and should serve all of them unevenly rather than one of them cleanly.

**Wire it into what already exists.** Roads through it under 2.8. A supply relationship under 12.3, so its material shows up in a settlement elsewhere. A seasonal classification under 10.2, which is free and immediately makes it feel like part of the same world rather than an annex.

**Ship it alone.** One zone per major patch, with nothing else competing. This is the advantage Classic+ has over every expansion ever made and it should be used rather than squandered on a batch.

### 13.6 The cost note

New zones are the second case in this document where the tier system misleads, after 12.6.

By reversibility, a new zone is Tier 1. It is the most purely additive thing possible: nothing is removed, nothing is rebalanced, no existing player knowledge is invalidated, and a player who ignores it entirely loses nothing.

By cost, it is Tier 3 and then some. Terrain, art, quests, encounters, itemization, and testing.

Both facts are true and they point in opposite directions. The practical reading is that new zones are safe to add and expensive to add, which is exactly the profile that suits a long slow content cadence and exactly the profile that suits nothing else.

---

## Appendix A: Proposals by Tier

| Proposal | Section | Tier |
|---|---|---|
| NPC idle behavior and work animations | 1.1 to 1.5 | 1 |
| City density with shift and daily routines | 1.6 | 1 |
| Hidden lore NPCs in hard-to-reach locations | 1.7 | 1 |
| Cart and caravan routes | 2 | 2 |
| Observational-only traffic (ships, zeppelin sightlines) | 2.5 | 1 |
| Caravan robbery reputation consequences | 2.6 | 2 |
| Route ruleset inheritance by zone | 2.7 | 1 |
| Trade network stock movement | 3 | 3 |
| Creature pack behavior and stalking | 4.1 | 1 |
| Creature rest and sleep cycles | 4.2 | 1 |
| Concealment vegetation art pass | 4.3 | 1 (art) |
| Species-specific behavior animation | 4.4 | 1 |
| Predator threats to caravans | 4.5 | 2 |
| Creatures reacting to corpses (scavenging) | 4.6 | 2 |
| Middle-tier humanoid camp behavior | 5 | 1 |
| Unscripted faction flare-ups | 6 | 2 |
| Flare-up quest integrity rules | 6.7 | 2 |
| Coin removal from beasts (flavor) | 7.2 | 2 |
| Coin rebalance as income repricing | 7.2 to 7.3 | 3 |
| Swallowed remains and rare story loot | 7.4 to 7.5 | 2 |
| Jewelcrafting | 8.1 | 2 |
| Inscription | 8.2 | 2 |
| Woodcutting | 8.3 | 2 |
| Regional cooking recipes | 8.4 | 2 |
| Trapping | 8.5 | 2 |
| Relic hunting | 8.6 | 2 |
| Cross-tier material requirements | 8.7 | 3 |
| Cross-profession dependencies | 8.8 | 2 |
| Craftable vendor trade goods | 8.9 | 2 |
| Vendor restock economy | 9 | 3 |
| Wagon delivery crediting vendor stock | 9.4 | 3 |
| Wandering profession trainers | 8.10 | 1 |
| Guard hint system for locating trainers | 8.11 | 2 |
| Seasonal calendar by latitude | 10.1 | 3 |
| Full seasonal turn, temperate belt | 10.2 | 3 |
| Muted seasonal pulse, climate statics | 10.2 | 1 |
| Winterspring multi-year thaw event | 10.2 | 2 |
| Felwood localized healing exception | 10.2 | 2 |
| Quilboar as horticulturalists, grown camps | 5 | 1 |
| Responsive Razorfen thorn growth | 5 | 2 |
| Blackrock war readable from surface activity | 6.8 | 2 |
| Steamwheedle cities as supply-dependent (fiction basis for carts) | 3.5 | 3 |
| Stormwind Park district, idle Stonemasons | 1.8 | 1 |
| Westfall supply interdiction | 9.5 | 3 |
| Visible corruption gradient, furbolg and gnoll | 4.7 | 1 |
| Corruption runners on canonical routes | 4.7 | 2 |
| Kobold density predicts ore density | 8.12 | 2 |
| Route funneling through existing chokepoints | 2.8 | 1 |
| Kodo Graveyard permanent scavenger presence | 4.6 | 1 |
| Seasonal year snapped to vanilla holiday calendar | 10.8 | 1 |
| Reagent legibility, behavioral tells for internal anatomy | 7.7 | 2 |
| Naturalist voice across anatomy item flavor text | 7.7 | 1 |
| Anti-Venom loop, poison tuning and sac distribution | 8.13 | 1 |
| Variety-over-fidelity art stance | 12.1 | 1 |
| Settlement differentiation by material, climate, threat, age | 12.2 | 1, high cost |
| Material sourcing made visible on the map | 12.3 | 1 |
| Contestable material sources | 12.3 | 2 |
| Shared architectural grammar per race | 12.4 | 1 |
| Inward zone additions through existing doors | 13.4 | 1 by risk, 3 by cost |
| Non-leveling reason required per new zone | 13.5 | 2 |
| Cyclical world state as the default model | 6.9 | 2 |
| One-way additive events, Lakeshire bridge | 6.9 | 2 |
| Player action with server-wide temporary effect | 6.10 | 2 |
| Conditional threats for outgrown zones | 6.11 | 1 |
| Weather-conditional creature behavior | 4.8 | 1 |
| Weather-conditional spawns | 4.8 | 2 |
| Weather-conditional gathering windows | 10.9 | 1 |
| Quest requirements scaling with seasonal density | 10.5 | 3 |
| Quest text audit for hardcoded numerals | 10.5 | 2, revisionary |
| Seasonal visual pass (cosmetic only) | 10.7 | 1 (art) |
| Per-species herb calendars | 10.3 | 3 |
| Seasonal beast density | 10.4 | 2 |
| Season-scaled gathering quests | 10.5 | 3 |

---

## Appendix B: Lore Accuracy Notes

Several common assumptions do not hold for vanilla specifically, and building on them would produce a design grounded in the wrong era.

**Everlook is a Steamwheedle Cartel city, not a Venture Company holding.** The Steamwheedle cities in Classic are Booty Bay, Ratchet, Gadgetzan, and Everlook [8].

**Highperch in Thousand Needles is a wyvern nesting ground, not a harpy roost.** Young Freewind Post tauren cull eggs there for Horde mounts. The zone's harpies are the Roguefeather [15].

**The Thousand Needles centaur are the Galak clan.** The Kolkar are the Barrens and Desolace clan. The five centaur clans are Kolkar, Magram, Gelkis, Maraudine, and Galak [11][15][16].

**Scarlet Crusade presence in Silverpine Forest is a much later addition.** Vanilla Silverpine's antagonists are the Dalaran wizards at Ambermill, the Rot Hide gnolls on Fenris Isle under Thule Ravenclaw, the Pyrewood worgen, and Alliance forces out of Southshore [14]. Scarlet Crusade anchors belong in Tirisfal and the Plaguelands.

**Stonetalon Mountains settlements in vanilla are Sun Rock Retreat (Horde tauren), Stonetalon Peak (Alliance night elf), and Malaka'jin (Darkspear trolls).** Krom'gar Fortress, Malfurion's Breach, and Talon Watch are Cataclysm-era and do not exist in Classic [9].

**Marshal's Refuge is in Un'goro Crater.** The neutral goblin presence in the Thousand Needles region is the Mirage Raceway on the Shimmering Flats [15].

**Vanilla pirate coves.** The Bloodsail operate along the Stranglethorn coast. The Southsea Freebooters hold Lost Rigger Cove in Tanaris, east of the Caverns of Time [8]. Thousand Needles is a dry canyon and salt flat with no coastline.

**The Razorfen grew from Agamaggan's blood, not his quills.** A common paraphrase has the thorns growing from the fallen boar's spines directly. The vanilla dungeon text and the lore both say his blood fell and thorn-ridden vines rose from the ground where it landed [27][28]. The distinction matters for the quilboar proposal in Section 5: the Razorfen is not a carcass the quilboar live inside, it is what the soil did afterward, which is why tending rather than building is the right read.

**Winterspring has canonically thawed.** Warcraft III placed the valley in a rare snowless spring or summer during Reign of Chaos, which is why 10.2 proposes a multi-year thaw event there rather than treating perpetual snow as absolute [23]. This is the strongest existing-lore hook in Section 10.

**Moonglade's stasis is explicit and it is pleasant.** The lore states the land never suffers extremes of weather and holds in a warm endless summer evening under a permanent high moon [24]. 10.2 treats this as arrest into life, the inverse of the Plaguelands, rather than as an ordinary static zone.

**Felwood was northern Ashenvale before its corruption** by Tichondrius and the Skull of Gul'dan during the Third War [25]. That shared origin is what makes the Ashenvale border the sharpest seasonal contrast available, and the Emerald Sanctuary with Greta Mosshoof is vanilla, which is what licenses the localized healing exception in 10.2.

**Desolace was Mashan'she, a fertile grassland, until the tauren shaman woke Princess Theradras**, who consumed the land's energies to regenerate herself and remains beneath the zone in Maraudon [26]. This makes Desolace an active drain rather than residue. Separately, the Cenarion Wildlands regrowth in central Desolace is a Cataclysm change and has no place in a Classic-era proposal.

**Caryssia Moonhunter is at Thalanaar in eastern Feralas, not in Thousand Needles.** Multiple profession guides place her on the edge of Thousand Needles, which is understandable because Thalanaar sits directly on the border and the Thousand Needles road terminates there, but the moonwell she stands beside is in Feralas [22]. Relevant to 8.10, since the whole point of that proposal is that these trainers are placed in specific remote spots rather than in cities.

---

## Appendix C: Visual Reference Index

For the inward additions in 13.4, ChromedDragon's Classic zone mockups are the most useful visual reference available for what several of these would look like built to vanilla's art standard rather than a later one: https://imgur.com/a/chromeddragons-classic-wow-zones-tvpk9SS

Direct links per named location, for screenshots, zone maps, and terrain reference. Where a Classic-specific page exists, use it: Stonetalon, Thousand Needles, Desolace, and Silverpine were all geographically rebuilt in Cataclysm, and the modern pages show terrain that does not exist in vanilla.

These follow the standard Wowpedia URL pattern. A few may redirect to a merged or renamed page.

**Better tool for route and density work.** Wowhead's Classic zone pages carry interactive maps with NPC and resource-node overlays, which is more useful than static screenshots for anything in Sections 2, 3, and 6. Base path: https://www.wowhead.com/classic/zone=

### Section 1: Ambient life

- Tranquil Gardens Cemetery: https://wowpedia.fandom.com/wiki/Tranquil_Gardens_Cemetery
- Raven Hill Cemetery: https://wowpedia.fandom.com/wiki/Raven_Hill_Cemetery
- The Rotting Orchard: https://wowpedia.fandom.com/wiki/The_Rotting_Orchard
- Darkshire: https://wowpedia.fandom.com/wiki/Darkshire
- Booty Bay: https://wowpedia.fandom.com/wiki/Booty_Bay
- Windshear Crag: https://wowpedia.fandom.com/wiki/Windshear_Crag
- Stonewrought Dam: https://wowpedia.fandom.com/wiki/Stonewrought_Dam
- Gol'Bolar Quarry: https://wowpedia.fandom.com/wiki/Gol%27Bolar_Quarry
- Valley of Strength: https://wowpedia.fandom.com/wiki/Valley_of_Strength
- Ring of Valor: https://wowpedia.fandom.com/wiki/Ring_of_Valor
- Marshal's Refuge: https://wowpedia.fandom.com/wiki/Marshal%27s_Refuge

### Sections 2 and 3: Routes and trade

- The Gold Road: https://wowpedia.fandom.com/wiki/Gold_Road
- The Crossroads: https://wowpedia.fandom.com/wiki/The_Crossroads
- Camp Taurajo: https://wowpedia.fandom.com/wiki/Camp_Taurajo
- Ratchet: https://wowpedia.fandom.com/wiki/Ratchet
- Northwatch Hold: https://wowpedia.fandom.com/wiki/Northwatch_Hold
- Talondeep Path: https://wowpedia.fandom.com/wiki/Talondeep_Path
- Gadgetzan: https://wowpedia.fandom.com/wiki/Gadgetzan
- Everlook: https://wowpedia.fandom.com/wiki/Everlook
- Shimmering Flats: https://wowpedia.fandom.com/wiki/Shimmering_Flats
- Mirage Raceway: https://wowpedia.fandom.com/wiki/Mirage_Raceway
- Dun Algaz: https://wowpedia.fandom.com/wiki/Dun_Algaz
- Menethil Harbor: https://wowpedia.fandom.com/wiki/Menethil_Harbor
- Dun Modr: https://wowpedia.fandom.com/wiki/Dun_Modr
- Thandol Span: https://wowpedia.fandom.com/wiki/Thandol_Span
- Grim Batol: https://wowpedia.fandom.com/wiki/Grim_Batol
- Thelsamar: https://wowpedia.fandom.com/wiki/Thelsamar
- Lakeshire: https://wowpedia.fandom.com/wiki/Lakeshire
- The Sepulcher: https://wowpedia.fandom.com/wiki/The_Sepulcher
- Southshore: https://wowpedia.fandom.com/wiki/Southshore
- Tarren Mill: https://wowpedia.fandom.com/wiki/Tarren_Mill
- Lost Rigger Cove: https://wowpedia.fandom.com/wiki/Lost_Rigger_Cove

### Sections 4 through 6: Ecology and emergent conflict

- Un'goro Crater (Classic): https://wowpedia.fandom.com/wiki/Un%27Goro_Crater
- The Charred Vale: https://wowpedia.fandom.com/wiki/The_Charred_Vale
- Mirkfallon Lake: https://wowpedia.fandom.com/wiki/Mirkfallon_Lake
- Sentinel Hill: https://wowpedia.fandom.com/wiki/Sentinel_Hill
- Moonbrook: https://wowpedia.fandom.com/wiki/Moonbrook
- Jangolode Mine: https://wowpedia.fandom.com/wiki/Jangolode_Mine
- Gold Coast Quarry: https://wowpedia.fandom.com/wiki/Gold_Coast_Quarry
- The Dagger Hills: https://wowpedia.fandom.com/wiki/The_Dagger_Hills
- Klaven's Tower: https://wowpedia.fandom.com/wiki/Klaven%27s_Tower
- Mo'grosh Stronghold: https://wowpedia.fandom.com/wiki/Mo%27grosh_Stronghold
- Freewind Post: https://wowpedia.fandom.com/wiki/Freewind_Post
- Highperch: https://wowpedia.fandom.com/wiki/Highperch
- Darkcloud Pinnacle: https://wowpedia.fandom.com/wiki/Darkcloud_Pinnacle
- Whitereach Post: https://wowpedia.fandom.com/wiki/Whitereach_Post
- Magram Village: https://wowpedia.fandom.com/wiki/Magram_Village
- Gelkis Village: https://wowpedia.fandom.com/wiki/Gelkis_Village
- Kolkar Village: https://wowpedia.fandom.com/wiki/Kolkar_Village
- Fenris Isle: https://wowpedia.fandom.com/wiki/Fenris_Isle
- Ambermill: https://wowpedia.fandom.com/wiki/Ambermill
- Pyrewood Village: https://wowpedia.fandom.com/wiki/Pyrewood_Village

### Section 8: Professions and wandering trainers

- Thalanaar: https://wowpedia.fandom.com/wiki/Thalanaar
- Tanner Camp: https://wowpedia.fandom.com/wiki/Tanner_Camp
- Ruins of Eldarath: https://wowpedia.fandom.com/wiki/Ruins_of_Eldarath
- Stromgarde Keep: https://wowpedia.fandom.com/wiki/Stromgarde_Keep
- Grom'gol Base Camp: https://wowpedia.fandom.com/wiki/Grom%27gol_Base_Camp
- Lethlor Ravine: https://wowpedia.fandom.com/wiki/Lethlor_Ravine

### Zone-level maps

- Stonetalon Mountains (Classic): https://wowpedia.fandom.com/wiki/Stonetalon_Mountains_(Classic)
- Thousand Needles (Classic): https://wowpedia.fandom.com/wiki/Thousand_Needles_(Classic)
- Silverpine Forest (Classic): https://wowpedia.fandom.com/wiki/Silverpine_Forest_(Classic)
- Westfall (Classic): https://wowpedia.fandom.com/wiki/Westfall_(Classic)
- Barrens (Classic): https://wowpedia.fandom.com/wiki/Barrens_(Classic)
- Wetlands (Classic): https://wowpedia.fandom.com/wiki/Wetlands_(Classic)
- Desolace: https://wowpedia.fandom.com/wiki/Desolace
- Duskwood: https://wowpedia.fandom.com/wiki/Duskwood
- Loch Modan: https://wowpedia.fandom.com/wiki/Loch_Modan

---

## Sources

[1] "Will WoW Classic+ Be Announced at BlizzCon 2026? What's Confirmed vs Rumored," timesaver.gg, July 2026. https://timesaver.gg/blog/will-wow-classic-plus-blizzcon-2026

[2] "Rumor: Blizzard is quietly testing WoW Classic Plus with influencers," Massively Overpowered, May 4, 2026. https://massivelyop.com/2026/05/04/rumor-blizzard-is-quietly-testing-wow-classic-plus-with-influencers/

[3] "Speculation Grows About WoW Classic's Rumored Next Phase," MMORPG.com, May 6, 2026. https://www.mmorpg.com/news/speculation-grows-about-wow-classics-rumored-next-phase-2000137992

[4] "Blizzard's Mystery Classic Creator Visits Have the Classic+ Rumor Mill Screaming Again," Master of Warcraft, May 11, 2026. https://www.masterofwarcraft.net/2026/05/blizzard-classic-creator-visits-classic-plus-rumors.html

[5] "Everything We Know About World Of Warcraft's Rumored Classic+," Kotaku, July 2026. https://kotaku.com/everything-we-know-about-world-of-warcrafts-rumored-classic-2000711801

[6] "Is World of Warcraft Classic Plus Coming in 2026? Latest Rumors," In Game News, May 12, 2026. https://www.ingamenews.com/2026/05/is-world-of-warcraft-classic-plus.html

[7] "Tranquil Gardens Cemetery," Wowpedia. https://wowpedia.fandom.com/wiki/Tranquil_Gardens_Cemetery

[8] "Steamwheedle Cartel," Warcraft Wiki and WoWWiki. https://warcraft.wiki.gg/wiki/Steamwheedle_Cartel and https://wowwiki-archive.fandom.com/wiki/Steamwheedle_Cartel

[9] "Stonetalon Mountains (Classic)," Wowpedia. https://wowpedia.fandom.com/wiki/Stonetalon_Mountains_(Classic)

[10] "Loch Modan storyline," Wowpedia, and Loch Modan quest walkthroughs. https://wowpedia.fandom.com/wiki/Loch_Modan_storyline

[11] "Barrens (Classic)," Wowpedia, and "The Barrens questing guide/Northern Barrens," Warcraft Wiki. https://wowpedia.fandom.com/wiki/Barrens_(Classic)

[12] "Westfall (Classic)," Wowpedia. https://wowpedia.fandom.com/wiki/Westfall_(Classic)

[13] "Loch Modan," Wowpedia, and "Wetlands (Classic)," Wowpedia. https://wowpedia.fandom.com/wiki/Loch_Modan and https://wowpedia.fandom.com/wiki/Wetlands_(Classic)

[14] "Silverpine Forest (Classic)," Wowpedia. https://wowpedia.fandom.com/wiki/Silverpine_Forest_(Classic)

[15] "Thousand Needles (Classic)," Wowpedia, and "Freewind Post," Wowpedia. https://wowpedia.fandom.com/wiki/Thousand_Needles_(Classic) and https://wowpedia.fandom.com/wiki/Freewind_Post

[16] "Magram clan," Wowpedia. https://wowpedia.fandom.com/wiki/Magram_clan

[17] "Gelkis clan," Wowpedia. https://wowpedia.fandom.com/wiki/Gelkis_clan

[18] "Magram Alliance," Wowhead Classic quest database. https://www.wowhead.com/classic/quest=1367/magram-alliance

[19] "Fresh Classic+ Info," MMO-Champion forum thread (leaked feature list, unverified). https://www.mmo-champion.com/threads/2668747-Fresh-Classic-Info

[20] "Vanilla Jewelcrafting Leveling Guide 1-300," WoW-Professions. https://www.wow-professions.com/guides/vanilla-jewelcrafting-leveling

[21] Steamwheedle Cartel reputation turn-in requirements, community reputation guides. https://enviitheinsane.wordpress.com/insane-in-the-membrane/steamwheedle-cartel/

[22] "Leatherworking specialization," Wowpedia, and "WoW Classic Leatherworking Guide 1-300," Warcraft Tavern. https://wowpedia.fandom.com/wiki/Leatherworking_specialization and https://www.warcrafttavern.com/wow-classic/guides/leatherworking-1-300/

[23] "Winterspring (Classic)," Warcraft Wiki. https://warcraft.wiki.gg/wiki/Winterspring_(Classic)

[24] "Moonglade," Wowpedia. https://wowpedia.fandom.com/wiki/Moonglade

[25] "Felwood," Wowpedia. https://wowpedia.fandom.com/wiki/Felwood

[26] "Desolace," Wowpedia. https://wowpedia.fandom.com/wiki/Desolace

[27] "Agamaggan," Wowpedia. https://wowpedia.fandom.com/wiki/Agamaggan

[28] "Razorfen Kraul (Classic)," Warcraft Wiki. https://warcraft.wiki.gg/wiki/Razorfen_Kraul_(Classic)

[29] "Blackrock Mountain," Wowpedia. https://wowpedia.fandom.com/wiki/Blackrock_Mountain

[30] "Know Your Lore: The Dark Iron Dwarves of Blackrock Mountain," Blizzard Watch. https://blizzardwatch.com/2017/12/22/know-lore-dark-iron-dwarves-blackrock-mountain/

[31] "Stonemasons Guild," Wowpedia. https://wowpedia.fandom.com/wiki/Stonemasons_Guild

[32] "Defias Brotherhood," Wowpedia. https://wowpedia.fandom.com/wiki/Defias_Brotherhood

[33] "House of Nobles," Wowpedia. https://wowpedia.fandom.com/wiki/House_of_Nobles

[34] "Falling to Corruption (Classic)," Wowpedia. https://wowpedia.fandom.com/wiki/Falling_to_Corruption_(Classic)

[35] "Timbermaw Hold (faction)," Wowpedia. https://wowpedia.fandom.com/wiki/Timbermaw_Hold_(faction)

[36] "Small Venom Sac," Warcraft Wiki. https://warcraft.wiki.gg/wiki/Small_Venom_Sac

[37] "Empty Venom Sac," Wowpedia. https://wowpedia.fandom.com/wiki/Empty_Venom_Sac

[38] "Warsong Gulch," Wowpedia. https://wowpedia.fandom.com/wiki/Warsong_Gulch

[39] "Ashenvale (Classic)," Warcraft Wiki. https://warcraft.wiki.gg/wiki/Ashenvale_(Classic)

[40] "WoW players want one classic zone to get a complete rework," Dot Esports, on Deadwind Pass and Karazhan's vanilla cut. https://dotesports.com/wow/news/wow-players-want-one-classic-zone-to-get-a-complete-rework-in-season-of-discovery

[41] "Dragons of Nightmare (Classic)," Wowpedia. https://wowpedia.fandom.com/wiki/Dragons_of_Nightmare_(Classic)

[42] "Dragons of Nightmare Raid Guides," Icy Veins. https://www.icy-veins.com/wow-classic/dragons-of-nightmare-raid-guides

[43] Allarielle, "Using phasing tech so zones can level with you," MMO-Champion, July 2026. The origin of the Lakeshire bridge, conditional-threat, and Stonewatch Keep proposals in 6.9 to 6.11, though this document rejects the phasing delivery mechanism it proposes. https://www.mmo-champion.com/threads/2669079-Using-phasing-tech-so-zones-can-level-with-you

[44] "Mooncloth," Wowpedia. https://wowpedia.fandom.com/wiki/Mooncloth

[45] "Mooncloth," Vanilla WoW Wiki. https://vanilla-wow-archive.fandom.com/wiki/Mooncloth

---

*Sources [1] through [6] are community reporting on unconfirmed rumors and should be treated as such. Source [19] is an unverified leak. Sources [7] through [18] and [20] through [22] are lore and game-data references used to ground design proposals in existing vanilla content.*

---

## Appendix D: Provenance

Added retroactively. Labels as defined in `classic-plus-talent-design.md`.

| Label | Meaning |
|---|---|
| **Taken** | Lifted essentially whole from a named source. |
| **Adapted** | The mechanism is someone else's, changed to fit vanilla's constraints. |
| **Inspired by** | The principle is someone else's, the implementation here is different. |
| **Vanilla precedent** | Already exists somewhere in vanilla. This document systematizes it. |
| **Brendan** | Specified by the author in conversation, not derived from a source. |
| **Derived here** | Follows from analysis performed in this project. |
| **Original** | No known source. Treat with the least confidence. |

Almost everything in this document is one of two things: an idea Brendan raised in conversation, or a piece of vanilla lore the world already asserts and does not show. That second category is the document's whole method, so **Vanilla precedent** is the default and the interesting entries are the ones that are not.

| Element | Provenance | Detail |
|---|---|---|
| The core method: find what vanilla lore already asserts and make the world show it | **Brendan** | The organising principle, raised in conversation before any section existed. |
| Ambient NPC behavior, trade routes, wildlife ecology, middle-tier humanoids, loot logic, professions, vendor economy | **Brendan** | Raised and developed in conversation. The document contributes grounding in named locations and the tier sorting. |
| Every named location, faction, and NPC anchor | **Vanilla precedent** | Verified against wikis. Appendix B records where common assumptions turned out to belong to later expansions. |
| Three implementation tiers | **Brendan** | Cost as a first-class design input. Now shared vocabulary across the whole suite. |
| Seasons as a world system | **Brendan** | |
| Growing season marching by latitude rather than two hemispheres flipping | **Derived here** | Brendan proposed offset hemispheres on the Earth model. Azeroth's warm band sits south on both continents, so latitude works without special-casing. Brendan accepted the revision. |
| Nothing disappears, it migrates | **Brendan** | Load-bearing for the whole seasonal economy. |
| Arrested zones reading as wounded because they do not turn | **Derived here** | Falls out of the seasonal system once zones that do not cycle need an explanation. |
| Quests scaling to seasonal density | **Brendan** | Raised immediately on hearing that wildlife density would move. |
| Weather changes what is available, not what you are capable of | **Brendan** | |
| The cooldown-is-planning, weather-is-waiting distinction | **Derived here** | The reason weather may gate a bonus but never a prerequisite. |
| World-indexed versus player-indexed change | **Derived here** | Design constraint six. |
| Seasonal year snapped to the vanilla holiday calendar | **Vanilla precedent** | The Lunar Festival is already held in the one zone that never has winter. Nobody had to write it. |
| The seasonal visual pass as a separable Tier 1 subset | **Derived here** | Follows from the tier logic. Later found to be the highest-reach node in the proposals graph, which makes a cosmetic job structurally critical. |
| Variety-over-fidelity art stance | **Brendan** | |
| Material sourcing made visible on the map | **Derived here** | When a zone's poverty is the point, the source must be external. |
| Inward zone additions through existing vanilla doors | **Brendan** | |
| World-state architecture: cyclical, permanent, phasing | **Derived here** | Needed once several systems all wanted to change the world and had to be told apart. |
