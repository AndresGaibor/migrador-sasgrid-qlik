# Portal UX, fase 1: nombres editables, traductor visible y centro de mando

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que se pueda nombrar, describir y renombrar Jobs, corregir expresiones traducidas y probar el traductor desde el portal, y que el resumen del proyecto diga siempre qué sigue y qué falta.

**Architecture:** Las ediciones humanas son capas en SQLite (`job_overrides`, `expression_overrides`, `portal_settings`) que `load_plans` superpone al `plans.json`; todo lo que consume el plan (preflight, apply, lote, exportaciones) las ve sin cambios. La API nueva vive en `apps/api/main.py` (las rutas reales; `apps/api/plans.py` y `projects.py` no están montados en ninguna app). La web añade componentes en archivos nuevos y monta dos en `PlansTab.tsx`.

**Tech Stack:** Python 3 / FastAPI / SQLite / pydantic / pytest (`uv run pytest`); React 19 + Vite + `bun test` + `renderToStaticMarkup`.

**Spec:** `docs/superpowers/specs/2026-10-28-portal-ux-design.md` (hoja de ruta de las 50 opciones y decisiones de diseño; este plan es la fase 1).

## Global Constraints

- Las ediciones se superponen al cargar; **nunca** se escribe a `plans.json` un plan con ediciones aplicadas. `load_plans(..., with_edits=False)` es la carga cruda.
- Nombre de Job: `^[A-Za-z_][A-Za-z0-9_]*$`, longitud ≤ 60 (`MAX_JOB_NAME`), único sin distinguir mayúsculas dentro del proyecto.
- Plantilla de nombres por defecto: `job_{programa}` (igual al comportamiento actual; las pruebas doradas no deben cambiar). Tokens: `{proyecto}`, `{carpeta}`, `{programa}`; `{programa}` es obligatorio.
- Una expresión editada conserva `requires_semantic_validation=True` y lleva `talend_edited=True`; la edición guarda el SAS original y solo se aplica si coincide.
- Ediciones (nombre, descripción, expresión, renombrado masivo) devuelven 409 si hay un lote o una creación de Talend activos en el proyecto.
- El portal no renombra Jobs en Studio: renombrar un Job ya creado devuelve un aviso, no una acción.
- Textos de interfaz en español. Sin variables de entorno nuevas.
- Un commit que toca `mcp/talend-mcp/` no toca nada fuera de él salvo `contract/`; esta fase no debería tocarlo.
- **Commits solo si la persona dueña los autoriza** (`AGENTS.md`). Si no los ha autorizado, omite los pasos «Commit» y deja los cambios en el worktree. Los mensajes terminan con `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.
- Verificación final: `uv run pytest -q`, y `bun test` + `bun run typecheck` en `apps/web`.

## Review Focus

Entradas y condiciones que el diseño implica y que ninguna tarea cubriría sola. Cada una tiene su prueba en la tarea indicada.

1. Renombrar un Job que ya se creó en Studio: la respuesta trae un aviso que dice que el Job anterior sigue en Studio (Tarea 4).
2. Dos nombres que solo difieren en mayúsculas (`Job_A` / `job_a`), o un nombre editado igual al nombre generado de otro Job: se rechaza (Tareas 2 y 4).
3. «Actualizar guías» después de renombrar y de editar expresiones: el nombre sobrevive; una edición cuyo SAS ya no coincide se ignora; un renombrado que ahora choca se ignora y queda reportado en `rename_ignored`. Además, `verify_project_plans` no incrusta ediciones en `plans.json` (Tareas 3 y 4).
4. Editar mientras corre un lote de creación: 409 sin cambios en la base (Tarea 4).
5. Entradas hostiles al traductor y al renombrado por regex: texto vacío, 20 001 caracteres, comilla sin cerrar, `lag(x)` (no traducible: 200 con `talend: null`, nunca 500), patrón `(a+)+$` (rechazado, no cuelga) (Tareas 2 y 4).

---

### Task 0: Worktree aislado y línea base

**Files:** ninguno.

Hay trabajo ajeno sin commitear en `apps/api/main.py`, `store.py`, `docs/progress.md` y `tests/integration/test_api_zip_projects.py` (reintento del análisis). No se mezcla.

- [ ] **Step 1:** Crear el worktree desde `main`: `git worktree add ../migrador-sasgrid-qlik-ux -b feat/portal-ux-fase1 main`. Trabajar ahí todo el plan (en Windows, con `uv sync` y `cd apps/web && bun install` dentro del worktree).
- [ ] **Step 2:** Línea base: `uv run pytest -q` y, en `apps/web`, `bun test` y `bun run typecheck`. Anotar qué falla antes de tocar nada.
- [ ] **Step 3:** Leer `git diff main -- apps/api/main.py src/sas_grid_migrator/persistence/store.py` en el repo original para saber qué cambió el otro trabajo (se rebasa al final, Tarea 13).

---

### Task 1: Tablas de ediciones y ajustes en el Store

**Files:**
- Modify: `src/sas_grid_migrator/persistence/store.py` (`SCHEMA`, `delete_project`, métodos nuevos)
- Test: `tests/unit/test_store_overrides.py` (mismo estilo de fixtures que `tests/unit/test_store_project_state.py`)

**Interfaces:**
- Produces (todo en `store.py`):
  - `@dataclass(frozen=True) class JobOverride: job_name: str | None; description: str | None`
  - `Store.set_job_override(project_id: str, program: str, job_name: str | None, description: str | None) -> None`: con ambos `None` borra la fila.
  - `Store.get_job_overrides(project_id: str) -> dict[str, JobOverride]` (clave: `program`).
  - `Store.set_expression_override(project_id: str, program: str, step_id: str, index: int, sas: str, talend: str | None) -> None`: `talend=None` borra.
  - `Store.get_expression_overrides(project_id: str) -> dict[tuple[str, str, int], tuple[str, str]]` (clave `(program, step_id, index)`, valor `(sas, talend)`).
  - `Store.get_setting(key: str, default: str | None = None) -> str | None`, `Store.set_setting(key: str, value: str) -> None`.
  - `Store.has_active_talend_work(project_id: str) -> bool`: lote `queued`/`running` o alguna operación `running` (las mismas dos consultas de `delete_project`; `delete_project` no se toca en esa parte).

- [ ] **Step 1: Write the failing tests** en `tests/unit/test_store_overrides.py`:
  - `test_job_override_round_trip`: tras `set_job_override(pid, "a.sas", "mi_job", "Carga diaria")`, `get_job_overrides(pid)["a.sas"] == JobOverride("mi_job", "Carga diaria")`.
  - `test_job_override_with_both_none_removes_the_row`: tras `set_job_override(pid, "a.sas", None, None)`, `"a.sas" not in get_job_overrides(pid)`.
  - `test_expression_override_round_trip_and_clear`: `set_expression_override(pid, "a.sas", "s1", 0, "x > 1", "input_row.x > 1")` → `get_expression_overrides(pid)[("a.sas","s1",0)] == ("x > 1","input_row.x > 1")`; con `talend=None` desaparece.
  - `test_settings_default_and_update`: `get_setting("k") is None`, `get_setting("k","d") == "d"`; tras `set_setting("k","v")` devuelve `"v"`.
  - `test_deleting_a_project_removes_its_overrides`: con overrides de las dos tablas, `delete_project(pid) is True` y las tablas quedan sin filas de ese proyecto (las claves foráneas están activas: sin esto la prueba falla con `IntegrityError`).
  - `test_has_active_talend_work`: `False` sin lote; `True` tras guardar un lote en `running` con `update_talend_apply_batch_state`; `False` cuando pasa a `applied`.
- [ ] **Step 2: Run** `uv run pytest tests/unit/test_store_overrides.py -q`. Expected: FAIL (`AttributeError`/`ImportError`).
- [ ] **Step 3: Implement** en `store.py`: añadir al `SCHEMA` `job_overrides(project_id, program, job_name, description, updated_at, primary key(project_id, program))`, `expression_overrides(project_id, program, step_id, idx, sas, talend, updated_at, primary key(project_id, program, step_id, idx))` (ambas con `references projects(id)`) y `portal_settings(key text primary key, value text not null)`; añadir las dos tablas por proyecto a la tupla de `delete_project`; escribir los métodos del bloque Interfaces con `insert … on conflict do update` como `set_talend_write_enabled`.
- [ ] **Step 4: Run** el mismo comando. Expected: PASS.
- [ ] **Step 5: Commit** `git add src/sas_grid_migrator/persistence/store.py tests/unit/test_store_overrides.py` · `feat: guarda ediciones de Jobs y expresiones y ajustes del portal`.

---

### Task 2: Reglas de nombres: validación, plantilla y renombrado masivo

**Files:**
- Create: `src/sas_grid_migrator/migration_planner/job_naming.py`
- Modify: `src/sas_grid_migrator/migration_planner/planner.py:186-218` (`unique_job_names` recibe el generador de nombres)
- Test: `tests/unit/test_job_naming.py`; `tests/unit/test_unique_job_names.py` debe seguir pasando sin cambios.

**Interfaces:**
- Produces (`job_naming.py`):
  - `DEFAULT_NAME_TEMPLATE = "job_{programa}"`, `TEMPLATE_TOKENS = ("proyecto", "carpeta", "programa")`.
  - `validate_job_name(name: str, *, taken: Collection[str]) -> str | None`: devuelve el mensaje de error o `None`. Mensajes exactos: `"El nombre debe empezar con una letra o guion bajo y usar solo letras, números y guion bajo."`, `"El nombre no puede pasar de 60 caracteres."`, `"Ya existe otro Job con ese nombre."` (comparación con `casefold`).
  - `validate_template(template: str) -> str | None`: error si falta `{programa}` (`"La plantilla debe incluir {programa}."`) o hay un token desconocido (`"Token desconocido: {x}."`).
  - `render_job_name(template: str, *, project: str, program: str, depth: int = 0) -> str`: sustituye con `planner.slug`; `{carpeta}` es la carpeta inmediata del programa (vacía si no hay); con `depth > 0`, `{programa}` antepone las `depth` carpetas anteriores (igual que `_job_name_with_folders`); el resultado se sanea a identificador (caracteres no válidos → `_`, `_` repetidos colapsados, sin `_` en los extremos; si queda vacío o empieza con dígito se antepone `job_`) y no se acota (el límite lo aplica `cap_job_name`).
  - `class BulkRule(BaseModel)`: `mode: Literal["prefix","suffix","replace","regex"]`, `text: str = ""`, `find: str = ""`, `replace_with: str = ""`, `programs: list[str] | None = None`.
  - `class RenamePreview(BaseModel)`: `program: str`, `current: str`, `proposed: str`, `error: str | None`.
  - `bulk_preview(plans: Sequence[JobPlan], rule: BulkRule) -> list[RenamePreview]`: solo los `programs` pedidos (o todos); `error` por fila con las reglas de `validate_job_name` aplicadas contra los nombres finales del resto del proyecto y contra las demás propuestas; filas sin cambio llevan `proposed == current` y `error=None`. Lanza `ValueError` con mensaje en español si el patrón regex no compila, pasa de 200 caracteres o tiene cuantificadores anidados (`re.search(r"\([^)]*[+*][^)]*\)[+*{]", find)`: `"El patrón es demasiado complejo."`).
- Modifies: `unique_job_names(plans: list[JobPlan], name_with_folders: Callable[[tuple[str, ...], int], str] = _job_name_with_folders) -> None`.

- [ ] **Step 1: Write the failing tests** en `tests/unit/test_job_naming.py`:
  - `validate_job_name("2abc", taken=[])` → mensaje de identificador; `"a" * 61` → mensaje de 60; `validate_job_name("JOB_A", taken=["job_a"])` → `"Ya existe otro Job con ese nombre."`; `validate_job_name("job_a", taken=[])` → `None`.
  - `render_job_name("job_{programa}", project="Finanzas", program="lz/Cod 2.sas") == "job_cod_2"`; con `"{proyecto}_{carpeta}_{programa}"` → `"finanzas_lz_cod_2"`; con `program="cod2.sas"` y plantilla de `{carpeta}` → sin guiones bajos dobles (`"finanzas_cod2"`); con `project="2024"` y `"{proyecto}_{programa}"` → empieza con `job_`; con `depth=1` y `program="a/x/run.sas"` y la plantilla por defecto → `"job_x_run"` (igual que `_job_name_with_folders`).
  - `validate_template("{proyecto}")` → `"La plantilla debe incluir {programa}."`; `validate_template("job_{programa}_{foo}")` → `"Token desconocido: {foo}."`; la plantilla por defecto → `None`.
  - `bulk_preview` con prefijo `"fin_"` sobre `job_a`, `job_b` → propuestas `fin_job_a`, `fin_job_b`, sin error; con `mode="replace"`, `find="job_"`, `replace_with=""` sobre `job_a` y `a` ya existente → la fila de `job_a` trae `error == "Ya existe otro Job con ese nombre."`; dos propuestas iguales entre sí → ambas con error; `mode="regex"`, `find="(a+)+$"` → `ValueError("El patrón es demasiado complejo.")`; `find="("` → `ValueError`.
  - `unique_job_names` con un `name_with_folders` propio usa ese generador (nombre `x_db2_bulkload` para el choque `DB2/bulkload.sas` vs `Hadoop/bulkload.sas`).
- [ ] **Step 2: Run** `uv run pytest tests/unit/test_job_naming.py -q`. Expected: FAIL (`ModuleNotFoundError`).
- [ ] **Step 3: Implement** `job_naming.py` según el bloque Interfaces y añadir el parámetro `name_with_folders` a `unique_job_names` (sustituye las dos llamadas a `_job_name_with_folders` dentro de la función).
- [ ] **Step 4: Run** `uv run pytest tests/unit/test_job_naming.py tests/unit/test_unique_job_names.py tests/unit/test_naming.py -q`. Expected: PASS.
- [ ] **Step 5: Commit** `feat: reglas de nombres de Job (validación, plantilla y renombrado masivo)`.

---

### Task 3: Capa de ediciones en el servicio de planes

**Files:**
- Modify: `src/sas_grid_migrator/migration_planner/models.py` (campos nuevos), `src/sas_grid_migrator/migration_planner/service.py` (`generate_plans`, `load_plans`, `get_plan`), `src/sas_grid_migrator/talend_adapter/apply_spec.py` (descripción), `src/sas_grid_migrator/reporting/exports.py` (descripción en el Markdown)
- Test: `tests/unit/test_plan_edits.py`, `tests/unit/test_talend_apply_spec.py` (caso nuevo)

**Interfaces:**
- Consumes: `Store.get_job_overrides`, `Store.get_expression_overrides`, `Store.get_setting`; `job_naming.render_job_name`, `DEFAULT_NAME_TEMPLATE`.
- Produces:
  - `JobPlan.description: str | None = None`, `JobPlan.job_name_edited: bool = False`, `JobPlan.rename_ignored: str | None = None`; `Expression.talend_edited: bool = False`.
  - `service.NAME_TEMPLATE_KEY = "job_name_template"`; `service.current_name_template(store: Store) -> str` (ajuste guardado o `DEFAULT_NAME_TEMPLATE`).
  - `load_plans(store: Store, project_id: str, *, with_edits: bool = True) -> PlanSet | None`; `get_plan(store, project_id, program, *, with_edits: bool = True)`.
  - `ApplySpec.description: str | None = None`; `to_mcp_arguments()` usa `self.description or f"Migrated from SAS program {self.program}"`; `build_apply_spec` la rellena con `plan.description`.
- Reglas de superposición (con `with_edits=True`), en este orden, sobre cada `JobPlan` de `ps.plans`:
  1. Renombrado: un override se acepta solo si su nombre (`casefold`) no coincide con el nombre generado de otro plan ni con un override ya aceptado (se recorre por `program` ordenado). Aceptado: `job_name` y `job_name_edited=True`. Rechazado: se conserva el generado y `rename_ignored = <nombre pedido>`.
  2. Descripción: `description` del override si no es `None`.
  3. Expresiones (en `steps` y en `children[*].steps`): el override `(program, step_id, index)` se aplica solo si `index` existe y `expression.sas == sas_guardado`; entonces `expression.talend = valor` y `expression.talend_edited = True`.

- [ ] **Step 1: Write the failing tests** en `tests/unit/test_plan_edits.py` (con un `Store` temporal y un `PlanSet` escrito en `store.plans_path`; mismo patrón que `_project_with_plans` de `tests/integration/test_api_talend_batch.py`):
  - `test_job_override_renames_the_plan_and_marks_it`: `load_plans(...).plans[0].job_name == "mi_job"` y `job_name_edited is True`; `with_edits=False` devuelve el nombre generado.
  - `test_override_colliding_with_a_generated_name_is_ignored`: override `JOB_B` en el plan A cuando el plan B se llama `job_b` → A conserva su nombre y `rename_ignored == "JOB_B"`.
  - `test_expression_override_applies_only_when_the_sas_matches`: con `sas` igual se aplica `talend` y `talend_edited`; con otro `sas` la expresión queda intacta.
  - `test_overrides_survive_regenerating_the_plans`: tras `generate_plans(store, pid)` sobre un ZIP del corpus pequeño (usar un fixture de `tests/fixtures`, como `test_api_guided_pipeline.py`), el override de nombre sigue aplicándose.
  - `test_generate_plans_uses_the_saved_name_template`: con `set_setting("job_name_template", "{proyecto}_{programa}")` los nombres generados empiezan con el slug del proyecto; sin ajuste son `job_<programa>`.
  - `test_unique_names_follow_the_template`: dos programas con el mismo nombre en carpetas distintas y la plantilla por defecto dan `job_db2_bulkload` y `job_hadoop_bulkload` (comportamiento actual).
  - En `tests/unit/test_talend_apply_spec.py`: `to_mcp_arguments()["description"] == "Carga diaria"` cuando el plan tiene descripción y `"Migrated from SAS program <programa>"` cuando no.
- [ ] **Step 2: Run** `uv run pytest tests/unit/test_plan_edits.py tests/unit/test_talend_apply_spec.py -q`. Expected: FAIL.
- [ ] **Step 3: Implement** los campos de `models.py`; en `generate_plans`, tras `plan_program`, fijar `plan.job_name = render_job_name(template, project=<nombre del proyecto>, program=plan.program)` y llamar `unique_job_names(plans, namer)` con `namer = lambda parts, depth: render_job_name(template, project=…, program="/".join(parts), depth=depth)`; en `service.py`, `_apply_edits(store, ps)` con las reglas del bloque anterior, llamado desde `load_plans` cuando `with_edits`; `ApplySpec`/`build_apply_spec` para la descripción; en `render_plan_md` (`exports.py`) una línea con la descripción bajo el título solo si existe.
- [ ] **Step 4: Run** `uv run pytest tests/unit tests/golden -q`. Expected: PASS (las pruebas doradas no cambian porque la plantilla por defecto reproduce los nombres actuales).
- [ ] **Step 5: Commit** `feat: capa de ediciones de nombre, descripción y expresiones sobre el plan`.

---

### Task 4: API de ediciones, traductor y ajustes

**Files:**
- Modify: `apps/api/main.py` (rutas nuevas junto a `patch_step`; `list_plans` añade `description`; `verify_project_plans` carga cruda)
- Create: `tests/support/plan_api.py` (copia de `_plan` y `_project_with_plans` de `tests/integration/test_api_talend_batch.py`, sin tocar ese archivo), `tests/integration/test_api_plan_edits.py`

**Interfaces:**
- Consumes: Tareas 1 a 3. Antes de editar, `from sas_grid_migrator.migration_planner.job_naming import …`.
- Produces (todas bajo `/api`; las de proyecto hacen `_require`):
  - `PATCH /projects/{id}/plans/{program:path}/meta`, cuerpo `{job_name: str | None, description: str | None}` → `{"plan": JobPlan, "warnings": [str]}`. `job_name` igual al generado, vacío o `None` borra el override. Valida con `validate_job_name(taken=<nombres finales de los demás Jobs>)` → 422 con el mensaje; descripción ≤ 500 caracteres → 422. Aviso si el Job ya se creó (estado de aplicación `applied`/`partially_applied` de ese programa o su entrada en el lote): `"Este Job ya se creó en Talend Studio con el nombre anterior (<anterior>). Studio conservará ese Job; el nuevo se creará en la próxima aplicación."`
  - `POST /projects/{id}/plans/rename-preview`, cuerpo `BulkRule` → `list[RenamePreview]` (422 con el mensaje del `ValueError`).
  - `POST /projects/{id}/plans/rename`, cuerpo `{renames: [{program: str, job_name: str}]}` → `{"renamed": int}`. Todo o nada: valida cada fila como en el preview contra el conjunto final y responde 422 con el primer error sin escribir nada.
  - `PATCH /projects/{id}/plans/{program:path}/steps/{step_id}/expressions/{index}`, cuerpo `{talend: str | None}` → `JobPlan`. `None` restaura la traducción automática; texto vacío, con salto de línea o de más de 2000 caracteres → 422; `index` inexistente → 404.
  - `POST /translator/translate`, cuerpo `{sas: str}` (1 a 20 000 caracteres, si no 422) → `{sas, talend: str | None, columns: [str], warnings: [str], engine: str, supported: bool, talend_engine_enabled: bool}` usando `expressions.translate` y `talend_expressions_enabled()`.
  - `GET /settings/naming` → `{template, default, tokens}`; `PATCH /settings/naming`, cuerpo `{template}` → igual (422 con el mensaje de `validate_template`); `GET /settings/naming/example?template=…` → `{example: str | None, error: str | None}` con proyecto de muestra `finanzas` y programa `lz/cod2.sas`.
  - Las cuatro rutas de edición de proyecto devuelven 409 `"No se puede editar mientras Talend crea Jobs de este proyecto."` si `Store.has_active_talend_work(id)`.

- [ ] **Step 1: Write the failing tests** en `tests/integration/test_api_plan_edits.py` (cliente `TestClient(apps.api.main.app)` con la misma preparación de entorno que `test_api_talend_batch.py`):
  - `test_rename_job_updates_the_plan_list_and_the_apply_spec`: `PATCH …/meta` con `job_name="mi_job"` → 200; `GET /plans` lista `job_name == "mi_job"`; `POST …/talend-apply/preview` trae `identity.job_name == "mi_job"`.
  - `test_rename_rejects_invalid_and_duplicate_names`: `"2abc"` → 422; `"JOB_B"` cuando otro Job se llama `job_b` → 422 «Ya existe otro Job con ese nombre.»; nada cambia en `GET /plans`.
  - `test_rename_after_studio_creation_warns`: con un estado de aplicación `applied` guardado (`store.save_talend_apply_state`), la respuesta trae el aviso de «ya se creó en Talend Studio».
  - `test_description_is_saved_and_sent_to_studio`: tras `PATCH …/meta` con `description="Carga diaria"`, el preview del Job trae esa descripción en los argumentos del MCP.
  - `test_edits_are_blocked_while_a_batch_runs`: con un lote `running` guardado, `PATCH …/meta` → 409 y `get_job_overrides` vacío.
  - `test_bulk_preview_and_apply_are_all_or_nothing`: preview con prefijo marca filas; `POST …/rename` con una fila inválida → 422 y ningún nombre cambia; con todas válidas → `renamed == 2`.
  - `test_expression_edit_round_trip`: `PATCH …/expressions/0` con `talend="input_row.x > 1"` → `JobPlan` con `talend_edited is True`; con `talend=null` vuelve a la traducción automática; `index=99` → 404; texto de 2001 caracteres → 422.
  - `test_translator_endpoint_handles_hostile_input`: `{"sas": ""}` → 422; 20 001 caracteres → 422; `{"sas": "x = 'abc"}` → 200 con `talend is None` y `warnings` no vacío; `{"sas": "lag(x)"}` → 200 con `supported is False`; `{"sas": "upcase(nome) = 'A'"}` → 200 con `supported is True` (usar una expresión que `translate()` resuelva en línea; ajustar al corpus de `tests/unit/test_talend_translator.py`).
  - `test_naming_settings_validate_and_apply_on_regenerate`: `PATCH /settings/naming` con `{"template": "{proyecto}"}` → 422; con `{"template": "{proyecto}_{programa}"}` → 200 y `GET /settings/naming/example` devuelve `finanzas_cod2`.
  - `test_verify_does_not_bake_edits_into_plans_json`: con un override de nombre, tras `POST /plans/verify` (con `_talend` falso que devuelve inventario vacío, como el `FakeTalend` del archivo de lote) `plans.json` leído en crudo conserva el nombre generado.
- [ ] **Step 2: Run** `uv run pytest tests/integration/test_api_plan_edits.py -q`. Expected: FAIL (404 en las rutas nuevas).
- [ ] **Step 3: Implement** las rutas en `main.py`; para el aviso de «ya creado» leer `s.get_talend_apply_state(project_id, program)` y el lote guardado (el mismo getter que usa `talend_apply_batch_status`); en `verify_project_plans`, cambiar `_plans(project_id)` por `load_plans(s, project_id, with_edits=False)` (con el mismo 409 si falta) antes de verificar y guardar; añadir `"description": p.description` a cada fila de `list_plans`.
- [ ] **Step 4: Run** `uv run pytest tests/integration tests/unit -q`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(api): edición de nombre, descripción y expresiones, renombrado masivo, traductor y plantilla de nombres`.

---

### Task 5: Progreso del proyecto y pendientes agrupados

**Files:**
- Create: `src/sas_grid_migrator/migration_planner/progress.py`
- Modify: `apps/api/main.py` (dos rutas `GET`)
- Test: `tests/unit/test_progress.py`, `tests/integration/test_api_progress.py`

**Interfaces:**
- Produces (`progress.py`):
  - `class Stage(BaseModel)`: `key: Literal["upload","analysis","guides","studio","complete","verify"]`, `label: str`, `status: Literal["done","current","todo","blocked"]`, `detail: str`.
  - `class NextAction(BaseModel)`: `key: str`, `label: str`, `tab: Literal["importar","resumen","planes"]`, `reason: str`.
  - `class ProjectProgress(BaseModel)`: `stages: list[Stage]`, `next: NextAction | None`.
  - `compute_progress(*, files: int, processing_status: str | None, plan_rows: list[dict] | None, batch_status: str | None) -> ProjectProgress`. `plan_rows` es la salida de `list_plans` (`steps`, `done`, `studio_status`).
  - `class PendingProgram(BaseModel)`: `program: str`, `job_name: str`, `step_ids: list[str]`; `class PendingGroup(BaseModel)`: `reason: str`, `steps: int`, `programs: list[PendingProgram]`.
  - `pending_groups(ps: PlanSet) -> list[PendingGroup]`: agrupa por el **texto exacto** de cada elemento de `step.pending` (pasos de `steps` y de `children[*].steps`, ignorando pasos `descartado`); orden: `steps` descendente y luego `reason`.
- Etapas: **upload** hecha si `files > 0`; **analysis** hecha si `processing_status == "completed"`, `current` si `queued`/`running` (detalle «en curso»), `blocked` si `failed`/`interrupted`; **guides** hecha si `plan_rows` no está vacío; **studio** hecha si `batch_status` ∈ {`applied`,`partially_applied`} o la etapa `complete` está hecha, `blocked` si `batch_status` ∈ {`failed`,`conflict`,`interrupted`}, `current` si `queued`/`running`; **complete** hecha si todo Job con `steps > 0` tiene `done == steps` (detalle «X de Y pasos»); **verify** hecha si todo Job con pasos tiene `studio_status == "verified"`. Una etapa sin la anterior hecha es `todo`; la primera no hecha y no bloqueada es `current`. `next` apunta a la primera etapa no hecha (`tab`: upload→`importar`, analysis→`resumen`, el resto→`planes`) y es `None` si todo está hecho.

- [ ] **Step 1: Write the failing tests** en `tests/unit/test_progress.py`:
  - `compute_progress(files=0, processing_status=None, plan_rows=None, batch_status=None)`: `next.key == "upload"`, `next.tab == "importar"`, resto `todo`.
  - `files=5, processing_status="running"`: `analysis` es `current`, `next.tab == "resumen"`.
  - `processing_status="failed"`: `analysis` es `blocked` y `next.key == "analysis"`.
  - Con guías y `batch_status=None`: `next.key == "studio"`; con `batch_status="applied"` y pasos sin hacer: `next.key == "complete"` y el detalle de `complete` es `"3 de 10 pasos"` para `[{"steps":10,"done":3}]`.
  - Todo hecho: `next is None`; con `batch_status="conflict"` `studio` es `blocked`.
  - `pending_groups`: dos pasos con `pending=["sistema y tabla de destino"]` en Jobs distintos y uno con `["ruta, delimitador"]` → dos grupos, el primero con `steps == 2` y dos `programs`; un paso `descartado` no cuenta; un paso de macro hija cuenta.
  - `tests/integration/test_api_progress.py`: `GET /projects/{id}/progress` y `GET /projects/{id}/pending-summary` sobre un proyecto con planes; sin planes `pending-summary` → 409 y `progress` → 200 con `guides` no hecha.
- [ ] **Step 2: Run** `uv run pytest tests/unit/test_progress.py tests/integration/test_api_progress.py -q`. Expected: FAIL.
- [ ] **Step 3: Implement** `progress.py` y las rutas `GET /api/projects/{id}/progress` (archivos de `get_project(...).manifest_summary`, estado de `get_processing`, `list_plans(project_id)` capturando el 409 como «sin guías», estado del lote guardado) y `GET /api/projects/{id}/pending-summary` (409 si no hay planes).
- [ ] **Step 4: Run** las mismas pruebas. Expected: PASS.
- [ ] **Step 5: Commit** `feat: progreso del proyecto y pendientes agrupados por motivo`.

---

### Task 6: Cliente web: tipos, llamadas y lógica pura

**Files:**
- Modify: `apps/web/src/types.ts`, `apps/web/src/api.ts`
- Create: `apps/web/src/project-progress.ts`
- Test: `apps/web/src/api.test.ts` (casos nuevos), `apps/web/src/project-progress.test.ts`

**Interfaces:**
- Produces (`types.ts`): `JobPlan` suma `description?: string | null; job_name_edited?: boolean; rename_ignored?: string | null`; `Step["expressions"][number]` suma `talend_edited?: boolean; target?: string | null`; `PlanRow` suma `description?: string | null`. Tipos nuevos `JobMetaResult = { plan: JobPlan; warnings: string[] }`, `BulkRenameRule = { mode: "prefix"|"suffix"|"replace"|"regex"; text?: string; find?: string; replace_with?: string; programs?: string[] }`, `RenamePreviewRow = { program: string; current: string; proposed: string; error: string | null }`, `TranslateResult = { sas: string; talend: string | null; columns: string[]; warnings: string[]; engine: string; supported: boolean; talend_engine_enabled: boolean }`, `NamingTemplate = { template: string; default: string; tokens: string[] }`, `ProjectStage = { key: "upload"|"analysis"|"guides"|"studio"|"complete"|"verify"; label: string; status: "done"|"current"|"todo"|"blocked"; detail: string }`, `ProjectProgress = { stages: ProjectStage[]; next: { key: string; label: string; tab: "importar"|"resumen"|"planes"; reason: string } | null }`, `PendingGroup = { reason: string; steps: number; programs: { program: string; job_name: string; step_ids: string[] }[] }`.
- Produces (`api.ts`, dentro de `api`): `updateJobMeta(id, file, body: { job_name: string | null; description: string | null })`, `renamePreview(id, rule)`, `renameJobs(id, renames: { program: string; job_name: string }[])`, `editExpression(id, file, step, index, talend: string | null)`, `translate(sas)`, `namingTemplate()`, `setNamingTemplate(template)`, `namingExample(template)`, `progress(id)`, `pendingSummary(id)`; rutas como en la Tarea 4, con `enc(file)` para el programa.
- Produces (`project-progress.ts`): `nextActionHref(id: string, next: ProjectProgress["next"]): string | null` (`link(id, next.tab)`); `stageTone(status: ProjectStage["status"]): "ok" | "warn" | "bad" | "neutral"` (done→ok, current→warn, blocked→bad, todo→neutral); `pendingTotals(groups: PendingGroup[]): { steps: number; jobs: number }` (Jobs distintos y pasos distintos).

- [ ] **Step 1: Write the failing tests:** en `api.test.ts`, con el patrón de `fetch` simulado del archivo: `updateJobMeta("p","dir/a ?#.sas",{job_name:"x",description:null})` hace `PATCH /api/projects/p/plans/dir/a%20%3F%23.sas/meta` con el cuerpo JSON; `translate("a")` hace `POST /api/translator/translate`; `renameJobs` envía `{renames:[…]}`. En `project-progress.test.ts`: `stageTone` para los cuatro estados; `nextActionHref("p", {tab:"planes",…}) === "#/p/p/planes"` y `null` si `next` es `null`; `pendingTotals` cuenta Jobs distintos aunque un Job aparezca en dos grupos.
- [ ] **Step 2: Run** `cd apps/web && bun test src/api.test.ts src/project-progress.test.ts`. Expected: FAIL.
- [ ] **Step 3: Implement** tipos, llamadas y `project-progress.ts` (importa `link` de `./views/common`).
- [ ] **Step 4: Run** `bun test && bun run typecheck`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(web): cliente de la API de ediciones, traductor y progreso`.

---

### Task 7: Nombre y descripción del Job en la guía y en la lista

**Files:**
- Create: `apps/web/src/views/plans/JobIdentity.tsx`
- Modify: `apps/web/src/views/PlansTab.tsx` (reemplaza `<h1>{p.job_name}</h1>` en `PlanDetail` por `<JobIdentity …/>`), `apps/web/src/views/plans/PlanListContent.tsx` (muestra `row.description` bajo el nombre), `apps/web/src/guide-export.ts` (descripción en el Markdown), `apps/web/src/styles.css`
- Test: `apps/web/src/views/plans/JobIdentity.test.tsx`

**Interfaces:**
- Consumes: `api.updateJobMeta`, `JobMetaResult`, `notifyError`, `notifySuccess`.
- Produces: `JobIdentity({ id, plan, folderPath, locked, onSaved }: { id: string; plan: JobPlan; folderPath?: string; locked: boolean; onSaved: (plan: JobPlan) => void })`. En reposo muestra `<h1>` con el nombre, insignia «editado» si `job_name_edited`, la descripción y la carpeta destino; «Editar nombre y descripción» abre un formulario con dos campos; guardar llama `api.updateJobMeta` y `onSaved(result.plan)`; los `warnings` se muestran como `.notice`; `rename_ignored` muestra un aviso «El nombre «X» ya no está disponible; se usa el generado»; `locked` deshabilita el botón con el texto «Hay una creación en curso».
- En `PlanDetail`, `folderPath` sale de `preview.data?.identity.folder_path` y `locked` de `isBatchRunning || isApplyRunning`; `onSaved={setOverride}`.

- [ ] **Step 1: Write the failing test** (`renderToStaticMarkup`, como `PlanListContent.test.tsx`): con `plan.job_name_edited=true` el marcado contiene `editado` y el nombre; con `rename_ignored="x"` contiene el aviso; con `locked` el botón `disabled`; con `description` aparece el texto; la carpeta destino aparece cuando se pasa `folderPath`. Una de `PlanListContent`: una fila con `description` la muestra.
- [ ] **Step 2: Run** `bun test src/views/plans`. Expected: FAIL.
- [ ] **Step 3: Implement** `JobIdentity.tsx` (formulario controlado con validación mínima en el cliente: no vacío salvo para volver al nombre generado; los errores de la API se muestran con `notifyError`); montar en `PlansTab.tsx`; fila de lista; descripción en `guideMarkdown`.
- [ ] **Step 4: Run** `bun test && bun run typecheck`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(web): nombre y descripción editables del Job`.

---

### Task 8: Renombrado masivo

**Files:**
- Create: `apps/web/src/views/plans/BulkRename.tsx`
- Modify: `apps/web/src/views/PlansTab.tsx` (botón «Renombrar Jobs» en `plan-rebuild-toolbar` y montaje del diálogo en `PlanList`), `apps/web/src/styles.css`
- Test: `apps/web/src/views/plans/BulkRename.test.tsx`

**Interfaces:**
- Consumes: `api.renamePreview`, `api.renameJobs`, `Dialog` de `components/Dialog`, `RenamePreviewRow`, `BulkRenameRule`.
- Produces: `BulkRename({ id, onClose, onDone }: { id: string; onClose: () => void; onDone: () => void })` y la pura `renameSummary(rows: RenamePreviewRow[]): { changes: number; errors: number; canApply: boolean }` (`canApply` solo si hay al menos un cambio y cero errores). El diálogo: selector de modo (prefijo, sufijo, buscar y reemplazar, regex), campos según el modo, tabla «Programa · Antes · Después · Error» recalculada al pulsar «Ver cambios» (no en cada tecla), botón «Aplicar N cambios» activo según `renameSummary`; errores del servidor (patrón complejo) en `role="alert"`. En `PlanList`, `onDone` recarga `q`, `summary` y `preflight` y muestra `notifySuccess`.

- [ ] **Step 1: Write the failing test:** `renameSummary` (vacío → `canApply false`; 2 cambios y 0 errores → `true`; 1 error → `false`; filas sin cambio no cuentan); `renderToStaticMarkup(<BulkRename …/>)` contiene los cuatro modos y el botón «Aplicar» deshabilitado en el estado inicial.
- [ ] **Step 2: Run** `bun test src/views/plans/BulkRename.test.tsx`. Expected: FAIL.
- [ ] **Step 3: Implement** el componente y su montaje; el botón se deshabilita mientras `batchActive`.
- [ ] **Step 4: Run** `bun test && bun run typecheck`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(web): renombrado masivo de Jobs con vista previa`.

---

### Task 9: Plantilla de nombres en Configuración

**Files:**
- Create: `apps/web/src/views/settings/NamingTemplateCard.tsx`
- Modify: `apps/web/src/views/SettingsView.tsx` (montar la tarjeta), `apps/web/src/styles.css`
- Test: `apps/web/src/views/settings/NamingTemplateCard.test.tsx`

**Interfaces:**
- Consumes: `api.namingTemplate`, `api.setNamingTemplate`, `api.namingExample`.
- Produces: `NamingTemplateCard()`: campo de plantilla con los tokens `{proyecto}`, `{carpeta}`, `{programa}` como botones que insertan el token, ejemplo en vivo (consulta con retardo de 300 ms a `namingExample`) y el error de validación bajo el campo; «Guardar» llama `setNamingTemplate`; «Restaurar `job_{programa}`». Texto fijo: «Se aplica al preparar o actualizar las guías. Los nombres que editaste a mano no cambian.»

- [ ] **Step 1: Write the failing test:** el marcado inicial (con los datos de `namingTemplate` ya resueltos, pasados por una prop opcional `initial?: NamingTemplate` para poder probarlo sin red) contiene los tres tokens, la plantilla por defecto y el texto fijo; el botón «Guardar» está deshabilitado si la plantilla no cambió.
- [ ] **Step 2: Run** `bun test src/views/settings`. Expected: FAIL.
- [ ] **Step 3: Implement** la tarjeta y montarla en `SettingsView` bajo la sección de Talend.
- [ ] **Step 4: Run** `bun test && bun run typecheck`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(web): plantilla de nombres de Job en Configuración`.

---

### Task 10: Laboratorio del traductor y edición de expresiones en el paso

**Files:**
- Create: `apps/web/src/views/TranslatorView.tsx`, `apps/web/src/views/plans/ExpressionEditor.tsx`
- Modify: `apps/web/src/App.tsx` (ruta `#/traductor` y enlace «Traductor» en el sidebar con un `IconName` existente de `components/Icon.tsx`), `apps/web/src/views/plans/PlanStepParts.tsx` (`StepInstructions` monta un `ExpressionEditor` por expresión), `apps/web/src/views/PlansTab.tsx` (pasa `onPlan={setOverride}` por `StepGroups` → `StepCard` → `StepInstructions`), `apps/web/src/styles.css`
- Test: `apps/web/src/views/TranslatorView.test.tsx`, `apps/web/src/views/plans/ExpressionEditor.test.tsx`

**Interfaces:**
- Consumes: `api.translate`, `api.editExpression`, `TranslateResult`.
- Produces:
  - `TranslatorView()`: textarea de SAS (máx. 20 000), botón «Traducir», resultado con el Java de Talend en `<pre>`, columnas detectadas, avisos, el motor usado y, si `!talend_engine_enabled` y no hubo traducción, la nota «El traductor ampliado con rutinas de Talend está apagado (`SGM_TALEND_EXPRESSIONS`).»; ejemplos de un clic (3 expresiones SAS).
  - `ExpressionEditor({ id, file, stepId, index, expression, onSaved }: { id: string; file: string; stepId: string; index: number; expression: Step["expressions"][number]; onSaved: (plan: JobPlan) => void })`: muestra el SAS y el Java actual con insignia «editada» si `talend_edited`; «Editar» abre un textarea de una línea; «Guardar» llama `api.editExpression`; «Volver a la traducción automática» llama con `null` (solo si está editada); si `talend` es `null` se muestra «Sin traducción automática» y se puede escribir una a mano.

- [ ] **Step 1: Write the failing test:** `ExpressionEditor` con `talend_edited: true` contiene «editada» y «Volver a la traducción automática»; con `talend: null` contiene «Sin traducción automática»; `TranslatorView` en estado inicial contiene el textarea, el botón «Traducir» y los tres ejemplos.
- [ ] **Step 2: Run** `bun test src/views/TranslatorView.test.tsx src/views/plans/ExpressionEditor.test.tsx`. Expected: FAIL.
- [ ] **Step 3: Implement** los dos componentes, la ruta y el enlace de menú, y el montaje por expresión en `StepInstructions`.
- [ ] **Step 4: Run** `bun test && bun run typecheck`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(web): laboratorio del traductor y edición de expresiones por paso`.

---

### Task 11: Centro de mando en el Resumen: etapas, siguiente acción y qué falta

**Files:**
- Create: `apps/web/src/components/ProjectStepper.tsx`, `apps/web/src/views/summary/ProjectCommandCenter.tsx`, `apps/web/src/views/summary/PendingPanel.tsx`
- Modify: `apps/web/src/views/SummaryTab.tsx` (monta `ProjectCommandCenter` bajo el `<h1>`; recibe `refreshKey`), `apps/web/src/styles.css`
- Test: `apps/web/src/components/ProjectStepper.test.tsx`, `apps/web/src/views/summary/PendingPanel.test.tsx`

**Interfaces:**
- Consumes: `api.progress`, `api.pendingSummary`, `nextActionHref`, `stageTone`, `pendingTotals`, `Badge`, `Load`, `link`.
- Produces:
  - `ProjectStepper({ stages }: { stages: ProjectStage[] })`: lista ordenada de 6 etapas, cada una con su nombre, detalle e insignia por `stageTone`; la etapa `current` lleva `aria-current="step"`.
  - `PendingPanel({ id, groups }: { id: string; groups: PendingGroup[] })`: encabezado «Qué falta» con `pendingTotals` («N pasos en M Jobs»), un `<details>` por grupo con el motivo, el número de pasos y la lista de Jobs que enlaza a `link(id, "planes", program)`; vacío → «No quedan pendientes.»
  - `ProjectCommandCenter({ id, refreshKey }: { id: string; refreshKey?: number })`: carga `progress` (y `pendingSummary` solo cuando la etapa `guides` está hecha; un 409 se trata como «sin guías»), muestra `ProjectStepper`, el botón principal «<next.label>» con `nextActionHref` y `next.reason`, y `PendingPanel`; recarga cuando cambia `refreshKey`.

- [ ] **Step 1: Write the failing test:** `ProjectStepper` con una etapa `current` contiene `aria-current="step"` exactamente una vez y las 6 etiquetas; `PendingPanel` con dos grupos contiene los motivos, «3 pasos en 2 Jobs» y un enlace `#/p/<id>/planes/<programa>`; con `groups=[]` contiene «No quedan pendientes.».
- [ ] **Step 2: Run** `bun test src/components src/views/summary`. Expected: FAIL.
- [ ] **Step 3: Implement** los tres componentes y montarlos en `SummaryTab`.
- [ ] **Step 4: Run** `bun test && bun run typecheck`. Expected: PASS.
- [ ] **Step 5: Commit** `feat(web): centro de mando del proyecto con etapas, siguiente acción y pendientes`.

---

### Task 12: Documentación

**Files:**
- Modify: `docs/conventions.md` (§3, fila «Job»: «`<proyecto>_<programa>`» pasa a describir la plantilla `job_{programa}` por defecto y que se edita en Configuración y por Job), `docs/agent-guide.md` (receta: «ediciones humanas sobre el plan»: tablas, `load_plans(with_edits=…)`, y que `plans.json` nunca lleva ediciones), `docs/progress.md` (entrada de la fase 1), `README.md` (la lista de funciones, si enumera pantallas)
- Test: ninguna (documentación).

- [x] **Step 1:** Actualizar los archivos de arriba; `docs/progress.md` anota qué opciones de la hoja de ruta quedaron hechas (1, 2, 3, 8, 9, 10, 19, 20).
- [x] **Step 2:** Comprobar enlaces relativos con `grep -rn "portal-ux" docs README.md` (los dos documentos nuevos deben encontrarse).
- [ ] **Step 3: Commit** `docs: fase 1 de UX (ediciones sobre el plan, plantilla de nombres, centro de mando)`.

---

### Task 13: Verificación completa y revisión visual

**Files:** ninguno (o correcciones menores que salgan de aquí).

- [x] **Step 1:** `uv run pytest -q`, `cd apps/web && bun test && bun run typecheck`. Expected: todo en verde, sin regresiones frente a la línea base de la Tarea 0.
- [x] **Step 2:** Como `to_mcp_arguments` cambió (`description`), comprobar el contrato: `uv run pytest tests/integration/test_mcp_contract.py -q` (arranca el MCP real con el preset `portal`). Si el MCP rechaza `description` personalizada, dejar el campo solo en el portal y documentarlo en `docs/progress.md`; no cambiar el MCP sin pasar por `AGENTS.md` («Regla de oro»).
- [ ] **Step 3:** Revisión visual con el skill `visual-tester` sobre `uv run sgm dev` (sin `--no-mcp` solo si Studio está abierto): capturas de Resumen (centro de mando), guía de un Job (identidad editable y editor de expresión), lista del plan con el diálogo de renombrado, Configuración (plantilla) y `#/traductor`, en ancho de escritorio y de móvil (≤ 600 px). Corregir lo que se vea roto. **Pendiente:** esta sesión no tiene navegador ni Playwright; se sustituyó por `bun run build` (pasa) y queda por hacer con el entorno levantado.
- [ ] **Step 4:** Rebasar sobre el `main` actual (que ya puede traer el reintento de análisis): `git rebase main`, resolver conflictos en `apps/api/main.py` y `store.py` conservando ambos cambios, y repetir el Step 1.
- [ ] **Step 5:** Informar a la persona dueña: qué repos se tocaron (solo el portal; el MCP no), qué quedó sin commitear o sin empujar, y qué opciones de la hoja de ruta siguen pendientes. No hacer `push`.
