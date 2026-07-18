# Benchmark Integrity Standard

Date: 2026-07-06

## Purpose

Etisiobi needs benchmark discipline strong enough to stop prose, formatting, and
agent confidence from being mistaken for research quality.

This standard adapts the useful part of external autonomous-research harnesses:
claims must be reproducible from committed evidence, benchmark failures must be
diagnosed rather than explained away, and status labels must separate structure
from substance.

## Non-Negotiable Rules

1. Every promoted research claim needs a receipt: a source path, experiment
   output, validator report, or review trace that a reader can inspect.
2. A passing structural gate cannot imply manuscript legitimacy, venue fit,
   rights clearance, novelty, or public-release readiness.
3. Any benchmark or validator failure must produce wall forensics: what failed,
   what kind of failure it was, and what exact evidence would change the status.
4. Any status downgrade, false readiness claim, contamination event, or benchmark
   definition change must be recorded in the claim integrity ledger.
5. No loop may optimize only against the current validator strings. At least one
   anti-fitting check must ask whether a fresh external reader would understand
   the field result without private lab/process framing.

## Required Surfaces

- `research/CLAIM_INTEGRITY_LEDGER.md` records status corrections, retractions,
  contamination risks, and benchmark-definition changes.
- `research/BENCHMARK_WALL_FORENSICS.md` records benchmark failures by class and
  converts them into evidence-producing next actions.
- `scripts/validate_benchmark_integrity.py` checks that readiness registries do
  not overclaim when external-reader or lab-standard gates fail.

## Status Vocabulary

Use these distinctions exactly:

- `PACKET_COMPLETE`: required files exist, but scientific quality is not implied.
- `STRUCTURAL_GATE_PASS`: schema, file, compile, or package checks pass.
- `EXTERNAL_READER_LEGITIMACY_FAIL`: the manuscript still reads like a lab
  packet, private process memo, or self-describing article.
- `SUBMISSION_REVIEW_CANDIDATE_HUMAN_SIGNOFF_BLOCKED`: a candidate can be
  reviewed by humans, but must not be called journal-ready.
- `READY_FOR_SUBMISSION`: reserved for a package with passing lab-standard,
  review-team, external-reader, rights/authority, and human sign-off gates.

## Anti-Fitting Questions

Before celebrating any benchmark improvement, answer:

- Did the manuscript become a stronger field contribution, or did it merely stop
  matching forbidden strings?
- Would a reader outside Etisiobi understand the result before seeing any
  process, packet, gate, or claim-ceiling language?
- Is the result supported by evidence that existed before the prose rewrite?
- Are negative controls, limitations, and failure cases still visible?
- Did the status label become more honest, or only more impressive?

## Current Application

The current ten-candidate Nwagu Aneke journal registry is a useful stress test.
It can be packet-complete while still failing external-reader legitimacy. That
state is not embarrassing; it is the signal the lab needs. The correct response
is not to generate more PDFs. The correct response is to rewrite one branch into
a real field contribution, rerun the same gates, and only then scale.
