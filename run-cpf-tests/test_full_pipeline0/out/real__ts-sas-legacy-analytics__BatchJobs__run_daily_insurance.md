# Job `job_run_daily_insurance`

- **Programa SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas` (sha256 `10f0cdc5b697`)
- **Instrucciones:** 5 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%run_daily_insurance(run_date, restart_from)` está integrada en el Job.

## Orquestación

- Planificación: Daily 07:00 via Control-M INS_MASTER
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas#1`, `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas#2`

### Recomendaciones Grid

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:4` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Daily 07:00 via Control-M INS_MASTER"
}
```

## Variables de contexto

- `context.CURR_DT` ← SAS `CURR_DT` (Variable SAS referenciada por %run_daily_insurance(run_date=...))
- `context.restart_from` ← SAS `restart_from` (Parámetro de la macro principal %run_daily_insurance; argumento SAS: sin asignar)
- `context.run_date` ← SAS `run_date` (Parámetro de la macro principal %run_daily_insurance; argumento SAS: &CURR_DT)

## Conexiones a crear

- `ARCHIVE` (BASE, /data/sas/archive) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Escribir WORK.BATCH_CONTROL

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:run_daily_insurance:s27` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:27`
- **Propiedades:**
  - `TABLE` = `batch_control` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:27
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:27
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:27
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:run_daily_insurance:op_27_write_1_row_count`, `vc_m:run_daily_insurance:op_27_write_1_schema`

### 2. Invocar macro %run_step

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:run_daily_insurance:s109` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:109`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:run_daily_insurance:op_27_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `run_step` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:109 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `1, Claims Processing,
    /opt/sas/custom/programs/Insurance/claims_processing.sas` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:109 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %run_step (definida en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas)

### 3. Invocar macro %run_step

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:run_daily_insurance:s112` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:112`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:run_daily_insurance:op_109_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `run_step` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:112 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `2, Policy Valuation,
    /opt/sas/custom/programs/Insurance/policy_valuation.sas` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:112 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %run_step (definida en real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas)

### 4. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `m:run_daily_insurance:s117` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:117`
- **Conexiones:** OnSubjobOk desde `m:run_daily_insurance:op_112_macro_call_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 5. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:run_daily_insurance:s121` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:121`
- **Conexiones:** OnSubjobOk desde `m:run_daily_insurance:op_117_report_1`
- **Propiedades:**
  - `TABLE` = `batch_control` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:121
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:121
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:121
- **Pendientes:**
  - Tabla base destino
  - Librería archive es de tipo BASE en /data/sas/archive: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:run_daily_insurance:op_121_append_1_row_count`

## Sin resolver

- include /opt/sas/config/Lev1/SASApp/autoexec.sas (real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:8) — candidate → real/ts-sas-legacy-analytics/Config/autoexec.sas
- macro sendmail (real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:96) — sin definición en el proyecto

## Casos de validación

- `vc_m:run_daily_insurance:op_27_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:run_daily_insurance:op_27_write_1_schema` (schema): Esquema destino
- `vc_m:run_daily_insurance:op_121_append_1_row_count` (row_count): Filas añadidas

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
