# Bridge: Oroma → Etisiobi (signal ingest, INBOUND)

> Direction: **product → research**. This complements the outbound
> `ETISIOBI_OROMA_FEED.md` (research → product). Together they close the loop.
> Status: spec. Not wired. No automation until the structure is proven.

## Principle
Oroma sends **signals, not conclusions**. A signal is a privacy-safe observation
of how the product behaves in use. Etisiobi decides whether a signal becomes a
research question. Oroma does not get to assert research findings.

## What Oroma MAY send
- QA report failures and regressions
- Screenshot/visual failures
- Product friction summaries (time-on-page, abandonment)
- Onboarding drop-offs
- Copy confusion patterns (e.g. "member-safe" misunderstood)
- Role confusion patterns
- Ask-Oroma failure / thin-data cases
- Report-preview failures
- Privacy / redaction incidents (described, never the private data itself)
- Support questions (themes, anonymized)

## What Oroma MUST NOT send (hard rule)
Names · phone numbers · emails · bank details · welfare details · private notes ·
raw receipts/documents · exact amounts where hidden · full member directory ·
raw question text containing any of the above. **No raw community data ever.**
If in doubt, aggregate or omit.

## Signal schema
```text
id: string
date: datetime
source: qa | telemetry | field | support
kind: friction | drop_off | copy_confusion | role_confusion |
      ask_failure | preview_failure | privacy_incident | regression
route: string           # e.g. "/reports"
role: member | treasurer | secretary | auditor | chairperson | public | pending
viewport: mobile | desktop
observation: string     # what happened, anonymized
frequency: count or note
community_id_hash: string   # hashed, never the real id
```

## Pipeline
```text
Oroma signal (anonymized)
  → triage: noise or research-worthy?
  → if worthy: open a ResearchSession (question, not answer)
  → gather sources / evidence
  → claim (with status) → review
  → product implication → ETISIOBI_OROMA_FEED.md item
  → Oroma ticket → UX/test/screenshot confirms
  → learning recorded (log.md / self_improvement_proposals/)
```

## Examples
1. Signal: members linger on `/reports` without publishing →
   Session: "Do users understand report readiness?" →
   Decision: move the missing-receipts warning above the preview button.
2. Signal: "member-safe" misunderstood →
   Experiment: "member-safe" vs "what members can see" →
   CopyLearning: use "what members can see" for elders.
3. Signal: Ask-Oroma cites thin data →
   Session: "How should Oroma explain thin data?" →
   CopyRule: "There is not enough recorded to answer that yet."

## Routing note
Today, product↔research routing runs through the sibling `../beaconos` dashboard
and `research/product_feedback/`. Keep signals there until a queue file is agreed.
