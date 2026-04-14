---
title: "Back to Bytes: Revisiting Tokenization Through UTF-8"
authors: [Amit Moryossef, Clara Meister, Pavel Stepachev, Desmond Elliott]
published: 2025-10-19
source_url: http://arxiv.org/abs/2510.16987v1
tags: [raw_source, arxiv]
processing_status: unread
---

# Back to Bytes: Revisiting Tokenization Through UTF-8

**Authors:** Amit Moryossef, Clara Meister, Pavel Stepachev, Desmond Elliott
**Published:** 2025-10-19
**Source:** [ArXiv Link](http://arxiv.org/abs/2510.16987v1)

## Abstract

We present UTF8Tokenizer, a minimalist byte-level tokenizer that maps text exactly to IDs corresponding to the bytes underlying the text's UTF-8 encoding (e.g., byte x09 is token ID 9). Unlike prior byte-level approaches (Xue et al., 2021; Pagnoni et al., 2025), our implementation never introduces out-of-range IDs (i.e. there is no token ID 256) or auxiliary tokens: all special behavior (e.g., padding, boundaries, conversation structure, attention segments, tool calling, "thinking" spans, etc.) is encoded using C0 control bytes - just as ASCII was originally designed to embed control information alongside printable text. These design principles yield practical benefits: (1) faster tokenization (14x) and significantly lower host-device transfer (8x less than int64); (2) simple, shareable 256*d embedding tables that can be aligned across models; and (3) a training-time enhancement via bit-biased embeddings, which exposes per-byte bit structure and can be added to the embedding table post-training, removing inference costs. Our HuggingFace-compatible implementation improves language modeling convergence.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

