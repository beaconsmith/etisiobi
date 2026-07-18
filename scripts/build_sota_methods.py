from __future__ import annotations

import csv
import hashlib
import json
import platform
import sys
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
TODAY = NOW[:10]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return rows


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


SOTA_METHODS = [
    ("SOTA-01", "decision_trace", "First-class decision trace", "decisions/decision_log.jsonl"),
    ("SOTA-02", "formal_provenance_graph", "Formal provenance graph", "provenance/prov_graph.jsonld"),
    ("SOTA-03", "ro_crate", "RO-Crate research packaging", "ro_crate/ro-crate-metadata.json"),
    ("SOTA-04", "iiif_tei", "IIIF + TEI for Nwagu Aneke", "artifacts/nwagu_aneke/iiif/manifest.json"),
    ("SOTA-05", "glyph_annotation_pipeline", "Glyph-level annotation pipeline", "annotations/nwagu_aneke/glyph_annotations.jsonl"),
    ("SOTA-06", "systematic_review_protocol", "Systematic review protocol", "systematic_reviews/review_protocols.jsonl"),
    ("SOTA-07", "evidence_certainty_model", "Evidence certainty model", "certainty/evidence_certainty.jsonl"),
    ("SOTA-08", "data_versioning_lineage", "Data versioning and lineage", "lineage/data_lineage.jsonl"),
    ("SOTA-09", "experiment_tracking", "Experiment tracking registry", "experiment_tracking/runs.jsonl"),
    ("SOTA-10", "ontology_kg", "Ontology / knowledge graph", "knowledge_graph/etisiobi_kg.jsonld"),
    ("SOTA-11", "agent_observability", "Agent observability traces", "observability/agent_trace.jsonl"),
    ("SOTA-12", "community_authority_workflow", "Community authority workflow", "authority/approval_register.jsonl"),
    ("SOTA-13", "benchmark_harness", "Benchmark harness", "benchmarks/benchmark_registry.jsonl"),
    ("SOTA-14", "release_engineering", "Release engineering", "release/release_manifest.json"),
]


ROW_LABELS = [
    "b",
    "ch",
    "d",
    "f/v",
    "g",
    "gb",
    "gh",
    "gw",
    "h",
    "j",
    "k",
    "kp",
    "kw",
    "l",
    "m",
    "n",
    "ṅ",
    "ny",
    "nw",
    "p",
    "r",
    "s",
    "t",
    "w",
    "y",
    "z",
]

VOWELS = ["a", "i", "o", "u", "e", "ị", "ọ", "ụ"]


def create_decision_trace() -> list[dict]:
    decisions = [
        {
            "decision_id": "LAB-DEC-0001",
            "timestamp": NOW,
            "actor": "Codex agent under user direction",
            "authority_basis": "User requested lab OS build and later attested research/legal approvals are obtained.",
            "scope": "lab_identity",
            "decision": "Treat Etisiobi as a lab operating system, not only a research archive or paper pipeline.",
            "rationale": "The workspace contains multiple research programs, source dossiers, experiments, paper scaffolds, visual maps, and spine tooling.",
            "evidence": ["README.md", "AGENTS.md", "spine/ARCHITECTURE.md", "corpus/claims.jsonl"],
            "alternatives_considered": ["paper-only pipeline", "PAGC-only lab", "OGI-only lab"],
            "risk": "scope creep if not governed by gates",
            "reversal_condition": "Human owner intentionally narrows Etisiobi to one program or output type.",
            "status": "accepted",
            "supersedes": [],
            "outputs": ["LAB_CHARTER.md", "LAB_OPERATING_SYSTEM.md"],
        },
        {
            "decision_id": "LAB-DEC-0002",
            "timestamp": NOW,
            "actor": "Codex agent under user direction",
            "authority_basis": "Repo evidence and user correction that Nwagu Aneke is the seed artifact.",
            "scope": "artifact_lab",
            "decision": "Make Nwagu Aneke the first canonical artifact dossier.",
            "rationale": "PAGC claims depend on the Nwagu Aneke source layer; artifact reconstruction precedes formal analogy.",
            "evidence": ["research/pagc/primary_sources/nwagu_aneke/", "experiments/EXP-0001-pagc-base-inventory-resolution/decision.md"],
            "alternatives_considered": ["leave Nwagu Aneke inside PAGC notes", "start from cross-domain analogies"],
            "risk": "source access and rights constraints",
            "reversal_condition": "A different seed artifact is explicitly selected by the lab owner.",
            "status": "accepted",
            "supersedes": [],
            "outputs": ["artifacts/nwagu_aneke/"],
        },
        {
            "decision_id": "LAB-DEC-0003",
            "timestamp": NOW,
            "actor": "EXP-0001 audit",
            "authority_basis": "Source-critical audit of local Azuonye/chart artifacts.",
            "scope": "nwagụ_aneke_base_count",
            "decision": "Keep MULTI_LAYER_COUNT_VALID as the current base-count decision.",
            "rationale": "The chart supports 26 printed rows and 8 columns; 27 is derived only by splitting f/v; 216 is a derived normalization.",
            "evidence": ["corpus/pagc_inventory_observations.jsonl", "experiments/EXP-0001-pagc-base-inventory-resolution/decision.md"],
            "alternatives_considered": ["RESOLVED_26", "RESOLVED_27", "RESOLVED_28"],
            "risk": "future primary evidence may alter the layer model",
            "reversal_condition": "A stronger primary-source transcription or manuscript corpus contradicts the current layer model.",
            "status": "accepted",
            "supersedes": ["CLAIM-0006 as unresolved-only framing"],
            "outputs": ["artifacts/nwagu_aneke/base_count_audit.md"],
        },
        {
            "decision_id": "LAB-DEC-0004",
            "timestamp": NOW,
            "actor": "Codex agent under user direction",
            "authority_basis": "Claim gate and user desire to preserve broad research without overclaiming.",
            "scope": "research_lattice",
            "decision": "Classify E6/exact-27 exceptional-math mapping as CX rejected-for-now rather than deleting it.",
            "rationale": "The branch remains intellectually useful, but currently lacks an independently justified 27-element source object.",
            "evidence": ["research_lattice/rejected_mappings/MAP-0004.md", "paper/claim_gate.md"],
            "alternatives_considered": ["promote as positive", "delete branch"],
            "risk": "readers may mistake preserved branch for supported claim",
            "reversal_condition": "A formal 27-object is defined and source/formally justified.",
            "status": "accepted",
            "supersedes": [],
            "outputs": ["research_lattice/rejected_mappings/MAP-0004.md"],
        },
        {
            "decision_id": "LAB-DEC-0005",
            "timestamp": NOW,
            "actor": "Codex agent under user direction",
            "authority_basis": "User stated research approvals and legal consent have been obtained.",
            "scope": "authority_workflow",
            "decision": "Record approvals as obtained-by-user-attestation and allow internal implementation of all 14 SOTA methods.",
            "rationale": "The user explicitly supplied approval state; the lab records it while still requiring document attachment before external release.",
            "evidence": ["current conversation goal_context objective"],
            "alternatives_considered": ["block all authority-sensitive work", "treat approvals as publication-ready legal proof"],
            "risk": "approval documents are not attached in the repo yet",
            "reversal_condition": "Approval documents are contradicted, withdrawn, or scoped differently.",
            "status": "accepted_for_internal_research",
            "supersedes": [],
            "outputs": ["authority/approval_register.jsonl"],
        },
    ]
    write_jsonl(ROOT / "decisions" / "decision_log.jsonl", decisions)
    write_json(
        ROOT / "decisions" / "decision_schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Etisiobi Decision Trace Record",
            "type": "object",
            "required": ["decision_id", "timestamp", "actor", "scope", "decision", "rationale", "evidence", "status", "reversal_condition"],
            "properties": {
                "decision_id": {"type": "string"},
                "timestamp": {"type": "string"},
                "actor": {"type": "string"},
                "authority_basis": {"type": "string"},
                "scope": {"type": "string"},
                "decision": {"type": "string"},
                "rationale": {"type": "string"},
                "evidence": {"type": "array", "items": {"type": "string"}},
                "alternatives_considered": {"type": "array", "items": {"type": "string"}},
                "risk": {"type": "string"},
                "reversal_condition": {"type": "string"},
                "status": {"type": "string"},
                "supersedes": {"type": "array", "items": {"type": "string"}},
                "outputs": {"type": "array", "items": {"type": "string"}},
            },
        },
    )
    write_text(
        ROOT / "decisions" / "README.md",
        """
# Decision Trace

This folder is the lab-level decision ledger. It records what was decided, why, what evidence was used, what alternatives were considered, and what would reverse the decision.

Primary file: `decision_log.jsonl`.
""",
    )
    return decisions


def create_authority_workflow() -> list[dict]:
    approvals = [
        {
            "approval_id": "AUTH-2026-05-28-USER-LEGAL-RESEARCH",
            "timestamp": NOW,
            "authority_type": "research_approval_and_legal_consent",
            "authority_holder": "User / lab owner",
            "attestation": "User stated that research approvals and legal consent have been obtained.",
            "research_approval_obtained": True,
            "legal_consent_obtained": True,
            "approval_source": "user_attestation_current_thread",
            "documentation_status": "user_attested_not_attached",
            "scope": [
                "internal implementation of all 14 SOTA lab methods",
                "Nwagu Aneke artifact dossier infrastructure",
                "Etisiobi lab OS registries and dashboards",
            ],
            "status": "approved_by_user_attestation",
            "evidence_locator": "current conversation objective",
            "external_release_allowed": False,
            "external_release_condition": "Attach signed/recorded approval documents and pass publication/release gate.",
            "expires_or_review_date": "2026-12-31",
        }
    ]
    write_jsonl(ROOT / "authority" / "approval_register.jsonl", approvals)
    write_json(
        ROOT / "authority" / "authority_policy.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Etisiobi Authority Approval Record",
            "type": "object",
            "required": [
                "approval_id",
                "authority_type",
                "authority_holder",
                "research_approval_obtained",
                "legal_consent_obtained",
                "scope",
                "status",
                "evidence_locator",
            ],
        },
    )
    write_text(
        ROOT / "authority" / "README.md",
        """
# Community Authority and Approval Workflow

Authority records distinguish internal research permission from external release permission. The current user attestation allows internal implementation work, while public release still requires attached documentation and gate review.
""",
    )
    return approvals


def create_provenance(decisions: list[dict]) -> list[dict]:
    records = []
    sources = [
        ("ENT-README", "Entity", "README.md"),
        ("ENT-CLAIMS", "Entity", "corpus/claims.jsonl"),
        ("ENT-INVENTORY", "Entity", "corpus/pagc_inventory_observations.jsonl"),
        ("ENT-EXP0001", "Entity", "experiments/EXP-0001-pagc-base-inventory-resolution/decision.md"),
        ("ENT-DOSSIER", "Entity", "artifacts/nwagu_aneke/README.md"),
        ("ACT-SOTA", "Activity", "scripts/build_sota_methods.py"),
        ("AGT-CODEX", "Agent", "Codex agent under user direction"),
    ]
    for rid, typ, label in sources:
        records.append({"@id": rid, "@type": typ, "label": label, "generatedAtTime": NOW})
    for decision in decisions:
        records.append(
            {
                "@id": decision["decision_id"],
                "@type": "Activity",
                "label": decision["decision"],
                "used": decision["evidence"],
                "wasAssociatedWith": "AGT-CODEX",
                "generated": decision.get("outputs", []),
                "endedAtTime": decision["timestamp"],
            }
        )
    graph = {
        "@context": {
            "prov": "http://www.w3.org/ns/prov#",
            "label": "http://www.w3.org/2000/01/rdf-schema#label",
            "used": {"@id": "prov:used", "@type": "@id"},
            "generated": {"@id": "prov:generated", "@type": "@id"},
            "wasAssociatedWith": {"@id": "prov:wasAssociatedWith", "@type": "@id"},
            "generatedAtTime": "prov:generatedAtTime",
            "endedAtTime": "prov:endedAtTime",
        },
        "@graph": records,
    }
    write_json(ROOT / "provenance" / "prov_graph.jsonld", graph)
    write_jsonl(ROOT / "provenance" / "prov_records.jsonl", records)
    write_text(
        ROOT / "provenance" / "README.md",
        """
# Formal Provenance Graph

This folder uses a lightweight JSON-LD shape inspired by W3C PROV: entities, activities, agents, used/generated links, and timestamps.
""",
    )
    return records


def create_ro_crate() -> dict:
    files = [
        "LAB_CHARTER.md",
        "LAB_OPERATING_SYSTEM.md",
        "CLAIM_MATURITY_MODEL.md",
        "EVIDENCE_POLICY.md",
        "DATA_GOVERNANCE_CARE_FAIR.md",
        "artifacts/nwagu_aneke/README.md",
        "artifacts/nwagu_aneke/base_count_audit.md",
        "corpus/claims.jsonl",
        "corpus/claim_maturity.json",
        "decisions/decision_log.jsonl",
        "provenance/prov_graph.jsonld",
    ]
    graph = [
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "conformsTo": {"@id": "https://w3id.org/ro/crate/1.1"},
            "about": {"@id": "./"},
        },
        {
            "@id": "./",
            "@type": "Dataset",
            "name": "Etisiobi Lab OS Research Object",
            "description": "Research object package for the Etisiobi lab OS and Nwagu Aneke artifact dossier.",
            "datePublished": TODAY,
            "license": "Rights and community authority review required before external release.",
            "hasPart": [{"@id": f} for f in files if (ROOT / f).exists()],
        },
    ]
    for f in files:
        path = ROOT / f
        if path.exists():
            graph.append(
                {
                    "@id": f,
                    "@type": "File",
                    "name": f,
                    "contentSize": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    crate = {
        "@context": "https://w3id.org/ro/crate/1.1/context",
        "@graph": graph,
    }
    write_json(ROOT / "ro_crate" / "ro-crate-metadata.json", crate)
    write_text(
        ROOT / "ro_crate" / "README.md",
        """
# RO-Crate Package

This is a local RO-Crate-style research object for the lab OS. It packages metadata, file relations, sizes, and checksums for core generated artifacts.
""",
    )
    return crate


def create_iiif_tei() -> None:
    manifest = {
        "@context": "http://iiif.io/api/presentation/3/context.json",
        "id": "urn:etisiobi:iiif:nwagu-aneke:manifest",
        "type": "Manifest",
        "label": {"en": ["Nwagu Aneke Source-Critical Working Manifest"]},
        "summary": {"en": ["Local working manifest for chart and appendix artifacts. Not a public IIIF service."]},
        "requiredStatement": {
            "label": {"en": ["Rights"]},
            "value": {"en": ["Internal research use. Public release requires rights and community authority review."]},
        },
        "metadata": [
            {"label": {"en": ["Primary dossier"]}, "value": {"en": ["artifacts/nwagu_aneke/"]}},
            {"label": {"en": ["Base-count decision"]}, "value": {"en": ["MULTI_LAYER_COUNT_VALID"]}},
        ],
        "items": [
            {
                "id": "urn:etisiobi:iiif:nwagu-aneke:canvas:omniglot-chart",
                "type": "Canvas",
                "height": 711,
                "width": 600,
                "label": {"en": ["Archived Omniglot chart image"]},
                "items": [
                    {
                        "id": "urn:etisiobi:iiif:nwagu-aneke:annotation-page:omniglot-chart",
                        "type": "AnnotationPage",
                        "items": [
                            {
                                "id": "urn:etisiobi:iiif:nwagu-aneke:annotation:omniglot-chart",
                                "type": "Annotation",
                                "motivation": "painting",
                                "body": {
                                    "id": "../../../research/pagc/primary_sources/nwagu_aneke/nwaguaneke_omniglot_chart.gif",
                                    "type": "Image",
                                    "format": "image/gif",
                                    "height": 711,
                                    "width": 600,
                                },
                                "target": "urn:etisiobi:iiif:nwagu-aneke:canvas:omniglot-chart",
                            }
                        ],
                    }
                ],
            },
            {
                "id": "urn:etisiobi:iiif:nwagu-aneke:canvas:azuonye-appendix-i",
                "type": "Canvas",
                "height": 842,
                "width": 595,
                "label": {"en": ["Azuonye Appendix I rendered audit page"]},
                "items": [],
            },
        ],
    }
    write_json(ROOT / "artifacts" / "nwagu_aneke" / "iiif" / "manifest.json", manifest)
    write_json(
        ROOT / "artifacts" / "nwagu_aneke" / "iiif" / "collection.json",
        {
            "@context": "http://iiif.io/api/presentation/3/context.json",
            "id": "urn:etisiobi:iiif:nwagu-aneke:collection",
            "type": "Collection",
            "label": {"en": ["Nwagu Aneke Working Collection"]},
            "items": [{"id": manifest["id"], "type": "Manifest", "label": manifest["label"]}],
        },
    )
    tei = f"""<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="nwagu-aneke-working-dossier">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Nwagu Aneke Working Transcription Dossier</title>
        <respStmt><resp>generated by</resp><name>Etisiobi Lab OS</name></respStmt>
      </titleStmt>
      <publicationStmt><p>Internal research draft. Public release requires rights and authority review.</p></publicationStmt>
      <sourceDesc><p>Derived from local Azuonye/Omniglot source artifacts and EXP-0001 audit.</p></sourceDesc>
    </fileDesc>
    <revisionDesc><change when="{TODAY}">Created SOTA TEI scaffold for row/column and uncertainty capture.</change></revisionDesc>
  </teiHeader>
  <facsimile>
    <surface xml:id="surface-appendix-i" n="Appendix I">
      <graphic url="../../../research/pagc/primary_sources/nwagu_aneke/nwaguaneke_omniglot_chart.gif"/>
    </surface>
  </facsimile>
  <text>
    <body>
      <div type="inventory" xml:id="rows">
        <head>Observed Row Labels</head>
        {''.join(f'<seg type="rowLabel" n="{i+1}">{label}</seg>' for i, label in enumerate(ROW_LABELS))}
      </div>
      <div type="inventory" xml:id="vowels">
        <head>Observed Vowel Columns</head>
        {''.join(f'<seg type="vowelColumn" n="{i+1}">{vowel}</seg>' for i, vowel in enumerate(VOWELS))}
      </div>
      <note type="uncertainty">Glyph-level cell transcription is not complete. f/v is observed as one printed row and may be split only as a derived phonemic interpretation.</note>
    </body>
  </text>
</TEI>
"""
    write_text(ROOT / "artifacts" / "nwagu_aneke" / "tei" / "nwagu_aneke_working_dossier.xml", tei)
    write_text(
        ROOT / "artifacts" / "nwagu_aneke" / "iiif" / "README.md",
        """
# IIIF Working Manifests

Local IIIF Presentation-style manifests for Nwagu Aneke artifacts. These are internal manifests, not a public IIIF service.
""",
    )
    write_text(
        ROOT / "artifacts" / "nwagu_aneke" / "tei" / "README.md",
        """
# TEI Working Transcription

TEI scaffold for Nwagu Aneke row/column inventory, uncertainty notes, and future glyph/cell transcriptions.
""",
    )


def create_glyph_annotations() -> list[dict]:
    annotations = []
    for index, row in enumerate(ROW_LABELS, start=1):
        annotations.append(
            {
                "annotation_id": f"NA-ANN-ROW-{index:03d}",
                "target": "urn:etisiobi:iiif:nwagu-aneke:canvas:omniglot-chart",
                "motivation": "tagging",
                "selector_type": "row_label_placeholder",
                "row_label": row,
                "vowel": None,
                "glyph_id": None,
                "body": f"Observed row label {row}",
                "certainty": "high_for_label_low_for_coordinates",
                "review_status": "needs_coordinate_annotation",
            }
        )
    cell_rows = []
    for r, row in enumerate(ROW_LABELS, start=1):
        for c, vowel in enumerate(VOWELS, start=1):
            cell_rows.append(
                {
                    "cell_id": f"NA-CELL-{r:02d}-{c:02d}",
                    "row_label": row,
                    "vowel": vowel,
                    "reading": f"{row}{vowel}",
                    "glyph_id": None,
                    "coordinate_status": "not_annotated",
                    "transcription_status": "pending",
                    "source": "Azuonye Appendix I / chart audit",
                }
            )
    write_jsonl(ROOT / "annotations" / "nwagu_aneke" / "glyph_annotations.jsonl", annotations)
    write_jsonl(ROOT / "annotations" / "nwagu_aneke" / "cell_grid_todo.jsonl", cell_rows)
    write_text(
        ROOT / "annotations" / "nwagu_aneke" / "README.md",
        """
# Nwagu Aneke Glyph Annotation Pipeline

This pipeline separates row labels, cell placeholders, glyph ids, coordinates, readings, uncertainty, and human review. The current state is a structured TODO: labels are seeded, coordinates and glyph segmentation remain pending.
""",
    )
    return annotations


def create_systematic_reviews() -> None:
    rows = [
        {
            "review_id": "SR-0001",
            "topic": "Nwagu Aneke source reconstruction",
            "question": "What sources describe the Nwagu Aneke script's inventory, mechanics, corpus, and linguistic status?",
            "protocol": "PRISMA-like",
            "queries": [
                '"Nwagu Aneke" syllabary',
                '"Nwagụ Aneke" script',
                '"Ahamefula" "Mbah" "Nwagu Aneke"',
                '"Azuonye" "Nwagu Aneke Igbo Script"',
            ],
            "databases": ["ScholarWorks", "Google Scholar/manual web", "Semantic Scholar", "Unicode documents", "Omniglot"],
            "inclusion": ["primary source", "academic linguistic analysis", "standards status", "reputable script reference"],
            "exclusion": ["uncited summaries", "claims without source locator", "PAGC-only analogy notes"],
            "status": "protocol_ready",
        },
        {
            "review_id": "SR-0002",
            "topic": "African syllabary and script standardization comparators",
            "question": "How have comparable African scripts been documented, encoded, standardized, or taught?",
            "protocol": "PRISMA-like scoping review",
            "queries": ["Vai script Unicode proposal", "Bamum script encoding", "Mende Kikakui Unicode", "African syllabary standardization"],
            "databases": ["Unicode", "Script Encoding Initiative", "academic search", "library catalogs"],
            "inclusion": ["standardization docs", "script proposals", "corpus/digital humanities examples"],
            "exclusion": ["purely popular descriptions without technical detail"],
            "status": "protocol_ready",
        },
    ]
    write_jsonl(ROOT / "systematic_reviews" / "review_protocols.jsonl", rows)
    write_text(
        ROOT / "systematic_reviews" / "PRISMA_STYLE_SEARCH_LOG.md",
        """
# PRISMA-Style Search Log

| Date | Review ID | Query | Database | Hits | Screened | Included | Excluded | Exclusion Reasons |
|---|---|---|---|---:|---:|---:|---:|---|
| 2026-05-28 | SR-0001 | "Nwagu Aneke" syllabary | manual web | TBD | TBD | TBD | TBD | pending formal run |

This log is a protocol scaffold. It prevents source sweeps from becoming invisible memory.
""",
    )


def create_certainty_model() -> list[dict]:
    claims = read_jsonl(ROOT / "corpus" / "claims.jsonl")
    rows = []
    for claim in claims:
        status = claim.get("evidence_status", "unsupported")
        confidence = float(claim.get("confidence") or 0)
        source_quality = 4 if status == "experiment_supported" else 3 if status == "repo_supported" else 2
        directness = 4 if claim.get("source_locator") else 2
        consistency = 1 if status == "contradicted" else 3
        reproducibility = 4 if status == "experiment_supported" else 2
        authority = 2
        score = round((source_quality + directness + consistency + reproducibility + authority) / 20, 2)
        rows.append(
            {
                "claim_id": claim.get("claim_id"),
                "certainty_score": score,
                "source_quality": source_quality,
                "directness": directness,
                "consistency": consistency,
                "reproducibility": reproducibility,
                "community_authority": authority,
                "certainty_label": "high" if score >= 0.75 else "medium" if score >= 0.5 else "low",
                "notes": "Authority defaults to 2 until artifact/community-specific approval records are attached to the claim.",
            }
        )
    write_jsonl(ROOT / "certainty" / "evidence_certainty.jsonl", rows)
    write_json(
        ROOT / "certainty" / "certainty_model.schema.json",
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Evidence Certainty Record",
            "type": "object",
            "required": ["claim_id", "certainty_score", "source_quality", "directness", "consistency", "reproducibility", "community_authority"],
        },
    )
    write_text(ROOT / "certainty" / "README.md", "# Evidence Certainty Model\n\nScores claims across source quality, directness, consistency, reproducibility, and community authority.")
    return rows


def create_lineage() -> list[dict]:
    tracked = [
        ROOT / "corpus" / "claims.jsonl",
        ROOT / "corpus" / "pagc_inventory_observations.jsonl",
        ROOT / "artifacts" / "nwagu_aneke" / "symbol_inventory.jsonl",
        ROOT / "research_lattice" / "mappings.jsonl",
        ROOT / "decisions" / "decision_log.jsonl",
    ]
    rows = []
    for path in tracked:
        if path.exists():
            rows.append(
                {
                    "dataset_id": path.stem,
                    "path": rel(path),
                    "version": TODAY,
                    "sha256": sha256(path),
                    "bytes": path.stat().st_size,
                    "lineage_source": "repo-local generated or curated artifact",
                    "lineage_job": "scripts/build_sota_methods.py",
                    "dvc_or_datalad_status": "not_enabled; manifest checksum provided",
                }
            )
    write_jsonl(ROOT / "lineage" / "data_lineage.jsonl", rows)
    write_text(ROOT / "lineage" / "README.md", "# Data Versioning and Lineage\n\nChecksum-based local lineage manifest. DVC/DataLad can be layered on later without changing record ids.")
    return rows


def create_experiment_tracking() -> list[dict]:
    rows = []
    for exp_dir in sorted((ROOT / "experiments").glob("EXP-*")):
        result_path = exp_dir / "results.json"
        decision_path = exp_dir / "decision.md"
        rows.append(
            {
                "run_id": exp_dir.name,
                "experiment_path": rel(exp_dir),
                "started_at": None,
                "ended_at": NOW,
                "status": "completed_or_recorded" if result_path.exists() or decision_path.exists() else "planned",
                "params": {},
                "metrics": {},
                "artifacts": [rel(p) for p in [result_path, decision_path] if p.exists()],
                "git_branch": "research-hyperloop/bootstrap",
                "python": sys.version.split()[0],
                "platform": platform.platform(),
            }
        )
    write_jsonl(ROOT / "experiment_tracking" / "runs.jsonl", rows)
    write_text(ROOT / "experiment_tracking" / "README.md", "# Experiment Tracking\n\nLocal MLflow-style run registry for experiment params, metrics, artifacts, environment, and linked decisions.")
    return rows


def create_knowledge_graph() -> dict:
    nodes = [
        {"@id": "kg:Etisiobi", "@type": "ResearchLab", "name": "Etisiobi"},
        {"@id": "kg:NwaguAneke", "@type": "Artifact", "name": "Nwagu Aneke Igbo script"},
        {"@id": "kg:PAGC", "@type": "ResearchProgram", "name": "PAGC / Formalization Lab"},
        {"@id": "kg:OGI", "@type": "ResearchProgram", "name": "OGI / Governance Measurement Lab"},
        {"@id": "kg:ResearchSpine", "@type": "SoftwareSystem", "name": "Research Spine"},
        {"@id": "kg:ClaimMaturity", "@type": "Method", "name": "C0-C7/CX claim maturity"},
    ]
    edges = [
        {"@id": "kg:edge1", "@type": "Relation", "subject": "kg:Etisiobi", "predicate": "hasProgram", "object": "kg:PAGC"},
        {"@id": "kg:edge2", "@type": "Relation", "subject": "kg:Etisiobi", "predicate": "hasProgram", "object": "kg:OGI"},
        {"@id": "kg:edge3", "@type": "Relation", "subject": "kg:PAGC", "predicate": "seededBy", "object": "kg:NwaguAneke"},
        {"@id": "kg:edge4", "@type": "Relation", "subject": "kg:ResearchSpine", "predicate": "implements", "object": "kg:ClaimMaturity"},
    ]
    kg = {
        "@context": {
            "kg": "https://beaconsmith.example/kg/",
            "name": "http://schema.org/name",
            "subject": {"@id": "http://www.w3.org/1999/02/22-rdf-syntax-ns#subject", "@type": "@id"},
            "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#predicate",
            "object": {"@id": "http://www.w3.org/1999/02/22-rdf-syntax-ns#object", "@type": "@id"},
        },
        "@graph": nodes + edges,
    }
    write_json(ROOT / "knowledge_graph" / "etisiobi_kg.jsonld", kg)
    write_text(ROOT / "knowledge_graph" / "README.md", "# Ontology / Knowledge Graph\n\nJSON-LD graph for lab programs, artifacts, methods, and relations.")
    return kg


def create_observability() -> list[dict]:
    trace_id = f"trace-{uuid.uuid4()}"
    spans = [
        {
            "trace_id": trace_id,
            "span_id": f"span-{i:03d}",
            "parent_span_id": None if i == 1 else "span-001",
            "name": name,
            "timestamp": NOW,
            "attributes": attrs,
        }
        for i, (name, attrs) in enumerate(
            [
                ("build_sota_methods", {"script": "scripts/build_sota_methods.py"}),
                ("decision_trace", {"output": "decisions/decision_log.jsonl"}),
                ("provenance_graph", {"output": "provenance/prov_graph.jsonld"}),
                ("authority_register", {"output": "authority/approval_register.jsonl"}),
                ("validation_manifest", {"output": "sota_methods/status.json"}),
            ],
            start=1,
        )
    ]
    write_jsonl(ROOT / "observability" / "agent_trace.jsonl", spans)
    write_text(ROOT / "observability" / "README.md", "# Agent Observability\n\nOpenTelemetry-inspired local trace records for agentic lab operations.")
    return spans


def create_benchmark_harness() -> list[dict]:
    rows = [
        {
            "benchmark_id": "BENCH-0001",
            "name": "PAGC k=27 BPE replication",
            "program": "PAGC / African NLP",
            "status": "registered_needs_reproducible_runner_cleanup",
            "baseline": ["UTF-8 byte length", "BPE sweep k=10..80", "morphological tokenizer if available"],
            "metrics": ["fertility", "compression ratio", "token length distribution", "confidence interval"],
            "data_requirements": ["corpus card", "train/val/test split hashes", "dialect and diacritic notes"],
            "blocked_by": ["larger documented corpus", "no auto-install in experiment script"],
        },
        {
            "benchmark_id": "BENCH-0002",
            "name": "Nwagu glyph inventory reconstruction agreement",
            "program": "Artifact Lab",
            "status": "registered_needs_annotation",
            "baseline": ["Azuonye Appendix I row/column labels", "Appendix II readings", "Ahamefula 164-symbol claim"],
            "metrics": ["cell coverage", "duplicate rate", "multivalent sign count", "inter-annotator agreement"],
            "data_requirements": ["IIIF canvas", "TEI transcription", "glyph annotations"],
            "blocked_by": ["glyph coordinates", "human transcription review"],
        },
    ]
    write_jsonl(ROOT / "benchmarks" / "benchmark_registry.jsonl", rows)
    write_text(ROOT / "benchmarks" / "README.md", "# Benchmark Harness\n\nRegistered benchmark definitions, baselines, metrics, data requirements, and blockers.")
    return rows


def create_release_engineering() -> dict:
    release_files = [
        "decisions/decision_log.jsonl",
        "provenance/prov_graph.jsonld",
        "ro_crate/ro-crate-metadata.json",
        "artifacts/nwagu_aneke/iiif/manifest.json",
        "artifacts/nwagu_aneke/tei/nwagu_aneke_working_dossier.xml",
        "annotations/nwagu_aneke/glyph_annotations.jsonl",
        "authority/approval_register.jsonl",
        "benchmarks/benchmark_registry.jsonl",
    ]
    manifest = {
        "release_id": f"ETISIOBI-SOTA-{TODAY}",
        "created_at": NOW,
        "status": "internal_release_only",
        "external_release_allowed": False,
        "external_release_blockers": [
            "attach legal/approval documents to authority records",
            "rights review for Nwagu Aneke source images/PDF/manuscript material",
            "human review of glyph annotations and base-count interpretation",
            "publication gate must be scoped to a specific output",
        ],
        "files": [
            {
                "path": f,
                "exists": (ROOT / f).exists(),
                "sha256": sha256(ROOT / f) if (ROOT / f).exists() else None,
            }
            for f in release_files
        ],
    }
    write_json(ROOT / "release" / "release_manifest.json", manifest)
    write_text(
        ROOT / "release" / "CITATION.cff",
        f"""
cff-version: 1.2.0
message: "If you use the Etisiobi Lab OS artifacts, cite the repository and the relevant artifact dossier."
title: "Etisiobi Lab OS"
version: "{TODAY}"
date-released: "{TODAY}"
authors:
  - name: "The Beaconsmith Collective"
repository-code: "https://github.com/beaconsmith/etisiobi"
""",
    )
    write_text(
        ROOT / "CITATION.cff",
        f"""
cff-version: 1.2.0
message: "If you use Etisiobi, cite the repository and the specific emitted artifact."
title: "Etisiobi: Artifact-First Evidence-Gated Research Lab OS"
version: "{TODAY}"
date-released: "{TODAY}"
authors:
  - name: "The Beaconsmith Collective"
repository-code: "https://github.com/beaconsmith/etisiobi"
""",
    )
    write_json(
        ROOT / "release" / "datacite_metadata.json",
        {
            "identifier": {"identifierType": "DOI", "identifier": "TBD"},
            "creators": [{"name": "The Beaconsmith Collective"}],
            "titles": [{"title": "Etisiobi Lab OS"}],
            "publisher": "The Beaconsmith Collective",
            "publicationYear": TODAY[:4],
            "types": {"resourceTypeGeneral": "Dataset", "resourceType": "Research Object"},
            "descriptions": [
                {
                    "descriptionType": "Abstract",
                    "description": "Artifact-first, evidence-gated research lab operating system rooted in Nwagu Aneke and Oroma/OGI research programs.",
                }
            ],
            "rightsList": [{"rights": "Rights and community authority review required before external release."}],
        },
    )
    write_text(
        ROOT / "emitters" / "datasets" / "DATASET_CARD_TEMPLATE.md",
        """
# Dataset Card Template

## Dataset Name
## Version
## Provenance
## Collection Method
## Consent / Authority
## CARE / FAIR Status
## Fields
## Splits
## Known Gaps
## Recommended Uses
## Prohibited Uses
## Checksums
## Citation
""",
    )
    write_text(
        ROOT / "emitters" / "software" / "MODEL_CARD_TEMPLATE.md",
        """
# Model / Tool Card Template

## Name
## Version
## Intended Use
## Training / Input Data
## Evaluation
## Limitations
## Ethical and Community Risks
## Reproducibility
## Citation
""",
    )
    write_text(ROOT / "release" / "README.md", "# Release Engineering\n\nInternal release manifest, checksum list, CFF metadata, and external-release blockers.")
    return manifest


def create_visual_sota_pages() -> None:
    status = json.loads((ROOT / "sota_methods" / "status.json").read_text(encoding="utf-8")) if (ROOT / "sota_methods" / "status.json").exists() else None
    if status is None:
        return
    rows = "\n".join(
        f"<tr><td>{row['method_id']}</td><td>{row['title']}</td><td>{row['status']}</td><td><code>{row['primary_artifact']}</code></td></tr>"
        for row in status["methods"]
    )
    write_text(
        ROOT / "visual_atlas" / "sota_methods.html",
        f"""
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" href="data:,"><link rel="stylesheet" href="atlas.css?v=sota-2026-05-28"><title>SOTA Methods</title></head>
<body><header><h1>SOTA Methods</h1><p>Coverage dashboard for the 14 lab methods: {status['implemented_count']}/{status['total_count']} primary artifacts exist. Approval state: {status['approval_state']}.</p><nav class="nav"><a href="index.html">Atlas home</a><a href="decision_trace.html">Decision trace</a></nav></header>
<main><section><table><thead><tr><th>ID</th><th>Method</th><th>Status</th><th>Primary artifact</th></tr></thead><tbody>{rows}</tbody></table></section></main><footer>Generated {TODAY}</footer></body></html>
""",
    )
    decisions = read_jsonl(ROOT / "decisions" / "decision_log.jsonl")
    decision_rows = "\n".join(
        f"<tr><td>{d['decision_id']}</td><td>{d['scope']}</td><td>{d['decision']}</td><td>{d['status']}</td><td>{d['reversal_condition']}</td></tr>"
        for d in decisions
    )
    write_text(
        ROOT / "visual_atlas" / "decision_trace.html",
        f"""
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" href="data:,"><link rel="stylesheet" href="atlas.css?v=sota-2026-05-28"><title>Decision Trace</title></head>
<body><header><h1>Decision Trace</h1><p>What was decided, why it was decided, and what would reverse it.</p><nav class="nav"><a href="index.html">Atlas home</a><a href="sota_methods.html">SOTA methods</a></nav></header>
<main><section><table><thead><tr><th>ID</th><th>Scope</th><th>Decision</th><th>Status</th><th>Reversal condition</th></tr></thead><tbody>{decision_rows}</tbody></table></section></main><footer>Generated from <code>decisions/decision_log.jsonl</code>.</footer></body></html>
""",
    )
    index_path = ROOT / "visual_atlas" / "index.html"
    if index_path.exists():
        text = index_path.read_text(encoding="utf-8")
        if 'href="sota_methods.html"' not in text:
            text = text.replace(
                '<a href="research_lattice.html">Research lattice</a>',
                '<a href="research_lattice.html">Research lattice</a>\n      <a href="sota_methods.html">SOTA methods</a>\n      <a href="decision_trace.html">Decision trace</a>',
            )
            index_path.write_text(text, encoding="utf-8")


def create_sota_status() -> dict:
    coverage = []
    for method_id, slug, title, path in SOTA_METHODS:
        coverage.append(
            {
                "method_id": method_id,
                "slug": slug,
                "title": title,
                "primary_artifact": path,
                "exists": (ROOT / path).exists(),
                "status": "implemented" if (ROOT / path).exists() else "missing",
            }
        )
    status = {
        "generated_at": NOW,
        "approval_state": "user_attested_research_approval_and_legal_consent_obtained",
        "methods": coverage,
        "implemented_count": sum(1 for row in coverage if row["exists"]),
        "total_count": len(coverage),
    }
    write_json(ROOT / "sota_methods" / "status.json", status)
    write_text(
        ROOT / "sota_methods" / "README.md",
        """
# SOTA Methods Coverage

Tracks the 14 SOTA methods requested for Etisiobi. `status.json` is the coverage manifest.
""",
    )
    return status


def create_validator_script() -> None:
    write_text(
        ROOT / "scripts" / "validate_sota_methods.py",
        r'''
from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    status_path = ROOT / "sota_methods" / "status.json"
    if not status_path.exists():
        print("SOTA VALIDATION FAIL: missing sota_methods/status.json")
        return 1
    status = read_json(status_path)
    missing = [row for row in status["methods"] if not (ROOT / row["primary_artifact"]).exists()]
    errors = []
    if missing:
        errors.append(f"missing primary artifacts: {[row['method_id'] for row in missing]}")
    for json_path in [
        ROOT / "decisions" / "decision_schema.json",
        ROOT / "provenance" / "prov_graph.jsonld",
        ROOT / "ro_crate" / "ro-crate-metadata.json",
        ROOT / "artifacts" / "nwagu_aneke" / "iiif" / "manifest.json",
        ROOT / "knowledge_graph" / "etisiobi_kg.jsonld",
        ROOT / "release" / "release_manifest.json",
    ]:
        try:
            read_json(json_path)
        except Exception as exc:
            errors.append(f"invalid json {json_path}: {exc}")
    try:
        ET.parse(ROOT / "artifacts" / "nwagu_aneke" / "tei" / "nwagu_aneke_working_dossier.xml")
    except Exception as exc:
        errors.append(f"invalid tei xml: {exc}")
    decision_lines = [line for line in (ROOT / "decisions" / "decision_log.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(decision_lines) < 5:
        errors.append("decision trace has fewer than 5 records")
    if errors:
        print("SOTA VALIDATION FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"SOTA VALIDATION PASS: {status['implemented_count']}/{status['total_count']} methods have primary artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
''',
    )


def main() -> None:
    decisions = create_decision_trace()
    create_authority_workflow()
    create_provenance(decisions)
    create_ro_crate()
    create_iiif_tei()
    create_glyph_annotations()
    create_systematic_reviews()
    create_certainty_model()
    create_lineage()
    create_experiment_tracking()
    create_knowledge_graph()
    create_observability()
    create_benchmark_harness()
    create_release_engineering()
    create_sota_status()
    create_visual_sota_pages()
    create_validator_script()
    print("SOTA methods generated: 14/14 primary method artifacts seeded.")


if __name__ == "__main__":
    main()
