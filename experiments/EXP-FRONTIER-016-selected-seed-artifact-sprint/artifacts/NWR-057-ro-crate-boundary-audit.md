# NWR-057 RO-Crate Boundary Audit

Seed: `NWR-057`

Source question: Which metadata belongs in the package and which does not

Evidence layer: infrastructure

Claim ceiling: artifact_not_paper_candidate

## Bounded Artifact

This audit classifies package material by release risk before any external
sharing pathway.

| Material class | Internal package status | Boundary question |
|---|---|---|
| Validators | Candidate internal metadata | Do they expose private paths or source content |
| Manifests | Candidate internal metadata | Do they imply release maturity |
| Source notes | Case-by-case | Do they quote restricted material |
| Reader responses | Excluded for now | Do they contain personal data |
| Source images | Excluded for now | Are rights and authority unresolved |

## Evidence Layer

The artifact is infrastructure. It audits metadata boundaries, not release
readiness.

## Falsification Gate

The audit fails if a restricted or private material class can enter the package
without review.

## Rights And Authority Guardrail

Dataset-boundary review remains required before any public package action.

## What This Teaches Oroma

A trustworthy archive starts with exclusions as much as inclusions.

## Next Action

Compare crate parts against boundary review requirements.
