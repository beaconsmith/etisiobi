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
