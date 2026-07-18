---
type: execution_risk_register
experiment_id: EXP-FRONTIER-007
status: pending_user_approval
created: "2026-06-22"
claim_ceiling: eval_harness_relevance_not_model_claim
---

# Execution Risk Register

| Risk | Impact | Control | Current State |
|---|---|---|---|
| Dependency drift | Later Inspect behavior may differ from the source-reviewed documentation. | Record dependency version and lockfile only in an approved execution cycle. | Pending. |
| Secret leakage | Model/API key could be written to logs or shell history. | Use approved secret handling and inspect output before commit. | Pending. |
| Private data leakage | A future operator could add private or restricted source data. | Use only packaged seed cases unless rights/authority review says otherwise. | Pending. |
| Label overtrust | Heuristic seed labels could be mistaken for gold labels. | Require human/domain review before claims about label quality. | Pending. |
| Harness overclaim | A pass could be misread as proving source facts or model reliability. | Claim ceiling remains `eval_harness_relevance_not_model_claim`. | Pending. |
| Negative control skipped | The run could claim harness value without comparing manual prompts. | Manual prompt negative control is required. | Pending. |

## Non-Negotiables

- no dependency installation in the current state;
- no model/API call in the current state;
- no private or restricted source data;
- no paper or public-release claim;
- human/domain review before gold-label language.
