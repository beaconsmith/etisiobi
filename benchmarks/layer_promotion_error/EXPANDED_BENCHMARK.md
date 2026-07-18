# Expanded Layer Promotion Error Benchmark

        Benchmark ID: `LPE-BENCH-002`

        ## Current Status

        `EXPANDED_BENCHMARK_INTERNAL_NOT_FRONTIER_PROOF`

        ## Scale

        - Cases: `510`
        - Source types: `{'real_repo_claim': 225, 'cross_program': 165, 'external_prior_art_control': 30, 'adversarial_hard_case': 90}`
        - Variants: `{'real_claim': 130, 'edited_real_claim': 130, 'adversarial_promotion': 130, 'external_control': 10, 'external_adversarial': 10, 'external_boundary': 10, 'hard_positive_no_trigger': 50, 'hard_negative_trigger_words': 40}`
        - Splits: `{'train': 292, 'dev': 107, 'test': 111}`

        ## Best Held-Out Test Baseline

        - Baseline: `rank_only_metadata`
        - Precision: `1.0`
        - Recall: `1.0`
        - F1: `1.0`
        - MCC: `1.0`

        ## Interpretation

        This is an internal expanded benchmark, not a frontier proof. It becomes
        a frontier candidate only after blind annotation, external/cross-project
        cases, comparison to real claim-verification/provenance/type-system
        baselines, and domain/rights review.
