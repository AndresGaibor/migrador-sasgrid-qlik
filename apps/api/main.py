import hashlib
import json
import os
import re
import tempfile
from contextlib import asynccontextmanager
from pathlib import Path, PurePosixPath
from threading import Condition

from fastapi import BackgroundTasks, FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from sas_grid_migrator import __version__
from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import (
    DependencyReport,
    build_dependencies,
    load_dependencies,
)
from sas_grid_migrator.domain.models import Manifest, Project
from sas_grid_migrator.domain.redaction import redact
from sas_grid_migrator.ingestion.importer import ImportError_, import_source
from sas_grid_migrator.migration_planner.models import JobPlan, PlanSet
from sas_grid_migrator.migration_planner.service import (
    generate_plans,
    get_plan,
    load_plans,
    set_decision,
)
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.reporting.exports import render_plan_md, steps_csv
from sas_grid_migrator.sas_parser.analyze import (
    AnalysisSummary,
    analyze_project,
    load_analysis,
    summarize,
)
from sas_grid_migrator.sas_parser.ast import ParsedProgram
from sas_grid_migrator.talend_adapter.batch import collect_child_results, order_plans_for_batch


@asynccontextmanager
async def lifespan(_app: FastAPI):
    store().recover_interrupted_operations()
    yield


app = FastAPI(title="SAS Grid Migrator", version=__version__, lifespan=lifespan)

_PIPELINE_CONDITION = Condition()
_PIPELINE_ACTIVE = 0
_PIPELINE_RESERVED = 0


def store() -> Store:
    return Store(Settings.from_env())


class NewProject(BaseModel):
    name: str


class NewImport(BaseModel):
    path: str  # carpeta o ZIP local


def _require(s: Store, project_id: str) -> None:
    if s.get_project(project_id) is None:
        raise HTTPException(404, "proyecto no encontrado")


def _reserve_pipeline(settings: Settings) -> bool:
    global _PIPELINE_RESERVED
    with _PIPELINE_CONDITION:
        capacity = settings.max_pipeline_concurrency + settings.max_queued_pipelines
        if _PIPELINE_ACTIVE + _PIPELINE_RESERVED >= capacity:
            return False
        _PIPELINE_RESERVED += 1
        return True


def _release_pipeline_reservation() -> None:
    global _PIPELINE_RESERVED
    with _PIPELINE_CONDITION:
        _PIPELINE_RESERVED = max(0, _PIPELINE_RESERVED - 1)
        _PIPELINE_CONDITION.notify_all()


def _run_project_pipeline(project_id: str, max_concurrency: int) -> None:
    global _PIPELINE_ACTIVE, _PIPELINE_RESERVED
    with _PIPELINE_CONDITION:
        while _PIPELINE_ACTIVE >= max_concurrency:
            _PIPELINE_CONDITION.wait()
        _PIPELINE_RESERVED = max(0, _PIPELINE_RESERVED - 1)
        _PIPELINE_ACTIVE += 1
    current_stage = "analysis"
    s = store()
    try:
        s.update_processing(
            project_id,
            status="running",
            stage=current_stage,
            message="Analizando los programas SAS y sus macros.",
        )
        analyze_project(s, project_id)
        current_stage = "dependencies"
        s.update_processing(
            project_id,
            status="running",
            stage=current_stage,
            message="Construyendo dependencias y orden de procesamiento.",
        )
        build_dependencies(s, project_id)
        current_stage = "plans"
        s.update_processing(
            project_id,
            status="running",
            stage=current_stage,
            message="Generando una guía por cada programa SAS.",
        )
        generate_plans(s, project_id)
        s.update_processing(
            project_id,
            status="completed",
            stage="completed",
            message="Análisis, dependencias y guías listos.",
        )
    except Exception as exc:
        s.update_processing(
            project_id,
            status="failed",
            stage=current_stage,
            message=f"Falló la etapa de {current_stage}.",
            error=str(exc),
        )
    finally:
        with _PIPELINE_CONDITION:
            _PIPELINE_ACTIVE = max(0, _PIPELINE_ACTIVE - 1)
            _PIPELINE_CONDITION.notify_all()


def _queue_project_pipeline(
    s: Store,
    project_id: str,
    background_tasks: BackgroundTasks,
    *,
    retry: bool = False,
    reserved: bool = False,
) -> object:
    owns_reservation = not reserved
    if owns_reservation and not _reserve_pipeline(s.settings):
        raise HTTPException(
            429, "Se alcanzó la capacidad de análisis; intenta de nuevo en unos minutos."
        )
    try:
        state = s.update_processing(
            project_id,
            status="queued",
            stage="queued",
            message="En cola para analizar el proyecto.",
            error=None,
            retry=retry,
        )
        background_tasks.add_task(
            _run_project_pipeline,
            project_id,
            s.settings.max_pipeline_concurrency,
        )
        return state
    except Exception:
        if owns_reservation:
            _release_pipeline_reservation()
        raise


@app.get("/api/health")
def health() -> dict[str, str | int]:
    settings = Settings.from_env()
    return {
        "status": "ok",
        "version": __version__,
        "max_pipeline_concurrency": settings.max_pipeline_concurrency,
        "max_queued_pipelines": settings.max_queued_pipelines,
    }


@app.post("/api/projects", status_code=201)
def create_project(body: NewProject) -> Project:
    return store().create_project(body.name)


@app.get("/api/projects")
def list_projects() -> list[Project]:
    return store().list_projects()


@app.post("/api/projects/uploads", status_code=201)
async def create_project_from_zip(
    background_tasks: BackgroundTasks,
    file: UploadFile,
    name: str | None = Form(default=None),
) -> dict:
    """Create one isolated project from a ZIP, then analyze it in the background."""
    s = store()
    archive_name = PurePosixPath((file.filename or "").replace("\\", "/")).name
    if PurePosixPath(archive_name).suffix.lower() != ".zip":
        raise HTTPException(422, "solo se permiten archivos .zip para crear un proyecto")
    display_name = (name or PurePosixPath(archive_name).stem).strip()
    if not display_name or len(display_name) > 120:
        raise HTTPException(422, "el nombre del proyecto debe tener entre 1 y 120 caracteres")
    if not _reserve_pipeline(s.settings):
        raise HTTPException(429, "Se alcanzó la capacidad de análisis; intenta de nuevo en unos minutos.")

    reserved = True
    try:
        s.settings.data_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=s.settings.data_dir) as tmp:
            temp_dir = Path(tmp)
            archive_path = temp_dir / "upload.zip"
            digest = hashlib.sha256()
            size = 0
            with archive_path.open("wb") as target:
                while chunk := await file.read(1024 * 1024):
                    size += len(chunk)
                    if size > s.settings.max_total_bytes:
                        raise HTTPException(413, "archivo demasiado grande")
                    digest.update(chunk)
                    target.write(chunk)
            staged_source = temp_dir / "staged" / "src"
            try:
                files, skipped = import_source(archive_path, staged_source, s.settings)
            except ImportError_ as exc:
                raise HTTPException(422, str(exc)) from exc
            if not files:
                raise HTTPException(422, "el ZIP no contiene archivos importables")
            try:
                project, _manifest = s.create_zip_project(
                    name=display_name,
                    archive_name=archive_name,
                    archive_sha256=digest.hexdigest(),
                    archive_size_bytes=size,
                    staged_source_dir=staged_source,
                    files=files,
                    skipped=skipped,
                )
            except (OSError, ValueError) as exc:
                raise HTTPException(422, f"No se pudo publicar el ZIP como proyecto: {exc}") from exc
        processing = _queue_project_pipeline(
            s, project.id, background_tasks, reserved=True
        )
        reserved = False
        return {"project": project, "processing": processing}
    finally:
        if reserved:
            _release_pipeline_reservation()


@app.get("/api/projects/{project_id}/processing")
def project_processing(project_id: str) -> object:
    s = store()
    _require(s, project_id)
    state = s.get_processing(project_id)
    if state is None:
        raise HTTPException(409, "el proyecto aún no tiene procesamiento automático")
    return state


@app.post("/api/projects/{project_id}/processing/retry", status_code=202)
def retry_project_processing(project_id: str, background_tasks: BackgroundTasks) -> object:
    s = store()
    _require(s, project_id)
    if not s.has_snapshot(project_id):
        raise HTTPException(409, "el proyecto no tiene archivos fuente para reintentar")
    current = s.get_processing(project_id)
    if current is None or current.status not in {"failed", "interrupted"}:
        raise HTTPException(409, "solo se puede reintentar un análisis fallido o interrumpido")
    return _queue_project_pipeline(s, project_id, background_tasks, retry=True)


@app.post("/api/projects/{project_id}/imports", status_code=201)
def import_batch(project_id: str, body: NewImport) -> Manifest:
    s = store()
    _require(s, project_id)
    if s.has_snapshot(project_id):
        raise HTTPException(409, "este proyecto ya tiene un lote; crea otro proyecto para importar otro ZIP")
    src = Path(body.path)
    roots = s.settings.import_roots
    if roots and not any(src.resolve().is_relative_to(r) for r in roots):
        raise HTTPException(403, "ruta fuera de SGM_IMPORT_ROOTS")
    if not src.exists():
        raise HTTPException(422, "ruta inexistente")
    try:
        return s.import_batch(project_id, src)
    except ImportError_ as e:
        raise HTTPException(422, str(e)) from e


@app.post("/api/projects/{project_id}/uploads", status_code=201)
async def upload_zip(project_id: str, file: UploadFile) -> Manifest:
    """Importa un ZIP de proyecto o un único archivo SAS subido desde el navegador."""
    import tempfile
    from pathlib import PurePosixPath

    s = store()
    _require(s, project_id)
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
        if s.has_snapshot(project_id):
            try:
                files, _skipped = import_source(
                    source, Path(tmp) / "validation", s.settings
                )
            except ImportError_ as e:
                raise HTTPException(422, str(e)) from e
            if not files:
                raise HTTPException(422, "el archivo no contiene programas importables")
            raise HTTPException(
                409,
                "este proyecto ya tiene un lote; crea otro proyecto para importar otro ZIP",
            )
        try:
            return s.import_batch(project_id, source.parent if is_sas else source)
        except ImportError_ as e:
            raise HTTPException(422, str(e)) from e


@app.get("/api/projects/{project_id}/inventory")
def inventory(project_id: str) -> Manifest:
    s = store()
    _require(s, project_id)
    return s.get_manifest(project_id)


@app.post("/api/projects/{project_id}/analyses", status_code=201)
def run_analysis(project_id: str) -> AnalysisSummary:
    s = store()
    _require(s, project_id)
    return summarize(analyze_project(s, project_id))


@app.get("/api/projects/{project_id}/analyses")
def get_analysis_summary(project_id: str) -> AnalysisSummary:
    s = store()
    _require(s, project_id)
    analysis = load_analysis(s, project_id)
    if analysis is None:
        raise HTTPException(409, "el proyecto aún no fue analizado")
    return summarize(analysis)


def _analysis(project_id: str):
    s = store()
    _require(s, project_id)
    a = load_analysis(s, project_id)
    if a is None:
        raise HTTPException(409, "el proyecto aún no fue analizado")
    return a


@app.get("/api/projects/{project_id}/programs")
def list_programs(project_id: str) -> list[dict]:
    return [
        {"file": p.file, "statements": p.stats.statements, "findings": len(p.findings)}
        for p in _analysis(project_id).programs
    ]


@app.get("/api/projects/{project_id}/programs/{path:path}")
def get_program(project_id: str, path: str) -> ParsedProgram:
    for p in _analysis(project_id).programs:
        if p.file == path:
            return p
    raise HTTPException(404, "programa no encontrado")


@app.get("/api/projects/{project_id}/source/{path:path}")
def source_evidence(project_id: str, path: str, line: int) -> PlainTextResponse:
    s = store()
    _require(s, project_id)
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
        "\n".join(f"{n:>5} | {lines[n - 1]}" for n in range(start, end + 1)),
        media_type="text/plain; charset=utf-8",
    )


@app.get("/api/projects/{project_id}/dependencies")
def dependencies(project_id: str) -> DependencyReport:
    s = store()
    _require(s, project_id)
    return load_dependencies(s, project_id) or build_dependencies(s, project_id)


class Decision(BaseModel):
    status: str
    note: str | None = None


@app.post("/api/projects/{project_id}/plans", status_code=201)
def create_plans(project_id: str) -> dict:
    s = store()
    _require(s, project_id)
    ps = generate_plans(s, project_id)
    return {"project_id": project_id, "plans": len(ps.plans), "rules_version": ps.rules_version}


def _plans(project_id: str) -> PlanSet:
    s = store()
    _require(s, project_id)
    ps = load_plans(s, project_id)
    if ps is None:
        raise HTTPException(409, "los planes aún no fueron generados")
    return ps


@app.get("/api/projects/{project_id}/plans")
def list_plans(project_id: str) -> list[dict]:
    out = []
    for p in _plans(project_id).plans:
        steps = p.steps + [x for c in p.children for x in c.steps]
        out.append(
            {
                "program": p.program,
                "job_name": p.job_name,
                "job_status": p.job_status,
                "steps": len(steps),
                "pending": sum(1 for x in steps if x.pending),
                "done": sum(1 for x in steps if x.status in ("verificado", "validado_manualmente")),
            }
        )
    return out


@app.get("/api/projects/{project_id}/plans/grid-recommendations")
def list_grid_recommendations(project_id: str) -> list[dict]:
    return [item.model_dump(mode="json") for item in _plans(project_id).grid_recommendations]


def _talend_apply_root() -> str:
    base = os.environ.get("TALEND_APPLY_FOLDER", "Process/PruebasWebSAS").replace("\\", "/").strip("/")
    if not base:
        base = "Process/PruebasWebSAS"
    return base


def _talend_apply_folder(program: str | None = None, *, project_id: str | None = None) -> str:
    base = _talend_apply_root()
    project = store().get_project(project_id) if project_id else None
    # Los planes unitarios/documentales sin proyecto persistido conservan el
    # destino anterior; los proyectos del portal reciben una ruta aislada.
    if project is not None:
        archive_or_project_name = project.archive_name or project.name
        slug_source = PurePosixPath(archive_or_project_name.replace("\\", "/")).stem
        slug = re.sub(r"[^\w.-]+", "-", slug_source, flags=re.UNICODE).strip(" .-_").casefold()
        slug = slug[:48] or "proyecto"
        base = f"{base}/{slug}-{project.id}"
    if not program:
        return base
    source_parent = PurePosixPath(program.replace("\\", "/")).parent.as_posix()
    if source_parent in {"", "."}:
        return base
    return f"{base}/{source_parent}"


def _talend_apply_preview_id(spec) -> str:
    identity = {
        "spec": spec.model_dump(by_alias=True, mode="json"),
        "arguments": spec.to_mcp_arguments(),
    }
    canonical = json.dumps(identity, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _talend_apply_spec(project_id: str, program: str, plans: PlanSet | None = None):
    from sas_grid_migrator.talend_adapter.apply_spec import build_apply_spec

    plans = plans or _plans(project_id)
    plan = next((item for item in plans.plans if item.program == program), None)
    if plan is None:
        raise HTTPException(404, "plan no encontrado")
    folder_paths = {
        item.program: _talend_apply_folder(item.program, project_id=project_id)
        for item in plans.plans
    }
    try:
        spec = build_apply_spec(
            plan,
            folder_paths[program],
            related_plans=plans.plans,
            related_folder_paths=folder_paths,
        )
    except ValueError as e:
        raise HTTPException(422, str(e)) from e
    return plan, spec


def _talend_batch_bundle(project_id: str) -> tuple[list, dict[str, object], str]:
    from sas_grid_migrator.talend_adapter.apply_spec import build_apply_spec

    plans = _plans(project_id)
    dependency_report = load_dependencies(store(), project_id)
    ordered = order_plans_for_batch(plans.plans, dependency_report.processing_order if dependency_report else [])
    folder_paths = {
        item.program: _talend_apply_folder(item.program, project_id=project_id)
        for item in plans.plans
    }
    specs = {}
    revision_items = []
    for plan in ordered:
        try:
            spec = build_apply_spec(
                plan,
                folder_paths[plan.program],
                related_plans=plans.plans,
                related_folder_paths=folder_paths,
            )
        except ValueError as e:
            raise HTTPException(422, str(e)) from e
        specs[plan.program] = spec
        revision_items.append(
            {
                "program": plan.program,
                "preview_id": _talend_apply_preview_id(spec),
                "folder_path": spec.folder_path,
            }
        )
    if not ordered or not any(spec.ready_for_creation for spec in specs.values()):
        raise HTTPException(409, "El proyecto no contiene Jobs con componentes, variables de contexto o Jobs hijos para crear.")
    canonical = json.dumps(revision_items, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    revision_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return ordered, specs, revision_hash


def _batch_job_key(job_name: object, folder_path: object) -> tuple[str, str] | None:
    if not isinstance(job_name, str) or not isinstance(folder_path, str):
        return None
    return job_name.casefold(), folder_path.replace("\\", "/").strip("/").casefold()


def _nested_child_spec_keys(children: list[dict]) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    pending = list(children)
    while pending:
        child = pending.pop()
        if not isinstance(child, dict):
            continue
        key = _batch_job_key(child.get("jobName"), child.get("folderPath"))
        if key:
            keys.add(key)
        nested = child.get("childJobs")
        if isinstance(nested, list):
            pending.extend(nested)
    return keys


def _child_apply_outcome(child: dict, spec) -> dict:
    child_arguments = spec.to_mcp_arguments()
    blocked_steps = [item.model_dump() for item in spec.blocked_steps]
    warnings = child.get("warnings", [])
    components = child_arguments.get("components", [])
    connections = child_arguments.get("connections", [])
    component_count = child.get("totalComponents")
    connection_count = child.get("connections")
    partial = bool(blocked_steps or warnings)
    if isinstance(component_count, int) and isinstance(components, list):
        partial = partial or component_count < len(components)
    if isinstance(connection_count, int) and isinstance(connections, list):
        partial = partial or connection_count < len(connections)
    return {
        "status": "partially_applied" if partial else "applied",
        "identity": {
            "project_id": spec.project_id,
            "program": spec.program,
            "source_sha256": spec.source_sha256,
            "rules_version": spec.rules_version,
            "job_name": spec.job_name,
            "folder_path": spec.folder_path,
        },
        "blocked_steps": blocked_steps,
        "warnings": warnings if isinstance(warnings, list) else [],
        "result": {key: value for key, value in child.items() if key != "childJobs"},
    }


@app.post("/api/projects/{project_id}/plans/{program:path}/talend-apply/preview")
def preview_talend_apply(project_id: str, program: str) -> dict:
    from sas_grid_migrator.talend_adapter.apply_spec import build_apply_spec

    plans = _plans(project_id)
    plan = next((item for item in plans.plans if item.program == program), None)
    if plan is None:
        raise HTTPException(404, "plan no encontrado")
    try:
        folder_paths = {
            item.program: _talend_apply_folder(item.program, project_id=project_id)
            for item in plans.plans
        }
        spec = build_apply_spec(
            plan,
            _talend_apply_folder(program, project_id=project_id),
            related_plans=plans.plans,
            related_folder_paths=folder_paths,
        )
    except ValueError as e:
        raise HTTPException(422, str(e)) from e
    return {
        "ready": spec.ready_for_creation,
        "preview_id": _talend_apply_preview_id(spec),
        "tools": ["talend_job_apply_custom_spec"],
        "identity": {
            "contract_version": spec.contract_version,
            "project_id": spec.project_id,
            "program": spec.program,
            "source_sha256": spec.source_sha256,
            "rules_version": spec.rules_version,
            "job_name": spec.job_name,
            "folder_path": spec.folder_path,
        },
        "components": [item.model_dump(by_alias=True, exclude_none=True) for item in spec.components],
        "child_jobs": [
            {
                "jobName": item.get("jobName"),
                "folderPath": item.get("folderPath"),
                "components": len(item.get("components", [])),
                "connections": len(item.get("connections", [])),
            }
            for item in spec.child_jobs
        ],
        "connections": [item.model_dump(by_alias=True) for item in spec.connections],
        "contexts": [item.model_dump() for item in spec.contexts],
        "blocked_steps": [item.model_dump() for item in spec.blocked_steps],
        "arguments": spec.to_mcp_arguments(),
    }


async def _apply_talend_plan(project_id: str, program: str) -> dict:
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    plans = _plans(project_id)
    _plan, spec = _talend_apply_spec(project_id, program, plans)
    s = store()
    if not spec.ready_for_creation:
        raise HTTPException(409, "No hay componentes ni variables de contexto para crear el Job.")
    identity = {
        "project_id": spec.project_id,
        "program": spec.program,
        "source_sha256": spec.source_sha256,
        "rules_version": spec.rules_version,
        "job_name": spec.job_name,
        "folder_path": spec.folder_path,
    }
    revision_hash = _talend_apply_preview_id(spec)
    persist_state = s.get_project(project_id) is not None
    previous = s.get_talend_apply_state(project_id, program) if persist_state else None
    if previous is not None:
        if previous["revision_hash"] != revision_hash:
            raise HTTPException(
                409,
                "El Job ya tiene una implementación con otra revisión; crea un nuevo ZIP/proyecto para evitar sobrescribirlo.",
            )
        if previous["status"] == "applied":
            return previous["result"]
        if previous["status"] == "conflict":
            raise HTTPException(409, previous["error"] or "El destino Talend tiene un conflicto pendiente.")
        if previous["status"] == "running":
            raise HTTPException(409, "La implementación de este Job ya está en curso.")
    if persist_state and spec.child_jobs:
        nested_child_keys = _nested_child_spec_keys(spec.child_jobs)
        for related_plan in plans.plans:
            if related_plan.program == program:
                continue
            child_key = _batch_job_key(
                related_plan.job_name,
                _talend_apply_folder(related_plan.program, project_id=project_id),
            )
            if child_key not in nested_child_keys:
                continue
            _child_plan, child_spec = _talend_apply_spec(project_id, related_plan.program, plans)
            child_previous = s.get_talend_apply_state(project_id, related_plan.program)
            if child_previous is None:
                continue
            if child_previous["revision_hash"] != _talend_apply_preview_id(child_spec):
                raise HTTPException(
                    409,
                    f"El Job hijo {related_plan.program} ya tiene una implementación con otra revisión; crea un nuevo ZIP/proyecto para evitar sobrescribirlo.",
                )
            if child_previous["status"] == "conflict":
                raise HTTPException(
                    409,
                    child_previous["error"] or f"El Job hijo {related_plan.program} tiene un conflicto pendiente.",
                )
            if child_previous["status"] == "running":
                raise HTTPException(409, f"La implementación del Job hijo {related_plan.program} ya está en curso.")
    if not _talend_write_enabled():
        raise HTTPException(403, "El MCP está en solo lectura. Configura TALEND_MCP_READONLY=false para habilitar la creación.")
    if persist_state:
        s.save_talend_apply_state(
            project_id,
            program,
            revision_hash=revision_hash,
            status="running",
            identity=identity,
        )
    try:
        result = await _talend().apply_custom_spec(spec.to_mcp_arguments())
    except TalendError as e:
        from sas_grid_migrator.domain.redaction import redact

        error = redact(str(e), "mcp-error.txt")
        conflict = bool(
            re.search(
                r"\b(CONFLICT|ALREADY_EXISTS|JOB_EXISTS)\b|colisi[oó]n|ya existe|already exists|target exists|job exists",
                error,
                re.IGNORECASE,
            )
        )
        if persist_state:
            s.save_talend_apply_state(
                project_id,
                program,
                revision_hash=revision_hash,
                status="conflict" if conflict else "failed",
                identity=identity,
                error=error,
            )
        raise HTTPException(409 if conflict else 502, error) from e
    applied_component_count = result.get("totalComponents")
    applied_connection_count = result.get("connections")
    warnings = result.get("warnings", [])
    partial = bool(spec.blocked_steps or warnings)
    if isinstance(applied_component_count, int):
        partial = partial or applied_component_count < len(spec.components)
    if isinstance(applied_connection_count, int):
        partial = partial or applied_connection_count < len(spec.connections)
    outcome = {
        "status": "partially_applied" if partial else "applied",
        "identity": identity,
        "blocked_steps": [item.model_dump() for item in spec.blocked_steps],
        "warnings": warnings,
        "result": result,
    }
    if persist_state:
        s.save_talend_apply_state(
            project_id,
            program,
            revision_hash=revision_hash,
            status=outcome["status"],
            identity=identity,
            result=outcome,
        )
    return outcome


@app.post("/api/projects/{project_id}/talend-apply-batch", status_code=202)
async def start_talend_apply_batch(project_id: str, background_tasks: BackgroundTasks) -> dict:
    s = store()
    _require(s, project_id)
    if not _talend_write_enabled():
        raise HTTPException(403, "El MCP está en solo lectura. Configura TALEND_MCP_READONLY=false para habilitar la creación.")
    ordered, _specs, revision_hash = _talend_batch_bundle(project_id)
    programs = [plan.program for plan in ordered]
    try:
        snapshot, started = s.begin_talend_apply_batch(project_id, revision_hash, programs)
    except ValueError as e:
        raise HTTPException(409, str(e)) from e
    if started:
        background_tasks.add_task(_run_talend_apply_batch, project_id, revision_hash, programs)
    return snapshot


@app.get("/api/projects/{project_id}/talend-apply-batch")
def talend_apply_batch_status(project_id: str) -> dict:
    s = store()
    _require(s, project_id)
    state = s.get_talend_apply_batch_state(project_id)
    if state is not None:
        return state
    return {
        "project_id": project_id,
        "revision_hash": None,
        "status": "not_started",
        "programs": [],
        "jobs": [],
        "current_program": None,
        "completed_jobs": 0,
        "total_jobs": 0,
        "error": None,
        "warnings": [],
        "attempt_count": 0,
        "started_at": None,
        "updated_at": None,
    }


async def _run_talend_apply_batch(project_id: str, revision_hash: str, ordered_programs: list[str]) -> None:
    s = store()
    snapshot = s.get_talend_apply_batch_state(project_id)
    if snapshot is None or snapshot["revision_hash"] != revision_hash:
        return
    jobs_by_program = {item["program"]: item for item in snapshot["jobs"]}
    jobs = [
        jobs_by_program.get(program, {"program": program, "status": "pending", "result": None, "error": None})
        for program in ordered_programs
    ]

    cycle_warnings: list[str] = []
    try:
        ordered, specs, current_revision = _talend_batch_bundle(project_id)
        dependency_report = load_dependencies(s, project_id)
        cycle_warnings = [
            "Se detectó un ciclo de dependencias entre "
            f"{', '.join(cycle)}. El lote usará un orden estable dentro de ese ciclo."
            for cycle in (dependency_report.cycles if dependency_report else [])
        ]
        if current_revision != revision_hash or [item.program for item in ordered] != ordered_programs:
            raise HTTPException(409, "El plan del proyecto cambió mientras se preparaba el lote; vuelve a revisar el proyecto.")
    except HTTPException as e:
        s.update_talend_apply_batch_state(
            project_id,
            status="conflict" if e.status_code == 409 else "failed",
            jobs=jobs,
            current_program=None,
            completed_count=sum(job["status"] in {"applied", "partially_applied", "failed", "conflict"} for job in jobs),
            error=str(e.detail),
            warnings=cycle_warnings,
        )
        return

    plans = _plans(project_id)
    key_to_programs: dict[tuple[str, str], list[str]] = {}
    for plan in plans.plans:
        spec = specs.get(plan.program)
        if spec is not None:
            key = _batch_job_key(spec.job_name, spec.folder_path)
            if key:
                key_to_programs.setdefault(key, []).append(plan.program)
    confirmed_children: set[str] = set()
    terminal = {"applied", "partially_applied", "failed", "conflict"}

    def persist(status: str, current_program: str | None = None, error: str | None = None) -> None:
        completed = sum(job["status"] in terminal for job in jobs)
        s.update_talend_apply_batch_state(
            project_id,
            status=status,
            jobs=jobs,
            current_program=current_program,
            completed_count=completed,
            error=error,
            warnings=cycle_warnings,
        )

    persist("running")
    for index, program in enumerate(ordered_programs):
        job = jobs[index]
        try:
            _current_order, _current_specs, current_revision = _talend_batch_bundle(project_id)
        except HTTPException as e:
            job.update(status="conflict" if e.status_code == 409 else "failed", error=str(e.detail))
            persist("conflict" if e.status_code == 409 else "running")
            if e.status_code == 409:
                return
            continue
        if current_revision != revision_hash:
            job.update(
                status="conflict",
                error="El plan del proyecto cambió durante la implementación; se detuvo el lote para evitar mezclar revisiones.",
            )
            persist("conflict", error=job["error"])
            return
        if job["status"] == "applied" or program in confirmed_children:
            continue
        job.update(status="running", error=None)
        persist("running", program)
        try:
            outcome = await _apply_talend_plan(project_id, program)
        except HTTPException as e:
            message = str(e.detail)
            is_conflict = e.status_code == 409 and bool(
                re.search(
                    r"\b(CONFLICT|ALREADY_EXISTS|JOB_EXISTS)\b|colisi[oó]n|ya existe|already exists|target exists|job exists|revisi[oó]n|destino|sobrescribir",
                    message,
                    re.IGNORECASE,
                )
            )
            job.update(status="conflict" if is_conflict else "failed", result=None, error=message)
            persist("running")
            continue
        job.update(status=outcome["status"], result=outcome, error=None)
        result = outcome.get("result")
        if isinstance(result, dict):
            for child in collect_child_results(result):
                key = _batch_job_key(child.get("jobName"), child.get("folderPath"))
                matching_programs = key_to_programs.get(key, []) if key else []
                if len(matching_programs) != 1:
                    continue
                child_program = matching_programs[0]
                if child_program == program:
                    continue
                child_job = next((item for item in jobs if item["program"] == child_program), None)
                if child_job is None or child_job["status"] == "applied":
                    confirmed_children.add(child_program)
                    continue
                child_outcome = _child_apply_outcome(child, specs[child_program])
                child_job.update(status=child_outcome["status"], result=child_outcome, error=None)
                s.save_talend_apply_state(
                    project_id,
                    child_program,
                    revision_hash=_talend_apply_preview_id(specs[child_program]),
                    status=child_outcome["status"],
                    identity=child_outcome["identity"],
                    result=child_outcome,
                )
                confirmed_children.add(child_program)
        persist("running")

    states = [job["status"] for job in jobs]
    successes = sum(status in {"applied", "partially_applied"} for status in states)
    errors = sum(status in {"failed", "conflict"} for status in states)
    if errors == 0 and all(status == "applied" for status in states):
        final_status = "applied"
    elif successes:
        final_status = "partially_applied"
    elif states and all(status == "conflict" for status in states):
        final_status = "conflict"
    else:
        final_status = "failed"
    persist(final_status)


@app.post("/api/projects/{project_id}/plans/{program:path}/talend-apply")
async def apply_talend_plan(project_id: str, program: str) -> dict:
    return await _apply_talend_plan(project_id, program)


@app.get("/api/projects/{project_id}/plans/{program:path}/talend-apply")
def talend_apply_status(project_id: str, program: str) -> dict:
    s = store()
    _require(s, project_id)
    state = s.get_talend_apply_state(project_id, program)
    if state is not None:
        return state
    return {
        "status": "not_started",
        "identity": None,
        "result": None,
        "error": None,
        "started_at": None,
        "updated_at": None,
    }


@app.patch("/api/projects/{project_id}/plans/{program:path}/steps/{step_id}")
def patch_step(project_id: str, program: str, step_id: str, body: Decision) -> JobPlan:
    s = store()
    _plans(project_id)
    if not set_decision(s, project_id, program, step_id, body.status, body.note):
        raise HTTPException(422, "paso o estado inválido")
    return get_plan(s, project_id, program)  # type: ignore[return-value]


@app.get("/api/projects/{project_id}/plans/{program:path}")
def get_job_plan(project_id: str, program: str, format: str = "json"):
    _plans(project_id)
    plan = get_plan(store(), project_id, program)
    if plan is None:
        raise HTTPException(404, "plan no encontrado")
    if format == "md":
        from fastapi.responses import PlainTextResponse

        return PlainTextResponse(render_plan_md(plan), media_type="text/markdown")
    return plan


@app.post("/api/projects/{project_id}/exports", status_code=201)
def export_plans(project_id: str) -> dict:
    from sas_grid_migrator.dependency_graph.builder import load_dependencies
    from sas_grid_migrator.reporting.exports import write_exports

    s = store()
    ps = _plans(project_id)
    ps = load_plans(s, project_id) or ps
    out = s.settings.data_dir / "projects" / project_id / "exports"
    files = write_exports(ps, out, load_dependencies(s, project_id))
    return {
        "directory": str(out),
        "files": [f.name for f in files],
        "steps_csv_rows": steps_csv(ps).count("\n") - 1,
    }


@app.get("/api/projects/{project_id}/exports/{name}")
def download_export(project_id: str, name: str) -> FileResponse:
    s = store()
    _plans(project_id)
    out = s.settings.data_dir / "projects" / project_id / "exports"
    if Path(name).name != name:
        raise HTTPException(404, "exportación no encontrada")
    target = (out / name).resolve()
    if not target.is_relative_to(out.resolve()) or not target.is_file():
        raise HTTPException(404, "exportación no encontrada")
    return FileResponse(target, filename=name)


class TalendInspect(BaseModel):
    job_path: str


def _talend():
    from sas_grid_migrator.talend_adapter.adapter import TalendAdapter

    return TalendAdapter.from_env()


def _talend_write_enabled() -> bool:
    return os.environ.get("TALEND_MCP_READONLY", "false").strip().casefold() in {
        "false", "0", "no", "off"
    }


@app.get("/api/integrations/talend/health")
async def talend_health() -> dict:
    health = await _talend().health_check()
    return {**health, "write_enabled": _talend_write_enabled(), "apply_folder": _talend_apply_folder()}


@app.post("/api/integrations/talend/inspect")
async def talend_inspect(body: TalendInspect):
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    try:
        return await _talend().inspect_job(body.job_path)
    except TalendError as e:
        raise HTTPException(502, str(e)) from e


class VerifyBody(BaseModel):
    job_paths: list[str]


@app.post("/api/projects/{project_id}/plans/verify")
async def verify_project_plans(project_id: str, body: VerifyBody) -> dict:
    from sas_grid_migrator.talend_adapter.adapter import TalendError
    from sas_grid_migrator.talend_adapter.verification import Catalog, verify_plans

    s = store()
    ps = _plans(project_id)
    catalog = Catalog()
    try:
        for path in body.job_paths:
            catalog.add(await _talend().inspect_job(path))
    except TalendError as e:
        raise HTTPException(502, str(e)) from e
    stats = verify_plans(ps, catalog)
    s.plans_path(project_id).write_text(ps.model_dump_json(), encoding="utf-8")
    return {"catalog_components": sorted(catalog.components), **stats}


@app.get("/api/talend/catalog")
def talend_catalog(q: str = "", family: str | None = None) -> dict:
    from sas_grid_migrator.talend_adapter.catalog import load_catalog

    cat = load_catalog()
    return {
        "count": len(cat.components),
        "families": {f: len(v) for f, v in cat.data["families"].items()},
        "components": cat.search(q, family)[:300],
        "official_inventory": {
            "release": cat.data["official_inventory"]["release"],
            "source": cat.data["official_inventory"]["source"],
            "count": len(cat.data["official_inventory"]["components"]),
            "components": [
                {"name": name, **meta}
                for name, meta in sorted(cat.data["official_inventory"]["components"].items())
                if not q
                or q.lower() in name.lower()
                or q.lower() in meta.get("connectivity", "").lower()
            ],
        },
    }


@app.get("/api/talend/catalog/{name}")
def talend_component(name: str) -> dict:
    from sas_grid_migrator.talend_adapter.catalog import load_catalog

    cat = load_catalog()
    comp = cat.get(name)  # solo nombres del catálogo: nada del usuario llega a una ruta de archivo
    if comp is None:
        raise HTTPException(404, "componente no está en el catálogo")
    doc = Path(__file__).resolve().parents[1] / "docs" / "reference" / "talend" / f"{name}.md"
    return {
        **comp,
        "variants": cat.variants_of(name),
        "doc_markdown": doc.read_text(encoding="utf-8") if doc.exists() else None,
    }


# UI compilada (apps/web/dist): se monta al final para que /api/* tenga prioridad
_dist = Path(os.environ.get("SGM_WEB_DIST", Path(__file__).resolve().parents[1] / "web" / "dist"))
if _dist.is_dir():
    app.mount("/", StaticFiles(directory=_dist, html=True), name="web")
