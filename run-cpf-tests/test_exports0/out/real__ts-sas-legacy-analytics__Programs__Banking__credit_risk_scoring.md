# Job `job_credit_risk_scoring`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas` (sha256 `63efb866c88f`)
- **Instrucciones:** 30 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%credit_risk_scoring(score_date, model_id)` está integrada en el Job.

## Orquestación

- Planificación: Weekly Sunday 02:00 via Control-M BANK_WEEKLY_01
- Depende de (datos): `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas`
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#3`

### Recomendaciones Grid

### `sas_macro_step.include_dispatch` (partial)

- **Accion:** Crea un Job hijo para cada programa resuelto y confirma sus parámetros antes de conectar la secuencia.
- **Motivo/limite:** The analyzer resolves tested macro dispatches, but macro defaults and failure behavior require review.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:127` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#2`
- **Confirmar:** Review macro dispatch semantics; Confirm child Job and context parameters
- **Datos interpretados:**

```json
{
  "kind": "sas_macro_step",
  "program": "/opt/sas/custom/programs/Banking/credit_risk_scoring.sas",
  "resolved_program": "real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas",
  "match_status": "resolved",
  "job_name": null,
  "queue": null,
  "waits": true,
  "params": {
    "step_num": "3",
    "step_name": "Credit Risk Scoring",
    "program": "/opt/sas/custom/programs/Banking/credit_risk_scoring.sas"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:11` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Weekly Sunday 02:00 via Control-M BANK_WEEKLY_01"
}
```

## Variables de contexto

- `context.CURR_DT` ← SAS `CURR_DT` (Variable SAS referenciada por %credit_risk_scoring(score_date=...))
- `context.model_id` ← SAS `model_id` (Parámetro de la macro principal %credit_risk_scoring; argumento SAS: sin asignar)
- `context.score_date` ← SAS `score_date` (&score_date en real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203)

## Conexiones a crear

- `CURATED` (BASE, /data/sas/curated) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `ORA_DW` (oracle, FINPROD) → tOracleConnection. Crear la conexión en Talend; no se copian credenciales
- `STG_BANK` (BASE, /data/sas/staging/banking) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:credit_risk_scoring:s20` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:20`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:20 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `score_date, _req=1` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:20 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:credit_risk_scoring:s21` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:21`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_20_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:21 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `model_id, _req=1` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:21 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Leer STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_21_macro_call_1`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_read_1_row_count`, `vc_m:credit_risk_scoring:op_33_read_1_schema`

### 4. Leer ORA_DW.BUREAU_SCORES

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `bureau_scores` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_read_2_row_count`, `vc_m:credit_risk_scoring:op_33_read_2_schema`

### 5. Leer ORA_DW.PAYMENT_HISTORY

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `payment_history` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_read_3_row_count`, `vc_m:credit_risk_scoring:op_33_read_3_schema`

### 6. Leer ORA_DW.COLLATERAL

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `collateral` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_read_4_row_count`, `vc_m:credit_risk_scoring:op_33_read_4_schema`

### 7. Unir (left join): stg_bank.cust_accounts_daily, ora_dw.bureau_scores, ora_dw.payment_history, ora_dw.collateral

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_33_read_1`, Lookup desde `m:credit_risk_scoring:op_33_read_2`, Lookup desde `m:credit_risk_scoring:op_33_read_3`, Lookup desde `m:credit_risk_scoring:op_33_read_4`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.CUSTOMER_ID = b.CUSTOMER_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
- **Esquema:** `CUSTOMER_ID` _(tipos por determinar)_
- **Expresión** (línea 33): SAS `on a.CUSTOMER_ID = b.CUSTOMER_ID and b.SCORE_DATE = (select max(SCORE_DATE) from ORA_DW.BUREAU_SCORES where CUSTOMER_ID = b.CUSTOMER_ID and SCORE_DATE <= "&score_date"d)` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_join_1_duplicates`, `vc_m:credit_risk_scoring:op_33_join_1_row_count`, `vc_m:credit_risk_scoring:op_33_join_1_nulls`

### 8. Unir (left join): stg_bank.cust_accounts_daily, ora_dw.bureau_scores, ora_dw.payment_history, ora_dw.collateral

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_33_join_1`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.ACCOUNT_ID = p.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 33): SAS `on a.ACCOUNT_ID = p.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_join_2_duplicates`, `vc_m:credit_risk_scoring:op_33_join_2_row_count`, `vc_m:credit_risk_scoring:op_33_join_2_nulls`

### 9. Unir (left join): stg_bank.cust_accounts_daily, ora_dw.bureau_scores, ora_dw.payment_history, ora_dw.collateral

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_33_join_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.ACCOUNT_ID = c.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 33): SAS `on a.ACCOUNT_ID = c.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_join_3_duplicates`, `vc_m:credit_risk_scoring:op_33_join_3_row_count`, `vc_m:credit_risk_scoring:op_33_join_3_nulls`

### 10. Filtrar filas (WHERE): a.SNAPSHOT_DATE = "&score_date"d and a.ACCOUNT_TYPE in ('MTG','AUTO','PERS','CC'

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_33_join_3`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 33): SAS `a.SNAPSHOT_DATE = "&score_date"d and a.ACCOUNT_TYPE in ('MTG','AUTO','PERS','CC','LOC','HELC')` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_filter_1_row_count`, `vc_m:credit_risk_scoring:op_33_filter_1_nulls`, `vc_m:credit_risk_scoring:op_33_filter_1_empty`

### 11. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_33_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `ACCOUNT_ID, CUSTOMER_ID, ACCOUNT_TYPE, CURRENT_BALANCE, CREDIT_LIMIT, ACCT_AGE_MONTHS, DAYS_INACTIVE, UTILIZATION_PCT, CUSTOMER_SEGMENT, REGION_CODE, FICO_SCORE, VANTAGE_SCORE, BUREAU_INQS_6MO, BUREAU_TRADES_OPEN, BUREAU_DEROGS, BUREAU_UTIL_PCT, BUREAU_OLDEST_TRADE_MO, PMT_ONTIME_12MO, PMT_LATE_30_12MO, PMT_LATE_60_12MO, PMT_LATE_90_12MO, MAX_DAYS_PAST_DUE_EVER, MONTHS_SINCE_LAST_DPD, AVG_PMT_RATIO_12MO, COLLATERAL_VALUE, LAST_APPRAISAL_DATE, case when c.COLLATERAL_VALUE > 0 then a.CURRENT_BALANCE / c.COLLATERAL_VALUE else . end as LTV format=8.4` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ACCOUNT_ID`, `CUSTOMER_ID`, `ACCOUNT_TYPE`, `CURRENT_BALANCE`, `CREDIT_LIMIT`, `ACCT_AGE_MONTHS`, `DAYS_INACTIVE`, `UTILIZATION_PCT`, `CUSTOMER_SEGMENT`, `REGION_CODE`, `FICO_SCORE`, `VANTAGE_SCORE`, `BUREAU_INQS_6MO`, `BUREAU_TRADES_OPEN`, `BUREAU_DEROGS`, `BUREAU_UTIL_PCT`, `BUREAU_OLDEST_TRADE_MO`, `PMT_ONTIME_12MO`, `PMT_LATE_30_12MO`, `PMT_LATE_60_12MO`, `PMT_LATE_90_12MO`, `MAX_DAYS_PAST_DUE_EVER`, `MONTHS_SINCE_LAST_DPD`, `AVG_PMT_RATIO_12MO`, `COLLATERAL_VALUE`, `LAST_APPRAISAL_DATE` _(tipos por determinar)_
- **Expresión** (línea 33): SAS `case when c.COLLATERAL_VALUE > 0 then a.CURRENT_BALANCE / c.COLLATERAL_VALUE else . end as LTV format=8.4` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ' . end as LT'
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_project_1_schema`

### 12. Escribir WORK.SCORE_INPUT (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:credit_risk_scoring:s32` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33`
- **Conexiones:** Main desde `m:credit_risk_scoring:op_33_project_1`
- **Propiedades:**
  - `TABLE` = `score_input` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:33
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:credit_risk_scoring:op_33_write_1_row_count`, `vc_m:credit_risk_scoring:op_33_write_1_schema`

### 13. Leer WORK.SCORE_INPUT

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:credit_risk_scoring:s92` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92`
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_33_write_1`
- **Propiedades:**
  - `TABLE` = `score_input` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:credit_risk_scoring:op_33_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:credit_risk_scoring:op_92_read_1_row_count`, `vc_m:credit_risk_scoring:op_92_read_1_schema`

### 14. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:credit_risk_scoring:s92` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_92_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `7 asignaciones, 49 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `INTERCEPT`, `WOE_AGE`, `WOE_DPD`, `WOE_FICO`, `WOE_LTV`, `WOE_UTIL`, `LOG_ODDS`, `PD`, `EAD`, `LGD`, `EXPECTED_LOSS`, `SCORE_DATE`, `MODEL_ID`, `SCORE_TIMESTAMP` _(tipos por determinar)_
- **Expresión** (línea 96): SAS `-3.2145` → Java `-3.2145`
- **Expresión** (línea 150): SAS `INTERCEPT
      + 0.412 * WOE_FICO
      + 0.198 * WOE_UTIL
      + 0.289 * WOE_DPD
      + 0.067 * WOE_AGE
      + 0.134 * WOE_LTV` → Java `(((((input_row.INTERCEPT + (0.412 * input_row.WOE_FICO)) + (0.198 * input_row.WOE_UTIL)) + (0.289 * input_row.WOE_DPD)) + (0.067 * input_row.WOE_AGE)) + (0.134 * input_row.WOE_LTV))`
- **Expresión** (línea 157): SAS `1 / (1 + exp(-LOG_ODDS))` → _sin traducción automática_
  - ⚠ Sin traducción automática: función exp
- **Expresión** (línea 179): SAS `PD * LGD * EAD` → Java `((input_row.PD * input_row.LGD) * input_row.EAD)`
- **Expresión** (línea 191): SAS `"&score_date"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Expresión** (línea 192): SAS `"&model_id"` → Java `"&model_id"`
- **Expresión** (línea 193): SAS `datetime()` → _sin traducción automática_
  - ⚠ Sin traducción automática: función datetime
- **Expresión** (línea 99): SAS `if not missing(FICO_SCORE) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 100): SAS `if FICO_SCORE >= 760      then WOE_FICO = -1.204` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 101): SAS `else if FICO_SCORE >= 720 then WOE_FICO = -0.812` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 102): SAS `else if FICO_SCORE >= 680 then WOE_FICO = -0.356` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 103): SAS `else if FICO_SCORE >= 640 then WOE_FICO =  0.198` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 104): SAS `else if FICO_SCORE >= 600 then WOE_FICO =  0.654` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 105): SAS `else WOE_FICO = 1.102` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 107): SAS `else WOE_FICO = 0.198` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 110): SAS `if not missing(UTILIZATION_PCT) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 111): SAS `if UTILIZATION_PCT <= 10      then WOE_UTIL = -0.956` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 112): SAS `else if UTILIZATION_PCT <= 30 then WOE_UTIL = -0.521` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 113): SAS `else if UTILIZATION_PCT <= 50 then WOE_UTIL = -0.102` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 114): SAS `else if UTILIZATION_PCT <= 70 then WOE_UTIL =  0.334` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 115): SAS `else if UTILIZATION_PCT <= 90 then WOE_UTIL =  0.789` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 116): SAS `else WOE_UTIL = 1.245` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 118): SAS `else WOE_UTIL = 0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 121): SAS `if not missing(PMT_LATE_90_12MO) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 122): SAS `if PMT_LATE_90_12MO = 0      then WOE_DPD = -0.678` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 123): SAS `else if PMT_LATE_90_12MO = 1  then WOE_DPD =  0.445` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 124): SAS `else WOE_DPD = 1.567` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 126): SAS `else WOE_DPD = 0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 129): SAS `if not missing(ACCT_AGE_MONTHS) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 130): SAS `if ACCT_AGE_MONTHS >= 120     then WOE_AGE = -0.534` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 131): SAS `else if ACCT_AGE_MONTHS >= 60 then WOE_AGE = -0.289` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 132): SAS `else if ACCT_AGE_MONTHS >= 24 then WOE_AGE =  0.045` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 133): SAS `else WOE_AGE = 0.456` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 135): SAS `else WOE_AGE = 0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 138): SAS `if ACCOUNT_TYPE in ('MTG','AUTO','HELC') then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 139): SAS `if not missing(LTV) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 140): SAS `if LTV <= 0.60      then WOE_LTV = -0.712` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 141): SAS `else if LTV <= 0.80 then WOE_LTV = -0.234` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 142): SAS `else if LTV <= 1.00 then WOE_LTV =  0.356` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 143): SAS `else WOE_LTV = 0.889` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 145): SAS `else WOE_LTV = 0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 147): SAS `else WOE_LTV = 0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 161): SAS `if ACCOUNT_TYPE in ('MTG','AUTO','HELC') then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 162): SAS `if not missing(LTV) then
        LGD = max(0, min(1, (LTV - 0.5) * 0.8))` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 164): SAS `else
        LGD = 0.40` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 167): SAS `else if ACCOUNT_TYPE = 'CC' then LGD = 0.75` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 168): SAS `else LGD = 0.50` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 172): SAS `if ACCOUNT_TYPE in ('CC','LOC','HELC') then
      EAD = CURRENT_BALANCE + 0.50 * (CREDIT_LIMIT - CURRENT_BALANCE)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 174): SAS `else
      EAD = CURRENT_BALANCE` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 183): SAS `if PD < 0.005      then NEW_RISK_RATING = 1` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 184): SAS `else if PD < 0.01  then NEW_RISK_RATING = 2` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 185): SAS `else if PD < 0.03  then NEW_RISK_RATING = 3` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 186): SAS `else if PD < 0.07  then NEW_RISK_RATING = 4` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 187): SAS `else if PD < 0.15  then NEW_RISK_RATING = 5` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 188): SAS `else if PD < 0.30  then NEW_RISK_RATING = 6` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 189): SAS `else NEW_RISK_RATING = 7` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:credit_risk_scoring:op_92_compute_1_nulls`, `vc_m:credit_risk_scoring:op_92_compute_1_dates`, `vc_m:credit_risk_scoring:op_92_compute_1_numeric`

### 15. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:credit_risk_scoring:s92` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_92_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: INTERCEPT, WOE_FICO, WOE_UTIL, WOE_DPD, WOE_AGE, WOE_LTV, LOG_ODDS` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92 · nombre oficial
- **Pruebas:** `vc_m:credit_risk_scoring:op_92_select_columns_1_schema`

### 16. Escribir WORK.SCORED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:credit_risk_scoring:s92` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92`
- **Conexiones:** Main desde `m:credit_risk_scoring:op_92_select_columns_1`
- **Propiedades:**
  - `TABLE` = `scored` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:92
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:credit_risk_scoring:op_92_write_1_row_count`, `vc_m:credit_risk_scoring:op_92_write_1_schema`

### 17. Leer WORK.SCORED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:credit_risk_scoring:s202` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203`
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_92_write_1`
- **Propiedades:**
  - `TABLE` = `scored` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:credit_risk_scoring:op_92_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:credit_risk_scoring:op_203_read_1_row_count`, `vc_m:credit_risk_scoring:op_203_read_1_schema`

### 18. Leer STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:credit_risk_scoring:s202` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:credit_risk_scoring:op_203_read_2_row_count`, `vc_m:credit_risk_scoring:op_203_read_2_schema`

### 19. Unir (inner join): work.scored, stg_bank.cust_accounts_daily

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:credit_risk_scoring:s202` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_203_read_1`, Lookup desde `m:credit_risk_scoring:op_203_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Inner Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `s.ACCOUNT_ID = a.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 203): SAS `on s.ACCOUNT_ID = a.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:credit_risk_scoring:op_203_join_1_duplicates`, `vc_m:credit_risk_scoring:op_203_join_1_row_count`, `vc_m:credit_risk_scoring:op_203_join_1_nulls`

### 20. Filtrar filas (WHERE): a.SNAPSHOT_DATE = "&score_date"d and (a.RISK_RATING ne s.NEW_RISK_RATING or a.RI

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:credit_risk_scoring:s202` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_203_join_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 203): SAS `a.SNAPSHOT_DATE = "&score_date"d and (a.RISK_RATING ne s.NEW_RISK_RATING or a.RISK_RATING is null)` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:credit_risk_scoring:op_203_filter_1_row_count`, `vc_m:credit_risk_scoring:op_203_filter_1_nulls`, `vc_m:credit_risk_scoring:op_203_filter_1_empty`

### 21. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:credit_risk_scoring:s202` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:credit_risk_scoring:op_203_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `"&score_date"d as SCORE_DATE format=date9., ACCOUNT_ID, PREV_RATING, CURR_RATING, case when a.RISK_RATING is null then 'NEW' when s.NEW_RISK_RATING < a.RISK_RATING then 'UPGRADE' when s.NEW_RISK_RATING > a.RISK_RATING then 'DOWNGRADE' else 'STABLE' end as MIGRATION_DIRECTION length=10, PD, EXPECTED_LOSS` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ACCOUNT_ID`, `PREV_RATING`, `CURR_RATING`, `PD`, `EXPECTED_LOSS` _(tipos por determinar)_
- **Expresión** (línea 203): SAS `"&score_date"d as SCORE_DATE format=date9.` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.'
- **Expresión** (línea 203): SAS `case when a.RISK_RATING is null then 'NEW' when s.NEW_RISK_RATING < a.RISK_RATING then 'UPGRADE' when s.NEW_RISK_RATING > a.RISK_RATING then 'DOWNGRADE' else 'STABLE' end as MIGRATION_DIRECTION length=10` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pruebas:** `vc_m:credit_risk_scoring:op_203_project_1_schema`

### 22. Escribir WORK.RISK_MIGRATION (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:credit_risk_scoring:s202` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203`
- **Conexiones:** Main desde `m:credit_risk_scoring:op_203_project_1`
- **Propiedades:**
  - `TABLE` = `risk_migration` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:203
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:credit_risk_scoring:op_203_write_1_row_count`, `vc_m:credit_risk_scoring:op_203_write_1_schema`

### 23. Invocar macro %lock

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:credit_risk_scoring:s229` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:229`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_203_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `lock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:229 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CURATED.RISK_SCORES` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:229 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 24. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:credit_risk_scoring:s231` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:231`
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_229_macro_call_1`
- **Propiedades:**
  - `TABLE` = `scored` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:231
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:231
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:231
- **Pendientes:**
  - Tabla base destino
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:credit_risk_scoring:op_231_append_1_row_count`

### 25. Invocar macro %lock

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:credit_risk_scoring:s234` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:234`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_231_append_1`
- **Propiedades:**
  - `PROCESS` (Job) = `lock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:234 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CURATED.RISK_SCORES, unlock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:234 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 26. Invocar macro %lock

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:credit_risk_scoring:s236` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:236`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_234_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `lock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:236 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CURATED.RISK_MIGRATION` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:236 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 27. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:credit_risk_scoring:s238` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:238`
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_236_macro_call_1`
- **Propiedades:**
  - `TABLE` = `risk_migration` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:238
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:238
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:238
- **Pendientes:**
  - Tabla base destino
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:credit_risk_scoring:op_238_append_1_row_count`

### 28. Invocar macro %lock

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:credit_risk_scoring:s241` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:241`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_238_append_1`
- **Propiedades:**
  - `PROCESS` (Job) = `lock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:241 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CURATED.RISK_MIGRATION, unlock` — SAS real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:241 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 29. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:credit_risk_scoring:s246` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:246`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_241_macro_call_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_m:credit_risk_scoring:op_246_aggregate_1_aggregates`, `vc_m:credit_risk_scoring:op_246_aggregate_1_numeric`

### 30. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:credit_risk_scoring:s264` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:264`
- **Conexiones:** OnSubjobOk desde `m:credit_risk_scoring:op_246_aggregate_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Sin resolver

- include /opt/sas/custom/macros/parmv.sas (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:15) — external
- include /opt/sas/custom/macros/nobs.sas (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:16) — external
- macro parmv (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:20) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:21) — sin definición en el proyecto
- macro lock (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:229) — sin definición en el proyecto
- macro lock (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:234) — sin definición en el proyecto
- macro lock (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:236) — sin definición en el proyecto
- macro lock (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:241) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:260) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas:261) — sin definición en el proyecto

## Casos de validación

- `vc_m:credit_risk_scoring:op_33_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:credit_risk_scoring:op_33_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:credit_risk_scoring:op_33_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:credit_risk_scoring:op_33_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:credit_risk_scoring:op_33_read_3_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:credit_risk_scoring:op_33_read_3_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:credit_risk_scoring:op_33_read_4_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:credit_risk_scoring:op_33_read_4_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:credit_risk_scoring:op_33_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:credit_risk_scoring:op_33_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:credit_risk_scoring:op_33_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:credit_risk_scoring:op_33_join_2_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:credit_risk_scoring:op_33_join_2_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:credit_risk_scoring:op_33_join_2_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:credit_risk_scoring:op_33_join_3_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:credit_risk_scoring:op_33_join_3_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:credit_risk_scoring:op_33_join_3_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:credit_risk_scoring:op_33_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:credit_risk_scoring:op_33_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:credit_risk_scoring:op_33_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:credit_risk_scoring:op_33_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:credit_risk_scoring:op_33_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:credit_risk_scoring:op_33_write_1_schema` (schema): Esquema destino
- `vc_m:credit_risk_scoring:op_92_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:credit_risk_scoring:op_92_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:credit_risk_scoring:op_92_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:credit_risk_scoring:op_92_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:credit_risk_scoring:op_92_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:credit_risk_scoring:op_92_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:credit_risk_scoring:op_92_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:credit_risk_scoring:op_92_write_1_schema` (schema): Esquema destino
- `vc_m:credit_risk_scoring:op_203_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:credit_risk_scoring:op_203_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:credit_risk_scoring:op_203_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:credit_risk_scoring:op_203_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:credit_risk_scoring:op_203_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:credit_risk_scoring:op_203_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:credit_risk_scoring:op_203_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:credit_risk_scoring:op_203_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:credit_risk_scoring:op_203_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:credit_risk_scoring:op_203_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:credit_risk_scoring:op_203_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:credit_risk_scoring:op_203_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:credit_risk_scoring:op_203_write_1_schema` (schema): Esquema destino
- `vc_m:credit_risk_scoring:op_231_append_1_row_count` (row_count): Filas añadidas
- `vc_m:credit_risk_scoring:op_238_append_1_row_count` (row_count): Filas añadidas
- `vc_m:credit_risk_scoring:op_246_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:credit_risk_scoring:op_246_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
