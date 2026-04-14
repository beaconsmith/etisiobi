---
title: "Newton-Puiseux Analysis for Interpretability and Calibration of Complex-Valued Neural Networks"
authors: [Piotr Migus]
published: 2025-04-27
source_url: http://arxiv.org/abs/2504.19176v2
tags: [raw_source, arxiv]
processing_status: unread
---

# Newton-Puiseux Analysis for Interpretability and Calibration of Complex-Valued Neural Networks

**Authors:** Piotr Migus
**Published:** 2025-04-27
**Source:** [ArXiv Link](http://arxiv.org/abs/2504.19176v2)

## Abstract

Complex-valued neural networks (CVNNs) are particularly suitable for handling phase-sensitive signals, including electrocardiography (ECG), radar/sonar, and wireless in-phase/quadrature (I/Q) streams. Nevertheless, their \emph{interpretability} and \emph{probability calibration} remain insufficiently investigated. In this work, we present a Newton--Puiseux framework that examines the \emph{local decision geometry} of a trained CVNN by (i) fitting a small, kink-aware polynomial surrogate to the \emph{logit difference} in the vicinity of uncertain inputs, and (ii) factorizing this surrogate using Newton--Puiseux expansions to derive analytic branch descriptors, including exponents, multiplicities, and orientations. These descriptors provide phase-aligned directions that induce class flips in the original network and allow for a straightforward, \emph{multiplicity-guided} temperature adjustment for improved calibration. We outline assumptions and diagnostic measures under which the surrogate proves informative and characterize potential failure modes arising from piecewise-holomorphic activations (e.g., modReLU). Our phase-aware analysis identifies sensitive directions and enhances Expected Calibration Error in two case studies beyond a controlled $\C^2$ synthetic benchmark -- namely, the MIT--BIH arrhythmia (ECG) dataset and RadioML 2016.10a (wireless modulation) -- when compared to uncalibrated softmax and standard post-hoc baselines. We also present confidence intervals, non-parametric tests, and quantify sensitivity to inaccuracies in estimating branch multiplicity. Crucially, this method requires no modifications to the architecture and applies to any CVNN with complex logits transformed to real moduli.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

