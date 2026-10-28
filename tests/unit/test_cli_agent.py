import json
from urllib.error import HTTPError

from typer.testing import CliRunner

from sas_grid_migrator.cli.main import app


class Response:
    status = 200

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return b'{"available":true}'


def test_agent_api_prints_json_and_calls_read_endpoint(monkeypatch):
    requests = []

    def open_request(request, timeout):
        requests.append((request, timeout))
        return Response()

    monkeypatch.setattr("sas_grid_migrator.cli.agent.urlopen", open_request)
    result = CliRunner().invoke(app, ["agent", "api", "GET", "/integrations/talend/health"])

    assert result.exit_code == 0, result.output
    assert json.loads(result.stdout) == {"available": True}
    assert requests[0][0].full_url == "http://127.0.0.1:8000/api/integrations/talend/health"
    assert requests[0][0].method == "GET"


def test_agent_api_sends_json_write_and_reports_http_errors(monkeypatch):
    requests = []

    def open_request(request, timeout):
        requests.append(request)
        raise HTTPError(request.full_url, 403, "Forbidden", {}, None)

    monkeypatch.setattr("sas_grid_migrator.cli.agent.urlopen", open_request)
    result = CliRunner().invoke(
        app,
        [
            "agent",
            "api",
            "PATCH",
            "/projects/abc/plans/program/steps/step",
            "--data",
            '{"status":"approved","note":"reviewed"}',
        ],
    )

    assert result.exit_code != 0
    assert json.loads(requests[0].data) == {"status": "approved", "note": "reviewed"}
    assert "403" in result.stderr


def test_agent_cannot_change_talend_write_permission(monkeypatch):
    def unexpected_request(*_args, **_kwargs):
        raise AssertionError("permission update must stay in Settings UI")

    monkeypatch.setattr("sas_grid_migrator.cli.agent.request_api", unexpected_request)
    result = CliRunner().invoke(
        app,
        ["agent", "api", "PATCH", "/api/integrations/talend/permissions", "--data", '{"write_enabled":true}'],
    )

    assert result.exit_code != 0
    assert not isinstance(result.exception, AssertionError)


def test_agent_migrate_runs_pipeline_and_returns_machine_readable_result(tmp_path, monkeypatch):
    source = tmp_path / "batch"
    source.mkdir()
    calls = []

    def fake_request(server, method, path, data=None, file=None):
        calls.append((method, path, data))
        if path == "/projects":
            return {"id": "abc123"}
        return {"ok": True}

    monkeypatch.setattr("sas_grid_migrator.cli.agent.request_api", fake_request)
    result = CliRunner().invoke(app, ["agent", "migrate", str(source), "--name", "sample"])

    assert result.exit_code == 0, result.output
    assert [call[1] for call in calls] == [
        "/projects",
        "/projects/abc123/imports",
        "/projects/abc123/analyses",
        "/projects/abc123/dependencies",
        "/projects/abc123/plans",
        "/projects/abc123/exports",
    ]
    assert json.loads(result.stdout)["project"] == {"id": "abc123"}
