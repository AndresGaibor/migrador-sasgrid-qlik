"""Corpus de generalización: el planificador debe tratar cualquier script SAS igual.

Cada fixture de tests/fixtures/sas/generalization/ es un programa nuevo, con nombres distintos a
los de Cod1/Cod2. Las aserciones son ESTRUCTURALES (conteos, componentes, categorías de
not_migrated, grupos de contexto); nunca dependen de nombres de macros, tablas o variables.

Estos tests son la especificación. Algunos fallan hoy a propósito: describen comportamiento que
todavía no existe (p. ej. ELT a tOracleRow, troceo de macros a joblet). No se usan skip ni xfail.
Cada test indica en su docstring qué espera del código.

Convención de pasos: los conteos excluyen el paso `tDie` de seguridad que el planificador añade a
todo Job, y cuentan una sola vez los pasos de un joblet (sus apariciones repiten los mismos pasos).
"""

from __future__ import annotations

import json
import shutil
from functools import cache
from pathlib import Path

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.models import JobPlan, PlanStep
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from tests.support.cache import cached_planset

REPO = Path(__file__).resolve().parents[2]
FIXTURES = REPO / "tests" / "fixtures" / "sas" / "generalization"
PANELS = REPO / "rules" / "talend" / "component-panels.json"

FIXTURE_NAMES = [
    "oracle_elt.sas",
    "teradata_carga_por_lotes.sas",
    "etl_archivos_simple.sas",
    "cambio_de_ambiente.sas",
    "macros_reporte.sas",
    "fontaneria_y_log.sas",
    "sql_multiples_joins.sas",
]

# Candidatos que no son componentes Talend: el planificador no ha decidido nada todavía.
NON_COMPONENT_CANDIDATES = {"por_determinar", "manual_decision"}


# ---------------------------------------------------------------- utilidades


def _generate(name: str, root: Path) -> JobPlan:
    """Genera el plan de un único fixture en `root` (un programa por directorio, como en Cod1)."""
    src = root / "src"
    src.mkdir(parents=True)
    shutil.copy(FIXTURES / name, src / name)
    store = Store(Settings(data_dir=root / "data"))
    project = store.create_project("generalizacion")
    store.import_batch(project.id, src)
    plans = generate_plans(store, project.id).plans
    assert len(plans) == 1, [p.program for p in plans]
    return plans[0]


@cache
def _plan(name: str) -> JobPlan:
    """Plan por fixture: caché de disco por contenido (tests/support/cache.py). Solo el test de determinismo
    vuelve a generarlo de verdad, a propósito."""
    return cached_planset(FIXTURES / name).plans[0]


def _all_steps(plan: JobPlan) -> list[PlanStep]:
    return plan.steps + [s for child in plan.children for s in child.steps]


def _counted_once(plan: JobPlan) -> list[PlanStep]:
    """Pasos del plan sin el tDie de seguridad y con cada joblet contado una sola vez."""
    seen: set[str] = set()
    out: list[PlanStep] = []
    for step in _all_steps(plan):
        if step.component_candidate == "tDie":
            continue
        if step.joblet_id:
            if step.joblet_id in seen:
                continue
            seen.add(step.joblet_id)
        out.append(step)
    return out


def _candidates(plan: JobPlan) -> list[str]:
    """Componentes del plan: los de cada paso y los de cada joblet."""
    names = [s.component_candidate for s in _all_steps(plan)]
    for joblet in plan.joblets:
        names.extend(joblet.components)
    return [n for n in names if n]


def _count(plan: JobPlan, component: str) -> int:
    return sum(1 for n in _candidates(plan) if n == component)


def _work_writes(plan: JobPlan) -> list[str]:
    """Pasos que escriben un dataset WORK (`Escribir WORK.*`)."""
    return [
        s.purpose
        for s in _all_steps(plan)
        if s.operation_type == "write" and "work." in s.purpose.lower()
    ]


def _hash_components(plan: JobPlan) -> list[str]:
    return [n for n in _candidates(plan) if n.startswith("tHash")]


def _panel_components() -> set[str]:
    """Snapshot del Studio más los componentes Row de motor que documenta el inventario oficial.

    El snapshot de paneles no trae tOracleRow, tMysqlRow...; el planificador los acepta si el inventario
    oficial los documenta (job_structure.official_inventory_names). Mismo criterio en ambos tests.
    """
    from sas_grid_migrator.migration_planner.job_structure import official_inventory_names

    return set(json.loads(PANELS.read_text(encoding="utf-8"))["components"]) | set(official_inventory_names())


def _dump(plan: JobPlan) -> str:
    """Representación estable del plan para comparar dos ejecuciones (sin el id de proyecto)."""
    return plan.model_dump_json(exclude={"project_id"})


# ------------------------------------------------- 1. ELT de BD a BD en Oracle


def test_oracle_elt_pass_through_becomes_row_components():
    """ELT: las sentencias `execute ... by oracle` y los `create table` entre tablas de la misma
    libname deben salir como componentes Row del motor (tOracleRow), una por sentencia, con el SQL.
    Hoy el planificador las trata como lectura + tMap + escritura, o como 'sin traducción'.
    """
    plan = _plan("oracle_elt.sas")
    assert _count(plan, "tOracleRow") >= 3, _candidates(plan)


def test_oracle_elt_has_no_intermediate_reads_or_writes():
    """ELT: no debe haber lectura del motor seguida de escritura de vuelta en la misma base.
    Como mucho una lectura de entrada y una escritura (la sentencia final, si la hay).
    """
    plan = _plan("oracle_elt.sas")
    assert _count(plan, "tOracleInput") <= 1, _candidates(plan)
    assert _count(plan, "tOracleOutput") <= 1, _candidates(plan)
    assert not _work_writes(plan)


def test_oracle_elt_sql_is_not_marked_unsupported():
    """Las sentencias pass-through son traducibles; no deben quedar como 'Lógica sin traducción'."""
    plan = _plan("oracle_elt.sas")
    unsupported = [s for s in _all_steps(plan) if s.operation_type == "unsupported"]
    assert len(unsupported) <= 1, [s.purpose for s in unsupported]


# -------------------- 2. Carga por lotes a Teradata con macro llamada tres veces


def test_teradata_batch_macro_is_one_joblet_with_three_occurrences():
    """La macro de carga se invoca tres veces con tablas distintas: UN joblet con 3 ocurrencias
    (o equivalente), no hijos. Cada ocurrencia lleva sus propios valores de parámetro.
    """
    plan = _plan("teradata_carga_por_lotes.sas")
    assert not plan.children, [c.name for c in plan.children]
    assert len(plan.joblets) == 1, [(j.name, len(j.occurrences)) for j in plan.joblets]
    occurrences = plan.joblets[0].occurrences
    assert len(occurrences) == 3
    distinct_values = {tuple(sorted(o.values.items())) for o in occurrences}
    assert len(distinct_values) == 3, [o.values for o in occurrences]


def test_teradata_batch_uses_teradata_output_component():
    """La salida de cada carga es un componente de escritura de Teradata."""
    plan = _plan("teradata_carga_por_lotes.sas")
    assert "tTeradataOutput" in _candidates(plan), _candidates(plan)


def test_teradata_batch_plumbing_is_not_migrated():
    """Troceo, shell, espera, timers y mensajes van a not_migrated, no a pasos."""
    plan = _plan("teradata_carga_por_lotes.sas")
    categories = {e.category for e in plan.not_migrated}
    assert {"troceado_lotes", "espera", "medicion", "mensajes"} <= categories, categories
    assert categories & {"shell_auxiliar", "carga_comando"}, categories


def test_teradata_batch_step_count_is_small():
    """Solo queda la carga: pocos pasos contando el joblet una sola vez."""
    plan = _plan("teradata_carga_por_lotes.sas")
    assert len(_counted_once(plan)) <= 6, [s.purpose for s in _counted_once(plan)]


# -------------------- 3. ETL de archivos con WORK (CSV, DATA step, sort, merge, export)


def test_file_etl_has_no_work_datasets():
    """Sin datasets WORK intermedios: ninguna escritura a WORK en el plan."""
    plan = _plan("etl_archivos_simple.sas")
    assert not _work_writes(plan), _work_writes(plan)
    assert not _hash_components(plan)


def test_file_etl_is_at_most_eight_steps():
    plan = _plan("etl_archivos_simple.sas")
    assert len(_counted_once(plan)) <= 8, [s.purpose for s in _counted_once(plan)]


def test_file_etl_filter_and_expressions_fused_in_one_tmap():
    """Filtro, columnas calculadas y renombrado van en un solo tMap (fusión), no en tres pasos."""
    plan = _plan("etl_archivos_simple.sas")
    fused = [s for s in _all_steps(plan) if s.component_candidate == "tMap" and len(s.fused_from) >= 2]
    assert fused, [(s.component_candidate, s.fused_from) for s in _all_steps(plan)]


def test_file_etl_dedupe_and_sort_components():
    """El nodupkey va con tUniqRow o tSortRow; el orden previo al cruce, con tSortRow."""
    plan = _plan("etl_archivos_simple.sas")
    assert {"tUniqRow", "tSortRow"} & set(_candidates(plan)), _candidates(plan)


def test_file_etl_writes_csv_and_has_no_children():
    plan = _plan("etl_archivos_simple.sas")
    assert not plan.children
    assert "tFileOutputDelimited" in _candidates(plan), _candidates(plan)


# -------------------- 4. Cambio de ambiente: valores de contexto por grupo


def test_environment_switch_becomes_context_group_values():
    """Las variables que cambian según el ambiente salen como contexto con valores por grupo.
    No se identifica la variable por su nombre: se buscan variables con group_values.
    """
    plan = _plan("cambio_de_ambiente.sas")
    grouped = [v for v in plan.context_variables if v.group_values]
    assert len(grouped) >= 2, [(v.name, v.group_values) for v in plan.context_variables]


def test_environment_group_values_cover_all_environments():
    """Entre los valores por grupo aparecen los tres ambientes distintos del programa."""
    plan = _plan("cambio_de_ambiente.sas")
    values = {
        v
        for ctx in plan.context_variables
        if ctx.group_values
        for v in ctx.group_values.values()
        if v is not None
    }
    assert len(values) >= 3, values


def test_environment_script_has_no_children():
    plan = _plan("cambio_de_ambiente.sas")
    assert not plan.children


# -------------------- 5. Macros de reporte: una llamada (inline) y una con tres usos


def test_macro_called_once_is_inline_and_repeated_macro_is_joblet():
    """Macro usada una vez: se expande en línea (sin hijo). Macro usada tres veces: joblet con
    tres ocurrencias. Ninguna de las dos genera Jobs hijos.
    """
    plan = _plan("macros_reporte.sas")
    assert not plan.children, [c.name for c in plan.children]
    assert len(plan.joblets) == 1, [(j.name, len(j.occurrences)) for j in plan.joblets]
    assert len(plan.joblets[0].occurrences) == 3


def test_report_procs_map_to_aggregate_and_sort():
    """proc means se traduce a tAggregateRow y proc sort a tSortRow."""
    plan = _plan("macros_reporte.sas")
    candidates = set(_candidates(plan))
    assert "tAggregateRow" in candidates, candidates
    assert "tSortRow" in candidates, candidates


def test_report_script_stays_small():
    plan = _plan("macros_reporte.sas")
    assert len(_counted_once(plan)) <= 8, [s.purpose for s in _counted_once(plan)]


# -------------------- 6. Fontanería: solo quedan las transformaciones


def test_plumbing_script_keeps_only_transformations():
    """Dos transformaciones: el plan no supera 5 pasos (sin contar el tDie de seguridad)."""
    plan = _plan("fontaneria_y_log.sas")
    assert len(_counted_once(plan)) <= 5, [s.purpose for s in _counted_once(plan)]


def test_plumbing_script_moves_control_code_to_not_migrated():
    """Shell, espera (sleep), timers, mensajes, borrado de WORK y contadores: not_migrated."""
    plan = _plan("fontaneria_y_log.sas")
    categories = {e.category for e in plan.not_migrated}
    required = {"shell_auxiliar", "espera", "medicion", "mensajes", "limpieza_datasets", "conteo"}
    assert required <= categories, sorted(categories)


def test_plumbing_script_has_no_children():
    plan = _plan("fontaneria_y_log.sas")
    assert not plan.children


# -------------------- 7. SQL con varios joins, agregación y consumo desde WORK


def test_sql_join_becomes_tmap_and_aggregation_becomes_taggregaterow():
    """El join entre tablas es un tMap (con lookups o combinado); la agregación, tAggregateRow."""
    plan = _plan("sql_multiples_joins.sas")
    candidates = set(_candidates(plan))
    assert "tMap" in candidates, candidates
    assert "tAggregateRow" in candidates, candidates


def test_sql_script_has_no_work_writes():
    """El resultado intermedio consumido desde WORK no se escribe como paso 'Escribir WORK.*'."""
    plan = _plan("sql_multiples_joins.sas")
    assert not _work_writes(plan), _work_writes(plan)
    assert not _hash_components(plan)


# -------------------- Comprobaciones genéricas sobre los siete fixtures


@pytest.mark.parametrize("name", FIXTURE_NAMES)
def test_every_component_candidate_is_a_known_panel(name):
    """Todo component_candidate es un componente de component-panels.json o un marcador
    (por_determinar / manual_decision). Los pasos manual_decision no tienen componente.
    """
    plan = _plan(name)
    known = _panel_components() | NON_COMPONENT_CANDIDATES
    unknown = sorted(
        {
            s.component_candidate
            for s in _all_steps(plan)
            if s.action != "manual_decision" and s.component_candidate not in known
        }
    )
    assert not unknown, unknown


@pytest.mark.parametrize("name", FIXTURE_NAMES)
def test_every_not_migrated_entry_explains_itself(name):
    """Cada fontanería no migrada lleva motivo y equivalente Talend, no solo una categoría."""
    plan = _plan(name)
    for entry in plan.not_migrated:
        assert entry.reason.strip(), entry.category
        assert entry.talend_equivalent.strip(), entry.category


@pytest.mark.parametrize("name", FIXTURE_NAMES)
def test_plan_is_deterministic(name, tmp_path):
    """Dos ejecuciones sobre el mismo programa producen el mismo plan."""
    first = _dump(_plan(name))
    second = _dump(_generate(name, tmp_path))
    assert first == second
