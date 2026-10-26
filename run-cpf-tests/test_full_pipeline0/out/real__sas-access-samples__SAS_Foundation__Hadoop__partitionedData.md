# Job `job_partitioneddata`

- **Programa SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas` (sha256 `bc5025a96512`)
- **Instrucciones:** 7 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `mydblib` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s28` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:28`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 2. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s35` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:37`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_28_maintenance_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_37_read_file_1_row_count`, `vc_op_37_read_file_1_nulls`

### 3. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s35` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:35`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_35_inline_data_1_row_count`

### 4. Escribir mydblib.dpart

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s35` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:35`
- **Conexiones:** Main desde `op_37_read_file_1`
- **Propiedades:**
  - `TABLE` = `dpart` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:35
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:35
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:35
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_35_write_1_row_count`, `vc_op_35_write_1_schema`

### 5. Leer mydblib.dpart

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s60` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:61`
- **Conexiones:** OnSubjobOk desde `op_35_write_1`
- **Propiedades:**
  - `TABLE` = `dpart` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:61
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset producido antes en este programa (op_35_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_61_read_1_row_count`, `vc_op_61_read_1_schema`

### 6. Filtrar filas (WHERE): dates = '01mar98'd

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s60` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:61`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_61_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 61): SAS `dates = '01mar98'd` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_op_61_filter_1_row_count`, `vc_op_61_filter_1_nulls`, `vc_op_61_filter_1_empty`

### 7. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s60` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:61`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_61_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `flight` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/partitionedData.sas:61
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `flight` _(tipos por determinar)_
- **Pruebas:** `vc_op_61_project_1_schema`

## Casos de validación

- `vc_op_37_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_37_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_35_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_35_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_35_write_1_schema` (schema): Esquema destino
- `vc_op_61_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_61_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_61_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_61_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_61_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_61_project_1_schema` (schema): Columnas y tipos de salida

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
