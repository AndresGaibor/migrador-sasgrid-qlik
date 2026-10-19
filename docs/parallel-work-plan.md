# Plan de trabajo para completar SAS Grid → Talend guiado en la web

## Meta del producto

El objetivo no es solo que pasen pruebas o que cada persona termine un sprint. El resultado final buscado es que una persona pueda entregar a la aplicación un proyecto/archivo SAS Grid y recibir en la web una guía de migración a Talend que pueda seguir, paso a paso, con evidencia del código fuente y sin ocultar lo que no se puede determinar.

Para declarar este objetivo cumplido, el producto debe ofrecer:

1. **Catálogo SAS Grid:** inventario versionado y con fuentes para los comandos, opciones, parámetros, directivas y patrones de planificación/Grid que el proyecto declara soportar. Debe indicar qué se reconoce, cómo se interpreta, a qué acción Talend se asocia, qué evidencia genera y qué no se soporta todavía.
2. **Catálogo Talend con trazabilidad oficial:** inventario navegable de componentes/artefactos Talend usados por las recomendaciones, propiedades pertinentes, compatibilidad/versionado y enlace a documentación oficial de Qlik/Talend. No llamar “oficial” a un dato solo porque aparezca en un catálogo comunitario o en Studio.
3. **Recorrido guiado en la web:** cargar un archivo/proyecto, analizar dependencias SAS Grid, y ver por cada programa/job un orden de pasos accionables para construir/configurar el equivalente en Talend. Cada paso debe enlazar la evidencia SAS (archivo y línea), el componente/artefacto recomendado, valores o decisiones requeridos, dependencias/orden y referencia oficial; permitir registrar progreso y exportar la guía.
4. **Límites transparentes:** todo caso ambiguo, incompleto o no soportado queda señalado con su motivo y la acción humana necesaria. No ejecutar SAS ni escribir directamente en Talend Studio como si la aplicación pudiera garantizar equivalencia automática.

### Qué significa “100%” en este plan

“100%” significa pasar todos los criterios de aceptación de abajo **para la matriz de soporte publicada y probada**, con fuentes, cobertura y limitaciones explícitas. No significa traducir cualquier programa SAS/Grid imaginable ni asegurar equivalencia en producción sin validación del usuario. Cada entrada fuera de la matriz queda identificada como no soportada; no se presenta como resultado terminado.

## Estado real y brechas conocidas

### Avance verificado en el repositorio

- **SAS Grid:** existe `rules/sas/grid_catalog.json` v1 con 10 entradas: 0 `supported`, 7 `partial`, 3 `unsupported`. El planner consume catálogo y mappings, con motivo y evidencia por ocurrencia. Las formas `sasgsub` son ilustrativas y no están confirmadas contra una versión real de SAS Grid; no elevar a `supported`.
- **Talend:** `rules/talend/components.json` separa ahora el inventario oficial Qlik R2026-01 (693 componentes) de 577 esquemas estructurados derivados de Talaxie/Talend Open Studio. Hay 398 nombres en común, 295 componentes oficiales sin esquema abierto y 179 esquemas fuera de ese inventario. El inventario oficial se muestra por separado en la web; no se debe llamar oficial a los parámetros derivados de Talaxie. La documentación local enlaza fuentes oficiales, pero aún falta trazabilidad/verificación por componente y versión para todo componente recomendado.
- **Backend (Andres):** se admite ZIP de proyecto y archivo `.sas` individual. La integración cubre ZIP multiarchivo, análisis, planes, recomendaciones Grid, evidencia, actualización del progreso y exportación. El progreso se guarda en la base del proyecto.
- **Web/catálogo (Byron):** la UI conecta el contrato API, muestra evidencia navegable, recomendaciones Grid, catálogo Talend y enlaces de exportación. `bun test` y `bun run build` pasan. El runner Playwright cubre el flujo requerido, pero no se pudo ejecutar porque Playwright no está instalado en este entorno.
- **Verificación del estado actual:** `pytest -q` (87 passed, 1 skipped), `ruff check .`, `cd apps/web && bun test` (2 passed) y `cd apps/web && bun run build` pasan. El test omitido requiere privilegio de symlink que Windows no concede aquí. No se ha hecho validación en Talend Studio.

### Estado por frente (no declarar 100% todavía)

- **Joseph:** matriz versionada, mappings y resultados verificables por entrada integrados. La sintaxis de ejemplos `sasgsub` sigue sin fuente de versión y todas esas entradas continúan parciales.
- **Andres:** integrado el catálogo al planner y validado ZIP → guía exportada por API. Siguen pendientes cobertura ampliada de errores/seguridad y pruebas tras reinicio del servicio.
- **Byron:** UI y catálogo conectados al API, con evidencia, progreso y exportaciones. Pendiente ejecutar el E2E con Playwright instalado y verificar componentes en Studio cuando esté disponible.

Estos avances describen solo lo que está comprobado en el repositorio; no equivalen a terminar el producto. Las brechas restantes y la definición de “100%” se mantienen en los criterios que siguen.

## Contrato funcional compartido

- Mantener el modelo de plan de `src/sas_grid_migrator/migration_planner/models.py` y sincronizar `schemas/migration-plan.schema.json` si se acuerda un cambio de contrato.
- Los pasos deben ser útiles sin leer el código de la aplicación: nombre del paso, instrucción concreta, resultado esperado, evidencia `archivo:línea`, componentes/artefactos y propiedades sugeridos, dependencias previas, elecciones que debe resolver la persona, estado y motivo de bloqueo si aplica.
- Separar “conocido por el catálogo”, “documentado oficialmente”, “probado en versión de Talend” y “validado en un Job de prueba”. No intercambiar estas etiquetas.
- Ningún dato desconocido se convierte en un valor supuesto. Conservar el código/valor original como evidencia, pedir decisión y explicar el riesgo.
- ZIP es el formato inicial acordado para un proyecto con varios archivos. Un SAS o script suelto se acepta solo si el recorrido y la detección de dependencias pueden funcionar sin perder contexto; en otro caso, explicar en la UI que se requiere un ZIP.

## Joseph — catálogo y cobertura SAS Grid → recomendaciones

**Meta:** que cada patrón SAS/Grid dentro de la matriz publicada tenga clasificación, evidencia, límites, pruebas y una recomendación Talend conservadora o un resultado explícito de no soportado.

**Propietario de datos/reglas:** `rules/sas/grid_catalog.json` (crear si se confirma que no existe), `rules/sas/constructs.json`, `rules/mappings/talend-components.json`, pruebas de parser/planner y matriz/casos bajo `tests/fixtures/sas/grid/`. No editar los componentes Talend generados ni el frontend/API.

### Trabajo hasta aceptación

1. **Definir la matriz de soporte con evidencia.** Inventariar variantes presentes en fixtures/corpus y ejemplos objetivo de `sasgsub`, invocaciones `sas`, opciones como `-grid`, `-queue`, `-name`, `-wait`, `-set`, `-sysin`, ejecución batch, referencias a scripts, dependencias, y planificadores externos identificados (por ejemplo LSF `bsub`/`bjobs` o Control-M cuando aparezcan). No marcar algo “soportado” solo por nombrarlo en documentación: debe haber un caso de entrada y un resultado comprobable.
2. **Registrar el catálogo de Grid con estructura verificable.** Para cada patrón: identificador, comando/directiva y formas admitidas, descripción, opciones y valores parseados, sistema/versión si se conoce, fuente/cita o fixture de origen, línea de entrada, patrón equivalente/no equivalente en Talend, requisitos previos, limitaciones y estado (`supported`, `partial` o `unsupported`). Especificar cómo se incorporan variantes nuevas sin alterar silenciosamente el significado.
3. **No mezclar catálogos.** Las semánticas SAS/Grid viven en el catálogo Grid; los componentes y propiedades destino permanecen en el catálogo Talend. Las reglas de mapping referencian el identificador de destino existente, no copian definiciones de componentes.
4. **Añadir escenarios representativos.** Cubrir casos positivos, espacios/comillas, orden distinto de argumentos, valor ausente/ambiguo, opción desconocida y referencia a archivo dependiente. Para cada elemento marcado soportado, verificar datos parseados, evidencia de origen y recomendación/pendiente esperado.
5. **Cubrir el salto a la acción Talend.** Para cada patrón soportado, escribir instrucciones concretas y orden de ejecución (qué crear, qué conectar/configurar, qué valor trasladar, qué confirmar). Si no hay equivalencia razonable, indicar que el usuario debe recrear/confirmar la orquestación y no sugerir un componente ficticio.
6. **Publicar límites y conteos.** Reportar cantidades por estado y cómo se calculan (entradas del catálogo, casos de fixture, ocurrencias u otra unidad). No usar un porcentaje ambiguo de cobertura.

### Pruebas y criterios de Joseph

- Ejecutar: `uv run pytest tests/unit/test_parser.py tests/unit/test_planner.py tests/unit/test_policy_and_fixtures.py tests/unit/test_talend_catalog.py` y `uv run ruff check`.
- Cada entrada declarada `supported` de la matriz tiene al menos un test de parseo/análisis y uno de recomendación/plan; casos `partial`/`unsupported` tienen test que comprueba el estado y el motivo.
- Validar que todo mapping usa componente/propiedad existentes en el catálogo Talend y que evidencia incluye ruta y línea reales.
- **100% de este frente:** matriz acordada versionada; todos los patrones dentro de la matriz tienen resultado probado; límites/versiones/fuentes documentados; ninguna recomendación afirma más de lo comprobado.

## Andres — ingesta, contrato, análisis e integración backend

**Meta:** recibir el ZIP del proyecto, analizar archivos SAS/Grid relacionados y entregar por API un plan completo, ordenado y legible por la web, con el catálogo Grid y mappings como entradas de datos comprobables.

**Propietario backend/contrato:** `apps/api/`, `src/sas_grid_migrator/ingestion/`, `src/sas_grid_migrator/grid_analysis/`, `src/sas_grid_migrator/intermediate_representation/`, `src/sas_grid_migrator/migration_planner/` excepto `expressions.py`, modelos/schema con coordinación, `tests/integration/`, `tests/unit/test_ingestion.py` y `docs/progress.md`. No modificar las reglas de Joseph, el catálogo Talend de Byron ni `apps/web/`.

### Trabajo hasta aceptación

1. **Especificar el input y sus fallos.** Documentar estructura de ZIP admitida, extensiones procesadas, límites actuales de tamaño/seguridad, nombres/rutas duplicadas, encoding, archivo corrupto, ZIP vacío y referencias a archivos fuera del proyecto. No relajar validaciones de extracción segura.
2. **Construir el inventario de proyecto.** Confirmar que los archivos SAS, scripts shell y referencias Grid se relacionan por ruta/identificador; conservar archivos que no se pueden resolver como pendientes con ruta y motivo, no descartarlos sin aviso.
3. **Consumir la matriz de Joseph.** El analizador backend debe producir resultado determinista por línea/patrón, con estado, datos interpretados, evidencia original, relación con job/programa y recomendación/razón. Rechazar esquema inválido con error legible; probar versión de catálogo y compatibilidad.
4. **Generar una guía ejecutable por persona.** El plan organiza pasos por job/programa y dependencias; cada paso incluye instrucción, resultado esperado, posición, evidencia, referencias de catálogo, valores sugeridos, decisiones manuales, prerequisitos y estado inicial. Validar el JSON contra modelo y schema y mantener compatibilidad con consumidores.
5. **Exponer flujo completo por API.** Probar carga del ZIP → proyecto/importación → análisis → plan(es) → lectura de detalle → actualización de estado/progreso → exportación. Asegurar errores útiles para ZIP no válido, proyecto sin fuentes, archivo con sintaxis no soportada y catálogo incompatible.
6. **Acordar progreso persistente.** Definir si estado de cada paso vive en backend y se conserva tras recargar/salir, o si el primer release lo persiste solo dentro del proyecto/session. La elección debe quedar consistente entre API, esquema, web y exportación; no prometer persistencia si no existe.
7. **Probar determinismo y regresiones.** Un mismo ZIP y versiones de catálogos iguales producen los mismos pasos/orden; un cambio en catalog version o contenido queda identificable. No requerir acceso a Talend ni a sistemas productivos para correr pruebas.

### Pruebas y criterios de Andres

- Ejecutar tests focalizados de `tests/integration/` y `tests/unit/test_ingestion.py`; suite completa `uv run pytest`; lint `uv run ruff check`.
- Tener pruebas de contrato/API con upload ZIP real de fixture y aserciones de contenido, evidencia, orden de pasos, estados, actualización de progreso y exportación; no limitarse a HTTP 200.
- Añadir pruebas de seguridad para ZIP malicioso/traversal/tamaño según límites existentes y regresiones de errores.
- **100% de este frente:** un fixture representativo multiarchivo llega por la API hasta una guía validada/exportada; errores y datos desconocidos son explícitos; progreso se conserva según decisión acordada; sin regresiones en suite.

## Byron — catálogo Talend trazable y experiencia guiada web

**Meta:** mostrar un catálogo de destino con referencias oficiales verificables y hacer que una persona siga la guía generada después de subir un proyecto, con estados y decisiones claros.

**Propietario catálogo/UI:** `rules/talend/components.json`, su generador/ingesta de catálogo (identificar ruta real antes de tocarla), `docs/reference/talend/`, `apps/web/` y tests web/E2E. No modificar API, modelos, catálogo Grid o mappings de Joseph.

### Trabajo hasta aceptación

1. **Auditar origen y versión del catálogo actual.** Para cada componente actualmente recomendado, contrastar nombre, familia, propósito y propiedades esenciales con documentación oficial Qlik/Talend de la versión objetivo o el entorno disponible. Guardar en el dato al menos versión/familia, URL oficial consultada, fecha/estado de verificación y limitaciones. El catálogo comunitario puede servir de índice semilla; no presentarlo como fuente oficial.
2. **Precisar el alcance oficial.** Definir versión de Talend objetivo y el conjunto de componentes requeridos por los mappings soportados. Completar el conjunto requerido antes de ampliar a todos los componentes existentes. Componente sin página oficial o discrepancia no confirmada queda `unverified`/`needs_review`; no inventar parámetros ni redistribuir contenido propietario de Qlik.
3. **Hacerlo explorable.** En la web ofrecer búsqueda/filtro en componentes usados por la guía; ficha con función, familia/versión, propiedades relevantes, estado de verificación y enlace oficial. Mostrar diferencia entre candidato de catálogo y verificación real en Studio.
4. **Implementar el modo guiado.** Tras cargar ZIP: indicar resultado de importación y proyectos; listar jobs/programas; permitir abrir guía ordenada; presentar claramente “haz esto en Talend”, campo/componente/valor sugerido, evidencia SAS clicable, fuente oficial, dependencias y decisión pendiente. No obligar a deducir pasos de JSON crudo.
5. **Permitir progreso utilizable.** Marcar paso pendiente/en progreso/completado/bloqueado, pedir confirmación en pasos inciertos, guardar/recuperar estado usando el mecanismo acordado con Andres y dejar visible por qué un paso está bloqueado. Añadir retorno a paso anterior y navegación entre jobs sin perder estado.
6. **Exportar el trabajo.** Exponer descarga de guía Markdown/JSON (y los formatos existentes que sean útiles) incluyendo referencias, estados y pendientes. No generar un artefacto nativo Talend `.item` salvo que se diseñe y valide aparte.
7. **Validar UI con datos reales/fakes representativos.** Automatizar el recorrido upload → resumen → job → guía → marcar estado → recargar/verificar → exportar. Comprobar vacíos, error de upload, análisis en progreso, API error, casos no soportados, teclado/labels y layout móvil básico.
8. **Validar con Talend cuando se disponga de Studio.** Ejecutar los pasos para casos representativos en proyecto de prueba, registrar versión, evidencia y resultado. Si Studio no está disponible, completar catálogo enlazado y E2E automatizado, pero mantener “validado en Studio” como pendiente y no declarar equivalencia real al 100%.

### Pruebas y criterios de Byron

- Ejecutar `cd apps/web && bun test` y `cd apps/web && bun run build`.
- Ejecutar smoke E2E con backend/web activos: `node .claude/scripts/e2e_web.mjs <urlWeb> <rutaFixtures> <dirCapturas>`; ampliar el runner si no cubre upload ZIP, guía/progreso y exportación.
- Cada componente usado por una recomendación soportada tiene referencia oficial accesible y estado de procedencia visible; propiedades mostradas están cotejadas o marcadas como no verificadas.
- **100% de este frente:** usuario termina el flujo de carga y guía en la UI sin inspeccionar internals; progreso y exportación funcionan; catálogo destino tiene trazabilidad oficial para todo componente requerido; resultado Studio se declara solo si se probó.

## Entrega, dependencias y coordinación

### Propiedad para evitar conflictos

- **Joseph:** datos/reglas SAS Grid, mappings y sus tests (`rules/sas/grid_catalog.json`, `rules/sas/constructs.json`, `rules/mappings/talend-components.json`, `tests/unit/test_parser.py`, `tests/unit/test_planner.py`, `tests/unit/test_policy_and_fixtures.py`).
- **Andres:** pipeline/backend, contrato e integración (`apps/api/`, `src/sas_grid_migrator/`, `schemas/`, `tests/integration/`, `tests/unit/test_ingestion.py`).
- **Byron:** componentes/fuentes Talend y web (`rules/talend/components.json`, generador de catálogo, `docs/reference/talend/`, `apps/web/`, pruebas web/E2E).
- Si una tarea requiere ruta ajena, abrir PR/issue y acordar el cambio; no copiar cambios de otra rama. Revisar generadores antes de editar archivos generados.

### Secuencia obligatoria

1. **Contrato de soporte (Andres coordina, Joseph y Byron confirman):** seleccionar versión de Talend, tipos de input y matriz de patrones Grid; definir las etiquetas de procedencia/validación y el contrato de cada paso.
2. **Trabajo paralelo:** Joseph construye catálogo/mappings y casos; Byron coteja catálogo Talend oficial y avanza UI con fixtures/contrato acordado; Andres implementa ingesta/plan API que consume esa forma de datos.
3. **Integración por etapas:** primero se valida el JSON del backend contra fixture y contrato; luego la web consume API real; después se corre E2E completo. No integrar tres prototipos con contratos incompatibles al final.
4. **Validación manual:** si existe Talend Studio, ejecutar matriz representativa en entorno de prueba. Si no existe, documentar claramente el bloqueo; la ausencia de Studio no impide terminar automatización/UI pero sí impide afirmar validación en Studio.
5. **Cierre:** suite completa, lint/build, auditoría de procedencia y matriz de soporte actualizada en `docs/progress.md`; cada brecha residual convertida en limitación/issue, no escondida bajo “100%”.

## Checklist final del producto

- [ ] La versión de Talend objetivo y ZIP/formato de entrada están documentados.
- [ ] Existe matriz versionada de SAS Grid con fuentes, opciones admitidas, pruebas, equivalencias y casos explícitamente no soportados.
- [ ] Los mappings solo recomiendan componentes/properties presentes en un catálogo Talend trazable; cada componente requerido enlaza documentación oficial de su versión.
- [ ] Un proyecto SAS Grid multiarchivo puede cargarse desde la web y no pierde relaciones/rutas de dependencias.
- [ ] La aplicación crea pasos ordenados por job, cada uno con instrucción, resultado esperado, valores, evidencia archivo/línea, enlaces y decisiones pendientes.
- [ ] La persona puede navegar, registrar progreso, recargar sin perderlo según la política acordada y exportar la guía completa.
- [ ] Desconocidos/errores no se interpretan en silencio ni se presentan como traducción verificada.
- [ ] Pruebas automatizadas cubren backend, catálogo, seguridad de upload, UI y el recorrido completo; `uv run pytest`, `uv run ruff check`, `cd apps/web && bun test`, `cd apps/web && bun run build` pasan.
- [ ] Validación de Talend Studio está demostrada con versión/evidencia o se deja explícitamente como única limitación de aceptación manual.
