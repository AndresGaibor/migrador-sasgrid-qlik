# Job `job_rx_build`

- **Programa SAS:** `real/tmsis-analytic-file/RX_build.sas` (sha256 `e3b268c2bc5a`)
- **Instrucciones:** 22 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.da_config_macro` ← SAS `da_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/da_config.sas"` (%LET de primer nivel)
- `context.FL` ← SAS `FL` = `RX` (%LET de primer nivel)
- `context.path` ← SAS `path` = `/sasdata/users/&sysuserid/&TMSIS/&sub_env/data_analytics/taf/rx` (%LET de primer nivel)
- `context.tms_config_macro` ← SAS `tms_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/tms_config.sas"` (%LET de primer nivel)

## Pasos

### 1. Invocar macro %setenv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s43` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:43`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `setenv` — SAS real/tmsis-analytic-file/RX_build.sas:43 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %setenv (definida en real/tmsis-analytic-file/001_batch_bsf.sas)

### 2. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s97` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:98`
- **Conexiones:** OnSubjobOk desde `op_43_macro_call_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 3. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s107` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:108`
- **Conexiones:** OnSubjobOk desde `op_98_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 4. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s119` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:119`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_108_unsupported_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/tmsis-analytic-file/RX_build.sas:119
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `rep_date`, `FILE_DATE` _(tipos por determinar)_
- **Expresión** (línea 122): SAS `input(strip("&REPORTING_PERIOD"),YYMMDD12.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 123): SAS `input(put(input("&REPORTING_PERIOD", ANYDTDTE10.),yymmn6.),6.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.),yymmn6.),'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_119_compute_1_nulls`, `vc_op_119_compute_1_dates`, `vc_op_119_compute_1_numeric`

### 5. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s119` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:124`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_119_compute_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/RX_build.sas:124 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 6. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s119` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:126`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_124_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/RX_build.sas:126 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 7. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s119` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:127`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_126_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/RX_build.sas:127 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 8. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s119` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:128`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_127_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/RX_build.sas:128 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 9. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s119` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:129`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_128_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/RX_build.sas:129 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 10. Invocar macro %process

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s184` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:184`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_129_set_variable_1`
- **Propiedades:**
  - `PROCESS` (Job) = `process` — SAS real/tmsis-analytic-file/RX_build.sas:184 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %process (definida en real/tmsis-analytic-file/IP_Build.sas)

## Definición de macro auxiliar `%setENV`()

## Definición de macro auxiliar `%PROCESS`()

### 1. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:PROCESS:s136` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:136`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 2. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:143`
- **Conexiones:** OnSubjobOk desde `m:PROCESS:op_136_maintenance_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 3. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:145`
- **Conexiones:** Main desde `m:PROCESS:op_143_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 4. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:147`
- **Conexiones:** Main desde `m:PROCESS:op_145_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 5. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:149`
- **Conexiones:** Main desde `m:PROCESS:op_147_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 6. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:151`
- **Conexiones:** Main desde `m:PROCESS:op_149_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 7. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:153`
- **Conexiones:** Main desde `m:PROCESS:op_151_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 8. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:155`
- **Conexiones:** Main desde `m:PROCESS:op_153_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 9. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:159`
- **Conexiones:** Main desde `m:PROCESS:op_155_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 10. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:164`
- **Conexiones:** Main desde `m:PROCESS:op_159_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 11. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:167`
- **Conexiones:** Main desde `m:PROCESS:op_164_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 12. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:PROCESS:s175` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/RX_build.sas:175`
- **Conexiones:** OnSubjobOk desde `m:PROCESS:op_167_unsupported_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Sin resolver

- include &tms_config_macro (real/tmsis-analytic-file/RX_build.sas:23) — ruta dinámica
- include &da_config_macro (real/tmsis-analytic-file/RX_build.sas:27) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/programs/AWS_Shared_Macros.sas" (real/tmsis-analytic-file/RX_build.sas:66) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/programs/AWS_Grouper_Macro.sas" (real/tmsis-analytic-file/RX_build.sas:67) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/rx/programs/AWS_RX_Macros.sas" (real/tmsis-analytic-file/RX_build.sas:68) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/programs/Fasc.sas" (real/tmsis-analytic-file/RX_build.sas:69) — ruta dinámica
- macro tmsis_connect (real/tmsis-analytic-file/RX_build.sas:99) — sin definición en el proyecto
- macro job_control_rd (real/tmsis-analytic-file/RX_build.sas:101) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/RX_build.sas:103) — sin definición en el proyecto
- macro tmsis_connect (real/tmsis-analytic-file/RX_build.sas:109) — sin definición en el proyecto
- macro job_control_updt (real/tmsis-analytic-file/RX_build.sas:111) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/RX_build.sas:113) — sin definición en el proyecto
- macro tmsis_connect (real/tmsis-analytic-file/RX_build.sas:142) — sin definición en el proyecto
- macro aws_maxid_pull (real/tmsis-analytic-file/RX_build.sas:144) — sin definición en el proyecto
- macro aws_claims_family_table_link (real/tmsis-analytic-file/RX_build.sas:146) — sin definición en el proyecto
- macro process_nppes (real/tmsis-analytic-file/RX_build.sas:148) — sin definición en el proyecto
- macro process_ccs (real/tmsis-analytic-file/RX_build.sas:150) — sin definición en el proyecto
- macro aws_extract_line_ (real/tmsis-analytic-file/RX_build.sas:152) — sin definición en el proyecto
- macro build_ (real/tmsis-analytic-file/RX_build.sas:154) — sin definición en el proyecto
- macro job_control_updt2 (real/tmsis-analytic-file/RX_build.sas:156) — sin definición en el proyecto
- macro create_meta_info (real/tmsis-analytic-file/RX_build.sas:160) — sin definición en el proyecto
- macro create_eftsmeta_info (real/tmsis-analytic-file/RX_build.sas:161) — sin definición en el proyecto
- macro create_meta_info (real/tmsis-analytic-file/RX_build.sas:165) — sin definición en el proyecto
- macro create_eftsmeta_info (real/tmsis-analytic-file/RX_build.sas:166) — sin definición en el proyecto
- macro final_control_info (real/tmsis-analytic-file/RX_build.sas:168) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/RX_build.sas:170) — sin definición en el proyecto

## Casos de validación

- `vc_op_119_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_119_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_119_compute_1_numeric` (numeric): Redondeo y precisión

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
