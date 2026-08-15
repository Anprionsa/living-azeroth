# What -34.8% Actually Measures

**August 2026**

*Checking a number before treating it as a problem.*

---

## 1. The short answer: it is mostly measuring something that should be true

The Druid median of -34.8% is the middle of **114 shapes, most of which put points in Restoration.** Restoration is a healing tree, and a damage build spending 21 points there is spending them on nothing.

Splitting the distribution shows it plainly:

| Druid shape | Result |
|---|---|
| Feral 30 / Balance 21 | **+0.0%**, ties the capstone |
| Feral 26 / Balance 25 | -2.1% |
| Feral 21 / Balance 20 / Resto 10 | -6.6% |
| Feral 30 / Resto 21 | **-27.0%** |
| Feral 26 / Resto 25 | -28.4% |

**Every shape pairing Feral with Balance sits between 0 and -8%. Every shape pairing it with Restoration falls off a cliff.**

That is not a design fault. A druid who spends 21 points in the healing tree and expects damage should get less damage.

## 2. Measured properly

Restricting to shapes that use only a class's damage trees:

| Class | Damage trees | All shapes | Damage-tree shapes only |
|---|---|---|---|
| Rogue | 3 | -8.1%, 55 of 114 within 7% | -8.1%, 55 of 114 |
| Mage | 3 | -14.8%, 31 of 114 | -14.8%, 31 of 114 |
| Warlock | 3 | -24.6%, 9 of 114 | -24.6%, 9 of 114 |
| **Druid** | **2** | -34.7%, 25 of 114 | **-18.4%, 2 of 4** |
| **Warrior** | **2** | -19.5%, 5 of 114 | **-3.7%, 2 of 4** |
| **Hunter** | **2** | -15.2%, 27 of 114 | **-1.5%, 4 of 4** |

**The classes with three damage trees have a large capstone-free design space. The classes with two have almost none, because there are only four shapes to have.**

Rogue's 55 of 114 against Druid's 25 is not Rogue being better designed. **It is Rogue having three damage trees and Druid having two.**

## 3. So is anything actually wrong?

**Warlock.** Three damage trees and only 9 of 114 shapes within 7%, the worst ratio of any class with the room to do better. Mage has the same structure and reaches 31. That gap is a real finding and it is the one worth pursuing.

**Warrior at 2 of 4** is worth a look but the sample is four shapes, so it says very little.

**Druid and Hunter are fine.** Both reach 0 to -2% on their best capstone-free shape, which is what the question was asking.

## 4. What I got wrong

I reported the Druid median as a finding twice: first as "nothing matters", then as "strongly capstone-dependent". **Both readings took the median of a population that is mostly off-role builds.**

The median across all 114 shapes is not a measure of design health. It is a measure of how many ways there are to spend points badly, and a class with a healing tree has more of them.

**The number to watch is the best capstone-free shape and how many shapes cluster near it**, restricted to trees the build can actually use.

## 5. Corrected headline

| Class | Best capstone-free build |
|---|---|
| Rogue | +5.3%, three-tree split |
| Mage | +3.3% |
| Druid | +0.0%, ties |
| Warrior | -0.1%, ties |
| Hunter | -1.5% |
| Warlock | -3.8% |

**Every class has at least one capstone-free build within four percent of its best capstone build.** That is the answer to the original question, and it is a better result than any of the three medians I quoted.
