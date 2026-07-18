# Layer-Safety Theorem

## One-line Result

PAGC applications can safely use the derived 27/216 layer only if every object is layer-qualified and grammar operations forbid derived-to-source promotion.

## Why It Matters

This is the first proof that converts the accepted count-layer foundation into a system-design safety invariant. The theorem does not make PAGC grander; it makes PAGC safer to build with.

## Practical Rule

Never use `token_id` alone as an application identifier. Use:

```text
qualified_token_id = layer::local_token_id
```

## Research Output

See `experiments/EXP-APP-003-layer-safety-proof/proof.md` and `verification_report.json`.
