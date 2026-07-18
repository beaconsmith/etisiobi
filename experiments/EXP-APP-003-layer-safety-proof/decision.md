# EXP-APP-003 Decision

Decision: `PROOF_ACCEPTED_WITH_ASSUMPTIONS`

## Novel proof obtained

We have a bounded proof: **Layer-Safety Theorem for PAGC Applications Grammar**.

It proves that, under a layer-qualified token representation and a forbidden-promotion matrix, derived 27/216 objects cannot become source-observed 26x8 objects through valid grammar operations.

## Discovery

The proof found a real representation hazard: local token IDs collide across source and derived layers. Therefore any application system that uses only local token IDs is unsafe. The repair is `qualified_token_id = layer::local_token_id`.

## Verification

- Unqualified collision count: `200`
- Qualified token count: `472`
- Qualified unique count: `472`
- Source count: `208`
- Derived count: `216`
- Governance/domain mapped count: `48`
- Proof passed: `True`

## What it does not prove

- It does not prove governance improvement.
- It does not prove Nwagu Aneke directly encodes governance semantics.
- It does not prove E6, universal compression, or glyph-shape grammar.
- It does not claim global mathematical novelty.
