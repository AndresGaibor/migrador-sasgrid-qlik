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
- Abierto: Studio marca los `tMap` sin mapeo con "Unknown value in the list [Mapping links display as:]" aunque el `.item` guarda `LINK_STYLE=AUTO`; parece una marca desactualizada de la vista Problemas (plugin Java).
- Resuelto: si la aplicación falla a mitad, el MCP borra los Jobs que creó en esa llamada y el error lo indica; los Jobs que ya existían no se tocan.
- Abierto: el generador no añade manejo de errores (`BP-ERR-01`); ver `docs/talend-best-practices.md`.
- Ningún componente se marca verificado solo por una inspección viva: `talend-mcp` está conectado, pero el piloto con programas reales sigue pendiente.
- El piloto con programas reales del cliente sigue pendiente (`docs/pilot-report.md`).
