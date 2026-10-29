# Guía de trabajo para agentes

Esta guía es el mapa de entrada al repositorio: identifica dónde buscar antes de cambiar código,
qué reglas de negocio no se deben inferir y qué pruebas corresponden a cada tipo de cambio. Para
límites obligatorios (permisos, subtree y acciones prohibidas), prevalece [AGENTS.md](../AGENTS.md).

## Antes de empezar una tarea

1. Revisa `git status --short` y `git diff`: conserva cambios locales que no sean parte de tu tarea.
2. Lee [AGENTS.md](../AGENTS.md) y esta guía. Para la integración Talend, lee también
   [`mcp/talend-mcp/AGENTS.md`](../mcp/talend-mcp/AGENTS.md).
3. Si hay CodeGraph indexado, úsalo para encontrar símbolos y seguir el flujo antes de buscar o
   leer código a mano. Después confirma en el código actual los detalles que no estén cubiertos.
4. Sigue una llamada desde su entrada pública hasta el núcleo antes de modificarla. La API debe
   coordinar el núcleo, no duplicar lógica de dominio.
5. Ejecuta la prueba más cercana al cambio y los comandos completos indicados en
   [AGENTS.md](../AGENTS.md) cuando el alcance lo justifique.

## Mapa rápido del repositorio

| Necesidad | Código principal | Pruebas / documentación |
| --- | --- | --- |
| Importar ZIP/carpeta, inventario seguro | `src/sas_grid_migrator/ingestion/`, `persistence/store.py` | `tests/unit/test_ingestion.py`, `tests/unit/test_security.py`, `tests/integration/test_api_zip_projects.py`; [`security.md`](security.md), [`zip-project-workspaces.md`](zip-project-workspaces.md) |
| Parsear SAS y analizar construcciones | `src/sas_grid_migrator/sas_parser/`, `macro_resolver/`, `semantic_analysis/` | `tests/unit/test_parser.py`, `tests/unit/test_golden.py`; [`sas-coverage.md`](sas-coverage.md) |
| Dependencias SAS y planificación Grid | `src/sas_grid_migrator/dependency_graph/`, `grid_analysis/` | `tests/unit/test_dependencies.py`; [`architecture.md`](architecture.md) |
| Modelo intermedio y guías por Job | `src/sas_grid_migrator/intermediate_representation/`, `migration_planner/`, `rules/` | `tests/unit/test_planner.py`, `tests/unit/test_talend_eligibility.py`; [`migration-rules.md`](migration-rules.md), [`equivalence-testing.md`](equivalence-testing.md) |
| API y persistencia de estados | `apps/api/`, `src/sas_grid_migrator/persistence/store.py` | `tests/integration/test_api_*.py`, `tests/unit/test_store_*.py`; OpenAPI local en `/docs` |
| Ediciones humanas sobre el plan, nombres de Job y progreso | `src/sas_grid_migrator/migration_planner/service.py` (`_apply_edits`), `job_naming.py`, `progress.py`; rutas en `apps/api/main.py` | `tests/unit/test_plan_edits.py`, `test_job_naming.py`, `test_progress.py`, `test_store_overrides.py`; `tests/integration/test_api_plan_edits.py`, `test_api_progress.py`; receta «Ediciones humanas sobre el plan» |
| CLI y desarrollo local | `src/sas_grid_migrator/cli/` | `tests/integration/test_cli_pipeline.py`, `tests/unit/test_cli_agent.py` |
| UI, pestañas y llamadas API | `apps/web/src/`, `apps/web/src/api.ts` | pruebas junto al componente en `apps/web/src/**/*.test.*` |
| Catálogo, política y adaptador Talend | `src/sas_grid_migrator/talend_adapter/`, `rules/talend/`, `rules/mappings/` | `tests/unit/test_talend_*.py`, `tests/integration/test_mcp_contract.py`; [`talend-mcp-tools.md`](talend-mcp-tools.md) |
| Tools/Bridge Talend MCP | `mcp/talend-mcp/` | leer primero `mcp/talend-mcp/AGENTS.md`; pruebas dentro de `mcp/talend-mcp/tests/` |

Los nombres de carpetas pueden cambiar. El código, las reglas y las pruebas son la fuente de
verdad; no copies una descripción histórica sin verificarla.

## Cómo funciona una migración

El flujo normal es:

```text
fuente SAS
  → importación validada y manifiesto con rutas/hash/codificación
  → parser SAS y resolución estática de macros/includes
  → análisis semántico y evidencia archivo/línea
  → dependencias de programas/datasets + tareas Grid inferidas
  → IR tipada + reglas versionadas
  → un plan conservador por programa/Job
  → revisión humana y, si se autoriza, aplicación controlada vía MCP/Studio
  → verificación de lectura en Studio + validación de equivalencia por desarrollador
```

El ZIP subido por UI/API crea un proyecto aislado y encola análisis, dependencias y planes en
segundo plano; consulta `GET /api/projects/{id}/processing` antes de asumir que terminó. En cambio,
la CLI local `sgm import`, `sgm analyze`, `sgm deps` y `sgm plan` ejecuta las etapas directamente.
`sgm agent migrate RUTA -n NOMBRE` usa la API y devuelve el resultado JSON del pipeline hasta la
exportación.

El análisis no ejecuta SAS, macros ni archivos importados. El sistema no convierte SAS
directamente a `.item`: propone una guía/plan con evidencia. Una prioridad P0/P1/P2, una sugerencia
de componente o una respuesta generada no equivale por sí sola a verificación en Studio ni a
equivalencia funcional.

## Contratos y vocabulario que importan

- **Evidencia**: una afirmación derivada debe conservar fuente SAS, ruta/línea cuando exista y su
  nivel de confianza. No inventes tipos, columnas, credenciales, valores, schemas ni componentes.
- **Candidato y verificado no son sinónimos**: los nombres de componentes/reglas pueden ser
  candidatos; `verified` exige la evidencia definida por el código y el contrato actual.
- **Desconocido significa pendiente**: conserva la duda en el plan/contexto `migration_todo_*`, no
  rellenes un valor plausible.
- **Grid no es flujo de filas**: dependencias entre ejecuciones son orquestación; no las conviertas
  en conexiones de datos Talend.
- **Decisiones humanas**: las notas/estados por paso se persisten; al regenerar planes deben
  conservarse según el contrato actual. Reimportar puede invalidar o borrar estado derivado: revisa
  `Store.import_batch` y sus pruebas antes de tocar ese comportamiento.
- **Versión de reglas**: cambios en `rules/` pueden cambiar la interpretación de planes. Mantén
  fixtures/golden y pruebas de contrato sincronizados.

Consulta [`migration-rules.md`](migration-rules.md), el schema de salida y los modelos del código
antes de agregar estados o campos. No definas vocabulario paralelo en UI/API/CLI.

## API y automatización

La API FastAPI es la frontera pública de la plataforma. En desarrollo, `uv run sgm dev` inicia MCP,
API y UI; `uv run uvicorn apps.api.main:app --reload` inicia solo la API. FastAPI publica Swagger
en `http://127.0.0.1:8000/docs` y el contrato OpenAPI en `/openapi.json`; consúltalos para el
detalle vigente de rutas, métodos, request y response.
La API no tiene autenticación: para desarrollo escucha en `127.0.0.1`; no la publiques en una
interfaz de red ni la expongas directamente a Internet. Consulta [`security.md`](security.md) antes
de cambiar el despliegue o los límites de importación.

La UI centraliza sus llamadas en `apps/web/src/api.ts`; el agente puede invocar directamente las
rutas actuales de migración:

```bash
uv run sgm agent api GET /projects
uv run sgm agent api GET /projects/ID/plans
uv run sgm agent api GET /projects/ID/talend-apply-batch/preflight
```

El preflight es de solo lectura. Para cuerpos usa `--data '{...}'` y
para cargas multipart `--file RUTA`; `--server URL` o `SGM_API` selecciona la API. En Windows
PowerShell, adapta las comillas al shell. La ruta de importación local debe existir también en la
máquina del servidor API; para una máquina remota, sube el archivo con el endpoint multipart.
La CLI bloquea deliberadamente la mutación de `/integrations/talend/permissions`: ese permiso solo
se cambia desde Configuración. No marques un paso `verificado` o `validado_manualmente` sin la
evidencia requerida; el texto de la decisión no sustituye la revisión en Studio ni una prueba de
equivalencia.

Al cambiar una llamada de UI, revisa en conjunto: ruta FastAPI, modelo/serialización, wrapper y
tipos de `apps/web/src/api.ts`, estados de carga/error y prueba de la vista. No dupliques reglas de
negocio dentro del componente React.

## Aplicación en Talend: pasos y límites

Antes de un lote, usa el preflight/resumen vigente y comprueba el destino, conflictos, proyecto
abierto y salud MCP/Bridge; el servidor vuelve a revisar el inventario antes de la primera escritura.
Para aplicar un Job individual, respeta los errores de conflicto/revisión de la API y MCP. Una
preview antigua no es autorización para escribir. El permiso se cambia únicamente en Configuración
y se conserva en SQLite; no lo habilites mediante variables de entorno ni llames su endpoint de
actualización desde CLI/agentes.

La integración aplica una especificación estructurada por MCP. El portal no ejecuta, compila ni
publica los Jobs. La verificación posterior lee lo que Studio guardó; no es una prueba de
equivalencia. Un Job debe validarse con datos de prueba según [`equivalence-testing.md`](equivalence-testing.md).

Para investigar una escritura, sigue la cadena:

```text
apps/web/src/api.ts → apps/api/main.py → talend_adapter/adapter.py
  → MCP preset/contract → Talend Studio Bridge
```

Para agregar una tool nueva usada por el portal, actualiza juntos `contract/portal-tools.json`, el
preset `portal` en `mcp/talend-mcp/src/server/registered-tools/preset-sets.ts` y
`tests/integration/test_mcp_contract.py`. No edites manualmente la allowlist derivada del contrato.

## Recetas de cambio

### Nueva construcción SAS o ajuste del análisis

1. Añade/corrige la regla versionada bajo `rules/sas/` o el módulo parser/analizador responsable.
2. Añade una fixture pequeña con caso esperado; usa golden si afecta la salida completa.
3. Revisa `tests/unit/test_parser.py`, `test_golden.py` y/o `test_dependencies.py` según la capa.
4. Comprueba que la evidencia conserva ruta y línea, y que los constructos dinámicos siguen siendo
   explícitamente desconocidos.

### Nueva correspondencia o propiedad Talend

1. Busca primero en `rules/mappings/`, `rules/talend/` y el catálogo que carga
   `src/sas_grid_migrator/talend_adapter/catalog.py`.
2. Distingue catálogo disponible, propiedad presente y verificación observada en Studio.
3. Actualiza pruebas de elegibilidad/spec/payload/contrato y la documentación del componente si
   corresponde. No uses documentación local ignorada por Git como única fuente reproducible.

### Nueva ruta, acción de UI o estado persistido

1. Define el contrato HTTP/modelo antes de implementarlo; usa los errores/status existentes.
2. Mantén lógica de dominio en `src/sas_grid_migrator/`; API y UI deben delegar.
3. Añade prueba de integración API y de UI/CLI en su frontera pública; para SQLite, prueba también
   lectura, persistencia y migración de esquema si aplica.
4. Actualiza este mapa/README cuando cambie el flujo, el permiso, los comandos o los límites.

### Ediciones humanas sobre el plan

Nombre del Job, descripción y traducción Talend de una expresión son ediciones del usuario. Se guardan en SQLite y se
superponen al plan al leerlo; no se escriben en `plans.json`:

| Tabla | Clave | Contenido |
| ----- | ----- | --------- |
| `job_overrides` | `project_id`, `program` | `job_name`, `description` |
| `expression_overrides` | `project_id`, `program`, `step_id`, `idx` | `sas` (texto SAS al editar), `talend` |
| `portal_settings` | `key` | ajustes del portal; hoy `job_name_template` |

Reglas:

- `load_plans(store, id)` y `get_plan(...)` superponen las ediciones por defecto. Con `with_edits=False` no se aplican
  las ediciones de nombre, descripción ni expresión, pero la superposición de decisiones de paso (estado y notas de
  `step_state`) se hace siempre al leer.
- `plans.json` nunca lleva ediciones de nombre, descripción ni expresión: `generate_plans` lo escribe en crudo. Las
  decisiones de paso sí se superponen al leer y `verify_project_plans` las vuelve a grabar; por eso, si escribes un plan
  de vuelta a disco, cárgalo con `with_edits=False` (así lo hace `verify_project_plans`) para no grabar las ediciones.
- Una expresión editada solo cambia `talend` y `talend_edited`; `requires_semantic_validation` se conserva. La edición
  se aplica únicamente si el texto SAS guardado sigue igual al del paso.
- Un nombre que choca con el de otro Job (generado o ya aceptado) se ignora y queda en `JobPlan.rename_ignored`.
- Las escrituras de edición responden 409 mientras hay un lote o una operación Talend activa en el proyecto
  (`Store.has_active_talend_work`).
- La plantilla de nombres (`{proyecto}`, `{carpeta}`, `{programa}`) se aplica al generar guías; un nombre editado a mano
  no cambia.

Las rutas viven en `apps/api/main.py`: `PATCH .../plans/{program}/meta`, `POST .../plans/rename-preview`,
`POST .../plans/rename`, `PATCH .../steps/{step_id}/expressions/{index}`, `POST /api/translator/translate` y
`GET|PATCH /api/settings/naming`, `GET /api/settings/naming/example`, `GET /api/projects/{id}/progress` y
`GET /api/projects/{id}/pending-summary` (lógica de progreso en `migration_planner/progress.py`). `apps/api/plans.py` y
`projects.py` no están montados en ninguna aplicación; no añadas rutas ahí.

Reglas de nombre de Job (`migration_planner/job_naming.py`): identificador que cumple `^[A-Za-z_][A-Za-z0-9_]*$`, como
máximo 60 caracteres y único sin distinguir mayúsculas. La plantilla debe incluir `{programa}`; los únicos tokens
permitidos son `{proyecto}`, `{carpeta}` y `{programa}`.

## Pruebas y comandos

```bash
uv sync
uv run pytest
uv run ruff check src tests
cd apps/web && bun install && bun test && bun run typecheck
cd mcp/talend-mcp && bun install && bun test && bun run typecheck
```

Pruebas focalizadas:

```bash
uv run pytest tests/unit/test_parser.py -q
uv run pytest tests/integration/test_api_talend_batch.py -q
uv run pytest tests/integration/test_cli_pipeline.py tests/unit/test_cli_agent.py -q
```

No instales el Bridge automáticamente como parte de las pruebas. Las pruebas Python/MCP deben ser
reproducibles sin Studio; las que requieren Studio son explícitamente smoke/L5 y deben respetar la
sesión abierta del usuario.

## Documentación relacionada

- [Arquitectura y límites](architecture.md)
- [Seguridad](security.md)
- [Cobertura SAS](sas-coverage.md)
- [Reglas y contrato del plan](migration-rules.md)
- [Operación de proyectos ZIP y lotes Talend](zip-project-workspaces.md)
- [Contrato de tools MCP](talend-mcp-tools.md)
- [Equivalencia SAS/Talend](equivalence-testing.md)
- [Flujo del subtree MCP](mcp-subtree.md)
