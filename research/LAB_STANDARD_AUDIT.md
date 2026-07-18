# Lab Standard Audit

Date: 2026-06-21

## Finding

The lab had accumulated strong infrastructure but weak institutional discipline.
The same repository could contain:

- working-paper drafts rendered as polished PDFs;
- stale vault notes claiming arXiv readiness;
- score histories that previously rewarded thin article bodies;
- many simultaneous article branches without portfolio promotion discipline.

That is not an A+ lab. It is an artifact factory with partial safeguards.

## Root Cause

The control plane was reactive. It added validators after each visible failure
instead of enforcing a single promotion system before drafting and PDF generation.

## Required Structural Fix

The lab now needs one canonical rule:

```text
No output may look more mature than its evidence stage.
```

If a branch has not passed `PAPER_CANDIDATE`, it may be a research note or
working draft, but not an impact article. If a branch has not passed
`SUBMISSION_CANDIDATE`, it may not claim human arXiv/submission readiness.

## Current Nwagu Aneke Decision

The ten article package is downgraded to:

```text
WORKING_PAPER_SET_NOT_IMPACT_READY
```

Only two branches should receive near-term hardening:

1. `ARTICLE-NA-002` — count-layer drift.
2. `ARTICLE-NA-010` — layer-safe generative design.

The remaining eight branches stay parked as research branches until they produce
article-specific results.

## What Must Happen Next

1. Build full source-critical dossier for the Nwagu Aneke artifact.
2. Run article-specific prior-art sweep for the two promoted branches.
3. Replace generic article prose with field-specific argument and methods.
4. Produce at least one external-facing result per branch.
5. Run review-team trace before any readiness language.

## Anti-Whack-A-Mole Rule

Do not patch individual article text in response to isolated criticism unless
the patch also improves the stage-gate evidence. If it does not change evidence,
novelty, reproducibility, rights, or reviewer survivability, it is cosmetic.

