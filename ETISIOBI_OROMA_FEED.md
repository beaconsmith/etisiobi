# Etisiobi Oroma Feed

> Version: 1.0
> Date: 2026-05-03
> Goal: Define the research-to-product bridge between Etisiobi and Oroma.

---

## What This Is

The **Oroma Feed** is the structured pipeline that turns Etisiobi research into Oroma product decisions.

It is not a wishlist. It is not a brainstorm. It is an **evidence-backed product feedback system**.

Every recommendation must include:
1. **Finding** — what we learned
2. **Evidence** — source IDs and quotes
3. **Recommendation** — what Oroma should do
4. **Acceptance Test** — how to know it worked

---

## Feed Types

### Type 1: Institution Template Feed
- **What:** Complete governance templates for specific institution types.
- **When:** When Oroma needs to onboard a new institution type.
- **Format:** Institution Template Research Pack (see `ETISIOBI_RESEARCH_DOCTRINE.md`)
- **Destination:** Oroma product team → feature requirements → UI flows

### Type 2: Governance Rule Feed
- **What:** Specific rules, rituals, or practices that should be encoded in Oroma.
- **Example:** "Rotation prevents conflict. Oroma should support term limits and automatic rotation reminders."
- **Format:** Finding + Evidence + Recommendation + Acceptance Test
- **Destination:** Oroma backend (rule engine) + frontend (UI prompts)

### Type 3: UX Pattern Feed
- **What:** How real users currently manage money and what they expect.
- **Example:** "Secretaries keep parallel WhatsApp and paper records. Oroma should allow quick photo receipt upload and WhatsApp-style notification."
- **Format:** Observation + Quote + Recommendation + Mockup suggestion
- **Destination:** Oroma frontend team

### Type 4: Trust & Legitimacy Feed
- **What:** What makes members trust an institution, and what breaks it.
- **Example:** "Members trust when the chairman and secretary are from different families. Oroma should display authority separation."
- **Format:** Trust pattern + Violation example + Recommendation
- **Destination:** Oroma trust page + public legitimacy features

### Type 5: Indicator & Metric Feed
- **What:** Quantifiable governance quality indicators computed from Oroma data.
- **Example:** "RV-01 (Rotation Validity) = 1 if roles rotated in last term, 0 otherwise."
- **Format:** Indicator definition + Formula + Data source + Target value
- **Destination:** Oroma analytics + BeaconOS dashboard

---

## Feed Production Process

```text
Etisiobi research
    ↓
Extract finding
    ↓
Validate with source
    ↓
Format as recommendation
    ↓
Review internally (Etisiobi peer review)
    ↓
Submit to Oroma Feed Queue
    ↓
Oroma product lead reviews
    ↓
Accepted → Ticket created
Rejected → Reason recorded
Deferred → Priority assigned
```

---

## Feed Queue Schema

```text
id: string
type: template | governance | ux | trust | indicator
status: proposed | accepted | rejected | deferred
finding: string
evidence: string[] (source IDs)
recommendation: string
acceptance_test: string
priority: critical | high | medium | low
submitted_by: string
submitted_at: datetime
reviewed_by: string (Oroma product lead)
reviewed_at: datetime
oroma_ticket: string (if accepted)
```

---

## Current Blockers

1. **Spine not operational:** `extractor.py` has never connected to Oroma DB.
2. **Missing schema events:** Oroma DB lacks 4 events needed for indicator computation:
   - `member.onboarding_survey_submitted`
   - `cases.findings`
   - `credential.exported`
   - `treasury.solvency_proof_generated`
3. **No feed queue exists:** Recommendations are scattered in `research/product_feedback/` without structured review.
4. **No Oroma owner assigned:** No explicit Oroma product lead responsible for reviewing Etisiobi feed.

---

## Immediate Actions

### Step 1: Connect spine
- Add `.env` with `OROMA_DB_URL`.
- Run `spine/extractor.py` against Oroma staging DB.
- Generate first `daily_facts.json`.

### Step 2: Create feed queue
- Add `spine/feed_queue.json` with schema above.
- Migrate existing `research/product_feedback/` items into queue.

### Step 3: Assign Oroma reviewer
- Oroma product lead reviews queue weekly.
- Etisiobi researcher presents top 3 recommendations in weekly sync.

### Step 4: Add missing schema events
- Oroma backend adds the 4 missing event types to `domain_events`.
- Etisiobi updates indicator formulas to use them.

---

## Example Feed Item

```json
{
  "id": "feed_001",
  "type": "governance",
  "status": "proposed",
  "finding": "Hometown associations use rotation (zoning) to prevent conflict over leadership and money control.",
  "evidence": ["interview_ha_secretary_enugu_2026_04_28", "document_ha_constitution_nsukka_2019"],
  "recommendation": "Oroma should support automatic role rotation reminders and term limit enforcement.",
  "acceptance_test": "A secretary can set a role term (e.g., 2 years). Oroma reminds the workspace 30 days before rotation and records the handover.",
  "priority": "high",
  "submitted_by": "etisiobi_researcher_01",
  "submitted_at": "2026-05-03T00:00:00Z"
}
```

---

## Success Criteria

1. `extractor.py` runs daily and produces non-empty facts.
2. Feed queue contains ≥10 reviewed items within 30 days.
3. ≥3 recommendations are accepted and converted to Oroma tickets.
4. One indicator (e.g., RV-01) is computed from real Oroma pilot data.
5. Weekly Etisiobi-Oroma sync reviews feed queue.

---

*Do not implement yet. Start by connecting `extractor.py` and creating the queue.*
