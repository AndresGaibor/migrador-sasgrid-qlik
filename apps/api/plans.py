from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse
from pydantic import BaseModel

from sas_grid_migrator.migration_planner.models import JobPlan
from sas_grid_migrator.migration_planner.service import (
    generate_plans,
    get_plan,
    load_plans,
    set_decision,
)
from sas_grid_migrator.persistence.artifacts import write_text_atomic
from sas_grid_migrator.reporting.exports import render_plan_md, steps_csv, write_exports

from .common import plans as get_plans
from .common import require_project, store

router = APIRouter(prefix="/api")


class Decision(BaseModel):
    status: str
    note: str | None = None


class VerifyBody(BaseModel):
    job_paths: list[str]


@router.post("/projects/{project_id}/plans", status_code=201)
def create_plans(project_id: str) -> dict:
    s = store()
    require_project(s, project_id)
    ps = generate_plans(s, project_id)
    return {"project_id": project_id, "plans": len(ps.plans), "rules_version": ps.rules_version}


@router.get("/projects/{project_id}/plans")
def list_plans(project_id: str) -> list[dict]:
    result = get_plans(project_id)
    out = []
    for plan in result.plans:
        steps = plan.steps + [step for child in plan.children for step in child.steps]
        out.append(
            {
                "program": plan.program,
                "job_name": plan.job_name,
                "job_status": plan.job_status,
                "steps": len(steps),
                "pending": sum(1 for step in steps if step.pending),
                "done": sum(
                    1 for step in steps if step.status in ("verificado", "validado_manualmente")
                ),
            }
        )
    return out


@router.get("/projects/{project_id}/plans/grid-recommendations")
def list_grid_recommendations(project_id: str) -> list[dict]:
    return [item.model_dump(mode="json") for item in get_plans(project_id).grid_recommendations]


@router.patch("/projects/{project_id}/plans/{program:path}/steps/{step_id}")
def patch_step(project_id: str, program: str, step_id: str, body: Decision) -> JobPlan:
    s = store()
    get_plans(project_id)
    if not set_decision(s, project_id, program, step_id, body.status, body.note):
        raise HTTPException(422, "paso o estado inválido")
    return get_plan(s, project_id, program)  # type: ignore[return-value]


@router.get("/projects/{project_id}/plans/{program:path}")
def get_job_plan(project_id: str, program: str, format: str = "json"):
    get_plans(project_id)
    plan = get_plan(store(), project_id, program)
    if plan is None:
        raise HTTPException(404, "plan no encontrado")
    if format == "md":
        return PlainTextResponse(render_plan_md(plan), media_type="text/markdown")
    return plan


@router.post("/projects/{project_id}/exports", status_code=201)
def export_plans(project_id: str) -> dict:
    from sas_grid_migrator.dependency_graph.builder import load_dependencies

    s = store()
    ps = get_plans(project_id)
    ps = load_plans(s, project_id) or ps
    out = s.settings.data_dir / "projects" / project_id / "exports"
    files = write_exports(ps, out, load_dependencies(s, project_id))
    return {
        "directory": str(out),
        "files": [file.name for file in files],
        "steps_csv_rows": steps_csv(ps).count("\n") - 1,
    }


@router.get("/projects/{project_id}/exports/{name}")
def download_export(project_id: str, name: str) -> FileResponse:
    s = store()
    get_plans(project_id)
    out = s.settings.data_dir / "projects" / project_id / "exports"
    if Path(name).name != name:
        raise HTTPException(404, "exportación no encontrada")
    target = (out / name).resolve()
    if not target.is_relative_to(out.resolve()) or not target.is_file():
        raise HTTPException(404, "exportación no encontrada")
    return FileResponse(target, filename=name)


@router.post("/projects/{project_id}/plans/verify")
async def verify_project_plans(project_id: str, body: VerifyBody) -> dict:
    from sas_grid_migrator.talend_adapter.adapter import TalendError
    from sas_grid_migrator.talend_adapter.verification import Catalog, verify_plans

    s = store()
    require_project(s, project_id)
    # Carga cruda: las ediciones del usuario viven en SQLite y no deben quedar grabadas en plans.json.
    result = load_plans(s, project_id, with_edits=False)
    if result is None:
        raise HTTPException(409, "los planes aún no fueron generados")
    catalog = Catalog()
    try:
        from .common import talend

        for path in body.job_paths:
            catalog.add(await talend().inspect_job(path))
    except TalendError as e:
        raise HTTPException(502, str(e)) from e
    stats = verify_plans(result, catalog)
    write_text_atomic(s.plans_path(project_id), result.model_dump_json())
    return {"catalog_components": sorted(catalog.components), **stats}
