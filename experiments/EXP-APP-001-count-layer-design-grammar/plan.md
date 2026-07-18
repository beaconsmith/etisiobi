# EXP-APP-001: Count-Layer Design Grammar

## Research question

Can the confirmed 26x8 source layer and derived 27/216 f/v split become a drift-safe grammar for designing novel systems?

## Hypothesis

If every generated design object carries a layer label, then PAGC applications can use source and derived layers without turning derived counts into source claims.

## Method

1. Load the BMC source-layer records.
2. Generate source-layer tokens.
3. Generate derived-layer tokens by splitting f/v.
4. Check count invariants.
5. Emit a reusable system-design grammar.

## Success criteria

- 208 source-layer tokens.
- 216 derived-layer tokens.
- Derived tokens carry `derived_fv_split`.
- No generated artifact calls 27/216 source-observed.
