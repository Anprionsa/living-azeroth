# A Living Azeroth — Design System

Design system for **A Living Azeroth**, a single-page web document presenting roughly 8,000 words
of systems design for WoW Classic+: NPC behavior, trade routes, wildlife ecology, loot logic,
professions, and economy, all anchored to named vanilla Azeroth locations and factions.

The page's job is to make a long, dense design document navigable and credible enough that a
stranger takes it seriously as design work rather than as fan speculation. The audience is WoW
players who follow Classic development closely, plus anyone who reads game design writing.

There is one product and one surface: the document itself.

## Sources given

Three files, supplied in a mounted read-only folder. Copies live in `assets/`:

- `claude-design-brief.md` — the original brief. `assets/source/claude-design-brief.md`.
- `art-direction-revision.md` — the revision that replaced the art direction. Structure,
  components, and interactive views were kept; the visual register was rebuilt.
  `assets/source/art-direction-revision.md`.
- `classic-plus-living-world-design.md` — the full 649-line document: 10 sections, 3 appendices,
  21 numbered sources. `assets/source/classic-plus-living-world-design.md`.
- `proposals.json` — 28 proposals with `tier`, `zones`, `factions`, `systems`, `dependsOn`,
  `enables`, `cost`, and `note`. `assets/data/proposals.json`. **This file is the source of the
  interlock tree.** The graph is derived from it at render time.

No Figma file, no repository, no logo, no imagery, and no font binaries were supplied.

## The register

The system cites vanilla World of Warcraft and earlier, precisely, rather than reaching for
generic fantasy. Two source bodies, used for different parts:

- **The Warcraft II manual and early Warcraft print material** for long prose. Those were framed
  as in-world chronicles, set as ink on paper, not as game UI. That is the right model for 8,000
  words of reading, and it is genuinely pre-vanilla.
- **The vanilla WoW client UI** for data and interactive components: quest log, item tooltip,
  talent tree. Precise, recognisable, and they carry structural logic that maps onto what the
  components already do.

Prose reads like a chronicle. Data reads like the client.

---

## Content fundamentals

**Register.** Plain, direct, specific. Someone writing a spec, not selling one. Sentences make a
claim and support it with a named place, faction, or source.

**No marketing voice.** No superlatives, no "delightful", no "seamless", no calls to action.
Compare: "The load-bearing feature of the whole document" (a structural claim, defensible) against
"Our most exciting proposal yet" (a mood).

**No exclamation points. No em dashes.** The source document uses neither, and neither does any
copy written for this system. Where an em dash would go, use a comma, a colon, or a full stop.

**Person.** Third person and impersonal by default: "This document assumes nothing about what
Blizzard is actually building." Second person only for what a player experiences: "If you are
nearby, you see it." No first person, singular or plural.

**Hedging is explicit, not weaselly.** When something is unconfirmed the copy says so and cites
the reporting: "Everything else is community inference built on a real but ambiguous evidence
base [2][3][4]."

**Casing.** Sentence case for headings and UI labels. Uppercase only for interface eyebrows and
data labels, always with wide tracking ("DEPENDS ON", "SECTION 2.3"). Title Case is not used.
Game proper nouns are spelled exactly as the game spells them: Un'goro Crater, Kolkar, Windshear
Crag, Steamwheedle Cartel.

**Numbers.** Section numbers are real cross-references and always appear as the document numbers
them ("4.5", "7.2 to 7.3", "8 / 1"). Never invent `01 / 02 / 03` decoration. Tiers are written
"Tier 1", or "T1" where space is tight.

**UI labels say what they do.** "Clear filters", "Copy view link", "Collapse all".

**Empty states point at the control that fixes them.** "No proposals match these filters. Remove
a tier or system filter, or clear the search field." Never "Oops", never "Sorry".

**Emoji are not used.** Anywhere.

**Terminology to keep exact:** proposal, tier, zone, system, faction, cost, node and tree (the
diagram), interlock (the relationship between proposals). "Classic+" always with the plus and in
quotation marks on first use, because it is not an announced product.

**Required legal line**, verbatim, on any published page: "Unofficial fan work. Not affiliated
with or endorsed by Blizzard Entertainment."

---

## Visual foundations

### Colour

From the client, not invented. Full token list in `tokens/colors.css`.

| Role | Token | Value |
|---|---|---|
| Quest log parchment, reading ground | `--parchment` | `#F0E6D2` |
| Sunk parchment | `--parchment-sunk` | `#E4D7BE` |
| UI stone panel, data ground | `--stone` | `#2B2721` |
| Raised stone | `--stone-raised` | `#40382C` |
| Ink on parchment | `--ink` | `#1C1710` |
| Text on stone | `--ink-inverse` | `#E8DCC4` |
| Interface gold | `--gold`, `--gold-dim`, `--gold-deep` | `#FFD100`, `#C79C6E`, `#8A6A2E` |

**Tiers are item quality colours**, which every player reads as escalating significance without
being told. These are the exact values the client returns:

- Tier 1, uncommon green `#1eff00` — the common upgrade you see constantly. Patchable anytime.
- Tier 2, rare blue `#0070dd` — real effort. Post-launch, but planned.
- Tier 3, epic purple `#a335ee` — the thing you plan around. Launch decision.
- Legendary orange `#ff8000` is reserved and currently unassigned. Do not spend it.

The client values are tuned for a dark UI and fail contrast on parchment, so the light ground uses
darkened equivalents (`--quality-uncommon-on-light` `#2C7A10`, `--quality-rare-on-light` `#02549F`,
`--quality-epic-on-light` `#7A2BB4`). Same ladder, same meaning. Anything on the stone panel, which
means every tooltip and the talent tree, keeps the exact values. `--tier-1/2/3` resolve to whichever
is correct for the current ground, so components never choose.

Interface gold is the only accent. Cost is three weights of ink, not a second colour scale.

### Type

Three roles. Vanilla ships `MORPHEUS.TTF` for quest titles and book text and `FRIZQT__.TTF`
(Friz Quadrata) for the entire interface; `SKURRI.TTF` is combat damage numbers and is not useful
here.

- **Display: Morpheus**, substituted by **Grenze Gotisch**. Section headings, the wordmark, view
  titles. Display only, never body, never blackletter for reading.
- **Interface: Friz Quadrata**, substituted by **Marcellus**. Item names, tooltips, panel labels,
  tier badges, table headers, the TOC, the footer. If a piece of text is a value rather than a
  sentence, it is set in this face.
- **Body: Source Serif 4**, 18px / 1.62, measure 68 characters. Friz Quadrata is a UI face and
  gets tiring across 8,000 words. That split is true to the source: the manuals were not set in
  the interface font either.

Section numbers set in the interface face sit as an eyebrow above each heading, uppercase, tracked
to `0.12em`. They are functional cross-references.

### Space and layout

A named step scale from 2 to 128 (`tokens/spacing.css`). Section gap 96, paragraph gap 20, heading
to body 16. Desktop is a 264px sidebar rail plus a fluid body column at a 68-character measure.
The talent tree is the only element allowed a panel of its own. The rail becomes an off-canvas
sheet under 900px.

### Backgrounds, texture, imagery

Flat panel colour only. **No aged or stained parchment texture overlay**, no paper grain, no
noise, no gradients. Texture is the specific tell that separates a fan site from a design
document. No hero image and no full-bleed imagery: none was supplied, and game screenshots and
Blizzard art are out of bounds. The only drawing in the system is the talent tree.

### Borders, corners, elevation

Hairlines and flat 1px panel edges carry all structure: `#E2D5B8` faint, `#D2C09C` standard,
`#B49E74` strong, and `--gold-dim` `#C79C6E` for panel and tooltip edges. Corners are 0 to 3px.
Nothing is pill-shaped except the quality dot.

**No bevel, no emboss, no 3D chrome, no glow.** Vanilla's panel edges are flat and thin, and the
beveled-metal look belongs to Warcraft III and retail. There is one shadow token,
`--shadow-sheet`, used only by the mobile contents sheet.

### Transparency and blur

Blur is not used. Transparency appears in three places: quality washes at 10 to 16% behind badges,
the gold wash at 10 to 16% for row hover and pressed chips, and 12 to 30% opacity used to dim
non-neighbour nodes and edges when a tree node is focused. Dimming, not hiding.

### Motion

The tree's cargo arrows draw in once over 1400ms with `cubic-bezier(.16,1,.3,1)`, staggered by
tier. Dashed "makes possible" arrows do not animate. Filters, hovers, and row expansion transition
over 140 to 220ms. Nothing else moves: no parallax, no reveal-on-scroll, no bounce, no scale-in.
Every duration token collapses to 0ms under `prefers-reduced-motion`.

### Interaction states

- **Hover:** the gold wash comes up, the border goes to `--gold-dim`, and a row title turns gold.
  Nothing lifts, scales, or shifts position.
- **Press:** the ground deepens one step. No transform.
- **Selected:** chips take gold, or their own quality colour when they represent a tier. The zone
  picker's selected state is solid `--gold-deep`, the heaviest selection weight in the system, and
  it is used only there.
- **Focus:** a 2px outline in `--gold-deep` on parchment or `--gold` on stone, at 2px offset,
  visible on every interactive element including table headers and tree nodes. Never removed.
- **Disabled:** 40% opacity, `not-allowed` cursor.

---

## Iconography

**There is no icon set, and that is deliberate.** No icon font, no SVG library, no CDN set. None
was supplied, and importing one would bring in a visual language the client does not have.

What stands in for icons:

- **The talent node.** A 44px square with 2px border in the tier's quality colour, filled with
  stone, carrying the section number in the interface face. A rank counter in the bottom-right
  corner holds the downstream reach number, exactly where a talent's points invested sits.
- **Talent arrows.** Orthogonal lines with a small solid arrowhead. Gold and weighted for cargo,
  thin and dashed for "makes possible".
- **The quality dot.** A 6 to 8px filled circle in the tier colour, inside badges and chips.
- **Glyphs from the type itself.** `+` and `−` for collapsed and expanded rows, `▲ ▼ △` for sort
  state, `×` for clearing a field, `·` as a separator, `—` for an empty value.
- **The select caret**, drawn as two CSS gradient triangles rather than an image.

No emoji. No dragons, swords, crossed axes, or heraldic shields as decoration. No logo mark:
**none was supplied, so none was created.** Wherever a mark would go, the title is set in the
display face (see `guidelines/brand-wordmark.card.html`).

## Fonts

Neither original can ship. **Morpheus is shareware and payment is required even for personal use.
Friz Quadrata is a commercial ITC face requiring a foundry licence.** The substitutes were chosen
on skeleton rather than mood:

- **Grenze Gotisch** for Morpheus. Morpheus is a gothic display face with tall vertical
  silhouettes, spear-like points and flared tops, but it is a gothic-roman hybrid rather than true
  blackletter, so it stays readable at heading size. Grenze Gotisch is the closest free match on
  those terms.
- **Marcellus** for Friz Quadrata. Friz Quadrata's signature is flared serifs and open lowercase
  bowls; Marcellus is the closest free flared Roman with a real lowercase at interface sizes.

**If you can license the originals, send `MORPHEUS.TTF` and `FRIZQT__.TTF`.** Drop them into
`assets/fonts/`, replace the `@import` in `tokens/fonts.css` with `@font-face` rules named
"Morpheus" and "Friz Quadrata", and put those names first in `--font-display` and `--font-ui`.
Nothing else in the system changes.

---

## The interlock tree

The signature element, and the only place the design raises its voice. It is drawn as a vanilla
talent tree because that is structurally what the data is: tiered nodes, dependency arrows, and a
count of what rides on each node. Every rule below is derived from `proposals.json`:

- **Tiers run top to bottom as rows**, with the tier name, deployment note, and proposal count in
  the left header, exactly where a talent tree carries its tier requirement. Every edge in the
  data runs Tier 1 to Tier 2, Tier 2 to Tier 3, or stays flat inside a tier. None run backward, so
  the layout states Section 10's argument visually: cheap behavioral work is what makes the
  expensive architectural work viable.
- **Arrow weight is transitive downstream reach.** The trunk emerges rather than being drawn in:
  extraction into haulage, haulage into exchange, exchange into stock.
- **Two arrow treatments, never one.** An edge whose both ends touch Trade or Economy carries
  cargo: solid, weighted, labelled with what moves along it (lumber, haulage, thread and flux and
  vials, ore and lumber, stock levels). Every other edge means "makes possible": 1px, dashed,
  unlabelled.
- **Nodes are identified by the document's own section numbers.** No second numbering scheme. The
  rank counter is the downstream count.
- **Proposals with no edges sit in a labelled independent band** with a dashed node border. Seven
  of the 28 ship without touching anything else, and saying so is useful information.

---

## Index

Root: `styles.css` (the entry point consumers link, `@import` lines only), `readme.md`, `SKILL.md`,
`thumbnail.html`.

`tokens/` — `fonts.css`, `colors.css`, `typography.css`, `spacing.css`, `borders.css`,
`motion.css`, `base.css`.

`components/` — `components.css` holds every component class; each group has one card HTML.

| Group | Components |
|---|---|
| `components/document/` | **TierBadge**, **SectionHeading**, **Prose**, **Note**, **CiteRef**, **DataField** |
| `components/controls/` | **Button**, **FilterChip**, **Select**, **SearchInput** |
| `components/data/` | **ProposalTable**, **ProposalTooltip**, **InterlockSpine**, **ZonePicker**, **EmptyState** |
| `components/navigation/` | **SidebarTOC**, **DocFooter** |

Every component has a sibling `.d.ts` props contract and a `.prompt.md` usage note.
`InterlockSpine` keeps its name for API stability; it renders the talent tree.

`ui_kits/living-azeroth/` — the full document: `index.html`, `kit.css`, `Hero.jsx`,
`DocumentBody.jsx`, `ZoneView.jsx`, `SpineView.jsx`, `ProposalBrowser.jsx`, `App.jsx`, plus its own
`README.md`.

`templates/document-page/` — a starting-point template consuming projects can copy.

`guidelines/` — foundation cards: colour (grounds, ink scale, item quality, quality on parchment,
interface gold, stone panel), type (display, body, interface, numbered heading, scale ladder),
spacing (scale, document rhythm), brand (wordmark, rules and radii, quest-log rows, interaction
states, motion, iconography).

`assets/` — `data/proposals.json` and `source/` (brief, revision, and design document).

### Intentional additions

The sources define no component library, so the inventory was authored from the described
surfaces. Three entries are additions rather than direct requirements:

- **CiteRef** — the document carries 21 numbered sources and credibility is the point, so inline
  references needed a real component.
- **DataField** — the label-and-value pair recurs across the zone view, the hero, and panel
  metadata.
- **ProposalTooltip** — named by the revision as a pattern ("the vanilla tooltip is already the
  proposal card") rather than as a component; it is factored out so the mapping from proposal
  record to tooltip structure is defined once.
