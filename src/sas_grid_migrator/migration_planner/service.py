"""Orquesta análisis → dependencias → IR → planes y conserva las decisiones humanas."""

import json
from collections import defaultdict

from sas_grid_migrator.dependency_graph.builder import build_dependencies, load_dependencies
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.intermediate_representation.models import LibraryRef
from sas_grid_migrator.macro_resolver.resolver import macro_index
from sas_grid_migrator.migration_planner.models import JobPlan, Orchestration, PlanSet
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import analyze_project, load_analysis
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
    plans = []
    for prog in analysis.programs:
        ir = build_ir(prog, macro_files)
        orch = Orchestration(
            grid_tasks=tasks[prog.file],
            schedules=scheds[prog.file],
            upstream=sorted(up[prog.file]),
            downstream=sorted(down[prog.file]),
        )
        plans.append(plan_program(ir, project_id, rules, libs, pending[prog.file], orch))
    ps = PlanSet(project_id=project_id, rules_version=rules.version, plans=plans)
    store.plans_path(project_id).write_text(ps.model_dump_json())
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
    return _overlay(store, PlanSet.model_validate(json.loads(p.read_text())))


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
