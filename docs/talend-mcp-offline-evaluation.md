# Evaluación: crear Jobs con Studio o en modo offline

Estado: **análisis de código del 2026-10-27, sin mediciones propias.** Las cifras de rendimiento salen de `talend-mcp/docs/MODO-OFFLINE.md`; la Tarea 7 del plan `docs/superpowers/plans/2026-10-27-talend-mcp-en-el-portal.md` las reemplaza por mediciones con guías reales del portal.

## Qué hace hoy el portal

`talend_job_apply_custom_spec` monta cada Job con la API de Studio: valida cada componente con `componentParameters`, abre el Job, agrega nodos y conexiones, y lee la vista Problemas. Eso exige Studio abierto con el Bridge, y el MCP serializa los montajes con un candado interno («Studio ocupado con otro montaje custom»). El lote del portal llama a esa tool una vez por Job.

## Qué ofrece el modo offline del MCP

Un Job es un par `NOMBRE_0.1.item` / `.properties` en `process/`. Las tools offline escriben ese par directamente:

| Tool | Hace |
|---|---|
| `talend_jobs_create_from_spec` | Crea un Job desde componentes y conexiones |
| `talend_jobs_create_batch` | Un Job por fila desde una plantilla `{{variable}}`, hasta 20 000, con `dryRun` |
| `talend_job_edit_offline` / `talend_jobs_edit_batch` | Lote atómico de operaciones (`add_node`, `set_params`, `set_schema`, `connect`, `set_context`, …) con diff |
| `talend_job_build_batch` | Genera y compila muchos Jobs sin abrir el editor (necesita Studio) |

Medido por el MCP (1 000 Jobs de dos componentes, Studio abierto): escribir 1,1 s, editar 0,9 s, compilar 268 s. Montar un Job con la API de Studio cuesta de 3,6 a 5,6 s por caso. Las garantías son: escritura atómica por Job, un fallo no frena el lote, `dryRun` con diff y negativa a pisar un Job abierto en un editor (`JOB_OPEN_IN_STUDIO`).

## Comparación con lo que el portal necesita

| Necesidad del portal | Studio (hoy) | Offline | Notas |
|---|---|---|---|
| Componentes, parámetros, esquemas, conexiones, contextos | Sí | Sí | Mismas formas de datos (`uniqueName`, `componentName`, `parameters`, `schema`, `connections`, `contexts`) |
| `mapper` de `tMap` | Sí | **No** | El portal lo envía; el MCP recomienda Studio para `tMap` |
| `tables` (parámetros de tipo TABLE) | Sí | **No** | `set_params` solo acepta cadenas |
| `draftOnly` / `draftReason` | Sí | Sin soporte | Se omite si el componente no está en el catálogo local |
| `childJobs` (Jobs hijos recursivos) | Sí | **No** | Habría que recorrer el árbol en el nuevo motor |
| `instructions` | Solo entra en el hash de propiedad | Se puede ignorar, pero debe seguir entrando en el hash | `apply-custom-job-spec.ts` no la usa para otra cosa |
| `replaceManagedTodoContexts` | Sí | **No** | Reemplaza contextos vacíos `migration_todo_<12 hex>` en la reaplicación |
| Reanudar un Job propio (marca `[portal-spec:<hash>]`) | Sí | **No** | La marca vive en la descripción del Job; offline tendría que escribirla y leerla igual, y calcular el mismo hash que el motor Studio |
| Vista Problemas en la misma llamada | Sí | **No** | Offline requiere `talend_job_build_batch` para compilar |
| Funciona con Studio cerrado | **No** | Sí | Útil para pruebas y para el lote |
| Velocidad | Segundos por Job | Milisegundos por Job | |
| Seguridad frente a Jobs abiertos | Studio lo gestiona | Guardia `JOB_OPEN_IN_STUDIO` | Sin Bridge, la guardia no detecta nada |

## Recomendación

No sustituir Studio por offline: añadir un **motor offline opcional** para las guías que no usan `mapper` ni `tables`, con un modo `auto` que cae a Studio cuando la guía lo necesita. La decisión final depende de la Tarea 7 del plan:

- Se adopta `auto` si el motor offline es al menos 20 veces más rápido por Job, el `.item` resultante abre y compila en Studio, y `talend_inspect_job` devuelve los mismos componentes, conexiones y contextos que con el motor Studio.
- Se mantiene `studio` por defecto si menos de la mitad de las guías de los ZIP de prueba son elegibles (sin `mapper` ni `tables`) o si hay cualquier diferencia de paridad.

## Medición del 2026-10-27

### Elegibilidad (solo lectura, `tools/offline_eligibility.py`)

| ZIP | Guías | Elegibles | Bloqueos |
|---|---|---|---|
| `bancolombia_sas_synthetic_orchestration.zip` | 8 | 8 (100 %) | ninguno |
| `bancolombia_sas_synthetic_orchestration_talend_ready.zip` | 8 | 8 (100 %) | ninguno |
| `sas_synthetic_customer360_multisource_v2.zip` | 8 | 8 (100 %) | ninguno |

Ninguna guía de los tres ZIP usa `mapper`, `tables` ni `childJobs`: las 24 son elegibles para el motor offline.

### Tiempo del motor offline

Con el MCP arrancado con el preset `portal` contra un proyecto de prueba, tres guías aplicadas con `talend_jobs_create_from_spec` (escritura directa de `.item`/`.properties`, sin Studio): media 271 ms por Job, mediana 273 ms, rango 225–315 ms. El tiempo incluye la ida y vuelta MCP; la escritura en disco es una fracción de eso. La medición usó ese tool porque `talend_jobs_create_batch` exige una plantilla común y las guías del portal no comparten los mismos componentes.

### Línea base con Studio: no medible en este equipo

El motor Studio (`talend_job_apply_custom_spec`) falló de forma reproducible al aplicar la primera guía:

- `APPLY_FAILED: OPERATION_FAILED: No se pudo abrir el job recien creado: El item recien creado no esta en el arbol de recursos`
- `APPLY_FAILED: OPERATION_FAILED: org.eclipse.core.runtime.OperationCanceledException`

`talend_job_apply_custom_spec` no dejó ningún `.item` en el proyecto y `talend_jobs_list` no listó los Jobs creados. El diagnóstico de diálogos (`talend_studio_ui_dialogs`) muestra un modal bloqueante de Studio: **«Talend Cloud Data Fabric — Your session timed out, exit or re-log in»**. El modal cancela las operaciones del IDE y explica ambos errores; no se cierra automáticamente porque exige una decisión del usuario (iniciar sesión o salir de Studio).

Sin un motor Studio operativo no hay referencia con la que comparar tiempos, componentes, conexiones ni contextos, y `talend_job_build_batch` no puede compilar Jobs que Studio no ve.

## Decisión

**Se descarta el motor offline `engine: "auto"` y se mantiene `studio` como predeterminado; la Tarea 8 no se implementa.**

Motivos medidos:

1. La elegibilidad cumple (100 % de las guías de prueba), pero es el único criterio que se pudo medir.
2. No se pudo medir la ventaja de velocidad frente a Studio: el motor Studio no aplica ninguna guía mientras el modal de sesión de Talend Cloud bloquee el IDE.
3. No se verificó paridad de componentes, conexiones y contextos ni que los `.item` offline compilen, porque falta la referencia de Studio.

Para revisar la decisión: cerrar el modal en Studio (iniciar sesión en Talend Cloud o salir), repetir `talend_job_apply_custom_spec` sobre una guía en una carpeta de prueba y, si completa, volver a correr la medición de la Tarea 7 completa (tiempos por Job, paridad con `talend_inspect_job` y `talend_job_build_batch`). Solo entonces se puede aprobar la Tarea 8.

## Ejemplos útiles del MCP

El directorio `examples/` del MCP solo trae un perfil de tarea (`examples/task-profiles/olist_raw.context.json`), no especificaciones de Jobs. Los ejemplos reales viven en las pruebas: `tests/talend/job-batch.test.ts` (plantillas y lotes), `tests/talend/custom-job-spec.test.ts` y `tests/tools/custom-spec-executor.test.ts` (el contrato de `talend_job_apply_custom_spec`), y en la guía del agente: `talend_guide { mode: "task", task: "migracion-masiva" }`.
