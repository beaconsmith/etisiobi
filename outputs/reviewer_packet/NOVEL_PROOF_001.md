# Novel Proof 001: Layer-Safety Theorem

## What was proved?

Under the PAGC applications grammar, if every object has a layer-qualified ID and the promotion matrix forbids derived-to-source promotion, then derived 27/216 objects cannot be converted into source-observed 26x8 objects by any valid grammar operation.

## Why is this new for Etisiobi?

The proof turns the count-layer discovery into a system-design invariant. It lets the lab build with the derived 27/216 layer without letting it drift back into a false source-observed claim.

## What was discovered during proof?

Local token IDs collide across source and derived layers. A system keyed only by `token_id` is unsafe. The repair is to use:

```text
qualified_token_id = layer::local_token_id
```

## Why should anyone believe it?

The proof is backed by a verifier:

- `experiments/EXP-APP-003-layer-safety-proof/verification_report.json`
- `experiments/EXP-APP-003-layer-safety-proof/layer_safe_tokens.jsonl`
- `experiments/EXP-APP-003-layer-safety-proof/promotion_rules.json`
- `experiments/EXP-APP-003-layer-safety-proof/proof.md`

## What it does not prove

It does not prove governance outcomes, E6, universal compression, glyph-shape grammar, or global mathematical novelty. It proves a bounded system-safety property for PAGC-derived applications.
