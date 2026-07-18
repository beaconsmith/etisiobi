# EXP-APP-002 Analysis

Generated governance grammar:

- Bases: `6`
- Modifiers: `8`
- State tokens: `48`
- Required transitions: `7`
- Blocked or partial transitions: `7`

Main finding:

The PAGC-derived grammar is useful when it turns a vague product gap into a missing transition guard. Example: DRL-01 is no longer just "dispute documentation incomplete"; it becomes:

`DisputeCase.Created -> DisputeCase.Closed` requires `findings`, `resolution`, and `evidence_refs`.

That is an implementable acceptance test.

Research value:

The grammar creates a bridge between cultural/source-layer formalization and product evidence design without claiming that the source layer itself directly encodes governance.
