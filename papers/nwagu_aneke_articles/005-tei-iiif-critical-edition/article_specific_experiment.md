# Article-Specific Experiment: EXP-NA-005

## Research Question

Can source-layer Nwagu Aneke records be mapped into TEI glyph declarations and
Web Annotation selector leads without claiming a complete IIIF critical edition?

## Hypothesis

If each mapped record preserves its TEI locator, Web Annotation body, selector
type, review status, and missing pixel-coordinate boundary, then the article can
support a standards bridge while blocking unsupported claims about source-image
annotation and public release.

## Inputs

- `experiments/EXP-NA-005-tei-iiif-selectors/results.json`
- `experiments/EXP-NA-005-tei-iiif-selectors/data/tei_glyph_declarations.jsonl`
- `experiments/EXP-NA-005-tei-iiif-selectors/data/web_annotation_sample.jsonld`
- `experiments/EXP-NA-005/results.json`
- `papers/nwagu_aneke_articles/005-tei-iiif-critical-edition/selector_bridge_comparison.md`

## Result

The experiment records 10 TEI glyph declaration leads and 10 Web Annotation-style
records. All 10 records use selector-layer references and carry
`human_review_needed` / `partial_selector_no_pixel_coordinates` status. The
number of records with pixel coordinates is 0.

## Negative Control

A manuscript, table, figure, prompt, or interface fails the control if it calls
the sample a complete IIIF edition, displays source-image crops without
clearance, treats TextQuoteSelector values as pixel coordinates, or removes the
human-review-needed status.

## Claim Ceiling

The article can support a partial standards bridge and a precise missing-work
ledger. It cannot support public source-image release, complete glyph-shape
interpretation, coordinate-level annotation, or venue-ready critical-edition
claims.
