# Proyectos aislados por ZIP

## Cargar y analizar un proyecto

Desde **Mis proyectos**, usa **Subir ZIP y crear proyecto**. El portal envía el ZIP y un nombre opcional en una solicitud multipart a `POST /api/projects/uploads`. El servidor valida y extrae el contenido en una carpeta temporal, registra el inventario y publica un proyecto nuevo solo cuando la importación termina correctamente. Un ZIP crea un proyecto; cargar otro ZIP nunca reemplaza el lote anterior.

Al terminar el registro, el API empieza en segundo plano estas etapas:

1. Análisis de programas y macros SAS.
2. Construcción del grafo de dependencias y del orden de procesamiento.
3. Generación de guías por programa/Job.

La respuesta incluye `project` y `processing`. El detalle del proyecto consulta `GET /api/projects/{id}/processing` y presenta el estado y etapa guardados, el mensaje, el inicio y la última actualización. Los estados posibles son:

| Estado | Significado |
| --- | --- |
| `queued` | Esperando capacidad de análisis en esta instancia del API. |
| `running` | Se ejecuta la etapa indicada (`analysis`, `dependencies` o `plans`). |
| `completed` | Análisis, dependencias y guías terminaron. |
| `failed` | Una etapa terminó con error. El mensaje queda asociado al proyecto. |
| `interrupted` | El proceso del API terminó antes de completar una tarea activa o en cola. |

Para `failed` e `interrupted`, **Reintentar análisis** vuelve a ejecutar el pipeline sobre la fuente ya extraída. No es necesario subir otra vez el ZIP. El resumen de análisis y el estado de implementación MCP se pueden volver a consultar después de recargar el portal.

Los proyectos anteriores sin metadatos de ZIP aparecen como **Proyecto existente** / **ZIP no registrado**. Conservan su navegación e importación manual. No se les asigna un nombre de ZIP ficticio.

## Límites de importación

Los valores predeterminados se configuran en `SGM_MAX_FILE_BYTES` (5 MiB por archivo extraído), `SGM_MAX_FILES` (5.000 archivos), y `SGM_MAX_TOTAL_BYTES` (256 MiB para el ZIP recibido). `SGM_IMPORT_ROOTS`, cuando se define, restringe las rutas usadas por importaciones locales; no es necesario para subir un ZIP desde el navegador.

## Operación local y escalabilidad

El estado se persiste en SQLite bajo `SGM_DATA_DIR` (por defecto `./data`). El procesamiento usa tareas de fondo de FastAPI y un límite por proceso: `SGM_MAX_PIPELINE_CONCURRENCY` (2 pipelines activos) y `SGM_MAX_QUEUED_PIPELINES` (20 solicitudes adicionales). El API devuelve `429` si se agota esa capacidad. El endpoint `GET /api/health` publica ambos límites.

Esta configuración está pensada para pruebas en **una instancia local del API**. La cola y el control de concurrencia viven en la memoria del proceso; no coordinan varias instancias. En un reinicio, las tareas activas o en cola se marcan `interrupted` y quedan disponibles para reintento desde el portal. El piloto no implementa una cola distribuida ni una base de datos compartida. Para escalar horizontalmente se requiere migrar a un almacén transaccional compartido y una cola durable con workers, además de deduplicación y coordinación entre instancias.

## Implementar todos los Jobs del proyecto en Talend

Desde **Plan de migración**, el botón único **Implementar todos los flujos del ZIP en Talend** inicia un lote para ese proyecto. La API toma los planes actuales, los ordena por las capas de dependencias del proyecto y llama secuencialmente a `talend_job_apply_custom_spec` por cada Job no confirmado. No crea un Job de lote especial ni usa una herramienta MCP diferente.

La API persiste una fila del lote y su resultado por programa en SQLite. `POST /api/projects/{id}/talend-apply-batch` inicia o reintenta la operación; `GET` en la misma ruta devuelve el estado, progreso (`completed_jobs`/`total_jobs`), programa actual, resultados y errores. Los estados del lote son `queued`, `running`, `applied`, `partially_applied`, `failed`, `conflict` e `interrupted`. El portal los consulta periódicamente mientras corre y los vuelve a consultar al reabrir el proyecto.

Un Job padre puede incluir Jobs hijos que el MCP crea recursivamente. Si la respuesta del MCP confirma un hijo por nombre y carpeta, se guarda el resultado asociado a su programa del ZIP y se omite una segunda llamada directa. Si el padre falla antes de devolver esa confirmación, el hijo se intenta después como Job independiente. Un fallo de un programa no oculta los resultados de los demás. Un mismo lote completado no se duplica; los lotes fallidos, parciales o interrumpidos se pueden reintentar con la misma revisión. Un cambio de revisión o conflicto de destino requiere intervención y no sobrescribe el Job.

Las guías individuales muestran el estado y resultado del lote (o de una implementación anterior) en modo de consulta; el botón para escribir está en la vista del proyecto. Los detalles técnicos sin resolver se conservan como contextos de migración para completarlos en Talend. La operación no compila ni ejecuta los Jobs.

La ruta de destino se deriva así:

```text
TALEND_APPLY_FOLDER/<slug-del-ZIP>-<project_id>/<subcarpeta-del-programa>
```

El valor local por defecto de `TALEND_APPLY_FOLDER` es `Process/PruebasWebSAS`. El slug usa el nombre del ZIP sin extensión, normalizado para formar una carpeta segura; el id estable evita que dos cargas con el mismo nombre choquen. La subcarpeta relativa conserva la organización del archivo dentro del ZIP. La guía muestra la ruta final calculada para ese Job. La API usa la misma ruta al obtener la vista previa y al llamar al MCP.

Una aplicación idéntica ya completada devuelve el resultado guardado sin duplicar el Job. Una revisión distinta o un Job ajeno en el destino se presenta como conflicto; el API no lo sobrescribe. El botón de lote respeta `TALEND_MCP_READONLY=true` y necesita el servidor MCP y el Bridge de Talend Studio disponibles para escribir.

La falta de origen de datos, esquema, credenciales o valor SAS no se resuelve con datos inventados. La guía pasa la información pendiente al MCP como contexto del Job para completarla posteriormente. Esto no impide construir los componentes que el plan sí especifica.
