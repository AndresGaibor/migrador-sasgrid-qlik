"""Etapa de fusión a corriente: WORK en línea, tReplicate, tMap fusionado, agregados que no se funden,
macro de una llamada en línea, macro repetida como joblet, fontanería en not_migrated y Cod1 opcional."""

import os
from pathlib import Path

import pytest

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.sas_parser.parser import parse_program

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sas"


def _plan(text: str, name: str = "prueba.sas", **kwargs):
    program = parse_program(text, name)
    return plan_program(build_ir(program), "fusion", load_mapping_rules(), {}, source_text=text, **kwargs)


def _steps(plan):
    return plan.steps + [s for child in plan.children for s in child.steps]


def _components(plan):
    return [s.component_candidate for s in plan.steps if not s.recommended]


def test_work_dataset_is_inlined_without_hash_components():
    plan = _plan(
        """
data work.a;
  set dwh.clientes;
  where saldo > 0;
run;
data stg.salida;
  set work.a;
  keep id saldo;
run;
"""
    )
    steps = _steps(plan)
    assert not [s for s in steps if s.component_candidate.startswith("tHash")]
    assert not [s for s in steps if "work." in (s.purpose or "").lower() and s.operation_type == "write"]
    # una lectura (dwh), el tMap o filtro, y una escritura (stg); ningún paso de work
    assert [s.operation_type for s in plan.steps if not s.recommended].count("write") == 1
    assert [s.operation_type for s in plan.steps if not s.recommended].count("read") == 1


def test_dataset_read_twice_gets_one_replicate():
    plan = _plan(
        """
data work.base;
  set dwh.clientes;
  saldo2 = saldo * 2;
run;
proc sql;
  create table stg.uno as select * from work.base where saldo2 > 1;
quit;
proc sql;
  create table stg.dos as select * from work.base where saldo2 < 1;
quit;
"""
    )
    # El reparto es un tMap con dos salidas FLOW (el MCP rechaza las conexiones de tReplicate).
    replicates = [s for s in plan.steps if s.operation_type == "replicate"]
    assert len(replicates) == 1 and replicates[0].component_candidate == "tMap"
    assert not [s for s in plan.steps if s.component_candidate == "tReplicate"]
    assert len([s for s in plan.steps if s.operation_type == "write"]) == 2
    # Cada salida tiene su propio filtro; ninguno se funde con el de la otra salida.
    filters = sorted(p.value for s in plan.steps for p in s.properties if p.name == "Output filter")
    assert filters == ["((input_row.saldo2 < 1))", "((input_row.saldo2 > 1))"]



def test_filter_compute_rename_keep_fuse_into_one_tmap():
    plan = _plan(
        """
data stg.final(keep=cliente_id nombre segmento);
  set dwh.clientes(rename=(id=cliente_id));
  where estado = 'A' and saldo > 0;
  if saldo >= 100000 then segmento = 'ALTO';
  else segmento = 'BAJO';
  drop estado;
run;
"""
    )
    tmaps = [s for s in plan.steps if s.component_candidate == "tMap"]
    assert len(tmaps) == 1
    fused = tmaps[0]
    assert fused.fused_from and len(fused.fused_from) >= 4
    assert fused.why and "tMap" in fused.why
    assert any(p.name == "Output filter" for p in fused.properties)
    assert [c.name for c in fused.schema_columns] == ["cliente_id", "nombre", "segmento"]
    assert all(e.line for e in fused.expressions)
    assert not [s for s in plan.steps if s.component_candidate in {"tFilterRow", "tFilterColumns"}]


def test_aggregate_and_sort_are_not_fused_into_the_tmap():
    plan = _plan(
        """
data stg.x;
  set dwh.clientes;
  where saldo > 0;
run;
proc sort data=stg.x out=stg.y;
  by saldo;
run;
proc sql;
  create table stg.z as select count(*) as n from stg.y;
quit;
"""
    )
    by_type = {s.operation_type: s for s in plan.steps if not s.recommended}
    assert "sort" in by_type and by_type["sort"].component_candidate == "tSortRow"
    assert "aggregate" in by_type and by_type["aggregate"].component_candidate == "tAggregateRow"
    assert not any(s.fused_from and "sort" in (s.operation_type or "") for s in plan.steps)


def test_macro_called_once_is_inlined_into_the_job():
    plan = _plan(
        """
%macro carga;
  data stg.m;
    set dwh.clientes;
    where saldo > 0;
  run;
%mend carga;
%carga;
"""
    )
    assert plan.children == []
    assert any(s.id.startswith("m:carga:") for s in plan.steps)


def test_macro_called_from_two_places_is_not_inlined():
    plan = _plan(
        """
%macro carga(t);
  data stg.&t;
    set dwh.clientes;
    where saldo > 0;
  run;
%mend carga;
%carga(a);
%carga(b);
"""
    )
    # varias llamadas: no se expande en línea; sus pasos son miembros de un joblet, no pasos sueltos
    assert all(s.joblet_id for s in plan.steps if s.id.startswith("m:carga:"))


def test_shell_sleep_and_timers_go_to_not_migrated():
    plan = _plan(
        """
data stg.k;
  set dwh.clientes;
  where saldo > 0;
run;
x "until [ $n -eq 0 ]; do sleep 5; done";
%put tiempo total;
"""
    )
    categories = {entry.category for entry in plan.not_migrated}
    # %put no llega al IR (el parser no lo emite como operación): queda sin registrar. Limitación documentada.
    assert "espera" in categories or "shell_auxiliar" in categories
    assert all(entry.talend_equivalent and entry.reason for entry in plan.not_migrated)
    assert not any(s.operation_type == "os_command" for s in _steps(plan))


def test_recommended_steps_are_at_most_three_per_job():
    plan = _plan(
        """
data stg.k;
  set dwh.clientes;
  where saldo > 0;
run;
"""
    )
    recommended = [s for s in _steps(plan) if s.recommended and s.component_candidate != "tRunJob"]
    assert len(recommended) <= 3
    assert not {s.component_candidate for s in recommended} & {"tPrejob", "tPostjob", "tWarn"}


def test_p0_fixture_is_at_most_four_pipeline_steps():
    text = (FIXTURES / "p0_clientes_activos.sas").read_text(encoding="utf-8")
    plan = _plan(text, "p0_clientes_activos.sas")
    core = [s for s in plan.steps if not s.recommended]
    assert len(core) <= 4, [(s.operation_type, s.component_candidate) for s in core]
    assert not [s for s in plan.steps if s.component_candidate.startswith("tHash")]


@pytest.mark.skipif(not os.environ.get("COD1_PATH"), reason="COD1_PATH no definido")
def test_cod1_has_no_hash_components_and_records_plumbing():
    source = Path(os.environ["COD1_PATH"])
    if not source.exists():
        pytest.skip("COD1_PATH no existe")
    text = source.read_text(encoding="utf-8", errors="replace")
    plan = _plan(text, "cod1_completo.sas")
    assert not [s for s in _steps(plan) if s.component_candidate.startswith("tHash")]
    assert plan.not_migrated, "la fontanería de Cod1 debe quedar registrada"
    assert {entry.category for entry in plan.not_migrated} & {"shell_auxiliar", "espera", "control_errores", "troceado_lotes"}
