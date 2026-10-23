# Proyectos aislados por ZIP — Diseño

## Intención

Cada ZIP de SAS debe convertirse en un proyecto independiente del portal. El portal conserva su estructura de carpetas, analiza el conjunto para descubrir programas, dependencias y componentes, y mantiene una relación inequívoca entre ZIP, guía y Job de Talend. Esto evita que una nueva carga mezcle flujos o reemplace silenciosamente los resultados de otro lote.

## Lo que existe hoy

- La interfaz permite crear un proyecto y luego subir un ZIP. Cada proyecto tiene un solo snapshot.
- `Store.import_batch()` reemplaza los archivos y borra análisis, dependencias y planes del proyecto. La API no guarda el nombre/hash del ZIP ni un historial de cargas.
- La extracción segura ya conserva rutas relativas y aplica límites configurables de tamaño y cantidad.
- El análisis, el grafo de dependencias y los planes son acciones separadas. Los estados de espera viven solo en la pantalla; al recargar, no se conoce si una tarea seguía activa.
- La biblioteca de proyectos muestra nombre y fecha, pero no el ZIP de origen ni el estado del análisis. El árbol de archivos abre todas las carpetas.
- El grafo, los planes y la integración MCP ya reciben `project_id`, por lo que se pueden reutilizar detrás de la nueva identidad por ZIP.

## Resultado esperado

Una persona carga un ZIP desde la biblioteca de proyectos. El portal crea un proyecto con nombre inicial derivado del ZIP, extrae el contenido y ejecuta el análisis estático, el grafo de dependencias y la generación de guías. En la biblioteca se ve una carpeta/tarjeta por ZIP, con su estado. Al abrirla se ven el ZIP de origen, las rutas del proyecto, los programas SAS, las relaciones entre programas y las guías/Jobs generadas por el plan.

La implementación en Talend sigue siendo explícita por Job. Cada solicitud MCP lleva la identidad del proyecto y la ruta del programa; no se mezclan instrucciones de otros ZIP. Los datos sin resolver se muestran como pendientes y se conservan en el contexto del Job, sin inventar valores. El portal nunca ejecuta el Job.

## Objetivos

- Un ZIP por proyecto y una carpeta de datos aislada por `project_id`.
- No reemplazar un lote existente al subir otro ZIP. La nueva carga siempre crea otro proyecto; para corregir un ZIP se crea un proyecto nuevo.
- Guardar nombre, hash, tamaño y fecha de recepción del ZIP como metadatos del proyecto.
- Ejecutar automáticamente extracción, análisis, dependencias y generación de guías después de cargar.
- Persistir estado por etapa y por implementación MCP: en cola, en curso, lista/parcial, error o interrumpida; mostrar etapa actual, timestamps, mensaje y una acción de recuperación.
- Mostrar contexto de origen en cada guía/Job: proyecto/ZIP, carpeta dentro del ZIP, programa SAS, dependencias y estado de implementación en Talend.
- Mantener límites de carga existentes; presentar errores en la etapa correcta y permitir reintentar un análisis sobre los archivos ya extraídos.
- Hacer navegables proyectos grandes mediante búsqueda/filtros, conteos por carpeta y árboles contraídos por defecto.

## No objetivos y anti-objetivos

- No ejecutar Jobs Talend ni código SAS al subir el ZIP o al implementar.
- No actualizar ni sobrescribir Jobs existentes automáticamente.
- No inventar origen de datos, esquemas, credenciales, valores dinámicos ni equivalencias. Lo pendiente sigue visible y trazable.
- No convertir el MCP en un intérprete de prosa libre: el portal envía contratos estructurados ligados a una revisión concreta del plan.
- No añadir una cola distribuida, microservicios ni una base de datos externa en esta entrega. El sistema mantiene la arquitectura FastAPI + SQLite del portal; escalar horizontalmente queda como fase futura.

## Enfoques considerados

1. **Un ZIP equivale a un proyecto (elegido por el usuario).** Aísla archivos, análisis y guías en el modelo existente de `project_id`; evita colisiones y no requiere versionar cada recurso derivado por ZIP dentro del mismo proyecto. Una corrección o nueva versión del ZIP crea otro proyecto.
2. **Varios ZIP por proyecto con snapshots independientes.** Facilita agrupar variantes, pero obliga a incluir un `archive_id` en manifest, análisis, decisiones, endpoints, exportaciones y aplicación MCP. Es más flexible, pero deja más oportunidades de cruzar identidades.
3. **Solo agrupar ZIPs visualmente sin cambiar el modelo de datos.** Se descarta: la carga actual reemplaza el snapshot y los resultados derivados; la apariencia no resolvería la causa de las guías incongruentes.

## Diseño de datos y API propuesto

- Ampliar el registro `projects` con metadatos del archivo de origen y estado actual del pipeline; añadir registro de operaciones con id, tipo, etapa, estado, mensaje/error, timestamps y resultado resumido.
- Añadir una ruta de carga que cree el proyecto desde el ZIP y devuelva su identidad/estado. Las rutas antiguas de carga/importación en un proyecto existente deben rechazar una segunda carga con mensaje claro, en vez de borrar los datos.
- Añadir consulta de estado por proyecto y consulta de estado de implementación por Job. La API persistirá el resultado final de MCP antes de responder y la UI lo recuperará al volver a abrir la página.
- Pipeline estático ordenado: extracción segura → parser/análisis → dependencias y orden de procesamiento → generación de planes/guías → estado listo. No iniciar MCP en este pipeline.
- El contrato MCP incluirá `project_id`, hash del ZIP, ruta del programa, hash/revisión del plan, `job_name` y carpeta Talend. La idempotencia y la recuperación deben conservar el comportamiento ya implementado por `talend_job_apply_custom_spec`.
- El destino Talend se aísla por ZIP debajo de `TALEND_APPLY_FOLDER`, con una carpeta legible y un identificador estable del proyecto antes de conservar las subcarpetas internas. Así dos ZIP que traigan el mismo programa no escriben sobre el mismo destino. La guía muestra la ruta exacta antes de implementar.
- Un reintento con la misma identidad y la misma revisión del plan reanuda la aplicación idempotente. Si el destino ya existe con otra identidad o cambió la revisión, el portal informa conflicto y no sobrescribe silenciosamente.
- Estado durable en SQLite. Al iniciar el API, operaciones que quedaron `running` pasan a `interrupted`; el análisis puede reintentarse desde los archivos extraídos. Una aplicación interrumpida se vuelve a comprobar con MCP antes de reintentar.

## Interfaz propuesta

- Biblioteca: acción principal **Subir ZIP y crear proyecto**; nombre inicial editable; tarjetas como carpetas con nombre del ZIP/proyecto, fecha, cantidad de programas, estado y última actividad.
- Proyecto: encabezado persistente con ZIP, tamaño/hash resumido, fecha, árbol de carpetas y barra de etapas accesible (sin porcentajes inventados). Los errores muestran etapa, diagnóstico y acción disponible.
- Resumen: conteos del proyecto y acciones siguientes; dependencias como grafo con alternativa tabular/filtros para programas grandes.
- Guías: agrupar por carpeta de origen del ZIP; cada Job indica dependencias, componentes propuestos, pendientes y estado MCP (`sin iniciar`, `creando`, `creado`, `parcial`, `error`). El estado sobrevive a recarga.
- Los datos vacíos o no verificados aparecen como pendientes; la interfaz distingue generado, aplicado parcialmente, revisado y ejecutado (este último estado no forma parte de esta entrega).

## Escalabilidad y disponibilidad dentro del alcance

- Mantener límites configurables de bytes/archivos, añadir límites por operación/concurrencia y no renderizar todos los nodos del árbol expandidos. API y worker local no requieren infraestructura nueva.
- Persistir transiciones para que navegar, recargar o reiniciar el API no pierda el estado observado. Ofrecer reintento para análisis y conciliación MCP cuando una operación quede interrumpida.
- Para despliegue en varias instancias, los workers locales y SQLite no bastan como coordinador distribuido. Esa expansión requerirá una cola/almacenamiento compartido y se diseña aparte; no se afirmará disponibilidad multiinstancia en esta fase.

## Restricciones y decisiones para implementación

- Conservar los IDs de proyectos existentes y su lectura. Los proyectos antiguos se muestran con origen “ZIP no registrado”; no se migran ni borran sus archivos durante la actualización.
- Conservar importación desde ruta local como alternativa avanzada, con la misma regla de un lote por proyecto.
- La carga debe validar extensión, ruta interna, tamaño total, número de archivos y traversal antes de publicar el snapshot; extraer primero a un directorio temporal y promoverlo solo cuando la carga sea válida.
- Si la carga o extracción falla antes de publicar el snapshot, se rechaza la operación y no aparece un proyecto vacío en la biblioteca. Si falla una etapa posterior, el proyecto ya publicado conserva sus archivos y muestra el error con opción de reintentar.
- La actualización de Jobs existentes, ejecución y validación funcional de equivalencia siguen fuera del alcance.
- La configuración MCP/Bridge y carpeta destino permanece configurable por entorno. Errores MCP se almacenan sin secretos y se presentan con un identificador de operación.

## Decisiones cerradas tras la revisión del diseño

- Fallo durante recepción/extracción: no publicar proyecto ni snapshot parcial; mostrar el error en el diálogo de carga. Esto evita carpetas sin ZIP y mantiene la biblioteca como inventario de fuentes válidas.
- Colisión/reintento Talend: separar el destino por ID de proyecto y subruta original. Reintentar solo la misma revisión de esa identidad; si cambia el plan o ya existe un Job ajeno en la ruta, informar el conflicto y no sobrescribir. El MCP seguirá usando su herramienta de aplicación vía API de Studio.

## Criterios de aceptación

1. Subir dos ZIP crea dos proyectos/carpeta con IDs y estados separados; ningún segundo ZIP borra archivos, análisis o guías del primero.
2. Al cargar un ZIP se dispara el pipeline estático y el estado progresa por etapas persistidas hasta `listo` o error recuperable.
3. El proyecto permite navegar archivos en su jerarquía original y ver programas, dependencias, orden y guías de ese ZIP únicamente.
4. Implementar un Job muestra la ruta de origen y el destino, persiste su estado, conserva pendientes en el contexto Talend y no ejecuta el Job.
5. Recargar o volver a abrir el proyecto conserva los estados y resultados. Reintentar una operación no duplica Jobs ni cruza proyectos.
6. La pantalla sigue siendo usable en un ZIP grande dentro de los límites configurados; errores de ZIP/MCP muestran etapa y siguiente acción clara.
