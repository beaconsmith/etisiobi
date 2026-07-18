from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    required = [
        ROOT / "research" / "frontier" / "SOTA_RESEARCH_LAB_METHODS.md",
        ROOT / "research" / "frontier" / "FRONTIER_LAB_OPERATING_SYSTEM.md",
        ROOT / "research" / "frontier" / "nwagu_aneke" / "FRONTIER_LAB_STATUS.json",
        ROOT / "research" / "frontier" / "nwagu_aneke" / "FRONTIER_LAB_STATUS.md",
        ROOT / "research" / "frontier" / "nwagu_layer_promotion_benchmark" / "SPRINT.md",
        ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "nwagu_research_atlas.jsonl",
        ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "summary.json",
        ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "prior_art_verification" / "verification_manifest.json",
        ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "prior_art_verification" / "SELECTED_INFRASTRUCTURE_PRIOR_ART.md",
        ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "prior_art_verification" / "verified_sources.csv",
        ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "prior_art_verification" / "claim_boundaries.csv",
        ROOT / "experiments" / "EXP-FRONTIER-007-inspect-ai-lpe-port" / "execution_gate" / "review" / "review_manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-007-inspect-ai-lpe-port" / "execution_gate" / "review" / "EXECUTION_GATE_REVIEW.md",
        ROOT / "experiments" / "EXP-FRONTIER-009-mlagentbench-keep-reject-loop" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-009-mlagentbench-keep-reject-loop" / "KEEP_REJECT_LOOP_DESIGN.md",
        ROOT / "experiments" / "EXP-FRONTIER-009-mlagentbench-keep-reject-loop" / "task_cards.csv",
        ROOT / "experiments" / "EXP-FRONTIER-009-mlagentbench-keep-reject-loop" / "decision_schema.json",
        ROOT / "experiments" / "EXP-FRONTIER-009-mlagentbench-keep-reject-loop" / "negative_control.md",
        ROOT / "experiments" / "EXP-FRONTIER-010-datalad-no-conversion-decision" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-010-datalad-no-conversion-decision" / "NO_CONVERSION_DECISION.md",
        ROOT / "experiments" / "EXP-FRONTIER-010-datalad-no-conversion-decision" / "conversion_blockers.csv",
        ROOT / "experiments" / "EXP-FRONTIER-010-datalad-no-conversion-decision" / "future_readiness_checklist.json",
        ROOT / "experiments" / "EXP-FRONTIER-011-software-heritage-no-identifier-decision" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-011-software-heritage-no-identifier-decision" / "NO_ARCHIVE_IDENTIFIER_DECISION.md",
        ROOT / "experiments" / "EXP-FRONTIER-011-software-heritage-no-identifier-decision" / "archive_blockers.csv",
        ROOT / "experiments" / "EXP-FRONTIER-011-software-heritage-no-identifier-decision" / "future_readiness_checklist.json",
        ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review" / "REPOSITORY_BOUNDARY_REVIEW.md",
        ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review" / "repository_asset_inventory.csv",
        ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review" / "excluded_repository_paths.csv",
        ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review" / "future_public_package_checklist.json",
        ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review" / "reviewer_questions.csv",
        ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake" / "REVIEWER_ASSIGNMENT_INTAKE.md",
        ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake" / "reviewer_assignment_tracker.csv",
        ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake" / "candidate_adjudication_matrix.csv",
        ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake" / "conflict_of_interest_checklist.json",
        ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake" / "decision_record_template.json",
        ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder" / "SAFE_ROLE_ASSIGNMENT_RECORDER.md",
        ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder" / "approved_role_assignment_schema.json",
        ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder" / "approved_role_assignment_template.json",
        ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder" / "redaction_rules.csv",
        ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder" / "approved_role_assignments.jsonl",
        ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "HUNDRED_PAPER_RECOVERY_INTAKE.md",
        ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "research_seeds.csv",
        ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "research_seed_schema.json",
        ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "claim_gate_matrix.csv",
        ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "sprint_selection.json",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "SELECTED_SEED_ARTIFACT_SPRINT.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifact_index.csv",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "approval_record.json",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-001-source-acquisition-decision-note.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-009-authority-role-map.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-017-reader-response-protocol.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-025-logograph-uncertainty-ledger.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-033-unicode-gap-map.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-041-modifier-operation-sketch.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-049-lpe-label-quality-audit.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-057-ro-crate-boundary-audit.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-065-layered-explainer-storyboard.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-073-layer-lineage-card.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-081-cross-domain-transfer-grid.md",
        ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "artifacts" / "NWR-089-portfolio-acceleration-dashboard-spec.md",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "LPE_LABEL_QUALITY_GATE.md",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "label_quality_gate_schema.json",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "quality_gate_matrix.csv",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "pilot_sample.csv",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "pilot_results.json",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "failure_cases.md",
        ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "paper_pathway.md",
        ROOT / "experiments" / "EXP-FRONTIER-006-nwagu-transfer-atlas" / "results.json",
        ROOT / "experiments" / "EXP-FRONTIER-001-layer-promotion-benchmark" / "results.json",
        ROOT / "experiments" / "EXP-FRONTIER-002-layer-promotion-expanded" / "results.json",
        ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation" / "pilot_results.json",
        ROOT / "experiments" / "EXP-FRONTIER-004-unicode-channel-risk-audit" / "results.json",
        ROOT / "experiments" / "EXP-FRONTIER-004-unicode-channel-risk-audit" / "analysis.md",
        ROOT / "experiments" / "EXP-FRONTIER-004-unicode-channel-risk-audit" / "decision.md",
        ROOT / "instruments" / "lpe_bench" / "manifest.json",
        ROOT / "instruments" / "lpe_bench" / "README.md",
        ROOT / "instruments" / "lpe_bench" / "VALIDATION.md",
        ROOT / "instruments" / "lpe_bench" / "BENCHMARK_CARD.md",
        ROOT / "instruments" / "lpe_bench" / "NEXT_EXPERIMENT.md",
        ROOT / "instruments" / "lpe_bench" / "leaderboard_internal.json",
        ROOT / "instruments" / "lpe_bench" / "demo.html",
        ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "plan.md",
        ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "manifest.json",
        ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "scores.json",
        ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "ANNOTATION_PROTOCOL.md",
        ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "AGENT_RUN_PROTOCOL.md",
        ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "gold_labels_template.csv",
        ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "agent_prompts" / "manifest.json",
        ROOT / "benchmarks" / "layer_promotion_error" / "scoreboard.json",
        ROOT / "benchmarks" / "layer_promotion_error" / "expanded_scoreboard.json",
        ROOT / "security" / "unicode_channel_audit" / "unicode_channel_audit.json",
        ROOT / "security" / "unicode_channel_audit" / "unicode_channel_findings.json",
        ROOT / "security" / "unicode_channel_audit" / "UNICODE_CHANNEL_AUDIT.md",
        ROOT / "scripts" / "validate_nwagu_frontier_lab_status.py",
        ROOT / "scripts" / "validate_nwagu_prior_art_verification_packet.py",
        ROOT / "scripts" / "validate_inspect_execution_gate_review.py",
        ROOT / "scripts" / "validate_mlagentbench_keep_reject_design.py",
        ROOT / "scripts" / "validate_datalad_no_conversion_decision.py",
        ROOT / "scripts" / "validate_software_heritage_no_identifier_decision.py",
        ROOT / "scripts" / "validate_repository_boundary_review.py",
        ROOT / "scripts" / "validate_repository_reviewer_assignment_intake.py",
        ROOT / "scripts" / "validate_safe_role_assignment_recorder.py",
        ROOT / "scripts" / "validate_hundred_paper_recovery_intake.py",
        ROOT / "scripts" / "validate_selected_seed_artifact_sprint.py",
        ROOT / "scripts" / "validate_lpe_label_quality_gate.py",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        results = read_json(ROOT / "experiments" / "EXP-FRONTIER-001-layer-promotion-benchmark" / "results.json")
        if results.get("status") != "FRONTIER_BENCHMARK_SEEDED_NOT_PAPER_READY":
            errors.append("frontier benchmark must be explicitly marked seeded and not paper-ready")
        if results.get("case_count", 0) < 30:
            errors.append("frontier benchmark must seed at least 30 cases")
        metrics = results.get("metrics", {})
        if metrics.get("precision", 0) < 0.8 or metrics.get("recall", 0) < 0.8:
            errors.append("frontier benchmark baseline must report precision and recall >= 0.8 on the seed set")
        if "Layer Promotion Error" not in results.get("research_claim", ""):
            errors.append("frontier result must name Layer Promotion Error as the research object")
        if "not yet" not in results.get("current_limit", "").lower():
            errors.append("frontier result must state current limit; no premature paper-readiness")

        atlas_summary = read_json(ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "summary.json")
        if atlas_summary.get("status") != "NWAGU_TRANSFER_ATLAS_SEEDED_NOT_PRIOR_ART_VERIFIED":
            errors.append("Nwagụ transfer atlas must be seeded but not prior-art verified")
        if atlas_summary.get("record_count", 0) < 40:
            errors.append("Nwagụ transfer atlas must include at least 40 transfer records")
        if atlas_summary.get("frontier_claim_status") != "not_ready":
            errors.append("Nwagụ transfer atlas must not claim frontier readiness")
        exp006 = read_json(ROOT / "experiments" / "EXP-FRONTIER-006-nwagu-transfer-atlas" / "results.json")
        if exp006.get("status") != "NWAGU_TRANSFER_ATLAS_SEEDED_NOT_PRIOR_ART_VERIFIED":
            errors.append("EXP-FRONTIER-006 must remain not prior-art verified")
        prior_art_packet = read_json(ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "prior_art_verification" / "verification_manifest.json")
        if prior_art_packet.get("status") != "selected_primary_source_relevance_verified_not_novelty_clearance":
            errors.append("selected prior-art packet must verify relevance without novelty clearance")
        if prior_art_packet.get("whole_atlas_prior_art_status") != "not_verified":
            errors.append("selected prior-art packet must keep the whole atlas not verified")
        if prior_art_packet.get("claim_ceiling") != "prior_art_relevance_not_frontier_claim":
            errors.append("selected prior-art packet must stay below frontier claim")
        inspect_review = read_json(ROOT / "experiments" / "EXP-FRONTIER-007-inspect-ai-lpe-port" / "execution_gate" / "review" / "review_manifest.json")
        if inspect_review.get("review_status") != "reviewed_keep_pending_do_not_execute":
            errors.append("Inspect execution gate review must keep execution blocked")
        if inspect_review.get("decision_status_after_review") != "pending_user_approval":
            errors.append("Inspect execution decision must remain pending after review")
        if inspect_review.get("dependencies_installed") is not False or inspect_review.get("model_or_api_run") is not False:
            errors.append("Inspect execution gate review must not install dependencies or run models/APIs")
        if inspect_review.get("claim_ceiling") != "eval_harness_relevance_not_model_claim":
            errors.append("Inspect execution gate review must preserve the eval harness claim ceiling")

        mlagentbench_design = read_json(ROOT / "experiments" / "EXP-FRONTIER-009-mlagentbench-keep-reject-loop" / "manifest.json")
        if mlagentbench_design.get("status") != "MLAGENTBENCH_KEEP_REJECT_DESIGN_READY_NO_AGENT_RUN":
            errors.append("MLAgentBench design must remain no-run design-ready")
        if mlagentbench_design.get("agents_run") is not False or mlagentbench_design.get("model_or_api_run") is not False:
            errors.append("MLAgentBench design must not run agents or models/APIs")
        if mlagentbench_design.get("dependencies_installed") is not False:
            errors.append("MLAgentBench design must not install dependencies")
        if mlagentbench_design.get("claim_ceiling") != "agent_evaluation_design_not_research_result":
            errors.append("MLAgentBench design must stay below research-result claims")
        if mlagentbench_design.get("task_card_count", 0) < 4:
            errors.append("MLAgentBench design must include at least four task cards")

        datalad_decision = read_json(ROOT / "experiments" / "EXP-FRONTIER-010-datalad-no-conversion-decision" / "manifest.json")
        if datalad_decision.get("status") != "DATALAD_NO_CONVERSION_DECISION_READY_NOT_EXECUTED":
            errors.append("DataLad decision must remain no-conversion ready and not executed")
        if datalad_decision.get("decision") != "defer_conversion_until_boundary_and_authority_gates":
            errors.append("DataLad decision must defer conversion until boundary and authority gates")
        if datalad_decision.get("claim_ceiling") != "reproducibility_planning_not_dataset_conversion":
            errors.append("DataLad decision must stay below dataset-conversion claims")
        for field in ["dependencies_installed", "datalad_installed", "datalad_command_run", "dataset_created", "private_data_downloaded", "public_release_claimed"]:
            if datalad_decision.get(field) is not False:
                errors.append(f"DataLad decision field must be false: {field}")
        if datalad_decision.get("external_actions_taken") != []:
            errors.append("DataLad decision must record no external actions")

        software_heritage_decision = read_json(ROOT / "experiments" / "EXP-FRONTIER-011-software-heritage-no-identifier-decision" / "manifest.json")
        if software_heritage_decision.get("status") != "SOFTWARE_HERITAGE_NO_IDENTIFIER_DECISION_READY_NOT_EXECUTED":
            errors.append("Software Heritage decision must remain no-identifier ready and not executed")
        if software_heritage_decision.get("decision") != "defer_archive_identifier_until_release_and_archive_gates":
            errors.append("Software Heritage decision must defer archive identifier work")
        if software_heritage_decision.get("claim_ceiling") != "software_provenance_planning_not_archive_action":
            errors.append("Software Heritage decision must stay below archive-action claims")
        for field in ["dependencies_installed", "software_heritage_request_made", "save_code_now_requested", "archive_identifier_claimed", "archive_identifier_assigned", "repository_deposited", "private_data_downloaded", "public_release_claimed"]:
            if software_heritage_decision.get(field) is not False:
                errors.append(f"Software Heritage decision field must be false: {field}")
        if software_heritage_decision.get("external_actions_taken") != []:
            errors.append("Software Heritage decision must record no external actions")

        repository_boundary = read_json(ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review" / "manifest.json")
        if repository_boundary.get("status") != "REPOSITORY_BOUNDARY_REVIEW_OPEN_NOT_APPROVED":
            errors.append("Repository-boundary review must be open but not approved")
        if repository_boundary.get("decision") != "open_repository_boundary_review_without_release_or_archive_action":
            errors.append("Repository-boundary review must not create release or archive action")
        if repository_boundary.get("claim_ceiling") != "repository_boundary_review_not_public_release":
            errors.append("Repository-boundary review must stay below public-release claims")
        if repository_boundary.get("candidate_inventory_status") != "draft_internal_candidates_only":
            errors.append("Repository-boundary inventory must remain internal draft candidates")
        for field in ["dependencies_installed", "private_data_downloaded", "repository_export_created", "software_heritage_request_made", "archive_identifier_claimed", "repository_deposited", "public_release_claimed", "public_package_approved"]:
            if repository_boundary.get(field) is not False:
                errors.append(f"Repository-boundary review field must be false: {field}")
        if repository_boundary.get("external_actions_taken") != []:
            errors.append("Repository-boundary review must record no external actions")

        reviewer_intake = read_json(ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake" / "manifest.json")
        if reviewer_intake.get("status") != "REPOSITORY_REVIEWER_ASSIGNMENT_INTAKE_READY_NO_ASSIGNMENTS":
            errors.append("Repository reviewer intake must be ready with no assignments")
        if reviewer_intake.get("decision") != "prepare_assignment_and_adjudication_intake_without_contact_or_approval":
            errors.append("Repository reviewer intake must not record contact or approval")
        if reviewer_intake.get("claim_ceiling") != "reviewer_assignment_intake_not_review_completion":
            errors.append("Repository reviewer intake must stay below review-completion claims")
        for field in ["dependencies_installed", "reviewer_identities_recorded", "private_contact_data_recorded", "invitations_sent", "reviews_collected", "adjudication_completed", "public_package_approved", "public_release_claimed", "software_heritage_request_made", "archive_identifier_claimed"]:
            if reviewer_intake.get(field) is not False:
                errors.append(f"Repository reviewer intake field must be false: {field}")
        if reviewer_intake.get("external_actions_taken") != []:
            errors.append("Repository reviewer intake must record no external actions")

        assignment_recorder = read_json(ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder" / "manifest.json")
        if assignment_recorder.get("status") != "SAFE_ROLE_ASSIGNMENT_RECORDER_READY_NO_ASSIGNMENTS_RECORDED":
            errors.append("Safe role assignment recorder must be ready with no assignments recorded")
        if assignment_recorder.get("decision") != "prepare_safe_assignment_recording_without_identity_or_contact_data":
            errors.append("Safe role assignment recorder must not record identity or contact data")
        if assignment_recorder.get("claim_ceiling") != "safe_role_assignment_recorder_not_assignment_completion":
            errors.append("Safe role assignment recorder must stay below assignment-completion claims")
        for field in ["dependencies_installed", "reviewer_identities_recorded", "private_contact_data_recorded", "approved_assignments_recorded", "invitations_sent", "reviews_collected", "adjudication_completed", "public_package_approved", "public_release_claimed", "software_heritage_request_made", "archive_identifier_claimed"]:
            if assignment_recorder.get(field) is not False:
                errors.append(f"Safe role assignment recorder field must be false: {field}")
        if assignment_recorder.get("external_actions_taken") != []:
            errors.append("Safe role assignment recorder must record no external actions")

        recovery_intake = read_json(ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "manifest.json")
        if recovery_intake.get("status") != "HUNDRED_PAPER_RECOVERY_INTAKE_READY_SEEDS_ONLY":
            errors.append("Hundred-paper recovery intake must remain seed-only")
        if recovery_intake.get("decision") != "seed_100_research_questions_without_paper_or_readiness_claims":
            errors.append("Hundred-paper recovery intake must avoid paper or readiness claims")
        if recovery_intake.get("claim_ceiling") != "research_intake_not_paper_pipeline_completion":
            errors.append("Hundred-paper recovery intake must stay below pipeline-completion claims")
        if recovery_intake.get("paper_count_target") != 100 or recovery_intake.get("seed_count") != 100:
            errors.append("Hundred-paper recovery intake must maintain 100 target seeds and 100 actual seeds")
        for field in ["dependencies_installed", "papers_generated", "manuscripts_generated", "publication_pdf_generated", "private_data_downloaded", "human_review_completed", "rights_or_authority_cleared", "public_release_claimed"]:
            if recovery_intake.get(field) is not False:
                errors.append(f"Hundred-paper recovery intake field must be false: {field}")
        if recovery_intake.get("external_actions_taken") != []:
            errors.append("Hundred-paper recovery intake must record no external actions")

        selected_seed_sprint = read_json(ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint" / "manifest.json")
        if selected_seed_sprint.get("status") != "SELECTED_SEED_ARTIFACTS_READY_INTERNAL_ONLY":
            errors.append("Selected seed artifact sprint must remain internal only")
        if selected_seed_sprint.get("decision") != "create_bounded_artifacts_from_approved_seed_selection_without_maturity_claims":
            errors.append("Selected seed artifact sprint must avoid maturity claims")
        if selected_seed_sprint.get("claim_ceiling") != "selected_seed_artifacts_not_paper_candidates":
            errors.append("Selected seed artifact sprint must stay below paper-candidate claims")
        if selected_seed_sprint.get("selected_seed_count") != 12 or selected_seed_sprint.get("artifact_count") != 12:
            errors.append("Selected seed artifact sprint must record 12 selected seeds and 12 artifacts")
        if selected_seed_sprint.get("lab_execution_approval_recorded") is not True:
            errors.append("Selected seed artifact sprint must record internal lab execution approval")
        for field in ["dependencies_installed", "papers_generated", "manuscripts_generated", "publication_pdf_generated", "private_data_downloaded", "external_submission_made", "rights_or_authority_cleared", "human_reviewer_identity_recorded", "public_release_claimed"]:
            if selected_seed_sprint.get(field) is not False:
                errors.append(f"Selected seed artifact sprint field must be false: {field}")
        if selected_seed_sprint.get("external_actions_taken") != []:
            errors.append("Selected seed artifact sprint must record no external actions")

        lpe_quality_gate = read_json(ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "manifest.json")
        if lpe_quality_gate.get("status") != "LPE_LABEL_QUALITY_GATE_PILOT_INTERNAL_NOT_FRONTIER_RESULT":
            errors.append("LPE label quality gate must remain internal and not frontier result")
        if lpe_quality_gate.get("decision") != "promote_nwr_049_into_branch_specific_quality_gate_pilot":
            errors.append("LPE label quality gate must promote NWR-049 into a branch-specific pilot")
        if lpe_quality_gate.get("claim_ceiling") != "quality_gate_pilot_not_paper_result":
            errors.append("LPE label quality gate must stay below paper-result claims")
        if lpe_quality_gate.get("sample_case_count") != 24 or lpe_quality_gate.get("source_gold_label_count") != 360:
            errors.append("LPE label quality gate must record 24 pilot cases from 360 source labels")
        for field in ["dependencies_installed", "model_or_api_run", "new_agent_run", "human_domain_review_completed", "rights_or_authority_cleared", "publication_pdf_generated", "external_submission_made", "public_release_claimed"]:
            if lpe_quality_gate.get(field) is not False:
                errors.append(f"LPE label quality gate field must be false: {field}")
        if lpe_quality_gate.get("external_actions_taken") != []:
            errors.append("LPE label quality gate must record no external actions")

        status_surface = read_json(ROOT / "research" / "frontier" / "nwagu_aneke" / "FRONTIER_LAB_STATUS.json")
        if status_surface.get("status_id") != "NWAGU-FRONTIER-LAB-STATUS-001":
            errors.append("Nwagu frontier lab status surface must use the canonical status_id")
        if status_surface.get("promotion_state") != "not_ready":
            errors.append("Nwagu frontier lab status surface must remain not_ready")
        if len(status_surface.get("lanes", [])) < 12:
            errors.append("Nwagu frontier lab status surface must cover all 12 lanes")
        if status_surface.get("claim_ceiling") != "status_surface_not_research_result":
            errors.append("Nwagu frontier lab status surface must not present itself as a research result")

        expanded = read_json(ROOT / "experiments" / "EXP-FRONTIER-002-layer-promotion-expanded" / "results.json")
        if expanded.get("status") != "EXPANDED_BENCHMARK_INTERNAL_NOT_FRONTIER_PROOF":
            errors.append("expanded LPE benchmark must be marked internal and not frontier proof")
        if expanded.get("case_count", 0) < 300:
            errors.append("expanded LPE benchmark must include at least 300 cases")
        source_counts = expanded.get("source_type_counts", {})
        external_or_cross = source_counts.get("external_prior_art_control", 0) + source_counts.get("cross_program", 0)
        if external_or_cross / max(1, expanded.get("case_count", 1)) < 0.30:
            errors.append("expanded LPE benchmark must include at least 30% external or cross-program cases")
        best = expanded.get("best_test_baseline", {})
        if not best.get("baseline"):
            errors.append("expanded LPE benchmark must report a best held-out test baseline")
        if expanded.get("frontier_claim_status") != "not_ready":
            errors.append("expanded LPE benchmark must not claim frontier readiness")
        if "heuristic" not in expanded.get("current_limit", "").lower():
            errors.append("expanded LPE benchmark must disclose heuristic labels")

        exp003 = read_json(ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation" / "manifest.json")
        if exp003.get("status") != "BLIND_ANNOTATION_PACKET_READY_UNLABELED":
            errors.append("EXP-FRONTIER-003 must be an unlabeled blind annotation packet")
        if exp003.get("case_count", 0) < 300:
            errors.append("EXP-FRONTIER-003 annotation packet must contain at least 300 cases")
        if exp003.get("labels_frozen") is not False:
            errors.append("EXP-FRONTIER-003 labels must remain unfrozen until independent annotation is complete")
        if exp003.get("frontier_claim_status") != "not_ready":
            errors.append("EXP-FRONTIER-003 must not claim frontier readiness before blind labels")
        exp003_counts = exp003.get("source_type_counts", {})
        if exp003_counts.get("real_agent_output", 0) < 100:
            errors.append("EXP-FRONTIER-003 must include at least 100 real agent/research output cases")
        exp003_external_cross = exp003_counts.get("cross_program", 0) + exp003_counts.get("external_prior_art_control", 0)
        if exp003_external_cross / max(1, exp003.get("case_count", 1)) < 0.30:
            errors.append("EXP-FRONTIER-003 must include at least 30% external or cross-program cases")

        pilot = read_json(ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation" / "pilot_results.json")
        if pilot.get("status") != "SYNTHETIC_PILOT_LABELS_CREATED_NOT_HUMAN_REVIEW":
            errors.append("EXP-FRONTIER-003 pilot must be explicitly synthetic and not human review")
        if pilot.get("case_count") != exp003.get("case_count"):
            errors.append("EXP-FRONTIER-003 pilot must annotate the full queue")
        if pilot.get("reviewer_count", 0) < 3:
            errors.append("EXP-FRONTIER-003 pilot must simulate at least three reviewer profiles")
        if pilot.get("frontier_claim_status") != "not_ready":
            errors.append("EXP-FRONTIER-003 pilot must not claim frontier readiness")
        if "cannot replace" not in pilot.get("current_limit", "").lower():
            errors.append("EXP-FRONTIER-003 pilot must state synthetic labels cannot replace human/domain annotation")

        exp005 = read_json(ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "manifest.json")
        if exp005.get("status") != "ANNOTATION_AND_AGENT_RUN_TEMPLATES_READY_NOT_SCORED":
            errors.append("EXP-FRONTIER-005 must have ready templates but remain unscored until gold labels and agent runs exist")
        if exp005.get("case_count") != exp003.get("case_count"):
            errors.append("EXP-FRONTIER-005 frozen queue must match EXP-FRONTIER-003 queue size")
        if exp005.get("frontier_claim_status") != "not_ready":
            errors.append("EXP-FRONTIER-005 must not claim frontier readiness")
        exp005_scores = read_json(ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval" / "scores.json")
        if exp005_scores.get("status") not in {"NOT_SCORED_MISSING_GOLD_OR_AGENT_RUNS", "SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM"}:
            errors.append("EXP-FRONTIER-005 scores must use an approved non-frontier status")
        if exp005_scores.get("frontier_claim_status") != "not_ready":
            errors.append("EXP-FRONTIER-005 scores must not claim frontier readiness")

        unicode_audit = read_json(ROOT / "security" / "unicode_channel_audit" / "unicode_channel_audit.json")
        if unicode_audit.get("status") != "UNICODE_CHANNEL_AUDIT_COMPLETE":
            errors.append("Unicode channel audit must complete before frontier lab validation")
        if unicode_audit.get("files_scanned", 0) < 100:
            errors.append("Unicode channel audit must scan frontier/publication-facing text outputs")
        interpretation = unicode_audit.get("defensive_interpretation", "").lower()
        if "not proof of covert-channel use" not in interpretation:
            errors.append("Unicode channel audit must frame findings defensively, not as covert-channel proof")
        if unicode_audit.get("non_utf8_text_files", 0) > 0 and "portability" not in interpretation:
            errors.append("Unicode channel audit must classify non-UTF-8 text as a portability risk")
        exp004 = read_json(ROOT / "experiments" / "EXP-FRONTIER-004-unicode-channel-risk-audit" / "results.json")
        if exp004.get("status") != "UNICODE_CHANNEL_AUDIT_COMPLETE_NOT_PUBLICATION_BLOCKING":
            errors.append("EXP-FRONTIER-004 must be complete without pretending to be a frontier proof")
        if "not proof of covert-channel use" not in exp004.get("interpretation", "").lower():
            errors.append("EXP-FRONTIER-004 interpretation must not overclaim covert-channel evidence")

        instrument = read_json(ROOT / "instruments" / "lpe_bench" / "manifest.json")
        if instrument.get("instrument_id") != "LPE-Bench":
            errors.append("frontier instrument must be named LPE-Bench")
        if instrument.get("status") != "PUBLIC_INSTRUMENT_DRAFT_NOT_FRONTIER_PROOF":
            errors.append("LPE-Bench must remain a public instrument draft until independent labels and real runs exist")
        if instrument.get("frontier_claim_status") != "not_ready":
            errors.append("LPE-Bench must not claim frontier readiness")
        if instrument.get("current_case_count", 0) < expanded.get("case_count", 0):
            errors.append("LPE-Bench manifest must include the expanded internal benchmark case count")
        if instrument.get("blind_annotation_queue_count", 0) < exp003.get("case_count", 0):
            errors.append("LPE-Bench manifest must include the blind annotation queue count")
        blockers = set(instrument.get("blocking_gates", []))
        for blocker in ("independent human/domain annotation", "real agent/model runs", "rights/authority review for public examples"):
            if blocker not in blockers:
                errors.append(f"LPE-Bench manifest missing blocker: {blocker}")

        trace = ROOT / "research" / "frontier" / "nwagu_layer_promotion_benchmark" / "review_team_trace.jsonl"
        if not trace.exists():
            errors.append("frontier sprint must record research-team review trace")
        else:
            rows = [json.loads(line) for line in trace.read_text(encoding="utf-8").splitlines() if line.strip()]
            roles = {row.get("role"): row for row in rows}
            for role in ("sota_scout", "methods_reviewer", "adversarial_impact_reviewer"):
                if role not in roles:
                    errors.append(f"frontier review trace missing {role}")
                elif roles[role].get("status") != "KEEP_AS_FRONTIER_SPRINT_NOT_PAPER_READY":
                    errors.append(f"{role} must keep sprint but block paper readiness")

    if errors:
        print("FRONTIER_LAB_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1
    print("FRONTIER_LAB_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
