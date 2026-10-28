"""Puerta de calidad: todos los programas SAS del repositorio, contra los contratos reales del MCP, sin Studio.

Cada corpus (la raiz de fixtures, cada proyecto de `real/` y de `synthetic/`) se importa como un proyecto, se planifica
y se prepara su especificacion de Talend. Despues se comprueba que:

1. cada especificacion cumple los invariantes de un Job de Talend (`tests/support/spec_invariants.py`);
2. los argumentos validan contra el `inputSchema` que el MCP real publica para su herramienta de escritura;
3. los Jobs elegibles para el modo offline validan contra el esquema de `talend_jobs_create_batch` y el MCP real
   los acepta con `dryRun` (valida y no escribe).

Si un programa de un proyecto real rompe algo, que se rompa aqui y no al aplicarlo en produccion.
Para correr la version completa contra tu Studio: `uv run python scripts/verify_in_studio.py <carpeta SAS>`.
"""

import asyncio
import json
import os
import shutil
import socket
import subprocess
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import apps.api.main as api_module
import pytest
from fastapi.testclient import TestClient
from jsonschema import Draft202012Validator
from tests.support.item_invariants import item_problems
from tests.support.spec_invariants import project_problems, walk

from sas_grid_migrator.talend_adapter.eligibility import offline_blockers
from sas_grid_migrator.talend_adapter.offline_payload import to_batch_arguments

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures" / "sas"
MCP_DIR = ROOT / "mcp" / "talend-mcp"
BUN = shutil.which("bun")
WRITE_TOOL = "talend_job_apply_custom_spec"
BATCH_TOOL = "talend_jobs_create_batch"
XMI = "{http://www.omg.org/XMI}"

#: Carpeta del proyecto temporal del MCP, para leer lo que escribe.
_MCP_PROJECT: dict[str, Path] = {}


def _corpora() -> dict[str, Path]:
    found = {"raiz": FIXTURES}
    for group in ("real", "synthetic"):
        base = FIXTURES / group
        if base.is_dir():
            found.update({f"{group}/{path.name}": path for path in sorted(base.iterdir()) if path.is_dir()})
    return found


CORPORA = _corpora()


def _require_bun() -> None:
    if BUN is None:
        if os.environ.get("CI", "").lower() in {"1", "true"}:
            pytest.fail("bun no esta instalado en CI: la puerta del corpus no puede saltarse")
        pytest.skip("bun no esta instalado")


@pytest.fixture(scope="module")
def corpus_trees(tmp_path_factory):
    """Para cada corpus, los argumentos de cada programa que se puede aplicar."""
    root = tmp_path_factory.mktemp("corpus-gate")
    os.environ.update(
        SGM_DATA_DIR=str(root / "data"), TALEND_APPLY_FOLDER="Process/Pruebas", TALEND_MCP_READONLY="false"
    )
    results: dict[str, dict] = {}
    # La raiz de fixtures contiene los demas corpus: se prueba solo con sus archivos propios.
    own = root / "raiz"
    shutil.copytree(FIXTURES, own, ignore=shutil.ignore_patterns("real", "synthetic"))
    with TestClient(api_module.app) as client:
        for label, path in CORPORA.items():
            path = own if label == "raiz" else path
            project = client.post("/api/projects", json={"name": label.replace("/", "-")}).json()["id"]
            assert client.post(f"/api/projects/{project}/imports", json={"path": str(path)}).status_code == 201
            assert client.post(f"/api/projects/{project}/analyses").status_code == 201
            assert client.post(f"/api/projects/{project}/plans").status_code == 201
            plans = client.get(f"/api/projects/{project}/plans").json()
            items = plans if isinstance(plans, list) else plans.get("plans", [])
            trees, skipped, errors = {}, [], []
            for item in items:
                response = client.post(f"/api/projects/{project}/plans/{item['program']}/talend-apply/preview")
                if response.status_code >= 500:
                    errors.append(f"{item['program']}: HTTP {response.status_code}")
                elif response.status_code == 200 and response.json().get("arguments"):
                    trees[item["program"]] = response.json()["arguments"]
                else:
                    skipped.append(item["program"])
            results[label] = {"trees": trees, "skipped": skipped, "errors": errors, "programs": len(items)}
    return results


@pytest.mark.parametrize("label", CORPORA)
def test_the_api_never_crashes_and_plans_every_program(corpus_trees, label):
    data = corpus_trees[label]

    assert not data["errors"], f"{label}: el API fallo con 5xx: {data['errors']}"
    assert data["programs"] >= 1, f"{label}: no se planifico ningun programa"


@pytest.mark.parametrize("label", CORPORA)
def test_every_spec_meets_the_talend_invariants(corpus_trees, label):
    problems = project_problems(corpus_trees[label]["trees"], component_limit=api_module._max_apply_components())

    assert not problems, f"{label}:\n" + "\n".join(problems[:30])


def _wait(url: str, process: subprocess.Popen, timeout: float = 40.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError("el MCP termino durante el arranque")
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                if response.status == 200:
                    return
        except (urllib.error.URLError, OSError):
            time.sleep(0.2)
    raise RuntimeError("el MCP no respondio")


@pytest.fixture(scope="module")
def mcp(corpus_trees, tmp_path_factory):
    """El MCP real con el preset portal y un proyecto vacio cuyo catalogo conoce los componentes del corpus."""
    _require_bun()
    names = {
        component["componentName"]
        for data in corpus_trees.values()
        for tree in data["trees"].values()
        for job in walk(tree)
        for component in job["components"]
    }
    base = tmp_path_factory.mktemp("mcp-gate")
    project = base / "proyecto"
    project.mkdir()
    (project / "talend.project").write_text("", encoding="utf-8")
    _MCP_PROJECT["path"] = project
    cwd = base / "cwd"
    (cwd / ".talend-mcp").mkdir(parents=True)
    entries = [
        {"componentName": name, "family": "Gate", "version": "0.102", "pluginJar": "", "definitionFiles": [],
         "parameters": [], "schemas": {"hasInputSchema": True, "hasOutputSchema": True, "hasDynamicSchema": False},
         "connectors": [], "dependencies": [], "limitations": []}
        for name in sorted(names)
    ]
    (cwd / ".talend-mcp" / "component-catalog.json").write_text(json.dumps({"entries": entries}), encoding="utf-8")
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    env = {
        **os.environ, "TALEND_MCP_FILTER": "portal", "TALEND_MCP_PORT": str(port), "TALEND_MCP_HOST": "127.0.0.1",
        "TALEND_MCP_LOG": "quiet", "TALEND_DISABLE_AUTODETECT": "1", "TALEND_PROJECT": str(project),
    }
    process = subprocess.Popen(
        [BUN, "run", str(MCP_DIR / "index.ts")], cwd=cwd, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    try:
        _wait(f"http://127.0.0.1:{port}/healthz", process)
        yield f"http://127.0.0.1:{port}/mcp"
    finally:
        process.terminate()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()


@pytest.fixture(scope="module")
def schemas(mcp):
    from sas_grid_migrator.talend_adapter.adapter import McpCaller

    tools = {tool["name"]: tool for tool in asyncio.run(McpCaller(mcp).list_tools())}
    return {name: Draft202012Validator(tools[name]["inputSchema"]) for name in (WRITE_TOOL, BATCH_TOOL)}


@pytest.mark.parametrize("label", CORPORA)
def test_arguments_validate_against_the_schema_the_mcp_publishes(corpus_trees, schemas, label):
    failures = []
    for program, tree in corpus_trees[label]["trees"].items():
        for error in schemas[WRITE_TOOL].iter_errors(tree):
            failures.append(f"{program}: {'/'.join(str(part) for part in error.absolute_path)}: {error.message[:140]}")
    assert not failures, f"{label}:\n" + "\n".join(failures[:15])


@pytest.mark.parametrize("label", CORPORA)
def test_offline_eligible_jobs_validate_and_the_real_mcp_accepts_them_with_dry_run(corpus_trees, schemas, mcp, label):
    from mcp import Client

    payloads = []
    for program, tree in corpus_trees[label]["trees"].items():
        for job in walk(tree):
            single = {**job, "childJobs": []}
            if offline_blockers(single):
                continue
            arguments = to_batch_arguments(single)
            arguments["dryRun"] = True
            for error in schemas[BATCH_TOOL].iter_errors(arguments):
                pytest.fail(f"{label}/{program}/{job['jobName']}: {error.message[:160]}")
            payloads.append((program, job["jobName"], arguments))

    async def run() -> list[str]:
        refused = []
        async with Client(mcp, read_timeout_seconds=60) as client:
            for program, job_name, arguments in payloads:
                result = await client.call_tool(BATCH_TOOL, arguments)
                content = result.structured_content or {}
                data = content.get("data") or {}
                if not content.get("ok") or data.get("fallos"):
                    detail = json.dumps(content, ensure_ascii=False)
                    refused.append(f"{program} / {job_name}: {detail[:200]}")
        return refused

    refused = asyncio.run(run())
    assert not refused, f"{label}: el MCP rechazo {len(refused)} de {len(payloads)} Jobs:\n" + "\n".join(refused[:10])


@pytest.mark.parametrize("label", CORPORA)
def test_the_files_the_mcp_writes_are_well_formed_xml_that_studio_can_link(corpus_trees, mcp, label):
    """Escribe de verdad los Jobs elegibles y parsea sus archivos con un parser estricto.

    Un `xsi:type` sin `xmlns:xsi` (visto con los tMap) hace que Studio no cargue el `.item`: el Job sale con
    "Error when loading the job" y, al borrarlo, el `.item` queda huerfano. El parser de ElementTree falla igual.
    """
    from mcp import Client

    index = list(CORPORA).index(label)
    written: list[tuple[str, str]] = []
    payloads = []
    for program, tree in corpus_trees[label]["trees"].items():
        for job in walk(tree):
            single = {**job, "childJobs": []}
            if offline_blockers(single):
                continue
            single["jobName"] = f"{job['jobName']}_g{index}"
            single["folderPath"] = f"Process/Gate{index}"
            payloads.append((program, to_batch_arguments(single)))

    async def run() -> list[str]:
        refused = []
        async with Client(mcp, read_timeout_seconds=60) as client:
            for program, arguments in payloads:
                result = await client.call_tool(BATCH_TOOL, arguments)
                data = (result.structured_content or {}).get("data") or {}
                if data.get("fallos") or not (result.structured_content or {}).get("ok"):
                    if not any("ya existe" in str(f.get("error", "")).lower() for f in data.get("fallos") or []):
                        refused.append(f"{program}: {json.dumps(result.structured_content, ensure_ascii=False)[:200]}")
                    continue
                for entry in data.get("jobs") or []:
                    if entry.get("itemPath"):
                        written.append((program, entry["itemPath"]))
        return refused

    refused = asyncio.run(run())
    assert not refused, f"{label}: el MCP no pudo escribir:\n" + "\n".join(refused[:8])

    broken = []
    for program, item in written:
        for path in (Path(item), Path(item).with_suffix(".properties")):
            try:
                ET.parse(path)
            except ET.ParseError as error:
                broken.append(f"{program}: {path.name}: {error}")
        properties = ET.parse(Path(item).with_suffix(".properties")).getroot()
        xmi_ids = {element.get(f"{XMI}id") for element in properties.iter()}
        for element in properties.iter():
            if element.tag.endswith("ProcessItem"):
                for attribute in ("property", "state"):
                    if element.get(attribute) not in xmi_ids:
                        broken.append(f"{program}: ProcessItem.{attribute} apunta a un id que no existe")
                process = element.find("process")
                if process is None or not str(process.get("href", "")).endswith(".item#/"):
                    broken.append(f"{program}: la referencia al .item no es #/")
    assert not broken, f"{label}:\n" + "\n".join(broken[:10])
    assert written, f"{label}: no se escribio ningun Job para comprobar"

    # Un `.item` bien formado puede igualmente dejar a Studio con un diálogo al abrirlo (tablas del tMap que no
    # siguen a sus conexiones): no sale en la vista Problemas, así que se comprueba aquí.
    incoherent = [f"{program}: {problem}" for program, item in written for problem in item_problems(Path(item))]
    assert not incoherent, f"{label}: Studio avisaría al abrir estos Jobs:\n" + "\n".join(incoherent[:10])
