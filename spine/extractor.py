"""
Research Spine: Evidence Extractor
===================================
Connects to Oroma DB (read-only), queries governance evidence,
computes OGI indicator values, writes structured facts to etisiobi.

Usage:
    python spine/extractor.py
    python spine/extractor.py --workspace ws_abc123
    python spine/extractor.py --days 30

Requirements:
    pip install psycopg2-binary python-dotenv

Environment:
    OROMA_DB_URL  — read-only Postgres connection string
    WORKSPACE_IDS — comma-separated workspace IDs (or 'all')
    ETISIOBI_PATH — path to etisiobi repo root (default: current dir)
"""

import os
import json
import argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from dotenv import load_dotenv

try:
    import psycopg2
    import psycopg2.extras
    HAS_DB = True
except ImportError:
    HAS_DB = False

load_dotenv()

OROMA_DB_URL = os.getenv("OROMA_DB_URL")
WORKSPACE_IDS = os.getenv("WORKSPACE_IDS", "all")
ETISIOBI_PATH = Path(os.getenv("ETISIOBI_PATH", "."))
SCHEMA_VERSION = "2026-04-16"
EXTRACTOR_VERSION = "0.1.0"

# OGI indicator definitions
# Each maps to one or more SQL queries against Oroma DB
OGI_INDICATORS = {
    "RV-01": "Verifiable Action Coverage Rate",
    "DPR-01": "Active Governance Participation Rate",
    "DPR-02": "Quorum Achievement Rate",
    "TTI-01": "Treasury Audit Completeness Rate",
    "TTI-02": "Solvency Provability Score",
    "DRL-01": "Dispute Resolution Completeness",
    "DRL-02": "Outcome Contestation Rate",
    "DRL-03": "Resolution Speed (median days)",
    "CPS-01": "Portable Identity Coverage",
    "CAS-01": "Record Exportability Rate",
    "FID-01": "First-Time Formal Participant Rate",
    "FID-02": "Gender Participation Parity Index",
    "FID-03": "Diaspora Integration Rate",
}

# Known product gaps — events/fields not yet in schema
# Update this as product ships new features
KNOWN_PRODUCT_GAPS = {
    "TTI-02": "treasury.solvency_proof_generated event not in domain_events schema",
    "CPS-01": "credential.exported event not in domain_events schema",
    "DRL-02": "case.reopened event not in domain_events schema",
    "FID-01": "member.onboarding_survey_submitted event not in schema",
    "FID-02": "gender field not in members schema",
    "FID-03": "diaspora flag not in members schema",
}


def get_connection():
    if not HAS_DB:
        raise ImportError("psycopg2 not installed. Run: pip install psycopg2-binary")
    if not OROMA_DB_URL:
        raise ValueError("OROMA_DB_URL not set in environment")
    return psycopg2.connect(OROMA_DB_URL, cursor_factory=psycopg2.extras.RealDictCursor)


def get_workspace_ids(conn):
    """Return list of active workspace IDs."""
    if WORKSPACE_IDS != "all":
        return WORKSPACE_IDS.split(",")
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM workspaces WHERE status = 'active'")
        return [row["id"] for row in cur.fetchall()]


def compute_rv01(conn, workspace_id, since):
    """RV-01: Verifiable Action Coverage Rate."""
    governance_event_types = (
        "proposal.created", "proposal.approved", "proposal.executed",
        "proposal.rejected", "treasury.contribution", "treasury.disbursement",
        "treasury.hold", "dispute.opened", "dispute.resolved",
        "member.joined", "record.created", "record.verified",
    )
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) as total FROM domain_events
            WHERE workspace_id = %s AND timestamp >= %s
              AND event_type = ANY(%s)
        """, (workspace_id, since, list(governance_event_types)))
        total = cur.fetchone()["count"]

        if total == 0:
            return None, "no_governance_events", total

        cur.execute("""
            SELECT COUNT(*) as verified FROM domain_events
            WHERE workspace_id = %s AND timestamp >= %s
              AND event_type = ANY(%s)
              AND provenance->>'blockRef' IS NOT NULL
              AND provenance->>'verificationState' IN ('verified', 'anchored')
        """, (workspace_id, since, list(governance_event_types)))
        verified = cur.fetchone()["count"]

        value = round((verified / total) * 100, 1)
        return value, "computed", total


def compute_dpr01(conn, workspace_id, since):
    """DPR-01: Active Governance Participation Rate."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) as total FROM members
            WHERE workspace_id = %s AND status = 'active'
        """, (workspace_id,))
        total_members = cur.fetchone()["count"]

        if total_members == 0:
            return None, "no_members", 0

        cur.execute("""
            SELECT COUNT(DISTINCT actor_ref->>'id') as active
            FROM domain_events
            WHERE workspace_id = %s AND timestamp >= %s
              AND event_type IN ('proposal.created', 'proposal.voted', 'proposal.approved')
        """, (workspace_id, since))
        active = cur.fetchone()["count"]

        value = round((active / total_members) * 100, 1)
        return value, "computed", total_members


def compute_dpr02(conn, workspace_id, since):
    """DPR-02: Quorum Achievement Rate."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) as total FROM proposals
            WHERE workspace_id = %s AND created_at >= %s
        """, (workspace_id, since))
        total = cur.fetchone()["count"]

        if total == 0:
            return None, "no_proposals", 0

        cur.execute("""
            SELECT COUNT(*) as approved FROM proposals
            WHERE workspace_id = %s AND created_at >= %s
              AND status IN ('approved', 'executed')
        """, (workspace_id, since))
        approved = cur.fetchone()["count"]

        value = round((approved / total) * 100, 1)
        return value, "computed", total


def compute_tti01(conn, workspace_id, since):
    """TTI-01: Treasury Audit Completeness Rate."""
    treasury_events = ("treasury.contribution", "treasury.disbursement", "treasury.hold")
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) as total FROM domain_events
            WHERE workspace_id = %s AND timestamp >= %s
              AND event_type = ANY(%s)
        """, (workspace_id, since, list(treasury_events)))
        total = cur.fetchone()["count"]

        if total == 0:
            return None, "no_treasury_movements", 0

        # Completeness: purpose >= 50 chars, proposalId not null, blockRef not null
        cur.execute("""
            SELECT COUNT(*) as complete FROM domain_events
            WHERE workspace_id = %s AND timestamp >= %s
              AND event_type = ANY(%s)
              AND LENGTH(payload->>'purpose') >= 50
              AND (payload->>'proposalId') IS NOT NULL
              AND (provenance->>'blockRef') IS NOT NULL
        """, (workspace_id, since, list(treasury_events)))
        complete = cur.fetchone()["count"]

        value = round((complete / total) * 100, 1)
        return value, "computed", total


def compute_drl01(conn, workspace_id, since):
    """DRL-01: Dispute Resolution Completeness."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) as total FROM cases
            WHERE workspace_id = %s AND case_type = 'dispute'
              AND created_at >= %s
        """, (workspace_id, since))
        total = cur.fetchone()["count"]

        if total == 0:
            return None, "no_disputes", 0

        cur.execute("""
            SELECT COUNT(*) as complete FROM cases
            WHERE workspace_id = %s AND case_type = 'dispute'
              AND created_at >= %s
              AND status IN ('resolved', 'dismissed')
              AND findings IS NOT NULL
              AND resolution IS NOT NULL
              AND evidence_refs IS NOT NULL
        """, (workspace_id, since))
        complete = cur.fetchone()["count"]

        value = round((complete / total) * 100, 1)
        return value, "computed", total


def compute_cas01(conn, workspace_id):
    """CAS-01: Record Exportability Rate."""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) as total FROM records
            WHERE workspace_id = %s
        """, (workspace_id,))
        total = cur.fetchone()["count"]

        if total == 0:
            return None, "no_records", 0

        cur.execute("""
            SELECT COUNT(*) as exportable FROM records
            WHERE workspace_id = %s
              AND verification_state = 'verified'
              AND (provenance->>'blockRef') IS NOT NULL
        """, (workspace_id,))
        exportable = cur.fetchone()["count"]

        value = round((exportable / total) * 100, 1)
        return value, "computed", total


def extract_workspace(conn, workspace_id, measurement_days=90):
    """Extract all computable OGI indicators for a workspace."""
    since = datetime.now(timezone.utc) - timedelta(days=measurement_days)
    result = {
        "id": workspace_id,
        "measurement_period_days": measurement_days,
        "measurement_since": since.isoformat(),
        "indicators": {},
        "OGI_core": None,
        "raw_counts": {},
    }

    # Computable indicators
    rv01, rv01_status, rv01_n = compute_rv01(conn, workspace_id, since)
    result["indicators"]["RV-01"] = {"value": rv01, "status": rv01_status, "n": rv01_n}

    dpr01, dpr01_status, dpr01_n = compute_dpr01(conn, workspace_id, since)
    result["indicators"]["DPR-01"] = {"value": dpr01, "status": dpr01_status, "n": dpr01_n}

    dpr02, dpr02_status, dpr02_n = compute_dpr02(conn, workspace_id, since)
    result["indicators"]["DPR-02"] = {"value": dpr02, "status": dpr02_status, "n": dpr02_n}

    tti01, tti01_status, tti01_n = compute_tti01(conn, workspace_id, since)
    result["indicators"]["TTI-01"] = {"value": tti01, "status": tti01_status, "n": tti01_n}

    drl01, drl01_status, drl01_n = compute_drl01(conn, workspace_id, since)
    result["indicators"]["DRL-01"] = {"value": drl01, "status": drl01_status, "n": drl01_n}

    cas01, cas01_status, cas01_n = compute_cas01(conn, workspace_id)
    result["indicators"]["CAS-01"] = {"value": cas01, "status": cas01_status, "n": cas01_n}

    # Mark known product gaps
    for ind, gap_note in KNOWN_PRODUCT_GAPS.items():
        result["indicators"][ind] = {"value": None, "status": "product_gap", "note": gap_note}

    # OGI-Core: RV-01 + DPR-01 + TTI-01 + DRL-01 (equally weighted)
    core_values = [
        rv01 if rv01 is not None else None,
        dpr01 if dpr01 is not None else None,
        tti01 if tti01 is not None else None,
        drl01 if drl01 is not None else None,
    ]
    computable = [v for v in core_values if v is not None]
    if computable:
        result["OGI_core"] = {
            "value": round(sum(computable) / len(computable), 1),
            "computable_dimensions": len(computable),
            "total_dimensions": 4,
            "note": f"Partial: {len(computable)}/4 core dimensions computed",
        }

    return result


def write_facts(date_str, workspaces_data, contradictions):
    """Write facts JSON and markdown to etisiobi."""
    facts_dir = ETISIOBI_PATH / "research" / "icegov" / "facts"
    facts_dir.mkdir(parents=True, exist_ok=True)

    output = {
        "date": date_str,
        "schema_version": SCHEMA_VERSION,
        "extractor_version": EXTRACTOR_VERSION,
        "workspaces": workspaces_data,
        "contradictions": contradictions,
        "product_gaps": list(KNOWN_PRODUCT_GAPS.values()),
    }

    json_path = facts_dir / f"{date_str}.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)

    # Write markdown summary
    md_path = facts_dir / f"{date_str}.md"
    with open(md_path, "w") as f:
        f.write(f"# Evidence Extraction: {date_str}\n\n")
        f.write(f"> Schema: {SCHEMA_VERSION} | Extractor: {EXTRACTOR_VERSION}\n\n")
        f.write("## Workspace Summaries\n\n")
        for ws in workspaces_data:
            f.write(f"### {ws['id']}\n")
            f.write(f"- Measurement period: last {ws['measurement_period_days']} days\n")
            core = ws.get("OGI_core")
            if core:
                f.write(f"- OGI-Core: **{core['value']}%** ({core['computable_dimensions']}/4 dimensions)\n")
            else:
                f.write("- OGI-Core: **not computable** — insufficient activity\n")
            f.write("\n| Indicator | Value | Status |\n|-----------|-------|--------|\n")
            for ind, data in ws["indicators"].items():
                val = f"{data['value']}%" if data["value"] is not None else "—"
                f.write(f"| {ind} | {val} | {data['status']} |\n")
            f.write("\n")

        if contradictions:
            f.write("## Contradictions\n\n")
            for c in contradictions:
                f.write(f"- {c}\n")

        f.write("\n## Product Gaps (indicators blocked by missing product features)\n\n")
        for ind, gap in KNOWN_PRODUCT_GAPS.items():
            f.write(f"- **{ind}**: {gap}\n")

    return json_path, md_path


def append_to_log(date_str, summary):
    """Append extraction summary to research log."""
    log_path = ETISIOBI_PATH / "log.md"
    entry = f"\n## [{date_str}] icegov | evidence-extraction | Daily OGI indicator extraction\n\n{summary}\n"
    with open(log_path, "a") as f:
        f.write(entry)


def run(days=90, workspace_filter=None):
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    contradictions = []

    if not HAS_DB or not OROMA_DB_URL:
        # Offline mode: write a "no connection" facts file
        print("No DB connection — writing offline facts file")
        workspace_data = [{
            "id": "offline",
            "measurement_period_days": days,
            "measurement_since": None,
            "indicators": {ind: {"value": None, "status": "no_db_connection"}
                           for ind in OGI_INDICATORS},
            "OGI_core": None,
            "raw_counts": {},
        }]
        json_path, md_path = write_facts(date_str, workspace_data, ["DB not connected"])
        print(f"Wrote: {json_path}")
        return

    try:
        conn = get_connection()
        workspace_ids = get_workspace_ids(conn)

        if workspace_filter:
            workspace_ids = [w for w in workspace_ids if w in workspace_filter.split(",")]

        workspaces_data = []
        for ws_id in workspace_ids:
            print(f"Extracting: {ws_id}")
            ws_data = extract_workspace(conn, ws_id, days)
            workspaces_data.append(ws_data)

            # Collect contradictions
            for ind, data in ws_data["indicators"].items():
                if data["status"] == "product_gap":
                    contradictions.append(f"[{ws_id}] {ind} uncomputable: {data.get('note', '')}")

        conn.close()

        json_path, md_path = write_facts(date_str, workspaces_data, contradictions)
        print(f"Wrote: {json_path}")
        print(f"Wrote: {md_path}")

        summary_lines = [f"Workspaces processed: {len(workspaces_data)}"]
        for ws in workspaces_data:
            core = ws.get("OGI_core")
            if core:
                summary_lines.append(f"- {ws['id']}: OGI-Core = {core['value']}%")
            else:
                summary_lines.append(f"- {ws['id']}: OGI-Core = not computable")

        append_to_log(date_str, "\n".join(summary_lines))

    except Exception as e:
        print(f"Extraction failed: {e}")
        # Write error facts file so the gap is documented
        write_facts(date_str, [], [f"Extraction error: {str(e)}"])
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OGI Evidence Extractor")
    parser.add_argument("--days", type=int, default=90, help="Measurement window in days")
    parser.add_argument("--workspace", type=str, help="Comma-separated workspace IDs")
    args = parser.parse_args()
    run(days=args.days, workspace_filter=args.workspace)
