# Trabajo paralelo: SAS Grid → Talend

## Estado de partida

El proyecto ya tiene implementadas la importación segura, API, parser, análisis de dependencias/Grid, IR, planes, exportación, frontend y catálogo Talend. No empezar esas partes de cero. Referencias: `docs/progress.md`, `docs/architecture.md`, `docs/sas-coverage.md`.

Este documento deja tres frentes listos para que **Joseph, Andres y Byron trabajen a la vez**, cada uno con entregables, rutas propietarias y criterios de aceptación. La asignación es nominal, no requiere otra decisión para arrancar. Si una tarea requiere salir del área asignada, abrir primero un issue/PR pequeño y acordar quién integra el cambio.

## Contrato común

El contrato vigente está en `src/sas_grid_migrator/migration_planner/models.py` y `schemas/migration-plan.schema.json`.

- No crear un segundo formato de plan.
- Cambiar el contrato solo si un caso concreto no puede expresarse hoy; actualizar modelo, esquema y prueba de sincronización en el mismo PR.
- Mantener la evidencia `archivo:línea`, los estados `in_catalog`/`verified` separados y las traducciones inciertas como pendientes/no traducibles.
- El JSON de fixture para UI debe derivarse del contrato actual, no inventar otra estructura.

## Andres — integración, API y recorrido completo

**Rama sugerida:** `feature/integration-e2e`

**Propiedad de archivos:** `apps/api/`, `src/sas_grid_migrator/ingestion/`, `src/sas_grid_migrator/intermediate_representation/`, `src/sas_grid_migrator/migration_planner/` salvo `expressions.py`, `schemas/`, `tests/integration/`, pruebas API/importación y documentación de estado.

**Tareas:**
1. Revisar y documentar las brechas del flujo existente: importar → analizar → generar plan → exportar. No reconstruir componentes que ya funcionan.
2. Añadir una prueba de aceptación de punta a punta con fixture representativo y verificar evidencia y pendientes.
3. Decidir con el equipo si hacen falta cargas de `.sas`/`.sh` sueltos. La UI/API actual soporta ZIP; si no hay necesidad demostrada, mantenerlo así. Si se acuerda implementar carga múltiple, reutilizar `import_source` y sus límites/validaciones.
4. Integrar PRs, resolver incompatibilidades y actualizar `docs/progress.md` cuando haya resultados verificados.

**No tocar sin coordinación:** `rules/sas/`, `rules/mappings/`, `migration_planner/expressions.py` y `apps/web/`.

**Aceptación:** recorrido reproducible probado; decisión documentada sobre carga individual; ninguna promesa de equivalencia automática que no esté cubierta por pruebas.

## Joseph — cobertura SAS y traducciones

**Rama sugerida:** `feature/sas-coverage`

**Propiedad de archivos:** `rules/sas/`, `rules/mappings/`, `src/sas_grid_migrator/macro_resolver/`, `src/sas_grid_migrator/migration_planner/expressions.py` y pruebas unitarias asociadas a reglas, macros y expresiones.

**Tareas:**
1. Usar frecuencias y ejemplos existentes en `docs/sas-coverage.md` y `tests/fixtures/sas/real/` para elegir construcciones aún incompletas; registrar construcción, archivo de evidencia y brecha.
2. Priorizar un lote pequeño de alta frecuencia (p. ej. `%sysfunc`, `%include`, `proc sql`, `merge`, `proc format`), confirmando primero qué está soportado.
3. Completar reglas/mapeos y el subconjunto conservador del traductor. Validar componentes y propiedades contra `rules/talend/components.json` y respetar el test de coherencia existente.
4. Añadir pruebas con casos mínimos derivados del corpus. Si la semántica no es segura, producir pendiente/no traducible con motivo; no adivinar.

**No tocar sin coordinación:** esquemas/modelos del plan, API, importador, UI ni catálogo Talend generado.

**Aceptación:** cada mejora tiene evidencia rastreable, test y mapeo válido en catálogo. No usar “90 %” hasta fijar denominador y corpus.

## Byron — experiencia web y validación con Talend

**Rama sugerida:** `feature/web-validation`

**Propiedad de archivos:** `apps/web/`, pruebas web, `.claude/scripts/e2e_web.mjs` si se conserva como runner vigente, y un informe nuevo `docs/validation/` para resultados manuales. No modificar reglas SAS/mappings ni el contrato compartido.

**Tareas:**
1. Ejecutar el recorrido web actual con Playwright: crear proyecto, subir ZIP, revisar inventario, generar/consultar plan, visualizar pendientes y exportar. Corregir solo problemas reproducibles de UX/funcionalidad.
2. Validar hasta tres planes representativos en Talend Studio (si Studio está disponible). Registrar plan/fixture, componente y propiedad probados, pasos confusos, discrepancias y evidencia. No marcar como `verified` por aparecer en el catálogo.
3. Enviar discrepancias de conversión a Joseph y de contrato/API a Andres como hallazgos con ejemplo, sin editar directamente sus archivos.
4. Proponer carga individual solo si las pruebas con usuarios la requieren; acordar el cambio API con Andres antes de implementarlo.

**No tocar sin coordinación:** backend/API, reglas/mapeos, modelos/esquema y catálogo de componentes.

**Aceptación:** prueba automatizada útil del flujo web y reporte de validación reproducible; las limitaciones de Studio/servidor se declaran, no se simulan.

## Flujo Git y sincronización

- Partir de `main` actualizado; usar worktrees separados si trabajan simultáneamente en la misma máquina, o ramas feature si cada quien trabaja en su clon.
- Nombres sugeridos: `feature/integration-e2e`, `feature/sas-coverage`, `feature/web-validation`.
- PR pequeños y enfocados; ejecutar las pruebas del área y dejar resultado en el PR. No mezclar cambios de otra área para “destrabar” una rama: coordinar primero.
- Orden de revisión: (1) Andres confirma contrato/áreas; (2) Joseph entrega primer lote de reglas con pruebas; (3) Byron valida UI y planes; (4) Andres integra y ejecuta el recorrido completo.
- Cambios compartidos a modelo/esquema se acuerdan en PR antes de que frontend/backend dependan de ellos.
- No habilitar servicios de sistema/Tailscale como parte de estas tareas: despliegue es trabajo separado.

## Primer sprint: trabajo simultáneo

Los tres frentes pueden arrancar desde `main` sin esperar cambios de otro frente. No cambien el contrato compartido durante este sprint; reporten una brecha con ejemplo si lo necesitan.

- **Andres — recorrido backend:** ejecutar y documentar el flujo API/importación → análisis → planes → exportación con un fixture del corpus; añadir la prueba de integración faltante si el flujo no queda cubierto. En paralelo, decidir con evidencia de uso si ZIP basta o se necesitan archivos individuales. Entregar PR y resultado de pruebas.
- **Joseph — dos reglas SAS:** identificar en `docs/sas-coverage.md` y el corpus dos brechas de alta prioridad no cubiertas; implementar las reglas en su área propietaria y añadir pruebas focalizadas. Entregar PR con archivo/línea de evidencia y limitaciones.
- **Byron — flujo web y validación:** ejecutar los tests web/E2E existentes, corregir fallos reproducibles solo en `apps/web/` y publicar un reporte de hasta tres planes revisados en Talend Studio (si está disponible). Si no hay Studio, dejar constancia y completar la prueba automatizada del flujo visible.

**Integración al cierre del sprint:** Andres revisa los tres resultados y ejecuta el conjunto de pruebas del proyecto. Joseph y Byron responden a observaciones en sus propias ramas. El sprint se considera cerrado cuando existen tres PRs revisables (o reportes de bloqueo con evidencia), pruebas ejecutadas por área y el flujo end-to-end está probado o su bloqueo está claramente identificado.
