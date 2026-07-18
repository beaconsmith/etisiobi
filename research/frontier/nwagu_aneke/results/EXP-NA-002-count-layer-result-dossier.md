---
type: result_dossier
program: nwagu_aneke_frontier
experiment_id: EXP-NA-002
status: audit_result_not_paper_ready
created: "2026-06-22"
updated: "2026-06-22"
goal: GOAL-FRONTIER-001
claim_ceiling: source-critical audit result only
---

# EXP-NA-002 Count-Layer Result Dossier

## Result Statement

The current Etisiobi evidence package supports a source-observed Nwagu Aneke
count layer of:

```text
26 rows x 8 vowel/modifier columns = 208 records
```

The 27/216 layer is not source-observed in the current evidence package. It is a
derived layer that appears only if the combined f/v row is split into separate
f and v rows:

```text
27 rows x 8 columns = 216 derived records
```

This is a source-critical audit result. It is not a complete reconstruction, not
a PAGC proof, not a Unicode proposal, not a linguistic final judgment, and not a
submission-ready paper.

## Evidence Inputs

| Evidence | Path | What it supports |
|---|---|---|
| Count-layer experiment plan | `experiments/EXP-NA-002-count-layer-ledger/plan.md` | Scope: convert active Nwagu count claims into a layer-labeled ledger. |
| Count-layer experiment result | `experiments/EXP-NA-002-count-layer-ledger/results.json` | 7 ledger records; 26/8/208 source layer; 27/216 derived layer. |
| Count-layer decision | `experiments/EXP-NA-002-count-layer-ledger/decision.md` | Decision: `COUNT_LAYERS_RECONCILED_WITH_REVIEW_BLOCKERS`. |
| f/v hinge result | `experiments/EXP-NA-003-f-v-hinge-audit/results.json` | f/v split is a derived operation, not a source row-count result. |
| Azuonye 1992 source note | `research/frontier/nwagu_aneke/results/EXP-NA-002-source-note-azuonye-1992.md` | Appendix I strengthens 26 printed rows, 8 printed columns, and combined f/v row; Appendix II remains unresolved. |
| Azuonye 1992 local audit | `artifacts/nwagu_aneke/azuonye_1992_audit.md` | Prior local audit of the official PDF and Appendix I render. |
| Article benchmark scoreboard | `benchmarks/nwagu_article_research/scoreboard.json` | Hard gate rejects any source-observed 27/216 claim. |
| Article manifest | `papers/nwagu_aneke_articles/manifest.json` | Working-paper status only; not submission-ready. |
| PAGC reset | `research/pagc/PAGC_RESET.md` | Claims remain false until source, extraction, and falsification gates pass. |
| Nwagu primary-source README | `research/pagc/primary_sources/nwagu_aneke/README.md` | Source archive status and missing primary-source review path. |

## Layer Ledger

| Layer | Count | Status | Allowed wording | Forbidden wording |
|---|---:|---|---|---|
| Source-observed row count | 26 | current evidence package | "source-observed 26 rows" | "27 source rows" |
| Source-observed columns | 8 | current evidence package | "8 vowel/modifier columns" | "8 proves universal modifier system" |
| Source-observed records | 208 | current evidence package | "26 x 8 = 208 source-layer records" | "216 source records" |
| Derived f/v split rows | 27 | derived interpretation | "27 rows if f/v is split" | "27 rows observed in the source" |
| Derived f/v split records | 216 | derived interpretation | "216 derived records under f/v split" | "216 source-observed tokens" |

## Why This Can Be Frontier-Relevant

The result is small but strategically important: it turns an attractive exact
number into a controlled evidence-layer distinction. That is a publishable kind
of negative/correction result if the source dossier and prior art are hardened.

The contribution path is:

```text
source-critical audit -> count-layer correction -> claim-gated research object
-> reviewer-visible prevention of false source promotion
```

This path is broader than LPE-Bench. LPE can later measure whether AI workflows
respect this distinction, but the Nwagu result itself is the count-layer audit.

## Contradiction and Attack Surface

### A1. Legacy exact-count temptation

Older or generated PAGC surfaces can make 27/216 look foundational. Examples
include old hypotheses around `27x8`, `216-token` systems, and exact matrix
language. These must be treated as derived/speculative unless supported by the
source dossier.

Required handling:

- keep 27/216 language only with derived-layer qualification;
- block any source-observed 27/216 claim;
- keep E6, universal compression, genetic-code, holographic, and exact
  mathematical analogies outside the result claim.

### A2. f/v interpretation remains review-sensitive

`EXP-NA-003` supports the current operational distinction:

```text
combined f/v row -> source-layer row
split f and v rows -> derived operation
```

This does not settle phonology, manuscript history, or expert script analysis.
If future primary-source review shows separate f and v rows, the source layer
must be revised.

Azuonye 1992 Appendix I, as reviewed in the local source note, strengthens the
current operational distinction because the printed chart uses one combined
`f/v` row. It does not settle whether a later Appendix II recovery, manuscript
review, or expert phonological review should model separate underlying entries.

### A3. Paper-looking artifacts already exist

The repo contains working-paper drafts and selected-paper artifacts that discuss
the count-layer result. They remain review drafts only. Their existence must not
be used as evidence of submission readiness.

### A4. Rights and authority are unresolved

The source archive currently includes an Omniglot chart, source-page archive,
and local Azuonye 1992 PDF. Appendix I has been reviewed internally for count
evidence, but Appendix II content recovery, public-source image use, cultural
authority, and rights review remain blockers.

## Prior-Art Questions

Before promotion to paper candidate, answer:

1. What do source-critical script reconstruction papers treat as sufficient
   evidence for row/character inventory claims?
2. What prior work exists on count drift, sign inventory drift, or repertoire
   uncertainty in underdocumented scripts?
3. How do Unicode proposal pipelines handle provisional character inventories?
4. How do TEI/IIIF/Web Annotation workflows represent uncertain glyph
   inventories without converting them into facts?
5. What African script documentation cases provide appropriate comparison
   without shallow analogy?

## Reviewer Attack Surface

| Reviewer concern | Current answer | Remaining blocker |
|---|---|---|
| "Is this just internal bookkeeping?" | It becomes externally relevant if framed as source-critical count drift in underdocumented script research. | Need article-specific prior art. |
| "Where is the primary source?" | Current archive is partial; source trail is documented. | Azuonye comparison and manuscript access/review. |
| "Why should 26 be trusted?" | It is the current repo-local source-observed ledger, not a final historical truth. | Human/domain transcription review. |
| "Why mention 27/216 at all?" | Because it is a real derived layer that can easily be promoted into a false source claim. | Keep derived label everywhere. |
| "Is PAGC being smuggled back in?" | No; PAGC remains hypothesis/speculation unless separately tested. | Claim gate all theory/application language. |
| "Is this paper-ready?" | No. This is an audit result dossier. | Review-team trace, rights, prior art, and source review. |

## Decision Trace

Decision: `KEEP_AS_PRIMARY_FRONTIER_BRANCH_NOT_PAPER_READY`

Why this branch outranks the others right now:

- It is the clearest Nwagu-centered result.
- It corrects a live claim-risk rather than adding prose.
- It is grounded in existing repo-local experiment outputs.
- It can support later LPE, provenance, Unicode, and design-system work.
- It has an honest claim ceiling and clear falsification path.

Why not Inspect/LPE first:

- LPE-Bench is an instrument for measuring layer-promotion behavior.
- The Nwagu program first needs the strongest source-critical result selected.
- Without the count-layer dossier, LPE would test an under-specified target.

## Next Work Package

Create a prior-art and source-review checklist for this branch:

```text
research/frontier/nwagu_aneke/results/EXP-NA-002-prior-art-and-source-review-checklist.md
```

The checklist should separate:

1. source-critical script reconstruction prior art;
2. Unicode/repertoire uncertainty prior art;
3. African script documentation comparators;
4. rights/authority review;
5. human transcription review;
6. paper-candidate promotion requirements.
