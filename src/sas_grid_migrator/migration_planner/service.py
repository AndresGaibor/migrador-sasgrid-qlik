"""Orquesta análisis → dependencias → IR → planes y conserva las decisiones humanas."""

import json
from collections import defaultdict

from sas_grid_migrator.dependency_graph.builder import build_dependencies, load_dependencies
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.intermediate_representation.models import LibraryRef
from sas_grid_migrator.macro_resolver.resolver import macro_index
from sas_grid_migrator.migration_planner.models import JobPlan, Orchestration, PlanSet
from sas_grid_migrator.migration_planner.planner import (
    grid_recommendation,
    load_grid_catalog,
    load_mapping_rules,
    plan_program,
)
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import analyze_project, load_analysis
from sas_grid_migrator.sas_parser.ast import Loc
from sas_grid_migrator.semantic_analysis.classify import load_rules

VALID_STATUS = {"propuesto", "pendiente", "verificado", "validado_manualmente", "descartado"}


def generate_plans(store: Store, project_id: str, fresh: bool = False) -> PlanSet:
    """Genera los planes. Reutiliza el análisis persistido salvo `fresh` o reglas distintas."""
    analysis = None if fresh else load_analysis(store, project_id)
    if analysis is None or analysis.rules_version != load_rules().version:
        analysis, deps = analyze_project(store, project_id), None
    else:
        deps = load_dependencies(store, project_id)
    deps = deps or build_dependencies(store, project_id)
    rules = load_mapping_rules()
    grid_catalog = load_grid_catalog()
    macro_files = {name: defs[0][0] for name, defs in macro_index(analysis.programs).items()}
    libs = {
        x.name.lower(): LibraryRef(name=x.name, engine=x.engine, path=x.path)
        for x in deps.libraries
    }
    # índices por archivo: evita recorrer tareas/aristas/pendientes por cada programa
    tasks, scheds = defaultdict(list), defaultdict(list)
    for t in deps.orchestration.tasks:
        for f in {t.resolved_program, t.source_file}:
            if f:
                tasks[f].append(t.id)
    for sc in deps.orchestration.schedules:
        scheds[sc.file].append(sc.text)
    up, down = defaultdict(set), defaultdict(set)
    for e in deps.edges:
        up[e.target].add(e.source)
        down[e.source].add(e.target)
    pending = defaultdict(list)
    for u in deps.unresolved:
        pending[u.file].append(
            f"{u.kind} {u.name} ({u.file}:{u.line}){' — ' + u.detail if u.detail else ''}"
        )
    grid_by_program, all_grid = defaultdict(list), []
    for task in deps.orchestration.tasks:
        if task.kind == "unsupported_scheduler":
            pattern_ids = ["scheduler.lsf"]
        elif task.kind == "sas_macro_step":
            pattern_ids = ["sas_macro_step.include_dispatch"]
        else:
            pattern_ids = ["sasgsub.submit" if task.kind == "sasgsub" else "sas_batch.sysin"]
            if task.kind == "sasgsub":
                pattern_ids.append("sasgsub.job_options")
                if task.params:
                    pattern_ids.append("sasgsub.set_parameters")
                if task.unknown_options:
                    pattern_ids.append("sasgsub.unverified_options")
                if task.incomplete_options:
                    pattern_ids.append("sasgsub.missing_option_value")
            if task.after or task.condition:
                pattern_ids.append("shell.inferred_sequence")
        for pattern_id in pattern_ids:
            rec = grid_recommendation(
                pattern_id,
                grid_catalog,
                rules,
                evidence=Loc(file=task.source_file, line=task.line, end_line=task.line),
                target_program=task.resolved_program,
                details={
                    "kind": task.kind,
                    "program": task.program,
                    "resolved_program": task.resolved_program,
                    "match_status": task.match_status,
                    "job_name": task.job_name,
                    "queue": task.queue,
                    "waits": task.waits,
                    "params": task.params,
                    "condition": task.condition,
                    "unknown_options": task.unknown_options,
                    "incomplete_options": task.incomplete_options,
                },
                dependencies=task.after,
            )
            all_grid.append(rec)
            if task.resolved_program:
                grid_by_program[task.resolved_program].append(rec)
    for schedule in deps.orchestration.schedules:
        rec = grid_recommendation(
            "scheduler.control_m",
            grid_catalog,
            rules,
            evidence=Loc(file=schedule.file, line=schedule.line, end_line=schedule.line),
            target_program=schedule.file if schedule.file.lower().endswith(".sas") else None,
            details={"schedule": schedule.text},
        )
        all_grid.append(rec)
        if schedule.file.lower().endswith(".sas"):
            grid_by_program[schedule.file].append(rec)

    plans = []
    for prog in analysis.programs:
        ir = build_ir(prog, macro_files)
        orch = Orchestration(
            grid_tasks=tasks[prog.file],
            schedules=scheds[prog.file],
            upstream=sorted(up[prog.file]),
            downstream=sorted(down[prog.file]),
            grid_recommendations=grid_by_program[prog.file],
        )
        plans.append(plan_program(ir, project_id, rules, libs, pending[prog.file], orch))
    ps = PlanSet(
        project_id=project_id,
        rules_version=rules.version,
        plans=plans,
        grid_recommendations=all_grid,
    )
    store.plans_path(project_id).write_text(ps.model_dump_json(), encoding="utf-8")
    return ps


def _overlay(store: Store, ps: PlanSet) -> PlanSet:
    states = store.get_step_states(ps.project_id)
    for plan in ps.plans:
        for step in plan.steps + [s for c in plan.children for s in c.steps]:
            st = states.get((plan.program, step.id))
            if st:
                step.status, step.note = st[0], st[1]  # type: ignore[assignment]
    return ps


def load_plans(store: Store, project_id: str) -> PlanSet | None:
    p = store.plans_path(project_id)
    if not p.exists():
        return None
    return _overlay(store, PlanSet.model_validate(json.loads(p.read_text(encoding="utf-8"))))


def get_plan(store: Store, project_id: str, program: str) -> JobPlan | None:
    ps = load_plans(store, project_id)
    return next((p for p in ps.plans if p.program == program), None) if ps else None


def set_decision(
    store: Store, project_id: str, program: str, step_id: str, status: str, note: str | None
) -> bool:
    plan = get_plan(store, project_id, program)
    ids = (
        {s.id for s in plan.steps + [s for c in plan.children for s in c.steps]} if plan else set()
    )
    if step_id not in ids or status not in VALID_STATUS:
        return False
    store.set_step_state(project_id, program, step_id, status, note)
    return True
