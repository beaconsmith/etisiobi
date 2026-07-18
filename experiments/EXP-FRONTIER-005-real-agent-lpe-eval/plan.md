# EXP-FRONTIER-005: Real Agent LPE Evaluation

## Purpose

Convert LPE-Bench from an internal instrument into a frontier-candidate
benchmark by testing real research agents against frozen, independently reviewed
Layer Promotion Error labels.

## Research Question

When AI research agents write claims from mixed source, derived, speculative,
blocked, and design-hypothesis evidence, how often do they promote weaker layers
into stronger claims?

## Required Inputs

- `experiments/EXP-FRONTIER-003-blind-lpe-annotation/annotation_queue.csv`
- Three independent annotation files from:
  - domain/source reviewer,
  - methods reviewer,
  - adversarial impact-journal reviewer.
- An adjudicated gold file:
  `experiments/EXP-FRONTIER-005-real-agent-lpe-eval/gold_labels.csv`

## Conditions

| Condition | Agent Context | Hypothesis |
|---|---|---|
| C0 | No explicit layer labels | Highest LPE rate. |
| C1 | Source/derived/speculative labels visible | Lower LPE rate. |
| C2 | Layer labels + claim-gate rules | Lower severity-weighted LPE rate. |
| C3 | Layer labels + claim gate + adversarial reviewer prompt | Best overall but possible over-restriction. |

## Agent Outputs

Each agent must produce:

- a short manuscript-style paragraph,
- extracted claims,
- self-assigned evidence layer,
- confidence,
- cited source row IDs.

## Metrics

- LPE precision/recall/F1 against adjudicated gold labels.
- Severity-weighted LPE rate.
- Source-observed false assertion rate.
- Derived-layer preservation rate for 27/216 claims.
- Over-restriction rate: valid derived/design claims incorrectly blocked.
- Reviewer catch rate.

## Baselines

- `majority_negative`
- `lexical_only`
- `metadata_free_text`
- `rank_only_metadata` as an upper-bound typed baseline, not a deployable model.
- `claim_gate_rule_set`

## Statistical Requirements

- Report Wilson confidence intervals for proportions.
- Report bootstrap confidence intervals for F1/MCC.
- Use the test split only once after all prompts and thresholds are frozen.

## Promotion Criteria

This experiment can promote LPE-Bench only if:

- independent labels are complete,
- inter-annotator agreement is reported,
- labels are adjudicated and frozen,
- at least three agent configurations are evaluated,
- all raw prompts, outputs, and scores are saved,
- rights/authority review approves public release of examples or examples are
  safely redacted.

## Failure Criteria

The experiment must remain blocked or negative if:

- annotators disagree too strongly to adjudicate,
- public examples cannot be released or redacted safely,
- agent prompts leak the gold labels,
- the benchmark is solved only by typed metadata,
- the result does not generalize beyond Etisiobi-local examples.

## Expected Output Files

```text
experiments/EXP-FRONTIER-005-real-agent-lpe-eval/
  plan.md
  annotation_inputs/
  gold_labels.csv
  agent_runs/
  raw_outputs.jsonl
  scores.json
  confidence_intervals.json
  analysis.md
  decision.md
```

