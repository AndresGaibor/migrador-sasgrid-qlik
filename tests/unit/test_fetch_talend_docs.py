import httpx
import pytest
from tools.fetch_talend_docs import (
    DOC_TEMPLATES,
    QlikLinkParser,
    component_lifecycle,
    component_navigation_subpages,
    component_subpage_url,
    component_urls,
    current_component_entries,
    discover_component_urls,
    enrich_index_record,
    fetch_route,
    get,
    is_component_page,
    is_component_root_url,
    is_official_url,
    overall_status,
    standard_properties_url_hints,
)


def test_official_urls_require_https_qlik_without_credentials_or_custom_port():
    assert is_official_url("https://help.qlik.com/talend/en-US/")
    assert not is_official_url("http://help.qlik.com/talend/en-US/")
    assert not is_official_url("https://user@help.qlik.com/talend/en-US/")
    assert not is_official_url("https://help.qlik.com:8443/talend/en-US/")
    assert not is_official_url("https://help.qlik.com:bad/talend/en-US/")


def test_component_urls_uses_official_jobs_and_routes_templates():
    assert component_urls(
        "tMap",
        [
            {"documentation_route": "Jobs"},
            {"documentation_route": "Jobs"},
        ],
        DOC_TEMPLATES,
    ) == [("Jobs", "https://help.qlik.com/talend/en-US/components/8.0/tmap")]
    assert component_urls("cAMQP", [{"documentation_route": "Routes"}], DOC_TEMPLATES) == [
        ("Routes", "https://help.qlik.com/talend/en-US/mediation-components/8.0/camqp")
    ]


def test_component_urls_prefers_the_official_index_path():
    page = "https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson"
    assert component_urls(
        "tFileInputJSON",
        [{"documentation_route": "Jobs"}],
        DOC_TEMPLATES,
        {"Jobs": {"tfileinputjson": page}},
    ) == [("Jobs", page)]


def test_missing_standard_pages_from_official_catalog_are_fetched_as_candidates():
    standard = "https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties"
    guide_index = {
        "components": [
            {
                "name": "tFilterColumns",
                "lifecycle_status": "current",
                "framework_codes": ["DI", "SPARK"],
                "documentation": {"configuration_pages": []},
            },
            {
                "name": "tMap",
                "lifecycle_status": "current",
                "framework_codes": ["DI", "SPARK"],
                "documentation": {
                    "configuration_pages": [{"title": "tMap Standard properties", "status": "ok"}]
                },
            },
        ]
    }
    catalog = {
        "components": {
            "tFilterColumns": {"doc_url": standard},
            "tMap": {
                "doc_url": "https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties"
            },
        }
    }

    hints = standard_properties_url_hints(catalog, guide_index)

    assert hints == {"tfiltercolumns": standard}
    assert component_urls(
        "tFilterColumns",
        [{"documentation_route": "Jobs"}],
        DOC_TEMPLATES,
        standard_urls=hints,
    ) == [
        ("Jobs", "https://help.qlik.com/talend/en-US/components/8.0/tfiltercolumns"),
        ("Jobs", standard),
    ]


def test_qlik_parser_finds_canonical_and_nested_component_settings_links():
    canonical = "https://help.qlik.com/talend/en-US/components/8.0/system/trunjob"
    standard = f"{canonical}-standard-properties"
    other = "https://help.qlik.com/talend/en-US/components/8.0/system/tsystem"
    parser = QlikLinkParser()
    parser.feed(
        f'<link rel="canonical" href="{canonical}"><nav><ul id="tree0">'
        f'<li><a href="{standard}">tRunJob Standard properties</a></li>'
        f'<li><a href="{other}">tSystem</a></li></ul></nav>'
    )

    assert parser.canonical_url == canonical
    assert [
        component_subpage_url(href, text, canonical, "tRunJob", "Jobs")
        for scope, text, href in parser.links
        if scope == "nav"
    ] == [standard, None]
    assert component_navigation_subpages(
        f'<nav><ul id="tree0"><li><a href="{standard}">tRunJob Standard properties</a>'
        f'</li><li><a href="{other}">tSystem</a></li></ul></nav>',
        canonical,
        "tRunJob",
        "Jobs",
    ) == [standard]


def test_component_lifecycle_uses_current_availability_records():
    assert component_lifecycle([{"family": "Databases/MySQL"}]) == "current"
    assert component_lifecycle([{"family": "Database/Legacy (Deprecated)"}]) == "deprecated"
    assert component_lifecycle([]) == "unknown"


def test_current_component_entries_use_only_the_current_guide_index():
    manifest = {
        "documentation_target": "Talend Studio 8.0 R2026-09",
        "components": [
            {
                "name": "tMap",
                "availability": [{"framework_code": "DI", "license_branding_codes": ["TP_ALL"]}],
            },
            {
                "name": "tFilterRow",
                "availability": [{"framework_code": "DI", "license_branding_codes": ["TP_ALL"]}],
            },
            {
                "name": "excluded_fixture",
                "availability": [
                    {"framework_code": "DI", "license_branding_codes": ["QTC_E", "QTC_P"]}
                ],
            },
            {
                "name": "tDeprecatedExample",
                "availability": [{"framework_code": "DI", "license_branding_codes": ["TP_ALL"]}],
            },
            {
                "name": "tOptionalFixture",
                "availability": [{"framework_code": "DI", "license_branding_codes": ["TP_ALL"]}],
            }
        ],
    }
    guide_index = {
        "documentation_target": "Talend Studio 8.0 R2026-09",
        "license_profile": {"code": "TP_ALL", "label": "Talend Data Fabric"},
        "components": [
            {"name": "tMap", "lifecycle_status": "current"},
            {"name": "excluded_fixture", "lifecycle_status": "current"},
            {"name": "tDeprecatedExample", "lifecycle_status": "deprecated"},
            {"name": "tOptionalFixture", "lifecycle_status": "optional_install"},
        ],
    }

    assert current_component_entries(manifest, guide_index) == {
        "tMap": [{"framework_code": "DI", "license_branding_codes": ["TP_ALL"]}],
    }
    with pytest.raises(ValueError, match="no coincide"):
        current_component_entries(
            manifest,
            {**guide_index, "documentation_target": "Talend Studio 8.0 R2026-08v1"},
        )


def test_enrich_index_records_lifecycle_and_known_redirects():
    record = {
        "routes": [
            {
                "requested_url": "https://help.qlik.com/old",
                "resolved_url": "https://help.qlik.com/new",
                "pages": [
                    {"url": "https://help.qlik.com/new", "status": "ok"},
                    {"url": "https://help.qlik.com/subpage", "status": "ok"},
                ],
            }
        ]
    }

    enriched = enrich_index_record(record, [{"family": "Databases/MySQL"}])

    assert enriched["availability_status"] == "listed"
    assert enriched["lifecycle_status"] == "current"
    assert enriched["fetcher_schema_version"] == 5
    assert enriched["routes"][0]["redirected"] is True
    assert enriched["routes"][0]["pages"][0]["redirected"] is True
    assert enriched["routes"][0]["pages"][1]["redirected"] is None
    assert enrich_index_record({"routes": []}, [])["lifecycle_status"] == "unknown"


def test_docs_only_component_uses_prefix_fallback_and_rejects_unsafe_name():
    assert component_urls("cDemo", [], DOC_TEMPLATES)[0][0] == "Routes"
    with pytest.raises(ValueError, match="Invalid Qlik component name"):
        component_urls("../secret", [], DOC_TEMPLATES)


def test_component_subpage_filter_keeps_framework_settings_only_for_component():
    page = "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput"
    assert component_subpage_url(
        "/talend/en-US/components/8.0/Content/Resources/attachments/tembeddingai-tpineconeclient_phone-review-files.zip",
        "tEmbeddingAI attachment",
        "https://help.qlik.com/talend/en-US/components/8.0/tembeddingai",
        "tEmbeddingAI",
        "Jobs",
    ) is None
    assert (
        component_subpage_url(
            "/talend/en-US/components/8.0/tfixedflowinput-properties-for-apache-spark-batch",
            "Spark Batch properties",
            page,
            "tFixedFlowInput",
            "Jobs",
        )
        == "https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput-properties-for-apache-spark-batch"
    )
    assert (
        component_subpage_url(
            "/talend/en-US/components/8.0/tfixedflowinput-examples",
            "Examples",
            page,
            "tFixedFlowInput",
            "Jobs",
        )
        is None
    )
    assert (
        component_subpage_url(
            "/talend/en-US/components/8.0/tmap-standard-properties",
            "Standard properties",
            page,
            "tFixedFlowInput",
            "Jobs",
        )
        is None
    )
    assert (
        component_subpage_url(
            "/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties",
            "tFilterColumns Standard properties",
            "https://help.qlik.com/talend/en-US/components/8.0/tfiltercolumns",
            "tFilterColumns",
            "Jobs",
        )
        == "https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties"
    )
    assert (
        component_subpage_url(
            "/talend/en-US/components/8.0/processing/tfiltercolumns-properties-for-apache-spark-streaming",
            "tFilterColumns properties for Apache Spark Streaming (deprecated)",
            "https://help.qlik.com/talend/en-US/components/8.0/tfiltercolumns",
            "tFilterColumns",
            "Jobs",
        )
        is None
    )
    assert (
        component_subpage_url(
            "/talend/en-US/components/8.0/json/tfileinputjson-standard-properties",
            "Standard properties",
            "https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson",
            "tFileInputJSON",
            "Jobs",
        )
        == "https://help.qlik.com/talend/en-US/components/8.0/json/tfileinputjson-standard-properties"
    )
    assert (
        component_subpage_url(
            "https://example.com/tfixedflowinput-properties",
            "properties",
            page,
            "tFixedFlowInput",
            "Jobs",
        )
        is None
    )


def test_discover_component_urls_from_official_family_index():
    base = "https://help.qlik.com/talend/en-US/components/8.0/"
    pages = {
        base: '<nav><ul id="tree0"><li><a href="/talend/en-US/components/8.0/json">JSON</a></li><li><a href="/talend/en-US/components/8.0/mysql">MySQL</a></li></ul></nav>',
        f"{base}json": '<div id="topicContent"><a href="/talend/en-US/components/8.0/json/json-component">JSON components</a></div>',
        f"{base}json/json-component": '<div id="topicContent"><a href="/talend/en-US/components/8.0/json/tfileinputjson">tFileInputJSON</a></div>',
    }

    def handler(request):
        if str(request.url) == f"{base}mysql":
            raise AssertionError("Discovery should stop after resolving its target")
        return httpx.Response(200, text=pages[str(request.url)])

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = discover_component_urls(
            client, "Jobs", {"tFileInputJSON"}, {"tFileInputJSON"}, delay=0
        )

    assert result == {"tfileinputjson": f"{base}json/tfileinputjson"}


def test_component_page_validation_and_route_status_aggregation():
    assert is_component_page("tMap", "tMap Standard properties", "")
    assert not is_component_page("tMap", "About components", "Generic documentation")
    assert overall_status([{"status": "ok"}, {"status": "not_found"}]) == "partial"
    assert overall_status([{"status": "not_found"}]) == "not_found"
    assert overall_status([{"status": "page_mismatch"}]) == "page_mismatch"


def test_fetch_route_records_redirects_for_component_pages(monkeypatch):
    monkeypatch.setattr(
        "tools.fetch_talend_docs.topic",
        lambda html, url, name, route: ("tMap", "Map rows.", []),
    )
    requested = "https://help.qlik.com/talend/en-US/components/8.0/old-tmap"
    resolved = "https://help.qlik.com/talend/en-US/components/8.0/tmap"

    def handler(request):
        if str(request.url) == requested:
            return httpx.Response(301, headers={"location": resolved})
        return httpx.Response(
            200,
            text='<div id="topicContent"><h1>tMap</h1><p>Map rows.</p></div>',
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        route, _ = fetch_route(client, "tMap", "Jobs", requested, delay=0)

    assert route["status"] == "ok"
    assert route["redirected"] is True
    assert route["requested_url"] == requested
    assert route["resolved_url"] == resolved
    assert route["pages"][0]["redirected"] is True


def test_fetch_route_uses_official_canonical_url(monkeypatch):
    monkeypatch.setattr(
        "tools.fetch_talend_docs.topic",
        lambda html, url, name, route: (
            "tSystem",
            "System commands.",
            ["https://help.qlik.com/talend/en-US/components/8.0/system/tsystem"],
        ),
    )
    requested = "https://help.qlik.com/talend/en-US/components/8.0/tsystem"
    canonical = "https://help.qlik.com/talend/en-US/components/8.0/system/tsystem"
    assert is_component_root_url(canonical, "tSystem", "Jobs")
    assert not is_component_root_url(f"{canonical}-standard-properties", "tSystem", "Jobs")

    def handler(request):
        return httpx.Response(
            200,
            text=f'<link rel="canonical" href="{canonical}"><div id="topicContent">ok</div>',
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        route, _ = fetch_route(client, "tSystem", "Jobs", requested, delay=0)

    assert route["status"] == "ok"
    assert route["resolved_url"] == requested
    assert route["pages"][0]["url"] == canonical
    assert route["pages"][0]["canonical_url"] == canonical
    assert route["pages"][0]["redirected"] is False
    assert len(route["pages"]) == 1


def test_fetch_route_ignores_external_canonical_url(monkeypatch):
    monkeypatch.setattr(
        "tools.fetch_talend_docs.topic",
        lambda html, url, name, route: ("tSystem", "System commands.", []),
    )
    requested = "https://help.qlik.com/talend/en-US/components/8.0/tsystem"

    def handler(request):
        return httpx.Response(
            200,
            text='<link rel="canonical" href="https://example.com/private">'
            '<div id="topicContent">ok</div>',
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        route, _ = fetch_route(client, "tSystem", "Jobs", requested, delay=0)

    assert route["pages"][0]["url"] == requested
    assert "canonical_url" not in route["pages"][0]


def test_fetch_route_ignores_unrelated_official_canonical_url(monkeypatch):
    monkeypatch.setattr(
        "tools.fetch_talend_docs.topic",
        lambda html, url, name, route: ("tMap", "Map rows.", []),
    )
    requested = "https://help.qlik.com/talend/en-US/components/8.0/tmap"
    canonical = "https://help.qlik.com/talend/en-US/components/8.0/maprdb/tmaprdbclose"

    def handler(request):
        return httpx.Response(
            200,
            text=f'<link rel="canonical" href="{canonical}"><div id="topicContent">Map rows.</div>',
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        route, _ = fetch_route(client, "tMap", "Jobs", requested, delay=0)

    assert route["pages"][0]["url"] == requested
    assert "canonical_url" not in route["pages"][0]


def test_get_follows_only_https_qlik_redirects():
    seen = []

    def handler(request):
        seen.append(str(request.url))
        if request.url.path == "/start":
            return httpx.Response(302, headers={"location": "https://example.com/private"})
        return httpx.Response(200, text="ok")

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        response = get(client, "https://help.qlik.com/start")

    assert response is not None and response.status_code == 302
    assert seen == ["https://help.qlik.com/start"]


def test_get_follows_same_origin_official_redirects():
    seen = []

    def handler(request):
        seen.append(str(request.url))
        if request.url.path == "/start":
            return httpx.Response(301, headers={"location": "/components/8.0/tmap"})
        return httpx.Response(200, text="ok")

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        response = get(client, "https://help.qlik.com/start")

    assert response is not None and response.status_code == 200
    assert seen == [
        "https://help.qlik.com/start",
        "https://help.qlik.com/components/8.0/tmap",
    ]
