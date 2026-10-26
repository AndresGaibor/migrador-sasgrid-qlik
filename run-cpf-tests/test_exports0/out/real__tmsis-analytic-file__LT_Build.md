# Job `job_lt_build`

- **Programa SAS:** `real/tmsis-analytic-file/LT_Build.sas` (sha256 `413c4d239eb6`)
- **Instrucciones:** 25 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.da_config_macro` ← SAS `da_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/da_config.sas"` (%LET de primer nivel)
- `context.FL` ← SAS `FL` = `LT` (%LET de primer nivel)
- `context.tms_config_macro` ← SAS `tms_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/tms_config.sas"` (%LET de primer nivel)

## Pasos

### 1. Invocar macro %setenv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s36` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:36`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `setenv` — SAS real/tmsis-analytic-file/LT_Build.sas:36 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %setenv (definida en real/tmsis-analytic-file/001_batch_bsf.sas)

### 2. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s75` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:76`
- **Conexiones:** OnSubjobOk desde `op_36_macro_call_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 3. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s87` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:88`
- **Conexiones:** OnSubjobOk desde `op_76_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 4. Invocar macro %process

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s157` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:157`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_88_unsupported_1`
- **Propiedades:**
  - `PROCESS` (Job) = `process` — SAS real/tmsis-analytic-file/LT_Build.sas:157 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %process (definida en real/tmsis-analytic-file/IP_Build.sas)

## Definición de macro auxiliar `%setENV`()

## Definición de macro auxiliar `%PROCESS`()

### 1. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:PROCESS:s100` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:100`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/tmsis-analytic-file/LT_Build.sas:100
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `rep_date`, `FILE_DATE` _(tipos por determinar)_
- **Expresión** (línea 103): SAS `put(year(input("&REPORTING_PERIOD",ANYDTDTE10.)),4.) || put(month(input("&REPORTING_PERIOD",ANYDTDTE10.)),Z2.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)),4.) || p'
- **Expresión** (línea 108): SAS `input(put(input("&REPORTING_PERIOD", ANYDTDTE10.),yymmn6.),6.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.),yymmn6.),'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:PROCESS:op_100_compute_1_nulls`, `vc_m:PROCESS:op_100_compute_1_dates`, `vc_m:PROCESS:op_100_compute_1_numeric`

### 2. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:PROCESS:s100` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:104`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:PROCESS:op_100_compute_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/LT_Build.sas:104 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 3. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:PROCESS:s100` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:105`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:PROCESS:op_104_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/LT_Build.sas:105 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 4. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:PROCESS:s100` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:106`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:PROCESS:op_105_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/LT_Build.sas:106 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 5. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:PROCESS:s100` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:107`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:PROCESS:op_106_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/LT_Build.sas:107 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 6. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:PROCESS:s100` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:109`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:PROCESS:op_107_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/LT_Build.sas:109 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 7. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:PROCESS:s100` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:110`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:PROCESS:op_109_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/LT_Build.sas:110 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 8. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:PROCESS:s113` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:113`
- **Conexiones:** OnSubjobOk desde `m:PROCESS:op_110_set_variable_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 9. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:120`
- **Conexiones:** OnSubjobOk desde `m:PROCESS:op_113_maintenance_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 10. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:122`
- **Conexiones:** Main desde `m:PROCESS:op_120_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 11. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:124`
- **Conexiones:** Main desde `m:PROCESS:op_122_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 12. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:126`
- **Conexiones:** Main desde `m:PROCESS:op_124_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 13. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:128`
- **Conexiones:** Main desde `m:PROCESS:op_126_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 14. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:130`
- **Conexiones:** Main desde `m:PROCESS:op_128_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 15. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:132`
- **Conexiones:** Main desde `m:PROCESS:op_130_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 16. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:134`
- **Conexiones:** Main desde `m:PROCESS:op_132_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 17. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:136`
- **Conexiones:** Main desde `m:PROCESS:op_134_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 18. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:139`
- **Conexiones:** Main desde `m:PROCESS:op_136_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 19. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:144`
- **Conexiones:** Main desde `m:PROCESS:op_139_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 20. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:PROCESS:s118` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:147`
- **Conexiones:** Main desde `m:PROCESS:op_144_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 21. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:PROCESS:s154` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/LT_Build.sas:154`
- **Conexiones:** OnSubjobOk desde `m:PROCESS:op_147_unsupported_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Sin resolver

- include &tms_config_macro (real/tmsis-analytic-file/LT_Build.sas:17) — ruta dinámica
- include &da_config_macro (real/tmsis-analytic-file/LT_Build.sas:21) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/programs/AWS_Shared_Macros.sas" (real/tmsis-analytic-file/LT_Build.sas:43) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/programs/AWS_Grouper_Macro.sas" (real/tmsis-analytic-file/LT_Build.sas:44) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/lt/programs/AWS_LT_Macros.sas" (real/tmsis-analytic-file/LT_Build.sas:45) — ruta dinámica
- include "/sasdata/users/&sysuserid/&tmsis./&sub_env./data_analytics/taf/programs/Fasc.sas" (real/tmsis-analytic-file/LT_Build.sas:46) — ruta dinámica
- macro tmsis_connect (real/tmsis-analytic-file/LT_Build.sas:77) — sin definición en el proyecto
- macro job_control_rd (real/tmsis-analytic-file/LT_Build.sas:79) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/LT_Build.sas:81) — sin definición en el proyecto
- macro tmsis_connect (real/tmsis-analytic-file/LT_Build.sas:89) — sin definición en el proyecto
- macro job_control_updt (real/tmsis-analytic-file/LT_Build.sas:91) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/LT_Build.sas:93) — sin definición en el proyecto
- macro tmsis_connect (real/tmsis-analytic-file/LT_Build.sas:119) — sin definición en el proyecto
- macro aws_maxid_pull (real/tmsis-analytic-file/LT_Build.sas:121) — sin definición en el proyecto
- macro aws_claims_family_table_link (real/tmsis-analytic-file/LT_Build.sas:123) — sin definición en el proyecto
- macro process_nppes (real/tmsis-analytic-file/LT_Build.sas:125) — sin definición en el proyecto
- macro process_ccs (real/tmsis-analytic-file/LT_Build.sas:127) — sin definición en el proyecto
- macro aws_extract_line_lt (real/tmsis-analytic-file/LT_Build.sas:129) — sin definición en el proyecto
- macro aws_assign_grouper_data_conv (real/tmsis-analytic-file/LT_Build.sas:131) — sin definición en el proyecto
- macro build_lt (real/tmsis-analytic-file/LT_Build.sas:133) — sin definición en el proyecto
- macro job_control_updt2 (real/tmsis-analytic-file/LT_Build.sas:135) — sin definición en el proyecto
- macro create_meta_info (real/tmsis-analytic-file/LT_Build.sas:140) — sin definición en el proyecto
- macro create_eftsmeta_info (real/tmsis-analytic-file/LT_Build.sas:141) — sin definición en el proyecto
- macro create_meta_info (real/tmsis-analytic-file/LT_Build.sas:145) — sin definición en el proyecto
- macro create_eftsmeta_info (real/tmsis-analytic-file/LT_Build.sas:146) — sin definición en el proyecto
- macro final_control_info (real/tmsis-analytic-file/LT_Build.sas:148) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/LT_Build.sas:150) — sin definición en el proyecto

## Casos de validación

- `vc_m:PROCESS:op_100_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:PROCESS:op_100_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:PROCESS:op_100_compute_1_numeric` (numeric): Redondeo y precisión

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
