"""Configuración global de pytest.

Las pruebas `slow` (MCP real, corpus completo) no se ejecutan en la pasada normal. Se marcan con `skip`
en vez de filtrarlas con `-m` en `addopts`: el filtro `-m` impide que pytest-testmon deseleccione lo que no
cambió (ver scripts/test.ps1 -Incremental). Se ejecutan con `--runslow`, con `-m slow`, o siempre en CI
(`CI=true`, lo fija GitHub Actions), así que el workflow no necesita cambios.
"""

import os

import pytest


def _ci() -> bool:
    return os.environ.get("CI", "").lower() in {"1", "true"}


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", help="ejecuta también las pruebas marcadas `slow`")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow") or _ci() or config.getoption("markexpr"):
        return
    skip = pytest.mark.skip(reason="slow: se omite en la pasada rápida; usa --runslow o scripts/test.ps1 -Full")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip)
