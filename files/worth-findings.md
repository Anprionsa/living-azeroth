# Recommended Fixes

**August 2026**

*What the capstone-free sweep surfaced, measured properly, with recommendations.*

---

## 1. Two flaws in my own measurement, found before recommending anything

The first sweep reported **176 of 277 talents worth exactly zero**, which included Bloodthirst, Shield Slam, Adrenaline Rush and Arcane Power. That is not credible and the sweep was wrong twice.

**It kept `grant` effects when stripping a talent.** For an ability-granting talent the grant is the entire value, so stripping everything else and leaving the grant measures nothing.

**It measured healing and tank trees with the damage simulator.** Every talent in Holy priest, Restoration druid, Restoration shaman, Holy paladin, Protection warrior and Protection paladin read zero for that reason alone.

Corrected: **89 of 206.**

## 2. The largest single fix: rotation follows the build, not the class

The simulator used one rotation per class. **Druid has a feral list that had never been used**, so a Feral build was measured against a caster rotation casting Wrath and Starfire.

Feral now casts Ferocious Bite, Shred and Rip, and reads **440 damage per second against the 290 it read as a caster**. Ten Feral talents went from zero to contributing.

**Recommendation: this is already applied.** Any class with more than one role needs its rotation chosen by which tree the build is deep in, and Shaman, Priest and Paladin all have healing lists that were equally unused.

## 3. The remaining 89, classified

| Cause | Share | Recommendation |
|---|---|---|
| Pet tag, build has no pet | largest | model a default pet per class |
| Ability not in this build's rotation | moderate | expected and correct |
| Tag no ability carries in this build | small | audit already catches the global case |
| Genuinely inert | remainder | rewrite |

### 3.1 Pet talents are the biggest group and the cheapest fix

Warlock Demonology reads ten zeros, Hunter Beast Mastery seven. **Both classes have a permanent pet in vanilla and neither summons one in the simulator unless a talent grants it.**

**Recommendation: give Warlock and Hunter a pet by default**, as Necromancy already gets one through Raise Skeleton. That is one line per class and it makes seventeen talents measurable.

### 3.2 Ability-scoped talents in a build that does not cast that ability

Improved Fireball reads zero in an Arcane build because the rotation casts Frostbolt. **That is correct behaviour and should not be fixed.** A talent that improves an ability you do not use is worth nothing, and a player would not take it.

The concern is only whether the selector takes it anyway. It does, because `_value` scores a talent by its effects rather than by whether the build uses the ability. **Recommendation: `_value` should score an ability-scoped effect at zero when that ability is not in the build's rotation.** That is a selector fix, not a design one.

### 3.3 The genuinely inert ones

**Rupture Line, Crippling Grip, Death Sentence, Sundering Blows, Bloodletting, Unbridled Wrath, Opportunity, Ruthlessness, Relentless Strikes, Initiative, Master of Deception, Nature's Grasp, Natural Shapeshifter.**

These do something the simulator can express and it amounts to nothing measurable. **Recommendation: rewrite them, and the shape to reach for is the one the project has already proven twice.** A scenario lever costs nothing where it does not apply and gains a great deal where it does: periodic cleave gained 18.8 points at zero sustained cost, and an opening window scored 4.8 burst per point.

Several of these are movement or control talents, which is exactly where a movement or switching lever belongs.

## 4. The Druid finding, which is separate and more serious

**Seven distinct results from 114 capstone-free shapes.** The point split barely determines what a Druid build does.

That measurement predates the rotation fix and should be rerun, since Feral was being measured as a caster throughout. **Rerun, and it did improve: 7 distinct results became 15, and 99 within 7% became 19.**

That is a different diagnosis. Druid is no longer indifferent, it is now **strongly capstone-dependent**: the median capstone-free build reads -34.4%, the worst figure of any class measured. Feral 30 / Balance 21 ties the capstone exactly and everything else falls away sharply.

**The earlier reading was an artefact of measuring a Feral build with a caster rotation.** Both the finding and its opposite came from the same broken measurement, which is worth stating plainly: **the Druid conclusion in `nocapstone-results.md` was wrong and should be read with this correction.**

## 5. Order

1. **Rerun the Druid sweep.** It may already be fixed and it is one command.
2. **Default pets for Warlock and Hunter.** Seventeen talents, one line each.
3. **Selector scores ability-scoped effects by whether the build uses the ability.** Stops the build taking talents it cannot benefit from.
4. **Rewrite the thirteen genuinely inert talents** as scenario levers.
5. **Sweep the healing and tank trees** with `heal.py` and `tank.py`, which has never been done and which the first attempt got wrong.
