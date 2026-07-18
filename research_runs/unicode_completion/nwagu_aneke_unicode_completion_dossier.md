# Nwagu Aneke Unicode Completion Dossier

Status: `UNICODE_COMPLETION_BLOCKED_EVIDENCE_PACKAGE`

This dossier prioritizes Nwagu Aneke for standards-facing completion work while
blocking premature submission. It is based on the current repo evidence and the
current public Unicode/SEWG submission requirements checked on 2026-07-07.

## External Submission Requirements Checked

Unicode/SEWG guidance says new script and character proposals must distinguish
characters from glyphs, submit through the SEW submission form, and provide a
single PDF proposal document. Proposed new scripts and characters need evidence
for usage, stability, and need for plain-text interchange. Proposal materials
generally include introduction/background, comparison with visually similar
characters, suggested properties, ordering, punctuation and line/word breaking
behavior, and, where shaping exists, enough glyph examples for implementers.
The submission form also collects UnicodeData/property changes, ISO/IEC 10646
summary information, and font files where applicable. A Unicode CLA is required
for submitter and authors, and potential IP holders may need endorsement and
licensing decisions.

Source URLs:

- https://sew.unicode.org/guidelines
- https://www.unicode.org/pending/docsubmit.html
- https://www.unicode.org/faq/char_proposal.html
- https://www.unicode.org/L2/L2023/23105r-new-script-template-april2023.pdf
- https://sei.berkeley.edu/2025/04/03/script-readiness-rubric/

## Current Repo Evidence

Present:

- Script identity is supported enough for readiness analysis.
- The source-observed count foundation is 26 rows by 8 vowel/modifier columns,
  yielding 208 records.
- The 27/216 layer is recorded as derived by f/v split only.
- `ARTICLE-NA-006` supplies a twelve-row Unicode-readiness matrix.
- `ARTICLE-NA-002` supplies count-layer discipline needed before repertoire
  claims.
- `ARTICLE-NA-010` supplies a non-promotion invariant for generated or derived
  representations.

Partial:

- Repertoire inventory exists as a source-table discussion, not a completed
  character repertoire.
- Character-glyph distinction is described, but not expert-reviewed across a
  public example set.
- Directionality is discussed from public descriptions, but needs source
  confirmation.
- Character-name material may be derivable from row/vowel readings, but no
  Unicode-style names list exists.

Blocked:

- Representative glyphs require source-image or glyph-example rights review.
- Usage examples require public source permissions or citable sources.
- The submitter relationship to Nwagu Aneke users, source holders, or scholarly
  sources must be documented. This is not a universal permission veto, but it is
  part of a credible new-script proposal.
- Public source-image or manuscript release remains out of scope.

Missing:

- Encoding model.
- Proposed character repertoire with names and properties.
- Punctuation and number evidence.
- Collation, segmentation, line-breaking, ordering, shaping, and normalization
  behavior.
- Font with appropriate licence.
- Proposal PDF and ISO/IEC 10646 summary information.
- CLA/IP-holder/author/submitter decisions.

## Completion Criteria Before Submission

A Nwagu Aneke Unicode proposal may be drafted by an independent submitter after
these checks are complete:

1. Source transcription review verifies the repertoire basis.
2. Every proposed character is separated from glyph variants, ligatures,
   abbreviations, derived analytical rows, and sequences of existing Unicode
   characters.
3. Representative glyph examples are rights-cleared and source-captioned.
4. Usage, stability, and interchange-need evidence is collected.
5. The submitter's relationship to users, source holders, and scholarly sources
   is documented, along with any consultation that has occurred or remains
   impossible.
6. Character names, ordering, properties, directionality, punctuation/numbers,
   segmentation, line breaking, shaping behavior, and normalization implications
   are drafted.
7. A publishable font or font plan with appropriate licence is available.
8. Authors, submitter, Unicode CLA status, potential IP holders, and any actual
   endorsement needs are resolved.
9. A proposal PDF and ISO/IEC 10646 summary information are prepared.
10. Human source, rights, and final package sign-offs approve submission.

## Current Decision

`DO_NOT_SUBMIT`

Do not submit the Nwagu Aneke package to Unicode, SEWG, UTC, or any external
standards body in its current state.

The next artifact should be a preliminary standards inquiry or readiness
research packet, not a formal proposal submission.
