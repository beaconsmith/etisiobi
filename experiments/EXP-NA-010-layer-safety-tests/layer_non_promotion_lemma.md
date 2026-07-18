# Layer Non-Promotion Lemma

    Let evidence labels be ordered by evidentiary strength:

    `source_observed < derived < speculative < blocked`

    A pipeline transform is layer-safe when it never emits an output label that
    is stronger than the strongest label licensed by its input evidence. For any
    finite composition of layer-safe transforms, a non-source claim cannot become
    a source-observed claim.

    Proof: For one transform, the property follows by definition. Assume a
    composition of `n` transforms cannot promote a label. Appending one more
    layer-safe transform cannot decrease the label rank, so the `n+1`
    composition also cannot promote a label. By induction, no finite
    layer-safe pipeline can turn derived, speculative, or blocked claims into
    source-observed claims. The publication gate rejects any violation where
    `rank(output) < rank(input)`.
