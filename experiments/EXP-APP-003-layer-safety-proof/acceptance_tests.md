# Acceptance Tests

The proof verifier must satisfy:

- [x] Detect that unqualified local IDs collide across layers.
- [x] Generate layer-qualified IDs.
- [x] Confirm all layer-qualified IDs are unique.
- [x] Confirm source count remains 208.
- [x] Confirm derived f/v split count remains 216.
- [x] Confirm governance/domain mapped count remains 48.
- [x] Confirm derived-to-source promotion is forbidden.
- [x] Confirm domain-mapped-to-source promotion is forbidden.

If any test fails, the proof is invalid or the grammar needs repair.
