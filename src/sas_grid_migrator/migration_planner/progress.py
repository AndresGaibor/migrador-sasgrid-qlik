"""Progreso del proyecto por etapas y pendientes agrupados por motivo (sin E/S)."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from sas_grid_migrator.migration_planner.models import PlanSet

StageKey = Literal["upload", "analysis", "guides", "studio", "complete", "verify"]
StageStatus = Literal["done", "current", "todo", "blocked"]

STAGE_LABELS: dict[str, str] = {
    "upload": "Cargar archivos",
    "analysis": "Analizar",
    "guides": "Preparar guías",
    "studio": "Crear en Studio",
    "complete": "Completar guías",
    "verify": "Verificar en Studio",
}

STAGE_TABS: dict[str, Literal["importar", "resumen", "planes"]] = {
    "upload": "importar",
    "analysis": "resumen",
    "guides": "planes",
    "studio": "planes",
    "complete": "planes",
    "verify": "planes",
}

ANALYSIS_DETAILS = {
    "completed": "completado",
    "queued": "en curso",
    "running": "en curso",
    "failed": "fallido",
    "interrupted": "interrumpido",
}

BATCH_DETAILS = {
    "applied": "Jobs creados en Studio",
    "partially_applied": "creación parcial en Studio",
    "queued": "en curso",
    "running": "en curso",
    "failed": "fallida",
    "conflict": "conflicto en Studio",
    "interrupted": "interrumpida",
}


class Stage(BaseModel):
    key: StageKey
    label: str
    status: StageStatus
    detail: str


class NextAction(BaseModel):
    key: str
    label: str
    tab: Literal["importar", "resumen", "planes"]
    reason: str


class ProjectProgress(BaseModel):
    stages: list[Stage]
    next: NextAction | None


class PendingProgram(BaseModel):
    program: str
    job_name: str
    step_ids: list[str]


class PendingGroup(BaseModel):
    reason: str
    steps: int
    programs: list[PendingProgram]


def compute_progress(
    *,
    files: int,
    processing_status: str | None,
    plan_rows: list[dict] | None,
    batch_status: str | None,
) -> ProjectProgress:
    rows = plan_rows or []
    jobs = [row for row in rows if row["steps"] > 0]
    total_steps = sum(row["steps"] for row in jobs)
    done_steps = sum(row["done"] for row in jobs)
    complete_done = bool(jobs) and all(row["done"] == row["steps"] for row in jobs)
    verify_done = bool(jobs) and all(row["studio_status"] == "verified" for row in jobs)
    verified_jobs = sum(row["studio_status"] == "verified" for row in jobs)

    studio_done = batch_status in ("applied", "partially_applied") or complete_done
    studio_blocked = batch_status in ("failed", "conflict", "interrupted")
    studio_detail = BATCH_DETAILS.get(batch_status or "", "completada" if studio_done else "pendiente")

    specs: list[tuple[str, bool, bool, str]] = [
        ("upload", files > 0, False, f"{files} archivos" if files > 0 else "sin archivos"),
        (
            "analysis",
            processing_status == "completed",
            processing_status in ("failed", "interrupted"),
            ANALYSIS_DETAILS.get(processing_status or "", "pendiente"),
        ),
        ("guides", bool(rows), False, f"{len(rows)} Jobs con guía" if rows else "sin guías"),
        ("studio", studio_done, studio_blocked, studio_detail),
        ("complete", complete_done, False, f"{done_steps} de {total_steps} pasos"),
        ("verify", verify_done, False, f"{verified_jobs} de {len(jobs)} Jobs verificados"),
    ]

    stages: list[Stage] = []
    previous_done = True
    for key, done, blocked, detail in specs:
        if done:
            status: StageStatus = "done"
        elif blocked:
            status = "blocked"
        elif not previous_done:
            status = "todo"
        else:
            status = "current"
        stages.append(Stage(key=key, label=STAGE_LABELS[key], status=status, detail=detail))
        previous_done = done

    pending = next((stage for stage in stages if stage.status != "done"), None)
    next_action = (
        NextAction(
            key=pending.key,
            label=pending.label,
            tab=STAGE_TABS[pending.key],
            reason=pending.detail,
        )
        if pending is not None
        else None
    )
    return ProjectProgress(stages=stages, next=next_action)


def pending_groups(ps: PlanSet) -> list[PendingGroup]:
    by_reason: dict[str, dict[str, PendingProgram]] = {}
    for plan in ps.plans:
        steps = [*plan.steps, *(step for child in plan.children for step in child.steps)]
        for step in steps:
            if step.status == "descartado":
                continue
            for reason in dict.fromkeys(step.pending):
                programs = by_reason.setdefault(reason, {})
                entry = programs.get(plan.program)
                if entry is None:
                    entry = PendingProgram(program=plan.program, job_name=plan.job_name, step_ids=[])
                    programs[plan.program] = entry
                entry.step_ids.append(step.id)

    groups = [
        PendingGroup(
            reason=reason,
            steps=sum(len(program.step_ids) for program in programs.values()),
            programs=list(programs.values()),
        )
        for reason, programs in by_reason.items()
    ]
    groups.sort(key=lambda group: (-group.steps, group.reason))
    return groups
