# Plan de migración — proyecto `5f8a983f6dfe`

Reglas v1 · 58 programas

## Orden de procesamiento sugerido

1. `inc/macros_comunes.sas`, `p0_clientes_activos.sas`, `p0_ejemplo_basico.sas`, `p0_resumen_sql.sas`, `p1_macro_parametrizada.sas`, `p1_merge_first_last.sas`, `p2_codigo_dinamico.sas`, `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas`, `real/ci360-download-client/macros/dsc_cdm_version_update.sas`, `real/ci360-download-client/macros/dsc_create_attrib.sas`, `real/ci360-download-client/macros/dsc_download.sas`, `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas`, `real/cmmi-shadow-bundles/a00_01_utility_macros.sas`, `real/cmmi-shadow-bundles/a00_02_assign_globals.sas`, `real/cmmi-shadow-bundles/a00_03_import_logic.sas`, `real/learning-sas-by-example/Example_code/Create_Datasets.sas`, `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas`, `real/sas-access-samples/SAS_Foundation/DB2/bulkload.sas`, `real/sas-access-samples/SAS_Foundation/Greenplum/bulkload.sas`, `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas`, `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas`, `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas`, `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas`, `real/sas-access-samples/SAS_Foundation/Impala/bulkload.sas`, `real/tmsis-analytic-file/001_base.sas`, `real/tmsis-analytic-file/001_batch_bsf.sas`, `real/tmsis-analytic-file/002_eligibility_dates.sas`, `real/tmsis-analytic-file/002_mc_macros.sas`, `real/tmsis-analytic-file/003_address_phone.sas`, `real/tmsis-analytic-file/003_bsf_ELG00003.sas`, `real/tmsis-analytic-file/005_id.sas`, `real/tmsis-analytic-file/005_oa.sas`, `real/tmsis-analytic-file/023_bsf_final.sas`, `real/tmsis-analytic-file/IP_Build.sas`, `real/tmsis-analytic-file/LT_Build.sas`, `real/tmsis-analytic-file/RX_build.sas`, `real/tmsis-analytic-file/de_annual_build.sas`, `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas`, `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas`, `real/ts-sas-legacy-analytics/Config/autoexec.sas`, `real/ts-sas-legacy-analytics/Formats/banking_formats.sas`, `real/ts-sas-legacy-analytics/Formats/insurance_formats.sas`, `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas`, `real/ts-sas-legacy-analytics/Macro/RunAll.sas`, `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas`, `real/ts-sas-legacy-analytics/Macro/batch_submit.sas`, `real/ts-sas-legacy-analytics/Macro/check_if_empty.sas`, `real/ts-sas-legacy-analytics/Macro/create_format.sas`, `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas`, `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas`, `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas`
2. `p0_macro_include.sas`, `real/learning-sas-by-example/Example_code/Programs_Used_in_the_Second_Edition.sas`, `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas`, `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas`, `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas`, `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas`
3. `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas`

Ciclos detectados (requieren decisión): real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas ↔ real/sas-access-samples/SAS_Foundation/DB2/bulkload.sas; real/sas-access-samples/SAS_Foundation/Greenplum/bulkload.sas ↔ real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas ↔ real/sas-access-samples/SAS_Foundation/Impala/bulkload.sas

## Jobs

| Job | Programa | Instrucciones |
| --- | --- | ---: |
| `job_macros_comunes` | `inc/macros_comunes.sas` | 2 paso(s) |
| `job_p0_clientes_activos` | `p0_clientes_activos.sas` | 11 paso(s) |
| `job_p0_ejemplo_basico` | `p0_ejemplo_basico.sas` | 7 paso(s) |
| `job_p0_macro_include` | `p0_macro_include.sas` | 3 paso(s) |
| `job_p0_resumen_sql` | `p0_resumen_sql.sas` | 9 paso(s) |
| `job_p1_macro_parametrizada` | `p1_macro_parametrizada.sas` | 5 paso(s) |
| `job_p1_merge_first_last` | `p1_merge_first_last.sas` | 13 paso(s) |
| `job_p2_codigo_dinamico` | `p2_codigo_dinamico.sas` | 6 paso(s) |
| `job_dsc_appendtocustomerdb` | `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas` | 14 paso(s) |
| `job_dsc_cdm_version_update` | `real/ci360-download-client/macros/dsc_cdm_version_update.sas` | 14 paso(s) |
| `job_dsc_create_attrib` | `real/ci360-download-client/macros/dsc_create_attrib.sas` | 30 paso(s) |
| `job_dsc_download` | `real/ci360-download-client/macros/dsc_download.sas` | 3 paso(s) |
| `job_a00_00_risk_adjustment_caller` | `real/cmmi-shadow-bundles/a00_00_risk_adjustment_caller.sas` | 23 paso(s) |
| `job_a00_01_utility_macros` | `real/cmmi-shadow-bundles/a00_01_utility_macros.sas` | 0 paso(s) |
| `job_a00_02_assign_globals` | `real/cmmi-shadow-bundles/a00_02_assign_globals.sas` | 1 paso(s) |
| `job_a00_03_import_logic` | `real/cmmi-shadow-bundles/a00_03_import_logic.sas` | 52 paso(s) |
| `job_create_datasets` | `real/learning-sas-by-example/Example_code/Create_Datasets.sas` | 252 paso(s) |
| `job_programs_used_in_the_second_edition` | `real/learning-sas-by-example/Example_code/Programs_Used_in_the_Second_Edition.sas` | 989 paso(s) |
| `job_solutions_to_odd_numbered_problems` | `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas` | 493 paso(s) |
| `job_bulkload` | `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas` | 8 paso(s) |
| `job_bulkload` | `real/sas-access-samples/SAS_Foundation/DB2/bulkload.sas` | 8 paso(s) |
| `job_bulkload` | `real/sas-access-samples/SAS_Foundation/Greenplum/bulkload.sas` | 10 paso(s) |
| `job_bulkload` | `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas` | 10 paso(s) |
| `job_createtableasselect` | `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas` | 13 paso(s) |
| `job_orcfileformat` | `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas` | 9 paso(s) |
| `job_partitioneddata` | `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas` | 7 paso(s) |
| `job_bulkload` | `real/sas-access-samples/SAS_Foundation/Impala/bulkload.sas` | 10 paso(s) |
| `job_001_base` | `real/tmsis-analytic-file/001_base.sas` | 5 paso(s) |
| `job_001_batch_bsf` | `real/tmsis-analytic-file/001_batch_bsf.sas` | 19 paso(s) |
| `job_002_eligibility_dates` | `real/tmsis-analytic-file/002_eligibility_dates.sas` | 4 paso(s) |
| `job_002_mc_macros` | `real/tmsis-analytic-file/002_mc_macros.sas` | 0 paso(s) |
| `job_003_address_phone` | `real/tmsis-analytic-file/003_address_phone.sas` | 4 paso(s) |
| `job_003_bsf_elg00003` | `real/tmsis-analytic-file/003_bsf_ELG00003.sas` | 5 paso(s) |
| `job_005_id` | `real/tmsis-analytic-file/005_id.sas` | 2 paso(s) |
| `job_005_oa` | `real/tmsis-analytic-file/005_oa.sas` | 2 paso(s) |
| `job_023_bsf_final` | `real/tmsis-analytic-file/023_bsf_final.sas` | 0 paso(s) |
| `job_ip_build` | `real/tmsis-analytic-file/IP_Build.sas` | 24 paso(s) |
| `job_lt_build` | `real/tmsis-analytic-file/LT_Build.sas` | 25 paso(s) |
| `job_rx_build` | `real/tmsis-analytic-file/RX_build.sas` | 22 paso(s) |
| `job_de_annual_build` | `real/tmsis-analytic-file/de_annual_build.sas` | 9 paso(s) |
| `job_run_daily_banking` | `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas` | 8 paso(s) |
| `job_run_daily_insurance` | `real/ts-sas-legacy-analytics/BatchJobs/run_daily_insurance.sas` | 5 paso(s) |
| `job_autoexec` | `real/ts-sas-legacy-analytics/Config/autoexec.sas` | 0 paso(s) |
| `job_banking_formats` | `real/ts-sas-legacy-analytics/Formats/banking_formats.sas` | 1 paso(s) |
| `job_insurance_formats` | `real/ts-sas-legacy-analytics/Formats/insurance_formats.sas` | 1 paso(s) |
| `job_createtableorview` | `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas` | 57 paso(s) |
| `job_runall` | `real/ts-sas-legacy-analytics/Macro/RunAll.sas` | 26 paso(s) |
| `job_runall_controltable` | `real/ts-sas-legacy-analytics/Macro/RunAll_ControlTable.sas` | 5 paso(s) |
| `job_batch_submit` | `real/ts-sas-legacy-analytics/Macro/batch_submit.sas` | 4 paso(s) |
| `job_check_if_empty` | `real/ts-sas-legacy-analytics/Macro/check_if_empty.sas` | 3 paso(s) |
| `job_create_format` | `real/ts-sas-legacy-analytics/Macro/create_format.sas` | 24 paso(s) |
| `job_credit_risk_scoring` | `real/ts-sas-legacy-analytics/Programs/Banking/credit_risk_scoring.sas` | 30 paso(s) |
| `job_daily_transaction_processing` | `real/ts-sas-legacy-analytics/Programs/Banking/daily_transaction_processing.sas` | 34 paso(s) |
| `job_load_customer_accounts` | `real/ts-sas-legacy-analytics/Programs/Banking/load_customer_accounts.sas` | 22 paso(s) |
| `job_monthly_regulatory_reporting` | `real/ts-sas-legacy-analytics/Programs/Banking/monthly_regulatory_reporting.sas` | 27 paso(s) |
| `job_claims_processing` | `real/ts-sas-legacy-analytics/Programs/Insurance/claims_processing.sas` | 30 paso(s) |
| `job_policy_valuation` | `real/ts-sas-legacy-analytics/Programs/Insurance/policy_valuation.sas` | 27 paso(s) |
| `job_customer_profitability` | `real/ts-sas-legacy-analytics/Programs/Reports/customer_profitability.sas` | 24 paso(s) |

## Recomendaciones Grid del proyecto

### `sas_batch.sysin` (partial)

- **Accion:** Implementa el programa como Job Talend y confirma primero qué opciones batch conservan su significado.
- **Motivo/limite:** The planner emits a child-Job candidate, but the batch environment and option semantics are unconfirmed.
- **Evidencia:** `grid/coverage_variants.sh:3` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Confirmar:** Implement and validate the child Job; Confirm SAS batch options
- **Datos interpretados:**

```json
{
  "kind": "sas_batch",
  "program": "/sas/prog/program with spaces.sas",
  "resolved_program": null,
  "match_status": "external",
  "job_name": null,
  "queue": null,
  "waits": true,
  "params": {
    "FECHA_PROC": "20241019"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.submit` (partial)

- **Accion:** Crea un Job hijo para el programa SAS identificado y configura su invocación solo después de validar entradas y parámetros.
- **Motivo/limite:** The planner emits this candidate, but the fixture syntax is illustrative and no SAS Grid version has been confirmed.
- **Evidencia:** `grid/coverage_variants.sh:4` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `grid/coverage_variants.sh#1`
- **Confirmar:** Implement and validate the child Job before invocation; Confirm job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [
    "-grid",
    "-queue",
    "-name",
    "-wait"
  ],
  "incomplete_options": []
}
```

### `sasgsub.job_options` (partial)

- **Accion:** Confirma con el equipo de operación cómo trasladar cola, nombre y espera al orquestador objetivo.
- **Motivo/limite:** Queue and Grid job name have no verified Talend component property mapping.
- **Evidencia:** `grid/coverage_variants.sh:4` | catalogo Grid v1
- **Depende de:** `grid/coverage_variants.sh#1`
- **Confirmar:** Confirm target scheduler and execution settings
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [
    "-grid",
    "-queue",
    "-name",
    "-wait"
  ],
  "incomplete_options": []
}
```

### `sasgsub.unverified_options` (unsupported)

- **Accion:** No traslades estas opciones; valida su significado con la versión de SAS Grid y decide el diseño manualmente.
- **Motivo/limite:** These option spellings are not interpreted by the current analyzer.
- **Evidencia:** `grid/coverage_variants.sh:4` | catalogo Grid v1
- **Depende de:** `grid/coverage_variants.sh#1`
- **Confirmar:** Confirm option syntax and semantics before defining a mapping
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [
    "-grid",
    "-queue",
    "-name",
    "-wait"
  ],
  "incomplete_options": []
}
```

### `shell.inferred_sequence` (partial)

- **Accion:** Revisa ramas y condiciones del script; conecta Jobs solo cuando el orden inferido esté confirmado.
- **Motivo/limite:** The planner preserves the inferred dependency, but untested shell control flow can change execution order.
- **Evidencia:** `grid/coverage_variants.sh:4` | catalogo Grid v1
- **Depende de:** `grid/coverage_variants.sh#1`
- **Confirmar:** Review inferred order and all source failure branches
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [
    "-grid",
    "-queue",
    "-name",
    "-wait"
  ],
  "incomplete_options": []
}
```

### `scheduler.lsf` (unsupported)

- **Accion:** Revisa manualmente el comando LSF y documenta un diseño de orquestación antes de migrarlo.
- **Motivo/limite:** Commands are detected, but LSF options and execution semantics are not parsed.
- **Evidencia:** `grid/coverage_variants.sh:5` | catalogo Grid v1
- **Confirmar:** Provide representative LSF scripts and confirm target scheduler
- **Datos interpretados:**

```json
{
  "kind": "unsupported_scheduler",
  "program": null,
  "resolved_program": null,
  "match_status": "unsupported",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `scheduler.lsf` (unsupported)

- **Accion:** Revisa manualmente el comando LSF y documenta un diseño de orquestación antes de migrarlo.
- **Motivo/limite:** Commands are detected, but LSF options and execution semantics are not parsed.
- **Evidencia:** `grid/coverage_variants.sh:6` | catalogo Grid v1
- **Confirmar:** Provide representative LSF scripts and confirm target scheduler
- **Datos interpretados:**

```json
{
  "kind": "unsupported_scheduler",
  "program": null,
  "resolved_program": null,
  "match_status": "unsupported",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.submit` (partial)

- **Accion:** Crea un Job hijo para el programa SAS identificado y configura su invocación solo después de validar entradas y parámetros.
- **Motivo/limite:** The planner emits this candidate, but the fixture syntax is illustrative and no SAS Grid version has been confirmed.
- **Evidencia:** `grid/coverage_variants.sh:7` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Confirmar:** Implement and validate the child Job before invocation; Confirm job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [],
  "incomplete_options": [
    "-gridqueue"
  ]
}
```

### `sasgsub.job_options` (partial)

- **Accion:** Confirma con el equipo de operación cómo trasladar cola, nombre y espera al orquestador objetivo.
- **Motivo/limite:** Queue and Grid job name have no verified Talend component property mapping.
- **Evidencia:** `grid/coverage_variants.sh:7` | catalogo Grid v1
- **Confirmar:** Confirm target scheduler and execution settings
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [],
  "incomplete_options": [
    "-gridqueue"
  ]
}
```

### `sasgsub.missing_option_value` (unsupported)

- **Accion:** Deten esta recomendacion y recupera el valor faltante antes de disenar la orquestacion.
- **Motivo/limite:** A required option value is absent; do not infer it.
- **Evidencia:** `grid/coverage_variants.sh:7` | catalogo Grid v1
- **Confirmar:** Recover the missing value from the authoritative job definition
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": null,
  "queue": null,
  "waits": false,
  "params": {},
  "condition": null,
  "unknown_options": [],
  "incomplete_options": [
    "-gridqueue"
  ]
}
```

### `sasgsub.submit` (partial)

- **Accion:** Crea un Job hijo para el programa SAS identificado y configura su invocación solo después de validar entradas y parámetros.
- **Motivo/limite:** The planner emits this candidate, but the fixture syntax is illustrative and no SAS Grid version has been confirmed.
- **Evidencia:** `grid/ejecutar_lote.sh:5` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Confirmar:** Implement and validate the child Job before invocation; Confirm job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "carga_clientes",
  "queue": null,
  "waits": true,
  "params": {
    "FECHA_PROC": "$FECHA_PROC"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.job_options` (partial)

- **Accion:** Confirma con el equipo de operación cómo trasladar cola, nombre y espera al orquestador objetivo.
- **Motivo/limite:** Queue and Grid job name have no verified Talend component property mapping.
- **Evidencia:** `grid/ejecutar_lote.sh:5` | catalogo Grid v1
- **Confirmar:** Confirm target scheduler and execution settings
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "carga_clientes",
  "queue": null,
  "waits": true,
  "params": {
    "FECHA_PROC": "$FECHA_PROC"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.set_parameters` (partial)

- **Accion:** Define variables de contexto en el Job hijo y copia únicamente los valores resueltos y confirmados.
- **Motivo/limite:** The planner preserves parsed values as evidence, but shell expansion and values with spaces are not resolved.
- **Evidencia:** `grid/ejecutar_lote.sh:5` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Confirmar:** Define and validate matching child Job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_clientes_activos.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "carga_clientes",
  "queue": null,
  "waits": true,
  "params": {
    "FECHA_PROC": "$FECHA_PROC"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.submit` (partial)

- **Accion:** Crea un Job hijo para el programa SAS identificado y configura su invocación solo después de validar entradas y parámetros.
- **Motivo/limite:** The planner emits this candidate, but the fixture syntax is illustrative and no SAS Grid version has been confirmed.
- **Evidencia:** `grid/ejecutar_lote.sh:6` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `grid/ejecutar_lote.sh#1`
- **Confirmar:** Implement and validate the child Job before invocation; Confirm job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_resumen_sql.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "resumen_ventas",
  "queue": "normal",
  "waits": true,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.job_options` (partial)

- **Accion:** Confirma con el equipo de operación cómo trasladar cola, nombre y espera al orquestador objetivo.
- **Motivo/limite:** Queue and Grid job name have no verified Talend component property mapping.
- **Evidencia:** `grid/ejecutar_lote.sh:6` | catalogo Grid v1
- **Depende de:** `grid/ejecutar_lote.sh#1`
- **Confirmar:** Confirm target scheduler and execution settings
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_resumen_sql.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "resumen_ventas",
  "queue": "normal",
  "waits": true,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.set_parameters` (partial)

- **Accion:** Define variables de contexto en el Job hijo y copia únicamente los valores resueltos y confirmados.
- **Motivo/limite:** The planner preserves parsed values as evidence, but shell expansion and values with spaces are not resolved.
- **Evidencia:** `grid/ejecutar_lote.sh:6` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `grid/ejecutar_lote.sh#1`
- **Confirmar:** Define and validate matching child Job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_resumen_sql.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "resumen_ventas",
  "queue": "normal",
  "waits": true,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `shell.inferred_sequence` (partial)

- **Accion:** Revisa ramas y condiciones del script; conecta Jobs solo cuando el orden inferido esté confirmado.
- **Motivo/limite:** The planner preserves the inferred dependency, but untested shell control flow can change execution order.
- **Evidencia:** `grid/ejecutar_lote.sh:6` | catalogo Grid v1
- **Depende de:** `grid/ejecutar_lote.sh#1`
- **Confirmar:** Review inferred order and all source failure branches
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p0_resumen_sql.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "resumen_ventas",
  "queue": "normal",
  "waits": true,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": null,
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.submit` (partial)

- **Accion:** Crea un Job hijo para el programa SAS identificado y configura su invocación solo después de validar entradas y parámetros.
- **Motivo/limite:** The planner emits this candidate, but the fixture syntax is illustrative and no SAS Grid version has been confirmed.
- **Evidencia:** `grid/ejecutar_lote.sh:7` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `grid/ejecutar_lote.sh#2`
- **Confirmar:** Implement and validate the child Job before invocation; Confirm job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p1_merge_first_last.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "pagos_cliente",
  "queue": null,
  "waits": false,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": "previous_success",
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.job_options` (partial)

- **Accion:** Confirma con el equipo de operación cómo trasladar cola, nombre y espera al orquestador objetivo.
- **Motivo/limite:** Queue and Grid job name have no verified Talend component property mapping.
- **Evidencia:** `grid/ejecutar_lote.sh:7` | catalogo Grid v1
- **Depende de:** `grid/ejecutar_lote.sh#2`
- **Confirmar:** Confirm target scheduler and execution settings
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p1_merge_first_last.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "pagos_cliente",
  "queue": null,
  "waits": false,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": "previous_success",
  "unknown_options": [],
  "incomplete_options": []
}
```

### `sasgsub.set_parameters` (partial)

- **Accion:** Define variables de contexto en el Job hijo y copia únicamente los valores resueltos y confirmados.
- **Motivo/limite:** The planner preserves parsed values as evidence, but shell expansion and values with spaces are not resolved.
- **Evidencia:** `grid/ejecutar_lote.sh:7` | catalogo Grid v1
- **Componente candidato:** `tRunJob`
- **Documentacion oficial Talend:** https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties
- **Depende de:** `grid/ejecutar_lote.sh#2`
- **Confirmar:** Define and validate matching child Job context parameters
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p1_merge_first_last.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "pagos_cliente",
  "queue": null,
  "waits": false,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": "previous_success",
  "unknown_options": [],
  "incomplete_options": []
}
```

### `shell.inferred_sequence` (partial)

- **Accion:** Revisa ramas y condiciones del script; conecta Jobs solo cuando el orden inferido esté confirmado.
- **Motivo/limite:** The planner preserves the inferred dependency, but untested shell control flow can change execution order.
- **Evidencia:** `grid/ejecutar_lote.sh:7` | catalogo Grid v1
- **Depende de:** `grid/ejecutar_lote.sh#2`
- **Confirmar:** Review inferred order and all source failure branches
- **Datos interpretados:**

```json
{
  "kind": "sasgsub",
  "program": "/sas/prog/p1_merge_first_last.sas",
  "resolved_program": null,
  "match_status": "candidate",
  "job_name": "pagos_cliente",
  "queue": null,
  "waits": false,
  "params": {
    "FECHA_PROC": "${1:-$(date +%Y%m%d)}"
  },
  "condition": "previous_success",
  "unknown_options": [],
  "incomplete_options": []
}
```

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
- **Evidencia:** `real/ts-sas-legacy-analytics/BatchJobs/run_daily_banking.sas:6` | catalogo Grid v1
- **Confirmar:** Recreate the authoritative schedule in the chosen scheduler
- **Datos interpretados:**

```json
{
  "schedule": "Daily 05:45 via Control-M BANK_MASTER"
}
```

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

