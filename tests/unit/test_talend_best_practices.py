from sas_grid_migrator.talend_adapter.best_practices import check_job_arguments


def _job(components, connections=None, contexts=None):
    return {
        "jobName": "job_demo",
        "components": components,
        "connections": connections or [],
        "contexts": contexts or [],
    }


def _component(unique_name, component_name, **parameters):
    return {"uniqueName": unique_name, "componentName": component_name, "parameters": parameters}


def _rules(findings):
    return sorted({finding.rule for finding in findings})


def test_a_clean_job_has_no_findings():
    job = _job(
        [
            _component("tFileInputDelimited_1", "tFileInputDelimited", FILENAME="context.input_file"),
            _component("tLogCatcher_2", "tLogCatcher"),
        ],
        contexts=[{"name": "input_file", "type": "id_String", "value": "x"}],
    )

    assert check_job_arguments(job) == []


def test_literal_environment_values_should_be_context_variables():
    job = _job(
        [
            _component("tFileInputDelimited_1", "tFileInputDelimited", FILENAME='"C:/datos/clientes.csv"'),
            _component("tMysqlInput_2", "tMysqlInput", HOST='"db.interno"', PORT='"3306"', DBNAME='"ventas"'),
            _component("tLogCatcher_3", "tLogCatcher"),
        ]
    )

    findings = [f for f in check_job_arguments(job) if f.rule == "BP-CTX-01"]

    assert {(f.component, f.parameter) for f in findings} == {
        ("tFileInputDelimited_1", "FILENAME"),
        ("tMysqlInput_2", "HOST"),
        ("tMysqlInput_2", "PORT"),
        ("tMysqlInput_2", "DBNAME"),
    }
    assert all(f.severity == "warning" for f in findings)


def test_values_taken_from_the_context_are_accepted():
    job = _job(
        [
            _component("tMysqlInput_1", "tMysqlInput", HOST="context.db_host", PORT="context.db_port"),
            _component("tLogCatcher_2", "tLogCatcher"),
        ]
    )

    assert "BP-CTX-01" not in _rules(check_job_arguments(job))


def test_a_literal_password_is_an_error_level_finding():
    job = _job(
        [
            _component("tMysqlInput_1", "tMysqlInput", PASS='"secreto"'),
            _component("tLogCatcher_2", "tLogCatcher"),
        ]
    )

    finding = next(f for f in check_job_arguments(job) if f.rule == "BP-SEC-01")

    assert finding.severity == "error"
    assert finding.parameter == "PASS"
    assert "secreto" not in finding.message


def test_encrypted_or_context_passwords_are_not_flagged():
    job = _job(
        [
            _component("tMysqlInput_1", "tMysqlInput", PASS="enc:system.encryption.key.v1:abc"),
            _component("tOracleInput_2", "tOracleInput", PASS="context.db_pass"),
            _component("tLogCatcher_3", "tLogCatcher"),
        ]
    )

    assert "BP-SEC-01" not in _rules(check_job_arguments(job))


def test_several_database_components_should_share_one_connection():
    job = _job(
        [
            _component("tMysqlInput_1", "tMysqlInput", HOST="context.h"),
            _component("tMysqlOutput_2", "tMysqlOutput", HOST="context.h"),
            _component("tLogCatcher_3", "tLogCatcher"),
        ]
    )

    assert "BP-DB-01" in _rules(check_job_arguments(job))

    with_connection = _job(
        [
            _component("tMysqlConnection_1", "tMysqlConnection", HOST="context.h"),
            _component("tMysqlInput_2", "tMysqlInput", USE_EXISTING_CONNECTION="true"),
            _component("tMysqlOutput_3", "tMysqlOutput", USE_EXISTING_CONNECTION="true"),
            _component("tLogCatcher_4", "tLogCatcher"),
        ]
    )
    assert "BP-DB-01" not in _rules(check_job_arguments(with_connection))


def test_a_job_without_error_handling_gets_an_info_finding():
    job = _job(
        [
            _component("tFileInputDelimited_1", "tFileInputDelimited", FILENAME="context.f"),
            _component("tLogRow_2", "tLogRow"),
        ]
    )

    finding = next(f for f in check_job_arguments(job) if f.rule == "BP-ERR-01")
    assert finding.severity == "info"


def test_error_connectors_count_as_error_handling():
    job = _job(
        [
            _component("tFileInputDelimited_1", "tFileInputDelimited", FILENAME="context.f"),
            _component("tDie_2", "tDie"),
        ],
        connections=[
            {"source": "tFileInputDelimited_1", "target": "tDie_2", "label": "err", "connectorName": "SUBJOB_ERROR"}
        ],
    )

    assert "BP-ERR-01" not in _rules(check_job_arguments(job))


def test_oversized_jobs_should_be_split():
    components = [_component(f"tLogRow_{i}", "tLogRow") for i in range(1, 32)]
    components.append(_component("tLogCatcher_99", "tLogCatcher"))

    finding = next(f for f in check_job_arguments(_job(components)) if f.rule == "BP-SIZE-01")

    assert finding.severity == "warning"
    assert "32" in finding.message


def test_single_component_jobs_do_not_ask_for_error_handling():
    assert check_job_arguments(_job([_component("tLogRow_1", "tLogRow")])) == []
