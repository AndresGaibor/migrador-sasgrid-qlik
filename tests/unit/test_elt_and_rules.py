"""Casos sintéticos genéricos de las reglas ELT y de planificador (R45, R46, R23, R50, R04, R13).

Cada caso es un SAS mínimo con nombres inventados (no los de Cod1/Cod2). Las aserciones son
estructurales: componentes, número de pasos, avisos. Se escribieron antes que la implementación.
"""

from __future__ import annotations

from sas_grid_migrator.intermediate_representation.builder import build_ir
from sas_grid_migrator.migration_planner.planner import load_mapping_rules, plan_program
from sas_grid_migrator.sas_parser.parser import parse_program


def _plan(text: str):
    program = parse_program(text, "caso_sintetico.sas")
    # source_text: el servicio lo pasa; lo usan los avisos que dependen del texto (p. ej. R13).
    return plan_program(build_ir(program), "casos", load_mapping_rules(), {}, source_text=text)


def _steps(plan):
    return plan.steps + [s for child in plan.children for s in child.steps]


def _real_steps(plan):
    """Pasos sin el tDie de seguridad ni la conexión compartida (la estructura del Job los añade)."""
    return [
        s
        for s in _steps(plan)
        if s.component_candidate not in ("tDie", "") and s.action != "manual_decision"
        and not (s.component_candidate == "por_determinar" and "onexi" in s.purpose)
        and not (s.component_candidate == "por_determinar" and "Cierra" in s.purpose)
    ]


def _candidates(plan):
    return [s.component_candidate for s in _steps(plan)]


def _unresolved_text(plan) -> str:
    texts = list(plan.unresolved) + [a for s in _steps(plan) for a in s.assumptions]
    return "\n".join(texts)


# ---------------------------------------------------------------- R45: ejecución pass-through


def test_r45_execute_by_engine_is_one_row_component_with_the_sql():
    """Una sentencia `execute (...) by motor` es UN componente Row del motor con el SQL completo."""
    plan = _plan(
        "proc sql;\n"
        "connect to oracle (user=etl path='ORCLX');\n"
        "execute (create table esq.resumen as select a.clave, sum(a.valor) as total "
        "from esq.origen a group by a.clave) by oracle;\n"
        "disconnect from oracle;\n"
        "quit;\n"
    )
    rows = [s for s in _steps(plan) if s.component_candidate == "tOracleRow"]
    assert len(rows) == 1, _candidates(plan)
    query = next(p.value for p in rows[0].properties if p.name == "QUERY")
    assert "group by a.clave" in (query or "")


def test_r45_each_execute_statement_is_its_own_step_in_order():
    """Dos sentencias seguidas de la misma conexión son dos pasos, en el orden del programa."""
    plan = _plan(
        "proc sql;\n"
        "connect to oracle (user=etl path='ORCLX');\n"
        "execute (create table esq.uno as select k from esq.a) by oracle;\n"
        "execute (create table esq.dos as select k from esq.b) by oracle;\n"
        "disconnect from oracle;\n"
        "quit;\n"
    )
    rows = [s for s in _steps(plan) if s.component_candidate == "tOracleRow"]
    assert len(rows) == 2, _candidates(plan)
    assert rows[0].order < rows[1].order


# ---------------------------------------------------------------- ELT BD a BD (mismo motor)


def test_elt_create_table_between_tables_of_one_libname_is_one_row_component():
    """create table <lib>.x as select ... from <lib>.y, con libname de motor: un solo Row, sin lectura
    ni escritura intermedias."""
    plan = _plan(
        "libname ext oracle user=etl path='ORCLX' schema=esq;\n"
        "proc sql;\n"
        "create table ext.res_dos as select b.clave, b.total from ext.origen_b b where b.total > 0;\n"
        "quit;\n"
    )
    candidates = _candidates(plan)
    assert candidates.count("tOracleRow") == 1, candidates
    assert "tOracleInput" not in candidates and "tOracleOutput" not in candidates, candidates
    assert "tMap" not in candidates, candidates


def test_elt_is_not_applied_when_source_and_target_differ():
    """Origen en WORK y destino en el motor: no es ELT, se mantiene la lectura y la escritura."""
    plan = _plan(
        "libname ext oracle user=etl path='ORCLX' schema=esq;\n"
        "proc sql;\n"
        "create table ext.res_dos as select b.clave from work.origen_b b;\n"
        "quit;\n"
    )
    assert "tOracleRow" not in _candidates(plan), _candidates(plan)


def test_elt_is_not_applied_with_sas_only_functions():
    """Una función solo SAS (monotonic) impide empujar la sentencia al motor."""
    plan = _plan(
        "libname ext oracle user=etl path='ORCLX' schema=esq;\n"
        "proc sql;\n"
        "create table ext.ranking as select b.clave, monotonic() as posicion from ext.origen_b b;\n"
        "quit;\n"
    )
    assert "tOracleRow" not in _candidates(plan), _candidates(plan)


# ---------------------------------------------------------------- R46: lectura pass-through


def test_r46_connection_to_read_becomes_input_component_with_the_query():
    """`from connection to motor (select ...)` que alimenta lógica SAS: tOracleInput con la consulta."""
    plan = _plan(
        "libname ext oracle user=etl path='ORCLX' schema=esq;\n"
        "proc sql;\n"
        "create table work.leido as select * from connection to oracle "
        "(select a.clave, b.dato from esq.origen_a a left join esq.origen_b b on a.clave = b.clave);\n"
        "quit;\n"
        "data out.final; set work.leido; if dato > 0; run;\n"
    )
    inputs = [s for s in _steps(plan) if s.component_candidate == "tOracleInput"]
    assert len(inputs) == 1, _candidates(plan)
    query = next(p.value for p in inputs[0].properties if p.name == "QUERY")
    assert "left join" in (query or "").lower()


# ---------------------------------------------------------------- R23: copia de vuelta en sitio


def test_r23_repeated_copy_back_on_work_dataset_is_one_tmap_chain():
    """Tres bloques `data tmp; set X; ...; data X; set tmp;` sobre WORK.X: sin escrituras ni lecturas de
    WORK ni temporales, y un tMap por bloque encadenado.

    Objetivo del catálogo (R23): UN solo tMap con las expresiones de los tres bloques. Antes (un tMap por
    bloque) el test fijaba la limitación de ChainState; cambió por diseño al introducir el versionado
    (versions.py): la reasignación de importe_m se sustituye por su expresión y la cadena no se corta.
    """
    plan = _plan(
        "data work.base; set src.clientes; run;\n"
        "data work.tmp1; set work.base; importe_m = importe * 2; run;\n"
        "data work.base; set work.tmp1; run;\n"
        "proc delete data=work.tmp1; run;\n"
        "data work.tmp2; set work.base; importe_m = importe_m + 1; run;\n"
        "data work.base; set work.tmp2; run;\n"
        "proc delete data=work.tmp2; run;\n"
        "data work.tmp3; set work.base; estado_n = input(left(estado), 8.); run;\n"
        "data work.base; set work.tmp3; run;\n"
        "proc delete data=work.tmp3; run;\n"
        "data out.clientes_final; set work.base; run;\n"
    )
    writes_work = [s for s in _steps(plan) if s.operation_type == "write" and "work." in s.purpose.lower()]
    assert not writes_work, [s.purpose for s in writes_work]
    real = _real_steps(plan)
    assert len([s for s in real if s.component_candidate == "tMap"]) == 1, _candidates(plan)
    assert len(real) <= 3, [(s.component_candidate, s.purpose) for s in real]


def test_r23_copy_back_on_external_table_keeps_one_final_write():
    """Copia de vuelta sobre una tabla de la base: la escritura final sí se conserva (una sola)."""
    plan = _plan(
        "libname src oracle user=etl path='ORCLX' schema=esq;\n"
        "data work.tmp_saldo; set src.cuentas; saldo_neto = saldo_bruto * 2; run;\n"
        "data src.cuentas; set work.tmp_saldo; run;\n"
        "proc delete data=work.tmp_saldo; run;\n"
    )
    candidates = _candidates(plan)
    assert candidates.count("tOracleOutput") == 1, candidates
    assert not [s for s in _steps(plan) if "work." in s.purpose.lower()], candidates


# ---------------------------------------------------------------- R50 / R04: exportación y sesión remota


def test_r50_export_then_upload_writes_directly_to_remote_path():
    """`proc export` a local + `proc upload` a la ruta remota: un tFileOutputDelimited a la ruta remota,
    sin paso de subida ni sesión."""
    plan = _plan(
        "proc export data=work.resumen outfile='D:\\salida\\resumen.txt' dbms=dlm replace;\n"
        "  delimiter='|';\n"
        "run;\n"
        "options remote=srv1 comamid=tcp;\n"
        "signon usuario_srv pass=\"secreto\";\n"
        "rsubmit srv1 wait=yes;\n"
        "  proc upload infile='D:\\salida\\resumen.txt' outfile='\\\\srv1\\share\\resumen.txt';\n"
        "run;\n"
        "endrsubmit;\n"
        "signoff;\n"
    )
    real = _real_steps(plan)
    assert [s.component_candidate for s in real] == ["tFileOutputDelimited"], [
        (s.component_candidate, s.purpose) for s in real
    ]
    assert "unsupported" not in {s.operation_type for s in _steps(plan)}
    assert any("srv1" in (p.value or "") for p in real[0].properties), real[0].properties


# ---------------------------------------------------------------- R13: DSN literal con selector


def test_r13_literal_dsn_next_to_environment_selector_raises_a_warning():
    """Programa con selector de entorno y una conexión con DSN escrito a mano: aviso de alta severidad."""
    plan = _plan(
        "%let entorno = DEV;\n"
        "%macro conexion;\n"
        "  %if &entorno = DEV %then %let dsn = DSN_DEV;\n"
        "  %else %if &entorno = PROD %then %let dsn = DSN_PROD;\n"
        "%mend;\n"
        "%conexion;\n"
        "proc sql;\n"
        "connect to oracle (dsn=DSN_PROD user=u password=p);\n"
        "create table work.copia as select * from connection to oracle (select k, v from esq.tabla);\n"
        "disconnect from oracle;\n"
        "quit;\n"
    )
    text = _unresolved_text(plan)
    assert "DSN_PROD" in text and "entorno" in text.lower(), text
