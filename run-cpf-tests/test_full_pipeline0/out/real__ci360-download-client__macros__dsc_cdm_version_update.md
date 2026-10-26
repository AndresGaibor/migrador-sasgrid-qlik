# Job `job_dsc_cdm_version_update`

- **Programa SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas` (sha256 `0f80ab9167b7`)
- **Instrucciones:** 14 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.version_num` ← SAS `version_num` (&version_num en real/ci360-download-client/macros/dsc_cdm_version_update.sas:44)

## Conexiones a crear

- `DSCCNFG` (BASE, &UtilityLocation./data/dsccnfg) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

## Definición de macro auxiliar `%dsc_cdm_version_update`(version_num)

### 1. Leer &ver_hist_ds.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_cdm_version_update:s13` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:14`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_14_read_1_row_count`, `vc_m:dsc_cdm_version_update:op_14_read_1_schema`

### 2. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:dsc_cdm_version_update:s13` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:14`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:dsc_cdm_version_update:op_14_read_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = `? = max(ver_num)` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:14 · nombre oficial
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_14_aggregate_1_aggregates`, `vc_m:dsc_cdm_version_update:op_14_aggregate_1_numeric`

### 3. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:dsc_cdm_version_update:s13` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:14`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:dsc_cdm_version_update:op_14_aggregate_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=cdm_ver_num` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:14 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 4. Leer &table_nm.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_cdm_version_update:s29` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:29`
- **Conexiones:** OnSubjobOk desde `m:dsc_cdm_version_update:op_14_set_variable_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_29_read_1_row_count`, `vc_m:dsc_cdm_version_update:op_29_read_1_schema`

### 5. Escribir &table_nm._bkp

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:dsc_cdm_version_update:s29` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:29`
- **Conexiones:** Main desde `m:dsc_cdm_version_update:op_29_read_1`
- **Propiedades:**
  - `TABLE` = `_bkp` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:29
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:29
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:29
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_29_write_1_row_count`, `vc_m:dsc_cdm_version_update:op_29_write_1_schema`

### 6. Leer &table_nm.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_cdm_version_update:s32` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:32`
- **Conexiones:** OnSubjobOk desde `m:dsc_cdm_version_update:op_29_write_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_32_read_1_row_count`, `vc_m:dsc_cdm_version_update:op_32_read_1_schema`

### 7. Escribir &table_nm.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:dsc_cdm_version_update:s32` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:32`
- **Conexiones:** Main desde `m:dsc_cdm_version_update:op_32_read_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:32
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:32
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_32_write_1_row_count`, `vc_m:dsc_cdm_version_update:op_32_write_1_schema`

### 8. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:dsc_cdm_version_update:s44` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:44`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:dsc_cdm_version_update:op_32_write_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:44
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ver_num`, `ver_create_dttm` _(tipos por determinar)_
- **Expresión** (línea 47): SAS `&version_num.` → Java `context.version_num`
  - ⚠ Macrovariable &version_num → context.version_num (crear variable de contexto)
- **Expresión** (línea 48): SAS `datetime()` → _sin traducción automática_
  - ⚠ Sin traducción automática: función datetime
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_44_compute_1_nulls`, `vc_m:dsc_cdm_version_update:op_44_compute_1_dates`, `vc_m:dsc_cdm_version_update:op_44_compute_1_numeric`

### 9. Escribir cdm_version_hist

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:dsc_cdm_version_update:s44` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:44`
- **Conexiones:** Main desde `m:dsc_cdm_version_update:op_44_compute_1`
- **Propiedades:**
  - `TABLE` = `cdm_version_hist` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:44
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:44
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:44
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_44_write_1_row_count`, `vc_m:dsc_cdm_version_update:op_44_write_1_schema`

### 10. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:dsc_cdm_version_update:s51` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:51`
- **Conexiones:** OnSubjobOk desde `m:dsc_cdm_version_update:op_44_write_1`
- **Propiedades:**
  - `TABLE` = `cdm_version_hist` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:51
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:51
  - `TABLE_ACTION` = `NONE` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:51
- **Pendientes:**
  - Tabla base destino
  - Librería dsccnfg es de tipo BASE en &UtilityLocation./data/dsccnfg: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_51_append_1_row_count`

### 11. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:dsc_cdm_version_update:s57` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:57`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:dsc_cdm_version_update:op_51_append_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:57
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ver_num`, `ver_create_dttm` _(tipos por determinar)_
- **Expresión** (línea 60): SAS `&version_num.` → Java `context.version_num`
  - ⚠ Macrovariable &version_num → context.version_num (crear variable de contexto)
- **Expresión** (línea 61): SAS `datetime()` → _sin traducción automática_
  - ⚠ Sin traducción automática: función datetime
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_57_compute_1_nulls`, `vc_m:dsc_cdm_version_update:op_57_compute_1_dates`, `vc_m:dsc_cdm_version_update:op_57_compute_1_numeric`

### 12. Escribir cdm_version_hist

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:dsc_cdm_version_update:s57` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:57`
- **Conexiones:** Main desde `m:dsc_cdm_version_update:op_57_compute_1`
- **Propiedades:**
  - `TABLE` = `cdm_version_hist` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:57
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:57
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:57
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_57_write_1_row_count`, `vc_m:dsc_cdm_version_update:op_57_write_1_schema`

### 13. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:dsc_cdm_version_update:s64` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:64`
- **Conexiones:** OnSubjobOk desde `m:dsc_cdm_version_update:op_57_write_1`
- **Propiedades:**
  - `TABLE` = `cdm_version_hist` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:64
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:64
  - `TABLE_ACTION` = `NONE` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:64
- **Pendientes:**
  - Tabla base destino
  - Librería dsccnfg es de tipo BASE en &UtilityLocation./data/dsccnfg: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:dsc_cdm_version_update:op_64_append_1_row_count`

### 14. Invocar macro %exit

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:dsc_cdm_version_update:s68` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_cdm_version_update.sas:68`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:dsc_cdm_version_update:op_64_append_1`
- **Propiedades:**
  - `PROCESS` (Job) = `exit` — SAS real/ci360-download-client/macros/dsc_cdm_version_update.sas:68 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- dataset_dynamic &ver_hist_ds. (real/ci360-download-client/macros/dsc_cdm_version_update.sas:13) — nombre de dataset con macrovariables
- dataset_dynamic &table_nm. (real/ci360-download-client/macros/dsc_cdm_version_update.sas:29) — nombre de dataset con macrovariables
- dataset_dynamic &table_nm._bkp (real/ci360-download-client/macros/dsc_cdm_version_update.sas:29) — nombre de dataset con macrovariables
- dataset_dynamic &table_nm. (real/ci360-download-client/macros/dsc_cdm_version_update.sas:32) — nombre de dataset con macrovariables
- macro exit (real/ci360-download-client/macros/dsc_cdm_version_update.sas:68) — sin definición en el proyecto

## Casos de validación

- `vc_m:dsc_cdm_version_update:op_14_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_cdm_version_update:op_14_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_cdm_version_update:op_14_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:dsc_cdm_version_update:op_14_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:dsc_cdm_version_update:op_29_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_cdm_version_update:op_29_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_cdm_version_update:op_29_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:dsc_cdm_version_update:op_29_write_1_schema` (schema): Esquema destino
- `vc_m:dsc_cdm_version_update:op_32_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_cdm_version_update:op_32_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_cdm_version_update:op_32_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:dsc_cdm_version_update:op_32_write_1_schema` (schema): Esquema destino
- `vc_m:dsc_cdm_version_update:op_44_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:dsc_cdm_version_update:op_44_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:dsc_cdm_version_update:op_44_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:dsc_cdm_version_update:op_44_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:dsc_cdm_version_update:op_44_write_1_schema` (schema): Esquema destino
- `vc_m:dsc_cdm_version_update:op_51_append_1_row_count` (row_count): Filas añadidas
- `vc_m:dsc_cdm_version_update:op_57_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:dsc_cdm_version_update:op_57_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:dsc_cdm_version_update:op_57_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:dsc_cdm_version_update:op_57_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:dsc_cdm_version_update:op_57_write_1_schema` (schema): Esquema destino
- `vc_m:dsc_cdm_version_update:op_64_append_1_row_count` (row_count): Filas añadidas

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
