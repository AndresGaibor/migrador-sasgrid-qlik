# Job `job_dsc_appendtocustomerdb`

- **Programa SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas` (sha256 `1c70d9431fd8`)
- **Instrucciones:** 14 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.range_id` ← SAS `range_id` (&range_id en real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10)

## Conexiones a crear

- `dictionary` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

## Definición de macro auxiliar `%dsc_appendtocustomerdb`(range_id)

### 1. Leer Download_details

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_appendtocustomerdb:s9` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10`
- **Propiedades:**
  - `TABLE` = `download_details` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_10_read_1_row_count`, `vc_m:dsc_appendtocustomerdb:op_10_read_1_schema`

### 2. Filtrar filas (WHERE): range_id= &range_id.

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:dsc_appendtocustomerdb:s9` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:dsc_appendtocustomerdb:op_10_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `range_id == &range_id.` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `range_id` _(tipos por determinar)_
- **Expresión** (línea 10): SAS `range_id= &range_id.` → Java `(input_row.range_id == context.range_id)`
  - ⚠ Macrovariable &range_id → context.range_id (crear variable de contexto)
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_10_filter_1_row_count`, `vc_m:dsc_appendtocustomerdb:op_10_filter_1_nulls`, `vc_m:dsc_appendtocustomerdb:op_10_filter_1_empty`

### 3. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:dsc_appendtocustomerdb:s9` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_appendtocustomerdb:op_10_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `distinct entityName, entity_cd` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `entity_cd` _(tipos por determinar)_
- **Expresión** (línea 10): SAS `distinct entityName` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_10_project_1_schema`

### 4. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:dsc_appendtocustomerdb:s9` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:dsc_appendtocustomerdb:op_10_project_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=Entities separated by '` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:10 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 5. Leer dictionary.tables

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_appendtocustomerdb:s35` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:36`
- **Conexiones:** OnSubjobOk desde `m:dsc_appendtocustomerdb:op_10_set_variable_1`
- **Propiedades:**
  - `TABLE` = `tables` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:36
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dictionary es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_36_read_1_row_count`, `vc_m:dsc_appendtocustomerdb:op_36_read_1_schema`

### 6. Filtrar filas (WHERE): upcase(libname) = "DSCEXTR" and MEMNAME like "&current_entity_cd%"

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:dsc_appendtocustomerdb:s35` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:36`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:dsc_appendtocustomerdb:op_36_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 36): SAS `upcase(libname) = "DSCEXTR" and MEMNAME like "&current_entity_cd%"` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_36_filter_1_row_count`, `vc_m:dsc_appendtocustomerdb:op_36_filter_1_nulls`, `vc_m:dsc_appendtocustomerdb:op_36_filter_1_empty`

### 7. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:dsc_appendtocustomerdb:s35` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:36`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:dsc_appendtocustomerdb:op_36_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `'DSCEXTR.' || memname` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:36
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `memname` _(tipos por determinar)_
- **Expresión** (línea 36): SAS `'DSCEXTR.' || memname` → Java `("DSCEXTR." + input_row.memname)`
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_36_project_1_schema`

### 8. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `m:dsc_appendtocustomerdb:s35` · **Confianza:** medium · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:36`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `m:dsc_appendtocustomerdb:op_36_project_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=TableParts separated by ' '` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:36 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 9. Leer &TableParts.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:dsc_appendtocustomerdb:s44` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:44`
- **Conexiones:** OnSubjobOk desde `m:dsc_appendtocustomerdb:op_36_set_variable_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_44_read_1_row_count`, `vc_m:dsc_appendtocustomerdb:op_44_read_1_schema`

### 10. Escribir &&entity&entityNum.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:dsc_appendtocustomerdb:s44` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:44`
- **Conexiones:** Main desde `m:dsc_appendtocustomerdb:op_44_read_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:44
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:44
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_44_write_1_row_count`, `vc_m:dsc_appendtocustomerdb:op_44_write_1_schema`

### 11. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:dsc_appendtocustomerdb:s48` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:48`
- **Conexiones:** OnSubjobOk desde `m:dsc_appendtocustomerdb:op_44_write_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:48
  - `TABLE_ACTION` = `NONE` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:48
- **Pendientes:**
  - Tabla base destino
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_48_append_1_row_count`

### 12. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:dsc_appendtocustomerdb:s55` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:55`
- **Conexiones:** OnSubjobOk desde `m:dsc_appendtocustomerdb:op_48_append_1`
- **Propiedades:**
  - `TABLE` = `download_history` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:55
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:55
  - `TABLE_ACTION` = `NONE` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:55
- **Pendientes:**
  - Tabla base destino
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_55_append_1_row_count`

### 13. Añadir filas a una tabla existente

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tDBOutput`
- **Subjob:** `m:dsc_appendtocustomerdb:s59` · **Confianza:** high · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:59`
- **Conexiones:** OnSubjobOk desde `m:dsc_appendtocustomerdb:op_55_append_1`
- **Propiedades:**
  - `TABLE` = `download_history` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:59
  - `DATA_ACTION` = `INSERT` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:59
  - `TABLE_ACTION` = `NONE` — SAS real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:59
- **Pendientes:**
  - Tabla base destino
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:dsc_appendtocustomerdb:op_59_append_1_row_count`

### 14. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:dsc_appendtocustomerdb:s65` · **Confianza:** low · **Origen SAS:** `real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:65`
- **Conexiones:** OnSubjobOk desde `m:dsc_appendtocustomerdb:op_59_append_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Sin resolver

- dataset_dynamic &TableParts. (real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:44) — nombre de dataset con macrovariables
- dataset_dynamic &&entity&entityNum. (real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:44) — nombre de dataset con macrovariables
- dataset_dynamic &&entity&entityNum. (real/ci360-download-client/macros/dsc_appendtocustomerdb.sas:48) — nombre de dataset con macrovariables

## Casos de validación

- `vc_m:dsc_appendtocustomerdb:op_10_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_appendtocustomerdb:op_10_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_appendtocustomerdb:op_10_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:dsc_appendtocustomerdb:op_10_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:dsc_appendtocustomerdb:op_10_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:dsc_appendtocustomerdb:op_10_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:dsc_appendtocustomerdb:op_36_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_appendtocustomerdb:op_36_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_appendtocustomerdb:op_36_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:dsc_appendtocustomerdb:op_36_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:dsc_appendtocustomerdb:op_36_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:dsc_appendtocustomerdb:op_36_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:dsc_appendtocustomerdb:op_44_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:dsc_appendtocustomerdb:op_44_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:dsc_appendtocustomerdb:op_44_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:dsc_appendtocustomerdb:op_44_write_1_schema` (schema): Esquema destino
- `vc_m:dsc_appendtocustomerdb:op_48_append_1_row_count` (row_count): Filas añadidas
- `vc_m:dsc_appendtocustomerdb:op_55_append_1_row_count` (row_count): Filas añadidas
- `vc_m:dsc_appendtocustomerdb:op_59_append_1_row_count` (row_count): Filas añadidas

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
