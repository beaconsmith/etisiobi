---
title: "Pre to Post-Treatment Glioblastoma MRI Prediction using a Latent Diffusion Model"
authors: [Alexandre G. Leclercq, Sébastien Bougleux, Noémie N. Moreau, Alexis Desmonts, Romain Hérault, Aurélien Corroyer-Dulmont]
published: 2025-10-13
source_url: http://arxiv.org/abs/2510.17851v1
tags: [raw_source, arxiv]
processing_status: unread
---

# Pre to Post-Treatment Glioblastoma MRI Prediction using a Latent Diffusion Model

**Authors:** Alexandre G. Leclercq, Sébastien Bougleux, Noémie N. Moreau, Alexis Desmonts, Romain Hérault, Aurélien Corroyer-Dulmont
**Published:** 2025-10-13
**Source:** [ArXiv Link](http://arxiv.org/abs/2510.17851v1)

## Abstract

Glioblastoma (GBM) is an aggressive primary brain tumor with a median survival of approximately 15 months. In clinical practice, the Stupp protocol serves as the standard first-line treatment. However, patients exhibit highly heterogeneous therapeutic responses which required at least two months before first visual impact can be observed, typically with MRI. Early prediction treatment response is crucial for advancing personalized medicine. Disease Progression Modeling (DPM) aims to capture the trajectory of disease evolution, while Treatment Response Prediction (TRP) focuses on assessing the impact of therapeutic interventions. Whereas most TRP approaches primarly rely on timeseries data, we consider the problem of early visual TRP as a slice-to-slice translation model generating post-treatment MRI from a pre-treatment MRI, thus reflecting the tumor evolution. To address this problem we propose a Latent Diffusion Model with a concatenation-based conditioning from the pre-treatment MRI and the tumor localization, and a classifier-free guidance to enhance generation quality using survival information, in particular post-treatment tumor evolution. Our model were trained and tested on a local dataset consisting of 140 GBM patients collected at Centre François Baclesse. For each patient we collected pre and post T1-Gd MRI, tumor localization manually delineated in the pre-treatment MRI by medical experts, and survival information.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

