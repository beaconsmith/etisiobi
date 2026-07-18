from __future__ import annotations

import json
import textwrap
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "papers" / "nwagu_aneke_articles"


REFERENCES = r"""
@article{azuonye1992,
  author = {Azuonye, Chukwuma},
  title = {The Nwagu Aneke Igbo Script: Its Origins, Features and Potentials as a Medium of Alternative Literacy in African Languages},
  journal = {Africana Studies Faculty Publication Series},
  number = {13},
  year = {1992},
  url = {https://scholarworks.umb.edu/africana_faculty_pubs/13/}
}

@misc{omniglotNwagu,
  author = {Ager, Simon},
  title = {Nwag{\d{u}} Aneke Syllabary},
  howpublished = {Omniglot},
  year = {n.d.},
  url = {https://www.omniglot.com/writing/nwaguaneke.htm},
  note = {Accessed 2026-06-20}
}

@misc{unicodeAfricanScripts2023,
  author = {{Unicode Consortium}},
  title = {2023 Update on African Scripts},
  howpublished = {Unicode Technical Committee document L2/23-203},
  year = {2023},
  url = {https://www.unicode.org/L2/L2023/23203-update-african-scripts.pdf}
}

@misc{scriptSourceNwagu,
  author = {{SIL International}},
  title = {Unicode Status (Nwagu Aneke Igbo)},
  howpublished = {ScriptSource},
  year = {n.d.},
  url = {https://scriptsource.org/cms/scripts/page.php?item_id=entry_detail&uid=mgqnsfqapq},
  note = {Accessed 2026-06-20}
}

@misc{seiProposalTips,
  author = {{Script Encoding Initiative}},
  title = {Tips for Writing Proposals},
  howpublished = {University of California, Berkeley},
  year = {n.d.},
  url = {https://sei.berkeley.edu/tips-for-proposals/},
  note = {Accessed 2026-06-20}
}

@misc{teiP5Glyphs,
  author = {{Text Encoding Initiative Consortium}},
  title = {TEI P5 Guidelines: Characters, Glyphs, and Writing Modes},
  howpublished = {TEI Guidelines},
  year = {n.d.},
  url = {https://www.tei-c.org/release/doc/tei-p5-doc/en/html/WD.html},
  note = {Accessed 2026-06-20}
}

@misc{iiifPresentation3,
  author = {{International Image Interoperability Framework Consortium}},
  title = {IIIF Presentation API 3.0},
  howpublished = {IIIF Specification},
  year = {n.d.},
  url = {https://iiif.io/api/presentation/3.0/},
  note = {Accessed 2026-06-20}
}

@misc{w3cAnnotationModel,
  author = {{World Wide Web Consortium}},
  title = {Web Annotation Data Model},
  howpublished = {W3C Recommendation},
  year = {2017},
  url = {https://www.w3.org/TR/annotation-model/}
}

@misc{w3cAnnotationVocab,
  author = {{World Wide Web Consortium}},
  title = {Web Annotation Vocabulary},
  howpublished = {W3C Recommendation},
  year = {2017},
  url = {https://www.w3.org/TR/annotation-vocab/}
}

@misc{w3cProvO,
  author = {{World Wide Web Consortium}},
  title = {PROV-O: The PROV Ontology},
  howpublished = {W3C Recommendation},
  year = {2013},
  url = {https://www.w3.org/TR/prov-o/}
}

@misc{rocrate12,
  author = {{RO-Crate Community}},
  title = {RO-Crate Metadata Specification 1.2.0},
  year = {2024},
  doi = {10.5281/zenodo.13751027},
  url = {https://zenodo.org/records/13751027}
}

@misc{cidocCrm,
  author = {{CIDOC CRM Special Interest Group}},
  title = {CIDOC Conceptual Reference Model},
  howpublished = {CIDOC CRM},
  url = {https://cidoc-crm.org/},
  note = {Accessed 2026-06-20}
}

@misc{datacite45,
  author = {{DataCite Metadata Working Group}},
  title = {DataCite Metadata Schema Documentation for the Publication and Citation of Research Data and Other Research Outputs, Version 4.5},
  year = {2024},
  doi = {10.14454/g8e5-6293},
  url = {https://schema.datacite.org/meta/kernel-4.5/}
}

@article{wilkinson2016fair,
  author = {Wilkinson, Mark D. and Dumontier, Michel and Aalbersberg, IJsbrand Jan and Appleton, Gabrielle and Axton, Myles and Baak, Arie and Blomberg, Niklas and Boiten, Jan-Willem and da Silva Santos, Luiz Bonino and Bourne, Philip E. and Bouwman, Jildau and Brookes, Anthony J. and Clark, Tim and Crosas, Merce and Dillo, Ingrid and Dumon, Olivier and Edmunds, Scott and Evelo, Chris T. and Finkers, Richard and Gonzalez-Beltran, Alejandra and Gray, Alasdair J. G. and Groth, Paul and Goble, Carole and Grethe, Jeffrey S. and Heringa, Jaap and 't Hoen, Peter A. C. and Hooft, Rob and Kuhn, Tobias and Kok, Ruben and Kok, Joost and Lusher, Scott J. and Martone, Maryann E. and Mons, Albert and Packer, Abel L. and Persson, Bengt and Rocca-Serra, Philippe and Roos, Marco and van Schaik, Rene and Sansone, Susanna-Assunta and Schultes, Erik and Sengstag, Thierry and Slater, Ted and Strawn, George and Swertz, Morris A. and Thompson, Mark and van der Lei, Johan and van Mulligen, Erik and Velterop, Jan and Waagmeester, Andra and Wittenburg, Peter and Wolstencroft, Katherine and Zhao, Jun and Mons, Barend},
  title = {The FAIR Guiding Principles for Scientific Data Management and Stewardship},
  journal = {Scientific Data},
  volume = {3},
  pages = {160018},
  year = {2016},
  doi = {10.1038/sdata.2016.18}
}

@article{carroll2020care,
  author = {Carroll, Stephanie Russo and Garba, Ibrahim and Figueroa-Rodriguez, Oscar L. and Holbrook, Jarita and Lovett, Raymond and Materechera, Simeon and Parsons, Mark and Raseroka, Kay and Rodriguez-Lonebear, Desi and Rowe, Robyn and Sara, Rodrigo and Walker, Jennifer D. and Anderson, Jane and Hudson, Maui},
  title = {The CARE Principles for Indigenous Data Governance},
  journal = {Data Science Journal},
  volume = {19},
  number = {1},
  pages = {43},
  year = {2020},
  doi = {10.5334/dsj-2020-043}
}

@misc{karpathyAutoresearch,
  author = {Karpathy, Andrej},
  title = {autoresearch: AI Agents Running Research on Single-GPU nanochat Training Automatically},
  howpublished = {GitHub repository},
  year = {n.d.},
  url = {https://github.com/karpathy/autoresearch},
  note = {Accessed 2026-06-20}
}

@misc{arxivSubmitTex,
  author = {{arXiv}},
  title = {Submit TeX/LaTeX},
  howpublished = {arXiv info},
  year = {n.d.},
  url = {https://info.arxiv.org/help/submit_tex.html},
  note = {Accessed 2026-06-20}
}

@misc{arxivTexLive,
  author = {{arXiv}},
  title = {TeX Live at arXiv},
  howpublished = {arXiv info},
  year = {n.d.},
  url = {https://info.arxiv.org/help/faq/texlive.html},
  note = {Accessed 2026-06-20}
}

@misc{acmSubmissions,
  author = {{Association for Computing Machinery}},
  title = {Submissions: The Workflow and Templates},
  howpublished = {ACM Publications},
  year = {n.d.},
  url = {https://www.acm.org/publications/authors/submissions},
  note = {Accessed 2026-06-20}
}

@misc{sirisNwaguProposal,
  author = {{Smithsonian Libraries and Archives}},
  title = {The Nwagu Aneke Research Project Proposal},
  howpublished = {SIRIS library catalogue record},
  year = {n.d.},
  url = {https://siris-libraries.si.edu/ipac20/ipac.jsp?uri=full=3100001~!553317~!0},
  note = {Accessed 2026-06-20}
}
"""


ARTICLES = [
    {
        "id": "ARTICLE-NA-001",
        "slug": "001-source-critical-reconstruction",
        "title": "A Source-Critical Reconstruction of the Nwagu Aneke Igbo Syllabary",
        "keywords": "Nwagu Aneke, Igbo syllabary, source criticism, artifact reconstruction, African writing systems",
        "abstract": "This article reconstructs what can be stated about the Nwagu Aneke Igbo syllabary from the current local evidence package without importing later PAGC theory. The contribution is a source-critical ledger: it aligns the Azuonye source anchor, local chart transcription, symbol inventory, 208-record row-vowel index, and uncertainty notes. The main result is deliberately narrow. The present evidence supports a source-observed 26 by 8 ledger and a derived f/v split layer, but it does not yet support a finished glyph corpus or public reproduction of source images. The article therefore establishes a globally reviewable baseline for future linguistic, digital-humanities, and systems-design work.",
        "question": "What exactly can be reconstructed from the current Nwagu Aneke source package without assuming PAGC, exceptional mathematics, or universal compression?",
        "central_claim": "The publishable object is a source-critical reconstruction ledger, not yet a complete glyph corpus.",
        "method": "The method aligns EXP-NA-001 evidence rows with local source files, then classifies each claim as source-observed, derived, secondary, or blocked.",
        "result": "The ledger supports 26 source-observed rows, eight vowel/modifier columns, and 208 row-vowel index records; all 208 BMC entries still require human review and lack source-region coordinates.",
        "citations": ["azuonye1992", "omniglotNwagu", "unicodeAfricanScripts2023", "sirisNwaguProposal", "carroll2020care"],
    },
    {
        "id": "ARTICLE-NA-002",
        "slug": "002-count-layer-drift",
        "title": "Count-Layer Drift in Nwagu Aneke: Auditing 26 by 8, 27, 216, 164, and 224 Claims",
        "keywords": "count-layer drift, symbolic inventory, Nwagu Aneke, claim audit, reproducibility",
        "abstract": "Exact counts are powerful but dangerous in symbolic research: they compress evidence, interpretation, and theory into numbers that can easily drift across abstraction layers. This article treats Nwagu Aneke count claims as an audit object. The current evidence package distinguishes a source-observed 26 by 8 layer from a derived 27/216 f/v split layer, while treating 164 and 224 as external leads that require line-verified source extraction. The contribution is a count-layer method for preventing downstream design or theory work from promoting derived counts into source claims.",
        "question": "Can the known Nwagu Aneke count claims be represented as separate evidence layers rather than forced into one authoritative number?",
        "central_claim": "The current evidence supports multi-layer count reconciliation, not a single magic count.",
        "method": "The audit treats every count as a tuple of source, locator, abstraction layer, confidence, and allowed downstream use.",
        "result": "The source layer is 26 rows by 8 columns, while 27 and 216 are valid only as a derived f/v split layer pending review; 164 and 224 remain source leads, not confirmed results.",
        "citations": ["azuonye1992", "omniglotNwagu", "unicodeAfricanScripts2023", "scriptSourceNwagu", "wilkinson2016fair"],
    },
    {
        "id": "ARTICLE-NA-003",
        "slug": "003-f-v-hinge",
        "title": "The f/v Hinge: Orthographic Economy and Derived-Layer Design in Nwagu Aneke",
        "keywords": "Igbo orthography, f/v split, syllabary design, Nwagu Aneke, derived layers",
        "abstract": "The f/v row is the hinge between the source-observed and derived layers of the current Nwagu Aneke research program. This article examines the row as a design and interpretation problem rather than as a resolved phonological claim. Locally, f/v appears as one printed row in a 26-row source layer. Splitting it yields a derived 27-row and 216-cell layer, but that split cannot be represented as source-observed without further linguistic and source review. The article frames f/v as a controlled interface between orthographic economy, dialectal interpretation, and system-design applications.",
        "question": "What research claims become possible, and which become unsafe, when the f/v row is treated as a hinge between source and derived layers?",
        "central_claim": "The f/v split is a useful derived design operation only when it remains explicitly labeled as derived.",
        "method": "The article compares source labels, derived count effects, and downstream design consequences under a layer-safety rule.",
        "result": "The f/v hinge explains the 26-to-27 transition without requiring any claim that 27 rows are printed in the current chart evidence.",
        "citations": ["azuonye1992", "omniglotNwagu", "carroll2020care", "w3cProvO", "wilkinson2016fair"],
    },
    {
        "id": "ARTICLE-NA-004",
        "slug": "004-logographs-in-a-syllabary",
        "title": "Logographs in a Syllabary: Separating Whole-Word Signs from Nwagu Aneke CV Cells",
        "keywords": "logographs, syllabary, Nwagu Aneke, sign inventory, African scripts",
        "abstract": "Public descriptions of Nwagu Aneke identify it as a syllabary with some logographic symbols, but a reviewable corpus must keep those layers separate. This article proposes a logograph ledger for whole-word signs observed in the local chart transcription and secondary sources. The contribution is not a completed logograph corpus. It is a research design that separates CV cell reconstruction from whole-word sign reconstruction, preventing logographs from being miscounted as syllabic cells or used as evidence for unsupported generative claims.",
        "question": "How should Nwagu Aneke whole-word signs be represented without contaminating the CV syllabary count layer?",
        "central_claim": "Logographs require a separate ledger with separate evidence, review, and publication gates.",
        "method": "The method defines a logograph record with source locator, reading, semantic gloss, confidence, and relation to CV cells.",
        "result": "The current evidence supports a visible lead set, not a complete logograph inventory; this is enough to specify the next corpus task.",
        "citations": ["azuonye1992", "omniglotNwagu", "unicodeAfricanScripts2023", "teiP5Glyphs", "w3cAnnotationModel"],
    },
    {
        "id": "ARTICLE-NA-005",
        "slug": "005-tei-iiif-critical-edition",
        "title": "Toward a TEI/IIIF Critical Edition of an Unencoded African Syllabary",
        "keywords": "TEI, IIIF, critical edition, Nwagu Aneke, digital humanities",
        "abstract": "Unencoded scripts require digital editions that can preserve evidence before Unicode encoding is available. This article specifies a TEI/IIIF critical-edition path for Nwagu Aneke. TEI provides character and glyph modeling tools; IIIF provides canvases and annotation pages; Web Annotation provides body, target, and motivation structures. The Nwagu Aneke case shows why these standards must be combined with uncertainty and authority gates: a digital edition must represent what is visible, what is transcribed, what is inferred, and what remains blocked by rights or review.",
        "question": "Can Nwagu Aneke be represented as a standards-compatible critical edition before Unicode encoding?",
        "central_claim": "A standards-compatible critical edition is possible as a staged artifact, but not yet as a public final corpus.",
        "method": "The article maps chart rows, vowel columns, source images, and review states into TEI, IIIF, and Web Annotation roles.",
        "result": "The standards path is technically clear; the limiting factors are source-image rights, selector-level annotation, and human glyph review.",
        "citations": ["teiP5Glyphs", "iiifPresentation3", "w3cAnnotationModel", "w3cAnnotationVocab", "azuonye1992"],
    },
    {
        "id": "ARTICLE-NA-006",
        "slug": "006-unicode-readiness",
        "title": "Unicode Readiness for Nwagu Aneke: Character, Glyph, Evidence, and Community Review",
        "keywords": "Unicode, script encoding, Nwagu Aneke, character-glyph distinction, standardization",
        "abstract": "Nwagu Aneke is not currently encoded in Unicode, and the present research package is not a Unicode proposal. This article defines what a future readiness dossier would need: stable repertoire evidence, character-glyph distinctions, names, representative glyphs, usage examples, directionality, sorting assumptions, community authority, and publication rights. The result is a gap matrix rather than an encoding claim. Its value is to prevent premature standardization while making the evidence requirements explicit for future community-led encoding work.",
        "question": "What evidence would a globally credible Unicode-readiness dossier for Nwagu Aneke require?",
        "central_claim": "Unicode readiness is a structured gap-analysis task, not an automatic consequence of a source chart.",
        "method": "The article compares the local source ledger against Unicode, ScriptSource, and Script Encoding Initiative expectations.",
        "result": "The local package supports early repertoire discussion but lacks glyph-level corpus, public usage evidence, and authority-reviewed character decisions.",
        "citations": ["unicodeAfricanScripts2023", "scriptSourceNwagu", "seiProposalTips", "azuonye1992", "carroll2020care"],
    },
    {
        "id": "ARTICLE-NA-007",
        "slug": "007-manuscript-corpus-provenance",
        "title": "Manuscript Corpus Provenance for Nwagu Aneke: A CARE-First Research Plan",
        "keywords": "manuscript provenance, CARE principles, African knowledge systems, Nwagu Aneke, authority review",
        "abstract": "Azuonye and later public summaries describe a substantial Nwagu Aneke manuscript corpus, but the current local evidence package does not contain a rights-cleared corpus. This article treats manuscript provenance as the next foundational research problem. It proposes a CARE-first ledger for holdings, custodianship, review authority, permitted uses, and publication constraints. The contribution is a protocol for moving from public claims about manuscript abundance to ethically reviewable corpus research without exposing sensitive or unauthorized materials.",
        "question": "How can the lab locate and study the Nwagu Aneke manuscript corpus without turning cultural authority into a technical afterthought?",
        "central_claim": "Manuscript provenance must precede public corpus claims and data release.",
        "method": "The proposed ledger records holding institution, owner/custodian, access condition, review authority, permitted output type, and evidence locator.",
        "result": "The present article can define the protocol, but cannot claim full corpus access or public release clearance.",
        "citations": ["azuonye1992", "sirisNwaguProposal", "carroll2020care", "wilkinson2016fair", "datacite45"],
    },
    {
        "id": "ARTICLE-NA-008",
        "slug": "008-comparative-standardization",
        "title": "Comparative Standardization Paths for African Syllabaries: Positioning Nwagu Aneke",
        "keywords": "African scripts, standardization, Unicode, comparative writing systems, Nwagu Aneke",
        "abstract": "Nwagu Aneke should be compared with other African script standardization paths without collapsing those histories into one model. This article proposes a comparative matrix over repertoire evidence, manuscript corpus, teaching use, digital tools, Unicode status, community authority, and rights readiness. The contribution is a research instrument: a way to position Nwagu Aneke among African syllabaries and symbolic systems while preserving the specific evidence requirements of each case.",
        "question": "Which comparative dimensions are useful for studying Nwagu Aneke without forcing it into a borrowed script-development template?",
        "central_claim": "Comparative standardization should compare evidence conditions, not just script typology.",
        "method": "The paper specifies a matrix using public status sources, Unicode reports, and local evidence categories.",
        "result": "Nwagu Aneke currently belongs in the unencoded, source-promising, review-blocked category rather than the release-ready category.",
        "citations": ["unicodeAfricanScripts2023", "scriptSourceNwagu", "seiProposalTips", "omniglotNwagu", "carroll2020care"],
    },
    {
        "id": "ARTICLE-NA-009",
        "slug": "009-igbo-tokenization",
        "title": "Igbo Tokenization from a Source-Grounded Nwagu Aneke Layer: A Research Design",
        "keywords": "Igbo NLP, tokenization, syllabary, Nwagu Aneke, low-resource language technology",
        "abstract": "The Nwagu Aneke source layer suggests tokenizer experiments for Igbo, but those experiments must not claim universal compression or historical validation from a design feature alone. This article defines a conservative research design: compare standard subword baselines to source-layer and derived-layer tokenizers while preserving layer labels, corpus cards, and confidence intervals. The result is a testable NLP agenda. A positive tokenizer result would show task-specific utility, not proof that the artifact is a universal compression system.",
        "question": "Can source-grounded syllabary structure inform Igbo tokenization experiments without overclaiming what the artifact proves?",
        "central_claim": "The proper claim is task-specific representational utility, not universal compression.",
        "method": "The proposed experiment compares BPE, unigram, source-layer CV tokens, and derived f/v tokens under fixed corpora and seeds.",
        "result": "No tokenizer result is claimed here; the article specifies the globally reviewable experiment needed before such claims are allowed.",
        "citations": ["azuonye1992", "wilkinson2016fair", "karpathyAutoresearch", "arxivSubmitTex", "carroll2020care"],
    },
    {
        "id": "ARTICLE-NA-010",
        "slug": "010-layer-safe-generative-design",
        "title": "Layer-Safe Generative Design Systems from Nwagu Aneke",
        "keywords": "generative design, symbolic systems, layer safety, Nwagu Aneke, research governance",
        "abstract": "Nwagu Aneke can inspire novel systems only if design layers do not masquerade as historical source claims. This article formalizes a layer-safe design rule for artifact-derived systems: source-observed, derived, speculative, and blocked claims must be typed separately, and outputs may not promote derived or speculative labels into source-observed labels. The contribution is a systems-design article grounded in the Nwagu Aneke count-layer case. It supports creative application while preserving the evidence boundary needed for scholarly review.",
        "question": "How can designers build from Nwagu Aneke without turning creative derivations into false source claims?",
        "central_claim": "Layer safety is the minimum research invariant for artifact-derived generative systems.",
        "method": "The article translates the source/derived distinction into a typed pipeline and checks design outputs against promotion errors.",
        "result": "The count-layer case gives a concrete invariant: source 26 by 8 and derived 27/216 may both be useful, but only if their labels cannot collapse.",
        "citations": ["azuonye1992", "w3cProvO", "rocrate12", "wilkinson2016fair", "karpathyAutoresearch"],
    },
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def cite_list(keys: list[str]) -> str:
    return ", ".join(f"\\cite{{{key}}}" for key in keys)


def article_tex(article: dict[str, object]) -> str:
    cites = cite_list(article["citations"])  # type: ignore[arg-type]
    return rf"""
    \documentclass[sigconf,nonacm]{{acmart}}
    \settopmatter{{printacmref=false}}
    \setcopyright{{none}}
    \renewcommand\footnotetextcopyrightpermission[1]{{}}
    \pagestyle{{plain}}

    \acmConference[Etisiobi Research Draft]{{Etisiobi Nwagu Aneke Article Program}}{{June 2026}}{{Enugu, Nigeria}}
    \acmYear{{2026}}
    \acmISBN{{}}
    \acmDOI{{}}

    \title{{{article["title"]}}}
    \author{{The Beaconsmith Collective}}
    \affiliation{{
      \institution{{Etisiobi Research Studio}}
      \city{{Enugu}}
      \country{{Nigeria}}
    }}
    \email{{research@example.invalid}}

    \begin{{abstract}}
    {article["abstract"]}
    \end{{abstract}}

    \keywords{{{article["keywords"]}}}

    \begin{{document}}
    \maketitle

    \section{{Research Question}}
    {article["question"]}

    \section{{Evidence Base}}
    The article is derived from the Nwagu Aneke source package and the
    EXP-NA-001 reconstruction result. The current baseline is source-observed
    26 rows by 8 vowel/modifier columns, giving 208 row-vowel ledger records.
    The 27/216 layer is treated only as a derived f/v split layer. The article
    uses Azuonye as the primary academic anchor and uses public standards only
    for method comparison and publication framing: {cites}.

    \section{{Central Claim}}
    \textbf{{Claim.}} {article["central_claim"]}

    This claim is intentionally scoped. It does not assert that the complete
    manuscript corpus has been digitized, that the glyph-shape corpus is
    complete, that 27/216 is source-observed, or that Nwagu Aneke validates
    universal compression, exceptional mathematics, or any other speculative
    PAGC branch.

    \section{{Method}}
    {article["method"]} The method follows four gates: source existence,
    locator availability, layer label, and human-review requirement. A claim
    that fails one of these gates can still be useful, but it must move to
    limitations, future work, or speculative design rather than becoming a
    positive result.

    \section{{Findings}}
    {article["result"]} This is sufficient for a globally reviewable article
    draft because it states exactly what can be read today and what remains
    blocked. It is not sufficient for final public submission until rights,
    source-image, and authority review are attached.

    \begin{{table}}[t]
    \caption{{Claim gate for {article["id"]}}}
    \label{{tab:claim-gate}}
    \begin{{tabular}}{{p{{0.28\columnwidth}}p{{0.62\columnwidth}}}}
    \toprule
    Claim class & Allowed status \\
    \midrule
    Source layer & 26 by 8 equals 208, pending human source review \\
    Derived layer & 27/216 only when labeled as f/v split derivation \\
    Glyph corpus & Not complete; must not be claimed as complete \\
    Public release & Blocked until rights and authority review \\
    Speculative systems & Allowed only as labeled design hypotheses \\
    \bottomrule
    \end{{tabular}}
    \end{{table}}

    \section{{Relation to Global Standards}}
    The formatting target is ACM-style two-column article layout using
    \texttt{{acmart}} in \texttt{{sigconf,nonacm}} mode, with a top matter
    abstract, keywords, numbered sections, tables, BibTeX citations, and an
    explicit limitations section. The source package should remain compatible
    with arXiv source-submission guidance: no hidden files, no external image
    dependencies, no shell escape, no minted cache, and no absolute paths
    \cite{{acmSubmissions,arxivSubmitTex,arxivTexLive}}.

    \section{{Limitations and Human Review}}
    The article is a draft for review, not a submission authorization. The
    required human gates are: source transcription review, rights review for
    images and manuscript excerpts, cultural authority review, and final
    author approval. The CARE and FAIR principles are treated as governance
    constraints for any public corpus or dataset release
    \cite{{carroll2020care,wilkinson2016fair}}.

    \section{{Reproducibility}}
    The local evidence path is \texttt{{experiments/EXP-NA-001-source-critical-reconstruction/}}.
    Regenerate the source reconstruction with
    \texttt{{python scripts/run\_na\_source\_reconstruction.py}}. Validate the
    manuscript package with
    \texttt{{python scripts/validate\_nwagu\_article\_manuscripts.py}}.

    \section{{Conclusion}}
    This article turns the Nwagu Aneke artifact into a disciplined research
    object for one publishable question. Its standard of success is not that
    every downstream application is already proven. Its standard is that the
    article can be read, reviewed, cited, rejected, or improved without
    confusing source evidence with derived or speculative design.

    \bibliographystyle{{ACM-Reference-Format}}
    \bibliography{{../references}}
    \end{{document}}
    """


def status_md(article: dict[str, object]) -> str:
    return f"""
    # {article["id"]}: {article["title"]}

    ## Format

    - LaTeX: `acmart`
    - Mode: `sigconf,nonacm`
    - Layout: double column
    - Abstract: top matter abstract before `\\maketitle`
    - Citations: BibTeX, shared `../references.bib`

    ## Central Claim

    {article["central_claim"]}

    ## Evidence Discipline

    - Source-observed layer: 26 x 8 = 208.
    - Derived layer: 27/216 only by f/v split.
    - Glyph-level corpus: not complete.
    - Public release: requires rights and authority review.

    ## Current Status

    `DRAFT_FOR_HUMAN_REVIEW_NOT_SUBMISSION_READY`
    """


def readme(generated_at: str) -> str:
    rows = "\n".join(
        f"| {article['id']} | [{article['title']}]({article['slug']}/main.tex) | DRAFT_FOR_HUMAN_REVIEW |"
        for article in ARTICLES
    )
    return f"""
    # Nwagu Aneke Ten-Article Manuscript Package

    Generated: {generated_at}

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
    {rows}

    ## Compile One Article

    ```powershell
    cd papers\\nwagu_aneke_articles\\001-source-critical-reconstruction
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    ```

    ## Validate Package

    ```powershell
    python scripts\\validate_nwagu_article_manuscripts.py
    ```
    """


def manifest(generated_at: str) -> dict[str, object]:
    return {
        "generated_at": generated_at,
        "format": "ACM-style double-column LaTeX",
        "documentclass": "acmart",
        "options": ["sigconf", "nonacm"],
        "article_count": len(ARTICLES),
        "source_observed_layer": {"rows": 26, "columns": 8, "records": 208},
        "derived_layer": {"rows_if_f_v_split": 27, "records_if_f_v_split": 216},
        "status": "DRAFT_FOR_HUMAN_REVIEW_NOT_SUBMISSION_READY",
        "human_gates": [
            "source transcription review",
            "rights review",
            "cultural/source authority review",
            "final author approval",
        ],
        "articles": [
            {
                "id": article["id"],
                "title": article["title"],
                "slug": article["slug"],
                "tex_path": f"{article['slug']}/main.tex",
                "citations": article["citations"],
            }
            for article in ARTICLES
        ],
    }


def main() -> int:
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT / "references.bib", REFERENCES)
    write(OUT / "README.md", readme(generated_at))
    (OUT / "manifest.json").write_text(json.dumps(manifest(generated_at), indent=2) + "\n", encoding="utf-8")

    for article in ARTICLES:
        article_dir = OUT / str(article["slug"])
        write(article_dir / "main.tex", article_tex(article))
        write(article_dir / "STATUS.md", status_md(article))

    print("NWAGU_ARTICLE_MANUSCRIPTS_GENERATED")
    print(f"articles={len(ARTICLES)}")
    print(f"output={OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
