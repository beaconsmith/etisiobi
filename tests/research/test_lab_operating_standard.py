from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "validate_lab_standard.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_lab_standard", SCRIPT)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_lab_standard_gate_passes() -> None:
    validator = load_validator()
    assert validator.main() == 0

