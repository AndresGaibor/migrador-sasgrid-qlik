# Job `job_p0_resumen_sql`

- **Programa SAS:** `p0_resumen_sql.sas` (sha256 `fb6d9d23beef`)
- **Instrucciones:** 9 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.anio` ← SAS `anio` = `2025` (%LET de primer nivel)

## Conexiones a crear

- `dwh` (BASE, /data/dwh) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer dwh.ventas

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
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

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
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

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Propiedades:**
  - `TABLE` = `productos` — SAS p0_resumen_sql.sas:6
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dwh es de tipo BASE en /data/dwh: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_6_read_3_row_count`, `vc_op_6_read_3_schema`

### 4. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s5` · **Confianza:** low · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Conexiones:** Main desde `op_6_read_1`
- **Supuestos:** SQL con JOIN encadenados: diseñar manualmente la topología de entradas y claves
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 5. Filtrar filas (WHERE): year(v.fecha) = &anio.

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_6_unsupported_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS p0_resumen_sql.sas:6 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `((input_row.fecha == null ? null : TalendDate.getPartOfDate("YEAR", input_row.fecha)) == context.anio)` — SAS p0_resumen_sql.sas:6 · nombre oficial
- **Esquema:** `fecha` _(tipos por determinar)_
- **Expresión** (línea 6): SAS `year(v.fecha) = &anio.` → Java `((input_row.fecha == null ? null : TalendDate.getPartOfDate("YEAR", input_row.fecha)) == context.anio)`
  - ⚠ Macrovariable &anio → context.anio (crear variable de contexto)
  - ⚠ year/month/day(): sobre un Date de Talend; con fecha SAS numérica validar la conversión de época
- **Pruebas:** `vc_op_6_filter_1_row_count`, `vc_op_6_filter_1_nulls`, `vc_op_6_filter_1_empty`

### 6. Agregar por c.region, p.categoria

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `op_6_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `region, categoria` — SAS p0_resumen_sql.sas:6 · nombre oficial
  - `OPERATIONS` (Operations) = `total_monto = sum(monto); clientes = count(cliente_id)` — SAS p0_resumen_sql.sas:6 · nombre oficial
- **Esquema:** `region`, `categoria`, `total_monto`, `clientes` _(tipos por determinar)_
- **Pruebas:** `vc_op_6_aggregate_1_aggregates`, `vc_op_6_aggregate_1_numeric`

### 7. Filtrar filas (HAVING): calculated total_monto > 1000

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
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

### 8. Escribir work.ventas_resumen (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Conexiones:** Main desde `op_6_filter_2`
- **Propiedades:**
  - `TABLE` = `ventas_resumen` — SAS p0_resumen_sql.sas:6
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p0_resumen_sql.sas:6
  - `DATA_ACTION` = `INSERT` — SAS p0_resumen_sql.sas:6
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
- **Pruebas:** `vc_op_6_write_1_row_count`, `vc_op_6_write_1_schema`

### 10. Detiene el Job ante un error de componente

- **Acción:** add_component · **Componente:** `tDie` ![Icono Talend](/talend-icons/tDie_icon32.png) (sin verificar)
- **Subjob:** `recomendado` · **Confianza:** high · **Origen SAS:** `p0_resumen_sql.sas:6`
- **Conexiones:** OnComponentError desde `op_6_write_1`

## Casos de validación

- `vc_op_6_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_6_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_6_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_read_3_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_6_read_3_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_6_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_6_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_6_filter_2_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_6_filter_2_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_6_filter_2_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_6_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_6_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
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
