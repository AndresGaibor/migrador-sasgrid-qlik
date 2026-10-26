# Job `job_createtableorview`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas` (sha256 `560b94d8ca6e`)
- **Instrucciones:** 57 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context._out_fileref` ← SAS `_out_fileref` (&_out_fileref en real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:758)
- `context.data` ← SAS `data` (&data en real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:611)
- `context.data_libname` ← SAS `data_libname` (&data_libname en real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787)
- `context.data_memname` ← SAS `data_memname` (&data_memname en real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787)
- `context.shell_libname` ← SAS `shell_libname` (&shell_libname en real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803)
- `context.shell_memname` ← SAS `shell_memname` (&shell_memname en real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803)
- `context.vars_sql` ← SAS `vars_sql` (&vars_sql en real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787)

## Conexiones a crear

- `dictionary` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

## Definición de macro auxiliar `%CreateTableOrView`(DATA, OUT, KEEP, DROP, BY, INDEX, WHERE, RENAME, META_COLUMNS, META_COLUMNS_COND, SHELL, LANG, TYPE, FILE, APPEND, RUN, PRE_PROCESS, POST_PROCESS)

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s573` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:573`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:573 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `DATA,               _req=1,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:573 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s574` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:574`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_573_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:574 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `OUT,                _req=1,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:574 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s575` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:575`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_574_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:575 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `KEEP,               _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:575 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 4. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s576` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:576`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_575_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:576 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `DROP,               _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:576 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 5. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s577` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:577`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_576_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:577 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `BY,                 _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:577 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 6. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s578` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:578`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_577_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:578 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `INDEX,              _req=0,_words=1,_case=U,_val=0 1` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:578 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 7. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s579` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:579`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_578_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:579 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `WHERE,              _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:579 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 8. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s580` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:580`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_579_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:580 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `RENAME,             _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:580 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 9. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s581` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:581`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_580_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:581 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `META_COLUMNS,       _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:581 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 10. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s582` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:582`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_581_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:582 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `META_COLUMNS_COND,  _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:582 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 11. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s583` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:583`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_582_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:583 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `SHELL,              _req=0,_words=0,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:583 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 12. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s584` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:584`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_583_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:584 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `LANG,               _req=1,_words=0,_case=U,_val=SAS SQL` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:584 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 13. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s585` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:585`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_584_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:585 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `TYPE,               _req=1,_words=0,_case=U,_val=TABLE VIEW` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:585 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 14. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s586` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:586`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_585_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:586 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `FILE,               _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:586 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 15. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s587` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:587`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_586_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:587 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `APPEND,             _req=0,_words=0,_case=U,_val=0 1` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:587 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 16. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s588` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:588`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_587_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:588 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `RUN,                _req=0,_words=0,_case=U,_val=0 1` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:588 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 17. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s589` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:589`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_588_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:589 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `PRE_PROCESS,        _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:589 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 18. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s590` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:590`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_589_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:590 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `POST_PROCESS,       _req=0,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:590 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 19. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s611` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:611`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_590_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:611 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `_msg=&data data set or view does not exist` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:611 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 20. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s617` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:617`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_611_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:617 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `_msg=The descending option is not supported for indexes` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:617 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 21. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s625` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:625`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_617_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:625 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `_msg=Indexes are not supported for views` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:625 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 22. Invocar macro %dump_mvars

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s697` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:697`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_625_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `dump_mvars` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:697 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `
   data     data_libname   data_memname   data_options
   out      out_libname    out_memname    out_options
   shell    shell_libname  shell_memname
   dslabel
   keep
   drop
   rename
   where
   by
   index    index_stmt
   file     run
` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:697 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %dump_mvars (definida en real/ts-sas-legacy-analytics/Macro/batch_submit.sas)

### 23. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:CreateTableOrView:s716` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:716`
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_697_macro_call_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 24. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:CreateTableOrView:s758` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:758`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_716_maintenance_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:758 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `_msg=&_out_fileref fileref is not allocated` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:758 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 25. Leer dictionary.columns

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:CreateTableOrView:s786` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787`
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_758_macro_call_1`
- **Propiedades:**
  - `TABLE` = `columns` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dictionary es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:CreateTableOrView:op_787_read_1_row_count`, `vc_m:CreateTableOrView:op_787_read_1_schema`

### 26. Filtrar filas (WHERE): libname="%upcase(&data_libname)" and memname="%upcase(&data_memname)"

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:CreateTableOrView:s786` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_787_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `libname == "%upcase(&data_libname)"; memname == "%upcase(&data_memname)"` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `libname`, `memname` _(tipos por determinar)_
- **Expresión** (línea 787): SAS `libname="%upcase(&data_libname)" and memname="%upcase(&data_memname)"` → Java `(input_row.libname.equals("%upcase(&data_libname)") && input_row.memname.equals("%upcase(&data_memname)"))`
- **Pruebas:** `vc_m:CreateTableOrView:op_787_filter_1_row_count`, `vc_m:CreateTableOrView:op_787_filter_1_nulls`, `vc_m:CreateTableOrView:op_787_filter_1_empty`

### 27. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:CreateTableOrView:s786` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_787_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `_order_, _uname_, &vars_sql` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `_order_`, `_uname_`, `name` _(tipos por determinar)_
- **Expresión** (línea 787): SAS `monotonic()+2000` → _sin traducción automática_
  - ⚠ Sin traducción automática: función monotonic
- **Expresión** (línea 787): SAS `upcase(name)` → Java `input_row.name.toUpperCase()`
  - ⚠ upcase(): comprobar nulos antes de invocar el método
- **Expresión** (línea 787): SAS `&vars_sql` → Java `context.vars_sql`
  - ⚠ Macrovariable &vars_sql → context.vars_sql (crear variable de contexto)
- **Pruebas:** `vc_m:CreateTableOrView:op_787_project_1_schema`

### 28. Ordenar por varnum

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:CreateTableOrView:s786` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_787_project_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `varnum` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787 · nombre oficial
- **Esquema:** `varnum` _(tipos por determinar)_
- **Pruebas:** `vc_m:CreateTableOrView:op_787_sort_1_ordering`

### 29. Escribir _meta_source_ (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:CreateTableOrView:s786` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787`
- **Conexiones:** Main desde `m:CreateTableOrView:op_787_sort_1`
- **Propiedades:**
  - `TABLE` = `_meta_source_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:787
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:CreateTableOrView:op_787_write_1_row_count`, `vc_m:CreateTableOrView:op_787_write_1_schema`

### 30. Leer dictionary.columns

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:CreateTableOrView:s802` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803`
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_787_write_1`
- **Propiedades:**
  - `TABLE` = `columns` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dictionary es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:CreateTableOrView:op_803_read_1_row_count`, `vc_m:CreateTableOrView:op_803_read_1_schema`

### 31. Filtrar filas (WHERE): libname="%upcase(&shell_libname)" and memname="%upcase(&shell_memname)"

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:CreateTableOrView:s802` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_803_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `libname == "%upcase(&shell_libname)"; memname == "%upcase(&shell_memname)"` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `libname`, `memname` _(tipos por determinar)_
- **Expresión** (línea 803): SAS `libname="%upcase(&shell_libname)" and memname="%upcase(&shell_memname)"` → Java `(input_row.libname.equals("%upcase(&shell_libname)") && input_row.memname.equals("%upcase(&shell_memname)"))`
- **Pruebas:** `vc_m:CreateTableOrView:op_803_filter_1_row_count`, `vc_m:CreateTableOrView:op_803_filter_1_nulls`, `vc_m:CreateTableOrView:op_803_filter_1_empty`

### 32. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:CreateTableOrView:s802` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_803_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `_order_, _uname_, &vars_sql` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `_order_`, `_uname_`, `name` _(tipos por determinar)_
- **Expresión** (línea 803): SAS `monotonic()` → _sin traducción automática_
  - ⚠ Sin traducción automática: función monotonic
- **Expresión** (línea 803): SAS `upcase(name)` → Java `input_row.name.toUpperCase()`
  - ⚠ upcase(): comprobar nulos antes de invocar el método
- **Expresión** (línea 803): SAS `&vars_sql` → Java `context.vars_sql`
  - ⚠ Macrovariable &vars_sql → context.vars_sql (crear variable de contexto)
- **Pruebas:** `vc_m:CreateTableOrView:op_803_project_1_schema`

### 33. Ordenar por varnum

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:CreateTableOrView:s802` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_803_project_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `varnum` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803 · nombre oficial
- **Esquema:** `varnum` _(tipos por determinar)_
- **Pruebas:** `vc_m:CreateTableOrView:op_803_sort_1_ordering`

### 34. Escribir _meta_shell_ (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:CreateTableOrView:s802` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803`
- **Conexiones:** Main desde `m:CreateTableOrView:op_803_sort_1`
- **Propiedades:**
  - `TABLE` = `_meta_shell_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:803
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:CreateTableOrView:op_803_write_1_row_count`, `vc_m:CreateTableOrView:op_803_write_1_schema`

### 35. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:CreateTableOrView:s819` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:820`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_803_write_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `_order_, _uname_, *` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:820
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `_order_`, `_uname_`, `name` _(tipos por determinar)_
- **Expresión** (línea 820): SAS `monotonic()+1000` → _sin traducción automática_
  - ⚠ Sin traducción automática: función monotonic
- **Expresión** (línea 820): SAS `upcase(name)` → Java `input_row.name.toUpperCase()`
  - ⚠ upcase(): comprobar nulos antes de invocar el método
- **Pruebas:** `vc_m:CreateTableOrView:op_820_project_1_schema`

### 36. Escribir _meta_columns_ (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:CreateTableOrView:s819` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:820`
- **Conexiones:** Main desde `m:CreateTableOrView:op_820_project_1`
- **Propiedades:**
  - `TABLE` = `_meta_columns_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:820
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:820
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:820
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:CreateTableOrView:op_820_write_1_row_count`, `vc_m:CreateTableOrView:op_820_write_1_schema`

### 37. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:CreateTableOrView:s819` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:827`
- **Conexiones:** Main desde `m:CreateTableOrView:op_820_write_1`
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 38. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:CreateTableOrView:s837` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_827_unsupported_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `8 asignaciones, 0 condicionales` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `buffer`, `rx`, `i`, `word`, `name`, `_uname_` _(tipos por determinar)_
- **Expresión** (línea 839): SAS `"&rename"` → Java `"&rename"`
- **Expresión** (línea 842): SAS `prxparse("s/\s*=\s*/=/")` → _sin traducción automática_
  - ⚠ Sin traducción automática: función prxparse
- **Expresión** (línea 843): SAS `prxchange(rx,-1,buffer)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función prxchange
- **Expresión** (línea 845): SAS `1` → Java `1`
- **Expresión** (línea 846): SAS `scan(buffer,i," ")` → _sin traducción automática_
  - ⚠ Sin traducción automática: función scan
- **Expresión** (línea 848): SAS `scan(word,1,"=")` → _sin traducción automática_
  - ⚠ Sin traducción automática: función scan
- **Expresión** (línea 850): SAS `upcase(name)` → Java `input_row.name.toUpperCase()`
  - ⚠ upcase(): comprobar nulos antes de invocar el método
- **Expresión** (línea 853): SAS `scan(buffer,i," ")` → _sin traducción automática_
  - ⚠ Sin traducción automática: función scan
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:CreateTableOrView:op_837_compute_1_nulls`, `vc_m:CreateTableOrView:op_837_compute_1_dates`, `vc_m:CreateTableOrView:op_837_compute_1_numeric`

### 39. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:CreateTableOrView:s837` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_837_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: _uname_, name, rename` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837 · nombre oficial
- **Esquema:** `_uname_`, `name`, `rename` _(tipos por determinar)_
- **Pruebas:** `vc_m:CreateTableOrView:op_837_select_columns_1_schema`

### 40. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:CreateTableOrView:s837` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_837_select_columns_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_m:CreateTableOrView:op_837_rename_1_schema`

### 41. Escribir _meta_rename_

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:CreateTableOrView:s837` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837`
- **Conexiones:** Main desde `m:CreateTableOrView:op_837_rename_1`
- **Propiedades:**
  - `TABLE` = `_meta_rename_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:837
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:CreateTableOrView:op_837_write_1_row_count`, `vc_m:CreateTableOrView:op_837_write_1_schema`

### 42. Leer %if

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_837_write_1`
- **Propiedades:**
  - `TABLE` = `%if` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:CreateTableOrView:op_859_read_1_row_count`, `vc_m:CreateTableOrView:op_859_read_1_schema`

### 43. Leer %sysfunc

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Propiedades:**
  - `TABLE` = `%sysfunc` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:CreateTableOrView:op_859_read_2_row_count`, `vc_m:CreateTableOrView:op_859_read_2_schema`

### 44. Leer %then

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Propiedades:**
  - `TABLE` = `%then` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:CreateTableOrView:op_859_read_3_row_count`, `vc_m:CreateTableOrView:op_859_read_3_schema`

### 45. Leer _meta_source_

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Propiedades:**
  - `TABLE` = `_meta_source_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:CreateTableOrView:op_859_read_4_row_count`, `vc_m:CreateTableOrView:op_859_read_4_schema`

### 46. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_859_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `_order_ → _order_so` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
- **Esquema:** `_order_so` _(tipos por determinar)_
- **Pruebas:** `vc_m:CreateTableOrView:op_859_rename_1_schema`

### 47. Unir (merge_by): %if, %sysfunc, %then, work._meta_source_

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_859_read_1`, Lookup desde `m:CreateTableOrView:op_859_read_2`, Lookup desde `m:CreateTableOrView:op_859_read_3`, Lookup desde `m:CreateTableOrView:op_859_read_4`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `_uname_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
- **Esquema:** `_uname_` _(tipos por determinar)_
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_m:CreateTableOrView:op_859_join_1_duplicates`, `vc_m:CreateTableOrView:op_859_join_1_row_count`, `vc_m:CreateTableOrView:op_859_join_1_nulls`

### 48. Filtrar filas (IF subsetting): _uname_ in (%upcase(%seplist(&keep,nest=QQ)))

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:875`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_859_join_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 875): SAS `_uname_ in (%upcase(%seplist(&keep,nest=QQ)))` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '%upcase(%sep'
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:CreateTableOrView:op_875_filter_1_row_count`, `vc_m:CreateTableOrView:op_875_filter_1_nulls`, `vc_m:CreateTableOrView:op_875_filter_1_empty`

### 49. Filtrar filas (IF subsetting): in_meta

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:885`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_875_filter_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:885 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `input_row.in_meta` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:885 · nombre oficial
- **Esquema:** `in_meta` _(tipos por determinar)_
- **Expresión** (línea 885): SAS `in_meta` → Java `input_row.in_meta`
- **Pruebas:** `vc_m:CreateTableOrView:op_885_filter_1_row_count`, `vc_m:CreateTableOrView:op_885_filter_1_nulls`, `vc_m:CreateTableOrView:op_885_filter_1_empty`

### 50. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_885_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 2 condicionales` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `_order_`, `in_meta` _(tipos por determinar)_
- **Expresión** (línea 870): SAS `coalesce(_order_sh,_order_md,_order_so)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función coalesce
- **Expresión** (línea 878): SAS `max(0,in_shell,in_columns,in_rename)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función max
- **Expresión** (línea 874): SAS `if _uname_ in (%upcase(%seplist(&drop,nest=QQ))) then delete` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 880): SAS `if (in_meta and not in_source) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:CreateTableOrView:op_859_compute_1_nulls`, `vc_m:CreateTableOrView:op_859_compute_1_dates`, `vc_m:CreateTableOrView:op_859_compute_1_numeric`

### 51. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_859_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: _order_so, _order_sh, _order_md, in_source, in_shell, in_columns, in_rename` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859 · nombre oficial
- **Pruebas:** `vc_m:CreateTableOrView:op_859_select_columns_1_schema`

### 52. Escribir _meta_columns_

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:CreateTableOrView:s859` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859`
- **Conexiones:** Main desde `m:CreateTableOrView:op_859_select_columns_1`
- **Propiedades:**
  - `TABLE` = `_meta_columns_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:859
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:CreateTableOrView:op_859_write_1_row_count`, `vc_m:CreateTableOrView:op_859_write_1_schema`

### 53. Leer _meta_columns_

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:CreateTableOrView:s889` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889`
- **Conexiones:** OnSubjobOk desde `m:CreateTableOrView:op_859_write_1`
- **Propiedades:**
  - `TABLE` = `_meta_columns_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:CreateTableOrView:op_889_read_1_row_count`, `vc_m:CreateTableOrView:op_889_read_1_schema`

### 54. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:CreateTableOrView:s889` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_889_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 3 condicionales` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `buffer` _(tipos por determinar)_
- **Expresión** (línea 896): SAS `catx(" ",buffer,name)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función catx
- **Expresión** (línea 897): SAS `if ^missing(rename) then buffer2=catx(" ",buffer2,catx("=",name,rename))` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 898): SAS `if (eof) then call symputx("keep",buffer,"F")` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 899): SAS `if (eof) then call symputx("rename",buffer2,"F")` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:CreateTableOrView:op_889_compute_1_nulls`, `vc_m:CreateTableOrView:op_889_compute_1_dates`, `vc_m:CreateTableOrView:op_889_compute_1_numeric`

### 55. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `m:CreateTableOrView:s889` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889`
- **Conexiones:** Main desde `m:CreateTableOrView:op_889_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_m:CreateTableOrView:op_889_stateful_1_ordering`, `vc_m:CreateTableOrView:op_889_stateful_1_duplicates`

### 56. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:CreateTableOrView:s889` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:CreateTableOrView:op_889_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: buffer, buffer2` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889 · nombre oficial
- **Pruebas:** `vc_m:CreateTableOrView:op_889_select_columns_1_schema`

### 57. Escribir _meta_columns_

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:CreateTableOrView:s889` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889`
- **Conexiones:** Main desde `m:CreateTableOrView:op_889_select_columns_1`
- **Propiedades:**
  - `TABLE` = `_meta_columns_` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:889
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:CreateTableOrView:op_889_write_1_row_count`, `vc_m:CreateTableOrView:op_889_write_1_schema`

## Sin resolver

- dataset_dynamic &data (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:996) — nombre de dataset con macrovariables
- dataset_dynamic &out (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:996) — nombre de dataset con macrovariables
- dataset_dynamic &out (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:1042) — nombre de dataset con macrovariables
- dataset_dynamic &out_saved (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:1042) — nombre de dataset con macrovariables
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:573) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:574) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:575) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:576) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:577) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:578) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:579) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:580) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:581) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:582) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:583) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:584) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:585) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:586) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:587) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:588) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:589) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:590) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:611) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:617) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:625) — sin definición en el proyecto
- macro data_attr (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:640) — sin definición en el proyecto
- macro count_words (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:683) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:758) — sin definición en el proyecto
- macro seplist (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:780) — sin definición en el proyecto
- macro seplist (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:874) — sin definición en el proyecto
- macro seplist (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:875) — sin definición en el proyecto
- macro varexist (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:954) — sin definición en el proyecto
- macro loop (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:1098) — sin definición en el proyecto
- macro splitvar (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:1166) — sin definición en el proyecto
- macro splitvar (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:1184) — sin definición en el proyecto
- macro loop (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:1345) — sin definición en el proyecto
- macro quit (real/ts-sas-legacy-analytics/Macro/CreateTableOrView.sas:1534) — sin definición en el proyecto

## Casos de validación

- `vc_m:CreateTableOrView:op_787_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:CreateTableOrView:op_787_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:CreateTableOrView:op_787_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:CreateTableOrView:op_787_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:CreateTableOrView:op_787_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:CreateTableOrView:op_787_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:CreateTableOrView:op_787_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:CreateTableOrView:op_787_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:CreateTableOrView:op_787_write_1_schema` (schema): Esquema destino
- `vc_m:CreateTableOrView:op_803_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:CreateTableOrView:op_803_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:CreateTableOrView:op_803_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:CreateTableOrView:op_803_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:CreateTableOrView:op_803_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:CreateTableOrView:op_803_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:CreateTableOrView:op_803_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:CreateTableOrView:op_803_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:CreateTableOrView:op_803_write_1_schema` (schema): Esquema destino
- `vc_m:CreateTableOrView:op_820_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:CreateTableOrView:op_820_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:CreateTableOrView:op_820_write_1_schema` (schema): Esquema destino
- `vc_m:CreateTableOrView:op_837_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:CreateTableOrView:op_837_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:CreateTableOrView:op_837_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:CreateTableOrView:op_837_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:CreateTableOrView:op_837_rename_1_schema` (schema): Nombres de columna finales
- `vc_m:CreateTableOrView:op_837_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:CreateTableOrView:op_837_write_1_schema` (schema): Esquema destino
- `vc_m:CreateTableOrView:op_859_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:CreateTableOrView:op_859_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:CreateTableOrView:op_859_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:CreateTableOrView:op_859_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:CreateTableOrView:op_859_read_3_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:CreateTableOrView:op_859_read_3_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:CreateTableOrView:op_859_read_4_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:CreateTableOrView:op_859_read_4_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:CreateTableOrView:op_859_rename_1_schema` (schema): Nombres de columna finales
- `vc_m:CreateTableOrView:op_859_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_m:CreateTableOrView:op_859_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_m:CreateTableOrView:op_859_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_m:CreateTableOrView:op_875_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:CreateTableOrView:op_875_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:CreateTableOrView:op_875_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:CreateTableOrView:op_885_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:CreateTableOrView:op_885_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:CreateTableOrView:op_885_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:CreateTableOrView:op_859_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:CreateTableOrView:op_859_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:CreateTableOrView:op_859_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:CreateTableOrView:op_859_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:CreateTableOrView:op_859_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:CreateTableOrView:op_859_write_1_schema` (schema): Esquema destino
- `vc_m:CreateTableOrView:op_889_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:CreateTableOrView:op_889_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:CreateTableOrView:op_889_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:CreateTableOrView:op_889_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:CreateTableOrView:op_889_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:CreateTableOrView:op_889_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_m:CreateTableOrView:op_889_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_m:CreateTableOrView:op_889_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:CreateTableOrView:op_889_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:CreateTableOrView:op_889_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
