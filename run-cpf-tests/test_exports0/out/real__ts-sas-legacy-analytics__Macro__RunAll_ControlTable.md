# Job `job_runall_controltable`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas` (sha256 `da0c61dfd48e`)
- **Instrucciones:** 5 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.abort` ← SAS `abort` = `Y` (%LET de primer nivel)
- `context.abort_codes` ← SAS `abort_codes` = `0 1` (%LET de primer nivel)
- `context.autoexec` ← SAS `autoexec` = `&base.&fs.&env.&fs.autoexec.sas` (%LET de primer nivel)
- `context.base` ← SAS `base` = `/proj/009/tak491_303` (%LET de primer nivel)
- `context.command` ← SAS `command` = `&sas` (%LET de primer nivel)
- `context.config` ← SAS `config` (%LET de primer nivel)
- `context.end_time` ← SAS `end_time` = `%sysfunc(datetime())` (%LET de primer nivel)
- `context.env` ← SAS `env` = `prod` (%LET de primer nivel)
- `context.fs` ← SAS `fs` = `/` (%LET de primer nivel)
- `context.log` ← SAS `log` = `&base.&fs.&env.&fs.output&fs.logs` (%LET de primer nivel)
- `context.max_threads` ← SAS `max_threads` = `10` (%LET de primer nivel)
- `context.options` ← SAS `options` = `-autoexec &autoexec` (%LET de primer nivel)
- `context.print` ← SAS `print` = `&base.&fs.&env.&fs.output&fs.reports` (%LET de primer nivel)
- `context.sas` ← SAS `sas` = `%sysget(SAS_ROOT)/sas` (%LET de primer nivel)
- `context.source` ← SAS `source` = `&base.&fs.&env.&fs.programs` (%LET de primer nivel)
- `context.start_time` ← SAS `start_time` = `%sysfunc(datetime())` (%LET de primer nivel)
- `context.summary_rpt` ← SAS `summary_rpt` = `&log.&fs.RunAll.&summary_rpt_type` (%LET de primer nivel)
- `context.summary_rpt_type` ← SAS `summary_rpt_type` = `html` (%LET de primer nivel)

## Pasos

### 1. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s126` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:128`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_128_read_file_1_row_count`, `vc_op_128_read_file_1_nulls`

### 2. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s126` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:126`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_126_inline_data_1_row_count`

### 3. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s126` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:126`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_128_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `4 asignaciones, 0 condicionales` — SAS real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:126
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `source`, `env`, `log`, `print` _(tipos por determinar)_
- **Expresión** (línea 129): SAS `"&source"` → Java `"&source"`
- **Expresión** (línea 130): SAS `"&env"` → Java `"&env"`
- **Expresión** (línea 131): SAS `quote("&log")` → _sin traducción automática_
  - ⚠ Sin traducción automática: función quote
- **Expresión** (línea 132): SAS `quote("&print")` → _sin traducción automática_
  - ⚠ Sin traducción automática: función quote
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_126_compute_1_nulls`, `vc_op_126_compute_1_dates`, `vc_op_126_compute_1_numeric`

### 4. Escribir programs

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s126` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:126`
- **Conexiones:** Main desde `op_126_compute_1`
- **Propiedades:**
  - `TABLE` = `programs` — SAS real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:126
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:126
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:126
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_126_write_1_row_count`, `vc_op_126_write_1_schema`

### 5. Invocar macro %runall

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s155` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:155`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_126_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `runall` — SAS real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:155 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `debug=N` — SAS real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:155 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %runall (definida en real/ts-sas-legacy-analytics/Macro/RunAll.sas)

## Sin resolver

- include /proj/009/tak491_303/RunAll.sas (real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas:154) — candidate → real/ts-sas-legacy-analytics/Macro/RunAll.sas

## Casos de validación

- `vc_op_128_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_128_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_126_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_126_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_126_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_126_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_126_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_126_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
