from __future__ import annotations

import json
import re
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"
SUMMARY = ROOT / "experiments" / "nwagu_aneke_article_experiments" / "results.json"
BENCH = ROOT / "benchmarks" / "nwagu_article_research" / "scoreboard.json"


EXTRA_REFERENCES = r"""
@inproceedings{sennrich2016bpe,
  author = {Sennrich, Rico and Haddow, Barry and Birch, Alexandra},
  title = {Neural Machine Translation of Rare Words with Subword Units},
  booktitle = {Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics},
  year = {2016},
  doi = {10.18653/v1/P16-1162}
}

@inproceedings{kudo2018sentencepiece,
  author = {Kudo, Taku and Richardson, John},
  title = {SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing},
  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
  year = {2018},
  doi = {10.18653/v1/D18-2012}
}

@inproceedings{bostrom2020bytepair,
  author = {Bostrom, Kaj and Durrett, Greg},
  title = {Byte Pair Encoding is Suboptimal for Language Model Pretraining},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2020},
  year = {2020},
  doi = {10.18653/v1/2020.findings-emnlp.414}
}

@inproceedings{rust2021tokenization,
  author = {Rust, Phillip and Pfeiffer, Jonas and Vuli{\'c}, Ivan and Ruder, Sebastian and Gurevych, Iryna},
  title = {How Good is Your Tokenizer? On the Monolingual Performance of Multilingual Language Models},
  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
  year = {2021},
  doi = {10.18653/v1/2021.acl-long.243}
}

@inproceedings{wadden2020scifact,
  author = {Wadden, David and Lin, Shanchuan and Lo, Kyle and Wang, Lucy Lu and van Zuylen, Madeleine and Cohan, Arman and Hajishirzi, Hannaneh},
  title = {Fact or Fiction: Verifying Scientific Claims},
  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
  year = {2020},
  doi = {10.18653/v1/2020.emnlp-main.609}
}

@inproceedings{gao2023alce,
  author = {Gao, Tianyu and Yen, Howard and Yu, Jiatong and Chen, Danqi},
  title = {Enabling Large Language Models to Generate Text with Citations},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
  year = {2023},
  doi = {10.18653/v1/2023.emnlp-main.398}
}
"""


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def result(summary: dict[str, Any], exp: str) -> dict[str, Any]:
    return summary.get("experiments", {}).get(exp, {})


def safe_tex(text: str) -> str:
    return (
        text.replace("&", "\\&")
        .replace("%", "\\%")
        .replace("#", "\\#")
        .replace("_", "\\_")
    )


DECISION_LABELS = {
    "COUNT_LAYERS_RECONCILED_WITH_REVIEW_BLOCKERS": "The count layers are internally reconciled, but human source review remains required.",
    "F_V_HINGE_CONFIRMED_AS_DERIVED_OPERATION_NOT_SOURCE_ROW_COUNT": "The f/v split is supported only as a derived operation in the current package.",
    "LOGOGRAPH_LEAD_SET_EXTRACTED_NOT_COMPLETE_CORPUS": "The logograph material is a lead set, not a complete reviewed corpus.",
    "SELECTOR_LAYER_SAMPLE_CREATED_PIXEL_COORDINATES_BLOCKED": "A selector sample exists, but reviewed image coordinates are still missing.",
    "UNICODE_GAP_MATRIX_CREATED_NOT_PROPOSAL_READY": "The work supports a readiness audit, not a Unicode proposal.",
    "RIGHTS_SAFE_PROVENANCE_LEDGER_STARTED_PUBLIC_CORPUS_BLOCKED": "A rights-safe provenance ledger exists; public corpus release remains blocked.",
    "COMPARATIVE_MATRIX_CREATED_NWAGU_POSITIONED_AS_UNENCODED_REVIEW_BLOCKED": "The comparative matrix positions Nwagu Aneke as unencoded and review-blocked.",
    "TOKENIZER_BASELINES_RAN_NO_DOWNSTREAM_TASK_RESULT": "Tokenizer baselines ran, but no downstream NLP result is available.",
    "LAYER_SAFETY_INVARIANT_TESTED_PROMOTION_ERRORS_REJECTED": "The non-promotion rule rejected the unsafe layer promotions in the test set.",
}


def public_text(text: str) -> str:
    text = re.sub(r"\bEXP-NA-\d{3}\b", "The study", text)
    text = re.sub(r"\bNA-BENCH-\d{3}\b", "the relevant evaluation target", text)
    replacements = {
        "BMC entries": "base-modifier ledger entries",
        "BMC records": "base-modifier ledger records",
        "BMC": "base-modifier ledger",
        "repo-local": "locally archived",
        "not-in-repo": "not available in the present research package",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def decision_label(decision: object) -> str:
    value = str(decision)
    return DECISION_LABELS.get(value, value.replace("_", " ").title())


COMMON_CITES = (
    "azuonye1992,omniglotNwagu,unicodeAfricanScripts2023,"
    "w3cProvO,wilkinson2016fair,carroll2020care"
)


ARTICLES = [
    {
        "id": "ARTICLE-NA-001",
        "slug": "001-source-critical-reconstruction",
        "title": "A Source-Critical Reconstruction Ledger for the Nwagu Aneke Igbo Syllabary",
        "venue": "Digital Scholarship in the Humanities / Digital Humanities Quarterly",
        "experiment": "EXP-NA-001",
        "benchmark": "NA-BENCH-002",
        "field": "digital humanities and writing-system reconstruction",
        "claim": "The present contribution is a source-critical reconstruction ledger, not a completed glyph corpus.",
        "abstract_result": "The ledger aligns twelve local evidence rows, thirty-six inventory records, and a 208-record row-vowel index.",
        "specific_result": "EXP-NA-001 checked twelve local source files, produced twelve evidence rows, recorded twenty-six row labels and eight vowel columns, and classified all 208 BMC entries as human-review-needed rather than reviewed glyph transcriptions.",
        "method_detail": "The audit treats row labels, vowel columns, BMC cells, source locator status, and uncertainty notes as separate units. A statement is allowed into the paper only when its layer is explicit: source-observed, derived, secondary, or blocked.",
        "discussion": "This result is useful because it converts a culturally important but unstable research archive into a reviewable scholarly object. It does not settle the full history of the script. It gives future editors a controlled point of departure.",
        "extra_cites": "teiP5Glyphs,iiifPresentation3,w3cAnnotationModel,sirisNwaguProposal",
    },
    {
        "id": "ARTICLE-NA-002",
        "slug": "002-count-layer-drift",
        "title": "Count-Layer Drift in Nwagu Aneke: A Reproducible Audit of 26 by 8, 27, and 216",
        "venue": "Digital Scholarship in the Humanities / scholarly data-quality venues",
        "experiment": "EXP-NA-002",
        "benchmark": "NA-BENCH-001",
        "field": "data quality, symbolic inventory audit, and digital humanities",
        "claim": "Nwagu Aneke count claims become coherent only when source-observed and derived layers are separated.",
        "abstract_result": "The executed ledger reconciles 26 by 8 equals 208 as the source-observed index and 27/216 as a derived f/v split layer.",
        "specific_result": "EXP-NA-002 created a seven-record count ledger. Five records are ready or derived; two remain blocked or lead-level. The source layer is 26 rows, eight vowels, and 208 records. The derived layer is 27 rows and 216 records only if f/v is split.",
        "method_detail": "Every count is represented as a tuple: quantity, value, abstraction layer, evidence file, allowed claim, blocked claim, confidence, and status. This prevents an attractive derived number from becoming a false source observation.",
        "discussion": "The experiment exposes the paper-worthy result: the discovery is not that 27 is wrong or that 26 is final. The discovery is that several useful counts inhabit different evidentiary layers and must be governed by different publication rules.",
        "extra_cites": "scriptSourceNwagu,datacite45,wadden2020scifact,gao2023alce",
    },
    {
        "id": "ARTICLE-NA-003",
        "slug": "003-f-v-hinge",
        "title": "The f/v Hinge in Nwagu Aneke: Derived Orthographic Expansion Without Source-Layer Promotion",
        "venue": "Written Language and Literacy / African linguistics venues",
        "experiment": "EXP-NA-003",
        "benchmark": "NA-BENCH-001",
        "field": "orthography, script analysis, and Igbo linguistic review",
        "claim": "The f/v split is a derived operation over the current ledger, not a source-observed row-count result.",
        "abstract_result": "The f/v audit shows that splitting one observed row produces exactly eight additional derived cells.",
        "specific_result": "EXP-NA-003 generated eight f/v records at the source layer and sixteen records after the derived split; the split therefore adds eight records.",
        "method_detail": "The experiment compares the printed f/v row against two derived rows, f and v, across the same eight vowel columns. The output is accepted only as a design and interpretation layer until expert linguistic review supplies examples.",
        "discussion": "The hinge interpretation creates useful system-design space while protecting the linguistic claim from overreach. It also gives reviewers a falsification route: if primary evidence later shows separate f and v rows, the source layer changes; if not, the derived label remains mandatory.",
        "extra_cites": "teiP5Glyphs,w3cAnnotationModel,wadden2020scifact,scriptSourceNwagu",
    },
    {
        "id": "ARTICLE-NA-004",
        "slug": "004-logographs-in-a-syllabary",
        "title": "Logographs in a Syllabary: A Lead-Set Audit for Nwagu Aneke Whole-Word Signs",
        "venue": "Digital Scholarship in the Humanities / script-studies venues",
        "experiment": "EXP-NA-004",
        "benchmark": "NA-BENCH-003",
        "field": "script studies, sign inventory, and lexical-corpus construction",
        "claim": "Whole-word signs must be inventoried separately from CV cells before claims about the Nwagu Aneke logograph layer can be made.",
        "abstract_result": "The current chart transcription yields a bounded lead set of thirty visible whole-word signs, not a complete logograph corpus.",
        "specific_result": "EXP-NA-004 extracted thirty logograph leads from the chart transcription and counted their semantic-domain labels. The result preserves unknown glosses and marks every item as a visible lead rather than a reviewed glyph record.",
        "method_detail": "The ledger stores ordinal, word, gloss, semantic domain, source path, and review status. A whole-word sign cannot be counted as a CV cell, and a visible lead cannot be promoted into the reported 100-plus manuscript corpus.",
        "discussion": "This article is strongest as a corpus-construction result. It identifies the first bounded object that a reviewer can inspect: a seed lead set for later human transcription and semantic review.",
        "extra_cites": "teiP5Glyphs,w3cAnnotationModel,w3cAnnotationVocab,sirisNwaguProposal",
    },
    {
        "id": "ARTICLE-NA-005",
        "slug": "005-tei-iiif-critical-edition",
        "title": "A TEI, IIIF, and Web Annotation Bridge for an Unencoded African Syllabary",
        "venue": "Digital Scholarship in the Humanities / DHQ",
        "experiment": "EXP-NA-005",
        "benchmark": "NA-BENCH-004",
        "field": "digital editions, cultural heritage infrastructure, and unencoded scripts",
        "claim": "Nwagu Aneke can be represented as a staged standards bridge before Unicode encoding, but the current bridge lacks coordinate-level source annotation.",
        "abstract_result": "The experiment created ten Web Annotation-style records and ten TEI glyph-declaration leads from BMC entries.",
        "specific_result": "EXP-NA-005 exported ten BMC records into annotation JSON-LD and ten TEI glyph declaration leads. Zero records have reviewed pixel coordinates, so the result is a partial selector layer rather than a complete critical edition.",
        "method_detail": "Each sample maps a BMC record to an annotation body, target, TEI locator, certainty value, and review status. The mapping deliberately records partiality instead of presenting the dossier as compliant final publication data.",
        "discussion": "The article's contribution is infrastructural: it shows how an unencoded script can move through TEI, IIIF, and Web Annotation while preserving uncertainty. The missing coordinate layer is not a minor detail; it is the next experimental requirement.",
        "extra_cites": "teiP5Glyphs,iiifPresentation3,w3cAnnotationModel,w3cAnnotationVocab,cidocCrm",
    },
    {
        "id": "ARTICLE-NA-006",
        "slug": "006-unicode-readiness",
        "title": "Unicode Readiness for Nwagu Aneke: A Gap Matrix for Character Evidence and Community Review",
        "venue": "Unicode proposal track / digital humanities methods venues",
        "experiment": "EXP-NA-006",
        "benchmark": "NA-BENCH-005",
        "field": "script encoding, standardization readiness, and community review",
        "claim": "The current package supports a Unicode-readiness audit, not a Unicode proposal.",
        "abstract_result": "The gap matrix records twelve requirements: one present, several partial, several missing, and several blocked.",
        "specific_result": "EXP-NA-006 created a twelve-row Unicode-readiness matrix. It marks script identity as present; repertoire inventory and character-glyph distinction as partial; representative glyphs, usage examples, and community authority as blocked; and encoding model, punctuation, numbers, implementation evidence, and proposal dossier as missing.",
        "method_detail": "The matrix compares local source evidence with Unicode status information, ScriptSource status, and proposal-preparation expectations. Each requirement receives a status that constrains manuscript claims.",
        "discussion": "This article prevents premature standardization. It also makes the work actionable: future contributors know exactly which evidence categories must be gathered before an encoding proposal is credible.",
        "extra_cites": "scriptSourceNwagu,seiProposalTips,arxivSubmitTex,acmSubmissions",
    },
    {
        "id": "ARTICLE-NA-007",
        "slug": "007-manuscript-corpus-provenance",
        "title": "A CARE-First Provenance Ledger for the Reported Nwagu Aneke Manuscript Corpus",
        "venue": "Data Science Journal / cultural-heritage data venues",
        "experiment": "EXP-NA-007",
        "benchmark": "NA-BENCH-006",
        "field": "data stewardship, manuscript provenance, and Indigenous data governance",
        "claim": "Manuscript provenance and authority review must precede any public corpus claim for Nwagu Aneke.",
        "abstract_result": "The experiment produced a rights-safe four-record provenance ledger that distinguishes public metadata, internal chart use, catalogue leads, and the blocked reported manuscript corpus.",
        "specific_result": "EXP-NA-007 recorded four holdings/provenance candidates: Azuonye 1992, the local archived chart, the SIRIS proposal record, and the reported 100-plus exercise-book corpus. The corpus itself is marked not-in-repo with unknown rights status.",
        "method_detail": "The ledger records holding description, locator, access status, rights status, and research use. It intentionally avoids reproducing or exposing restricted material.",
        "discussion": "The paper's value is the constraint it imposes. It refuses to convert a famous corpus claim into a public dataset claim until custodianship, access, authority, and permitted uses have been documented.",
        "extra_cites": "sirisNwaguProposal,datacite45,rocrate12,cidocCrm",
    },
    {
        "id": "ARTICLE-NA-008",
        "slug": "008-comparative-standardization",
        "title": "Comparative Evidence Conditions for African Script Standardization: Positioning Nwagu Aneke",
        "venue": "comparative writing-system and digital-humanities venues",
        "experiment": "EXP-NA-008",
        "benchmark": "NA-BENCH-007",
        "field": "comparative writing systems and standardization studies",
        "claim": "Nwagu Aneke should be compared with other African scripts by evidence condition and standardization readiness, not only by typological resemblance.",
        "abstract_result": "The comparative matrix positions Nwagu Aneke as unencoded and review-blocked beside encoded and proposal-history comparators.",
        "specific_result": "EXP-NA-008 compared eight scripts: Vai, Bamum, Mende Kikakui, Ndebe, Nsibidi (New), Kpelle, Loma, and Nwagu Aneke. Three are encoded, several are proposal leads or unencoded, and Nwagu Aneke is marked not encoded and not on the roadmap.",
        "method_detail": "The matrix records script type, Unicode status, standardization signal, comparison relevance, and source. This turns comparison into a reproducible evidence table rather than a broad analogy.",
        "discussion": "The result reframes the comparative question. Nwagu Aneke's nearest research peers are not simply other syllabaries; they are scripts whose evidence, community, implementation, and proposal states can be compared without erasing local authority.",
        "extra_cites": "scriptSourceNwagu,seiProposalTips,cidocCrm,datacite45",
    },
    {
        "id": "ARTICLE-NA-009",
        "slug": "009-igbo-tokenization",
        "title": "Source-Layer and Derived-Layer Tokenizers for Igbo: A Bounded Nwagu Aneke Baseline",
        "venue": "African NLP workshops / low-resource NLP venues",
        "experiment": "EXP-NA-009",
        "benchmark": "NA-BENCH-008",
        "field": "low-resource NLP, tokenization, and Igbo language technology",
        "claim": "Nwagu Aneke can generate tokenizer hypotheses, but the current experiment shows segmentation behavior rather than downstream NLP improvement.",
        "abstract_result": "On 5,000 held-out local corpus words, BPE-200 averages 3.6164 tokens per word, while source-layer and derived f/v greedy CV tokenizers average 3.6708 tokens per word with 0.6746 CV-character coverage.",
        "specific_result": "EXP-NA-009 used 25,000 training words, 5,000 test words, seed 42, character and word baselines, a 200-merge BPE baseline, and source/derived CV greedy tokenizers. The source CV tokenizer is slightly worse than BPE-200 by 0.0544 mean tokens per word. Derived f/v splitting changes neither coverage nor token count in this corpus slice.",
        "method_detail": "The experiment trains BPE merges on the training split and evaluates token count, characters per token, confidence intervals, and CV-character coverage on the test split. It does not train a language model, POS tagger, NER system, or classifier.",
        "discussion": "The negative result is useful. It blocks the tempting claim that source-layer CV units already beat standard subword baselines. The next NLP paper requires a downstream task and stronger linguistic quality metrics.",
        "extra_cites": "sennrich2016bpe,kudo2018sentencepiece,bostrom2020bytepair,rust2021tokenization,karpathyAutoresearch",
    },
    {
        "id": "ARTICLE-NA-010",
        "slug": "010-layer-safe-generative-design",
        "title": "Layer-Safe Generative Design from Nwagu Aneke: A Non-Promotion Invariant",
        "venue": "design-science, information systems theory, or ACM CHI/DIS",
        "experiment": "EXP-NA-010",
        "benchmark": "NA-BENCH-009",
        "field": "generative design systems, provenance, and research governance",
        "claim": "Artifact-derived design systems require a non-promotion invariant: generated outputs must not upgrade derived, speculative, or blocked claims into source-observed claims.",
        "abstract_result": "The experiment detected all three intentional promotion errors in a seven-case test set and produced a finite-composition non-promotion lemma.",
        "specific_result": "EXP-NA-010 tested seven layer-safety cases, detected three unsafe promotions, and recorded a 1.0 promotion-error detection rate. The proof artifact states that finite compositions of layer-safe transforms cannot make a non-source claim become source-observed.",
        "method_detail": "The method orders labels by evidentiary strength: source-observed, derived, speculative, and blocked. A transform is safe only if it never emits a stronger evidence label than its input licenses.",
        "discussion": "This is currently the strongest systems article in the package. It converts the 26-by-8 versus 27/216 contradiction into a reusable design invariant. The next step is comparison to provenance logic, type systems, and claim-verification benchmarks.",
        "extra_cites": "rocrate12,w3cProvO,wadden2020scifact,gao2023alce,karpathyAutoresearch",
    },
]


def cite_keys(article: dict[str, str]) -> str:
    keys = []
    for group in [COMMON_CITES, article["extra_cites"], "acmSubmissions,arxivSubmitTex,arxivTexLive"]:
        keys.extend(key.strip() for key in group.split(",") if key.strip())
    seen: list[str] = []
    for key in keys:
        if key not in seen:
            seen.append(key)
    return ",".join(seen)


def article_tex(article: dict[str, str], exp_result: dict[str, Any], scoreboard: dict[str, Any]) -> str:
    citations = cite_keys(article)
    decision = decision_label(exp_result.get("decision", "see experiment output"))
    source_layer = "26 rows by 8 vowel/modifier columns, giving 208 source-observed ledger records"
    derived_layer = "27 rows and 216 records only when the combined f/v row is split as a derived layer"
    public_claim = public_text(article["claim"])
    public_abstract_result = public_text(article["abstract_result"])
    public_specific_result = public_text(article["specific_result"])
    public_method_detail = public_text(article["method_detail"])
    return rf"""
    \documentclass[sigconf,nonacm]{{acmart}}
    \settopmatter{{printacmref=false}}
    \setcopyright{{none}}
    \renewcommand\footnotetextcopyrightpermission[1]{{}}
    \pagestyle{{plain}}
    \raggedbottom

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
    This article studies Nwagu Aneke as a source-grounded research artifact for
    {article["field"]}. The accepted foundation is fixed throughout: the
    source-observed layer is {source_layer}; {derived_layer}. {public_claim}
    {public_abstract_result} The contribution is therefore bounded:
    it reports a bounded audit, states what can be believed from the current
    evidence package, and identifies the remaining human review
    needed before journal submission.
    \end{{abstract}}

    \keywords{{Nwagu Aneke, Igbo writing systems, source-grounded research, evidence ledger, evidence review}}

    \begin{{document}}
    \maketitle

    \section{{Introduction}}
    Nwagu Aneke is a rare case where a twentieth-century African writing
    artifact can support several research programs at once: historical
    reconstruction, digital editions, script standardization, low-resource NLP,
    and artifact-derived system design. The risk is that those programs can
    silently exchange evidentiary layers. A derived design count can become a
    historical count; a chart lead can become a corpus claim; a tokenizer
    hypothesis can become a performance claim. This paper avoids that failure
    by treating layer labels as part of the result rather than as editorial
    footnotes.

    The paper's research question is: what can be concluded about {article["field"]}
    from the present Nwagu Aneke evidence package, and what remains blocked?
    The answer is intentionally narrow. The current article does not claim a
    completed public glyph corpus, a cleared manuscript dataset, universal
    compression, exceptional mathematics, or a completed Unicode proposal. It
    reports the audit described here and uses that result to define a defensible
    contribution for {article["venue"]}.

    \section{{Related Work}}
    Azuonye's 1992 account remains the academic anchor for this work
    \cite{{azuonye1992}}. Public status sources describe Nwagu Aneke as an
    unencoded script and record its relation to African script standardization
    work \cite{{omniglotNwagu,unicodeAfricanScripts2023,scriptSourceNwagu}}.
    The digital-methods side draws on provenance, research-object packaging,
    source annotation, and data-governance standards
    \cite{{w3cProvO,rocrate12,teiP5Glyphs,iiifPresentation3,w3cAnnotationModel,wilkinson2016fair,carroll2020care}}.
    For scientific control, the draft follows the claim-verification principle
    that generated or reconstructed claims must remain attached to evidence
    rather than to persuasive prose alone \cite{{wadden2020scifact,gao2023alce}}.
    The article-specific citations are: \cite{{{article["extra_cites"]}}}.

    \section{{Prior-Art Gap and Contribution}}
    The article does not claim novelty by naming Nwagu Aneke alone. Its
    contribution is the combination of a source-critical artifact layer, a
    bounded audit, and a source-evidence boundary that keeps historical,
    technical, and design claims separate. Existing standards help with parts
    of this problem: TEI can model writing systems and glyph declarations,
    IIIF can identify canvases, Web Annotation can connect bodies and targets,
    PROV-O can model provenance, RO-Crate can package research objects, and
    CARE/FAIR can govern ethical and reusable data practice. Those standards
    do not by themselves decide whether a count is source-observed, derived,
    speculative, or blocked for this artifact. That decision is the article's
    local research contribution.

    For {article["field"]}, the gap is therefore practical and scholarly:
    reviewers need to see a result that can be checked without accepting the
    entire PAGC theory. The paper supplies that result by narrowing the claim
    to the present audit. The article can be rejected, revised, or
    extended on that basis. It does not depend on a broad claim that African
    symbolic systems are universally compressive, mathematically exceptional,
    or automatically ready for software standardization.

    The public claim is deliberately narrow. The article should be read as a
    testable contribution in {article["field"]}, not as a progress report about
    lab infrastructure. Its central value is that the result can be accepted,
    corrected, or rejected without accepting any broader PAGC programme.

    \section{{Materials and Evidence}}
    The materials are locally archived and reproducible. The source-critical base is
    the Nwagu Aneke dossier, the chart transcription, the symbol inventory, the
    base-modifier ledger records, the count reconciliation file, and the
    article-specific audit output. The governing count distinction is fixed:
    source-observed 26 by 8 equals 208; 27/216 is a derived f/v split layer.
    This distinction is not negotiable inside the experiment because it is the
    control variable that prevents layer drift.
    \section{{Method}}
    {public_method_detail} The same rule is applied to the manuscript.
    A claim can be source-observed, derived, externally contextualized,
    experimentally produced, or blocked. Blocked claims are not deleted; they
    are made visible as limitations or future work. This matters because the
    article is not trying to produce persuasive prose from weak evidence. It is
    trying to make each conclusion inspectable.

    The evaluation has two roles. First, it asks whether the promised artifact
    was actually produced. Second, it asks whether the manuscript still exposes
    unsupported claims, missing evidence, or public-release blockers. A revision
    is kept only when it strengthens evidence, removes an overclaim, or makes a
    blocker clearer without weakening the source boundary.

    The experimental design has three controls. First, all source claims inherit
    the 26-by-8 source ledger unless a later human source review changes it.
    Second, all 27/216 claims are typed as derived f/v split claims. Third,
    every article must expose the missing evidence that would change the
    conclusion. This makes the method adversarial: it is designed to reject
    attractive claims when they are unsupported.

    The method also records negative information. Missing coordinates, task
    labels, manuscript access, or authority clearance are represented as
    blockers, not as prose gaps.

    \section{{Results}}
    \textbf{{Main result.}} {public_specific_result}

    \begin{{table}}[t]
    \caption{{Public-facing evidence summary}}
    \label{{tab:result-{article["id"].lower().replace("_", "-")}}}
    \begin{{tabular}}{{p{{0.30\columnwidth}}p{{0.58\columnwidth}}}}
    \toprule
    Audit item & Finding \\
    \midrule
    Current result & {safe_tex(str(decision))} \\
    Source layer & 26 by 8 equals 208 records \\
    Derived layer & 27/216 only by f/v split \\
    Human review & Source transcription, rights, and authority review required \\
    \bottomrule
    \end{{tabular}}
    \end{{table}}

    This result is not a universal theory. It is a bounded research finding
    over the current evidence package. Its value is that it can be reproduced
    locally and falsified directly: change the source ledger, source review,
    rights status, or experiment output, and the paper must change.

    \section{{Falsification}}
    The claim would fail under clear conditions. It fails if a reviewed primary
    source shows that the current source layer is not 26 by 8. It fails if the
    f/v split is shown to be source-observed rather than derived. It fails if a
    required rights or authority record blocks the public claim being made. It
    also fails if a stronger baseline or more complete corpus reverses the
    article-specific experiment result. These failure modes are not rhetorical
    caveats; they are the conditions under which the article must be revised.

    In that sense, the article is intentionally easier to falsify than the
    earlier speculative PAGC branches. A journal reviewer does not need to
    accept broad claims about ancestral compression to evaluate the result.
    They need only inspect the source ledger, the audit output, and the
    blocked evidence ledger.

    \section{{Discussion}}
    {article["discussion"]} The broader implication is methodological. The
    artifact can generate novel applications, but the applications only become
    research when their claims are typed and tested. The 26-by-8 source layer
    is therefore not a limitation on imagination; it is the stable floor that
    allows derived systems to be explored without falsifying the source record.

    The result also changes the lab workflow. Revisions must improve against
    fixed evidence criteria rather than local persuasion.

    \section{{Limitations}}
    The strongest limitation is human review. The current package still needs
    source transcription review, rights review, cultural/source authority
    review, and article-specific expert review. Public image reproduction and
    public manuscript corpus release are not authorized by this article. The
    current result is suitable for targeted human review and further research,
    not automatic public submission.

    The second limitation is article-specific. The article-specific claim
    remains tied to the present audit. If later source review contradicts
    the row inventory, the f/v split, the visible logograph leads, or the
    annotation status, the article must be revised rather than patched
    rhetorically.

    \section{{Venue Fit}}
    The plausible venue class is {article["venue"]}. The draft has a
    reproducible result, but it is not a final submission until field-specific
    prior art, source transcription review, authority clearance, and expert
    field review are complete.

    \section{{Reproducibility}}
    The analysis package records the source ledger, derived-layer audit,
    generated tables, manuscript source, and reproduction scripts. A public
    release should include those materials only after source transcription,
    rights, and authority review. Until then, the paper can be independently
    assessed by checking whether each visible claim is typed as source-observed,
    derived, externally contextualized, or blocked.

    \section{{Conclusion}}
    This article contributes a bounded, reproducible result derived from the
    Nwagu Aneke artifact. It preserves the accepted foundation: source-observed
    26 by 8 equals 208, with 27/216 only as a derived f/v split layer. On that
    foundation, the article identifies one application or research pathway that
    can be tested, criticized, and improved without promoting design
    speculation into source evidence.

    \bibliographystyle{{ACM-Reference-Format}}
    \bibliography{{../references}}
    \end{{document}}
    """


def status_md(article: dict[str, str], exp_result: dict[str, Any]) -> str:
    return f"""
    # {article["id"]}: {article["title"]}

    ## Current Article Type

    Research article draft based on executed experiment `{article["experiment"]}`.

    ## Central Claim

    {article["claim"]}

    ## Experiment Decision

    `{exp_result.get("decision", "unknown")}`

    ## Status

    `TARGETED_HUMAN_REVIEW_DRAFT_NOT_SUBMISSION_READY`

    ## Remaining Blockers

    - Source transcription review.
    - Rights and public-release review.
    - Cultural/source authority review.
    - Article-specific expert review.
    """


def update_references() -> None:
    ref_path = PACKAGE / "references.bib"
    current = ref_path.read_text(encoding="utf-8") if ref_path.exists() else ""
    additions = []
    for block in EXTRA_REFERENCES.strip().split("\n\n"):
        key = block.split("{", 1)[1].split(",", 1)[0].strip()
        if f"{{{key}," not in current:
            additions.append(block)
    if additions:
        ref_path.write_text(current.rstrip() + "\n\n" + "\n\n".join(additions) + "\n", encoding="utf-8")


def main() -> int:
    summary = read_json(SUMMARY, {})
    scoreboard = read_json(BENCH, {})
    generated_at = now()
    update_references()
    manifest = read_json(PACKAGE / "manifest.json", {})
    manifest["rewritten_from_benchmark_at"] = generated_at
    manifest["status"] = "TARGETED_HUMAN_REVIEW_DRAFTS_NOT_SUBMISSION_READY"
    manifest["benchmark"] = {
        "path": "benchmarks/nwagu_article_research/scoreboard.json",
        "evidence_completion_score": scoreboard.get("evidence_completion_score"),
        "impact_journal_readiness_score": scoreboard.get("impact_journal_readiness_score"),
    }
    article_manifest = []
    for article in ARTICLES:
        exp_result = result(summary, article["experiment"])
        article_dir = PACKAGE / article["slug"]
        write_text(article_dir / "main.tex", article_tex(article, exp_result, scoreboard))
        write_text(article_dir / "STATUS.md", status_md(article, exp_result))
        article_manifest.append(
            {
                "id": article["id"],
                "title": article["title"],
                "slug": article["slug"],
                "tex_path": f"{article['slug']}/main.tex",
                "experiment_id": article["experiment"],
                "benchmark_task_id": article["benchmark"],
                "readiness_status": "TARGETED_HUMAN_REVIEW_DRAFT_NOT_SUBMISSION_READY",
            }
        )
    manifest["articles"] = article_manifest
    write_json(PACKAGE / "manifest.json", manifest)
    write_text(
        PACKAGE / "impact_readiness_audit.md",
        f"""
        # Nwagu Aneke Ten-Article Working-Paper Audit

        Generated: {generated_at}

        ## Bottom Line

        The ten manuscripts are working-paper drafts, not impact-journal
        articles. They contain bounded audits and experiments, but they remain
        too shallow for global submission standards because article-specific
        prior art, rights, cultural/source authority, domain review, and
        manuscript depth remain open. The strongest near-term candidates for
        serious development are Article 2, count-layer drift, and Article 10,
        layer-safe generative design.

        ## Benchmark Control

        - Evidence completion score: `{scoreboard.get("evidence_completion_score")}`
        - Impact-journal readiness score: `{scoreboard.get("impact_journal_readiness_score")}`
        - Benchmark status: `{scoreboard.get("status")}`
        - Benchmark path: `benchmarks/nwagu_article_research/scoreboard.json`

        ## Accepted Foundation

        The source-observed layer is 26 rows by 8 vowel/modifier columns, giving
        208 records. The 27/216 layer is only a derived f/v split layer.

        ## Current Status

        `TARGETED_HUMAN_REVIEW_DRAFTS_NOT_SUBMISSION_READY`
        """,
    )
    print("NWAGU_ARTICLES_REWRITTEN_FROM_BENCHMARK")
    print(f"articles={len(ARTICLES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
