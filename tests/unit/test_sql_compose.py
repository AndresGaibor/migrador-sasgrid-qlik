"""Composición SQL (migration_planner/sql_compose.py): cadenas de create table en una sola consulta.

Casos sintéticos con nombres inventados. Cubren: cadena de tres sentencias = una consulta con dos CTE y un paso;
intermedio con dos lectores = no se compone; funciones y construcciones solo SAS = no se compone; macro variables
= no se compone; un componente Row por motor cuando todo es del mismo motor; determinismo.
"""

from __future__ import annotations

import pytest

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.migration_planner.sql_compose import (
    compose_items,
    compose_statements,
    mask,
    rewrite_refs,
    split_with,
    sql_functions,
    translate_functions,
    unknown_functions,
)
from sas_grid_migrator.sas_parser.parser import parse_program


def _items(text: str):
    ir = build_ir(parse_program(text, "compone.sas"))
    return [(op, "") for op in ir.operations if op.type != "include"]


def _compose(text: str, libs=None):
    rules = load_mapping_rules()
    return compose_items(_items(text), set(), libs or {}, rules.engines)


def _sql_writes(items):
    return [op for op, _ in items if op.type == "write" and op.details.get("sql")]


def _plan(text: str):
    program = parse_program(text, "compone.sas")
    return plan_program(build_ir(program), "compone", load_mapping_rules(), {}, source_text=text)


def _steps(plan):
    return plan.steps + [s for child in plan.children for s in child.steps]


WORK_CHAIN = """
proc sql;
create table work.paso_uno as select id, saldo from work.base where saldo > 0;
create table work.paso_dos as select id, saldo * 2 as doble from work.paso_uno;
create table stg.final as select id, doble from work.paso_dos where doble > 10;
quit;
"""


def test_chain_of_three_creates_is_one_statement_with_two_ctes():
    items, notes = _compose(WORK_CHAIN)
    writes = _sql_writes(items)
    assert [w.outputs for w in writes] == [["stg.final"]], [w.outputs for w in writes]
    sql = writes[0].details["sql"]
    assert sql.lower().startswith("create table stg.final as with "), sql
    assert sql.lower().count(" as (") == 2, sql
    assert len(writes[0].details["composed_from"]) == 2
    assert any(n.startswith("Compuesta work.paso_uno") for n in notes)
    assert any(n.startswith("Compuesta work.paso_dos") for n in notes)


def test_chain_of_three_creates_is_one_plan_write():
    plan = _plan(
        "libname x oracle user=u path='p' schema=s;\n" + WORK_CHAIN.replace("stg.final", "x.final")
    )
    assert sum(1 for s in _steps(plan) if s.operation_type == "write") <= 1


def test_intermediate_with_two_readers_in_different_statements_is_not_composed():
    text = """
proc sql;
create table work.compartida as select id, saldo from work.base where saldo > 0;
create table stg.uno as select id from work.compartida;
create table stg.dos as select saldo from work.compartida;
quit;
"""
    items, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")], notes
    assert {w.outputs[0] for w in _sql_writes(items)} == {"work.compartida", "stg.uno", "stg.dos"}


def test_intermediate_read_twice_in_one_statement_is_a_shared_cte():
    """Dos lecturas de la misma intermedia en UNA consulta: un solo CTE compartido (motor, para que el ELT lo use)."""
    text = """
libname ext oracle user=etl path='SRV' schema=esq;
proc sql;
create table ext.base2 as select b.id, b.saldo from ext.base b where b.saldo > 0;
create table ext.par as select a.id, a.saldo from ext.base2 a where a.saldo > 5 union all select c.id, c.saldo from ext.base2 c where c.saldo < 0;
quit;
"""
    plan = _plan(text)
    rows = [s for s in _steps(plan) if s.component_candidate == "tOracleRow"]
    assert len(rows) == 1, [s.component_candidate for s in _steps(plan)]
    query = next(p.value for p in rows[0].properties if p.name == "QUERY")
    assert query.lower().count("base2_cte") >= 3 and query.lower().count(" as (") == 1, query


def test_union_on_work_tables_is_not_composed():
    """UNION sobre WORK: el intermedio no se cablea en el tMap; la sentencia queda como estaba."""
    text = """
proc sql;
create table work.base2 as select id, saldo from work.base where saldo > 0;
create table stg.par as select a.id from work.base2 a union all select c.id from work.base2 c;
quit;
"""
    _, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")], notes


def test_sas_only_function_in_producer_blocks_composition():
    text = """
proc sql;
create table work.con_sas as select id, cats(nombre, apellido) as completo from work.base;
create table stg.uso as select id, completo from work.con_sas;
quit;
"""
    items, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")]
    assert {w.outputs[0] for w in _sql_writes(items)} == {"work.con_sas", "stg.uso"}
    assert any("cats" in n for n in notes), notes


def test_calculated_keyword_blocks_composition():
    text = """
proc sql;
create table work.calc as select id, saldo * 2 as doble, calculated doble + 1 as triple from work.base;
create table stg.uso as select id, triple from work.calc;
quit;
"""
    _, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")], notes


def test_into_macro_variable_blocks_composition():
    """`into :x` dentro de la sentencia que se quiere componer: no se compone (compose_statements lo rechaza)."""
    producer = "create table work.copia as select id, saldo into :total from work.base"
    consumer = "create table stg.uso as select id from work.copia"
    sql, reason = compose_statements(producer, consumer, "work.copia", expected_refs=1)
    assert sql is None and "INTO" in reason, reason


def test_select_into_statement_does_not_block_a_neighbouring_chain():
    """Un SELECT INTO suelto no forma parte de ninguna cadena: la cadena vecina sí se compone."""
    text = """
proc sql noprint;
select count(*) into :total from work.base;
create table work.copia as select id from work.base;
create table stg.uso as select id from work.copia;
quit;
"""
    items, notes = _compose(text)
    assert [n for n in notes if n.startswith("Compuesta")], notes
    assert any(op.type == "set_variable" for op, _ in items)


def test_macro_variable_blocks_composition():
    text = """
proc sql;
create table work.filtrada as select id, saldo from work.base where saldo > &umbral;
create table stg.uso as select id from work.filtrada;
quit;
"""
    _, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")], notes


def test_order_by_in_producer_blocks_composition():
    text = """
proc sql;
create table work.ordenada as select id, saldo from work.base order by saldo;
create table stg.uso as select id from work.ordenada;
quit;
"""
    _, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")], notes


ENGINE_CHAIN = """
libname ext {engine} user=etl path='SRV' schema=esq;
proc sql;
create table ext.uno as select b.clave, b.total from ext.origen b where b.total > 0;
create table ext.dos as select u.clave, u.total * 2 as doble from ext.uno u;
create table ext.tres as select d.clave, d.doble from ext.dos d where d.doble > 10;
quit;
"""

ROW_BY_ENGINE = {
    "oracle": "tOracleRow",
    "teradata": "tTeradataRow",
    "impala": "tImpalaRow",
    "postgres": "tPostgresqlRow",
}


@pytest.mark.parametrize("engine", sorted(ROW_BY_ENGINE))
def test_engine_chain_is_one_row_component_with_the_composed_query(engine):
    plan = _plan(ENGINE_CHAIN.format(engine=engine))
    rows = [s for s in _steps(plan) if s.component_candidate == ROW_BY_ENGINE[engine]]
    assert len(rows) == 1, [s.component_candidate for s in _steps(plan)]
    query = next(p.value for p in rows[0].properties if p.name == "QUERY")
    assert query.lower().count(" as (") == 2, query
    assert "esq.origen" in query and "ext." not in query, query


def test_engine_join_consumer_with_engine_producer_is_composed():
    text = """
libname ext oracle user=etl path='SRV' schema=esq;
proc sql;
create table ext.filtro as select b.clave, b.total from ext.origen b where b.total > 0;
create table ext.resumen as select f.clave, c.nombre from ext.filtro f join ext.clientes c on f.clave = c.clave;
quit;
"""
    plan = _plan(text)
    rows = [s for s in _steps(plan) if s.component_candidate == "tOracleRow"]
    assert len(rows) == 1, [s.component_candidate for s in _steps(plan)]
    query = next(p.value for p in rows[0].properties if p.name == "QUERY")
    assert "esq.clientes" in query and "filtro_cte" in query, query


def test_join_consumer_on_work_tables_is_not_composed():
    """Una consumidora con JOIN solo se compone con tablas de un motor: en WORK el JOIN intermedio no se cablea."""
    text = """
proc sql;
create table work.filtro as select b.clave, b.total from work.origen b where b.total > 0;
create table stg.resumen as select f.clave, c.nombre from work.filtro f join work.clientes c on f.clave = c.clave;
quit;
"""
    _, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")], notes
    assert any("no son todas de un mismo motor" in n for n in notes), notes


def test_composition_is_deterministic():
    first, _ = _compose(WORK_CHAIN)
    second, _ = _compose(WORK_CHAIN)
    assert [w.details["sql"] for w in _sql_writes(first)] == [
        w.details["sql"] for w in _sql_writes(second)
    ]


def test_sql_functions_dictionary_marks_sas_only_and_portable():
    table = sql_functions()
    assert table["cats"]["status"] == "sas_only"
    assert table["sum"]["status"] == "portable"
    assert table["substrn"]["status"] == "translated"
    assert unknown_functions("select sum(a), coalesce(b, 0) from t where x in (1, 2)") == set()
    assert unknown_functions("select cats(a, b) from t") == {"cats"}


def test_translated_function_is_renamed_for_its_engine():
    assert "substr(" in translate_functions("select substrn(a, 1, 2) from t", "oracle")


def test_mask_hides_literals_and_comments_keeps_length():
    sql = "select 'a(b' as x /* ( */ from t -- ( \n"
    masked = mask(sql)
    assert len(masked) == len(sql)
    assert "(" not in masked.split("as x")[0][len("select ") :]
    assert masked.count("(") == 0


def test_split_with_reads_nested_ctes_and_main_select():
    ctes, main = split_with(
        "with a as (select f(1) from t), b as (select * from a) select * from b"
    )
    assert [name for name, _ in ctes] == ["a", "b"]
    assert main == "select * from b"


def test_rewrite_refs_replaces_qualified_and_bare_work_references():
    sql, refs = rewrite_refs(
        "select x.id from work.base x join work.base y on x.id = y.id", "work", "base", "base_cte"
    )
    assert refs == 2 and "work.base" not in sql.lower()
    sql2, refs2 = rewrite_refs(
        "select base.id from base join other on 1 = 1", "work", "base", "base_cte"
    )
    assert refs2 == 1 and sql2.startswith("select base_cte.id from base_cte")


def _engine_libs(engine: str):
    from sas_grid_migrator.intermediate_representation.models import LibraryRef

    return {"ext": LibraryRef(name="ext", engine=engine, db_schema="esq")}


def test_outer_union_corr_is_sas_syntax_and_blocks_composition():
    text = """
proc sql;
create table work.unida as select id from work.a outer union corr select id from work.b;
create table stg.uso as select id from work.unida where id > 0;
quit;
"""
    _, notes = _compose(text)
    assert not [n for n in notes if n.startswith("Compuesta")], notes
    assert any("OUTER UNION CORR" in n for n in notes), notes
