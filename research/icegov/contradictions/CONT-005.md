---
id: CONT-005
program: icegov
indicator: ["FID-02", "FID-03"]
type: sensitive_identity
severity: major
status: open
opened: 2026-04-16
---

# CONT-005: Gender and diaspora fields require governance policy decision

**Description:** FID-02 (Gender Participation Parity) and FID-03 (Diaspora Integration Rate) require demographic attributes — gender and geographic location — that are not in the `members` schema. Unlike CONT-001 through CONT-004, this is NOT a normal engineering gap. This is a **governance-sensitive data decision**.

**Why this is different:** Collecting gender and diaspora status involves:
- Self-identification privacy (members may not wish to identify)
- Community consent (the workspace as a whole must agree to this data collection)
- Potential for discriminatory use if exposed
- CARE Principles implications (Authority to Control)

**This contradiction does NOT go to the engineering backlog.** It goes to a governance policy decision track.

**Required decision path:**
1. Beaconsmith policy team defines collection criteria (voluntary? mandatory? aggregate-only?)
2. Community governance approval (workspace-level consent)
3. NHREC or equivalent ethics review for demographic data collection
4. Only then: product adds fields with appropriate access controls

**Paper impact:** FID-02 and FID-03 remain `blocked` in the registry. Paper v3 must explicitly note that demographic data collection requires community consent and ethics clearance — and frame this as a governance design principle, not just a missing feature.

**Resolution:** ~
