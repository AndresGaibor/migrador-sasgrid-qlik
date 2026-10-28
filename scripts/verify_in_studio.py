"""Verifica un proyecto SAS completo contra un Talend Studio real, antes de llevarlo a produccion.

Importa la carpeta SAS como un proyecto del portal, la analiza, la planifica y la aplica en Studio por el mismo flujo de
lote que usa la interfaz. Despues lee los problemas que Studio marca en cada Job y falla si hay alguno que no sea un
pendiente esperado de un borrador. Al terminar borra de Studio los Jobs que creo (salvo con --keep).

Uso:
    uv run python scripts/verify_in_studio.py <carpeta con los .sas> [--folder Process/Verificacion] [--keep]

Requisitos: Talend Studio abierto con el Bridge instalado (`bun run bridge:install` en mcp/talend-mcp) y bun en el PATH.
Codigos de salida: 0 todo bien; 1 hay Jobs fallidos o con errores inesperados; 2 no se pudo hablar con Studio.
"""

import argparse
import asyncio
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

#: Errores de Studio que son pendientes esperados de un borrador (faltan datos que el SAS no trae), no defectos.
EXPECTED_PENDING = [
    re.compile(r"must have at least one value", re.I),
    re.compile(r"No schema has been defined yet", re.I),
    re.compile(r"Module .+ required", re.I),
]


def is_expected(message: str) -> bool:
    return any(pattern.search(message) for pattern in EXPECTED_PENDING)


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _start_mcp() -> tuple[subprocess.Popen, str]:
    bun = shutil.which("bun")
    if bun is None:
        raise SystemExit("bun no esta instalado: el MCP no se puede arrancar")
    port = _free_port()
    env = {
        **os.environ, "TALEND_MCP_FILTER": "talend_job_delete_in_studio,talend_delete_job,portal",
        "TALEND_MCP_PORT": str(port), "TALEND_MCP_HOST": "127.0.0.1", "TALEND_MCP_LOG": "quiet",
    }
    process = subprocess.Popen(
        [bun, "run", str(ROOT / "mcp" / "talend-mcp" / "index.ts")], cwd=ROOT / "mcp" / "talend-mcp", env=env,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for _ in range(200):
        if process.poll() is not None:
            raise SystemExit("el MCP termino durante el arranque")
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/healthz", timeout=1)
            return process, f"http://127.0.0.1:{port}/mcp"
        except OSError:
            time.sleep(0.2)
    raise SystemExit("el MCP no respondio")


def _job_names(result: dict | None, names: set[str]) -> None:
    if isinstance(result, dict):
        if result.get("jobName"):
            names.add(str(result["jobName"]))
        for child in result.get("childJobs") or []:
            _job_names(child, names)


async def _cleanup(url: str, names: set[str]) -> list[str]:
    from mcp import Client

    left: list[str] = []
    async with Client(url, read_timeout_seconds=240) as client:
        for name in sorted(names):
            # El Job puede estar cargado en Studio (se borra del repositorio) o solo escrito en disco (offline).
            await client.call_tool("talend_job_delete_in_studio", {"name": name, "version": "0.1"})
            await client.call_tool("talend_delete_job", {"jobName": name})
        listing = await client.call_tool("talend_jobs_list", {"limit": 5000})
        jobs = (listing.structured_content or {}).get("data", {}).get("jobs", [])
        left = [job["name"] for job in jobs if job["name"] in names]
    return left


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path, help="carpeta con los programas SAS del proyecto")
    parser.add_argument("--folder", default="Process/VerificacionPortal", help="carpeta de Studio donde crear los Jobs")
    parser.add_argument("--keep", action="store_true", help="no borrar los Jobs creados")
    parser.add_argument("--timeout", type=int, default=1800, help="segundos maximos de espera del lote")
    parser.add_argument("--json", type=Path, help="guardar el informe en este archivo")
    args = parser.parse_args()
    if not args.source.is_dir():
        print(f"No existe la carpeta {args.source}", file=sys.stderr)
        return 2
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    mcp, url = _start_mcp()
    data_dir = tempfile.mkdtemp(prefix="sgm-verify-")
    os.environ.update(
        SGM_DATA_DIR=data_dir, TALEND_MCP_URL=url, TALEND_APPLY_FOLDER=args.folder, TALEND_MCP_READONLY="false",
        TALEND_MCP_TIMEOUT_SECONDS="180",
    )
    names: set[str] = set()
    report: dict = {"source": str(args.source), "jobs": []}
    exit_code = 0
    try:
        from fastapi.testclient import TestClient

        import apps.api.main as api

        with TestClient(api.app) as client:
            client.patch("/api/integrations/talend/permissions", json={"write_enabled": True})
            health = client.get("/api/integrations/talend/health").json()
            if not health.get("available"):
                print(f"Studio no esta disponible: {health.get('diagnosis')} - {health.get('fix_hint')}", file=sys.stderr)
                return 2
            project = client.post("/api/projects", json={"name": args.source.name}).json()["id"]
            client.post(f"/api/projects/{project}/imports", json={"path": str(args.source.resolve())})
            client.post(f"/api/projects/{project}/analyses")
            client.post(f"/api/projects/{project}/plans")
            preflight = client.get(f"/api/projects/{project}/talend-apply-batch/preflight").json()
            print(f"{preflight.get('total_jobs')} Jobs a crear en {args.folder}; "
                  f"{preflight.get('conflict_count', 0)} conflictos con Jobs existentes")
            started = time.time()
            client.post(f"/api/projects/{project}/talend-apply-batch", json={"expected_revision": preflight["revision_hash"]})
            state: dict = {}
            while time.time() - started < args.timeout:
                time.sleep(3)
                state = client.get(f"/api/projects/{project}/talend-apply-batch").json()
                if state["status"] not in {"running", "pending", "queued", "not_started"}:
                    break
            report["seconds"] = round(time.time() - started)
            report["status"] = state.get("status")

            counts: dict[str, int] = {}
            for job in state.get("jobs", []):
                outcome = job.get("result") or {}
                _job_names(outcome.get("result"), names)
                counts[job["status"]] = counts.get(job["status"], 0) + 1
                errors = list(outcome.get("design_errors") or [])
                unexpected = [error for error in errors if not is_expected(error)]
                mode = (outcome.get("result") or {}).get("mode") or "en vivo"
                entry = {
                    "program": job["program"], "status": job["status"], "mode": mode,
                    "design_errors": errors, "unexpected": unexpected, "error": job.get("error"),
                }
                report["jobs"].append(entry)
                bad = job["status"] in {"failed", "conflict"} or unexpected
                if bad:
                    exit_code = 1
                flag = "FALLA" if bad else "ok   "
                print(f"[{flag}] {job['program']:55s} {job['status']:17s} {mode}")
                for message in unexpected[:5]:
                    print(f"          error inesperado: {message[:180]}")
                if job.get("error"):
                    print(f"          {str(job['error'])[:220]}")
            report["counts"] = counts
            print(f"\nResumen: {counts} en {report['seconds']} s")
            if report["status"] in {"running", "pending", "queued"}:
                print("El lote no termino en el tiempo dado", file=sys.stderr)
                exit_code = 1
    except Exception as error:  # noqa: BLE001 - es un script de verificacion: se informa y se limpia
        print(f"No se pudo completar la verificacion: {type(error).__name__}: {error}", file=sys.stderr)
        exit_code = 2
    finally:
        if names and not args.keep:
            try:
                left = asyncio.run(_cleanup(url, names))
                report["left_in_studio"] = left
                print(f"Borrados {len(names) - len(left)} de {len(names)} Jobs de Studio" + (f"; quedan: {left}" if left else ""))
                if left:
                    exit_code = max(exit_code, 1)
            except Exception as error:  # noqa: BLE001
                print(f"No se pudieron borrar los Jobs de prueba: {error}", file=sys.stderr)
                exit_code = max(exit_code, 1)
        mcp.terminate()
        shutil.rmtree(data_dir, ignore_errors=True)
        if args.json:
            args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
