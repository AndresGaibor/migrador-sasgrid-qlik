# Progreso

## Estado validado

| Área | Estado | Evidencia y límites |
| ---- | ------ | ------------------ |
| SAS Grid / Joseph | Integrado, cobertura parcial | Catálogo v1: 10 entradas (0 `supported`, 7 `partial`, 3 `unsupported`). El planner consume catálogo y mappings; cada patrón de la matriz produce recomendación/estado con motivo y archivo/línea. |
| API / Andres | Flujo API validado | Prueba de integración cubre ZIP multiarchivo, análisis, plan, evidencia, progreso y exportación. El progreso se conserva en la base del proyecto. |
| Web / Byron | UI integrada; E2E pendiente de ejecución | ZIP, resumen, navegación a job/guía, evidencia, estados, catálogo Talend, enlaces de exportación y adaptación móvil implementados. `bun test` y build pasan. El runner Playwright está actualizado, pero Playwright no está instalado en este entorno. |
| Validación automatizada | Suite Python y web verificadas | `pytest -q`: 87 passed, 1 skipped; `ruff check .`: all checks passed; `bun test`: 2 passed; `bun run build`: passed. |
| Talend Studio | Conectado y verificado (28/10/2026) | Studio 8.0.1 con el Bridge `readWrite`. El portal lista 55 Jobs, crea y lee Jobs, y los fixtures P0 se aplican como borradores en `Process/PruebasPortal`. Los errores de Studio se informan en `design_errors`. No se afirma equivalencia SAS ↔ Talend: eso sigue siendo manual (`docs/equivalence-testing.md`). |

## Cobertura Grid

Los conteos describen entradas del catálogo, no ocurrencias ni porcentaje del universo SAS Grid. Se añadió [`docs/sas-grid-support.md`](sas-grid-support.md), basado entre otras fuentes en *Grid Computing in SAS 9.4, Fifth Edition* (PDF oficial local, ignorado por Git). La referencia confirma argumentos como `-GRIDJOBNAME`, `-GRIDWAITRESULTS` y el paso de opciones de proveedor mediante `-GRIDJOBOPTS`; no confirma el entorno objetivo del proyecto. Las formas `sasgsub` del fixture siguen siendo ilustrativas: las recomendaciones relacionadas permanecen `partial`; LSF y opciones desconocidas/incompletas quedan `unsupported` con motivo y evidencia. No elevar estados hasta identificar versión/proveedor y contrastar scripts representativos.

La suite omitió una prueba de importación de symlink porque Windows no concede el privilegio requerido en este entorno. La protección de symlinks no se declara validada aquí.

## Límites pendientes

- Ejecutar `.claude/scripts/e2e_web.mjs` con Playwright instalado y servicios web/API activos; confirmar upload, errores, navegación, progreso tras recarga, descarga, teclado y viewport móvil.
- Verificar nombres/opciones Grid con documentación o scripts representativos de una versión identificada.
- Probar casos representativos en Talend Studio y registrar versión, pasos, evidencia y resultado. Hecho con los fixtures P0 y P1; falta con programas reales.
- Abierto: Studio marca los `tMap` sin mapeo con "Unknown value in the list [Mapping links display as:]" en la vista Problemas (aparece en `design_errors`). Descartado: el `.item` guarda `LINK_STYLE=AUTO`; ningún valor (`AUTO`, `LINE`, `BEZIER_CURVE`) ni reconfigurar el nodo, cerrar y reabrir el editor o refrescar el workspace lo limpia; solo desaparece si el `tMap` recibe una conexión. Pendiente: abrir el Job en la interfaz de Studio para ver si la marca es real, y depurar el plugin Java (`JobProblems`).
- Resuelto: si la aplicación falla a mitad, el MCP borra los Jobs que creó en esa llamada y el error lo indica; los Jobs que ya existían no se tocan.
- Resuelto: el generador añade `tLogCatcher` + `tLogRow` y, si hay un componente de inicio, `tDie` por `SUBJOB_ERROR` (`BP-ERR-01`); ver `docs/talend-best-practices.md`.
- Ningún componente se marca verificado solo por una inspección viva: `talend-mcp` está conectado, pero el piloto con programas reales sigue pendiente.
- El piloto con programas reales del cliente sigue pendiente (`docs/pilot-report.md`).

## Corrida masiva contra Studio (28/10/2026)

Proyecto sintético `bancolombia_sas_synthetic_orchestration` (7 programas y un orquestador), aplicado por el flujo de lote
contra Studio 8.0.1: **8 de 8 Jobs creados** en 43 s, todos como `partially_applied` (borradores con pendientes de esquema
y de expresiones SAS). La primera pasada creó 6 de 8; lo que falló y se corrigió en el MCP y el plugin:

- Conectar dos `tFilterRow` seguidos (dos `WHERE` encadenados) se rechazaba: el validador buscaba la entrada en el conector `FILTER`, que es solo de salida.
- Esa misma conexión abre en Studio el diálogo modal "Do you want to get the schema of the target component?" que dejaba el hilo de interfaz colgado. El plugin lo contesta con No, y el MCP atiende los diálogos conocidos mientras conecta.
- `talend_job_problems` y la aplicación abrían el editor de cada Job y no lo cerraban; en lotes grandes saturaban Studio. Ahora cierran los editores que ellos abrieron (nunca uno que ya estaba abierto).

Abierto: la vista Problemas sigue marcando `tMap` (`LINK_STYLE`) y `tFilterRow` (`LOGICAL_OP`) borradores con "Unknown value in the list", aunque lo guardado en el `.item` coincide con lo que escribe Studio (`AUTO` y `&&`). Parece la caché en memoria de Studio; se confirmaría reiniciándolo y reabriendo uno de los Jobs.

### Corpus reales aplicados contra Studio (28/10/2026)

| Corpus | Programas | Resultado |
| ------ | --------- | --------- |
| `bancolombia_sas_synthetic_orchestration` | 8 | 8 creados |
| `ts-sas-legacy-analytics` (ETL banca y seguros) | 18 | 18 creados |
| `sas-access-samples` | 8 | 8 creados |
| `cmmi-shadow-bundles` | 4 | 4 creados |
| `ci360-download-client` | 4 | 4 creados |
| `learning-sas-by-example` | 3 | 3 bloqueados por tamaño (167, 205 y 500 componentes) |

Lo que fallaba y se corrigió: `tFilterRow` encadenados; el diálogo de esquema que colgaba la interfaz; editores sin cerrar que saturaban Studio; un trigger hacia un componente que no inicia subjob (`customer_profitability`); `tUnite` (entradas ilimitadas); nombres de Job repetidos entre carpetas (cuatro `bulkload.sas`). Un Job de 500 componentes agota el tiempo y dejaba restos, así que el API rechaza los de más de `TALEND_MAX_COMPONENTS` (200 por defecto) con un mensaje que pide dividir el programa.

## Verificación en Studio con el modo offline (28/10/2026)

`scripts/verify_in_studio.py` sobre todos los corpus, con escritura offline por defecto y sin errores inesperados de Studio:

| Corpus | Jobs | Tiempo | Antes (en vivo) |
| ------ | ---- | ------ | --------------- |
| `bancolombia_sas_synthetic_orchestration` | 8 | 19 s | 71 s |
| `ts-sas-legacy-analytics` | 18 | 39 s | 105 s |
| `tmsis-analytic-file` | 13 | 45 s | 71 s |
| `sas-access-samples` | 8 | 31 s | 51 s |
| `cmmi-shadow-bundles` y `ci360-download-client` | 4 + 4 | 16 s y 15 s | 27 s y 37 s |
| `sas_synthetic_customer360_multisource_v2` | 8 | 38 s | sin medir |
| `learning-sas-by-example` (3 programas, 47 Jobs con los hijos) | 47 | 56 s | 366 s y un Job de 500 componentes que fallaba |

Los Jobs nacen sin los errores de `tMap`, `tFilterRow` (`LOGICAL_OP`) ni `tRunJob` que producía montar los nodos por la API.
Quedan los pendientes esperados de un borrador (`Valores` vacíos, esquemas sin definir). Puertas automáticas sin Studio:
`tests/integration/test_corpus_gate.py` y `tests/integration/test_adversarial_projects.py`; ver `docs/production-readiness.md`.

Abierto: tras decenas de pruebas seguidas con los mismos nombres, la sesión de Studio devolvió errores de un Job anterior para
`job_02_load_accounts` (el mismo spec con otro nombre salió limpio); se despeja reiniciando Studio.

## Traductor de expresiones — MIG-009 (28/10/2026)

Las comparaciones que involucran columnas sin un tipo conocido ya no emiten una expresión Java candidata. El plan conserva
las condiciones simples de `tFilterRow` cuando se pueden representar, pero las deja como borrador con advertencia de tipos,
conversión y semántica de missing/nulos. Esto cubre comparaciones columna-columna, columna-literal y `IN`; no se ejecutaron
SAS, código importado, Studio ni Jobs Talend.

Métrica antes (`f4d3630`) → después: `real`, 8,1 % → 8,1 % (2 063 pasos; sin esquema 1 750 → 1 749; 627 expresiones);
`synthetic`, 16,8 % → 16,8 % (429 pasos; 303 sin esquema; 95 expresiones). No aumenta la automatización: se prioriza no
promover comparaciones cuyo tipo no puede demostrarse. Verificación: `uv run pytest -q` (556 passed, 1 skipped) y Ruff.
La comprobación en Studio queda pendiente por el límite de ejecución de esta tarea.

## Importación ZIP — MIG-029 (28/10/2026)

Se añadió `max_zip_members` (10 000 por defecto; configurable con `SGM_MAX_ZIP_MEMBERS`) y el importador rechaza el ZIP
completo cuando supera la cuota, antes de ordenar, extraer o acumular miembros omitidos. Python `ZipFile.infolist()` aún
materializa la tabla central, así que el límite no elimina el coste inicial de metadatos. Prueba sintética offline para
excedentes compuestos solo por rutas inseguras. Métricas antes → después: `real` 8,1 % → 8,1 % (2 063 pasos), `synthetic`
16,8 % → 16,8 % (429 pasos); cambio no relacionado con automatización SAS. Verificación focal: 20 passed, 1 skipped;
Ruff pasó. Sin SAS, código importado, Studio ni Jobs Talend.

## Aplicación offline Talend — MIG-023 (28/10/2026)

El fallback a Studio queda limitado a fallos de `dryRun`; un error durante la escritura se devuelve sin repetir la operación
por otra vía. El batch crea los dos ficheros con exclusión y revierte el `.item` nuevo si falla el `.properties`. Para una
respuesta perdida tras una escritura completa, el portal añade una marca SHA-256 de propiedad; el batch reconoce en el
reintento el par que conserva esa misma marca y no sobrescribe un Job distinto. Métrica antes → después: `real` 8,1 % →
8,1 % (2 063 pasos), `synthetic` 16,8 % → 16,8 % (429 pasos). Verificación focal offline de Python y MCP; la simulación
de timeout posterior a persistencia completa no se ejecutó. Sin Studio ni Jobs Talend.

## Fase 1 de UX del portal (28/10/2026)

Se entregaron las opciones 1, 2, 3, 8, 9, 10, 19 y 20 de la hoja de ruta de [`docs/superpowers/specs/2026-10-28-portal-ux-design.md`](superpowers/specs/2026-10-28-portal-ux-design.md). El plan de ejecución está en [`docs/superpowers/plans/2026-10-28-portal-ux-fase1.md`](superpowers/plans/2026-10-28-portal-ux-fase1.md).

| Opción | Entrega | Dónde se ve |
| ------ | ------- | ----------- |
| 1 y 2 | Nombre y descripción del Job editables. La descripción se incluye en los argumentos enviados al MCP (`to_mcp_arguments`); no se ha verificado que Studio muestre el valor personalizado | Cabecera de la guía del Job (`views/plans/JobIdentity.tsx`) |
| 3 | Renombrado masivo con vista previa, error por fila y aplicación todo o nada | Lista del plan (`views/plans/BulkRename.tsx`) |
| 8 | Plantilla de nombres `job_{programa}`, editable, con ejemplo en vivo | Configuración |
| 9 | Laboratorio del traductor: SAS de entrada, Java para Talend, columnas, avisos y motor | Ruta `#/traductor` |
| 10 | Edición de la expresión Talend en cada paso, con marca «editada» y «Volver a la traducción automática» | Tarjeta de paso (`views/plans/ExpressionEditor.tsx`) |
| 19 | Barra de seis etapas y botón con la siguiente acción | Resumen del proyecto (`components/ProjectStepper.tsx`, `views/summary/ProjectCommandCenter.tsx`) |
| 20 | «Qué falta»: pendientes agrupados por motivo, con enlaces a los Jobs afectados | Resumen del proyecto (`views/summary/PendingPanel.tsx`) |

Las ediciones se guardan en SQLite (tablas `job_overrides`, `expression_overrides` y `portal_settings`) y se superponen al plan al leerlo. `plans.json` no recibe ediciones de nombre, descripción ni expresión. Detalle y reglas en la receta «Ediciones humanas sobre el plan» de [`agent-guide.md`](agent-guide.md). Las escrituras de edición responden 409 mientras un lote o una operación Talend esté activo en el proyecto.

Verificación ejecutada en el worktree `migrador-sasgrid-qlik-ux`:

- `uv run pytest -q --ignore=tests/integration/test_corpus_gate.py --ignore=tests/integration/test_mcp_contract.py`: 584 passed, 1 skipped. Esos dos archivos dependen del MCP, que no está instalado en el worktree, así que no se ejecutaron.
- `cd apps/web && bun test`: 106 pass, 0 fail.
- `cd apps/web && bun run typecheck`: sin errores.

Pendiente y no verificado:

- Nada se ha comprobado en un navegador. Solo hay pruebas unitarias y de componente con `bun test`.
- Nada se ha comprobado contra Talend Studio. La `description` enviada al MCP no se ha aplicado en Studio.
- No se ha ejecutado `tests/integration/test_mcp_contract.py` para comprobar que el MCP acepta una `description` personalizada; queda pendiente hasta tener el MCP instalado.
- Renombrar un Job que ya existe en Studio no lo renombra en Studio. El portal lo indica; el Job anterior queda y el nuevo se creará al aplicar de nuevo (no verificado contra Studio).
