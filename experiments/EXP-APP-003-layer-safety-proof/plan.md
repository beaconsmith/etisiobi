# EXP-APP-003: Layer-Safety Proof

## Research question

Can the PAGC applications grammar formally prevent derived 27/216 objects from being mistaken for source-observed 26x8 objects?

## Hypothesis

If every object uses a layer-qualified ID and all promotion rules forbid derived-to-source promotion, then count-layer drift is impossible through valid grammar operations.

## Method

1. Load source, derived, and governance-domain tokens.
2. Find local ID collisions.
3. Repair representation with layer-qualified IDs.
4. Define allowed and forbidden promotion rules.
5. Verify uniqueness and forbidden-promotion invariants.
6. Write a formal proof and bounded novelty claim.
