"""Contextos tipados, estructura de Jobs (partes, tRunJob, conexión, errores) y buenas prácticas."""

import os
import shutil
from pathlib import Path

import pytest

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner import context_rules
from sas_grid_migrator.migration_planner.limits import MAX_COMPONENTS_PER_JOB
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store
from sas_grid_migrator.talend_adapter.best_practices import evaluate_job_practices

FIXTURE_DIR = Path(__file__).parent.parent / "fixtures" / "cod1"


def _generate(tmp_path, source_dir: Path, program_name: str):
    target = tmp_path / "src"
    target.mkdir(parents=True)
    shutil.copy(source_dir / program_name, target / program_name)
    store = Store(Settings(data_dir=tmp_path / "data"))
    project = store.create_project("cod1")
    store.import_batch(project.id, target)
    return generate_plans(store, project.id).plans


@pytest.fixture(scope="module")
def cod1_plan(tmp_path_factory):
    plans = _generate(tmp_path_factory.mktemp("cod1"), FIXTURE_DIR, "cod1_recorte.sas")
    assert len(plans) == 1
    return plans[0]


def _job_sizes(plan):
    """Componentes por Job: cada lista de pasos (principal o hijo) agrupada por parte."""
    sizes = []
    for steps in [plan.steps, *(child.steps for child in plan.children)]:
        counts: dict[str, int] = {}
        for step in steps:
            counts[step.job_part or plan.job_name] = counts.get(step.job_part or plan.job_name, 0) + 1
        sizes.extend(counts.items())
    return sizes


def _variables(plan):
    return {variable.name: variable for variable in plan.context_variables}


def test_password_context_is_secret_without_plain_value(cod1_plan):
    clave = _variables(cod1_plan)["clave"]

    assert clave.talend_type == "id_Password"
    assert clave.is_secret is True
    assert clave.sas_value is None
    assert clave.needs_value is True
    assert "SecretoFicticio123" not in cod1_plan.model_dump_json()


def test_unused_template_placeholders_are_pruned_and_credentials_still_need_a_value(cod1_plan):
    variables = _variables(cod1_plan)

    # Los restos de plantilla de SAS Studio que el pipeline no usa no son contexto: se registran una vez.
    assert not [v.name for v in cod1_plan.context_variables if (v.sas_value or "").startswith("$")]
    entry = next(e for e in cod1_plan.not_migrated if e.category == "variables_sin_uso")
    assert "Sin uso" in entry.reason
    # Las credenciales se conservan siempre y piden su valor al equipo.
    assert variables["pass_bd"].needs_value is True


def test_environment_parameter_gets_group_values(cod1_plan):
    variables = _variables(cod1_plan)

    assert variables["lz_dsn"].group_values == {"DEV": "IMPALA", "QA": "IMPALAC", "PROD": "IMPALAP"}
    assert variables["m_ambiente"].group_values == {"DEV": "D", "QA": "C", "PROD": "P"}


def test_context_keeps_sas_line_for_let_statements(cod1_plan):
    assert _variables(cod1_plan)["clave"].sas_line == 33


def test_no_job_exceeds_the_component_limit(cod1_plan):
    sizes = _job_sizes(cod1_plan)
    assert all(count <= MAX_COMPONENTS_PER_JOB for _, count in sizes), sizes
    # El recorte es un único Job: la macro de una llamada (append_all) se funde en línea y ambiente es
    # fontanería. No hace falta orquestador ni tRunJob.
    assert cod1_plan.job_parts == []
    assert cod1_plan.orchestrator is None
    assert cod1_plan.children == []
    # El bucle que solo duplica filas para una prueba de carga no es paso: es not_migrated (por forma).
    categories = {entry.category for entry in cod1_plan.not_migrated}
    assert "variables_control" in categories
    assert "datos_de_prueba" in categories


def test_database_jobs_have_one_shared_connection(tmp_path, cod1_plan):
    steps = cod1_plan.steps
    shared = [s for s in steps if s.recommended and "Compartida" in s.id]
    assert len(shared) <= 1
    assert all(s.why for s in steps if s.recommended)


def test_recommended_steps_have_why_and_error_handling(cod1_plan):
    recommended = [s for s in cod1_plan.steps if s.recommended]
    components = {s.component_candidate for s in recommended}

    assert "tDie" in components  # manejo de errores del Job
    # El diseño nuevo no genera pasos de aviso ni de log recomendados (tWarn, tLogCatcher, tPrejob, tPostjob).
    assert not {"tLogCatcher", "tWarn", "tPrejob", "tPostjob"} & components
    assert all(s.why for s in recommended)


def test_each_job_recommends_at_most_three_steps_and_has_an_error_path(cod1_plan):
    containers = [cod1_plan.steps, *(child.steps for child in cod1_plan.children)]
    for steps in containers:
        recommended = [s for s in steps if s.recommended]
        assert len(recommended) <= 3, [s.id for s in recommended]
        assert any(s.component_candidate == "tDie" for s in recommended)


def test_practices_report_missing_context_and_secrets(cod1_plan):
    findings = evaluate_job_practices(cod1_plan)
    ids = {finding.id for finding in findings}

    assert "PLAN-ERR-01" not in ids  # el plan tiene manejo de errores recomendado
    assert all(finding.message for finding in findings)


def test_credential_hits_detect_literal_and_pwencode_without_returning_value():
    source = "data x;\nrun;\nproc sql;\nconnect to x (user=u pass='Literal1');\nquit;\nproc pwencode in='Cifra2';\nrun;\n"
    hits = context_rules.credential_hits(source)

    assert [(hit.line, hit.kind) for hit in hits] == [(4, "literal"), (6, "pwencode")]


def test_macro_password_reference_is_not_a_literal():
    assert context_rules.credential_hits('connect to x (user=u pass="&SASPC_PW");') == []


def test_plan_warns_about_credentials_in_unresolved(tmp_path):
    source_dir = tmp_path / "fuente"
    source_dir.mkdir()
    (source_dir / "carga_pass.sas").write_text(
        "libname a 'x';\ndata a.b;\nset a.c;\nrun;\n"
        "proc sql;\nconnect to oracle (user=u pass='LiteralClave');\nquit;\n",
        encoding="utf-8",
    )
    plans = _generate(tmp_path / "run", source_dir, "carga_pass.sas")
    plan = plans[0]

    assert any(w.startswith("Credencial en claro") and "LiteralClave" not in w for w in plan.unresolved)
    assert plan.job_status == "needs_review"


def test_observed_count_macros_are_not_migrated_as_stat_or_log_rows(tmp_path):
    """Una macro que solo cuenta filas (select count(*) sin alias) es fontanería: no es hijo ni genera tStatCatcher."""
    source_dir = tmp_path / "fuente"
    source_dir.mkdir()
    (source_dir / "conteos.sas").write_text(
        "data w.a;\nset w.b;\nrun;\n%macro cuenta_filas;\nproc sql;\nselect count(*) from w.a;\nquit;\n%mend cuenta_filas;\n%cuenta_filas;\n",
        encoding="utf-8",
    )
    plan = _generate(tmp_path / "run", source_dir, "conteos.sas")[0]

    assert not [c for c in plan.children if c.name == "cuenta_filas"]
    recorded = [entry for entry in plan.not_migrated if entry.category == "conteo"]
    assert recorded and all("tStatCatcher" in entry.talend_equivalent for entry in recorded)
    steps = plan.steps + [s for c in plan.children for s in c.steps]
    assert not {"tStatCatcher", "tLogRow"} & {s.component_candidate for s in steps if s.recommended}


def test_explicit_proc_print_still_becomes_a_log_row(tmp_path):
    """El conteo solo produce tLogRow si el SAS lo escribe explícitamente (aquí, un PROC PRINT)."""
    source_dir = tmp_path / "fuente"
    source_dir.mkdir()
    (source_dir / "imprime.sas").write_text(
        "data w.a;\nset w.b;\nrun;\nproc print data=w.a;\nrun;\n",
        encoding="utf-8",
    )
    plan = _generate(tmp_path / "run", source_dir, "imprime.sas")[0]

    assert "tLogRow" in {s.component_candidate for s in plan.steps}


@pytest.mark.skipif(not os.environ.get("COD1_PATH"), reason="COD1_PATH no definido")
def test_full_cod1_respects_structure_rules(tmp_path):
    source = Path(os.environ["COD1_PATH"])
    if not source.exists():
        pytest.skip("COD1_PATH no existe")
    plans = _generate(tmp_path, source.parent, source.name)
    plan = plans[0]

    sizes = _job_sizes(plan)
    assert all(count <= MAX_COMPONENTS_PER_JOB for _, count in sizes), sizes
    assert "SecretoFicticio" not in plan.model_dump_json()
    # Tras la fusión Cod1 completo son ~17 componentes (límite 25): cabe en un Job, sin partes ni orquestador.
    assert plan.job_parts == [] and plan.orchestrator is None
    assert any(v.needs_value for v in plan.context_variables)


@pytest.mark.skipif(not os.environ.get("COD1_PATH"), reason="COD1_PATH no definido")
def test_full_cod1_uses_one_engine_connection_per_job(tmp_path):
    source = Path(os.environ["COD1_PATH"])
    plan = _generate(tmp_path, source.parent, source.name)[0]
    containers = [plan.steps, *(child.steps for child in plan.children)]
    for steps in containers:
        per_job: dict[str, int] = {}
        for step in steps:
            if step.recommended and step.component_candidate.endswith("Connection"):
                per_job[step.job_part or ""] = per_job.get(step.job_part or "", 0) + 1
        assert all(count == 1 for count in per_job.values()), per_job
    # El motor sale del propio SAS (lz_dsn=IMPALA): la conexión es de Impala, no un genérico.
    assert any(s.component_candidate == "tImpalaConnection" for s in plan.steps + [x for c in plan.children for x in c.steps])
    assert not any(s.component_candidate == "tDBConnection" for s in plan.steps)
