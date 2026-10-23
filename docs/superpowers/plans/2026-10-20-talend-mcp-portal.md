# Implementación automática de guías en Talend — Plan

> Plan de implementación solamente. No se han modificado el portal ni `talend-mcp`.

**Meta:** después de analizar un proyecto SAS, convertir la guía generada por el portal en una especificación estructurada que `talend-mcp` pueda aplicar a un Job real de Talend, y mostrar el resultado, los pendientes y la forma de recuperación en el portal.

**Arquitectura:** el portal seguirá analizando SAS y proponiendo planes. Un adaptador del backend transformará cada JobPlan en un contrato de aplicación versionado; `talend-mcp`, ejecutándose junto al workspace Talend, validará, previsualizará y escribirá los archivos del Job. El usuario podrá ordenar la aplicación desde la guía; el MCP no recibirá prosa libre ni credenciales SAS, y cada aplicación quedará vinculada al Job, a la revisión del plan y a una copia recuperable.

**Tecnologías existentes:** FastAPI/Pydantic/SQLite en `apps/api` y `src/sas_grid_migrator`; React/TypeScript/Vite/Bun en `apps/web`; servidor MCP HTTP en Bun/TypeScript en `talend-mcp`.

## Lo que existe y lo que falta

- El portal genera `JobPlan` y `PlanStep` estructurados en `src/sas_grid_migrator/migration_planner/models.py`. Cada paso puede incluir acción, componente candidato, propiedades, schema, conexiones, evidencia SAS, confianza, decisiones pendientes y estado. El plan no es todavía una especificación completa de Talend.
- `TalendAdapter` en `src/sas_grid_migrator/talend_adapter/adapter.py` solo expone herramientas de lectura/vista previa por la política en `policy.py`.
- `talend-mcp` tiene herramientas de validación/preview y escritura, incluyendo `talend_job_apply_custom_spec` y `talend_jobs_apply_pipeline_spec`. La ruta de aplicación escribe `.item` y `.properties`, puede crear un snapshot y puede intentar refrescar/abrir el recurso vía Studio Bridge.
- Los patrones disponibles en el MCP son acotados; la guía SAS puede incluir conexiones, expresiones, macros, orquestación Grid, variables y componentes que no tengan conversión automática completa.
- Hay una ruta interna de aplicación que depende de un Studio Bridge marcado como no implementado; antes de integrarla se debe escoger y probar la herramienta de aplicación real del MCP. La generación directa de XML tampoco se debe tratar como prueba de que Studio abrió o ejecutó correctamente el Job.
- El portal se documenta desplegado en Ubuntu/Tailscale; el MCP local detecta un workspace configurado por `TALEND_PROJECT` o `TALEND_WORKSPACE`. Para el MVP, ambos procesos deben correr en el mismo equipo que puede acceder a ese workspace Talend.

## Flujo de usuario objetivo

1. La persona carga el ZIP SAS, ejecuta el análisis y abre la guía del Job que desea migrar.
2. Elige **Implementar en Talend**. El portal comprueba MCP, Studio/workspace y el Job destino; permite crear un Job nuevo o seleccionar uno existente. Crear uno nuevo en una carpeta de prueba es la opción inicial recomendada.
3. El portal muestra un resumen legible antes de escribir: componentes y valores que se crearán, conexiones y columnas, cambios en Job existente, decisiones que debe resolver la persona y transformaciones que no se pueden generar con seguridad.
4. Tras una sola confirmación explícita para ese Job y esa versión de la guía, el backend envía la especificación validada a MCP. MCP toma snapshot, aplica, refresca Studio y devuelve resultado y diagnósticos. Este es el modo inicial de automatización: una confirmación por Job, sin aprobar manualmente cada parámetro.
5. La guía muestra aplicado, aplicado parcialmente, bloqueado o error; conserva los pendientes y permite abrir el Job, ver diagnóstico, reintentar de forma idempotente o restaurar el snapshot. Nunca marca “validado en Studio” solo porque se escribieron archivos.

Los pasos totalmente resueltos se pueden aplicar juntos. Pasos con baja confianza, `manual_decision`, componente/parámetro sin verificar, conexión a producción, credenciales o lógica SAS no traducida se bloquean para decisión humana y no se rellenan con valores inventados. Un modo futuro de aplicación sin confirmación podrá activarse por el usuario solo para Jobs que pasen todos los controles y nunca incluirá ejecución del Job.

## Contrato entre el portal y MCP

Crear un contrato `TalendApplySpec` versionado y distinto del JSON de presentación de la guía. La versión inicial debe incluir:

- identidad: `project_id`, ruta/programa SAS, hash de fuente, `rules_version`, `schema_version`, `job_name`, `target_job` y carpeta destino;
- operaciones tipadas y ordenadas por Job: crear/configurar componente, schema, conexión, contexto no secreto y dependencias;
- valores de parámetros únicamente cuando estén resueltos; componente, propiedad, tipo, origen SAS (`file:line`), referencia de catálogo y estado de verificación;
- pendientes, motivo de bloqueo, confianza y decisión del usuario;
- política de escritura: `create_new` o `update_existing`, nunca overwrite implícito;
- clave de idempotencia ligada al hash de guía + Job destino, y un identificador de intento de aplicación.

El adaptador traducirá nombres y estructura al esquema MCP elegido. No enviará el texto Markdown al modelo ni le pedirá que interprete instrucciones de manera abierta. Si el contrato no puede representar fielmente un paso, se devuelve como no soportado y queda fuera de la aplicación automática.

## Fases

### 0. Prueba técnica real y decisión del mecanismo de escritura

1. Fijar host de ejecución. Recomendación: portal API y MCP en Windows local, con `TALEND_PROJECT` apuntando a un proyecto Talend temporal; conservar el MCP en `127.0.0.1`.
2. Confirmar que el servidor MCP actual inicia en el commit disponible y enumerar las herramientas realmente expuestas por su filtro. Verificar esquemas, no basarse solo en nombres/documentación.
3. En un proyecto Talend de prueba, comparar `talend_job_apply_custom_spec` con `talend_jobs_apply_pipeline_spec`: comprobar creación, snapshot, actualización de Job existente, refresco del workspace, apertura en Studio, diagnósticos y restauración. Resolver la dependencia del Bridge que está incompleta antes de seleccionar la ruta.
4. Guardar un caso pequeño que se pueda construir desde un `JobPlan` sencillo y contrastarlo visualmente en Studio. Registrar versiones MCP/Studio, archivos tocados, evidencia y limitaciones.

**Salida/aceptación:** herramienta de escritura elegida con evidencia de aplicación real y recuperación probada. Si no se logra, la siguiente fase puede avanzar solo con preview; no se ofrece “Implementar” conectado a un writer no comprobado.

### 1. Traductor JobPlan → TalendApplySpec

1. Crear un módulo adaptador separado, inicialmente `src/sas_grid_migrator/talend_adapter/apply_spec.py`, y modelos Pydantic versionados para contrato, operación, bloqueo, preview y resultado.
2. Traducir únicamente una matriz inicial acordada de mappings soportados. Usar los `PlanStep`, catálogos y mappings existentes; no convertir texto libre de `purpose` en parámetros.
3. Marcar como `blocked` cualquier recomendación `unsupported`/`partial` que no tenga transformador validado, campo sin verificar, expresión con `talend=None`, valor faltante, dependencia externa o decisión pendiente.
4. Usar nombres estables de operación para permitir comparación e idempotencia entre reintentos.
5. Añadir unit tests con varios `JobPlan` representativos: simple soportado, conexión desconocida, parámetro no verificado, macro/child job y Job con bloqueos.

**Aceptación:** la salida puede reconstruirse de forma determinista y nunca convierte candidatos inciertos en instrucciones de escritura.

### 2. Preview, validación, aplicación y recuperación por el backend

1. Expandir `TalendAdapter` y la política hacia una allowlist explícita de herramientas de validación, preview, snapshot, aplicación y restauración. Cada acción debe tener un método tipado; la API no acepta el nombre arbitrario de una tool.
2. Añadir endpoints por proyecto/Job: crear preview, consultar preview, confirmar y aplicar una revisión concreta, consultar estado/log de aplicación y restaurar snapshot. Usar estados persistidos y rechazar confirmación si cambió el hash de fuente, guía o Job destino desde el preview.
3. En preview, verificar nombres/propiedades contra el catálogo y el Job de destino; rechazar valores de credenciales/contexto sensibles. Mostrar alta/actualización de Job, componentes, parámetros, conexiones, schemas, bloqueos y warnings.
4. Antes de escribir: confirmar que destino está dentro del `TALEND_PROJECT` configurado, que no hay colisión no autorizada, crear snapshot de `.item` y `.properties`, guardar el manifiesto de archivos y diffs, y fijar la clave de idempotencia.
5. Aplicar el spec y luego inspeccionar los archivos/Job con herramientas de lectura. Refrescar/abrir el recurso mediante Studio Bridge si está disponible. Si hay fallo parcial, mantener resultado parcial, snapshot y diagnóstico; restauración debe ser una acción explícita.
6. No ejecutar Jobs ni conectar a sistemas de producción en este flujo. La ejecución de prueba quedará en una fase posterior con datasets locales, autorización y diseño propio.

**Archivos:** `src/sas_grid_migrator/talend_adapter/adapter.py`, `policy.py`, `apps/api/main.py`, persistencia SQLite (`src/sas_grid_migrator/persistence/store.py` o módulo dedicado), schemas y tests API.

**Aceptación:** solo un preview confirmado para la revisión exacta puede escribir; cada escritura deja snapshot/diff/estado y el bloqueo/error explica qué falta.

### 3. Experiencia web de aplicación automática controlada

1. Añadir en `apps/web/src/views/PlansTab.tsx` la acción **Implementar en Talend** por Job y mostrar estados MCP/workspace antes de iniciar.
2. Añadir panel de preview con destino, conteo de componentes/cambios, pasos automatizables, bloqueos, valores sensibles omitidos y enlaces clicables a la evidencia SAS y al catálogo.
3. Exigir una confirmación clara que nombre el Job destino y los cambios principales. La confirmación aplica el conjunto elegible en secuencia y guarda la revisión aprobada; no se confirma por checkbox genérico ni se aprueban bloqueos.
4. Mostrar progreso por fases (validando, snapshot, escribiendo, inspeccionando, refrescando), resultado por operación, diagnóstico MCP/Studio y enlaces al snapshot y Job.
5. Añadir controles de reintento seguro, abrir Job, restaurar snapshot y revisar/reanudar los pasos bloqueados. Navegación entre Jobs conserva su estado de aplicación.
6. Actualizar `apps/web/src/api.ts`, `types.ts`, estilos y tests; estados sin conexión, análisis aún en progreso, preview desactualizado, aplicación parcial, MCP error, workspace ausente, Job duplicado y viewport móvil.

**Aceptación:** una persona no técnica comprende qué se escribirá, inicia una aplicación por Job, sabe qué terminó y puede recuperar o continuar cuando algo queda pendiente.

### 4. Endurecer `talend-mcp` para escritura gobernada

1. Revisar y corregir la herramienta seleccionada para que `overwrite=false` cree solo Jobs nuevos y un update existente requiera target inequívoco; validar rutas contra raíz del proyecto y evitar path traversal.
2. Hacer que snapshot de `.item` y `.properties` sea obligatorio y atómico antes de cada cambio; si snapshot falla, abortar sin escribir. Probar restore de ambos archivos y manejo de nombres/versiones.
3. Añadir modo dry-run/capacidad de validar el mismo spec y retornar diff sin escritura. La confirmación de portal debe quedar enlazada a un token/hash de preview de un solo uso, con expiración breve.
4. Asegurar que errores y logs no incluyan contraseñas, valores de contextos sensibles o datos SAS completos.
5. Añadir tests de concurrencia y fuente obsoleta: si Studio/usuario modifica el Job después del preview, no sobrescribir; volver a inspeccionar y exigir nuevo preview.

**Archivos previstos:** `src/talend/studio/tools-job-spec.ts` o herramienta de aplicación seleccionada, `src/talend/job-generator.ts`, funciones de snapshots, schemas/tool safety y tests del MCP. Coordinar cambios del contrato en ambos repositorios en una versión identificable.

**Aceptación:** el writer no sobrescribe silenciosamente, no opera fuera del proyecto, falla seguro si no logra snapshot y permite restaurar un cambio probado.

### 5. E2E, despliegue y activación gradual

1. Con un MCP falso en CI, automatizar portal → ZIP → análisis → guía → preview → confirmación → resultado aplicado → recarga → diagnóstico/restore. El MCP falso no modifica archivos reales.
2. Ejecutar suites portal y MCP: `uv run pytest`, `uv run ruff check`, `cd apps/web && bun test`, `cd apps/web && bun run build`; en la raíz del repo `talend-mcp`, `bun test` y `bun run typecheck`.
3. Realizar smoke con Talend Studio y un proyecto desechable, primero crear un Job básico y después actualizar una copia. Inspeccionar visualmente el Job, revisar Problems/metadata, probar restore y registrar evidencia.
4. Empezar con feature flag apagado; habilitar solo mappings/casos que pasaron Studio. Para cualquier otro paso, mantener “requiere intervención” y no aplicar.
5. Documentar instalación/arranque MCP, ubicación del workspace, versiones probadas, límites, copia de seguridad, recuperación y política de acceso. Para Ubuntu/Tailscale, no habilitar escrituras hasta demostrar que el proceso tiene acceso al workspace correcto y un modelo de acceso individual/autorizado.

**Aceptación:** recorrido automatizado E2E completo; aplicación real revisada en Studio para los casos habilitados; mappings no probados permanecen bloqueados y los informes distinguen “generado”, “inspeccionado” y “validado en Studio”.

## Reglas de seguridad y alcance

- El MCP solo escucha en loopback durante el MVP y la API es el único cliente; no exponer MCP a Internet ni permitir endpoint arbitrario en una UI sin autenticación.
- El portal inicia la aplicación en una acción explícita del usuario. No auto-aplicar al subir ZIP. Un futuro modo automático se limita a mappings validados y necesita activación separada.
- Crear en carpeta/proyecto de prueba por defecto. Nunca aplicar sobre Jobs productivos, ejecutar Jobs, borrar componentes ni guardar credenciales en esta versión.
- No declarar creado/validado solo por recibir `ok`: inspeccionar el Job resultante y usar estado de Studio separado.
- Referencias de catálogo y parámetros no verificados siguen visibles; el MCP puede confirmar estructura en el workspace, pero eso no sustituye documentación oficial ni equivalencia semántica con SAS.

## Decisiones pendientes para arrancar la implementación

1. Confirmar que el primer destino será un proyecto Talend de prueba en el mismo Windows donde corre el MCP.
2. Definir si la primera versión debe crear Jobs nuevos únicamente o permitir actualizar una copia de Jobs existentes. Recomendación: crear nuevos y añadir actualización después de validar snapshot/diff/restore.
3. Seleccionar el primer mapping piloto de SAS→Talend, sencillo y con datos locales, para medir el recorrido completo antes de ampliar cobertura.
