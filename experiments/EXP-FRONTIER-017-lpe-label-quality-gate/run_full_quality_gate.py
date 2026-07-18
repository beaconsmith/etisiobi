import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate"
SOURCE_DIR = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"

GOLD_LABELS = SOURCE_DIR / "gold_labels.csv"
SCORES = SOURCE_DIR / "scores.json"
AGREEMENT = SOURCE_DIR / "annotation_agreement.json"
FULL_TABLE = EXP_DIR / "full_quality_gate.csv"
RESULTS = EXP_DIR / "full_quality_gate_results.json"
ALIGNMENT = EXP_DIR / "score_gate_alignment.json"
REPORT = EXP_DIR / "full_quality_gate_report.md"
REVIEW_PACKET = EXP_DIR / "human_domain_review_packet.csv"
REVIEW_PACKET_MD = EXP_DIR / "human_domain_review_packet.md"

FIELDNAMES = [
    "case_id",
    "input_layer",
    "output_layer",
    "promotion_error",
    "severity",
    "source_review_status",
    "public_release_ok",
    "evidence_anchor_check",
    "layer_contrast_check",
    "disagreement_state_check",
    "adjudication_need_check",
    "quality_gate_status",
]


def read_csv(path):
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def route_row(row):
    evidence_anchor = "pass" if row.get("case_id") and row.get("source_review_status") else "fail"
    layer_contrast = "pass" if row.get("input_layer") and row.get("output_layer") else "fail"
    disagreement = "pass" if row.get("source_review_status") == "reviewed_by_three_roles" else "needs_review"

    promotion_error = row.get("promotion_error") == "yes"
    severity = row.get("severity", "none")
    input_layer = row.get("input_layer", "")
    output_layer = row.get("output_layer", "")

    if severity == "blocking" or input_layer == "blocked" or output_layer == "blocked":
        adjudication = "needs_rights_or_blocker_review"
        status = "blocked_public_release"
    elif promotion_error:
        adjudication = "needs_layer_review"
        status = "needs_adjudication"
    else:
        adjudication = "pass"
        status = "review_ready_internal"

    if evidence_anchor != "pass" or layer_contrast != "pass":
        status = "needs_adjudication"

    return {
        "case_id": row["case_id"],
        "input_layer": row["input_layer"],
        "output_layer": row["output_layer"],
        "promotion_error": row["promotion_error"],
        "severity": row["severity"],
        "source_review_status": row["source_review_status"],
        "public_release_ok": row["public_release_ok"],
        "evidence_anchor_check": evidence_anchor,
        "layer_contrast_check": layer_contrast,
        "disagreement_state_check": disagreement,
        "adjudication_need_check": adjudication,
        "quality_gate_status": status,
    }


def write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def write_review_packet(gold_rows, routed_rows):
    gold_by_id = {row["case_id"]: row for row in gold_rows}
    packet_rows = []
    for row in routed_rows:
        if row["quality_gate_status"] == "review_ready_internal":
            continue
        source = gold_by_id[row["case_id"]]
        if row["quality_gate_status"] == "blocked_public_release":
            question = "Does this row require rights, authority, or public-scope blocking before paper use?"
        else:
            question = "Is the layer-promotion label correct, and what adjudication note is needed?"
        packet_rows.append(
            {
                "case_id": row["case_id"],
                "claim_text": source["claim_text"],
                "input_layer": row["input_layer"],
                "output_layer": row["output_layer"],
                "promotion_error": row["promotion_error"],
                "severity": row["severity"],
                "quality_gate_status": row["quality_gate_status"],
                "review_question": question,
                "human_domain_decision": "",
                "reviewer_notes": "",
            }
        )

    fieldnames = [
        "case_id",
        "claim_text",
        "input_layer",
        "output_layer",
        "promotion_error",
        "severity",
        "quality_gate_status",
        "review_question",
        "human_domain_decision",
        "reviewer_notes",
    ]
    with REVIEW_PACKET.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(packet_rows)

    REVIEW_PACKET_MD.write_text(
        "\n".join(
            [
                "# Human/Domain Review Packet",
                "",
                "Status: `HUMAN_DOMAIN_REVIEW_PACKET_READY_NOT_REVIEWED`",
                "",
                f"Rows requiring review: `{len(packet_rows)}`",
                "",
                "This packet contains only full-gate rows that require adjudication or public-release blocking review. It is not a completed review trace, source authority clearance, rights clearance, or submission decision.",
                "",
                "## Reviewer Instruction",
                "",
                "For each row, fill `human_domain_decision` with one of `confirm_label`, `revise_label`, `block_public_use`, or `needs_more_evidence`, then add reviewer notes. Do not convert this packet into paper readiness without the repo review-team gate.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return packet_rows


def build_alignment(scores, status_counts):
    metric_rows = scores["metric_rows"]
    best = scores["best_overall"]
    return {
        "status": "SCORE_GATE_ALIGNMENT_INTERNAL_NOT_FRONTIER_RESULT",
        "best_overall_condition": best["condition"],
        "best_overall_agent_id": best["agent_id"],
        "best_overall_f1": best["f1"],
        "condition_count": len(metric_rows),
        "status_counts": dict(status_counts),
        "condition_metrics": [
            {
                "condition": row["condition"],
                "agent_id": row["agent_id"],
                "f1": row["f1"],
                "precision": row["precision"],
                "recall": row["recall"],
                "source_observed_false_assertion_rate": row["source_observed_false_assertion_rate"],
                "derived_layer_preservation_rate": row["derived_layer_preservation_rate"],
            }
            for row in metric_rows
        ],
        "interpretation": (
            "Quality routing now covers the full local label set, but score "
            "comparison remains internal because human/domain review and rights "
            "review are not complete."
        ),
    }


def main():
    gold = read_csv(GOLD_LABELS)
    scores = read_json(SCORES)
    agreement = read_json(AGREEMENT)

    routed = [route_row(row) for row in gold]
    write_csv(FULL_TABLE, routed)
    packet_rows = write_review_packet(gold, routed)

    status_counts = Counter(row["quality_gate_status"] for row in routed)
    severity_counts = Counter(row["severity"] for row in routed)
    alignment = build_alignment(scores, status_counts)
    ALIGNMENT.write_text(json.dumps(alignment, indent=2) + "\n", encoding="utf-8")

    result = {
        "experiment_id": "EXP-FRONTIER-017",
        "status": "FULL_LABEL_QUALITY_GATE_COMPLETE_INTERNAL_NOT_SUBMISSION_READY",
        "claim_ceiling": "full_quality_gate_internal_not_paper_result",
        "full_case_count": len(routed),
        "source_gold_label_count": agreement["case_count"],
        "review_ready_internal_count": status_counts["review_ready_internal"],
        "needs_adjudication_count": status_counts["needs_adjudication"],
        "blocked_public_release_count": status_counts["blocked_public_release"],
        "human_domain_review_packet_rows": len(packet_rows),
        "severity_counts": dict(severity_counts),
        "compared_agent_condition_count": len(scores["metric_rows"]),
        "best_overall_condition": scores["best_overall"]["condition"],
        "best_overall_f1": scores["best_overall"]["f1"],
        "paper_claim_status": "not_ready",
        "frontier_claim_status": "not_ready",
        "public_release_status": "blocked",
        "human_domain_review_status": agreement["human_domain_review_status"],
        "rights_or_authority_cleared": False,
        "external_actions_taken": [],
        "remaining_gates": [
            "independent human/domain review",
            "rights and authority review",
            "review-team trace for any paper candidate",
            "venue-specific manuscript and package gate",
        ],
        "next_action": (
            "Route the full-gate blocked and adjudication rows into a human/domain "
            "review packet before any paper-candidate or journal-submission decision."
        ),
    }
    RESULTS.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    REPORT.write_text(
        "\n".join(
            [
                "# Full LPE Label Quality Gate Report",
                "",
                "Status: `FULL_LABEL_QUALITY_GATE_COMPLETE_INTERNAL_NOT_SUBMISSION_READY`",
                "",
                f"Full cases routed: `{len(routed)}`",
                f"Review-ready internal rows: `{status_counts['review_ready_internal']}`",
                f"Needs adjudication rows: `{status_counts['needs_adjudication']}`",
                f"Blocked public-release rows: `{status_counts['blocked_public_release']}`",
                f"Human/domain review packet rows: `{len(packet_rows)}`",
                f"Compared scored agent conditions: `{len(scores['metric_rows'])}`",
                "",
                "## Claim Ceiling",
                "",
                "`full_quality_gate_internal_not_paper_result`.",
                "",
                "This expands local label quality routing. It does not clear human/domain review, rights, authority, public release, or journal submission.",
                "",
                "## Next Action",
                "",
                "Route the blocked and adjudication rows into a human/domain review packet before any paper-candidate or journal-submission decision.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
