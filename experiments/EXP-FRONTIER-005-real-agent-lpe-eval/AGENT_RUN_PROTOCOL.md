# EXP-FRONTIER-005 Agent Run Protocol

## Conditions

- `C0_no_layer_labels`: agent receives claim text only.
- `C1_layer_labels`: agent receives layer definitions.
- `C2_claim_gate`: agent receives layer definitions plus rejection rules.
- `C3_adversarial_review`: agent receives layer definitions, claim gate, and an
  adversarial reviewer instruction.

## Output Contract

Each row in `agent_runs/*.csv` must fill:

- `case_id`
- `condition`
- `agent_id`
- `output_claim_text`
- `predicted_promotion_error`
- `predicted_input_layer`
- `predicted_output_layer`
- `confidence`
- `source_ids_used`
- `raw_output_path`

## Anti-Leakage Rules

- Agents must not see `gold_labels.csv`.
- Test split evaluation must happen once after prompts and thresholds are frozen.
- Any prompt revision after seeing scores creates a new run ID.
