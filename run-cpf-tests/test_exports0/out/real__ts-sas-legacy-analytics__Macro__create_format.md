# Job `job_create_format`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas` (sha256 `529f42d3a29f`)
- **Instrucciones:** 24 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.cntlin` ← SAS `cntlin` (&cntlin en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.DATA` ← SAS `DATA` (&DATA en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.default` ← SAS `default` (&default en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.fuzz` ← SAS `fuzz` (&fuzz en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.keep` ← SAS `keep` (&keep en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.max` ← SAS `max` (&max en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.min` ← SAS `min` (&min en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.NAME` ← SAS `NAME` (&NAME en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.START` ← SAS `START` (&START en real/ts-sas-legacy-analytics/Macro/create_format.sas:239)
- `context.WHERE` ← SAS `WHERE` (&WHERE en real/ts-sas-legacy-analytics/Macro/create_format.sas:301)

## Conexiones a crear

- `_crtfmt_` (spde, %sysfunc(pathname(work))) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

## Definición de macro auxiliar `%create_format`(DATA, LIB, CAT, NAME, TYPE, START, END, LABEL, DEFAULT, MIN, MAX, FUZZ, OTHER, KEEP, WHERE, DEDUP)

### 1. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s215` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:215`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:215 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `DATA,         _req=1,_words=1,_case=N` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:215 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 2. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s216` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:216`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_215_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:216 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `LIB,          _req=1,_words=0,_case=U` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:216 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 3. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s217` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:217`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_216_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:217 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `CAT,          _req=1,_words=0,_case=U` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:217 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 4. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s218` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:218`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_217_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:218 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `NAME,         _req=1,_words=0,_case=U` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:218 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 5. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s219` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:219`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_218_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:219 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `TYPE,         _req=1,_words=0,_case=U,_val=CHR_FORMAT NUM_FORMAT CHR_INFORMAT NUM_INFORMAT` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:219 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 6. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s220` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:220`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_219_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:220 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `START,        _req=1,_words=0,_case=U` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:220 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 7. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s221` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:221`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_220_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:221 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `END,          _req=0,_words=0,_case=U` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:221 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 8. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s222` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:222`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_221_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:222 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `LABEL,        _req=1,_words=0,_case=U` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:222 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 9. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s223` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:223`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_222_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:223 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `DEFAULT,      _req=0,_words=0,_case=U,_val=POSITIVE` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:223 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 10. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s224` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:224`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_223_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:224 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `MIN,          _req=0,_words=0,_case=U,_val=POSITIVE` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:224 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 11. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s225` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:225`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_224_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:225 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `MAX,          _req=0,_words=0,_case=U,_val=POSITIVE` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:225 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 12. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s226` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:226`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_225_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:226 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `FUZZ,         _req=0,_words=0,_case=U` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:226 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 13. Invocar macro %parmv

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s227` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:227`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_226_macro_call_1`
- **Propiedades:**
  - `PROCESS` (Job) = `parmv` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:227 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `DEDUP,        _req=1,_words=0,_case=U,_val=0 1` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:227 · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

### 14. Leer &DATA

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:create_format:s239` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:239`
- **Conexiones:** OnSubjobOk desde `m:create_format:op_227_macro_call_1`
- **Propiedades:**
  - `TABLE` = `&DATA` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:239
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:create_format:op_239_read_1_row_count`, `vc_m:create_format:op_239_read_1_schema`

### 15. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:create_format:s239` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:239`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `m:create_format:op_239_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: &keep` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:239 · nombre oficial
- **Esquema:** `&keep` _(tipos por determinar)_
- **Pruebas:** `vc_m:create_format:op_239_select_columns_1_schema`

### 16. Filtrar filas (sentencia WHERE): &WHERE

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:create_format:s239` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:301`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:create_format:op_239_select_columns_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:301 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `context.WHERE` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:301 · nombre oficial
- **Expresión** (línea 301): SAS `&WHERE` → Java `context.WHERE`
  - ⚠ Macrovariable &WHERE → context.WHERE (crear variable de contexto)
- **Pruebas:** `vc_m:create_format:op_301_filter_1_row_count`, `vc_m:create_format:op_301_filter_1_nulls`, `vc_m:create_format:op_301_filter_1_empty`

### 17. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `m:create_format:s239` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:239`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:create_format:op_301_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `8 asignaciones, 2 condicionales` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:239
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `FMTNAME`, `TYPE`, `START`, `DEFAULT`, `MIN`, `MAX`, `FUZZ`, `HLO` _(tipos por determinar)_
- **Expresión** (línea 304): SAS `&NAME` → Java `context.NAME`
  - ⚠ Macrovariable &NAME → context.NAME (crear variable de contexto)
- **Expresión** (línea 305): SAS `"&type"` → Java `"&type"`
- **Expresión** (línea 306): SAS `&START` → Java `context.START`
  - ⚠ Macrovariable &START → context.START (crear variable de contexto)
- **Expresión** (línea 311): SAS `&default` → Java `context.default`
  - ⚠ Macrovariable &default → context.default (crear variable de contexto)
- **Expresión** (línea 315): SAS `&min` → Java `context.min`
  - ⚠ Macrovariable &min → context.min (crear variable de contexto)
- **Expresión** (línea 319): SAS `&max` → Java `context.max`
  - ⚠ Macrovariable &max → context.max (crear variable de contexto)
- **Expresión** (línea 323): SAS `&fuzz` → Java `context.fuzz`
  - ⚠ Macrovariable &fuzz → context.fuzz (crear variable de contexto)
- **Expresión** (línea 349): SAS `"O"` → Java `"O"`
- **Expresión** (línea 266): SAS `if _n_=1 then call missing(of _all_)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 329): SAS `if (_last_) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_m:create_format:op_239_compute_1_nulls`, `vc_m:create_format:op_239_compute_1_dates`, `vc_m:create_format:op_239_compute_1_numeric`

### 18. Escribir &cntlin

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:create_format:s239` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:239`
- **Conexiones:** Main desde `m:create_format:op_239_compute_1`
- **Propiedades:**
  - `TABLE` = `&cntlin` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:239
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:239
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:239
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:create_format:op_239_write_1_row_count`, `vc_m:create_format:op_239_write_1_schema`

### 19. Leer _crtfmt_._cntlin_

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:create_format:s385` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:385`
- **Conexiones:** OnSubjobOk desde `m:create_format:op_239_write_1`
- **Propiedades:**
  - `TABLE` = `_cntlin_` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:385
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería _crtfmt_ es de tipo BASE en %sysfunc(pathname(work)): Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:create_format:op_385_read_1_row_count`, `vc_m:create_format:op_385_read_1_schema`

### 20. Ordenar por fmtname, start

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `m:create_format:s385` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:385`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `m:create_format:op_385_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `fmtname, start` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:385 · nombre oficial
- **Esquema:** `fmtname`, `start` _(tipos por determinar)_
- **Pruebas:** `vc_m:create_format:op_385_sort_1_ordering`

### 21. Eliminar duplicados

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `m:create_format:s385` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:385`
- **Conexiones:** Main desde `m:create_format:op_385_sort_1`
- **Propiedades:**
  - `UNIQUE_KEY` = `fmtname, start` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:385
- **Esquema:** `fmtname`, `start` _(tipos por determinar)_
- **Pendientes:**
  - Definir la clave y la lógica para conservar la fila correcta por grupo; confirmar una opción disponible en la instalación actual.
- **Pruebas:** `vc_m:create_format:op_385_dedupe_1_duplicates`

### 22. Escribir &cntlin

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:create_format:s385` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:385`
- **Conexiones:** Main desde `m:create_format:op_385_dedupe_1`
- **Propiedades:**
  - `TABLE` = `&cntlin` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:385
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:385
  - `DATA_ACTION` = `INSERT` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:385
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:create_format:op_385_write_1_row_count`, `vc_m:create_format:op_385_write_1_schema`

### 23. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `m:create_format:s400` · **Confianza:** medium · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:400`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_385_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = _por configurar_ — regla mappings · nombre oficial
  - `INTABLE` (Inline Table) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_m:create_format:op_400_format_definition_1_schema`

### 24. Invocar macro %quit

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:create_format:s403` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/create_format.sas:403`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:create_format:op_400_format_definition_1`
- **Propiedades:**
  - `PROCESS` (Job) = `quit` — SAS real/ts-sas-legacy-analytics/Macro/create_format.sas:403 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Macro sin definición en el proyecto
- **Pendientes:**
  - Job o joblet hijo que implementa la macro

## Sin resolver

- dataset_dynamic &DATA (real/ts-sas-legacy-analytics/Macro/create_format.sas:239) — nombre de dataset con macrovariables
- dataset_dynamic &cntlin (real/ts-sas-legacy-analytics/Macro/create_format.sas:239) — nombre de dataset con macrovariables
- dataset_dynamic &cntlin (real/ts-sas-legacy-analytics/Macro/create_format.sas:385) — nombre de dataset con macrovariables
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:215) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:216) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:217) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:218) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:219) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:220) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:221) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:222) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:223) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:224) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:225) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:226) — sin definición en el proyecto
- macro parmv (real/ts-sas-legacy-analytics/Macro/create_format.sas:227) — sin definición en el proyecto
- macro nobs (real/ts-sas-legacy-analytics/Macro/create_format.sas:390) — sin definición en el proyecto
- macro quit (real/ts-sas-legacy-analytics/Macro/create_format.sas:403) — sin definición en el proyecto

## Casos de validación

- `vc_m:create_format:op_239_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:create_format:op_239_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:create_format:op_239_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_m:create_format:op_301_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:create_format:op_301_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:create_format:op_301_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:create_format:op_239_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_m:create_format:op_239_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_m:create_format:op_239_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_m:create_format:op_239_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:create_format:op_239_write_1_schema` (schema): Esquema destino
- `vc_m:create_format:op_385_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:create_format:op_385_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:create_format:op_385_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_m:create_format:op_385_dedupe_1_duplicates` (duplicates): Se conserva la misma fila por clave (NODUPKEY conserva la primera)
- `vc_m:create_format:op_385_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:create_format:op_385_write_1_schema` (schema): Esquema destino
- `vc_m:create_format:op_400_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
