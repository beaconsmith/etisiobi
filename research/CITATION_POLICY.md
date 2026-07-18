# Citation Policy

> Standards for how sources are cited, stored, and referenced across all papers.

---

## Citation Preferences

1. **DOI preferred** — If a source has a DOI, use it as the canonical identifier.
2. **Stable URL fallback** — If no DOI, use the most stable URL available (institutional repository > publisher > personal site > blog).
3. **Archive.org backup** — For web sources at risk of disappearing, note an archive.org snapshot URL if available.

---

## BibTeX Key Convention

Format: `AuthorYear` with disambiguation letter if needed.

Examples:
- `Tyler2006` — Tyler, Tom R. 2006
- `Ostrom1990` — Ostrom, Elinor. 1990
- `Ferreira2026` — Ferreira, Pedro. 2026
- `Aguerre2024` — Aguerre et al. 2024
- `HessOstrom2003` — Hess and Ostrom. 2003

For multiple works by same author in same year: `Tyler2006a`, `Tyler2006b`

---

## Local PDF Storage

Store downloaded PDFs in `library/papers/` with naming convention:

`Author_Year_ShortTitle.pdf`

Examples:
- `Muwafu_2024_InformalGovernanceUrbanSSA.pdf`
- `Tyler_2006_PsychologicalPerspectivesLegitimacy.pdf`
- `Ferreira_2026_MythsBlockchainGovernance.pdf`

---

## Quote Preservation Rules

When preserving a quote in `quote_bank.md`:

1. Copy exact text — do not paraphrase
2. Include page number or section reference
3. Include full citation
4. Note why the quote is worth preserving
5. Mark any emphasis added vs. original emphasis

---

## Cross-Paper Source Sharing

Sources used across multiple papers:
- Maintain a single entry in `library/papers/`
- Reference by BibTeX key in each paper's `source_registry.md`
- Note which papers use it: `Used in: T11, T1, T7`

---

## Forbidden Practices

- ❌ Citing a source you have not actually read (at least abstract + relevant sections)
- ❌ Citing a Wikipedia article as a primary source (use the sources Wikipedia cites)
- ❌ Citing a blog post as evidence for an empirical claim
- ❌ Fabricating page numbers
- ❌ Using "[n.d.]" when the year is findable
- ❌ Citing "personal communication" without specifying who and when
