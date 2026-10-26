# Job `job_daily_transaction_processing`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas` (sha256 `872c0d44f0d7`)
- **Instrucciones:** 34 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%daily_transaction_processing(txn_date)` está integrada en el Job.

## Orquestación

- Planificación: Daily 07:30 via Control-M job BANK_DAILY_02
- Depende de (datos): `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas`
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#2`

### Recomendaciones Grid

### `sas_macro_step.include_dispatch` (partial)

- **Accion:** Crea un Job hijo para cada programa resuelto y confirma sus parámetros antes de conectar la secuencia.
- **Motivo/limite:** The analyzer resolves tested macro dispatches, but macro defaults and failure behavior require review.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:124` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#1`
- **Confirmar:** Review macro dispatch semantics; Confirm child Job and context parameters
- **Datos interpretados:**

```json
{
  "kind": "sas_macro_step",
  "program": "/opt/sas/custom/programs/Banking/daily_transaction_processing.sas",
  "resolved_program": "real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas",
  "match_status": "resolved",
  "job_name": null,
  "queue": null,
  "waits": true,
  "params": {
    "step_num": "2",
    "step_name": "Daily Transaction Processing",
    "program": "/opt/sas/custom/programs/Banking/daily_transaction_processing.sas"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:10` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Daily 07:30 via Control-M job BANK_DAILY_02"
}
```

## Variables de contexto

- `context.CURR_DT` ← SAS `CURR_DT` (Variable SAS referenciada por %daily_transaction_processing(txn_date=...))
- `context.txn_date` ← SAS `txn_date` (Parámetro de la macro principal %daily_transaction_processing; argumento SAS: &CURR_DT)
- `context.txn_ds` ← SAS `txn_ds` (&txn_ds en real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45)

## Conexiones a crear

- `CURATED` (BASE, /data/sas/curated) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `STG_BANK` (BASE, /data/sas/staging/banking) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:daily_transaction_processing:s21` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:21`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:21 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `txn_date, _req=1` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:21 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Leer RAW_BANK.&txn_ds

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s45` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_21_macro_call_1`
- **Propiedades:**
  - `TABLE` = `&txn_ds` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:daily_transaction_processing:op_45_read_1_row_count`, `vc_m:daily_transaction_processing:op_45_read_1_schema`

### 3. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:daily_transaction_processing:s45` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_45_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `6 asignaciones, 6 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `REJECT_REASON` _(tipos por determinar)_
- **Expresión** (línea 54): SAS `'Missing TRANSACTION_ID'` → Java `"Missing TRANSACTION_ID"`
- **Expresión** (línea 60): SAS `'Missing ACCOUNT_ID'` → Java `"Missing ACCOUNT_ID"`
- **Expresión** (línea 66): SAS `'Missing TRANSACTION_AMOUNT'` → Java `"Missing TRANSACTION_AMOUNT"`
- **Expresión** (línea 73): SAS `catx(' ', 'Amount exceeds threshold:',
        put(TRANSACTION_AMOUNT, dollar18.2))` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.2))'
- **Expresión** (línea 82): SAS `catx(' ', 'Invalid transaction type:', TRANSACTION_TYPE)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función catx
- **Expresión** (línea 89): SAS `catx(' ', 'Future dated:',
        put(TRANSACTION_DATE, date9.))` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.))'
- **Expresión** (línea 53): SAS `if missing(TRANSACTION_ID) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 59): SAS `if missing(ACCOUNT_ID) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 65): SAS `if missing(TRANSACTION_AMOUNT) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 72): SAS `if abs(TRANSACTION_AMOUNT) > 10000000 then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 80): SAS `if TRANSACTION_TYPE not in ('DEP','WDR','TRF','PMT','FEE','INT','ADJ','REV','CHG','REF')
    then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 88): SAS `if TRANSACTION_DATE > "&txn_date"d then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:daily_transaction_processing:op_45_compute_1_nulls`, `vc_m:daily_transaction_processing:op_45_compute_1_dates`, `vc_m:daily_transaction_processing:op_45_compute_1_numeric`

### 4. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:daily_transaction_processing:s45` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_45_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: REJECT_REASON` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45 · nombre oficial
- **Pruebas:** `vc_m:daily_transaction_processing:op_45_select_columns_1_schema`

### 5. Escribir WORK.TXN_VALIDATED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s45` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_45_select_columns_1`
- **Propiedades:**
  - `TABLE` = `txn_validated` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:daily_transaction_processing:op_45_write_1_row_count`, `vc_m:daily_transaction_processing:op_45_write_1_schema`

### 6. Escribir WORK.TXN_REJECTED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s45` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_45_write_1`
- **Propiedades:**
  - `TABLE` = `txn_rejected` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:daily_transaction_processing:op_45_write_2_row_count`, `vc_m:daily_transaction_processing:op_45_write_2_schema`

### 7. Leer WORK.TXN_VALIDATED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s105` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_45_write_2`
- **Propiedades:**
  - `TABLE` = `txn_validated` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:daily_transaction_processing:op_45_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:daily_transaction_processing:op_106_read_1_row_count`, `vc_m:daily_transaction_processing:op_106_read_1_schema`

### 8. Leer STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s105` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:daily_transaction_processing:op_106_read_2_row_count`, `vc_m:daily_transaction_processing:op_106_read_2_schema`

### 9. Unir (left join): work.txn_validated, stg_bank.cust_accounts_daily

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:daily_transaction_processing:s105` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_106_read_1`, Lookup desde `m:daily_transaction_processing:op_106_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `t.ACCOUNT_ID = a.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 106): SAS `on t.ACCOUNT_ID = a.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:daily_transaction_processing:op_106_join_1_duplicates`, `vc_m:daily_transaction_processing:op_106_join_1_row_count`, `vc_m:daily_transaction_processing:op_106_join_1_nulls`

### 10. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:daily_transaction_processing:s105` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_106_join_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*, ACCOUNT_TYPE, CUSTOMER_ID, CUSTOMER_SEGMENT, REGION_CODE, BRANCH_ID, PRE_TXN_BALANCE, case when t.TRANSACTION_TYPE in ('DEP','INT','REF','REV') then a.CURRENT_BALANCE + t.TRANSACTION_AMOUNT when t.TRANSACTION_TYPE in ('WDR','PMT','FEE','CHG') then a.CURRENT_BALANCE - abs(t.TRANSACTION_AMOUNT) when t.TRANSACTION_TYPE in ('TRF','ADJ') then a.CURRENT_BALANCE + t.TRANSACTION_AMOUNT else a.CURRENT_BALANCE end as POST_TXN_BALANCE format=dollar18.2, RISK_RATING` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ACCOUNT_TYPE`, `CUSTOMER_ID`, `CUSTOMER_SEGMENT`, `REGION_CODE`, `BRANCH_ID`, `PRE_TXN_BALANCE`, `RISK_RATING` _(tipos por determinar)_
- **Expresión** (línea 106): SAS `case when t.TRANSACTION_TYPE in ('DEP','INT','REF','REV') then a.CURRENT_BALANCE + t.TRANSACTION_AMOUNT when t.TRANSACTION_TYPE in ('WDR','PMT','FEE','CHG') then a.CURRENT_BALANCE - abs(t.TRANSACTION_AMOUNT) when t.TRANSACTION_TYPE in ('TRF','ADJ') then a.CURRENT_BALANCE + t.TRANSACTION_AMOUNT else a.CURRENT_BALANCE end as POST_TXN_BALANCE format=dollar18.2` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.2'
- **Pruebas:** `vc_m:daily_transaction_processing:op_106_project_1_schema`

### 11. Ordenar por t.ACCOUNT_ID, t.TRANSACTION_DATE, t.TRANSACTION_ID

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:daily_transaction_processing:s105` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_106_project_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `t.ACCOUNT_ID, t.TRANSACTION_DATE, t.TRANSACTION_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106 · nombre oficial
- **Esquema:** `ACCOUNT_ID`, `TRANSACTION_DATE`, `TRANSACTION_ID` _(tipos por determinar)_
- **Pruebas:** `vc_m:daily_transaction_processing:op_106_sort_1_ordering`

### 12. Escribir WORK.TXN_ENRICHED (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s105` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_106_sort_1`
- **Propiedades:**
  - `TABLE` = `txn_enriched` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:106
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:daily_transaction_processing:op_106_write_1_row_count`, `vc_m:daily_transaction_processing:op_106_write_1_schema`

### 13. Leer WORK.TXN_ENRICHED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s137` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_106_write_1`
- **Propiedades:**
  - `TABLE` = `txn_enriched` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:daily_transaction_processing:op_106_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:daily_transaction_processing:op_137_read_1_row_count`, `vc_m:daily_transaction_processing:op_137_read_1_schema`

### 14. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:daily_transaction_processing:s137` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_137_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 4 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 143): SAS `if first.ACCOUNT_ID then
      RUNNING_BALANCE = PRE_TXN_BALANCE` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 146): SAS `if TRANSACTION_TYPE in ('DEP','INT','REF','REV') then
      RUNNING_BALANCE = RUNNING_BALANCE + TRANSACTION_AMOUNT` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 148): SAS `else if TRANSACTION_TYPE in ('WDR','PMT','FEE','CHG') then
      RUNNING_BALANCE = RUNNING_BALANCE - abs(TRANSACTION_AMOUNT)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 150): SAS `else if TRANSACTION_TYPE in ('TRF','ADJ') then
      RUNNING_BALANCE = RUNNING_BALANCE + TRANSACTION_AMOUNT` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:daily_transaction_processing:op_137_compute_1_nulls`, `vc_m:daily_transaction_processing:op_137_compute_1_dates`, `vc_m:daily_transaction_processing:op_137_compute_1_numeric`

### 15. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `m:daily_transaction_processing:s137` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_137_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_m:daily_transaction_processing:op_137_stateful_1_ordering`, `vc_m:daily_transaction_processing:op_137_stateful_1_duplicates`

### 16. Escribir WORK.TXN_WITH_BALANCE

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s137` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_137_stateful_1`
- **Propiedades:**
  - `TABLE` = `txn_with_balance` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:137
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:daily_transaction_processing:op_137_write_1_row_count`, `vc_m:daily_transaction_processing:op_137_write_1_schema`

### 17. Leer CURATED.DAILY_TRANSACTIONS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s159` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_137_write_1`
- **Propiedades:**
  - `TABLE` = `daily_transactions` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:daily_transaction_processing:op_160_read_1_row_count`, `vc_m:daily_transaction_processing:op_160_read_1_schema`

### 18. Filtrar filas (WHERE): TRANSACTION_DATE >= intnx('day', "&txn_date"d, -90)

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:daily_transaction_processing:s159` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_160_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 160): SAS `TRANSACTION_DATE >= intnx('day', "&txn_date"d, -90)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intnx
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:daily_transaction_processing:op_160_filter_1_row_count`, `vc_m:daily_transaction_processing:op_160_filter_1_nulls`, `vc_m:daily_transaction_processing:op_160_filter_1_empty`

### 19. Agregar por ACCOUNT_ID

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:daily_transaction_processing:s159` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_160_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160 · nombre oficial
  - `OPERATIONS` (Operations) = `AVG_TXN_AMT = mean(abs(TRANSACTION_AMOUNT)); TXN_COUNT = count(*)` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160 · nombre oficial
- **Esquema:** `ACCOUNT_ID`, `AVG_TXN_AMT`, `STD_TXN_AMT`, `TXN_COUNT` _(tipos por determinar)_
- **Pruebas:** `vc_m:daily_transaction_processing:op_160_aggregate_1_aggregates`, `vc_m:daily_transaction_processing:op_160_aggregate_1_numeric`

### 20. Escribir WORK.TXN_STATS (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s159` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_160_aggregate_1`
- **Propiedades:**
  - `TABLE` = `txn_stats` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:160
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:daily_transaction_processing:op_160_write_1_row_count`, `vc_m:daily_transaction_processing:op_160_write_1_schema`

### 21. Leer WORK.TXN_WITH_BALANCE

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s172` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_160_write_1`
- **Propiedades:**
  - `TABLE` = `txn_with_balance` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:daily_transaction_processing:op_137_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:daily_transaction_processing:op_173_read_1_row_count`, `vc_m:daily_transaction_processing:op_173_read_1_schema`

### 22. Leer WORK.TXN_STATS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s172` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173`
- **Propiedades:**
  - `TABLE` = `txn_stats` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:daily_transaction_processing:op_160_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:daily_transaction_processing:op_173_read_2_row_count`, `vc_m:daily_transaction_processing:op_173_read_2_schema`

### 23. Unir (left join): work.txn_with_balance, work.txn_stats

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:daily_transaction_processing:s172` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_173_read_1`, Lookup desde `m:daily_transaction_processing:op_173_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `e.ACCOUNT_ID = s.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 173): SAS `on e.ACCOUNT_ID = s.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:daily_transaction_processing:op_173_join_1_duplicates`, `vc_m:daily_transaction_processing:op_173_join_1_row_count`, `vc_m:daily_transaction_processing:op_173_join_1_nulls`

### 24. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:daily_transaction_processing:s172` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_173_join_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*, AVG_TXN_AMT, STD_TXN_AMT, Z_SCORE, case when calculated Z_SCORE > 3 then 'HIGH_AMOUNT' when e.RUNNING_BALANCE < 0 then 'OVERDRAFT' when e.TRANSACTION_TYPE = 'WDR' and abs(e.TRANSACTION_AMOUNT) > e.PRE_TXN_BALANCE * 0.9 then 'LARGE_WITHDRAWAL' when missing(e.CUSTOMER_ID) then 'ORPHAN_ACCOUNT' else '' end as ANOMALY_TYPE length=20` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `AVG_TXN_AMT`, `STD_TXN_AMT`, `Z_SCORE` _(tipos por determinar)_
- **Expresión** (línea 173): SAS `case when s.STD_TXN_AMT > 0 then (abs(e.TRANSACTION_AMOUNT) - s.AVG_TXN_AMT) / s.STD_TXN_AMT else . end` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ' . end'
- **Expresión** (línea 173): SAS `case when calculated Z_SCORE > 3 then 'HIGH_AMOUNT' when e.RUNNING_BALANCE < 0 then 'OVERDRAFT' when e.TRANSACTION_TYPE = 'WDR' and abs(e.TRANSACTION_AMOUNT) > e.PRE_TXN_BALANCE * 0.9 then 'LARGE_WITHDRAWAL' when missing(e.CUSTOMER_ID) then 'ORPHAN_ACCOUNT' else '' end as ANOMALY_TYPE length=20` → _sin traducción automática_
  - ⚠ Construcción SAS sin traducción automática
- **Pruebas:** `vc_m:daily_transaction_processing:op_173_project_1_schema`

### 25. Filtrar filas (HAVING): ANOMALY_TYPE ne ''

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:daily_transaction_processing:s172` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_173_project_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `ANOMALY_TYPE != ''` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `ANOMALY_TYPE` _(tipos por determinar)_
- **Expresión** (línea 173): SAS `ANOMALY_TYPE ne ''` → Java `!input_row.ANOMALY_TYPE.equals("")`
  - ⚠ Missing numérico: en SAS es menor que cualquier número; en Java un null no compara igual
- **Pruebas:** `vc_m:daily_transaction_processing:op_173_filter_1_row_count`, `vc_m:daily_transaction_processing:op_173_filter_1_nulls`, `vc_m:daily_transaction_processing:op_173_filter_1_empty`

### 26. Escribir WORK.TXN_ANOMALIES (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s172` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_173_filter_1`
- **Propiedades:**
  - `TABLE` = `txn_anomalies` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:173
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:daily_transaction_processing:op_173_write_1_row_count`, `vc_m:daily_transaction_processing:op_173_write_1_schema`

### 27. Invocar macro %lock

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:daily_transaction_processing:s205` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:205`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_173_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `lock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:205 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CURATED.DAILY_TRANSACTIONS` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:205 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 28. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s207` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:207`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_205_macro_call_1`
- **Propiedades:**
  - `TABLE` = `txn_with_balance` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:207
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:207
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:207
- **Pendientes:**
  - Tabla base destino
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:daily_transaction_processing:op_207_append_1_row_count`

### 29. Invocar macro %lock

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:daily_transaction_processing:s211` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:211`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_207_append_1`
- **Propiedades:**
  - `PROCESS` (Job) = `lock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:211 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CURATED.DAILY_TRANSACTIONS, unlock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:211 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 30. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s214` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:214`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_211_macro_call_1`
- **Propiedades:**
  - `TABLE` = `txn_anomalies` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:214
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:214
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:214
- **Pendientes:**
  - Tabla base destino
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:daily_transaction_processing:op_214_append_1_row_count`

### 31. Leer WORK.TXN_WITH_BALANCE

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:daily_transaction_processing:s222` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222`
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_214_append_1`
- **Propiedades:**
  - `TABLE` = `txn_with_balance` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:daily_transaction_processing:op_137_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:daily_transaction_processing:op_222_read_1_row_count`, `vc_m:daily_transaction_processing:op_222_read_1_schema`

### 32. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:daily_transaction_processing:s222` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:daily_transaction_processing:op_222_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: ACCOUNT_ID, TRANSACTION_DATE, TRANSACTION_ID, RUNNING_BALANCE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222 · nombre oficial
- **Esquema:** `ACCOUNT_ID`, `TRANSACTION_DATE`, `TRANSACTION_ID`, `RUNNING_BALANCE` _(tipos por determinar)_
- **Pruebas:** `vc_m:daily_transaction_processing:op_222_select_columns_1_schema`

### 33. Escribir CURATED.RUNNING_BALANCES

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:daily_transaction_processing:s222` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222`
- **Conexiones:** Main desde `m:daily_transaction_processing:op_222_select_columns_1`
- **Propiedades:**
  - `TABLE` = `running_balances` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:222
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:daily_transaction_processing:op_222_write_1_row_count`, `vc_m:daily_transaction_processing:op_222_write_1_schema`

### 34. Invocar macro %exit

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:daily_transaction_processing:s238` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:238`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:daily_transaction_processing:op_222_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `exit` — SAS real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:238 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- include /opt/sas/custom/macros/parmv.sas (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:15) — external
- include /opt/sas/custom/macros/nobs.sas (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:16) — external
- include /opt/sas/custom/macros/lock.sas (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:17) — external
- dataset_dynamic RAW_BANK.&txn_ds (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:45) — nombre de dataset con macrovariables
- macro parmv (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:21) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:42) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:99) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:199) — sin definición en el proyecto
- macro lock (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:205) — sin definición en el proyecto
- macro lock (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:211) — sin definición en el proyecto
- macro exit (real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas:238) — sin definición en el proyecto

## Casos de validación

- `vc_m:daily_transaction_processing:op_45_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_45_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_45_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:daily_transaction_processing:op_45_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:daily_transaction_processing:op_45_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:daily_transaction_processing:op_45_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:daily_transaction_processing:op_45_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:daily_transaction_processing:op_45_write_1_schema` (schema): Esquema destino
- `vc_m:daily_transaction_processing:op_45_write_2_row_count` (row_count): Filas escritas iguales
- `vc_m:daily_transaction_processing:op_45_write_2_schema` (schema): Esquema destino
- `vc_m:daily_transaction_processing:op_106_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_106_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_106_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_106_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_106_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:daily_transaction_processing:op_106_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:daily_transaction_processing:op_106_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:daily_transaction_processing:op_106_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:daily_transaction_processing:op_106_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:daily_transaction_processing:op_106_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:daily_transaction_processing:op_106_write_1_schema` (schema): Esquema destino
- `vc_m:daily_transaction_processing:op_137_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_137_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_137_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:daily_transaction_processing:op_137_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:daily_transaction_processing:op_137_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:daily_transaction_processing:op_137_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_m:daily_transaction_processing:op_137_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_m:daily_transaction_processing:op_137_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:daily_transaction_processing:op_137_write_1_schema` (schema): Esquema destino
- `vc_m:daily_transaction_processing:op_160_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_160_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_160_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:daily_transaction_processing:op_160_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:daily_transaction_processing:op_160_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:daily_transaction_processing:op_160_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:daily_transaction_processing:op_160_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:daily_transaction_processing:op_160_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:daily_transaction_processing:op_160_write_1_schema` (schema): Esquema destino
- `vc_m:daily_transaction_processing:op_173_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_173_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_173_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_173_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_173_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:daily_transaction_processing:op_173_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:daily_transaction_processing:op_173_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:daily_transaction_processing:op_173_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:daily_transaction_processing:op_173_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:daily_transaction_processing:op_173_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:daily_transaction_processing:op_173_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:daily_transaction_processing:op_173_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:daily_transaction_processing:op_173_write_1_schema` (schema): Esquema destino
- `vc_m:daily_transaction_processing:op_207_append_1_row_count` (row_count): Filas añadidas
- `vc_m:daily_transaction_processing:op_214_append_1_row_count` (row_count): Filas añadidas
- `vc_m:daily_transaction_processing:op_222_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:daily_transaction_processing:op_222_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:daily_transaction_processing:op_222_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:daily_transaction_processing:op_222_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:daily_transaction_processing:op_222_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
