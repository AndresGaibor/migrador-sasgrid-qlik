# sas-grid-migrator

Analizador y asistente de migración por lotes de **SAS 9.4 / SAS Grid** a **Talend Studio**.

No convierte `.sas` a `.item` por sí solo. Python analiza y propone; cuando el usuario pulsa el botón del proyecto, el portal envía secuencialmente al MCP los planes de todos los Jobs del ZIP para construirlos en Talend Studio. La ejecución y validación de los Jobs siguen siendo responsabilidad del desarrollador.

Salida principal: inventario, grafo de dependencias y plan de construcción por Job (JSON + Markdown), con trazabilidad archivo/línea a SAS.

## Estado

F1–F7 completas: importación segura, parser P0/P1/P2, dependencias y Grid, IR + planes por Job (Markdown/JSON/CSV), guía web y creación controlada de Jobs de prueba por medio de talend-mcp. Ver [docs/pilot-report.md](docs/pilot-report.md) y [docs/equivalence-testing.md](docs/equivalence-testing.md). Ver [docs/architecture.md](docs/architecture.md) para arquitectura, fases y alcance.

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

Para operar el portal con proyectos ZIP, análisis automático, reintentos y destinos aislados en Talend, consulta [la guía operativa](docs/zip-project-workspaces.md). Despliegue persistente (systemd + Tailscale Serve): ver [ops/systemd/README.md](ops/systemd/README.md).

Frontend (`apps/web`, React + TS + Vite + Bun):

```bash
uv run uvicorn apps.api.main:app --port 8000     # API
cd apps/web && bun install && bun run dev         # UI en :5173; SGM_API=http://127.0.0.1:8000 si la API usa otro puerto
bun test && bun run build
```

## Crear Jobs de prueba en Talend

En «Mis proyectos», **Subir ZIP y crear proyecto** registra un proyecto aislado y arranca extracción, análisis SAS, dependencias y guías. La página conserva el estado y ofrece reintento si falla. En «Plan de migración», **Implementar todos los flujos del ZIP en Talend** consulta primero el inventario completo de Studio y muestra qué Jobs se crearán, actualizarán en su carpeta destino o bloquearán el lote por conflicto. La API vuelve a comprobar el inventario antes de escribir. El botón se activa solo con inventario disponible y sin conflictos. La operación muestra avance y resultado por programa; los Jobs no se ejecutan.

El portal usa estas variables de entorno. Los valores predeterminados sirven para la prueba local; cambia los valores en el entorno del proceso API si MCP usa otro puerto o carpeta:

```dotenv
TALEND_MCP_URL=http://127.0.0.1:3927/mcp
TALEND_MCP_TIMEOUT_SECONDS=60
TALEND_MCP_READONLY=false
TALEND_APPLY_FOLDER=Process/PruebasWebSAS
SGM_DATA_DIR=./data
SGM_MAX_TOTAL_BYTES=268435456
SGM_MAX_PIPELINE_CONCURRENCY=2
SGM_MAX_QUEUED_PIPELINES=20
```

En el `.env.local` de `talend-mcp`, `TALEND_MCP_HOST` y `TALEND_MCP_PORT` configuran el servidor (por defecto `127.0.0.1` y `3927`). Si cambias alguno, ajusta `TALEND_MCP_URL` para que coincida. Mantén el MCP en loopback y reinicia los dos procesos después de cambiar su configuración.

Arranca el MCP con `bun run start:server`, la API con `uv run uvicorn apps.api.main:app --host 127.0.0.1 --port 8000` y la UI con `cd apps/web && bun run dev`. Al subir un ZIP, el portal conserva la estructura de carpetas y muestra el estado de cada etapa. En «Plan de migración», pulsa **Implementar todos los flujos del ZIP en Talend**. La API llama secuencialmente a `talend_job_apply_custom_spec` una vez por Job que no haya sido confirmado dentro de un Job padre. El estado y los resultados se guardan por proyecto; el portal consulta el avance al recargar. Los Jobs no se ejecutan.

`TALEND_MCP_READONLY` fija el valor inicial del permiso de escritura: `true` arranca en solo lectura. Después decide el interruptor de «Configuración», que se guarda en la base y por defecto permite crear. El destino por ZIP combina la raíz configurada, un nombre seguro del ZIP, el id estable del proyecto y la subcarpeta del programa. Un Job ausente se crea; uno que ya existe en esa carpeta exacta se actualiza mediante la API de Talend Studio; un homónimo de otra carpeta bloquea el lote. El portal vuelve a comprobar MCP antes de reintentar conflictos guardados o restaurar Jobs borrados. `TALEND_APPLY_FOLDER` debe estar dentro de `Process/`.

El lote se persiste en SQLite. `GET /api/projects/{id}/talend-apply-batch` devuelve `queued`, `running`, `applied`, `partially_applied`, `failed`, `conflict` o `interrupted`, además del Job actual, las advertencias de dependencias y el estado de cada programa. Si hay ciclos, el portal los informa y usa un orden estable para procesar los Jobs. Los resultados `failed`, `partially_applied` e `interrupted` permiten reintentar el mismo lote sin volver a aplicar los Jobs ya confirmados. Si el Job padre devuelve un resultado confirmado para un Job hijo, el portal lo registra y lo omite como llamada independiente. Una revisión distinta del ZIP/plan se bloquea para evitar sobrescribir el destino.

En PowerShell puedes cambiar la dirección antes de arrancar la API con `$env:TALEND_MCP_URL = "http://127.0.0.1:4927/mcp"`. `uvicorn` no carga `.env` automáticamente; `.env.example` documenta los nombres y valores recomendados.

El portal conserva las carpetas relativas que trae el ZIP en Inventario, Programas SAS y Jobs y guías. Las variables con valor conocido se envían con ese valor; las que no tienen dato quedan vacías. Cada detalle técnico no resuelto se conserva en un contexto `migration_todo_*`, con su descripción en el comentario. El MCP agrega los nodos, valores, esquemas y conexiones que la guía sí puede verificar y mantiene el resto pendiente, sin inventar filas, credenciales, esquemas ni equivalencias SAS.

## Estructura

- `src/sas_grid_migrator/` núcleo: ingestion, sas_parser, macro_resolver, semantic_analysis, grid_analysis, dependency_graph, intermediate_representation, migration_planner, talend_adapter, reporting, validation, persistence, cli.
- `apps/api` FastAPI; `apps/web` frontend React.
- `rules/` reglas versionadas (sas, talend, mappings); `schemas/` contratos JSON; `templates/` plantillas de salida.
- `tests/` fixtures SAS, unit, integration, golden.
- `docs/` arquitectura, cobertura SAS, reglas de migración, seguridad.
