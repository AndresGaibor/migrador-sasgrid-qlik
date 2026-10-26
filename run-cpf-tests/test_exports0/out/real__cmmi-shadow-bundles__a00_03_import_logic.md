# Job `job_a00_03_import_logic`

- **Programa SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas` (sha256 `ad893fef25cb`)
- **Instrucciones:** 52 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.clinical_logic_date` ← SAS `clinical_logic_date` (&clinical_logic_date en real/cmmi-shadow-bundles/a00_03_import_logic.sas:16)
- `context.cov_ds_name_list` ← SAS `cov_ds_name_list` (&cov_ds_name_list en real/cmmi-shadow-bundles/a00_03_import_logic.sas:133)
- `context.cov_sheet_name_list` ← SAS `cov_sheet_name_list` (&cov_sheet_name_list en real/cmmi-shadow-bundles/a00_03_import_logic.sas:134)
- `context.keep_cols` ← SAS `keep_cols` (&keep_cols en real/cmmi-shadow-bundles/a00_03_import_logic.sas:104)
- `context.logic_path` ← SAS `logic_path` (&logic_path en real/cmmi-shadow-bundles/a00_03_import_logic.sas:16)
- `context.out_path` ← SAS `out_path` (&out_path en real/cmmi-shadow-bundles/a00_03_import_logic.sas:12)
- `context.t` ← SAS `t` (&t en real/cmmi-shadow-bundles/a00_03_import_logic.sas:116)
- `context.vars` ← SAS `vars` (&vars en real/cmmi-shadow-bundles/a00_03_import_logic.sas:116)

## Conexiones a crear

- `ref` (BASE, &out_path.\output\ref) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

## Definición de macro auxiliar `%a00_03_import_logic`()

### 1. Invocar macro %mkdirs

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_03_import_logic:s12` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:12`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `mkdirs` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:12 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `&out_path.\output,&out_path.\output\ref` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:12 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %mkdirs (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 2. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `m:a00_03_import_logic:s16` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:16`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_12_macro_call_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = `&logic_path.\&clinical_logic_date._bpci_a_trigger_list.xlsx` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:16 · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_m:a00_03_import_logic:op_16_read_file_1_row_count`, `vc_m:a00_03_import_logic:op_16_read_file_1_nulls`

### 3. Leer ip_ce_drg

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s24` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:25`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_16_read_file_1`
- **Propiedades:**
  - `TABLE` = `ip_ce_drg` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:a00_03_import_logic:op_25_read_1_row_count`, `vc_m:a00_03_import_logic:op_25_read_1_schema`

### 4. Filtrar filas (WHERE): not missing(d)

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:a00_03_import_logic:s24` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:25`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_25_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `!((input_row.d == null))` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25 · nombre oficial
- **Esquema:** `d` _(tipos por determinar)_
- **Expresión** (línea 25): SAS `not missing(d)` → Java `!((input_row.d == null))`
  - ⚠ missing(): null (y cadena vacía si es texto) en Java
- **Pruebas:** `vc_m:a00_03_import_logic:op_25_filter_1_row_count`, `vc_m:a00_03_import_logic:op_25_filter_1_nulls`, `vc_m:a00_03_import_logic:op_25_filter_1_empty`

### 5. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s24` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:25`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_25_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `distinct d as episode_group_id format=$5. length=5, ce_description, anchor_type, epi_type, e as drg format=$3. length=3` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ce_description`, `anchor_type`, `epi_type` _(tipos por determinar)_
- **Expresión** (línea 25): SAS `distinct d as episode_group_id format=$5. length=5` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '$5. length=5'
- **Expresión** (línea 25): SAS `"ip"` → Java `"ip"`
- **Expresión** (línea 25): SAS `substr(strip(c),1,2)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función substr
- **Expresión** (línea 25): SAS `e as drg format=$3. length=3` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '$3. length=3'
- **Pruebas:** `vc_m:a00_03_import_logic:op_25_project_1_schema`

### 6. Ordenar por substr(d,4,2)

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s24` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:25`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_25_project_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `substr(d,4,2)` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25 · nombre oficial
- **Esquema:** `substr(d,4,2)` _(tipos por determinar)_
- **Pruebas:** `vc_m:a00_03_import_logic:op_25_sort_1_ordering`

### 7. Escribir ref.ip_ce_drg (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:a00_03_import_logic:s24` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:25`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_25_sort_1`
- **Propiedades:**
  - `TABLE` = `ip_ce_drg` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25
  - `DATA_ACTION` = `INSERT` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:25
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:a00_03_import_logic:op_25_write_1_row_count`, `vc_m:a00_03_import_logic:op_25_write_1_schema`

### 8. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `m:a00_03_import_logic:s38` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:38`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_25_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = `&logic_path.\&clinical_logic_date._bpci_a_trigger_list.xlsx` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:38 · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_m:a00_03_import_logic:op_38_read_file_1_row_count`, `vc_m:a00_03_import_logic:op_38_read_file_1_nulls`

### 9. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `m:a00_03_import_logic:s46` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:46`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_38_read_file_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = `&logic_path.\&clinical_logic_date._bpci_a_hcpcs_apc_mapping.xlsx` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:46 · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_m:a00_03_import_logic:op_46_read_file_1_row_count`, `vc_m:a00_03_import_logic:op_46_read_file_1_nulls`

### 10. Leer op_ce

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:55`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_46_read_file_1`
- **Propiedades:**
  - `TABLE` = `op_ce` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:55
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:a00_03_import_logic:op_55_read_1_row_count`, `vc_m:a00_03_import_logic:op_55_read_1_schema`

### 11. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:55`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_55_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `distinct d as episode_group_id format=$5. length=5, c as ce_description format=$70. length=70, anchor_type, epi_type` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:55
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `anchor_type`, `epi_type` _(tipos por determinar)_
- **Expresión** (línea 55): SAS `distinct d as episode_group_id format=$5. length=5` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '$5. length=5'
- **Expresión** (línea 55): SAS `c as ce_description format=$70. length=70` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '$70. length='
- **Expresión** (línea 55): SAS `"op"` → Java `"op"`
- **Expresión** (línea 55): SAS `substr(strip(c),1,2)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función substr
- **Pruebas:** `vc_m:a00_03_import_logic:op_55_project_1_schema`

### 12. Ordenar por d

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:55`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_55_project_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `d` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:55 · nombre oficial
- **Esquema:** `d` _(tipos por determinar)_
- **Pruebas:** `vc_m:a00_03_import_logic:op_55_sort_1_ordering`

### 13. Escribir ref.op_ce (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:55`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_55_sort_1`
- **Propiedades:**
  - `TABLE` = `op_ce` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:55
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:55
  - `DATA_ACTION` = `INSERT` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:55
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:a00_03_import_logic:op_55_write_1_row_count`, `vc_m:a00_03_import_logic:op_55_write_1_schema`

### 14. Leer op_apc

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:63`
- **Propiedades:**
  - `TABLE` = `op_apc` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:a00_03_import_logic:op_63_read_1_row_count`, `vc_m:a00_03_import_logic:op_63_read_1_schema`

### 15. Leer op_apc

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:63`
- **Propiedades:**
  - `TABLE` = `op_apc` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:a00_03_import_logic:op_63_read_2_row_count`, `vc_m:a00_03_import_logic:op_63_read_2_schema`

### 16. Concatenar entradas

- **Acción:** add_component · **Componente:** `tUnite` ![Icono Talend](assets/talend-icons/tUnite_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** medium · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:63`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_55_write_1`
- **Pendientes:**
  - Esquemas compatibles entre entradas
- **Pruebas:** `vc_m:a00_03_import_logic:op_63_union_1_row_count`

### 17. Filtrar filas (WHERE): not missing(g)

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:63`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_63_union_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `!((input_row.g == null))` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63 · nombre oficial
- **Esquema:** `g` _(tipos por determinar)_
- **Expresión** (línea 63): SAS `not missing(g)` → Java `!((input_row.g == null))`
  - ⚠ missing(): null (y cadena vacía si es texto) en Java
- **Pruebas:** `vc_m:a00_03_import_logic:op_63_filter_1_row_count`, `vc_m:a00_03_import_logic:op_63_filter_1_nulls`, `vc_m:a00_03_import_logic:op_63_filter_1_empty`

### 18. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:63`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_63_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `c as ce_description format=$70. length=70, year, g as apc format=$4. length=4` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `year` _(tipos por determinar)_
- **Expresión** (línea 63): SAS `c as ce_description format=$70. length=70` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '$70. length='
- **Expresión** (línea 63): SAS `g as apc format=$4. length=4` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '$4. length=4'
- **Pruebas:** `vc_m:a00_03_import_logic:op_63_project_1_schema`

### 19. Escribir ref.op_apc (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:63`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_63_project_1`
- **Propiedades:**
  - `TABLE` = `op_apc` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63
  - `DATA_ACTION` = `INSERT` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:63
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:a00_03_import_logic:op_63_write_1_row_count`, `vc_m:a00_03_import_logic:op_63_write_1_schema`

### 20. Leer ref.op_ce

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:76`
- **Propiedades:**
  - `TABLE` = `op_ce` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:a00_03_import_logic:op_76_read_1_row_count`, `vc_m:a00_03_import_logic:op_76_read_1_schema`

### 21. Leer ref.op_apc

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:76`
- **Propiedades:**
  - `TABLE` = `op_apc` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:a00_03_import_logic:op_76_read_2_row_count`, `vc_m:a00_03_import_logic:op_76_read_2_schema`

### 22. Unir (implicit): ref.op_ce, ref.op_apc

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** medium · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:76`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_55_read_1`, Lookup desde `m:a00_03_import_logic:op_63_read_1`, Lookup desde `m:a00_03_import_logic:op_63_read_2`, Lookup desde `m:a00_03_import_logic:op_76_read_1`, Lookup desde `m:a00_03_import_logic:op_76_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.ce_description = b.ce_description` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76
- **Esquema:** `ce_description` _(tipos por determinar)_
- **Expresión** (línea 76): SAS `a.ce_description = b.ce_description` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Supuestos:** Join por coma: la condición está en el WHERE
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:a00_03_import_logic:op_76_join_1_duplicates`, `vc_m:a00_03_import_logic:op_76_join_1_row_count`, `vc_m:a00_03_import_logic:op_76_join_1_nulls`

### 23. Filtrar filas (WHERE): a.ce_description = b.ce_description

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:76`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_76_join_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `(input_row.ce_description == input_row.ce_description)` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76 · nombre oficial
- **Esquema:** `ce_description` _(tipos por determinar)_
- **Expresión** (línea 76): SAS `a.ce_description = b.ce_description` → Java `(input_row.ce_description == input_row.ce_description)`
- **Pruebas:** `vc_m:a00_03_import_logic:op_76_filter_1_row_count`, `vc_m:a00_03_import_logic:op_76_filter_1_nulls`, `vc_m:a00_03_import_logic:op_76_filter_1_empty`

### 24. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:76`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_76_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `distinct a.episode_group_id, anchor_type, epi_type, *` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `anchor_type`, `epi_type` _(tipos por determinar)_
- **Expresión** (línea 76): SAS `distinct a.episode_group_id` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pruebas:** `vc_m:a00_03_import_logic:op_76_project_1_schema`

### 25. Ordenar por substr(episode_group_id,4,2)

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:76`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_76_project_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `substr(episode_group_id,4,2)` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76 · nombre oficial
- **Esquema:** `substr(episode_group_id,4,2)` _(tipos por determinar)_
- **Pruebas:** `vc_m:a00_03_import_logic:op_76_sort_1_ordering`

### 26. Escribir ref.op_ce_apc (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:a00_03_import_logic:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:76`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_76_sort_1`
- **Propiedades:**
  - `TABLE` = `op_ce_apc` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76
  - `DATA_ACTION` = `INSERT` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:76
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:a00_03_import_logic:op_76_write_1_row_count`, `vc_m:a00_03_import_logic:op_76_write_1_schema`

### 27. Leer ref.ip_ce_drg

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s87` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:87`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_76_write_1`
- **Propiedades:**
  - `TABLE` = `ip_ce_drg` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:a00_03_import_logic:op_87_read_1_row_count`, `vc_m:a00_03_import_logic:op_87_read_1_schema`

### 28. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:a00_03_import_logic:s87` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:87`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_87_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: EPISODE_GROUP_ID, CE_DESCRIPTION, EPI_TYPE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87 · nombre oficial
- **Esquema:** `EPISODE_GROUP_ID`, `CE_DESCRIPTION`, `EPI_TYPE` _(tipos por determinar)_
- **Pruebas:** `vc_m:a00_03_import_logic:op_87_select_columns_1_schema`

### 29. Leer ref.op_ce

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s87` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:87`
- **Propiedades:**
  - `TABLE` = `op_ce` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:a00_03_import_logic:op_87_read_2_row_count`, `vc_m:a00_03_import_logic:op_87_read_2_schema`

### 30. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:a00_03_import_logic:s87` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:87`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_87_select_columns_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: EPISODE_GROUP_ID, CE_DESCRIPTION, EPI_TYPE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87 · nombre oficial
- **Esquema:** `EPISODE_GROUP_ID`, `CE_DESCRIPTION`, `EPI_TYPE` _(tipos por determinar)_
- **Pruebas:** `vc_m:a00_03_import_logic:op_87_select_columns_2_schema`

### 31. Concatenar entradas

- **Acción:** add_component · **Componente:** `tUnite` ![Icono Talend](assets/talend-icons/tUnite_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:a00_03_import_logic:s87` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:87`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_87_select_columns_2`
- **Pendientes:**
  - Esquemas compatibles entre entradas
- **Pruebas:** `vc_m:a00_03_import_logic:op_87_union_1_row_count`

### 32. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:a00_03_import_logic:s87` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:87`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_87_union_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ce_id` _(tipos por determinar)_
- **Expresión** (línea 91): SAS `substr(strip(EPISODE_GROUP_ID),4,2)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función substr
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:a00_03_import_logic:op_87_compute_1_nulls`, `vc_m:a00_03_import_logic:op_87_compute_1_dates`, `vc_m:a00_03_import_logic:op_87_compute_1_numeric`

### 33. Escribir ref.ce_id_epi_type_all

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:a00_03_import_logic:s87` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:87`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_87_compute_1`
- **Propiedades:**
  - `TABLE` = `ce_id_epi_type_all` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87
  - `DATA_ACTION` = `INSERT` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:87
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:a00_03_import_logic:op_87_write_1_row_count`, `vc_m:a00_03_import_logic:op_87_write_1_schema`

### 34. Leer ref.ce_id_epi_type_all

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s94` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:94`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_87_write_1`
- **Propiedades:**
  - `TABLE` = `ce_id_epi_type_all` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:94
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:a00_03_import_logic:op_94_read_1_row_count`, `vc_m:a00_03_import_logic:op_94_read_1_schema`

### 35. Ordenar por ce_id, EPISODE_GROUP_ID, CE_DESCRIPTION, EPI_TYPE

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s94` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:94`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_94_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ce_id, EPISODE_GROUP_ID, CE_DESCRIPTION, EPI_TYPE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:94 · nombre oficial
- **Esquema:** `ce_id`, `EPISODE_GROUP_ID`, `CE_DESCRIPTION`, `EPI_TYPE` _(tipos por determinar)_
- **Pruebas:** `vc_m:a00_03_import_logic:op_94_sort_1_ordering`

### 36. Eliminar duplicados

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s94` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:94`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_94_sort_1`
- **Propiedades:**
  - `UNIQUE_KEY` = `ce_id, EPISODE_GROUP_ID, CE_DESCRIPTION, EPI_TYPE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:94
- **Esquema:** `ce_id`, `EPISODE_GROUP_ID`, `CE_DESCRIPTION`, `EPI_TYPE` _(tipos por determinar)_
- **Pendientes:**
  - Definir la clave y la lógica para conservar la fila correcta por grupo; confirmar una opción disponible en la instalación actual.
- **Pruebas:** `vc_m:a00_03_import_logic:op_94_dedupe_1_duplicates`

### 37. Escribir ref.ce_id_epi_type_all

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:a00_03_import_logic:s94` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:94`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_94_dedupe_1`
- **Propiedades:**
  - `TABLE` = `ce_id_epi_type_all` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:94
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:94
  - `DATA_ACTION` = `INSERT` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:94
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:a00_03_import_logic:op_94_write_1_row_count`, `vc_m:a00_03_import_logic:op_94_write_1_schema`

### 38. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_03_import_logic:s99` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:99`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_94_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:99 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `vars, tha
                  ~ tsa
                  , dlm= ~` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:99 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 39. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_03_import_logic:s104` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:104`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_99_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:104 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `kept_var, &keep_cols.` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:104 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 40. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_03_import_logic:s107` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:107`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_104_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:107 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `rename_var, Covariate ICD_Version Source_DGN_code Code_Specification ICD_Diagnosis_Code Code_Description` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:107 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 41. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_03_import_logic:s110` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:110`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_107_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:110 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `length_var, $100. $10. $10. $20. $10. $300.` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:110 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 42. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `m:a00_03_import_logic:s116` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:116`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_110_macro_call_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = `&&vars&t.._dgn` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:116 · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_m:a00_03_import_logic:op_116_read_file_1_row_count`, `vc_m:a00_03_import_logic:op_116_read_file_1_nulls`

### 43. Leer ref.&&vars&t.._covariates_list

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s126` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:127`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_116_read_file_1`
- **Propiedades:**
  - `TABLE` = `_covariates_list` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:127
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:a00_03_import_logic:op_127_read_1_row_count`, `vc_m:a00_03_import_logic:op_127_read_1_schema`

### 44. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:a00_03_import_logic:s126` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:127`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_127_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `substr(VARIABLES, 5, lengthn(VARIABLES)), case when lengthn(substr(VARIABLES, 5)) > 29 then substr(VARIABLES, 5, 29) else substr(VARIABLES, 5, lengthn(VARIABLES)) end` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:127
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 127): SAS `substr(VARIABLES, 5, lengthn(VARIABLES))` → _sin traducción automática_
  - ⚠ Sin traducción automática: función substr
- **Expresión** (línea 127): SAS `case when lengthn(substr(VARIABLES, 5)) > 29 then substr(VARIABLES, 5, 29) else substr(VARIABLES, 5, lengthn(VARIABLES)) end` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pruebas:** `vc_m:a00_03_import_logic:op_127_project_1_schema`

### 45. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:a00_03_import_logic:s126` · **Confianza:** medium · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:127`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_127_project_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=cov_sheet_name_list separated by "~"` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:127 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 46. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:a00_03_import_logic:s126` · **Confianza:** medium · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:127`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:a00_03_import_logic:op_127_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=cov_ds_name_list separated by "~"` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:127 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 47. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_03_import_logic:s133` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:133`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_127_set_variable_2`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:133 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `ds_names, &cov_ds_name_list., dlm = "~" ` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:133 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 48. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_03_import_logic:s134` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:134`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_133_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:134 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `sheet_names, &cov_sheet_name_list., dlm = "~" ` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:134 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 49. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `m:a00_03_import_logic:s138` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:138`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_134_macro_call_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_m:a00_03_import_logic:op_138_read_file_1_row_count`, `vc_m:a00_03_import_logic:op_138_read_file_1_nulls`

### 50. Leer ref.&&ds_names&a.._&&vars&t..

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_03_import_logic:s148` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:148`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_138_read_file_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:a00_03_import_logic:op_148_read_1_row_count`, `vc_m:a00_03_import_logic:op_148_read_1_schema`

### 51. Escribir ref.&&ds_names&a.._&&vars&t..

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:a00_03_import_logic:s148` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:148`
- **Conexiones:** Main desde `m:a00_03_import_logic:op_148_read_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:148
  - `DATA_ACTION` = `INSERT` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:148
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:a00_03_import_logic:op_148_write_1_row_count`, `vc_m:a00_03_import_logic:op_148_write_1_schema`

### 52. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `m:a00_03_import_logic:s160` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_03_import_logic.sas:160`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `m:a00_03_import_logic:op_148_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = `fname` — SAS real/cmmi-shadow-bundles/a00_03_import_logic.sas:160 · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_m:a00_03_import_logic:op_160_read_file_1_row_count`, `vc_m:a00_03_import_logic:op_160_read_file_1_nulls`

## Sin resolver

- dataset_dynamic ref.&&vars&t.._covariates_list (real/cmmi-shadow-bundles/a00_03_import_logic.sas:116) — nombre de dataset con macrovariables
- dataset_dynamic ref.&&vars&t.._covariates_list (real/cmmi-shadow-bundles/a00_03_import_logic.sas:126) — nombre de dataset con macrovariables
- dataset_dynamic ref.&&ds_names&a.._&&vars&t.. (real/cmmi-shadow-bundles/a00_03_import_logic.sas:138) — nombre de dataset con macrovariables
- dataset_dynamic ref.&&ds_names&a.._&&vars&t.. (real/cmmi-shadow-bundles/a00_03_import_logic.sas:148) — nombre de dataset con macrovariables

## Casos de validación

- `vc_m:a00_03_import_logic:op_16_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_m:a00_03_import_logic:op_16_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_m:a00_03_import_logic:op_25_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_25_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_25_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:a00_03_import_logic:op_25_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:a00_03_import_logic:op_25_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:a00_03_import_logic:op_25_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:a00_03_import_logic:op_25_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:a00_03_import_logic:op_25_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:a00_03_import_logic:op_25_write_1_schema` (schema): Esquema destino
- `vc_m:a00_03_import_logic:op_38_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_m:a00_03_import_logic:op_38_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_m:a00_03_import_logic:op_46_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_m:a00_03_import_logic:op_46_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_m:a00_03_import_logic:op_55_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_55_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_55_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:a00_03_import_logic:op_55_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:a00_03_import_logic:op_55_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:a00_03_import_logic:op_55_write_1_schema` (schema): Esquema destino
- `vc_m:a00_03_import_logic:op_63_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_63_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_63_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_63_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_63_union_1_row_count` (row_count): Suma de filas de las entradas (UNION sin ALL elimina duplicados)
- `vc_m:a00_03_import_logic:op_63_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:a00_03_import_logic:op_63_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:a00_03_import_logic:op_63_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:a00_03_import_logic:op_63_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:a00_03_import_logic:op_63_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:a00_03_import_logic:op_63_write_1_schema` (schema): Esquema destino
- `vc_m:a00_03_import_logic:op_76_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_76_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_76_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_76_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_76_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:a00_03_import_logic:op_76_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:a00_03_import_logic:op_76_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:a00_03_import_logic:op_76_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:a00_03_import_logic:op_76_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:a00_03_import_logic:op_76_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:a00_03_import_logic:op_76_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:a00_03_import_logic:op_76_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:a00_03_import_logic:op_76_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:a00_03_import_logic:op_76_write_1_schema` (schema): Esquema destino
- `vc_m:a00_03_import_logic:op_87_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_87_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_87_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:a00_03_import_logic:op_87_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_87_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_87_select_columns_2_schema` (schema): Solo las columnas esperadas
- `vc_m:a00_03_import_logic:op_87_union_1_row_count` (row_count): Suma de filas de las entradas (UNION sin ALL elimina duplicados)
- `vc_m:a00_03_import_logic:op_87_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:a00_03_import_logic:op_87_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:a00_03_import_logic:op_87_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:a00_03_import_logic:op_87_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:a00_03_import_logic:op_87_write_1_schema` (schema): Esquema destino
- `vc_m:a00_03_import_logic:op_94_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_94_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_94_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:a00_03_import_logic:op_94_dedupe_1_duplicates` (duplicates): Se conserva la misma fila por clave (NODUPKEY conserva la primera)
- `vc_m:a00_03_import_logic:op_94_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:a00_03_import_logic:op_94_write_1_schema` (schema): Esquema destino
- `vc_m:a00_03_import_logic:op_116_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_m:a00_03_import_logic:op_116_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_m:a00_03_import_logic:op_127_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_127_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_127_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:a00_03_import_logic:op_138_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_m:a00_03_import_logic:op_138_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_m:a00_03_import_logic:op_148_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_03_import_logic:op_148_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_03_import_logic:op_148_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:a00_03_import_logic:op_148_write_1_schema` (schema): Esquema destino
- `vc_m:a00_03_import_logic:op_160_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_m:a00_03_import_logic:op_160_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
