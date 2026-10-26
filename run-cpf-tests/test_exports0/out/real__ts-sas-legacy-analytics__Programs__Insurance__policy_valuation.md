# Job `job_policy_valuation`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas` (sha256 `d732c84ab0e6`)
- **Instrucciones:** 27 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%policy_valuation(val_date, lob)` está integrada en el Job.

## Orquestación

- Planificación: Monthly 5th business day via Control-M INS_MONTHLY_01
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas#2`

### Recomendaciones Grid

### `sas_macro_step.include_dispatch` (partial)

- **Accion:** Crea un Job hijo para cada programa resuelto y confirma sus parámetros antes de conectar la secuencia.
- **Motivo/limite:** The analyzer resolves tested macro dispatches, but macro defaults and failure behavior require review.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:112` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas#1`
- **Confirmar:** Review macro dispatch semantics; Confirm child Job and context parameters
- **Datos interpretados:**

```json
{
  "kind": "sas_macro_step",
  "program": "/opt/sas/custom/programs/Insurance/policy_valuation.sas",
  "resolved_program": "real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas",
  "match_status": "resolved",
  "job_name": null,
  "queue": null,
  "waits": true,
  "params": {
    "step_num": "2",
    "step_name": "Policy Valuation",
    "program": "/opt/sas/custom/programs/Insurance/policy_valuation.sas"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:10` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Monthly 5th business day via Control-M INS_MONTHLY_01"
}
```

## Variables de contexto

- `context.CURR_DT` ← SAS `CURR_DT` (Variable SAS referenciada por %policy_valuation(val_date=...))
- `context.lob` ← SAS `lob` (Parámetro de la macro principal %policy_valuation; argumento SAS: sin asignar)
- `context.val_date` ← SAS `val_date` (Parámetro de la macro principal %policy_valuation; argumento SAS: &CURR_DT)

## Conexiones a crear

- `RAW_INS` (BASE, /data/sas/raw/insurance) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `REPORTS` (BASE, /data/sas/reports) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `STG_INS` (BASE, /data/sas/staging/insurance) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:policy_valuation:s19` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:19`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:19 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `val_date, _req=1` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:19 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:policy_valuation:s20` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:20`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_19_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:20 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `lob, _req=0, _val=ALL AUTO HOME WL TL UL HLTH` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:20 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Leer RAW_INS.POLICIES

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:policy_valuation:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35`
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_20_macro_call_1`
- **Propiedades:**
  - `TABLE` = `policies` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería raw_ins es de tipo BASE en /data/sas/raw/insurance: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:policy_valuation:op_35_read_1_row_count`, `vc_m:policy_valuation:op_35_read_1_schema`

### 4. Filtrar filas (WHERE): p.STATUS = 'ACTIVE' and p.EFFECTIVE_DATE <= "&val_date"d and p.EXPIRATION_DATE >

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:policy_valuation:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_35_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 35): SAS `p.STATUS = 'ACTIVE' and p.EFFECTIVE_DATE <= "&val_date"d and p.EXPIRATION_DATE >= "&val_date"d %if &lob ne ALL %then %do` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ' %if &lob ne'
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:policy_valuation:op_35_filter_1_row_count`, `vc_m:policy_valuation:op_35_filter_1_nulls`, `vc_m:policy_valuation:op_35_filter_1_empty`

### 5. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:policy_valuation:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_35_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `POLICY_ID`, `CUSTOMER_ID`, `POLICY_TYPE`, `EFFECTIVE_DATE`, `EXPIRATION_DATE`, `ANNUAL_PREMIUM`, `SUM_INSURED`, `DEDUCTIBLE`, `RISK_CATEGORY`, `UNDERWRITING_CLASS`, `AGENT_ID`, `BRANCH_CODE`, `POLICY_AGE_MONTHS`, `MONTHS_TO_EXPIRY`, `case when p.EXPIRATION_DATE <= intnx('month', "&val_date"d, 3) then 'Y' else 'N' end as RENEWAL_DUE_FLAG length=1`, `p.ANNUAL_PREMIUM / 12 * min(12, intck('month', max(p.EFFECTIVE_DATE, intnx('year', "&val_date"d, 0, 'B')), min("&val_date"d, p.EXPIRATION_DATE))) as YTD_EARNED_PREMIUM format=dollar18.2` _(tipos por determinar)_
- **Pruebas:** `vc_m:policy_valuation:op_35_aggregate_1_aggregates`, `vc_m:policy_valuation:op_35_aggregate_1_numeric`

### 6. Escribir WORK.INFORCE (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:policy_valuation:s34` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35`
- **Conexiones:** Main desde `m:policy_valuation:op_35_aggregate_1`
- **Propiedades:**
  - `TABLE` = `inforce` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:35
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:policy_valuation:op_35_write_1_row_count`, `vc_m:policy_valuation:op_35_write_1_schema`

### 7. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:policy_valuation:s34` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:67`
- **Conexiones:** Main desde `m:policy_valuation:op_35_write_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 8. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:policy_valuation:s34` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:69`
- **Conexiones:** Main desde `m:policy_valuation:op_67_unsupported_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 9. Leer RAW_INS.CLAIMS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:policy_valuation:s78` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79`
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_69_unsupported_1`
- **Propiedades:**
  - `TABLE` = `claims` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería raw_ins es de tipo BASE en /data/sas/raw/insurance: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:policy_valuation:op_79_read_1_row_count`, `vc_m:policy_valuation:op_79_read_1_schema`

### 10. Filtrar filas (WHERE): c.LOSS_DATE >= intnx('month', "&val_date"d, -12) and c.LOSS_DATE <= "&val_date"d

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:policy_valuation:s78` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_79_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 79): SAS `c.LOSS_DATE >= intnx('month', "&val_date"d, -12) and c.LOSS_DATE <= "&val_date"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intnx
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:policy_valuation:op_79_filter_1_row_count`, `vc_m:policy_valuation:op_79_filter_1_nulls`, `vc_m:policy_valuation:op_79_filter_1_empty`

### 11. Agregar por c.POLICY_ID

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:policy_valuation:s78` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_79_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `POLICY_ID` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79 · nombre oficial
  - `OPERATIONS` (Operations) = `NUM_CLAIMS = count(CLAIM_ID); DENIED_CLAIMS = sum(CLAIM_STATUS = 'DENY' then 1 else 0 end)` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79 · nombre oficial
- **Esquema:** `POLICY_ID`, `NUM_CLAIMS`, `sum(c.INCURRED_AMOUNT) as TOTAL_INCURRED format=dollar18.2`, `sum(c.PAID_AMOUNT) as TOTAL_PAID format=dollar18.2`, `sum(c.RESERVED_AMOUNT) as TOTAL_RESERVED format=dollar18.2`, `max(c.LOSS_DATE) as LAST_CLAIM_DATE format=date9.`, `sum(case when c.CLAIM_STATUS in ('OPEN','INV','ADJ','PEND') then c.RESERVED_AMOUNT else 0 end) as OPEN_RESERVES format=dollar18.2`, `DENIED_CLAIMS` _(tipos por determinar)_
- **Pruebas:** `vc_m:policy_valuation:op_79_aggregate_1_aggregates`, `vc_m:policy_valuation:op_79_aggregate_1_numeric`

### 12. Escribir WORK.CLAIMS_EXP (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:policy_valuation:s78` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79`
- **Conexiones:** Main desde `m:policy_valuation:op_79_aggregate_1`
- **Propiedades:**
  - `TABLE` = `claims_exp` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:79
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:policy_valuation:op_79_write_1_row_count`, `vc_m:policy_valuation:op_79_write_1_schema`

### 13. Leer RAW_INS.PREMIUMS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:policy_valuation:s102` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103`
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_79_write_1`
- **Propiedades:**
  - `TABLE` = `premiums` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería raw_ins es de tipo BASE en /data/sas/raw/insurance: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:policy_valuation:op_103_read_1_row_count`, `vc_m:policy_valuation:op_103_read_1_schema`

### 14. Filtrar filas (WHERE): PAYMENT_DATE >= intnx('year', "&val_date"d, 0, 'B') and PAYMENT_DATE <= "&val_da

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:policy_valuation:s102` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_103_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 103): SAS `PAYMENT_DATE >= intnx('year', "&val_date"d, 0, 'B') and PAYMENT_DATE <= "&val_date"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intnx
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:policy_valuation:op_103_filter_1_row_count`, `vc_m:policy_valuation:op_103_filter_1_nulls`, `vc_m:policy_valuation:op_103_filter_1_empty`

### 15. Agregar por POLICY_ID

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:policy_valuation:s102` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_103_filter_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = `POLICY_ID` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103 · nombre oficial
  - `OPERATIONS` (Operations) = `LATE_PAYMENTS = count(case when PAYMENT_STATUS = 'LATE' then 1 end)` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103 · nombre oficial
- **Esquema:** `POLICY_ID`, `sum(PREMIUM_AMOUNT) as COLLECTED_PREMIUM format=dollar18.2`, `sum(case when PAYMENT_STATUS = 'RETURNED' then PREMIUM_AMOUNT else 0 end) as RETURNED_PREMIUM format=dollar18.2`, `max(PAYMENT_DATE) as LAST_PAYMENT_DATE format=date9.`, `LATE_PAYMENTS` _(tipos por determinar)_
- **Pruebas:** `vc_m:policy_valuation:op_103_aggregate_1_aggregates`, `vc_m:policy_valuation:op_103_aggregate_1_numeric`

### 16. Escribir WORK.PREMIUM_COLL (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:policy_valuation:s102` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103`
- **Conexiones:** Main desde `m:policy_valuation:op_103_aggregate_1`
- **Propiedades:**
  - `TABLE` = `premium_coll` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:103
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:policy_valuation:op_103_write_1_row_count`, `vc_m:policy_valuation:op_103_write_1_schema`

### 17. Leer WORK.INFORCE

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:policy_valuation:s123` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123`
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_103_write_1`
- **Propiedades:**
  - `TABLE` = `inforce` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:policy_valuation:op_35_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:policy_valuation:op_123_read_1_row_count`, `vc_m:policy_valuation:op_123_read_1_schema`

### 18. Leer WORK.CLAIMS_EXP

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:policy_valuation:s123` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123`
- **Propiedades:**
  - `TABLE` = `claims_exp` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:policy_valuation:op_79_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:policy_valuation:op_123_read_2_row_count`, `vc_m:policy_valuation:op_123_read_2_schema`

### 19. Leer WORK.PREMIUM_COLL

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:policy_valuation:s123` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123`
- **Propiedades:**
  - `TABLE` = `premium_coll` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:policy_valuation:op_103_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:policy_valuation:op_123_read_3_row_count`, `vc_m:policy_valuation:op_123_read_3_schema`

### 20. Unir (merge_by): work.inforce, work.claims_exp, work.premium_coll

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:policy_valuation:s123` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_123_read_1`, Lookup desde `m:policy_valuation:op_123_read_2`, Lookup desde `m:policy_valuation:op_123_read_3`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `POLICY_ID` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
- **Esquema:** `POLICY_ID` _(tipos por determinar)_
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_m:policy_valuation:op_123_join_1_duplicates`, `vc_m:policy_valuation:op_123_join_1_row_count`, `vc_m:policy_valuation:op_123_join_1_nulls`

### 21. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:policy_valuation:s123` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_123_join_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 7 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `IBNR_ESTIMATE`, `TOTAL_RESERVE`, `VALUATION_DATE` _(tipos por determinar)_
- **Expresión** (línea 155): SAS `max(0, YTD_EARNED_PREMIUM * 0.15 - coalesce(TOTAL_PAID, 0))` → _sin traducción automática_
  - ⚠ Sin traducción automática: función max
- **Expresión** (línea 159): SAS `coalesce(OPEN_RESERVES, 0) + IBNR_ESTIMATE` → _sin traducción automática_
  - ⚠ Sin traducción automática: función coalesce
- **Expresión** (línea 162): SAS `"&val_date"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Expresión** (línea 136): SAS `if YTD_EARNED_PREMIUM > 0 then
      LOSS_RATIO = coalesce(TOTAL_INCURRED, 0) / YTD_EARNED_PREMIUM` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 138): SAS `else
      LOSS_RATIO = .` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 143): SAS `if YTD_EARNED_PREMIUM > 0 then
      COMBINED_RATIO = LOSS_RATIO + 0.30` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 145): SAS `else
      COMBINED_RATIO = .` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 150): SAS `if COMBINED_RATIO = . then PREMIUM_ADEQUATE = 'N'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 151): SAS `else if COMBINED_RATIO > 1.0 then PREMIUM_ADEQUATE = 'N'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 152): SAS `else PREMIUM_ADEQUATE = 'Y'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:policy_valuation:op_123_compute_1_nulls`, `vc_m:policy_valuation:op_123_compute_1_dates`, `vc_m:policy_valuation:op_123_compute_1_numeric`

### 22. Escribir STG_INS.POLICY_VALUATION

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:policy_valuation:s123` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123`
- **Conexiones:** Main desde `m:policy_valuation:op_123_compute_1`
- **Propiedades:**
  - `TABLE` = `policy_valuation` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:123
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería stg_ins es de tipo BASE en /data/sas/staging/insurance: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:policy_valuation:op_123_write_1_row_count`, `vc_m:policy_valuation:op_123_write_1_schema`

### 23. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:policy_valuation:s169` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:169`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_123_write_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_m:policy_valuation:op_169_aggregate_1_aggregates`, `vc_m:policy_valuation:op_169_aggregate_1_numeric`

### 24. Leer REPORTS.LOSS_RATIO_SUMMARY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:policy_valuation:s184` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184`
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_169_aggregate_1`
- **Propiedades:**
  - `TABLE` = `loss_ratio_summary` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:policy_valuation:op_184_read_1_row_count`, `vc_m:policy_valuation:op_184_read_1_schema`

### 25. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:policy_valuation:s184` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:policy_valuation:op_184_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 1 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `TOTAL_EARNED`, `TOTAL_INCURRED`, `AGG_LOSS_RATIO`, `AGG_COMBINED_RATIO` _(tipos por determinar)_
- **Expresión** (línea 187): SAS `TOTAL_INCURRED / TOTAL_EARNED` → Java `(input_row.TOTAL_INCURRED / input_row.TOTAL_EARNED)`
- **Expresión** (línea 188): SAS `AGG_LOSS_RATIO + 0.30` → Java `(input_row.AGG_LOSS_RATIO + 0.30)`
- **Expresión** (línea 186): SAS `if TOTAL_EARNED > 0 then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:policy_valuation:op_184_compute_1_nulls`, `vc_m:policy_valuation:op_184_compute_1_dates`, `vc_m:policy_valuation:op_184_compute_1_numeric`

### 26. Escribir REPORTS.LOSS_RATIO_SUMMARY

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:policy_valuation:s184` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184`
- **Conexiones:** Main desde `m:policy_valuation:op_184_compute_1`
- **Propiedades:**
  - `TABLE` = `loss_ratio_summary` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:184
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería reports es de tipo BASE en /data/sas/reports: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:policy_valuation:op_184_write_1_row_count`, `vc_m:policy_valuation:op_184_write_1_schema`

### 27. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:policy_valuation:s200` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:200`
- **Conexiones:** OnSubjobOk desde `m:policy_valuation:op_184_write_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Sin resolver

- include /opt/sas/custom/macros/parmv.sas (real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:14) — external
- include /opt/sas/custom/macros/nobs.sas (real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:15) — external
- macro parmv (real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:19) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:20) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:73) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas:197) — sin definición en el proyecto

## Casos de validación

- `vc_m:policy_valuation:op_35_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:policy_valuation:op_35_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:policy_valuation:op_35_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:policy_valuation:op_35_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:policy_valuation:op_35_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:policy_valuation:op_35_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:policy_valuation:op_35_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:policy_valuation:op_35_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:policy_valuation:op_35_write_1_schema` (schema): Esquema destino
- `vc_m:policy_valuation:op_79_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:policy_valuation:op_79_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:policy_valuation:op_79_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:policy_valuation:op_79_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:policy_valuation:op_79_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:policy_valuation:op_79_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:policy_valuation:op_79_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:policy_valuation:op_79_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:policy_valuation:op_79_write_1_schema` (schema): Esquema destino
- `vc_m:policy_valuation:op_103_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:policy_valuation:op_103_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:policy_valuation:op_103_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:policy_valuation:op_103_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:policy_valuation:op_103_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:policy_valuation:op_103_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:policy_valuation:op_103_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:policy_valuation:op_103_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:policy_valuation:op_103_write_1_schema` (schema): Esquema destino
- `vc_m:policy_valuation:op_123_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:policy_valuation:op_123_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:policy_valuation:op_123_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:policy_valuation:op_123_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:policy_valuation:op_123_read_3_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:policy_valuation:op_123_read_3_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:policy_valuation:op_123_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:policy_valuation:op_123_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:policy_valuation:op_123_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:policy_valuation:op_123_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:policy_valuation:op_123_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:policy_valuation:op_123_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:policy_valuation:op_123_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:policy_valuation:op_123_write_1_schema` (schema): Esquema destino
- `vc_m:policy_valuation:op_169_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_m:policy_valuation:op_169_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_m:policy_valuation:op_184_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:policy_valuation:op_184_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:policy_valuation:op_184_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:policy_valuation:op_184_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:policy_valuation:op_184_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:policy_valuation:op_184_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:policy_valuation:op_184_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
