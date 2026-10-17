# Reglas de migración y contrato del plan

## Entidades

`Project`, `SourceFile`, `Program`, `Macro`, `Dataset`, `Operation`, `GridTask`, `Finding`, `MigrationPlan`, `ValidationCase`.

## Contrato de cada paso del plan

- Acción: qué hace el desarrollador en Talend Studio.
- Componente candidato: validado contra el catálogo si se pudo verificar; si no, `por_determinar`.
- Propiedades: nombre exacto, valor propuesto y origen.
- Esquema: columnas, tipos Talend, nulabilidad, longitud, precisión.
- Conexiones: componente anterior, tipo de conexión, orden.
- Expresiones: código/condición propuesta y referencia SAS (archivo:línea).
- Supuestos y pendientes.
- Pruebas de equivalencia.
- Estado: `propuesto` | `verificado` | `pendiente` | `validado_manualmente`.

## Orquestación vs. datos

Una dependencia de ejecución Grid (esperar otro job) NO se traduce a conexión de filas; se registra como dependencia de orquestación.

## Equivalencia

Comparar: conteo, esquema/tipos, missing/nulos, duplicados/claves, numéricos y fechas, orden (solo si es contrato), agregaciones/joins/filtros, datos vacíos o inválidos.

## Reglas versionadas

`rules/sas/`, `rules/talend/`, `rules/mappings/`. Cada reporte incluye versión de reglas y hashes de origen.
