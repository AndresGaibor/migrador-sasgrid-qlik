"""`tools/automation_metrics.py` es la métrica del plan de automatización: no debe romperse sin que nadie lo note."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("automation_metrics", ROOT / "tools" / "automation_metrics.py")
automation_metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(automation_metrics)


def test_measure_reports_how_many_steps_still_need_a_person():
    report = automation_metrics.measure(ROOT / "tests" / "fixtures" / "sas" / "synthetic" / "bancolombia_sas_synthetic_orchestration")

    assert report["programs"] > 0
    assert report["steps"] >= report["steps_with_pending"] > 0
    assert 0 <= report["automated_percent"] <= 100
    # Las lecturas de datasets intermedios ya no son pasos (versions.py los encadena); lo que queda son lecturas de
    # archivo (proc import), que sí cuentan como pasos que pueden necesitar a una persona.
    assert "read_file" in report["by_operation"]
    assert report["pending_categories"]


def test_pending_categories_ignore_names_paths_and_numbers():
    first = automation_metrics.pending_category("Paso 1 (`a.sas`:3): propiedad TABLE sin valor verificado; origen X")
    second = automation_metrics.pending_category("Paso 7 (`b.sas`:99): propiedad TABLE sin valor verificado; origen Y")

    assert first == second
