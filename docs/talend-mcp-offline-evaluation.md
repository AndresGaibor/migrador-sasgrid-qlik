# Evaluación: crear Jobs con Studio o en modo offline

Estado: **medido el 2026-10-27 con guías reales del portal.** La decisión final está al final del documento; las cifras de la sección introductoria sobre el modo offline salen de `talend-mcp/docs/MODO-OFFLINE.md` y se conservan como referencia del MCP, no como medición del portal.

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

### Tiempos por Job con Studio y en modo offline

MCP con el preset `portal` sobre el proyecto de Studio real, 20 de las 24 guías elegibles (8, 8 y 4 en el orden de los ZIP), cada una aplicada a la vez con el motor Studio (`talend_job_apply_custom_spec`) y con el motor offline (`talend_jobs_create_from_spec`). El tiempo incluye la ida y vuelta MCP. Se usó `talend_jobs_create_from_spec` y no `talend_jobs_create_batch` porque el lote exige una plantilla común y las guías del portal no comparten los mismos componentes.

| Motor | Jobs | Media | Mediana | Mínimo | Máximo | Total |
|---|---|---|---|---|---|---|
| Studio | 20 | 12,89 s | 11,73 s | 0,34 s | 22,84 s | 257,75 s |
| Offline | 20 | 0,50 s | 0,50 s | 0,02 s | 1,26 s | 10,00 s |

El motor offline es unas 23 veces más rápido por mediana y unas 26 veces por tiempo total, y creó los 20 Jobs sin un solo error.

### Fallos del motor Studio

`talend_job_apply_custom_spec` falló en 16 de los 20 Jobs:

| Error | Casos |
|---|---|
| `El hilo de la interfaz de Studio esta ocupado (se acabo el tiempo de espera)` | 9 |
| `IConnection.getMetadataTable() is null` al clonar la tabla de metadatos | 5 |
| `el conector 'FILTER' de 'tFilterRow' no admite entradas` | 2 |

No hay diálogo bloqueante: `talend_studio_ui_dialogs` responde `blocked: false` y `dialogs: []`. Los fallos son del propio montaje y no de una sesión de Talend Cloud caducada, y en varios casos el Job quedó creado pero vacío.

### Paridad entre motores

Solo 4 de los 20 Jobs quedaron aplicados por ambos motores. En dos de ellos (`MedS_01`, `MedS_17`) el Job de origen no tiene componentes, así que no hay nada que comparar. En los otros dos (`MedS_02`, `MedS_16`) coinciden los tipos de componente y el número de conexiones, pero no los `uniqueName`: Studio renumera al crear (`tFileInputDelimited_2`) y el motor offline conserva los del portal (`tFileInputDelimited_1`).

Los contextos no coinciden, y la causa no era el nombre de las claves. Comprobado el 2026-10-28 contra el MCP real: `talend_jobs_create_from_spec` **descarta `contexts` sin avisar**, tanto con las claves del portal (`type`/`value`/`comment`) como con las suyas (`tipo`/`valor`/`comentario`). El generador de `create-from-spec.ts` construye el `JobSpec` sin ese campo. Los Jobs offline de la medición quedaron sin contextos por eso. `talend_jobs_create_batch`, en cambio, sí escribe `contexts` y usa la misma forma que el portal; una plantilla con una sola fila vacía crea un Job. El portal ya tiene esa conversión (`talend_adapter/offline_payload.py`, `to_batch_arguments`) y una prueba contra el MCP real que comprueba que el contexto llega al `.item`.

Dos defectos del MCP que conviene reportar al upstream: `talend_jobs_create_from_spec` ignora `contexts` aunque lo acepta en su schema, y sin `folder` falla con `ENOENT` porque no crea la carpeta `process/`.

Además, `create_batch` expande `{{variable}}` en todos los textos de la plantilla. Un valor SAS con esa sintaxis rompería o alteraría el Job, así que `offline_blockers` lo trata como bloqueo (`placeholder:<componente>`).

### Compilación: no verificable en este equipo

`talend_job_build_batch` no sirvió para comprobar que los `.item` offline compilan. Responde `No se encuentra la carpeta generada del job <nombre>` para los Jobs medidos y también para un Job nativo de Studio (`Carga_Datos_SS`), y una llamada posterior agotó los 25 s del puente (`BRIDGE_UNAVAILABLE`). El fallo está en la generación de código del lote, no en los archivos que escribe el motor offline.

## Decisión

**Se mantiene `studio` como predeterminado y la Tarea 8 no se implementa.**

Motivos medidos:

1. Velocidad: el criterio de 20 veces se cumple con holgura (23 veces por mediana, 26 por total).
2. Paridad: no se pudo verificar. El motor Studio falla en 16 de 20 casos y renumera los `uniqueName` cuando funciona. Los contextos faltaban en la medición porque se usó `talend_jobs_create_from_spec`, que los descarta; con `talend_jobs_create_batch` sí se escriben (ver arriba), así que ese punto ya no bloquea.
3. Compilación: no se pudo comprobar porque `talend_job_build_batch` falla también con Jobs nativos de Studio.

Para revisar la decisión: estabilizar el montaje del motor Studio (los tres errores de la tabla), repetir la medición de 20 guías usando `to_batch_arguments` (contextos incluidos) y verificar con `talend_job_build_batch` que los `.item` offline compilan. Solo entonces se puede aprobar la Tarea 8. La medición con el payload corregido está pendiente: necesita un Studio estable y no se repitió el 2026-10-28.

## Ejemplos útiles del MCP

El directorio `examples/` del MCP solo trae un perfil de tarea (`examples/task-profiles/olist_raw.context.json`), no especificaciones de Jobs. Los ejemplos reales viven en las pruebas: `tests/talend/job-batch.test.ts` (plantillas y lotes), `tests/talend/custom-job-spec.test.ts` y `tests/tools/custom-spec-executor.test.ts` (el contrato de `talend_job_apply_custom_spec`), y en la guía del agente: `talend_guide { mode: "task", task: "migracion-masiva" }`.
