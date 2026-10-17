# Job `job_p0_resumen_sql`

- **Programa SAS:** `p0_resumen_sql.sas` (sha256 `45215ef70662`)
- **Estado:** needs_review · **Pasos:** 9 · **Reglas:** v1
- **Aviso:** los nombres de componente y propiedad provienen del catálogo oficial de Talend; solo los marcados «verificado» se contrastaron con un Job real vía talend-mcp.

## Variables de contexto

- `context.anio` ← SAS `anio` = `2025` (%LET de primer nivel)

## Conexiones a crear

- `dwh` (BASE, /data/dwh) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer dwh.ventas

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Propiedades:**
  - `TABLE` = `ventas` — SAS p0_resumen_sql.sas:6
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dwh es de tipo BASE en /data/dwh: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_6_read_1_row_count`, `vc_op_6_read_1_schema`

### 2. Leer dwh.clientes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Propiedades:**
  - `TABLE` = `clientes` — SAS p0_resumen_sql.sas:6
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dwh es de tipo BASE en /data/dwh: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_6_read_2_row_count`, `vc_op_6_read_2_schema`

### 3. Leer dwh.productos

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Propiedades:**
  - `TABLE` = `productos` — SAS p0_resumen_sql.sas:6
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dwh es de tipo BASE en /data/dwh: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_6_read_3_row_count`, `vc_op_6_read_3_schema`

### 4. Unir (inner join): dwh.ventas, dwh.clientes, dwh.productos

- **Acción:** add_component · **Componente:** `tMap` (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap)
- **Conexiones:** Main desde `op_6_read_1`, Lookup desde `op_6_read_2`, Lookup desde `op_6_read_3`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Inner Join` — SAS p0_resumen_sql.sas:6
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `v.cliente_id = c.id` — SAS p0_resumen_sql.sas:6
- **Esquema:** `cliente_id`, `id` _(tipos por determinar)_
- **Expresión** (línea 6): SAS `on v.cliente_id = c.id` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_op_6_join_1_duplicates`, `vc_op_6_join_1_row_count`, `vc_op_6_join_1_nulls`

### 5. Unir (left join): dwh.ventas, dwh.clientes, dwh.productos

- **Acción:** add_component · **Componente:** `tMap` (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap)
- **Conexiones:** Main desde `op_6_join_1`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS p0_resumen_sql.sas:6
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `v.producto_id = p.id` — SAS p0_resumen_sql.sas:6
- **Esquema:** `producto_id`, `id` _(tipos por determinar)_
- **Expresión** (línea 6): SAS `on v.producto_id = p.id` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_op_6_join_2_duplicates`, `vc_op_6_join_2_row_count`, `vc_op_6_join_2_nulls`

### 6. Filtrar filas (WHERE): year(v.fecha) = &anio.

- **Acción:** add_component · **Componente:** `tFilterRow` (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfilterrow)
- **Conexiones:** Main desde `op_6_join_2`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 6): SAS `year(v.fecha) = &anio.` → _sin traducción automática_
  - ⚠ Sin traducción automática: función year
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_op_6_filter_1_row_count`, `vc_op_6_filter_1_nulls`, `vc_op_6_filter_1_empty`

### 7. Agregar por c.region, p.categoria

- **Acción:** add_component · **Componente:** `tAggregateRow` (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Estado:** propuesto · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/taggregaterow)
- **Conexiones:** Main desde `op_6_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `region, categoria` — SAS p0_resumen_sql.sas:6 · nombre oficial
  - `OPERATIONS` (Operations) = `total_monto = sum(monto); clientes = count(cliente_id)` — SAS p0_resumen_sql.sas:6 · nombre oficial
- **Esquema:** `region`, `categoria`, `total_monto`, `clientes` _(tipos por determinar)_
- **Pruebas:** `vc_op_6_aggregate_1_aggregates`, `vc_op_6_aggregate_1_numeric`

### 8. Filtrar filas (HAVING): calculated total_monto > 1000

- **Acción:** add_component · **Componente:** `tFilterRow` (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfilterrow)
- **Conexiones:** Main desde `op_6_aggregate_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 6): SAS `calculated total_monto > 1000` → _sin traducción automática_
  - ⚠ Construcción SAS sin traducción automática
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_op_6_filter_2_row_count`, `vc_op_6_filter_2_nulls`, `vc_op_6_filter_2_empty`

### 9. Escribir work.ventas_resumen (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Conexiones:** Main desde `op_6_filter_2`
- **Propiedades:**
  - `TABLE` = `ventas_resumen` — SAS p0_resumen_sql.sas:6
  - `ACTION_ON_TABLE` = _por configurar_ — regla mappings
  - `ACTION_ON_DATA` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
- **Pruebas:** `vc_op_6_write_1_row_count`, `vc_op_6_write_1_schema`

## Casos de validación

- `vc_op_6_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_6_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_6_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_read_3_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_6_read_3_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_6_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_6_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_6_join_2_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_6_join_2_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_6_join_2_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_6_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_6_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_6_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_6_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_6_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_6_filter_2_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_6_filter_2_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_6_filter_2_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_6_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_6_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
