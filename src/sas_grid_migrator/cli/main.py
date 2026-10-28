from collections import Counter
from pathlib import Path

import typer

from sas_grid_migrator import __version__
from sas_grid_migrator.cli.dev import dev
from sas_grid_migrator.config import Settings
from sas_grid_migrator.ingestion.importer import ImportError_
from sas_grid_migrator.persistence.store import Store

app = typer.Typer(help="SAS Grid Migrator: análisis estático y planes de migración a Talend.")


@app.callback()
def main() -> None:
    """Fuerza modo multi-comando (los comandos se añaden por fase)."""


@app.command()
def version() -> None:
    """Muestra la versión."""
    typer.echo(__version__)


app.command("dev")(dev)


@app.command("import")
def import_cmd(
    path: Path = typer.Argument(..., exists=True, help="Carpeta o ZIP con el lote"),
    name: str = typer.Option(..., "--name", "-n", help="Nombre del proyecto"),
) -> None:
    """Crea un proyecto e importa un lote de forma segura (sin ejecutar nada)."""
    store = Store(Settings.from_env())
    project = store.create_project(name)
    try:
        m = store.import_batch(project.id, path)
    except ImportError_ as e:
        raise typer.Exit(typer.echo(f"importación rechazada: {e}", err=True) or 1)
    typer.echo(f"{project.id}  {len(m.files)} archivos, {len(m.skipped)} omitidos")


@app.command()
def inventory(project_id: str) -> None:
    """Inventario por tipo de archivo y omitidos."""
    store = Store(Settings.from_env())
    if store.get_project(project_id) is None:
        raise typer.Exit(typer.echo("proyecto no encontrado", err=True) or 1)
    m = store.get_manifest(project_id)
    for kind, n in sorted(Counter(f.kind.value for f in m.files).items()):
        typer.echo(f"{kind:6} {n}")
    for s in m.skipped:
        typer.echo(f"omitido  {s.path}: {s.reason}")


@app.command()
def analyze(project_id: str) -> None:
    """Análisis estático: parsea los .sas, clasifica construcciones P0/P1/P2."""
    from sas_grid_migrator.sas_parser.analyze import analyze_project, summarize

    store = Store(Settings.from_env())
    if store.get_project(project_id) is None:
        raise typer.Exit(typer.echo("proyecto no encontrado", err=True) or 1)
    s = summarize(analyze_project(store, project_id))
    typer.echo(
        f"{s.programs} programas, {s.statements} sentencias, {s.unrecognized} no reconocidas, "
        f"{s.macro_fragments} fragmentos de macro"
    )
    typer.echo("hallazgos: " + ", ".join(f"{k}={v}" for k, v in s.findings_by_priority.items()))
    for c in s.coverage:
        typer.echo(f"{c.priority} {c.tag:28} {c.count}")


@app.command()
def deps(project_id: str) -> None:
    """Grafo de dependencias, orden de procesamiento y orquestación Grid."""
    from sas_grid_migrator.dependency_graph.builder import build_dependencies

    store = Store(Settings.from_env())
    if store.get_project(project_id) is None:
        raise typer.Exit(typer.echo("proyecto no encontrado", err=True) or 1)
    r = build_dependencies(store, project_id)
    typer.echo(
        f"{len(r.programs)} programas, {len(r.datasets)} datasets, {len(r.edges)} aristas, "
        f"{len(r.cycles)} ciclos, {len(r.unresolved)} sin resolver, {len(r.orchestration.tasks)} tareas Grid"
    )
    for i, layer in enumerate(r.processing_order, 1):
        typer.echo(f"capa {i}: {len(layer)} programas")
    for t in r.orchestration.tasks:
        after = f" (tras {', '.join(t.after)})" if t.after else ""
        typer.echo(
            f"tarea {t.id} [{t.kind}] {t.program or '?'} → {t.resolved_program or t.match_status}{after}"
        )


@app.command()
def plan(
    project_id: str,
    out: Path = typer.Option(
        None, "--out", "-o", help="Directorio de salida (Markdown, JSON, CSV)"
    ),
    fresh: bool = typer.Option(
        False, "--fresh", help="Reanalizar en vez de reutilizar el análisis"
    ),
) -> None:
    """Genera los planes de migración por Job y los exporta."""
    from sas_grid_migrator.dependency_graph.builder import load_dependencies
    from sas_grid_migrator.migration_planner.service import generate_plans
    from sas_grid_migrator.reporting.exports import write_exports

    store = Store(Settings.from_env())
    if store.get_project(project_id) is None:
        raise typer.Exit(typer.echo("proyecto no encontrado", err=True) or 1)
    ps = generate_plans(store, project_id, fresh=fresh)
    steps = sum(len(p.steps) + sum(len(c.steps) for c in p.children) for p in ps.plans)
    review = sum(1 for p in ps.plans if p.job_status == "needs_review")
    typer.echo(f"{len(ps.plans)} planes, {steps} pasos, {review} requieren revisión")
    target = out or store.settings.data_dir / "projects" / project_id / "exports"
    files = write_exports(ps, target, load_dependencies(store, project_id))
    typer.echo(f"{len(files)} archivos en {target}")
