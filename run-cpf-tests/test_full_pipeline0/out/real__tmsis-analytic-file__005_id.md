# Job `job_005_id`

- **Programa SAS:** `real/tmsis-analytic-file/005_id.sas` (sha256 `82a5afaa25be`)
- **Instrucciones:** 2 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.year` ← SAS `year` (&year en real/tmsis-analytic-file/005_id.sas:24)

## Pasos

## Definición de macro auxiliar `%create_ID`()

### 1. Invocar macro %annual_segment

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ID:s24` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/005_id.sas:24`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `annual_segment` — SAS real/tmsis-analytic-file/005_id.sas:24 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `fileseg=IDT, dtfile=PRV, collist=collist_s, mnths=PRVDR_ID_FLAG, outtbl=id_pr_&year.` — SAS real/tmsis-analytic-file/005_id.sas:24 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %create_splmlt

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_ID:s73` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/005_id.sas:73`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_ID:op_24_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `create_splmlt` — SAS real/tmsis-analytic-file/005_id.sas:73 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `segname=ID, segfile=id_pr_&year.` — SAS real/tmsis-analytic-file/005_id.sas:73 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro annual_segment (real/tmsis-analytic-file/005_id.sas:24) — sin definición en el proyecto
- macro create_splmlt (real/tmsis-analytic-file/005_id.sas:73) — sin definición en el proyecto
- macro table_id_cols (real/tmsis-analytic-file/005_id.sas:98) — sin definición en el proyecto
- macro drop_tables (real/tmsis-analytic-file/005_id.sas:112) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
