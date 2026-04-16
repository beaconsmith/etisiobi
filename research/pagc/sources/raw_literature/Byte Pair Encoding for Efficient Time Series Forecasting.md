---
title: "Byte Pair Encoding for Efficient Time Series Forecasting"
authors: [Leon Götz, Marcel Kollovieh, Stephan Günnemann, Leo Schwinn]
published: 2025-05-20
source_url: http://arxiv.org/abs/2505.14411v3
tags: [raw_source, arxiv]
processing_status: unread
---

# Byte Pair Encoding for Efficient Time Series Forecasting

**Authors:** Leon Götz, Marcel Kollovieh, Stephan Günnemann, Leo Schwinn
**Published:** 2025-05-20
**Source:** [ArXiv Link](http://arxiv.org/abs/2505.14411v3)

## Abstract

Existing time series tokenization methods predominantly encode a constant number of samples into individual tokens. This inflexible approach can generate excessive tokens for even simple patterns like extended constant values, resulting in substantial computational overhead. Inspired by the success of byte pair encoding, we propose the first pattern-centric tokenization scheme for time series analysis. Based on a discrete vocabulary of frequent motifs, our method merges samples with underlying patterns into tokens, compressing time series adaptively. Exploiting our finite set of motifs and the continuous properties of time series, we further introduce conditional decoding as a lightweight yet powerful post-hoc optimization method, which requires no gradient computation and adds no computational overhead. On recent time series foundation models, our motif-based tokenization improves forecasting performance by 36% and boosts efficiency by 1990% on average. Conditional decoding further reduces MSE by up to 44%. In an extensive analysis, we demonstrate the adaptiveness of our tokenization to diverse temporal patterns, its generalization to unseen data, and its meaningful token representations capturing distinct time series properties, including statistical moments and trends.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

