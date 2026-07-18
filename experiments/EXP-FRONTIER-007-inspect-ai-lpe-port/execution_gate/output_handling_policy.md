---
type: output_handling_policy
experiment_id: EXP-FRONTIER-007
status: pending_user_approval
created: "2026-06-22"
claim_ceiling: eval_harness_relevance_not_model_claim
---

# Output Handling Policy

Any future Inspect execution output must be treated as evaluation-infrastructure
evidence only. The claim ceiling is `eval_harness_relevance_not_model_claim`.

## Allowed Output Claims

- The adapter ran or failed under a named environment.
- A model or agent response matched or missed the expected LPE label.
- The formal harness was easier or harder to audit than the manual prompt
  negative control.

## Disallowed Output Claims

- The run proves Nwagu Aneke source facts.
- The run replaces human/domain review.
- The run settles rights or authority.
- The run validates publication, release, or article promotion.
- The run upgrades derived `27/216` language into a source-observed count.

## Storage Rules

- Do not commit secrets.
- Do not commit raw provider credentials, request headers, or private contact
  data.
- Do not add private or restricted source data.
- Store only prompts, model outputs, scores, error logs, environment metadata,
  and redacted execution notes.

## Review Rule

Before any output is cited outside this experiment directory, review it for
secret leakage, source-layer promotion, rights/authority risk, and claim-ceiling
violations.
