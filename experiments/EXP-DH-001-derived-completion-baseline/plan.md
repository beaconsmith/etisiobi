# EXP-DH-001: Derived Completion Toy Baseline

## Purpose

Test DH-001 as a formal hypothesis without weakening the Nwagụ Aneke source
boundary.

The experiment compares three small models on a constructed role-recovery task:

1. `source_26x8_collapsed`: preserves the source-observed 26-row view and cannot
   distinguish f-role from v-role inside the collapsed row.
2. `derived_27x8_role_split`: preserves the source count as source metadata but
   adds a derived f/v role split for the formal task.
3. `shuffled_completion`: preserves a 27-row-looking completion but assigns
   f/v roles by a deterministic shuffled baseline.

## Non-Negotiable Boundary

The source-observed layer remains:

```text
26 rows x 8 vowel/modifier columns = 208 records
```

The derived completion remains:

```text
27 rows x 8 modifier slots = 216 derived formal slots
```

The second statement is not a source claim.

## Metrics

- `role_recovery_accuracy`: share of role-labeled cases where the model recovers
  the expected f/v role.
- `role_collision_count`: number of source-row collisions after model mapping.
- `source_claim_safety`: whether the model reports the source layer as 26 x 8 =
  208 and keeps 27 x 8 in the derived lane.
- `counterexample_gate_accuracy`: share of source-promotion counterexamples and
  safe boundary statements classified with the expected gate.
- `source_constraint_violations`: count of current transcription constraints
  violated by the model.
- `source_record_gate_accuracy`: share of reviewed source-record cases preserved
  without promotion.
- `adversarial_overclaim_rejections`: number of adversarial variants where the
  model refuses to infer value beyond available evidence.

## Expected Outcome

The derived split should outperform the collapsed source view on the constructed
role-recovery task. If it does not, DH-001 stays parked. If it does, DH-001
earns only a toy-model result and needs counterexamples plus non-toy
source-transcription constraints before article work.

## Counterexample Screen

The experiment now includes six source-boundary counterexamples and six
source-transcription constraints. The screen rejects unsafe source-promotion
claims such as source-observed 27 rows or 216 source records, while preserving
safe statements that label the f/v split as derived.

## Source-Record And Adversarial Screen

The next screen adds eight reviewed source-record cases and six adversarial
variants. These variants remove role labels or present only source-level
evidence. The correct decision is `insufficient_evidence`, because DH-001 has
not yet shown that the f/v split adds value beyond explicit role labels.
