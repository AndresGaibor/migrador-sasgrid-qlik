# Job `job_run_daily_banking`

- **Programa SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas` (sha256 `5590a44d669e`)
- **Instrucciones:** 8 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%run_daily_banking(run_date, restart_from)` está integrada en el Job.

## Orquestación

- Planificación: Daily 05:45 via Control-M BANK_MASTER
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#1`, `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#2`, `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#3`, `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#4`

### Recomendaciones Grid

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:6` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Daily 05:45 via Control-M BANK_MASTER"
}
```

## Variables de contexto

- `context.batch_id` ← SAS `batch_id` (&batch_id en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146)
- `context.CURR_DT` ← SAS `CURR_DT` (Variable SAS referenciada por %run_daily_banking(run_date=...))
- `context.EMAIL_DL` ← SAS `EMAIL_DL` (&EMAIL_DL en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146)
- `context.job_count` ← SAS `job_count` (&job_count en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146)
- `context.job_fail` ← SAS `job_fail` (&job_fail en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146)
- `context.job_pass` ← SAS `job_pass` (&job_pass en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146)
- `context.restart_from` ← SAS `restart_from` (Parámetro de la macro principal %run_daily_banking; argumento SAS: sin asignar)
- `context.run_date` ← SAS `run_date` (Parámetro de la macro principal %run_daily_banking; argumento SAS: &CURR_DT)
- `context.start_tm` ← SAS `start_tm` (&start_tm en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146)

## Conexiones a crear

- `ARCHIVE` (BASE, /data/sas/archive) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Escribir WORK.BATCH_CONTROL

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:run_daily_banking:s31` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:31`
- **Propiedades:**
  - `TABLE` = `batch_control` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:31
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:31
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:31
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:run_daily_banking:op_31_write_1_row_count`, `vc_m:run_daily_banking:op_31_write_1_schema`

### 2. Invocar macro %run_step

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:run_daily_banking:s121` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:121`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:run_daily_banking:op_31_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `run_step` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:121 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `1, Load Customer Accounts,
    /opt/sas/custom/programs/Banking/load_customer_accounts.sas` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:121 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %run_step (definida en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas)

### 3. Invocar macro %run_step

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:run_daily_banking:s124` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:124`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:run_daily_banking:op_121_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `run_step` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:124 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `2, Daily Transaction Processing,
    /opt/sas/custom/programs/Banking/daily_transaction_processing.sas` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:124 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %run_step (definida en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas)

### 4. Invocar macro %run_step

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:run_daily_banking:s127` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:127`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:run_daily_banking:op_124_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `run_step` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:127 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `3, Credit Risk Scoring,
    /opt/sas/custom/programs/Banking/credit_risk_scoring.sas` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:127 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %run_step (definida en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas)

### 5. Invocar macro %run_step

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:run_daily_banking:s130` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:130`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:run_daily_banking:op_127_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `run_step` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:130 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `4, Monthly Regulatory Reporting,
    /opt/sas/custom/programs/Banking/monthly_regulatory_reporting.sas` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:130 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %run_step (definida en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas)

### 6. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `m:run_daily_banking:s137` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:137`
- **Conexiones:** OnSubjobOk desde `m:run_daily_banking:op_130_macro_call_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 7. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:run_daily_banking:s142` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:142`
- **Conexiones:** OnSubjobOk desde `m:run_daily_banking:op_137_report_1`
- **Propiedades:**
  - `TABLE` = `batch_control` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:142
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:142
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:142
- **Pendientes:**
  - Tabla base destino
  - Librería archive es de tipo BASE en /data/sas/archive: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:run_daily_banking:op_142_append_1_row_count`

### 8. Invocar macro %sendmail

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:run_daily_banking:s146` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:run_daily_banking:op_142_append_1`
- **Propiedades:**
  - `PROCESS` (Job) = `sendmail` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
    to=&EMAIL_DL,
    subject=Batch &batch_id: &job_pass pass / &job_fail fail of &job_count steps,
    body=See ARCHIVE.BATCH_HISTORY for details. Duration: %sysfunc(putn(%sysevalf(%sysfunc(datetime())-&start_tm), time8.))
  ` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- include /opt/sas/config/Lev1/SASApp/autoexec.sas (real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:10) — candidate → real/ts-sas-legacy-analytics/Config/autoexec.sas
- macro sendmail (real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:106) — sin definición en el proyecto
- macro sendmail (real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:146) — sin definición en el proyecto

## Casos de validación

- `vc_m:run_daily_banking:op_31_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:run_daily_banking:op_31_write_1_schema` (schema): Esquema destino
- `vc_m:run_daily_banking:op_142_append_1_row_count` (row_count): Filas añadidas

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
