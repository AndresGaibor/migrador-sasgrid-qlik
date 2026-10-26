# Job `job_claims_processing`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas` (sha256 `febd3f80e2f7`)
- **Instrucciones:** 30 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

La macro principal `%claims_processing(proc_date)` está integrada en el Job.

## Orquestación

- Planificación: Daily 08:00 via Control-M INS_DAILY_01
- Tareas Grid: `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas#1`

### Recomendaciones Grid

### `sas_macro_step.include_dispatch` (partial)

- **Accion:** Crea un Job hijo para cada programa resuelto y confirma sus parámetros antes de conectar la secuencia.
- **Motivo/limite:** The analyzer resolves tested macro dispatches, but macro defaults and failure behavior require review.
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas:109` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Confirmar:** Review macro dispatch semantics; Confirm child Job and context parameters
- **Datos interpretados:**

```json
{
  "kind": "sas_macro_step",
  "program": "/opt/sas/custom/programs/Insurance/claims_processing.sas",
  "resolved_program": "real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas",
  "match_status": "resolved",
  "job_name": null,
  "queue": null,
  "waits": true,
  "params": {
    "step_num": "1",
    "step_name": "Claims Processing",
    "program": "/opt/sas/custom/programs/Insurance/claims_processing.sas"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `scheduler.control_m` (partial)

- **Accion:** Obtén la definición real de Control-M y recrea calendario y dependencias en el planificador elegido.
- **Motivo/limite:** Only a comment is captured; Control-M calendars, dependencies, and job definitions are not parsed.
- **Evidencia:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:10` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Daily 08:00 via Control-M INS_DAILY_01"
}
```

## Variables de contexto

- `context.CURR_DT` ← SAS `CURR_DT` (Variable SAS referenciada por %claims_processing(proc_date=...))
- `context.EMAIL_ONCALL` ← SAS `EMAIL_ONCALL` (&EMAIL_ONCALL en real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:209)
- `context.feed_ds` ← SAS `feed_ds` (&feed_ds en real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38)
- `context.nobs_fraud` ← SAS `nobs_fraud` (&nobs_fraud en real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:209)
- `context.proc_date` ← SAS `proc_date` (&proc_date en real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:209)

## Conexiones a crear

- `STG_INS` (BASE, /data/sas/staging/insurance) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `TERA_DW` (teradata, tdprod.internal.corp) → tTeradataConnection. Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:claims_processing:s20` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:20`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:20 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `proc_date, _req=1` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:20 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Leer RAW_INS.&feed_ds

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:claims_processing:s38` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_20_macro_call_1`
- **Propiedades:**
  - `TABLE` = `&feed_ds` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:claims_processing:op_38_read_1_row_count`, `vc_m:claims_processing:op_38_read_1_schema`

### 3. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:claims_processing:s38` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_38_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `4 asignaciones, 4 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `rc`, `VALIDATION_ERROR` _(tipos por determinar)_
- **Expresión** (línea 57): SAS `h_pol.find()` → _sin traducción automática_
  - ⚠ Sin traducción automática: función h_pol.find
- **Expresión** (línea 60): SAS `catx(' ', 'Policy not found or inactive:', POLICY_ID)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función catx
- **Expresión** (línea 67): SAS `catx(' ', 'Loss date', put(LOSS_DATE, date9.),
        'outside policy period',
        put(EFFECTIVE_DATE, date9.), '-', put(EXPIRATION_DATE, date9.))` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ".), 'outside"
- **Expresión** (línea 76): SAS `catx(' ', 'Claimed amount',
        put(CLAIMED_AMOUNT, dollar18.2), 'exceeds sum insured',
        put(SUM_INSURED, dollar18.2))` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ".2), 'exceed"
- **Expresión** (línea 46): SAS `if _N_ = 1 then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 59): SAS `if rc ne 0 then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 66): SAS `if LOSS_DATE < EFFECTIVE_DATE or LOSS_DATE > EXPIRATION_DATE then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 75): SAS `if CLAIMED_AMOUNT > SUM_INSURED then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:claims_processing:op_38_compute_1_nulls`, `vc_m:claims_processing:op_38_compute_1_dates`, `vc_m:claims_processing:op_38_compute_1_numeric`

### 4. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `m:claims_processing:s38` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38`
- **Conexiones:** Main desde `m:claims_processing:op_38_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_m:claims_processing:op_38_stateful_1_ordering`, `vc_m:claims_processing:op_38_stateful_1_duplicates`

### 5. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:claims_processing:s38` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_38_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: VALIDATION_ERROR, rc` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38 · nombre oficial
- **Pruebas:** `vc_m:claims_processing:op_38_select_columns_1_schema`

### 6. Escribir WORK.CLAIMS_VALID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:claims_processing:s38` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38`
- **Conexiones:** Main desde `m:claims_processing:op_38_select_columns_1`
- **Propiedades:**
  - `TABLE` = `claims_valid` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:claims_processing:op_38_write_1_row_count`, `vc_m:claims_processing:op_38_write_1_schema`

### 7. Escribir WORK.CLAIMS_INVALID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:claims_processing:s38` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38`
- **Conexiones:** Main desde `m:claims_processing:op_38_write_1`
- **Propiedades:**
  - `TABLE` = `claims_invalid` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:claims_processing:op_38_write_2_row_count`, `vc_m:claims_processing:op_38_write_2_schema`

### 8. Leer WORK.CLAIMS_VALID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:claims_processing:s93` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_38_write_2`
- **Propiedades:**
  - `TABLE` = `claims_valid` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:claims_processing:op_38_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:claims_processing:op_94_read_1_row_count`, `vc_m:claims_processing:op_94_read_1_schema`

### 9. Leer TERA_DW.FRAUD_INDICATORS

- **Acción:** add_component · **Componente:** `tTeradataInput` ![Icono Talend](assets/talend-icons/tTeradataInput_icon32.png) (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:claims_processing:s93` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatainput-standard-properties) · variantes: `tAS400Input`, `tAccessInput`, `tAmazonAuroraInput`, `tAmazonOracleInput`, `tApacheLogInput`, `tAzureSynapseInput`, `tBigQueryInput`, `tDB2Input`
- **Propiedades:**
  - `TABLE` (Table Name) = `fraud_indicators` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94 · nombre oficial
  - `QUERY` (Query) = _por configurar_ — regla mappings · nombre oficial
  - `CONNECTION` (Component List) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Librería tera_dw usa el motor teradata
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:claims_processing:op_94_read_2_row_count`, `vc_m:claims_processing:op_94_read_2_schema`

### 10. Unir (left join): work.claims_valid, tera_dw.fraud_indicators

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:claims_processing:s93` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_94_read_1`, Lookup desde `m:claims_processing:op_94_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `c.POLICY_ID = f.POLICY_ID, c.CLAIMANT_ID = f.CLAIMANT_ID` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94
- **Esquema:** `POLICY_ID`, `CLAIMANT_ID` _(tipos por determinar)_
- **Expresión** (línea 94): SAS `on c.POLICY_ID = f.POLICY_ID and c.CLAIMANT_ID = f.CLAIMANT_ID` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_m:claims_processing:op_94_join_1_duplicates`, `vc_m:claims_processing:op_94_join_1_row_count`, `vc_m:claims_processing:op_94_join_1_nulls`

### 11. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:claims_processing:s93` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_94_join_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*, FRAUD_SCORE, INDICATOR_FLAGS, case when f.FRAUD_SCORE >= 80 then 'HIGH' when f.FRAUD_SCORE >= 50 then 'MEDIUM' else 'LOW' end as FRAUD_RISK length=6` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `FRAUD_SCORE`, `INDICATOR_FLAGS` _(tipos por determinar)_
- **Expresión** (línea 94): SAS `case when f.FRAUD_SCORE >= 80 then 'HIGH' when f.FRAUD_SCORE >= 50 then 'MEDIUM' else 'LOW' end as FRAUD_RISK length=6` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pruebas:** `vc_m:claims_processing:op_94_project_1_schema`

### 12. Escribir WORK.FRAUD_CHECK (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:claims_processing:s93` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94`
- **Conexiones:** Main desde `m:claims_processing:op_94_project_1`
- **Propiedades:**
  - `TABLE` = `fraud_check` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:94
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:claims_processing:op_94_write_1_row_count`, `vc_m:claims_processing:op_94_write_1_schema`

### 13. Leer WORK.FRAUD_CHECK

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:claims_processing:s112` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_94_write_1`
- **Propiedades:**
  - `TABLE` = `fraud_check` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:claims_processing:op_94_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:claims_processing:op_112_read_1_row_count`, `vc_m:claims_processing:op_112_read_1_schema`

### 14. Filtrar filas (sentencia WHERE): FRAUD_RISK = 'HIGH'

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:claims_processing:s112` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:114`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_112_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:114 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `FRAUD_RISK == 'HIGH'` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:114 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:114 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `FRAUD_RISK` _(tipos por determinar)_
- **Expresión** (línea 114): SAS `FRAUD_RISK = 'HIGH'` → Java `input_row.FRAUD_RISK.equals("HIGH")`
- **Pruebas:** `vc_m:claims_processing:op_114_filter_1_row_count`, `vc_m:claims_processing:op_114_filter_1_nulls`, `vc_m:claims_processing:op_114_filter_1_empty`

### 15. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:claims_processing:s112` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_114_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ALERT_REASON`, `ALERT_DATE` _(tipos por determinar)_
- **Expresión** (línea 115): SAS `catx('; ',
      catx(' ', 'Fraud score:', put(FRAUD_SCORE, 4.)),
      INDICATOR_FLAGS)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)), INDICAT'
- **Expresión** (línea 118): SAS `"&proc_date"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:claims_processing:op_112_compute_1_nulls`, `vc_m:claims_processing:op_112_compute_1_dates`, `vc_m:claims_processing:op_112_compute_1_numeric`

### 16. Escribir WORK.FRAUD_ALERTS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:claims_processing:s112` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112`
- **Conexiones:** Main desde `m:claims_processing:op_112_compute_1`
- **Propiedades:**
  - `TABLE` = `fraud_alerts` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:112
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:claims_processing:op_112_write_1_row_count`, `vc_m:claims_processing:op_112_write_1_schema`

### 17. Leer WORK.FRAUD_CHECK

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:claims_processing:s127` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_112_write_1`
- **Propiedades:**
  - `TABLE` = `fraud_check` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:claims_processing:op_94_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:claims_processing:op_127_read_1_row_count`, `vc_m:claims_processing:op_127_read_1_schema`

### 18. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:claims_processing:s127` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_127_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `12 asignaciones, 3 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ADJUDICATION_RESULT`, `ADJUDICATION_REASON`, `APPROVED_AMOUNT` _(tipos por determinar)_
- **Expresión** (línea 137): SAS `'DENY'` → Java `"DENY"`
- **Expresión** (línea 138): SAS `'High fraud risk - SIU referral'` → Java `"High fraud risk - SIU referral"`
- **Expresión** (línea 139): SAS `0` → Java `0`
- **Expresión** (línea 149): SAS `'APPR'` → Java `"APPR"`
- **Expresión** (línea 150): SAS `'Auto-approved: low risk, small claim'` → Java `"Auto-approved: low risk, small claim"`
- **Expresión** (línea 151): SAS `max(0, CLAIMED_AMOUNT - DEDUCTIBLE)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función max
- **Expresión** (línea 161): SAS `'APPR'` → Java `"APPR"`
- **Expresión** (línea 162): SAS `'Auto-approved: within 25% of sum insured'` → Java `"Auto-approved: within 25% of sum insured"`
- **Expresión** (línea 163): SAS `max(0, CLAIMED_AMOUNT - DEDUCTIBLE)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función max
- **Expresión** (línea 169): SAS `'PEND'` → Java `"PEND"`
- **Expresión** (línea 170): SAS `catx('; ',
      ifc(FRAUD_RISK='MEDIUM', 'Medium fraud risk', ''),
      ifc(CLAIMED_AMOUNT > 50000, 'Large claim', ''),
      ifc(CLAIMED_AMOUNT > SUM_INSURED * 0.25, 'Exceeds 25% threshold', ''))` → _sin traducción automática_
  - ⚠ Sin traducción automática: función catx
- **Expresión** (línea 174): SAS `.` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.'
- **Expresión** (línea 136): SAS `if FRAUD_RISK = 'HIGH' then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 145): SAS `if FRAUD_RISK = 'LOW'
      and CLAIMED_AMOUNT <= 5000
      and POLICY_TYPE in ('AUTO','HOME','RENT')
    then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 157): SAS `if FRAUD_RISK = 'LOW'
      and CLAIMED_AMOUNT <= SUM_INSURED * 0.25
      and CLAIMED_AMOUNT <= 50000
    then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:claims_processing:op_127_compute_1_nulls`, `vc_m:claims_processing:op_127_compute_1_dates`, `vc_m:claims_processing:op_127_compute_1_numeric`

### 19. Escribir WORK.AUTO_ADJUDICATED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:claims_processing:s127` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127`
- **Conexiones:** Main desde `m:claims_processing:op_127_compute_1`
- **Propiedades:**
  - `TABLE` = `auto_adjudicated` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:claims_processing:op_127_write_1_row_count`, `vc_m:claims_processing:op_127_write_1_schema`

### 20. Escribir WORK.MANUAL_REVIEW

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:claims_processing:s127` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127`
- **Conexiones:** Main desde `m:claims_processing:op_127_write_1`
- **Propiedades:**
  - `TABLE` = `manual_review` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:127
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:claims_processing:op_127_write_2_row_count`, `vc_m:claims_processing:op_127_write_2_schema`

### 21. Leer WORK.AUTO_ADJUDICATED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:claims_processing:s184` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_127_write_2`
- **Propiedades:**
  - `TABLE` = `auto_adjudicated` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:claims_processing:op_127_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:claims_processing:op_184_read_1_row_count`, `vc_m:claims_processing:op_184_read_1_schema`

### 22. Leer WORK.MANUAL_REVIEW

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:claims_processing:s184` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184`
- **Propiedades:**
  - `TABLE` = `manual_review` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (m:claims_processing:op_127_write_2): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:claims_processing:op_184_read_2_row_count`, `vc_m:claims_processing:op_184_read_2_schema`

### 23. Concatenar entradas

- **Acción:** add_component · **Componente:** `tUnite` ![Icono Talend](assets/talend-icons/tUnite_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:claims_processing:s184` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_184_read_1`
- **Pendientes:**
  - Esquemas compatibles entre entradas
- **Pruebas:** `vc_m:claims_processing:op_184_union_1_row_count`

### 24. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:claims_processing:s184` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:claims_processing:op_184_union_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `PROCESSING_DATE`, `ADJUDICATION_RESULT`, `CLAIM_STATUS` _(tipos por determinar)_
- **Expresión** (línea 188): SAS `"&proc_date"d` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Expresión** (línea 189): SAS `ADJUDICATION_RESULT` → Java `input_row.ADJUDICATION_RESULT`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:claims_processing:op_184_compute_1_nulls`, `vc_m:claims_processing:op_184_compute_1_dates`, `vc_m:claims_processing:op_184_compute_1_numeric`

### 25. Escribir WORK.CLAIMS_COMBINED

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:claims_processing:s184` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184`
- **Conexiones:** Main desde `m:claims_processing:op_184_compute_1`
- **Propiedades:**
  - `TABLE` = `claims_combined` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:184
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:claims_processing:op_184_write_1_row_count`, `vc_m:claims_processing:op_184_write_1_schema`

### 26. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:claims_processing:s194` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:194`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_184_write_1`
- **Propiedades:**
  - `TABLE` = `claims_combined` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:194
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:194
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:194
- **Pendientes:**
  - Tabla base destino
  - Librería stg_ins es de tipo BASE en /data/sas/staging/insurance: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:claims_processing:op_194_append_1_row_count`

### 27. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:claims_processing:s199` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:199`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_194_append_1`
- **Propiedades:**
  - `TABLE` = `manual_review` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:199
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:199
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:199
- **Pendientes:**
  - Tabla base destino
  - Librería stg_ins es de tipo BASE en /data/sas/staging/insurance: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:claims_processing:op_199_append_1_row_count`

### 28. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:claims_processing:s205` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:205`
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_199_append_1`
- **Propiedades:**
  - `TABLE` = `fraud_alerts` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:205
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:205
  - `TABLE_ACTION` = `NONE` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:205
- **Pendientes:**
  - Tabla base destino
  - Librería stg_ins es de tipo BASE en /data/sas/staging/insurance: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:claims_processing:op_205_append_1_row_count`

### 29. Invocar macro %sendmail

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:claims_processing:s209` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:209`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_205_append_1`
- **Propiedades:**
  - `PROCESS` (Job) = `sendmail` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:209 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
      to=&EMAIL_ONCALL,
      subject=SIU ALERT: &nobs_fraud high-risk claims on &proc_date,
      body=&nobs_fraud claims flagged for SIU review. See STG_INS.FRAUD_ALERTS.
    ` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:209 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 30. Invocar macro %exit

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:claims_processing:s229` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:229`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:claims_processing:op_209_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `exit` — SAS real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:229 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- include /opt/sas/custom/macros/parmv.sas (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:14) — external
- include /opt/sas/custom/macros/nobs.sas (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:15) — external
- include /opt/sas/custom/macros/sendmail.sas (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:16) — external
- dataset_dynamic RAW_INS.&feed_ds (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:38) — nombre de dataset con macrovariables
- macro parmv (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:20) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:87) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:122) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:178) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:179) — sin definición en el proyecto
- macro sendmail (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:209) — sin definición en el proyecto
- macro exit (real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas:229) — sin definición en el proyecto

## Casos de validación

- `vc_m:claims_processing:op_38_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:claims_processing:op_38_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:claims_processing:op_38_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:claims_processing:op_38_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:claims_processing:op_38_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:claims_processing:op_38_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_m:claims_processing:op_38_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_m:claims_processing:op_38_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:claims_processing:op_38_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:claims_processing:op_38_write_1_schema` (schema): Esquema destino
- `vc_m:claims_processing:op_38_write_2_row_count` (row_count): Filas escritas iguales
- `vc_m:claims_processing:op_38_write_2_schema` (schema): Esquema destino
- `vc_m:claims_processing:op_94_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:claims_processing:op_94_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:claims_processing:op_94_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:claims_processing:op_94_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:claims_processing:op_94_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:claims_processing:op_94_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:claims_processing:op_94_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:claims_processing:op_94_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:claims_processing:op_94_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:claims_processing:op_94_write_1_schema` (schema): Esquema destino
- `vc_m:claims_processing:op_112_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:claims_processing:op_112_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:claims_processing:op_114_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:claims_processing:op_114_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:claims_processing:op_114_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:claims_processing:op_112_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:claims_processing:op_112_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:claims_processing:op_112_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:claims_processing:op_112_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:claims_processing:op_112_write_1_schema` (schema): Esquema destino
- `vc_m:claims_processing:op_127_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:claims_processing:op_127_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:claims_processing:op_127_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:claims_processing:op_127_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:claims_processing:op_127_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:claims_processing:op_127_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:claims_processing:op_127_write_1_schema` (schema): Esquema destino
- `vc_m:claims_processing:op_127_write_2_row_count` (row_count): Filas escritas iguales
- `vc_m:claims_processing:op_127_write_2_schema` (schema): Esquema destino
- `vc_m:claims_processing:op_184_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:claims_processing:op_184_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:claims_processing:op_184_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:claims_processing:op_184_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:claims_processing:op_184_union_1_row_count` (row_count): Suma de filas de las entradas (UNION sin ALL elimina duplicados)
- `vc_m:claims_processing:op_184_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:claims_processing:op_184_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:claims_processing:op_184_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:claims_processing:op_184_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:claims_processing:op_184_write_1_schema` (schema): Esquema destino
- `vc_m:claims_processing:op_194_append_1_row_count` (row_count): Filas añadidas
- `vc_m:claims_processing:op_199_append_1_row_count` (row_count): Filas añadidas
- `vc_m:claims_processing:op_205_append_1_row_count` (row_count): Filas añadidas

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
