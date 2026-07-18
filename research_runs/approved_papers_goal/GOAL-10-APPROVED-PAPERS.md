# Goal: 10 Approved Etisiobi Papers

Updated: 2026-06-21T14:42:02+01:00

Status: `APPROVED_PAPERS_GOAL_NOT_MET`

Approved count: 2 / 10

## Counting Rule

A paper counts only when:

- `approved_paper.json` says `APPROVED_INTERNAL_RESEARCH_PAPER`;
- all approval gates are `PASS`;
- `review_team_trace.jsonl` contains PASS reviews from all required roles;
- source, rights, citation, evidence, reproducibility, and review gates are clear;
- manuscript does not contain internal benchmark/progress-note language;
- manuscript preserves the 26x8 source layer and derived-only 27/216 invariant.

## Active Hardening Batch

- `ARTICLE-NA-005`: A TEI, IIIF, and Web Annotation Bridge for an Unencoded African Syllabary (`005-tei-iiif-critical-edition`)
- `ARTICLE-NA-009`: Source-Layer and Derived-Layer Tokenizers for Igbo: A Bounded Nwagu Aneke Baseline (`009-igbo-tokenization`)

## Stop Rule

Continue approved-paper loops until approved count is 10 / 10. Do not count
working drafts, formatted notes, review-blocked manuscripts, or papers with
rights/source/citation blockers.
