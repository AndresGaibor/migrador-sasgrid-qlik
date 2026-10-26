# Job `job_003_bsf_elg00003`

- **Programa SAS:** `real/tmsis-analytic-file/003_bsf_ELG00003.sas` (sha256 `3dfbcaa32ce1`)
- **Instrucciones:** 5 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.DA_RUN_ID` ← SAS `DA_RUN_ID` (&DA_RUN_ID en real/tmsis-analytic-file/003_bsf_ELG00003.sas:626)
- `context.DA_SCHEMA` ← SAS `DA_SCHEMA` (&DA_SCHEMA en real/tmsis-analytic-file/003_bsf_ELG00003.sas:626)
- `context.tab_no` ← SAS `tab_no` (&tab_no en real/tmsis-analytic-file/003_bsf_ELG00003.sas:629)

## Pasos

## Definición de macro auxiliar `%create_prmry_lang_cd_table`()

## Definición de macro auxiliar `%create_ELG00003`(tab_no, _2x_segment, eff_date, end_date)

### 1. Invocar macro %create_prmry_lang_cd_table

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELG00003:s523` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/003_bsf_ELG00003.sas:523`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `create_prmry_lang_cd_table` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:523 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %create_prmry_lang_cd_table (definida en real/tmsis-analytic-file/003_bsf_ELG00003.sas)

### 2. Invocar macro %multiids

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELG00003:s578` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/003_bsf_ELG00003.sas:578`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ELG00003:op_523_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `multiids` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:578 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `sort_key=%str(coalesce(mrtl_stus_cd,'xx') || coalesce(cast(ssn_num as char(10)),'xx') || coalesce(incm_cd,'xx') ||
                        coalesce(vet_ind,'xx') ||coalesce(ctznshp_ind,'xx') || coalesce(imgrtn_stus_cd,'xx') || 
                        coalesce(upper(prmry_lang_cd),'xx') || coalesce(hsehld_size_cd,'xx') || coalesce(mdcr_hicn_num,'xx') ||
                        coalesce(chip_cd,'xx') || coalesce(ENGLSH_PRFCNCY_CD,'xx')),suffix=,val=_v` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:578 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Invocar macro %get_audt_counts

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELG00003:s626` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/003_bsf_ELG00003.sas:626`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ELG00003:op_578_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `get_audt_counts` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:626 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `&DA_SCHEMA.,&DA_RUN_ID., 003_bsf_ELG00003, 0.1. create_initial_table` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:626 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 4. Invocar macro %get_audt_counts

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELG00003:s627` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/003_bsf_ELG00003.sas:627`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ELG00003:op_626_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `get_audt_counts` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:627 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `&DA_SCHEMA.,&DA_RUN_ID., 003_bsf_ELG00003, 0.2. MultiIds` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:627 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 5. Invocar macro %drop_table_multi

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELG00003:s629` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/003_bsf_ELG00003.sas:629`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ELG00003:op_627_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `drop_table_multi` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:629 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `&tab_no. &tab_no._recCt &tab_no._uniq &tab_no.A &tab_no._multi &tab_no._multi_all &tab_no._multi_step2` — SAS real/tmsis-analytic-file/003_bsf_ELG00003.sas:629 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro multiids (real/tmsis-analytic-file/003_bsf_ELG00003.sas:578) — sin definición en el proyecto
- macro get_audt_counts (real/tmsis-analytic-file/003_bsf_ELG00003.sas:626) — sin definición en el proyecto
- macro get_audt_counts (real/tmsis-analytic-file/003_bsf_ELG00003.sas:627) — sin definición en el proyecto
- macro drop_table_multi (real/tmsis-analytic-file/003_bsf_ELG00003.sas:629) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
