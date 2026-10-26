import tempfile
from pathlib import Path, PurePosixPath

from fastapi import APIRouter, HTTPException, UploadFile
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

from sas_grid_migrator.dependency_graph.builder import (
    DependencyReport,
    build_dependencies,
    load_dependencies,
)
from sas_grid_migrator.domain.models import Manifest, Project
from sas_grid_migrator.domain.redaction import redact
from sas_grid_migrator.ingestion.importer import ImportError_
from sas_grid_migrator.sas_parser.analyze import (
    AnalysisSummary,
    analyze_project,
    load_analysis,
    summarize,
)
from sas_grid_migrator.sas_parser.ast import ParsedProgram

from .common import analysis, require_project, store

router = APIRouter(prefix="/api")


class NewProject(BaseModel):
    name: str


class NewImport(BaseModel):
    path: str  # carpeta o ZIP local


@router.post("/projects", status_code=201)
def create_project(body: NewProject) -> Project:
    return store().create_project(body.name)


@router.get("/projects")
def list_projects() -> list[Project]:
    return store().list_projects()


@router.post("/projects/{project_id}/imports", status_code=201)
def import_batch(project_id: str, body: NewImport) -> Manifest:
    s = store()
    require_project(s, project_id)
    src = Path(body.path)
    roots = s.settings.import_roots
    if roots and not any(src.resolve().is_relative_to(root) for root in roots):
        raise HTTPException(403, "ruta fuera de SGM_IMPORT_ROOTS")
    if not src.exists():
        raise HTTPException(422, "ruta inexistente")
    try:
        return s.import_batch(project_id, src)
    except ImportError_ as e:
        raise HTTPException(422, str(e)) from e


@router.post("/projects/{project_id}/uploads", status_code=201)
async def upload_zip(project_id: str, file: UploadFile) -> Manifest:
    """Importa un ZIP de proyecto o un único archivo SAS subido desde el navegador."""
    s = store()
    require_project(s, project_id)
    limit = s.settings.max_total_bytes
    s.settings.data_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=s.settings.data_dir) as tmp:
        name = PurePosixPath((file.filename or "").replace("\\", "/")).name
        suffix = PurePosixPath(name).suffix.lower()
        if suffix not in {".zip", ".sas"}:
            raise HTTPException(422, "solo se permiten archivos .zip o .sas")
        is_sas = suffix == ".sas"
        source = Path(tmp) / "single" if is_sas else Path(tmp) / "upload.zip"
        if is_sas:
            source.mkdir()
            source = source / name
        size = 0
        with source.open("wb") as out:
            while chunk := await file.read(1024 * 1024):
                size += len(chunk)
                if size > limit:
                    raise HTTPException(413, "archivo demasiado grande")
                out.write(chunk)
        try:
            return s.import_batch(project_id, source.parent if is_sas else source)
        except ImportError_ as e:
            raise HTTPException(422, str(e)) from e


@router.get("/projects/{project_id}/inventory")
def inventory(project_id: str) -> Manifest:
    s = store()
    require_project(s, project_id)
    return s.get_manifest(project_id)


@router.post("/projects/{project_id}/analyses", status_code=201)
def run_analysis(project_id: str) -> AnalysisSummary:
    s = store()
    require_project(s, project_id)
    return summarize(analyze_project(s, project_id))


@router.get("/projects/{project_id}/analyses")
def get_analysis_summary(project_id: str) -> AnalysisSummary | None:
    s = store()
    require_project(s, project_id)
    result = load_analysis(s, project_id)
    return summarize(result) if result else None


@router.get("/projects/{project_id}/programs")
def list_programs(project_id: str) -> list[dict]:
    return [
        {"file": p.file, "statements": p.stats.statements, "findings": len(p.findings)}
        for p in analysis(project_id).programs
    ]


@router.get("/projects/{project_id}/programs/{path:path}")
def get_program(project_id: str, path: str) -> ParsedProgram:
    for program in analysis(project_id).programs:
        if program.file == path:
            return program
    raise HTTPException(404, "programa no encontrado")


@router.get("/projects/{project_id}/source/{path:path}")
def source_evidence(project_id: str, path: str, line: int) -> PlainTextResponse:
    s = store()
    require_project(s, project_id)
    source = next((item for item in s.get_manifest(project_id).files if item.path == path), None)
    if source is None or source.encoding is None:
        raise HTTPException(404, "archivo de texto no encontrado")
    root = s.source_dir(project_id).resolve()
    target = (root / path).resolve()
    if not target.is_relative_to(root):
        raise HTTPException(404, "archivo no encontrado")
    text = target.read_text(encoding=source.encoding, errors="replace")
    lines = redact(text, path).splitlines()
    if line < 1 or line > len(lines):
        raise HTTPException(404, "línea no encontrada")
    start, end = max(1, line - 2), min(len(lines), line + 2)
    return PlainTextResponse(
        "\n".join(f"{number:>5} | {lines[number - 1]}" for number in range(start, end + 1)),
        media_type="text/plain; charset=utf-8",
    )


@router.get("/projects/{project_id}/dependencies")
def dependencies(project_id: str) -> DependencyReport:
    s = store()
    require_project(s, project_id)
    return load_dependencies(s, project_id) or build_dependencies(s, project_id)
