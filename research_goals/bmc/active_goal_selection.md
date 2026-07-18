# BMC Active Goal Selection

## Selected Active Goals

| Goal | Reason | Dependency State |
|---|---|---|
| GOAL-001 | Creates the BMC substrate all other goals depend on. | No prior BMC dependency. |
| GOAL-002 | Resolves row/vowel/cell/foundation-count drift before grammar or compression work. | Depends on GOAL-001 seed. |
| GOAL-003 | Turns the BMC into a paper-claim gate before manuscript generation. | Depends on GOAL-001 seed. |

## Blocked or Pending

- GOAL-004 is blocked until GOAL-002 stabilizes count layers.
- GOAL-005 is blocked until GOAL-004 yields a grammar or negative grammar result.
- GOAL-006 is pending until GOAL-003 creates claim-gate records.
- GOAL-007 is pending until GOAL-006 produces a certainty model.
- GOAL-008 is pending until GOAL-007 produces graph-queryable BMC objects.
- GOAL-009 is pending until GOAL-003 and GOAL-006 link claims and certainty to authority.
- GOAL-010 is blocked until GOAL-001 through GOAL-009 pass or produce explicit negative results.

## Next Experiment

`experiments/EXP-BMC-001/`: generate and validate `corpus/base_modifier_cache.jsonl` from repo-local artifacts.

## Next Human Review Needed

Source transcription and exact-count review for GOAL-001/GOAL-002, followed by authority/cultural review before public release use.
