from apps.api.main import app as api
from fastapi.testclient import TestClient
from typer.testing import CliRunner

from sas_grid_migrator import __version__
from sas_grid_migrator.cli.main import app as cli


def test_cli_version():
    assert CliRunner().invoke(cli, ["version"]).stdout.strip() == __version__


def test_api_health():
    assert TestClient(api).get("/api/health").json()["status"] == "ok"
