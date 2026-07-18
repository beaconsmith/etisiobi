from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BMC_PATH = ROOT / "corpus" / "base_modifier_cache.jsonl"
OUT_DIR = ROOT / "exports" / "cidoc_crm"
OUT_PATH = OUT_DIR / "bmc_cidoc_mapping.jsonld"


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def export() -> dict:
    rows = read_jsonl(BMC_PATH)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    graph: list[dict] = [
        {
            "@id": "bmc:source-artifact/nwagu-aneke-working-chart",
            "@type": "crm:E22_Human-Made_Object",
            "rdfs:label": "Nwagu Aneke source chart / working cultural artifact reference",
            "bmc:mappingNote": "Cultural object placeholder; exact source-object authority requires human review.",
        },
        {
            "@id": "bmc:digital-object/bmc-dataset",
            "@type": "crm:E73_Information_Object",
            "rdfs:label": "Base Modifier Cache dataset",
            "crm:P129_is_about": {"@id": "bmc:source-artifact/nwagu-aneke-working-chart"},
        },
        {
            "@id": "bmc:activity/bmc-generation",
            "@type": ["crm:E13_Attribute_Assignment", "crmdig:D7_Digital_Machine_Event"],
            "rdfs:label": "BMC row-vowel annotation and count-layer assignment",
            "crm:P140_assigned_attribute_to": {"@id": "bmc:digital-object/bmc-dataset"},
            "bmc:mappingStatus": "proposal_not_validated_by_cidoc_expert",
        },
        {
            "@id": "bmc:actor/etisiobi-research-collective",
            "@type": "crm:E39_Actor",
            "rdfs:label": "Etisiobi Research Collective",
        },
    ]
    for row in rows:
        graph.append(
            {
                "@id": f"bmc:object/{row['bmc_id']}",
                "@type": "crm:E73_Information_Object",
                "rdfs:label": f"BMC object {row['bmc_id']} ({row.get('reading', '')})",
                "crm:P1_is_identified_by": row.get("cell_id"),
                "crm:P2_has_type": ["BaseModifierCacheRecord", row.get("review_status", "unknown")],
                "crm:P129_is_about": {"@id": "bmc:source-artifact/nwagu-aneke-working-chart"},
                "crm:P94i_was_created_by": {"@id": "bmc:activity/bmc-generation"},
                "bmc:teiLocator": row.get("tei_locator"),
                "bmc:iiifCanvas": row.get("iiif_canvas"),
                "bmc:certainty": row.get("certainty"),
                "bmc:claimDependencies": row.get("claim_dependencies", []),
            }
        )
    payload = {
        "@context": {
            "crm": "http://www.cidoc-crm.org/cidoc-crm/",
            "crmdig": "http://www.cidoc-crm.org/extensions/crmdig/",
            "bmc": "https://beaconsmith.github.io/etisiobi/ns/bmc#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        },
        "@id": "urn:etisiobi:cidoc-crm:bmc-mapping",
        "generatedAtTime": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "bmc:cidocVersion": "CIDOC CRM 7.1.3",
        "bmc:crmdigVersion": "CRMdig 5.0",
        "bmc:status": "lightweight_mapping_proposal_not_domain_validated",
        "@graph": graph,
    }
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT_DIR / "README.md").write_text(
        "# BMC CIDOC CRM / CRMdig Mapping\n\n"
        "This directory contains a lightweight JSON-LD mapping proposal from Base Modifier Cache records to CIDOC CRM / CRMdig concepts.\n\n"
        "Status: mapping proposal only. It maps the source artifact, digital BMC object, annotation/assignment activity, actor, and BMC records, but it has not been validated by a CIDOC CRM or cultural-heritage ontology expert.\n",
        encoding="utf-8",
    )
    return {"mapped_records": len(rows), "path": str(OUT_PATH)}


if __name__ == "__main__":
    print(json.dumps(export(), indent=2))
