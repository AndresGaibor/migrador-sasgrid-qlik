# sas-grid-migrator

Analizador y asistente de migración por lotes de **SAS 9.4 / SAS Grid** a **Talend Studio**.

No convierte `.sas` a `.item`. Python analiza y propone; `talend-mcp` (solo lectura) inspecciona las capacidades reales de Talend; el desarrollador construye y valida los Jobs en Talend Studio.

Salida principal: inventario, grafo de dependencias y plan de construcción por Job (JSON + Markdown), con trazabilidad archivo/línea a SAS.

## Estado

F1–F7 completas: importación segura, parser P0/P1/P2, dependencias y Grid, IR + planes por Job (Markdown/JSON/CSV) y adaptador talend-mcp de solo lectura (opcional). F6 (frontend) y F7 (endurecimiento, golden tests, guías) completas. Ver [docs/pilot-report.md](docs/pilot-report.md) y [docs/equivalence-testing.md](docs/equivalence-testing.md). Ver [docs/architecture.md](docs/architecture.md) para arquitectura, fases y alcance.

## Uso

```bash
uv sync
uv run pytest
uv run sgm version
uv run sgm import tests/fixtures/sas -n corpus   # crea proyecto e importa el lote
uv run sgm inventory <project_id>
uv run sgm analyze <project_id>               # parseo + cobertura P0/P1/P2
uv run sgm deps <project_id>                  # dependencias, capas y tareas Grid
uv run sgm plan <project_id> [-o dir]         # planes por Job + index.md + steps.csv
uv run uvicorn apps.api.main:app --reload   # API local
```

Despliegue persistente (systemd + Tailscale Serve): ver [ops/systemd/README.md](ops/systemd/README.md).

Frontend (`apps/web`, React + TS + Vite + Bun):

```bash
uv run uvicorn apps.api.main:app --port 8000     # API
cd apps/web && bun install && bun run dev         # UI en :5173; SGM_API=http://127.0.0.1:8000 si la API usa otro puerto
bun test && bun run build
```

## Estructura

- `src/sas_grid_migrator/` núcleo: ingestion, sas_parser, macro_resolver, semantic_analysis, grid_analysis, dependency_graph, intermediate_representation, migration_planner, talend_adapter, reporting, validation, persistence, cli.
- `apps/api` FastAPI; `apps/web` frontend (pendiente).
- `rules/` reglas versionadas (sas, talend, mappings); `schemas/` contratos JSON; `templates/` plantillas de salida.
- `tests/` fixtures SAS, unit, integration, golden.
- `docs/` arquitectura, cobertura SAS, reglas de migración, seguridad.
