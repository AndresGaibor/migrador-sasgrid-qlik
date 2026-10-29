"""Project-level migration progress and actionable pending work."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Any

from .models import PlanSet


@dataclass(frozen=True)
class Stage:
    key: str
    label: str
    status: str
    detail: str
    tab: str


@dataclass(frozen=True)
class NextAction:
    key: str
    label: str
    tab: str


@dataclass(frozen=True)
class Progress:
    stages: list[Stage]
    next: NextAction | None


@dataclass(frozen=True)
class PendingProgram:
    program: str
    job_name: str
    step_ids: list[str]


@dataclass(frozen=True)
class PendingGroup:
    reason: str
    steps: int
    programs: list[PendingProgram]


def compute_progress(
    *, files: int, processing_status: str | None,
    plan_rows: list[dict[str, Any]] | None, batch_status: str | None,
) -> Progress:
    has_files = files > 0
    analyzed = processing_status == "completed" or plan_rows is not None
    plans_ready = plan_rows is not None
    all_steps = sum(max(0, int(row.get("steps", 0))) for row in plan_rows or [])
    done_steps = sum(max(0, int(row.get("done", 0))) for row in plan_rows or [])
    all_studio = bool(plan_rows) and all(row.get("studio_status") == "verified" for row in plan_rows)
    batch_done = batch_status in {"applied", "completed"}

    labels = [
        ("upload", "Archivos", "importar"),
        ("analysis", "Análisis", "resumen"),
        ("guides", "Guías", "planes"),
        ("talend", "Jobs en Talend", "planes"),
        ("studio", "Verificación en Studio", "planes"),
        ("complete", "Migración revisada", "resumen"),
    ]
    facts = [has_files, analyzed, plans_ready, batch_done, all_studio, all_studio]
    current = next((i for i, complete in enumerate(facts) if not complete), len(facts))

    stages: list[Stage] = []
    for i, (key, label, tab) in enumerate(labels):
        status = "done" if facts[i] else "todo"
        if i == current:
            status = "current"
        if i == 1 and processing_status in {"failed", "interrupted"}:
            status = "blocked"
        if i == 3 and batch_status in {"conflict", "failed", "partial"}:
            status = "blocked"
        if i == 4 and batch_done and not all_studio:
            status = "current"
        if key == "guides" and plans_ready:
            detail = f"{len(plan_rows or [])} programas"
        elif key == "talend" and plans_ready:
            detail = f"{sum(int(r.get('studio_verified', 0)) for r in plan_rows or [])} Jobs verificados en Studio"
        elif key == "studio" and plans_ready:
            detail = f"{sum(int(r.get('done', 0)) for r in plan_rows or [])} de {all_steps} pasos"
        elif key == "analysis" and processing_status:
            detail = processing_status
        else:
            detail = "Listo" if status == "done" else "Pendiente"
        stages.append(Stage(key, label, status, detail, tab))

    if current == len(facts):
        action = None
    elif current == 0:
        action = NextAction("upload", "Cargar archivos", "importar")
    elif current == 1:
        action = NextAction("analysis", "Revisar análisis", "resumen")
    elif current == 2:
        action = NextAction("guides", "Revisar guías", "planes")
    elif current == 3:
        action = NextAction("talend", "Crear Jobs en Talend", "planes")
    elif current == 4:
        action = NextAction("studio", "Verificar en Talend Studio", "planes")
    else:
        action = NextAction("complete", "Revisar migración", "resumen")
    if batch_status in {"conflict", "failed", "partial"} and plans_ready:
        action = NextAction("studio", "Resolver y verificar en Talend Studio", "planes")
    elif batch_done and plans_ready and not all_studio:
        action = NextAction("complete", "Revisar la migración", "resumen")
    return Progress(stages, action)


def pending_groups(plans: PlanSet) -> list[PendingGroup]:
    grouped: dict[str, dict[tuple[str, str], list[str]]] = defaultdict(lambda: defaultdict(list))
    names: dict[tuple[str, str], str] = {}
    for plan in plans.plans:
        jobs = [(plan.job_name, plan.steps)] + [
            (child.name, child.steps) for child in plan.children
        ]
        for job_name, steps in jobs:
            for step in steps:
                if step.status == "descartado":
                    continue
                key = (plan.program, job_name)
                for reason in step.pending:
                    grouped[reason][key].append(step.id)
                    names[key] = job_name
    return [
        PendingGroup(
            reason=reason,
            steps=sum(len(ids) for ids in jobs.values()),
            programs=[
                PendingProgram(program, names[(program, job)], ids)
                for (program, job), ids in sorted(jobs.items())
            ],
        )
        for reason, jobs in sorted(grouped.items())
    ]
