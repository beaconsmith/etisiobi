from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BMC_PATH = ROOT / "corpus" / "base_modifier_cache.jsonl"
OUT_DIR = ROOT / "exports" / "web_annotation"
OUT_PATH = OUT_DIR / "bmc_web_annotations.jsonld"


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def annotation_from_bmc(row: dict) -> dict:
    target: dict = {
        "type": "SpecificResource",
        "source": row.get("iiif_canvas") or row.get("tei_locator") or row.get("cell_id"),
        "bmc:teiLocator": row.get("tei_locator"),
    }
    if row.get("source_region"):
        target["selector"] = {
            "type": "FragmentSelector",
            "conformsTo": "http://www.w3.org/TR/media-frags/",
            "value": row["source_region"],
        }
    else:
        target["bmc:selectorStatus"] = row.get("source_region_status", "not_annotated")

    return {
        "id": f"urn:etisiobi:web-annotation:{row['bmc_id']}",
        "type": "Annotation",
        "motivation": ["classifying", "linking"],
        "body": [
            {
                "type": "TextualBody",
                "purpose": "tagging",
                "value": row.get("reading", ""),
                "format": "text/plain",
                "bmc:baseId": row.get("base_id"),
                "bmc:modifierId": row.get("modifier_id"),
                "bmc:rowLabel": row.get("row_label"),
                "bmc:vowelLabel": row.get("vowel_label"),
            },
            {
                "type": "TextualBody",
                "purpose": "assessing",
                "value": row.get("certainty_basis", ""),
                "format": "text/plain",
                "bmc:certainty": row.get("certainty"),
                "bmc:reviewStatus": row.get("review_status"),
            },
        ],
        "target": target,
        "bmc:bmcId": row.get("bmc_id"),
        "bmc:cellId": row.get("cell_id"),
        "bmc:glyphObservationId": row.get("glyph_observation_id"),
        "bmc:provenanceActivity": row.get("provenance_activity"),
        "bmc:lineageRecord": row.get("lineage_record"),
        "bmc:claimDependencies": row.get("claim_dependencies", []),
        "bmc:mappingStatus": "partial_web_annotation_mapping",
    }


def export() -> dict:
    rows = read_jsonl(BMC_PATH)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    graph = [annotation_from_bmc(row) for row in rows]
    payload = {
        "@context": [
            "http://www.w3.org/ns/anno.jsonld",
            {
                "bmc": "https://beaconsmith.github.io/etisiobi/ns/bmc#",
                "prov": "http://www.w3.org/ns/prov#",
                "dcterms": "http://purl.org/dc/terms/",
            },
        ],
        "id": "urn:etisiobi:web-annotation:base-modifier-cache",
        "type": "AnnotationCollection",
        "generatedAtTime": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "label": "Base Modifier Cache Web Annotation export",
        "total": len(graph),
        "first": {
            "type": "AnnotationPage",
            "items": graph,
        },
        "bmc:complianceStatus": "mapping_proposal_not_validated_full_compliance",
    }
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT_DIR / "README.md").write_text(
        "# BMC Web Annotation Export\n\n"
        "This directory contains a JSON-LD mapping from Base Modifier Cache records to the W3C Web Annotation pattern.\n\n"
        "Status: partial mapping proposal. Each BMC record becomes an Annotation with TextualBody entries for reading and certainty, and a SpecificResource target using the IIIF canvas and TEI locator. Most records lack reviewed pixel selectors, so this is not claimed as full Web Annotation compliance.\n",
        encoding="utf-8",
    )
    return {"annotations": len(graph), "path": str(OUT_PATH)}


if __name__ == "__main__":
    print(json.dumps(export(), indent=2))
