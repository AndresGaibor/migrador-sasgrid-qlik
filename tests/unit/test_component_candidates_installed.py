"""Cada component_candidate sale del snapshot del Studio instalado (`rules/talend/component-panels.json`)
o queda como decisión manual con su motivo. Los componentes genéricos tDB* no existen en ese Studio y
no deben aparecer como candidatos."""

import json
import os
import shutil
from pathlib import Path

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.job_structure import official_inventory_names
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.sas_parser.parser import parse_program
from tests.support.cache import cached_planset

ROOT = Path(__file__).parent.parent.parent
SNAPSHOT = frozenset(
    json.loads((ROOT / "rules" / "talend" / "component-panels.json").read_text(encoding="utf-8"))[
        "components"
    ]
)
GOLDEN_SOURCES = Path(__file__).parent.parent / "fixtures" / "sas"
GENERIC_TDB = {"tDBInput", "tDBOutput", "tDBRow"}
PLACEHOLDERS = {"por_determinar", "ninguno"}
# Componentes Row de motor (tOracleRow, tMysqlRow...): el snapshot de paneles solo cubre un alcance; el
# inventario oficial los documenta y el planificador los propone solo si lo hace (job_structure).
_ENGINE_MAPPINGS = json.loads((ROOT / "rules" / "mappings" / "talend-components.json").read_text(encoding="utf-8"))
OFFICIAL_ENGINE_ROWS = frozenset(
    engine["row"] for engine in _ENGINE_MAPPINGS["engines"].values() if engine.get("row")
) & frozenset(official_inventory_names())


def _steps(plans):
    for plan in plans:
        for step in plan.steps + [s for child in plan.children for s in child.steps]:
            yield plan.program, step


def _problems(plans) -> list[str]:
    problems = []
    for program, step in _steps(plans):
        candidate = step.component_candidate
        where = f"{program} {step.id}"
        if candidate in GENERIC_TDB:
            problems.append(f"{where}: genérico {candidate} fuera del Studio instalado")
        if step.action == "manual_decision":
            if candidate == "" and not step.why:
                problems.append(f"{where}: candidato vacío sin motivo (why)")
            continue
        if candidate == "":
            problems.append(f"{where}: candidato vacío sin manual_decision")
        elif candidate not in SNAPSHOT and candidate not in PLACEHOLDERS and candidate not in OFFICIAL_ENGINE_ROWS:
            problems.append(f"{where}: {candidate} no está en el snapshot")
    return problems


def _generate(root: Path, source_dir: Path, file_name: str | None = None):
    if file_name is None:
        # Carpeta entera: caché de disco por contenido (tests/support/cache.py).
        return cached_planset(source_dir).plans
    store = Store(Settings(data_dir=root / "data"))
    project = store.create_project("candidatos")
    if file_name is None:
        store.import_batch(project.id, source_dir)
    else:
        target = root / "src"
        target.mkdir()
        shutil.copy(source_dir, target / file_name)
        store.import_batch(project.id, target)
    return generate_plans(store, project.id).plans


def test_golden_and_matrix_candidates_come_from_the_installed_studio(tmp_path):
    plans = _generate(tmp_path, GOLDEN_SOURCES)
    assert plans, "no se generó ningún plan"
    assert _problems(plans) == []


@pytest.mark.skipif(not os.environ.get("COD1_PATH"), reason="COD1_PATH no definido")
def test_cod1_candidates_come_from_the_installed_studio(tmp_path):
    source = Path(os.environ["COD1_PATH"])
    if not source.exists():
        pytest.skip("COD1_PATH no existe")
    plans = _generate(tmp_path, source, "cod1_completo.sas")
    assert _problems(plans) == []


def _plan_source(text: str):
    program = parse_program(text, "candidato.sas")
    return plan_program(build_ir(program), "candidatos", load_mapping_rules(), {})


def _candidates(plan):
    return [(s.component_candidate, s.action) for s in plan.steps + [x for c in plan.children for x in c.steps]]


def test_odbc_library_has_no_candidate_and_asks_for_a_manual_choice():
    plan = _plan_source(
        "libname src odbc dsn=DEMO;\ndata work.a; set src.tabla; run;\n"
    )
    read = next(s for s in plan.steps if s.operation_type == "read" and (s.library or "").lower() == "src")
    assert read.component_candidate == ""
    assert read.action == "manual_decision"
    assert read.why and "ODBC" in read.why
    assert "tDBInput" not in json.dumps(plan.model_dump(mode="json"))


def test_impala_library_uses_impala_input_and_output():
    plan = _plan_source(
        "libname imp impala server=x;\n"
        "data work.a; set imp.t; run;\n"
        "data imp.u; set work.a; run;\n"
    )
    candidates = [c for c, _ in _candidates(plan)]
    assert "tImpalaInput" in candidates
    assert "tImpalaOutput" in candidates


def test_execute_by_impala_is_a_row_component_and_keeps_the_sql():
    plan = _plan_source(
        "proc sql;\nconnect to impala (server=x);\n"
        "execute (create table s.r as select a from s.e group by a) by impala;\nquit;\n"
    )
    row = next(s for s in plan.steps if s.component_candidate == "tImpalaRow")
    assert row.operation_type == "sql_passthrough"
    assert any(p.name == "QUERY" and "group by a" in (p.value or "") for p in row.properties)


def test_execute_by_unknown_engine_is_manual_without_a_generic_component():
    # Aster no tiene componente Row documentado (oracle sí: tOracleRow, ver job_structure.official_inventory_names).
    plan = _plan_source("proc sql;\nexecute (delete from s.e) by aster;\nquit;\n")
    step = next(s for s in plan.steps if s.operation_type == "sql_passthrough")
    assert step.component_candidate == ""
    assert step.action == "manual_decision"
    assert step.why


def test_maintenance_on_unknown_library_does_not_fall_back_to_tdbrow():
    plan = _plan_source("proc datasets library=work nolist; delete scratch; quit;\n")
    candidates = {c for c, _ in _candidates(plan)}
    assert not (candidates & GENERIC_TDB)
