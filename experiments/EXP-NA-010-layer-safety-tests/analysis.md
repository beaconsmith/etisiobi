# Analysis

The layer-safety gate now has two evidence layers.

The original seven-case test set showed that the non-promotion invariant rejects
simple transformations from derived, speculative, or blocked labels into
source-observed labels.

The expanded 24-case matrix adds safe weakening cases, abstract/title/figure
promotion probes, rights-blocker probes, and shallow baseline comparisons. The
gate detected all 14 intentional promotion errors. Provenance-only checking
missed 11 promotion errors, citation-only checking missed 7, and a no-label gate
missed all 14.

This supports a bounded systems claim: provenance and citation metadata are
necessary but insufficient for layer-safe artifact-derived generation unless the
allowed evidence layer is also preserved through the output.

The result remains bounded. The experiment does not prove completeness for all
cultural-heritage AI systems, and it does not grant public source, rights, or
authority clearance.
