scan:
	python scripts/scan_repo.py

corpus:
	python scripts/build_corpus.py

goals:
	python scripts/generate_goals.py

obsidian:
	python scripts/build_obsidian_vault.py

validate:
	python scripts/validate_research_system.py
	python scripts/validate_lab_standard.py
	python scripts/validate_benchmark_integrity.py
	python scripts/validate_nwagu_prior_art_verification_packet.py
	python scripts/validate_nwagu_frontier_lab_status.py
	python scripts/validate_frontier_lab.py
	python scripts/validate_inspect_lpe_port.py
	python scripts/validate_inspect_execution_gate.py
	python scripts/validate_inspect_execution_gate_review.py
	python scripts/validate_mlagentbench_keep_reject_design.py
	python scripts/validate_datalad_no_conversion_decision.py
	python scripts/validate_software_heritage_no_identifier_decision.py
	python scripts/validate_repository_boundary_review.py
	python scripts/validate_repository_reviewer_assignment_intake.py
	python scripts/validate_safe_role_assignment_recorder.py
	python scripts/validate_hundred_paper_recovery_intake.py
	python scripts/validate_selected_seed_artifact_sprint.py
	python scripts/validate_lpe_label_quality_gate.py
	python scripts/validate_nwagu_frontier_ro_crate.py
	python scripts/validate_nwagu_preservation_decision.py
	python scripts/validate_nwagu_dataset_boundary.py
	python scripts/validate_nwagu_dataset_boundary_review_gate.py
	python scripts/validate_nwagu_dataset_boundary_review_intake.py
	python scripts/validate_nwagu_dataset_boundary_review_dispatch.py
	python scripts/validate_nwagu_dataset_boundary_contact_approval.py
	python scripts/validate_continuous_research_loop.py
	python scripts/validate_review_team_gate.py

loop:
	python scripts/research_loop.py --mode dry-run --max-iterations 1

paper:
	latexmk -pdf -interaction=nonstopmode -halt-on-error paper/main.tex || true

arxiv-check:
	python scripts/arxiv_check.py

events:
	python scripts/project_research_events.py
	python scripts/validate_research_events.py

control-plane:
	python scripts/project_research_events.py
	python scripts/validate_research_events.py
	python scripts/build_retrieval_manifest.py
	python scripts/validate_retrieval_manifest.py
	python scripts/validate_lab_standard.py
	python scripts/validate_frontier_lab.py
	python tests/research/test_lab_operating_standard.py
	python tests/research/test_frontier_lab.py
	python scripts/validate_nwagu_article_benchmark.py
	python tests/research/test_lab_quality_bar.py
	python tests/research/test_public_article_quality.py
	python scripts/validate_review_team_gate.py
	python tests/retrieval/test_stale_pagc_exclusion.py
	python tests/retrieval/test_research_event_trace.py
	python scripts/vendor_neutrality_audit.py

clean-generated:
	python scripts/clean_generated.py

paper-assets:
	python scripts/generate_paper_assets.py

phase5:
	python scripts/phase5_arxiv_ready.py

nwagu-experiments:
	python scripts/run_nwagu_article_experiments.py

nwagu-articles:
	python scripts/rewrite_nwagu_articles_from_benchmark.py
	python scripts/compile_nwagu_article_manuscripts.py

nwagu-benchmark:
	python scripts/run_nwagu_article_experiments.py
	python scripts/benchmark_nwagu_article_research.py
	python scripts/rewrite_nwagu_articles_from_benchmark.py
	python scripts/benchmark_nwagu_article_research.py
	python scripts/validate_nwagu_article_benchmark.py
	python tests/research/test_lab_quality_bar.py
	python scripts/compile_nwagu_article_manuscripts.py
	python tests/research/test_public_article_quality.py
	python scripts/validate_nwagu_article_manuscripts.py
	python scripts/validate_nwagu_article_impact_readiness.py

nwagu-pdfs:
	python scripts/compile_nwagu_article_manuscripts.py

frontier-benchmark:
	python scripts/build_nwagu_transfer_atlas.py
	python scripts/validate_nwagu_transfer_atlas.py
	python scripts/validate_nwagu_prior_art_verification_packet.py
	python scripts/run_frontier_layer_promotion_benchmark.py
	python scripts/run_frontier_lpe_benchmark_v2.py
	python scripts/prepare_frontier_lpe_exp003_annotation_packet.py
	python scripts/run_frontier_lpe_exp003_pilot.py
	python scripts/audit_unicode_channel_risk.py
	python scripts/build_lpe_bench_instrument.py
	python scripts/prepare_lpe_bench_exp005.py
	python scripts/prepare_lpe_agent_prompts_exp005.py
	python scripts/adjudicate_lpe_bench_exp005.py
	python scripts/run_lpe_bench_exp005_baselines.py
	python scripts/score_lpe_bench_exp005.py
	python scripts/validate_lpe_bench_instrument.py
	python scripts/validate_inspect_lpe_port.py
	python scripts/validate_inspect_execution_gate.py
	python scripts/validate_inspect_execution_gate_review.py
	python scripts/validate_mlagentbench_keep_reject_design.py
	python scripts/validate_datalad_no_conversion_decision.py
	python scripts/validate_software_heritage_no_identifier_decision.py
	python scripts/validate_repository_boundary_review.py
	python scripts/validate_repository_reviewer_assignment_intake.py
	python scripts/validate_safe_role_assignment_recorder.py
	python scripts/validate_hundred_paper_recovery_intake.py
	python scripts/validate_selected_seed_artifact_sprint.py
	python scripts/validate_lpe_label_quality_gate.py
	python scripts/validate_nwagu_frontier_ro_crate.py
	python scripts/validate_nwagu_preservation_decision.py
	python scripts/validate_nwagu_dataset_boundary.py
	python scripts/validate_nwagu_dataset_boundary_review_gate.py
	python scripts/validate_nwagu_dataset_boundary_review_intake.py
	python scripts/validate_nwagu_dataset_boundary_review_dispatch.py
	python scripts/validate_nwagu_dataset_boundary_contact_approval.py
	python scripts/validate_nwagu_frontier_lab_status.py
	python scripts/validate_frontier_lab.py
	python tests/research/test_frontier_lab.py

continuous-research:
	python scripts/continuous_research_loop.py --mode cycle --max-experiments 5
	python scripts/validate_continuous_research_loop.py

approved-papers-loop:
	python scripts/approved_papers_loop.py --max-active 2
	python scripts/validate_approved_papers_goal.py

nwagu-cycle2:
	python scripts/generate_nwagu_cycle2_papers.py
	python scripts/validate_nwagu_cycle2_papers.py

arxiv-quality-gate:
	python scripts/validate_arxiv_quality_gate.py

context-contamination:
	python scripts/validate_context_contamination.py

human-source-rights-packets:
	python scripts/validate_human_source_rights_packets.py

unicode-completion-gate:
	python scripts/validate_unicode_completion_gate.py
