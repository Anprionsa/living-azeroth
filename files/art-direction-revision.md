# Art Direction Revision: Vanilla-Era Warcraft

Paste into Claude Design as a revision to the existing brief. Everything in the original brief holds except the art direction section, which this replaces. The structure, components, and interactive views stay as built.

---

## What was wrong

The original brief banned the fantasy register to avoid looking like a fan site. That was an overcorrection. It pushed the system into a generic technical-documentation look, which is not neutral, it is just a different kind of anonymous. This is a Warcraft document and it should look like one.

The distinction that matters is not "Warcraft versus not Warcraft." It is between generic fantasy kitsch, which does read as amateur, and precise period citation of Warcraft's own design vocabulary, which reads as someone who knows exactly what they are referencing.

Target era is vanilla World of Warcraft and earlier. Not Warcraft III, not retail.

## The register

Two source bodies, used for different parts of the system.

**Warcraft II manual and the early Warcraft print material** for the long prose sections. Those manuals were framed as in-world chronicles and tomes, set as ink on paper with heavy inked illustration, not as game UI. That is the right model for 8,000 words of reading, and it is genuinely pre-vanilla.

**Vanilla WoW client UI** for the data and interactive components. Quest log, tooltip, talent tree. These are precise, recognizable, and they carry real structural logic that maps onto what the components already do.

Prose reads like a chronicle. Data reads like the client.

## Typography

Vanilla WoW ships three font files, and two of them are the entire typographic identity of the era:

- `MORPHEUS.TTF`, used for quest titles and in-game book text. This is the display face. Section headings, the wordmark, view titles.
- `FRIZQT__.TTF`, Friz Quadrata, the main UI face. Item names, tooltips, panel labels, everything in the interface. Use it for component chrome, labels, tier badges, table headers.
- `SKURRI.TTF` is combat damage numbers. Not useful here.

Both Morpheus and Friz Quadrata are commercial faces, so check licensing before shipping. If licensing blocks it, the closest free substitutes are a humanist flared serif for Friz Quadrata and a heavy calligraphic display for Morpheus, but the real ones are worth the trouble because the recognition is instant and exact.

Body text stays a readable serif at length. Friz Quadrata is a UI face and gets tiring over 8,000 words, so keep Source Serif 4 or similar for running prose and let the Warcraft faces carry headings and interface. That split is also true to the source: the manuals were not set in the UI font either.

Drop IBM Plex Mono. Friz Quadrata takes over the data and label role.

## Palette

From the vanilla client rather than invented.

- `#F0E6D2` quest log parchment, the warm panel behind reading content
- `#2B2721` and `#40382C` the UI stone panel, dark ground
- `#FFD100` and `#C79C6E` the classic interface gold, for headings and rules
- `#1C1710` ink for body text on the parchment ground

## Tier colors become item quality colors

This is the change that pays off most. Replace the invented slate, brass, and copper scale with vanilla's item quality colors, which every player reads as escalating significance without being told:

- Tier 1 uncommon green `#1eff00`
- Tier 2 rare blue `#0070dd`
- Tier 3 epic purple `#a335ee`

These are the exact values the client returns. Reserve legendary orange `#ff8000` for nothing, or for a single callout if one proposal ever earns it.

The semantics line up on their own. Uncommon is the common upgrade you see constantly, rare comes from real effort, epic is the thing you plan around. That is exactly the tier ladder.

## The spine becomes a talent tree

The interlock spine has been fighting its own layout, currently rendering at 1364 by 1152 with 666 pixels of empty column. The vanilla talent tree solves the visual register and the layout problem in one move, because it is structurally the same object: tiered nodes, dependency arrows between them, points invested indicating weight.

Specifics worth carrying over:

- Tiers run top to bottom as rows, not left to right as columns. That turns the 12-station Tier 2 band into a wide row instead of a tall column and gets the whole graph into one screen.
- Talent arrows are the dependency edges. Vanilla arrows are a specific, recognizable shape and they already mean "this required that."
- Point counters on each node carry the downstream reach number.
- The tier header on the left of a vanilla talent tree carries the tier requirement. Use it for the tier name and station count.

A talent tree is explicitly not a single sequence, which was the original objection to the rail. It is a tiered directed graph, which is what the data actually is.

## Component patterns

**Proposal cards become tooltips.** The vanilla item tooltip has a fixed structure: name in quality color at the top, attribute lines beneath, then flavor text in gold italic at the bottom. That maps directly onto the proposal records. Title in tier color, then section, zones, systems, cost as attribute lines, then the `note` field as the gold italic flavor line. Nothing has to be invented.

**The document body becomes a quest log.** Quest title, objectives, description. Section headings in Morpheus over the parchment panel, with the numbered subsections in the objectives register.

**Keep ledger banding out.** The alternating-row treatment was from the previous direction and does not belong here. Use the vanilla list-row hover instead.

## What still holds

- No aged or stained parchment texture overlays. Flat panel color only. Texture is the tell that separates a fan site from a design document.
- No dragons, swords, crossed axes, or heraldic shields as decoration.
- No beveled or glowing 3D chrome. Vanilla's panel edges are flat and thin.
- No blackletter for body text. Morpheus for display only.
- No game screenshots or Blizzard art assets. Unchanged.
- Not the Warcraft III or retail heraldic look. Vanilla or earlier only.

Spend the boldness on the talent tree. Everything around it stays quiet.
