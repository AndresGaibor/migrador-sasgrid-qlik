# Job `job_p0_ejemplo_basico`

- **Programa SAS:** `p0_ejemplo_basico.sas` (sha256 `26582c6a2355`)
- **Instrucciones:** 7 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `sashelp` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer sashelp.class

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s4` · **Confianza:** high · **Origen SAS:** `p0_ejemplo_basico.sas:4`
- **Propiedades:**
  - `TABLE` = `class` — SAS p0_ejemplo_basico.sas:4
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería sashelp es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_4_read_1_row_count`, `vc_op_4_read_1_schema`

### 2. Filtrar filas (IF subsetting): age >= 13

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s4` · **Confianza:** high · **Origen SAS:** `p0_ejemplo_basico.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_4_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS p0_ejemplo_basico.sas:6 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `age >= 13` — SAS p0_ejemplo_basico.sas:6 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS p0_ejemplo_basico.sas:6 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `age` _(tipos por determinar)_
- **Expresión** (línea 6): SAS `age >= 13` → Java `(input_row.age >= 13)`
- **Pruebas:** `vc_op_6_filter_1_row_count`, `vc_op_6_filter_1_nulls`, `vc_op_6_filter_1_empty`

### 3. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s4` · **Confianza:** high · **Origen SAS:** `p0_ejemplo_basico.sas:4`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_6_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS p0_ejemplo_basico.sas:4
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `height`, `estatura_cm` _(tipos por determinar)_
- **Expresión** (línea 7): SAS `height * 2.54` → Java `(input_row.height * 2.54)`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_4_compute_1_nulls`, `vc_op_4_compute_1_dates`, `vc_op_4_compute_1_numeric`

### 4. Escribir work.personas_filtradas

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s4` · **Confianza:** high · **Origen SAS:** `p0_ejemplo_basico.sas:4`
- **Conexiones:** Main desde `op_4_compute_1`
- **Propiedades:**
  - `TABLE` = `personas_filtradas` — SAS p0_ejemplo_basico.sas:4
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p0_ejemplo_basico.sas:4
  - `DATA_ACTION` = `INSERT` — SAS p0_ejemplo_basico.sas:4
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_4_write_1_row_count`, `vc_op_4_write_1_schema`

### 5. Leer work.personas_filtradas

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s10` · **Confianza:** high · **Origen SAS:** `p0_ejemplo_basico.sas:11`
- **Conexiones:** OnSubjobOk desde `op_4_write_1`
- **Propiedades:**
  - `TABLE` = `personas_filtradas` — SAS p0_ejemplo_basico.sas:11
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_4_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_11_read_1_row_count`, `vc_op_11_read_1_schema`

### 6. Agregar por sex

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s10` · **Confianza:** high · **Origen SAS:** `p0_ejemplo_basico.sas:11`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `op_11_read_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `sex` — SAS p0_ejemplo_basico.sas:11 · nombre oficial
  - `OPERATIONS` (Operations) = `personas = count(*); promedio_estatura_cm = avg(estatura_cm)` — SAS p0_ejemplo_basico.sas:11 · nombre oficial
- **Esquema:** `sex`, `personas`, `promedio_estatura_cm` _(tipos por determinar)_
- **Pruebas:** `vc_op_11_aggregate_1_aggregates`, `vc_op_11_aggregate_1_numeric`

### 7. Escribir work.resumen (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s10` · **Confianza:** high · **Origen SAS:** `p0_ejemplo_basico.sas:11`
- **Conexiones:** Main desde `op_11_aggregate_1`
- **Propiedades:**
  - `TABLE` = `resumen` — SAS p0_ejemplo_basico.sas:11
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p0_ejemplo_basico.sas:11
  - `DATA_ACTION` = `INSERT` — SAS p0_ejemplo_basico.sas:11
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_11_write_1_row_count`, `vc_op_11_write_1_schema`

## Casos de validación

- `vc_op_4_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_4_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_6_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_6_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_4_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_4_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_4_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_4_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_4_write_1_schema` (schema): Esquema destino
- `vc_op_11_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_11_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_11_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_11_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_11_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_11_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
