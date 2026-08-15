# Partial Builds: Do They Count, Are They Competitive, What Are They Called

**August 2026**

*The question the fluid-tree model rests on. Most of it is computable from the rebuilt trees, and the answers are mixed.*

---

## 1. Does a player who does not go deep have a build?

Vanilla already answers this and the answer is yes, but only sometimes, and the difference is instructive.

A vanilla fury warrior at 17/34/0 does not have a build. They have a spec with some points parked in Arms to reach Impale. Nobody calls that anything. It is written as three numbers because there is nothing else to say about it.

A vanilla warlock at 30/0/21 has a build, and everyone calls it SM/Ruin.

The difference is not depth. Both are hybrids. **The difference is that the warlock's split is named after two talents that define it, and the warrior's is named after nothing.** Shadow Mastery and Ruin are a pair. Impale is filler on the way to a number.

So the test for whether a partial build is a build is not how the points are distributed. It is whether the player can name it after what it does.

## 2. What players actually call builds

Vanilla naming is consistent once you look at it. Builds are named after **signature talent pairs**, never after point splits and rarely after specs:

- SM/Ruin and DS/Ruin, warlock, two talents each
- Combat Swords and Combat Daggers, rogue, a tree and a weapon
- 17/34/0, warrior, no name because there is no pair

The pair is the unit. One signature talent gives you a spec name, which players already have. Two signature talents from different trees give you a build name, which they do not.

**That makes cross-tree conditionals name generators**, and it is the strongest practical argument for them that this project has found. A talent in Arms that changes what Fury's abilities do produces a thing players will name, because it produces a pair.

## 3. What the rebuilt trees predict

Every cross-tree node in the 27 rebuilds was extracted and mapped to the tree it reaches toward. Thirty-four edges. Eleven of them are **mutual**, meaning both trees carry a node pointing at the other.

| Class | Pair | The two talents |
|---|---|---|
| Warrior | Arms and Fury | Mortal Cleave / Sundering Blows |
| Paladin | Protection and Retribution | Crusader's Resolve / Bulwark of Faith |
| Paladin | Holy and Protection | Righteous Shield / Hand of Light |
| Priest | Discipline and Holy | Grace / Empowered Shield |
| Priest | Discipline and Shadow | Shadow Affinity / Inner Light |
| Druid | Balance and Feral | Eclipse / Nature's Grip |
| Druid | Balance and Restoration | Wild Growth, both directions |
| Shaman | Elemental and Enhancement | Stormstrike Affinity / Elemental Weapons |
| Shaman | Elemental and Restoration | Tidal Mastery / Elemental Communion |
| Hunter | Beast Mastery and Marksmanship | Marksman's Bond / Pack Tactics |
| Rogue | Assassination and Subtlety | Shadow Focus / a poison node |

**These eleven are the prediction.** A 26/25 or 30/21 build across a mutual pair takes both talents and gets two effects that reference each other. That is a pair, which by section 2 means it gets a name.

Vanilla had one such pair per class at best and usually none. The rebuilds produce eleven across nine classes, and the point budget supports them: 30/21, 26/25, 26/21/4, and 25/25/1 all reach tier five or six in two trees at once.

## 4. Where the wiring is uneven, which is the more useful finding

Twelve edges are one-way. A tree reaches toward another that does not reach back.

**Mage has no mutual pair at all.** Frost reaches toward Fire, Arcane reaches toward Fire and Frost, and neither Fire nor Frost reaches toward anything. Every mage cross-tree talent points at Fire or Frost and neither answers. So mage, the class with the healthiest trees and the most repetitive gameplay, is also the only class the rebuild gives no named hybrid to. That is a gap and it was invisible until the edges were mapped.

**Warlock is a chain, not a pair.** Demonology reaches toward Affliction and Destruction, Affliction reaches toward Destruction, and Destruction reaches toward nobody. Everything flows one way into the tree that already has Ruin. Given that warlock is the one vanilla class with two competing named builds, ending up with zero mutual pairs after a rebuild is a poor result.

**Rogue Combat reaches toward Assassination and Subtlety and neither reaches back**, so the tree everyone actually plays is the only rogue tree with no partner.

**Hunter Survival reaches toward both other trees and neither reaches back**, which repeats the vanilla problem that Survival exists next to the class rather than inside it.

The fix in each case is small: one node in the tree that does not reach back. Fire needs a talent reaching toward Frost. Destruction needs one reaching toward Affliction or Demonology. Assassination or Subtlety needs one reaching toward Combat. Marksmanship or Beast Mastery needs one reaching toward Survival.

**Four nodes across four classes turns four one-way chains into mutual pairs**, and takes the prediction from eleven named builds to fifteen.

## 5. Is a partial build competitive?

This is the part that is not computable and the document should not pretend otherwise.

What is settled: the depth dividend is linear, so spreading points costs no stats, and a 26/25 build receives the same curve total as a 31/20 build. The entire difference is which talents are owned. That removes the structural penalty vanilla imposes on hybrids, where the deep tree's back-loaded power made splitting a straightforward loss.

What is not settled is the tuning rule from talent design 5.6: two tier-five seats plus a tier-two should land in the same band as a capstone plus a tier-four. That is a target, not a result. Nobody has simmed it, the coefficients are unset, and it is the single assumption the whole fluid-tree argument rests on.

**If that rule holds, partial builds are competitive by construction.** If it does not, the eleven named builds above are eleven ways to be worse, and players will name them and then not play them, which is worse than not having them.

## 6. What can actually be predicted

**Confidently.** Which pairs exist, because the edges are mapped. That players will name builds after talent pairs rather than point splits, because vanilla already does. That mage and warlock currently produce no named hybrid, because their edges do not reciprocate. That the reachable shapes are 31/20, 30/21, 26/25, 26/21/4, 25/25/1, and 21/21/9, because that is arithmetic.

**Not confidently.** Whether any of them are good. Whether the simulator finds a single best pair per class and collapses the diversity, which is the specific failure mode named in talent design 5.3 and still unaddressed. Whether players use the names or invent their own, which they will.

**Not at all.** What the community calls them. SM/Ruin was not designed, it was named by players after the fact, and no amount of structure produces the name. The most this project can do is make sure there is something worth naming.
