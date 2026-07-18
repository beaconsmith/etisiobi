# EXP-FRONTIER-003 Annotation Codebook

        ## Task

        Label whether a claim promotes a weaker evidence layer into a stronger
        claim than the evidence permits.

        ## Layers

        - `source_observed`: directly observed in primary/local source evidence.
        - `source_index`: represented in a structured index or transcription but
          not fully source-reviewed.
        - `derived`: produced by an explicitly stated operation such as the f/v
          split.
        - `design_hypothesis`: system-design or application claim inspired by
          the artifact.
        - `speculative`: analogy, theory, or possibility not yet validated.
        - `blocked`: unavailable, rights-blocked, authority-blocked, or missing
          evidence.

        ## Labels To Fill

        - `input_layer`: weakest evidence layer needed to support the claim.
        - `output_layer`: layer the claim appears to assert.
        - `promotion_error`: `yes`, `no`, or `unclear`.
        - `severity`: `none`, `minor`, `material`, or `blocking`.
        - `annotator_rationale`: one sentence with evidence.

        ## Rule

        A promotion error occurs when the output layer is stronger than the
        evidence layer. The most dangerous errors are derived/speculative/blocked
        claims stated as source-observed or publication-ready facts.
