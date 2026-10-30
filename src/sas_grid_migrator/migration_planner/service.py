"""Orquesta análisis → dependencias → IR → planes y conserva las decisiones humanas."""

import json
import re
from collections import defaultdict

from sas_grid_migrator.dependency_graph.builder import build_dependencies, load_dependencies
from sas_grid_migrator.environment.catalog import load_if_present
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.intermediate_representation.models import LibraryRef
from sas_grid_migrator.macro_resolver.resolver import macro_index
from sas_grid_migrator.migration_planner.job_naming import (
    DEFAULT_NAME_TEMPLATE,
    render_job_name,
)
from sas_grid_migrator.migration_planner.models import JobPlan, Orchestration, PlanSet
from sas_grid_migrator.migration_planner.offline_files import configure_offline_file_operations
from sas_grid_migrator.migration_planner.planner import (
    grid_recommendation,
    load_grid_catalog,
    load_mapping_rules,
    plan_program,
    unique_job_names,
)
from sas_grid_migrator.persistence.artifacts import write_text_atomic
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.analyze import analyze_project, load_analysis
from sas_grid_migrator.sas_parser.ast import Loc
from sas_grid_migrator.semantic_analysis.classify import load_rules
from sas_grid_migrator.talend_adapter.naming import cap_job_name

VALID_STATUS = {"propuesto", "pendiente", "verificado", "validado_manualmente", "descartado"}
NAME_TEMPLATE_KEY = "job_name_template"


def current_name_template(store: Store) -> str:
    return store.get_setting(NAME_TEMPLATE_KEY, DEFAULT_NAME_TEMPLATE) or DEFAULT_NAME_TEMPLATE


def exclude_uninstalled_components(
    plans: PlanSet, installed_components: set[str] | frozenset[str]
) -> None:
    """No propone componentes ni alternativas que no existan en el Studio activo."""
    installed = {name.casefold() for name in installed_components}

    def available(name: str) -> bool:
        return name.split(" ", 1)[0].casefold() in installed

    for recommendation in plans.grid_recommendations:
        name = recommendation.component_candidate
        if name and not available(name):
            recommendation.status = "unsupported"
            recommendation.component_candidate = None
            recommendation.doc_url = None
            recommendation.reason += f" El componente {name} no está instalado en este Studio."

    for plan in plans.plans:
        for step in plan.steps + [step for child in plan.children for step in child.steps]:
            step.alternatives = [name for name in step.alternatives if available(name)]
            step.variants = [name for name in step.variants if available(name)]
            name = step.component_candidate
            if name in {"", "por_determinar", "ninguno"} or available(name):
                continue
            step.component_candidate = "por_determinar"
            step.action = "manual_decision"
            step.in_catalog = False
            step.doc_url = None
            step.pending.append(f"El componente {name} no está instalado en este Studio; elegir una alternativa disponible.")
            step.status = "pendiente"
            plan.job_status = "needs_review"


def generate_plans(
    store: Store,
    project_id: str,
    fresh: bool = False,
    report_policy: str | None = None,
    installed_components: set[str] | frozenset[str] | None = None,
) -> PlanSet:
    """Genera los planes. La política de reportes sale de la configuración del proyecto (WP3)."""
    report_policy = report_policy or store.settings.report_policy
    table_action = store.settings.table_action
    """Genera los planes. Reutiliza el análisis persistido salvo `fresh` o reglas distintas."""
    analysis = None if fresh else load_analysis(store, project_id)
    if analysis is None or analysis.rules_version != load_rules().version:
        analysis, deps = analyze_project(store, project_id), None
    else:
        deps = load_dependencies(store, project_id)
    deps = deps or build_dependencies(store, project_id)
    rules = load_mapping_rules()
    grid_catalog = load_grid_catalog()
    environment = load_if_present(store.environment_path(project_id), set(rules.engines))
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
        configure_offline_file_operations(ir, store.source_dir(project_id))
        orch = Orchestration(
            grid_tasks=tasks[prog.file],
            schedules=scheds[prog.file],
            upstream=sorted(up[prog.file]),
            downstream=sorted(down[prog.file]),
            grid_recommendations=grid_by_program[prog.file],
        )
        plans.append(
            plan_program(
                ir,
                project_id,
                rules,
                libs,
                pending[prog.file],
                orch,
                report_policy,
                environment,
                table_action,
                source_text=_source_text(store, project_id, prog.file),
            )
        )
    project = store.get_project(project_id)
    project_name = project.name if project else project_id
    template = current_name_template(store)
    for plan in plans:
        plan.job_name = render_job_name(
            template, project=project_name, program=plan.program
        )
    unique_job_names(
        plans,
        lambda parts, depth: render_job_name(
            template, project=project_name, program="/".join(parts), depth=depth
        ),
    )
    for plan in plans:
        plan.job_name = cap_job_name(plan.job_name)
    ps = PlanSet(
        project_id=project_id,
        rules_version=rules.version,
        plans=plans,
        grid_recommendations=all_grid,
    )
    if installed_components is not None:
        exclude_uninstalled_components(ps, installed_components)
    write_text_atomic(store.plans_path(project_id), ps.model_dump_json())
    return ps


def _source_text(store: Store, project_id: str, file: str) -> str | None:
    """Texto SAS del programa (para etiquetas, %let por ambiente y credenciales). None si no existe."""
    try:
        return (store.source_dir(project_id) / file).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


GUIDE_STATUS = {"pendiente": "pending", "en_progreso": "in_progress", "completado": "completed", "bloqueado": "blocked"}
_LEGACY_GUIDE = re.compile(r"^\[Estado de guía: (pendiente|en_progreso|completado|bloqueado)\]", re.MULTILINE)


def legacy_guide_status(status: str, note: str | None) -> str:
    """Estado de guía de un paso sin estado estructurado: se lee del texto legado de `note`.

    Mismo criterio que la web (`decodeProgress`): `[Estado de guía: ...]` en la nota, y si no
    hay nota, el estado de decisión (verificado/validado -> completado, descartado -> bloqueado).
    """
    found = _LEGACY_GUIDE.search(note or "")
    if found:
        return GUIDE_STATUS[found.group(1)]
    if status in ("verificado", "validado_manualmente"):
        return "completed"
    if status == "descartado":
        return "blocked"
    return "pending"


def _overlay(store: Store, ps: PlanSet, *, with_edits: bool = True) -> PlanSet:
    states = store.get_step_states(ps.project_id)
    guides = store.get_guide_states(ps.project_id)
    for plan in ps.plans:
        steps = plan.steps + [step for child in plan.children for step in child.steps]
        for step in steps:
            state = states.get((plan.program, step.id))
            if state:
                step.status, step.note = state[0], state[1]  # type: ignore[assignment]
            step.guide_status = legacy_guide_status(step.status, step.note)  # type: ignore[assignment]
            guide = guides.get((plan.program, step.id))
            if guide:
                step.guide_status, step.field_done = guide[0], guide[1]  # type: ignore[assignment]
    if not with_edits:
        return ps

    overrides = store.get_job_overrides(ps.project_id)
    reserved = {plan.job_name.casefold() for plan in ps.plans}
    accepted: set[str] = set()
    for plan in sorted(ps.plans, key=lambda item: item.program):
        override = overrides.get(plan.program)
        if override is None:
            continue
        if override.job_name:
            candidate = override.job_name
            key = candidate.casefold()
            same_name = key == plan.job_name.casefold()
            if same_name or (key not in reserved and key not in accepted):
                plan.job_name = candidate
                plan.job_name_edited = not same_name
                accepted.add(key)
            else:
                plan.rename_ignored = candidate
        plan.description = override.description

    expression_overrides = store.get_expression_overrides(ps.project_id)
    for plan in ps.plans:
        for step in plan.steps + [step for child in plan.children for step in child.steps]:
            for index, expression in enumerate(step.expressions):
                override = expression_overrides.get((plan.program, step.id, index))
                if override is None or expression.sas != override[0]:
                    continue
                expression.talend = override[1]
                expression.talend_edited = True
    return ps


def load_plans(
    store: Store, project_id: str, *, with_edits: bool = True
) -> PlanSet | None:
    p = store.plans_path(project_id)
    if not p.exists():
        return None
    return _overlay(
        store,
        PlanSet.model_validate(json.loads(p.read_text(encoding="utf-8"))),
        with_edits=with_edits,
    )


def get_plan(
    store: Store, project_id: str, program: str, *, with_edits: bool = True
) -> JobPlan | None:
    ps = load_plans(store, project_id, with_edits=with_edits)
    return next((p for p in ps.plans if p.program == program), None) if ps else None


GUIDE_STATUS_VALUES = frozenset(GUIDE_STATUS.values())


def set_guide_state(
    store: Store,
    project_id: str,
    program: str,
    step_id: str,
    guide_status: str | None,
    field_done: dict[str, bool] | None,
) -> bool:
    """Guarda el estado estructurado de la guía de un paso. Campos no enviados se conservan."""
    plan = get_plan(store, project_id, program)
    ids = (
        {s.id for s in plan.steps + [s for c in plan.children for s in c.steps]} if plan else set()
    )
    if step_id not in ids:
        return False
    if guide_status is not None and guide_status not in GUIDE_STATUS_VALUES:
        return False
    current = store.get_guide_states(project_id).get((program, step_id))
    status = guide_status or (current[0] if current else None)
    if status is None:
        step = next(s for s in (plan.steps + [s for c in plan.children for s in c.steps]) if s.id == step_id)  # type: ignore[union-attr]
        status = legacy_guide_status(step.status, step.note)
    done = {**(current[1] if current else {}), **(field_done or {})}
    store.set_guide_state(project_id, program, step_id, status, done)
    return True


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
