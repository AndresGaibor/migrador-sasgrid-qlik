# Job `job_load_customer_accounts`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas` (sha256 `11035230a26e`)
- **Instrucciones:** 22 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%load_customer_accounts(run_date, region)` está integrada en el Job.

## Orquestación

- Planificación: Daily 06:00 via Control-M job BANK_DAILY_01
- Lo consumen: `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas`, `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas`, `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas`, `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas`
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas#1`

### Recomendaciones Grid

### `sas_macro_step.include_dispatch` (partial)

- **Accion:** Crea un Job hijo para cada programa resuelto y confirma sus parámetros antes de conectar la secuencia.
- **Motivo/limite:** The analyzer resolves tested macro dispatches, but macro defaults and failure behavior require review.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:121` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Confirmar:** Review macro dispatch semantics; Confirm child Job and context parameters
- **Datos interpretados:**

```json
{
  "kind": "sas_macro_step",
  "program": "/opt/sas/custom/programs/Banking/load_customer_accounts.sas",
  "resolved_program": "real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas",
  "match_status": "resolved",
  "job_name": null,
  "queue": null,
  "waits": true,
  "params": {
    "step_num": "1",
    "step_name": "Load Customer Accounts",
    "program": "/opt/sas/custom/programs/Banking/load_customer_accounts.sas"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:9` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Daily 06:00 via Control-M job BANK_DAILY_01"
}
```

## Variables de contexto

- `context.CURR_DT` ← SAS `CURR_DT` (Variable SAS referenciada por %load_customer_accounts(run_date=...))
- `context.EMAIL_ONCALL` ← SAS `EMAIL_ONCALL` (&EMAIL_ONCALL en real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:175)
- `context.nobs_except` ← SAS `nobs_except` (&nobs_except en real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:175)
- `context.region` ← SAS `region` (Parámetro de la macro principal %load_customer_accounts; argumento SAS: sin asignar)
- `context.run_date` ← SAS `run_date` (&run_date en real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:175)

## Conexiones a crear

- `ORA_DW` (oracle, FINPROD) → tOracleConnection. Crear la conexión en Talend; no se copian credenciales
- `STG_BANK` (BASE, /data/sas/staging/banking) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:load_customer_accounts:s19` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:19`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:19 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `run_date, _req=1, _msg=Run date is required` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:19 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:load_customer_accounts:s20` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:20`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_19_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:20 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `region,   _req=0, _val=ALL NE SE MW SW W NW` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:20 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Leer ORA_DW.CUST_ACCOUNTS

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_20_macro_call_1`
- **Propiedades:**
  - `TABLE` (Table Name) = `cust_accounts` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:load_customer_accounts:op_35_read_1_row_count`, `vc_m:load_customer_accounts:op_35_read_1_schema`

### 4. Leer ORA_DW.CUST_DEMOGRAPHICS

- **Acción:** add_component · **Componente:** `tOracleInput` ![Icono Talend](assets/talend-icons/tOracleInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `cust_demographics` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería ora_dw usa el motor oracle
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:load_customer_accounts:op_35_read_2_row_count`, `vc_m:load_customer_accounts:op_35_read_2_schema`

### 5. Unir (inner join): ora_dw.cust_accounts, ora_dw.cust_demographics

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:load_customer_accounts:op_35_read_1`, Lookup desde `m:load_customer_accounts:op_35_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Inner Join` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `a.CUSTOMER_ID = d.CUSTOMER_ID` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35
- **Esquema:** `CUSTOMER_ID` _(tipos por determinar)_
- **Expresión** (línea 35): SAS `on a.CUSTOMER_ID = d.CUSTOMER_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:load_customer_accounts:op_35_join_1_duplicates`, `vc_m:load_customer_accounts:op_35_join_1_row_count`, `vc_m:load_customer_accounts:op_35_join_1_nulls`

### 6. Filtrar filas (WHERE): a.ACCOUNT_STATUS not in ('W', 'C') and a.OPEN_DATE <= "&run_date"d %if &region n

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:load_customer_accounts:op_35_join_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 35): SAS `a.ACCOUNT_STATUS not in ('W', 'C') and a.OPEN_DATE <= "&run_date"d %if &region ne ALL %then %do` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ' %if &region'
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:load_customer_accounts:op_35_filter_1_row_count`, `vc_m:load_customer_accounts:op_35_filter_1_nulls`, `vc_m:load_customer_accounts:op_35_filter_1_empty`

### 7. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:load_customer_accounts:op_35_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `ACCOUNT_ID, CUSTOMER_ID, ACCOUNT_TYPE, ACCOUNT_STATUS, OPEN_DATE, CLOSE_DATE, CURRENT_BALANCE, AVAILABLE_BALANCE, CREDIT_LIMIT, INTEREST_RATE, BRANCH_ID, OFFICER_ID, LAST_ACTIVITY_DATE, FIRST_NAME, LAST_NAME, SSN_HASH, DATE_OF_BIRTH, CUSTOMER_SEGMENT, RISK_RATING, REGION_CODE, PRIMARY_EMAIL, PHONE_NUMBER` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ACCOUNT_ID`, `CUSTOMER_ID`, `ACCOUNT_TYPE`, `ACCOUNT_STATUS`, `OPEN_DATE`, `CLOSE_DATE`, `CURRENT_BALANCE`, `AVAILABLE_BALANCE`, `CREDIT_LIMIT`, `INTEREST_RATE`, `BRANCH_ID`, `OFFICER_ID`, `LAST_ACTIVITY_DATE`, `FIRST_NAME`, `LAST_NAME`, `SSN_HASH`, `DATE_OF_BIRTH`, `CUSTOMER_SEGMENT`, `RISK_RATING`, `REGION_CODE`, `PRIMARY_EMAIL`, `PHONE_NUMBER` _(tipos por determinar)_
- **Pruebas:** `vc_m:load_customer_accounts:op_35_project_1_schema`

### 8. Escribir WORK.ACCT_RAW (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35`
- **Conexiones:** Main desde `m:load_customer_accounts:op_35_project_1`
- **Propiedades:**
  - `TABLE` = `acct_raw` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:35
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:load_customer_accounts:op_35_write_1_row_count`, `vc_m:load_customer_accounts:op_35_write_1_schema`

### 9. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:65`
- **Conexiones:** Main desde `m:load_customer_accounts:op_35_write_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 10. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:load_customer_accounts:s34` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:67`
- **Conexiones:** Main desde `m:load_customer_accounts:op_65_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 11. Leer WORK.ACCT_RAW

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:load_customer_accounts:s82` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82`
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_67_unsupported_1`
- **Propiedades:**
  - `TABLE` = `acct_raw` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:load_customer_accounts:op_35_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:load_customer_accounts:op_82_read_1_row_count`, `vc_m:load_customer_accounts:op_82_read_1_schema`

### 12. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:load_customer_accounts:s82` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:load_customer_accounts:op_82_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `10 asignaciones, 9 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ACCT_AGE_MONTHS`, `DAYS_INACTIVE`, `EXCEPTION_CODE`, `EXCEPTION_DESC`, `SNAPSHOT_DATE`, `LOAD_TIMESTAMP` _(tipos por determinar)_
- **Expresión** (línea 100): SAS `intck('month', OPEN_DATE, "&run_date"d)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intck
- **Expresión** (línea 103): SAS `"&run_date"d - LAST_ACTIVITY_DATE` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Expresión** (línea 125): SAS `'NEG_BAL'` → Java `"NEG_BAL"`
- **Expresión** (línea 126): SAS `catx(' ', 'Negative balance',
        put(CURRENT_BALANCE, dollar18.2),
        'on deposit account', ACCOUNT_ID)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ".2), 'on dep"
- **Expresión** (línea 134): SAS `'HIGH_UTIL'` → Java `"HIGH_UTIL"`
- **Expresión** (línea 135): SAS `catx(' ', 'Utilization at',
        put(UTILIZATION_PCT, 5.1), '%',
        'for account', ACCOUNT_ID)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función catx
- **Expresión** (línea 143): SAS `'NO_RISK'` → Java `"NO_RISK"`
- **Expresión** (línea 144): SAS `catx(' ', 'Missing risk rating for customer',
        CUSTOMER_ID)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función catx
- **Expresión** (línea 150): SAS `"&run_date"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Expresión** (línea 151): SAS `datetime()` → _sin traducción automática_
  - ⚠ Sin traducción automática: función datetime
- **Expresión** (línea 106): SAS `if ACCOUNT_TYPE in ('CC', 'LOC', 'HELC') and CREDIT_LIMIT > 0 then
      UTILIZATION_PCT = (CURRENT_BALANCE / CREDIT_LIMIT) * 100` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 108): SAS `else
      UTILIZATION_PCT = .` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 112): SAS `if DAYS_INACTIVE > 365 and ACCOUNT_STATUS = 'A' then
      DORMANCY_FLAG = 'Y'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 114): SAS `else
      DORMANCY_FLAG = 'N'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 118): SAS `if CURRENT_BALANCE >= 250000 then
      HIGH_BALANCE_FLAG = 'Y'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 120): SAS `else
      HIGH_BALANCE_FLAG = 'N'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 124): SAS `if ACCOUNT_TYPE in ('CHK', 'SAV', 'MMA', 'CD') and CURRENT_BALANCE < 0 then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 133): SAS `if UTILIZATION_PCT > 95 then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 142): SAS `if RISK_RATING = . then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:load_customer_accounts:op_82_compute_1_nulls`, `vc_m:load_customer_accounts:op_82_compute_1_dates`, `vc_m:load_customer_accounts:op_82_compute_1_numeric`

### 13. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:load_customer_accounts:s82` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:load_customer_accounts:op_82_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: EXCEPTION_CODE, EXCEPTION_DESC` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82 · nombre oficial
- **Pruebas:** `vc_m:load_customer_accounts:op_82_select_columns_1_schema`

### 14. Escribir STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:load_customer_accounts:s82` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82`
- **Conexiones:** Main desde `m:load_customer_accounts:op_82_select_columns_1`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:load_customer_accounts:op_82_write_1_row_count`, `vc_m:load_customer_accounts:op_82_write_1_schema`

### 15. Escribir WORK.ACCT_EXCEPTIONS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:load_customer_accounts:s82` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82`
- **Conexiones:** Main desde `m:load_customer_accounts:op_82_write_1`
- **Propiedades:**
  - `TABLE` = `acct_exceptions` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:82
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:load_customer_accounts:op_82_write_2_row_count`, `vc_m:load_customer_accounts:op_82_write_2_schema`

### 16. Leer WORK.ACCT_EXCEPTIONS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:load_customer_accounts:s167` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168`
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_82_write_2`
- **Propiedades:**
  - `TABLE` = `acct_exceptions` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:load_customer_accounts:op_82_write_2): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:load_customer_accounts:op_168_read_1_row_count`, `vc_m:load_customer_accounts:op_168_read_1_schema`

### 17. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:load_customer_accounts:s167` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:load_customer_accounts:op_168_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_m:load_customer_accounts:op_168_project_1_schema`

### 18. Escribir STG_BANK.ACCT_EXCEPTIONS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:load_customer_accounts:s167` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168`
- **Conexiones:** Main desde `m:load_customer_accounts:op_168_project_1`
- **Propiedades:**
  - `TABLE` = `acct_exceptions` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:168
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:load_customer_accounts:op_168_write_1_row_count`, `vc_m:load_customer_accounts:op_168_write_1_schema`

### 19. Incluir otro programa

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`, `Rutina`
- **Subjob:** `m:load_customer_accounts:s174` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:174`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_168_write_1`
- **Propiedades:**
  - `PROCESS` (Job) = `"/opt/sas/custom/macros/sendmail.sas"` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:174 · nombre oficial
- **Pendientes:**
  - Confirmar si el programa incluido se migra como Job hijo

### 20. Invocar macro %sendmail

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:load_customer_accounts:s175` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:175`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_174_include_1`
- **Propiedades:**
  - `PROCESS` (Job) = `sendmail` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:175 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
        to=&EMAIL_ONCALL,
        subject=ALERT: &nobs_except account exceptions on &run_date,
        body=Critical volume of account exceptions. Review STG_BANK.ACCT_EXCEPTIONS.
      ` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:175 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 21. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:load_customer_accounts:s188` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:188`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_175_macro_call_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_m:load_customer_accounts:op_188_aggregate_1_aggregates`, `vc_m:load_customer_accounts:op_188_aggregate_1_numeric`

### 22. Invocar macro %exit

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:load_customer_accounts:s207` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:207`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:load_customer_accounts:op_188_aggregate_1`
- **Propiedades:**
  - `PROCESS` (Job) = `exit` — SAS real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:207 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- include /opt/sas/custom/macros/parmv.sas (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:13) — external
- include /opt/sas/custom/macros/nobs.sas (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:14) — external
- include /opt/sas/custom/macros/lock.sas (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:15) — external
- macro parmv (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:19) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:20) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:71) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:162) — sin definición en el proyecto
- macro sendmail (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:175) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:186) — sin definición en el proyecto
- macro exit (real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas:207) — sin definición en el proyecto

## Casos de validación

- `vc_m:load_customer_accounts:op_35_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:load_customer_accounts:op_35_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:load_customer_accounts:op_35_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:load_customer_accounts:op_35_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:load_customer_accounts:op_35_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:load_customer_accounts:op_35_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:load_customer_accounts:op_35_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:load_customer_accounts:op_35_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:load_customer_accounts:op_35_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:load_customer_accounts:op_35_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:load_customer_accounts:op_35_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:load_customer_accounts:op_35_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:load_customer_accounts:op_35_write_1_schema` (schema): Esquema destino
- `vc_m:load_customer_accounts:op_82_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:load_customer_accounts:op_82_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:load_customer_accounts:op_82_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:load_customer_accounts:op_82_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:load_customer_accounts:op_82_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:load_customer_accounts:op_82_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:load_customer_accounts:op_82_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:load_customer_accounts:op_82_write_1_schema` (schema): Esquema destino
- `vc_m:load_customer_accounts:op_82_write_2_row_count` (row_count): Filas escritas iguales
- `vc_m:load_customer_accounts:op_82_write_2_schema` (schema): Esquema destino
- `vc_m:load_customer_accounts:op_168_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:load_customer_accounts:op_168_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:load_customer_accounts:op_168_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:load_customer_accounts:op_168_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:load_customer_accounts:op_168_write_1_schema` (schema): Esquema destino
- `vc_m:load_customer_accounts:op_188_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:load_customer_accounts:op_188_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
