# Job `job_001_base`

- **Programa SAS:** `real/tmsis-analytic-file/001_base.sas` (sha256 `39618570f7cd`)
- **Instrucciones:** 5 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.p` ← SAS `p` (&p en real/tmsis-analytic-file/001_base.sas:302)
- `context.pyear` ← SAS `pyear` (&pyear en real/tmsis-analytic-file/001_base.sas:170)
- `context.pyears` ← SAS `pyears` (&pyears en real/tmsis-analytic-file/001_base.sas:302)
- `context.year` ← SAS `year` (&year en real/tmsis-analytic-file/001_base.sas:162)

## Pasos

## Definición de macro auxiliar `%create_BASE`()

### 1. Invocar macro %create_temp_table

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_BASE:s22` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_base.sas:22`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `create_temp_table` — SAS real/tmsis-analytic-file/001_base.sas:22 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `base_nondemo,
		          subcols=%nrbquote( %last_best(CTZNSHP_VRFCTN_IND)
								     %last_best(IMGRTN_STUS_CD)
								     %last_best(IMGRTN_VRFCTN_IND) 

									 ,null :: smallint as PRGNCY_FLAG_01
									 ,null :: smallint as PRGNCY_FLAG_02
									 ,null :: smallint as PRGNCY_FLAG_03
									 ,null :: smallint as PRGNCY_FLAG_04
									 ,null :: smallint as PRGNCY_FLAG_05
									 ,null :: smallint as PRGNCY_FLAG_06
									 ,null :: smallint as PRGNCY_FLAG_07
									 ,null :: smallint as PRGNCY_FLAG_08
									 ,null :: smallint as PRGNCY_FLAG_09
									 ,null :: smallint as PRGNCY_FLAG_10
									 ,null :: smallint as PRGNCY_FLAG_11
									 ,null :: smallint as PRGNCY_FLAG_12

									 ,null :: smallint as PRGNCY_FLAG_EVR

									 %monthly_array(ELGBLTY_GRP_CD)
									 %last_best(ELGBLTY_GRP_CD,outcol=ELGBLTY_GRP_CD_LTST)
									 %monthly_array(MASBOE_CD)
									 %last_best(MASBOE_CD,outcol=MASBOE_CD_LTST)
									 %last_best(CARE_LVL_STUS_CD)
									 %ever_year(DEAF_DSBL_FLAG)
									 %ever_year(BLND_DSBL_FLAG)
									 %ever_year(DFCLTY_CONC_DSBL_FLAG,outcol=DFCLTY_CNCNTRTNG_DSBL_FLAG_EVR)
									 %ever_year(DFCLTY_WLKG_DSBL_FLAG)
									 %ever_year(DFCLTY_DRSNG_BATHG_DSBL_FLAG,outcol=DFCLTY_DRSNG_BTH_DSBL_FLAG_EVR)
									 %ever_year(DFCLTY_ERRANDS_ALN_DSBL_FLAG,outcol=DFCLTY_ERNDS_ALN_DSBL_FLAG_EVR)
									 %ever_year(OTHR_DSBL_FLAG)

									 %monthly_array(CHIP_CD)
									 %last_best(CHIP_CD,outcol=CHIP_CD_LTST)
     
									 %monthly_array(STATE_SPEC_ELGBLTY_FCTR_TXT,outcol=STATE_SPEC_ELGBLTY_GRP)
									 %last_best(STATE_SPEC_ELGBLTY_FCTR_TXT,outcol=STATE_SPEC_ELGBLTY_GRP_LTST)
									 %monthly_array(DUAL_ELGBL_CD)
									 %last_best(DUAL_ELGBL_CD,outcol=DUAL_ELGBL_CD_LTST)
									                     
									 %mc_type_rank(smonth=1,emonth=2)
									                  
									 %monthly_array(RSTRCTD_BNFTS_CD)
									 %last_best(RSTRCTD_BNFTS_CD,outcol=RSTRCTD_BNFTS_CD_LTST)
									 %last_best(SSDI_IND)
									 %last_best(SSI_IND)
									 %last_best(SSI_STATE_SPLMT_STUS_CD)
									 %last_best(SSI_STUS_CD)
									 %last_best(BIRTH_CNCPTN_IND)
									 %last_best(TANF_CASH_CD)
									 %last_best(TPL_INSRNC_CVRG_IND)
									 %last_best(TPL_OTHR_CVRG_IND)	

									 %misg_enrlmt_type
									 
									 %last_best(incol=AGE_NUM, outcol = AGE_NUM_TEMP)	
									 %last_best(incol=AGE_GRP_FLAG, outcol = AGE_GRP_FLAG_TEMP)	
									 %last_best(incol=ELGBL_AFTR_EOM_IND, outcol = ELGBL_AFTR_EOM_TEMP)
									 %nonmiss_month(incol = msis_ident_num,outcol = BSF_RECORD)

									 %monthly_array(ELGBLTY_CHG_RSN_CD)

		              ),
                      subcols2=%nrbquote(
                                     %mc_type_rank(smonth=3,emonth=4)
                     ),
                      subcols3=%nrbquote(
                                     %mc_type_rank(smonth=5,emonth=6)
                     ),
                      subcols4=%nrbquote(
                                     %mc_type_rank(smonth=7,emonth=8)
                     ),
                      subcols5=%nrbquote(
                                     %mc_type_rank(smonth=9,emonth=10)
                     ),
                      subcols6=%nrbquote(
                                     %mc_type_rank(smonth=11,emonth=12)

                     ) ` — SAS real/tmsis-analytic-file/001_base.sas:22 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %demographics

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_BASE:s162` · **Confianza:** high · **Origen SAS:** `real/tmsis-analytic-file/001_base.sas:162`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_BASE:op_22_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `demographics` — SAS real/tmsis-analytic-file/001_base.sas:162 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `&year.` — SAS real/tmsis-analytic-file/001_base.sas:162 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %demographics (definida en real/tmsis-analytic-file/001_base.sas)

### 3. Invocar macro %create_hist_demo

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_BASE:s170` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_base.sas:170`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_BASE:op_162_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `create_hist_demo` — SAS real/tmsis-analytic-file/001_base.sas:170 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `base_demo, inyear = &pyear.` — SAS real/tmsis-analytic-file/001_base.sas:170 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 4. Invocar macro %drop_tables

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_BASE:s302` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_base.sas:302`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_BASE:op_170_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `drop_tables` — SAS real/tmsis-analytic-file/001_base.sas:302 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `base_demo_&year. %do p=1 %to %sysfunc(countw(&pyears.));
	 		      							%let pyear=%scan(&pyears.,&p.); 
                                            base_demo_&pyear.
									  %end; ` — SAS real/tmsis-analytic-file/001_base.sas:302 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 5. Invocar macro %drop_tables

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_BASE:s382` · **Confianza:** low · **Origen SAS:** `real/tmsis-analytic-file/001_base.sas:382`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_BASE:op_302_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `drop_tables` — SAS real/tmsis-analytic-file/001_base.sas:382 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `base_&year. enrolled_days_&year. MNGD_CARE_SPLMTL_&year. WAIVER_SPLMTL_&year. MFP_SPLMTL_&year.
	             HH_SPO_SPLMTL_&year. DIS_NEED_SPLMTLS_&year.` — SAS real/tmsis-analytic-file/001_base.sas:382 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- macro create_temp_table (real/tmsis-analytic-file/001_base.sas:22) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/001_base.sas:22) — sin definición en el proyecto
- macro monthly_array (real/tmsis-analytic-file/001_base.sas:22) — sin definición en el proyecto
- macro ever_year (real/tmsis-analytic-file/001_base.sas:22) — sin definición en el proyecto
- macro mc_type_rank (real/tmsis-analytic-file/001_base.sas:22) — sin definición en el proyecto
- macro misg_enrlmt_type (real/tmsis-analytic-file/001_base.sas:22) — sin definición en el proyecto
- macro nonmiss_month (real/tmsis-analytic-file/001_base.sas:22) — sin definición en el proyecto
- macro create_temp_table (real/tmsis-analytic-file/001_base.sas:109) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/001_base.sas:109) — sin definición en el proyecto
- macro monthly_array (real/tmsis-analytic-file/001_base.sas:109) — sin definición en el proyecto
- macro nonmiss_month (real/tmsis-analytic-file/001_base.sas:109) — sin definición en el proyecto
- macro assign_nonmiss_month (real/tmsis-analytic-file/001_base.sas:109) — sin definición en el proyecto
- macro create_hist_demo (real/tmsis-analytic-file/001_base.sas:170) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/001_base.sas:180) — sin definición en el proyecto
- macro address_same_year (real/tmsis-analytic-file/001_base.sas:212) — sin definición en el proyecto
- macro last_best (real/tmsis-analytic-file/001_base.sas:212) — sin definición en el proyecto
- macro age_date_calculate (real/tmsis-analytic-file/001_base.sas:252) — sin definición en el proyecto
- macro drop_tables (real/tmsis-analytic-file/001_base.sas:302) — sin definición en el proyecto
- macro drop_tables (real/tmsis-analytic-file/001_base.sas:382) — sin definición en el proyecto
- macro unique_claims_ids (real/tmsis-analytic-file/001_base.sas:389) — sin definición en el proyecto
- macro table_id_cols (real/tmsis-analytic-file/001_base.sas:656) — sin definición en el proyecto

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
