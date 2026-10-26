# Job `job_customer_profitability`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas` (sha256 `b387416e9301`)
- **Instrucciones:** 24 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%customer_profitability(report_month)` está integrada en el Job.

## Orquestación

- Planificación: Monthly 10th business day via Control-M BANK_MONTHLY_03
- Depende de (datos): `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas`

### Recomendaciones Grid

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:11` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Monthly 10th business day via Control-M BANK_MONTHLY_03"
}
```

## Variables de contexto

- `context.PREV_YM` ← SAS `PREV_YM` (Variable SAS referenciada por %customer_profitability(report_month=...))
- `context.report_month` ← SAS `report_month` (&report_month en real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:159)
- `context.REPORT_PATH` ← SAS `REPORT_PATH` (&REPORT_PATH en real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:159)

## Conexiones a crear

- `CURATED` (BASE, /data/sas/curated) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `REPORTS` (BASE, /data/sas/reports) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `STG_BANK` (BASE, /data/sas/staging/banking) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:customer_profitability:s21` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:21`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:21 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `report_month, _req=1` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:21 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Leer STG_BANK.CUST_ACCOUNTS_DAILY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:customer_profitability:s35` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36`
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_21_macro_call_1`
- **Propiedades:**
  - `TABLE` = `cust_accounts_daily` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería stg_bank es de tipo BASE en /data/sas/staging/banking: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:customer_profitability:op_36_read_1_row_count`, `vc_m:customer_profitability:op_36_read_1_schema`

### 3. Filtrar filas (WHERE): a.SNAPSHOT_DATE = "&month_end"d

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s35` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_36_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 36): SAS `a.SNAPSHOT_DATE = "&month_end"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:customer_profitability:op_36_filter_1_row_count`, `vc_m:customer_profitability:op_36_filter_1_nulls`, `vc_m:customer_profitability:op_36_filter_1_empty`

### 4. Agregar por a.CUSTOMER_ID

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s35` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_36_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `CUSTOMER_ID` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36 · nombre oficial
  - `OPERATIONS` (Operations) = `CUSTOMER_SEGMENT = max(CUSTOMER_SEGMENT); REGION_CODE = max(REGION_CODE); BRANCH_ID = max(BRANCH_ID); NUM_ACCOUNTS = count(ACCOUNT_ID)` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36 · nombre oficial
- **Esquema:** `CUSTOMER_ID`, `CUSTOMER_SEGMENT`, `REGION_CODE`, `BRANCH_ID`, `sum(case when a.ACCOUNT_TYPE in ('MTG','AUTO','PERS','CC','LOC','HELC') then a.CURRENT_BALANCE * a.INTEREST_RATE / 12 else 0 end) as LENDING_INCOME format=dollar18.2`, `sum(case when a.ACCOUNT_TYPE in ('CHK','SAV','MMA','CD','IRA') then a.CURRENT_BALANCE * a.INTEREST_RATE / 12 else 0 end) as DEPOSIT_COST format=dollar18.2`, `calculated LENDING_INCOME - calculated DEPOSIT_COST as NET_INTEREST_INCOME format=dollar18.2`, `NUM_ACCOUNTS`, `sum(a.CURRENT_BALANCE) as TOTAL_RELATIONSHIP format=dollar18.2` _(tipos por determinar)_
- **Pruebas:** `vc_m:customer_profitability:op_36_aggregate_1_aggregates`, `vc_m:customer_profitability:op_36_aggregate_1_numeric`

### 5. Escribir WORK.INTEREST_INCOME (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:customer_profitability:s35` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36`
- **Conexiones:** Main desde `m:customer_profitability:op_36_aggregate_1`
- **Propiedades:**
  - `TABLE` = `interest_income` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:36
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:customer_profitability:op_36_write_1_row_count`, `vc_m:customer_profitability:op_36_write_1_schema`

### 6. Leer CURATED.DAILY_TRANSACTIONS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:customer_profitability:s65` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66`
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_36_write_1`
- **Propiedades:**
  - `TABLE` = `daily_transactions` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:customer_profitability:op_66_read_1_row_count`, `vc_m:customer_profitability:op_66_read_1_schema`

### 7. Filtrar filas (WHERE): t.TRANSACTION_DATE between "&month_start"d and "&month_end"d

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s65` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_66_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 66): SAS `t.TRANSACTION_DATE between "&month_start"d and "&month_end"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:customer_profitability:op_66_filter_1_row_count`, `vc_m:customer_profitability:op_66_filter_1_nulls`, `vc_m:customer_profitability:op_66_filter_1_empty`

### 8. Agregar por t.CUSTOMER_ID

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s65` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_66_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `CUSTOMER_ID` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66 · nombre oficial
  - `OPERATIONS` (Operations) = `TXN_VOLUME = count(*)` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66 · nombre oficial
- **Esquema:** `CUSTOMER_ID`, `sum(case when t.TRANSACTION_TYPE = 'FEE' then abs(t.TRANSACTION_AMOUNT) else 0 end) as FEE_INCOME format=dollar18.2`, `sum(case when t.TRANSACTION_TYPE = 'INT' then abs(t.TRANSACTION_AMOUNT) else 0 end) as INT_CREDITED format=dollar18.2`, `TXN_VOLUME` _(tipos por determinar)_
- **Pruebas:** `vc_m:customer_profitability:op_66_aggregate_1_aggregates`, `vc_m:customer_profitability:op_66_aggregate_1_numeric`

### 9. Escribir WORK.FEE_INCOME (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:customer_profitability:s65` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66`
- **Conexiones:** Main desde `m:customer_profitability:op_66_aggregate_1`
- **Propiedades:**
  - `TABLE` = `fee_income` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:66
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:customer_profitability:op_66_write_1_row_count`, `vc_m:customer_profitability:op_66_write_1_schema`

### 10. Leer CURATED.RISK_SCORES

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:customer_profitability:s85` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86`
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_66_write_1`
- **Propiedades:**
  - `TABLE` = `risk_scores` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:customer_profitability:op_86_read_1_row_count`, `vc_m:customer_profitability:op_86_read_1_schema`

### 11. Leer CURATED.RISK_SCORES

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:customer_profitability:s85` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86`
- **Propiedades:**
  - `TABLE` = `risk_scores` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería curated es de tipo BASE en /data/sas/curated: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:customer_profitability:op_86_read_2_row_count`, `vc_m:customer_profitability:op_86_read_2_schema`

### 12. Filtrar filas (WHERE): r.SCORE_DATE = (select max(SCORE_DATE) from CURATED.RISK_SCORES where SCORE_DATE

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s85` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_86_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 86): SAS `r.SCORE_DATE = (select max(SCORE_DATE) from CURATED.RISK_SCORES where SCORE_DATE <= "&month_end"d)` → _sin traducción automática_
  - ⚠ Sin traducción automática: paréntesis sin cerrar
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:customer_profitability:op_86_filter_1_row_count`, `vc_m:customer_profitability:op_86_filter_1_nulls`, `vc_m:customer_profitability:op_86_filter_1_empty`

### 13. Agregar por r.CUSTOMER_ID

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s85` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_86_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `CUSTOMER_ID` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86 · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `CUSTOMER_ID`, `sum(r.EXPECTED_LOSS) as TOTAL_ECL format=dollar18.2` _(tipos por determinar)_
- **Pruebas:** `vc_m:customer_profitability:op_86_aggregate_1_aggregates`, `vc_m:customer_profitability:op_86_aggregate_1_numeric`

### 14. Escribir WORK.ECL (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:customer_profitability:s85` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86`
- **Conexiones:** Main desde `m:customer_profitability:op_86_aggregate_1`
- **Propiedades:**
  - `TABLE` = `ecl` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:86
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:customer_profitability:op_86_write_1_row_count`, `vc_m:customer_profitability:op_86_write_1_schema`

### 15. Leer WORK.INTEREST_INCOME

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:customer_profitability:s100` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100`
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_86_write_1`
- **Propiedades:**
  - `TABLE` = `interest_income` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:customer_profitability:op_36_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:customer_profitability:op_100_read_1_row_count`, `vc_m:customer_profitability:op_100_read_1_schema`

### 16. Leer WORK.FEE_INCOME

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:customer_profitability:s100` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100`
- **Propiedades:**
  - `TABLE` = `fee_income` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:customer_profitability:op_66_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:customer_profitability:op_100_read_2_row_count`, `vc_m:customer_profitability:op_100_read_2_schema`

### 17. Leer WORK.ECL

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:customer_profitability:s100` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100`
- **Propiedades:**
  - `TABLE` = `ecl` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:customer_profitability:op_86_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:customer_profitability:op_100_read_3_row_count`, `vc_m:customer_profitability:op_100_read_3_schema`

### 18. Unir (merge_by): work.interest_income, work.fee_income, work.ecl

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:customer_profitability:s100` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_100_read_1`, Lookup desde `m:customer_profitability:op_100_read_2`, Lookup desde `m:customer_profitability:op_100_read_3`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `CUSTOMER_ID` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
- **Esquema:** `CUSTOMER_ID` _(tipos por determinar)_
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_m:customer_profitability:op_100_join_1_duplicates`, `vc_m:customer_profitability:op_100_join_1_row_count`, `vc_m:customer_profitability:op_100_join_1_nulls`

### 19. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:customer_profitability:s100` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:customer_profitability:op_100_join_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `4 asignaciones, 6 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `NUM_ACCOUNTS`, `OPERATING_COST`, `TOTAL_REVENUE`, `NET_PROFIT`, `REPORT_MONTH` _(tipos por determinar)_
- **Expresión** (línea 109): SAS `NUM_ACCOUNTS * 15` → Java `(input_row.NUM_ACCOUNTS * 15)`
- **Expresión** (línea 113): SAS `sum(NET_INTEREST_INCOME, FEE_INCOME, 0)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función sum
- **Expresión** (línea 117): SAS `TOTAL_REVENUE - OPERATING_COST - coalesce(TOTAL_ECL, 0)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función coalesce
- **Expresión** (línea 134): SAS `"&report_month"` → Java `"&report_month"`
- **Expresión** (línea 121): SAS `if TOTAL_RELATIONSHIP > 0 then
      ROA = (NET_PROFIT * 12) / TOTAL_RELATIONSHIP` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 123): SAS `else
      ROA = .` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 129): SAS `if NET_PROFIT >= 500    then PROFIT_TIER = 'Highly Profitable'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 130): SAS `else if NET_PROFIT >= 100 then PROFIT_TIER = 'Profitable'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 131): SAS `else if NET_PROFIT >= 0   then PROFIT_TIER = 'Marginal'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 132): SAS `else PROFIT_TIER = 'Unprofitable'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:customer_profitability:op_100_compute_1_nulls`, `vc_m:customer_profitability:op_100_compute_1_dates`, `vc_m:customer_profitability:op_100_compute_1_numeric`

### 20. Escribir REPORTS.CUSTOMER_PNL

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:customer_profitability:s100` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100`
- **Conexiones:** Main desde `m:customer_profitability:op_100_compute_1`
- **Propiedades:**
  - `TABLE` = `customer_pnl` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:100
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:customer_profitability:op_100_write_1_row_count`, `vc_m:customer_profitability:op_100_write_1_schema`

### 21. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s140` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:140`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_100_write_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_m:customer_profitability:op_140_aggregate_1_aggregates`, `vc_m:customer_profitability:op_140_aggregate_1_numeric`

### 22. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:customer_profitability:s150` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:150`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_140_aggregate_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_m:customer_profitability:op_150_aggregate_1_aggregates`, `vc_m:customer_profitability:op_150_aggregate_1_numeric`

### 23. Invocar macro %export_xlsx

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:customer_profitability:s159` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:159`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_150_aggregate_1`
- **Propiedades:**
  - `PROCESS` (Job) = `export_xlsx` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:159 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
    data=REPORTS.SEGMENT_PROFITABILITY,
    file=&REPORT_PATH/PROFITABILITY_&report_month..xlsx,
    sheet=By_Segment
  ` — SAS real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:159 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 24. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:customer_profitability:s170` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:170`
- **Conexiones:** OnSubjobOk desde `m:customer_profitability:op_159_macro_call_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Sin resolver

- include /opt/sas/custom/macros/parmv.sas (real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:15) — external
- include /opt/sas/custom/macros/nobs.sas (real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:16) — external
- include /opt/sas/custom/macros/export_xlsx.sas (real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:17) — external
- macro parmv (real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:21) — sin definición en el proyecto
- macro export_xlsx (real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:159) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas:167) — sin definición en el proyecto

## Casos de validación

- `vc_m:customer_profitability:op_36_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:customer_profitability:op_36_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:customer_profitability:op_36_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:customer_profitability:op_36_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:customer_profitability:op_36_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:customer_profitability:op_36_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:customer_profitability:op_36_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:customer_profitability:op_36_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:customer_profitability:op_36_write_1_schema` (schema): Esquema destino
- `vc_m:customer_profitability:op_66_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:customer_profitability:op_66_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:customer_profitability:op_66_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:customer_profitability:op_66_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:customer_profitability:op_66_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:customer_profitability:op_66_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:customer_profitability:op_66_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:customer_profitability:op_66_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:customer_profitability:op_66_write_1_schema` (schema): Esquema destino
- `vc_m:customer_profitability:op_86_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:customer_profitability:op_86_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:customer_profitability:op_86_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:customer_profitability:op_86_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:customer_profitability:op_86_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:customer_profitability:op_86_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:customer_profitability:op_86_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:customer_profitability:op_86_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:customer_profitability:op_86_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:customer_profitability:op_86_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:customer_profitability:op_86_write_1_schema` (schema): Esquema destino
- `vc_m:customer_profitability:op_100_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:customer_profitability:op_100_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:customer_profitability:op_100_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:customer_profitability:op_100_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:customer_profitability:op_100_read_3_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:customer_profitability:op_100_read_3_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:customer_profitability:op_100_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:customer_profitability:op_100_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:customer_profitability:op_100_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:customer_profitability:op_100_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:customer_profitability:op_100_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:customer_profitability:op_100_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:customer_profitability:op_100_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:customer_profitability:op_100_write_1_schema` (schema): Esquema destino
- `vc_m:customer_profitability:op_140_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:customer_profitability:op_140_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:customer_profitability:op_150_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:customer_profitability:op_150_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
