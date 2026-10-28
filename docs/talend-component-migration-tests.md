# Pruebas de migración por componente Talend

La matriz mantenida en
[`tests/fixtures/sas/synthetic/migration_matrix/component-test-cases.json`](../tests/fixtures/sas/synthetic/migration_matrix/component-test-cases.json)
enumera todos los componentes del alcance actual y apunta a uno o más programas SAS de prueba.
El alcance canónico está en
[`rules/talend/migration-candidate-scope.json`](../rules/talend/migration-candidate-scope.json):
33 componentes base y 9 alternativas. No es el catálogo completo de los 870 componentes de Studio;
muchos no tienen correspondencia SAS razonable. Componentes fuera de ese alcance no se presentan
como migrables.

## Qué cubre la suite

| Familia | Componentes/casos |
| --- | --- |
| Entradas/salidas de archivos | `tFileInputDelimited`, `tFileInputPositional`, `tFileInputExcel`, `tFileOutputDelimited`, `tFileOutputPositional`, `tFileOutputExcel` |
| Transformación y flujo | `tMap`, `tFilterRow`, `tFilterColumns`, `tJoin`, `tUnite`, `tAggregateRow`, `tSortRow`, `tFixedFlowInput`, `tLogRow` |
| Orquestación/estado | `tRunJob`, `tSystem`, `tSetGlobalVar`, `tFlowToIterate`, `tJava`, `tJavaRow` |
| Bases de datos | `tDBInput`, `tDBOutput`, `tDBRow`, y entrada/salida de DB2, Greenplum, SQL Server, MySQL, Netezza, Oracle, PostgreSQL, Redshift y Teradata |

`tests/unit/test_component_migration_coverage.py` recorre cada caso por la frontera pública
parser → IR → plan. Para componentes base exige que el planner emita ese candidato; para alternativas
exige que aparezcan en el paso correspondiente. Además, verifica cada operación declarada en las
reglas, sus casos de validación, y que operaciones SAS sin traducción permanezcan pendientes. Los
`%include` se comprueban en el IR y no se presentan como Jobs hijos listos: su resolución depende de
la expansión de macros y del proyecto importado. También verifica que el manifiesto no omita ni
agregue nombres respecto del alcance versionado.

## Casos detallados de tMap

La matriz contiene fixtures separados para:

- cálculos aritméticos y preservación del nombre de salida;
- filtrado y alternativa de filtro avanzado;
- joins SQL con conexiones `Main` y `Lookup` y esquema de salida;
- CASE/ruteo de filas y salidas múltiples;
- limpieza de texto, conversiones y funciones no traducidas;
- conversiones de fechas y missing;
- ordenación por varias claves y dirección `DESCENDING` sin contaminar el schema ni la clave de
  `NODUPKEY`;
- normalización de listas y selección de columnas;
- estado entre filas (`RETAIN`/`FIRST.`/`LAST.`), que debe quedar pendiente si no es seguro.

La prueba exige que una expresión no traducida permanezca explícitamente sin traducción y con
advertencias/revisión semántica; no acepta una expresión inventada como si fuera equivalente.
Los casos no demuestran ejecución ni equivalencia: eso requiere datos congelados y ejecución
controlada de SAS y Talend fuera de la suite offline.

La suite también cubre AND/OR y `missing()` en filtros; múltiples claves ASC/DESC y `NODUP` frente
a `NODUPKEY`; `UNION` frente a `UNION ALL`; `PROC APPEND FORCE`; joins inner/left/full y `MERGE`;
agregaciones de SQL frente a `PROC MEANS`/`PROC FREQ`; y el límite final de `build_apply_spec`, que
debe dejar como borrador los componentes con semántica sin confirmar.

## Casos de integridad de Studio y proyecto

- **Conectores**: `mcp/talend-mcp/tests/talend/component-definitions.test.ts` construye definiciones
  XML sintéticas y prueba `MIN_INPUT` sin `MAX_INPUT` en `tUnite`, además de entradas/salidas
  incompatibles. El parser XML comprueba que los límites no se confundan con cero.
- **Nombres de Jobs**: `tests/unit/test_unique_job_names.py` cubre basenames repetidos como
  `bulkload.sas`, jerarquía de carpetas, colisiones con nombres ya ocupados, rutas Windows y rutas
  idénticas. `tests/integration/test_project_job_name_collisions.py` verifica además que el flujo
  de generación de planes del proyecto aplique esa unicidad.

## Ejecutar antes de integrar

```bash
uv run pytest tests/unit/test_component_migration_coverage.py tests/unit/test_unique_job_names.py tests/unit/test_project_job_name_collisions.py tests/unit/test_planner.py -q
cd mcp/talend-mcp && bun test tests/talend/component-definitions.test.ts
```

Estas comprobaciones son offline: no requieren credenciales, conexiones a bases de datos, SAS Grid
ni una escritura a Talend Studio.
