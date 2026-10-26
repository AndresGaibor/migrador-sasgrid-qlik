# Job `job_monthly_regulatory_reporting`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas` (sha256 `55b71f669666`)
- **Instrucciones:** 27 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%monthly_regulatory_reporting(report_month)` está integrada en el Job.

## Orquestación

- Planificación: Monthly 3rd business day via Control-M BANK_MONTHLY_01
- Depende de (datos): `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas`
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#4`

### Recomendaciones Grid

### `sas_macro_step.include_dispatch` (partial)

- **Accion:** Crea un Job hijo para cada programa resuelto y confirma sus parámetros antes de conectar la secuencia.
- **Motivo/limite:** The analyzer resolves tested macro dispatches, but macro defaults and failure behavior require review.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:130` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#3`
- **Confirmar:** Review macro dispatch semantics; Confirm child Job and context parameters
- **Datos interpretados:**

```json
{
  "kind": "sas_macro_step",
  "program": "/opt/sas/custom/programs/Banking/monthly_regulatory_reporting.sas",
  "resolved_program": "real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas",
  "match_status": "resolved",
  "job_name": null,
  "queue": null,
  "waits": true,
  "params": {
    "step_num": "4",
    "step_name": "Monthly Regulatory Reporting",
    "program": "/opt/sas/custom/programs/Banking/monthly_regulatory_reporting.sas"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:14` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Monthly 3rd business day via Control-M BANK_MONTHLY_01"
}
```

## Variables de contexto

- `context.PREV_YM` ← SAS `PREV_YM` (Variable SAS referenciada por %monthly_regulatory_reporting(report_month=...))
- `context.report_month` ← SAS `report_month` (&report_month en real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:146)
- `context.REPORT_PATH` ← SAS `REPORT_PATH` (&REPORT_PATH en real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:146)

## Conexiones a crear

- `ORA_DW` (oracle, FINPROD) → tOracleConnection. Crear la conexión en Talend; no se copian credenciales
- `REPORTS` (BASE, /data/sas/reports) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `STG_BANK` (BASE, /data/sas/staging/banking) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:monthly_regulatory_reporting:s24` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:24`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:24 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `report_month, _req=1` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:24 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Leer STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:monthly_regulatory_reporting:s40` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41`
- **Conexiones:** OnSubjobOk desde `m:monthly_regulatory_reporting:op_24_macro_call_1`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_41_read_1_row_count`, `vc_m:monthly_regulatory_reporting:op_41_read_1_schema`

### 3. Leer ORA_DW.LOAN_DETAILS

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:monthly_regulatory_reporting:s40` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `loan_details` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_41_read_2_row_count`, `vc_m:monthly_regulatory_reporting:op_41_read_2_schema`

### 4. Unir (left join): stg_bank.cust_accounts_daily, ora_dw.loan_details

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:monthly_regulatory_reporting:s40` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_41_read_1`, Lookup desde `m:monthly_regulatory_reporting:op_41_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.ACCOUNT_ID = l.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 41): SAS `on a.ACCOUNT_ID = l.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_41_join_1_duplicates`, `vc_m:monthly_regulatory_reporting:op_41_join_1_row_count`, `vc_m:monthly_regulatory_reporting:op_41_join_1_nulls`

### 5. Filtrar filas (WHERE): a.SNAPSHOT_DATE = "&month_end"d

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:monthly_regulatory_reporting:s40` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_41_join_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 41): SAS `a.SNAPSHOT_DATE = "&month_end"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_41_filter_1_row_count`, `vc_m:monthly_regulatory_reporting:op_41_filter_1_nulls`, `vc_m:monthly_regulatory_reporting:op_41_filter_1_empty`

### 6. Agregar por 1, 2, 3, 4

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:monthly_regulatory_reporting:s40` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_41_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `1, 2, 3, 4` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41 · nombre oficial
  - `OPERATIONS` (Operations) = `N_ACCOUNTS = count(*)` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41 · nombre oficial
- **Esquema:** `"&report_month" as REPORT_MONTH length=6`, `ACCOUNT_TYPE`, `CUSTOMER_SEGMENT`, `RISK_WEIGHT`, `N_ACCOUNTS`, `sum(CURRENT_BALANCE) as TOTAL_EXPOSURE format=dollar20.2`, `sum(CURRENT_BALANCE * calculated RISK_WEIGHT) as RWA format=dollar20.2`, `1`, `2`, `3`, `4` _(tipos por determinar)_
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_41_aggregate_1_aggregates`, `vc_m:monthly_regulatory_reporting:op_41_aggregate_1_numeric`

### 7. Ordenar por ACCOUNT_TYPE, CUSTOMER_SEGMENT

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:monthly_regulatory_reporting:s40` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_41_aggregate_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ACCOUNT_TYPE, CUSTOMER_SEGMENT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41 · nombre oficial
- **Esquema:** `ACCOUNT_TYPE`, `CUSTOMER_SEGMENT` _(tipos por determinar)_
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_41_sort_1_ordering`

### 8. Escribir REPORTS.MONTHLY_RWA (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:monthly_regulatory_reporting:s40` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41`
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_41_sort_1`
- **Propiedades:**
  - `TABLE` = `monthly_rwa` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:41
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_41_write_1_row_count`, `vc_m:monthly_regulatory_reporting:op_41_write_1_schema`

### 9. Leer STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:monthly_regulatory_reporting:s72` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73`
- **Conexiones:** OnSubjobOk desde `m:monthly_regulatory_reporting:op_41_write_1`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_73_read_1_row_count`, `vc_m:monthly_regulatory_reporting:op_73_read_1_schema`

### 10. Leer ORA_DW.LOAN_DETAILS

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:monthly_regulatory_reporting:s72` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `loan_details` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_73_read_2_row_count`, `vc_m:monthly_regulatory_reporting:op_73_read_2_schema`

### 11. Unir (left join): stg_bank.cust_accounts_daily, ora_dw.loan_details

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:monthly_regulatory_reporting:s72` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_73_read_1`, Lookup desde `m:monthly_regulatory_reporting:op_73_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.ACCOUNT_ID = l.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 73): SAS `on a.ACCOUNT_ID = l.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_73_join_1_duplicates`, `vc_m:monthly_regulatory_reporting:op_73_join_1_row_count`, `vc_m:monthly_regulatory_reporting:op_73_join_1_nulls`

### 12. Filtrar filas (WHERE): a.SNAPSHOT_DATE = "&month_end"d and a.ACCOUNT_TYPE in ('MTG','AUTO','PERS','CC',

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:monthly_regulatory_reporting:s72` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_73_join_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 73): SAS `a.SNAPSHOT_DATE = "&month_end"d and a.ACCOUNT_TYPE in ('MTG','AUTO','PERS','CC','LOC','HELC')` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_73_filter_1_row_count`, `vc_m:monthly_regulatory_reporting:op_73_filter_1_nulls`, `vc_m:monthly_regulatory_reporting:op_73_filter_1_empty`

### 13. Agregar por 1, 2, 3, 4

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:monthly_regulatory_reporting:s72` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_73_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `1, 2, 3, 4` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73 · nombre oficial
  - `OPERATIONS` (Operations) = `N_ACCOUNTS = count(*)` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73 · nombre oficial
- **Esquema:** `"&report_month" as REPORT_MONTH length=6`, `ACCOUNT_TYPE`, `REGION_CODE`, `case when DAYS_PAST_DUE = 0 then 'Current' when DAYS_PAST_DUE between 1 and 29 then '1-29' when DAYS_PAST_DUE between 30 and 59 then '30-59' when DAYS_PAST_DUE between 60 and 89 then '60-89' when DAYS_PAST_DUE between 90 and 119 then '90-119' when DAYS_PAST_DUE between 120 and 179 then '120-179' when DAYS_PAST_DUE >= 180 then '180+' else 'Unknown' end as DELINQ_BUCKET length=10`, `N_ACCOUNTS`, `sum(CURRENT_BALANCE) as TOTAL_BALANCE format=dollar20.2`, `sum(PAST_DUE_AMOUNT) as TOTAL_PAST_DUE format=dollar20.2`, `1`, `2`, `3`, `4` _(tipos por determinar)_
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_73_aggregate_1_aggregates`, `vc_m:monthly_regulatory_reporting:op_73_aggregate_1_numeric`

### 14. Ordenar por ACCOUNT_TYPE, REGION_CODE, case when calculated DELINQ_BUCKET = 'Current' then 0 when calculated DELINQ_BUCKET = '1-29' then 1 when calculated DELINQ_BUCKET = '30-59' then 2 when calculated DELINQ_BUCKET = '60-89' then 3 when calculated DELINQ_BUCKET = '90-119' then 4 when calculated DELINQ_BUCKET = '120-179' then 5 when calculated DELINQ_BUCKET = '180+' then 6 else 7 end

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:monthly_regulatory_reporting:s72` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_73_aggregate_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ACCOUNT_TYPE, REGION_CODE, case when calculated DELINQ_BUCKET = 'Current' then 0 when calculated DELINQ_BUCKET = '1-29' then 1 when calculated DELINQ_BUCKET = '30-59' then 2 when calculated DELINQ_BUCKET = '60-89' then 3 when calculated DELINQ_BUCKET = '90-119' then 4 when calculated DELINQ_BUCKET = '120-179' then 5 when calculated DELINQ_BUCKET = '180+' then 6 else 7 end` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73 · nombre oficial
- **Esquema:** `ACCOUNT_TYPE`, `REGION_CODE`, `case when calculated DELINQ_BUCKET = 'Current' then 0 when calculated DELINQ_BUCKET = '1-29' then 1 when calculated DELINQ_BUCKET = '30-59' then 2 when calculated DELINQ_BUCKET = '60-89' then 3 when calculated DELINQ_BUCKET = '90-119' then 4 when calculated DELINQ_BUCKET = '120-179' then 5 when calculated DELINQ_BUCKET = '180+' then 6 else 7 end` _(tipos por determinar)_
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_73_sort_1_ordering`

### 15. Escribir REPORTS.DELINQUENCY_AGING (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:monthly_regulatory_reporting:s72` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73`
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_73_sort_1`
- **Propiedades:**
  - `TABLE` = `delinquency_aging` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:73
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_73_write_1_row_count`, `vc_m:monthly_regulatory_reporting:op_73_write_1_schema`

### 16. Leer STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:monthly_regulatory_reporting:s114` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115`
- **Conexiones:** OnSubjobOk desde `m:monthly_regulatory_reporting:op_73_write_1`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_115_read_1_row_count`, `vc_m:monthly_regulatory_reporting:op_115_read_1_schema`

### 17. Leer ORA_DW.LOAN_DETAILS

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:monthly_regulatory_reporting:s114` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `loan_details` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_115_read_2_row_count`, `vc_m:monthly_regulatory_reporting:op_115_read_2_schema`

### 18. Unir (inner join): stg_bank.cust_accounts_daily, ora_dw.loan_details

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:monthly_regulatory_reporting:s114` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_115_read_1`, Lookup desde `m:monthly_regulatory_reporting:op_115_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Inner Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.ACCOUNT_ID = l.ACCOUNT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115
- **Esquema:** `ACCOUNT_ID` _(tipos por determinar)_
- **Expresión** (línea 115): SAS `on a.ACCOUNT_ID = l.ACCOUNT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_115_join_1_duplicates`, `vc_m:monthly_regulatory_reporting:op_115_join_1_row_count`, `vc_m:monthly_regulatory_reporting:op_115_join_1_nulls`

### 19. Filtrar filas (WHERE): a.SNAPSHOT_DATE = "&month_end"d and a.ACCOUNT_TYPE in ('MTG','AUTO','PERS','CC',

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:monthly_regulatory_reporting:s114` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_115_join_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 115): SAS `a.SNAPSHOT_DATE = "&month_end"d and a.ACCOUNT_TYPE in ('MTG','AUTO','PERS','CC','LOC','HELC')` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_115_filter_1_row_count`, `vc_m:monthly_regulatory_reporting:op_115_filter_1_nulls`, `vc_m:monthly_regulatory_reporting:op_115_filter_1_empty`

### 20. Agregar por 1, 2

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:monthly_regulatory_reporting:s114` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_115_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `1, 2` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115 · nombre oficial
  - `OPERATIONS` (Operations) = `N_LOANS = count(*)` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115 · nombre oficial
- **Esquema:** `"&report_month" as REPORT_MONTH length=6`, `ACCOUNT_TYPE`, `N_LOANS`, `sum(a.CURRENT_BALANCE) as GROSS_LOANS format=dollar20.2`, `sum(l.ALLOWANCE_AMT) as TOTAL_ALLOWANCE format=dollar20.2`, `case when sum(a.CURRENT_BALANCE) > 0 then sum(l.ALLOWANCE_AMT) / sum(a.CURRENT_BALANCE) * 100 else 0 end as COVERAGE_PCT format=8.2`, `sum(case when l.DAYS_PAST_DUE >= 90 then a.CURRENT_BALANCE else 0 end) as NPL_BALANCE format=dollar20.2`, `case when calculated NPL_BALANCE > 0 then sum(l.ALLOWANCE_AMT) / calculated NPL_BALANCE * 100 else 0 end as NPL_COVERAGE_PCT format=8.2`, `1`, `2` _(tipos por determinar)_
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_115_aggregate_1_aggregates`, `vc_m:monthly_regulatory_reporting:op_115_aggregate_1_numeric`

### 21. Escribir REPORTS.LLP_COVERAGE (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:monthly_regulatory_reporting:s114` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115`
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_115_aggregate_1`
- **Propiedades:**
  - `TABLE` = `llp_coverage` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:115
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_115_write_1_row_count`, `vc_m:monthly_regulatory_reporting:op_115_write_1_schema`

### 22. Invocar macro %export_xlsx

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:monthly_regulatory_reporting:s146` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:146`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:monthly_regulatory_reporting:op_115_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `export_xlsx` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:146 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
    data=REPORTS.MONTHLY_RWA,
    file=&REPORT_PATH/REG_REPORT_&report_month..xlsx,
    sheet=RWA
  ` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:146 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 23. Invocar macro %export_xlsx

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:monthly_regulatory_reporting:s152` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:152`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:monthly_regulatory_reporting:op_146_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `export_xlsx` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:152 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
    data=REPORTS.DELINQUENCY_AGING,
    file=&REPORT_PATH/REG_REPORT_&report_month..xlsx,
    sheet=Delinquency
  ` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:152 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 24. Invocar macro %export_xlsx

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:monthly_regulatory_reporting:s158` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:158`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:monthly_regulatory_reporting:op_152_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `export_xlsx` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:158 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
    data=REPORTS.LLP_COVERAGE,
    file=&REPORT_PATH/REG_REPORT_&report_month..xlsx,
    sheet=LLP_Coverage
  ` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:158 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 25. Leer REPORTS.MONTHLY_RWA

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:monthly_regulatory_reporting:s169` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:170`
- **Conexiones:** OnSubjobOk desde `m:monthly_regulatory_reporting:op_158_macro_call_1`
- **Propiedades:**
  - `TABLE` = `monthly_rwa` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:170
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset producido antes en este programa (m:monthly_regulatory_reporting:op_41_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_170_read_1_row_count`, `vc_m:monthly_regulatory_reporting:op_170_read_1_schema`

### 26. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:monthly_regulatory_reporting:s169` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:170`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_170_read_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `"&report_month" as REPORT_MONTH length=6`, `sum(RWA) as TOTAL_RWA format=dollar20.2`, `50000000 as CET1_CAPITAL format=dollar20.2`, `65000000 as TIER1_CAPITAL format=dollar20.2`, `80000000 as TOTAL_CAPITAL format=dollar20.2`, `case when sum(RWA) > 0 then 50000000 / sum(RWA) * 100 else . end as CET1_RATIO format=8.2`, `case when sum(RWA) > 0 then 65000000 / sum(RWA) * 100 else . end as TIER1_RATIO format=8.2`, `case when sum(RWA) > 0 then 80000000 / sum(RWA) * 100 else . end as TOTAL_CAPITAL_RATIO format=8.2`, `case when sum(RWA) = 0 then 'PASS' when 50000000/sum(RWA)*100 >= 4.5 then 'PASS' else 'FAIL' end as CET1_STATUS length=4`, `case when sum(RWA) = 0 then 'PASS' when 65000000/sum(RWA)*100 >= 6.0 then 'PASS' else 'FAIL' end as TIER1_STATUS length=4`, `case when sum(RWA) = 0 then 'PASS' when 80000000/sum(RWA)*100 >= 8.0 then 'PASS' else 'FAIL' end as TOTAL_CAPITAL_STATUS length=4` _(tipos por determinar)_
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_170_aggregate_1_aggregates`, `vc_m:monthly_regulatory_reporting:op_170_aggregate_1_numeric`

### 27. Escribir REPORTS.CAPITAL_ADEQUACY (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:monthly_regulatory_reporting:s169` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:170`
- **Conexiones:** Main desde `m:monthly_regulatory_reporting:op_170_aggregate_1`
- **Propiedades:**
  - `TABLE` = `capital_adequacy` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:170
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:170
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:170
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:monthly_regulatory_reporting:op_170_write_1_row_count`, `vc_m:monthly_regulatory_reporting:op_170_write_1_schema`

## Sin resolver

- include /opt/sas/custom/macros/parmv.sas (real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:18) — external
- include /opt/sas/custom/macros/nobs.sas (real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:19) — external
- include /opt/sas/custom/macros/export_xlsx.sas (real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:20) — external
- macro parmv (real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:24) — sin definición en el proyecto
- macro export_xlsx (real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:146) — sin definición en el proyecto
- macro export_xlsx (real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:152) — sin definición en el proyecto
- macro export_xlsx (real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas:158) — sin definición en el proyecto

## Casos de validación

- `vc_m:monthly_regulatory_reporting:op_41_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:monthly_regulatory_reporting:op_41_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:monthly_regulatory_reporting:op_41_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:monthly_regulatory_reporting:op_41_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:monthly_regulatory_reporting:op_41_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:monthly_regulatory_reporting:op_41_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:monthly_regulatory_reporting:op_41_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:monthly_regulatory_reporting:op_41_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:monthly_regulatory_reporting:op_41_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:monthly_regulatory_reporting:op_41_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:monthly_regulatory_reporting:op_41_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:monthly_regulatory_reporting:op_41_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:monthly_regulatory_reporting:op_41_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:monthly_regulatory_reporting:op_41_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:monthly_regulatory_reporting:op_41_write_1_schema` (schema): Esquema destino
- `vc_m:monthly_regulatory_reporting:op_73_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:monthly_regulatory_reporting:op_73_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:monthly_regulatory_reporting:op_73_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:monthly_regulatory_reporting:op_73_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:monthly_regulatory_reporting:op_73_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:monthly_regulatory_reporting:op_73_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:monthly_regulatory_reporting:op_73_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:monthly_regulatory_reporting:op_73_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:monthly_regulatory_reporting:op_73_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:monthly_regulatory_reporting:op_73_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:monthly_regulatory_reporting:op_73_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:monthly_regulatory_reporting:op_73_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:monthly_regulatory_reporting:op_73_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:monthly_regulatory_reporting:op_73_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:monthly_regulatory_reporting:op_73_write_1_schema` (schema): Esquema destino
- `vc_m:monthly_regulatory_reporting:op_115_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:monthly_regulatory_reporting:op_115_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:monthly_regulatory_reporting:op_115_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:monthly_regulatory_reporting:op_115_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:monthly_regulatory_reporting:op_115_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:monthly_regulatory_reporting:op_115_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:monthly_regulatory_reporting:op_115_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:monthly_regulatory_reporting:op_115_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:monthly_regulatory_reporting:op_115_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:monthly_regulatory_reporting:op_115_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:monthly_regulatory_reporting:op_115_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:monthly_regulatory_reporting:op_115_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:monthly_regulatory_reporting:op_115_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:monthly_regulatory_reporting:op_115_write_1_schema` (schema): Esquema destino
- `vc_m:monthly_regulatory_reporting:op_170_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:monthly_regulatory_reporting:op_170_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:monthly_regulatory_reporting:op_170_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:monthly_regulatory_reporting:op_170_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:monthly_regulatory_reporting:op_170_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:monthly_regulatory_reporting:op_170_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
