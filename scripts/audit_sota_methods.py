from __future__ import annotations

import csv
import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def ok(name: str, passed: bool, evidence: str, gap: str = "") -> dict:
    return {
        "requirement": name,
        "passed": bool(passed),
        "evidence": evidence,
        "gap": gap if not passed else "",
    }


def audit() -> list[dict]:
    checks: list[dict] = []

    decisions = read_jsonl(ROOT / "decisions" / "decision_log.jsonl")
    required_decision_fields = {"decision_id", "timestamp", "actor", "scope", "decision", "rationale", "evidence", "status", "reversal_condition"}
    checks.append(ok("SOTA-01 decision trace has >=5 decisions", len(decisions) >= 5, "decisions/decision_log.jsonl"))
    checks.append(ok("SOTA-01 every decision has required trace fields", all(required_decision_fields <= set(d) for d in decisions), "decisions/decision_log.jsonl"))
    checks.append(ok("SOTA-01 approval/legal decision is represented", any(d.get("scope") == "authority_workflow" for d in decisions), "decisions/decision_log.jsonl"))

    prov = read_json(ROOT / "provenance" / "prov_graph.jsonld")
    graph = prov.get("@graph", [])
    checks.append(ok("SOTA-02 provenance graph has entities", any(g.get("@type") == "Entity" for g in graph), "provenance/prov_graph.jsonld"))
    checks.append(ok("SOTA-02 provenance graph has activities", any(g.get("@type") == "Activity" for g in graph), "provenance/prov_graph.jsonld"))
    checks.append(ok("SOTA-02 provenance graph has agent association", any(g.get("wasAssociatedWith") for g in graph), "provenance/prov_graph.jsonld"))

    crate = read_json(ROOT / "ro_crate" / "ro-crate-metadata.json")
    crate_graph = crate.get("@graph", [])
    root_dataset = next((g for g in crate_graph if g.get("@id") == "./"), {})
    has_parts = root_dataset.get("hasPart", [])
    file_nodes = [g for g in crate_graph if g.get("@type") == "File"]
    checksum_ok = all((ROOT / f["@id"]).exists() and sha256(ROOT / f["@id"]) == f.get("sha256") for f in file_nodes)
    checks.append(ok("SOTA-03 RO-Crate has root dataset", bool(root_dataset), "ro_crate/ro-crate-metadata.json"))
    checks.append(ok("SOTA-03 RO-Crate has file parts", len(has_parts) >= 5 and len(file_nodes) >= 5, "ro_crate/ro-crate-metadata.json"))
    checks.append(ok("SOTA-03 RO-Crate file checksums match", checksum_ok, "ro_crate/ro-crate-metadata.json"))

    iiif = read_json(ROOT / "artifacts" / "nwagu_aneke" / "iiif" / "manifest.json")
    tei_path = ROOT / "artifacts" / "nwagu_aneke" / "tei" / "nwagu_aneke_working_dossier.xml"
    tei_root = ET.parse(tei_path).getroot()
    tei_text = tei_path.read_text(encoding="utf-8")
    checks.append(ok("SOTA-04 IIIF manifest is a Manifest with canvases", iiif.get("type") == "Manifest" and len(iiif.get("items", [])) >= 2, "artifacts/nwagu_aneke/iiif/manifest.json"))
    checks.append(ok("SOTA-04 TEI parses as XML", tei_root.tag.endswith("TEI"), "artifacts/nwagu_aneke/tei/nwagu_aneke_working_dossier.xml"))
    checks.append(ok("SOTA-04 TEI includes row and vowel inventories", "rowLabel" in tei_text and "vowelColumn" in tei_text, "artifacts/nwagu_aneke/tei/nwagu_aneke_working_dossier.xml"))

    glyph_rows = read_jsonl(ROOT / "annotations" / "nwagu_aneke" / "glyph_annotations.jsonl")
    cell_rows = read_jsonl(ROOT / "annotations" / "nwagu_aneke" / "cell_grid_todo.jsonl")
    checks.append(ok("SOTA-05 glyph annotation seeds 26 row labels", len(glyph_rows) == 26, "annotations/nwagu_aneke/glyph_annotations.jsonl"))
    checks.append(ok("SOTA-05 cell grid seeds 208 row-column cells", len(cell_rows) == 208, "annotations/nwagu_aneke/cell_grid_todo.jsonl"))
    checks.append(ok("SOTA-05 annotation records carry review status", all("review_status" in row for row in glyph_rows), "annotations/nwagu_aneke/glyph_annotations.jsonl"))

    reviews = read_jsonl(ROOT / "systematic_reviews" / "review_protocols.jsonl")
    checks.append(ok("SOTA-06 systematic review has >=2 protocols", len(reviews) >= 2, "systematic_reviews/review_protocols.jsonl"))
    checks.append(ok("SOTA-06 protocols include queries/inclusion/exclusion", all(row.get("queries") and row.get("inclusion") and row.get("exclusion") for row in reviews), "systematic_reviews/review_protocols.jsonl"))

    claims = read_jsonl(ROOT / "corpus" / "claims.jsonl")
    certainties = read_jsonl(ROOT / "certainty" / "evidence_certainty.jsonl")
    checks.append(ok("SOTA-07 certainty records cover corpus claims", len(certainties) == len(claims), "certainty/evidence_certainty.jsonl"))
    checks.append(ok("SOTA-07 certainty scores are bounded", all(0 <= row.get("certainty_score", -1) <= 1 for row in certainties), "certainty/evidence_certainty.jsonl"))

    lineage = read_jsonl(ROOT / "lineage" / "data_lineage.jsonl")
    lineage_ok = all((ROOT / row["path"]).exists() and sha256(ROOT / row["path"]) == row["sha256"] for row in lineage)
    checks.append(ok("SOTA-08 lineage tracks >=5 datasets/artifacts", len(lineage) >= 5, "lineage/data_lineage.jsonl"))
    checks.append(ok("SOTA-08 lineage checksums match current files", lineage_ok, "lineage/data_lineage.jsonl"))

    runs = read_jsonl(ROOT / "experiment_tracking" / "runs.jsonl")
    checks.append(ok("SOTA-09 experiment registry tracks >=4 runs", len(runs) >= 4, "experiment_tracking/runs.jsonl"))
    checks.append(ok("SOTA-09 experiment records include status and artifacts", all("status" in row and "artifacts" in row for row in runs), "experiment_tracking/runs.jsonl"))

    kg = read_json(ROOT / "knowledge_graph" / "etisiobi_kg.jsonld")
    kg_graph = kg.get("@graph", [])
    checks.append(ok("SOTA-10 knowledge graph has nodes and relations", any(g.get("@type") == "ResearchLab" for g in kg_graph) and any(g.get("@type") == "Relation" for g in kg_graph), "knowledge_graph/etisiobi_kg.jsonld"))
    checks.append(ok("SOTA-10 KG links PAGC to Nwagu Aneke", any(g.get("predicate") == "seededBy" for g in kg_graph), "knowledge_graph/etisiobi_kg.jsonld"))

    spans = read_jsonl(ROOT / "observability" / "agent_trace.jsonl")
    checks.append(ok("SOTA-11 observability has >=5 spans", len(spans) >= 5, "observability/agent_trace.jsonl"))
    checks.append(ok("SOTA-11 spans share a trace id", len({row.get("trace_id") for row in spans}) == 1, "observability/agent_trace.jsonl"))

    approvals = read_jsonl(ROOT / "authority" / "approval_register.jsonl")
    approval = approvals[0] if approvals else {}
    checks.append(ok("SOTA-12 authority register has approval record", bool(approval), "authority/approval_register.jsonl"))
    checks.append(ok("SOTA-12 approval records research approval and legal consent", approval.get("research_approval_obtained") is True and approval.get("legal_consent_obtained") is True, "authority/approval_register.jsonl"))

    benchmarks = read_jsonl(ROOT / "benchmarks" / "benchmark_registry.jsonl")
    checks.append(ok("SOTA-13 benchmark registry has >=2 benchmarks", len(benchmarks) >= 2, "benchmarks/benchmark_registry.jsonl"))
    checks.append(ok("SOTA-13 benchmarks define baselines, metrics, data requirements", all(row.get("baseline") and row.get("metrics") and row.get("data_requirements") for row in benchmarks), "benchmarks/benchmark_registry.jsonl"))

    release = read_json(ROOT / "release" / "release_manifest.json")
    files = release.get("files", [])
    release_ok = all((ROOT / f["path"]).exists() and sha256(ROOT / f["path"]) == f.get("sha256") for f in files)
    checks.append(ok("SOTA-14 release manifest files exist and checksums match", release_ok, "release/release_manifest.json"))
    checks.append(ok("SOTA-14 citation and DataCite metadata exist", (ROOT / "CITATION.cff").exists() and (ROOT / "release" / "datacite_metadata.json").exists(), "CITATION.cff; release/datacite_metadata.json"))

    return checks


def write_reports(checks: list[dict]) -> None:
    out_dir = ROOT / "sota_methods"
    out_dir.mkdir(parents=True, exist_ok=True)
    passed = sum(1 for check in checks if check["passed"])
    report = {
        "status": "complete" if passed == len(checks) else "incomplete",
        "passed": passed,
        "total": len(checks),
        "checks": checks,
    }
    (out_dir / "completion_audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (out_dir / "coverage_matrix.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["requirement", "passed", "evidence", "gap"])
        writer.writeheader()
        writer.writerows(checks)
    lines = [
        "# SOTA Methods Completion Audit",
        "",
        f"Status: **{report['status']}**",
        "",
        f"Passed: {passed}/{len(checks)}",
        "",
        "| Requirement | Passed | Evidence | Gap |",
        "|---|---:|---|---|",
    ]
    for check in checks:
        lines.append(f"| {check['requirement']} | {check['passed']} | `{check['evidence']}` | {check['gap']} |")
    (out_dir / "COMPLETION_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    checks = audit()
    write_reports(checks)
    failures = [check for check in checks if not check["passed"]]
    if failures:
        print(f"SOTA COMPLETION AUDIT FAIL: {len(failures)} failing checks")
        for failure in failures:
            print(f"- {failure['requirement']}: {failure['gap'] or failure['evidence']}")
        return 1
    print(f"SOTA COMPLETION AUDIT PASS: {len(checks)}/{len(checks)} method-specific checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
