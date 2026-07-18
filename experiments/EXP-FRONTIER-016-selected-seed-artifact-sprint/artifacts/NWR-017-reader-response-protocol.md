# NWR-017 Reader Response Protocol

Seed: `NWR-017`

Source question: Can readers distinguish source-observed and derived count layers

Evidence layer: derived

Claim ceiling: artifact_not_paper_candidate

## Bounded Artifact

This protocol defines a small comprehension task for the count-layer interface.
It creates the protocol only. It does not collect responses.

| Prompt target | Reader task | Correct signal |
|---|---|---|
| Source-observed count | Identify the 26 by 8 layer | Reader marks it as source-observed |
| Derived split | Identify the f/v split layer | Reader marks it as derived |
| Blocked claim | Reject source promotion for derived count | Reader refuses overstrong claim |

## Evidence Layer

The artifact is derived-layer interface testing. It tests whether readers can
see the distinction between observed and derived count views.

## Falsification Gate

The protocol fails if it rewards confident answers without checking whether the
reader preserved the evidence layer.

## Rights And Authority Guardrail

The protocol should use metadata-only examples until rights and authority review
approve any public-facing source material.

## What This Teaches Oroma

Trust interfaces should test whether people understand what a record can and
cannot prove.

## Next Action

Prepare a local response template without collecting responses.
