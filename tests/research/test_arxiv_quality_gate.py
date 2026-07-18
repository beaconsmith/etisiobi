from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "validate_arxiv_quality_gate.py"


def load_module():
    spec = importlib.util.spec_from_file_location("validate_arxiv_quality_gate", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_arxiv_quality_status_requires_all_articles_to_pass() -> None:
    module = load_module()

    assert module.quality_gate_status(20, 20) == "ARXIV_QUALITY_GATE_PASS"
    assert module.quality_gate_status(9, 20) == "ARXIV_QUALITY_GATE_PARTIAL"
    assert module.quality_gate_status(0, 20) == "ARXIV_QUALITY_GATE_FAIL"
    assert module.quality_gate_status(0, 0) == "ARXIV_QUALITY_GATE_FAIL"


if __name__ == "__main__":
    test_arxiv_quality_status_requires_all_articles_to_pass()
    print("ARXIV_QUALITY_GATE_TEST_PASS")
