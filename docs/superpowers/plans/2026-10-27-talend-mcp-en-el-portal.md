# Talend MCP dentro del portal e integración verificable — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Traer `talend-mcp` al repositorio del portal sin perder su independencia pública, y hacer que el contrato portal↔MCP (tools, schemas, versión del cliente) se verifique automáticamente en vez de depender de parches locales.

**Architecture:** El MCP entra por `git subtree` (squash) en `mcp/talend-mcp/`; `AndresGaibor/talend-mcp` sigue siendo el upstream público y los cambios de ese código se empujan de vuelta con `git subtree push`. Un manifiesto `contract/portal-tools.json` es la fuente única de las tools que el portal necesita; `policy.py` lo lee, un preset `portal` del MCP las publica y una prueba de contrato arranca el MCP real y compara. El health del portal usa el mismo manifiesto para explicar qué falta y cómo arreglarlo. Además se mide el modo offline del MCP (escritura directa de `.item`, milisegundos por Job y sin Studio) y, si cumple los criterios, se añade como motor opcional `engine: "auto"` que usa offline salvo cuando la guía necesita `mapper`, `tables` o `childJobs`.

**Tech Stack:** Python 3.12 (FastAPI, `mcp` 2.x, pytest, uv), Bun/TypeScript (talend-mcp), React/TypeScript (`apps/web`), Git subtree, GitHub Actions.

**Spec:** Esta conversación (diagnóstico en la sección «Contexto»); contrato previo en `mcp/talend-mcp/docs/superpowers/specs/2026-10-21-integracion-portal-talend-mcp-design.md` (existe tras la Tarea 3). Antecesor: `docs/superpowers/plans/2026-10-27-mcp-portal-realignment.md` (alinea el checkout del MCP; este plan lo reemplaza como mecanismo de alineación).

## Contexto

Hallazgos verificados en el código el 2026-10-27:

1. `origin/main` de `talend-mcp` ya incluye `talend_job_apply_custom_spec` en `PRESET_AGENT`, pero **10 tools de lectura de la allowlist del portal siguen fuera**: `talend_inspect_component`, `talend_inspect_job`, `talend_job_info`, `talend_job_problems`, `talend_list_components`, `talend_preview_component_parameter`, `talend_preview_schema_column`, `talend_repo_sources`, `talend_repo_status`, `talend_analyze_tdboutput`. `inspect_job` y `job_problems` alimentan «Volver a comprobar pasos en Studio».
2. El README del portal manda arrancar el MCP con `bun run start:server` (sin filtro: publica todo) mientras que `bun run start` aplica `agent` por defecto. Dos caminos oficiales, dos catálogos distintos.
3. `pyproject.toml` declara `mcp>=1.0` pero el código usa `from mcp import Client` con `read_timeout_seconds` (API 2.x; `uv.lock` fija 2.3.0). Con `pip install` se obtiene 1.x y falla con `ImportError`.
4. Quedan 3 archivos sin resolver en el índice (`README.md`, `apps/web/src/views/PlansTab.tsx`, `docs/zip-project-workspaces.md`).
5. `apps/api/integrations.py` define `talend_health` y otras rutas que no están montadas (`main.py` no hace `include_router`); solo se importan algunas funciones sueltas.
6. No existe CI en el portal (`.github/` no existe).
7. `talend_job_apply_custom_spec` no depende de `unsafeActions` en el lado TypeScript; el lado Java del Bridge no se revisó (Tarea 10 lo comprueba con Studio).
8. El MCP tiene un modo offline (`talend_jobs_create_from_spec`, `talend_jobs_create_batch`, `talend_job_edit_offline`) que escribe `.item`/`.properties` sin Studio: ~1 ms por Job frente a 3,6–5,6 s con la API de Studio (cifras del propio MCP). El editor offline **no soporta** `mapper` (tMap), `tables`, `childJobs` ni `replaceManagedTodoContexts`, y no reconoce la marca de propiedad `[portal-spec:<hash>]`. El portal envía `mapper` en ~45 puntos de `apply_spec.py` y `tables` en ~9. Comparación completa en `docs/talend-mcp-offline-evaluation.md`.
9. `instructions` solo participa en el hash de propiedad del Job (`ownership()` en `apply-custom-job-spec.ts`); cualquier motor nuevo debe incluirla en el hash aunque no la use.
10. El directorio `examples/` del MCP solo trae un perfil de tarea (`olist_raw.context.json`); los ejemplos de especificaciones están en `tests/talend/job-batch.test.ts`, `tests/talend/custom-job-spec.test.ts` y `tests/tools/custom-spec-executor.test.ts`.

## Global Constraints

- `talend-mcp` es público: nada del portal (datos de clientes, rutas locales, código SAS) entra en `mcp/talend-mcp/`.
- No ejecutar, compilar ni publicar Jobs migrados en ninguna prueba; el smoke test de la Tarea 10 solo crea y lee. La única compilación permitida es la de la Tarea 7 (`talend_job_build_batch`) sobre Jobs de prueba en una carpeta aparte, para comprobar que el `.item` offline es válido.
- El motor `studio` sigue siendo el predeterminado hasta que la Tarea 7 cumpla sus criterios de aceptación; ningún cambio de la Tarea 8 altera el comportamiento de `engine: "studio"`.
- Un Job creado por un motor debe poder reanudarse con el otro: ambos escriben y comparan la misma marca `[portal-spec:<hash>]` calculada sobre la especificación **sin** el campo `engine`.
- No recargar el Bridge (`bun run bridge:install`) con Jobs o diálogos en curso en Studio.
- El permiso de escritura lo decide únicamente la vista Configuración (persistido en la base), nunca una variable de entorno.
- `TALEND_APPLY_FOLDER` permanece bajo `Process/`.
- Cada tarea termina con la suite relacionada en verde y un commit propio; no mezclar el subtree con otros cambios.
- Windows 11 como plataforma principal; usar `core.longpaths=true` para el subtree (`addons/` tiene rutas profundas).

## Review Focus

- MCP arrancado con `bun run start:server` (sin filtro) o con `agent`: el health debe nombrar las tools que faltan y el comando exacto, no «servidor desactualizado».
- `mcp` 1.x instalado: el error debe decir qué versión se necesita, no `ImportError` ni `no disponible`.
- Manifiesto con una tool inexistente en el MCP (renombrada upstream): la prueba de contrato debe fallar por nombre, no el usuario en producción.
- Bun no instalado en una máquina que corre `pytest`: la prueba de contrato se salta con motivo explícito, no falla ni cuelga.
- `git subtree pull` con cambios locales en `mcp/talend-mcp/`: el procedimiento documentado no debe perder commits (se usa siempre desde un árbol limpio).
- Guía con `mapper` o `tables` y `engine: "auto"`: debe ir por Studio sin error; con `engine: "offline"` forzado debe rechazarse con `OFFLINE_UNSUPPORTED` nombrando los componentes, sin escribir nada.
- Job abierto en un editor de Studio mientras se aplica en modo offline: debe rechazarse con `JOB_OPEN_IN_STUDIO` y el portal debe mostrar el mensaje, no un 500 ni una escritura silenciosa.
- Job creado offline y reaplicado por Studio (y al revés) con la misma guía: se reanuda sin `CONFLICT`; con una guía distinta, `CONFLICT` sin sobrescribir.

---

## Mapa de archivos

| Archivo | Responsabilidad |
|---|---|
| `contract/portal-tools.json` (nuevo) | Tools de lectura, tool de escritura y campos obligatorios del `inputSchema`. Fuente única del lado portal. |
| `src/sas_grid_migrator/talend_adapter/contract.py` (nuevo) | Carga el manifiesto: `PortalContract`, `load_contract()`. |
| `src/sas_grid_migrator/talend_adapter/policy.py` | `READ_TOOLS`/`WRITE_TOOLS` derivados del contrato. |
| `src/sas_grid_migrator/talend_adapter/adapter.py` | `McpCaller` (error de versión) y `custom_spec_status` (`missing_tools`, `diagnosis`, `fix_hint`). |
| `mcp/talend-mcp/src/server/registered-tools/preset-sets.ts` | Nuevo `PRESET_PORTAL`. |
| `mcp/talend-mcp/src/server/registered-tools/presets.ts` | Regla `portal` en `PRESET_RULES`. |
| `tests/integration/test_mcp_contract.py` (nuevo) | Arranca el MCP real con preset `portal` y compara con el manifiesto. |
| `apps/web/src/views/SettingsView.tsx` | Muestra `diagnosis` y `fix_hint`. |
| `src/sas_grid_migrator/talend_adapter/eligibility.py` (nuevo) | `offline_blockers(spec)`: por qué una especificación no puede ir por el motor offline. |
| `tools/offline_eligibility.py` (nuevo) | Mide cuántas guías de un ZIP son elegibles para offline y compara motores. |
| `docs/talend-mcp-offline-evaluation.md` | Comparación Studio/offline y resultados de la medición. |
| `mcp/talend-mcp/src/talend/studio/apply-custom-job-spec-offline.ts` (nuevo, condicional a Tarea 7) | Motor offline de `talend_job_apply_custom_spec`. |
| `mcp/talend-mcp/src/talend/studio/custom-job-spec.ts` | Campo opcional `engine` y función `ownership()` compartida. |
| `scripts/dev.ps1` (nuevo) | Levanta MCP + API + web con la configuración correcta. |
| `AGENTS.md` (nuevo) | Mapa para agentes: qué es de cada lado, contrato, cómo probar, cómo sincronizar el subtree. |
| `.github/workflows/ci.yml` (nuevo) | pytest, bun test del portal y del MCP importado. |

---

### Task 1: Dejar el repositorio limpio

**Files:**
- Modify: índice de git para `README.md`, `apps/web/src/views/PlansTab.tsx`, `docs/zip-project-workspaces.md`.

**Interfaces:**
- Produces: árbol de trabajo sin rutas `UU`; requisito de `git subtree add` en la Tarea 3.

- [ ] **Step 1: Confirmar que no hay marcadores de conflicto**

Run: `git grep -n "^<<<<<<<\|^>>>>>>>" -- README.md apps/web/src/views/PlansTab.tsx docs/zip-project-workspaces.md`
Expected: sin salida (ya se comprobó que los archivos de trabajo no tienen marcadores).

- [ ] **Step 2: Revisar el contenido final de cada uno de los 3 archivos con `git diff` contra `HEAD`**

Verificar que el texto conserva ambos lados esperados (cambios del trabajo staged y de `3435b72`). Si falta algo, restaurarlo a mano antes del siguiente paso.

- [ ] **Step 3: Marcar como resueltos**

Run: `git add README.md apps/web/src/views/PlansTab.tsx docs/zip-project-workspaces.md && git status --short | grep "^UU"`
Expected: sin salida.

- [ ] **Step 4: Verificar que nada se rompió**

Run: `uv run pytest tests/unit/test_talend_adapter.py tests/unit/test_talend_apply_spec.py tests/integration/test_api_talend_batch.py -q` y `cd apps/web && bun test`
Expected: todo pasa (100 pruebas Python al 2026-10-27).

- [ ] **Step 5: Commit**

```bash
git commit -m "chore: resolver merge pendiente y consolidar cambios de integración MCP"
```

---

### Task 2: Requisito `mcp>=2.3` y error de cliente claro

**Files:**
- Modify: `pyproject.toml:13`
- Modify: `src/sas_grid_migrator/talend_adapter/adapter.py` (`McpCaller.call`, `list_tools`, `describe_tool`)
- Test: `tests/unit/test_mcp_requirement.py` (nuevo), `tests/unit/test_talend_adapter.py`

**Interfaces:**
- Produces: `class McpClientUnavailable(TalendError)` en `adapter.py`; mensaje exacto `"Falta el cliente MCP 2.x: ejecuta «uv sync» (mcp>=2.3)"`.

- [ ] **Step 1: Escribir las pruebas que fallan**

`test_mcp_requirement.py::test_pyproject_requires_mcp_2` lee `pyproject.toml` con `tomllib` y afirma que la dependencia `mcp` empieza por `mcp>=2`. En `test_talend_adapter.py`, `test_mcp_caller_reports_client_version_when_import_fails` hace que `monkeypatch.setitem(sys.modules, "mcp", None)` y afirma que `run(McpCaller("http://x/mcp").list_tools())` lanza `TalendError` con `match="uv sync"`.

- [ ] **Step 2: Ejecutar y comprobar que fallan**

Run: `uv run pytest tests/unit/test_mcp_requirement.py tests/unit/test_talend_adapter.py -k "requires_mcp or client_version" -v`
Expected: FAIL (`mcp>=1.0` y mensaje actual `talend-mcp no disponible: ImportError`).

- [ ] **Step 3: Implementar**

Cambiar la dependencia a `"mcp>=2.3"`. En `adapter.py` añadir `McpClientUnavailable` y un helper `_import_client()` que traduzca `ImportError`/`AttributeError` de `from mcp import Client` a esa excepción; usarlo en los tres métodos que hoy hacen `from mcp import Client`.

- [ ] **Step 4: Ejecutar y comprobar que pasan**

Run: `uv lock --check && uv run pytest tests/unit/test_mcp_requirement.py tests/unit/test_talend_adapter.py -q`
Expected: PASS y `uv.lock` coherente (ya fija 2.3.0).

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml uv.lock src/sas_grid_migrator/talend_adapter/adapter.py tests/unit/test_mcp_requirement.py tests/unit/test_talend_adapter.py
git commit -m "fix: exigir mcp>=2.3 y explicar la versión del cliente cuando falla"
```

---

### Task 3: Importar `talend-mcp` con git subtree

**Files:**
- Create: `mcp/talend-mcp/**` (vía subtree)
- Modify: `.gitignore`, `README.md` (sección de arranque del MCP)

**Interfaces:**
- Produces: código del MCP en `mcp/talend-mcp/` con la historia comprimida en un commit; remoto de trabajo `talend-mcp-upstream`.

- [ ] **Step 1: Preparar**

Run: `git config core.longpaths true && git remote add talend-mcp-upstream https://github.com/AndresGaibor/talend-mcp.git && git fetch talend-mcp-upstream main`
Expected: `origin/main` del MCP descargado (commit `6c7e391` o posterior).

- [ ] **Step 2: Importar**

Run: `git subtree add --prefix=mcp/talend-mcp talend-mcp-upstream main --squash`
Expected: commit de merge creado; `mcp/talend-mcp/package.json` existe. Requiere árbol limpio (Tarea 1).

- [ ] **Step 3: Verificar que el MCP funciona desde su nueva ubicación**

Run: `cd mcp/talend-mcp && bun install && bun run typecheck && bun test tests/tools/tool-presets.test.ts`
Expected: typecheck sin errores y prueba de presets en verde.

- [ ] **Step 4: Ignorar lo local y apuntar el README**

Añadir a `.gitignore`: `mcp/talend-mcp/workspace/`, `mcp/talend-mcp/docs/media/video/out/`. En el README del portal, reemplazar «Arranca el MCP con `bun run start:server`» por una referencia a `scripts/dev.ps1` (Tarea 9) y explicar que el MCP vive en `mcp/talend-mcp/`.

- [ ] **Step 5: Commit**

```bash
git add .gitignore README.md
git commit -m "docs: ubicación del MCP dentro del portal"
```

---

### Task 4: Manifiesto de contrato y política derivada

**Files:**
- Create: `contract/portal-tools.json`, `src/sas_grid_migrator/talend_adapter/contract.py`
- Modify: `src/sas_grid_migrator/talend_adapter/policy.py`, `src/sas_grid_migrator/talend_adapter/adapter.py` (lista de campos obligatorios de `custom_spec_status`)
- Test: `tests/unit/test_talend_contract.py` (nuevo)

**Interfaces:**
- Produces: `PortalContract` (dataclass congelada) con `read_tools: frozenset[str]`, `write_tool: str`, `required_top_fields: frozenset[str]`, `required_component_fields: frozenset[str]`; `load_contract() -> PortalContract` (cacheada).
- Consumes: nada de tareas anteriores salvo la estructura de `mcp/`.

- [ ] **Step 1: Escribir las pruebas que fallan**

`test_contract_matches_policy`: `load_contract().read_tools == policy.READ_TOOLS` y `{load_contract().write_tool} == policy.WRITE_TOOLS`.
`test_manifest_covers_every_tool_the_portal_calls`: recorre `src/` y `apps/api/` con regex `"(talend_[a-z_]+)"` y afirma que cada nombre usado en una llamada `_data("...")`/`caller.call("...")` está en el contrato.
`test_required_fields_are_those_checked_by_health`: `required_top_fields == {"childJobs","instructions","replaceManagedTodoContexts"}` y `required_component_fields == {"draftOnly","draftReason","tables"}`.

- [ ] **Step 2: Ejecutar y comprobar que fallan**

Run: `uv run pytest tests/unit/test_talend_contract.py -v`
Expected: FAIL (`contract.py` no existe).

- [ ] **Step 3: Implementar**

`portal-tools.json` con las 22 tools de lectura actuales de `READ_TOOLS`, `write_tool` y los dos grupos de campos. `contract.py` carga el JSON desde `Path(__file__).resolve().parents[3] / "contract" / "portal-tools.json"`. `policy.py` pasa a derivar `READ_TOOLS`/`WRITE_TOOLS` de `load_contract()`. `custom_spec_status` usa los conjuntos del contrato en lugar de literales. Revisar los 5 nombres del portal que el MCP no registra (`talend_apply_batches`, `talend_apply_operations`, `talend_jobs_untouched`, `talend_type`, `talend_unique_name`): si son datos de prueba, dejarlos fuera del contrato; si son llamadas reales, quitar la llamada.

- [ ] **Step 4: Ejecutar y comprobar que pasan**

Run: `uv run pytest tests/unit -q`
Expected: PASS, sin regresiones en `test_policy_and_fixtures.py`.

- [ ] **Step 5: Commit**

```bash
git add contract src/sas_grid_migrator/talend_adapter tests/unit/test_talend_contract.py
git commit -m "feat: manifiesto único de tools del portal y política derivada"
```

---

### Task 5: Preset `portal` en el MCP

**Files:**
- Modify: `mcp/talend-mcp/src/server/registered-tools/preset-sets.ts`, `mcp/talend-mcp/src/server/registered-tools/presets.ts`, comentario de cabecera de presets.
- Test: `mcp/talend-mcp/tests/tools/tool-presets.test.ts`

**Interfaces:**
- Produces: `export const PRESET_PORTAL: Set<string>` = `PRESET_AGENT` ∪ las 10 tools de lectura listadas en «Contexto»; preset `portal` en `PRESET_RULES`. `PRESET_AGENT` no cambia (la decisión de ocultar `talend_job_problems` es deliberada).

- [ ] **Step 1: Escribir la prueba que falla**

En `tool-presets.test.ts`: `portal preset publishes every tool the portal needs` — con `applyFilter(allTools, "portal")` afirma que contiene `talend_job_apply_custom_spec`, `talend_inspect_job`, `talend_job_problems`, `talend_job_info` y los otros 7, y que `agent` sigue **sin** contener `talend_job_problems`. `knownPresets()` incluye `"portal"`.

- [ ] **Step 2: Ejecutar y comprobar que falla**

Run: `cd mcp/talend-mcp && bun test tests/tools/tool-presets.test.ts`
Expected: FAIL (preset desconocido).

- [ ] **Step 3: Implementar**

Definir `PRESET_PORTAL` y la regla `portal: (name) => PRESET_PORTAL.has(name)`; documentar el preset en la cabecera de `preset-sets.ts` y en `docs/` donde se listan presets (`bun run docs:tools` si el catálogo lo requiere).

- [ ] **Step 4: Ejecutar y comprobar que pasa**

Run: `cd mcp/talend-mcp && bun run typecheck && bun test tests/tools tests/scripts`
Expected: PASS (incluye `mapa.test.ts`, que cuenta tools por preset).

- [ ] **Step 5: Commit**

```bash
git add mcp/talend-mcp
git commit -m "feat(mcp): preset portal con las tools que usa el migrador"
```

---

### Task 6: Prueba de contrato contra el MCP real

**Files:**
- Create: `tests/integration/test_mcp_contract.py`

**Interfaces:**
- Consumes: `load_contract()` (Tarea 4), preset `portal` (Tarea 5), `McpCaller.list_tools()`.

- [ ] **Step 1: Escribir la prueba**

Fixture de módulo `mcp_server`: salta con `pytest.skip("bun no está instalado")` si `shutil.which("bun")` es `None`; crea un directorio temporal con un `talend.project` mínimo, elige un puerto libre, arranca `bun run index.ts` en `mcp/talend-mcp` con `TALEND_MCP_FILTER=portal`, `TALEND_MCP_PORT`, `TALEND_PROJECT`, espera `/healthz` (timeout 30 s) y lo termina al final.
`test_published_tools_cover_the_contract`: `names = {t["name"] for t in run(McpCaller(url).list_tools())}`; afirma `contract.read_tools | {contract.write_tool} <= names` con mensaje que lista las faltantes.
`test_write_tool_schema_has_required_fields`: comprueba `required_top_fields` en `properties` y `required_component_fields` en `components.items.properties` del `inputSchema`.
`test_agent_preset_alone_is_reported_incomplete`: arranca con `agent` y comprueba que `custom_spec_status()` devuelve `missing_tools` no vacío (se completa tras la Tarea 9; marcar `xfail` hasta entonces).

- [ ] **Step 2: Ejecutar**

Run: `uv run pytest tests/integration/test_mcp_contract.py -v`
Expected: PASS si hay Bun; SKIPPED con motivo si no. Verificar a mano que cambiar un nombre en `contract/portal-tools.json` hace fallar el primer test nombrando la tool.

- [ ] **Step 3: Commit**

```bash
git add tests/integration/test_mcp_contract.py
git commit -m "test: contrato portal↔MCP contra el servidor real"
```

---

### Task 7: Medir el modo offline frente a Studio (spike con decisión)

Esta tarea no cambia comportamiento del portal ni del MCP; produce datos y una decisión escrita. Requiere Studio abierto con el Bridge y un proyecto Talend de prueba (no el de producción).

**Files:**
- Create: `src/sas_grid_migrator/talend_adapter/eligibility.py`, `tools/offline_eligibility.py`
- Modify: `docs/talend-mcp-offline-evaluation.md` (tabla de resultados y decisión)
- Test: `tests/unit/test_talend_eligibility.py` (nuevo)

**Interfaces:**
- Produces: `offline_blockers(spec: dict[str, Any]) -> list[str]` — vacío si la especificación puede ir por offline; si no, una cadena por bloqueo con el formato `"mapper:<uniqueName>"`, `"tables:<uniqueName>"` o `"childJobs"`. Recorre `childJobs` solo para informar el bloqueo, no recursivamente.
- Consumes: `build_apply_spec(plan, ...)` de `apply_spec.py` y los ZIP de `tests/fixtures/sas`.

- [ ] **Step 1: Escribir las pruebas que fallan**

`test_spec_without_mapper_or_tables_is_eligible`: una especificación con `tFileInputDelimited` y `tFilterRow` devuelve `[]`.
`test_mapper_blocks_offline`: un componente `tMap_1` con clave `mapper` devuelve `["mapper:tMap_1"]`.
`test_tables_blocks_offline`: un componente con `tables` no vacío devuelve `["tables:<uniqueName>"]`; `tables: {}` no bloquea.
`test_child_jobs_block_offline`: `childJobs` no vacío devuelve `["childJobs"]`.

- [ ] **Step 2: Ejecutar y comprobar que fallan**

Run: `uv run pytest tests/unit/test_talend_eligibility.py -v`
Expected: FAIL (el módulo no existe).

- [ ] **Step 3: Implementar `offline_blockers` y el script de medición**

El script `tools/offline_eligibility.py <zip-o-carpeta>` importa el ZIP con `Store`, construye la especificación de cada guía con `build_apply_spec` e imprime: total de guías, elegibles, y el conteo de bloqueos por tipo. Solo lee; no llama al MCP.

- [ ] **Step 4: Ejecutar y comprobar que pasan**

Run: `uv run pytest tests/unit/test_talend_eligibility.py -q`
Expected: PASS.

- [ ] **Step 5: Medir elegibilidad con ZIP reales**

Run: `uv run python tools/offline_eligibility.py <zip de prueba 1> <zip 2> <zip 3>`
Expected: tabla de elegibilidad por ZIP. Copiarla a `docs/talend-mcp-offline-evaluation.md`.

- [ ] **Step 6: Medir tiempo y paridad con el MCP real**

Con el MCP corriendo con preset `portal` y la carpeta `Process/PruebasOffline` (aparte de `PruebasWebSAS`): para 20 guías elegibles, (a) aplicar con `talend_job_apply_custom_spec` y anotar el tiempo por Job; (b) crear los mismos Jobs con `talend_jobs_create_batch` (una fila por Job, plantilla con los mismos componentes, `dryRun:true` primero) y anotar el tiempo; (c) comparar con `talend_inspect_job` componentes, conexiones y contextos de cada par; (d) ejecutar `talend_job_build_batch` sobre los Jobs offline y confirmar `noCompilan` vacío. Registrar los números en el documento.

- [ ] **Step 7: Decisión**

Escribir en `docs/talend-mcp-offline-evaluation.md` una sección «Decisión» con el criterio ya fijado: se adopta el motor offline (`auto`) si es ≥20× más rápido por Job, todos los Jobs offline compilan, hay paridad en componentes/conexiones/contextos y ≥50 % de las guías de los ZIP son elegibles; en otro caso se descarta y se omite la Tarea 8. Si se descarta, anotar el motivo medido.

- [ ] **Step 8: Commit**

```bash
git add src/sas_grid_migrator/talend_adapter/eligibility.py tools/offline_eligibility.py tests/unit/test_talend_eligibility.py docs/talend-mcp-offline-evaluation.md
git commit -m "feat: medir elegibilidad y rendimiento del modo offline del MCP"
```

---

### Task 8: Motor offline de `talend_job_apply_custom_spec` (solo si la Tarea 7 lo aprueba)

Se implementa en `mcp/talend-mcp/` y se envía al upstream público por PR. No debe nombrar el portal en código, mensajes ni documentación.

**Files:**
- Create: `mcp/talend-mcp/src/talend/studio/apply-custom-job-spec-offline.ts`
- Modify: `mcp/talend-mcp/src/talend/studio/custom-job-spec.ts`, `mcp/talend-mcp/src/talend/studio/apply-custom-job-spec.ts` (exportar `ownership`, `folderOf`, `existingFolderOf`), `mcp/talend-mcp/src/talend/studio/tools-custom-job-spec.ts`
- Modify: `contract/portal-tools.json` (`engine` entra en `required_top_fields`), `src/sas_grid_migrator/talend_adapter/adapter.py`, `src/sas_grid_migrator/talend_adapter/apply_spec.py` (envía `engine`), `apps/api/main.py` (`TALEND_APPLY_ENGINE`, por defecto `studio`)
- Test: `mcp/talend-mcp/tests/talend/apply-custom-job-spec-offline.test.ts` (nuevo), `tests/unit/test_talend_apply_spec.py`

**Interfaces:**
- Produces (MCP): campo opcional `engine?: "studio" | "offline" | "auto"` en `CustomJobSpec` (por defecto `"studio"`). `applyCustomJobSpecOffline(input: CustomJobSpec, deps: { projectPath: string; listJobs: CustomSpecDependencies["listJobs"]; componentVersions: Record<string, string>; openJobs: (names: string[]) => Promise<string[]> }): Promise<Result>` con el mismo `Result` que el motor Studio más `engine: "offline"`; `problems` queda `undefined`. Error `OFFLINE_UNSUPPORTED: <componentes>` cuando hay `mapper`, `tables` o `childJobs`. `ownership(spec)` excluye `engine` del hash.
- Consumes: `createJobsFromTemplate`/`applyJobEdits` (`src/talend/job-batch/batch.ts`, `src/talend/editor/job-edit.ts`), `jobsAbiertosEnStudio` (`src/talend/job-batch/open-guard.ts`).
- Produces (portal): `TalendAdapter.apply_custom_spec` pasa `engine` al MCP; `custom_spec_status` exige que el `inputSchema` publique `engine` cuando `TALEND_APPLY_ENGINE != "studio"`.

- [ ] **Step 1: Escribir las pruebas del motor offline (MCP) que fallan**

En `apply-custom-job-spec-offline.test.ts`, con un proyecto temporal: (a) crea un Job nuevo con 3 componentes y 2 conexiones y `inspect` lee lo mismo; (b) la descripción del `.properties` contiene `ownership(spec)` y reaplicar la misma especificación reutiliza (`reusedExisting: true`, `generatedComponents: 0`); (c) una especificación distinta con el mismo nombre lanza `CONFLICT`; (d) `mapper` o `tables` lanzan `OFFLINE_UNSUPPORTED` nombrando el componente y no escriben archivos; (e) `openJobs` devolviendo el Job lanza `JOB_OPEN_IN_STUDIO` sin escribir; (f) un contexto con valor existente se conserva cuando la nueva especificación lo trae vacío; (g) un componente `draftOnly` ausente del catálogo local se omite con aviso y sus conexiones también; (h) el hash de `ownership` es idéntico con y sin `engine`.

- [ ] **Step 2: Ejecutar y comprobar que fallan**

Run: `cd mcp/talend-mcp && bun test tests/talend/apply-custom-job-spec-offline.test.ts`
Expected: FAIL (módulo inexistente).

- [ ] **Step 3: Implementar el motor offline**

Reutilizar las reglas de destino de `apply-custom-job-spec.ts` (carpeta bajo `Process/`, conflicto por marca de propiedad, reanudación solo con la misma marca). Crear con `createJobsFromTemplate` (una fila) o completar con `applyJobEdits` los nodos, conexiones y contextos que falten, de forma atómica. Aplicar `replaceManagedTodoContexts` con la misma expresión `^migration_todo_[a-f0-9]{12}$` que el motor Studio. Refrescar Studio al terminar si responde.

- [ ] **Step 4: Enrutar por `engine` en la tool**

En `tools-custom-job-spec.ts`: `studio` → motor actual; `offline` → motor nuevo; `auto` → offline si `offlineBlockers(spec)` está vacío y, si no, Studio, devolviendo en `warnings` el motivo del enrutamiento. `engine` se añade al `inputSchema` como opcional para no romper clientes existentes.

- [ ] **Step 5: Ejecutar las pruebas del MCP**

Run: `cd mcp/talend-mcp && bun run typecheck && bun test tests/talend tests/tools`
Expected: PASS, incluidas las pruebas existentes de `custom-spec-executor` sin cambios.

- [ ] **Step 6: Pruebas del portal (fallan primero)**

En `test_talend_apply_spec.py`: `test_apply_passes_configured_engine` — con `TALEND_APPLY_ENGINE=auto` el argumento enviado a `apply_custom_spec` incluye `"engine": "auto"`; por defecto no incluye `engine` o es `"studio"`. En `test_talend_adapter.py`: `custom_spec_status` marca `contract_incomplete` si el motor configurado no es `studio` y el schema no publica `engine`.

- [ ] **Step 7: Implementar el lado portal y comprobar**

Run: `uv run pytest tests -q` y `uv run pytest tests/integration/test_mcp_contract.py -q`
Expected: PASS; la prueba de contrato confirma que el preset `portal` publica `engine`.

- [ ] **Step 8: Repetir la medición de la Tarea 7 con `engine: "auto"` sobre un ZIP completo**

Anotar tiempo total del lote y número de guías que cayeron a Studio por bloqueo, en `docs/talend-mcp-offline-evaluation.md`.

- [ ] **Step 9: Commit y PR upstream**

```bash
git add mcp/talend-mcp contract src apps tests docs
git commit -m "feat: motor offline opcional para talend_job_apply_custom_spec"
```

Después, `git subtree push --prefix=mcp/talend-mcp talend-mcp-upstream feat/apply-spec-offline-engine` y abrir PR en `AndresGaibor/talend-mcp`.

---

### Task 9: Diagnóstico accionable y arranque unificado

**Files:**
- Modify: `src/sas_grid_migrator/talend_adapter/adapter.py` (`custom_spec_status`, `health_check`), `apps/api/main.py:1807-1810`, `apps/web/src/views/SettingsView.tsx`, `apps/web/src/api.ts`, `apps/web/src/views/SettingsView.test.mjs`
- Create: `scripts/dev.ps1`
- Delete: rutas muertas de salud en `apps/api/integrations.py` (`talend_health` y `talend_inspect`, no montadas).
- Test: `tests/unit/test_talend_adapter.py`

**Interfaces:**
- Produces: `custom_spec_status()` añade `missing_tools: list[str]`, `diagnosis: "ok" | "mcp_down" | "client_incompatible" | "tools_missing" | "contract_incomplete" | "bridge_down"` y `fix_hint: str | None`. `health_check()` los propaga; la API los devuelve en `/api/integrations/talend/health`.
- Consumes: `load_contract()` (Tarea 4), `McpClientUnavailable` (Tarea 2).

- [ ] **Step 1: Escribir las pruebas que fallan**

Con `ListingFake` (ya existe en `test_talend_adapter.py`): (a) tools publicadas sin `talend_job_problems` → `diagnosis == "tools_missing"`, `missing_tools == ["talend_job_problems"]`, `fix_hint` contiene `TALEND_MCP_FILTER=portal`; (b) sin la tool de escritura → `tools_missing` y la lista la incluye; (c) schema sin `childJobs` → `contract_incomplete`; (d) `McpClientUnavailable` → `client_incompatible` con `fix_hint` que contiene `uv sync`; (e) todo presente y bridge caído → `bridge_down`. Prueba web: la vista renderiza `fix_hint` cuando `diagnosis !== "ok"`.

- [ ] **Step 2: Ejecutar y comprobar que fallan**

Run: `uv run pytest tests/unit/test_talend_adapter.py -k diagnosis -v` y `cd apps/web && bun test src/views/SettingsView.test.mjs`
Expected: FAIL.

- [ ] **Step 3: Implementar**

Calcular `missing_tools` como `(contract.read_tools | {contract.write_tool}) - nombres publicados`. `fix_hint` fijo por diagnóstico. Mostrar ambos en `SettingsView.tsx` junto al estado por etapas existente.

- [ ] **Step 4: Crear `scripts/dev.ps1`**

Arranca tres procesos: MCP (`bun run start` en `mcp/talend-mcp` con `TALEND_MCP_FILTER=portal`), API (`uv run uvicorn apps.api.main:app --host 127.0.0.1 --port 8000`) y web (`bun run dev` en `apps/web`). Antes comprueba `bun`, `uv` y que los puertos 3927/8000/5173 estén libres; imprime `bun run doctor` al final. No reinicia procesos ajenos.

- [ ] **Step 5: Ejecutar y comprobar que pasan**

Run: `uv run pytest tests -q` y `cd apps/web && bun test && bun run typecheck`
Expected: todo en verde.

- [ ] **Step 6: Commit**

```bash
git add src apps scripts tests
git commit -m "feat: diagnóstico accionable del MCP y arranque unificado"
```

---

### Task 10: Smoke test manual con Studio

**Files:**
- Modify: `docs/talend-mcp-tools.md` (resultado y matriz de prerequisitos)

**Interfaces:**
- Consumes: `scripts/dev.ps1` (Tarea 9), Studio 8.0.1 abierto con el Bridge instalado.

- [ ] **Step 1: Instalación en limpio**

En otra carpeta, clonar el repo y seguir solo el README (`uv sync`, `bun install` en `mcp/talend-mcp` y `apps/web`, `scripts/dev.ps1`). Anotar cada paso donde haga falta algo que el README no dice y corregir el README.

- [ ] **Step 2: Probar cada diagnóstico**

Con el MCP arrancado con `agent`, `all`, `portal` y apagado, y con Studio cerrado, confirmar que Configuración muestra el `diagnosis` esperado y que el `fix_hint` resuelve el caso.

- [ ] **Step 3: Crear y leer un Job en `Process/PruebasWebSAS`**

Aplicar una guía, comprobar con «Volver a comprobar pasos en Studio» que `talend_inspect_job` y `talend_job_problems` responden, repetir para ver la colisión de nombre. No compilar ni ejecutar.

- [ ] **Step 4: Comprobar si hace falta `unsafeActions`**

Repetir el Step 3 con el Bridge en modo solo lectura (`unsafeActions=false`) y registrar en `docs/talend-mcp-tools.md` si la creación funciona o qué error devuelve.

- [ ] **Step 5: Commit**

```bash
git add docs/talend-mcp-tools.md README.md
git commit -m "docs: resultados del smoke test y prerequisitos verificados"
```

---

### Task 11: Documentación para agentes, CI y flujo del subtree

**Files:**
- Create: `AGENTS.md`, `.github/workflows/ci.yml`, `docs/mcp-subtree.md`
- Modify: `mcp/talend-mcp/docs/superpowers/**` (retirar lo duplicado), `docs/superpowers/` (conservar como fuente de los planes del portal)

**Interfaces:**
- Consumes: todo lo anterior.

- [ ] **Step 1: `AGENTS.md`**

Secciones: qué es cada carpeta (`src/`, `apps/`, `mcp/talend-mcp/`, `contract/`), la regla «una tool nueva del portal se añade al manifiesto, al preset `portal` y pasa la prueba de contrato», comandos de verificación (`uv run pytest`, `bun test` en `apps/web` y `mcp/talend-mcp`) y la advertencia de no tocar el Bridge con Studio ocupado. Enlazar `mcp/talend-mcp/AGENTS.md` en vez de copiarlo.

- [ ] **Step 2: `docs/mcp-subtree.md`**

Procedimientos exactos con árbol limpio: traer upstream (`git subtree pull --prefix=mcp/talend-mcp talend-mcp-upstream main --squash`) y publicar cambios del MCP (`git subtree push --prefix=mcp/talend-mcp talend-mcp-upstream feat/<nombre>` y abrir PR en `AndresGaibor/talend-mcp`; nunca empujar a `main`). Regla: un commit que toca `mcp/talend-mcp/` no toca nada fuera de esa carpeta salvo `contract/` y sus pruebas.

- [ ] **Step 3: Retirar docs duplicados del MCP**

Los planes y specs del portal que Byron copió en `mcp/talend-mcp/docs/superpowers/` (`2026-10-21-portal-talend-mcp.md`, `2026-10-22-*`, `2026-10-23-*`, y los specs asociados) dejan de vivir en el MCP: moverlos a `docs/superpowers/` del portal (o borrarlos si ya están) y empujar la eliminación por PR al upstream, porque el MCP público no debe mencionar el portal.

- [ ] **Step 4: CI**

`ci.yml` con tres jobs en `windows-latest`: Python (`uv sync && uv run pytest`), web (`bun install && bun test && bun run typecheck && bun run build` en `apps/web`) y MCP (`bun install && bun run typecheck && bun test` en `mcp/talend-mcp`, con Bun instalado también para que la Tarea 6 no se salte).

- [ ] **Step 5: Verificar**

Run: `gh workflow run ci.yml` (o push a una rama) y `gh run watch`
Expected: los tres jobs en verde.

- [ ] **Step 6: Commit**

```bash
git add AGENTS.md docs .github
git commit -m "docs: guía para agentes, CI y flujo del subtree"
```
