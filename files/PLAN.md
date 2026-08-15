# Plan

**August 2026**

*Three pieces of work in dependency order. Written after checking the current state rather than from memory, so the numbers are current as of this writing and should be re-measured before starting.*

---

## Phase 1: Make the document match the data

**Why first.** Of 477 core talents, 40 do not appear in `classic-plus-talent-design.md` at all and 327 more carry different text. That is 77% divergence. The document is what a person reads and it currently describes a version of the rework that no longer exists. Nothing should be shown to anyone until this is closed.

**The complication, found on inspection.** Tree sections are not a clean block of listings. Prose is interleaved *between* gate blocks: each gate is followed by a paragraph saying what was deleted and why. So the tree cannot simply be regenerated and spliced over a contiguous region.

### Steps

**1.1 Separate argument from listing, per section.** Each rebuild section has three kinds of content: diagnosis prose that stays hand-written, gate blocks that become generated, and deletion notes that currently sit between gates. Move every deletion note out of the gate sequence into a single "What was deleted" paragraph at the end of each section. That makes the gate sequence contiguous and generatable.

**1.2 Add generated-block markers.** Wrap each tree's gate sequence in HTML comment delimiters so the regenerator knows exactly what it owns and never touches prose.

**1.3 Extend `render.py`** to emit document-ready markdown matching the existing house style, including the tier label line and the flag annotations for subtraction, cross-tree, and reciprocal nodes.

**1.4 Regenerate all 27 core tree sections and splice.**

**1.5 Verify.** Zero em dashes, prose sections byte-identical outside the markers, every talent in the data present in the document, no talent in the document absent from the data, and section cross-references still resolving.

**Exit criterion.** The divergence measurement returns zero in both directions, and re-running it becomes a standing check.

**Risk.** 1.1 is hand work across 27 sections and is where an error would silently drop an argument. Do it as a move rather than a rewrite, and diff the prose before and after.

---

## Phase 2: Bring the expansion to core's standard

**Why second.** The core is now the model. Everything the expansion needs has already been solved once, so this is application rather than design.

### Steps

**2.1 The 85 rank and effect mismatches.** All in the absorbed and original trees: Blackguard, Bladedancer, Runeblade, and absorbed Survival at 12 each, Necromancy, Metamorphosis, and Conduit at 11, Dreamer and Radiance at 2. Same treatment as core's 68: multi-rank talents state one discrete effect per rank.

**2.2 REG-25's change list**, which the validator independently rediscovered. Delete the flat nodes in all seven absorbed trees and fund their local mechanic with the budget, per REG-05. Grow gate 20 from six to eight. Add subtraction nodes to Metamorphosis, Conduit, and Survival.

**2.3 REG-48's six reciprocal nodes.** Necromancy, Metamorphosis, Bladedancer, Conduit, Runeblade, and absorbed Survival have no core tree reaching toward them. One node each and the expansion becomes symmetric, matching what core already has.

**2.4 The two structural rebuilds already specified but not applied to data.** Metamorphosis needs the Section 9 treatment for premise failure, and absorbed Survival should take the Section 17.2 rebuild rather than carrying vanilla Survival's content forward.

**2.5 Validate expanded to zero warnings**, matching core.

**2.6 Regenerate `classic-plus-class-absorption.md`'s tree sections** using the Phase 1 machinery.

**Exit criterion.** `validate.py expanded` returns zero errors and zero warnings, and the class document matches the data.

---

## Phase 3: Unblock, verify, and repackage

These are independent of each other and can run in any order once Phase 1 is done.

### 3.1 Specify the simulation handoff

The last two empty fields, `dividend.stats` and ability `coefficient`, are blocked on simulation. That work is outside this project, but what a simulator needs from us is not, and specifying it is the thing that actually unblocks it.

Write a handoff document covering: which build per spec is being tested, since eleven of thirteen in `specs-baseline.json` are still unconfirmed; where the control comes from, which is Warcraft Logs Naxxramas rankings rather than a simulated baseline; the band neutrality target from REG-01; and the confounds that will invalidate the comparison if unrecorded, world buffs chief among them.

### 3.2 Verification debt, five items

Confirm the eleven unverified canonical builds against a talent calculator. Verify MORPHEUS.TTF and FRIZQT__ licensing before anything public ships. Confirm the ChromedDragon image permission is actual rather than assumed. Check the Arms rebuild's gate assignments, which the document still flags as unverified. Review the flat and behavior classifier, which was validated on one tree.

### 3.3 The four InterlockSpine rendering bugs

Edge weight hardcoded so the most load-bearing nodes draw thinnest, label halos stippling their own departing edges, a fixed canvas that cannot downscale, and a stray band divider. All documented, none fixed. The talent-tree layout from the art direction revision is the intended structural fix for the third.

### 3.4 Repackage for Claude Design

Claude Design is working from files that predate the schema, the dataset, the validator, and both configurations. Rebuild the handoff around `talent-data.json` as the single source, with `MANIFEST.md` updated to describe the data-first arrangement rather than the document-first one it currently describes.

---

## Sequencing

Phase 1 blocks everything that involves showing the work to anyone, including 3.4.

Phase 2 depends on Phase 1 only for its final step, 2.6, which reuses the same regeneration machinery. Steps 2.1 through 2.5 can start immediately.

Phase 3 is independent throughout, and 3.1 is the highest value item in it because it is the only thing standing between the current state and a simulated answer to whether any of this is balanced.

## What this plan does not include

Any new design. No new trees, no new mechanics, no further conversion work. The tag conversion decision from REG-38 and REG-42 is settled at three classes and deliberately not scheduled here, because it should be built after the expansion reaches parity rather than alongside it.

The seasonal and world systems are on their own clock and are untouched by any of this.
