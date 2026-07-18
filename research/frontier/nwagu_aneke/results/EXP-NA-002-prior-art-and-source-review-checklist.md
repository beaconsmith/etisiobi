---
type: promotion_checklist
program: nwagu_aneke_frontier
experiment_id: EXP-NA-002
status: open_blockers
created: "2026-06-22"
updated: "2026-06-22"
goal: GOAL-FRONTIER-001
claim_ceiling: checklist_only_no_paper_promotion
---

# EXP-NA-002 Prior-Art and Source-Review Checklist

## Purpose

This checklist defines what must be verified before the count-layer audit can
move from result dossier to paper-candidate consideration.

It does not promote the branch. It turns blockers into inspectable work.

Current branch:

```text
EXP-NA-002-count-layer-ledger
```

Current result:

```text
26 rows x 8 vowel/modifier columns = 208 source-layer records
27 rows x 8 columns = 216 derived records only if f/v is split
```

Forbidden promotion:

```text
27/216 must not be described as source-observed.
```

## Current Evidence Status

| Area | Status | Evidence |
|---|---|---|
| Count-layer audit | present | `experiments/EXP-NA-002-count-layer-ledger/results.json` |
| f/v derived split audit | present | `experiments/EXP-NA-003-f-v-hinge-audit/results.json` |
| Source archive | partial | `research/pagc/primary_sources/nwagu_aneke/README.md` |
| Source audit | partial | `research/pagc/primary_sources/nwagu_aneke/SOURCE_AUDIT.md` |
| Chart transcription | partial | `research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md` |
| Prior-art matrix | partial | `papers/SELECTED_PAPER/related_work_matrix.csv` |
| Rights/authority | blocked | `experiments/EXP-NA-007-provenance-ledger/results.json` |
| Paper-candidate status | blocked | `benchmarks/nwagu_article_research/BENCHMARK.md` |

## Gate A: Source-Critical Script Reconstruction Prior Art

| ID | Work item | Evidence target | Promotion impact |
|---|---|---|---|
| A1 | Verify Azuonye 1992 from the official ScholarWorks landing page and full paper. | Source note with bibliographic metadata, source-status, and count-relevant extracts. | Required before any source-layer count claim is called article-grade. |
| A2 | Extract Appendix I / Appendix II evidence relevant to rows, columns, f/v, and logographs. | Structured extraction table linked from the source note. | Determines whether 26/208 remains current or must be revised. |
| A3 | Verify whether the chart matrix is Aneke's structure, Azuonye's presentation, or a later pedagogical arrangement. | Method note separating artifact structure from editorial display. | Prevents matrix-as-generative-grammar overclaim. |
| A4 | Locate or mark unavailable Ahamefula & Mbah 2011 full text. | Source note or unavailability record. | Needed for independent linguistic count comparison. |
| A5 | Compare with at least two script/glyph inventory projects or reconstruction cases. | Prior-art matrix rows with relationship and gap. | Needed to answer "is this just local bookkeeping?" |

Minimum pass condition:

```text
A1 and A2 complete; A3 explicitly classified; A4 either extracted or marked
unavailable after search; A5 has at least two documented comparator rows.
```

## Gate B: Unicode and Repertoire-Uncertainty Prior Art

| ID | Work item | Evidence target | Promotion impact |
|---|---|---|---|
| B1 | Review Unicode proposal/repertoire expectations relevant to unencoded scripts. | Source note or matrix row tied to `EXP-NA-006`. | Prevents premature Unicode-proposal framing. |
| B2 | Reconcile count-layer audit with `EXP-NA-006-unicode-gap-matrix`. | Short bridge note: what the audit teaches Unicode readiness, what remains blocked. | Makes the count result useful outside PAGC. |
| B3 | Identify which evidence fields are missing for repertoire stabilization. | Checklist row for each missing field: glyph image, name, value, representative source, variant status. | Defines why source review still blocks promotion. |

Minimum pass condition:

```text
The branch can say what the count-layer audit contributes to repertoire
uncertainty without implying a Unicode proposal is ready.
```

## Gate C: Standards and Provenance Comparators

Existing candidate comparators from `papers/SELECTED_PAPER/related_work_matrix.csv`:

- PROV-O and PROV-DM;
- RO-Crate;
- IIIF Presentation API;
- TEI Guidelines and TEI character/glyph guidance;
- W3C Web Annotation;
- CIDOC CRM / CRMdig;
- FAIR and DataCite.

| ID | Work item | Evidence target | Promotion impact |
|---|---|---|---|
| C1 | Mark each comparator as method infrastructure, not novelty proof. | Updated matrix rows or branch-specific prior-art note. | Prevents standards mapping from replacing the Nwagu result. |
| C2 | Identify what each comparator cannot solve: count drift, source/derived separation, authority, or claim promotion. | Gap column for each comparator. | Sharpens contribution without overstating novelty. |
| C3 | Decide whether RO-Crate/DataLad/Software Heritage belongs in this branch or only later reproducibility packaging. | Decision note. | Keeps EXP-NA-002 from becoming a tooling paper too early. |

Minimum pass condition:

```text
The branch has a clear novelty boundary: standards support traceability, while
the Nwagu contribution is the count-layer correction and claim gate.
```

## Gate D: Rights and Authority Review

| ID | Work item | Evidence target | Promotion impact |
|---|---|---|---|
| D1 | Record rights status for Omniglot chart and archived HTML. | Rights ledger row. | Required before any public image reproduction. |
| D2 | Record rights status for Azuonye 1992 PDF and appendices. | Rights ledger row. | Required before quoting, reproducing figures, or packaging excerpts. |
| D3 | Record status of manuscript exercise books: location, custodian, access, permissions, unknowns. | Provenance ledger update. | Blocks corpus claims until resolved. |
| D4 | Define cultural/source authority review needed for public claims. | Authority-review checklist with reviewer role, scope, and decision fields. | Required before public-release or community-facing claims. |

Minimum pass condition:

```text
The branch can cite public metadata and describe blockers, but cannot release
restricted images, corpus material, or authority-sensitive claims.
```

## Gate E: Human Transcription and Domain Review

| ID | Work item | Evidence target | Promotion impact |
|---|---|---|---|
| E1 | Human-review the 26 printed rows and 8 columns from the archived chart. | Reviewer trace with row/column agreement and uncertainty notes. | Required before calling the count ledger externally robust. |
| E2 | Human-review f/v row interpretation. | Review note: combined row, split rationale, disagreement path. | Required before using 27/216 as a controlled derived layer in publication prose. |
| E3 | Human-review logograph count and uncertainty. | Logograph ledger review note. | Prevents logograph claims from contaminating count-layer claims. |
| E4 | Domain-review Igbo phonology assumptions behind vowel/modifier language. | Domain note separating Igbo phonology from chart observation. | Prevents "8 columns" from becoming unsupported linguistic theory. |

Minimum pass condition:

```text
Human/domain review confirms or revises the row/column ledger and records all
uncertainty without erasing disagreement.
```

## Gate F: Paper-Candidate Promotion Requirements

This branch can be considered for paper-candidate status only after:

- Gate A minimum pass condition is satisfied.
- Gate D has no unresolved blocker that affects the planned public artifact.
- Gate E has at least one documented human/domain review trace.
- A branch-specific reviewer attack surface exists.
- A branch-specific prior-art matrix exists.
- The result dossier is updated with any source-review changes.
- `python scripts\validate_lab_standard.py` passes.
- `python scripts\validate_review_team_gate.py` passes before any readiness
  language is used.

Do not count this branch as paper-candidate merely because a manuscript draft,
compiled PDF, benchmark score, or formatted package exists.

## First Execution Slice

Start with Gate A because it controls every downstream claim.

Next concrete artifact:

```text
research/frontier/nwagu_aneke/results/EXP-NA-002-source-note-azuonye-1992.md
```

That note must answer:

1. What exact source is being used?
2. What does it say about row count, column count, f/v, and logographs?
3. Is the matrix an observed structure, editorial display, or unresolved?
4. What rights/quotation limits apply?
5. Does the source confirm, revise, or weaken the current 26/208 vs derived
   27/216 audit?
