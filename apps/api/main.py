from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from sas_grid_migrator import __version__
from sas_grid_migrator.config import Settings
from sas_grid_migrator.dependency_graph.builder import (
    DependencyReport,
    build_dependencies,
    load_dependencies,
)
from sas_grid_migrator.domain.models import Manifest, Project
from sas_grid_migrator.ingestion.importer import ImportError_
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

app = FastAPI(title="SAS Grid Migrator", version=__version__)


def store() -> Store:
    return Store(Settings.from_env())


class NewProject(BaseModel):
    name: str


class NewImport(BaseModel):
    path: str  # carpeta o ZIP local


def _require(s: Store, project_id: str) -> None:
    if s.get_project(project_id) is None:
        raise HTTPException(404, "proyecto no encontrado")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}


@app.post("/api/projects", status_code=201)
def create_project(body: NewProject) -> Project:
    return store().create_project(body.name)


@app.get("/api/projects")
def list_projects() -> list[Project]:
    return store().list_projects()


@app.post("/api/projects/{project_id}/imports", status_code=201)
def import_batch(project_id: str, body: NewImport) -> Manifest:
    s = store()
    _require(s, project_id)
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


class TalendInspect(BaseModel):
    job_path: str


def _talend():
    from sas_grid_migrator.talend_adapter.adapter import TalendAdapter

    return TalendAdapter.from_env()


@app.get("/api/integrations/talend/health")
async def talend_health() -> dict:
    return await _talend().health_check()


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
    s.plans_path(project_id).write_text(ps.model_dump_json())
    return {"catalog_components": sorted(catalog.components), **stats}
