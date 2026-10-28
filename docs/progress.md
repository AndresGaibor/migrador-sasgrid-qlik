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

Los conteos describen entradas del catálogo, no ocurrencias ni porcentaje del universo SAS Grid. Las formas `sasgsub` del fixture son ilustrativas: no se confirmó su sintaxis contra una versión de SAS Grid. Por eso las recomendaciones relacionadas permanecen `partial`; LSF y opciones desconocidas/incompletas quedan `unsupported` con motivo y evidencia. No elevar estados hasta contrastar scripts representativos o fuentes de la versión objetivo.

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
