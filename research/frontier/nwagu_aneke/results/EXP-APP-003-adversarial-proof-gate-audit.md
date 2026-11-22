# Adversarial audit: a false pass in EXP-APP-003's proof checker

Status: **internal reproducible methods finding; not a publication or global novelty claim**  
Date: 2026-11-22  
Scope: `scripts/prove_pagc_layer_safety.py` and `experiments/EXP-APP-003-layer-safety-proof/promotion_rules.json`

## Question

Does the existing `proof_passed` condition independently check the theorem's central premise: **no sequence of allowed promotions takes any non-source layer to `source_observed`**?

## Observation

The legacy generator tests for *presence* of two forbidden-rule declarations (`derived_fv_split -> source_observed` and `domain_mapped_from_pagc_count_layer -> source_observed`) and token uniqueness/counts. It does not traverse the full directed graph of **allowed** transitions. The published proof also refers to every non-source layer, but the explicit forbidden-rule list does not mention `publishable_claim` or `blocked`.

These omissions do **not** show the committed rules to be unsafe. They demonstrate that the verification procedure did not establish the premise for arbitrary future modifications.

## Falsification fixture (synthetic mutation; never committed to the canonical rules)

The committed allowed rules already contain:

```text
derived_fv_split
  -> domain_mapped_from_pagc_count_layer
  -> publishable_claim
```

Add exactly one allowed rule in memory (test-only):

```json
{"from": "publishable_claim", "to": "source_observed",
 "operation": "bad_retroactive_evidence_promotion", "requires": []}
```

The legacy forbidden-presence flags remain **true** even though the new allowed graph contains:

```text
derived_fv_split
  -> domain_mapped_from_pagc_count_layer
  -> publishable_claim
  -> source_observed
```

This is a counterexample to the sufficiency of the *checker*, not to the conditional theorem. The same omission applies to a direct `blocked -> source_observed` mutation.

## Repair

`scripts/validate_promotion_graph.py` checks the actual directed transition graph. It requires all endpoints to be declared layers, rejects rules that are simultaneously allowed and forbidden, and searches from **every** non-source layer for any path to `source_observed`. It returns a concrete witness path on failure. The EXP-APP-003 generator now includes this check in its `proof_passed` predicate.

The rule verifier is read-only. Existing historical results and decisions were **not** rewritten.

## Reproduction

```bash
python scripts/validate_promotion_graph.py
python -m unittest discover -s tests/research -p 'test_promotion_graph.py' -v
```

The test `test_published_gate_flags_do_not_detect_mutant` demonstrates that the legacy declarations are still present when the injected edge breaks reachability. The graph validator must reject that mutant and print the exact path. CI exercises both the committed baseline and the regression fixtures.

## Interpretation and limitations

- A useful methods result: checking that forbidden rules **exist** is weaker than checking that forbidden states are **unreachable**. This is an instance of a known class of state-machine verification errors, not a claimed new theorem.
- Verified transition safety remains only one precondition. The tool does not prove that runtime code enforces the transition rules, that provenance is authentic, that evidence is sound, or that domain semantics/rights are correct.
- Promoting any research claim remains subject to Etisiobi's independent source, review-team, authority, and publication gates.
- Further work should test whether actual applications enforce the machine-readable rules rather than merely storing them as research declarations.
