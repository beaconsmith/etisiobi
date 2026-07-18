# External Prior-Art Audit: ARTICLE-NA-003

## Scope

This audit supports the f/v hinge article. The article's result is narrow: the
f/v split is a deterministic derived operation over the local Nwagu Aneke
inventory, not a primary source-row claim.

## Compared Literatures

1. African writing-system documentation and script-status references: Azuonye's
   public account of Nwagu Aneke, Omniglot, ScriptSource, the Smithsonian record,
   and the Unicode African scripts update establish that the script is a real
   documentation object, but they do not license promotion of a derived f/v split
   into a source-observed row count.
2. Unicode and script-proposal practice: proposal guidance requires stable
   repertoire evidence, names, examples, usage, and community review. The f/v
   hinge audit is useful pre-proposal evidence, but it is not a repertoire
   proposal.
3. Digital humanities source criticism: TEI, IIIF, Web Annotation, PROV-O,
   RO-Crate, CIDOC CRM, FAIR, CARE, and DataCite show how to preserve source,
   transcription, derivation, package, and governance metadata. The local gap is
   not metadata vocabulary; it is a decision rule for when a split is permitted.
4. Claim-verification and citation-grounded generation: SciFact, ALCE, and
   related evaluation work make the evidence-claim boundary inspectable, but the
   Nwagu Aneke article adds an artifact-specific promotion rule for source vs.
   derived inventory claims.
5. Tokenization and orthographic modeling: subword/tokenizer literature shows
   that small segmentation choices can materially affect downstream systems. The
   hinge audit therefore treats the f/v split as a modeling choice with provenance,
   not as a silent source correction.

## Novelty Claim Ceiling

The article may claim a formal derived-layer audit for the f/v hinge inside the
current local evidence package. It may not claim priority over all African script
documentation, a complete phonological account of Igbo, a completed Unicode
proposal, or a public glyph corpus.

## Submission-Review Prior-Art Decision

`orthographic_hinge_comparison.md` now records the non-human comparison against
writing-system documentation, orthographic modeling, script proposal practice,
digital-humanities source infrastructure, and claim verification. Before
external submission, a human domain/source reviewer should still compare the
public wording against African orthographic history and the target venue's
expectations. That remaining item is a human sign-off gate, not an unresolved
technical-evidence blocker.
