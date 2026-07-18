---
type: dataset_boundary_contact_approval
contact_approval_id: BOUNDARY-REVIEW-CONTACT-APPROVAL-EXP-FRONTIER-008-001
dispatch_id: BOUNDARY-REVIEW-DISPATCH-EXP-FRONTIER-008-001
status: contact_approval_packet_ready_no_contacts_no_send_approval
created: "2026-06-22"
claim_ceiling: contact_approval_packet_ready_not_dispatch_approval
---

# Contact Approval Runbook

## Purpose

This contact approval packet prepares reviewer selection and send approval for
the `EXP-FRONTIER-008` dataset-boundary review dispatch. It does not send any
message, collect review evidence, or approve any release.

Status: not sent.

Current blocker: contact targets are blank and no explicit approval to send has
been recorded.

Do not send any invitation from this packet until the approval record is
completed by a human.

## Privacy Rule

No private contact data should be put in this repo. The repo template keeps reviewer
name, contact channel, contact target, and private contact storage blank until a
human provides a safe contact handling decision.

If a reviewer has only private contact details, store those details outside the
research package and record only the role status here.

## Reviewer Selection

Use `reviewer_selection_criteria.csv` to check each real human reviewer for
role fit, independence, and disqualifying conflicts before any dispatch.

## Contact Intake

Use `contact_intake_template.csv` as the blank in-repo record. It must stay at
`not_collected` with `approval_to_contact=no`, `approval_to_send=no`, and
`external_action_taken=no` until the user gives explicit approval to send.

## Send Approval

Use `send_approval_record_template.json` only after reviewer identity, contact
target, selected invitation template, and explicit approval to send are known.
The template itself is not approval.

## Claim Ceiling

`contact_approval_packet_ready_not_dispatch_approval`

This packet says the contact approval workflow is ready. It does not say any
review request was sent, any reviewer accepted, or any review result exists.

## Exact Next Action

Fill reviewer identity and safe contact handling details, then obtain explicit
approval to send each role-specific invitation.
