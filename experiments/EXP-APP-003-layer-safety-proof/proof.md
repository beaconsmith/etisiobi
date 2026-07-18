# Layer-Safety Theorem for PAGC Applications Grammar

## Status

`PROOF_ACCEPTED_WITH_ASSUMPTIONS`

## Definitions

Let a design object be a tuple:

```text
o = (qualified_id, local_id, layer, base, modifier, provenance)
```

Let the layer set be:

```text
L = {source_observed, derived_fv_split, domain_mapped_from_pagc_count_layer, speculative, publishable_claim, blocked}
```

Let a valid grammar operation be one listed in `promotion_rules.json`.

## Theorem

In the PAGC applications grammar, if all objects use `qualified_id = layer::local_id` and the promotion matrix forbids promotion from `derived_fv_split`, `domain_mapped_from_pagc_count_layer`, or `speculative` to `source_observed`, then no valid sequence of grammar operations can turn a derived, domain-mapped, or speculative object into a source-observed object.

## Proof

Every object contains an explicit layer. The qualified identifier includes the layer, so two objects with the same local identifier but different layers are distinct objects.

The only way for an object's layer to change is by a valid promotion operation. By construction, the promotion matrix contains no valid operation from `derived_fv_split` to `source_observed`, no valid operation from `domain_mapped_from_pagc_count_layer` to `source_observed`, and no valid operation from `speculative` to `source_observed`.

Consider any finite sequence of valid operations applied to an object whose initial layer is not `source_observed`. We prove by induction on the length of the operation sequence that the resulting object is not `source_observed`.

Base case: with zero operations, the object's layer is its initial non-source layer, so it is not `source_observed`.

Inductive step: assume after `n` valid operations the object is not `source_observed`. The `(n+1)`-th operation is valid only if it appears in the promotion matrix. Since the promotion matrix forbids every non-source-to-source promotion relevant to this grammar, the operation cannot output `source_observed`. Therefore the object remains not `source_observed`.

By induction, no finite valid operation sequence can convert a derived, domain-mapped, or speculative object into a source-observed object.

## Counterexample Without Qualified IDs

The verifier found local token ID collisions across source and derived layers. Therefore a system keyed only by local `token_id` can confuse source and derived objects. The theorem depends on layer-qualified IDs or an equivalent type system.

## Novelty Claim

This proof is novel inside Etisiobi/PAGC because it formally connects the Nwagu Aneke count-layer decision to a system-design safety invariant: applications may use the derived 27/216 layer, but the grammar prevents it from being promoted back into source evidence.

This is not claimed as a globally first theorem in type systems, state machines, or formal methods.
