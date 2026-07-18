---
type: claim_layer_schema
program: nwagu_aneke_frontier
status: active_schema_draft
created: "2026-06-22"
updated: "2026-06-22T11:47:04+01:00"
goal: GOAL-FRONTIER-001
---

# Claim Layer Schema

## Purpose

This schema defines how Nwagu Aneke records, claims, experiments, and
applications should label evidence layers. It supports expansive exploration
without allowing unsupported promotion.

## Layer Vocabulary

| Layer | Code | Definition | Promotion rule |
|---|---|---|---|
| Source-observed | `source_observed` | Directly visible or explicitly supported by an identified source. | Requires source locator and extraction method. |
| Community-attested | `community_attested` | Supported by an identified community authority or knowledge holder. | Requires authority record and permission boundary. |
| Derived | `derived` | Produced by documented transformation, split, count, transcription, or inference. | Must retain derivation path. |
| Speculative | `speculative` | Hypothesis, analogy, proposed model, or exploratory interpretation. | Must not be written as fact. |
| Computationally-generated | `computationally_generated` | Produced by software, AI, simulation, clustering, or formal transformation. | Requires method, inputs, and validation status. |
| Experimentally-supported | `experimentally_supported` | Tested under a documented protocol with reproducible evidence. | Requires protocol, outputs, baselines/failure criteria. |
| Applied | `applied` | Design, product, system, interface, artwork, or benchmark built from prior layers. | Requires source-to-abstraction lineage. |
| Contested | `contested` | Supported and challenged by credible competing interpretations. | Requires contradiction record. |
| Restricted | `restricted` | Known or suspected to exist but limited by rights, consent, privacy, or access. | Requires access boundary and no public-release assumption. |
| Dropped | `dropped` | Discarded, falsified, or parked branch. | Requires reason and reopen condition if any. |

## Minimal Record Shape

```json
{
  "record_id": "NA-CLAIM-0001",
  "claim_text": "26 rows x 8 columns = 208 records in the current source-observed chart model.",
  "layer": "source_observed",
  "source_refs": ["research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md"],
  "derivation_refs": [],
  "method_refs": ["experiments/EXP-NA-002-count-layer-ledger/results.json"],
  "rights_status": "review_required_before_public_reproduction",
  "authority_status": "not_reviewed",
  "uncertainty": "current evidence package; human/domain review required",
  "contradictions": ["derived 27/216 if f/v is split"],
  "promotion_status": "not_ready",
  "collapse_conditions": ["A primary source shows separate f and v rows."]
}
```

## Required Fields

| Field | Required | Notes |
|---|---|---|
| `record_id` | yes | Stable identifier. |
| `claim_text` | yes | Plain-language statement. |
| `layer` | yes | One value from layer vocabulary. |
| `source_refs` | yes | Empty only for pure speculation or applied prototypes. |
| `derivation_refs` | yes | Required for `derived`, `computationally_generated`, and `applied`. |
| `method_refs` | yes | Required for experimental/computational claims. |
| `rights_status` | yes | Never assume public release. |
| `authority_status` | yes | Never assume community authority. |
| `uncertainty` | yes | Must be explicit, not hidden in prose. |
| `contradictions` | yes | Empty list allowed only after review. |
| `promotion_status` | yes | `explore`, `candidate`, `result`, `not_ready`, `dropped`. |
| `collapse_conditions` | yes | What would weaken or falsify the record. |

## Promotion Checks

| From | To | Required evidence |
|---|---|---|
| `speculative` | `derived` | Explicit operation and input record. |
| `derived` | `experimentally_supported` | Executed protocol and reproducible result. |
| `source_observed` | public claim | Source locator, extraction method, rights boundary, review status. |
| `applied` | product/public demo | Source-to-abstraction lineage, rights review, usability/contact test. |
| any layer | `ready` language | Branch-specific review, validators, decision trace, rights/authority where relevant. |

## Current Canonical Count Records

| Record | Layer | Statement |
|---|---|---|
| `NA-COUNT-001` | `source_observed` | Current chart model uses 26 rows x 8 vowel/modifier columns = 208 records. |
| `NA-COUNT-002` | `derived` | 27/216 appears only if the combined f/v row is analytically split. |
| `NA-COUNT-003` | `restricted` | Manuscript exercise-book corpus is reported but not available as a public dataset in the current evidence package. |
| `NA-COUNT-004` | `speculative` | PAGC, universal compression, E6, and cross-domain claims remain hypotheses until independently tested. |

## Implementation Notes

This schema is a working research artifact, not a final ontology. It should be
converted to JSON Schema only after two or three branches use it successfully.

First fixture use: `research/frontier/nwagu_aneke/claim_layer_fixtures.jsonl`
and `research/frontier/nwagu_aneke/claim_layer_fixture_review.md`.
