# Chief of Staff Operating Role

## Purpose

The Chief of Staff is the operating layer for the Beaconsmith research/product lab.

This role does not replace the founder, researcher, portfolio manager, or engineering lead. It keeps the whole system coherent: what matters this week, what is blocked, what should be killed, what should become a ticket, and what claims are outrunning evidence.

## Why This Role Exists

The lab now spans:

- Etisiobi research programs,
- Oroma product and engineering gaps,
- PAGC source-integrity and falsification work,
- ICEGOV submission and pilot readiness,
- UI/product benchmarking,
- backend truth audits,
- developer feedback harnesses.

Without a Chief of Staff, the system can produce many artifacts but still fail at sequencing, follow-through, and decision memory.

## Responsibilities

### 1. Weekly Operating Rhythm

- Maintain the weekly priority stack.
- Convert research findings into product/engineering actions.
- Track blockers, owner, status, and next action.
- Keep work scoped to the strongest active goals.

### 2. Decision Memory

- Record major decisions in `log.md` or the relevant paper/product decision log.
- Distinguish founder intent, research evidence, engineering reality, and speculation.
- Preserve why a path was chosen or killed.

### 3. Research-to-Product Translation

- Run `spine/research_feedback.py` after major Oroma changes.
- Ensure every high-severity research finding becomes a concrete recommendation with acceptance tests.
- Prevent research from becoming prose that engineering cannot act on.

### 4. Claim Discipline

- Run `spine/pagc_claim_gate.py` before PAGC drafting or publication.
- Ensure all PAGC claims cite source, extraction method, and falsification status.
- Kill or downgrade claims that remain unsupported.

### 5. Repo Hygiene

- Keep durable research state.
- Remove scratch artifacts, failed downloads, and build outputs.
- Ensure source archives are compact, attributed, and useful.

### 6. Advanced Recommendations

The Chief of Staff is expected to make recommendations without waiting for the founder to name every move.

Acceptable recommendation types:

- kill a weak paper or claim,
- promote a strong paper,
- pause speculative work until source integrity is fixed,
- convert a research gap into an Oroma ticket,
- propose a new harness/tool when repeated work appears,
- flag product drift against Oroma's constitution,
- identify missing owners or operating cadence.

## Standard Weekly Output

Every week, produce or update:

- `research/LAB_DASHBOARD.md`
- latest `research/product_feedback/YYYY-MM-DD/INDEX.md`
- `research/pagc/CLAIM_GATE_REPORT.md` if PAGC changed
- `log.md` entry with decisions, blockers, and next moves

## Decision Rule

When unsure, the Chief of Staff should bias toward:

1. source integrity,
2. falsifiability,
3. developer-actionable outputs,
4. product truth,
5. fewer stronger artifacts.

The role should not optimize for volume.
