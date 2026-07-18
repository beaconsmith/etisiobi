---
type: fixture_review
program: nwagu_aneke_frontier
backlog_id: EXP-BL-002
status: completed_internal_with_validator
created: "2026-06-22"
updated: "2026-06-22T11:47:04+01:00"
goal: GOAL-FRONTIER-001
claim_ceiling: method_fixture_only
---

# Claim-Layer Fixture Review

## Question

Can the draft claim-layer schema preserve source-observed, derived,
speculative, computational, applied, contested, restricted, and dropped records
without flattening them into one evidence status?

## Layer

Method infrastructure. The fixture set is about representation discipline, not
about paper readiness or public release.

## Method

Created `claim_layer_fixtures.jsonl` using the minimal record shape in
`CLAIM_LAYER_SCHEMA.md`. Each fixture includes:

- `record_id`;
- `claim_text`;
- `layer`;
- `source_refs`;
- `derivation_refs`;
- `method_refs`;
- `rights_status`;
- `authority_status`;
- `uncertainty`;
- `contradictions`;
- `promotion_status`;
- `collapse_conditions`.

Added `scripts/validate_claim_layer_fixtures.py` so this fixture set can be
checked repeatably rather than only by ad hoc inspection.

## Fixture Coverage

| Fixture | Layer | Purpose |
|---|---|---|
| `NA-FIX-001` | `source_observed` | Appendix I 26 x 8 source-display count. |
| `NA-FIX-002` | `derived` | 27/216 f/v split as derived count. |
| `NA-FIX-003` | `restricted` | Reported manuscript corpus without public dataset access. |
| `NA-FIX-004` | `speculative` | PAGC and cross-domain theory kept exploratory. |
| `NA-FIX-005` | `applied` | Layer-safe design grammar as application, not source fact. |
| `NA-FIX-006` | `restricted` | Appendix II named but unrecovered. |
| `NA-FIX-007` | `computationally_generated` | LPE/agent evaluation as computational artifact. |
| `NA-FIX-008` | `contested` | Ahamefula/Mbah 164/224 as separate count layer lead. |
| `NA-FIX-009` | `dropped` | Failed automated ScholarWorks refresh as negative recovery result. |
| `NA-FIX-010` | `dropped` | Source-observed 27/216 wording rejected unless evidence changes. |

## Expected Learning

The schema can represent the current frontier problem more cleanly than a
single confidence score. It keeps:

- Appendix I source-display evidence separate from derived f/v arithmetic;
- missing Appendix II evidence separate from absence claims;
- computational LPE artifacts separate from source facts;
- applied design grammar separate from historical meaning;
- external repertoire leads separate from locally verified claims.

## Failure Condition

The schema would fail if future records cannot express one of these distinctions
without inventing prose exceptions:

- source display vs. complete inventory;
- restricted source vs. missing source;
- derived count vs. observed count;
- applied design vs. source meaning;
- computational evaluation vs. artifact evidence;
- contested count types vs. contradiction.

## Rights Implication

The fixtures use file paths, metadata, and count statements only. They do not
reproduce source figures, restricted manuscript content, or long source text.

## Next-Branch Options

- Convert `CLAIM_LAYER_SCHEMA.md` into JSON Schema.
- Add a fixture validator for required fields and allowed layer values.
- Use the fixture set to seed LPE benchmark cases.
- Use the fixture set to drive the Track C count-layer interface outline.

## Exact Next Action

Use the fixture set to drive the Track C count-layer interface outline, so the
reader-facing view inherits the same source/derived/restricted/speculative
separation.
