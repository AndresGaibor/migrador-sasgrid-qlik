import hashlib
import json
import os
import re
import tempfile
from collections import Counter
from collections.abc import Awaitable, Callable
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from pathlib import Path, PurePosixPath
from threading import Condition
from typing import Any

from fastapi import BackgroundTasks, FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, StrictBool

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
from sas_grid_migrator.persistence.store import ProjectDeletionBlockedError, Store
from sas_grid_migrator.reporting.exports import render_plan_md, steps_csv
from sas_grid_migrator.sas_parser.analyze import (
    AnalysisSummary,
    analyze_project,
    load_analysis,
    summarize,
)
from sas_grid_migrator.sas_parser.ast import ParsedProgram
from sas_grid_migrator.talend_adapter.batch import collect_child_results, order_plans_for_batch
from sas_grid_migrator.talend_adapter.best_practices import check_job_arguments
from sas_grid_migrator.talend_adapter.naming import folder_path, folder_segment


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


class DeleteProjectConfirmation(BaseModel):
    confirmation: str


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


@app.get("/health")
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


@app.delete("/api/projects/{project_id}")
def delete_project(project_id: str, body: DeleteProjectConfirmation) -> dict[str, object]:
    s = store()
    project = s.get_project(project_id)
    if project is None:
        raise HTTPException(404, "proyecto no encontrado")
    if body.confirmation != project.name:
        raise HTTPException(422, "escribe el nombre exacto del proyecto para confirmar")
    try:
        deleted = s.delete_project(project_id)
    except ProjectDeletionBlockedError as exc:
        raise HTTPException(409, str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(409, str(exc)) from exc
    if not deleted:
        raise HTTPException(404, "proyecto no encontrado")
    return {
        "deleted": True,
        "project_id": project_id,
        "name": project.name,
        "talend_jobs_untouched": True,
    }


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
def get_analysis_summary(project_id: str) -> AnalysisSummary | None:
    s = store()
    _require(s, project_id)
    analysis = load_analysis(s, project_id)
    if analysis is None and not s.get_manifest(project_id).files:
        raise HTTPException(409, "el proyecto aún no fue analizado")
    return summarize(analysis) if analysis else None


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
    plans = _plans(project_id)
    s = store()
    out = []
    for p in plans.plans:
        steps = p.steps + [x for c in p.children for x in c.steps]
        state = s.get_talend_apply_state(project_id, p.program)
        verification = None
        if state and state.get("result"):
            try:
                current_spec = _talend_apply_spec(project_id, p.program, plans)[1]
            except (HTTPException, ValueError):
                current_spec = None
            if current_spec is not None and state.get("revision_hash") == _talend_apply_preview_id(current_spec):
                verification = state["result"].get("verification")
        verified_step_ids = {
            (item.get("program"), item.get("step_id"))
            for item in (verification or {}).get("steps", [])
            if item.get("status") == "verified"
        }
        studio_verified = sum((p.program, step.id) in verified_step_ids for step in steps)
        has_verification = verification is not None
        out.append(
            {
                "program": p.program,
                "job_name": p.job_name,
                "job_status": p.job_status,
                "steps": len(steps),
                "pending": sum(1 for x in steps if x.pending),
                "done": sum(1 for x in steps if x.status in ("verificado", "validado_manualmente")),
                "studio_verified": studio_verified,
                "studio_pending": max(0, len(steps) - studio_verified) if has_verification else 0,
                "studio_status": (
                    "unavailable" if verification and verification.get("status") == "unavailable"
                    else "verified" if has_verification and studio_verified == len(steps)
                    else "pending" if has_verification
                    else "not_checked"
                ),
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
        # Nombre acotado y saneado (sin acentos ni simbolos) mas el id: el segmento raiz repite en la ruta de
        # cada Job, y en Windows el codigo generado por Studio duplica carpetas y nombre de Job.
        slug = folder_segment(slug_source).casefold()[:30].strip("._-") or "proyecto"
        base = f"{base}/{slug}-{project.id}"
    if not program:
        return base
    source_parent = PurePosixPath(program.replace("\\", "/")).parent.as_posix()
    if source_parent in {"", "."}:
        return base
    # Las carpetas del proyecto SAS se sanean: `src`/`tests`/`target` rompen Git en Talend, y los acentos, los
    # simbolos y las rutas largas dan problemas en el codigo generado y en Windows.
    return folder_path(base, source_parent)


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
            error_handling=True,
            max_components=_max_apply_components(),
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
                error_handling=True,
                max_components=_max_apply_components(),
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


def _spec_review_warnings(spec) -> list[str]:
    warnings = []
    drafts = sum(item.draft_only for item in spec.components)
    if drafts:
        warnings.append(f"{drafts} componente(s) en borrador; completa su configuración en Talend Studio.")
    if spec.instructions.get("pending"):
        warnings.append("Hay información SAS pendiente de resolver; revisa los contextos TODO del Job.")
    return warnings


async def _child_apply_outcome(child: dict, spec) -> dict:
    child_arguments = spec.to_mcp_arguments()
    blocked_steps = [item.model_dump() for item in spec.blocked_steps]
    child_warnings = child.get("warnings", [])
    warnings = list(child_warnings) if isinstance(child_warnings, list) else []
    review_warnings = _spec_review_warnings(spec)
    components = child_arguments.get("components", [])
    connections = child_arguments.get("connections", [])
    component_count = child.get("totalComponents")
    connection_count = child.get("connections")
    partial = bool(blocked_steps or warnings)
    if isinstance(component_count, int) and isinstance(components, list):
        partial = partial or component_count < len(components)
    if isinstance(connection_count, int) and isinstance(connections, list):
        partial = partial or connection_count < len(connections)
    verification = await _verify_applied_job(spec, child)
    design_errors = verification.get("design_errors", [])
    if design_errors:
        warnings.append(_design_errors_warning(design_errors))
        partial = True
    elif verification.get("studio_problems") is not None and not verification["studio_problems"]["clean"]:
        warnings.append("Talend Studio reporta problemas de diseño. Revísalos antes de probar o publicar el Job.")
        partial = True
    if verification["status"] == "unavailable" or verification["pending_steps"]:
        pending_count = verification["pending_steps"]
        warnings.append(
            f"La lectura de Studio dejó {pending_count} paso(s) sin comprobar en el Job hijo."
            if verification["status"] != "unavailable"
            else "No se pudo leer el Job hijo de vuelta desde Studio."
        )
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
        "review_required": bool(review_warnings or blocked_steps or warnings or partial),
        "review_warnings": review_warnings,
        "design_errors": design_errors,
        "best_practices": _best_practices(spec),
        "verification": verification,
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
            error_handling=True,
            max_components=_max_apply_components(),
        )
    except ValueError as e:
        raise HTTPException(422, str(e)) from e
    return {
        "ready": spec.ready_for_creation and _component_limit_error(spec) is None,
        "component_count": len(spec.components),
        "split_into_children": bool(spec.instructions.get("split")),
        "component_limit": _max_apply_components(),
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


def _verification_check(status: str, expected: Any = None, actual: Any = None, reason: str | None = None) -> dict[str, Any]:
    return {"status": status, "expected": expected, "actual": actual, "reason": reason}


def _normalized_schema(schema: dict[str, Any]) -> tuple[str, tuple[tuple[str, str, bool | None], ...]]:
    connector = str(schema.get("connector") or "FLOW").casefold()
    columns = schema.get("columns") if isinstance(schema.get("columns"), list) else []
    signature = tuple(sorted(
        (
            str(column.get("name") or "").casefold(),
            str(column.get("type") or "").casefold(),
            column.get("nullable") if isinstance(column.get("nullable"), bool) else None,
        )
        for column in columns if isinstance(column, dict)
    ))
    return connector, signature


def _normalized_connection(connection: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(connection.get("connectorName") or connection.get("connector_name") or "").casefold(),
        str(connection.get("source") or "").casefold(),
        str(connection.get("target") or "").casefold(),
        str(connection.get("label") or "").casefold(),
    )


def _expected_mapper_entries(component: dict[str, Any]) -> list[tuple[str, str, str, str, bool | None]]:
    mapper = component.get("mapper") or {}
    entries: list[tuple[str, str, str, str, bool | None]] = []
    for table in mapper.get("outputs", []) if isinstance(mapper.get("outputs"), list) else []:
        if not isinstance(table, dict):
            continue
        for column in table.get("columns", []) if isinstance(table.get("columns"), list) else []:
            if not isinstance(column, dict):
                continue
            entries.append((
                str(table.get("name") or "").casefold(),
                str(column.get("name") or "").casefold(),
                str(column.get("expression") or "").replace(" ", "").casefold(),
                str(column.get("type") or "").casefold(),
                column.get("nullable") if isinstance(column.get("nullable"), bool) else None,
            ))
    return entries


async def _verify_job_arguments(arguments: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    """Vuelve a leer un Job de Studio y compara los artefactos enviados por el portal."""
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    requested_components = [item for item in arguments.get("components", []) if isinstance(item, dict)]
    aliases = result.get("componentAliases") if isinstance(result.get("componentAliases"), dict) else {}
    actual_name_for = lambda name: str(aliases.get(name, name))
    requested_names = {str(item.get("uniqueName") or "") for item in requested_components}
    expected_edges = [
        {
            **connection,
            "source": actual_name_for(str(connection.get("source") or "")),
            "target": actual_name_for(str(connection.get("target") or "")),
        }
        for connection in arguments.get("connections", []) if isinstance(connection, dict)
    ]
    item_path = result.get("itemPath") or (result.get("result") or {}).get("itemPath")
    job_name = str(arguments.get("jobName") or result.get("jobName") or "")
    program = str((arguments.get("instructions") or {}).get("source", {}).get("program") or "")
    verification: dict[str, Any] = {
        "job_name": job_name,
        "program": program,
        "checked_at": datetime.now(UTC).isoformat(),
        "item_path": str(item_path) if item_path else None,
        "status": "unavailable",
        "reason": None,
        "components_requested": len(requested_names),
        "components_created": None,
        "missing_components": [],
        "steps": [],
        "configured_steps": 0,
        "pending_steps": 0,
    }
    instructions = arguments.get("instructions") or {}
    all_steps = list(instructions.get("steps") or [])
    for macro in instructions.get("macros") or []:
        all_steps.extend(macro.get("steps") or [])

    def mark_unavailable_steps(reason: str) -> list[dict[str, Any]]:
        return [
            {
                "step_id": step.get("id"),
                "talend_unique_name": step.get("talendUniqueName"),
                "studio_unique_name": None,
                "program": program,
                "job_name": job_name,
                "checked_at": verification["checked_at"],
                "status": "unavailable",
                "reason": reason,
                "checks": {},
            }
            for step in all_steps if isinstance(step, dict)
        ]
    if not item_path:
        verification["reason"] = "La respuesta de creación no incluyó la ruta del Job .item para inspeccionarlo."
        verification["steps"] = mark_unavailable_steps(verification["reason"])
        verification["pending_steps"] = len(verification["steps"])
        return verification
    try:
        inspection = await _talend().inspect_job(str(item_path))
    except TalendError as e:
        verification["reason"] = redact(str(e), "mcp-inspect-error.txt")
        verification["steps"] = mark_unavailable_steps(verification["reason"])
        verification["pending_steps"] = len(verification["steps"])
        return verification

    actual_components = {item.unique_name: item for item in inspection.components}
    verification["status"] = "inspected"
    verification["components_created"] = len(actual_components)
    verification["missing_components"] = sorted(
        name for name in requested_names if actual_name_for(name) not in actual_components
    )
    actual_connections = Counter(_normalized_connection(item) for item in inspection.connection_details)
    expected_connection_counts = Counter(
        _normalized_connection(item)
        for item in expected_edges
    )
    instruction_data = arguments.get("instructions") or {}
    all_steps = list(instruction_data.get("steps") or [])
    for macro in instruction_data.get("macros") or []:
        all_steps.extend(macro.get("steps") or [])
    components_by_name = {str(item.get("uniqueName") or ""): item for item in requested_components}
    for step in all_steps:
        if not isinstance(step, dict):
            continue
        unique_name = str(step.get("talendUniqueName") or "")
        actual_unique_name = actual_name_for(unique_name) if unique_name else ""
        expected_component = components_by_name.get(unique_name)
        actual_component = actual_components.get(actual_unique_name)
        reasons: list[str] = []
        checks: dict[str, dict[str, Any]] = {}
        if not unique_name or expected_component is None:
            checks["component"] = _verification_check(
                "pending", reason="El plan no asignó un componente Talend a este paso SAS."
            )
            reasons.append("No tiene componente Talend asociado.")
        elif actual_component is None:
            checks["component"] = _verification_check(
                "pending", unique_name, None, "El componente solicitado no aparece en la lectura de Studio."
            )
            reasons.append("El componente no aparece en Studio.")
        else:
            component_matches = actual_component.component == expected_component.get("componentName")
            checks["component"] = _verification_check(
                "verified" if component_matches else "pending",
                expected_component.get("componentName"), actual_component.component,
                None if component_matches else "El tipo de componente leído difiere del solicitado.",
            )
            if not component_matches:
                reasons.append("El tipo de componente no coincide.")
            expected_parameters = expected_component.get("parameters") or {}
            actual_parameters = actual_component.parameter_values or {}
            parameter_mismatches = {
                key: {"expected": value, "actual": actual_parameters.get(key)}
                for key, value in expected_parameters.items()
                if key not in actual_parameters or str(actual_parameters[key]) != str(value)
            }
            checks["parameters"] = _verification_check(
                "verified" if not parameter_mismatches else "pending",
                expected_parameters,
                {key: actual_parameters.get(key) for key in expected_parameters},
                None if not parameter_mismatches else "Uno o más parámetros no coinciden con la especificación aplicada.",
            )
            if parameter_mismatches:
                reasons.append("Hay parámetros que no coinciden.")
            expected_schema = expected_component.get("schema")
            if expected_schema:
                expected_signature = _normalized_schema(expected_schema)
                actual_signatures = [_normalized_schema(item) for item in actual_component.schemas]
                schema_matches = expected_signature in actual_signatures
                checks["schema"] = _verification_check(
                    "verified" if schema_matches else "pending",
                    expected_signature,
                    actual_signatures,
                    None if schema_matches else "El esquema esperado no coincide con los esquemas leídos en Studio.",
                )
                if not schema_matches:
                    reasons.append("El esquema no coincide.")
            else:
                checks["schema"] = _verification_check("not_required")
            expected_mapper = _expected_mapper_entries(expected_component)
            if expected_mapper:
                actual_mapper = [
                    (
                        str(entry.get("table") or "").casefold(),
                        str(entry.get("name") or "").casefold(),
                        str(entry.get("expression") or "").replace(" ", "").casefold(),
                        str(entry.get("type") or "").casefold(),
                        entry.get("nullable") if isinstance(entry.get("nullable"), bool) else None,
                    )
                    for entry in inspection.mapper_entries
                    if entry.get("componentUniqueName") == actual_unique_name
                ]
                mapper_matches = Counter(expected_mapper) == Counter(actual_mapper)
                owner_known = all(
                    entry.get("componentUniqueName")
                    for entry in inspection.mapper_entries
                ) or not inspection.mapper_entries
                checks["mapper"] = _verification_check(
                    "verified" if mapper_matches and owner_known else "pending",
                    sorted(expected_mapper), sorted(actual_mapper),
                    None if mapper_matches and owner_known else "El mapper no coincide o el MCP no identifica a qué componente pertenecen sus expresiones.",
                )
                if not mapper_matches or not owner_known:
                    reasons.append("El mapper no coincide o no se pudo atribuir al componente.")
            else:
                checks["mapper"] = _verification_check("not_required")
            actual_component_connections = Counter(
                _normalized_connection(connection)
                for connection in inspection.connection_details
                if connection.get("target") == actual_unique_name
                or connection.get("source") == actual_unique_name
            )
            expected_component_connections = Counter(
                _normalized_connection(connection)
                for connection in expected_edges
                if connection.get("target") == actual_unique_name
                or connection.get("source") == actual_unique_name
            )
            connections_match = expected_component_connections == actual_component_connections
            checks["connections"] = _verification_check(
                "verified" if connections_match else "pending",
                sorted(expected_component_connections.elements()),
                sorted(actual_component_connections.elements()),
                None if connections_match else "Las conexiones de entrada no coinciden con el plan aplicado.",
            )
            if not connections_match:
                reasons.append("Las conexiones no coinciden.")
            if expected_component.get("draftOnly"):
                reasons.append(expected_component.get("draftReason") or "El componente se creó como borrador.")
        step_status = "verified" if not reasons else "pending"
        verification["steps"].append({
            "step_id": step.get("id"),
            "talend_unique_name": unique_name or None,
            "studio_unique_name": actual_unique_name or None,
            "program": program,
            "job_name": job_name,
            "checked_at": verification["checked_at"],
            "status": step_status,
            "reason": "; ".join(dict.fromkeys(reasons)) or None,
            "checks": checks,
        })

    missing_expected = expected_connection_counts - actual_connections
    verification["connections"] = {
        "status": "verified" if not missing_expected else "pending",
        "expected": sum(expected_connection_counts.values()),
        "actual": sum(actual_connections.values()),
        "missing": list(missing_expected.elements()),
    }
    child_results = {
        (str(child.get("jobName") or "").casefold(), str(child.get("folderPath") or "").replace("\\", "/").casefold()): child
        for child in result.get("childJobs", []) if isinstance(child, dict)
    }
    verification["jobs"] = []
    for child_arguments in arguments.get("childJobs", []) if isinstance(arguments.get("childJobs"), list) else []:
        if not isinstance(child_arguments, dict):
            continue
        key = (
            str(child_arguments.get("jobName") or "").casefold(),
            str(child_arguments.get("folderPath") or "").replace("\\", "/").casefold(),
        )
        child_result = child_results.get(key)
        if child_result is None:
            child_instruction = child_arguments.get("instructions") or {}
            child_steps = list(child_instruction.get("steps") or [])
            for macro in child_instruction.get("macros") or []:
                child_steps.extend(macro.get("steps") or [])
            child_reason = "La respuesta del MCP no confirmó el Job hijo."
            unavailable_steps = [
                {
                    "step_id": step.get("id"),
                    "talend_unique_name": step.get("talendUniqueName"),
                    "studio_unique_name": None,
                    "program": str(child_instruction.get("source", {}).get("program") or ""),
                    "job_name": child_arguments.get("jobName"),
                    "checked_at": verification["checked_at"],
                    "status": "unavailable",
                    "reason": child_reason,
                    "checks": {},
                }
                for step in child_steps if isinstance(step, dict)
            ]
            verification["steps"].extend(unavailable_steps)
            verification["jobs"].append({
                "job_name": child_arguments.get("jobName"),
                "folder_path": child_arguments.get("folderPath"),
                "status": "unavailable",
                "reason": child_reason,
                "steps": unavailable_steps,
            })
            continue
        child_verification = await _verify_job_arguments(child_arguments, child_result)
        verification["steps"].extend(child_verification["steps"])
        verification["jobs"].append({
            "job_name": child_verification["job_name"],
            "folder_path": child_arguments.get("folderPath"),
            "status": child_verification["status"],
            "reason": child_verification["reason"],
            "steps": child_verification["steps"],
        })
    verification["configured_steps"] = sum(item["status"] == "verified" for item in verification["steps"])
    verification["pending_steps"] = sum(item["status"] != "verified" for item in verification["steps"])
    return verification


def _design_errors(studio_items: list[dict], write_result: dict) -> list[str]:
    """Errores de diseño de un Job: vista Problemas de Studio y respuesta de la escritura."""
    found: list[str] = []
    for item in studio_items:
        if str(item.get("severity", "")).upper() != "ERROR":
            continue
        node = str(item.get("node") or "").strip()
        text = str(item.get("description") or item.get("message") or "").strip()
        found.append(f"{node}: {text}" if node and text else text or node)
    reported = write_result.get("problems")
    if isinstance(reported, dict):
        found.extend(error for error in reported.get("errors", []) if isinstance(error, str))
    return list(dict.fromkeys(error for error in found if error))


DEFAULT_MAX_COMPONENTS = 200


def _max_apply_components() -> int:
    """Tope de componentes de un Job al aplicarlo en Studio (`TALEND_MAX_COMPONENTS`)."""
    try:
        return max(1, int(os.environ.get("TALEND_MAX_COMPONENTS", DEFAULT_MAX_COMPONENTS)))
    except ValueError:
        return DEFAULT_MAX_COMPONENTS


def _component_limit_error(spec) -> str | None:
    """Mensaje si el Job supera el tope: crearlo congelaría Studio y podría quedar a medias."""
    limit = _max_apply_components()
    jobs = [(spec.job_name, len(spec.components))]
    pending = list(spec.child_jobs)
    while pending:
        child = pending.pop()
        jobs.append((str(child.get("jobName")), len(child.get("components") or [])))
        pending.extend(child.get("childJobs") or [])
    name, count = max(jobs, key=lambda item: item[1])
    if count <= limit:
        return None
    return (
        f"El Job {name} tendría {count} componentes y el máximo para aplicarlo en "
        f"Studio es {limit}. Un Job grande se parte solo en Jobs hijo cuando sus componentes son independientes; "
        f"este tiene un flujo conectado demasiado grande. Divide el programa SAS en programas más pequeños (la guía "
        f"de Talend recomienda hasta 20 componentes por Job) o sube TALEND_MAX_COMPONENTS."
    )


def _best_practices(spec) -> list[dict]:
    """Recomendaciones de buenas prácticas de Talend; no cambian el estado de la aplicación."""
    findings = check_job_arguments(spec.to_mcp_arguments())
    return [finding.model_dump(exclude_none=True) for finding in findings]


def _design_errors_warning(errors: list[str]) -> str:
    shown = "; ".join(errors[:5]) + ("…" if len(errors) > 5 else "")
    return f"Talend Studio reporta {len(errors)} error(es) de diseño: {shown}"


async def _verify_applied_job(spec, result: dict) -> dict:
    """Inspecciona cada Job en Studio y consulta sus problemas; no ejecuta Jobs."""
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    verification = await _verify_job_arguments(spec.to_mcp_arguments(), result)
    studio_items: list[dict] = []
    try:
        problems = await _talend().job_problems(spec.job_name)
    except TalendError as e:
        verification["problems_reason"] = redact(str(e), "mcp-problems-error.txt")
        verification["studio_problems"] = None
    else:
        studio_items = problems["problems"]
        verification["studio_problems"] = {
            "clean": problems["clean"],
            "items": studio_items[:20],
        }
    verification["design_errors"] = _design_errors(studio_items, result)
    return verification


async def _apply_talend_plan(
    project_id: str,
    program: str,
    *,
    allow_conflict_retry: bool = False,
    allow_missing_retry: bool = False,
    unapplied_revision_retry_programs: frozenset[str] = frozenset(),
    on_phase: Callable[[str], Awaitable[None]] | None = None,
) -> dict:
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    plans = _plans(project_id)
    _plan, spec = _talend_apply_spec(project_id, program, plans)
    s = store()
    if not spec.ready_for_creation:
        raise HTTPException(409, "No hay componentes ni variables de contexto para crear el Job.")
    if (too_big := _component_limit_error(spec)) is not None:
        raise HTTPException(422, too_big)
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
        safe_revision_retry = (
            program in unapplied_revision_retry_programs
            and previous["status"] in {"failed", "conflict"}
            and previous["result"] is None
        )
        if previous["revision_hash"] != revision_hash and not safe_revision_retry:
            raise HTTPException(
                409,
                "El Job ya tiene una implementación con otra revisión; crea un nuevo ZIP/proyecto para evitar sobrescribirlo.",
            )
        if previous["status"] == "applied" and not allow_missing_retry:
            return previous["result"]
        if previous["status"] == "conflict" and not allow_conflict_retry:
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
            safe_child_revision_retry = (
                related_plan.program in unapplied_revision_retry_programs
                and child_previous["status"] in {"failed", "conflict"}
                and child_previous["result"] is None
            )
            if (
                child_previous["revision_hash"] != _talend_apply_preview_id(child_spec)
                and not safe_child_revision_retry
            ):
                raise HTTPException(
                    409,
                    f"El Job hijo {related_plan.program} ya tiene una implementación con otra revisión; crea un nuevo ZIP/proyecto para evitar sobrescribirlo.",
                )
            if child_previous["status"] == "conflict" and not allow_conflict_retry:
                raise HTTPException(
                    409,
                    child_previous["error"] or f"El Job hijo {related_plan.program} tiene un conflicto pendiente.",
                )
            if child_previous["status"] == "running":
                raise HTTPException(409, f"La implementación del Job hijo {related_plan.program} ya está en curso.")
    if not _talend_write_enabled():
        raise HTTPException(403, "La escritura está desactivada. Habilítala en Configuración para crear Jobs.")
    if persist_state:
        s.save_talend_apply_state(
            project_id,
            program,
            revision_hash=revision_hash,
            status="running",
            identity=identity,
        )
    try:
        if on_phase is not None:
            await on_phase("applying")
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
    if on_phase is not None:
        await on_phase("inspecting")
    verification = await _verify_applied_job(spec, result)
    warnings = list(result.get("warnings", []))
    review_warnings = _spec_review_warnings(spec)
    missing = verification.get("missing_components") or []
    if missing:
        preview_names = ", ".join(missing[:5]) + ("…" if len(missing) > 5 else "")
        warnings.append(
            f"El Job creado no contiene {len(missing)} componente(s) solicitado(s): {preview_names}."
        )
    if verification.get("status") == "unavailable":
        warnings.append("No se pudo confirmar automáticamente la configuración de los flujos en Studio.")
    elif verification.get("pending_steps"):
        warnings.append(
            f"Studio confirmó {verification.get('configured_steps', 0)} paso(s); "
            f"{verification['pending_steps']} requieren revisión de componente, esquema, mapper o conexiones."
        )
    studio_problems = verification.get("studio_problems")
    design_errors = verification.get("design_errors", [])
    if design_errors:
        warnings.append(_design_errors_warning(design_errors))
    elif studio_problems is not None and not studio_problems["clean"]:
        warnings.append("Talend Studio reporta problemas de diseño. Revísalos antes de probar o publicar el Job.")
    non_verification_warnings = [
        warning for warning in warnings
        if not warning.startswith(("No se pudo confirmar automáticamente", "Studio confirmó "))
    ]
    partial = bool(spec.blocked_steps or non_verification_warnings)
    if isinstance(applied_component_count, int):
        partial = partial or applied_component_count < len(spec.components)
    if isinstance(applied_connection_count, int):
        partial = partial or applied_connection_count < len(spec.connections)
    outcome = {
        "status": "partially_applied" if partial else "applied",
        "identity": identity,
        "blocked_steps": [item.model_dump() for item in spec.blocked_steps],
        "warnings": warnings,
        "review_required": bool(review_warnings or spec.blocked_steps or warnings or verification["status"] != "inspected"),
        "review_warnings": review_warnings,
        "design_errors": design_errors,
        "best_practices": _best_practices(spec),
        "verification": verification,
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


async def _talend_batch_preflight(project_id: str) -> dict:
    from sas_grid_migrator.talend_adapter.adapter import TalendError
    from sas_grid_migrator.talend_adapter.preflight import classify_jobs

    ordered, specs, revision_hash = _talend_batch_bundle(project_id)
    try:
        inventory = await _talend().list_jobs()
    except TalendError as e:
        raise HTTPException(502, f"No se pudo comprobar el destino Talend: {e}") from e

    classified = classify_jobs([specs[plan.program] for plan in ordered], inventory)
    return {
        "project_id": project_id,
        "revision_hash": revision_hash,
        "checked_at": datetime.now(UTC).isoformat(),
        "available": True,
        "inventory_count": len(inventory),
        "total_jobs": len(ordered),
        **classified,
    }


@app.get("/api/projects/{project_id}/talend-apply-batch/preflight")
async def talend_apply_batch_preflight(project_id: str) -> dict:
    s = store()
    _require(s, project_id)
    return await _talend_batch_preflight(project_id)


class TalendBatchConfirmation(BaseModel):
    expected_revision: str = Field(pattern=r"^[0-9a-f]{64}$", min_length=64, max_length=64)


@app.post("/api/projects/{project_id}/talend-apply-batch", status_code=202)
async def start_talend_apply_batch(
    project_id: str,
    background_tasks: BackgroundTasks,
    body: TalendBatchConfirmation | None = None,
) -> dict:
    s = store()
    _require(s, project_id)
    if not _talend_write_enabled():
        raise HTTPException(403, "La escritura está desactivada. Habilítala en Configuración para crear Jobs.")
    compatibility = await _talend().custom_spec_status()
    if not compatibility["spec_supported"]:
        raise HTTPException(409, compatibility["spec_error"])
    preflight = await _talend_batch_preflight(project_id)
    if preflight["conflict_count"]:
        collisions = [
            f"{item['job_name']}: {item['reason']} {item['existing_path'] or ''}".strip()
            for item in preflight["jobs"]
            if item["action"] == "conflict"
        ]
        raise HTTPException(
            409,
            "La comprobación encontró conflictos en el destino Talend; no se modificó ningún Job. "
            + "; ".join(collisions),
        )
    ordered, _specs, revision_hash = _talend_batch_bundle(project_id)
    if preflight["revision_hash"] != revision_hash:
        raise HTTPException(
            409,
            "El plan del proyecto cambió durante la comprobación del destino; vuelve a revisar el proyecto.",
        )
    if body is not None and body.expected_revision != revision_hash:
        raise HTTPException(409, "El plan cambió desde la vista previa. Actualiza la revisión antes de crear los Jobs.")
    programs = [plan.program for plan in ordered]
    missing_programs = {
        item["program"] for item in preflight["jobs"] if item["action"] == "create"
    }
    previous_batch = s.get_talend_apply_batch_state(project_id)
    previous_jobs = previous_batch.get("jobs", []) if previous_batch else []
    previous_operations = {
        program: s.get_talend_apply_state(project_id, program) for program in programs
    }
    prior_operations_unapplied = all(
        operation is None
        or (
            operation.get("status") in {"failed", "conflict"}
            and operation.get("result") is None
        )
        for operation in previous_operations.values()
    )
    allow_revision_reset = bool(
        previous_batch
        and previous_batch.get("status") in {"failed", "conflict"}
        and previous_batch.get("programs") == programs
        and len(previous_jobs) == len(programs)
        and all(
            job.get("status") in {"failed", "conflict"}
            and job.get("result") is None
            for job in previous_jobs
        )
        and prior_operations_unapplied
        and preflight["create_count"] == len(programs)
        and preflight["update_count"] == 0
        and preflight["conflict_count"] == 0
    )
    try:
        snapshot, started = s.begin_talend_apply_batch(
            project_id,
            revision_hash,
            programs,
            retry_conflicts=True,
            retry_programs=missing_programs,
            allow_revision_reset=allow_revision_reset,
        )
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


@app.get("/api/projects/{project_id}/talend-apply-batch/summary")
def talend_apply_batch_summary(project_id: str) -> dict:
    """Resumen pre-vuelo del lote: qué se crearía y qué necesita a una persona."""
    s = store()
    _require(s, project_id)
    ordered, specs, revision_hash = _talend_batch_bundle(project_id)
    programs: list[dict[str, Any]] = []
    for plan in ordered:
        spec = specs.get(plan.program)
        if spec is None:
            continue
        draft_components = [
            {
                "unique_name": item.unique_name,
                "reason": item.draft_reason or "Información técnica pendiente; completar en Talend.",
            }
            for item in spec.components
            if item.draft_only
        ]
        programs.append({
            "program": plan.program,
            "job_name": spec.job_name,
            "folder_path": spec.folder_path,
            "ready_for_creation": spec.ready_for_creation,
            "creation_kind": "components" if spec.components or spec.child_jobs else "context_only",
            "components": len(spec.components),
            "connections": len(spec.connections),
            "contexts": len(spec.contexts),
            "child_jobs": len(spec.child_jobs),
            "blocked_steps": [item.model_dump() for item in spec.blocked_steps],
            "pending": list(spec.instructions.get("pending", [])),
            "draft_components": draft_components,
        })
    return {
        "project_id": project_id,
        "revision_hash": revision_hash,
        "destination_root": _talend_apply_folder(project_id=project_id),
        "total_jobs": len(programs),
        "creatable_jobs": sum(item["ready_for_creation"] for item in programs),
        "cycles": (report.cycles if (report := load_dependencies(s, project_id)) else []),
        "total_components": sum(item["components"] for item in programs),
        "total_connections": sum(item["connections"] for item in programs),
        "total_contexts": sum(item["contexts"] for item in programs),
        "programs": programs,
    }


async def _run_talend_apply_batch(project_id: str, revision_hash: str, ordered_programs: list[str]) -> None:
    from sas_grid_migrator.talend_adapter.adapter import TalendError
    from sas_grid_migrator.talend_adapter.preflight import classify_jobs

    s = store()
    snapshot = s.get_talend_apply_batch_state(project_id)
    if snapshot is None or snapshot["revision_hash"] != revision_hash:
        return
    jobs_by_program = {item["program"]: item for item in snapshot["jobs"]}
    jobs = [
        jobs_by_program.get(program, {"program": program, "status": "pending", "result": None, "error": None})
        for program in ordered_programs
    ]
    for job in jobs:
        job.setdefault("phase", None)

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

    try:
        inventory = await _talend().list_jobs()
    except TalendError as e:
        error = f"No se pudo volver a comprobar el destino Talend; no se escribió ningún Job: {e}"
        for job in jobs:
            if job["status"] != "applied":
                job.update(status="failed", result=None, error=error)
        persist("failed", error=error)
        return

    preflight = classify_jobs([specs[program] for program in ordered_programs], inventory)
    if preflight["conflict_count"]:
        actions = {item["program"]: item for item in preflight["jobs"]}
        for job in jobs:
            action = actions[job["program"]]
            if action["action"] == "conflict":
                job.update(status="conflict", result=None, error=action["reason"])
            elif job["status"] != "applied":
                job.update(status="pending", result=None, error=None)
        error = "La comprobación del destino encontró conflictos nuevos; no se modificó ningún Job."
        persist("conflict", error=error)
        return

    missing_programs = {
        item["program"] for item in preflight["jobs"] if item["action"] == "create"
    }

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
        if (job["status"] == "applied" and program not in missing_programs) or program in confirmed_children:
            continue
        job.update(status="running", error=None)
        persist("running", program)

        async def set_phase(phase_name: str, current: dict = job, current_program: str = program) -> None:
            current["phase"] = phase_name
            persist("running", current_program)

        try:
            outcome = await _apply_talend_plan(
                project_id,
                program,
                allow_conflict_retry=True,
                allow_missing_retry=program in missing_programs,
                unapplied_revision_retry_programs=frozenset(missing_programs),
                on_phase=set_phase,
            )
        except HTTPException as e:
            job["phase"] = None
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
        job["phase"] = None
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
                child_outcome = await _child_apply_outcome(child, specs[child_program])
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


@app.post("/api/projects/{project_id}/plans/{program:path}/talend-apply/verify")
async def verify_talend_plan(project_id: str, program: str) -> dict:
    """Actualiza solo la evidencia de lectura de Studio; no aplica ni ejecuta Jobs."""
    s = store()
    _require(s, project_id)
    plans = _plans(project_id)
    try:
        _plan, spec = _talend_apply_spec(project_id, program, plans)
    except ValueError as e:
        raise HTTPException(422, str(e)) from e
    previous = s.get_talend_apply_state(project_id, program)
    if previous is None or not isinstance(previous.get("result"), dict):
        raise HTTPException(409, "Primero crea el Job en Talend Studio para poder volver a comprobarlo.")
    revision_hash = _talend_apply_preview_id(spec)
    if previous.get("revision_hash") != revision_hash:
        raise HTTPException(409, "El plan cambió desde la creación; no se aplicará la verificación anterior a esta revisión.")
    apply_result = previous["result"].get("result")
    if not isinstance(apply_result, dict):
        raise HTTPException(409, "La creación guardada no contiene el resultado del Job que se debe inspeccionar.")
    verification = await _verify_applied_job(spec, apply_result)
    outcome = {**previous["result"], "verification": verification}
    warnings = [
        warning for warning in outcome.get("warnings", [])
        if not warning.startswith(("No se pudo confirmar automáticamente", "Studio confirmó "))
    ]
    if verification.get("status") == "unavailable":
        warnings.append("No se pudo confirmar automáticamente la configuración de los flujos en Studio.")
    elif verification.get("pending_steps"):
        warnings.append(
            f"Studio confirmó {verification.get('configured_steps', 0)} paso(s); "
            f"{verification['pending_steps']} requieren revisión de componente, esquema, mapper o conexiones."
        )
    outcome["warnings"] = warnings
    outcome["review_required"] = bool(
        outcome.get("review_required")
        or warnings
        or verification.get("status") == "unavailable"
        or verification.get("pending_steps")
    )
    s.save_talend_apply_state(
        project_id,
        program,
        revision_hash=revision_hash,
        status=previous["status"],
        identity=previous["identity"],
        result=outcome,
    )
    return outcome


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
    plans = _plans(project_id)
    if not set_decision(s, project_id, program, step_id, body.status, body.note):
        raise HTTPException(422, "paso o estado inválido")
    plan = get_plan(s, project_id, program)
    if plan is None:
        raise HTTPException(404, "plan no encontrado")
    return _annotate_plan_studio_checks(s, project_id, plan, plans)  # type: ignore[return-value]


def _annotate_plan_studio_checks(s: Store, project_id: str, plan: JobPlan, plans: PlanSet) -> dict[str, Any]:
    """Expose current apply evidence beside a step without changing its manual state."""
    data = plan.model_dump(mode="json")
    state = s.get_talend_apply_state(project_id, plan.program)
    if not state or not isinstance(state.get("result"), dict):
        return data
    try:
        spec = _talend_apply_spec(project_id, plan.program, plans)[1]
    except (HTTPException, ValueError):
        return data
    if state.get("revision_hash") != _talend_apply_preview_id(spec):
        return data
    verification = state["result"].get("verification")
    if not isinstance(verification, dict):
        return data
    by_step = {
        (item.get("program"), item.get("step_id")): {
            "status": item.get("status"),
            "reason": item.get("reason"),
            "checked_at": item.get("checked_at"),
            "talend_unique_name": item.get("talend_unique_name"),
            "studio_unique_name": item.get("studio_unique_name"),
            "checks": item.get("checks", {}),
        }
        for item in verification.get("steps", [])
        if isinstance(item, dict)
    }
    for step in data.get("steps", []):
        check = by_step.get((plan.program, step.get("id")))
        if check:
            step["studio_verification"] = check
    for child in data.get("children", []):
        for step in child.get("steps", []):
            check = by_step.get((plan.program, step.get("id")))
            if check:
                step["studio_verification"] = check
    return data


@app.get("/api/projects/{project_id}/plans/{program:path}")
def get_job_plan(project_id: str, program: str, format: str = "json"):
    plans = _plans(project_id)
    plan = get_plan(store(), project_id, program)
    if plan is None:
        raise HTTPException(404, "plan no encontrado")
    if format == "md":
        from fastapi.responses import PlainTextResponse

        return PlainTextResponse(render_plan_md(plan), media_type="text/markdown")
    return _annotate_plan_studio_checks(store(), project_id, plan, plans)


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

    return TalendAdapter.from_env(write_enabled=_talend_write_enabled())


def _talend_write_enabled() -> bool:
    """El permiso se administra desde la interfaz y se conserva en SQLite."""
    return store().talend_write_enabled()


class TalendPermissions(BaseModel):
    write_enabled: StrictBool


@app.get("/api/integrations/talend/permissions")
def talend_permissions() -> dict:
    return {"write_enabled": _talend_write_enabled()}


@app.patch("/api/integrations/talend/permissions")
def update_talend_permissions(body: TalendPermissions) -> dict:
    store().set_talend_write_enabled(body.write_enabled)
    return {"write_enabled": body.write_enabled}


@app.get("/api/integrations/talend/health")
async def talend_health() -> dict:
    health = await _talend().health_check()
    return {**health, "write_enabled": _talend_write_enabled(), "apply_folder": _talend_apply_folder()}


class TalendRestart(BaseModel):
    only_if_memory_above: int | None = Field(default=None, ge=1, le=99)
    force: StrictBool = True


@app.post("/api/integrations/talend/studio/restart")
async def talend_studio_restart(body: TalendRestart | None = None) -> dict:
    """Reinicia Talend Studio a petición: cierra sus diálogos y, si no sale, fuerza el cierre.

    Sin cuerpo reinicia siempre; con `only_if_memory_above` solo si el heap supera ese porcentaje.
    """
    from sas_grid_migrator.talend_adapter.adapter import TalendError

    if not _talend_write_enabled():
        raise HTTPException(403, "La escritura está desactivada. Habilítala en Configuración para reiniciar Studio.")
    options = body or TalendRestart()
    try:
        return await _talend().restart_studio(only_if_memory_above=options.only_if_memory_above, force=options.force)
    except TalendError as e:
        raise HTTPException(502, str(e)) from e


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
    from .integrations import talend_catalog as current_catalog

    return current_catalog(q, family)


@app.get("/api/talend/catalog/archived")
def talend_archived_catalog(q: str = "") -> dict:
    from .integrations import talend_archived_catalog as archived_catalog

    return archived_catalog(q)


@app.get("/api/talend/catalog/archived/{name}")
def talend_archived_component(name: str) -> dict:
    from .integrations import talend_archived_component as archived_component

    return archived_component(name)


@app.get("/api/talend/studio-configuration")
def talend_studio_configuration() -> dict:
    from .integrations import talend_studio_configuration as studio_configuration

    return studio_configuration()


@app.get("/api/talend/catalog/{name}")
def talend_component(name: str) -> dict:
    from .integrations import talend_component as current_component

    return current_component(name)


# UI compilada (apps/web/dist): se monta al final para que /api/* tenga prioridad
_dist = Path(os.environ.get("SGM_WEB_DIST", Path(__file__).resolve().parents[1] / "web" / "dist"))
if _dist.is_dir():
    app.mount("/", StaticFiles(directory=_dist, html=True), name="web")
