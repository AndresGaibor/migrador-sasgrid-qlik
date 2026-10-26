# Job `job_orcfileformat`

- **Programa SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas` (sha256 `9b1debec099f`)
- **Instrucciones:** 9 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `mydblib` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s28` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:28`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 2. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s29` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:29`
- **Conexiones:** OnSubjobOk desde `op_28_maintenance_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 3. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s36` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:42`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_29_maintenance_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_42_read_file_1_row_count`, `vc_op_42_read_file_1_nulls`

### 4. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s36` · **Confianza:** medium · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_36_inline_data_1_row_count`

### 5. Escribir mydblib.compare

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s36` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36`
- **Conexiones:** Main desde `op_42_read_file_1`
- **Propiedades:**
  - `TABLE` = `compare` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_36_write_1_row_count`, `vc_op_36_write_1_schema`

### 6. Escribir work.apd

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s36` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36`
- **Conexiones:** Main desde `op_36_write_1`
- **Propiedades:**
  - `TABLE` = `apd` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_36_write_2_row_count`, `vc_op_36_write_2_schema`

### 7. Escribir mydblib.seqtab1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s36` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36`
- **Conexiones:** Main desde `op_36_write_2`
- **Propiedades:**
  - `TABLE` = `seqtab1` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:36
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_36_write_3_row_count`, `vc_op_36_write_3_schema`

### 8. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s70` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:70`
- **Conexiones:** OnSubjobOk desde `op_36_write_3`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 9. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s73` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/orcFileFormat.sas:73`
- **Conexiones:** OnSubjobOk desde `op_70_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

## Casos de validación

- `vc_op_42_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_42_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_36_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_36_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_36_write_1_schema` (schema): Esquema destino
- `vc_op_36_write_2_row_count` (row_count): Filas escritas iguales
- `vc_op_36_write_2_schema` (schema): Esquema destino
- `vc_op_36_write_3_row_count` (row_count): Filas escritas iguales
- `vc_op_36_write_3_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
