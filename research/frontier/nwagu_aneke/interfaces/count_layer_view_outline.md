---
type: interface_outline
program: nwagu_aneke_frontier
backlog_id: EXP-BL-003
status: first_outline_complete_with_prototype_usability_packet_and_scorer
created: "2026-06-22"
updated: "2026-06-22T18:34:57+01:00"
goal: GOAL-FRONTIER-001
claim_ceiling: interface_outline_only
source_fixture: research/frontier/nwagu_aneke/claim_layer_fixtures.jsonl
---

# Count-Layer View Outline

## Question

Can a simple layer-view artifact make observation, derivation, speculation, and
application distinguishable to a reader without turning the visual into proof?

## Layer

Applied/interface. The view is a reader-facing organization of claims and
fixtures. It is not a source, proof, publication figure, or product-ready demo.

## Method

Use `claim_layer_fixtures.jsonl` as the data source. Render each record in the
panel matching its `layer`, while preserving visible lineage, rights status,
authority status, uncertainty, contradictions, promotion status, and collapse
conditions.

The first outline uses text and abstract tables only. It does not reproduce
Appendix I, source glyphs, manuscript images, or restricted cultural material.

## Reader Contract

The view must make these distinctions visible without requiring a reader to open
the raw fixture file:

| Reader question | Required visual answer |
|---|---|
| What is observed in the current source-display layer? | `26 x 8 = 208`, labeled source-observed Appendix I chart layer. |
| What is derived? | `27/216`, labeled derived f/v split and visibly marked "not source-observed". |
| What is unavailable or restricted? | Manuscript corpus and Appendix II records shown in a restricted/blocked panel. |
| What is speculation? | PAGC/cross-domain claims shown as exploratory hypotheses only. |
| What is applied? | Layer-safe design grammar shown as an application with lineage, not historical meaning. |
| What is computational? | LPE/agent records shown as evaluation artifacts, not Nwagu source evidence. |
| What is contested? | Ahamefula/Mbah 164/224 shown as a separate unresolved repertoire-count lead. |
| What has been dropped? | Failed automated PDF refresh and source-observed 27/216 wording shown as non-current branches. |

## Static View Structure

### 1. Source-Observed Panel

Fixture:

- `NA-FIX-001`

Display:

| Field | Value |
|---|---|
| Headline count | `26 rows x 8 columns = 208 source-display cells` |
| Evidence label | Source-observed, Appendix I chart layer |
| Confidence language | Current evidence package; not complete inventory |
| Rights marker | Internal review only; no public figure reproduction |
| Authority marker | Not reviewed by community authority |
| Collapse condition | Revised if stronger source or recovered Appendix II changes row/column inventory |

Design rule:

- This panel may be visually primary because it is the current source-observed
  chart layer.
- It must still carry the limits: "Appendix I chart layer", "not full
  manuscript inventory", and "rights review required".

### 2. Derived f/v Panel

Fixture:

- `NA-FIX-002`

Display:

| Field | Value |
|---|---|
| Headline count | `27 rows / 216 cells` |
| Evidence label | Derived f/v split |
| Required marker | `NOT SOURCE-OBSERVED` |
| Derivation path | Combined `f/v` row -> split into `f` and `v` rows -> multiply by 8 columns |
| Contradiction link | `NA-FIX-001` source-observed combined f/v row |
| Collapse condition | Reopen if source or expert review shows separate source-layer f/v rows |

Design rule:

- This panel must never look like a correction of the source-observed panel.
- It is an analytic branch, not the canonical source layer.

### 3. Restricted / Blocked Panel

Fixtures:

- `NA-FIX-003`
- `NA-FIX-006`

Display:

| Record | Status | Reader-facing wording |
|---|---|---|
| Manuscript corpus | Restricted / no public dataset | Reported corpus; custody, access, rights, and completeness unresolved. |
| Appendix II | Named but unrecovered | Appendix II is a live source blocker, not an absence claim. |

Design rule:

- Use "blocked" or "restricted", not "missing forever".
- Include exact next action: human-review the unsent ScholarWorks request draft.

### 4. Speculative / Frontier Hypothesis Panel

Fixture:

- `NA-FIX-004`

Display:

| Field | Value |
|---|---|
| Claims | PAGC, universal compression, E6, cross-domain theory |
| Label | Speculative / exploratory |
| Required caveat | Permitted for discovery; not promoted as artifact fact |
| Collapse condition | Unsupported source-fact wording or failed controlled test |

Design rule:

- The panel should invite exploration without borrowing authority from the
  source-observed panel.
- It should route hypotheses toward tests, not toward publication claims.

### 5. Applied / Design Panel

Fixture:

- `NA-FIX-005`

Display:

| Field | Value |
|---|---|
| Artifact | Layer-safe design grammar |
| Label | Applied |
| Lineage | Source/derived records -> explicit abstraction -> design output |
| Required caveat | Application is not historical meaning |
| Failure mode | Reader infers unsupported source claim from design output |

Design rule:

- Show source-to-abstraction lineage before showing any design result.
- No glyph-derived visuals until rights review supports them.

### 6. Computational / Evaluation Panel

Fixture:

- `NA-FIX-007`

Display:

| Field | Value |
|---|---|
| Artifact | Layer-promotion-error / agent evaluation |
| Label | Computationally generated |
| Role | Tests whether agents preserve claim layers |
| Required caveat | Does not prove Nwagu source facts |

Design rule:

- Do not use agent scores as source evidence.
- Show them as method-infrastructure diagnostics.

### 7. Contested Count Panel

Fixture:

- `NA-FIX-008`

Display:

| Count layer | Status |
|---|---|
| `164 actual symbols` | External lead, not locally hardened |
| `224 ideal symbols` | External lead, not locally hardened |
| `208 Appendix I chart cells` | Different count type from current source-display layer |

Design rule:

- Keep count types side-by-side without merging them.
- Require local extraction before any claim hardening.

### 8. Dropped / Non-Current Branches Panel

Fixtures:

- `NA-FIX-009`
- `NA-FIX-010`

Display:

| Dropped branch | Why dropped |
|---|---|
| Automated ScholarWorks refresh as source check | 403/HTML proves access failure only, not PDF incompleteness. |
| Source-observed 27/216 wording | Current Appendix I evidence supports combined `f/v`; 27/216 is derived only. |

Design rule:

- Dropped branches should remain visible so future agents do not rediscover and
  re-promote them.

## Interaction Model For Later Prototype

This outline can become a static HTML or dashboard prototype later. Required
interactions:

1. Layer filter: source-observed, derived, restricted, speculative, applied,
   computational, contested, dropped.
2. Count comparison toggle: show `26/208`, `27/216`, `164`, `224` as different
   count types, never as one sequence of corrections.
3. Evidence drawer: source refs, method refs, rights status, authority status,
   contradictions, and collapse conditions.
4. Claim ceiling indicator: `not_ready`, `result`, `candidate`, `explore`, or
   `dropped`.
5. "Why not ready?" drawer for rights/authority/source blockers.

## Expected Learning

The interface should make the current source discipline easier to understand:

- readers see why `26/208` and `27/216` can both exist without contradiction;
- readers see that Appendix II is not recovered rather than silently ignored;
- readers see that design and computational work can proceed without becoming
  source claims;
- readers see exactly which next actions could change the model.

## Failure Condition

The outline fails if a reader could reasonably infer that:

- `27/216` is source-observed;
- speculative PAGC claims are source facts;
- a design grammar proves historical meaning;
- the missing Appendix II list proves nonexistence;
- LPE/agent evaluation proves the Nwagu source layer;
- rights/authority review is optional for public use.

## Rights Implication

This interface uses non-sensitive metadata, count statements, and source paths.
It must not reproduce Appendix I, source glyphs, Appendix II if recovered,
manuscript pages, or restricted cultural material without rights and authority
review.

## Next-Branch Options

- Static HTML prototype using fixture records as data.
- JSON Schema for interface-facing fixture fields.
- Reader/usability test with source/derived distinction questions.
- Visual atlas after rights-safe glyph and figure policy is resolved.
- Export to LPE benchmark cases for interface-induced promotion errors.

## Usability Packet

The first comprehension-test packet now lives under
`research/frontier/nwagu_aneke/interfaces/usability/`.

The scorer lives at `scripts/score_count_layer_comprehension_results.py` and
keeps the strongest allowed result at
`human_comprehension_signal_not_source_evidence`.

It checks whether readers can answer these questions from the prototype alone:

- `26/208` is the current source-observed Appendix I chart layer;
- `27/216` is a derived f/v split and not source-observed;
- Appendix II is named but unrecovered, not disproved;
- PAGC remains speculative;
- design outputs and computational evaluations are not source evidence;
- 164/224 remains a separate external repertoire-count lead;
- source-observed 27/216 wording remains a dropped branch.

## Exact Next Action

Run the comprehension protocol with 3-5 human readers, score the dated response
CSV, and revise prototype labels if the scorer returns
`FAIL_LABEL_REVISION_REQUIRED`.
