# Talent Data Schema

**Version 1.0 | August 2026**

*One shape for every tree in the project, designed so that measurements are declarative rather than one-off scripts, so gear can be modelled later without a migration, and so cross-checks run as a suite.*

---

## 0. Why this exists

Three datasets currently describe talents and none of them share a field name. `talents-classified.json` nests classes inside trees inside a talent dictionary and calls a rank count `maxRank`. `rebuilt-trees.json` uses an array of rows and calls it `ranks`. `trees.json` uses the same rows but carries a dozen tree-level fields the others lack.

Every measurement so far has therefore been a bespoke script that reshapes its input first. That is why the same question got three different answers: the reshaping was where the errors lived.

Three things this schema has to support, in order of how soon they bite:

**Cross-checks as a suite.** Twelve validation rules have accumulated across the project as prose in a register. They should be code that runs against data, so a rule change is one edit and a re-run rather than a manual sweep of 27 documents. This is the failure mode recorded as REG-24 and it has recurred five times.

**Expansion without migration.** New trees arrive regularly. A new tree should be a data entry, not a schema change.

**Gear, eventually.** Gear effectiveness needs to know what a stat point does, which needs abilities to be first-class objects with declared scaling. Nothing models that yet, and retrofitting it later means touching every talent. Better to leave the sockets in now even if they stay empty.

---

## 1. The four entities

### 1.1 Tree

The container. One per talent tree, whether vanilla, rebuilt, absorbed, or original.

| Field | Type | Notes |
|---|---|---|
| `id` | string | stable slug, `warrior-arms`, `mage-fire` |
| `class` | string | the host class |
| `name` | string | display name |
| `kind` | enum | `vanilla`, `rebuilt`, `absorbed`, `original` |
| `status` | enum | `shipped`, `committed`, `candidate` |
| `supersedes` | id or null | a rebuilt tree points at the vanilla tree it replaces |
| `availablePoints` | int | computed, not authored |
| `rows` | array | see 1.2 |
| `mechanic` | object or null | `{name, description}`. Absorbed and original trees only |
| `dividend` | object | what depth grants automatically. See 1.5 |
| `lore` | object | `verb`, `verbNote`, `professionGate`, `permanentCost`, `worldAnchors`, `loreAnchor`. Absorbed and original only |

Keeping vanilla and rebuilt in the same file with `supersedes` is what makes before-and-after comparison a query rather than a join across two schemas.

### 1.2 Row

| Field | Type | Notes |
|---|---|---|
| `row` | int | 1 to 7 |
| `gate` | int | points required already invested. Always `5 * (row - 1)` |
| `talents` | array | see 1.3 |

`gate` is stored rather than derived because storing it makes the reachability check a comparison rather than an assumption, and the assumption is what produced the REG-C10 error twice.

### 1.3 Talent

| Field | Type | Notes |
|---|---|---|
| `id` | string | `warrior-arms-bloodletting` |
| `name` | string | |
| `ranks` | int | |
| `text` | string | full effect description |
| `buys` | enum | `number`, `behavior`, `ability` |
| `reads` | array | categories whose new members this would automatically affect. See 2 |
| `modifies` | array | ability ids this specifically changes |
| `grants` | array | ability ids this creates |
| `crossTree` | object or null | `{target: tree id, standsAlone: bool}` |
| `flags` | array | `subtraction`, `mark`, `capstone`, `permission`, `dead`, `aura` |

The distinction between `reads` and `modifies` is the one the project spent three wrong answers learning. **`reads` is a category, `modifies` is a named ability.** A tag conversion can exploit `reads` and cannot touch `modifies`. Keyword matching conflates them, which is why it failed in both directions.

### 1.4 Ability

New, and empty for now. The thing talents point at.

| Field | Type | Notes |
|---|---|---|
| `id` | string | `mortal-strike`, `frostbolt` |
| `class` | string | |
| `name` | string | |
| `tags` | array | the same vocabulary as `reads`. `frostbolt` is `[frost, spell]` |
| `scalesWith` | array | `attackPower`, `spellDamage`, `weaponDamage`, `healingBonus`, and so on |
| `coefficient` | number or null | how much of that stat converts |

This is the gear socket. **Gear effectiveness is a question about abilities, not talents**, and it cannot be answered until abilities exist as objects with declared scaling. Leaving the table empty is fine; leaving it out is not, because adding it later means editing every talent to point at something.

It also makes tag conversion checkable at the ability level rather than by reading prose: a conversion changes an ability's `tags`, and every talent whose `reads` intersects the new tags now applies. That is a set operation.

### 1.5 Dividend

What depth in a tree grants automatically, from talent design 5.1.

| Field | Type | Notes |
|---|---|---|
| `stats` | array | `{stat, perPoint}`, linear per REG-03 |
| `thresholds` | array | `{atPoints, grants}` for world-facing rewards and moved auras |
| `calibratedAgainst` | string or null | the canonical build whose flat sum this reproduces |

Absorbed and original trees carry `stats: []` per REG-C1, with their mechanic scaling instead. That is now expressible rather than a note in prose.

---

## 2. The category vocabulary

Fixed. A `reads` or `tags` value outside this list is a validation error.

**Schools.** fire, frost, arcane, shadow, holy, nature, physical
**Effect types.** bleed, poison, curse, disease, periodic
**Delivery.** melee, ranged, spell
**Support.** heal, absorb, threat, shout
**Entities.** pet, totem, trap, weapon
**States.** stealth, form

Twenty-four categories. The list is deliberately short: every addition makes conversion more powerful and the tuning surface larger.

---

## 3. Validation rules

Each becomes a function in `validate.py`. They exist as prose in the register today, which is why enforcing them has been manual and why five rule changes failed to propagate.

| Rule | Applies to | Check |
|---|---|---|
| `gate-arithmetic` | all | owning a tier N talent costs `5(N-1)+1` |
| `reachability` | all | cumulative points below each gate meet that gate |
| `hybrid-seat-weight` | rebuilt, absorbed, original | gate 20 carries at least 8 points |
| `no-numbers` | rebuilt, absorbed, original | no talent has `buys: number` |
| `subtraction-present` | rebuilt, absorbed, original | at least one talent flagged `subtraction` |
| `cross-tree-stands-alone` | all | every `crossTree` talent has `standsAlone: true` |
| `no-passive-aura-capstone` | all | no row 7 talent flagged both `aura` and not `ability` |
| `mechanic-coverage-band` | absorbed, original | 40 to 80 percent of points reference the tree's mechanic |
| `mechanic-present` | absorbed, original | the mechanic appears in the tree at all |
| `no-permissions` | rebuilt | no talent flagged `permission` |
| `tree-size-band` | all | availablePoints between 45 and 64 |
| `vocabulary` | all | every `reads` and `tags` value is in the fixed list |

Rules carry a severity: `error` for correctness, `warn` for design guidance. Reachability is an error. Mechanic coverage is a warning, because Dreamer at 100% was legal and wrong rather than broken.

---

## 4. What this makes cheap that is currently expensive

**Before and after on any tree.** `supersedes` plus one query.

**The conversion question.** Change an ability's tags, intersect against every talent's `reads`, count. No prose parsing.

**Gear, when it arrives.** Abilities already exist and already declare what they scale with. The sim reads the same file.

**Any rule change.** Edit one function, re-run the suite, get a list. The five propagation failures in the register were all a rule changing and the sweep not happening.

**Cross-checking my own work.** Every number in every document should be reproducible from this file by a named rule. Where it is not, the number is an assertion rather than a measurement, and it should be labelled as one.

---

## 5. First run

`migrate.py` builds `talent-data.json` from the three existing files. `validate.py` runs the twelve rules against it.

**64 trees, 1,091 talents, 12 rules. Zero errors, 32 warnings.**

Six rules pass clean: gate arithmetic, reachability, cross-tree stands alone, tree size band, vocabulary, and permissions.

**The 32 warnings are almost entirely one thing.** Every finding on `no-numbers`, `subtraction-present`, `hybrid-seat-weight`, and `mechanic-coverage-band` lands on the seven absorbed trees, and every one of them is already on the change list in `absorbed-revisions.md`.

That is the result worth having. **The suite independently rediscovered REG-25 without being told it existed.** Twelve rules derived from prose across twenty sessions, run against data, produced the same list of outstanding work that was written by hand. Rules that reproduce a known answer are rules worth trusting.

The two findings outside that: Restoration druid has no talent flagged `subtraction`, because its answer to the no-choice problem was three mutually exclusive one-point paths rather than a node saying subtraction, and three capstones flag as passive auras where the aura has already been moved to the dividend and the flag is stale.

## 6. Authoring debt, recorded in the file itself

The first run also found a problem with its own input, which is the point of a validator.

`standsAlone` was inferred from phrasing and flagged 37 false positives on the first pass. It is now set to null rather than false, because **an inferred field that looks authored is worse than an empty one.** Same failure as `reads`, one turn later, which is the second instance of the same lesson.

Four items of authoring debt are recorded in `talent-data.json` under `meta.authoringDebt`:

- `standsAlone`, unset on 37 cross-tree talents
- `flags`, where `capstone` and `mark` are reliable and `subtraction` and `aura` are not
- `reads`, authored for the 27 rebuilt trees and empty for vanilla and absorbed
- `abilities`, empty by design and waiting for gear

Recording debt in the data rather than in a document means the next measurement can check whether the field it depends on has been authored, instead of discovering afterwards that it was guessed.

---

## 7. Core is complete

Working solely on the core configuration, the 27 rebuilt vanilla trees, everything that could be authored has been.

**Validation: twelve rules, zero errors, zero warnings.** The three remaining warnings from the previous run resolved as follows. Restoration druid's gate 20 grew to eight and its three mutually exclusive one-point paths, Grove, Torrent, and Communion, are now flagged `subtraction`, which they always were in substance. The three capstone aura flags were stale: Moonkin Form, Apex Predator, and Trueshot had already moved their auras to the dividend, and that move is now recorded in each tree's `dividend.thresholds` rather than implied by prose.

**Cross-tree graph: 54 edges, 26 mutual pairs, zero one-way.** Twelve reciprocal nodes were added to close every unanswered edge inside core. Eight of nine classes now have all three possible pairs between their trees.

**Priest is the ninth and it is deliberate.** Holy and Shadow are left unwired because Shadowform forbids casting Holy spells, so the class's own mechanics already rule the pair out. Wiring it would be symmetry against the game. Recorded in `meta.deliberateGaps` so nobody closes it later thinking it was an oversight.

**Abilities: 188 authored**, bounded by what core talents actually reference rather than by a full spell list. Each carries `tags` drawn from the same twenty-four category vocabulary as talent `reads`, and `scalesWith` naming the stat it converts.

That vocabulary sharing is the point. **A tag conversion is now a set intersection**: change an ability's `tags`, intersect against every talent's `reads`, and the answer falls out. No text search, no keyword heuristic, and none of the three wrong answers that question produced before the data existed.

`coefficient` is null on all 188 and stays that way until simulation, per REG-02. That is the last blocked field in the core dataset and it is blocked on work outside this project rather than on authoring.

### 7.1 What core no longer needs

Nothing. Every field that can be filled without simulation is filled, every rule passes, and the expansion hooks are in place as `availableIn: ["expanded"]` talents that the core configuration filters out.

The expansion inherits a working base: a validated schema, twenty-six named build pairs, an ability table with a shared vocabulary, and a validator that catches a rule violation the same day the rule is written.
