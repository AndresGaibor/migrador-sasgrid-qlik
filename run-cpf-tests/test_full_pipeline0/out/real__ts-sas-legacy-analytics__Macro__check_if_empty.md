# Job `job_check_if_empty`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Macro/check_if_empty.sas` (sha256 `0ee0d02e06be`)
- **Instrucciones:** 3 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.dataset` ← SAS `dataset` (&dataset en real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:136)

## Pasos

## Definición de macro auxiliar `%check_if_empty`(DATA)

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:check_if_empty:s119` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:119`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:119 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `DATA,         _req=1,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:119 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:check_if_empty:s136` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:136`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:check_if_empty:op_119_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:136 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `_msg=&dataset does not exist` — SAS real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:136 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:check_if_empty:s142` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:142`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:check_if_empty:op_136_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:142 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `_msg=Unable to open &dataset for input` — SAS real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:142 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro parmv (real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:119) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:136) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:142) — sin definición en el proyecto
- macro quit (real/ts-sas-legacy-analytics/Macro/check_if_empty.sas:147) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
