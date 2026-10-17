# Arquitectura

## Principios

- Python analiza y propone. `talend-mcp` inspecciona (solo lectura). El desarrollador construye y valida en Talend Studio.
- Análisis estático: nunca se ejecuta código SAS, macros ni scripts importados.
- El análisis SAS funciona sin `talend-mcp` conectado.
- Nunca afirmar que un componente o propiedad existe sin verificarlo (`verified: false` por defecto).
- Modelo intermedio tipado entre parser y planner; las reglas viven en `rules/`, no en condicionales dispersos.
- Aplicación única modular: sin microservicios, colas, Kubernetes ni BD externa. Persistencia: SQLite + JSON.

## Pipeline

1. Ingestion: manifiesto (rutas relativas, hashes, codificación).
2. Parser SAS a nivel de sentencia/paso (`sas_parser`: lexer propio + constructor de pasos DATA/PROC/macros + cláusulas de PROC SQL), con archivo/línea. No hay gramática de expresiones; Lark/ANTLR quedan para cuando F4 necesite parsear expresiones.
3. Resolución de macros (`%LET`, `%MACRO`, `%INCLUDE` estático).
4. Análisis semántico: tablas, columnas, filtros, joins, agregaciones.
5. Dependencias (NetworkX): programas, macros, datasets, archivos; ciclos y referencias faltantes.
6. Análisis de Grid: modelo de ejecución separado del modelo de procesamiento.
7. Clasificación: traducible / requiere contexto / no soportado, con severidad y confianza.
8. Planificación: reglas de migración → plan por Job.
9. Contraste con Talend vía `talend_adapter` (lectura).
10. Validación y reportes (Markdown, JSON, CSV/XLSX).

## Integración talend-mcp

Repo existente: https://github.com/AndresGaibor/talend-mcp (HTTP :3927 por defecto o stdio). Solo herramientas de inspección (`talend_list_jobs`, `talend_read_job`, `talend_list_components`, `talend_show_flow`, `talend_inspect_component`, `talend_inspect_job`, contextos). Modificación y `talend_run_job` quedan deshabilitadas en el adaptador. Antes de implementar el adaptador, inspeccionar los nombres y esquemas reales del servidor (F0/F5).

## Fuera del MVP

Generación de `.item`, ejecución de SAS, edición automática de Jobs, traducción universal de PROCs, reproducción total de la planificación Grid, conexión a bases de producción, orquestación distribuida, agente que apruebe sus propias traducciones. LLM opcional, nunca requisito.

## Fases

| Fase | Contenido |
| ---- | --------- |
| F0 | Corpus de prueba, matriz de cobertura, revisión real de talend-mcp |
| F1 | Backend: modelos Pydantic, CLI, API, importación segura, SQLite |
| F2 | Parser e inventario semántico |
| F3 | Grafo de dependencias y Grid |
| F4 | IR, reglas versionadas, planes y reportes |
| F5 | Adaptador Talend MCP |
| F6 | Frontend React + TS + Vite + Bun |
| F7 | Validación, endurecimiento, piloto |

Primer hito: un comando que recibe una carpeta de `.sas` y genera inventario, grafo de dependencias y plan de construcción Talend verificable.

## Decisión F2: parser a nivel de sentencia

SAS no tiene una gramática limpia (macros reescriben el código, sentencias dependen del contexto del paso). El parser no expande macros: divide en sentencias respetando comentarios, cadenas, `%str(;)` y bloques `datalines`, agrupa en pasos y extrae datasets de entrada/salida, `BY`, `WHERE`, cláusulas SQL y etiquetas de construcción (`constructs`). `rules/sas/constructs.json` mapea cada etiqueta a P0/P1/P2; los hallazgos P1/P2 llevan archivo y línea (en DATA steps, la línea de la sentencia concreta). Sentencias sueltas dentro de macros (código que solo tiene sentido al expandirse) se cuentan como `macro_fragment`, no como error.

Medido sobre el corpus (58 programas, 7231 sentencias): 2 no reconocidas fuera de macros (ejercicios incompletos de un libro) y 164 fragmentos de macro.

## Decisión F3: dependencias y Grid

- **Resolución estática** (`macro_resolver`): índice de macros del proyecto, constantes `%LET` de primer nivel (solo si tienen un único valor en todo el proyecto) y casado de rutas `%INCLUDE`/programa por sufijo de ruta. `resolved` exige ≥2 componentes coincidentes; si solo coincide el nombre de archivo queda como `candidate` y no se enlaza. Lo dinámico (`&param`) se informa como `dataset_dynamic`/`include dinámico`, nunca se adivina.
- **Grafo de procesamiento** (`dependency_graph`, NetworkX): cada programa y cada macro es una unidad con lecturas/escrituras propias; el efectivo de un programa se obtiene por cierre transitivo sobre macros llamadas e includes. Aristas programa→programa por dataset (productor→consumidor) e include (incluido→includer). Los datasets `work.*` no enlazan programas distintos. `processing_order` son capas (programas independientes dentro de una capa); los ciclos son componentes fuertemente conexos. Rol de dataset: `source` (nadie lo produce en el proyecto), `intermediate`, `final`, `temporary` (work).
- **Orquestación** (`grid_analysis`), separada de los datos: tareas desde scripts shell (`sasgsub`, `sas -sysin`, `-set`, cola, nombre, `-gridwaitresults`, condición `[ $? -eq 0 ] &&`) y desde *macros orquestadoras* (macro que hace `%include "&param"`: cada llamada es un paso, con sus argumentos). `after` es secuencia inferida (`inferred: true`); también se extrae `Schedule:` (p. ej. Control-M) de los comentarios de cabecera.
- Un `WAIT` o `after` entre tareas es una dependencia de orquestación; no se convierte en conexión de filas.

Medido sobre el corpus: 58 programas, 372 datasets, 6 tareas de macro orquestadora resueltas contra los programas del proyecto (banca y seguros), 9 planificaciones Control-M.

## Decisión F4: IR y planes

- `intermediate_representation`: operaciones tipadas (`read`, `join`, `aggregate`, …) con ids estables `op_{línea}_{tipo}_{n}`, evidencia `archivo:línea` y confianza. Sin ejecución ni expansión de macros.
- Reglas en `rules/mappings/talend-components.json` (versionadas). Nombres de componente y propiedad son **candidatos** hasta que talend-mcp los confirme.
- Traductor SAS→Java conservador (`migration_planner/expressions.py`): si no es seguro devuelve `talend=None`; avisa de semántica de missing numérico.
- Un plan por programa (`JobPlan`); macros → jobs hijos; `%let` → variables de contexto; librerías → conexiones por crear sin credenciales.
- Decisiones humanas (estado/nota por paso) viven en SQLite (`step_state`) y se superponen al regenerar; reimportar borra planes.
- Exportación: Markdown por Job + `index.md` + `steps.csv` + JSON (schema en `schemas/migration-plan.schema.json`, sincronizado por test).

## Decisión F5: adaptador Talend

- `talend_adapter/adapter.py`: `TalendAdapter` sobre un `Caller` (HTTP vía `mcp.Client`); cada llamada pasa por `policy.assert_allowed`. Sin Talend, `health_check` devuelve `available: false` y el resto del sistema funciona.
- Entradas reales (del código de talend-mcp): `talend_inspect_job{jobPath}`, `talend_inspect_component{jobPath,uniqueName}`, `talend_list_components{jobName}`, `talend_read_contexts{jobName}`. Respuesta: envoltorio `{ok, data|error}`.
- No existe catálogo global. `verification.py` construye un catálogo desde Jobs de referencia y marca `verified` solo si el componente y todas las propiedades del paso aparecen ahí.
- Limitación: el clon revisado de talend-mcp no arranca (`Tool duplicada: talend_bridge_select_component`), así que el adaptador se validó contra su código y mocks, no contra un servidor vivo. Además `inspect_component` en ese código devuelve un componente vacío; el adaptador descarta componentes sin `componentName`.

## Catálogo de componentes Talend

- `rules/talend/components.json` (577 componentes, 91 familias): generado por `tools/build_talend_catalog.py` desde las definiciones XML de Talaxie (Apache-2.0). Por componente: descripción, familias, conectores (FLOW/REJECT/ITERATE/…), parámetros con **nombre interno**, etiqueta, campo, requerido, valor por defecto, opciones de listas cerradas, columnas de tablas de parámetros y drivers (`imports`). `variants` agrupa tecnologías hermanas (tOracleInput ↔ tMysqlInput) solo para familias de bases de datos, nube y ficheros.
- Un nombre que está en el catálogo es un nombre real de Talend (`in_catalog`); `verified` sigue significando «contrastado en un Job real vía talend-mcp». Las propiedades de tMap son del editor del mapper y se marcan aparte; `generic_components` en las reglas lista los que existen en Studio pero no en el catálogo abierto (tDBInput, tHiveInput…).
- Documentación en prosa: `tools/fetch_talend_docs.py` descarga de help.qlik.com (resumen + «Standard properties» + subpáginas) a `docs/reference/talend/` (no se versiona: copyright de Qlik). 550 de 577 componentes tienen página; los 27 sin ella son internos (tMapIn, tSortIn…).
- API: `GET /api/talend/catalog[?q=&family=]`, `GET /api/talend/catalog/{componente}` (incluye la doc local si existe). UI: «Catálogo Talend».
- Test de coherencia: toda propiedad y componente de `rules/mappings` existe en el catálogo (encontró `KEY/VALUE` → `VARIABLES` y `CONTEXT_PARAMS` → `CONTEXTPARAMS`).

## API prevista

`POST /api/projects`, `POST /api/projects/{id}/imports`, `POST /api/projects/{id}/analyses`, `GET /api/projects/{id}/inventory`, `GET /api/projects/{id}/dependencies`, `GET /api/projects/{id}/programs` y `GET /api/projects/{id}/programs/{path}` (en lugar de `/api/programs/{id}`: el programa se identifica por proyecto + ruta), `POST|GET /api/projects/{id}/plans`, `GET /api/projects/{id}/plans/{path}[?format=md]`, `PATCH /api/projects/{id}/plans/{path}/steps/{step_id}`, `POST /api/projects/{id}/plans/verify`, `POST /api/projects/{id}/exports`, `GET /api/integrations/talend/health`, `POST /api/integrations/talend/inspect`.
