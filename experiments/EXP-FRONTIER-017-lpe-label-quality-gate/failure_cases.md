# LPE Label Quality Gate Failure Cases

Claim ceiling: `quality_gate_pilot_not_paper_result`.

This note defines how the LPE label quality gate should fail. A failed gate is
useful: it prevents weak labels from silently becoming benchmark evidence.

## Failure Modes

| Failure mode | Example signal | Required response |
|---|---|---|
| Floating label | No source or case anchor | Block from scoring evidence |
| Layer blur | Input and output layers are missing | Send to adjudication |
| Disagreement erasure | Review disagreement has no state | Preserve disagreement before score use |
| Public leakage | Row still needs rights review | Block public release |
| Score overreach | Metric treated as paper evidence | Demote to internal pilot |

## What This Teaches Oroma

The LPE label quality gate treats disagreement and blocked release as useful
states. Oroma should do the same for civic records: uncertainty is not a bug if
the system can route it.

## Next Action

Review the 70 unresolved full-gate rows: 28 require adjudication and 42 are
blocked from public release until rights, authority, or public-scope decisions
are recorded.
