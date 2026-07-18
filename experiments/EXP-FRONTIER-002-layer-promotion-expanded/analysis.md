# Analysis

        EXP-FRONTIER-002 expands Layer Promotion Error from a 30-case seed into
        a 510-case internal benchmark built from repo claims,
        cross-program claims, adversarial rewrites, and external prior-art
        controls.

        The best held-out test baseline is `rank_only_metadata` with:

        - precision: 1.0
        - recall: 1.0
        - F1: 1.0
        - balanced accuracy: 1.0
        - MCC: 1.0
        - severity-weighted recall: 1.0

        This is stronger than the seed benchmark because it includes locked
        splits, multiple baselines, cross-program cases, external controls, and
        transition-level metrics. It is still not frontier proof because labels
        are heuristic, not blind-reviewed, and the dataset is not independently
        annotated.
