# Job `job_dsc_create_attrib`

- **Programa SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas` (sha256 `12debc94f783`)
- **Instrucciones:** 30 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.schemaUrl` ← SAS `schemaUrl` (&schemaUrl en real/ci360-download-client/macros/dsc_create_attrib.sas:19)
- `context.Tbl` ← SAS `Tbl` (&Tbl en real/ci360-download-client/macros/dsc_create_attrib.sas:56)
- `context.TblNum` ← SAS `TblNum` (&TblNum en real/ci360-download-client/macros/dsc_create_attrib.sas:56)

## Pasos

## Definición de macro auxiliar `%dsc_create_attrib`(schemaName, schemaVersion, schemaUrl)

### 1. Invocar macro %dsc_get_schema

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:dsc_create_attrib:s19` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:19`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `dsc_get_schema` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:19 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `schemaUrl=&schemaUrl` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:19 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Leer schema_details

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s26` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:26`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_19_macro_call_1`
- **Propiedades:**
  - `TABLE` = `schema_details` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:26
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_26_read_1_row_count`, `vc_m:dsc_create_attrib:op_26_read_1_schema`

### 3. Ordenar por table_name, column_sequence

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:dsc_create_attrib:s26` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:26`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_26_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `table_name, column_sequence` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:26 · nombre oficial
- **Esquema:** `table_name`, `column_sequence` _(tipos por determinar)_
- **Pruebas:** `vc_m:dsc_create_attrib:op_26_sort_1_ordering`

### 4. Escribir schema_details

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:dsc_create_attrib:s26` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:26`
- **Conexiones:** Main desde `m:dsc_create_attrib:op_26_sort_1`
- **Propiedades:**
  - `TABLE` = `schema_details` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:26
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:26
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:26
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:dsc_create_attrib:op_26_write_1_row_count`, `vc_m:dsc_create_attrib:op_26_write_1_schema`

### 5. Leer schema_details

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s28` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:29`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_26_write_1`
- **Propiedades:**
  - `TABLE` = `schema_details` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:29
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_29_read_1_row_count`, `vc_m:dsc_create_attrib:op_29_read_1_schema`

### 6. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:dsc_create_attrib:s28` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:29`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_29_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `distinct table_name` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:29
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 29): SAS `distinct table_name` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pruebas:** `vc_m:dsc_create_attrib:op_29_project_1_schema`

### 7. Escribir schema_Table_names (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:dsc_create_attrib:s28` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:29`
- **Conexiones:** Main desde `m:dsc_create_attrib:op_29_project_1`
- **Propiedades:**
  - `TABLE` = `schema_table_names` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:29
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:29
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:29
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:dsc_create_attrib:op_29_write_1_row_count`, `vc_m:dsc_create_attrib:op_29_write_1_schema`

### 8. Leer schema_Table_names

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s37` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:37`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_29_write_1`
- **Propiedades:**
  - `TABLE` = `schema_table_names` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:37
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_37_read_1_row_count`, `vc_m:dsc_create_attrib:op_37_read_1_schema`

### 9. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `m:dsc_create_attrib:s37` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:37`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `m:dsc_create_attrib:op_37_read_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_m:dsc_create_attrib:op_37_write_file_1_row_count`

### 10. Leer schema_details

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s43` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:44`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_37_write_file_1`
- **Propiedades:**
  - `TABLE` = `schema_details` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:44
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_44_read_1_row_count`, `vc_m:dsc_create_attrib:op_44_read_1_schema`

### 11. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:dsc_create_attrib:s43` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:44`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_44_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `distinct table_name` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:44
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 44): SAS `distinct table_name` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pruebas:** `vc_m:dsc_create_attrib:op_44_project_1_schema`

### 12. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:dsc_create_attrib:s43` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:44`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_44_project_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=Table_List separated by '` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:44 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 13. Leer schema_Table_names

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s56` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:56`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_44_set_variable_1`
- **Propiedades:**
  - `TABLE` = `schema_table_names` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:56
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_56_read_1_row_count`, `vc_m:dsc_create_attrib:op_56_read_1_schema`

### 14. Filtrar filas (opción where= del dataset): table_name="&&Tbl&TblNum"

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:dsc_create_attrib:s56` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:56`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_56_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:56 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `table_name == "&&Tbl&TblNum"` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:56 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:56 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `table_name` _(tipos por determinar)_
- **Expresión** (línea 56): SAS `table_name="&&Tbl&TblNum"` → Java `input_row.table_name.equals("&&Tbl&TblNum")`
- **Pruebas:** `vc_m:dsc_create_attrib:op_56_filter_1_row_count`, `vc_m:dsc_create_attrib:op_56_filter_1_nulls`, `vc_m:dsc_create_attrib:op_56_filter_1_empty`

### 15. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:dsc_create_attrib:s56` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:56`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_56_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 0 condicionales` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:56
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ident0`, `martNm`, `verNo` _(tipos por determinar)_
- **Expresión** (línea 58): SAS `4` → Java `4`
- **Expresión** (línea 59): SAS `symget('schemaName')` → _sin traducción automática_
  - ⚠ Sin traducción automática: función symget
- **Expresión** (línea 60): SAS `symget('schemaVersion')` → _sin traducción automática_
  - ⚠ Sin traducción automática: función symget
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:dsc_create_attrib:op_56_compute_1_nulls`, `vc_m:dsc_create_attrib:op_56_compute_1_dates`, `vc_m:dsc_create_attrib:op_56_compute_1_numeric`

### 16. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `m:dsc_create_attrib:s56` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:56`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `m:dsc_create_attrib:op_56_compute_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_m:dsc_create_attrib:op_56_write_file_1_row_count`

### 17. Leer schema_details

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s75` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:75`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_56_write_file_1`
- **Propiedades:**
  - `TABLE` = `schema_details` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:75
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_75_read_1_row_count`, `vc_m:dsc_create_attrib:op_75_read_1_schema`

### 18. Filtrar filas (opción where= del dataset): table_name="&&Tbl&TblNum"

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:dsc_create_attrib:s75` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:75`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_75_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:75 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `table_name == "&&Tbl&TblNum"` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:75 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:75 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `table_name` _(tipos por determinar)_
- **Expresión** (línea 75): SAS `table_name="&&Tbl&TblNum"` → Java `input_row.table_name.equals("&&Tbl&TblNum")`
- **Pruebas:** `vc_m:dsc_create_attrib:op_75_filter_1_row_count`, `vc_m:dsc_create_attrib:op_75_filter_1_nulls`, `vc_m:dsc_create_attrib:op_75_filter_1_empty`

### 19. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:dsc_create_attrib:s75` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:75`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_75_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `5 asignaciones, 10 condicionales` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:75
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `default_datatype`, `map_datatype_default`, `ident1`, `ident2`, `numFormat` _(tipos por determinar)_
- **Expresión** (línea 77): SAS `'FORMAT=$4000.'` → Java `"FORMAT=$4000."`
- **Expresión** (línea 78): SAS `'FORMAT=$4000.'` → Java `"FORMAT=$4000."`
- **Expresión** (línea 79): SAS `8` → Java `8`
- **Expresión** (línea 80): SAS `12` → Java `12`
- **Expresión** (línea 97): SAS `'NLNUM' || compress(tranwrd(column_type,',','.'),'.','kd')` → _sin traducción automática_
  - ⚠ Sin traducción automática: función compress
- **Expresión** (línea 82): SAS `if _n_ = 1 then  put @ident1 'attrib '` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 85): SAS `if( data_type= 'varchar' or data_type= 'char' )then 
                put @ident2 column_name 'FORMAT=$' data_length +(-1) '.'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 88): SAS `else if data_type='timestamp' then
                put @ident2 column_name 'LENGTH=8 FORMAT=DATETIME27.6 INFORMAT=ymddttm.'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 91): SAS `else if data_type='date' then
    			put @ident2 column_name 'LENGTH=8 FORMAT=DATE10. INFORMAT=yymmdd.'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 94): SAS `else if (data_type='smallint' or data_type='tinyint' or data_type='int' or data_type='bigint' or data_type='decimal') then
			do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 102): SAS `if index(numFormat,'.')  > 0 then put @ident2 column_name 'LENGTH=8.'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 103): SAS `else put @ident2 column_name 'LENGTH=8.'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 107): SAS `else if( data_type = 'map' ) then
                put @ident2 column_name map_datatype_default` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 109): SAS `else
                put @ident2 column_name default_datatype` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 112): SAS `if eof then put @ident2 ';'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:dsc_create_attrib:op_75_compute_1_nulls`, `vc_m:dsc_create_attrib:op_75_compute_1_dates`, `vc_m:dsc_create_attrib:op_75_compute_1_numeric`

### 20. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `m:dsc_create_attrib:s75` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:75`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `m:dsc_create_attrib:op_75_compute_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_m:dsc_create_attrib:op_75_write_file_1_row_count`

### 21. Leer schema_details

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s116` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:116`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_75_write_file_1`
- **Propiedades:**
  - `TABLE` = `schema_details` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:116
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_116_read_1_row_count`, `vc_m:dsc_create_attrib:op_116_read_1_schema`

### 22. Filtrar filas (opción where= del dataset): table_name="&&Tbl&TblNum"

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:dsc_create_attrib:s116` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:116`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_116_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:116 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `table_name == "&&Tbl&TblNum"` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:116 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:116 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `table_name` _(tipos por determinar)_
- **Expresión** (línea 116): SAS `table_name="&&Tbl&TblNum"` → Java `input_row.table_name.equals("&&Tbl&TblNum")`
- **Pruebas:** `vc_m:dsc_create_attrib:op_116_filter_1_row_count`, `vc_m:dsc_create_attrib:op_116_filter_1_nulls`, `vc_m:dsc_create_attrib:op_116_filter_1_empty`

### 23. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:dsc_create_attrib:s116` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:116`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_116_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 2 condicionales` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:116
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ident1`, `ident2` _(tipos por determinar)_
- **Expresión** (línea 118): SAS `8` → Java `8`
- **Expresión** (línea 119): SAS `12` → Java `12`
- **Expresión** (línea 121): SAS `if _n_ = 1 then  put @ident1 'input '` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 125): SAS `if eof then put @ident2 ';'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:dsc_create_attrib:op_116_compute_1_nulls`, `vc_m:dsc_create_attrib:op_116_compute_1_dates`, `vc_m:dsc_create_attrib:op_116_compute_1_numeric`

### 24. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `m:dsc_create_attrib:s116` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:116`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `m:dsc_create_attrib:op_116_compute_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_m:dsc_create_attrib:op_116_write_file_1_row_count`

### 25. Leer schema_Table_names

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_create_attrib:s129` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:129`
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_116_write_file_1`
- **Propiedades:**
  - `TABLE` = `schema_table_names` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:129
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_create_attrib:op_129_read_1_row_count`, `vc_m:dsc_create_attrib:op_129_read_1_schema`

### 26. Filtrar filas (opción where= del dataset): table_name="&&Tbl&TblNum"

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:dsc_create_attrib:s129` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:129`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_129_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:129 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `table_name == "&&Tbl&TblNum"` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:129 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:129 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `table_name` _(tipos por determinar)_
- **Expresión** (línea 129): SAS `table_name="&&Tbl&TblNum"` → Java `input_row.table_name.equals("&&Tbl&TblNum")`
- **Pruebas:** `vc_m:dsc_create_attrib:op_129_filter_1_row_count`, `vc_m:dsc_create_attrib:op_129_filter_1_nulls`, `vc_m:dsc_create_attrib:op_129_filter_1_empty`

### 27. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:dsc_create_attrib:s129` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:129`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_create_attrib:op_129_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:129
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ident0` _(tipos por determinar)_
- **Expresión** (línea 131): SAS `4` → Java `4`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:dsc_create_attrib:op_129_compute_1_nulls`, `vc_m:dsc_create_attrib:op_129_compute_1_dates`, `vc_m:dsc_create_attrib:op_129_compute_1_numeric`

### 28. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `m:dsc_create_attrib:s129` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:129`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `m:dsc_create_attrib:op_129_compute_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_m:dsc_create_attrib:op_129_write_file_1_row_count`

### 29. Invocar macro %dsc_schema_sync

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:dsc_create_attrib:s143` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:143`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_129_write_file_1`
- **Propiedades:**
  - `PROCESS` (Job) = `dsc_schema_sync` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:143 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 30. Invocar macro %exit

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:dsc_create_attrib:s145` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_create_attrib.sas:145`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:dsc_create_attrib:op_143_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `exit` — SAS real/ci360-download-client/macros/dsc_create_attrib.sas:145 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro dsc_get_schema (real/ci360-download-client/macros/dsc_create_attrib.sas:19) — sin definición en el proyecto
- macro dsc_schema_sync (real/ci360-download-client/macros/dsc_create_attrib.sas:143) — sin definición en el proyecto
- macro exit (real/ci360-download-client/macros/dsc_create_attrib.sas:145) — sin definición en el proyecto

## Casos de validación

- `vc_m:dsc_create_attrib:op_26_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_26_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_26_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:dsc_create_attrib:op_26_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:dsc_create_attrib:op_26_write_1_schema` (schema): Esquema destino
- `vc_m:dsc_create_attrib:op_29_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_29_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_29_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:dsc_create_attrib:op_29_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:dsc_create_attrib:op_29_write_1_schema` (schema): Esquema destino
- `vc_m:dsc_create_attrib:op_37_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_37_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_37_write_file_1_row_count` (row_count): Mismas filas
- `vc_m:dsc_create_attrib:op_44_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_44_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_44_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:dsc_create_attrib:op_56_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_56_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_56_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:dsc_create_attrib:op_56_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:dsc_create_attrib:op_56_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:dsc_create_attrib:op_56_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:dsc_create_attrib:op_56_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:dsc_create_attrib:op_56_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:dsc_create_attrib:op_56_write_file_1_row_count` (row_count): Mismas filas
- `vc_m:dsc_create_attrib:op_75_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_75_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_75_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:dsc_create_attrib:op_75_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:dsc_create_attrib:op_75_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:dsc_create_attrib:op_75_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:dsc_create_attrib:op_75_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:dsc_create_attrib:op_75_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:dsc_create_attrib:op_75_write_file_1_row_count` (row_count): Mismas filas
- `vc_m:dsc_create_attrib:op_116_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_116_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_116_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:dsc_create_attrib:op_116_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:dsc_create_attrib:op_116_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:dsc_create_attrib:op_116_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:dsc_create_attrib:op_116_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:dsc_create_attrib:op_116_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:dsc_create_attrib:op_116_write_file_1_row_count` (row_count): Mismas filas
- `vc_m:dsc_create_attrib:op_129_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_create_attrib:op_129_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_create_attrib:op_129_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:dsc_create_attrib:op_129_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:dsc_create_attrib:op_129_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:dsc_create_attrib:op_129_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:dsc_create_attrib:op_129_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:dsc_create_attrib:op_129_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:dsc_create_attrib:op_129_write_file_1_row_count` (row_count): Mismas filas

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
