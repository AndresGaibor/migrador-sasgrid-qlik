"""Mide cuánto de la migración está automatizado: qué pasos de los planes siguen necesitando a una persona y por qué.

Uso:
    uv run python tools/automation_metrics.py [carpeta con los .sas ...] [--json salida.json]

Sin argumentos mide los corpus `real/` y `synthetic/` de `tests/fixtures/sas`. Un paso está *automatizado* cuando el plan
no le deja ningún pendiente: ni el componente, ni el esquema, ni las expresiones, ni el origen o destino de los datos.
Es la métrica del plan de automatización (`docs/automation-plan.md`): cada paquete de trabajo debe bajar estos números.
"""

import argparse
import json
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sas_grid_migrator.config import Settings
from sas_grid_migrator.migration_planner.service import generate_plans
from sas_grid_migrator.persistence.store import Store

FIXTURES = ROOT / "tests" / "fixtures" / "sas"
UNDECIDED = {"por_determinar", "ninguno", ""}


def pending_category(text: str) -> str:
    """Agrupa pendientes que solo difieren en nombres, rutas o números."""
    text = re.sub(r"`[^`]*`", "X", text)
    text = re.sub(r"SAS [\w/\\.\-]+:\d+", "SAS <loc>", text)
    text = re.sub(r"expresión SAS .* sin traducción Talend verificada", "expresión SAS <e> sin traducción Talend verificada", text)
    text = re.sub(r"propiedad [\w\s/]+ sin valor verificado.*", "propiedad <p> sin valor verificado", text)
    return re.sub(r"\d+", "N", text)[:110]


def measure(source: Path, environment: Path | None = None) -> dict:
    """Métricas de un corpus: se importa como un proyecto y se planifica.

    Con `environment`, el catálogo de entorno se copia al proyecto antes de planificar: sirve para medir cuánto sube la
    automatización cuando el entorno se conoce (WP5/WP6).
    """
    store = Store(Settings(data_dir=Path(tempfile.mkdtemp(prefix="sgm-metrics-")) / "data"))
    project = store.create_project(source.name)
    store.import_batch(project.id, source)
    if environment is not None:
        store.environment_path(project.id).write_text(
            environment.read_text(encoding="utf-8"), encoding="utf-8"
        )
    plans = generate_plans(store, project.id).plans
    steps = [step for plan in plans for step in plan.steps]

    steps_by_category: Counter[str] = Counter()
    pending_by_operation: Counter[str] = Counter()
    steps_by_operation: Counter[str] = Counter()
    for step in steps:
        operation = step.operation_type or "?"
        steps_by_operation[operation] += 1
        if step.pending:
            pending_by_operation[operation] += 1
        for category in {pending_category(item) for item in step.pending}:
            steps_by_category[category] += 1

    total = len(steps)
    pending = sum(1 for step in steps if step.pending)
    return {
        "source": source.name,
        "programs": len(plans),
        "steps": total,
        "steps_with_pending": pending,
        "automated_percent": round(100 * (total - pending) / total, 1) if total else 0.0,
        "steps_without_component": sum(1 for step in steps if step.component_candidate in UNDECIDED),
        "steps_without_schema": sum(1 for step in steps if not step.schema_columns),
        "expressions": sum(len(step.expressions) for step in steps),
        "by_operation": {
            operation: {"steps": count, "with_pending": pending_by_operation[operation]}
            for operation, count in steps_by_operation.most_common()
        },
        "pending_categories": dict(steps_by_category.most_common(25)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("sources", nargs="*", type=Path, help="carpetas con programas SAS (por defecto, los corpus de fixtures)")
    parser.add_argument("--json", type=Path, help="guardar el informe en este archivo")
    parser.add_argument(
        "--environment", type=Path, help="catálogo de entorno (environment.json) para medir con entorno conocido"
    )
    args = parser.parse_args()
    sources = args.sources or [FIXTURES / "real", FIXTURES / "synthetic"]

    report = [measure(source, args.environment) for source in sources]
    for corpus in report:
        print(f"\n== {corpus['source']}: {corpus['programs']} programas, {corpus['steps']} pasos ==")
        print(f"automatizados (sin pendientes): {corpus['automated_percent']} %")
        print(f"sin componente: {corpus['steps_without_component']} · sin esquema: {corpus['steps_without_schema']} · expresiones: {corpus['expressions']}")
        print("por operación (pasos / con pendientes):")
        for operation, counts in list(corpus["by_operation"].items())[:12]:
            print(f"  {operation:24s} {counts['steps']:5d} / {counts['with_pending']:5d}")
        print("pendientes más frecuentes (pasos afectados):")
        for category, count in list(corpus["pending_categories"].items())[:10]:
            print(f"  {count:5d}  {category}")
    if args.json:
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
