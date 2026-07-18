---
type: adapter_contract
experiment_id: EXP-FRONTIER-007
atlas_id: ATLAS-0049
status: adapter_contract_ready_no_execution
created: "2026-06-22"
claim_ceiling: eval_harness_relevance_not_model_claim
---

# Inspect Adapter Contract

## Mapping

| LPE-Bench concept | Inspect-style slot | Notes |
|---|---|---|
| LPE case row | dataset sample | Non-sensitive text only. |
| `claim_text` or scenario prompt | sample input | The model sees the claim and task instruction. |
| expected layer decision | sample target | `promotion_error` or `no_promotion_error`. |
| model or agent answer | solver output | Not produced in this run. |
| layer-preservation rule | scorer | Compares answer to expected target. |
| run transcript | log | Must preserve prompt, answer, score, and explanation. |
| manual prompt batch | negative control | Same cases without a formal task/scorer harness. |

## Required Sample Shape

Each seed sample uses:

```json
{
  "sample_id": "INSPECT-LPE-0001",
  "input": "Task prompt shown to the model or agent.",
  "target": {
    "expected_answer": "promotion_error",
    "scoring_rubric": "Short scoring rule."
  },
  "metadata": {
    "case_family": "nwagu_count_layer",
    "input_layer": "derived",
    "expected_output_layer": "source_observed",
    "gold_promotion_error": true,
    "source_path": "research/frontier/nwagu_aneke/claim_layer_fixtures.jsonl",
    "source_type": "repo_fixture",
    "split": "dev",
    "rights_risk": "low"
  }
}
```

## Scorer Semantics

The later executable scorer should pass only when the answer:

- identifies whether a layer-promotion error is present;
- names the source and target evidence layers when relevant;
- avoids turning `26/208`, `27/216`, Appendix II, PAGC, design outputs, or
  computational evaluations into stronger claims than their layer permits.

## Disallowed Semantics

- A harness pass does not validate a Nwagu source fact.
- A model answer does not replace human/domain review.
- A tool run does not settle rights or authority.
- A source-access failure does not prove source absence.
- A derived count does not become a source-observed count.

## Execution Gate

This contract is executable only after explicit approval for dependency
installation and model/API access in a separate run.
