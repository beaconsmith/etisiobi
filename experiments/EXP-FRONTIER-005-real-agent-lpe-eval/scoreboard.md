# EXP-FRONTIER-005 Scoreboard

Status: `SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM`

| Rank | Condition | Agent | F1 | MCC | Precision | Recall | FP | FN | Derived Preservation |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `C0_no_layer_labels` | `codex_C0_no_layer_labels` | 0.7692 | 0.7248 | 0.75 | 0.7895 | 15 | 12 | 0.0 |
| 2 | `C2_claim_gate` | `codex_C2_claim_gate` | 0.5316 | 0.5564 | 0.9545 | 0.3684 | 1 | 36 | 0.3871 |
| 3 | `C0_no_layer_labels` | `baseline_C0_no_layer_labels` | 0.5039 | 0.4022 | 0.4571 | 0.5614 | 38 | 25 | 0.3226 |
| 4 | `C1_layer_labels` | `baseline_C1_layer_labels` | 0.4662 | 0.3536 | 0.4079 | 0.5439 | 45 | 26 | 0.3226 |
| 5 | `C2_claim_gate` | `baseline_C2_claim_gate` | 0.4571 | 0.3407 | 0.3855 | 0.5614 | 51 | 25 | 0.3226 |
| 6 | `C3_adversarial_review` | `baseline_C3_adversarial_review` | 0.4103 | 0.2782 | 0.3232 | 0.5614 | 67 | 25 | 0.3226 |
| 7 | `C1_layer_labels` | `codex_C1_layer_labels` | 0.4054 | 0.4415 | 0.8824 | 0.2632 | 2 | 42 | 0.6452 |
| 8 | `C3_adversarial_review` | `codex_C3_adversarial_review` | 0.2899 | 0.3434 | 0.8333 | 0.1754 | 2 | 47 | 0.2903 |

## Interpretation

This is an internal benchmark result against AI-reviewer adjudicated labels.
It is not a frontier claim because human/domain gold labels, external frontier model runs, and rights/authority review remain incomplete.
