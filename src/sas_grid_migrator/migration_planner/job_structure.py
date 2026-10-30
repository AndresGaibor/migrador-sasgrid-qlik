"""Estructura de los Jobs generados: partes por tamaño, Job padre con tRunJob, conexión
compartida por motor, manejo de errores y observabilidad.

Todo lo que se añade aquí son pasos recomendados (`recommended=True`, con `why`); no son
traducciones de SAS. El umbral sale de `limits.MAX_COMPONENTS_PER_JOB`. Los candidatos de
componente se comprueban contra el Studio instalado (`rules/talend/component-panels.json`):
si un componente no está, el candidato queda `por_determinar` y el `why` lo explica.
"""

import json
import re
from functools import lru_cache
from pathlib import Path

from sas_grid_migrator.migration_planner import context_rules
from sas_grid_migrator.migration_planner.limits import (
    DATABASE_ACCESS,
    DATABASE_CONNECTION,
    DATABASE_FAMILIES,
    INFRA_RESERVE,
    MAX_COMPONENTS_PER_JOB,
    MAX_RECOMMENDED_PER_JOB,
)
from sas_grid_migrator.migration_planner.models import (
    Connection,
    JobPart,
    JobPlan,
    OrchestratorJob,
    PlanStep,
    RunJobCall,
)
from sas_grid_migrator.sas_parser.ast import Loc

ROOT = Path(__file__).resolve().parents[3]
PANELS_PATH = ROOT / "rules" / "talend" / "component-panels.json"
MAPPINGS_PATH = ROOT / "rules" / "mappings" / "talend-components.json"

MAX_JOB_LENGTH = 60
OBSERVED_RESERVE = 2  # tStatCatcher + tLogRow
_ENGINE = re.compile(
    rf"^t({DATABASE_FAMILIES})(?:Input|Output|Row|SP|BulkExec|OutputBulk|OutputBulkExec)$"
)


@lru_cache(maxsize=4)
def _installed_names(panels: str, mappings: str, panels_mtime: float, mappings_mtime: float) -> frozenset[str]:
    """Snapshot del Studio (`component-panels.json`) como única fuente. Solo si no hay snapshot se
    usan los nombres citados en el mapeo, para no proponer nada inventado."""
    try:
        data = json.loads(Path(panels).read_text(encoding="utf-8"))
        return frozenset(data.get("components", {}))
    except (OSError, ValueError):
        pass
    try:
        return frozenset(re.findall(r'"(t\w+)"', Path(mappings).read_text(encoding="utf-8")))
    except OSError:
        return frozenset()


OFFICIAL_INVENTORY_PATH = ROOT / "rules" / "talend" / "official-component-inventory.json"


@lru_cache(maxsize=1)
def official_inventory_names() -> frozenset[str]:
    """Componentes documentados en el inventario oficial de Talend (no solo en el snapshot de paneles).

    El snapshot de paneles cubre un alcance (p. ej. no trae tOracleRow aunque el motor Oracle sí tenga su Row).
    Un componente Row de motor se acepta si el inventario oficial lo documenta; el resto sigue el snapshot."""
    try:
        data = json.loads(OFFICIAL_INVENTORY_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return frozenset()
    return frozenset(item["name"] for item in data.get("components", []) if isinstance(item, dict) and "name" in item)


def installed_components() -> frozenset[str]:
    """Componentes que existen en el Studio instalado (paneles y mapeos del repositorio)."""

    def stamp(path: Path) -> float:
        return path.stat().st_mtime if path.exists() else 0.0

    return _installed_names(
        str(PANELS_PATH), str(MAPPINGS_PATH), stamp(PANELS_PATH), stamp(MAPPINGS_PATH)
    )


def engine_of(component: str) -> str | None:
    """Motor de un acceso (`tImpalaInput` -> `Impala`); None para componentes sin motor concreto."""
    match = _ENGINE.match(component)
    # tDBInput/tDBRow son genéricos: no existen en el Studio instalado y no dicen el motor.
    return match.group(1) if match and match.group(1) != "DB" else None


def component_step_id(component: str, role: str, job: str) -> str:
    """Nombre `tComponente_Rol` del paso recomendado, único por Job."""
    return f"{component}_{role}__{job}"


def _candidate(component: str, installed: frozenset[str]) -> str:
    return component if component in installed else "por_determinar"


def _recommended(
    job: str,
    component: str,
    role: str,
    purpose: str,
    why: str,
    evidence: Loc,
    order: int,
    *,
    connections: list[Connection] | None = None,
) -> PlanStep:
    return PlanStep(
        id=component_step_id(component, role, job),
        order=order,
        subjob="recomendado",
        action="add_component",
        component_candidate=component,
        purpose=purpose,
        evidence=evidence,
        recommended=True,
        why=why,
        job_part=job,
        connections=connections or [],
    )


_ENGINE_TOKEN = re.compile(r"[A-Za-z]+")
_HINT_FAMILIES = tuple(family for family in DATABASE_FAMILIES.split("|") if family != "DB")


def engine_hint(plan: JobPlan) -> str | None:
    """Motor que el propio SAS nombra (libname, DSN o valor de ambiente), p. ej. IMPALA -> Impala."""
    texts = [library.engine or "" for library in plan.libraries_needed]
    for variable in plan.context_variables:
        texts.append(variable.sas_value or "")
        texts.extend(value or "" for value in (variable.group_values or {}).values())
    return engine_hint_from_texts(texts)


def engine_hint_from_texts(texts: list[str]) -> str | None:
    """Motor nombrado en algún texto (engine de libname, DSN, valor de ambiente)."""
    for text in texts:
        for token in _ENGINE_TOKEN.findall(text):
            for family in _HINT_FAMILIES:
                if token.upper().startswith(family.upper()):
                    return family
    return None


def _database_engine(steps: list[PlanStep], hint: str | None = None) -> str | None | bool:
    """False: sin accesos a base de datos. Motor del componente o, si no lo trae, la pista del SAS."""
    engines = [
        engine_of(step.component_candidate)
        for step in steps
        if DATABASE_ACCESS.match(step.component_candidate)
    ]
    if not engines:
        return False
    concrete = [engine for engine in engines if engine]
    return concrete[0] if concrete else hint


def _infra_steps(job: str, steps: list[PlanStep], *, engine: str | None | bool) -> list[PlanStep]:
    """Pasos recomendados de un Job: conexión y cierre compartidos si hay base de datos, y el error."""
    installed = installed_components()
    evidence = steps[0].evidence if steps else Loc(file="", line=1, end_line=1)
    last_order = max((step.order for step in steps), default=0)
    last_id = steps[-1].id if steps else None
    error_from = [Connection(type="OnComponentError", from_step=last_id)] if last_id else []
    infra: list[PlanStep] = []
    if engine is not False:
        if engine:
            connection = _candidate(f"t{engine}Connection", installed)
            close = _candidate(f"t{engine}Close", installed)
            engine_note = f"motor {engine}"
        else:
            connection, close = "por_determinar", "por_determinar"
            engine_note = "motor sin determinar en el SAS"
        close_why = (
            f"Cierra la sesión {engine_note} al terminar el flujo para no dejar conexiones abiertas."
            if close != "por_determinar"
            else f"Cerrar la sesión ({engine_note}): el Studio instalado no trae un componente de cierre "
            "para este motor; cierra la conexión con el mecanismo que indique el administrador."
        )
        infra += [
            _recommended(
                job, connection, "Compartida", f"Conexión única a la base de datos ({engine_note})",
                "Una sola conexión reutilizada por todos los accesos evita abrir y cerrar sesiones "
                "por cada tabla y permite confirmar o revertir en un solo punto.",
                evidence, -1,
            ),
            _recommended(
                job, close, "Cierre", "Cierra la conexión compartida", close_why,
                evidence, last_order + 1,
            ),
        ]
    infra.append(
        _recommended(
            job, "tDie", "Error", "Detiene el Job ante un error de componente",
            "Corta la ejecución cuando el dato queda incompleto, igual que el ABORT o el error de SAS; "
            "se conecta con OnComponentError.",
            evidence, last_order + 2, connections=error_from,
        )
    )
    return infra


def _observability_steps(job: str, steps: list[PlanStep]) -> list[PlanStep]:
    evidence = steps[0].evidence if steps else Loc(file="", line=1, end_line=1)
    return [
        _recommended(
            job, "tLogRow", "Conteos", "Muestra el conteo de registros procesados",
            "El SAS compara conteos en la macro; el conteo se verifica en la ejecución con tLogRow "
            "en vez de traducir la comparación 1:1.",
            evidence, 10_000,
        ),
    ]


def _rank(step: PlanStep) -> int:
    """Prioridad de un paso recomendado: error (0), conexión (1), cierre (2), conteo (3)."""
    role = step.id.split("__")[0]
    if "_Error" in role or step.component_candidate in ("tDie", "tLogCatcher"):
        return 0
    if "_Compartida" in role:
        return 1
    if "_Cierre" in role:
        return 2
    return 3


def _cap_recommended(plan: JobPlan) -> None:
    """Como máximo MAX_RECOMMENDED_PER_JOB pasos recomendados por Job; se quitan los de menor prioridad."""
    steps = plan.steps + [s for child in plan.children for s in child.steps]
    per_job: dict[str, list[PlanStep]] = {}
    for step in steps:
        if step.recommended and step.component_candidate != "tRunJob":
            per_job.setdefault(step.job_part or "", []).append(step)
    dropped: set[str] = set()
    for group in per_job.values():
        ranked = sorted(group, key=lambda s: (_rank(s), s.order))
        dropped |= {s.id for s in ranked[MAX_RECOMMENDED_PER_JOB:]}
    if not dropped:
        return
    plan.steps = [s for s in plan.steps if s.id not in dropped]
    for child in plan.children:
        child.steps = [s for s in child.steps if s.id not in dropped]
    for part in plan.job_parts:
        part.step_ids = [sid for sid in part.step_ids if sid not in dropped]
        part.component_count = len(part.step_ids)
    for step in plan.steps + [s for child in plan.children for s in child.steps]:
        step.connections = [c for c in step.connections if c.from_step not in dropped]


def _groups(steps: list[PlanStep]) -> list[list[PlanStep]]:
    """Subjobs lógicos: pasos consecutivos del mismo `subjob` (no se corta un bloque SAS)."""
    groups: list[list[PlanStep]] = []
    for step in steps:
        if groups and groups[-1][-1].subjob == step.subjob:
            groups[-1].append(step)
        else:
            groups.append([step])
    return groups


def _partition(steps: list[PlanStep], capacity: int) -> list[list[PlanStep]]:
    parts: list[list[PlanStep]] = []
    current: list[PlanStep] = []
    for group in _groups(steps):
        if current and len(current) + len(group) > capacity:
            parts.append(current)
            current = []
        current.extend(group)
    if current:
        parts.append(current)
    return parts


def _business_title(steps: list[PlanStep]) -> str:
    titles = list(dict.fromkeys(step.business_subjob for step in steps if step.business_subjob))
    if not titles:
        return steps[0].purpose if steps else "Parte del programa"
    shown = "; ".join(titles[:3])
    return shown + ("; ..." if len(titles) > 3 else "")


def _part_name(job: str, number: int) -> str:
    return f"{job[: MAX_JOB_LENGTH - 4]}_p{number:02d}"


def _run_job(parent: str, job: str, order: int, title: str, evidence: Loc) -> PlanStep:
    return PlanStep(
        id=component_step_id("tRunJob", f"Parte{order:02d}", parent),
        order=order,
        subjob="orquestador",
        action="add_component",
        component_candidate="tRunJob",
        purpose=f"Ejecuta el Job {job}: {title}",
        evidence=evidence,
        recommended=True,
        why="El programa supera el tamaño recomendado; el Job padre llama a cada parte en orden "
        "y transmite todo el contexto.",
        job_part=parent,
    )


def _organize(
    unit: str,
    steps: list[PlanStep],
    of: str,
    reserve: int = INFRA_RESERVE,
    hint: str | None = None,
) -> tuple[list[PlanStep], list[JobPart]]:
    """Reparte los pasos reales de un Job en partes si no caben y añade sus pasos recomendados.

    `reserve` deja hueco para los pasos recomendados que se añadan después. Devuelve los pasos
    del Job (todas las partes incluidas) y las partes (vacío si cabe entero).
    """
    capacity = MAX_COMPONENTS_PER_JOB - reserve
    if len(steps) <= capacity:
        for step in steps:
            step.job_part = unit
        return steps + _infra_steps(unit, steps, engine=_database_engine(steps, hint)), []
    out: list[PlanStep] = []
    parts: list[JobPart] = []
    for number, part in enumerate(_partition(steps, capacity), 1):
        name = _part_name(unit, number)
        for step in part:
            step.job_part = name
        infra = _infra_steps(name, part, engine=_database_engine(part, hint))
        out += part + infra
        parts.append(
            JobPart(
                name=name,
                title=_business_title(part),
                of=of,
                step_ids=[step.id for step in part + infra],
                component_count=len(part) + len(infra),
            )
        )
    return out, parts


def apply_structure(plan: JobPlan, source: str | None) -> None:
    """Asigna Job y subjob de negocio a cada paso; reparte los Jobs que superan el umbral y añade
    pasos recomendados (conexión, errores, observabilidad), partes y orquestador."""
    labels = context_rules.business_labels(source)
    for step in plan.steps + [s for child in plan.children for s in child.steps]:
        step.business_subjob = context_rules.label_for_line(labels, step.evidence.line)

    job = plan.job_name
    plan.job_parts = []
    hint = engine_hint(plan)
    main_steps, main_parts = _organize(job, plan.steps, of=job, hint=hint)
    if main_parts:
        evidence = plan.steps[0].evidence
        calls = [
            _run_job(job, part.name, index, part.title, evidence)
            for index, part in enumerate(main_parts, 1)
        ]
        parent = [*calls, *_infra_steps(job, [], engine=False)]
        for step in parent:
            step.job_part = job
        plan.steps = [*parent, *main_steps]
        plan.job_parts = main_parts
    else:
        plan.steps = main_steps

    for child in plan.children:
        # Un bloque que cuenta filas (agregado sin agrupar) se observa con tStatCatcher/tLogRow.
        observed = any(step.operation_type == "aggregate" for step in child.steps)
        child.steps, child_parts = _organize(
            child.name,
            list(child.steps),
            of=child.name,
            reserve=INFRA_RESERVE + (OBSERVED_RESERVE if observed else 0),
            hint=hint,
        )
        if observed and child.steps:
            # La observabilidad va en la primera parte del macro (conteos y tiempos del SAS).
            first = child_parts[0] if child_parts else None
            unit = first.name if first else child.name
            extra = _observability_steps(unit, child.steps)
            child.steps += extra
            if first:
                first.step_ids += [step.id for step in extra]
                first.component_count += len(extra)
        plan.job_parts += child_parts

    _cap_recommended(plan)
    _orchestrate(plan, job)


def _orchestrate(plan: JobPlan, job: str) -> None:
    """Orquestador con tRunJob hacia partes y macros. Solo si hay partes o varias macros."""
    main_parts = [part for part in plan.job_parts if part.of == job]
    # Un macro definido varias veces (bloques repetidos en el SAS) se llama una sola vez: su
    # primera definición; las demás no tienen Job propio.
    macros = list(dict.fromkeys(child.name for child in plan.children))
    if len(main_parts) <= 1 and len(macros) < 2:
        plan.orchestrator = None
        return
    if main_parts:
        name = job
        calls = [RunJobCall(job=part.name, order=i, title=part.title) for i, part in enumerate(main_parts, 1)]
    else:
        name = f"{job[: MAX_JOB_LENGTH - 4]}_orq"
        calls = [RunJobCall(job=job, order=1, title="programa principal")]
    for macro in macros:
        calls.append(RunJobCall(job=macro, order=len(calls) + 1, title=f"macro %{macro}"))
    plan.orchestrator = OrchestratorJob(name=name, run_jobs=calls)
