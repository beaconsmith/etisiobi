# Nwagu Aneke Ten-Article Manuscript Package

    Generated: 2026-06-20T00:16:11+01:00

    This package contains ten Nwagu Aneke-derived research article drafts in
    double-column ACM-style LaTeX. Each article uses a central top abstract,
    full BibTeX citations, explicit limitations, and a claim gate that preserves
    the current source/derived distinction:

    ```text
    source-observed: 26 rows x 8 vowel/modifier columns = 208 records
    derived: 27 / 216 only when the f/v row is split
    ```

    These are review drafts, not public-submission approvals.

    | ID | Manuscript | Status |
    |---|---|---|
    | ARTICLE-NA-001 | [A Source-Critical Reconstruction of the Nwagu Aneke Igbo Syllabary](001-source-critical-reconstruction/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-002 | [Count-Layer Drift in Nwagu Aneke: Auditing 26 by 8, 27, 216, 164, and 224 Claims](002-count-layer-drift/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-003 | [The f/v Hinge: Orthographic Economy and Derived-Layer Design in Nwagu Aneke](003-f-v-hinge/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-004 | [Logographs in a Syllabary: Separating Whole-Word Signs from Nwagu Aneke CV Cells](004-logographs-in-a-syllabary/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-005 | [Toward a TEI/IIIF Critical Edition of an Unencoded African Syllabary](005-tei-iiif-critical-edition/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-006 | [Unicode Readiness for Nwagu Aneke: Character, Glyph, Evidence, and Community Review](006-unicode-readiness/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-007 | [Manuscript Corpus Provenance for Nwagu Aneke: A CARE-First Research Plan](007-manuscript-corpus-provenance/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-008 | [Comparative Standardization Paths for African Syllabaries: Positioning Nwagu Aneke](008-comparative-standardization/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-009 | [Igbo Tokenization from a Source-Grounded Nwagu Aneke Layer: A Research Design](009-igbo-tokenization/main.tex) | DRAFT_FOR_HUMAN_REVIEW |
| ARTICLE-NA-010 | [Layer-Safe Generative Design Systems from Nwagu Aneke](010-layer-safe-generative-design/main.tex) | DRAFT_FOR_HUMAN_REVIEW |

    ## Compile One Article

    ```powershell
    cd papers\nwagu_aneke_articles\001-source-critical-reconstruction
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    ```

    ## Validate Package

    ```powershell
    python scripts\validate_nwagu_article_manuscripts.py
    ```
