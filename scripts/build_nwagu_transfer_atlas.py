from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "frontier" / "nwagu_transfer_atlas"
EXP = ROOT / "experiments" / "EXP-FRONTIER-006-nwagu-transfer-atlas"


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def rec(
    project: str,
    source_family: str,
    native_problem: str,
    mechanism: str,
    nwagu_object: str,
    evidence: list[str],
    experiment: str,
    negative_control: str,
    claim_ceiling: str,
    article: str,
    phase: str,
    rights: str,
    urls: list[str],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    row = {
        "project": project,
        "source_family": source_family,
        "native_problem": native_problem,
        "transferable_mechanism": mechanism,
        "nwagu_research_object": nwagu_object,
        "required_evidence": evidence,
        "experiment": experiment,
        "negative_control": negative_control,
        "claim_ceiling": claim_ceiling,
        "prior_art_status": "seeded_from_attachment_requires_verification",
        "rights_risk": rights,
        "article_candidate": article,
        "phase_gate": phase,
        "status": "opened",
        "source_urls": urls,
    }
    if extra:
        row.update(extra)
    return row


RECORDS = [
    rec("Kraken", "historical handwriting recognition", "trainable OCR for historical/non-Latin scripts", "layout analysis plus human-corrected recognition", "reviewed chart/manuscript glyph recognition", ["reviewed cell inventory", "segmented glyph images", "transcription rules"], "train a tiny recognizer on reviewed cells and measure error by row/column", "shuffled row/column labels with same crops", "OCR usefulness, not complete decipherment", "Human-Corrected OCR for an Underdocumented Igbo Script", "begin_now", "medium", ["https://github.com/mittagessen/kraken"]),
    rec("eScriptorium", "historical handwriting recognition", "web transcription and OCR training workflow", "human-in-the-loop transcription flywheel", "cell/page annotation workflow", ["annotation protocol", "reviewer roles", "page images"], "simulate transcription rounds and measure disagreement reduction", "static spreadsheet with no feedback loop", "workflow efficiency, not source truth", "A Transcription Flywheel for Nwagụ Aneke", "begin_now", "medium", ["https://gitlab.inria.fr/scripta/escriptorium"]),
    rec("HTR-United", "ground-truth data standards", "shareable HTR datasets for patrimonial documents", "image-linked ground truth with provenance", "publishable ground-truth packaging pattern", ["image locators", "transcription rules", "reuse conditions"], "package reviewed chart cells as HTR-style ground-truth metadata without public image release", "unlinked image folder", "dataset structure only until rights clear", "Ground Truth Without Overrelease", "begin_now", "high", ["https://github.com/HTR-United/htr-united"]),
    rec("OCR-D", "OCR workflow infrastructure", "interoperable OCR pipelines", "workflow modularity and PAGE/ALTO-style interchange", "repeatable OCR/transcription pipeline", ["workflow manifest", "input/output schemas", "quality checks"], "run empty pipeline validation over chart metadata", "manual one-off transcription", "pipeline reproducibility, not recognition accuracy", "Workflow Standards for Nwagụ OCR", "begin_now", "low", ["https://github.com/OCR-D"]),
    rec("Calamari OCR", "OCR model comparison", "OCR model training and voting", "ensemble disagreement as uncertainty", "review-priority ranking for uncertain cells", ["segmented glyphs", "multiple recognizers", "review labels"], "rank cells by model disagreement for expert review", "random review order", "active-learning priority, not identity proof", "Disagreement-Guided Glyph Review", "after_reviewed_glyph_inventory", "medium", ["https://github.com/Calamari-OCR/calamari"]),
    rec("DeepMind Ithaca", "ancient-text restoration", "restoration, attribution, and dating for damaged inscriptions", "uncertainty-aware historian assistance", "ambiguous Nwagụ sequence ranking", ["manuscript passages", "metadata", "candidate readings"], "rank alternatives for ambiguous signs with confidence and source context", "top-1 answer without alternatives", "decision support, not autonomous reading", "Uncertainty-Aware Restoration for Nwagụ Aneke", "after_manuscript_access", "high", ["https://github.com/google-deepmind/ithaca"]),
    rec("EpiDoc", "epigraphic encoding", "encoding gaps, supplied text, corrections, variants", "editorial apparatus for uncertain readings", "source-critical transcription records", ["source locators", "uncertainty tags", "variant readings"], "encode five disputed cells with apparatus rather than single labels", "single flattened reading", "apparatus quality, not final transcription", "An Editorial Apparatus for Nwagụ Aneke", "begin_now", "medium", ["https://epidoc.stoa.org/"]),
    rec("CDLI", "ancient document infrastructure", "cataloging and transliteration for cuneiform collections", "object-level metadata and transliteration separation", "notebook/page catalog model", ["custody map", "page IDs", "transliteration layer"], "design notebook catalog schema separating object, image, sign, reading", "flat note filenames", "catalog design, not manuscript access", "Cataloging the Nwagụ Notebook Tradition", "after_manuscript_access", "high", ["https://cdli.mpiwg-berlin.mpg.de/"]),
    rec("ORACC", "ancient corpora", "linked editions and lexical resources", "corpus edition as queryable research object", "future Nwagụ corpus edition", ["transcribed text", "translation", "lexical entries"], "draft edition schema for one sample page when access exists", "plain text transcript", "edition architecture, not corpus claims", "A Queryable Edition Model for Nwagụ Aneke", "after_manuscript_access", "high", ["http://oracc.museum.upenn.edu/"]),
    rec("DeepScribe", "sign localization", "cuneiform sign localization and classification", "top-k sign suggestions and clusters", "glyph-family discovery independent of readings", ["source images", "bounding boxes", "review labels"], "cluster signs by visual features and compare to readings", "reading-based clusters", "visual families, not linguistic values", "Visual Sign Families in Nwagụ Aneke", "after_reviewed_glyph_inventory", "high", ["https://voices.uchicago.edu/ochre/project/deepscribe/"]),
    rec("DigiPal", "digital paleography", "letter-form annotation linked to manuscript images", "graph-level palaeographic feature annotation", "variant and allograph registry", ["glyph images", "feature schema", "reviewer labels"], "annotate endpoints, loops, crossings, and compare across rows", "pixel-only similarity", "palaeographic feature model, not character inventory", "Constraint-Graph Palaeography for Nwagụ Aneke", "after_reviewed_glyph_inventory", "medium", ["https://github.com/kcl-ddh/digipal"]),
    rec("Mirador", "IIIF image comparison", "side-by-side image viewing and annotation", "expert comparison interface", "chart/manuscript comparison", ["IIIF manifests", "image regions", "annotation storage"], "build a private IIIF comparison protocol for disputed cells", "single static contact sheet", "review interface, not publication clearance", "Image Comparison for Nwagụ Sign Review", "begin_now", "high", ["https://github.com/ProjectMirador/mirador"]),
    rec("Omniglot", "one-shot character learning", "handwritten character dataset and stroke traces", "few-shot glyph learning benchmark pattern", "minimal teaching-key experiment", ["reviewed glyph crops", "train/test splits", "human/model tasks"], "measure held-out cell prediction from K examples", "random labels with same crops", "learnability, not historical intention", "Keyed, Few-Shot, and Unkeyed Reading of Nwagụ Aneke", "after_reviewed_glyph_inventory", "medium", ["https://github.com/brendenlake/omniglot"]),
    rec("Bayesian Program Learning", "program induction for characters", "characters as stochastic drawing programs", "drawing-program hypothesis comparison", "candidate reusable stroke grammar", ["vectorized glyphs", "stroke features", "holdout cells"], "compare lookup table vs program library by description length", "complexity-matched random glyph charts", "formal regularity, not author intention", "Reverse Procedural Archaeology of Nwagụ Glyphs", "after_reviewed_glyph_inventory", "medium", ["https://www.science.org/doi/10.1126/science.aab3050"]),
    rec("DreamCoder", "program synthesis", "discover reusable abstractions across tasks", "wake-sleep abstraction discovery", "glyph primitive library", ["vector forms", "task definitions", "scoring rules"], "induce reusable drawing primitives and test held-out reconstruction", "independent primitive per glyph", "compressive formal model, not historical proof", "Program Induction for an Underdocumented Igbo Script", "after_reviewed_glyph_inventory", "medium", ["https://github.com/ellisk42/ec"]),
    rec("SketchGraphs", "constraint-graph geometry", "CAD sketches as geometric constraint graphs", "topological/constraint representation", "stroke relation graph for glyphs", ["vectorized signs", "junction/loop extraction", "feature labels"], "test whether graph features predict row/column better than pixels", "pixel embeddings only", "structural signal, not meaning", "Nwagụ Constraint-Graph Palaeography", "after_reviewed_glyph_inventory", "medium", ["https://github.com/PrincetonLIPS/SketchGraphs"]),
    rec("DeepSVG", "vector graphics modeling", "learning vector-command structure", "sequence model over SVG commands", "digital glyph representation stability", ["SVG traces", "normalization policy", "review labels"], "compare SVG-command similarity to human confusion", "raster similarity", "vector legibility, not character identity", "Vector Structure in Nwagụ Glyphs", "after_reviewed_glyph_inventory", "medium", ["https://github.com/alexandre01/deepsvg"]),
    rec("diffvg", "differentiable vector graphics", "optimization over vector paths", "stroke-path reconstruction and perturbation", "glyph transport and ambiguity tests", ["image crops", "vectorization", "error metrics"], "fit vector paths to crops and measure robustness under rendering changes", "manual SVG only", "rendering robustness, not glyph truth", "Transport Fragility in Nwagụ Digitization", "after_reviewed_glyph_inventory", "medium", ["https://github.com/BachiLi/diffvg"]),
    rec("giotto-tda", "topological data analysis", "topological features for shapes", "loop/junction/topology measurement", "shape-family graph", ["binary glyph images", "topological feature extraction", "labels"], "test whether topology clusters by row/vowel/full-word status", "raw pixel clustering", "topological regularity only", "Topological Sign Families in Nwagụ Aneke", "after_reviewed_glyph_inventory", "low", ["https://github.com/giotto-ai/giotto-tda"]),
    rec("Edinburgh Centre for Language Evolution", "cultural transmission", "iterated learning and language evolution", "copying/learning chains", "script cultural-evolution lab", ["teaching materials", "participant protocol", "ethics review"], "transmit sign subsets through learner chains and measure regularization", "one-generation memorization", "transmission pressure, not historical origin", "Cultural Transmission of Nwagụ-Like Signs", "after_reviewed_glyph_inventory", "medium", ["https://cle.ppls.ed.ac.uk/"]),
    rec("EGG", "emergent communication", "controlled communication games", "synthetic null communication systems", "row-vowel signaling pressures", ["task environment", "synthetic inventories", "analysis metrics"], "test whether agents invent factorized signals under Nwagụ-like constraints", "unconstrained signaling game", "functional pressure, not Aneke intention", "Emergent Communication Under Nwagụ-Like Constraints", "after_reviewed_glyph_inventory", "low", ["https://github.com/facebookresearch/EGG"]),
    rec("Iterated language games", "artificial grammar learning", "human transmission experiments", "simplification/regularization measurement", "glyph learnability and drift", ["participant protocol", "sign subsets", "error taxonomy"], "compare drift of real vs synthetic control signs", "random symbol set only", "learning pressure, not manuscript history", "Human Transmission of Nwagụ Sign Subsets", "after_reviewed_glyph_inventory", "medium", ["https://cle.ppls.ed.ac.uk/"]),
    rec("Masakhane", "African NLP", "distributed African-language NLP community", "participatory evaluation and data ownership", "Igbo/Nwagụ community-led evaluation", ["community review", "language resources", "evaluation protocol"], "define community-facing success criteria for Nwagụ tools", "external-only NLP metrics", "evaluation governance, not technical accuracy alone", "Community-Led Evaluation for Nwagụ NLP", "begin_now", "high", ["https://github.com/masakhane-io"]),
    rec("Nkọwa okwu", "Igbo lexical resources", "Igbo dictionary, dialect, OCR/audio resources", "dialect-sensitive lexical comparison", "full-word symbol allocation", ["verified word-sign readings", "Igbo lexical data", "dialect metadata"], "compare full-word signs to frequency, dialect, and semantic categories", "random Igbo word set", "lexical allocation signal, not cultural proof", "What Receives a Whole-Word Sign?", "after_logograph_review", "medium", ["https://github.com/nkowaokwu"]),
    rec("Common Voice", "community speech collection", "open speech corpus infrastructure", "speech-script alignment pattern", "Umuleri speech/Roman/Nwagụ alignment", ["speaker consent", "audio", "transcriptions"], "design consented alignment corpus protocol", "text-only corpus", "corpus protocol, not immediate data release", "Script, Speech, and Dialect Alignment for Nwagụ", "after_authority_review", "high", ["https://github.com/common-voice"]),
    rec("Mukurtu", "Indigenous digital heritage governance", "cultural protocols and community records", "item-level access and authority rules", "machine-readable cultural authority", ["authority register", "access policy", "record-level restrictions"], "attach access/training/display permissions to each source record", "single global license", "governance model, not publication permission", "Machine-Readable Cultural Authority for Nwagụ", "begin_now", "high", ["https://github.com/MukurtuCMS/mukurtucms"]),
    rec("Local Contexts", "traditional knowledge labels", "community authority labels", "permission labels beyond copyright", "rights and training policy per item", ["community decision process", "label mapping", "release manifest"], "prototype non-public label fields for Nwagụ records", "copyright-only metadata", "protocol expressivity, not consent itself", "CARE/FAIR Tension in Nwagụ Data", "begin_now", "high", ["https://localcontexts.org/"]),
    rec("CARE Principles", "Indigenous data governance", "collective benefit, authority, responsibility, ethics", "authority-aware benchmark release criteria", "release gate for datasets/tools", ["community authority record", "benefit statement", "risk review"], "add CARE gate to every atlas record", "FAIR-only release checklist", "governance quality, not rights clearance", "CARE-Gated Script Documentation", "begin_now", "high", ["https://www.gida-global.org/care"]),
    rec("Arches", "cultural heritage inventories", "graph-based heritage inventory platform", "heritage object graph", "Nwagụ object/sign/source graph", ["entity schema", "relations", "rights fields"], "model glyph instance, page, source, reading, rights as linked entities", "flat spreadsheet", "graph structure, not source evidence", "A Cultural-Heritage Graph for Nwagụ Aneke", "begin_now", "medium", ["https://github.com/archesproject/arches"]),
    rec("ResearchSpace", "semantic cultural heritage", "semantic research environment", "interpretation graph and competing readings", "contradiction discovery platform", ["CIDOC-aligned entities", "claims", "counterreadings"], "query which claims depend on the same weak source", "manual contradiction list", "queryability, not claim truth", "Contradiction Discovery in Nwagụ Evidence Graphs", "begin_now", "medium", ["https://github.com/researchspace/researchspace"]),
    rec("Linked Art", "linked cultural data", "JSON-LD model for art/heritage objects", "interoperable object metadata", "source/chart/notebook record exchange", ["object metadata", "provenance", "rights"], "map Nwagụ source objects to Linked Art-like JSON-LD", "custom-only JSON", "interoperability, not source access", "Linked Cultural Data for Nwagụ Sources", "begin_now", "medium", ["https://linked.art/"]),
    rec("CIDOC CRM", "cultural heritage ontology", "events, objects, actors, interpretations", "source event and interpretation model", "claim provenance graph", ["source inventory", "actor records", "event types"], "map chart transcription as interpretation event", "untyped provenance strings", "ontology mapping, not historical proof", "CIDOC CRM for Nwagụ Evidence Chains", "begin_now", "low", ["https://www.cidoc-crm.org/"]),
    rec("HarfBuzz", "text shaping", "OpenType shaping and rendering behavior", "rendering survivability tests", "pre-Unicode digital twin", ["stable glyph IDs", "font prototype", "test strings"], "test glyph rendering/copying without assigning Unicode code points", "static PNG only", "transport behavior, not encoding readiness", "When the Font Is the Key", "after_repertoire_stability", "high", ["https://github.com/harfbuzz/harfbuzz"]),
    rec("fontTools", "font engineering", "font manipulation and QA", "font build/test pipeline", "controlled private font experiments", ["glyph IDs", "font metadata", "QA tests"], "build non-public test font with explicit non-Unicode status", "handmade font file", "font QA, not public standardization", "Pre-Unicode Font QA for Nwagụ Aneke", "after_repertoire_stability", "high", ["https://github.com/fonttools/fonttools"]),
    rec("Keyman", "input systems", "cross-platform keyboard infrastructure", "input method prototype and usability test", "Nwagụ data-entry workflow", ["character model", "keyboard mapping", "community review"], "test ASCII-ID entry vs visual keyboard for reviewed signs", "manual copy/paste", "input ergonomics, not release approval", "Keyboard Before Unicode? Input Prototyping for Nwagụ", "after_repertoire_stability", "high", ["https://github.com/keymanapp/keyman"]),
    rec("ICU", "internationalization", "Unicode normalization/collation infrastructure", "normalization and sorting risk testing", "transport-survival matrix", ["experimental IDs", "test corpus", "platform matrix"], "measure copy/sort/search failures across representations", "single platform test", "digital survivability, not encoding proposal", "Digital Survivability of an Unencoded African Script", "after_repertoire_stability", "medium", ["https://github.com/unicode-org/icu"]),
    rec("Script Encoding Initiative", "script encoding support", "evidence and proposal support for missing scripts", "encoding readiness criteria", "Unicode readiness gate", ["stable inventory", "usage evidence", "community review"], "score Nwagụ against encoding readiness criteria", "premature codepoint table", "readiness audit, not proposal", "Unicode Before or After Community?", "after_authority_review", "high", ["https://sei.berkeley.edu/"]),
    rec("Vesuvius Challenge", "open research challenge", "modular blind tasks and public leaderboards", "governed open-problem challenge", "Nwagụ challenge task design", ["rights-cleared data", "blind split", "evaluation metric"], "define tasks for segmentation, variant matching, and evidence-preserving interpretation", "open-ended decode challenge", "challenge design, not data release", "A Governed Nwagụ Open-Problem Challenge", "after_authority_review", "high", ["https://github.com/ScrollPrize/villa"]),
    rec("RO-Crate", "research object packaging", "structured metadata package for research objects", "release packaging and provenance", "atlas package reproducibility", ["metadata", "license fields", "provenance files"], "package non-sensitive benchmark metadata as RO-Crate", "zip of files", "packaging, not clearance", "RO-Crate for Source-Critical Script Research", "begin_now", "low", ["https://github.com/ResearchObject/ro-crate"]),
    rec("DataLad", "data versioning", "distributed dataset tracking", "versioned hypotheses and artifacts", "inventory version control", ["dataset tree", "metadata", "change logs"], "track count-model changes and affected papers", "manual changelog only", "reproducibility, not evidence truth", "Versioned Hypotheses for Nwagụ Aneke", "begin_now", "low", ["https://www.datalad.org/", "https://handbook.datalad.org/en/latest/book_main.html"], {"status": "deferred_by_preservation_decision", "preservation_decision": "PRESERVE-EXP-FRONTIER-008-001", "decision_status": "defer_until_dataset_boundary_review", "decision_artifact": "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/PRESERVATION_DECISION.md"}),
    rec("DVC", "experiment data versioning", "pipeline and data artifact tracking", "experiment reproducibility", "glyph experiment pipelines", ["pipeline stages", "data hashes", "metrics"], "define pipeline for crop -> feature -> cluster -> report", "notebook-only analysis", "pipeline reproducibility, not model validity", "Reproducible Glyph Experiments for Nwagụ", "after_reviewed_glyph_inventory", "low", ["https://github.com/iterative/dvc"]),
    rec("Zenodo", "research output publication", "citable research records", "release DOI and metadata process", "controlled publication package", ["release manifest", "metadata", "rights statement"], "create dry-run metadata for non-sensitive atlas release", "uncited GitHub folder", "metadata readiness, not publication approval", "Citable Research Objects for Nwagụ Work", "after_authority_review", "medium", ["https://zenodo.org/"]),
    rec("Software Heritage", "software preservation", "source archive identifiers", "code provenance for experiments", "experiment code preservation", ["repository snapshot", "SWHID", "scripts"], "map benchmark scripts to preservation identifiers", "local script only", "software provenance, not scientific validity", "Preserving Nwagụ Research Software", "begin_now", "low", ["https://www.softwareheritage.org/", "https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html"], {"status": "deferred_by_preservation_decision", "preservation_decision": "PRESERVE-EXP-FRONTIER-008-001", "decision_status": "defer_until_public_release_or_archive_approval", "decision_artifact": "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/PRESERVATION_DECISION.md"}),
    rec("Label Studio", "annotation tooling", "multi-type annotation workflows", "disagreement-preserving labels", "cell/sign/review annotation", ["annotation schema", "review roles", "export format"], "prototype label config for cells and promotion-error claims", "single reviewer spreadsheet", "annotation workflow, not gold truth", "Disagreement as Data in Nwagụ Annotation", "begin_now", "medium", ["https://github.com/HumanSignal/label-studio"]),
    rec("CVAT", "visual annotation", "collaborative image annotation and QA", "bounding boxes and glyph segmentation", "cell crop segmentation pipeline", ["source images", "bounding boxes", "QA roles"], "segment chart/manuscript glyph instances with reviewer agreement", "automatic crop grid only", "segmentation quality, not interpretation", "Visual Annotation Workflow for Nwagụ Cells", "after_authority_review", "high", ["https://github.com/cvat-ai/cvat"]),
    rec("CLDF/pycldf", "linguistic data standards", "machine-readable cross-linguistic datasets", "separate sign, reading, language variety, concept", "linguistic data package", ["readings", "concept IDs", "dialect metadata"], "model Nwagụ readings as CLDF-like tables", "English gloss-only records", "data interoperability, not source truth", "CLDF-Inspired Nwagụ Reading Records", "begin_now", "medium", ["https://github.com/cldf/pycldf"]),
    rec("Concepticon", "concept metadata", "stable concept identifiers", "full-word sign semantic comparison", "logograph semantic field analysis", ["confirmed full-word signs", "glosses", "concept mapping"], "map word signs to concept sets and test allocation patterns", "unmapped English glosses", "semantic comparison, not cultural meaning", "Concept-Linked Full-Word Signs", "after_logograph_review", "medium", ["https://concepticon.clld.org/"]),
    rec("LingPy", "historical linguistics computation", "lexical comparison and sound-class methods", "phonological distance baselines", "visual-phonological geometry", ["readings", "phonological forms", "glyph features"], "test relation between visual distance and phonological distance", "random phonological assignment", "correlation, not design intention", "Visual-Phonological Geometry in Nwagụ Aneke", "after_reviewed_glyph_inventory", "low", ["https://github.com/lingpy/lingpy"]),
    rec("Inspect AI", "model evaluation", "repeatable AI evaluation framework", "agent benchmark harness", "LPE/Nwagụ epistemic-integrity tasks", ["frozen cases", "scoring functions", "model configs"], "port LPE-Bench to Inspect-style evals", "manual prompt batch", "eval harness, not model claim", "Can AI Preserve Evidence Layers?", "begin_now", "low", ["https://github.com/UKGovernmentBEIS/inspect_ai"]),
    rec("LM Evaluation Harness", "language model benchmarks", "standardized few-shot evaluation", "few-shot acquisition ladder", "Nwagụ keyed/few-shot tasks", ["task spec", "gold labels", "model list"], "implement A0-A5 acquisition conditions as eval tasks", "single model demo", "benchmark comparability, not decipherment", "Keyed vs Unkeyed Nwagụ Acquisition", "after_reviewed_glyph_inventory", "low", ["https://github.com/EleutherAI/lm-evaluation-harness"]),
    rec("STORM", "research knowledge curation", "multi-perspective retrieval and outline generation", "prior-art-first article generation", "ATLAS literature sweep discipline", ["topic records", "source matrix", "claim map"], "run pre-writing research before article claims", "paper-first drafting", "curation quality, not proof", "Pre-Writing Knowledge Curation for Artifact Research", "begin_now", "low", ["https://storm-project.stanford.edu/research/storm/"]),
    rec("MLAgentBench", "agent experimentation benchmark", "goal-driven ML experiments with automatic evaluation", "autonomous research loop metrics", "Etisiobi benchmark discipline", ["fixed tasks", "metrics", "logs"], "define keep/reject loops for LPE and glyph tasks", "unscored agent notes", "agent evaluation, not research result", "Benchmarking AI Research Agents on Evidence Scarcity", "begin_now", "low", ["https://arxiv.org/abs/2310.03302"]),
    rec("AI Scientist", "automated scientific discovery", "ideation, experiments, writing, review", "paper-generation cautionary baseline", "research-machine comparison", ["experiment results", "review traces", "claim gate"], "compare paper-readiness gains with/without evidence gate", "auto paper without evidence", "workflow comparison, not scientific discovery", "Evidence-Gated Autoresearch for Cultural Artifacts", "begin_now", "medium", ["https://arxiv.org/abs/2408.06292"]),
    rec("GLOSSOPETRAE", "procedural symbolic benchmarks", "deterministic symbolic systems and raw-result traces", "controlled representation/acquisition experiments", "shadow-script and digital survivability controls", ["reviewed cells", "synthetic controls", "raw traces"], "compare real chart to shuffled and synthetic control charts", "no-control pattern spotting", "experimental architecture, not evidence about Nwagụ", "Procedural Null Models for Nwagụ Aneke", "after_reviewed_glyph_inventory", "low", ["https://github.com/elder-plinius/GLOSSOPETRAE"]),
]


def main() -> int:
    records = []
    for index, row in enumerate(RECORDS, start=1):
        item = {"atlas_id": f"ATLAS-{index:04d}", **row}
        records.append(item)

    by_phase = Counter(row["phase_gate"] for row in records)
    by_family = Counter(row["source_family"] for row in records)
    by_risk = Counter(row["rights_risk"] for row in records)
    summary = {
        "generated_at": now(),
        "status": "NWAGU_TRANSFER_ATLAS_SEEDED_NOT_PRIOR_ART_VERIFIED",
        "record_count": len(records),
        "phase_gate_counts": dict(by_phase),
        "source_family_counts": dict(by_family),
        "rights_risk_counts": dict(by_risk),
        "core_rule": "Transfer mechanisms, not conclusions. Synthetic or generated forms must never enter the historical inventory.",
        "frontier_claim_status": "not_ready",
    }
    write_jsonl(OUT / "nwagu_research_atlas.jsonl", records)
    write_json(OUT / "summary.json", summary)
    write_text(
        OUT / "README.md",
        f"""
# Nwagụ Transfer ATLAS

Artifact-to-Lab Transfer and Latent-Structure Atlas.

## Purpose

Convert external labs, repositories, and methods into falsifiable Nwagụ Aneke
research programmes without importing their conclusions.

## Current Status

`{summary['status']}`

Records: `{len(records)}`

## Core Rule

```text
transfer mechanism != evidence about Nwagụ Aneke
```

Every record must specify:

- transferable mechanism,
- Nwagụ research object,
- required evidence,
- experiment,
- negative control,
- claim ceiling,
- rights risk,
- article candidate,
- phase gate.

## Immediate Use

The atlas should drive experiment selection. It should not be cited as prior-art
verification until the source URLs and related literature have been checked.
""",
    )
    write_text(
        OUT / "ATLAS_METHOD.md",
        """
# ATLAS Method

## Evidence Firewall

ATLAS begins after the source-grounded dossier. It must preserve the current
Nwagụ boundary:

```text
source-observed: 26 rows x 8 vowel/modifier columns = 208 records
derived: 27 / 216 by f/v split only
```

## Transfer Test

For each external project, ask:

1. What mechanism does it contribute?
2. What Nwagụ research object can it interrogate?
3. What evidence is required?
4. What negative control would falsify the analogy?
5. What claim ceiling prevents overreach?
6. What rights/community gate applies?

## Forbidden Move

Do not say an external method proves anything about Nwagụ Aneke. It can only
unlock a test.
""",
    )
    write_text(
        OUT / "TOP_PROGRAMS.md",
        """
# Top ATLAS Programmes

## 1. Nwagụ Digital Twin

Community-governed representation linking source, glyph, variant, reading,
uncertainty, rights, and experiments.

## 2. Latent Glyph Grammar Challenge

Compare lookup-table, stroke-primitive, row-vowel, graph-grammar, and shuffled
control models.

## 3. Script Digital Survivability Matrix

Measure whether representations survive scan, SVG, PUA, font, PDF, database,
copy/paste, tokenizer, and model interfaces.

## 4. Epistemic Integrity Benchmark

Test whether AI preserves observed, source-indexed, derived, speculative, and
blocked statuses without inventing certainty.

Lead harness path: `ATLAS-0049` / `EXP-FRONTIER-007`, an Inspect-style LPE port
plan with no dependency installation and no model run yet.

Packaging path: `ATLAS-0039` / `EXP-FRONTIER-008`, a detached RO-Crate-style
metadata package for non-sensitive frontier artifacts. It is internal and does
not clear release, rights, or authority. The preservation decision
`PRESERVE-EXP-FRONTIER-008-001` keeps the package repo-local now and defers
DataLad / Software Heritage actions.

## 5. Full-Word Sign Allocation Study

Test whether full-word signs correlate with frequency, ambiguity, semantic
domain, cultural salience, or manuscript genre.
""",
    )
    write_json(
        EXP / "results.json",
        {
            "experiment_id": "EXP-FRONTIER-006",
            "title": "Nwagụ Transfer ATLAS",
            "status": summary["status"],
            "record_count": len(records),
            "outputs": [
                "research/frontier/nwagu_transfer_atlas/nwagu_research_atlas.jsonl",
                "research/frontier/nwagu_transfer_atlas/summary.json",
                "research/frontier/nwagu_transfer_atlas/README.md",
                "research/frontier/nwagu_transfer_atlas/ATLAS_METHOD.md",
                "research/frontier/nwagu_transfer_atlas/TOP_PROGRAMS.md",
            ],
            "frontier_claim_status": "not_ready",
            "interpretation": "The atlas turns external labs and repositories into falsifiable Nwagụ experiments. It does not verify prior art or prove any claim about the artifact.",
        },
    )
    print("NWAGU_TRANSFER_ATLAS_BUILT")
    print(f"records={len(records)}")
    print(f"status={summary['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
