# Job `job_p0_clientes_activos`

- **Programa SAS:** `p0_clientes_activos.sas` (sha256 `21ee224bdf60`)
- **Instrucciones:** 11 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `dwh` (BASE, /data/dwh) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `stg` (BASE, /data/staging) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer dwh.clientes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Propiedades:**
  - `TABLE` = `clientes` — SAS p0_clientes_activos.sas:5
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dwh es de tipo BASE en /data/dwh: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_5_read_1_row_count`, `vc_op_5_read_1_schema`

### 2. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_5_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `id → cliente_id` — SAS p0_clientes_activos.sas:5
- **Esquema:** `cliente_id` _(tipos por determinar)_
- **Pruebas:** `vc_op_5_rename_1_schema`

### 3. Filtrar filas (sentencia WHERE): estado = 'A' and saldo > 0

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:7`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_5_rename_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `AND` — SAS p0_clientes_activos.sas:7 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `estado == 'A'; saldo > 0` — SAS p0_clientes_activos.sas:7 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS p0_clientes_activos.sas:7 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `estado`, `saldo` _(tipos por determinar)_
- **Expresión** (línea 7): SAS `estado = 'A' and saldo > 0` → _sin traducción automática_
  - ⚠ Comparación con columna sin tipo conocido: validar conversión, orden y semántica de missing/nulos
- **Pruebas:** `vc_op_7_filter_1_row_count`, `vc_op_7_filter_1_nulls`, `vc_op_7_filter_1_empty`

### 4. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s5` · **Confianza:** medium · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_7_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 3 condicionales` — SAS p0_clientes_activos.sas:5
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 9): SAS `if saldo >= 100000 then segmento = 'ALTO'` → _sin traducción automática_
  - ⚠ Condicional IF/THEN sin traducción automática de la condición o los valores
- **Expresión** (línea 10): SAS `else if saldo >= 10000 then segmento = 'MEDIO'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE sin traducción automática
- **Expresión** (línea 11): SAS `else segmento = 'BAJO'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE sin traducción automática
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Condicional IF/ELSE sin traducción automática: revisar a mano
- **Pruebas:** `vc_op_5_compute_1_nulls`, `vc_op_5_compute_1_dates`, `vc_op_5_compute_1_numeric`

### 5. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_5_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: estado` — SAS p0_clientes_activos.sas:5 · nombre oficial
- **Pruebas:** `vc_op_5_select_columns_1_schema`

### 6. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_5_select_columns_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: cliente_id, nombre, saldo, segmento` — SAS p0_clientes_activos.sas:5 · nombre oficial
- **Esquema:** `cliente_id`, `nombre`, `saldo`, `segmento` _(tipos por determinar)_
- **Pruebas:** `vc_op_5_select_columns_2_schema`

### 7. Escribir stg.clientes_activos

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Conexiones:** Main desde `op_5_select_columns_2`
- **Propiedades:**
  - `TABLE` = `clientes_activos` — SAS p0_clientes_activos.sas:5
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p0_clientes_activos.sas:5
  - `DATA_ACTION` = `INSERT` — SAS p0_clientes_activos.sas:5
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería stg es de tipo BASE en /data/staging: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_5_write_1_row_count`, `vc_op_5_write_1_schema`

### 8. Leer stg.clientes_activos

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s15` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:15`
- **Conexiones:** OnSubjobOk desde `op_5_write_1`
- **Propiedades:**
  - `TABLE` = `clientes_activos` — SAS p0_clientes_activos.sas:15
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset producido antes en este programa (op_5_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg es de tipo BASE en /data/staging: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_15_read_1_row_count`, `vc_op_15_read_1_schema`

### 9. Ordenar por cliente_id

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s15` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:15`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_15_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `cliente_id ASC` — SAS p0_clientes_activos.sas:15 · nombre oficial
- **Esquema:** `cliente_id` _(tipos por determinar)_
- **Pruebas:** `vc_op_15_sort_1_ordering`

### 10. Eliminar duplicados

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s15` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:15`
- **Conexiones:** Main desde `op_15_sort_1`
- **Propiedades:**
  - `UNIQUE_KEY` = `cliente_id` — SAS p0_clientes_activos.sas:15
- **Esquema:** `cliente_id` _(tipos por determinar)_
- **Pendientes:**
  - Definir la clave y la lógica para conservar la fila correcta por grupo; confirmar una opción disponible en la instalación actual.
- **Pruebas:** `vc_op_15_dedupe_1_duplicates`

### 11. Escribir stg.clientes_activos_ord

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s15` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:15`
- **Conexiones:** Main desde `op_15_dedupe_1`
- **Propiedades:**
  - `TABLE` = `clientes_activos_ord` — SAS p0_clientes_activos.sas:15
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p0_clientes_activos.sas:15
  - `DATA_ACTION` = `INSERT` — SAS p0_clientes_activos.sas:15
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería stg es de tipo BASE en /data/staging: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_15_write_1_row_count`, `vc_op_15_write_1_schema`

## Casos de validación

- `vc_op_5_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_5_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_5_rename_1_schema` (schema): Nombres de columna finales
- `vc_op_7_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_7_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_7_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_5_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_5_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_5_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_5_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_5_select_columns_2_schema` (schema): Solo las columnas esperadas
- `vc_op_5_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_5_write_1_schema` (schema): Esquema destino
- `vc_op_15_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_15_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_15_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_15_dedupe_1_duplicates` (duplicates): Se conserva la misma fila por clave (NODUPKEY conserva la primera)
- `vc_op_15_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_15_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
