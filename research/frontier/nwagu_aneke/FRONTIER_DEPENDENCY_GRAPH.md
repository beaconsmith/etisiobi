---
type: frontier_dependency_graph
program: nwagu_aneke_frontier
status: active_dependency_map
created: "2026-06-22"
updated: "2026-06-22T11:09:00+01:00"
goal: GOAL-FRONTIER-001
---

# Frontier Dependency Graph

## Purpose

This graph shows how sources, claims, datasets, scripts, experiments, products,
reviews, rights, and publications depend on one another. It is designed to keep
the frontier broad while preventing immature branches from looking ready.

## High-Level Graph

```mermaid
flowchart TD
  A["Source artifacts and metadata"] --> B["Observation ledger"]
  B --> C["Uncertainty and contradiction maps"]
  C --> D["Claim layer schema"]
  D --> E["Count-layer audit"]
  D --> F["Script and logograph inventories"]
  D --> G["Computational experiments"]
  D --> H["Interfaces and applications"]
  E --> I["Reviewer attack surface"]
  F --> I
  G --> I
  H --> I
  A --> J["Rights and authority ledger"]
  J --> K["Release boundary"]
  I --> L["Portfolio scorecard"]
  L --> M["Branch decision trace"]
  M --> N["Result candidate"]
  N --> O["External research candidate"]
  K --> O
  O --> P["Publication, release, productization, or partnership"]
```

## Critical Dependencies

| Output | Depends on | Blocks if missing |
|---|---|---|
| Source-facing claim | Source locator, extraction method, uncertainty record | Artifact-specific public claim |
| Derived count claim | Source input, transformation rule, derivation path | 27/216 language |
| Public image/table release | Rights status, authority review, attribution boundary | Public release or exhibition |
| LPE benchmark claim | Validated labels, external controls, reproducible runs | Frontier AI-eval claim |
| Unicode-readiness claim | Repertoire evidence, source status, authority review | Standards/proposal language |
| Product/design claim | Source-to-abstraction lineage, application-layer label, rights review | Public product/demo claim |
| Paper-candidate branch | Result dossier, prior art, reviewer attack surface, validators | Draft hardening or readiness language |

## Current Branch Dependencies

### `EXP-NA-002` Count-Layer Audit

```mermaid
flowchart LR
  S["Azuonye / Omniglot / source archive"] --> O["Observed 26x8 chart model"]
  O --> A["EXP-NA-002 count-layer ledger"]
  O --> B["EXP-NA-003 f/v hinge audit"]
  B --> D["Derived 27/216 model"]
  A --> R["Result dossier"]
  D --> R
  R --> P["Prior-art and source-review checklist"]
  P --> N["Source note: Azuonye 1992"]
  N --> Q["Revised or confirmed count-layer audit"]
```

Current blocker: source note and human/domain review.

### LPE / Agent Evaluation

```mermaid
flowchart LR
  C["Claim layer schema"] --> F["LPE fixtures"]
  F --> H["Human/domain validation"]
  H --> R["Reproducible agent runs"]
  R --> E["External controls"]
  E --> B["Benchmark claim candidate"]
```

Current blocker: validation and external controls.

### Interface / Public Legibility

```mermaid
flowchart LR
  S["Layer schema"] --> V["Static layer view"]
  R["Rights-safe assets"] --> V
  V --> U["Usability/contact test"]
  U --> P["Public interface candidate"]
```

Current blocker: rights-safe asset boundary and contact test.

## No-Shortcut Rules

- A manuscript draft does not satisfy source review.
- A benchmark score does not satisfy human/domain validation.
- A compiled PDF does not satisfy rights or authority review.
- A useful prototype does not prove a historical claim.
- A striking analogy does not prove a mechanism.
- A standards mapping does not prove compliance or readiness.

## Next Graph Update

Update this graph after the first parallel exploration sprint selects and
records Track A, Track B, and Track C artifacts.
