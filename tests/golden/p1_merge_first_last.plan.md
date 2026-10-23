# Job `job_p1_merge_first_last`

- **Programa SAS:** `p1_merge_first_last.sas` (sha256 `e59f0d643755`)
- **Instrucciones:** 13 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Pasos

### 1. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s2` · **Confianza:** medium · **Origen SAS:** `p1_merge_first_last.sas:2`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = _por configurar_ — regla mappings · nombre oficial
  - `INTABLE` (Inline Table) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_2_format_definition_1_schema`

### 2. Leer work.pagos

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s6` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:6`
- **Conexiones:** OnSubjobOk desde `op_2_format_definition_1`
- **Propiedades:**
  - `TABLE` = `pagos` — SAS p1_merge_first_last.sas:6
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_6_read_1_row_count`, `vc_op_6_read_1_schema`

### 3. Ordenar por cliente_id, fecha_pago

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s6` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_6_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `cliente_id, fecha_pago` — SAS p1_merge_first_last.sas:6 · nombre oficial
- **Esquema:** `cliente_id`, `fecha_pago` _(tipos por determinar)_
- **Pruebas:** `vc_op_6_sort_1_ordering`

### 4. Escribir work.pagos

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s6` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:6`
- **Conexiones:** Main desde `op_6_sort_1`
- **Propiedades:**
  - `TABLE` = `pagos` — SAS p1_merge_first_last.sas:6
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p1_merge_first_last.sas:6
  - `DATA_ACTION` = `INSERT` — SAS p1_merge_first_last.sas:6
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_6_write_1_row_count`, `vc_op_6_write_1_schema`

### 5. Leer work.clientes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s7` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:7`
- **Conexiones:** OnSubjobOk desde `op_6_write_1`
- **Propiedades:**
  - `TABLE` = `clientes` — SAS p1_merge_first_last.sas:7
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_7_read_1_row_count`, `vc_op_7_read_1_schema`

### 6. Ordenar por cliente_id

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s7` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:7`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_7_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `cliente_id` — SAS p1_merge_first_last.sas:7 · nombre oficial
- **Esquema:** `cliente_id` _(tipos por determinar)_
- **Pruebas:** `vc_op_7_sort_1_ordering`

### 7. Escribir work.clientes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s7` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:7`
- **Conexiones:** Main desde `op_7_sort_1`
- **Propiedades:**
  - `TABLE` = `clientes` — SAS p1_merge_first_last.sas:7
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p1_merge_first_last.sas:7
  - `DATA_ACTION` = `INSERT` — SAS p1_merge_first_last.sas:7
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_7_write_1_row_count`, `vc_op_7_write_1_schema`

### 8. Leer work.clientes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s9` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:9`
- **Conexiones:** OnSubjobOk desde `op_7_write_1`
- **Propiedades:**
  - `TABLE` = `clientes` — SAS p1_merge_first_last.sas:9
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_7_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_9_read_1_row_count`, `vc_op_9_read_1_schema`

### 9. Leer work.pagos

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s9` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:9`
- **Propiedades:**
  - `TABLE` = `pagos` — SAS p1_merge_first_last.sas:9
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_6_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_9_read_2_row_count`, `vc_op_9_read_2_schema`

### 10. Unir (merge_by): work.clientes, work.pagos

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s9` · **Confianza:** medium · **Origen SAS:** `p1_merge_first_last.sas:9`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_9_read_1`, Lookup desde `op_9_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS p1_merge_first_last.sas:9
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `cliente_id` — SAS p1_merge_first_last.sas:9
- **Esquema:** `cliente_id` _(tipos por determinar)_
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_op_9_join_1_duplicates`, `vc_op_9_join_1_row_count`, `vc_op_9_join_1_nulls`

### 11. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s9` · **Confianza:** medium · **Origen SAS:** `p1_merge_first_last.sas:9`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_9_join_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 3 condicionales` — SAS p1_merge_first_last.sas:9
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `dias`, `mes_pago`, `tramo` _(tipos por determinar)_
- **Expresión** (línea 18): SAS `intck('day', fecha_pago, today())` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intck
- **Expresión** (línea 19): SAS `put(fecha_pago, yymmn6.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 20): SAS `put(edad, tramo.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 15): SAS `if first.cliente_id then acumulado = 0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 17): SAS `if missing(monto) then flag_sin_pago = 1` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 21): SAS `if last.cliente_id then output` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_9_compute_1_nulls`, `vc_op_9_compute_1_dates`, `vc_op_9_compute_1_numeric`

### 12. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s9` · **Confianza:** low · **Origen SAS:** `p1_merge_first_last.sas:9`
- **Conexiones:** Main desde `op_9_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_9_stateful_1_ordering`, `vc_op_9_stateful_1_duplicates`

### 13. Escribir work.pagos_cliente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s9` · **Confianza:** high · **Origen SAS:** `p1_merge_first_last.sas:9`
- **Conexiones:** Main desde `op_9_stateful_1`
- **Propiedades:**
  - `TABLE` = `pagos_cliente` — SAS p1_merge_first_last.sas:9
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p1_merge_first_last.sas:9
  - `DATA_ACTION` = `INSERT` — SAS p1_merge_first_last.sas:9
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_9_write_1_row_count`, `vc_op_9_write_1_schema`

## Casos de validación

- `vc_op_2_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_6_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_6_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_6_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_6_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_6_write_1_schema` (schema): Esquema destino
- `vc_op_7_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_7_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_7_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_7_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_7_write_1_schema` (schema): Esquema destino
- `vc_op_9_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_9_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_9_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_9_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_9_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_9_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_9_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_9_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_9_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_9_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_9_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_9_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_9_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_9_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
