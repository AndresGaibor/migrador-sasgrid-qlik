# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "beautifulsoup4", "markdownify"]
# ///
"""Descarga la documentación de componentes de help.qlik.com y la guarda como Markdown local.

Por componente del catálogo: página resumen + páginas «Standard properties» (se omiten Spark/MapReduce/Storm
y escenarios). Reanudable (salta lo ya descargado). Salida: docs/reference/talend/<componente>.md
(gitignorada: el contenido es de Qlik, solo para consulta local) e index.json con el estado de cada uno.

Uso: uv run tools/fetch_talend_docs.py [--workers 4] [--version 8.0] [--only tFilterRow,tMap]
"""

import argparse
import json
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "reference" / "talend"
BASE = "https://help.qlik.com/talend/en-US/components/{v}/"
SKIP = re.compile(r"spark|mapreduce|storm|streaming|batch|big data|scenario", re.IGNORECASE)
lock = threading.Lock()


def get(client: httpx.Client, url: str) -> httpx.Response | None:
    for attempt in range(3):
        try:
            r = client.get(url, follow_redirects=False, timeout=30)
            if r.status_code in (429, 503):
                time.sleep(5 * (attempt + 1))
                continue
            return r
        except httpx.HTTPError:
            time.sleep(2 * (attempt + 1))
    return None


def topic(html: str, url: str, name: str) -> tuple[str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    node = soup.find(id="topicContent")
    if node is None:
        return "", []
    key = name.lower()
    links = []
    for a in node.select("a[href]"):
        text = a.get_text(" ", strip=True)
        path = a["href"].split("#")[0].split("?")[0]
        if not path.startswith("/talend/en-US/components/") or SKIP.search(text + " " + path):
            continue
        parts = path.rstrip("/").split("/")
        # solo subpáginas de este componente (mismo prefijo o carpeta), no escenarios ni enlaces cruzados
        if (parts[-1].startswith(key) or parts[-2] == key) and "related" not in path:
            links.append(urljoin(url, path))
    for tag in node.select("script,style,.feedback,nav"):
        tag.decompose()
    md = markdownify(str(node), heading_style="ATX", strip=["img"])
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    md = re.sub(r"Did this page help you\?.*", "", md, flags=re.DOTALL).strip()
    return md, links


MAX_PAGES = 8


def fetch_component(client: httpx.Client, name: str, version: str, delay: float) -> dict:
    target = OUT / f"{name}.md"
    if target.exists():
        return {"name": name, "status": "cached"}
    url = BASE.format(v=version) + name.lower()
    r = get(client, url)
    time.sleep(delay)
    if r is None or r.status_code != 200:
        return {"name": name, "status": f"sin página ({r.status_code if r else 'error'})"}
    overview, links = topic(r.text, url, name)
    parts = [f"<!-- fuente: {url} · versión {version} -->", overview]
    seen = {url}
    queue = [(link, 1) for link in links]
    while queue and len(seen) < MAX_PAGES:
        link, depth = queue.pop(0)
        if link in seen:
            continue
        seen.add(link)
        sub = get(client, link)
        time.sleep(delay)
        if sub is not None and sub.status_code == 200:
            md, more = topic(sub.text, link, name)
            parts.append(f"\n\n---\n<!-- fuente: {link} -->\n{md}")
            if depth < 2:
                queue += [(m, depth + 1) for m in more]
    target.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return {"name": name, "status": "ok", "pages": len(seen), "bytes": target.stat().st_size}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--version", default="8.0")
    ap.add_argument("--delay", type=float, default=0.3)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    names = sorted(json.loads((ROOT / "rules/talend/components.json").read_text())["components"])
    if a.only:
        names = [n for n in names if n in a.only.split(",")]
    headers = {"User-Agent": "sgm-docs-fetch/1.0 (uso local; contacto: repo migrador-sasgrid-qlik)"}
    results = []
    with httpx.Client(headers=headers) as client, ThreadPoolExecutor(a.workers) as pool:
        for i, res in enumerate(
            pool.map(lambda n: fetch_component(client, n, a.version, a.delay), names), 1
        ):
            results.append(res)
            if i % 25 == 0 or i == len(names):
                ok = sum(1 for r in results if r["status"] in ("ok", "cached"))
                print(f"{i}/{len(names)} ok={ok}", flush=True)
    (OUT / "index.json").write_text(json.dumps(results, ensure_ascii=False, indent=1))
    print("sin página:", [r["name"] for r in results if r["status"].startswith("sin")][:40])


if __name__ == "__main__":
    main()
