# Progreso

## Estado validado

| Área | Estado | Evidencia y límites |
| ---- | ------ | ------------------ |
| SAS Grid / Joseph | Integrado, cobertura parcial | Catálogo v1: 10 entradas (0 `supported`, 7 `partial`, 3 `unsupported`). El planner consume catálogo y mappings; cada patrón de la matriz produce recomendación/estado con motivo y archivo/línea. |
| API / Andres | Flujo API validado | Prueba de integración cubre ZIP multiarchivo, análisis, plan, evidencia, progreso y exportación. El progreso se conserva en la base del proyecto. |
| Web / Byron | UI integrada; E2E pendiente de ejecución | ZIP, resumen, navegación a job/guía, evidencia, estados, catálogo Talend, enlaces de exportación y adaptación móvil implementados. `bun test` y build pasan. El runner Playwright está actualizado, pero Playwright no está instalado en este entorno. |
| Validación automatizada | Suite Python y web verificadas (28/10/2026) | `pytest -q`: 680 passed, 1 skipped, 1 failed (`test_talend_catalog`: la regla local declara 870 componentes y el JSON modificado trae 634); `ruff check`: limpio salvo `F841` en `migration_planner/progress.py`, de cambio local ajeno; `bun test`: 81 passed; `bun run typecheck` y `bun run build`: pasan. E2E de Playwright sigue pendiente de ejecución. |
| Talend Studio | Conectado y verificado (28/10/2026) | Studio 8.0.1 con el Bridge `readWrite`. El portal lista 55 Jobs, crea y lee Jobs, y los fixtures P0 se aplican como borradores en `Process/PruebasPortal`. Los errores de Studio se informan en `design_errors`. No se afirma equivalencia SAS ↔ Talend: eso sigue siendo manual (`docs/equivalence-testing.md`). |

## Portal UX, fase 1 (28/10/2026)

Opciones 1, 2, 3, 8, 9, 10, 19 y 20 de la hoja de ruta de
[`2026-10-28-portal-ux-design.md`](superpowers/specs/2026-10-28-portal-ux-design.md):

- Nombre y descripción del Job editables, con validación de identificador, longitud y duplicados; la
  carpeta destino se muestra en la guía.
- Renombrado masivo por prefijo, sufijo, reemplazo o regex, con vista previa y aplicación todo o nada.
- Plantilla de nombres en Configuración (`job_{programa}` por defecto) con ejemplo en vivo; se aplica
  al preparar o actualizar las guías.
- Laboratorio del traductor en `#/traductor` y edición de la expresión Talend por paso, con
  «volver a la traducción automática».
- Centro de mando en el Resumen: seis etapas, siguiente acción y pendientes agrupados por motivo.

Las ediciones se superponen al cargar y no se escriben en `plans.json`; regenerar las conserva si el
SAS coincide y las ignora si cambió. Estado verificado: `pytest` 680 pasan, 1 omitida y un fallo
ajeno en `test_talend_catalog` (la regla local declara 870 componentes y el catálogo cargado trae
634); `bun test` 81 pasan y `typecheck` pasa. Pendiente: revisión visual con navegador y rebase sobre
`main`.

## Cobertura Grid

Los conteos describen entradas del catálogo, no ocurrencias ni porcentaje del universo SAS Grid. Se añadió [`docs/sas-grid-support.md`](sas-grid-support.md), basado entre otras fuentes en *Grid Computing in SAS 9.4, Fifth Edition* (PDF oficial local, ignorado por Git). La referencia confirma argumentos como `-GRIDJOBNAME`, `-GRIDWAITRESULTS` y el paso de opciones de proveedor mediante `-GRIDJOBOPTS`; no confirma el entorno objetivo del proyecto. Las formas `sasgsub` del fixture siguen siendo ilustrativas: las recomendaciones relacionadas permanecen `partial`; LSF y opciones desconocidas/incompletas quedan `unsupported` con motivo y evidencia. No elevar estados hasta identificar versión/proveedor y contrastar scripts representativos.

La suite omitió una prueba de importación de symlink porque Windows no concede el privilegio requerido en este entorno. La protección de symlinks no se declara validada aquí.

## Límites pendientes

- Ejecutar `.claude/scripts/e2e_web.mjs` con Playwright instalado y servicios web/API activos; confirmar upload, errores, navegación, progreso tras recarga, descarga, teclado y viewport móvil.
- Verificar nombres/opciones Grid con documentación o scripts representativos de una versión identificada.
- Probar casos representativos en Talend Studio y registrar versión, pasos, evidencia y resultado. Hecho con los fixtures P0 y P1; falta con programas reales.
- Abierto: Studio marca los `tMap` sin mapeo con "Unknown value in the list [Mapping links display as:]" en la vista Problemas (aparece en `design_errors`). Descartado: el `.item` guarda `LINK_STYLE=AUTO`; ningún valor (`AUTO`, `LINE`, `BEZIER_CURVE`) ni reconfigurar el nodo, cerrar y reabrir el editor o refrescar el workspace lo limpia; solo desaparece si el `tMap` recibe una conexión. Pendiente: abrir el Job en la interfaz de Studio para ver si la marca es real, y depurar el plugin Java (`JobProblems`).
- Resuelto: si la aplicación falla a mitad, el MCP borra los Jobs que creó en esa llamada y el error lo indica; los Jobs que ya existían no se tocan.
- Resuelto: el generador añade `tLogCatcher` + `tLogRow` y, si hay un componente de inicio, `tDie` por `SUBJOB_ERROR` (`BP-ERR-01`); ver `docs/talend-best-practices.md`.
- Ningún componente se marca verificado solo por una inspección viva: `talend-mcp` está conectado, pero el piloto con programas reales sigue pendiente.
- El piloto con programas reales del cliente sigue pendiente (`docs/pilot-report.md`).

## Corrida masiva contra Studio (28/10/2026)

Proyecto sintético `bancolombia_sas_synthetic_orchestration` (7 programas y un orquestador), aplicado por el flujo de lote
contra Studio 8.0.1: **8 de 8 Jobs creados** en 43 s, todos como `partially_applied` (borradores con pendientes de esquema
y de expresiones SAS). La primera pasada creó 6 de 8; lo que falló y se corrigió en el MCP y el plugin:

- Conectar dos `tFilterRow` seguidos (dos `WHERE` encadenados) se rechazaba: el validador buscaba la entrada en el conector `FILTER`, que es solo de salida.
- Esa misma conexión abre en Studio el diálogo modal "Do you want to get the schema of the target component?" que dejaba el hilo de interfaz colgado. El plugin lo contesta con No, y el MCP atiende los diálogos conocidos mientras conecta.
- `talend_job_problems` y la aplicación abrían el editor de cada Job y no lo cerraban; en lotes grandes saturaban Studio. Ahora cierran los editores que ellos abrieron (nunca uno que ya estaba abierto).

Abierto: la vista Problemas sigue marcando `tMap` (`LINK_STYLE`) y `tFilterRow` (`LOGICAL_OP`) borradores con "Unknown value in the list", aunque lo guardado en el `.item` coincide con lo que escribe Studio (`AUTO` y `&&`). Parece la caché en memoria de Studio; se confirmaría reiniciándolo y reabriendo uno de los Jobs.

### Corpus reales aplicados contra Studio (28/10/2026)

| Corpus | Programas | Resultado |
| ------ | --------- | --------- |
| `bancolombia_sas_synthetic_orchestration` | 8 | 8 creados |
| `ts-sas-legacy-analytics` (ETL banca y seguros) | 18 | 18 creados |
| `sas-access-samples` | 8 | 8 creados |
| `cmmi-shadow-bundles` | 4 | 4 creados |
| `ci360-download-client` | 4 | 4 creados |
| `learning-sas-by-example` | 3 | 3 bloqueados por tamaño (167, 205 y 500 componentes) |

Lo que fallaba y se corrigió: `tFilterRow` encadenados; el diálogo de esquema que colgaba la interfaz; editores sin cerrar que saturaban Studio; un trigger hacia un componente que no inicia subjob (`customer_profitability`); `tUnite` (entradas ilimitadas); nombres de Job repetidos entre carpetas (cuatro `bulkload.sas`). Un Job de 500 componentes agota el tiempo y dejaba restos, así que el API rechaza los de más de `TALEND_MAX_COMPONENTS` (200 por defecto) con un mensaje que pide dividir el programa.

## Verificación en Studio con el modo offline (28/10/2026)

`scripts/verify_in_studio.py` sobre todos los corpus, con escritura offline por defecto y sin errores inesperados de Studio:

| Corpus | Jobs | Tiempo | Antes (en vivo) |
| ------ | ---- | ------ | --------------- |
| `bancolombia_sas_synthetic_orchestration` | 8 | 19 s | 71 s |
| `ts-sas-legacy-analytics` | 18 | 39 s | 105 s |
| `tmsis-analytic-file` | 13 | 45 s | 71 s |
| `sas-access-samples` | 8 | 31 s | 51 s |
| `cmmi-shadow-bundles` y `ci360-download-client` | 4 + 4 | 16 s y 15 s | 27 s y 37 s |
| `sas_synthetic_customer360_multisource_v2` | 8 | 38 s | sin medir |
| `learning-sas-by-example` (3 programas, 47 Jobs con los hijos) | 47 | 56 s | 366 s y un Job de 500 componentes que fallaba |

Los Jobs nacen sin los errores de `tMap`, `tFilterRow` (`LOGICAL_OP`) ni `tRunJob` que producía montar los nodos por la API.
Quedan los pendientes esperados de un borrador (`Valores` vacíos, esquemas sin definir). Puertas automáticas sin Studio:
`tests/integration/test_corpus_gate.py` y `tests/integration/test_adversarial_projects.py`; ver `docs/production-readiness.md`.

Abierto: tras decenas de pruebas seguidas con los mismos nombres, la sesión de Studio devolvió errores de un Job anterior para
`job_02_load_accounts` (el mismo spec con otro nombre salió limpio); se despeja reiniciando Studio.

## Traductor de expresiones — MIG-009 (28/10/2026)

Las comparaciones que involucran columnas sin un tipo conocido ya no emiten una expresión Java candidata. El plan conserva
las condiciones simples de `tFilterRow` cuando se pueden representar, pero las deja como borrador con advertencia de tipos,
conversión y semántica de missing/nulos. Esto cubre comparaciones columna-columna, columna-literal y `IN`; no se ejecutaron
SAS, código importado, Studio ni Jobs Talend.

Métrica antes (`f4d3630`) → después: `real`, 8,1 % → 8,1 % (2 063 pasos; sin esquema 1 750 → 1 749; 627 expresiones);
`synthetic`, 16,8 % → 16,8 % (429 pasos; 303 sin esquema; 95 expresiones). No aumenta la automatización: se prioriza no
promover comparaciones cuyo tipo no puede demostrarse. Verificación: `uv run pytest -q` (556 passed, 1 skipped) y Ruff.
La comprobación en Studio queda pendiente por el límite de ejecución de esta tarea.

## Importación ZIP — MIG-029 (28/10/2026)

Se añadió `max_zip_members` (10 000 por defecto; configurable con `SGM_MAX_ZIP_MEMBERS`) y el importador rechaza el ZIP
completo cuando supera la cuota, antes de ordenar, extraer o acumular miembros omitidos. Python `ZipFile.infolist()` aún
materializa la tabla central, así que el límite no elimina el coste inicial de metadatos. Prueba sintética offline para
excedentes compuestos solo por rutas inseguras. Métricas antes → después: `real` 8,1 % → 8,1 % (2 063 pasos), `synthetic`
16,8 % → 16,8 % (429 pasos); cambio no relacionado con automatización SAS. Verificación focal: 20 passed, 1 skipped;
Ruff pasó. Sin SAS, código importado, Studio ni Jobs Talend.

## Aplicación offline Talend — MIG-023 (28/10/2026)

El fallback a Studio queda limitado a fallos de `dryRun`; un error durante la escritura se devuelve sin repetir la operación
por otra vía. El batch crea los dos ficheros con exclusión y revierte el `.item` nuevo si falla el `.properties`. Para una
respuesta perdida tras una escritura completa, el portal añade una marca SHA-256 de propiedad; el batch reconoce en el
reintento el par que conserva esa misma marca y no sobrescribe un Job distinto. Métrica antes → después: `real` 8,1 % →
8,1 % (2 063 pasos), `synthetic` 16,8 % → 16,8 % (429 pasos). Verificación focal offline de Python y MCP; la simulación
de timeout posterior a persistencia completa no se ejecutó. Sin Studio ni Jobs Talend.

## Cola de procesamiento API — MIG-031/032 (28/10/2026)

El retry de un proyecto ahora usa una transición SQLite condicional (`failed`/`interrupted` → `queued`) antes de programar
la tarea; una petición concurrente perdedora recibe HTTP 409 y devuelve su reserva de capacidad. El worker también incluye
la creación de `Store` dentro del `try/finally`, de modo que un fallo al inicializarlo libera el slot activo. Pruebas
offline con `Store` temporal, dos peticiones sincronizadas y un inicializador falso; no se ejecutó pipeline SAS. La métrica
de automatización no cambia: `real` 8,1 % (2 063 pasos), `synthetic` 16,8 % (429 pasos).

## Traductor a componentes de Talend: pruebas — A4 (28/10/2026)

`tests/unit/test_talend_translator.py` fija el Java que emite el traductor para cada función del mapeo (texto, aritmética,
agregados, condicionales, perdidos, fechas, formatos) y añade una prueba de contrato: toda llamada `Rutina.metodo(...)` del
Java emitido debe existir en las rutinas de sistema de Studio 8.0 (`StringHandling`, `TalendDate`, `Mathematical`,
`Relational`), y ninguna expresión puede mencionar una rutina propia. Si alguien inventa un método, la prueba falla.

Al escribir las pruebas se corrigieron dos defectos del traductor:

- `max`/`min` con todos los argumentos perdidos devolvían un `NullPointerException` en Java; en SAS dan perdido.
- `round` usaba `Math.round`, que lleva `-2,5` a `-2`; SAS redondea fuera del cero (`-3`).

El interruptor `SGM_TALEND_EXPRESSIONS` sigue apagado: no se ha comprobado en Studio que el Java emitido compile (B1).
No se re-midió `tools/automation_metrics.py` porque nada del camino por defecto cambió (el traductor sigue inactivo).
Verificación: `uv run pytest -q` (591 passed, 1 skipped) y Ruff limpio. Sin SAS, Studio ni Jobs de Talend. Repos tocados:
solo el portal; sin commitear.

## Persistencia de artefactos — MIG-033 (28/10/2026)

Análisis, dependencias y planes ahora se escriben en un archivo temporal dentro del mismo directorio, se sincronizan con
`fsync` y se publican mediante `os.replace`; las rutas de API que guardan planes verificados usan el mismo mecanismo.
Una falla antes del reemplazo deja intacto el JSON anterior. Prueba parametrizada con `Store` temporal e inyección de
fallo al reemplazar para cada uno de los tres artefactos; los loaders aún leen el documento previo y no quedan temporales.
La suite focal relevante pasó (46 tests) y Ruff pasó para los archivos del lote. La suite completa sigue con los dos fallos
de cobertura del planner ya reportados (591 passed, 1 skipped). Los artefactos que ya estuvieran corruptos por versiones
anteriores no se reparan automáticamente. Sin SAS, Studio ni Jobs Talend.

## WP2 y WP3: datos incrustados y política de reportes (28/10/2026)

Métricas con `tools/automation_metrics.py` sobre `tests/fixtures/sas/real`:

| Medida | Antes | Después |
| ------ | ----- | ------- |
| Automatizados | 8,1 % | **28,1 %** |
| Pasos | 2 063 | 1 903 |
| Sin esquema | 1 749 | 1 527 |
| `report` con pendientes | 238 de 238 | **0** |
| `inline_data` con pendientes | 161 de 161 | 99 |
| `compute` con pendientes | 178 de 178 | 111 |
| `read_file` | 206 (206 con pendientes) | 46 (46) |

- **WP3 · Política de reportes.** `Settings.report_policy` (`SGM_REPORT_POLICY`, valor por defecto `log`) y el planificador
  eligen el componente: `log` → `tLogRow` con `BASIC_MODE`, sin pendiente; `csv` → `tFileOutputDelimited` con la ruta como
  pendiente y variable de contexto `path_<reporte>`; `discard` → sin componente, paso `descartado` y nota de qué se perdió.
  Una política desconocida falla en vez de caer en un valor supuesto. Documentada en `docs/conventions.md`, sección 6.
- **WP2 · Datos incrustados.** El lexer conserva las filas de `datalines`/`cards` (antes las descartaba), el parser las
  lleva al `DataStep`, el IR las pasa al paso y el planificador arma `tFixedFlowInput` con `USE_SINGLEMODE`, `NB_ROWS`,
  tabla `VALUES` y esquema (`String` para `$`, `Double` para numérico). No se inventa nada: entrada por columnas o punteros
  (`@1`, `#2`), filas que no cuadran con el `INPUT`, bloque vacío o sin `INPUT` siguen como pendiente con su motivo.
  Además, un `DATA` con `datalines` ya no genera un `read_file` paralelo: era el mismo trabajo contado dos veces.
- **WP7 (parte).** El tipo de cada columna calculada sale de la expresión (aritmética → `Double`, texto → `String`,
  comparación → `Boolean`, fecha → `Date`); `compute` baja de 178 a 111 pasos con pendientes. Lo que el traductor no sabe
  tipar sigue pidiendo el esquema.

Pruebas nuevas: `tests/unit/test_report_policy_and_inline_data.py` (10) y `tests/unit/test_talend_translator.py` (25).
Verificación: `uv run pytest --ignore=tests/integration` (482 passed, 1 skipped) y `tests/integration` (126 passed); golden
del plan regenerado con `UPDATE_GOLDEN=1` porque el pendiente de tipos desapareció. Ruff limpio en lo tocado.

**Para el 80 % falta el catálogo de entorno** (WP5, WP6, WP7): `write` 413, `read` 264, `read_file` 46 y 1 527 pasos sin
esquema no se pueden cerrar sin saber de dónde salen los esquemas, y la sección 10 del plan lo deja como decisión del
usuario. Después: `aggregate` 104, `macro_call` 62, `format_definition` 51, `unsupported` 45.

Nota de árbol: durante esta tanda otro agente modificó en paralelo `apps/api/*`, `apps/web/src/views/ProjectsView.tsx`,
`src/sas_grid_migrator/cli/dev.py`, `persistence/artifacts.py`, `dependency_graph/builder.py`, `sas_parser/analyze.py` y
añadió planes en `docs/superpowers/`. No los toqué. Sin commitear.

## WP4: PROC MEANS/FREQ y PROC FORMAT (28/10/2026)

`real` con `tools/automation_metrics.py`: **30,0 %** de pasos automatizados (1 903 pasos; antes de esta tanda 28,1 %).
`synthetic`: 22,0 % (428 pasos). Totales frente a la línea base: **8,1 % → 30,0 %**.

- **PROC MEANS/SUMMARY → `tAggregateRow`.** Grupos de `CLASS` y `BY`, variables del `VAR`, estadísticas pedidas y los
  nombres de salida del `OUTPUT OUT=`; sin `OUTPUT`, las estadísticas por defecto de SAS (`N`, `MEAN`, `STD`, `MIN`, `MAX`).
  `aggregate`: 104 → **75** pasos con pendientes.
- **PROC FREQ → `tAggregateRow`.** Una única tabla simple (`tables a * b`) da los `GROUPBYS` y `COUNT`; varias tablas u
  opciones (`/ nocol`) quedan pendientes. PROC TABULATE y UNIVARIATE quedan pendientes: su salida no es una fila por grupo.
- **PROC FORMAT → tabla de lookup.** Un formato de valores sueltos ya no deja pendiente. Los formatos con rangos
  (`30-50`, `51-high`, `low-<13`), comparaciones, `OTHER` o clave vacía (el valor perdido) siguen pendientes con el motivo:
  necesitan lógica, no una tabla. `format_definition`: 51 → **44**.
- Se corrigieron tres trampas antes de darlas por buenas: `OUTPUT` con un solo nombre para varias variables (SAS exige
  `AUTONAME`), el rango `30-50` (la detección miraba solo el primer carácter y lo daba por valor suelto) y la clave vacía
  de un formato numérico, que es el valor perdido. Sin esas correcciones la métrica habría subido un punto de más con pasos
  mal traducidos.

Pruebas nuevas: `tests/unit/test_aggregate_and_formats.py` (20), incluidos los casos que deben seguir pendientes.
Verificación: `tests/unit/test_planner.py`, `test_golden.py`, `test_parser.py`, `test_ingestion.py`,
`test_offline_file_configuration.py`, `test_talend_offline_payload.py`, `test_talend_apply_spec.py`,
`test_automation_metrics.py`, `test_talend_translator.py` (25), `test_report_policy_and_inline_data.py` (10),
`test_aggregate_and_formats.py` (20) y `tests/integration/test_corpus_gate.py`: 226 pasan, 1 omitido. Golden del plan
regenerado (`p0_clientes_activos` pierde el pendiente de tipos). Ruff limpio en lo tocado.

Aviso de árbol: el otro agente sigue editando `store.py`, `apps/` y añadiendo pruebas en paralelo. En una corrida completa
aparecieron fallos intermitentes en `test_store_overrides.py` y en los tests de iconos, que pasan en aislamiento y con
`test_planner.py`: no son de este cambio y no los toqué.

Lo que falta para el 80 % sigue igual: `write` 413, `read` 264 y 1 488 pasos sin esquema necesitan el catálogo de entorno
(WP5), y eso depende de las decisiones de la sección 10.

## Corrida de la métrica honesta, condicionales y catálogo de entorno (28/10/2026)

Tres cosas en esta tanda, y la primera es una corrección que **baja** la cifra:

- **Condicionales de `compute`.** Los `IF/THEN/ELSE` de un DATA step se traducían a una expresión con `talend=None` y el
  paso seguía contando como automatizado. Eran **55 pasos con un hueco silencioso**. Ahora: si la condición y las dos ramas
  se traducen, sale una ternaria de `tMap` (`(cond ? a : b)`; sin `ELSE`, `null`, que es el perdido de SAS) y el tipo sale
  de la rama verdadera; si no, el paso queda pendiente con el motivo. `compute` pasa de 111 a **165** pasos con pendientes
  y la métrica global baja de 30,0 % a **27,2 %**. Es el número real: los otros 55 no estaban automatizados.
- **WP5 · Catálogo de entorno.** `src/sas_grid_migrator/environment/` con modelo y validación (motores tomados de
  `rules/mappings/talend-components.json`, tipos de Talend admitidos, datasets huérfanos, delimitador obligatorio en un
  archivo delimitado, versión de esquema). `schemas/environment.schema.json` versionado y ejemplo en
  `rules/environment/learning-sas-by-example.json`. Las credenciales no se guardan: solo el nombre del grupo de contexto.
- **WP6 (parte).** Con catálogo, `read`/`write` toman la tabla física, las columnas con su tipo y el componente del motor
  aunque el SAS no traiga el `LIBNAME`; dejan de pedir esquema y destino. La acción al escribir pasa a ser del proyecto
  (`Settings.table_action`, `SGM_TABLE_ACTION`, por defecto `drop_create`, que es lo que hace SAS), así que desaparece el
  pendiente «Confirmar la acción sobre la tabla». Una acción desconocida queda pendiente en vez de suponerse.

Métricas (`tools/automation_metrics.py`; modo nuevo `--environment archivo.json` para medir con entorno conocido):

| Corpus | Antes de la tanda | Después | Con catálogo de ejemplo |
| ------ | ----------------- | ------- | ----------------------- |
| `real` | 30,0 % (falso) | **27,2 %** | **28,3 %** |
| `synthetic` | 22,0 % | 22,0 % | — |

El catálogo de ejemplo solo declara dos datasets, así que su efecto en un corpus de 50 programas es pequeño: lo que
demuestra es el mecanismo. Con los esquemas reales del cliente (decisión pendiente, sección 10 del plan) es donde `read`,
`write` y los 1 497 pasos sin esquema se cierran.

Pruebas nuevas: `tests/unit/test_conditionals.py` (5) y `tests/unit/test_environment_catalog.py` (14, incluida la
sincronía del esquema JSON). Verificación: `uv run pytest --ignore=tests/integration` → 544 pasan, 1 omitido, 1 fallo ajeno
(`test_talend_catalog.py::test_api_catalog_exposes_only_current_studio_8_components`, espera 870 componentes y recibe 634;
viene de `apps/api/integrations.py` y del catálogo del MCP que está editando el otro agente). Golden del plan regenerado:
desaparece el pendiente de la acción al escribir.

Sin commitear. Repos tocados: solo el portal.
