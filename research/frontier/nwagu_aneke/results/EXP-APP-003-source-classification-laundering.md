# EXP-APP-003: Source-layer classification laundering (internal result)

Date: 2026-11-22  
Status: **reproduced mutation, targeted repair; NOT a historical-source or global novelty claim**  
Scope: `EXP-APP-003` qualified-token proof generator.

## Question

Can a malformed input claim to be source-observed evidence while still satisfying the existing proof's count and qualified-identifier tests?

## Observed structure in the checked-in artifacts

- Source-observed layer: **208** records.
- Derived layer: **216** records: **200 unchanged carry-through records** plus **16 explicitly recorded f/v split children of eight combined source cells**.
- Domain-mapped layer: **48** derived design hypotheses. These are *applications/analogies*, not Nwagụ Aneke source observations.
- Each derived record carries a `source_bmc_id` resolving to a source record. The 200 unchanged records have no explicit `derived_rule` because they are identity carry-through; the 16 actual split children carry `split f/v row into f and v`.

The source/derived distinction matters: 216 entries in a derived representation do not constitute 216 independent historical observations or 216 independent transformations.

## Mutation that defeats the old gate

Choose a source cell and the matching unchanged derived cell with the same local ID. Swap **only** their `layer` fields in the two input arrays; leave the source-observed boolean untouched.

Under the old checks:

1. The total source count remains 208 and the derived count remains 216.
2. Qualified IDs remain pairwise unique; `source_observed::ID` and `derived_fv_split::ID` have merely exchanged which input carries them.
3. The allowed-promotion graph is unchanged and safe.
4. The old forbidden-rule declarations are still present.

Nevertheless the records' declared layer now contradicts both the input provenance boundary and the explicit `source_observed` flags. A blanket `qualify(row)` transformation marks both as `layer_safety_status=qualified` despite this inconsistency.

This is a **checker incompleteness counterexample**, not evidence of actual tampering in the committed dataset.

## Repair

`scripts/validate_pagc_token_lineage.py` now separately checks:
- source records are explicitly source-observed and have unique source BMC and token identities;
- derived records remain explicitly derived, reference a source parent, and are either unchanged carry-through or a correctly specified f/v split;
- each f/v source has exactly two correctly formed children; each ordinary source has exactly one unchanged child;
- domain-mapped design records remain explicitly hypotheses rather than source observations;
- derived and domain token identities remain unique.

`scripts/prove_pagc_layer_safety.py` now requires both the previously merged graph-reachability guard and this lineage check before reporting `proof_passed=true`. The validator reports 200 carry-through and 16 split children separately.

## Reproduce

```bash
python3 scripts/validate_pagc_token_lineage.py
python3 -m unittest discover -s tests/research -p 'test_pagc_token_lineage.py' -v
python3 scripts/prove_pagc_layer_safety.py
```

All mutations are in-memory test fixtures. The canonical source datasets and historical decision log remain unchanged.

## Boundary

The validator checks internal consistency against the source-layer input artifact. It **does not independently authenticate the historical chart, prove community authority, establish source rights, or guarantee a runtime consumer applies these rules**. Those require separate source-critical and downstream application reviews. No paper or public-release promotion follows from this finding.
