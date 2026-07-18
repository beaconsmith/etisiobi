# External Prior-Art Audit: ARTICLE-NA-005

## Scope

This audit supports the TEI, IIIF, and Web Annotation bridge article. The
article's result is narrow: ten records can be represented as TEI glyph
declaration leads and Web Annotation records, while pixel-coordinate IIIF
selectors remain blocked.

## Compared Literatures

1. Source-critical digital editions: TEI P5 provides structures for character,
   glyph, uncertainty, and editorial apparatus. The article uses TEI as a
   declaration layer, not as proof of complete glyph review.
2. Image-based cultural heritage: IIIF Presentation API and Web Annotation
   provide the target architecture for canvas and selector references. The
   current experiment uses textual selectors only, so it cannot claim
   coordinate-level edition status.
3. Provenance and research-object packaging: PROV-O, RO-Crate, DataCite, and
   CIDOC CRM show how to package entities, activities, derivations, and cultural
   heritage objects. The local gap is the transition from row/column evidence to
   reviewed source-image coordinates.
4. Governance and reuse: FAIR and CARE principles require that reuse and
   community authority boundaries remain visible. The article therefore keeps
   source-image release and public glyph crops blocked.
5. Claim verification and citation-grounded generation: SciFact, ALCE, and
   related work motivate checking that standards citations do not overstate the
   local evidence.
6. Script encoding practice: Unicode and Script Encoding Initiative guidance
   distinguish documentation samples from encoding proposals. A selector-layer
   bridge is evidence infrastructure, not repertoire approval.

## Novelty Claim Ceiling

The article may claim a standards-mapping sample and a clear missing-coordinate
boundary. It may not claim a complete critical edition, public image release,
completed IIIF manifest, reviewed glyph corpus, Unicode readiness, or community
authorization.

## Submission-Review Prior-Art Decision

`selector_bridge_comparison.md` now records the non-human comparison against TEI
glyph practice, IIIF Presentation API, Web Annotation, source-critical digital
editions, provenance/research-object packaging, FAIR, and CARE. Before external
submission, a human domain/source reviewer should still compare the public
wording against digital critical-edition expectations, IIIF annotation
workflows, African script documentation, and the target venue's standards. That
remaining item is a human sign-off gate, not an unresolved technical-evidence
blocker.
