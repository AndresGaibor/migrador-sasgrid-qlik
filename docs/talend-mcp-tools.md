# Integración actual con Talend MCP

El portal se conecta al MCP local por `TALEND_MCP_URL` (por defecto `http://127.0.0.1:3927/mcp`). La API FastAPI llama al MCP; el navegador no se conecta al MCP directamente.

## Tools usadas por el portal

- `talend_jobs_list`: comprueba que el servidor MCP responde y devuelve el número de Jobs del workspace.
- `talend_bridge_ping`: confirma que Talend Studio y el Bridge local están disponibles para aplicar cambios.
- `talend_studio_ui_dialogs`: lista los diálogos de Studio y marca los modales que bloquean el IDE; el diagnóstico del portal lo consulta en cada comprobación.
- `talend_studio_memory`: heap que lleva usado Studio; el diagnóstico del portal lo muestra y recomienda reiniciar a partir del 75 %.
- `talend_studio_restart`: reinicia Studio a petición (`POST /api/integrations/talend/studio/restart` o el botón de Configuración). Cierra los diálogos abiertos, pide el cierre de la ventana principal y, si Studio no sale en 2 minutos, termina el proceso (`force`, por defecto). Requiere el permiso de escritura. Con `onlyIfMemoryAbove` solo reinicia si el heap supera ese porcentaje.
- `talend_job_apply_custom_spec`: recibe la guía estructurada y aplica el Job mediante las operaciones de Studio.

La herramienta de escritura recibe `jobName`, `version`, `defaultContext`, `folderPath`, `description`, `purpose`, `components`, `connections`, `contexts` e `instructions`. Cada componente puede incluir propiedades, tablas, esquema, mapper y una marca de borrador con el motivo pendiente. El MCP valida el componente y sus propiedades contra la paleta y los parámetros que responde Studio.

Una aplicación crea el Job en la carpeta configurada o reabre el Job coincidente y reutiliza sus componentes. Agrega contextos que faltan, conserva un valor de contexto existente cuando la nueva instrucción lo deja vacío y sustituye una conexión solo cuando la guía solicita la misma pareja de componentes con otro conector. Los componentes marcados como borrador reciben las propiedades verificadas por el portal; no se rellenan los datos desconocidos.

El planificador selecciona componentes por operación: por ejemplo, `tFilterRow` para filtros, `tMap` para joins/proyecciones/cálculos, `tAggregateRow` para agregaciones y componentes específicos de archivo o base de datos para entrada/salida. Para un `tMap` de una entrada Main y una salida Main, el portal genera el mapper si conoce los esquemas y puede traducir las columnas directas o una expresión aritmética segura. Las operaciones ambiguas, los joins sin definición inequívoca y las divisiones decimales sin regla de escala se conservan como borradores con su motivo; no se inventa una configuración.

Ejemplo conceptual del mapper enviado al MCP para copiar `amount` y calcular una comisión decimal:

```json
{
  "componentName": "tMap",
  "mapper": {
    "inputs": [{ "name": "row_2_1", "columns": [{ "name": "amount", "type": "id_BigDecimal" }] }],
    "outputs": [{ "name": "row_3_1", "columns": [
      { "name": "service_fee", "type": "id_BigDecimal", "expression": "...BigDecimal.multiply(...)" }
    ] }]
  }
}
```

El mapper aritmético usa `BigDecimal` para evitar una expresión Java inválida sobre importes decimales. La división queda pendiente hasta acordar escala y redondeo. Generar el mapper no cuenta como verificación de Studio: después de aplicarlo, la API lee el `.item` del Job y compara componente, parámetros, esquemas, mapper y conexiones, usando `componentAliases` para respetar los nombres reales de Studio.

La evidencia aparece por paso en la guía y en el resumen del proyecto. Se guarda con la revisión actual de la especificación y no modifica los estados manuales ni sus notas. Si Studio no responde durante la lectura, los pasos quedan «No verificable»; el botón **Volver a comprobar pasos en Studio** reintenta solo la lectura y no vuelve a aplicar ni ejecutar el Job. El resultado significa «configurado y leído en Studio»; no compila ni ejecuta el Job.

## Contextos de migración

El portal envía valores SAS solo cuando el análisis los conoce. Las variables desconocidas quedan vacías. Los pendientes técnicos se agrupan por paso o por asunto en contextos `migration_todo_<hash>` vacíos; sus comentarios conservan cada detalle de la guía. El hash mantiene un nombre estable entre reintentos. Al reaplicar una guía, el MCP sustituye los marcadores vacíos antiguos que creó el portal y conserva cualquier marcador que alguien ya haya llenado.

Al re aplicar una guía, un contexto `migration_todo_*` vacío no borra un valor que alguien haya completado en Talend. El MCP devuelve cuántos contextos agregó, actualizó o conservó.

## Configuración local

```dotenv
TALEND_MCP_URL=http://127.0.0.1:3927/mcp
TALEND_MCP_TIMEOUT_SECONDS=60
TALEND_APPLY_FOLDER=Process/PruebasWebSAS
```

El MCP configura su propio host y puerto con `TALEND_MCP_HOST` y `TALEND_MCP_PORT`. La URL de la API debe coincidir con esos valores. Mantén los procesos en el mismo Windows que Talend Studio para que MCP pueda comunicarse con el Bridge.

### Parámetros individuales por Job (.cpf)

Qlik documenta la configuración de contextos y la carga dinámica con `tContextLoad` o Implicit Context Load, pero no documenta `.cpf` como extensión nativa de Talend. El motor acepta `.cpf` como archivo de parámetros del portal: UTF-8, una asignación `nombre=valor` por línea; líneas vacías y comentarios `#` o `!` se ignoran. Por ejemplo:

```text
source_path=/data/input.csv
run_date=2026-10-26
```

El llamador del generador selecciona el archivo del Job con `build_apply_spec(plan, context_file=Path("daily.cpf"))`. Los pares se convierten en variables del contexto Talend, reemplazan variables con el mismo nombre (sin distinguir mayúsculas) y agregan las nuevas. Nombres inválidos, valores vacíos, duplicados, extensión distinta de `.cpf`, archivo inexistente o problemas de lectura producen un error de validación. Los valores no se transforman ni se insertan en código Java.

El modelo actual no declara qué parámetros son obligatorios, así que no se puede rechazar un archivo solo porque omita uno. Las variables suministradas deben ser referenciadas por los componentes como `context.nombre`; el `.cpf` no se adjunta como artefacto ni configura por sí solo la carga dinámica en tiempo de ejecución.

### Diagnóstico de la conexión

El MCP expone `GET /healthz` en su puerto para comprobar si el servidor responde sin invocar tools. La vista **Configuración** del portal consulta `GET /api/integrations/talend/health` y muestra el estado por etapas: servidor MCP, Bridge de Studio y escritura de Jobs, junto con la URL, el timeout y la carpeta de aplicación activos. `mcp_available` y `bridge_available` separan los dos fallos habituales (servidor caído frente a Studio cerrado), y el estado general es `Conectado`, `Parcial` (MCP responde pero no hay Bridge) o `Sin conexión`. Los `outputSchema` de las tools deben mantenerse consistentes con lo que devuelven: un cliente MCP con validación estricta rechaza cualquier respuesta que no cumpla el schema publicado.

La misma comprobación de salud lista las tools publicadas y devuelve `tools` (número de tools) y `write_tool` (si `talend_job_apply_custom_spec` está publicada). Así el portal distingue tres casos: el MCP no publica la tool de creación (servidor desactualizado), la tool existe pero su `inputSchema` no trae `childJobs`, `instructions`, `replaceManagedTodoContexts`, `draftOnly`, `draftReason` y `tables`, o el contrato está completo y solo falta el permiso de escritura.

El permiso de escritura se controla únicamente desde el interruptor de la vista **Configuración** y se guarda en la base; no depende de variables de entorno. `TALEND_APPLY_FOLDER` debe estar bajo `Process/`. La carpeta destino por ZIP es `<TALEND_APPLY_FOLDER>/<slug-del-ZIP>-<project_id>/<subcarpeta-del-programa>`; así dos ZIP con el mismo nombre se mantienen aislados y cada programa conserva su subcarpeta. La guía muestra la ruta exacta que se enviará al MCP.

`TALEND_MCP_TIMEOUT_SECONDS` limita cuánto espera la API cada respuesta del MCP. Antes de implementar, la API recorre el inventario completo de `talend_jobs_list`, incluso si excede el límite predeterminado de 50, y compara nombre y carpeta. Un Job ausente se crea; un Job que ya está en la carpeta exacta se actualiza; un homónimo que solo existe en otra carpeta bloquea el lote. El portal publica el endpoint de solo lectura `GET /api/projects/{id}/talend-apply-batch/preflight` para mostrar esas acciones. Una lectura MCP incompleta o fallida detiene la escritura.

El resultado del lote se persiste por proyecto y programa y la vista consulta el estado mientras corre o al recargarse. Los estados del lote son `queued`, `running`, `applied`, `partially_applied`, `failed`, `conflict` e `interrupted`; cada programa conserva además su resultado y error. La comprobación se repite al iniciar el lote y antes de la primera escritura, y el hash de revisión debe seguir igual. Si un conflicto guardado ya no existe, se puede reintentar con el inventario actual; si se borró un Job de un lote completado, solo se vuelve a crear ese Job. Las colisiones fuera de la carpeta destino no se sobrescriben.

El botón **Implementar todos los flujos del ZIP en Talend** inicia un lote de proyecto. La API ordena las guías por dependencias y hace llamadas secuenciales a `talend_job_apply_custom_spec`; el navegador nunca se conecta directamente al MCP. La vista de proyecto muestra el Job actual, el conteo terminado, la comprobación de destino y los resultados de cada Job agrupados por las carpetas de origen. Un hijo que aparezca confirmado en la respuesta recursiva del MCP se registra en el lote y no se envía otra vez como Job independiente. Al fallar un Job, se conserva el error y se continúa con los siguientes.

Los valores técnicos no resueltos se agregan como contextos `migration_todo_*` con su descripción. El resultado de cada Job puede ser completo o parcial. El lote no compila ni ejecuta los Jobs. La vista individual de una guía permite consultar el destino y resultado, pero la escritura comienza desde el botón único del proyecto.

## Smoke test con Studio (2026-10-27)

Prueba manual de la Tarea 10 del plan `docs/superpowers/plans/2026-10-27-talend-mcp-en-el-portal.md`, con Talend Studio 8.0.1 abierto y el Bridge en `readWrite`. No se compiló, ejecutó ni publicó ningún Job.

### Instalación en limpio

Clon de `origin/main` en una carpeta aparte, siguiendo solo el README:

| Paso | Resultado |
|---|---|
| `uv sync` | correcto; solo avisa de rutas de referencia duplicadas en `docs/reference/talend/` |
| `bun install` en `apps/web` | 166 paquetes |
| `bun install` en `mcp/talend-mcp` | 17 paquetes |
| `scripts/dev.ps1` (versión inicial, hoy reemplazada por `uv run sgm dev`) | MCP en 3927 con 66 tools, API en 8000 y web en 5173; el `doctor` ve Studio, JDK, Bridge y proyecto |

Dos hallazgos corregidos o anotados:

- La web se anunciaba en `http://127.0.0.1:5173`, pero Vite escuchaba en `localhost` (IPv6 `::1`) y esa dirección no respondía. `scripts/dev.ps1` ahora pasa `--host 127.0.0.1`; verificado con respuesta 200 en la dirección anunciada.
- Con el puerto 3927 libre, el arranque del MCP muestra «No se pudo liberar el puerto 3927». Es un aviso cosmético de `mcp/talend-mcp/scripts/start.ts`: PowerShell devuelve 1 cuando `Get-NetTCPConnection` no encuentra conexiones. El servidor arranca igual.

El `doctor` avisa de que `TALEND_PROJECT` y `TALEND_WORKSPACE` no están definidos; el MCP infiere ambos del workspace abierto, así que no bloquea la prueba.

### Diagnóstico por caso

| Caso | `diagnosis` | Respuesta observada |
|---|---|---|
| MCP apagado | `mcp_down` | `mcp_available=false`; el `fix_hint` indica arrancar el MCP |
| Preset `agent` (56 tools) | `tools_missing` | faltan 10 tools del contrato; el `fix_hint` pide `TALEND_MCP_FILTER=portal` |
| Preset `all` (241 tools) | `ok` | contrato completo |
| Preset `portal` (66 tools) | `ok` | contrato completo y `write_tool=true` |
| Bridge inaccesible | `bridge_down` | `mcp_available=true` y `bridge_available=false`; el `fix_hint` pide abrir Studio |

Para el último caso no se cerró Studio: se arrancó otro MCP con `TALEND_BRIDGE_PORT=3939`, sin nadie escuchando, que produce el mismo estado sin tocar la sesión del usuario.

### Creación y lectura en `Process/PruebasWebSAS`

Guía `job_01_load_customers` del ZIP sintético, aplicada con `talend_job_apply_custom_spec` y el motor Studio:

- 4 componentes (`tFileInputDelimited`, `tFilterRow`, `tMap`, `tFileOutputDelimited`), 1 conexión y 13 contextos.
- `talend_inspect_job` devuelve los cuatro componentes y `talend_job_problems` responde sin problemas.
- Repetir la misma guía en el mismo proyecto reanuda el Job sin `CONFLICT`.
- Aplicar otra guía con el mismo nombre devuelve `CONFLICT` y no sobrescribe.

El hash del marcador `[portal-spec:...]` incluye `instructions.source.projectId`. Dos proyectos distintos con la misma guía no se reconocen como la misma especificación; es el comportamiento esperado, pero conviene tenerlo en cuenta al probar con proyectos temporales.

### `unsafeActions`

Con `unsafeActions=false` y `readOnly=false` en `~/.talend-bridge/config.json`, la creación del mismo Job siguió funcionando y la lectura devolvió los mismos 4 componentes, 1 conexión y 13 contextos. La creación no depende de `unsafeActions`; la escritura la limitan el permiso del portal y, si se activa, `readOnly` del Bridge. La configuración original se restauró al terminar.

### Modal bloqueante en Studio

El primer intento falló con «El hilo de la interfaz de Studio esta ocupado» y después con `OperationCanceledException`. La causa era un modal «Network Issue Occured» (conexión al servidor con timeout) que bloqueaba el hilo de UI. `talend_studio_ui_dialogs` lo detecta y marca `blocked: true`. El diagnóstico del portal consulta esa tool y, si hay un modal, devuelve `diagnosis: studio_blocked` con los títulos en la pista de arreglo y el detalle en `studio_dialogs`; la creación y la lectura de Jobs siguen disponibles porque no pasan por el hilo de la interfaz. Si la comprobación no responde (Bridge anterior al endpoint), queda `studio_dialogs.checked: false` y el resto del diagnóstico no cambia.
