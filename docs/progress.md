# Progreso

## Estado validado

| Área | Estado | Evidencia y límites |
| ---- | ------ | ------------------ |
| SAS Grid / Joseph | Integrado, cobertura parcial | Catálogo v1: 10 entradas (0 `supported`, 7 `partial`, 3 `unsupported`). El planner consume catálogo y mappings; cada patrón de la matriz produce recomendación/estado con motivo y archivo/línea. |
| API / Andres | Flujo API validado | Prueba de integración cubre ZIP multiarchivo, análisis, plan, evidencia, progreso y exportación. El progreso se conserva en la base del proyecto. |
| Web / Byron | UI integrada; E2E pendiente de ejecución | ZIP, resumen, navegación a job/guía, evidencia, estados, catálogo Talend, enlaces de exportación y adaptación móvil implementados. `bun test` y build pasan. El runner Playwright está actualizado, pero Playwright no está instalado en este entorno. |
| Validación automatizada | Suite Python y web verificadas | `pytest -q`: 87 passed, 1 skipped; `ruff check .`: all checks passed; `bun test`: 2 passed; `bun run build`: passed. |
| Talend Studio | Pendiente | No se encontró instalación de Talend Studio. No se afirma equivalencia validada en Studio. |

## Cobertura Grid

Los conteos describen entradas del catálogo, no ocurrencias ni porcentaje del universo SAS Grid. Las formas `sasgsub` del fixture son ilustrativas: no se confirmó su sintaxis contra una versión de SAS Grid. Por eso las recomendaciones relacionadas permanecen `partial`; LSF y opciones desconocidas/incompletas quedan `unsupported` con motivo y evidencia. No elevar estados hasta contrastar scripts representativos o fuentes de la versión objetivo.

La suite omitió una prueba de importación de symlink porque Windows no concede el privilegio requerido en este entorno. La protección de symlinks no se declara validada aquí.

## Límites pendientes

- Ejecutar `.claude/scripts/e2e_web.mjs` con Playwright instalado y servicios web/API activos; confirmar upload, errores, navegación, progreso tras recarga, descarga, teclado y viewport móvil.
- Verificar nombres/opciones Grid con documentación o scripts representativos de una versión identificada.
- Probar casos representativos en Talend Studio y registrar versión, pasos, evidencia y resultado cuando esté disponible.
- El servidor `talend-mcp` no está conectado; ningún componente se marca verificado por una inspección viva.
- El piloto con programas reales del cliente sigue pendiente (`docs/pilot-report.md`).
