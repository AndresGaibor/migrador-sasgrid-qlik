# Job `job_bulkload`

- **Programa SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas` (sha256 `580355ec76b0`)
- **Instrucciones:** 10 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Orquestación

- Depende de (datos): `real/sas-access-samples/SAS_Foundation/Greenplum/bulkload.sas`, `real/sas-access-samples/SAS_Foundation/Impala/bulkload.sas`
- Lo consumen: `real/sas-access-samples/SAS_Foundation/Greenplum/bulkload.sas`, `real/sas-access-samples/SAS_Foundation/Impala/bulkload.sas`

## Variables de contexto

- `context.HOST` ← SAS `HOST` (%LET de primer nivel)
- `context.PORT` ← SAS `PORT` (%LET de primer nivel)

## Conexiones a crear

- `mydblib` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s36` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:36`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 2. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s37` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:37`
- **Conexiones:** OnSubjobOk desde `op_36_maintenance_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 3. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s40` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_37_maintenance_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_41_read_file_1_row_count`, `vc_op_41_read_file_1_nulls`

### 4. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s40` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:40`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_40_inline_data_1_row_count`

### 5. Escribir work.testblkld

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s40` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:40`
- **Conexiones:** Main desde `op_41_read_file_1`
- **Propiedades:**
  - `TABLE` = `testblkld` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:40
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:40
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:40
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_40_write_1_row_count`, `vc_op_40_write_1_schema`

### 6. Leer work.testblkld

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s67` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68`
- **Conexiones:** OnSubjobOk desde `op_40_write_1`
- **Propiedades:**
  - `TABLE` = `testblkld` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_40_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_68_read_1_row_count`, `vc_op_68_read_1_schema`

### 7. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s67` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_68_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_op_68_project_1_schema`

### 8. Escribir mydblib.testblkld1 (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s67` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68`
- **Conexiones:** Main desde `op_68_project_1`
- **Propiedades:**
  - `TABLE` = `testblkld1` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:68
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_68_write_1_row_count`, `vc_op_68_write_1_schema`

### 9. Leer work.testblkld

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s77` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:77`
- **Conexiones:** OnSubjobOk desde `op_68_write_1`
- **Propiedades:**
  - `TABLE` = `testblkld` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:77
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_40_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_77_read_1_row_count`, `vc_op_77_read_1_schema`

### 10. Escribir mydblib.testblkld2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s77` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:77`
- **Conexiones:** Main desde `op_77_read_1`
- **Propiedades:**
  - `TABLE` = `testblkld2` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:77
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:77
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/HAWQ/bulkload.sas:77
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_77_write_1_row_count`, `vc_op_77_write_1_schema`

## Casos de validación

- `vc_op_41_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_41_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_40_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_40_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_40_write_1_schema` (schema): Esquema destino
- `vc_op_68_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_68_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_68_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_68_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_68_write_1_schema` (schema): Esquema destino
- `vc_op_77_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_77_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_77_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_77_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
