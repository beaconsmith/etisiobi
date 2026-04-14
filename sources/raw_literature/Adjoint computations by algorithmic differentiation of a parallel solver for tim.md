---
title: "Adjoint computations by algorithmic differentiation of a parallel solver for time-dependent PDEs"
authors: [J. I. Cardesa, L. Hascoët, C. Airiau]
published: 2019-12-25
source_url: http://arxiv.org/abs/1912.11717v3
tags: [raw_source, arxiv]
processing_status: unread
---

# Adjoint computations by algorithmic differentiation of a parallel solver for time-dependent PDEs

**Authors:** J. I. Cardesa, L. Hascoët, C. Airiau
**Published:** 2019-12-25
**Source:** [ArXiv Link](http://arxiv.org/abs/1912.11717v3)

## Abstract

A computational fluid dynamics code is differentiated using algorithmic differentiation (AD) in both tangent and adjoint modes. The two novelties of the present approach are 1) the adjoint code is obtained by letting the AD tool Tapenade invert the complete layer of message passing interface (MPI) communications, and 2) the adjoint code integrates time-dependent, non-linear and dissipative (hence physically irreversible) PDEs with an explicit time integration loop running for ca. $10^{6}$ time steps. The approach relies on using the Adjoinable MPI library to reverse the non-blocking communication patterns in the original code, and by controlling the memory overhead induced by the time-stepping loop with binomial checkpointing. A description of the necessary code modifications is provided along with the validation of the computed derivatives and a performance comparison of the tangent and adjoint codes.

## Extracted Concepts (Auto-Generated)
> [!info] 
> This is a raw source file. An autonomous agent should read this abstract and extract specific `[[concepts]]`, methodologies, and falsification tests related to the Principle of Ancestral Generative Compression (PAGC).

