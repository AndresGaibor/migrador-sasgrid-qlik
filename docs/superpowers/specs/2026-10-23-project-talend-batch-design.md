# Implementación Talend por proyecto ZIP — Diseño

## Intención

Permitir que una persona implemente todos los Jobs de un ZIP desde una sola acción del portal. El portal conserva su papel de instructor: prepara el contrato estructurado de cada guía y el MCP crea los Jobs y sus elementos en Talend Studio. La persona ve el avance y el resultado de cada Job, incluso después de recargar la página.

## Lo que existe hoy

- Cada ZIP vive en un `project_id` propio y tiene planes, dependencias y destino Talend aislados.
- La guía de cada programa tiene un botón que llama la API actual del MCP para aplicar un Job.
- La API guarda estado e idempotencia por proyecto y programa. El MCP puede crear recursivamente `childJobs` antes del Job orquestador.
- El análisis de dependencias devuelve capas en `processing_order`; las capas ordenan dependencias antes que consumidores y ordenan miembros de ciclos de forma estable.
- La vista de guías ya agrupa programas por carpetas del ZIP.

## Resultado esperado

En la vista de guías del proyecto aparecerá una sola acción **Implementar todos los Jobs en Talend**. Al activarla, el servidor iniciará un lote persistido y procesará las guías secuencialmente, en orden de dependencias. La vista mostrará el Job actual, cuántos terminaron, el estado de cada Job, y los errores o datos técnicos pendientes. Un reintento reutilizará los estados e idempotencia por Job ya existentes. El lote nunca ejecuta Jobs de Talend.

## Objetivos

- Una acción explícita por proyecto ZIP para recorrer todas sus guías.
- Ordenar por las capas de `processing_order`; incluir guías que no aparezcan en el grafo al final, en orden de ruta. Aplanar ciclos de forma determinista y advertirlo.
- Enviar cada plan al MCP actual mediante la operación por Job ya existente; no añadir un segundo contrato de creación por lote.
- Persistir estado de lote y detalle por Job: en cola, en curso, aplicado, parcial, fallido, conflicto o interrumpido.
- Permitir volver a abrir la vista y recuperar el lote. Reintentar los Jobs fallidos/interrumpidos/parciales con el mismo contrato, y no volver a escribir Jobs que ya terminaron aplicados.
- Intentar el resto de los Jobs aunque falle uno; informar el resultado parcial en vez de ocultar los errores posteriores.
- Mantener la ruta Talend por proyecto y subcarpeta del ZIP, y preservar contextos pendientes sin inventar valores.
- Retirar la acción de implementación individual de la interfaz de cada guía; conservar su estado y resultado como información de solo lectura.

## No objetivos y anti-objetivos

- No compilar, validar funcionalmente ni ejecutar Jobs.
- No actualizar un Job con una revisión distinta, resolver conflictos del Studio ni inventar conexiones, credenciales, esquemas o valores.
- No añadir una nueva tool al servidor MCP. No ejecutar solicitudes de escritura en paralelo.
- No cambiar el aislamiento por ZIP, el análisis ni el contrato estructurado ya enviado por el portal.
- No afirmar que el Job es ejecutable si aún tiene información técnica pendiente.

## Enfoques considerados

1. **Orquestar secuencialmente desde la API del portal y reutilizar la operación actual del MCP (elegido por el usuario).** Conserva la idempotencia, la identidad por guía y el detalle MCP existente; permite persistir avance por Job sin duplicar lógica Talend.
2. **Añadir una nueva herramienta de lote al MCP.** Centralizaría el bucle en el servidor MCP, pero duplicaría su contrato de operación/progreso y desplazaría al ejecutor el orden y estado que hoy administra el portal. No se eligió.

## Diseño de API y datos

- Añadir `POST /api/projects/{project_id}/talend-apply-batch` para iniciar/reintentar y `GET` en la misma ruta para leer el estado durable del lote.
- El POST devolverá el estado existente si el lote ya está en curso o terminó correctamente sin cambios en sus planes. Si terminó parcial, falló o fue interrumpido, un nuevo clic inicia un reintento; para una revisión diferente, reportará conflicto y no sobrescribirá implementaciones registradas.
- Un worker local de FastAPI ejecutará las llamadas de una en una; el POST responde sin esperar a que todos los Jobs terminen. Las guías que MCP incluya como `childJobs` se procesarán dentro de la llamada del orquestador y se reconciliarán desde el árbol `childJobs` de la respuesta, para no volver a aplicarlas.
- Añadir una fila SQLite de estado por proyecto con revisión del lote, lista ordenada de programas, índice/Job actual, conteo completado, estado, resumen por Job, error y timestamps. Los estados `running` se recuperan como `interrupted` al iniciar el API, igual que las operaciones MCP actuales.
- Antes de cada Job se verificará que la revisión del lote siga siendo la misma. Cada resultado individual seguirá guardándose con el estado de implementación existente por proyecto/programa.
- El lote se marcará `applied` si todas las guías terminan completas; `partially_applied` si hay resultados parciales o fallidos junto a resultados utilizables; `failed` si ninguna pudo aplicarse; `conflict` si la revisión o el destino colisiona; `interrupted` si el API se reinicia durante el trabajo.
- Un Job orquestador puede pedir al MCP crear hijos recursivamente. Cuando la respuesta confirma un hijo, el lote asociará ese resultado con su guía por Job y carpeta, persistirá el estado de esa guía y la omitirá como llamada independiente. Si la operación falla antes de que MCP confirme qué hijos creó, el lote intentará sus guías aún no confirmadas por separado; MCP conservará su idempotencia en la ruta del proyecto.

## Interfaz

- Colocar el botón único en **Plan de migración** del proyecto, junto al nombre ZIP y el conteo de Jobs.
- Deshabilitarlo si no hay guías o el MCP/Bridge no puede escribir. Mientras esté activo, mostrar progreso cuantificable como `terminados / total`, Job en curso y acción de reintento cuando concluya parcial o fallido.
- Mostrar una fila por guía, agrupable por carpetas existentes del ZIP, con `pendiente`, `creando`, `creado`, `parcial`, `fallido` o `conflicto`, y su detalle.
- La guía individual conserva información del último resultado MCP, pero ya no inicia implementaciones por sí misma.
- Aclarar que Talend Studio y Bridge deben estar disponibles y que ningún Job se ejecuta automáticamente.

## Criterios de aceptación

1. Un clic del proyecto inicia exactamente un lote y procesa sus guías secuencialmente en el orden del grafo; las rutas fuera del grafo se incluyen una vez. Una guía creada como `childJob` se cuenta desde el resultado del orquestador y no recibe una segunda llamada MCP.
2. La API conserva estado por proyecto y por Job, devuelve progreso durante el procesamiento y lo restaura tras recargar la vista.
3. Un error de un Job queda visible y no impide intentar los demás; el estado final refleja éxito completo, parcial, fallo o conflicto correctamente.
4. Reintentar no duplica Jobs completados, y una revisión distinta no reemplaza silenciosamente un destino existente.
5. La interfaz ofrece una sola acción de implementación para el lote y ninguna acción individual en las guías.
6. Los componentes, conexiones, carpetas y contextos siguen saliendo del plan vigente; la implementación no ejecuta Jobs ni rellena datos no inferidos.

## Decisiones para quien implemente

- Mantener la API `BackgroundTasks`/SQLite local ya usada por el portal; la operación requiere un único proceso servidor, igual que el procesamiento actual.
- Calcular la identidad del lote de forma determinista desde los contratos de todas las guías, sus carpetas y el orden resuelto.
- Reutilizar una función interna común de aplicación por Job desde las rutas individual y de lote para que validación, errores, idempotencia y persistencia no diverjan.
- Añadir tests de orden, reintento/idempotencia, progreso persistido, fallo por Job, conflicto de revisión, proyecto vacío y contrato de UI.
