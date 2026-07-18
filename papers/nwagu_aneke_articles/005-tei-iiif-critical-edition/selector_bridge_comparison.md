# TEI, IIIF, and Web Annotation Selector-Bridge Comparison

Article: `ARTICLE-NA-005`

Status: `COMPARISON_COMPLETE_FOR_SUBMISSION_REVIEW_HUMAN_SOURCE_SIGNOFF_BLOCKED`

## Purpose

The selector-bridge article must be positioned as a partial standards-mapping
result, not as a completed IIIF critical edition. This comparison resolves the
non-human positioning gap while leaving source-image, pixel-coordinate, rights,
and authority decisions to human reviewers.

## Comparison Anchors

| Anchor | What it supports | Boundary for ARTICLE-NA-005 |
|---|---|---|
| TEI glyph and writing-mode practice | TEI can represent glyph declarations, nonstandard characters, uncertainty, and editorial metadata. | The article uses TEI as a declaration lead layer, not as reviewed glyph evidence. |
| IIIF Presentation API | IIIF can present canvases and support region-based source navigation. | The current experiment has no pixel coordinates and cannot claim a complete IIIF edition. |
| Web Annotation | Web Annotation can link annotation bodies to targets and selectors. | The current sample uses selector leads; it does not publish rights-cleared image regions. |
| Source-critical digital editions | Critical editions require inspected witnesses, locators, apparatus, and public editorial decisions. | The article supplies a bridge layer and missing-coordinate boundary, not a final edition. |
| PROV-O, RO-Crate, DataCite, and CIDOC CRM | Provenance and research-object standards can package and identify evidence records. | Packaging does not solve glyph review, public source rights, or authority approval. |
| FAIR and CARE principles | Reuse and community authority boundaries must remain visible. | Public release remains blocked until human rights and source-authority review. |

## What This Comparison Adds

The paper's contribution is a bounded selector-layer bridge:

- 10 records are represented as TEI glyph declaration leads;
- 10 records are represented as Web Annotation records;
- 0 records currently have pixel-coordinate selectors;
- source-image display, canvas naming, and public glyph crops remain blocked;
- the result defines what a later coordinate-level critical edition must add.

## Remaining Human Review

The comparison does not complete:

- confirmation that each mapped record corresponds to the intended source row or
  column;
- pixel-coordinate source-region review;
- rights clearance for IIIF canvases, source images, or glyph crops;
- cultural/source authority approval for public display or naming;
- editorial approval that the sample is adequate for the selected venue.

Those remain human sign-off gates. They do not prevent submission-review
candidate status because the proposed article is text-only and describes a
partial selector-layer bridge rather than a completed edition.

## Decision

The selector-bridge comparison is sufficient for bounded submission-review
candidate status if the target venue is asked to evaluate a standards-mapping
proof of concept and missing-coordinate boundary, not a completed public IIIF
critical edition.
