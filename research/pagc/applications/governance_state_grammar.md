# PAGC-Inspired Governance State Grammar

Status: `ACTIVE_PRODUCT_RESEARCH_BRANCH`

This grammar maps Oroma/OGI governance evidence into base x modifier state tokens. It is inspired by the accepted PAGC count-layer foundation but does not claim that Nwagu Aneke directly encodes governance semantics.

## Core Discovery

OGI computability gaps can be represented as missing transitions:

- DRL-01 needs `DisputeCase.Created -> DisputeCase.Closed` guarded by findings, resolution, and evidence references.
- TTI-01 needs `TreasuryMovement.Created -> TreasuryMovement.ProvenanceAnchored` guarded by purpose, proposalId, and blockRef.
- TTI-02 needs `TreasuryMovement.EvidenceAttached -> TreasuryMovement.Closed` guarded by a solvency-proof event.
- CPS-01 needs `IchiCredential.AuthorityChecked -> IchiCredential.Exported`.
- FID-01 needs `ParticipantOnboarding.Created -> ParticipantOnboarding.EvidenceAttached`.

## Result

See `experiments/EXP-APP-002-governance-state-grammar/results.json`.
