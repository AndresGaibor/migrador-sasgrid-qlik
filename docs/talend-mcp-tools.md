# Integración actual con Talend MCP

El portal se conecta al MCP local por `TALEND_MCP_URL` (por defecto `http://127.0.0.1:3927/mcp`). La API FastAPI llama al MCP; el navegador no se conecta al MCP directamente.

## Tools usadas por el portal

- `talend_jobs_list`: comprueba que el servidor MCP responde y devuelve el número de Jobs del workspace.
- `talend_bridge_ping`: confirma que Talend Studio y el Bridge local están disponibles para aplicar cambios.
- `talend_job_apply_custom_spec`: recibe la guía estructurada y aplica el Job mediante las operaciones de Studio.

La herramienta de escritura recibe `jobName`, `version`, `defaultContext`, `folderPath`, `description`, `purpose`, `components`, `connections`, `contexts` e `instructions`. Cada componente puede incluir propiedades, tablas, esquema, mapper y una marca de borrador con el motivo pendiente. El MCP valida el componente y sus propiedades contra la paleta y los parámetros que responde Studio.

Una aplicación crea el Job en la carpeta configurada o reabre el Job coincidente y reutiliza sus componentes. Agrega contextos que faltan, conserva un valor de contexto existente cuando la nueva instrucción lo deja vacío y sustituye una conexión solo cuando la guía solicita la misma pareja de componentes con otro conector. Los componentes marcados como borrador reciben las propiedades verificadas por el portal; no se rellenan los datos desconocidos.

## Contextos de migración

El portal envía valores SAS solo cuando el análisis los conoce. Las variables desconocidas quedan vacías. Los pendientes técnicos se agrupan por paso o por asunto en contextos `migration_todo_<hash>` vacíos; sus comentarios conservan cada detalle de la guía. El hash mantiene un nombre estable entre reintentos. Al reaplicar una guía, el MCP sustituye los marcadores vacíos antiguos que creó el portal y conserva cualquier marcador que alguien ya haya llenado.

Al re aplicar una guía, un contexto `migration_todo_*` vacío no borra un valor que alguien haya completado en Talend. El MCP devuelve cuántos contextos agregó, actualizó o conservó.

## Configuración local

```dotenv
TALEND_MCP_URL=http://127.0.0.1:3927/mcp
TALEND_MCP_TIMEOUT_SECONDS=60
TALEND_MCP_READONLY=false
TALEND_APPLY_FOLDER=Process/PruebasWebSAS
```

El MCP configura su propio host y puerto con `TALEND_MCP_HOST` y `TALEND_MCP_PORT`. La URL de la API debe coincidir con esos valores. Mantén los procesos en el mismo Windows que Talend Studio para que MCP pueda comunicarse con el Bridge.

### Diagnóstico de la conexión

El MCP expone `GET /healthz` en su puerto para comprobar si el servidor responde sin invocar tools. La vista **Configuración** del portal consulta `GET /api/integrations/talend/health` y muestra el estado por etapas: servidor MCP, Bridge de Studio y escritura de Jobs, junto con la URL, el timeout y la carpeta de aplicación activos. `mcp_available` y `bridge_available` separan los dos fallos habituales (servidor caído frente a Studio cerrado), y el estado general es `Conectado`, `Parcial` (MCP responde pero no hay Bridge) o `Sin conexión`. Los `outputSchema` de las tools deben mantenerse consistentes con lo que devuelven: un cliente MCP con validación estricta rechaza cualquier respuesta que no cumpla el schema publicado.

La misma comprobación de salud lista las tools publicadas y devuelve `tools` (número de tools) y `write_tool` (si `talend_job_apply_custom_spec` está publicada). Así el portal distingue tres casos: el MCP no publica la tool de creación (servidor desactualizado), la tool existe pero su `inputSchema` no trae `childJobs`, `instructions`, `replaceManagedTodoContexts`, `draftOnly`, `draftReason` y `tables`, o el contrato está completo y solo falta el permiso de escritura.

`TALEND_MCP_READONLY=true` hace arrancar el portal en solo lectura; el permiso definitivo lo decide el interruptor de la vista **Configuración**, guardado en la base. `TALEND_APPLY_FOLDER` debe estar bajo `Process/`. La carpeta destino por ZIP es `<TALEND_APPLY_FOLDER>/<slug-del-ZIP>-<project_id>/<subcarpeta-del-programa>`; así dos ZIP con el mismo nombre se mantienen aislados y cada programa conserva su subcarpeta. La guía muestra la ruta exacta que se enviará al MCP.

`TALEND_MCP_TIMEOUT_SECONDS` limita cuánto espera la API cada respuesta del MCP. El resultado del lote se persiste por proyecto y programa y la vista consulta el estado mientras corre o al recargarse. Los estados del lote son `queued`, `running`, `applied`, `partially_applied`, `failed`, `conflict` e `interrupted`; cada programa conserva además su resultado y error. Una revisión idéntica que ya terminó devuelve el resultado guardado; una colisión no sobrescribe el Job encontrado.

El botón **Implementar todos los flujos del ZIP en Talend** inicia un lote de proyecto. La API ordena las guías por dependencias y hace llamadas secuenciales a `talend_job_apply_custom_spec`; el navegador nunca se conecta directamente al MCP. La vista de proyecto muestra el Job actual, el conteo terminado y los resultados de cada Job agrupados por las carpetas de origen. Un hijo que aparezca confirmado en la respuesta recursiva del MCP se registra en el lote y no se envía otra vez como Job independiente. Al fallar un Job, se conserva el error y se continúa con los siguientes.

Los valores técnicos no resueltos se agregan como contextos `migration_todo_*` con su descripción. El resultado de cada Job puede ser completo o parcial. El lote no compila ni ejecuta los Jobs. La vista individual de una guía permite consultar el destino y resultado, pero la escritura comienza desde el botón único del proyecto.
