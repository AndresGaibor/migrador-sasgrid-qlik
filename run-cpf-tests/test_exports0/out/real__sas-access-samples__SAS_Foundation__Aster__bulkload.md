# Job `job_bulkload`

- **Programa SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas` (sha256 `63a03b397085`)
- **Instrucciones:** 8 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Orquestación

- Depende de (datos): `real/sas-access-samples/SAS_Foundation/DB2/bulkload.sas`
- Lo consumen: `real/sas-access-samples/SAS_Foundation/DB2/bulkload.sas`

## Variables de contexto

- `context.bl_dbname` ← SAS `bl_dbname` (%LET de primer nivel)
- `context.bl_host` ← SAS `bl_host` (%LET de primer nivel)
- `context.bl_path` ← SAS `bl_path` (%LET de primer nivel)

## Conexiones a crear

- `mydblib` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s41` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:42`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_42_read_file_1_row_count`, `vc_op_42_read_file_1_nulls`

### 2. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s41` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:41`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_41_inline_data_1_row_count`

### 3. Escribir work.DUBLKDAT

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s41` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:41`
- **Conexiones:** Main desde `op_42_read_file_1`
- **Propiedades:**
  - `TABLE` = `dublkdat` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:41
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:41
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:41
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_41_write_1_row_count`, `vc_op_41_write_1_schema`

### 4. Leer work.DUBLKDAT

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s67` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68`
- **Conexiones:** OnSubjobOk desde `op_41_write_1`
- **Propiedades:**
  - `TABLE` = `dublkdat` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_41_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_68_read_1_row_count`, `vc_op_68_read_1_schema`

### 5. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s67` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_68_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_op_68_project_1_schema`

### 6. Escribir mydblib.DUBLKTAB (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s67` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68`
- **Conexiones:** Main desde `op_68_project_1`
- **Propiedades:**
  - `TABLE` = `dublktab` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:68
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_68_write_1_row_count`, `vc_op_68_write_1_schema`

### 7. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s81` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:81`
- **Conexiones:** OnSubjobOk desde `op_68_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 8. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s93` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Aster/bulkload.sas:93`
- **Conexiones:** OnSubjobOk desde `op_81_report_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

## Casos de validación

- `vc_op_42_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_42_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_41_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_41_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_41_write_1_schema` (schema): Esquema destino
- `vc_op_68_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_68_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_68_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_68_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_68_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
