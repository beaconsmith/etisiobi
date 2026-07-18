---
type: dataset_boundary_review_dispatch
dispatch_id: BOUNDARY-REVIEW-DISPATCH-EXP-FRONTIER-008-001
intake_id: BOUNDARY-REVIEW-INTAKE-EXP-FRONTIER-008-001
status: ready_to_prepare_contacts_not_sent
created: "2026-06-22"
claim_ceiling: dispatch_packet_ready_not_sent
---

# Review Dispatch Runbook

## Purpose

This review dispatch packet prepares the five dataset-boundary review requests
for delivery. It does not send messages, approve reviewers, record human
review, approve the boundary, or authorize any external archive action.

Status: not sent.

Current blocker: missing reviewer contact for every required role.

## Dispatch Tracker

Use `dispatch_tracker.csv` to record reviewer name, contact channel, contact
target, approval to send, sent timestamp, and sender after the user approves
external dispatch.

Every row currently has `dispatch_status` set to
`not_sent_missing_reviewer_contact`.

## Role-Specific Invitation

Use the matching role-specific invitation template in
`invitation_templates/`. Each template includes subject, message, review
packet, required `PASS` / `REJECT` / `REVISE` output, schema-valid response
requirements, and the reminder that agent may not approve.

## Send Rule

Do not send externally until the user provides reviewer identity, contact
target, channel, and explicit approval to send.

## Claim Ceiling

`dispatch_packet_ready_not_sent`

This packet says review dispatch materials are ready. It does not say review
requests were sent.

## Exact Next Action

Fill in reviewer contacts and obtain explicit approval to send each
role-specific invitation.
