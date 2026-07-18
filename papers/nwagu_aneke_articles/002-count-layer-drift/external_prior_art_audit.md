# External Prior-Art Audit

Article: `ARTICLE-NA-002`

Status: `PARTIAL_PRIOR_ART_AUDIT_NEEDS_DEEPER_REVIEW`

## Article-Specific Contribution Under Audit

This article's bounded contribution is not that Nwagu Aneke is newly discovered
and not that 27/216 is false in every possible model. The contribution under
review is:

> a reproducible count-layer audit that separates the current source-observed
> 26 x 8 index layer from the derived f/v split layer that yields 27 rows and
> 216 cells.

## Public Prior-Art Anchors Checked

| Source | Relevance | Boundary for This Article |
|---|---|---|
| Azuonye 1992, ScholarWorks landing page and PDF | Primary scholarly account of origins, features, mechanics, and literacy potential of the Nwagu Aneke Igbo syllabary. | Does not by itself clear the current repo's count ledger for external publication; source chart review remains needed. |
| Unicode L2/23-203, 2023 Update on African Scripts | Standards-facing status note that lists Nwagu Aneke as an unencoded syllabary with some logographic symbols and no Unicode proposal yet. | Supports standards relevance, but not a final repertoire or count-layer claim. |
| ScriptSource Unicode Status for Nwagu Aneke Igbo | Records that the script is not yet in Unicode or the Unicode Roadmap and is listed among scripts not yet encoded. | Confirms encoding-status gap; does not establish 26 x 8 or 27/216. |
| Omniglot Nwagu Aneke page | Public descriptive reference for script type, direction, dialect context, and logographic symbols. | Useful background only; not sufficient for article novelty or source authority. |
| Ahamefula/Mbah references in repo source registry | Reports ideal/actual symbol counts, multivalent characters, duplicate-symbol syllables, and f/v sharing. | Must be read against full text before the article claims novelty against linguistic prior art. |

## Repo Evidence Anchors

- `experiments/EXP-NA-002-count-layer-ledger/results.json`
- `experiments/EXP-NA-002-count-layer-ledger/data/count_layer_ledger.csv`
- `experiments/EXP-NA-002-count-layer-ledger/data/count_layer_ledger.jsonl`
- `corpus/bmc_count_reconciliation.json`
- `corpus/base_modifier_cache.jsonl`
- `artifacts/nwagu_aneke/symbol_inventory.jsonl`
- `research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md`
- `spine/events/current_state.md`

## Novelty-Risk Assessment

Risk: `MEDIUM`

The article is plausible as a data-quality/source-critical result only if it is
positioned against mature work in African script documentation, Unicode proposal
evidence, digital scholarly editing, provenance, and claim verification. The
current repo evidence supports a narrow count-layer audit, not a broad novelty
claim.

## Required Before Impact-Journal Candidate Status

1. Full article-specific literature review for African script standardization
   and digital humanities data-quality methods.
2. Direct review of Ahamefula/Mbah full text, not only registry notes.
3. Comparison against at least three analogous script-encoding or source-ledger
   cases.
4. Domain expert review confirming that the contribution is not merely an
   internal correction note.
5. Updated bibliography and related-work rewrite.

## Current Decision

The prior-art audit is started but not passed. The article may be described as
an evidence-pack-in-progress, not an impact-journal candidate.
