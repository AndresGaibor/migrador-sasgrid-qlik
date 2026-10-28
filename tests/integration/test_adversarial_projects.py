"""Proyectos SAS hostiles: nada debe romperse con 500 y cada Job generado debe ser un Job de Talend valido.

Esta prueba existe para que un proyecto real que se salga de lo habitual falle aqui, no en produccion.
"""

import re
from pathlib import Path

import apps.api.main as api_module
import pytest
from fastapi.testclient import TestClient
from tests.support.spec_invariants import project_problems

JOB_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
COMPONENT_NAME = re.compile(r"^t[A-Za-z0-9_]+$")
UNIQUE_NAME = re.compile(r"^[A-Za-z_]\w*$")

SIMPLE = "data work.salida; set work.entrada; where edad > 18; run;\n"
SQL = "proc sql; create table work.r as select a, count(*) as n from work.t group by a; quit;\n"
MACRO = "%macro corre(x); data work.o&x; set work.i&x; run; %mend; %corre(1); %corre(2);\n"

NL = chr(10)
BS = chr(92)
INCLUDE_B = "%include 'b.sas';" + NL + "data work.a; set work.x; run;" + NL
INCLUDE_A = "%include 'a.sas';" + NL + "data work.b; set work.y; run;" + NL
INCLUDE_WINDOWS = "%include 'C:" + BS + "datos" + BS + "comun.sas';" + NL + "data work.z; set work.w; run;" + NL
INCLUDE_MISSING = "%include '/no/existe/nunca.sas';" + NL + "data work.q; set work.r; run;" + NL
MACRO_UNO = "%macro comun(x); data work.u&x; set work.v&x; run; %mend;" + NL
MACRO_DOS = "%macro comun(x); proc sql; create table work.d&x as select * from work.e&x; quit; %mend;" + NL + "%comun(1);" + NL

#: ruta relativa -> contenido (bytes o texto)
HOSTILE: dict[str, bytes | str] = {
    "con espacios y (parentesis).sas": SIMPLE,
    "acentuación_ñandú.sas": SIMPLE,
    "123_empieza_por_numero.sas": SIMPLE,
    "UPPER_Y_lower.SAS": SIMPLE,
    "a-b.c.d.sas": SIMPLE,
    "x" * 180 + ".sas": SIMPLE,
    "carpeta uno/duplicado.sas": SIMPLE,
    "carpeta dos/duplicado.sas": SQL,
    "carpeta tres/sub/duplicado.sas": MACRO,
    "tests/src_y_target.sas": SIMPLE,
    "src/main.sas": SQL,
    "target/out.sas": SIMPLE,
    "vacio.sas": "",
    "solo_comentarios.sas": "/* nada */\n* otro;\n",
    "bom_y_crlf.sas": "﻿" + SIMPLE.replace("\n", "\r\n"),
    "binario.sas": bytes(range(256)) * 4,
    "sin_punto_y_coma.sas": "data work.x set work.y",
    "macro_sin_cerrar.sas": "%macro abierta(x); data work.a; set work.b; run;\n",
    "unicode_en_el_codigo.sas": "data work.café; set work.niño; run;\n",
    "caso/Cargar.sas": SIMPLE,
    "caso2/cargar.sas": SQL,
    "ciclo/a.sas": INCLUDE_B,
    "ciclo/b.sas": INCLUDE_A,
    "inc_windows.sas": INCLUDE_WINDOWS,
    "inc_inexistente.sas": INCLUDE_MISSING,
    ".oculta/escondido.sas": SIMPLE,
    "n1/n2/n3/n4/n5/n6/n7/n8/n9/n10/n11/n12/profundo.sas": SIMPLE,
    "macros/uno.sas": MACRO_UNO,
    "macros/dos.sas": MACRO_DOS,
    "linea_enorme.sas": "data work.a; set work.b; where " + " or ".join(f"x = {i}" for i in range(3000)) + "; run;\n",
}


def _write(root: Path) -> None:
    for relative, content in HOSTILE.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))


@pytest.fixture(scope="module")
def hostile_previews(tmp_path_factory):
    root = tmp_path_factory.mktemp("hostile")
    source = root / "sas"
    _write(source)
    import os

    os.environ["SGM_DATA_DIR"] = str(root / "data")
    os.environ["TALEND_APPLY_FOLDER"] = "Process/Pruebas"
    os.environ["TALEND_MCP_READONLY"] = "false"
    with TestClient(api_module.app) as client:
        project_id = client.post("/api/projects", json={"name": "hostil"}).json()["id"]
        assert client.post(f"/api/projects/{project_id}/imports", json={"path": str(source)}).status_code == 201
        assert client.post(f"/api/projects/{project_id}/analyses").status_code == 201
        assert client.post(f"/api/projects/{project_id}/plans").status_code == 201
        plans = client.get(f"/api/projects/{project_id}/plans").json()
        items = plans if isinstance(plans, list) else plans.get("plans", [])
        previews = {}
        for item in items:
            response = client.post(f"/api/projects/{project_id}/plans/{item['program']}/talend-apply/preview")
            previews[item["program"]] = response
    return previews


def _arguments(hostile_previews):
    return {
        program: response.json()["arguments"]
        for program, response in hostile_previews.items()
        if response.status_code == 200 and response.json().get("arguments")
    }


def _walk(arguments):
    yield arguments
    for child in arguments.get("childJobs") or []:
        yield from _walk(child)


def test_no_program_makes_the_api_crash(hostile_previews):
    errors = {program: response.status_code for program, response in hostile_previews.items() if response.status_code >= 500}
    assert not errors, f"El API respondio 5xx: {errors}"


def test_every_program_is_planned(hostile_previews):
    planned = set(hostile_previews)
    missing = {path for path in HOSTILE if path not in planned and not path.endswith(("binario.sas",))}
    assert not missing, f"Programas sin plan: {sorted(missing)}"


def test_every_job_meets_the_talend_invariants_and_names_are_unique_in_the_project(hostile_previews):
    problems = project_problems(_arguments(hostile_previews), component_limit=api_module._max_apply_components())

    assert not problems, NL.join(problems[:25])
