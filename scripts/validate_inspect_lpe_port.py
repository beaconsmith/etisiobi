from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-007-inspect-ai-lpe-port"
MANIFEST_PATH = EXP_DIR / "manifest.json"
PLAN_PATH = EXP_DIR / "plan.md"
CONTRACT_PATH = EXP_DIR / "inspect_adapter_contract.md"
README_PATH = EXP_DIR / "README.md"
SEED_CASES_PATH = EXP_DIR / "data" / "inspect_lpe_seed_cases.jsonl"
NEGATIVE_CONTROL_PATH = EXP_DIR / "data" / "manual_prompt_negative_control.jsonl"

REQUIRED_FILES = [
    MANIFEST_PATH,
    PLAN_PATH,
    CONTRACT_PATH,
    README_PATH,
    SEED_CASES_PATH,
    NEGATIVE_CONTROL_PATH,
]

REQUIRED_MANIFEST_FIELDS = {
    "experiment_id",
    "status",
    "atlas_id",
    "claim_ceiling",
    "dependency_policy",
    "case_count",
    "negative_control_count",
    "primary_sources",
    "blocking_gates",
    "exact_next_action",
}

REQUIRED_CASE_FIELDS = {
    "sample_id",
    "input",
    "target",
    "metadata",
}

REQUIRED_METADATA_FIELDS = {
    "case_family",
    "input_layer",
    "expected_output_layer",
    "gold_promotion_error",
    "source_path",
    "source_type",
    "split",
    "rights_risk",
}

PRIMARY_SOURCE_URLS = {
    "https://inspect.aisi.org.uk/",
    "https://github.com/UKGovernmentBEIS/inspect_ai",
    "https://www.aisi.gov.uk/blog/inspect-evals",
    "https://inspect.aisi.org.uk/tutorial.html",
}

FORBIDDEN_TEXT = [
    "benchmark result",
    "model result",
    "installed inspect",
    "pip install inspect-ai",
    "paper-ready",
    "submission-ready",
    "frontier-ready",
    "source-observed 27/216",
]


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        missing_manifest = sorted(REQUIRED_MANIFEST_FIELDS - manifest.keys())
        if missing_manifest:
            errors.append(f"manifest missing fields: {missing_manifest}")

        if manifest.get("experiment_id") != "EXP-FRONTIER-007":
            errors.append("manifest experiment_id must be EXP-FRONTIER-007")
        if manifest.get("atlas_id") != "ATLAS-0049":
            errors.append("manifest atlas_id must be ATLAS-0049")
        if manifest.get("status") != "INSPECT_LPE_PORT_PLAN_READY_NO_DEPENDENCY_INSTALL":
            errors.append("manifest status must remain plan-ready with no dependency install")
        if manifest.get("claim_ceiling") != "eval_harness_relevance_not_model_claim":
            errors.append("manifest claim ceiling must block model/result claims")
        if manifest.get("dependency_policy") != "no_install_in_continuous_loop":
            errors.append("manifest dependency policy must forbid install during this loop")

        sources = set(manifest.get("primary_sources", []))
        missing_sources = sorted(PRIMARY_SOURCE_URLS - sources)
        if missing_sources:
            errors.append(f"manifest missing primary sources: {missing_sources}")

        blockers = set(manifest.get("blocking_gates", []))
        for blocker in [
            "explicit dependency approval",
            "model/API key approval",
            "human/domain review of seed labels",
            "no private or restricted source data",
        ]:
            if blocker not in blockers:
                errors.append(f"manifest missing blocker: {blocker}")

        cases = load_jsonl(SEED_CASES_PATH)
        controls = load_jsonl(NEGATIVE_CONTROL_PATH)
        if manifest.get("case_count") != len(cases):
            errors.append("manifest case_count does not match seed case JSONL")
        if manifest.get("negative_control_count") != len(controls):
            errors.append("manifest negative_control_count does not match control JSONL")
        if len(cases) < 8:
            errors.append("Inspect LPE seed set must include at least 8 cases")
        if len(controls) < 2:
            errors.append("negative control must include at least 2 manual prompt cases")

        seen_ids: set[str] = set()
        split_counts: dict[str, int] = {}
        families: set[str] = set()
        promotion_values: set[bool] = set()
        for index, record in enumerate(cases, start=1):
            sample_id = str(record.get("sample_id", f"line {index}"))
            if sample_id in seen_ids:
                errors.append(f"{sample_id}: duplicate sample_id")
            seen_ids.add(sample_id)

            missing = sorted(REQUIRED_CASE_FIELDS - record.keys())
            if missing:
                errors.append(f"{sample_id}: missing fields {missing}")
                continue

            metadata = record.get("metadata")
            if not isinstance(metadata, dict):
                errors.append(f"{sample_id}: metadata must be an object")
                continue

            missing_metadata = sorted(REQUIRED_METADATA_FIELDS - metadata.keys())
            if missing_metadata:
                errors.append(f"{sample_id}: metadata missing fields {missing_metadata}")

            target = record.get("target")
            if not isinstance(target, dict):
                errors.append(f"{sample_id}: target must be an object")
            else:
                if target.get("expected_answer") not in {"promotion_error", "no_promotion_error"}:
                    errors.append(f"{sample_id}: target expected_answer invalid")
                if "scoring_rubric" not in target:
                    errors.append(f"{sample_id}: target missing scoring_rubric")

            split_counts[str(metadata.get("split", ""))] = split_counts.get(str(metadata.get("split", "")), 0) + 1
            families.add(str(metadata.get("case_family", "")))
            promotion = metadata.get("gold_promotion_error")
            if isinstance(promotion, bool):
                promotion_values.add(promotion)
            else:
                errors.append(f"{sample_id}: gold_promotion_error must be boolean")

            if metadata.get("source_type") == "restricted_private_data":
                errors.append(f"{sample_id}: restricted private data is not allowed")
            if metadata.get("rights_risk") not in {"low", "medium"}:
                errors.append(f"{sample_id}: rights_risk must be low or medium")

        for required_split in ["dev", "test"]:
            if split_counts.get(required_split, 0) == 0:
                errors.append(f"seed cases must include split {required_split}")
        for required_family in ["nwagu_count_layer", "speculation_boundary", "external_prior_art_control"]:
            if required_family not in families:
                errors.append(f"seed cases missing family {required_family}")
        if promotion_values != {False, True}:
            errors.append("seed cases must include both promotion and non-promotion labels")

        combined_text = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in [PLAN_PATH, CONTRACT_PATH, README_PATH]
        )
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined_text:
                errors.append(f"forbidden overclaim/install text: {forbidden}")

    if errors:
        print("INSPECT_LPE_PORT_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("INSPECT_LPE_PORT_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
