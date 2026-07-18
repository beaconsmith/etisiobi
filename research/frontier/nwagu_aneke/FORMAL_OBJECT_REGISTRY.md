---
type: formal_object_registry
program: nwagu_aneke_frontier
status: seeded_open_registry
created: "2026-06-22"
updated: "2026-06-22T11:16:30+01:00"
goal: GOAL-FRONTIER-001
claim_ceiling: candidate_formalisms_not_theory_claims
---

# Formal Object Registry

## Purpose

This registry seeds competing formalizations without selecting a destination
theory. Each formal object must state primitives, operations, invariants, data
needed, and collapse conditions before promotion.

## Candidate Formula Families

| ID | Family | Claim class | Primitive idea | Test/proof path |
|---|---|---|---|---|
| FF-001 | Count-layer tuple | `[FORM]` | `(rows, columns, records, layer)` | Validate against count ledger |
| FF-002 | f/v split transformation | `[DERIVED]` | `split(row_fv) -> row_f + row_v` | Compare source and derived records |
| FF-003 | Layered claim graph | `[FORM]` | claims as typed nodes with derivation edges | Build fixture validator |
| FF-004 | Uncertainty lattice | `[FORM]` | claims ordered by certainty and review status | Test on source and LPE records |
| FF-005 | Bipartite row-column graph | `[FORM]` | row nodes connected to vowel-column nodes | Compare to chart inventory |
| FF-006 | Hypergraph of glyph readings | `[FORM]` | glyph, sound, source, review as hyperedges | Requires glyph review |
| FF-007 | Finite-state reading model | `[FORM]` | signs as states/transitions | Needs text samples |
| FF-008 | Transducer for transliteration | `[FORM]` | source signs to Latin outputs | Needs validated sign list |
| FF-009 | Modifier composition algebra | `[MATH]` | operators over base signs | Needs source evidence of operations |
| FF-010 | Variant equivalence classes | `[FORM]` | allographs grouped by evidence | Needs glyph crops |
| FF-011 | Logograph side-channel model | `[FORM]` | direct word-symbol lookup channel | Needs reviewed logograph inventory |
| FF-012 | Provenance dependency DAG | `[FORM]` | sources -> observations -> claims -> outputs | Implement via dependency graph |
| FF-013 | Claim promotion type system | `[FORM]` | only allowed layer transitions type-check | Build checker |
| FF-014 | LPE confusion matrix | `[COMP]` | source/derived/speculative promotions as errors | Needs validated labels |
| FF-015 | Information-density model | `[TEST]` | record counts vs representation cost | Needs corpus |
| FF-016 | Error-correction analogy | `[ANALOGY]` | redundancy supports recovery | Must become mechanism or drop |
| FF-017 | Teaching sequence model | `[COG]` | ordered acquisition of signs/layers | Needs learner study |
| FF-018 | Authority protocol game | `[SOC]` | claim release as turn-taking protocol | Needs authority review |
| FF-019 | Portfolio selection score | `[NEW]` | branch utility by evidence and information gain | Compare to outcomes |
| FF-020 | Interface layer projection | `[APPLIED]` | show claim layers as separate views | Test with readers |

## Competing Formal Representations

1. Set of source-observed records.
2. Relation between row labels and column labels.
3. Bipartite graph of rows and columns.
4. Hypergraph linking glyph, reading, source, review, and rights.
5. Transformation system from source layer to derived layer.
6. Type system for claim promotion.
7. Lattice of uncertainty and review states.
8. DAG of provenance and publication dependencies.
9. Finite-state/transducer model for reading/transliteration.
10. Interface projection model for public legibility.

## Promotion Rule

No formal object is promoted until it has a minimum dataset, alternatives,
failure cases, and a proof or test path.
