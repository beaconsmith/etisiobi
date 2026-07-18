# EXP-0002

## Linked goal

GOAL-0002

## Hypothesis

A machine-readable gate audit can become a reusable research-lab contribution.

## Baseline

Current claim/evidence state from `corpus/claims.jsonl` and linked repo files.

## Intervention

Diff portfolio, runtime manifests, promote gates, source gaps, and submission rules.

## Controlled variables

- Source locator and version
- Corpus or fixture identity
- Script version
- Random seed where applicable

## Metrics

- Claim confidence delta
- Reproducibility completeness
- Negative-result clarity

## Seeds

- `20260528` where randomized computation is introduced.

## Commands

See `commands.sh`.

## Expected runtime/cost

Dry-run or manual audit first. No paid compute approved.

## Success threshold

The experiment produces a decision artifact and updates the linked claim state.

## Failure threshold

The method cannot distinguish support from refutation or relies on hidden assumptions.

## Rollback plan

Generated artifacts can be regenerated; code changes require git diff review.

## Human approval needed?

no
