"""API-backed commands for agents; every platform API route is callable as JSON."""

import json
import os
import uuid
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import typer

agent_app = typer.Typer(help="Interfaz de automatización para agentes; respuestas JSON en stdout.")


def request_api(
    server: str,
    method: str,
    path: str,
    data: dict | list | None = None,
    file: Path | None = None,
) -> object:
    if not path.startswith("/") or path.startswith("//") or "://" in path:
        raise ValueError("la ruta debe ser relativa a la API y comenzar con '/'")
    route = path if path.startswith("/api/") else f"/api{path}"
    url = f"{server.rstrip('/')}{route}"
    headers: dict[str, str] = {"Accept": "application/json"}
    body: bytes | None = None
    if file is not None:
        boundary = uuid.uuid4().hex
        headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        parts = []
        for key, value in (data or {}).items():
            parts.extend([
                f"--{boundary}\r\nContent-Disposition: form-data; name=\"{key}\"\r\n\r\n".encode(),
                str(value).encode(),
                b"\r\n",
            ])
        parts.extend([
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{file.name}\"\r\n"
            f"Content-Type: application/octet-stream\r\n\r\n".encode(),
            file.read_bytes(),
            f"\r\n--{boundary}--\r\n".encode(),
        ])
        body = b"".join(parts)
    elif data is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")

    req = Request(url, data=body, headers=headers, method=method.upper())
    try:
        with urlopen(req, timeout=120) as response:
            payload = response.read()
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(detail)
        except json.JSONDecodeError:
            parsed = detail
        typer.echo(json.dumps({"error": parsed, "status": exc.code, "url": url}, ensure_ascii=False), err=True)
        raise typer.Exit(1) from exc
    except URLError as exc:
        typer.echo(json.dumps({"error": str(exc.reason), "url": url}, ensure_ascii=False), err=True)
        raise typer.Exit(1) from exc

    if not payload:
        return None
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return payload.decode("utf-8", errors="replace")


def _emit(value: object) -> None:
    typer.echo(json.dumps(value, ensure_ascii=False, separators=(",", ":")))


@agent_app.command("api")
def api_request(
    method: str = typer.Argument(..., help="Método HTTP; por ejemplo GET, POST, PATCH o DELETE."),
    path: str = typer.Argument(..., help="Ruta API, por ejemplo /projects o /integrations/talend/health."),
    data: str = typer.Option(None, "--data", help="Cuerpo JSON."),
    file: Path = typer.Option(None, "--file", exists=True, dir_okay=False, help="Archivo para endpoints multipart."),
    server: str = typer.Option(
        os.environ.get("SGM_API", "http://127.0.0.1:8000"), "--server", help="URL base de la API."
    ),
) -> None:
    """Invoca cualquier endpoint de la plataforma; cubre también las funciones de la UI."""
    try:
        parsed_data = json.loads(data) if data is not None else None
    except json.JSONDecodeError as exc:
        raise typer.BadParameter(f"JSON inválido: {exc.msg}", param_hint="--data") from exc
    if parsed_data is not None and not isinstance(parsed_data, (dict, list)):
        raise typer.BadParameter("el cuerpo debe ser un objeto o una lista JSON", param_hint="--data")
    if file is not None and parsed_data is not None and not isinstance(parsed_data, dict):
        raise typer.BadParameter("--data debe ser un objeto al combinarlo con --file", param_hint="--data")
    permission_path = path.split("?", 1)[0]
    if permission_path.startswith("/api/"):
        permission_path = permission_path[4:]
    if method.upper() not in {"GET", "HEAD"} and permission_path == "/integrations/talend/permissions":
        raise typer.BadParameter("el permiso de escritura se administra solo desde Configuración")
    _emit(request_api(server, method, path, parsed_data, file))


@agent_app.command()
def migrate(
    path: Path = typer.Argument(..., exists=True, help="Carpeta o ZIP accesible desde el servidor de API."),
    name: str = typer.Option(..., "--name", "-n", help="Nombre del proyecto."),
    server: str = typer.Option(
        os.environ.get("SGM_API", "http://127.0.0.1:8000"), "--server", help="URL base de la API."
    ),
) -> None:
    """Crea proyecto, importa, analiza, genera planes y exporta; no escribe Jobs en Talend."""
    project = request_api(server, "POST", "/projects", {"name": name})
    if not isinstance(project, dict) or not project.get("id"):
        raise typer.Exit(1)
    project_id = project["id"]
    imported = request_api(server, "POST", f"/projects/{project_id}/imports", {"path": str(path.resolve())})
    analysis = request_api(server, "POST", f"/projects/{project_id}/analyses")
    dependencies = request_api(server, "GET", f"/projects/{project_id}/dependencies")
    plans = request_api(server, "POST", f"/projects/{project_id}/plans")
    exports = request_api(server, "POST", f"/projects/{project_id}/exports")
    _emit({
        "project": project,
        "import": imported,
        "analysis": analysis,
        "dependencies": dependencies,
        "plans": plans,
        "exports": exports,
    })
