# Job `job_003_address_phone`

- **Programa SAS:** `real/tmsis-analytic-file/003_address_phone.sas` (sha256 `2bf6676587cf`)
- **Instrucciones:** 4 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.getprior` ← SAS `getprior` (&getprior en real/tmsis-analytic-file/003_address_phone.sas:189)
- `context.p` ← SAS `p` (&p en real/tmsis-analytic-file/003_address_phone.sas:189)
- `context.pyear` ← SAS `pyear` (&pyear en real/tmsis-analytic-file/003_address_phone.sas:72)
- `context.pyears` ← SAS `pyears` (&pyears en real/tmsis-analytic-file/003_address_phone.sas:189)
- `context.year` ← SAS `year` (&year en real/tmsis-analytic-file/003_address_phone.sas:64)

## Pasos

## Definición de macro auxiliar `%create_CNTCT_DTLS`()

### 1. Invocar macro %create_temp_table

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_CNTCT_DTLS:s15` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/003_address_phone.sas:15`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `create_temp_table` — SAS real/tmsis-analytic-file/003_address_phone.sas:15 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `name,
	              subcols=%nrbquote(  %last_best(ELGBL_1ST_NAME)
	                                  %last_best(ELGBL_LAST_NAME)
	                                  %last_best(ELGBL_MDL_INITL_NAME)

				 ) ` — SAS real/tmsis-analytic-file/003_address_phone.sas:15 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %address_phone

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_CNTCT_DTLS:s64` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/003_address_phone.sas:64`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_CNTCT_DTLS:op_15_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `address_phone` — SAS real/tmsis-analytic-file/003_address_phone.sas:64 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `&year.` — SAS real/tmsis-analytic-file/003_address_phone.sas:64 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %address_phone (definida en real/tmsis-analytic-file/003_address_phone.sas)

### 3. Invocar macro %create_hist_adr

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_CNTCT_DTLS:s72` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/003_address_phone.sas:72`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_CNTCT_DTLS:op_64_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `create_hist_adr` — SAS real/tmsis-analytic-file/003_address_phone.sas:72 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `address_phone, inyear = &pyear.` — SAS real/tmsis-analytic-file/003_address_phone.sas:72 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 4. Invocar macro %drop_tables

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_CNTCT_DTLS:s189` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/003_address_phone.sas:189`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_CNTCT_DTLS:op_72_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `drop_tables` — SAS real/tmsis-analytic-file/003_address_phone.sas:189 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `name_&year. name_address_phone_&year. address_phone_&year._out
	             %if &getprior.=1 %then %do;
                      address_phone_&year. 
					  %do p=1 %to %sysfunc(countw(&pyears.));
	 		      		   %let pyear=%scan(&pyears.,&p.);
                   		   address_phone_&pyear. 
                      %end;
                 %end; ` — SAS real/tmsis-analytic-file/003_address_phone.sas:189 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro create_temp_table (real/tmsis-analytic-file/003_address_phone.sas:15) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/003_address_phone.sas:15) — sin definición en el proyecto
- macro create_temp_table (real/tmsis-analytic-file/003_address_phone.sas:26) — sin definición en el proyecto
- macro monthly_array (real/tmsis-analytic-file/003_address_phone.sas:26) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/003_address_phone.sas:26) — sin definición en el proyecto
- macro nonmiss_month (real/tmsis-analytic-file/003_address_phone.sas:26) — sin definición en el proyecto
- macro address_flag (real/tmsis-analytic-file/003_address_phone.sas:26) — sin definición en el proyecto
- macro assign_nonmiss_month (real/tmsis-analytic-file/003_address_phone.sas:26) — sin definición en el proyecto
- macro create_hist_adr (real/tmsis-analytic-file/003_address_phone.sas:72) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/003_address_phone.sas:78) — sin definición en el proyecto
- macro address_same_year (real/tmsis-analytic-file/003_address_phone.sas:93) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/003_address_phone.sas:93) — sin definición en el proyecto
- macro table_id_cols (real/tmsis-analytic-file/003_address_phone.sas:165) — sin definición en el proyecto
- macro drop_tables (real/tmsis-analytic-file/003_address_phone.sas:189) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
