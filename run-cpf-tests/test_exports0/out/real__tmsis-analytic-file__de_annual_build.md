# Job `job_de_annual_build`

- **Programa SAS:** `real/tmsis-analytic-file/de_annual_build.sas` (sha256 `e4468a94ecea`)
- **Instrucciones:** 9 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.basedir` ← SAS `basedir` = `/sasdata/users/&sysuserid/&TMSIS/&sub_env/data_analytics/taf/ann_de` (%LET de primer nivel)
- `context.da_config_macro` ← SAS `da_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/da_config.sas"` (%LET de primer nivel)
- `context.DA_RUN_ID` ← SAS `DA_RUN_ID` = `&DA_RUN_ID.` (%LET de primer nivel)
- `context.MONTHSB` ← SAS `MONTHSB` = `12 11 10 09 08 07 06 05 04 03 02 01` (%LET de primer nivel)
- `context.NMCSLOTS` ← SAS `NMCSLOTS` = `16` (%LET de primer nivel)
- `context.NWAIVSLOTS` ← SAS `NWAIVSLOTS` = `10` (%LET de primer nivel)
- `context.pyear` ← SAS `pyear` (&pyear en real/tmsis-analytic-file/de_annual_build.sas:180)
- `context.tms_config_macro` ← SAS `tms_config_macro` = `"/sasdata/users/&sysuserid/tmsislockdown/config/tms_config.sas"` (%LET de primer nivel)
- `context.YEAR` ← SAS `YEAR` = `&YEAR.` (%LET de primer nivel)

## Pasos

### 1. Invocar macro %setenv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s41` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `setenv` — SAS real/tmsis-analytic-file/de_annual_build.sas:41 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %setenv (definida en real/tmsis-analytic-file/001_batch_bsf.sas)

### 2. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s119` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:120`
- **Conexiones:** OnSubjobOk desde `op_41_macro_call_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 3. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s119` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:125`
- **Conexiones:** Main desde `op_120_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 4. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s137` · **Confianza:** medium · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:138`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** OnSubjobOk desde `op_125_unsupported_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/tmsis-analytic-file/de_annual_build.sas:138 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 5. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s141` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:141`
- **Conexiones:** OnSubjobOk desde `op_138_set_variable_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 6. Invocar macro %create_pyears

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s152` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:152`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_141_maintenance_1`
- **Propiedades:**
  - `PROCESS` (Job) = `create_pyears` — SAS real/tmsis-analytic-file/de_annual_build.sas:152 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 7. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s157` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:237`
- **Conexiones:** OnSubjobOk desde `op_152_macro_call_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 8. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s244` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:244`
- **Conexiones:** OnSubjobOk desde `op_237_unsupported_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Definición de macro auxiliar `%setENV`()

## Definición de macro auxiliar `%priorids`()

### 1. Invocar macro %max_run_id

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:priorids:s180` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/de_annual_build.sas:180`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `max_run_id` — SAS real/tmsis-analytic-file/de_annual_build.sas:180 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `file=DE, tbl=taf_ann_de_base, inyear=&pyear.` — SAS real/tmsis-analytic-file/de_annual_build.sas:180 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- include &tms_config_macro (real/tmsis-analytic-file/de_annual_build.sas:13) — ruta dinámica
- include &da_config_macro (real/tmsis-analytic-file/de_annual_build.sas:17) — ruta dinámica
- include "/sasdata/users/&sysuserid/&TMSIS/&sub_env/data_analytics/taf/programs/AWS_Shared_Macros.sas" (real/tmsis-analytic-file/de_annual_build.sas:59) — ruta dinámica
- include "&basedir./programs/annual_macros.sas" (real/tmsis-analytic-file/de_annual_build.sas:65) — ruta dinámica
- include "&basedir./programs/001_base.sas" (real/tmsis-analytic-file/de_annual_build.sas:66) — ruta dinámica
- include "&basedir./programs/002_eligibility_dates.sas" (real/tmsis-analytic-file/de_annual_build.sas:67) — ruta dinámica
- include "&basedir./programs/003_address_phone.sas" (real/tmsis-analytic-file/de_annual_build.sas:68) — ruta dinámica
- include "&basedir./programs/005_managed_care.sas" (real/tmsis-analytic-file/de_annual_build.sas:69) — ruta dinámica
- include "&basedir./programs/006_waiver.sas" (real/tmsis-analytic-file/de_annual_build.sas:70) — ruta dinámica
- include "&basedir./programs/007_mfp.sas" (real/tmsis-analytic-file/de_annual_build.sas:71) — ruta dinámica
- include "&basedir./programs/008_hh_spo.sas" (real/tmsis-analytic-file/de_annual_build.sas:72) — ruta dinámica
- include "&basedir./programs/009_disability_need.sas" (real/tmsis-analytic-file/de_annual_build.sas:73) — ruta dinámica
- macro tmsis_connect (real/tmsis-analytic-file/de_annual_build.sas:121) — sin definición en el proyecto
- macro job_control_rd (real/tmsis-analytic-file/de_annual_build.sas:123) — sin definición en el proyecto
- macro job_control_updt (real/tmsis-analytic-file/de_annual_build.sas:127) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/de_annual_build.sas:129) — sin definición en el proyecto
- macro left (real/tmsis-analytic-file/de_annual_build.sas:141) — sin definición en el proyecto
- macro create_pyears (real/tmsis-analytic-file/de_annual_build.sas:152) — sin definición en el proyecto
- macro tmsis_connect (real/tmsis-analytic-file/de_annual_build.sas:158) — sin definición en el proyecto
- macro max_run_id (real/tmsis-analytic-file/de_annual_build.sas:166) — sin definición en el proyecto
- macro max_run_id (real/tmsis-analytic-file/de_annual_build.sas:168) — sin definición en el proyecto
- macro max_run_id (real/tmsis-analytic-file/de_annual_build.sas:169) — sin definición en el proyecto
- macro max_run_id (real/tmsis-analytic-file/de_annual_build.sas:170) — sin definición en el proyecto
- macro max_run_id (real/tmsis-analytic-file/de_annual_build.sas:171) — sin definición en el proyecto
- macro max_run_id (real/tmsis-analytic-file/de_annual_build.sas:180) — sin definición en el proyecto
- macro any_pyear (real/tmsis-analytic-file/de_annual_build.sas:193) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:198) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:202) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:207) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:212) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:217) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:222) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:227) — sin definición en el proyecto
- macro create_segment (real/tmsis-analytic-file/de_annual_build.sas:233) — sin definición en el proyecto
- macro job_control_updt2 (real/tmsis-analytic-file/de_annual_build.sas:238) — sin definición en el proyecto
- macro tmsis_disconnect (real/tmsis-analytic-file/de_annual_build.sas:240) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
