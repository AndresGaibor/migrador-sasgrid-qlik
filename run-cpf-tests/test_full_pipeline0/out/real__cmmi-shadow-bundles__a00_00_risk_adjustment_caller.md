# Job `job_a00_00_risk_adjustment_caller`

- **Programa SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas` (sha256 `345abc29d70f`)
- **Instrucciones:** 23 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%a00_00_risk_adjustment_caller(code_dir, run_date, clinical_logic_date, medical_code_list, fy_version, cy_version, obs, import_switch, ce_start_index, ce_end_index, run_a_series, run_process_af, run_ach_threshold, run_mjrle_stage0, run_b_series, import_covariates, run_risk_adjustment, run_tsp_model, run_GLM_model)` está integrada en el Job.

## Variables de contexto

- `context.ce_end_index` ← SAS `ce_end_index` (&ce_end_index en real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:111)
- `context.ce_epi_type_list` ← SAS `ce_epi_type_list` (&ce_epi_type_list en real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:119)
- `context.ce_id_list` ← SAS `ce_id_list` (&ce_id_list en real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:118)
- `context.ce_start_index` ← SAS `ce_start_index` (&ce_start_index en real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:111)
- `context.clinical_logic_date` ← SAS `clinical_logic_date` = `2024_06_14` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 2024_06_14)
- `context.code_dir` ← SAS `code_dir` = `/** All series parameters **/
                      run_date            = 2025_02_12` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: /** All series parameters **/
                      run_date            = 2025_02_12)
- `context.cy_version` ← SAS `cy_version` = `24` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 24)
- `context.fy_version` ← SAS `fy_version` = `24` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 24)
- `context.import_covariates` ← SAS `import_covariates` = `0` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 0)
- `context.import_switch` ← SAS `import_switch` = `0` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 0)
- `context.logic_path` ← SAS `logic_path` (&logic_path en real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:138)
- `context.medical_code_list` ← SAS `medical_code_list` = `2024_08_19` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 2024_08_19)
- `context.obs` ← SAS `obs` = `max` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: max)
- `context.run_a_series` ← SAS `run_a_series` = `/** b series switches   **/
                     run_b_series         = 0` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: /** b series switches   **/
                     run_b_series         = 0)
- `context.run_ach_threshold` ← SAS `run_ach_threshold` = `1` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 1)
- `context.run_b_series` ← SAS `run_b_series` = `/** To run risk adjustment` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: /** To run risk adjustment)
- `context.run_date` ← SAS `run_date` = `/** a series switches   **/
                      run_a_series        = 1` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: /** a series switches   **/
                      run_a_series        = 1)
- `context.run_GLM_model` ← SAS `run_GLM_model` (&run_GLM_model en real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:131)
- `context.run_mjrle_stage0` ← SAS `run_mjrle_stage0` = `0` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 0)
- `context.run_process_af` ← SAS `run_process_af` = `0` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 0)
- `context.run_risk_adjustment` ← SAS `run_risk_adjustment` = `1` (Parámetro de la macro principal %a00_00_risk_adjustment_caller; argumento SAS: 1)
- `context.run_tsp_model` ← SAS `run_tsp_model` (&run_tsp_model en real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:131)

## Conexiones a crear

- `ref` (BASE, &out_path.\output\ref) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %a00_01_utility_macros

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s50` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:50`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `a00_01_utility_macros` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:50 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %a00_01_utility_macros (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 2. Invocar macro %a00_02_assign_globals

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s54` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:54`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_50_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a00_02_assign_globals` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:54 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %a00_02_assign_globals (definida en real/cmmi-shadow-bundles/a00_02_assign_globals.sas)

### 3. Invocar macro %a00_03_import_logic

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s58` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:58`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_54_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a00_03_import_logic` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:58 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %a00_03_import_logic (definida en real/cmmi-shadow-bundles/a00_03_import_logic.sas)

### 4. Invocar macro %a00_04_assign_libs

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s62` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:62`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_58_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a00_04_assign_libs` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:62 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 5. Invocar macro %generate_log

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s74` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:74`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_62_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `generate_log` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:74 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `log_filename=process_af` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:74 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %generate_log (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 6. Invocar macro %a01_01_process_af

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s76` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:76`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_74_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a01_01_process_af` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:76 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 7. Invocar macro %generate_log

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s82` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:82`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_76_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `generate_log` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:82 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `log_filename=ach_threshold` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:82 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %generate_log (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 8. Invocar macro %a01_02_ach_threshold

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s83` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:83`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_82_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a01_02_ach_threshold` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:83 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 9. Invocar macro %a02_01_prep_episodes_for_logit

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s89` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:89`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_83_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a02_01_prep_episodes_for_logit` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:89 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 10. Invocar macro %a02_02_logit_regression

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s91` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:91`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_89_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a02_02_logit_regression` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:91 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 11. Invocar macro %a02_03_flag_pseudo_op

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s93` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:93`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_91_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `a02_03_flag_pseudo_op` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:93 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 12. Invocar macro %b00_01_assign_libs_globals

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s101` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:101`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_93_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `b00_01_assign_libs_globals` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:101 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 13. Invocar macro %b01_01_prep_risk_adj_covariates

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s104` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:104`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_101_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `b01_01_prep_risk_adj_covariates` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:104 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `ref_files = 1,
                                          tsp_files = 1` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:104 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 14. Invocar macro %b01_02_assign_covariate

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s109` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:109`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_104_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `b01_02_assign_covariate` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:109 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 15. Invocar macro %generate_log

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s111` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:111`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_109_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `generate_log` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:111 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `log_filename=ra_ce_&ce_start_index._start_ce._&ce_end_index._end_ce.` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:111 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %generate_log (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 16. Leer ref.ce_id_epi_type_all

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s113` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114`
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_111_macro_call_1`
- **Propiedades:**
  - `TABLE` = `ce_id_epi_type_all` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería ref es de tipo BASE en &out_path.\output\ref: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:a00_00_risk_adjustment_caller:op_114_read_1_row_count`, `vc_m:a00_00_risk_adjustment_caller:op_114_read_1_schema`

### 17. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:a00_00_risk_adjustment_caller:s113` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:a00_00_risk_adjustment_caller:op_114_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `episode_group_id, epi_type` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `episode_group_id`, `epi_type` _(tipos por determinar)_
- **Pruebas:** `vc_m:a00_00_risk_adjustment_caller:op_114_project_1_schema`

### 18. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s113` · **Confianza:** medium · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:a00_00_risk_adjustment_caller:op_114_project_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY= ce_id_list separated by " "` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 19. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s113` · **Confianza:** medium · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:a00_00_risk_adjustment_caller:op_114_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY= ce_epi_type_list separated by " "` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:114 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 20. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s118` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:118`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_114_set_variable_2`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:118 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `ce_ids, &ce_id_list.` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:118 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 21. Invocar macro %macarray

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s119` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:119`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_118_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `macarray` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:119 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `epi_types, &ce_epi_type_list.` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:119 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %macarray (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

### 22. Invocar macro %b02_01_risk_adjustment

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s131` · **Confianza:** low · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:131`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_119_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `b02_01_risk_adjustment` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:131 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `run_tsp = &run_tsp_model.,
                                       run_glm = &run_GLM_model.` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:131 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 23. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `m:a00_00_risk_adjustment_caller:s138` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:138`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `m:a00_00_risk_adjustment_caller:op_131_macro_call_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = `&logic_path.\Acumen_calculated_estimates.xlsx` — SAS real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:138 · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_m:a00_00_risk_adjustment_caller:op_138_read_file_1_row_count`, `vc_m:a00_00_risk_adjustment_caller:op_138_read_file_1_nulls`

## Sin resolver

- dataset_dynamic out&ce_id_short..&ce_id_w_type._estimates (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:138) — nombre de dataset con macrovariables
- macro a00_04_assign_libs (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:62) — sin definición en el proyecto
- macro a01_01_process_af (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:76) — sin definición en el proyecto
- macro a01_02_ach_threshold (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:83) — sin definición en el proyecto
- macro a02_01_prep_episodes_for_logit (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:89) — sin definición en el proyecto
- macro a02_02_logit_regression (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:91) — sin definición en el proyecto
- macro a02_03_flag_pseudo_op (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:93) — sin definición en el proyecto
- macro b00_01_assign_libs_globals (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:101) — sin definición en el proyecto
- macro b01_01_prep_risk_adj_covariates (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:104) — sin definición en el proyecto
- macro b01_02_assign_covariate (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:109) — sin definición en el proyecto
- macro b02_01_risk_adjustment (real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas:131) — sin definición en el proyecto

## Casos de validación

- `vc_m:a00_00_risk_adjustment_caller:op_114_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:a00_00_risk_adjustment_caller:op_114_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:a00_00_risk_adjustment_caller:op_114_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:a00_00_risk_adjustment_caller:op_138_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_m:a00_00_risk_adjustment_caller:op_138_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
