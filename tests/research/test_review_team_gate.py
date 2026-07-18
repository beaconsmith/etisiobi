from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "validate_review_team_gate.py"


def load_module():
    spec = importlib.util.spec_from_file_location("validate_review_team_gate", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_trace(paper_dir: Path, roles: list[str]) -> None:
    rows = [
        {
            "role": role,
            "agent_id": f"{role}-agent",
            "status": "PASS",
            "summary": f"{role} found no blocker in this fixture.",
            "files_reviewed": ["main.tex"],
            "blocking_issues": [],
        }
        for role in roles
    ]
    (paper_dir / "review_team_trace.jsonl").write_text(
        "\n".join(json.dumps(row) for row in rows) + "\n",
        encoding="utf-8",
    )


def test_ready_paper_without_review_team_trace_fails() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paper_dir = root / "papers" / "candidate"
        paper_dir.mkdir(parents=True)
        (paper_dir / "final_submission_readiness_decision.md").write_text(
            "# Decision\n\nREADY_FOR_HUMAN_ARXIV_REVIEW\n",
            encoding="utf-8",
        )

        errors = module.validate_root(root)

    assert errors
    assert any("missing review_team_trace.jsonl" in error for error in errors)


def test_ready_paper_with_complete_review_team_trace_passes() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paper_dir = root / "papers" / "candidate"
        paper_dir.mkdir(parents=True)
        (paper_dir / "final_submission_readiness_decision.md").write_text(
            "# Decision\n\nStatus: READY_FOR_HUMAN_ARXIV_REVIEW\n",
            encoding="utf-8",
        )
        write_trace(paper_dir, list(module.REQUIRED_ROLES))

        errors = module.validate_root(root)

    assert errors == []


def test_non_ready_paper_does_not_require_review_team_trace() -> None:
    module = load_module()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        paper_dir = root / "papers" / "candidate"
        paper_dir.mkdir(parents=True)
        (paper_dir / "STATUS.md").write_text(
            "# Status\n\nNOT_READY_GLYPH_REVIEW_BLOCKED\n",
            encoding="utf-8",
        )

        errors = module.validate_root(root)

    assert errors == []


if __name__ == "__main__":
    test_ready_paper_without_review_team_trace_fails()
    test_ready_paper_with_complete_review_team_trace_passes()
    test_non_ready_paper_does_not_require_review_team_trace()
    print("REVIEW_TEAM_GATE_TEST_PASS")
