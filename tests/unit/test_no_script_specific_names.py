"""Guardia anti-sobreajuste: el código no debe llevar nombres propios de los scripts Cod1/Cod2.

El planificador tiene que servir para cualquier programa SAS. Si alguien vuelve a escribir
un nombre de macro, tabla o variable de los scripts del usuario dentro del código o de las
reglas, esta prueba falla y muestra archivo:línea de cada coincidencia.

Cuenta cualquier aparición, sin distinguir mayúsculas, como palabra o como parte de un
identificador. Los nombres del LENGUAJE SAS (proc, sleep, %put, datetime...) no están aquí:
son el lenguaje, no el script.
"""

from __future__ import annotations

import re
from bisect import bisect_right
from itertools import accumulate
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
THIS_FILE = Path(__file__).resolve()

# Nombres propios de los scripts Cod1/Cod2 del usuario. Ampliar si aparecen más.
FORBIDDEN_NAMES = [
    "mainprogram",
    "executebulkload",
    "waitforbulkloads",
    "split3",
    "split2",
    "create_commands",
    "execimpalaquery",
    "capturacampos",
    "resolver_delimitador",
    "comparaRegistros",
    "comparacampos",
    "delprocesstables",
    "deletetablelz",
    "showmessage",
    "exportar_s3",
    "importar_s3",
    "bulkload_generic",
    "BULKLOAD_VARS",
    "jl_CargaImpala",
    "carga_impala",
    "cars_poc",
    "sashelp.cars",
    "pidexecution",
    "wprefix",
    "wpgmbl",
    "wt_errslz",
    "lz_dsn",
    "m_ambiente",
    "SASGRIDCOMP",
    "capturaCampos",
    "append_all",
    "web_open_table",
    "web_drop_table",
    "select_bucket",
    "grid_util",
    "activenodelzcode",
    "countTableSas",
    "countTableLz",
    "syslput",
    # Nombres adicionales detectados en Cod1.txt / Cod2.txt (variables y macros propias).
    "wserv_computo",
    "obtener_sin_incorrectos",
    "spltables",
    "wcampos",
    "wlibre_origen",
    "wpathpgmbl",
    "wpathdata",
    "tbldes_lz",
    "wtbltmp",
    "wtabsrc",
    "wlibtemp",
    "wsplit",
    "numobsperssession",
]

# Donde se busca: código Python del paquete y reglas de mapeo/Talend (sin archivo).
SEARCH_GLOBS = [
    ("src/sas_grid_migrator", "*.py"),
    ("rules/mappings", "*.json"),
    ("rules/talend", "*.json"),
]


def _pattern() -> re.Pattern[str]:
    # Una sola regex para todos los nombres, en minúsculas (el texto también se pasa a minúsculas: sin
    # IGNORECASE es varias veces más rápida), y sin letra ni dígito pegados a ambos lados: cubre la palabra
    # completa y el nombre como parte de un identificador separado por `_` (p. ej. `split3_`). No marca
    # nombres que solo aparecen dentro de otro identificador.
    alternatives = "|".join(re.escape(name.lower()) for name in sorted(FORBIDDEN_NAMES, key=len, reverse=True))
    return re.compile(r"(?<![a-z0-9])(?:" + alternatives + r")(?![a-z0-9])")


def _files() -> list[Path]:
    found: list[Path] = []
    for base, pattern in SEARCH_GLOBS:
        for path in sorted((REPO / base).rglob(pattern)):
            if "archive" in path.parts or "__pycache__" in path.parts:
                continue
            if path.resolve() == THIS_FILE:
                continue
            found.append(path)
    return found


def _matches() -> list[str]:
    # Una pasada por archivo: la regex combinada recorre el texto entero y solo se traduce a línea
    # cada coincidencia. El resultado (y su orden) es el mismo que con una regex por nombre y línea.
    pattern = _pattern()
    lowered_names = {name.lower() for name in FORBIDDEN_NAMES}
    hits: list[str] = []
    for path in _files():
        rel = path.relative_to(REPO).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        low = text.lower()
        # Prefiltro: la mayoría de archivos no contiene ningún nombre; ahí no hace falta la regex.
        if not any(name in low for name in lowered_names):
            continue
        # Mismos saltos de línea que `splitlines()`: así el número coincide con el de un editor.
        pieces = low.splitlines(keepends=True)
        starts = list(accumulate((len(piece) for piece in pieces), initial=0))
        lines = text.splitlines()
        found: dict[int, set[str]] = {}
        for match in pattern.finditer(low):
            found.setdefault(bisect_right(starts, match.start()), set()).add(match.group(0))
        for number in sorted(found):
            for name in FORBIDDEN_NAMES:  # mismo orden y mismo desglose que la versión con una regex por nombre
                if name.lower() in found[number]:
                    hits.append(f"{rel}:{number}: {name}: {lines[number - 1].strip()[:120]}")
    return hits


def test_no_script_specific_names_in_code_or_rules():
    hits = _matches()
    assert not hits, (
        f"{len(hits)} coincidencias con nombres propios de Cod1/Cod2 "
        "(generalizar: quitar el nombre y tratar el patrón de forma genérica):\n"
        + "\n".join(hits)
    )


def test_search_scope_is_not_empty():
    # Si el alcance se queda vacío (ruta cambiada), la prueba anterior pasaría sin mirar nada.
    files = _files()
    assert any(p.suffix == ".py" for p in files)
    assert any(p.suffix == ".json" and "rules/mappings" in p.as_posix() for p in files)
    assert any(p.suffix == ".json" and "rules/talend" in p.as_posix() for p in files)
