# Oroma DB Schema → OGI Indicator Mapping
> This is the evidence bridge between product and research.
> Generated: 2026-04-16. Update when schema changes.

---

## Core Evidence Source: `domain_events`

The `domain_events` table is the primary OGI evidence source. It is append-only, has provenance (blockRef, txRef, verificationState), and captures every consequential governance action.

```
domain_events
├── id, workspaceId, federationId
├── actorRef        → who performed the action
├── authority       → what authorized it (role, scope, policyRef)
├── intent          → why (human-readable purpose — maps to ISO 15489 reliability)
├── entityRef       → what was affected (entityType, entityId)
├── eventType       → classification
├── timestamp
├── payload         → domain-specific data
├── idempotencyKey  → prevents duplicate events
├── causationId     → causal chain
├── correlationId   → workflow grouping
└── provenance      → sourceKind, sourceRef, blockRef, txRef, verificationState
```

---

## OGI Dimension → DB Query

### RV-01: Verifiable Action Coverage Rate

```sql
-- Numerator: governance actions with on-chain provenance
SELECT COUNT(*) FROM domain_events
WHERE workspace_id = $workspaceId
  AND (provenance->>'blockRef') IS NOT NULL
  AND (provenance->>'verificationState') IN ('verified', 'anchored')
  AND timestamp >= NOW() - INTERVAL '90 days';

-- Denominator: all governance actions
SELECT COUNT(*) FROM domain_events
WHERE workspace_id = $workspaceId
  AND timestamp >= NOW() - INTERVAL '90 days';

-- RV-01 = numerator / denominator × 100
```

**Event types that count as "governance actions":**
- proposal.created, proposal.approved, proposal.executed, proposal.rejected
- treasury.contribution, treasury.disbursement, treasury.hold
- dispute.opened, dispute.resolved
- member.joined, member.role_changed
- record.created, record.verified

---

### DPR-01: Active Governance Participation Rate

```sql
-- Numerator: unique members who voted or proposed in 90-day window
SELECT COUNT(DISTINCT (actor_ref->>'id')) FROM domain_events
WHERE workspace_id = $workspaceId
  AND event_type IN ('proposal.created', 'proposal.voted', 'proposal.approved')
  AND timestamp >= NOW() - INTERVAL '90 days';

-- Denominator: total registered members
SELECT COUNT(*) FROM members
WHERE workspace_id = $workspaceId
  AND status = 'active';
```

### DPR-02: Quorum Achievement Rate

```sql
-- Numerator: proposals that reached quorum
SELECT COUNT(*) FROM proposals
WHERE workspace_id = $workspaceId
  AND status IN ('approved', 'executed')
  AND created_at >= NOW() - INTERVAL '90 days';

-- Denominator: total initiated proposals
SELECT COUNT(*) FROM proposals
WHERE workspace_id = $workspaceId
  AND created_at >= NOW() - INTERVAL '90 days';
```

---

### TTI-01: Treasury Audit Completeness Rate

```sql
-- Numerator: treasury movements with complete metadata
SELECT COUNT(*) FROM domain_events
WHERE workspace_id = $workspaceId
  AND event_type IN ('treasury.contribution', 'treasury.disbursement', 'treasury.hold')
  AND (payload->>'purpose') IS NOT NULL
  AND LENGTH(payload->>'purpose') >= 50
  AND (payload->>'proposalId') IS NOT NULL
  AND (provenance->>'blockRef') IS NOT NULL;

-- Denominator: all treasury movements
SELECT COUNT(*) FROM domain_events
WHERE workspace_id = $workspaceId
  AND event_type IN ('treasury.contribution', 'treasury.disbursement', 'treasury.hold');
```

**Completeness requirements (enforced at contract level, verified in research):**
- `payload.purpose` string ≥ 50 chars
- `payload.proposalId` not null (links to authorizing proposal)
- `provenance.blockRef` not null (on-chain anchor)
- `authority.role` must be in approved signatory set

### TTI-02: Solvency Provability Score

```sql
-- Binary: has the workspace generated a ZK solvency proof this cycle?
SELECT COUNT(*) > 0 FROM domain_events
WHERE workspace_id = $workspaceId
  AND event_type = 'treasury.solvency_proof_generated'
  AND timestamp >= $cycleStart;
```

---

### DRL-01: Dispute Resolution Completeness

```sql
-- Source: cases table (disputes are cases with caseType = 'dispute')
-- Numerator: closed cases with full documentation
SELECT COUNT(*) FROM cases
WHERE workspace_id = $workspaceId
  AND case_type = 'dispute'
  AND status IN ('resolved', 'dismissed')
  AND findings IS NOT NULL
  AND resolution IS NOT NULL
  AND remediation IS NOT NULL;
  -- evidence_refs is not null also required

-- Denominator: all initiated disputes
SELECT COUNT(*) FROM cases
WHERE workspace_id = $workspaceId
  AND case_type = 'dispute';
```

### DRL-02: Outcome Contestation Rate (inverse scored)

```sql
-- Cases reopened within 30 days of resolution
SELECT COUNT(*) FROM domain_events
WHERE workspace_id = $workspaceId
  AND event_type = 'case.reopened'
  AND (payload->>'daysSinceResolution')::int <= 30;
```

### DRL-03: Resolution Speed

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY
  EXTRACT(EPOCH FROM (closed_at - created_at)) / 86400
) AS median_days
FROM cases
WHERE workspace_id = $workspaceId
  AND case_type = 'dispute'
  AND status = 'resolved';
```

---

### CPS-01: Portable Identity Coverage

```sql
-- Requires Ichi credential export tracking
-- Currently: check domain_events for credential export events
SELECT COUNT(DISTINCT (actor_ref->>'id')) FROM domain_events
WHERE workspace_id = $workspaceId
  AND event_type = 'credential.exported'
  AND (payload->>'evidenceEventCount')::int >= 3;
```

**Gap:** `credential.exported` event may not exist yet. This is one of the 4 product gaps blocking OGI computability.

---

### CAS-01: Record Exportability Rate

```sql
-- Records with verified provenance and block anchor
SELECT COUNT(*) FROM records
WHERE workspace_id = $workspaceId
  AND verification_state = 'verified'
  AND (provenance->>'blockRef') IS NOT NULL;

-- Denominator: all records
SELECT COUNT(*) FROM records
WHERE workspace_id = $workspaceId;
```

---

### FID-01: First-Time Formal Participant Rate

```sql
-- Requires onboarding survey response at wallet creation
-- Stored in: domain_events with event_type = 'member.onboarding_survey_submitted'
-- payload: { firstTimeParticipant: boolean }

SELECT COUNT(*) FROM domain_events
WHERE workspace_id = $workspaceId
  AND event_type = 'member.onboarding_survey_submitted'
  AND (payload->>'firstTimeParticipant')::boolean = true
  AND timestamp >= $measurementPeriodStart;
```

**Gap:** `member.onboarding_survey_submitted` event doesn't exist yet. Product must add survey at wallet creation.

---

## Summary: What's Computable Now vs Needs Product Work

| OGI Indicator | Computable Now? | Blocker |
|---------------|----------------|---------|
| RV-01 | ✓ Once testnet has activity | Need provenance.blockRef populated |
| DPR-01 | ✓ | — |
| DPR-02 | ✓ | — |
| TTI-01 | Partial | purpose ≥50 chars not enforced at contract level yet |
| TTI-02 | ✗ | ZK solvency proof event not in schema |
| DRL-01 | Partial | cases.findings + cases.evidenceRefs not always populated |
| DRL-02 | ✗ | case.reopened event not in domain_events |
| DRL-03 | ✓ | — |
| CPS-01 | ✗ | credential.exported event missing |
| CAS-01 | ✓ | — |
| FID-01 | ✗ | Onboarding survey not built |
| FID-02 | ✗ | Gender field not in members schema |

**OGI-Core (RV-01 + DPR-01 + TTI-01 + DRL-01) computable:** Partial — after first real governance cycles on testnet.
