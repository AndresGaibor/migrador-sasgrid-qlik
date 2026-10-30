# Job `job_p0_clientes_activos`

- **Programa SAS:** `p0_clientes_activos.sas` (sha256 `21ee224bdf60`)
- **Instrucciones:** 5 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `dwh` (BASE, /data/dwh) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `stg` (BASE, /data/staging) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer dwh.clientes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`
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

### 2. Transformar en un solo tMap: Renombrar columnas; Filtrar filas (sentencia WHERE): estado = 'A' and saldo > 0; Calcular columnas (asignaciones y condicionales); Conservar/descartar columnas; Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s5` · **Confianza:** medium · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_5_read_1`
- **Propiedades:**
  - `Output filter` = `(("A".equals(input_row.estado) && (input_row.saldo > 0)))` — SAS fusionado
  - `Output columns` = `id → cliente_id` — SAS fusionado
- **Esquema:** `cliente_id`, `nombre`, `saldo`, `segmento`:String _(tipos por determinar)_
- **Expresión** (línea 7): SAS `estado = 'A' and saldo > 0` → Java `("A".equals(input_row.estado) && (input_row.saldo > 0))`
  - ⚠ Filtro de salida del tMap: tipo no confirmado: el tipo numérico se infiere del literal de la comparación; validar que la columna es numérica
  - ⚠ Filtro de salida del tMap: tipo no confirmado: se asumió texto; confirmar con el esquema real
- **Expresión** (línea 9): SAS `if saldo >= 100000 then segmento = 'ALTO' else if saldo >= 10000 then segmento = 'MEDIO' else segmento = 'BAJO'` → Java `((input_row.saldo >= 100000) ? "ALTO" : ((input_row.saldo >= 10000) ? "MEDIO" : "BAJO"))`
  - ⚠ tipo no confirmado: el tipo numérico se infiere del literal de la comparación; validar que la columna es numérica
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pruebas:** `vc_op_5_rename_1_schema`, `vc_op_7_filter_1_row_count`, `vc_op_7_filter_1_nulls`, `vc_op_7_filter_1_empty`, `vc_op_5_compute_1_nulls`, `vc_op_5_compute_1_dates`, `vc_op_5_compute_1_numeric`, `vc_op_5_select_columns_1_schema`, `vc_op_5_select_columns_2_schema`

### 3. Eliminar duplicados

- **Acción:** add_component · **Componente:** `tUniqRow` ![Icono Talend](/talend-icons/tUniqRow_icon32.png) (sin verificar)
- **Subjob:** `s15` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:15`
- **Conexiones:** Main desde `tmap_op_5_rename_1`
- **Propiedades:**
  - `UNIQUE_KEY` = `cliente_id` — SAS p0_clientes_activos.sas:15
- **Esquema:** `cliente_id` _(tipos por determinar)_
- **Supuestos:** PROC SORT NODUPKEY: tUniqRow conserva la primera fila de cada clave en el orden de entrada; SAS la conservaba en el orden ordenado. Validar si el resto de columnas difiere entre duplicados.
- **Pendientes:**
  - Confirmar la clave única (columnas del esquema) y que tUniqRow conserva la primera fila por clave.
- **Pruebas:** `vc_op_15_dedupe_1_duplicates`

### 4. Escribir stg.clientes_activos_ord

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`
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

### 6. Detiene el Job ante un error de componente

- **Acción:** add_component · **Componente:** `tDie` ![Icono Talend](/talend-icons/tDie_icon32.png) (sin verificar)
- **Subjob:** `recomendado` · **Confianza:** high · **Origen SAS:** `p0_clientes_activos.sas:5`
- **Conexiones:** OnComponentError desde `op_15_write_1`

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
