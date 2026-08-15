# The Expanded Trees, Which I Had Left Out

**August 2026**

---

## 1. The error

Every analysis in the last several passes used `A.builds(cls)`, whose `withExpanded` parameter defaults to `False`.

**The 320-build comparison against Classic, the 69 hybrids, the build names, and the band-neutral tuning targets were all core only.** Blackguard, Necromancy, Metamorphosis, Bladedancer, Conduit, Runeblade, Survival and Chronomancer appeared in none of it.

Two smaller faults in the same place. **The expanded map held one tree per class**, so Chronomancer was silently dropped even when the flag was set, since Mage already had Necromancy. And Druid and Priest had no entry at all rather than an empty one.

**One thing was not broken.** The band-neutral pass scaled by class rather than by tree, so the expanded trees received their class's depth coefficient correctly. Blackguard sits at Paladin's 1.2711, Necromancy and Chronomancer at Mage's 0.8527. **The tuning holds; only the analysis was blind.**

## 2. What the expanded trees do to the picture

| Class | Logged | Best core | Best expanded | Change |
|---|---|---|---|---|
| **Warrior** | 100.0% | 85.1% | **99.8%** | **+17.3%** |
| **Rogue** | 84.2% | 74.9% | **90.7%** | **+21.0%** |
| Mage | 74.8% | 67.9% | 67.9% | none |
| Warlock | 64.4% | 62.4% | 62.4% | none |
| Hunter | 60.8% | 58.8% | 58.8% | none |
| Druid | 60.5% | 58.8% | 58.8% | none |
| **Shaman** | 51.8% | 53.1% | **57.6%** | **+8.4%** |
| Priest | 42.4% | 46.7% | 46.7% | none |
| **Paladin** | 39.1% | 44.9% | **46.7%** | **+4.1%** |

**Four of nine classes have an expanded tree in their best build. Five do not.**

## 3. The four that changed

**Warrior, Fury 31 / Runeblade 20, at 99.8%.** Reaches Bloodthirst and Improved Berserker Rage, then Shattering Blow and Killing Frost. **The largest single gain in the table and the one that matters most**, because Warrior's core third tree is Protection and a damage build gets nothing from it. Runeblade is the tree that gives Warrior a third damage option at all, and it lifts the class 17.3%.

**Rogue, Assassination 21 / Bladedancer 20 / Combat 10, at 90.7%.** A three-tree split reaching Toxicology and Envenom, then Sweeping Kick and Momentum, then Riposte. **The biggest proportional gain at 21.0%**, and it beats every core rogue build.

**Shaman, Elemental 26 / Conduit 25, at 57.6%.** Lightning Mastery and Elemental Fury, then Elemental Bond and Surge.

**Paladin, Blackguard 31 / Retribution 20, at 46.7%.** Damnation and Reaping, then Seal of Command. **The only case where an expanded tree is the deep tree rather than the partner.**

## 4. The five that did not change is the more interesting half

Mage, Warlock, Hunter, Druid and Priest all have their best build unchanged by adding an expanded tree.

**For Druid and Priest that is expected**: their expanded trees are Dreamer and Radiance, both held out as candidates, so those classes had nothing added.

**For Mage, Warlock and Hunter it is a real result.** Necromancy, Chronomancer, Metamorphosis and the reworked Survival are all available and none of them beats the class's best core build. They are alternatives rather than upgrades.

**That is the outcome the absorption proposal wanted and it should be stated as a success rather than a null.** An absorbed tree that beat every core build would make the core trees obsolete, which is the failure mode the whole "trees not classes" argument was trying to avoid.

## 5. Which leaves a question about Warrior and Rogue

Those two are the exceptions, at +17.3% and +21.0%.

**Warrior's case is defensible.** The gain is not Runeblade being strong, it is Protection being useless to a damage build. A warrior choosing between Arms, Fury and Protection has two real options; a warrior choosing between Arms, Fury, Protection and Runeblade has three. **The expanded tree fixes a structural gap rather than adding power.**

**Rogue's case is not.** Rogue already had three usable damage trees. Bladedancer beating all of them by 21% means it is simply stronger, and that is the failure mode.

**Bladedancer's depth coefficient is 0.8169, the same as the core rogue trees, so the band-neutral pass never treated it separately.** Bringing it into line is one number and does not require touching the tree.

## 6. What needs rerunning

**The hybrid list and the build names are core only and should be regenerated.** Fury/Runeblade and the Assassination/Bladedancer/Combat split are both competitive builds that never appeared in either document.

**The 320-build comparison should become the full set.** With expanded trees the count is far higher: Mage alone goes from 48 shapes to 360.

**The band-neutral targets should be set against the best build including expanded trees**, not the best core build, or the tuning is fitted to a build nobody would take.
