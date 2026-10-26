# Job `job_dsc_download`

- **Programa SAS:** `real/ci360-download-client/macros/dsc_download.sas` (sha256 `1c4e03a8464b`)
- **Instrucciones:** 3 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.AUTORESET` ← SAS `AUTORESET` = `yes` (%LET de primer nivel)
- `context.CATEGORY` ← SAS `CATEGORY` (%LET de primer nivel)
- `context.CODE` ← SAS `CODE` (%LET de primer nivel)
- `context.DSC_AGENT_NAME` ← SAS `DSC_AGENT_NAME` = `ci360_agent` (%LET de primer nivel)
- `context.DSC_DOWNLOAD_URL` ← SAS `DSC_DOWNLOAD_URL` = `%nrstr(https://extapigwservice-prod.ci360.sas.com/marketingGateway/discoverService/dataDownload/eventData/)` (%LET de primer nivel)
- `context.DSC_FILE_READ_OPTION` ← SAS `DSC_FILE_READ_OPTION` = `%str(LRECL=60000 MISSOVER)` (%LET de primer nivel)
- `context.DSC_HTTP_MAX_RETRY_ATTEMPTS` ← SAS `DSC_HTTP_MAX_RETRY_ATTEMPTS` = `3` (%LET de primer nivel)
- `context.DSC_HTTP_RETRY_WAIT_SEC` ← SAS `DSC_HTTP_RETRY_WAIT_SEC` = `5` (%LET de primer nivel)
- `context.DSC_LOAD_END_DTTM` ← SAS `DSC_LOAD_END_DTTM` = `%nrquote(12Nov2019 13:59:59)` (%LET de primer nivel)
- `context.DSC_LOAD_START_DTTM` ← SAS `DSC_LOAD_START_DTTM` = `%nrquote(12Nov2019 13:00:00)` (%LET de primer nivel)
- `context.DSC_PROXY_AUTH` ← SAS `DSC_PROXY_AUTH` (%LET de primer nivel)
- `context.DSC_PROXY_HOST` ← SAS `DSC_PROXY_HOST` (%LET de primer nivel)
- `context.DSC_PROXY_PORT` ← SAS `DSC_PROXY_PORT` (%LET de primer nivel)
- `context.DSC_SCHEMA_VERSION` ← SAS `DSC_SCHEMA_VERSION` = `1` (%LET de primer nivel)
- `context.DSC_SECRET_KEY` ← SAS `DSC_SECRET_KEY` = `***` (%LET de primer nivel)
- `context.DSC_SUB_HOURLY_MINUTES` ← SAS `DSC_SUB_HOURLY_MINUTES` = `60` (%LET de primer nivel)
- `context.DSC_TENANT_ID` ← SAS `DSC_TENANT_ID` = `%str(abc123-ci360-tenant-id-xyz)` (%LET de primer nivel)
- `context.mart_nm` ← SAS `mart_nm` = `detail` (%LET de primer nivel)
- `context.RESET_DAY_OFFSET` ← SAS `RESET_DAY_OFFSET` = `60` (%LET de primer nivel)
- `context.reset_day_offset` ← SAS `reset_day_offset` (&reset_day_offset en real/ci360-download-client/macros/dsc_download.sas:157)
- `context.UtilityLocation` ← SAS `UtilityLocation` = `C:\dev\Client` (%LET de primer nivel)

## Pasos

### 1. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s37` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_download.sas:37`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 2. Invocar macro %dsc_download_data

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s157` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_download.sas:157`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_37_maintenance_1`
- **Propiedades:**
  - `PROCESS` (Job) = `dsc_download_data` — SAS real/ci360-download-client/macros/dsc_download.sas:157 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `mart_nm=&mart_nm., reset_day_offset=&reset_day_offset.` — SAS real/ci360-download-client/macros/dsc_download.sas:157 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s162` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_download.sas:162`
- **Conexiones:** OnSubjobOk desde `op_157_macro_call_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Sin resolver

- macro left (real/ci360-download-client/macros/dsc_download.sas:37) — sin definición en el proyecto
- macro dsc_download_data (real/ci360-download-client/macros/dsc_download.sas:157) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
