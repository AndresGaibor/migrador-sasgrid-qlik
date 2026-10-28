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
uv run sgm dev                                   # MCP (preset portal) + API + UI con un solo comando (Ctrl+C detiene todo)
uv run sgm import tests/fixtures/sas -n corpus   # crea proyecto e importa el lote
uv run sgm inventory <project_id>
uv run sgm analyze <project_id>               # parseo + cobertura P0/P1/P2
uv run sgm deps <project_id>                  # dependencias, capas y tareas Grid
uv run sgm plan <project_id> [-o dir]         # planes por Job + index.md + steps.csv
uv run sgm agent migrate ./lote_sas -n clientes # importar → analizar → planear → exportar
uv run sgm agent api GET /projects             # API completa, salida JSON para agentes
uv run uvicorn apps.api.main:app --reload   # API local
```

### CLI para agentes

`sgm agent api METHOD PATH` permite invocar los endpoints de la plataforma y devuelve JSON
por stdout. Cubre las operaciones de migración de la UI (proyectos, inventario, análisis,
planes, decisiones, catálogo Talend, consulta de permisos, preflight, aplicación, verificación y exportación),
además de endpoints nuevos sin tener que ampliar la CLI. Usa `--data '{...}'` para cuerpos JSON,
`--file archivo.zip` para cargas multipart y `--server URL` o `SGM_API` si la API no está en
`http://127.0.0.1:8000`. El cambio del permiso de escritura está bloqueado en la CLI y se hace
únicamente desde Configuración.

```bash
PROJECT_ID=abc123
uv run sgm agent api GET "/projects/$PROJECT_ID/plans"
uv run sgm agent api PATCH "/projects/$PROJECT_ID/plans/programa.sas/steps/step_id" --data '{"status":"pendiente","note":"requiere cotejo en Studio"}'
uv run sgm agent api POST "/projects/$PROJECT_ID/plans/programa.sas/talend-apply/preview"
uv run sgm agent api GET "/projects/$PROJECT_ID/talend-apply-batch/preflight"
```

La escritura sigue sujeta a los controles del servidor y al permiso administrado en Configuración;
la CLI no elude esos controles. `sgm agent migrate PATH -n NOMBRE` ejecuta el flujo seguro hasta
generar planes y exportarlos, pero no crea ni ejecuta Jobs de Talend. La ruta de importación debe
ser accesible desde la máquina donde corre la API. Si una etapa falla, el proyecto queda disponible
para inspección y reintento.

## Trabajar en el repositorio

Para orientarse en el código, el flujo SAS → Talend, las reglas de negocio y las pruebas por área,
empieza por la [guía para agentes](docs/agent-guide.md). La [arquitectura](docs/architecture.md)
explica límites y modelos; la [guía de seguridad](docs/security.md) y la
[operación de proyectos ZIP](docs/zip-project-workspaces.md) describen las restricciones en tiempo
de ejecución. El archivo [AGENTS.md](AGENTS.md) contiene las reglas obligatorias para cambios y
trabajo con el subtree del MCP.

Para operar el portal con proyectos ZIP, análisis automático, reintentos y destinos aislados en Talend, consulta [la guía operativa](docs/zip-project-workspaces.md). Despliegue persistente (systemd + Tailscale Serve): ver [ops/systemd/README.md](ops/systemd/README.md).

Para revisar el alcance actual del analizador de orquestación SAS Grid, sus límites y la lista de datos que se deben confirmar en el entorno origen, consulta la [guía SAS Grid](docs/sas-grid-support.md). La documentación oficial descargada para consulta local está en `docs/reference/sas/` y no se versiona por copyright.

Frontend (`apps/web`, React + TS + Vite + Bun):

```bash
uv run sgm dev --no-mcp                           # solo API + UI, si el MCP ya corre aparte
uv run uvicorn apps.api.main:app --port 8000     # API
cd apps/web && bun install && bun run dev         # UI en :5173; SGM_API=http://127.0.0.1:8000 si la API usa otro puerto
bun test && bun run build
```

## Crear Jobs de prueba en Talend

En «Mis proyectos», **Subir ZIP y crear proyecto** registra un proyecto aislado y arranca extracción, análisis SAS, dependencias y guías. La página conserva el estado y ofrece reintento si falla. En «Plan de migración», **Implementar todos los flujos del ZIP en Talend** consulta primero el inventario completo de Studio y muestra qué Jobs se crearán, actualizarán en su carpeta destino o bloquearán el lote por conflicto. La API vuelve a comprobar el inventario antes de escribir. El botón se activa solo con inventario disponible y sin conflictos. La operación muestra avance y resultado por programa; los Jobs no se ejecutan.

Para escribir Jobs hace falta Talend Studio 8.0.1 abierto, con el proyecto cargado y el Bridge instalado. Si Studio no responde, la vista **Configuración** muestra el diagnóstico; si tiene un diálogo modal abierto, la guía no se aplica y el diálogo debe cerrarse en Studio. Los Jobs creados no se compilan ni se ejecutan automáticamente.

El portal usa estas variables de entorno. Los valores predeterminados sirven para la prueba local; cambia los valores en el entorno del proceso API si MCP usa otro puerto o carpeta:

```dotenv
TALEND_MCP_URL=http://127.0.0.1:3927/mcp
TALEND_MCP_TIMEOUT_SECONDS=60
TALEND_APPLY_FOLDER=Process/PruebasWebSAS
SGM_DATA_DIR=./data
SGM_MAX_TOTAL_BYTES=268435456
SGM_MAX_PIPELINE_CONCURRENCY=2
SGM_MAX_QUEUED_PIPELINES=20
```

En el `.env.local` de `mcp/talend-mcp`, `TALEND_MCP_HOST` y `TALEND_MCP_PORT` configuran el servidor (por defecto `127.0.0.1` y `3927`). Si cambias alguno, ajusta `TALEND_MCP_URL` para que coincida. Mantén el MCP en loopback y reinicia los dos procesos después de cambiar su configuración.

El código del MCP vive en `mcp/talend-mcp/` (subtree de [AndresGaibor/talend-mcp](https://github.com/AndresGaibor/talend-mcp)). Para levantar MCP, API y UI con la configuración correcta, usa `uv run sgm dev` (o `scripts/dev.ps1`, que lo invoca); el MCP arranca con `bun run start:server` y el preset `portal`, sin tocar el plugin de un Studio abierto. Si el puerto 3927 ya está ocupado, reutiliza ese servidor. Al subir un ZIP, el portal conserva la estructura de carpetas y muestra el estado de cada etapa. En «Plan de migración», pulsa **Implementar todos los flujos del ZIP en Talend**. La API llama secuencialmente a `talend_job_apply_custom_spec` una vez por Job que no haya sido confirmado dentro de un Job padre. El estado y los resultados se guardan por proyecto; el portal consulta el avance al recargar. Los Jobs no se ejecutan.

El permiso de escritura se administra únicamente con el interruptor de «Configuración» y se guarda en la base; por defecto permite crear. No depende de variables de entorno. El destino por ZIP combina la raíz configurada, un nombre seguro del ZIP, el id estable del proyecto y la subcarpeta del programa. Un Job ausente se crea; uno que ya existe en esa carpeta exacta se actualiza mediante la API de Talend Studio; un homónimo de otra carpeta bloquea el lote. El portal vuelve a comprobar MCP antes de reintentar conflictos guardados o restaurar Jobs borrados. `TALEND_APPLY_FOLDER` debe estar dentro de `Process/`.

El lote se persiste en SQLite. `GET /api/projects/{id}/talend-apply-batch` devuelve `queued`, `running`, `applied`, `partially_applied`, `failed`, `conflict` o `interrupted`, además del Job actual, las advertencias de dependencias y el estado de cada programa. Si hay ciclos, el portal los informa y usa un orden estable para procesar los Jobs. Los resultados `failed`, `partially_applied` e `interrupted` permiten reintentar el mismo lote sin volver a aplicar los Jobs ya confirmados. Si el Job padre devuelve un resultado confirmado para un Job hijo, el portal lo registra y lo omite como llamada independiente. Una revisión distinta del ZIP/plan se bloquea para evitar sobrescribir el destino.

En PowerShell puedes cambiar la dirección antes de arrancar la API con `$env:TALEND_MCP_URL = "http://127.0.0.1:4927/mcp"`. `uvicorn` no carga `.env` automáticamente; `.env.example` documenta los nombres y valores recomendados.

El portal conserva las carpetas relativas que trae el ZIP en Inventario, Programas SAS y Jobs y guías. Las variables con valor conocido se envían con ese valor; las que no tienen dato quedan vacías. Cada detalle técnico no resuelto se conserva en un contexto `migration_todo_*`, con su descripción en el comentario. El MCP agrega los nodos, valores, esquemas y conexiones que la guía sí puede verificar y mantiene el resto pendiente, sin inventar filas, credenciales, esquemas ni equivalencias SAS.

## Estructura

- `src/sas_grid_migrator/` núcleo: ingestion, sas_parser, macro_resolver, semantic_analysis, grid_analysis, dependency_graph, intermediate_representation, migration_planner, talend_adapter, reporting, validation, persistence, cli.
- `apps/api` FastAPI; `apps/web` frontend React.
- `rules/` reglas versionadas (sas, talend, mappings); `schemas/` contratos JSON; `templates/` plantillas de salida.
- `tests/` fixtures SAS, unit, integration, golden.
- `docs/` arquitectura, cobertura SAS, reglas de migración, seguridad.
