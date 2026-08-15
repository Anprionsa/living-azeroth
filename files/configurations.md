# Two Configurations

**August 2026**

*Fixing Classic, and then expanding on it. Encoded in `talent-data.json` as `meta.configurations`, enforced by `validate.py <config>`, and queried by `analyse.py`.*

---

## 1. Why two

The project has been treating one thing as two: a rework of vanilla's talents, and a set of new trees. Those are separate products with separate risk, and they were sharing a dataset without sharing a name.

**Core, "Fixing Classic".** The 27 rebuilt vanilla trees. Three per class, 51 points, nothing new. This is the argument that vanilla's talent system is badly built and can be rebuilt without adding anything.

**Expanded, "Expanding on it".** Core plus the seven absorbed and three original trees. Four trees per class, five for mage.

The reason to name them is that **core has to stand alone.** If the expansion never ships, the rework must still be complete, and if the rework depends on the expansion for any of its argument, then it was never a rework, it was the first half of something else.

## 2. It does stand alone, and that is checkable now

Run against the core configuration only:

| | Core | Expanded |
|---|---|---|
| Trees | 27 | 37 |
| Talents | 890 | 1,102 |
| Validation errors | 0 | 0 |
| Validation warnings | **5** | 31 |
| Cross-tree edges | 42 | 55 |
| Mutual pairs | 15 | 21 |
| Classes with a named hybrid | 9 of 9 | 9 of 9 |

**Core passes ten of twelve rules clean with five warnings total.** Every mutual pair it needs is internal: fifteen pairs across nine classes, none of them touching a tree that might never exist. Restoration druid's thin gate 20 and missing subtraction flag account for two of the five warnings, and three stale aura flags account for the rest.

**Twenty-six of expanded's thirty-one warnings are the seven absorbed trees**, and all of them are the outstanding work already listed in `absorbed-revisions.md`. The expansion's debt is confined to the expansion, which is exactly the property the split was meant to expose.

## 3. What the expansion actually adds

Six new mutual pairs, all between a core tree and a new one:

- Chronomancer with Arcane and with Frost
- Dreamer with Feral Combat and with Restoration
- Radiance with Holy priest and with Shadow

That required seven **reciprocal nodes** in core trees, which exist only in the expanded configuration and are marked `availableIn: ["expanded"]`. Without them the expansion was entirely one-way: ten new trees reaching toward core and no core tree reaching back, which meant splashing a new tree was a relationship the rest of the game did not acknowledge.

### 3.1 The first draft of those nodes was wrong

Written as pure conditionals, they read like "your Arcane Missiles extend an Echo held on any ally", which does nothing whatsoever for a mage without Chronomancer points. That is precisely the trap REG-07 exists to prevent, and the validator caught it as seven `cross-tree-stands-alone` failures on the first run.

All seven are rewritten with a base effect that works for anyone plus the new-tree interaction as upside. Temporal Resonance now makes Evocation channellable while moving for any mage, and extends an Echo if you hold one.

**The rule caught a violation in work written minutes after the rule was encoded.** That is a better argument for encoding rules than any amount of describing them.

## 4. What this changes about how the work is presented

**Core ships first and is defensible alone.** Its case is the audit: 1,352 vanilla points, 991 buying numbers, 27 trees rebuilt so that points buy behaviour. No new classes, no new fantasy, nothing to argue about beyond whether the rebuilds are good.

**Expanded is a second argument** and it should be made second, because it depends on accepting the first. A reader who rejects the rework will reject ten new trees built to its rules; a reader who accepts it has already accepted the standard the new trees are held to.

**The seasonal and world systems in the living world document are orthogonal to both.** They ship on their own clock, and the deployment note in that document already treats them that way.

## 5. Still open

**Four absorbed trees remain unreached.** Blackguard now has Sanguine Rite from Holy paladin, but Necromancy, Metamorphosis, Bladedancer, Conduit, Runeblade, and absorbed Survival have nothing pointing at them. Six more reciprocal nodes, one per tree, and the expansion is symmetric.

**Eleven edges are still one-way inside core**, and they are the same list as before: Survival, Arcane, and Combat reaching toward trees that do not answer, plus Feral toward Restoration and Retribution toward Holy. Those are core problems, not expansion problems, and they should be fixed in core.

**The point budget is unchanged at 51 in both configurations**, so expanded does not add power, it adds options. That claim now needs testing rather than asserting, because five trees of options against three is a materially different search space for a simulator.
