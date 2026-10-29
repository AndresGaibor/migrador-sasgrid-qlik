"""Arranque local de la API y la UI de desarrollo con un solo comando."""

from __future__ import annotations

import os
import shutil
import signal
import socket
import subprocess
import sys
import time
import webbrowser
from pathlib import Path
from typing import Any

import typer

IS_WINDOWS = os.name == "nt"
# JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE: al cerrar el job mueren todos sus procesos.
_KILL_ON_JOB_CLOSE = 0x2000
_JobObject = tuple[Any, int]


def repo_root() -> Path:
    """Directorio del repositorio, aunque el comando se invoque desde otra carpeta."""
    for candidate in (Path.cwd(), *Path(__file__).resolve().parents):
        if (candidate / "apps" / "web" / "package.json").is_file():
            return candidate
    raise typer.BadParameter("No se encontró apps/web/package.json; ejecuta desde el repositorio.")


def ensure_deps(directory: Path, bun: str, label: str) -> None:
    if (directory / "node_modules").is_dir():
        return
    typer.echo(f"Instalando dependencias de {label} (bun install)...")
    result = subprocess.run([bun, "install"], cwd=directory, check=False)
    if result.returncode != 0:
        raise typer.Exit(result.returncode)


def create_job() -> _JobObject | None:
    """Job de Windows para que Ctrl+C (o un cierre inesperado) no deje hijos vivos."""
    if not IS_WINDOWS:
        return None
    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

    class BasicLimits(ctypes.Structure):
        _fields_ = [
            ("PerProcessUserTimeLimit", ctypes.c_int64),
            ("PerJobUserTimeLimit", ctypes.c_int64),
            ("LimitFlags", wintypes.DWORD),
            ("MinimumWorkingSetSize", ctypes.c_size_t),
            ("MaximumWorkingSetSize", ctypes.c_size_t),
            ("ActiveProcessLimit", wintypes.DWORD),
            ("Affinity", ctypes.c_size_t),
            ("PriorityClass", wintypes.DWORD),
            ("SchedulingClass", wintypes.DWORD),
        ]

    class ExtendedLimits(ctypes.Structure):
        _fields_ = [
            ("BasicLimitInformation", BasicLimits),
            ("IoInfo", ctypes.c_size_t * 6),
            ("ProcessMemoryLimit", ctypes.c_size_t),
            ("JobMemoryLimit", ctypes.c_size_t),
            ("PeakProcessMemoryUsed", ctypes.c_size_t),
            ("PeakJobMemoryUsed", ctypes.c_size_t),
        ]

    handle = kernel32.CreateJobObjectW(None, None)
    if not handle:
        return None
    info = ExtendedLimits()
    info.BasicLimitInformation.LimitFlags = _KILL_ON_JOB_CLOSE
    kernel32.SetInformationJobObject(handle, 9, ctypes.byref(info), ctypes.sizeof(info))
    return kernel32, handle


def spawn(
    command: list[str],
    cwd: Path,
    env: dict[str, str],
    job: _JobObject | None,
    *,
    no_console: bool = False,
) -> Any:
    if IS_WINDOWS:
        flags = subprocess.CREATE_NEW_PROCESS_GROUP
        if no_console:
            # Uvicorn's reload worker can emit Ctrl+C on Windows; keep it from
            # delivering that console event to this supervisor and sibling services.
            flags |= subprocess.CREATE_NO_WINDOW
        options: dict[str, Any] = {"creationflags": flags}
    else:
        options = {"start_new_session": True}
    process = subprocess.Popen(command, cwd=cwd, env=env, **options)
    if job is not None:
        kernel32, handle = job
        # PROCESS_SET_QUOTA | PROCESS_TERMINATE
        process_handle = kernel32.OpenProcess(0x0100 | 0x0001, False, process.pid)
        if process_handle:
            kernel32.AssignProcessToJobObject(handle, process_handle)
            kernel32.CloseHandle(process_handle)
    return process


def stop(processes: list[Any], job: _JobObject | None) -> None:
    if job is not None:
        kernel32, handle = job
        kernel32.TerminateJobObject(handle, 1)
        kernel32.CloseHandle(handle)
    else:
        for process in reversed(processes):
            if process.poll() is None:
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    for process in processes:
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()


def wait_for_port(host: str, port: int, timeout: float = 30.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return True
        except OSError:
            time.sleep(0.2)
    return False


def port_in_use(host: str, port: int) -> bool:
    try:
        with socket.create_connection((host, port), timeout=0.3):
            return True
    except OSError:
        return False


def mcp_launch(
    root: Path, bun: str, env: dict[str, str]
) -> tuple[list[str], Path, dict[str, str]] | None:
    """Comando del MCP del subtree con el preset `portal`; `None` si no está importado.

    Usa `start:server` y no `start`: este reinstala el plugin en un Studio abierto
    y libera el puerto matando al proceso que lo ocupe.
    """
    mcp = root / "mcp" / "talend-mcp"
    if not (mcp / "package.json").is_file():
        return None
    return [bun, "run", "start:server"], mcp, {**env, "TALEND_MCP_FILTER": "portal"}


def dev(
    host: str = typer.Option("127.0.0.1", "--host", help="Interfaz donde escuchan API y UI"),
    api_port: int = typer.Option(8000, "--api-port", help="Puerto de la API"),
    web_port: int = typer.Option(5173, "--web-port", help="Puerto de la UI"),
    reload: bool = typer.Option(True, "--reload/--no-reload", help="Recargar la API al editar"),
    open_browser: bool = typer.Option(True, "--open/--no-open", help="Abrir la UI al arrancar"),
    mcp: bool = typer.Option(True, "--mcp/--no-mcp", help="Arrancar también el MCP de Talend (preset portal)"),
) -> None:
    """Arranca el MCP, la API y la UI de desarrollo, y las detiene juntas con Ctrl+C."""
    root = repo_root()
    web = root / "apps" / "web"
    bun = shutil.which("bun")
    if bun is None:
        raise typer.Exit(
            typer.echo("bun no está instalado: https://bun.sh/docs/installation", err=True) or 1
        )
    ensure_deps(web, bun, "el frontend")

    env = {**os.environ, "SGM_API": f"http://{host}:{api_port}", "PYTHONUNBUFFERED": "1"}
    api_command = [
        sys.executable,
        "-m",
        "uvicorn",
        "apps.api.main:app",
        "--host",
        host,
        "--port",
        str(api_port),
    ]
    if reload:
        api_command.append("--reload")

    job = create_job()
    named: list[tuple[str, Any]] = []
    launch = mcp_launch(root, bun, env) if mcp else None
    mcp_port = int(os.environ.get("TALEND_MCP_PORT", "3927"))
    if launch is None:
        if mcp:
            typer.echo("MCP: mcp/talend-mcp no está importado; se omite.", err=True)
    elif port_in_use("127.0.0.1", mcp_port):
        typer.echo(
            f"MCP: el puerto {mcp_port} ya está en uso; se reutiliza ese servidor. "
            "Si no usa TALEND_MCP_FILTER=portal, Configuración lo indicará."
        )
    else:
        command, mcp_dir, mcp_env = launch
        ensure_deps(mcp_dir, bun, "el MCP")
        named.append(("MCP", spawn(command, mcp_dir, mcp_env, job)))
        typer.echo(f"MCP: http://127.0.0.1:{mcp_port}/mcp (preset portal)")
    named.append(("API", spawn(api_command, root, env, job, no_console=reload)))
    named.append(("UI", spawn([bun, "run", "dev", "--host", host, "--port", str(web_port)], web, env, job)))
    processes = [process for _, process in named]
    url = f"http://{host}:{web_port}/"
    typer.echo(f"API: http://{host}:{api_port}")
    typer.echo(f"UI:  {url}")
    typer.echo("Ctrl+C para detener todos los procesos iniciados aquí.")

    status: int | None = None
    try:
        if open_browser and wait_for_port(host, web_port):
            webbrowser.open(url)
        while status is None:
            for name, process in named:
                exit_code = process.poll()
                if exit_code is not None:
                    typer.echo(f"{name} terminó con código {exit_code}; deteniendo el resto.", err=True)
                    status = exit_code
                    break
            else:
                time.sleep(0.5)
    except KeyboardInterrupt:
        typer.echo("\nDeteniendo procesos...")
    finally:
        stop(processes, job)
    if status:
        raise typer.Exit(status)
