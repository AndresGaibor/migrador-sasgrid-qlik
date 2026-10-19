import json
import sys
from types import SimpleNamespace

from tools import fetch_talend_docs


def test_only_refreshes_selected_doc_and_preserves_full_index(tmp_path, monkeypatch):
    root = tmp_path
    catalog = root / "rules" / "talend" / "components.json"
    catalog.parent.mkdir(parents=True)
    catalog.write_text(json.dumps({"components": {"tFilterRow": {}, "tMap": {}}}))

    out = root / "docs"
    out.mkdir()
    (out / "tMap.md").write_text("stale")
    (out / "index.json").write_text(
        json.dumps(
            [
                {"name": "tFilterRow", "status": "ok"},
                {"name": "tMap", "status": "cached"},
            ]
        )
    )
    monkeypatch.setattr(fetch_talend_docs, "ROOT", root)
    monkeypatch.setattr(fetch_talend_docs, "OUT", out)
    requested = []

    def fake_get(_client, url):
        requested.append(url)
        return SimpleNamespace(status_code=200, text="html")

    monkeypatch.setattr(fetch_talend_docs, "get", fake_get)
    monkeypatch.setattr(fetch_talend_docs, "topic", lambda *_: ("fresh docs", []))
    monkeypatch.setattr(
        sys, "argv", ["fetch_talend_docs.py", "--only", "tMap", "--refresh", "--delay", "0"]
    )

    fetch_talend_docs.main()

    assert requested == [fetch_talend_docs.BASE.format(v="8.0") + "tmap"]
    assert "fresh docs" in (out / "tMap.md").read_text()
    index = {row["name"]: row for row in json.loads((out / "index.json").read_text())}
    assert set(index) == {"tFilterRow", "tMap"}
    assert index["tFilterRow"] == {"name": "tFilterRow", "status": "ok"}
    assert index["tMap"]["status"] == "ok"


def test_get_follows_redirects():
    import httpx

    requested = []

    def respond(request):
        requested.append(request.url.path)
        if request.url.path == "/redirect":
            return httpx.Response(302, headers={"Location": "/target"})
        return httpx.Response(200)

    with httpx.Client(transport=httpx.MockTransport(respond)) as client:
        response = fetch_talend_docs.get(client, "https://example.test/redirect")

    assert response is not None and response.status_code == 200
    assert requested == ["/redirect", "/target"]
