# Claude Design Brief: A Living Azeroth

Paste everything below the line into Claude Design. Attach `classic-plus-living-world-design.md` and `proposals.json` alongside it.

---

## What I'm building

A single-page web document for a WoW Classic+ design proposal called **A Living Azeroth**. It's about 27,000 words of systems design across fourteen sections and 105 subsections, covering NPC behavior, trade routes, wildlife ecology, loot logic, professions, economy, seasons, world-state architecture, art direction, and how to add zones to a shipped game. Every proposal is anchored to named vanilla Azeroth locations and factions, and there are 45 cited sources.

There is also a companion document, **Class Absorption**, arguing that post-vanilla classes should be absorbed as talent trees rather than shipped as classes. It builds eight complete trees, seven rows each, roughly 170 talents.

Four attachments: both documents as markdown, `proposals.json` (74 world proposals), and `trees.json` (7 trees with full talent tables).

**These are two documents on one site, not two sites.** The join is real and it is the reason to build them together: every tree is acquired through a quest chain running through named vanilla locations, so `trees.json` carries a `worldAnchors` field that joins directly to the `zones` field in `proposals.json`. One document describes the world. The other describes something you go into that world to get.

**The page's job:** make a long, dense design document navigable and credible enough that a stranger takes it seriously as design work rather than as fan speculation.

**Audience:** WoW players who follow Classic development closely, plus anyone who reads game design writing. They are skeptical by default and allergic to fan-site aesthetics.

## The thing that makes this page worth building

`proposals.json` sorts all 74 proposals on **five independent axes**, and no two of them agree. That disagreement is the whole content of the page. A reader who only sees the document reads it linearly and never notices; a reader who can pivot the dataset sees the argument immediately.

The five axes, all present as fields:

1. **`tier`** (1, 2, 3). Architectural risk and reversibility.
2. **`cost`** (low, medium, high). Art and engineering hours. **Deliberately not the same as tier.** Two proposals are Tier 1 by risk and Tier 3 by cost, and the document calls both out as places where the tier system misleads.
3. **`deployment`** (live, ptr, fresh). Where it can ship on a running game. 9 could ship to live realms tomorrow. 47 need a PTR. 18 need a fresh realm.
4. **`layer`** (1 to 4). Dependency ordering. The world in motion, reacting, circulating, on a clock.
5. **`change`** (additive, revisionary). Whether it invalidates knowledge players already have. 50 additive, 24 revisionary.

**Design implication, and please hold this line:** only ONE axis gets color. Tier owns color. Deployment owns grouping and position. Layer owns a dedicated view. Change type owns a single glyph. Three competing color scales on one page would be unreadable.

## Art direction

The subject's real vernacular is not swords and dragons. It's **survey work and freight**: trade routes, cargo manifests, supply ledgers, field observation notes, tier classifications. The whole document is a naturalist's field survey crossed with a logistics plan. Design from that, not from fantasy.

No parchment textures. No blackletter. No dragons. No Warcraft logo pastiche.

### Palette

- `#F0F2EC` pale drafting green, light ground
- `#0F1418` deep ink blue-black, dark ground
- `#1C2419` ink, primary text on light
- `#D6DDD4` text on dark ground
- `#1F3A5F` route blue, links and the interlock lines
- Tier scale, semantic, used consistently everywhere a tier appears:
  - Tier 1 `#4A6B62` slate green, low risk, patchable
  - Tier 2 `#9A7B3F` brass, medium, needs engineering
  - Tier 3 `#8C4A38` oxidized copper, architectural, launch-only

Support both light and dark.

### Type

Three roles, three families. A humanist serif for body at generous measure, a grotesque for UI and labels, and a mono for tier tags, IDs, and anything from the dataset. The mono is doing real work here: it signals that the structured data is data.

## Components

### 1. Header
Title, subtitle, version 1.2, and three counts that establish scale immediately: 74 proposals, 14 sections, 45 sources. Restrained.

### 2. The thesis, above everything
Two or three sentences pulled from Section 0, set larger than body. The method statement is the key line: find something vanilla already asserts, then make the world show it. A reader who bounces should still take that away.

### 3. Deployment view, and I want this first among the interactive pieces
Three columns: **Ships to live realms** (9), **Needs a PTR** (47), **Fresh realm** (18).

This is the most useful view in the dataset because it answers the reader's real question, which is whether any of this could actually happen. Nine things could go into the next patch. Lead with that.

Within the PTR column, subgroup by `ptrReason`: load, exploit, stale-knowledge, taste. Four different reasons needing four different test plans is a detail that signals the document thought about implementation rather than just ideas.

### 4. Layer view
Four columns, 1 through 4, as a roadmap. Ordering is by dependency, not cost, and the page should say so: each layer is what makes the next one legible. Material chains don't parse if every settlement still looks alike. Seasons don't land without ambient life to react to them.

### 5. Proposal browser
All 74, filterable on every axis, searchable. Each card: title, section reference, tier chip in tier color, cost, deployment badge, layer, zones, systems, and the `note` field. The notes are written to be read, so give them room rather than truncating them.

Revisionary proposals get a small glyph and a tooltip. Additive is the unmarked default, which is correct because additive is the safe case.

### 6. The interlock diagram
The `dependsOn` and `enables` fields form a real graph. Cart routes enable four things. Seasonal calendar enables four. The scavenging system needs pack behavior first.

This is the single strongest credibility signal on the page, because it demonstrates that the proposals are a system rather than a wish list. Keep it legible over pretty: a directed graph with route blue edges, nodes colored by tier. Clicking a node should filter the browser.

### 7. Zone index
The 74 proposals touch roughly 50 named zones. A reader who cares about one zone should be able to click Westfall and see everything that touches it.

If you want one showpiece: the seasonal classification from 10.2 covers every zone on both continents sorted into full turn, muted pulse, or arrest, with arrest subdivided into residue, active, and held. That's a complete map of Azeroth by how much it responds to the year, and it's a genuinely novel artifact. A schematic map or a sorted grid both work. Do not attempt a literal world map.

### 8. Section navigation
Sticky, fourteen sections. Deep-linkable.

### 9. Appendix B, the lore notes
Do not bury these. It's a list of places the document verified vanilla lore and corrected common errors, including one about Agamaggan's blood rather than his quills, and one about a trainer's location that several guides get wrong. For a skeptical audience this is the section that proves the work is real. Give it a proper treatment rather than a footer.

## The class document's components

The class doc does not fit the five-axis model, and forcing it in would be wrong. Almost every tree is Tier 3, fresh realm, revisionary, so those filters collapse to a single value and become useless. It needs its own treatment.

### 10. The eight trees
The centerpiece. Each tree renders as an actual seven-row talent tree, because that is what it is and no other presentation will read as credible to this audience.

Per tree: name, host class, concept line, local mechanic, acquisition verb, profession gate, and the row-by-row talents with rank counts and point requirements. Row 5 (the mark) and row 7 (the capstone) need visual emphasis, because the two-signature structure is the document's central mechanical claim.

Show the available-points figure per tree. Rows one through six carry 57 to 64 points against the 30 needed to reach the capstone, and that slack is the argument that these behave like vanilla trees rather than modern ones.

### 11. The weapon fork
Bladedancer alone forks three abilities on equipped weapon. A small toggle between "bladed" and "fist or unarmed" that live-updates those three rows is the single most demonstrable idea in either document, and it takes one control.

### 12. Acquisition verbs
Seven verbs across eight trees: forged, taught, taken, fallen, earned, granted, copied, remembered. Present them as a set, since the whole point is that no two chains are structurally alike.

Three trees have no route specified yet. **Show that as an open item rather than hiding it.** A document that marks its own gaps reads as work in progress by someone honest, which is the correct impression.

### 13. The join view, and this is what makes the site worth building
Any zone appearing in both datasets should surface both. Clicking **Ashenvale** shows the world proposals that touch it and the fact that the Metamorphosis chain ends at Demon Fall Ridge. Clicking **Searing Gorge** shows the arrested-zone classification, the Blackrock surface war, and the forge where a runeblade gets made.

The overlap is currently modest: Western and Eastern Plaguelands, Redridge, the Barrens, Ashenvale, Searing Gorge, and the Burning Steppes. Modest is fine. It is the seam, and showing it is the argument that these are one design rather than two hobbies.

## Tone and constraints

- No em dashes anywhere in generated copy. The source document has zero and that's deliberate.
- Don't invent proposals, zones, or numbers. Everything comes from the attachments.
- The document is a proposal, not a prediction. Section 0 is explicit that Classic+ is unannounced, and the page must not imply otherwise anywhere.
- Long-form reading is the primary use. Interactive views support the document; they don't replace it.
- Mobile has to work. The three-column views collapse to stacked sections with the filter set persisting.
- The two documents share a spine and should share navigation, a palette, and the tier vocabulary. They should not share a filter bar, because their axes genuinely differ.
- The class document is more contentious than the world document. Its page should lead with the Metamorphosis precedent, which is a verifiable fact rather than an opinion, before it shows a single talent.
