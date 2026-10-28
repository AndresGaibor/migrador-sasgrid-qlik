from sas_grid_migrator.talend_adapter.naming import (
    MAX_FOLDER_CHARS,
    MAX_JOB_NAME,
    cap_job_name,
    folder_path,
    folder_segment,
)


def test_reserved_git_names_get_a_suffix_in_any_case():
    assert folder_segment("src") == "src_sas"
    assert folder_segment("Tests") == "Tests_sas"
    assert folder_segment("TARGET") == "TARGET_sas"
    assert folder_segment("source") == "source"


def test_accents_spaces_and_symbols_become_a_safe_name():
    assert folder_segment("Cargas diarias (v2)") == "Cargas_diarias_v2"
    assert folder_segment("acentuación_ñandú") == "acentuacion_nandu"
    assert folder_segment("  .oculta. ") == "oculta"


def test_an_empty_or_dot_only_segment_gets_a_placeholder():
    assert folder_segment("") == "carpeta"
    assert folder_segment("...") == "carpeta"
    assert folder_segment("¿¡") == "carpeta"


def test_a_long_segment_is_capped_but_stays_distinguishable():
    first = folder_segment("a" * 90)
    second = folder_segment("a" * 89 + "b")

    assert len(first) <= 40 and len(second) <= 40
    assert first != second
    assert first == folder_segment("a" * 90)


def test_folder_path_drops_parent_references_and_empty_parts():
    assert folder_path("Process/Proyecto", "../../etc/./clientes//src") == "Process/Proyecto/etc/clientes/src_sas"
    assert folder_path("Process/Proyecto", "") == "Process/Proyecto"
    assert folder_path("Process/Proyecto", "inc") == "Process/Proyecto/inc"


def test_a_deep_or_long_path_is_collapsed_to_stay_within_windows_limits():
    deep = "/".join(f"carpeta_numero_{index}" for index in range(12))

    result = folder_path("Process/P", deep)

    assert len(result) - len("Process/P/") <= MAX_FOLDER_CHARS
    assert result.startswith("Process/P/")
    assert result == folder_path("Process/P", deep)
    assert result != folder_path("Process/P", deep + "/otra")


def test_a_short_job_name_is_left_alone_and_a_long_one_keeps_a_unique_tail():
    assert cap_job_name("job_clientes") == "job_clientes"
    long_a = cap_job_name("job_" + "x" * 150)
    long_b = cap_job_name("job_" + "x" * 149 + "y")

    assert len(long_a) <= MAX_JOB_NAME and len(long_b) <= MAX_JOB_NAME
    assert long_a != long_b
    assert long_a.startswith("job_xxxxxxxx")
