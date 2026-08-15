# Manifest

**Classic+ design suite, August 2026**

*Read this first. The arrangement changed partway through: the data is now canonical and the documents are rendered from it, which is the reverse of how the project started.*

---

## 1. The single source

**`talent-data.json`** is canonical for **what a talent does**. 64 trees, 1,340 talents, 210 abilities, two configurations, three rulesets usable as controls, and every effect expressed in a closed vocabulary.

The design documents are canonical for **why**. Their tree listings are generated from this file and marked with `<!-- GENERATED -->`; anything inside those markers is a rendering and hand-editing it will be overwritten.

**`SCHEMA.md`** explains the shape: four entities, the closed vocabularies, and what each field is for. Read it before touching the data.

## 2. The two configurations

| | Trees | Argument |
|---|---|---|
| **core**, "Fixing Classic" | the 27 rebuilt vanilla trees | vanilla's talents are badly built and can be rebuilt without adding anything |
| **expanded**, "Expanding on it" | core plus 7 absorbed and 3 original trees | a fourth tree per class, a fifth for mage |

Core stands alone and is checkable that it does. `validate.py core` and `validate.py expanded` both pass with zero errors and zero warnings. Explained in `configurations.md`.

## 3. Documents

| File | What it is |
|---|---|
| `classic-plus-talent-design.md` | **Behavior Over Numbers.** All 27 vanilla trees rebuilt. 27 sections. Tree rows generated. |
| `classic-plus-class-absorption.md` | **Class Absorption.** The 10 new trees, plus the absorbed-versus-original distinction in 7.9. Tree rows generated. |
| `classic-plus-living-world-design.md` | **A Living Azeroth.** World texture, seasons, art direction, zone additions. Untouched by the simulation work. |
| `spec-grievances.md` | Why players complain about specific specs, with a computed forced-flat floor per tree. |
| `build-diversity.md` | The 26 mutual pairs and what players would name them. |
| `partial-builds.md` | Whether a hybrid is a build, answered from vanilla's own naming. |
| `configurations.md` | Why core and expanded are separate products. |
| `sim-data-gap.md`, `sim-instruments.md`, `sim-tanking.md`, `sim-healing.md` | What each instrument measures and why one was not enough. |
| `sim-results.md` | Every simulation result, including the ones that were later invalidated. |
| `PLAN.md` | Phased plan. Phases 1 and 2 are complete. |
| `open-register.md` | State of play. Arbitrates any contradiction between the others. |

## 4. Code

| File | What it does |
|---|---|
| `validate.py` | 21 rules against the data. Takes a configuration: `validate.py core`. |
| `render_doc.py` | Regenerates the talent document's tree rows from the data. |
| `render_class.py` | The same for the class document. |
| `sim.py` | Damage simulator. Vanilla attack table, five fight scenarios, role-aware build selection. |
| `tank.py` | Threat and survivability. Reports TPS, damage taken, effective health, crit immunity. |
| `heal.py` | Healing. Reports effective HPS, healing per mana, overheal, time to out of mana. |
| `effects.py` | Drafts structured effects from talent text. **Output is a draft, not data.** |
| `migrate.py`, `extract.py`, `author.py`, `analyse.py`, `floor.py`, `ledger.py` | Build and query helpers. |

## 5. Where the work actually stands

**Core is complete.** 484 of 484 talents authored with structured effects, 21 validation rules passing clean, both documents matching the data exactly, and all 27 trees measurable by at least one instrument.

**Expanded is complete.** All 212 talents authored, all 10 trees validating clean, and every subtraction node carrying its cost as a real effect rather than as prose.

**The headline simulation result:** across the damage pairs the capstone premium is a median 3.7% with four of six inside five percent, which meets the tuning target in talent design 5.6. The two outside are Bloodthirst and Shadowform, both throughput capstones landing on rotations built from their own school. On tanks the premium is 5.7% to 14.2% and the target is not met.

## 6. Five things that will save you a day

**Data is canonical, documents are rendered.** Editing a talent means editing `talent-data.json` and running the renderer. Editing inside a `GENERATED` block is wasted work.

**A derived set should be recomputed by whatever consumes it, never stored.** A 69-talent scope was computed against one build selector and used with another; half the authoring went to talents the simulator never compares.

**When a measurement returns exactly zero, suspect the consumer before the data.** This happened four times: the extractor, the tag lookup, the build selector, and the value function.

**Partial authoring produces a biased answer, not a noisy one.** At 67% coverage several pairs favoured the mid-tree shape; at 100% none did, because the unauthored talents were disproportionately capstones.

**A value heuristic encodes an objective.** The same selector that correctly refuses a crit-removing talent for a damage build must take it for a tank. `build()` takes a `role` for this reason.


## 10. The simulation work

Built after the design documents, to answer whether talent design 5.6's tuning rule holds. It does: **every core pair sits inside -7% to +7% against its mid-tree alternative across five scenarios, and every class has a capstone-free build within 6.3% of its best capstone build.**

### 10.1 The instruments

| File | Measures | Covers |
|---|---|---|
| `sim.py` | damage per second across five fight scenarios | the damage trees |
| `tank.py` | threat, damage taken, effective health, crit immunity | four tank trees |
| `heal.py` | effective healing, healing per mana, overheal, time to out of mana | five healing trees |

Five scenarios: `patchwerk`, `burst`, `movement`, `cleave`, `switching`. A talent's worth is its profile across them, not one number.

### 10.2 The checkers

| File | What it does |
|---|---|
| `fullaudit.py` | nine completeness checks in one place. **Run this first.** |
| `coverage.py` | which authored effects any simulator actually reads |
| `ability_audit.py` | abilities granted but unreachable, or cast without the data they need |
| `worth_sweep.py` | every talent's contribution in the damage trees |
| `role_sweep.py` | the same for healing and tank trees, with their own instruments |

### 10.3 The tuners

`tune.py` for expanded trees, `tune_core.py` and `tune_band.py` for core pairs, `tune_tank.py` for tanks. `tune_band.py` targets the worst scenario cell rather than the sustained one, which is the only version that works.

`nocapstone.py` sweeps 114 capstone-free shapes per class. `candidates.py` and `arms_candidates.py` A/B test candidate designs on two axes. `band_study.py` prices band policies. `talent_worth.py` measures one talent by removing it.

### 10.4 The record

`sim-results.md` is the running log including numbers later invalidated, and `full-pass.md` is the current state. Between them: `sim-instruments.md`, `sim-tanking.md`, `sim-healing.md`, `sim-expanded.md`, `effect-coverage.md`, `ability-coverage.md`, `behaviour-pass.md`, `tuning-pass.md`, `burst-fix.md`, `candidate-test.md`, `band-policy.md`, `poison-options.md`, `poison-model.md`, `ramp-prior-art.md`, `nocapstone-results.md`, `reading-the-number.md`, `warlock-chase.md`, `worth-findings.md`, `flags-closed.md`, `state-after-worth-fixes.md`, `full-audit-run.md`, `final-suite.md`, `final-state.md`, `sim-drift.md`, `text-and-resource.md`, `whats-left.md`, `suite-results.md`, `suite.py`, `behaviour.py`.

**Two of those are corrections rather than findings.** `reading-the-number.md` corrects a capstone-free median I reported as a design signal twice when it was measuring off-role builds. `sim-drift.md` records that 30% of authored talents had drifted into percentages, which `behaviour-pass.md` then repaired.

## 11. What the simulation changed about the design

**Eleven talents were rewritten because measurement showed they did not work**, not because anyone disliked them. Dark Pact returned mana to a build that had enough. Shadow and Flame rewarded alternating two spells cast thirteen to one. Unbound said "you may have two demons" and was authored as a damage percentage. Death Wish carried both a permanent bonus and a cooldown, which made one point worth ten percent and collapsed the warrior design space.

**Nine rogue talents modified a `poison` tag no ability carried**, so Assassination read exactly 0.0% on every scenario since the project began.

**The scenario levers are the reusable result.** A periodic cleave gained 18.8 points on three targets at zero cost on one. An opening window gained 4.8 points of burst per point of sustained. **A lever that pays everywhere is a buff; a lever that pays in one place is a fix**, and it must sit on the talent that differs between the two builds or it lifts both and closes nothing.

## 7. Superseded, and kept only as a record

These were canonical before the schema work and are now inputs to `talent-data.json` rather than sources of truth. **Do not edit them.**

`talents-classified.json` holds vanilla only. `rebuilt-trees.json` and `trees.json` were merged into the unified file. `sim-authoring-scope.json` is regenerated by whatever consumes it and should never be trusted as stored. `render.py` is superseded by `render_doc.py` and `render_class.py`. `flat-floors.json`, `specs-baseline.json` and `proposals.json` predate the schema and are unmigrated.

## 8. Working documents

Records of decisions and their reasoning, all still accurate:

`chronomancer.md` and `two-trees.md` argue the three original trees. `tag-conversion.md` and `conversion-framing.md` work out where tag conversion earns its place, settled at three classes. `absorbed-audit.md` and `absorbed-revisions.md` measured the seven absorbed trees before Phase 2 and carry scope notes saying so. `sim-baseline-protocol.md` sets the control methodology. `sim-first-results.md` and `sim-scope-correction.md` record early simulation runs whose numbers were later invalidated and are kept because the method is the point. `art-direction-revision.md` and `appendix-d-portable.md` predate all of it. `claude-design-brief.md` describes the world and class documents and **does not cover the talent work at all**, which is its main limitation.

## 9. If you are handing this to someone

Give them `SCHEMA.md`, `talent-data.json`, `open-register.md`, and this file. Everything else is reachable from those four, and the register will tell them what is decided, what is open, and what has already been tried and rejected.
