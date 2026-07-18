# LPE-Bench Validation Report

## Current Verdict

`PUBLIC_INSTRUMENT_DRAFT_NOT_FRONTIER_PROOF`

## What Has Been Validated

- The benchmark object is defined: Layer Promotion Error.
- The internal expanded dataset has `510` cases.
- The blind annotation packet has `360` unlabeled cases.
- Internal baselines run and produce held-out test metrics.
- Unicode/channel-risk audit runs as defensive publication hygiene.
- EXP-005 can now produce independent AI-review adjudication and local
  baseline scores.

## What Has Not Been Validated

- Human/domain gold labels.
- Generalization beyond Etisiobi-local cases.
- Real frontier-agent/model performance.
- Statistical confidence intervals for final public claims.
- Rights/authority approval for public examples.

## Current EXP-005 Result

- Annotation status: `ANNOTATION_ADJUDICATED_GOLD_CREATED_AI_REVIEW_NOT_HUMAN_FRONTIER_READY`
- Promotion-error Fleiss kappa: `0.6245`
- Severity Fleiss kappa: `0.5316`
- Score status: `SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM`
- Agent predictions: `2880`
- Best overall run: `codex_C0_no_layer_labels` / F1 `0.7692`
- Best Codex-agent run: `codex_C0_no_layer_labels` / F1 `0.7692`

Interpretation: the current score is useful for internal benchmark
development. It is not a frontier result because labels are AI-reviewer
adjudications and the agent runs are deterministic local baselines, not
external frontier agents.

## Defects / Risks

| Risk | Status | Required Fix |
|---|---|---|
| Construct leakage from typed metadata | Open | Score metadata-free conditions against frozen labels. |
| Heuristic labels | Open | Use independent annotators and adjudication. |
| Internal-only source distribution | Open | Add external non-Etisiobi research-agent outputs. |
| Publication rights | Open | Authority review before public examples. |
| Overclaiming from perfect typed baseline | Controlled | Manifest blocks frontier-proof status. |

## Promotion Rule

No paper may cite LPE-Bench as a frontier result until this report
records passing independent labels, real baselines, and review-team
approval.
