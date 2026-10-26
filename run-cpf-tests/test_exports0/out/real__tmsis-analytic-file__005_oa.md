# Job `job_005_oa`

- **Programa SAS:** `real/tmsis-analytic-file/005_oa.sas` (sha256 `f5983c821c20`)
- **Instrucciones:** 2 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Pasos

## Definición de macro auxiliar `%create_OA`()

### 1. Invocar macro %create_temp_table

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_OA:s13` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/005_oa.sas:13`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `create_temp_table` — SAS real/tmsis-analytic-file/005_oa.sas:13 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `fileseg=MCP, tblname=oa_pl,
		          subcols=%nrbquote( 
									 %monthly_array(WVR_ID_01, nslots=1)
									 %monthly_array(WVR_ID_02, nslots=1)
									 %monthly_array(WVR_ID_03, nslots=1)
									 %monthly_array(WVR_ID_04, nslots=1)
									 ),
		          subcols2=%nrbquote(
									 %monthly_array(WVR_ID_05, nslots=1)
									 %monthly_array(WVR_ID_06, nslots=1)
									 %monthly_array(WVR_ID_07, nslots=1)
									 %monthly_array(WVR_ID_08, nslots=1)
									 %monthly_array(WVR_ID_09, nslots=1)
									 ),
		          subcols3=%nrbquote(
									 %monthly_array(WVR_ID_10, nslots=1)
									 %monthly_array(WVR_ID_11, nslots=1)
									 %monthly_array(WVR_ID_12, nslots=1)
									 %monthly_array(WVR_ID_13, nslots=1)
									 %monthly_array(WVR_ID_14, nslots=1)
									 %monthly_array(WVR_ID_15, nslots=1)
									),
		          subcols4=%nrbquote(
									 %monthly_array(OPRTG_AUTHRTY_01, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_02, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_03, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_04, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_05, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_06, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_07, nslots=1)
									 ),
		          subcols5=%nrbquote(
									 %monthly_array(OPRTG_AUTHRTY_08, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_09, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_10, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_11, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_12, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_13, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_14, nslots=1)
									 %monthly_array(OPRTG_AUTHRTY_15, nslots=1)
									 ) ` — SAS real/tmsis-analytic-file/005_oa.sas:13 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %create_splmlt

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_OA:s126` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/005_oa.sas:126`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_OA:op_13_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `create_splmlt` — SAS real/tmsis-analytic-file/005_oa.sas:126 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `segname=OPRTG_AUTHRTY, segfile=OpAuth1` — SAS real/tmsis-analytic-file/005_oa.sas:126 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro create_temp_table (real/tmsis-analytic-file/005_oa.sas:13) — sin definición en el proyecto
- macro monthly_array (real/tmsis-analytic-file/005_oa.sas:13) — sin definición en el proyecto
- macro create_splmlt (real/tmsis-analytic-file/005_oa.sas:126) — sin definición en el proyecto
- macro table_id_cols (real/tmsis-analytic-file/005_oa.sas:149) — sin definición en el proyecto
- macro drop_tables (real/tmsis-analytic-file/005_oa.sas:163) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
