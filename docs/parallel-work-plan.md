# Trabajo paralelo: SAS Grid → Talend

## Objetivo y punto de partida

Este plan asigna trabajo concreto a **Joseph, Andres y Byron**, en tres frentes que pueden avanzar simultáneamente. El proyecto ya cuenta con importación segura, API, parser, dependencias/Grid, IR, generación y exportación de planes, frontend y catálogo Talend. La tarea es validar y mejorar esas capacidades, no reconstruirlas.

Estado y diseño existente: `docs/progress.md`, `docs/architecture.md`, `docs/sas-coverage.md`, `docs/pilot-report.md`. Antes de tomar cualquier punto, buscar si ya tiene implementación o test. Si ya funciona, producir evidencia de validación en vez de rehacerlo.

**Objetivo del primer sprint:** tres entregas revisables e independientes: un recorrido backend probado por Andres, dos mejoras SAS acotadas por Joseph y un flujo web validado por Byron. Cada persona trabaja en su rama/worktree y no edita las rutas propietarias de otra persona.

## Contrato y reglas compartidas

El contrato vigente está en `src/sas_grid_migrator/migration_planner/models.py`; el JSON Schema sincronizado está en `schemas/migration-plan.schema.json`.

- No crear otro formato de plan ni reemplazar el contrato por el JSON de un prototipo.
- No cambiar modelos/esquema durante el primer sprint, salvo que un caso real no pueda expresarse. En ese caso, describir el caso, acordarlo con Andres y actualizar modelo, esquema, pruebas y consumidor frontend en un PR coordinado.
- Preservar evidencia SAS (`archivo:línea`), estados `in_catalog` y `verified` diferenciados, y resultados inciertos como pendientes/no traducibles con motivo.
- Las reglas de conversión deben seguir usando el catálogo existente `rules/talend/components.json`; no editar a mano el catálogo generado.
- No declarar equivalencia o verificación de Talend solo porque un componente aparezca en el catálogo.

## Andres — backend e integración de extremo a extremo

**Meta:** demostrar con una prueba reproducible que las piezas backend existentes producen un plan utilizable y exportable, y cerrar la brecha que esa prueba revele.

**Rama sugerida:** `feature/integration-e2e`.

**Rutas que puede cambiar:** `apps/api/`, `src/sas_grid_migrator/ingestion/`, `src/sas_grid_migrator/intermediate_representation/`, `src/sas_grid_migrator/migration_planner/` excepto `expressions.py`, `schemas/` solo con acuerdo, `tests/integration/`, `tests/unit/test_ingestion.py`, un nuevo `tests/integration/test_api_e2e.py` si hace falta y `docs/progress.md`. Andres no edita `tests/unit/test_planner.py`, que Joseph puede necesitar para expresiones/reglas.

**No cambiar durante el trabajo normal:** `rules/sas/`, `rules/mappings/`, `src/sas_grid_migrator/migration_planner/expressions.py`, `apps/web/` ni el catálogo generado. Coordinar si una corrección cruza esas fronteras.

### Tareas detalladas

1. **Establecer la línea base.** Ejecutar la suite Python y anotar comandos, resultado y cualquier fallo preexistente. No atribuir a este trabajo fallos ajenos.
2. **Elegir un escenario vertical.** Usar uno de los fixtures ya mantenidos, por ejemplo `tests/fixtures/sas/p0_clientes_activos.sas` o el lote de `tests/fixtures/sas/real/ts-sas-legacy-analytics/`. Cubrir importación → análisis → generación de planes → lectura del plan → exportación Markdown/JSON/CSV.
3. **Verificar contenido, no solo HTTP 200.** La prueba debe comprobar que el plan corresponde al programa esperado, que los pasos conservan `evidence.file` y `evidence.line`, que hay estado/pendientes coherentes, que el JSON valida contra `JobPlan`/schema y que los archivos esperados de exportación se producen.
4. **Arreglar solo una brecha reproducida.** Si el recorrido descubre un defecto, corregirlo en la capa responsable, añadir regresión y mantener los límites de importador/API. No ampliar a una reescritura del parser.
5. **Decidir el formato de entrada.** La web actual sube ZIP; la API de ruta local acepta rutas del servidor. Revisar con el equipo si usuarios necesitan `.sas`/`.sh` sueltos. Si no existe caso de uso confirmado, documentar que ZIP es suficiente y no añadir formatos. Si se acuerda hacerlo, reutilizar `import_source` y cubrir límites, extensión, errores y entradas múltiples.
6. **Actualizar estado al final.** Cambiar `docs/progress.md` solo con resultados comprobados y quitar o corregir afirmaciones que ya no describan el estado real.

### Pruebas y entrega

- Focalizadas: `uv run pytest tests/integration tests/unit/test_ingestion.py`.
- Suite completa antes de integrar: `uv run pytest`.
- Calidad: `uv run ruff check`.
- PR con: escenario reproducido, archivos afectados, comportamiento esperado/real, prueba añadida y resultado de comandos.

**Terminado cuando:** el escenario vertical tiene prueba automatizada que inspecciona contenido del plan y exportación; cualquier defecto corregido tiene regresión; la decisión sobre cargas ZIP/individuales queda escrita. No se exige que el plan traduzca automáticamente lo que correctamente marca como pendiente.

## Joseph — cobertura SAS, macros y reglas de conversión

**Meta:** cerrar dos brechas SAS demostrables y de prioridad alta, con conversión prudente y pruebas derivadas del corpus existente.

**Rama sugerida:** `feature/sas-coverage`.

**Rutas que puede cambiar:** `rules/sas/`, `rules/mappings/`, `src/sas_grid_migrator/macro_resolver/`, `src/sas_grid_migrator/migration_planner/expressions.py`, `tests/unit/test_parser.py`, `tests/unit/test_planner.py`, `tests/unit/test_policy_and_fixtures.py` y nuevos tests focalizados de reglas/macros/expresiones. Estas pruebas quedan bajo Joseph para evitar conflictos con la integración de Andres.

**No cambiar sin acuerdo:** modelos/esquemas de plan, API, importador, frontend ni `rules/talend/components.json`/catálogo generado. Las propiedades de reglas deben apuntar a nombres existentes; si el catálogo parece incorrecto, reportar la evidencia a Andres en vez de parchearlo localmente.

### Tareas detalladas

1. **Crear una lista de brechas antes de editar.** Revisar frecuencias de `docs/sas-coverage.md`, casos de `tests/fixtures/sas/real/` y reglas presentes en `rules/sas/constructs.json` y `rules/mappings/talend-components.json`. Para cada candidata anotar construcción SAS, archivo/fragmento de evidencia, comportamiento actual, resultado esperado y prueba afectada.
2. **Escoger exactamente dos primeros casos.** Priorizar por frecuencia/impacto y factibilidad; `%sysfunc`, `%include`, `proc sql`, `merge` o `proc format` son candidatas, no tareas obligatorias si ya están cubiertas. Evitar asumir que hace falta un nuevo `rules/sas/catalog.json`: primero demostrar qué información no expresa el esquema actual de construcciones/reglas.
3. **Definir el comportamiento seguro.** Para cada caso especificar cuándo se traduce, qué propiedades/componentes sugiere, qué evidencia conserva, qué debe confirmar una persona y qué entradas quedan sin resolver. En semántica ambigua, producir pendiente/no traducible con motivo; no inventar Java ni parámetros Talend.
4. **Implementar en la capa responsable.** Clasificación en `rules/sas/constructs.json`; correspondencia en `rules/mappings/talend-components.json`; expansión estática solo en `macro_resolver`; expresiones solo en `migration_planner/expressions.py`. Mantener separados los cambios por caso cuando sea posible.
5. **Añadir pruebas pequeñas y representativas.** Cada regla debe tener test positivo y al menos un límite/error relevante. Para expresiones, comprobar tanto la traducción como el rechazo explícito de formas no soportadas. Usar fixtures mínimos nuevos o existentes; nunca depender de datos de cliente no versionados.
6. **Comprobar compatibilidad del catálogo.** Correr el test de coherencia de mappings/catalog y verificar que cada nombre de componente/propiedad realmente pertenece al catálogo aplicable. `in_catalog` no equivale a `verified` por Talend Studio.
7. **Informar cobertura con precisión.** No afirmar “90 %” hasta definir el corpus y el denominador (ocurrencias, construcciones únicas o pruebas). En el PR reportar qué casos se cubrieron y cuáles permanecen pendientes.

### Pruebas y entrega

- Ejecutar los tests focalizados que correspondan: `uv run pytest tests/unit/test_talend_catalog.py tests/unit/test_parser.py tests/unit/test_planner.py tests/unit/test_policy_and_fixtures.py` (omitir rutas inexistentes solo si se renombra/organiza la suite en un PR acordado).
- Suite completa y lint antes de pedir integración: `uv run pytest` y `uv run ruff check`.
- PR con una tabla por cada uno de los dos casos: evidencia, antes/después, regla/código, pruebas, limitaciones y pendientes deliberados.

**Terminado cuando:** hay dos mejoras comprobables, pruebas de resultado y de límite, nombres compatibles con catálogo y explicación de qué sigue sin traducirse. No se requiere cobertura universal de macros/expresiones.

## Byron — web, recorrido de usuario y validación Talend

**Meta:** confirmar que una persona puede seguir la guía web actual y distinguir pasos propuestos, pendientes y verificados; corregir problemas de frontend reproducibles y validar planes si hay Talend Studio disponible.

**Rama sugerida:** `feature/web-validation`.

**Rutas que puede cambiar:** `apps/web/`, pruebas web, `.claude/scripts/e2e_web.mjs` si es necesario, y reportes nuevos en `docs/validation/`.

**No cambiar sin acuerdo:** API/backend, reglas SAS/mappings, modelos/esquema y catálogo Talend generado. Reportar discrepancias de datos a Joseph (mapeos) o Andres (contrato/API) con el ejemplo exacto.

### Tareas detalladas

1. **Ejecutar la prueba web existente.** Revisar `apps/web/package.json`, las pruebas en `apps/web/src/` y el runner `.claude/scripts/e2e_web.mjs`. El runner existente navega proyectos, importación por ruta, resumen, programas, dependencias, planes, una decisión de estado, exportación y catálogo; no asume carga ZIP si esa parte no está cubierta por el recorrido.
2. **Completar el flujo que usa el usuario.** Comprobar creación de proyecto, importación ZIP desde navegador, inventario, análisis, generación de planes, detalle con evidencia/pending, decisión por paso y exportación. Añadir un test para cualquier ruta importante que falte y evitar duplicar pruebas API pertenecientes a Andres.
3. **Corregir únicamente defectos reproducibles de UI.** Comprobar estados de carga/error, errores de subida, enlaces/volver, mensajes de pendientes y diferencias entre `in_catalog` y `verified`. Mantener navegación accesible y errores entendibles. No rediseñar la aplicación ni introducir otra forma de representar planes.
4. **Hacer la prueba manual de Talend si hay entorno.** Seleccionar hasta tres planes distintos (por ejemplo, uno dominado por SQL, uno DATA step/`merge` y uno con macro/Grid). Para cada uno, anotar programa/plan, pasos intentados, componente y propiedades contrastados, resultado, ambigüedades y captura/evidencia permitida. No editar un Job de producción ni afirmar validación si solo se consultó el catálogo.
5. **Si Studio no está disponible, no bloquear el frente.** Registrar la falta de entorno y el impacto, ejecutar la prueba automatizada del recorrido web, y dejar una lista priorizada de los casos que se deben contrastar cuando exista Studio.
6. **Gestionar los hallazgos por el dueño.** Discrepancia de componente/regla → Joseph; campo que falta en JSON o respuesta API → Andres. Abrir issue/PR con fixture, ruta, resultado esperado/real y severidad. Byron no cambia esos archivos en su rama.

### Pruebas y entrega

- Unit tests web: `cd apps/web && bun test`.
- Tipos/build: `cd apps/web && bun run build`.
- Smoke E2E existente requiere servidor y Chromium; uso documentado en el propio script: `node .claude/scripts/e2e_web.mjs <urlWeb> <rutaFixtures> <dirCapturas>`. Guardar capturas fuera de artefactos versionados salvo que sean evidencia necesaria y aprobada.
- PR con pruebas ejecutadas, pasos manuales, defectos encontrados/corregidos y resultados de validación Talend o bloqueo de entorno.

**Terminado cuando:** pruebas web/build pasan; el recorrido principal puede seguirse con estados y errores entendibles; existe reporte con validaciones reales o bloqueo explícito y plan de validación pendiente. No se exige que un usuario sin contexto externo resuelva datos de negocio que el SAS no contiene.

## Coordinación, ramas y no solapamiento

- Partir de `main` actualizado. Si comparten máquina, usar tres worktrees; si cada persona tiene clon propio, usar una rama por persona. No trabajar en el mismo directorio Git simultáneamente.
- Ramas: `feature/integration-e2e` (Andres), `feature/sas-coverage` (Joseph), `feature/web-validation` (Byron). Mantener ramas breves; abrir PR hacia `main`, no hacer push directo a `main`.
- Antes de empezar, cada persona comenta en el canal compartido: rama, fixture/caso elegido y archivos previstos. Si se necesita una ruta fuera de su propiedad, pedir acuerdo antes de editarla.
- Sincronización 1 (inicio): Andres confirma que el contrato actual basta para los casos elegidos. Si no, se trata como cambio coordinado separado.
- Sincronización 2 (mitad): Joseph comparte sus dos casos/reglas y evidencia; Andres confirma que encajan en el generador actual; Byron elige planes representativos para su recorrido.
- Sincronización 3 (integración): Byron presenta hallazgos UI/Talend; Joseph y Andres reciben issues por área; Andres revisa PRs y ejecuta la suite integrada.
- Cada PR debe explicar intención, pruebas y riesgos, y no incluir cambios de otra rama copiados para resolver conflictos.
- Fuera de alcance de este sprint: habilitar servicios de sistema/Tailscale, migración de datos, generación de `.item`, ejecución de SAS, conexión a bases productivas o prometer equivalencia completa.

## Cierre del primer sprint

El sprint se cierra cuando:

1. Andres deja un test automatizado de recorrido backend que comprueba contenido del plan y exportación, o un bloqueo reproducible con diagnóstico.
2. Joseph entrega dos cambios de cobertura SAS con pruebas focalizadas, límites documentados y compatibilidad con catálogo.
3. Byron entrega pruebas del flujo web/build y un reporte Talend de hasta tres planes, o documenta de forma explícita la falta de Studio y los casos pendientes.
4. Los tres PRs son revisados; Andres informa qué pruebas integradas corrieron y actualiza `docs/progress.md` solo con hechos comprobados.

Ningún trabajo se considera terminado solo por abrir un PR, escribir una regla, pasar TypeScript o consultar el catálogo: debe cumplir la aceptación de su frente y declarar qué no se pudo verificar.
