"""Pipeline completo por CLI sobre el corpus: import → analyze → deps → plan."""

import json
import re
from pathlib import Path

from typer.testing import CliRunner

from sas_grid_migrator.cli.main import app

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"


def test_full_pipeline(tmp_path, monkeypatch):
    monkeypatch.setenv("SGM_DATA_DIR", str(tmp_path / "data"))
    r = CliRunner()
    res = r.invoke(app, ["import", str(FIXTURES), "-n", "corpus"])
    assert res.exit_code == 0, res.output
    pid = re.search(r"\b([0-9a-f]{12})\b", res.output).group(1)
    for cmd in ("analyze", "deps"):
        res = r.invoke(app, [cmd, pid])
        assert res.exit_code == 0, res.output
    out = tmp_path / "out"
    res = r.invoke(app, ["plan", pid, "-o", str(out)])
    assert res.exit_code == 0 and "planes" in res.output, res.output
    assert (out / "index.md").exists() and (out / "steps.csv").exists()
    plan = json.loads((out / "p0_clientes_activos.json").read_text())
    assert plan["steps"] and not any(s["verified"] for s in plan["steps"])
    assert r.invoke(app, ["plan", "inexistente"]).exit_code != 0
