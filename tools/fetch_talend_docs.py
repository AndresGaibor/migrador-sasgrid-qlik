# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "beautifulsoup4", "markdownify"]
# ///
"""Fetch official Talend component pages and linked configuration topics into a local cache."""

import argparse
import json
import re
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit, urlunsplit

import httpx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "reference" / "talend"
INVENTORY = ROOT / "rules" / "talend" / "official-component-inventory.json"
GUIDE_INDEX = ROOT / "rules" / "talend" / "component-documentation-index.json"
CATALOG = ROOT / "rules" / "talend" / "components.json"
DOC_TEMPLATES = {
    "Jobs": "https://help.qlik.com/talend/en-US/components/8.0/{name}",
    "Routes": "https://help.qlik.com/talend/en-US/mediation-components/8.0/{name}",
}
DOC_INDEX_URLS = {
    route: template.split("{name}", 1)[0] for route, template in DOC_TEMPLATES.items()
}
UNRELATED = re.compile(r"scenario|example|related|deprecated", re.IGNORECASE)
MAX_PAGES_PER_ROUTE = 250
MAX_INDEX_PAGES = 500
MAX_REDIRECTS = 5
FETCHER_SCHEMA_VERSION = 5
CURRENT_FRAMEWORKS = {"DI", "SPARK", "STRUCTUREDSTREAMING", "CAMEL"}
LICENSE_PROFILE_CODE = "TP_ALL"


class QlikLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonical_url: str | None = None
        self.nav_depth = 0
        self.topic_depth = 0
        self.anchor: tuple[str, str, list[str]] | None = None
        self.links: list[tuple[str, str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "link" and "canonical" in (attributes.get("rel") or "").casefold().split():
            href = attributes.get("href")
            if isinstance(href, str):
                self.canonical_url = href
        if tag in {"nav", "ul"} and attributes.get("id") == "tree0":
            self.nav_depth = 1
        elif tag in {"nav", "ul"} and self.nav_depth:
            self.nav_depth += 1
        if tag == "div" and attributes.get("id") == "topicContent":
            self.topic_depth = 1
        elif tag == "div" and self.topic_depth:
            self.topic_depth += 1
        href = attributes.get("href")
        if tag == "a" and isinstance(href, str) and (self.nav_depth or self.topic_depth):
            self.anchor = ("nav" if self.nav_depth else "topic", href, [])

    def handle_data(self, data: str) -> None:
        if self.anchor:
            self.anchor[2].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self.anchor:
            scope, href, text = self.anchor
            self.links.append((scope, " ".join(" ".join(text).split()), href))
            self.anchor = None
        if tag in {"nav", "ul"} and self.nav_depth:
            self.nav_depth -= 1
        if tag == "div" and self.topic_depth:
            self.topic_depth -= 1


def is_official_url(url: str) -> bool:
    parsed = urlsplit(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname != "help.qlik.com"
        or parsed.username
        or parsed.password
    ):
        return False
    try:
        return parsed.port in (None, 443)
    except ValueError:
        return False


def get(client: httpx.Client, url: str) -> httpx.Response | None:
    for attempt in range(3):
        current = url
        response = None
        try:
            for _ in range(MAX_REDIRECTS + 1):
                response = client.get(current, follow_redirects=False, timeout=30)
                if response.status_code in (429, 503):
                    break
                location = response.headers.get("location")
                if response.status_code not in (301, 302, 303, 307, 308) or not location:
                    return response
                destination = urljoin(current, location)
                if not is_official_url(destination):
                    return response
                current = destination
            if response is not None and response.status_code not in (429, 503):
                return response
            time.sleep(5 * (attempt + 1))
        except httpx.HTTPError:
            time.sleep(2 * (attempt + 1))
    return None


def component_lifecycle(availability: list[dict]) -> str:
    if not availability:
        return "unknown"
    deprecated = []
    for record in availability:
        families = [
            family.strip().casefold()
            for family in str(record.get("family", "")).split("|")
            if family.strip()
        ]
        deprecated.append(bool(families) and all("(deprecated)" in family for family in families))
    return "deprecated" if all(deprecated) else "current"


def enrich_index_record(record: dict, availability: list[dict]) -> dict:
    record["availability_status"] = (
        "listed" if availability else "not_listed_in_current_availability"
    )
    record["lifecycle_status"] = component_lifecycle(availability)
    record["fetcher_schema_version"] = FETCHER_SCHEMA_VERSION
    for route in record.get("routes", []):
        requested, resolved = route.get("requested_url"), route.get("resolved_url")
        route["redirected"] = (
            requested != resolved
            if isinstance(requested, str) and isinstance(resolved, str)
            else None
        )
        for index, page in enumerate(route.get("pages", [])):
            if "requested_url" in page:
                continue
            if index == 0 and isinstance(requested, str) and isinstance(resolved, str):
                page["requested_url"] = requested
                page["resolved_url"] = resolved
                page["redirected"] = requested != resolved
            else:
                page["requested_url"] = None
                page["resolved_url"] = page.get("url")
                page["redirected"] = None
    return record


def component_urls(
    name: str,
    availability: list[dict],
    templates: dict[str, str],
    documentation_urls: dict[str, dict[str, str]] | None = None,
    standard_urls: dict[str, str] | None = None,
) -> list[tuple[str, str]]:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]+", name):
        raise ValueError(f"Invalid Qlik component name: {name!r}")
    routes: set[str] = set()
    for item in availability:
        route = item.get("documentation_route")
        if isinstance(route, str) and route in templates:
            routes.add(route)
    if not routes:
        routes = {"Routes" if name.startswith("c") else "Jobs"}
    result = []
    for route in sorted(routes):
        template = templates.get(route)
        if not isinstance(template, str):
            raise TypeError(f"Missing official documentation template for route {route}")
        if template != DOC_TEMPLATES[route]:
            raise ValueError(f"Unexpected documentation template for route {route}")
        url_map = (documentation_urls or {}).get(route, {})
        indexed = url_map.get(name.casefold())
        primary = indexed or template.format(name=name.lower())
        result.append((route, primary))
        standard = (standard_urls or {}).get(name.casefold())
        if (
            route == "Jobs"
            and standard
            and standard != primary
            and is_official_url(standard)
            and route_documentation_url(standard, DOC_INDEX_URLS[route], route)
        ):
            result.append((route, standard))
    return result


def route_documentation_url(href: str, current_url: str, route: str) -> str | None:
    absolute = urljoin(current_url, href)
    parsed = urlsplit(absolute)
    if not is_official_url(absolute):
        return None
    prefix_path = urlsplit(DOC_INDEX_URLS[route]).path
    if not parsed.path.startswith(prefix_path):
        return None
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", ""))


def standard_properties_url_hints(
    catalog: dict[str, Any], guide_index: dict[str, Any]
) -> dict[str, str]:
    catalog_components = catalog.get("components", {})
    if not isinstance(catalog_components, dict):
        return {}
    hints = {}
    for item in guide_index.get("components", []):
        if item.get("lifecycle_status") != "current" or "DI" not in item.get("framework_codes", []):
            continue
        documentation = item.get("documentation", {})
        pages = documentation.get("configuration_pages", [])
        if any(
            page.get("status") == "ok"
            and "standard properties" in str(page.get("title", "")).casefold()
            for page in pages
        ):
            continue
        catalog_item = catalog_components.get(item["name"], {})
        url = catalog_item.get("doc_url") if isinstance(catalog_item, dict) else None
        path = urlsplit(url).path.casefold() if isinstance(url, str) else ""
        if (
            isinstance(url, str)
            and is_official_url(url)
            and item["name"].casefold() in path
            and path.endswith("-standard-properties")
            and route_documentation_url(url, DOC_INDEX_URLS["Jobs"], "Jobs")
        ):
            hints[item["name"].casefold()] = url
    return hints


def is_component_topic_url(url: str, names: set[str]) -> bool:
    leaf = urlsplit(url).path.rstrip("/").rsplit("/", 1)[-1].casefold()
    return any(
        leaf == name.casefold() or leaf.startswith(f"{name.casefold()}-") for name in names
    )


def discover_component_urls(
    client: httpx.Client,
    route: str,
    target_names: set[str],
    known_names: set[str],
    delay: float,
) -> dict[str, str]:
    response = get(client, DOC_INDEX_URLS[route])
    time.sleep(delay)
    if response is None or response.status_code != 200:
        return {}

    target_by_key = {name.casefold(): name for name in target_names}
    known_keys = {name.casefold() for name in known_names}
    discovered: dict[str, str] = {}
    category_urls: set[str] = set()
    listing_urls: set[str] = set()

    def collect(html: str, current_url: str, *, root: bool = False) -> None:
        parser = QlikLinkParser()
        parser.feed(html)
        prefix_path = urlsplit(DOC_INDEX_URLS[route]).path
        for scope, text, href in parser.links:
            url = route_documentation_url(href, current_url, route)
            if not url:
                continue
            name = target_by_key.get(text.casefold())
            if name:
                discovered.setdefault(name.casefold(), url)
                continue
            path = urlsplit(url).path
            relative = path[len(prefix_path) :].strip("/")
            parts = relative.split("/") if relative else []
            leaf = parts[-1].casefold() if parts else ""
            if UNRELATED.search(f"{text} {leaf}"):
                continue
            if leaf.endswith("-component"):
                listing_urls.add(url)
            elif (
                len(parts) == 1
                and leaf != "about"
                and not is_component_topic_url(url, known_names)
                and (
                    (scope == "nav" and text.casefold() not in known_keys)
                    or (not root and scope == "topic")
                )
            ):
                category_urls.add(url)

    collect(response.text, str(response.url), root=True)
    visited_categories = {str(response.url)}
    visited_listings: set[str] = set()

    def collect_listings() -> None:
        for current_url in sorted(listing_urls - visited_listings):
            if len(discovered) >= len(target_names):
                break
            visited_listings.add(current_url)
            page = get(client, current_url)
            time.sleep(delay)
            if page is None or page.status_code != 200:
                continue
            parser = QlikLinkParser()
            parser.feed(page.text)
            for _, text, href in parser.links:
                name = target_by_key.get(text.casefold())
                url = route_documentation_url(href, str(page.url), route)
                if name and url:
                    discovered.setdefault(name.casefold(), url)

    collect_listings()
    for _ in range(MAX_INDEX_PAGES):
        if len(discovered) >= len(target_names):
            break
        pending = sorted(category_urls - visited_categories)
        if not pending:
            break
        current_url = pending[0]
        visited_categories.add(current_url)
        page = get(client, current_url)
        time.sleep(delay)
        if page is not None and page.status_code == 200:
            collect(page.text, str(page.url))
            collect_listings()
    return discovered


def component_subpage_url(
    href: str, text: str, current_url: str, name: str, route: str
) -> str | None:
    absolute = urljoin(current_url, href)
    parsed = urlsplit(absolute)
    if parsed.scheme != "https" or parsed.hostname != "help.qlik.com":
        return None
    root = "mediation-components" if route == "Routes" else "components"
    prefix = f"/talend/en-US/{root}/8.0/"
    if (
        not parsed.path.startswith(prefix)
        or "/content/resources/" in parsed.path.lower()
        or UNRELATED.search(f"{text} {parsed.path}")
    ):
        return None
    relative = parsed.path[len(prefix) :].strip("/")
    leaf = relative.rsplit("/", 1)[-1].lower()
    key = name.casefold()
    if leaf != key and not leaf.startswith(f"{key}-"):
        return None
    return urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", ""))


def component_navigation_subpages(html: str, url: str, name: str, route: str) -> list[str]:
    parser = QlikLinkParser()
    parser.feed(html)
    return sorted(
        {
            link
            for scope, text, href in parser.links
            if scope == "nav"
            and (link := component_subpage_url(href, text, url, name, route)) is not None
        }
    )


def topic(html: str, url: str, name: str, route: str) -> tuple[str, str, list[str]]:
    from bs4 import BeautifulSoup  # pyright: ignore[reportMissingImports]
    from markdownify import markdownify  # pyright: ignore[reportMissingImports]

    soup = BeautifulSoup(html, "html.parser")
    node = soup.find(id="topicContent")
    if node is None:
        return "", "", []
    heading = node.find(["h1", "h2"]) or soup.find("title")
    title = heading.get_text(" ", strip=True) if heading else ""
    links = set(component_navigation_subpages(html, url, name, route))
    for anchor in node.select("a[href]"):
        href = anchor.get("href")
        if not isinstance(href, str):
            continue
        link = component_subpage_url(href, anchor.get_text(" ", strip=True), url, name, route)
        if link:
            links.add(link)
    for tag in node.select("script,style,.feedback,nav"):
        tag.decompose()
    markdown = markdownify(str(node), heading_style="ATX", strip=["img"])
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    markdown = re.sub(r"Did this page help you\?.*", "", markdown, flags=re.DOTALL).strip()
    return title, markdown, sorted(links)


def is_component_page(name: str, title: str, markdown: str) -> bool:
    return name.casefold() in title.casefold()


def is_component_canonical_url(url: str, name: str, title: str, route: str) -> bool:
    if not is_official_url(url) or not is_component_page(name, title, ""):
        return False
    root = "mediation-components" if route == "Routes" else "components"
    if not urlsplit(url).path.startswith(f"/talend/en-US/{root}/8.0/"):
        return False
    leaf = urlsplit(url).path.rstrip("/").rsplit("/", 1)[-1].casefold()
    slug = name.casefold()
    if leaf == slug:
        return True
    if leaf.startswith(f"{slug}-"):
        suffix = leaf[len(slug) + 1 :]
        return suffix in {"component", "standard-properties"} or suffix.startswith(
            "properties-for-"
        )
    return False


def is_component_root_url(url: str, name: str, route: str) -> bool:
    if not is_official_url(url):
        return False
    root = "mediation-components" if route == "Routes" else "components"
    prefix = f"/talend/en-US/{root}/8.0/"
    path = urlsplit(url).path
    if not path.startswith(prefix):
        return False
    leaf = path.rstrip("/").rsplit("/", 1)[-1].casefold()
    return leaf == name.casefold()


def fetch_route(
    client: httpx.Client, name: str, route: str, url: str, delay: float
) -> tuple[dict, list[str]]:
    response = get(client, url)
    time.sleep(delay)
    if response is None:
        return {
            "route": route,
            "status": "network_error",
            "requested_url": url,
            "redirected": None,
            "pages": [],
        }, []
    resolved_url = str(response.url)
    redirected = resolved_url != url

    def page_result(
        requested: str,
        resolved: str | None,
        status: str,
        title: str | None = None,
        canonical: str | None = None,
    ) -> dict:
        canonical = (
            canonical
            if canonical and title and is_component_canonical_url(canonical, name, title, route)
            else None
        )
        record = {
            "url": canonical or resolved or requested,
            "status": status,
            "requested_url": requested,
            "resolved_url": resolved,
            "redirected": resolved != requested if resolved else None,
        }
        if title:
            record["title"] = title
        if canonical:
            record["canonical_url"] = canonical
        return record

    if response.status_code != 200:
        location = response.headers.get("location")
        target = urljoin(url, location) if location else ""
        status = (
            "not_found"
            if response.status_code == 404
            else "external_redirect"
            if target and not is_official_url(target)
            else f"http_{response.status_code}"
        )
        return {
            "route": route,
            "status": status,
            "requested_url": url,
            "resolved_url": resolved_url,
            "redirected": redirected,
            "pages": [page_result(url, resolved_url, status)],
        }, []

    title, markdown, links = topic(response.text, resolved_url, name, route)
    if not markdown:
        status = "no_topic_content"
        return {
            "route": route,
            "status": status,
            "requested_url": url,
            "resolved_url": resolved_url,
            "redirected": redirected,
            "pages": [page_result(url, resolved_url, status)],
        }, []
    if not is_component_page(name, title, markdown):
        status = "page_mismatch"
        return {
            "route": route,
            "status": status,
            "requested_url": url,
            "resolved_url": resolved_url,
            "redirected": redirected,
            "title": title,
            "pages": [page_result(url, resolved_url, status, title)],
        }, []

    parser = QlikLinkParser()
    parser.feed(response.text)
    canonical = parser.canonical_url
    pages = [page_result(url, resolved_url, "ok", title, canonical)]
    parts = [f"<!-- fuente: {response.url} · versión 8.0 -->\n{markdown}"]
    root_pages = {url, resolved_url}
    if (
        canonical
        and is_component_canonical_url(canonical, name, title, route)
        and is_component_root_url(canonical, name, route)
    ):
        root_pages.add(canonical)

    def page_key(page_url: str) -> str:
        return route_documentation_url(page_url, url, route) or page_url

    queued = {page_key(root) for root in root_pages}
    queue = deque(link for link in links if page_key(link) not in queued)
    queued.update(page_key(link) for link in queue)
    partial = False
    truncated = False
    while queue:
        if len(pages) >= MAX_PAGES_PER_ROUTE:
            truncated = True
            break
        sub_url = queue.popleft()
        sub = get(client, sub_url)
        time.sleep(delay)
        if sub is None:
            pages.append(page_result(sub_url, None, "network_error"))
            partial = True
            continue
        if sub.status_code != 200:
            sub_status = "not_found" if sub.status_code == 404 else f"http_{sub.status_code}"
            pages.append(page_result(sub_url, str(sub.url), sub_status))
            partial = True
            continue
        sub_title, sub_markdown, more = topic(sub.text, str(sub.url), name, route)
        if not sub_markdown:
            pages.append(page_result(sub_url, str(sub.url), "no_topic_content"))
            partial = True
            continue
        sub_parser = QlikLinkParser()
        sub_parser.feed(sub.text)
        pages.append(page_result(sub_url, str(sub.url), "ok", sub_title, sub_parser.canonical_url))
        parts.append(f"\n\n---\n<!-- fuente: {sub.url} -->\n{sub_markdown}")
        for link in more:
            key = page_key(link)
            if key not in queued:
                queued.add(key)
                queue.append(link)
    if queue:
        truncated = True
    status = "truncated" if truncated else "partial" if partial else "ok"
    result = {
        "route": route,
        "status": status,
        "requested_url": url,
        "resolved_url": resolved_url,
        "redirected": redirected,
        "pages": pages,
    }
    if truncated:
        result["unfetched_links"] = len(queue)
    return result, parts


def overall_status(routes: list[dict]) -> str:
    statuses = [route["status"] for route in routes]
    if statuses and all(status == "ok" for status in statuses):
        return "ok"
    if any(status in ("ok", "partial", "truncated") for status in statuses):
        return "partial"
    if statuses and all(status == "not_found" for status in statuses):
        return "not_found"
    if statuses and all(status == "page_mismatch" for status in statuses):
        return "page_mismatch"
    return "unavailable"


def fetch_component(
    client: httpx.Client,
    name: str,
    availability: list[dict],
    templates: dict[str, str],
    inventory_version: str,
    documentation_target: str,
    delay: float,
    refresh: bool,
    previous: dict | None = None,
    documentation_urls: dict[str, dict[str, str]] | None = None,
    standard_urls: dict[str, str] | None = None,
) -> dict:
    target = OUT / f"{name}.md"
    if (
        not refresh
        and target.exists()
        and previous
        and previous.get("status") == "ok"
        and previous.get("fetcher_schema_version") == FETCHER_SCHEMA_VERSION
        and previous.get("source_inventory_version") == inventory_version
        and previous.get("documentation_target") == documentation_target
    ):
        return {**previous, "cache_hit": True}

    route_results = []
    content = []
    candidates = component_urls(name, availability, templates, documentation_urls, standard_urls)
    for route, url in candidates:
        result, parts = fetch_route(client, name, route, url, delay)
        route_results.append(result)
        content.extend(parts)
    status = overall_status(route_results)
    if content:
        temporary = target.with_suffix(".md.tmp")
        temporary.write_text("\n".join(content) + "\n", encoding="utf-8")
        temporary.replace(target)
    return {
        "name": name,
        "status": status,
        "availability_status": "listed" if availability else "not_listed_in_current_availability",
        "lifecycle_status": component_lifecycle(availability),
        "source_inventory_version": inventory_version,
        "documentation_target": documentation_target,
        "fetcher_schema_version": FETCHER_SCHEMA_VERSION,
        "routes": route_results,
        "pages": sum(len(result["pages"]) for result in route_results),
        "bytes": target.stat().st_size if target.exists() else 0,
        "stale_file_preserved": not content and target.exists(),
    }


def current_component_entries(
    manifest: dict[str, Any], guide_index: dict[str, Any]
) -> dict[str, list[dict[str, Any]]]:

    if guide_index.get("documentation_target") != manifest.get("documentation_target"):
        raise ValueError("el índice de guías no coincide con el target documental")
    if guide_index.get("license_profile", {}).get("code") != LICENSE_PROFILE_CODE:
        raise ValueError("el índice de guías no coincide con el perfil de licencia")
    current_names = {
        item["name"]
        for item in guide_index["components"]
        if item.get("lifecycle_status") == "current"
    }
    return {
        item["name"]: records
        for item in manifest["components"]
        if item["name"] in current_names
        and (
            records := [
                record
                for record in item["availability"]
                if record.get("framework_code") in CURRENT_FRAMEWORKS
                and LICENSE_PROFILE_CODE in record.get("license_branding_codes", [])
            ]
        )
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--delay", type=float, default=0.3)
    parser.add_argument("--only", default="", help="coma-separado; por defecto, todo el inventario")
    parser.add_argument(
        "--refresh", action="store_true", help="vuelve a descargar aunque haya caché válida"
    )
    args = parser.parse_args()
    if not 1 <= args.workers <= 16 or not 0 <= args.delay <= 5:
        parser.error("--workers debe estar entre 1 y 16 y --delay entre 0 y 5")

    try:
        manifest = json.loads(INVENTORY.read_text(encoding="utf-8"))
        inventory_version = manifest["availability_snapshot_version"]
        templates = manifest["source"]["component_documentation_templates"]
        documentation_target = manifest["documentation_target"]
        guide_index = json.loads(GUIDE_INDEX.read_text(encoding="utf-8"))
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        entries = current_component_entries(manifest, guide_index)
        standard_urls = standard_properties_url_hints(catalog, guide_index)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        parser.error(f"no se pudo leer el inventario/índice oficial vigente: {exc}")
    OUT.mkdir(parents=True, exist_ok=True)
    index_path = OUT / "index.json"
    previous = {}
    if index_path.exists():
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
            if not isinstance(index, list) or any(
                not isinstance(item, dict) or not isinstance(item.get("name"), str)
                for item in index
            ):
                raise ValueError("index.json debe ser una lista de registros con name")
            previous = {item["name"]: item for item in index if item["name"] in entries}
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            parser.error(f"no se pudo leer el índice local {index_path}: {exc}")
    names = sorted(entries)
    if args.only:
        selected = {name.strip() for name in args.only.split(",") if name.strip()}
        unknown = selected - set(names)
        if unknown:
            parser.error(
                f"nombres fuera del inventario oficial y caché: {', '.join(sorted(unknown))}"
            )
        names = sorted(selected)

    headers = {"User-Agent": "sgm-docs-fetch/1.0 (uso local; contacto: repo migrador-sasgrid-qlik)"}
    results = []
    with httpx.Client(headers=headers, follow_redirects=False) as client:
        needs_discovery = (
            set(names)
            if args.refresh or not previous
            else {name for name in names if previous.get(name, {}).get("status") != "ok"}
        )
        targets_by_route: dict[str, set[str]] = {}
        for name in needs_discovery:
            for route, _ in component_urls(
                name, entries.get(name, []), templates, standard_urls=standard_urls
            ):
                targets_by_route.setdefault(route, set()).add(name)
        documentation_urls = {}
        for route, target_names in sorted(targets_by_route.items()):
            found = discover_component_urls(
                client, route, target_names, set(names) | set(previous), args.delay
            )
            documentation_urls[route] = found
            print(
                f"Qlik {route} index resolved {len(found)}/{len(target_names)} component pages",
                flush=True,
            )

        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = pool.map(
                lambda name: fetch_component(
                    client,
                    name,
                    entries.get(name, []),
                    templates,
                    inventory_version,
                    documentation_target,
                    args.delay,
                    args.refresh,
                    previous.get(name),
                    documentation_urls,
                    standard_urls,
                ),
                names,
            )
            for index, result in enumerate(futures, 1):
                results.append(result)
                if index % 25 == 0 or index == len(names):
                    complete = sum(item["status"] in ("ok", "cached") for item in results)
                    print(f"{index}/{len(names)} complete={complete}", flush=True)

    previous.update({result["name"]: result for result in results})
    previous = {
        name: enrich_index_record(record, entries.get(name, []))
        for name, record in previous.items()
    }
    index_names = sorted(previous if args.only else entries)
    temporary = index_path.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps([previous[name] for name in index_names], ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    temporary.replace(index_path)
    counts: dict[str, int] = {}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    print(f"Index: {len(index_names)} components; fetched statuses: {counts}", flush=True)


if __name__ == "__main__":
    main()
