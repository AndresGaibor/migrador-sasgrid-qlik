# Job `job_create_datasets`

- **Programa SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas` (sha256 `8a60a8fe35e5`)
- **Instrucciones:** 252 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `learn` (BASE, c:\books\learning) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s27` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:28`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_28_read_file_1_row_count`, `vc_op_28_read_file_1_nulls`

### 2. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s27` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:27`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_27_inline_data_1_row_count`

### 3. Escribir learn.address

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s27` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:27`
- **Conexiones:** Main desde `op_28_read_file_1`
- **Propiedades:**
  - `TABLE` = `address` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:27
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:27
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:27
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_27_write_1_row_count`, `vc_op_27_write_1_schema`

### 4. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s44` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:45`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_27_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_45_read_file_1_row_count`, `vc_op_45_read_file_1_nulls`

### 5. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s44` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:44`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_44_inline_data_1_row_count`

### 6. Escribir learn.chars

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s44` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:44`
- **Conexiones:** Main desde `op_45_read_file_1`
- **Propiedades:**
  - `TABLE` = `chars` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:44
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:44
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:44
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_44_write_1_row_count`, `vc_op_44_write_1_schema`

### 7. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s64` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:65`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_44_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_65_read_file_1_row_count`, `vc_op_65_read_file_1_nulls`

### 8. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s64` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:64`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_64_inline_data_1_row_count`

### 9. Escribir learn.careless

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s64` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:64`
- **Conexiones:** Main desde `op_65_read_file_1`
- **Propiedades:**
  - `TABLE` = `careless` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:64
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:64
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:64
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_64_write_1_row_count`, `vc_op_64_write_1_schema`

### 10. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s73` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:75`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_64_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_75_read_file_1_row_count`, `vc_op_75_read_file_1_nulls`

### 11. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s73` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:73`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_73_inline_data_1_row_count`

### 12. Escribir learn.cleaning

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s73` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:73`
- **Conexiones:** Main desde `op_75_read_file_1`
- **Propiedades:**
  - `TABLE` = `cleaning` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:73
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:73
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:73
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_73_write_1_row_count`, `vc_op_73_write_1_schema`

### 13. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s83` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:84`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_73_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_84_read_file_1_row_count`, `vc_op_84_read_file_1_nulls`

### 14. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s83` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:83`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_83_inline_data_1_row_count`

### 15. Escribir learn.oneper

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s83` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:83`
- **Conexiones:** Main desde `op_84_read_file_1`
- **Propiedades:**
  - `TABLE` = `oneper` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:83
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:83
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:83
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_83_write_1_row_count`, `vc_op_83_write_1_schema`

### 16. Leer learn.oneper

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s93` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:93`
- **Conexiones:** OnSubjobOk desde `op_83_write_1`
- **Propiedades:**
  - `TABLE` = `oneper` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:93
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset producido antes en este programa (op_83_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_93_read_1_row_count`, `vc_op_93_read_1_schema`

### 17. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s93` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:93`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_93_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:93
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Diagnosis` _(tipos por determinar)_
- **Expresión** (línea 98): SAS `Dx{Visit}` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '{Visit}'
- **Expresión** (línea 97): SAS `if missing(Dx{Visit}) then leave` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_93_compute_1_nulls`, `vc_op_93_compute_1_dates`, `vc_op_93_compute_1_numeric`

### 18. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s93` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:93`
- **Conexiones:** Main desde `op_93_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_93_stateful_1_ordering`, `vc_op_93_stateful_1_duplicates`

### 19. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s93` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:93`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_93_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Subj, Diagnosis, Visit` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:93 · nombre oficial
- **Esquema:** `Subj`, `Diagnosis`, `Visit` _(tipos por determinar)_
- **Pruebas:** `vc_op_93_select_columns_1_schema`

### 20. Escribir learn.manyper

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s93` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:93`
- **Conexiones:** Main desde `op_93_select_columns_1`
- **Propiedades:**
  - `TABLE` = `manyper` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:93
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:93
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:93
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_93_write_1_row_count`, `vc_op_93_write_1_schema`

### 21. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s105` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:106`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_93_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_106_read_file_1_row_count`, `vc_op_106_read_file_1_nulls`

### 22. Escribir learn.school

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s105` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:105`
- **Conexiones:** Main desde `op_106_read_file_1`
- **Propiedades:**
  - `TABLE` = `school` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:105
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:105
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:105
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_105_write_1_row_count`, `vc_op_105_write_1_schema`

### 23. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s115` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:116`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_105_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_116_read_file_1_row_count`, `vc_op_116_read_file_1_nulls`

### 24. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s115` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:115`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_115_inline_data_1_row_count`

### 25. Escribir learn.month_day_year

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s115` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:115`
- **Conexiones:** Main desde `op_116_read_file_1`
- **Propiedades:**
  - `TABLE` = `month_day_year` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:115
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:115
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:115
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_115_write_1_row_count`, `vc_op_115_write_1_schema`

### 26. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s124` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:125`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_115_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_125_read_file_1_row_count`, `vc_op_125_read_file_1_nulls`

### 27. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s124` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:124`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_124_inline_data_1_row_count`

### 28. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s124` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:124`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_125_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:124
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Quantity`, `UnitCost`, `TotalSales` _(tipos por determinar)_
- **Expresión** (línea 133): SAS `Quantity * UnitCost` → Java `(input_row.Quantity * input_row.UnitCost)`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_124_compute_1_nulls`, `vc_op_124_compute_1_dates`, `vc_op_124_compute_1_numeric`

### 29. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s124` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:124`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_124_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Date` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:124 · nombre oficial
- **Pruebas:** `vc_op_124_select_columns_1_schema`

### 30. Escribir learn.sales

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s124` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:124`
- **Conexiones:** Main desde `op_124_select_columns_1`
- **Propiedades:**
  - `TABLE` = `sales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:124
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:124
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:124
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_124_write_1_row_count`, `vc_op_124_write_1_schema`

### 31. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s155` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:156`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_124_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_156_read_file_1_row_count`, `vc_op_156_read_file_1_nulls`

### 32. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s155` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:155`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_155_inline_data_1_row_count`

### 33. Escribir learn.medical

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s155` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:155`
- **Conexiones:** Main desde `op_156_read_file_1`
- **Propiedades:**
  - `TABLE` = `medical` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:155
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:155
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:155
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_155_write_1_row_count`, `vc_op_155_write_1_schema`

### 34. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s176` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:177`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_155_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_177_read_file_1_row_count`, `vc_op_177_read_file_1_nulls`

### 35. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s176` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:176`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_176_inline_data_1_row_count`

### 36. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s176` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:176`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_177_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:176
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `UnitCost`, `Units`, `TotalSales` _(tipos por determinar)_
- **Expresión** (línea 182): SAS `(Units * UnitCost) / 1000` → Java `(((input_row.Units * input_row.UnitCost)) / 1000)`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_176_compute_1_nulls`, `vc_op_176_compute_1_dates`, `vc_op_176_compute_1_numeric`

### 37. Escribir learn.bicycles

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s176` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:176`
- **Conexiones:** Main desde `op_176_compute_1`
- **Propiedades:**
  - `TABLE` = `bicycles` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:176
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:176
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:176
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_176_write_1_row_count`, `vc_op_176_write_1_schema`

### 38. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s208` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:208`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_176_write_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:208
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Group` _(tipos por determinar)_
- **Expresión** (línea 210): SAS `ranuni(1357)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función ranuni
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_208_compute_1_nulls`, `vc_op_208_compute_1_dates`, `vc_op_208_compute_1_numeric`

### 39. Escribir temp

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s208` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:208`
- **Conexiones:** Main desde `op_208_compute_1`
- **Propiedades:**
  - `TABLE` = `temp` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:208
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:208
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:208
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_208_write_1_row_count`, `vc_op_208_write_1_schema`

### 40. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s214` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:214`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_208_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = _por configurar_ — regla mappings · nombre oficial
  - `INTABLE` (Inline Table) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_214_format_definition_1_schema`

### 41. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s217` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:217`
- **Conexiones:** OnSubjobOk desde `op_214_format_definition_1`
- **Supuestos:** PROC RANK sin traducción definida
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 42. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s224` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:225`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_217_unsupported_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_225_read_file_1_row_count`, `vc_op_225_read_file_1_nulls`

### 43. Escribir learn.survey

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s224` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:224`
- **Conexiones:** Main desde `op_225_read_file_1`
- **Propiedades:**
  - `TABLE` = `survey` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:224
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:224
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:224
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_224_write_1_row_count`, `vc_op_224_write_1_schema`

### 44. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s233` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:233`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_224_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:233 · nombre oficial
  - `INTABLE` (Inline Table) = `gender | F | Female
gender |   | Not entered
gender | other | Miscoded
age | 30-50 | 30 to 50
age | 51-high | 51+
likert | 2 | Disagree
likert | 3 | No opinion
likert | 4 | Agree
likert | 5 | Strongly agree` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:233 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_233_format_definition_1_schema`

### 45. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s249` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:250`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_233_format_definition_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_250_read_file_1_row_count`, `vc_op_250_read_file_1_nulls`

### 46. Escribir learn.survey

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s249` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:249`
- **Conexiones:** Main desde `op_250_read_file_1`
- **Propiedades:**
  - `TABLE` = `survey` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:249
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:249
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:249
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_249_write_1_row_count`, `vc_op_249_write_1_schema`

### 47. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s273` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:273`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_249_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:273 · nombre oficial
  - `INTABLE` (Inline Table) = `dx | 2 | Cold
dx | 3 | Heart Problems
dx | 4 | GI Problems
dx | 5 | Psychiatric
dx | 6 | Injury
dx | 7 | Infection` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:273 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_273_format_definition_1_schema`

### 48. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s282` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:283`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_273_format_definition_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_283_read_file_1_row_count`, `vc_op_283_read_file_1_nulls`

### 49. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s282` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:282`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_282_inline_data_1_row_count`

### 50. Escribir learn.clinic

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s282` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:282`
- **Conexiones:** Main desde `op_283_read_file_1`
- **Propiedades:**
  - `TABLE` = `clinic` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:282
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:282
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:282
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_282_write_1_row_count`, `vc_op_282_write_1_schema`

### 51. Leer learn.clinic

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s303` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:303`
- **Conexiones:** OnSubjobOk desde `op_282_write_1`
- **Propiedades:**
  - `TABLE` = `clinic` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:303
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset producido antes en este programa (op_282_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_303_read_1_row_count`, `vc_op_303_read_1_schema`

### 52. Ordenar por ID, VisitDate

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s303` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:303`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_303_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ID, VisitDate` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:303 · nombre oficial
- **Esquema:** `ID`, `VisitDate` _(tipos por determinar)_
- **Pruebas:** `vc_op_303_sort_1_ordering`

### 53. Escribir learn.clinic

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s303` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:303`
- **Conexiones:** Main desde `op_303_sort_1`
- **Propiedades:**
  - `TABLE` = `clinic` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:303
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:303
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:303
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_303_write_1_row_count`, `vc_op_303_write_1_schema`

### 54. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s308` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:308`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_303_write_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `4 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:308
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `AdmitDate`, `quarter`, `DOB`, `DischrDate` _(tipos por determinar)_
- **Expresión** (línea 310): SAS `int(ranuni(1234)*1200 + 15500)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función int
- **Expresión** (línea 311): SAS `intck('qtr','01jan2002'd,AdmitDate)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intck
- **Expresión** (línea 317): SAS `int(25000*Ranuni(0) + '01jan1920'd)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función int
- **Expresión** (línea 318): SAS `AdmitDate + abs(10*rannor(0) + 1)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función abs
- **Expresión** (línea 313): SAS `if ranuni(0) lt .1 and weekday(AdmitDate) eq 1 then
            AdmitDate = AdmitDate + 1` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 315): SAS `if ranuni(0) lt .1 and weekday(AdmitDate) eq 7 then
            AdmitDate = AdmitDate - int(3*ranuni(0) + 1)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_308_compute_1_nulls`, `vc_op_308_compute_1_dates`, `vc_op_308_compute_1_numeric`

### 55. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s308` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:308`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_308_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: i, j` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:308 · nombre oficial
- **Pruebas:** `vc_op_308_select_columns_1_schema`

### 56. Escribir learn.hosp

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s308` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:308`
- **Conexiones:** Main desde `op_308_select_columns_1`
- **Propiedades:**
  - `TABLE` = `hosp` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:308
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:308
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:308
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_308_write_1_row_count`, `vc_op_308_write_1_schema`

### 57. Leer Learn.hosp

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s328` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:328`
- **Conexiones:** OnSubjobOk desde `op_308_write_1`
- **Propiedades:**
  - `TABLE` = `hosp` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:328
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset producido antes en este programa (op_308_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_328_read_1_row_count`, `vc_op_328_read_1_schema`

### 58. Filtrar filas (opción where= del dataset): Discharge between '01Jan2003'd
                         and '31Dec2003'd

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s328` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:328`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_328_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 328): SAS `Discharge between '01Jan2003'd
                         and '31Dec2003'd` → _sin traducción automática_
  - ⚠ Sin traducción automática: texto sobrante
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_op_328_filter_1_row_count`, `vc_op_328_filter_1_nulls`, `vc_op_328_filter_1_empty`

### 59. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s328` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:328`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_328_filter_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Subject, DischrDate` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:328 · nombre oficial
- **Esquema:** `Subject`, `DischrDate` _(tipos por determinar)_
- **Pruebas:** `vc_op_328_select_columns_1_schema`

### 60. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s328` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:328`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_328_select_columns_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `Subject → Patient, DischrDate → Discharge` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:328
- **Esquema:** `Patient`, `Discharge` _(tipos por determinar)_
- **Pruebas:** `vc_op_328_rename_1_schema`

### 61. Escribir Learn.Hosp_Discharge

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s328` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:328`
- **Conexiones:** Main desde `op_328_rename_1`
- **Propiedades:**
  - `TABLE` = `hosp_discharge` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:328
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:328
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:328
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_328_write_1_row_count`, `vc_op_328_write_1_schema`

### 62. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s339` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:340`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_328_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_340_read_file_1_row_count`, `vc_op_340_read_file_1_nulls`

### 63. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s339` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:339`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_339_inline_data_1_row_count`

### 64. Escribir learn.health

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s339` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:339`
- **Conexiones:** Main desde `op_340_read_file_1`
- **Propiedades:**
  - `TABLE` = `health` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:339
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:339
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:339
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_339_write_1_row_count`, `vc_op_339_write_1_schema`

### 65. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s351` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:352`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_339_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_352_read_file_1_row_count`, `vc_op_352_read_file_1_nulls`

### 66. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s351` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:351`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_351_inline_data_1_row_count`

### 67. Escribir learn.demographic

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s351` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:351`
- **Conexiones:** Main desde `op_352_read_file_1`
- **Propiedades:**
  - `TABLE` = `demographic` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:351
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:351
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:351
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_351_write_1_row_count`, `vc_op_351_write_1_schema`

### 68. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s365` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:366`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_351_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_366_read_file_1_row_count`, `vc_op_366_read_file_1_nulls`

### 69. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s365` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:365`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_365_inline_data_1_row_count`

### 70. Escribir learn.new_members

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s365` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:365`
- **Conexiones:** Main desde `op_366_read_file_1`
- **Propiedades:**
  - `TABLE` = `new_members` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:365
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:365
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:365
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_365_write_1_row_count`, `vc_op_365_write_1_schema`

### 71. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s377` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:379`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_365_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_379_read_file_1_row_count`, `vc_op_379_read_file_1_nulls`

### 72. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s377` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:377`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_377_inline_data_1_row_count`

### 73. Escribir one

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s377` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:377`
- **Conexiones:** Main desde `op_379_read_file_1`
- **Propiedades:**
  - `TABLE` = `one` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:377
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:377
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:377
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_377_write_1_row_count`, `vc_op_377_write_1_schema`

### 74. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s386` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:388`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_377_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_388_read_file_1_row_count`, `vc_op_388_read_file_1_nulls`

### 75. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s386` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:386`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_386_inline_data_1_row_count`

### 76. Escribir two

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s386` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:386`
- **Conexiones:** Main desde `op_388_read_file_1`
- **Propiedades:**
  - `TABLE` = `two` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:386
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:386
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:386
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_386_write_1_row_count`, `vc_op_386_write_1_schema`

### 77. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s394` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:396`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_386_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_396_read_file_1_row_count`, `vc_op_396_read_file_1_nulls`

### 78. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s394` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:394`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_394_inline_data_1_row_count`

### 79. Escribir three

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s394` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:394`
- **Conexiones:** Main desde `op_396_read_file_1`
- **Propiedades:**
  - `TABLE` = `three` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:394
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:394
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:394
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_394_write_1_row_count`, `vc_op_394_write_1_schema`

### 80. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s404` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:406`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_394_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_406_read_file_1_row_count`, `vc_op_406_read_file_1_nulls`

### 81. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s404` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:404`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_404_inline_data_1_row_count`

### 82. Escribir Employee

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s404` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:404`
- **Conexiones:** Main desde `op_406_read_file_1`
- **Propiedades:**
  - `TABLE` = `employee` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:404
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:404
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:404
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_404_write_1_row_count`, `vc_op_404_write_1_schema`

### 83. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s415` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:417`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_404_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_417_read_file_1_row_count`, `vc_op_417_read_file_1_nulls`

### 84. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s415` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:415`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_415_inline_data_1_row_count`

### 85. Escribir Hours

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s415` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:415`
- **Conexiones:** Main desde `op_417_read_file_1`
- **Propiedades:**
  - `TABLE` = `hours` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:415
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:415
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:415
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_415_write_1_row_count`, `vc_op_415_write_1_schema`

### 86. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s428` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:429`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_415_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_429_read_file_1_row_count`, `vc_op_429_read_file_1_nulls`

### 87. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s428` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:428`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_428_inline_data_1_row_count`

### 88. Escribir Bert

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s428` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:428`
- **Conexiones:** Main desde `op_429_read_file_1`
- **Propiedades:**
  - `TABLE` = `bert` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:428
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:428
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:428
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_428_write_1_row_count`, `vc_op_428_write_1_schema`

### 89. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s435` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:436`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_428_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_436_read_file_1_row_count`, `vc_op_436_read_file_1_nulls`

### 90. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s435` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:435`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_435_inline_data_1_row_count`

### 91. Escribir Ernie

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s435` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:435`
- **Conexiones:** Main desde `op_436_read_file_1`
- **Propiedades:**
  - `TABLE` = `ernie` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:435
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:435
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:435
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_435_write_1_row_count`, `vc_op_435_write_1_schema`

### 92. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s444` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:445`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_435_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_445_read_file_1_row_count`, `vc_op_445_read_file_1_nulls`

### 93. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s444` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:444`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_444_inline_data_1_row_count`

### 94. Escribir Division1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s444` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:444`
- **Conexiones:** Main desde `op_445_read_file_1`
- **Propiedades:**
  - `TABLE` = `division1` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:444
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:444
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:444
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_444_write_1_row_count`, `vc_op_444_write_1_schema`

### 95. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s455` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:456`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_444_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_456_read_file_1_row_count`, `vc_op_456_read_file_1_nulls`

### 96. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s455` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:455`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_455_inline_data_1_row_count`

### 97. Escribir Division2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s455` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:455`
- **Conexiones:** Main desde `op_456_read_file_1`
- **Propiedades:**
  - `TABLE` = `division2` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:455
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:455
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:455
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_455_write_1_row_count`, `vc_op_455_write_1_schema`

### 98. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s466` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:467`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_455_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_467_read_file_1_row_count`, `vc_op_467_read_file_1_nulls`

### 99. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s466` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:466`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_466_inline_data_1_row_count`

### 100. Escribir Oscar

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s466` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:466`
- **Conexiones:** Main desde `op_467_read_file_1`
- **Propiedades:**
  - `TABLE` = `oscar` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:466
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:466
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:466
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_466_write_1_row_count`, `vc_op_466_write_1_schema`

### 101. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s479` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:481`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_466_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_481_read_file_1_row_count`, `vc_op_481_read_file_1_nulls`

### 102. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s479` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:479`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_479_inline_data_1_row_count`

### 103. Escribir Prices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s479` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:479`
- **Conexiones:** Main desde `op_481_read_file_1`
- **Propiedades:**
  - `TABLE` = `prices` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:479
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:479
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:479
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_479_write_1_row_count`, `vc_op_479_write_1_schema`

### 104. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s490` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:492`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_479_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_492_read_file_1_row_count`, `vc_op_492_read_file_1_nulls`

### 105. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s490` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:490`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_490_inline_data_1_row_count`

### 106. Escribir New15Dec2017

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s490` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:490`
- **Conexiones:** Main desde `op_492_read_file_1`
- **Propiedades:**
  - `TABLE` = `new15dec2017` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:490
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:490
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:490
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_490_write_1_row_count`, `vc_op_490_write_1_schema`

### 107. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s500` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:501`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_490_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_501_read_file_1_row_count`, `vc_op_501_read_file_1_nulls`

### 108. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s500` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:500`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_500_inline_data_1_row_count`

### 109. Escribir learn.insurance

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s500` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:500`
- **Conexiones:** Main desde `op_501_read_file_1`
- **Propiedades:**
  - `TABLE` = `insurance` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:500
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:500
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:500
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_500_write_1_row_count`, `vc_op_500_write_1_schema`

### 110. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s511` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:512`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_500_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_512_read_file_1_row_count`, `vc_op_512_read_file_1_nulls`

### 111. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s511` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:511`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_511_inline_data_1_row_count`

### 112. Escribir learn.new_members_order

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s511` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:511`
- **Conexiones:** Main desde `op_512_read_file_1`
- **Propiedades:**
  - `TABLE` = `new_members_order` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:511
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:511
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:511
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_511_write_1_row_count`, `vc_op_511_write_1_schema`

### 113. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s523` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:524`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_511_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_524_read_file_1_row_count`, `vc_op_524_read_file_1_nulls`

### 114. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s523` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:523`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_523_inline_data_1_row_count`

### 115. Escribir learn.inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s523` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:523`
- **Conexiones:** Main desde `op_524_read_file_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:523
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:523
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:523
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_523_write_1_row_count`, `vc_op_523_write_1_schema`

### 116. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s536` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:537`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_523_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_537_read_file_1_row_count`, `vc_op_537_read_file_1_nulls`

### 117. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s536` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:536`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_536_inline_data_1_row_count`

### 118. Escribir learn.purchase

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s536` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:536`
- **Conexiones:** Main desde `op_537_read_file_1`
- **Propiedades:**
  - `TABLE` = `purchase` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:536
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:536
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:536
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_536_write_1_row_count`, `vc_op_536_write_1_schema`

### 119. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s546` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:547`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_536_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_547_read_file_1_row_count`, `vc_op_547_read_file_1_nulls`

### 120. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s546` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:546`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_546_inline_data_1_row_count`

### 121. Escribir learn.newproducts

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s546` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:546`
- **Conexiones:** Main desde `op_547_read_file_1`
- **Propiedades:**
  - `TABLE` = `newproducts` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:546
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:546
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:546
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_546_write_1_row_count`, `vc_op_546_write_1_schema`

### 122. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s555` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:556`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_546_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_556_read_file_1_row_count`, `vc_op_556_read_file_1_nulls`

### 123. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s555` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:555`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_555_inline_data_1_row_count`

### 124. Escribir learn.demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s555` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:555`
- **Conexiones:** Main desde `op_556_read_file_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:555
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:555
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:555
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_555_write_1_row_count`, `vc_op_555_write_1_schema`

### 125. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s568` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:569`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_555_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_569_read_file_1_row_count`, `vc_op_569_read_file_1_nulls`

### 126. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s568` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:568`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_568_inline_data_1_row_count`

### 127. Escribir learn.survey1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s568` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:568`
- **Conexiones:** Main desde `op_569_read_file_1`
- **Propiedades:**
  - `TABLE` = `survey1` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:568
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:568
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:568
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_568_write_1_row_count`, `vc_op_568_write_1_schema`

### 128. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s580` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:581`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_568_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_581_read_file_1_row_count`, `vc_op_581_read_file_1_nulls`

### 129. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s580` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:580`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_580_inline_data_1_row_count`

### 130. Escribir learn.survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s580` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:580`
- **Conexiones:** Main desde `op_581_read_file_1`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:580
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:580
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:580
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_580_write_1_row_count`, `vc_op_580_write_1_schema`

### 131. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s592` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:594`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_580_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_594_read_file_1_row_count`, `vc_op_594_read_file_1_nulls`

### 132. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s592` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:592`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_592_inline_data_1_row_count`

### 133. Escribir learn.test_scores

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s592` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:592`
- **Conexiones:** Main desde `op_594_read_file_1`
- **Propiedades:**
  - `TABLE` = `test_scores` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:592
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:592
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:592
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_592_write_1_row_count`, `vc_op_592_write_1_schema`

### 134. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s606` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:607`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_592_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_607_read_file_1_row_count`, `vc_op_607_read_file_1_nulls`

### 135. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s606` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:606`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_606_inline_data_1_row_count`

### 136. Escribir learn.upper

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s606` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:606`
- **Conexiones:** Main desde `op_607_read_file_1`
- **Propiedades:**
  - `TABLE` = `upper` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:606
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:606
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:606
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_606_write_1_row_count`, `vc_op_606_write_1_schema`

### 137. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s616` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:617`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_606_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_617_read_file_1_row_count`, `vc_op_617_read_file_1_nulls`

### 138. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s616` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:616`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_616_inline_data_1_row_count`

### 139. Escribir learn.psych

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s616` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:616`
- **Conexiones:** Main desde `op_617_read_file_1`
- **Propiedades:**
  - `TABLE` = `psych` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:616
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:616
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:616
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_616_write_1_row_count`, `vc_op_616_write_1_schema`

### 140. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s627` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:628`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_616_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_628_read_file_1_row_count`, `vc_op_628_read_file_1_nulls`

### 141. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s627` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:627`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_627_inline_data_1_row_count`

### 142. Escribir learn.char_num

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s627` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:627`
- **Conexiones:** Main desde `op_628_read_file_1`
- **Propiedades:**
  - `TABLE` = `char_num` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:627
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:627
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:627
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_627_write_1_row_count`, `vc_op_627_write_1_schema`

### 143. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s636` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:638`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_627_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_638_read_file_1_row_count`, `vc_op_638_read_file_1_nulls`

### 144. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s636` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:636`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_636_inline_data_1_row_count`

### 145. Escribir learn.stocks

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s636` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:636`
- **Conexiones:** Main desde `op_638_read_file_1`
- **Propiedades:**
  - `TABLE` = `stocks` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:636
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:636
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:636
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_636_write_1_row_count`, `vc_op_636_write_1_schema`

### 146. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s649` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:650`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_636_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_650_read_file_1_row_count`, `vc_op_650_read_file_1_nulls`

### 147. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s649` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:649`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_649_inline_data_1_row_count`

### 148. Escribir learn.names_and_more

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s649` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:649`
- **Conexiones:** Main desde `op_650_read_file_1`
- **Propiedades:**
  - `TABLE` = `names_and_more` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:649
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:649
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:649
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_649_write_1_row_count`, `vc_op_649_write_1_schema`

### 149. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s663` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:664`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_649_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_664_read_file_1_row_count`, `vc_op_664_read_file_1_nulls`

### 150. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s663` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:663`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_663_inline_data_1_row_count`

### 151. Escribir learn.phone

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s663` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:663`
- **Conexiones:** Main desde `op_664_read_file_1`
- **Propiedades:**
  - `TABLE` = `phone` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:663
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:663
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:663
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_663_write_1_row_count`, `vc_op_663_write_1_schema`

### 152. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s673` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:674`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_663_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_674_read_file_1_row_count`, `vc_op_674_read_file_1_nulls`

### 153. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s673` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:673`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_673_inline_data_1_row_count`

### 154. Escribir learn.study

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s673` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:673`
- **Conexiones:** Main desde `op_674_read_file_1`
- **Propiedades:**
  - `TABLE` = `study` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:673
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:673
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:673
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_673_write_1_row_count`, `vc_op_673_write_1_schema`

### 155. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s688` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:689`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_673_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_689_read_file_1_row_count`, `vc_op_689_read_file_1_nulls`

### 156. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s688` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:688`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_688_inline_data_1_row_count`

### 157. Escribir learn.errors

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s688` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:688`
- **Conexiones:** Main desde `op_689_read_file_1`
- **Propiedades:**
  - `TABLE` = `errors` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:688
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:688
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:688
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_688_write_1_row_count`, `vc_op_688_write_1_schema`

### 158. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s701` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:702`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_688_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_702_read_file_1_row_count`, `vc_op_702_read_file_1_nulls`

### 159. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s701` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:701`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_701_inline_data_1_row_count`

### 160. Escribir learn.expose

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s701` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:701`
- **Conexiones:** Main desde `op_702_read_file_1`
- **Propiedades:**
  - `TABLE` = `expose` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:701
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:701
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:701
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_701_write_1_row_count`, `vc_op_701_write_1_schema`

### 161. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s712` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:713`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_701_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_713_read_file_1_row_count`, `vc_op_713_read_file_1_nulls`

### 162. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s712` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:712`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_712_inline_data_1_row_count`

### 163. Escribir learn.mixed

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s712` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:712`
- **Conexiones:** Main desde `op_713_read_file_1`
- **Propiedades:**
  - `TABLE` = `mixed` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:712
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:712
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:712
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_712_write_1_row_count`, `vc_op_712_write_1_schema`

### 164. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s721` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:722`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_712_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_722_read_file_1_row_count`, `vc_op_722_read_file_1_nulls`

### 165. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s721` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:721`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_721_inline_data_1_row_count`

### 166. Escribir learn.mixed_UNITS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s721` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:721`
- **Conexiones:** Main desde `op_722_read_file_1`
- **Propiedades:**
  - `TABLE` = `mixed_units` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:721
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:721
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:721
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_721_write_1_row_count`, `vc_op_721_write_1_schema`

### 167. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s731` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:732`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_721_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_732_read_file_1_row_count`, `vc_op_732_read_file_1_nulls`

### 168. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s731` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:731`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_731_inline_data_1_row_count`

### 169. Escribir social1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s731` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:731`
- **Conexiones:** Main desde `op_732_read_file_1`
- **Propiedades:**
  - `TABLE` = `social1` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:731
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:731
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:731
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_731_write_1_row_count`, `vc_op_731_write_1_schema`

### 170. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s741` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:742`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_731_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_742_read_file_1_row_count`, `vc_op_742_read_file_1_nulls`

### 171. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s741` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:741`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_741_inline_data_1_row_count`

### 172. Escribir social2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s741` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:741`
- **Conexiones:** Main desde `op_742_read_file_1`
- **Propiedades:**
  - `TABLE` = `social2` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:741
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:741
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:741
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_741_write_1_row_count`, `vc_op_741_write_1_schema`

### 173. Leer social1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s751` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:752`
- **Conexiones:** OnSubjobOk desde `op_741_write_1`
- **Propiedades:**
  - `TABLE` = `social1` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:752
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_731_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_752_read_1_row_count`, `vc_op_752_read_1_schema`

### 174. Leer social2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s751` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:752`
- **Propiedades:**
  - `TABLE` = `social2` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:752
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_741_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_752_read_2_row_count`, `vc_op_752_read_2_schema`

### 175. Unir (implicit): work.social1, work.social2

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s751` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:752`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_752_read_1`, Lookup desde `op_752_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Supuestos:** Join por coma: la condición está en el WHERE
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Condición de join no reducible a igualdad de columnas: revisar manualmente
- **Pruebas:** `vc_op_752_join_1_duplicates`, `vc_op_752_join_1_row_count`, `vc_op_752_join_1_nulls`

### 176. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s751` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:752`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_752_join_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:752
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_op_752_project_1_schema`

### 177. Escribir learn.social (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s751` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:752`
- **Conexiones:** Main desde `op_752_project_1`
- **Propiedades:**
  - `TABLE` = `social` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:752
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:752
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:752
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_752_write_1_row_count`, `vc_op_752_write_1_schema`

### 178. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s758` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:759`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_752_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_759_read_file_1_row_count`, `vc_op_759_read_file_1_nulls`

### 179. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s758` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:758`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_758_inline_data_1_row_count`

### 180. Escribir learn.SPSS

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s758` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:758`
- **Conexiones:** Main desde `op_759_read_file_1`
- **Propiedades:**
  - `TABLE` = `spss` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:758
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:758
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:758
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_758_write_1_row_count`, `vc_op_758_write_1_schema`

### 181. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s768` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:769`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_758_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_769_read_file_1_row_count`, `vc_op_769_read_file_1_nulls`

### 182. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s768` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:768`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_768_inline_data_1_row_count`

### 183. Escribir learn.personal

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s768` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:768`
- **Conexiones:** Main desde `op_769_read_file_1`
- **Propiedades:**
  - `TABLE` = `personal` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:768
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:768
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:768
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_768_write_1_row_count`, `vc_op_768_write_1_schema`

### 184. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s794` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:795`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_768_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_795_read_file_1_row_count`, `vc_op_795_read_file_1_nulls`

### 185. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s794` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:794`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_794_inline_data_1_row_count`

### 186. Escribir learn.nines

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s794` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:794`
- **Conexiones:** Main desde `op_795_read_file_1`
- **Propiedades:**
  - `TABLE` = `nines` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:794
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:794
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:794
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_794_write_1_row_count`, `vc_op_794_write_1_schema`

### 187. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s804` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:805`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_794_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_805_read_file_1_row_count`, `vc_op_805_read_file_1_nulls`

### 188. Escribir learn.blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s804` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:804`
- **Conexiones:** Main desde `op_805_read_file_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:804
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:804
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:804
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_804_write_1_row_count`, `vc_op_804_write_1_schema`

### 189. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s821` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:822`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_804_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_822_read_file_1_row_count`, `vc_op_822_read_file_1_nulls`

### 190. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s821` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:821`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_821_inline_data_1_row_count`

### 191. Escribir learn.bloodpressure

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s821` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:821`
- **Conexiones:** Main desde `op_822_read_file_1`
- **Propiedades:**
  - `TABLE` = `bloodpressure` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:821
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:821
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:821
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_821_write_1_row_count`, `vc_op_821_write_1_schema`

### 192. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s838` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:839`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_821_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_839_read_file_1_row_count`, `vc_op_839_read_file_1_nulls`

### 193. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s838` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:838`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_838_inline_data_1_row_count`

### 194. Escribir learn.numeric

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s838` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:838`
- **Conexiones:** Main desde `op_839_read_file_1`
- **Propiedades:**
  - `TABLE` = `numeric` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:838
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:838
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:838
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_838_write_1_row_count`, `vc_op_838_write_1_schema`

### 195. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s848` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:849`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_838_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_849_read_file_1_row_count`, `vc_op_849_read_file_1_nulls`

### 196. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s848` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:848`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_848_inline_data_1_row_count`

### 197. Escribir learn.codes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s848` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:848`
- **Conexiones:** Main desde `op_849_read_file_1`
- **Propiedades:**
  - `TABLE` = `codes` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:848
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:848
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:848
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_848_write_1_row_count`, `vc_op_848_write_1_schema`

### 198. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s860` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:860`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_848_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:860 · nombre oficial
  - `INTABLE` (Inline Table) = `yesno | N','0 | No
yesno |   | Not Given
size | M | Medium
size | L | Large
size |   | Missing
gender | M | Male
gender |   | Not Given` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:860 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_860_format_definition_1_schema`

### 199. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s873` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:873`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_860_format_definition_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 11 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:873
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `StudentID`, `GPA`, `ClassRank` _(tipos por determinar)_
- **Expresión** (línea 876): SAS `put(round(ranuni(123456)*10000),z5.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 884): SAS `round(rannor(0)*.5 + 3.5,.01)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.5 + 3.5,.01'
- **Expresión** (línea 886): SAS `int(ranuni(0)*60 + 41)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función int
- **Expresión** (línea 877): SAS `if ranuni(0) lt .4 then Gender = 'M'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 878): SAS `else Gender = 'F'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 879): SAS `if ranuni(0) lt .3 then SchoolSize = 'S'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 880): SAS `else if ranuni(0) lt .7 then SchoolSize = 'M'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 881): SAS `else SchoolSize = 'L'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 882): SAS `if ranuni(0) lt .2 then Scholarship = 'Y'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 883): SAS `else Scholarship = 'N'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 885): SAS `if GPA gt 4 then GPA = 4` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 887): SAS `if ranuni(0) lt .1 then call missing(ClassRank)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 888): SAS `if ranuni(0) lt .05 then call missing(SchoolSize)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 889): SAS `if ranuni(0) lt .05 then call missing(GPA)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_873_compute_1_nulls`, `vc_op_873_compute_1_dates`, `vc_op_873_compute_1_numeric`

### 200. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s873` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:873`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_873_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: i` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:873 · nombre oficial
- **Pruebas:** `vc_op_873_select_columns_1_schema`

### 201. Escribir learn.college

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s873` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:873`
- **Conexiones:** Main desde `op_873_select_columns_1`
- **Propiedades:**
  - `TABLE` = `college` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:873
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:873
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:873
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_873_write_1_row_count`, `vc_op_873_write_1_schema`

### 202. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s899` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:899`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_873_write_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:899
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `TimeMile`, `RestPulse`, `MaxPulse` _(tipos por determinar)_
- **Expresión** (línea 902): SAS `round(rand('normal',8,2),.1)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.1)'
- **Expresión** (línea 904): SAS `40 + int(2*TimeMile) + rand('normal',5,5)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función int
- **Expresión** (línea 905): SAS `int(RestPulse + rand('normal',100,5))` → _sin traducción automática_
  - ⚠ Sin traducción automática: función int
- **Expresión** (línea 903): SAS `if TimeMile lt 4.5 then TimeMile = TimeMile + 4` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_899_compute_1_nulls`, `vc_op_899_compute_1_dates`, `vc_op_899_compute_1_numeric`

### 203. Escribir learn.fitness

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s899` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:899`
- **Conexiones:** Main desde `op_899_compute_1`
- **Propiedades:**
  - `TABLE` = `fitness` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:899
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:899
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:899
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_899_write_1_row_count`, `vc_op_899_write_1_schema`

### 204. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s911` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:912`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_899_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_912_read_file_1_row_count`, `vc_op_912_read_file_1_nulls`

### 205. Escribir learn.grades

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s911` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:911`
- **Conexiones:** Main desde `op_912_read_file_1`
- **Propiedades:**
  - `TABLE` = `grades` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:911
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:911
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:911
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_911_write_1_row_count`, `vc_op_911_write_1_schema`

### 206. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s917` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:918`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_911_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_918_read_file_1_row_count`, `vc_op_918_read_file_1_nulls`

### 207. Escribir learn.gym

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s917` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:917`
- **Conexiones:** Main desde `op_918_read_file_1`
- **Propiedades:**
  - `TABLE` = `gym` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:917
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:917
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:917
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_917_write_1_row_count`, `vc_op_917_write_1_schema`

### 208. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s926` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:927`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_917_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_927_read_file_1_row_count`, `vc_op_927_read_file_1_nulls`

### 209. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s926` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:926`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_926_inline_data_1_row_count`

### 210. Escribir learn.dxcodes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s926` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:926`
- **Conexiones:** Main desde `op_927_read_file_1`
- **Propiedades:**
  - `TABLE` = `dxcodes` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:926
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:926
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:926
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_926_write_1_row_count`, `vc_op_926_write_1_schema`

### 211. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s942` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:943`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_926_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_943_read_file_1_row_count`, `vc_op_943_read_file_1_nulls`

### 212. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s942` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:942`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_942_inline_data_1_row_count`

### 213. Escribir learn.wide

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s942` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:942`
- **Conexiones:** Main desde `op_943_read_file_1`
- **Propiedades:**
  - `TABLE` = `wide` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:942
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:942
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:942
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_942_write_1_row_count`, `vc_op_942_write_1_schema`

### 214. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s951` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:952`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_942_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_952_read_file_1_row_count`, `vc_op_952_read_file_1_nulls`

### 215. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s951` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:951`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_951_inline_data_1_row_count`

### 216. Escribir learn.EndOfYear

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s951` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:951`
- **Conexiones:** Main desde `op_952_read_file_1`
- **Propiedades:**
  - `TABLE` = `endofyear` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:951
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:951
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:951
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_951_write_1_row_count`, `vc_op_951_write_1_schema`

### 217. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s964` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:965`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_951_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_965_read_file_1_row_count`, `vc_op_965_read_file_1_nulls`

### 218. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s964` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:964`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_964_inline_data_1_row_count`

### 219. Escribir learn.narrow

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s964` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:964`
- **Conexiones:** Main desde `op_965_read_file_1`
- **Propiedades:**
  - `TABLE` = `narrow` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:964
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:964
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:964
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_964_write_1_row_count`, `vc_op_964_write_1_schema`

### 220. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s977` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:978`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_964_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_978_read_file_1_row_count`, `vc_op_978_read_file_1_nulls`

### 221. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s977` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:977`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_977_inline_data_1_row_count`

### 222. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s977` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:977`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_978_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:977
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 983): SAS `if not missing(Price) then output` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_977_compute_1_nulls`, `vc_op_977_compute_1_dates`, `vc_op_977_compute_1_numeric`

### 223. Escribir learn.dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s977` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:977`
- **Conexiones:** Main desde `op_977_compute_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:977
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:977
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:977
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_977_write_1_row_count`, `vc_op_977_write_1_schema`

### 224. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s995` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:996`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_977_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_996_read_file_1_row_count`, `vc_op_996_read_file_1_nulls`

### 225. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s995` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:995`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_995_inline_data_1_row_count`

### 226. Escribir learn.left

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s995` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:995`
- **Conexiones:** Main desde `op_996_read_file_1`
- **Propiedades:**
  - `TABLE` = `left` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:995
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:995
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:995
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_995_write_1_row_count`, `vc_op_995_write_1_schema`

### 227. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1007` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1008`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_995_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1008_read_file_1_row_count`, `vc_op_1008_read_file_1_nulls`

### 228. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1007` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1007`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1007_inline_data_1_row_count`

### 229. Escribir learn.right

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1007` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1007`
- **Conexiones:** Main desde `op_1008_read_file_1`
- **Propiedades:**
  - `TABLE` = `right` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1007
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1007
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1007
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1007_write_1_row_count`, `vc_op_1007_write_1_schema`

### 230. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1020` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1021`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1007_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1021_read_file_1_row_count`, `vc_op_1021_read_file_1_nulls`

### 231. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1020` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1020`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1020_inline_data_1_row_count`

### 232. Escribir learn.missing

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1020` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1020`
- **Conexiones:** Main desde `op_1021_read_file_1`
- **Propiedades:**
  - `TABLE` = `missing` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1020
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1020
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1020
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1020_write_1_row_count`, `vc_op_1020_write_1_schema`

### 233. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1032` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1033`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1020_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1033_read_file_1_row_count`, `vc_op_1033_read_file_1_nulls`

### 234. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1032` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1032`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1032_inline_data_1_row_count`

### 235. Escribir learn.first

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1032` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1032`
- **Conexiones:** Main desde `op_1033_read_file_1`
- **Propiedades:**
  - `TABLE` = `first` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1032
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1032
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1032
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1032_write_1_row_count`, `vc_op_1032_write_1_schema`

### 236. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1041` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1042`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1032_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1042_read_file_1_row_count`, `vc_op_1042_read_file_1_nulls`

### 237. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1041` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1041`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1041_inline_data_1_row_count`

### 238. Escribir learn.second

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1041` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1041`
- **Conexiones:** Main desde `op_1042_read_file_1`
- **Propiedades:**
  - `TABLE` = `second` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1041
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1041
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1041
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1041_write_1_row_count`, `vc_op_1041_write_1_schema`

### 239. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1051` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1051`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1041_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1051 · nombre oficial
  - `INTABLE` (Inline Table) = `two | low-3 | Group 1
two | 4-5 | Group 2
two | . | Missing
two | other | Other values` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1051 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1051_format_definition_1_schema`

### 240. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1060` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1061`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1051_format_definition_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1061_read_file_1_row_count`, `vc_op_1061_read_file_1_nulls`

### 241. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1060` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1060`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1060_inline_data_1_row_count`

### 242. Escribir learn.grouping

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1060` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1060`
- **Conexiones:** Main desde `op_1061_read_file_1`
- **Propiedades:**
  - `TABLE` = `grouping` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1060
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1060
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1060
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1060_write_1_row_count`, `vc_op_1060_write_1_schema`

### 243. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1066` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1067`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1060_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1067_read_file_1_row_count`, `vc_op_1067_read_file_1_nulls`

### 244. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1066` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1066`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1066_inline_data_1_row_count`

### 245. Escribir Many_One

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1066` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1066`
- **Conexiones:** Main desde `op_1067_read_file_1`
- **Propiedades:**
  - `TABLE` = `many_one` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1066
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1066
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1066
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1066_write_1_row_count`, `vc_op_1066_write_1_schema`

### 246. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1076` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1077`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1066_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1077_read_file_1_row_count`, `vc_op_1077_read_file_1_nulls`

### 247. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1076` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1076`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1076_inline_data_1_row_count`

### 248. Escribir Many_Two

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1076` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1076`
- **Conexiones:** Main desde `op_1077_read_file_1`
- **Propiedades:**
  - `TABLE` = `many_two` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1076
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1076
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1076
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1076_write_1_row_count`, `vc_op_1076_write_1_schema`

### 249. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1087` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1088`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1076_write_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1088_read_file_1_row_count`, `vc_op_1088_read_file_1_nulls`

### 250. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1087` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1087`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1087_inline_data_1_row_count`

### 251. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1087` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1087`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1088_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `4 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1087
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Age`, `WtKg`, `Weight`, `Next_Dollar` _(tipos por determinar)_
- **Expresión** (línea 1089): SAS `int(Age)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función int
- **Expresión** (línea 1090): SAS `round(Weight/2.2, .1)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: ' .1)'
- **Expresión** (línea 1091): SAS `round(Weight)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función round
- **Expresión** (línea 1092): SAS `Ceil(Cost)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función Ceil
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1087_compute_1_nulls`, `vc_op_1087_compute_1_dates`, `vc_op_1087_compute_1_numeric`

### 252. Escribir Truncate

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1087` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Create_Datasets.sas:1087`
- **Conexiones:** Main desde `op_1087_compute_1`
- **Propiedades:**
  - `TABLE` = `truncate` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1087
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1087
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Create_Datasets.sas:1087
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1087_write_1_row_count`, `vc_op_1087_write_1_schema`

## Casos de validación

- `vc_op_28_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_28_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_27_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_27_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_27_write_1_schema` (schema): Esquema destino
- `vc_op_45_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_45_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_44_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_44_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_44_write_1_schema` (schema): Esquema destino
- `vc_op_65_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_65_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_64_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_64_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_64_write_1_schema` (schema): Esquema destino
- `vc_op_75_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_75_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_73_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_73_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_73_write_1_schema` (schema): Esquema destino
- `vc_op_84_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_84_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_83_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_83_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_83_write_1_schema` (schema): Esquema destino
- `vc_op_93_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_93_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_93_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_93_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_93_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_93_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_93_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_93_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_93_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_93_write_1_schema` (schema): Esquema destino
- `vc_op_106_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_106_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_105_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_105_write_1_schema` (schema): Esquema destino
- `vc_op_116_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_116_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_115_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_115_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_115_write_1_schema` (schema): Esquema destino
- `vc_op_125_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_125_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_124_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_124_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_124_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_124_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_124_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_124_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_124_write_1_schema` (schema): Esquema destino
- `vc_op_156_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_156_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_155_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_155_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_155_write_1_schema` (schema): Esquema destino
- `vc_op_177_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_177_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_176_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_176_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_176_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_176_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_176_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_176_write_1_schema` (schema): Esquema destino
- `vc_op_208_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_208_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_208_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_208_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_208_write_1_schema` (schema): Esquema destino
- `vc_op_214_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_225_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_225_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_224_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_224_write_1_schema` (schema): Esquema destino
- `vc_op_233_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_250_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_250_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_249_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_249_write_1_schema` (schema): Esquema destino
- `vc_op_273_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_283_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_283_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_282_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_282_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_282_write_1_schema` (schema): Esquema destino
- `vc_op_303_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_303_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_303_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_303_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_303_write_1_schema` (schema): Esquema destino
- `vc_op_308_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_308_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_308_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_308_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_308_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_308_write_1_schema` (schema): Esquema destino
- `vc_op_328_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_328_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_328_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_328_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_328_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_328_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_328_rename_1_schema` (schema): Nombres de columna finales
- `vc_op_328_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_328_write_1_schema` (schema): Esquema destino
- `vc_op_340_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_340_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_339_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_339_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_339_write_1_schema` (schema): Esquema destino
- `vc_op_352_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_352_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_351_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_351_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_351_write_1_schema` (schema): Esquema destino
- `vc_op_366_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_366_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_365_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_365_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_365_write_1_schema` (schema): Esquema destino
- `vc_op_379_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_379_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_377_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_377_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_377_write_1_schema` (schema): Esquema destino
- `vc_op_388_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_388_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_386_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_386_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_386_write_1_schema` (schema): Esquema destino
- `vc_op_396_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_396_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_394_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_394_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_394_write_1_schema` (schema): Esquema destino
- `vc_op_406_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_406_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_404_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_404_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_404_write_1_schema` (schema): Esquema destino
- `vc_op_417_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_417_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_415_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_415_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_415_write_1_schema` (schema): Esquema destino
- `vc_op_429_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_429_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_428_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_428_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_428_write_1_schema` (schema): Esquema destino
- `vc_op_436_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_436_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_435_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_435_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_435_write_1_schema` (schema): Esquema destino
- `vc_op_445_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_445_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_444_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_444_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_444_write_1_schema` (schema): Esquema destino
- `vc_op_456_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_456_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_455_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_455_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_455_write_1_schema` (schema): Esquema destino
- `vc_op_467_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_467_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_466_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_466_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_466_write_1_schema` (schema): Esquema destino
- `vc_op_481_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_481_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_479_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_479_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_479_write_1_schema` (schema): Esquema destino
- `vc_op_492_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_492_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_490_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_490_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_490_write_1_schema` (schema): Esquema destino
- `vc_op_501_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_501_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_500_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_500_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_500_write_1_schema` (schema): Esquema destino
- `vc_op_512_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_512_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_511_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_511_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_511_write_1_schema` (schema): Esquema destino
- `vc_op_524_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_524_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_523_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_523_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_523_write_1_schema` (schema): Esquema destino
- `vc_op_537_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_537_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_536_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_536_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_536_write_1_schema` (schema): Esquema destino
- `vc_op_547_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_547_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_546_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_546_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_546_write_1_schema` (schema): Esquema destino
- `vc_op_556_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_556_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_555_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_555_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_555_write_1_schema` (schema): Esquema destino
- `vc_op_569_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_569_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_568_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_568_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_568_write_1_schema` (schema): Esquema destino
- `vc_op_581_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_581_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_580_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_580_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_580_write_1_schema` (schema): Esquema destino
- `vc_op_594_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_594_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_592_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_592_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_592_write_1_schema` (schema): Esquema destino
- `vc_op_607_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_607_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_606_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_606_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_606_write_1_schema` (schema): Esquema destino
- `vc_op_617_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_617_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_616_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_616_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_616_write_1_schema` (schema): Esquema destino
- `vc_op_628_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_628_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_627_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_627_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_627_write_1_schema` (schema): Esquema destino
- `vc_op_638_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_638_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_636_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_636_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_636_write_1_schema` (schema): Esquema destino
- `vc_op_650_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_650_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_649_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_649_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_649_write_1_schema` (schema): Esquema destino
- `vc_op_664_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_664_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_663_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_663_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_663_write_1_schema` (schema): Esquema destino
- `vc_op_674_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_674_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_673_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_673_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_673_write_1_schema` (schema): Esquema destino
- `vc_op_689_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_689_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_688_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_688_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_688_write_1_schema` (schema): Esquema destino
- `vc_op_702_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_702_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_701_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_701_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_701_write_1_schema` (schema): Esquema destino
- `vc_op_713_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_713_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_712_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_712_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_712_write_1_schema` (schema): Esquema destino
- `vc_op_722_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_722_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_721_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_721_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_721_write_1_schema` (schema): Esquema destino
- `vc_op_732_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_732_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_731_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_731_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_731_write_1_schema` (schema): Esquema destino
- `vc_op_742_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_742_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_741_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_741_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_741_write_1_schema` (schema): Esquema destino
- `vc_op_752_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_752_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_752_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_752_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_752_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_752_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_752_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_752_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_752_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_752_write_1_schema` (schema): Esquema destino
- `vc_op_759_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_759_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_758_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_758_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_758_write_1_schema` (schema): Esquema destino
- `vc_op_769_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_769_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_768_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_768_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_768_write_1_schema` (schema): Esquema destino
- `vc_op_795_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_795_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_794_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_794_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_794_write_1_schema` (schema): Esquema destino
- `vc_op_805_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_805_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_804_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_804_write_1_schema` (schema): Esquema destino
- `vc_op_822_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_822_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_821_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_821_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_821_write_1_schema` (schema): Esquema destino
- `vc_op_839_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_839_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_838_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_838_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_838_write_1_schema` (schema): Esquema destino
- `vc_op_849_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_849_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_848_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_848_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_848_write_1_schema` (schema): Esquema destino
- `vc_op_860_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_873_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_873_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_873_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_873_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_873_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_873_write_1_schema` (schema): Esquema destino
- `vc_op_899_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_899_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_899_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_899_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_899_write_1_schema` (schema): Esquema destino
- `vc_op_912_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_912_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_911_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_911_write_1_schema` (schema): Esquema destino
- `vc_op_918_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_918_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_917_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_917_write_1_schema` (schema): Esquema destino
- `vc_op_927_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_927_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_926_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_926_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_926_write_1_schema` (schema): Esquema destino
- `vc_op_943_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_943_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_942_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_942_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_942_write_1_schema` (schema): Esquema destino
- `vc_op_952_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_952_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_951_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_951_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_951_write_1_schema` (schema): Esquema destino
- `vc_op_965_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_965_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_964_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_964_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_964_write_1_schema` (schema): Esquema destino
- `vc_op_978_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_978_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_977_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_977_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_977_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_977_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_977_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_977_write_1_schema` (schema): Esquema destino
- `vc_op_996_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_996_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_995_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_995_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_995_write_1_schema` (schema): Esquema destino
- `vc_op_1008_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1008_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1007_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1007_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1007_write_1_schema` (schema): Esquema destino
- `vc_op_1021_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1021_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1020_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1020_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1020_write_1_schema` (schema): Esquema destino
- `vc_op_1033_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1033_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1032_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1032_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1032_write_1_schema` (schema): Esquema destino
- `vc_op_1042_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1042_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1041_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1041_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1041_write_1_schema` (schema): Esquema destino
- `vc_op_1051_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1061_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1061_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1060_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1060_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1060_write_1_schema` (schema): Esquema destino
- `vc_op_1067_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1067_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1066_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1066_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1066_write_1_schema` (schema): Esquema destino
- `vc_op_1077_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1077_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1076_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1076_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1076_write_1_schema` (schema): Esquema destino
- `vc_op_1088_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1088_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1087_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1087_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1087_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1087_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1087_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1087_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
