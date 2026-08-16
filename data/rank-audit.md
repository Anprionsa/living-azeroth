# Rank-clause audit

August 2026, regenerated after the finalization pass. The calculator decomposes a multi-rank talent's text into one bullet per rank, splitting on sentences and "then" chains, and inherits the first clause's subject where a later clause starts with a verb. This report lists where the data does not decompose: clause count differs from rank count, so the calculator falls back to the plain tooltip text.

Multi-rank talents in the shown configurations: 548. Decomposing cleanly: 548.

No talent in the shown configurations mismatches its rank count. The August finalization pass restaged every mismatched tooltip against its design chapter, with the full-rank end state held fixed.

## Per-rank magnitude gaps

Coverage after the finalization pass: 1901 of 1917 rank clauses (99%). Authored effects carry explicit rank bindings where a clause describes them; display annotations verified against their clause carry source:"reviewed" and are never simulated; 0 machine-drafted effects remain, rendering with a (drafted) suffix.

The ranks below remain unbound. Each names a mechanic the closed effect vocabulary cannot express; extending the vocabulary is a design decision, not an authoring gap.

| Tree | Talent | Ranks | Unbound ranks |
|---|---|---|---|
| mage-frost-rebuilt | Frozen Hour | 2 | 2 |
| paladin-holy-rebuilt | Beacon | 5 | 1 |
| paladin-retribution-rebuilt | Pursuit of Justice | 2 | 2 |
| paladin-retribution-rebuilt | Bulwark of Faith | 3 | 2 |
| warlock-destruction-rebuilt | Improved Shadow Bolt | 5 | 4 |
| warrior-protection-rebuilt | Sword and Board | 3 | 1 |
| blackguard | Morbid Strength | 5 | 4 |
| necromancy | Dark Command | 2 | 1 |
| chronomancer | Recollection | 5 | 1 |
| chronomancer | Dilation | 3 | 1 |
| chronomancer | Unwind | 4 | 4 |
| chronomancer | Frozen Moment | 2 | 2 |
| chronomancer | Timeless | 5 | 5 |
| dreamer | Verdance | 4 | 1 |
| radiance | Effulgence | 5 | 4 |
| radiance | Doctrine | 5 | 3 |
