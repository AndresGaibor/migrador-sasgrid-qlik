# Job `job_001_batch_bsf`

- **Programa SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas` (sha256 `eee7c90f6b5c`)
- **Instrucciones:** 19 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.BSF_FILE_DATE` ← SAS `BSF_FILE_DATE` = `&TAF_FILE_DATE` (%LET de primer nivel)
- `context.da_config_macro` ← SAS `da_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/da_config.sas"` (%LET de primer nivel)
- `context.FIL_4TH_NODE` ← SAS `FIL_4TH_NODE` = `BSF` (%LET de primer nivel)
- `context.MAX_KEEP` ← SAS `MAX_KEEP` = `0` (%LET de primer nivel)
- `context.path` ← SAS `path` = `/sasdata/users/&sysuserid/&TMSIS/&sub_env/data_analytics/taf/bsf` (%LET de primer nivel)
- `context.prog_path` ← SAS `prog_path` = `&path./programs` (%LET de primer nivel)
- `context.TABLE_NAME` ← SAS `TABLE_NAME` = `TAF_MON_BSF` (%LET de primer nivel)
- `context.TEST_RUN` ← SAS `TEST_RUN` = `NO` (%LET de primer nivel)
- `context.tms_config_macro` ← SAS `tms_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/tms_config.sas"` (%LET de primer nivel)

## Pasos

### 1. Invocar macro %setenv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s39` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:39`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `setenv` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:39 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %setenv (definida en real/tmsis-analytic-file/001_batch_bsf.sas)

### 2. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s87` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:88`
- **Conexiones:** OnSubjobOk desde `op_39_macro_call_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 3. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s87` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:94`
- **Conexiones:** Main desde `op_88_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 4. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s102` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:102`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_94_unsupported_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `6 asignaciones, 0 condicionales` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:102
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `begmon`, `BSF_FILE_DATE`, `RPT_PRD`, `RPT_OUT`, `FILE_DT_END`, `numdays` _(tipos por determinar)_
- **Expresión** (línea 103): SAS `put(intnx('month',input("&REPORTING_PERIOD",YYMMDD12.),0,"BEGINNING"),date9.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.),0,"BEGINN'
- **Expresión** (línea 107): SAS `input(put(input("&REPORTING_PERIOD",YYMMDD12.),yymmn6.),6.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.),yymmn6.),'
- **Expresión** (línea 110): SAS `cats("'",put(input(strip("&REPORTING_PERIOD"),YYMMDD12.),date9.),"'")` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.),date9.),"'
- **Expresión** (línea 113): SAS `compress(RPT_PRD,"'")` → _sin traducción automática_
  - ⚠ Sin traducción automática: función compress
- **Expresión** (línea 116): SAS `put(intnx('month',input("&sysdate",date9.),0,"END"),date9.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.),0,"END"),'
- **Expresión** (línea 121): SAS `day(input("&REPORTING_PERIOD",YYMMDD12.))` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.))'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_102_compute_1_nulls`, `vc_op_102_compute_1_dates`, `vc_op_102_compute_1_numeric`

### 5. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:104`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_102_compute_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:104 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 6. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:105`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_104_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:105 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 7. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:108`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_105_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:108 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 8. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:111`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_108_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:111 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 9. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:114`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_111_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:114 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 10. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:117`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_114_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:117 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 11. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:119`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_117_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:119 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 12. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s102` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:122`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_119_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/001_batch_bsf.sas:122 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 13. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s126` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:126`
- **Conexiones:** OnSubjobOk desde `op_122_set_variable_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 14. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s165` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:236`
- **Conexiones:** OnSubjobOk desde `op_126_maintenance_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 15. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s165` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:238`
- **Conexiones:** Main desde `op_236_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 16. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s165` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:240`
- **Conexiones:** Main desde `op_238_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 17. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s165` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:242`
- **Conexiones:** Main desde `op_240_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 18. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s165` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:245`
- **Conexiones:** Main desde `op_242_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 19. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s253` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_batch_bsf.sas:253`
- **Conexiones:** OnSubjobOk desde `op_245_unsupported_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Definición de macro auxiliar `%setENV`()

## Sin resolver

- include &tms_config_macro (real/tmsis-analytic-file/001_batch_bsf.sas:16) — ruta dinámica
- include &da_config_macro (real/tmsis-analytic-file/001_batch_bsf.sas:20) — ruta dinámica
- include "/sasdata/users/&sysuserid/&TMSIS/&sub_env/data_analytics/taf/programs/AWS_Shared_Macros.sas" (real/tmsis-analytic-file/001_batch_bsf.sas:59) — ruta dinámica
- include "&prog_path./000_bsf_macros.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:140) — ruta dinámica
- include "&prog_path./002_bsf_ELG00002.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:141) — ruta dinámica
- include "&prog_path./003_bsf_ELG00003.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:142) — ruta dinámica
- include "&prog_path./004_bsf_ELG00004.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:143) — ruta dinámica
- include "&prog_path./005_bsf_ELG00005.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:144) — ruta dinámica
- include "&prog_path./006_bsf_ELG00006.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:145) — ruta dinámica
- include "&prog_path./007_bsf_ELG00007.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:146) — ruta dinámica
- include "&prog_path./008_bsf_ELG00008.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:147) — ruta dinámica
- include "&prog_path./009_bsf_ELG00009.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:148) — ruta dinámica
- include "&prog_path./010_bsf_ELG00010.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:149) — ruta dinámica
- include "&prog_path./011_bsf_ELG00011.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:150) — ruta dinámica
- include "&prog_path./012_bsf_ELG00012.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:151) — ruta dinámica
- include "&prog_path./013_bsf_ELG00013.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:152) — ruta dinámica
- include "&prog_path./014_bsf_ELG00014.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:153) — ruta dinámica
- include "&prog_path./015_bsf_ELG00015.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:154) — ruta dinámica
- include "&prog_path./016_bsf_ELG00016.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:155) — ruta dinámica
- include "&prog_path./017_bsf_ELG00017.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:156) — ruta dinámica
- include "&prog_path./018_bsf_ELG00018.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:157) — ruta dinámica
- include "&prog_path./020_bsf_ELG00020.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:158) — ruta dinámica
- include "&prog_path./021_bsf_ELG00021.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:159) — ruta dinámica
- include "&prog_path./022b_bsf_ELG00022.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:160) — ruta dinámica
- include "&prog_path./022_bsf_TPL00002.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:161) — ruta dinámica
- include "&prog_path./023_bsf_final.sas" /source2 (real/tmsis-analytic-file/001_batch_bsf.sas:162) — ruta dinámica
- macro tmsis_connect (real/tmsis-analytic-file/001_batch_bsf.sas:89) — sin definición en el proyecto
- macro job_control_rd (real/tmsis-analytic-file/001_batch_bsf.sas:91) — sin definición en el proyecto
- macro job_control_updt (real/tmsis-analytic-file/001_batch_bsf.sas:96) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/001_batch_bsf.sas:98) — sin definición en el proyecto
- macro tmsis_connect (real/tmsis-analytic-file/001_batch_bsf.sas:167) — sin definición en el proyecto
- macro aws_maxid_pull_bsf (real/tmsis-analytic-file/001_batch_bsf.sas:169) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:171) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:172) — sin definición en el proyecto
- macro create_elg00002 (real/tmsis-analytic-file/001_batch_bsf.sas:173) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:175) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:176) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:179) — sin definición en el proyecto
- macro create_elg00004 (real/tmsis-analytic-file/001_batch_bsf.sas:180) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:182) — sin definición en el proyecto
- macro create_elg00005 (real/tmsis-analytic-file/001_batch_bsf.sas:183) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:185) — sin definición en el proyecto
- macro create_elg00006 (real/tmsis-analytic-file/001_batch_bsf.sas:186) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:188) — sin definición en el proyecto
- macro create_elg00007 (real/tmsis-analytic-file/001_batch_bsf.sas:189) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:191) — sin definición en el proyecto
- macro create_elg00008 (real/tmsis-analytic-file/001_batch_bsf.sas:192) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:194) — sin definición en el proyecto
- macro create_elg00009 (real/tmsis-analytic-file/001_batch_bsf.sas:195) — sin definición en el proyecto
- macro create_initial_table (real/tmsis-analytic-file/001_batch_bsf.sas:196) — sin definición en el proyecto
- … y 32 más

## Casos de validación

- `vc_op_102_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_102_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_102_compute_1_numeric` (numeric): Redondeo y precisión

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
