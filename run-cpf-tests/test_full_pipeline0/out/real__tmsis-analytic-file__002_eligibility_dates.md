# Job `job_002_eligibility_dates`

- **Programa SAS:** `real/tmsis-analytic-file/002_eligibility_dates.sas` (sha256 `2b1bfa2c8b50`)
- **Instrucciones:** 4 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.year` ← SAS `year` (&year en real/tmsis-analytic-file/002_eligibility_dates.sas:413)

## Pasos

## Definición de macro auxiliar `%create_ELDTS`()

### 1. Invocar macro %create_temp_table

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELDTS:s23` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/002_eligibility_dates.sas:23`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `create_temp_table` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:23 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `eligibility_dates,
	                subcols=%nrbquote( %monthly_array_eldts(MDCD_ENRLMT_EFF_DT_,nslots=16,truncfirst=1)

					),
	                subcols2=%nrbquote( %monthly_array_eldts(MDCD_ENRLMT_END_DT_,nslots=16,truncfirst=0) 
					),
	                subcols3=%nrbquote( %monthly_array_eldts(CHIP_ENRLMT_EFF_DT_,nslots=16,truncfirst=1)
					),
	                subcols4=%nrbquote( %monthly_array_eldts(CHIP_ENRLMT_END_DT_,nslots=16,truncfirst=0)
					) ` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:23 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %dates

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELDTS:s317` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/002_eligibility_dates.sas:317`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ELDTS:op_23_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `dates` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:317 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `MDCD,1` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:317 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %dates (definida en real/tmsis-analytic-file/002_eligibility_dates.sas)

### 3. Invocar macro %dates

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELDTS:s318` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/002_eligibility_dates.sas:318`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ELDTS:op_317_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `dates` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:318 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CHIP,2` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:318 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %dates (definida en real/tmsis-analytic-file/002_eligibility_dates.sas)

### 4. Invocar macro %drop_tables

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ELDTS:s413` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/002_eligibility_dates.sas:413`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ELDTS:op_318_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `drop_tables` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:413 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `eligibility_dates_&year. MDCD_dates_out CHIP_dates_out MDCD_days_out CHIP_days_out numbers` — SAS real/tmsis-analytic-file/002_eligibility_dates.sas:413 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro create_temp_table (real/tmsis-analytic-file/002_eligibility_dates.sas:23) — sin definición en el proyecto
- macro monthly_array_eldts (real/tmsis-analytic-file/002_eligibility_dates.sas:23) — sin definición en el proyecto
- macro drop_tables (real/tmsis-analytic-file/002_eligibility_dates.sas:312) — sin definición en el proyecto
- macro table_id_cols (real/tmsis-analytic-file/002_eligibility_dates.sas:347) — sin definición en el proyecto
- macro drop_tables (real/tmsis-analytic-file/002_eligibility_dates.sas:413) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
