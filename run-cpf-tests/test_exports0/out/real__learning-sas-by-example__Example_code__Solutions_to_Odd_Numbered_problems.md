# Job `job_solutions_to_odd_numbered_problems`

- **Programa SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas` (sha256 `533c753d2f02`)
- **Instrucciones:** 493 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Orquestación

- Depende de (datos): `real/learning-sas-by-example/Example_code/Create_Datasets.sas`, `real/learning-sas-by-example/Example_code/Programs_Used_in_the_Second_Edition.sas`

## Conexiones a crear

- `learn` (BASE, c:\books\learning) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales
- `perm` (BASE, c:\books\learning) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s52` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:53`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_53_read_file_1_row_count`, `vc_op_53_read_file_1_nulls`

### 2. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s52` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:52`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_53_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:52
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Number`, `Price`, `Value` _(tipos por determinar)_
- **Expresión** (línea 55): SAS `Number*Price` → Java `(input_row.Number * input_row.Price)`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_52_compute_1_nulls`, `vc_op_52_compute_1_dates`, `vc_op_52_compute_1_numeric`

### 3. Escribir portfolio

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s52` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:52`
- **Conexiones:** Main desde `op_52_compute_1`
- **Propiedades:**
  - `TABLE` = `portfolio` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:52
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:52
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:52
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_52_write_1_row_count`, `vc_op_52_write_1_schema`

### 4. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s59` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:59`
- **Conexiones:** OnSubjobOk desde `op_52_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 5. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s63` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:63`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_59_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_63_aggregate_1_aggregates`, `vc_op_63_aggregate_1_numeric`

### 6. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s74` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:75`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_63_aggregate_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_75_read_file_1_row_count`, `vc_op_75_read_file_1_nulls`

### 7. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s74` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:74`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_74_inline_data_1_row_count`

### 8. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s74` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:74`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_75_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:74
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `X`, `Z`, `y`, `Sum` _(tipos por determinar)_
- **Expresión** (línea 77): SAS `X + y + Z` → Java `((input_row.X + input_row.y) + input_row.Z)`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_74_compute_1_nulls`, `vc_op_74_compute_1_dates`, `vc_op_74_compute_1_numeric`

### 9. Escribir XYZ

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s74` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:74`
- **Conexiones:** Main desde `op_74_compute_1`
- **Propiedades:**
  - `TABLE` = `xyz` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:74
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:74
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:74
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_74_write_1_row_count`, `vc_op_74_write_1_schema`

### 10. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s123` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:123`
- **Conexiones:** OnSubjobOk desde `op_74_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 11. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s127` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:128`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_123_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_128_read_file_1_row_count`, `vc_op_128_read_file_1_nulls`

### 12. Escribir cache

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s127` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:127`
- **Conexiones:** Main desde `op_128_read_file_1`
- **Propiedades:**
  - `TABLE` = `cache` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:127
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:127
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:127
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_127_write_1_row_count`, `vc_op_127_write_1_schema`

### 13. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s139` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:139`
- **Conexiones:** OnSubjobOk desde `op_127_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 14. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s143` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:144`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_139_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_144_read_file_1_row_count`, `vc_op_144_read_file_1_nulls`

### 15. Escribir cache

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s143` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:143`
- **Conexiones:** Main desde `op_144_read_file_1`
- **Propiedades:**
  - `TABLE` = `cache` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:143
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:143
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:143
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_143_write_1_row_count`, `vc_op_143_write_1_schema`

### 16. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s153` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:153`
- **Conexiones:** OnSubjobOk desde `op_143_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 17. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s157` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:158`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_153_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_158_read_file_1_row_count`, `vc_op_158_read_file_1_nulls`

### 18. Escribir employ

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s157` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:157`
- **Conexiones:** Main desde `op_158_read_file_1`
- **Propiedades:**
  - `TABLE` = `employ` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:157
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:157
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:157
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_157_write_1_row_count`, `vc_op_157_write_1_schema`

### 19. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s170` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:170`
- **Conexiones:** OnSubjobOk desde `op_157_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 20. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s177` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:178`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_170_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_178_read_file_1_row_count`, `vc_op_178_read_file_1_nulls`

### 21. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s177` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:177`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_177_inline_data_1_row_count`

### 22. Escribir learn.perm

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s177` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:177`
- **Conexiones:** Main desde `op_178_read_file_1`
- **Propiedades:**
  - `TABLE` = `perm` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:177
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:177
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:177
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_177_write_1_row_count`, `vc_op_177_write_1_schema`

### 23. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s193` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:193`
- **Conexiones:** OnSubjobOk desde `op_177_write_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 24. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s200` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:201`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_193_maintenance_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_201_read_file_1_row_count`, `vc_op_201_read_file_1_nulls`

### 25. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s200` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:200`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_200_inline_data_1_row_count`

### 26. Escribir perm.Survey2018

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s200` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:200`
- **Conexiones:** Main desde `op_201_read_file_1`
- **Propiedades:**
  - `TABLE` = `survey2018` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:200
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:200
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:200
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería perm es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_200_write_1_row_count`, `vc_op_200_write_1_schema`

### 27. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s217` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:217`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_200_write_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_217_aggregate_1_aggregates`, `vc_op_217_aggregate_1_numeric`

### 28. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s222` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:222`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_217_aggregate_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:222 · nombre oficial
  - `INTABLE` (Inline Table) = `agegrp | 31 - 50 | 31 to 50
agegrp | 51 - 70 | 50 to 70
agegrp | 71 - high | 71 and older
party | R | Republican
likert | 2 | Disagree
likert | 3 | No Opinion
likert | 4 | Agree
likert | 5 | Strongly Agree` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:222 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_222_format_definition_1_schema`

### 29. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s236` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:237`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_222_format_definition_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_237_read_file_1_row_count`, `vc_op_237_read_file_1_nulls`

### 30. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s236` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:236`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_236_inline_data_1_row_count`

### 31. Escribir voter

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s236` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:236`
- **Conexiones:** Main desde `op_237_read_file_1`
- **Propiedades:**
  - `TABLE` = `voter` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:236
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:236
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:236
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_236_write_1_row_count`, `vc_op_236_write_1_schema`

### 32. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s256` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:256`
- **Conexiones:** OnSubjobOk desde `op_236_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 33. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s262` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:262`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_256_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_262_aggregate_1_aggregates`, `vc_op_262_aggregate_1_numeric`

### 34. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s267` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:268`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_262_aggregate_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_268_read_file_1_row_count`, `vc_op_268_read_file_1_nulls`

### 35. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s267` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:267`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_267_inline_data_1_row_count`

### 36. Escribir colors

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s267` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:267`
- **Conexiones:** Main desde `op_268_read_file_1`
- **Propiedades:**
  - `TABLE` = `colors` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:267
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:267
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:267
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_267_write_1_row_count`, `vc_op_267_write_1_schema`

### 37. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s272` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:272`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_267_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:272 · nombre oficial
  - `INTABLE` (Inline Table) = `color | Y','O | Group 2
color |   | Not Given
color | Other | Group 3` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:272 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_272_format_definition_1_schema`

### 38. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s280` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:280`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_272_format_definition_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_280_aggregate_1_aggregates`, `vc_op_280_aggregate_1_numeric`

### 39. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s294` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:294`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_280_aggregate_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:294 · nombre oficial
  - `INTABLE` (Inline Table) = `age20yr | low-20 | 1
age20yr | 21-40 | 2
age20yr | 41-60 | 3
age20yr | 61-80 | 4
age20yr | 81-high | 5` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:294 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_294_format_definition_1_schema`

### 40. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s316` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:316`
- **Conexiones:** OnSubjobOk desde `op_294_format_definition_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 41. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s320` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:321`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_316_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_321_read_file_1_row_count`, `vc_op_321_read_file_1_nulls`

### 42. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s320` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:320`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_320_inline_data_1_row_count`

### 43. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s320` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:320`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_321_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 7 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:320
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `CourseGrade` _(tipos por determinar)_
- **Expresión** (línea 329): SAS `.2*QuizGrade + .3*Midterm + .5*Final` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.2*QuizGrade'
- **Expresión** (línea 322): SAS `if Age = 12 then Grade = 6` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 323): SAS `else if Age = 13 then Grade = 9` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 324): SAS `if Quiz = 'A' then QuizGrade = 95` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 325): SAS `else if Quiz = 'B' then QuizGrade = 85` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 326): SAS `else if Quiz = 'C' then QuizGrade = 75` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 327): SAS `else if Quiz = 'D' then QuizGrade = 70` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 328): SAS `else if Quiz = 'F' then QuizGrade = 65` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_320_compute_1_nulls`, `vc_op_320_compute_1_dates`, `vc_op_320_compute_1_numeric`

### 44. Escribir school

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s320` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:320`
- **Conexiones:** Main desde `op_320_compute_1`
- **Propiedades:**
  - `TABLE` = `school` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:320
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:320
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:320
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_320_write_1_row_count`, `vc_op_320_write_1_schema`

### 45. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s340` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:340`
- **Conexiones:** OnSubjobOk desde `op_320_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 46. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s345` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:345`
- **Conexiones:** OnSubjobOk desde `op_340_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 47. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s349` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:349`
- **Conexiones:** OnSubjobOk desde `op_345_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 48. Leer learn.blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s354` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:354`
- **Conexiones:** OnSubjobOk desde `op_349_report_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:354
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_354_read_1_row_count`, `vc_op_354_read_1_schema`

### 49. Escribir blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s354` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:354`
- **Conexiones:** Main desde `op_354_read_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:354
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:354
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:354
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_354_write_1_row_count`, `vc_op_354_write_1_schema`

### 50. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s366` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:366`
- **Conexiones:** OnSubjobOk desde `op_354_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 51. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s371` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:371`
- **Conexiones:** OnSubjobOk desde `op_366_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 52. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s380` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:381`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_371_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_381_read_file_1_row_count`, `vc_op_381_read_file_1_nulls`

### 53. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s380` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:380`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_380_inline_data_1_row_count`

### 54. Escribir vitals

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s380` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:380`
- **Conexiones:** Main desde `op_381_read_file_1`
- **Propiedades:**
  - `TABLE` = `vitals` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:380
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:380
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:380
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_380_write_1_row_count`, `vc_op_380_write_1_schema`

### 55. Leer vitals

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s400` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400`
- **Conexiones:** OnSubjobOk desde `op_380_write_1`
- **Propiedades:**
  - `TABLE` = `vitals` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_380_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_400_read_1_row_count`, `vc_op_400_read_1_schema`

### 56. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s400` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_400_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 10 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 402): SAS `if Age lt 50 and not missing(Age) then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 403): SAS `if Pulse lt 70 then PulseGroup = 'Low '` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 404): SAS `else PulseGroup = 'High'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 405): SAS `if SBP lt 140 then SBPGroup = 'Low '` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 406): SAS `else SBPGroup = 'High'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 408): SAS `else if Age ge 50 then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 409): SAS `if Pulse lt 74 then PulseGroup = 'Low'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 410): SAS `else PulseGroup = 'High'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 411): SAS `if SBP lt 140 then SBPGroup = 'Low'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 412): SAS `else SBPGroup = 'High'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_400_compute_1_nulls`, `vc_op_400_compute_1_dates`, `vc_op_400_compute_1_numeric`

### 57. Escribir newvitals

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s400` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400`
- **Conexiones:** Main desde `op_400_compute_1`
- **Propiedades:**
  - `TABLE` = `newvitals` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:400
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_400_write_1_row_count`, `vc_op_400_write_1_schema`

### 58. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s417` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:417`
- **Conexiones:** OnSubjobOk desde `op_400_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 59. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s421` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:422`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_417_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_422_read_file_1_row_count`, `vc_op_422_read_file_1_nulls`

### 60. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s421` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:421`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_421_inline_data_1_row_count`

### 61. Escribir test

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s421` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:421`
- **Conexiones:** Main desde `op_422_read_file_1`
- **Propiedades:**
  - `TABLE` = `test` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:421
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:421
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:421
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_421_write_1_row_count`, `vc_op_421_write_1_schema`

### 62. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s432` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:432`
- **Conexiones:** OnSubjobOk desde `op_421_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 63. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s436` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:436`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_432_report_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:436
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `LogN` _(tipos por determinar)_
- **Expresión** (línea 438): SAS `log(N)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función log
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_436_compute_1_nulls`, `vc_op_436_compute_1_dates`, `vc_op_436_compute_1_numeric`

### 64. Escribir logs

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s436` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:436`
- **Conexiones:** Main desde `op_436_compute_1`
- **Propiedades:**
  - `TABLE` = `logs` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:436
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:436
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:436
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_436_write_1_row_count`, `vc_op_436_write_1_schema`

### 65. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s444` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:444`
- **Conexiones:** OnSubjobOk desde `op_436_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 66. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s448` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:448`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_444_report_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:448
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `y` _(tipos por determinar)_
- **Expresión** (línea 450): SAS `3*x**2 - 5*x + 10` → _sin traducción automática_
  - ⚠ Sin traducción automática: inesperado: '*'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_448_compute_1_nulls`, `vc_op_448_compute_1_dates`, `vc_op_448_compute_1_numeric`

### 67. Escribir plotit

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s448` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:448`
- **Conexiones:** Main desde `op_448_compute_1`
- **Propiedades:**
  - `TABLE` = `plotit` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:448
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:448
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:448
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_448_write_1_row_count`, `vc_op_448_write_1_schema`

### 68. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s456` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:456`
- **Conexiones:** OnSubjobOk desde `op_448_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 69. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s461` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:463`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_456_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_463_read_file_1_row_count`, `vc_op_463_read_file_1_nulls`

### 70. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s461` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:461`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_461_inline_data_1_row_count`

### 71. Escribir temperatures

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s461` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:461`
- **Conexiones:** Main desde `op_463_read_file_1`
- **Propiedades:**
  - `TABLE` = `temperatures` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:461
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:461
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:461
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_461_write_1_row_count`, `vc_op_461_write_1_schema`

### 72. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s471` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:471`
- **Conexiones:** OnSubjobOk desde `op_461_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 73. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s475` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:479`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_471_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_479_read_file_1_row_count`, `vc_op_479_read_file_1_nulls`

### 74. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s475` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:475`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_475_inline_data_1_row_count`

### 75. Escribir temperature

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s475` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:475`
- **Conexiones:** Main desde `op_479_read_file_1`
- **Propiedades:**
  - `TABLE` = `temperature` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:475
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:475
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:475
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_475_write_1_row_count`, `vc_op_475_write_1_schema`

### 76. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s492` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:492`
- **Conexiones:** OnSubjobOk desde `op_475_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 77. Escribir money

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s496` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:496`
- **Conexiones:** OnSubjobOk desde `op_492_report_1`
- **Propiedades:**
  - `TABLE` = `money` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:496
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:496
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:496
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_496_write_1_row_count`, `vc_op_496_write_1_schema`

### 78. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s508` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:508`
- **Conexiones:** OnSubjobOk desde `op_496_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 79. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s512` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:513`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_508_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_513_read_file_1_row_count`, `vc_op_513_read_file_1_nulls`

### 80. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s512` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:512`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_512_inline_data_1_row_count`

### 81. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s512` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:512`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_513_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:512
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Age` _(tipos por determinar)_
- **Expresión** (línea 516): SAS `yrdif(DOB,Visit,'Actual')` → _sin traducción automática_
  - ⚠ Sin traducción automática: función yrdif
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_512_compute_1_nulls`, `vc_op_512_compute_1_dates`, `vc_op_512_compute_1_numeric`

### 82. Escribir dates

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s512` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:512`
- **Conexiones:** Main desde `op_512_compute_1`
- **Propiedades:**
  - `TABLE` = `dates` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:512
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:512
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:512
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_512_write_1_row_count`, `vc_op_512_write_1_schema`

### 83. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s524` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:524`
- **Conexiones:** OnSubjobOk desde `op_512_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 84. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s529` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:530`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_524_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_530_read_file_1_row_count`, `vc_op_530_read_file_1_nulls`

### 85. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s529` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:529`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_529_inline_data_1_row_count`

### 86. Escribir year1910_2006

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s529` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:529`
- **Conexiones:** Main desde `op_530_read_file_1`
- **Propiedades:**
  - `TABLE` = `year1910_2006` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:529
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:529
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:529
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_529_write_1_row_count`, `vc_op_529_write_1_schema`

### 87. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s542` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:542`
- **Conexiones:** OnSubjobOk desde `op_529_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 88. Leer learn.hosp

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s546` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546`
- **Conexiones:** OnSubjobOk desde `op_542_report_1`
- **Propiedades:**
  - `TABLE` = `hosp` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_546_read_1_row_count`, `vc_op_546_read_1_schema`

### 89. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s546` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_546_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: AdmitDate` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546 · nombre oficial
- **Esquema:** `AdmitDate` _(tipos por determinar)_
- **Pruebas:** `vc_op_546_select_columns_1_schema`

### 90. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s546` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_546_select_columns_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Day`, `Month`, `Year` _(tipos por determinar)_
- **Expresión** (línea 548): SAS `weekday(AdmitDate)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función weekday
- **Expresión** (línea 549): SAS `month(AdmitDate)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función month
- **Expresión** (línea 550): SAS `year(AdmitDate)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función year
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_546_compute_1_nulls`, `vc_op_546_compute_1_dates`, `vc_op_546_compute_1_numeric`

### 91. Escribir freq

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s546` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546`
- **Conexiones:** Main desde `op_546_compute_1`
- **Propiedades:**
  - `TABLE` = `freq` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:546
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_546_write_1_row_count`, `vc_op_546_write_1_schema`

### 92. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s553` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:553`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_546_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:553 · nombre oficial
  - `INTABLE` (Inline Table) = `days | 7 | Sat` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:553 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_553_format_definition_1_schema`

### 93. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s564` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:564`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_553_format_definition_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_564_aggregate_1_aggregates`, `vc_op_564_aggregate_1_numeric`

### 94. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s571` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:571`
- **Conexiones:** OnSubjobOk desde `op_564_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 95. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s577` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:578`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_571_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_578_read_file_1_row_count`, `vc_op_578_read_file_1_nulls`

### 96. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s577` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:577`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_577_inline_data_1_row_count`

### 97. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s577` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:577`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_578_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:577
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 579): SAS `if missing(Day) then Date = mdy(Month,15,Year)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 580): SAS `else Date = mdy(Month,Day,Year)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_577_compute_1_nulls`, `vc_op_577_compute_1_dates`, `vc_op_577_compute_1_numeric`

### 98. Escribir dates

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s577` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:577`
- **Conexiones:** Main desde `op_577_compute_1`
- **Propiedades:**
  - `TABLE` = `dates` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:577
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:577
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:577
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_577_write_1_row_count`, `vc_op_577_write_1_schema`

### 99. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s589` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:589`
- **Conexiones:** OnSubjobOk desde `op_577_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 100. Leer learn.medical

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s593` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593`
- **Conexiones:** OnSubjobOk desde `op_589_report_1`
- **Propiedades:**
  - `TABLE` = `medical` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_593_read_1_row_count`, `vc_op_593_read_1_schema`

### 101. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s593` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_593_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Quarters` _(tipos por determinar)_
- **Expresión** (línea 595): SAS `intck('qtr','01Jan2006'd,VisitDate)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intck
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_593_compute_1_nulls`, `vc_op_593_compute_1_dates`, `vc_op_593_compute_1_numeric`

### 102. Escribir intervals

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s593` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593`
- **Conexiones:** Main desde `op_593_compute_1`
- **Propiedades:**
  - `TABLE` = `intervals` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:593
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_593_write_1_row_count`, `vc_op_593_write_1_schema`

### 103. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s599` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:599`
- **Conexiones:** OnSubjobOk desde `op_593_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 104. Leer learn.medical

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s603` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603`
- **Conexiones:** OnSubjobOk desde `op_599_report_1`
- **Propiedades:**
  - `TABLE` = `medical` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_603_read_1_row_count`, `vc_op_603_read_1_schema`

### 105. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s603` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_603_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Patno, VisitDate` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603 · nombre oficial
- **Esquema:** `Patno`, `VisitDate` _(tipos por determinar)_
- **Pruebas:** `vc_op_603_select_columns_1_schema`

### 106. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s603` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_603_select_columns_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Return` _(tipos por determinar)_
- **Expresión** (línea 605): SAS `intnx('month',VisitDate,6,'sameday')` → _sin traducción automática_
  - ⚠ Sin traducción automática: función intnx
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_603_compute_1_nulls`, `vc_op_603_compute_1_dates`, `vc_op_603_compute_1_numeric`

### 107. Escribir return

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s603` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603`
- **Conexiones:** Main desde `op_603_compute_1`
- **Propiedades:**
  - `TABLE` = `return` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:603
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_603_write_1_row_count`, `vc_op_603_write_1_schema`

### 108. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s610` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:610`
- **Conexiones:** OnSubjobOk desde `op_603_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 109. Leer learn.blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s614` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614`
- **Conexiones:** OnSubjobOk desde `op_610_report_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_614_read_1_row_count`, `vc_op_614_read_1_schema`

### 110. Filtrar filas (sentencia WHERE): Gender eq 'Female' and BloodType='AB'

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s614` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:616`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_614_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:616 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `Gender == 'Female'; BloodType == 'AB'` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:616 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:616 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `BloodType`, `Gender` _(tipos por determinar)_
- **Expresión** (línea 616): SAS `Gender eq 'Female' and BloodType='AB'` → Java `(input_row.Gender.equals("Female") && input_row.BloodType.equals("AB"))`
- **Pruebas:** `vc_op_616_filter_1_row_count`, `vc_op_616_filter_1_nulls`, `vc_op_616_filter_1_empty`

### 111. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s614` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_616_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Combined` _(tipos por determinar)_
- **Expresión** (línea 617): SAS `.001*WBC + RBC` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.001*WBC + R'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_614_compute_1_nulls`, `vc_op_614_compute_1_dates`, `vc_op_614_compute_1_numeric`

### 112. Escribir subset_a

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s614` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614`
- **Conexiones:** Main desde `op_614_compute_1`
- **Propiedades:**
  - `TABLE` = `subset_a` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:614
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_614_write_1_row_count`, `vc_op_614_write_1_schema`

### 113. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s621` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:621`
- **Conexiones:** OnSubjobOk desde `op_614_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 114. Leer learn.blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s624` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624`
- **Conexiones:** OnSubjobOk desde `op_621_report_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_624_read_1_row_count`, `vc_op_624_read_1_schema`

### 115. Filtrar filas (IF subsetting): Gender eq 'Female' and BloodType='AB' and Combined ge 14

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s624` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:627`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_624_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:627 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `Gender == 'Female'; BloodType == 'AB'; Combined >= 14` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:627 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:627 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `BloodType`, `Combined`, `Gender` _(tipos por determinar)_
- **Expresión** (línea 627): SAS `Gender eq 'Female' and BloodType='AB' and Combined ge 14` → Java `((input_row.Gender.equals("Female") && input_row.BloodType.equals("AB")) && (input_row.Combined >= 14))`
- **Pruebas:** `vc_op_627_filter_1_row_count`, `vc_op_627_filter_1_nulls`, `vc_op_627_filter_1_empty`

### 116. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s624` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_627_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Combined` _(tipos por determinar)_
- **Expresión** (línea 626): SAS `.001*WBC + RBC` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.001*WBC + R'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_624_compute_1_nulls`, `vc_op_624_compute_1_dates`, `vc_op_624_compute_1_numeric`

### 117. Escribir subset_b

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s624` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624`
- **Conexiones:** Main desde `op_624_compute_1`
- **Propiedades:**
  - `TABLE` = `subset_b` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:624
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_624_write_1_row_count`, `vc_op_624_write_1_schema`

### 118. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s631` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:631`
- **Conexiones:** OnSubjobOk desde `op_624_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 119. Leer learn.blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s635` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635`
- **Conexiones:** OnSubjobOk desde `op_631_report_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_635_read_1_row_count`, `vc_op_635_read_1_schema`

### 120. Filtrar filas (sentencia WHERE): Chol lt 100 and Chol is not missing

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s635` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:637`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_635_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 637): SAS `Chol lt 100 and Chol is not missing` → _sin traducción automática_
  - ⚠ Construcción SAS sin traducción automática
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_op_637_filter_1_row_count`, `vc_op_637_filter_1_nulls`, `vc_op_637_filter_1_empty`

### 121. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s635` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_637_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 641): SAS `if Gender = 'Female' then output lowfemale` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 642): SAS `else if Gender = 'Male' then output lowmale` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_635_compute_1_nulls`, `vc_op_635_compute_1_dates`, `vc_op_635_compute_1_numeric`

### 122. Escribir lowmale

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s635` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635`
- **Conexiones:** Main desde `op_635_compute_1`
- **Propiedades:**
  - `TABLE` = `lowmale` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_635_write_1_row_count`, `vc_op_635_write_1_schema`

### 123. Escribir lowfemale

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s635` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635`
- **Conexiones:** Main desde `op_635_write_1`
- **Propiedades:**
  - `TABLE` = `lowfemale` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:635
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_635_write_2_row_count`, `vc_op_635_write_2_schema`

### 124. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s646` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:646`
- **Conexiones:** OnSubjobOk desde `op_635_write_2`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 125. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s650` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:650`
- **Conexiones:** OnSubjobOk desde `op_646_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 126. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s655` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:655`
- **Conexiones:** OnSubjobOk desde `op_650_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 127. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s659` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:659`
- **Conexiones:** OnSubjobOk desde `op_655_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 128. Leer learn.inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s662` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662`
- **Conexiones:** OnSubjobOk desde `op_659_report_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_662_read_1_row_count`, `vc_op_662_read_1_schema`

### 129. Leer learn.newproducts

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s662` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662`
- **Propiedades:**
  - `TABLE` = `newproducts` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_662_read_2_row_count`, `vc_op_662_read_2_schema`

### 130. Concatenar entradas

- **Acción:** add_component · **Componente:** `tUnite` ![Icono Talend](assets/talend-icons/tUnite_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s662` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-standard-properties)
- **Conexiones:** Main desde `op_662_read_1`
- **Pendientes:**
  - Esquemas compatibles entre entradas
- **Pruebas:** `vc_op_662_union_1_row_count`

### 131. Escribir updated

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s662` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662`
- **Conexiones:** Main desde `op_662_union_1`
- **Propiedades:**
  - `TABLE` = `updated` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:662
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_662_write_1_row_count`, `vc_op_662_write_1_schema`

### 132. Leer updated

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s666` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666`
- **Conexiones:** OnSubjobOk desde `op_662_write_1`
- **Propiedades:**
  - `TABLE` = `updated` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_662_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_666_read_1_row_count`, `vc_op_666_read_1_schema`

### 133. Ordenar por Model

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s666` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_666_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `Model` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666 · nombre oficial
- **Esquema:** `Model` _(tipos por determinar)_
- **Pruebas:** `vc_op_666_sort_1_ordering`

### 134. Escribir updated

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s666` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666`
- **Conexiones:** Main desde `op_666_sort_1`
- **Propiedades:**
  - `TABLE` = `updated` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:666
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_666_write_1_row_count`, `vc_op_666_write_1_schema`

### 135. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s671` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:671`
- **Conexiones:** OnSubjobOk desde `op_666_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 136. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s675` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:675`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_671_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_675_aggregate_1_aggregates`, `vc_op_675_aggregate_1_numeric`

### 137. Leer learn.gym

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s681` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681`
- **Conexiones:** OnSubjobOk desde `op_675_aggregate_1`
- **Propiedades:**
  - `TABLE` = `gym` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_681_read_1_row_count`, `vc_op_681_read_1_schema`

### 138. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s681` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_681_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `FeePercent` _(tipos por determinar)_
- **Expresión** (línea 684): SAS `round(100*fee / Fee_Mean)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función round
- **Expresión** (línea 683): SAS `if _n_ = 1 then set Meanfee` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_681_compute_1_nulls`, `vc_op_681_compute_1_dates`, `vc_op_681_compute_1_numeric`

### 139. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s681` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_681_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Fee_Mean` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681 · nombre oficial
- **Pruebas:** `vc_op_681_select_columns_1_schema`

### 140. Escribir percent

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s681` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681`
- **Conexiones:** Main desde `op_681_select_columns_1`
- **Propiedades:**
  - `TABLE` = `percent` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:681
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_681_write_1_row_count`, `vc_op_681_write_1_schema`

### 141. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s689` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:689`
- **Conexiones:** OnSubjobOk desde `op_681_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 142. Leer learn.inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s693` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693`
- **Conexiones:** OnSubjobOk desde `op_689_report_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_693_read_1_row_count`, `vc_op_693_read_1_schema`

### 143. Ordenar por Model

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s693` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_693_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `Model` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693 · nombre oficial
- **Esquema:** `Model` _(tipos por determinar)_
- **Pruebas:** `vc_op_693_sort_1_ordering`

### 144. Escribir inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s693` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693`
- **Conexiones:** Main desde `op_693_sort_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:693
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_693_write_1_row_count`, `vc_op_693_write_1_schema`

### 145. Leer learn.purchase

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s697` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697`
- **Conexiones:** OnSubjobOk desde `op_693_write_1`
- **Propiedades:**
  - `TABLE` = `purchase` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_697_read_1_row_count`, `vc_op_697_read_1_schema`

### 146. Ordenar por Model

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s697` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_697_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `Model` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697 · nombre oficial
- **Esquema:** `Model` _(tipos por determinar)_
- **Pruebas:** `vc_op_697_sort_1_ordering`

### 147. Escribir purchase

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s697` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697`
- **Conexiones:** Main desde `op_697_sort_1`
- **Propiedades:**
  - `TABLE` = `purchase` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:697
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_697_write_1_row_count`, `vc_op_697_write_1_schema`

### 148. Leer inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s701` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701`
- **Conexiones:** OnSubjobOk desde `op_697_write_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_693_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_701_read_1_row_count`, `vc_op_701_read_1_schema`

### 149. Leer purchase

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s701` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701`
- **Propiedades:**
  - `TABLE` = `purchase` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_697_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_701_read_2_row_count`, `vc_op_701_read_2_schema`

### 150. Unir (merge_by): work.inventory, work.purchase

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s701` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_701_read_1`, Lookup desde `op_701_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `Model` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701
- **Esquema:** `Model` _(tipos por determinar)_
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_op_701_join_1_duplicates`, `vc_op_701_join_1_row_count`, `vc_op_701_join_1_nulls`

### 151. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s701` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_701_join_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Price`, `Quantity`, `TotalPrice` _(tipos por determinar)_
- **Expresión** (línea 706): SAS `Quantity*Price` → Java `(input_row.Quantity * input_row.Price)`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_701_compute_1_nulls`, `vc_op_701_compute_1_dates`, `vc_op_701_compute_1_numeric`

### 152. Escribir pur_price

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s701` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701`
- **Conexiones:** Main desde `op_701_compute_1`
- **Propiedades:**
  - `TABLE` = `pur_price` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:701
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_701_write_1_row_count`, `vc_op_701_write_1_schema`

### 153. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s711` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:711`
- **Conexiones:** OnSubjobOk desde `op_701_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 154. Leer learn.inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s716` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716`
- **Conexiones:** OnSubjobOk desde `op_711_report_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_716_read_1_row_count`, `vc_op_716_read_1_schema`

### 155. Leer learn.purchase

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s716` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716`
- **Propiedades:**
  - `TABLE` = `purchase` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_716_read_2_row_count`, `vc_op_716_read_2_schema`

### 156. Unir (merge_by): learn.inventory, learn.purchase

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s716` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_716_read_1`, Lookup desde `op_716_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_op_716_join_1_duplicates`, `vc_op_716_join_1_row_count`, `vc_op_716_join_1_nulls`

### 157. Escribir try1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s716` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716`
- **Conexiones:** Main desde `op_716_join_1`
- **Propiedades:**
  - `TABLE` = `try1` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:716
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_716_write_1_row_count`, `vc_op_716_write_1_schema`

### 158. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s721` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:721`
- **Conexiones:** OnSubjobOk desde `op_716_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 159. Leer learn.inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s725` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725`
- **Conexiones:** OnSubjobOk desde `op_721_report_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_725_read_1_row_count`, `vc_op_725_read_1_schema`

### 160. Leer learn.purchase

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s725` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725`
- **Propiedades:**
  - `TABLE` = `purchase` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_725_read_2_row_count`, `vc_op_725_read_2_schema`

### 161. Unir (merge_by): learn.inventory, learn.purchase

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s725` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_725_read_1`, Lookup desde `op_725_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_op_725_join_1_duplicates`, `vc_op_725_join_1_row_count`, `vc_op_725_join_1_nulls`

### 162. Escribir try2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s725` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725`
- **Conexiones:** Main desde `op_725_join_1`
- **Propiedades:**
  - `TABLE` = `try2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:725
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_725_write_1_row_count`, `vc_op_725_write_1_schema`

### 163. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s730` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:730`
- **Conexiones:** OnSubjobOk desde `op_725_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 164. Leer learn.inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s734` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734`
- **Conexiones:** OnSubjobOk desde `op_730_report_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_734_read_1_row_count`, `vc_op_734_read_1_schema`

### 165. Leer learn.purchase

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s734` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734`
- **Propiedades:**
  - `TABLE` = `purchase` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_734_read_2_row_count`, `vc_op_734_read_2_schema`

### 166. Unir (merge_by): learn.inventory, learn.purchase

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s734` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_734_read_1`, Lookup desde `op_734_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_op_734_join_1_duplicates`, `vc_op_734_join_1_row_count`, `vc_op_734_join_1_nulls`

### 167. Escribir try3

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s734` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734`
- **Conexiones:** Main desde `op_734_join_1`
- **Propiedades:**
  - `TABLE` = `try3` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:734
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_734_write_1_row_count`, `vc_op_734_write_1_schema`

### 168. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s739` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:739`
- **Conexiones:** OnSubjobOk desde `op_734_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 169. Leer learn.demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s745` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745`
- **Conexiones:** OnSubjobOk desde `op_739_report_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_745_read_1_row_count`, `vc_op_745_read_1_schema`

### 170. Ordenar por ID

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s745` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_745_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745 · nombre oficial
- **Esquema:** `ID` _(tipos por determinar)_
- **Pruebas:** `vc_op_745_sort_1_ordering`

### 171. Escribir demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s745` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745`
- **Conexiones:** Main desde `op_745_sort_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:745
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_745_write_1_row_count`, `vc_op_745_write_1_schema`

### 172. Leer learn.survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s749` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749`
- **Conexiones:** OnSubjobOk desde `op_745_write_1`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_749_read_1_row_count`, `vc_op_749_read_1_schema`

### 173. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s749` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_749_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `ID → NumID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749
- **Esquema:** `NumID` _(tipos por determinar)_
- **Pruebas:** `vc_op_749_rename_1_schema`

### 174. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s749` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_749_rename_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ID` _(tipos por determinar)_
- **Expresión** (línea 751): SAS `put(NumID,z3.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_749_compute_1_nulls`, `vc_op_749_compute_1_dates`, `vc_op_749_compute_1_numeric`

### 175. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s749` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_749_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: NumID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749 · nombre oficial
- **Pruebas:** `vc_op_749_select_columns_1_schema`

### 176. Escribir survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s749` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749`
- **Conexiones:** Main desde `op_749_select_columns_1`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:749
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_749_write_1_row_count`, `vc_op_749_write_1_schema`

### 177. Leer survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s755` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755`
- **Conexiones:** OnSubjobOk desde `op_749_write_1`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_749_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_755_read_1_row_count`, `vc_op_755_read_1_schema`

### 178. Ordenar por ID

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s755` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_755_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755 · nombre oficial
- **Esquema:** `ID` _(tipos por determinar)_
- **Pruebas:** `vc_op_755_sort_1_ordering`

### 179. Escribir survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s755` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755`
- **Conexiones:** Main desde `op_755_sort_1`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:755
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_755_write_1_row_count`, `vc_op_755_write_1_schema`

### 180. Leer demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s759` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759`
- **Conexiones:** OnSubjobOk desde `op_755_write_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_745_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_759_read_1_row_count`, `vc_op_759_read_1_schema`

### 181. Leer survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s759` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_755_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_759_read_2_row_count`, `vc_op_759_read_2_schema`

### 182. Unir (merge_by): work.demographic_id, work.survey2

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s759` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_759_read_1`, Lookup desde `op_759_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `ID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759
- **Esquema:** `ID` _(tipos por determinar)_
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_op_759_join_1_duplicates`, `vc_op_759_join_1_row_count`, `vc_op_759_join_1_nulls`

### 183. Escribir combine

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s759` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759`
- **Conexiones:** Main desde `op_759_join_1`
- **Propiedades:**
  - `TABLE` = `combine` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:759
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_759_write_1_row_count`, `vc_op_759_write_1_schema`

### 184. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s766` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:766`
- **Conexiones:** OnSubjobOk desde `op_759_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 185. Leer learn.demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s771` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771`
- **Conexiones:** OnSubjobOk desde `op_766_report_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_771_read_1_row_count`, `vc_op_771_read_1_schema`

### 186. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s771` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_771_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `ID → CharID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771
- **Esquema:** `CharID` _(tipos por determinar)_
- **Pruebas:** `vc_op_771_rename_1_schema`

### 187. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s771` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_771_rename_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ID` _(tipos por determinar)_
- **Expresión** (línea 773): SAS `input(CharID,3.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_771_compute_1_nulls`, `vc_op_771_compute_1_dates`, `vc_op_771_compute_1_numeric`

### 188. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s771` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_771_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: CharID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771 · nombre oficial
- **Pruebas:** `vc_op_771_select_columns_1_schema`

### 189. Escribir demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s771` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771`
- **Conexiones:** Main desde `op_771_select_columns_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:771
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_771_write_1_row_count`, `vc_op_771_write_1_schema`

### 190. Leer demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s777` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777`
- **Conexiones:** OnSubjobOk desde `op_771_write_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_771_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_777_read_1_row_count`, `vc_op_777_read_1_schema`

### 191. Ordenar por ID

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s777` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_777_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777 · nombre oficial
- **Esquema:** `ID` _(tipos por determinar)_
- **Pruebas:** `vc_op_777_sort_1_ordering`

### 192. Escribir demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s777` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777`
- **Conexiones:** Main desde `op_777_sort_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:777
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_777_write_1_row_count`, `vc_op_777_write_1_schema`

### 193. Leer learn.survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s781` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781`
- **Conexiones:** OnSubjobOk desde `op_777_write_1`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_781_read_1_row_count`, `vc_op_781_read_1_schema`

### 194. Ordenar por ID

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s781` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_781_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `ID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781 · nombre oficial
- **Esquema:** `ID` _(tipos por determinar)_
- **Pruebas:** `vc_op_781_sort_1_ordering`

### 195. Escribir survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s781` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781`
- **Conexiones:** Main desde `op_781_sort_1`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:781
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_781_write_1_row_count`, `vc_op_781_write_1_schema`

### 196. Leer demographic_ID

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s785` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785`
- **Conexiones:** OnSubjobOk desde `op_781_write_1`
- **Propiedades:**
  - `TABLE` = `demographic_id` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_777_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_785_read_1_row_count`, `vc_op_785_read_1_schema`

### 197. Leer survey2

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s785` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785`
- **Propiedades:**
  - `TABLE` = `survey2` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_781_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_785_read_2_row_count`, `vc_op_785_read_2_schema`

### 198. Unir (merge_by): work.demographic_id, work.survey2

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s785` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_785_read_1`, Lookup desde `op_785_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `ID` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785
- **Esquema:** `ID` _(tipos por determinar)_
- **Supuestos:** MERGE BY no es un join SQL: con claves repetidas en ambos lados el resultado difiere
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
  - Determinar el tipo de join (el programa no usa `if a;`/`if a and b;` de forma reconocible)
- **Pruebas:** `vc_op_785_join_1_duplicates`, `vc_op_785_join_1_row_count`, `vc_op_785_join_1_nulls`

### 199. Escribir combine

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s785` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785`
- **Conexiones:** Main desde `op_785_join_1`
- **Propiedades:**
  - `TABLE` = `combine` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:785
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_785_write_1_row_count`, `vc_op_785_write_1_schema`

### 200. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s792` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:792`
- **Conexiones:** OnSubjobOk desde `op_785_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 201. Leer learn.health

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s796` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796`
- **Conexiones:** OnSubjobOk desde `op_792_report_1`
- **Propiedades:**
  - `TABLE` = `health` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_796_read_1_row_count`, `vc_op_796_read_1_schema`

### 202. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s796` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_796_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `5 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `BMI`, `BMIRound`, `BMIRound_tenth`, `BMIGroup`, `BMITrunc` _(tipos por determinar)_
- **Expresión** (línea 798): SAS `(Weight/2.2) / (Height*.0254)**2` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.0254)**2'
- **Expresión** (línea 799): SAS `round(BMI)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función round
- **Expresión** (línea 800): SAS `round(BMI,.1)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.1)'
- **Expresión** (línea 801): SAS `round(BMI,5)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función round
- **Expresión** (línea 802): SAS `int(BMI)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función int
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_796_compute_1_nulls`, `vc_op_796_compute_1_dates`, `vc_op_796_compute_1_numeric`

### 203. Escribir health

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s796` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796`
- **Conexiones:** Main desde `op_796_compute_1`
- **Propiedades:**
  - `TABLE` = `health` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:796
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_796_write_1_row_count`, `vc_op_796_write_1_schema`

### 204. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s806` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:806`
- **Conexiones:** OnSubjobOk desde `op_796_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 205. Leer learn.blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s810` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810`
- **Conexiones:** OnSubjobOk desde `op_806_report_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_810_read_1_row_count`, `vc_op_810_read_1_schema`

### 206. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s810` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_810_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 812): SAS `if missing(WBC) then call missing(Gender,RBC, Chol)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_810_compute_1_nulls`, `vc_op_810_compute_1_dates`, `vc_op_810_compute_1_numeric`

### 207. Escribir miss_blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s810` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810`
- **Conexiones:** Main desde `op_810_compute_1`
- **Propiedades:**
  - `TABLE` = `miss_blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:810
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_810_write_1_row_count`, `vc_op_810_write_1_schema`

### 208. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s816` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:816`
- **Conexiones:** OnSubjobOk desde `op_810_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 209. Leer learn.psych

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820`
- **Conexiones:** OnSubjobOk desde `op_816_report_1`
- **Propiedades:**
  - `TABLE` = `psych` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_820_read_1_row_count`, `vc_op_820_read_1_schema`

### 210. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s820` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_820_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `QuesAve`, `ScoreAve`, `Composit` _(tipos por determinar)_
- **Expresión** (línea 828): SAS `ScoreAve + 10*QuesAve` → Java `(input_row.ScoreAve + (10 * input_row.QuesAve))`
- **Expresión** (línea 822): SAS `if n(of Score1-Score5) ge 3 then
   ScoreAve = mean(largest(1,of Score1-Score5),
                   largest(2,of Score1-Score5),
                   largest(3,of Score1-Score5))` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 826): SAS `if n(of Ques1-Ques10) ge 7 then 
      QuesAve = mean(of Ques1-Ques10)` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_820_compute_1_nulls`, `vc_op_820_compute_1_dates`, `vc_op_820_compute_1_numeric`

### 211. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_820_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: ID, ScoreAve, QuesAve, Composit` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820 · nombre oficial
- **Esquema:** `ID`, `ScoreAve`, `QuesAve`, `Composit` _(tipos por determinar)_
- **Pruebas:** `vc_op_820_select_columns_1_schema`

### 212. Escribir psychscore

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820`
- **Conexiones:** Main desde `op_820_select_columns_1`
- **Propiedades:**
  - `TABLE` = `psychscore` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:820
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_820_write_1_row_count`, `vc_op_820_write_1_schema`

### 213. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s833` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:833`
- **Conexiones:** OnSubjobOk desde `op_820_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 214. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s837` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:837`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_833_report_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `6 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:837
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `x`, `y`, `z`, `AbsZ`, `ExpX`, `Circumference` _(tipos por determinar)_
- **Expresión** (línea 838): SAS `10` → Java `10`
- **Expresión** (línea 838): SAS `20` → Java `20`
- **Expresión** (línea 838): SAS `-30` → Java `-30`
- **Expresión** (línea 839): SAS `abs(z)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función abs
- **Expresión** (línea 840): SAS `round(exp(x),.001)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.001)'
- **Expresión** (línea 841): SAS `round(2*constant('pi')*y,.001)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.001)'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_837_compute_1_nulls`, `vc_op_837_compute_1_dates`, `vc_op_837_compute_1_numeric`

### 215. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s846` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:846`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_837_compute_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:846
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Age` _(tipos por determinar)_
- **Expresión** (línea 850): SAS `9 + ceil(rand('uniform')*51)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función ceil
- **Expresión** (línea 848): SAS `if rand('uniform') le .4 then Gender = 'Female'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 849): SAS `else Gender = 'Male'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_846_compute_1_nulls`, `vc_op_846_compute_1_dates`, `vc_op_846_compute_1_numeric`

### 216. Escribir fake

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s846` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:846`
- **Conexiones:** Main desde `op_846_compute_1`
- **Propiedades:**
  - `TABLE` = `fake` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:846
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:846
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:846
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_846_write_1_row_count`, `vc_op_846_write_1_schema`

### 217. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s856` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:856`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_846_write_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_856_aggregate_1_aggregates`, `vc_op_856_aggregate_1_numeric`

### 218. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s861` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:861`
- **Conexiones:** OnSubjobOk desde `op_856_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 219. Leer learn.char_num

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s865` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865`
- **Conexiones:** OnSubjobOk desde `op_861_report_1`
- **Propiedades:**
  - `TABLE` = `char_num` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_865_read_1_row_count`, `vc_op_865_read_1_schema`

### 220. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s865` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_865_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `Age → Char_Age, Weight → Char_Weight, Zip → Num_Zip, SS → Num_ss` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865
- **Esquema:** `Char_Age`, `Char_Weight`, `Num_Zip`, `Num_ss` _(tipos por determinar)_
- **Pruebas:** `vc_op_865_rename_1_schema`

### 221. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s865` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_865_rename_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `4 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Age`, `Weight`, `SS`, `Zip` _(tipos por determinar)_
- **Expresión** (línea 871): SAS `input(Char_Age,8.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 872): SAS `input(Char_Weight,8.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 873): SAS `put(Num_SS,ssn11.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 874): SAS `put(Num_Zip,z5.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_865_compute_1_nulls`, `vc_op_865_compute_1_dates`, `vc_op_865_compute_1_numeric`

### 222. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s865` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_865_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Char_:, Num_:` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865 · nombre oficial
- **Pruebas:** `vc_op_865_select_columns_1_schema`

### 223. Escribir convert

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s865` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865`
- **Conexiones:** Main desde `op_865_select_columns_1`
- **Propiedades:**
  - `TABLE` = `convert` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:865
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_865_write_1_row_count`, `vc_op_865_write_1_schema`

### 224. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s879` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:879`
- **Conexiones:** OnSubjobOk desde `op_865_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 225. Leer learn.stocks

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s883` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883`
- **Conexiones:** OnSubjobOk desde `op_879_report_1`
- **Propiedades:**
  - `TABLE` = `stocks` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_883_read_1_row_count`, `vc_op_883_read_1_schema`

### 226. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s883` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_883_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Price1`, `Price2`, `Average` _(tipos por determinar)_
- **Expresión** (línea 885): SAS `lag(Price)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lag
- **Expresión** (línea 886): SAS `lag2(Price)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lag2
- **Expresión** (línea 887): SAS `mean(Price, Price1, Price2)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función mean
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_883_compute_1_nulls`, `vc_op_883_compute_1_dates`, `vc_op_883_compute_1_numeric`

### 227. Escribir smooth

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s883` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883`
- **Conexiones:** Main desde `op_883_compute_1`
- **Propiedades:**
  - `TABLE` = `smooth` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:883
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_883_write_1_row_count`, `vc_op_883_write_1_schema`

### 228. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s891` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:891`
- **Conexiones:** OnSubjobOk desde `op_883_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 229. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s902` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:902`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_891_report_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `11 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:902
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Name`, `A`, `B`, `AandB`, `Cat`, `Substring`, `L_A`, `L_B`, `L_Name`, `L_AandB`, `L_Cat`, `L_Match`, `L_Substring` _(tipos por determinar)_
- **Expresión** (línea 904): SAS `'Goldstein'` → Java `"Goldstein"`
- **Expresión** (línea 905): SAS `A || B` → Java `(input_row.A + input_row.B)`
- **Expresión** (línea 906): SAS `cats(A,B)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función cats
- **Expresión** (línea 909): SAS `substr(Name,5,2)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función substr
- **Expresión** (línea 910): SAS `lengthc(A)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lengthc
- **Expresión** (línea 911): SAS `lengthc(B)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lengthc
- **Expresión** (línea 912): SAS `lengthc(Name)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lengthc
- **Expresión** (línea 913): SAS `lengthc(AandB)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lengthc
- **Expresión** (línea 914): SAS `lengthc(Cat)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lengthc
- **Expresión** (línea 915): SAS `lengthc(Match)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lengthc
- **Expresión** (línea 916): SAS `lengthc(Substring)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función lengthc
- **Expresión** (línea 907): SAS `if Name = 'Smith' then Match = 'No'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 908): SAS `else Match = 'Yes'` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_902_compute_1_nulls`, `vc_op_902_compute_1_dates`, `vc_op_902_compute_1_numeric`

### 230. Escribir storage

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s902` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:902`
- **Conexiones:** Main desde `op_902_compute_1`
- **Propiedades:**
  - `TABLE` = `storage` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:902
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:902
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:902
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_902_write_1_row_count`, `vc_op_902_write_1_schema`

### 231. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s920` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:920`
- **Conexiones:** OnSubjobOk desde `op_902_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 232. Leer learn.names_and_more

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s936` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936`
- **Conexiones:** OnSubjobOk desde `op_920_report_1`
- **Propiedades:**
  - `TABLE` = `names_and_more` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_936_read_1_row_count`, `vc_op_936_read_1_schema`

### 233. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s936` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_936_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Name`, `Phone` _(tipos por determinar)_
- **Expresión** (línea 938): SAS `compbl(Name)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función compbl
- **Expresión** (línea 939): SAS `compress(Phone,,'kd')` → _sin traducción automática_
  - ⚠ Sin traducción automática: función compress
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_936_compute_1_nulls`, `vc_op_936_compute_1_dates`, `vc_op_936_compute_1_numeric`

### 234. Escribir names_and_more

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s936` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936`
- **Conexiones:** Main desde `op_936_compute_1`
- **Propiedades:**
  - `TABLE` = `names_and_more` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:936
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_936_write_1_row_count`, `vc_op_936_write_1_schema`

### 235. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s943` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:943`
- **Conexiones:** OnSubjobOk desde `op_936_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 236. Leer learn.names_and_more

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s947` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947`
- **Conexiones:** OnSubjobOk desde `op_943_report_1`
- **Propiedades:**
  - `TABLE` = `names_and_more` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_947_read_1_row_count`, `vc_op_947_read_1_schema`

### 237. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s947` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_947_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Mixed` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947 · nombre oficial
- **Esquema:** `Mixed` _(tipos por determinar)_
- **Pruebas:** `vc_op_947_select_columns_1_schema`

### 238. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s947` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_947_select_columns_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `4 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Integer`, `Numerator`, `Denominator`, `Price` _(tipos por determinar)_
- **Expresión** (línea 949): SAS `input(scan(Mixed,1,' /'),8.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 950): SAS `input(scan(Mixed,2,' /'),8.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 951): SAS `input(scan(Mixed,3,' /'),8.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 954): SAS `round(Price,.001)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.001)'
- **Expresión** (línea 952): SAS `if missing(Numerator) then Price = Integer` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 953): SAS `else Price = Integer + Numerator / Denominator` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_947_compute_1_nulls`, `vc_op_947_compute_1_dates`, `vc_op_947_compute_1_numeric`

### 239. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s947` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_947_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Numerator, Denominator, Integer` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947 · nombre oficial
- **Pruebas:** `vc_op_947_select_columns_2_schema`

### 240. Escribir convert

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s947` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947`
- **Conexiones:** Main desde `op_947_select_columns_2`
- **Propiedades:**
  - `TABLE` = `convert` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:947
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_947_write_1_row_count`, `vc_op_947_write_1_schema`

### 241. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s959` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:959`
- **Conexiones:** OnSubjobOk desde `op_947_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 242. Leer learn.study

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s964` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964`
- **Conexiones:** OnSubjobOk desde `op_959_report_1`
- **Propiedades:**
  - `TABLE` = `study` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_964_read_1_row_count`, `vc_op_964_read_1_schema`

### 243. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s964` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_964_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Group, Subgroup` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964 · nombre oficial
- **Esquema:** `Group`, `Subgroup` _(tipos por determinar)_
- **Pruebas:** `vc_op_964_select_columns_1_schema`

### 244. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s964` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_964_select_columns_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Combined` _(tipos por determinar)_
- **Expresión** (línea 967): SAS `catx('-',Group,Subgroup)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función catx
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_964_compute_1_nulls`, `vc_op_964_compute_1_dates`, `vc_op_964_compute_1_numeric`

### 245. Escribir concat

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s964` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964`
- **Conexiones:** Main desde `op_964_compute_1`
- **Propiedades:**
  - `TABLE` = `concat` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:964
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_964_write_1_row_count`, `vc_op_964_write_1_schema`

### 246. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s971` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:971`
- **Conexiones:** OnSubjobOk desde `op_964_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 247. Leer learn.study

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s975` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975`
- **Conexiones:** OnSubjobOk desde `op_971_report_1`
- **Propiedades:**
  - `TABLE` = `study` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_975_read_1_row_count`, `vc_op_975_read_1_schema`

### 248. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s975` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_975_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Group, Subgroup` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975 · nombre oficial
- **Esquema:** `Group`, `Subgroup` _(tipos por determinar)_
- **Pruebas:** `vc_op_975_select_columns_1_schema`

### 249. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s975` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_975_select_columns_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Combined` _(tipos por determinar)_
- **Expresión** (línea 978): SAS `trim(Group) || '-' || put(Subgroup,1.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_975_compute_1_nulls`, `vc_op_975_compute_1_dates`, `vc_op_975_compute_1_numeric`

### 250. Escribir concat

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s975` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975`
- **Conexiones:** Main desde `op_975_compute_1`
- **Propiedades:**
  - `TABLE` = `concat` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:975
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_975_write_1_row_count`, `vc_op_975_write_1_schema`

### 251. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s982` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:982`
- **Conexiones:** OnSubjobOk desde `op_975_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 252. Leer learn.sales

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s986` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:986`
- **Conexiones:** OnSubjobOk desde `op_982_report_1`
- **Propiedades:**
  - `TABLE` = `sales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:986
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_986_read_1_row_count`, `vc_op_986_read_1_schema`

### 253. Filtrar filas (sentencia WHERE): find(Customer,'spirit','i')

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s986` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:988`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_986_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 988): SAS `find(Customer,'spirit','i')` → _sin traducción automática_
  - ⚠ Sin traducción automática: función find
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_op_988_filter_1_row_count`, `vc_op_988_filter_1_nulls`, `vc_op_988_filter_1_empty`

### 254. Escribir spirited

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s986` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:986`
- **Conexiones:** Main desde `op_988_filter_1`
- **Propiedades:**
  - `TABLE` = `spirited` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:986
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:986
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:986
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_986_write_1_row_count`, `vc_op_986_write_1_schema`

### 255. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s992` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:992`
- **Conexiones:** OnSubjobOk desde `op_986_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 256. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s997` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:997`
- **Conexiones:** OnSubjobOk desde `op_992_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 257. Leer learn.social

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1003` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003`
- **Conexiones:** OnSubjobOk desde `op_997_report_1`
- **Propiedades:**
  - `TABLE` = `social` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1003_read_1_row_count`, `vc_op_1003_read_1_schema`

### 258. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1003` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1003_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1005): SAS `if SS1 eq SS2 then output exact` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1006): SAS `else if spedis(SS1,SS2) le 25 and 
      not missing(SS1) and
      not missing(SS2) then output 
      within25` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1003_compute_1_nulls`, `vc_op_1003_compute_1_dates`, `vc_op_1003_compute_1_numeric`

### 259. Escribir exact

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1003` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003`
- **Conexiones:** Main desde `op_1003_compute_1`
- **Propiedades:**
  - `TABLE` = `exact` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1003_write_1_row_count`, `vc_op_1003_write_1_schema`

### 260. Escribir within25

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1003` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003`
- **Conexiones:** Main desde `op_1003_write_1`
- **Propiedades:**
  - `TABLE` = `within25` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1003
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1003_write_2_row_count`, `vc_op_1003_write_2_schema`

### 261. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1013` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1013`
- **Conexiones:** OnSubjobOk desde `op_1003_write_2`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 262. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1017` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1017`
- **Conexiones:** OnSubjobOk desde `op_1013_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 263. Leer learn.names_and_more

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1021` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021`
- **Conexiones:** OnSubjobOk desde `op_1017_report_1`
- **Propiedades:**
  - `TABLE` = `names_and_more` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1021_read_1_row_count`, `vc_op_1021_read_1_schema`

### 264. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1021` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1021_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: phone` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021 · nombre oficial
- **Esquema:** `phone` _(tipos por determinar)_
- **Pruebas:** `vc_op_1021_select_columns_1_schema`

### 265. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1021` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1021_select_columns_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `AreaCode` _(tipos por determinar)_
- **Expresión** (línea 1024): SAS `substr(Phone,2,3)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función substr
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1021_compute_1_nulls`, `vc_op_1021_compute_1_dates`, `vc_op_1021_compute_1_numeric`

### 266. Escribir numbers

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1021` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021`
- **Conexiones:** Main desde `op_1021_compute_1`
- **Propiedades:**
  - `TABLE` = `numbers` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1021
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1021_write_1_row_count`, `vc_op_1021_write_1_schema`

### 267. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1028` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1028`
- **Conexiones:** OnSubjobOk desde `op_1021_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 268. Leer learn.personal

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1032` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032`
- **Conexiones:** OnSubjobOk desde `op_1028_report_1`
- **Propiedades:**
  - `TABLE` = `personal` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1032_read_1_row_count`, `vc_op_1032_read_1_schema`

### 269. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1032` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1032_read_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Food1-Food8` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032 · nombre oficial
- **Pruebas:** `vc_op_1032_select_columns_1_schema`

### 270. Escribir personal

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1032` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032`
- **Conexiones:** Main desde `op_1032_select_columns_1`
- **Propiedades:**
  - `TABLE` = `personal` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1032
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1032_write_1_row_count`, `vc_op_1032_write_1_schema`

### 271. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1039` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1039`
- **Conexiones:** OnSubjobOk desde `op_1032_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 272. Leer learn.survey1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1043` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043`
- **Conexiones:** OnSubjobOk desde `op_1039_report_1`
- **Propiedades:**
  - `TABLE` = `survey1` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1043_read_1_row_count`, `vc_op_1043_read_1_schema`

### 273. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1043` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043`
- **Conexiones:** Main desde `op_1043_read_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1043_stateful_1_ordering`, `vc_op_1043_stateful_1_duplicates`

### 274. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1043` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1043_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: i` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043 · nombre oficial
- **Pruebas:** `vc_op_1043_select_columns_1_schema`

### 275. Escribir survey1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1043` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043`
- **Conexiones:** Main desde `op_1043_select_columns_1`
- **Propiedades:**
  - `TABLE` = `survey1` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1043
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1043_write_1_row_count`, `vc_op_1043_write_1_schema`

### 276. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1053` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1053`
- **Conexiones:** OnSubjobOk desde `op_1043_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 277. Leer learn.nines

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1057` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057`
- **Conexiones:** OnSubjobOk desde `op_1053_report_1`
- **Propiedades:**
  - `TABLE` = `nines` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1057_read_1_row_count`, `vc_op_1057_read_1_schema`

### 278. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1057` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1057_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1061): SAS `if nums{i} = 999 then
      call missing(nums{i})` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1057_compute_1_nulls`, `vc_op_1057_compute_1_dates`, `vc_op_1057_compute_1_numeric`

### 279. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1057` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057`
- **Conexiones:** Main desde `op_1057_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1057_stateful_1_ordering`, `vc_op_1057_stateful_1_duplicates`

### 280. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1057` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1057_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: i` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057 · nombre oficial
- **Pruebas:** `vc_op_1057_select_columns_1_schema`

### 281. Escribir nonines

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1057` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057`
- **Conexiones:** Main desde `op_1057_select_columns_1`
- **Propiedades:**
  - `TABLE` = `nonines` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1057
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1057_write_1_row_count`, `vc_op_1057_write_1_schema`

### 282. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1068` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1068`
- **Conexiones:** OnSubjobOk desde `op_1057_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 283. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1072` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1076`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1068_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1076_read_file_1_row_count`, `vc_op_1076_read_file_1_nulls`

### 284. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1072` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1072_inline_data_1_row_count`

### 285. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1072` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1076_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `NumberPassed` _(tipos por determinar)_
- **Expresión** (línea 1077): SAS `0` → Java `0`
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1072_compute_1_nulls`, `vc_op_1072_compute_1_dates`, `vc_op_1072_compute_1_numeric`

### 286. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1072` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072`
- **Conexiones:** Main desde `op_1072_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1072_stateful_1_ordering`, `vc_op_1072_stateful_1_duplicates`

### 287. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1072` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1072_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Test` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072 · nombre oficial
- **Pruebas:** `vc_op_1072_select_columns_1_schema`

### 288. Escribir passing

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1072` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072`
- **Conexiones:** Main desde `op_1072_select_columns_1`
- **Propiedades:**
  - `TABLE` = `passing` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1072
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1072_write_1_row_count`, `vc_op_1072_write_1_schema`

### 289. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1089` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1089`
- **Conexiones:** OnSubjobOk desde `op_1072_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 290. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1095` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1095`
- **Conexiones:** OnSubjobOk desde `op_1089_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 291. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1108` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1108`
- **Conexiones:** OnSubjobOk desde `op_1095_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 292. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1124` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1124`
- **Conexiones:** OnSubjobOk desde `op_1108_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 293. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1134` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1134`
- **Conexiones:** OnSubjobOk desde `op_1124_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 294. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1148` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1148`
- **Conexiones:** OnSubjobOk desde `op_1134_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 295. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1162` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1162`
- **Conexiones:** OnSubjobOk desde `op_1148_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 296. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1173` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1173`
- **Conexiones:** OnSubjobOk desde `op_1162_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 297. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1212` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1212`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1173_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1212_aggregate_1_aggregates`, `vc_op_1212_aggregate_1_numeric`

### 298. Leer learn.college

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1224` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224`
- **Conexiones:** OnSubjobOk desde `op_1212_aggregate_1`
- **Propiedades:**
  - `TABLE` = `college` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1224_read_1_row_count`, `vc_op_1224_read_1_schema`

### 299. Ordenar por SchoolSize

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s1224` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_1224_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `SchoolSize` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224 · nombre oficial
- **Esquema:** `SchoolSize` _(tipos por determinar)_
- **Pruebas:** `vc_op_1224_sort_1_ordering`

### 300. Escribir college

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1224` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224`
- **Conexiones:** Main desde `op_1224_sort_1`
- **Propiedades:**
  - `TABLE` = `college` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1224
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1224_write_1_row_count`, `vc_op_1224_write_1_schema`

### 301. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1230` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1230`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1224_write_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1230_aggregate_1_aggregates`, `vc_op_1230_aggregate_1_numeric`

### 302. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1242` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1242`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1230_aggregate_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1242_aggregate_1_aggregates`, `vc_op_1242_aggregate_1_numeric`

### 303. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1254` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1254`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1242_aggregate_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1254 · nombre oficial
  - `INTABLE` (Inline Table) = `rank | 51-74 | Third Quartile
rank | 75-100 | Top Quarter` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1254 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1254_format_definition_1_schema`

### 304. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1262` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1262`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1254_format_definition_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1262_aggregate_1_aggregates`, `vc_op_1262_aggregate_1_numeric`

### 305. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1272` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1272`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1262_aggregate_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1272_aggregate_1_aggregates`, `vc_op_1272_aggregate_1_numeric`

### 306. Leer summary

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Conexiones:** OnSubjobOk desde `op_1272_aggregate_1`
- **Propiedades:**
  - `TABLE` = `summary` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_1279_read_1_row_count`, `vc_op_1279_read_1_schema`

### 307. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1279` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1279_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 4 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1285): SAS `if _type_ = '00' then output grand` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1286): SAS `else if _type_ = '10' then output bygender` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1287): SAS `else if _type_ = '01' then output bysize` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1288): SAS `else if _type_ = '11' then output cell` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1279_compute_1_nulls`, `vc_op_1279_compute_1_dates`, `vc_op_1279_compute_1_numeric`

### 308. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1279_compute_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: _freq_` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279 · nombre oficial
- **Pruebas:** `vc_op_1279_select_columns_1_schema`

### 309. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1279_select_columns_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Gender, SchoolSize` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279 · nombre oficial
- **Pruebas:** `vc_op_1279_select_columns_2_schema`

### 310. Escribir grand

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Conexiones:** Main desde `op_1279_select_columns_2`
- **Propiedades:**
  - `TABLE` = `grand` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1279_write_1_row_count`, `vc_op_1279_write_1_schema`

### 311. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1279_write_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: SchoolSize` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279 · nombre oficial
- **Pruebas:** `vc_op_1279_select_columns_3_schema`

### 312. Escribir bygender

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Conexiones:** Main desde `op_1279_select_columns_3`
- **Propiedades:**
  - `TABLE` = `bygender` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1279_write_2_row_count`, `vc_op_1279_write_2_schema`

### 313. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1279_write_2`
- **Propiedades:**
  - `SCHEMA` (Schema) = `drop: Gender` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279 · nombre oficial
- **Pruebas:** `vc_op_1279_select_columns_4_schema`

### 314. Escribir bysize

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Conexiones:** Main desde `op_1279_select_columns_4`
- **Propiedades:**
  - `TABLE` = `bysize` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1279_write_3_row_count`, `vc_op_1279_write_3_schema`

### 315. Escribir cell

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1279` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279`
- **Conexiones:** Main desde `op_1279_write_3`
- **Propiedades:**
  - `TABLE` = `cell` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1279
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1279_write_4_row_count`, `vc_op_1279_write_4_schema`

### 316. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1292` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1292`
- **Conexiones:** OnSubjobOk desde `op_1279_write_4`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 317. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1296` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1296`
- **Conexiones:** OnSubjobOk desde `op_1292_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 318. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1300` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1300`
- **Conexiones:** OnSubjobOk desde `op_1296_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 319. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1304` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1304`
- **Conexiones:** OnSubjobOk desde `op_1300_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 320. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1309` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1309`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1304_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_1309_aggregate_1_aggregates`, `vc_op_1309_aggregate_1_numeric`

### 321. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1314` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1314`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1309_aggregate_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1314 · nombre oficial
  - `INTABLE` (Inline Table) = `cholgrp | 201-high | High
cholgrp | . | Missing` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1314 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1314_format_definition_1_schema`

### 322. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1322` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1322`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1314_format_definition_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_1322_aggregate_1_aggregates`, `vc_op_1322_aggregate_1_numeric`

### 323. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1329` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1329`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1322_aggregate_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_1329_aggregate_1_aggregates`, `vc_op_1329_aggregate_1_numeric`

### 324. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1335` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1335`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1329_aggregate_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1335 · nombre oficial
  - `INTABLE` (Inline Table) = `rank | 71-high | 71 and higher` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1335 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1335_format_definition_1_schema`

### 325. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1341` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1341`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1335_format_definition_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_1341_aggregate_1_aggregates`, `vc_op_1341_aggregate_1_numeric`

### 326. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1348` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1348`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1341_aggregate_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_1348_aggregate_1_aggregates`, `vc_op_1348_aggregate_1_numeric`

### 327. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1355` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1355`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1348_aggregate_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC TABULATE: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC TABULATE a operaciones de agregación
- **Pruebas:** `vc_op_1355_aggregate_1_aggregates`, `vc_op_1355_aggregate_1_numeric`

### 328. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1355` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1355`
- **Conexiones:** Main desde `op_1355_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 329. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1363` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1363`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1355_report_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1363 · nombre oficial
  - `INTABLE` (Inline Table) = `gender | M | Male` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1363 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1363_format_definition_1_schema`

### 330. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1368` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1368`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1363_format_definition_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC TABULATE: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC TABULATE a operaciones de agregación
- **Pruebas:** `vc_op_1368_aggregate_1_aggregates`, `vc_op_1368_aggregate_1_numeric`

### 331. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1368` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1368`
- **Conexiones:** Main desde `op_1368_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 332. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1379` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1379`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1368_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC TABULATE: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC TABULATE a operaciones de agregación
- **Pruebas:** `vc_op_1379_aggregate_1_aggregates`, `vc_op_1379_aggregate_1_numeric`

### 333. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1379` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1379`
- **Conexiones:** Main desde `op_1379_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 334. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1394` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1394`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1379_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC TABULATE: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC TABULATE a operaciones de agregación
- **Pruebas:** `vc_op_1394_aggregate_1_aggregates`, `vc_op_1394_aggregate_1_numeric`

### 335. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1394` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1394`
- **Conexiones:** Main desde `op_1394_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 336. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1410` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1410`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1394_report_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1410 · nombre oficial
  - `INTABLE` (Inline Table) = `gender | M | Male` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1410 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1410_format_definition_1_schema`

### 337. Leer learn.college

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1414` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414`
- **Conexiones:** OnSubjobOk desde `op_1410_format_definition_1`
- **Propiedades:**
  - `TABLE` = `college` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1414_read_1_row_count`, `vc_op_1414_read_1_schema`

### 338. Ordenar por descending, Scholarship

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s1414` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_1414_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `descending, Scholarship` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414 · nombre oficial
- **Esquema:** `descending`, `Scholarship` _(tipos por determinar)_
- **Pruebas:** `vc_op_1414_sort_1_ordering`

### 339. Escribir college

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1414` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414`
- **Conexiones:** Main desde `op_1414_sort_1`
- **Propiedades:**
  - `TABLE` = `college` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1414
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1414_write_1_row_count`, `vc_op_1414_write_1_schema`

### 340. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1417` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1417`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1414_write_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC TABULATE: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC TABULATE a operaciones de agregación
- **Pruebas:** `vc_op_1417_aggregate_1_aggregates`, `vc_op_1417_aggregate_1_numeric`

### 341. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1417` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1417`
- **Conexiones:** Main desde `op_1417_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 342. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1435` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1435`
- **Conexiones:** OnSubjobOk desde `op_1417_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 343. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1438` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1438`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1435_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1438_aggregate_1_aggregates`, `vc_op_1438_aggregate_1_numeric`

### 344. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1451` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1451`
- **Conexiones:** OnSubjobOk desde `op_1438_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 345. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1454` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1454`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1451_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1454_aggregate_1_aggregates`, `vc_op_1454_aggregate_1_numeric`

### 346. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1463` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1463`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1454_aggregate_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC UNIVARIATE: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC UNIVARIATE a operaciones de agregación
- **Pruebas:** `vc_op_1463_aggregate_1_aggregates`, `vc_op_1463_aggregate_1_numeric`

### 347. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1463` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1463`
- **Conexiones:** Main desde `op_1463_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 348. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1469` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1469`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1463_report_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC UNIVARIATE: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC UNIVARIATE a operaciones de agregación
- **Pruebas:** `vc_op_1469_aggregate_1_aggregates`, `vc_op_1469_aggregate_1_numeric`

### 349. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1469` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1469`
- **Conexiones:** Main desde `op_1469_aggregate_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 350. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1475` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1475`
- **Conexiones:** OnSubjobOk desde `op_1469_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 351. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1481` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1481`
- **Conexiones:** OnSubjobOk desde `op_1475_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 352. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1488` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1488`
- **Conexiones:** OnSubjobOk desde `op_1481_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 353. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1494` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1494`
- **Conexiones:** OnSubjobOk desde `op_1488_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 354. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1500` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1500`
- **Conexiones:** OnSubjobOk desde `op_1494_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 355. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1506` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1506`
- **Conexiones:** OnSubjobOk desde `op_1500_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 356. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1511` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1512`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1506_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1512_read_file_1_row_count`, `vc_op_1512_read_file_1_nulls`

### 357. Escribir prob21_1

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1511` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1511`
- **Conexiones:** Main desde `op_1512_read_file_1`
- **Propiedades:**
  - `TABLE` = `prob21_1` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1511
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1511
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1511
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1511_write_1_row_count`, `vc_op_1511_write_1_schema`

### 358. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1518` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1518`
- **Conexiones:** OnSubjobOk desde `op_1511_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 359. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1522` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1523`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1518_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1523_read_file_1_row_count`, `vc_op_1523_read_file_1_nulls`

### 360. Escribir prob21_3

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1522` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1522`
- **Conexiones:** Main desde `op_1523_read_file_1`
- **Propiedades:**
  - `TABLE` = `prob21_3` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1522
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1522
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1522
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1522_write_1_row_count`, `vc_op_1522_write_1_schema`

### 361. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1530` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1530`
- **Conexiones:** OnSubjobOk desde `op_1522_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 362. Leer learn.bicycles

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1535` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535`
- **Conexiones:** OnSubjobOk desde `op_1530_report_1`
- **Propiedades:**
  - `TABLE` = `bicycles` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1535_read_1_row_count`, `vc_op_1535_read_1_schema`

### 363. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1535` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1535_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1540): SAS `if lastrec then
      put "---------------------------------------"/
          "Total Units Sold is " TotalUnits comma10. /
          "Sales Total is " Sum_of_Sales dollar10.0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1535_compute_1_nulls`, `vc_op_1535_compute_1_dates`, `vc_op_1535_compute_1_numeric`

### 364. Escribir prob21_5

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1535` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535`
- **Conexiones:** Main desde `op_1535_compute_1`
- **Propiedades:**
  - `TABLE` = `prob21_5` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1535_write_1_row_count`, `vc_op_1535_write_1_schema`

### 365. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `s1535` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1535`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `op_1535_write_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_op_1535_write_file_1_row_count`

### 366. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1547` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1548`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1535_write_file_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1548_read_file_1_row_count`, `vc_op_1548_read_file_1_nulls`

### 367. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1547` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1547`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1548_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1547
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1551): SAS `if last_of_a then infile 'c:\books\learning\file_B.txt'
          firstobs=2` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1547_compute_1_nulls`, `vc_op_1547_compute_1_dates`, `vc_op_1547_compute_1_numeric`

### 368. Escribir prob21_7

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1547` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1547`
- **Conexiones:** Main desde `op_1547_compute_1`
- **Propiedades:**
  - `TABLE` = `prob21_7` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1547
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1547
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1547
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1547_write_1_row_count`, `vc_op_1547_write_1_schema`

### 369. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1557` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1557`
- **Conexiones:** OnSubjobOk desde `op_1547_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 370. Escribir prob21_9

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1561` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1561`
- **Conexiones:** OnSubjobOk desde `op_1557_report_1`
- **Propiedades:**
  - `TABLE` = `prob21_9` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1561
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1561
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1561
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1561_write_1_row_count`, `vc_op_1561_write_1_schema`

### 371. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1569` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1569`
- **Conexiones:** OnSubjobOk desde `op_1561_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 372. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1573` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1574`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1569_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1574_read_file_1_row_count`, `vc_op_1574_read_file_1_nulls`

### 373. Escribir prob21_11

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1573` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1573`
- **Conexiones:** Main desde `op_1574_read_file_1`
- **Propiedades:**
  - `TABLE` = `prob21_11` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1573
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1573
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1573
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1573_write_1_row_count`, `vc_op_1573_write_1_schema`

### 374. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1581` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1581`
- **Conexiones:** OnSubjobOk desde `op_1573_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 375. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1585` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1585`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1581_report_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1585 · nombre oficial
  - `INTABLE` (Inline Table) = `high_sbp | 140 - high | High SBP
high_dbp | 90 - high | High DBP` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1585 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1585_format_definition_1_schema`

### 376. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1593` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1593`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1585_format_definition_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC FREQ: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC FREQ a operaciones de agregación
- **Pruebas:** `vc_op_1593_aggregate_1_aggregates`, `vc_op_1593_aggregate_1_numeric`

### 377. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1600` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1600`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1593_aggregate_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1600 · nombre oficial
  - `INTABLE` (Inline Table) = `high_sbp | 140 - high | High SBP
high_dbp | 90 - high | High DBP` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1600 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1600_format_definition_1_schema`

### 378. Leer learn.bloodpressure

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1606` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606`
- **Conexiones:** OnSubjobOk desde `op_1600_format_definition_1`
- **Propiedades:**
  - `TABLE` = `bloodpressure` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1606_read_1_row_count`, `vc_op_1606_read_1_schema`

### 379. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1606` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1606_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `SBPGroup`, `DBPGroup` _(tipos por determinar)_
- **Expresión** (línea 1608): SAS `put(SBP,high_sbp.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Expresión** (línea 1609): SAS `put(DBP,high_dbp.)` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '.)'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1606_compute_1_nulls`, `vc_op_1606_compute_1_dates`, `vc_op_1606_compute_1_numeric`

### 380. Escribir bloodpressure

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1606` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606`
- **Conexiones:** Main desde `op_1606_compute_1`
- **Propiedades:**
  - `TABLE` = `bloodpressure` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1606
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1606_write_1_row_count`, `vc_op_1606_write_1_schema`

### 381. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1613` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1613`
- **Conexiones:** OnSubjobOk desde `op_1606_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 382. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1617` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1617`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1613_report_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = _por configurar_ — regla mappings · nombre oficial
  - `INTABLE` (Inline Table) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1617_format_definition_1_schema`

### 383. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1626` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1627`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1617_format_definition_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1627_read_file_1_row_count`, `vc_op_1627_read_file_1_nulls`

### 384. Escribir lettergrades

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1626` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1626`
- **Conexiones:** Main desde `op_1627_read_file_1`
- **Propiedades:**
  - `TABLE` = `lettergrades` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1626
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1626
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1626
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1626_write_1_row_count`, `vc_op_1626_write_1_schema`

### 385. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1632` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1632`
- **Conexiones:** OnSubjobOk desde `op_1626_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 386. Leer learn.dxcodes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1636` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636`
- **Conexiones:** OnSubjobOk desde `op_1632_report_1`
- **Propiedades:**
  - `TABLE` = `dxcodes` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1636_read_1_row_count`, `vc_op_1636_read_1_schema`

### 387. Renombrar columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s1636` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1636_read_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `Dx → Start, Description → Label` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636
- **Esquema:** `Start`, `Label` _(tipos por determinar)_
- **Pruebas:** `vc_op_1636_rename_1_schema`

### 388. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1636` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636`
- **Conexiones:** Main desde `op_1636_rename_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1636_stateful_1_ordering`, `vc_op_1636_stateful_1_duplicates`

### 389. Escribir control

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1636` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636`
- **Conexiones:** Main desde `op_1636_stateful_1`
- **Propiedades:**
  - `TABLE` = `control` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1636
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1636_write_1_row_count`, `vc_op_1636_write_1_schema`

### 390. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1642` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1642`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1636_write_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = _por configurar_ — regla mappings · nombre oficial
  - `INTABLE` (Inline Table) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1642_format_definition_1_schema`

### 391. Definir formatos como tabla de lookup

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar) · alternativas: `tMap (lookup)`, `Rutina Java`
- **Subjob:** `s1647` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1647`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1642_format_definition_1`
- **Propiedades:**
  - `USE_INTABLE` (Use Inline Table) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1647 · nombre oficial
  - `INTABLE` (Inline Table) = `muggle | 01jan1990'd - '31dec2004'd | Too Early
muggle | 01jan2007'd - high | Too Late` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1647 · nombre oficial
- **Esquema:** `FORMAT`:String, `CODE`:String, `LABEL`:String _(tipos por determinar)_
- **Pendientes:**
  - Confirmar cómo aplicar el formato: los rangos y OTHER necesitan lógica equivalente, no solo una tabla de filas
- **Pruebas:** `vc_op_1647_format_definition_1_schema`

### 392. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1655` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1655`
- **Conexiones:** OnSubjobOk desde `op_1647_format_definition_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 393. Leer learn.wide

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1660` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660`
- **Conexiones:** OnSubjobOk desde `op_1655_report_1`
- **Propiedades:**
  - `TABLE` = `wide` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1660_read_1_row_count`, `vc_op_1660_read_1_schema`

### 394. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1660` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1660_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `2 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `X`, `Y` _(tipos por determinar)_
- **Expresión** (línea 1665): SAS `X_array[Time]` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '[Time]'
- **Expresión** (línea 1666): SAS `y_array{Time]` → _sin traducción automática_
  - ⚠ Sin traducción automática: token no soportado: '{Time]'
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1660_compute_1_nulls`, `vc_op_1660_compute_1_dates`, `vc_op_1660_compute_1_numeric`

### 395. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1660` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660`
- **Conexiones:** Main desde `op_1660_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1660_stateful_1_ordering`, `vc_op_1660_stateful_1_duplicates`

### 396. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1660` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1660_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Subj, Time, X, Y` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660 · nombre oficial
- **Esquema:** `Subj`, `Time`, `X`, `Y` _(tipos por determinar)_
- **Pruebas:** `vc_op_1660_select_columns_1_schema`

### 397. Escribir long

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1660` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660`
- **Conexiones:** Main desde `op_1660_select_columns_1`
- **Propiedades:**
  - `TABLE` = `long` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1660
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1660_write_1_row_count`, `vc_op_1660_write_1_schema`

### 398. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1673` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1673`
- **Conexiones:** OnSubjobOk desde `op_1660_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 399. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s1677` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1677`
- **Conexiones:** OnSubjobOk desde `op_1673_report_1`
- **Supuestos:** PROC TRANSPOSE sin traducción definida
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 400. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1685` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1685`
- **Conexiones:** OnSubjobOk desde `op_1677_unsupported_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 401. Leer learn.dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1689` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689`
- **Conexiones:** OnSubjobOk desde `op_1685_report_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1689_read_1_row_count`, `vc_op_1689_read_1_schema`

### 402. Ordenar por Symbol, Date

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s1689` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_1689_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `Symbol, Date` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689 · nombre oficial
- **Esquema:** `Symbol`, `Date` _(tipos por determinar)_
- **Pruebas:** `vc_op_1689_sort_1_ordering`

### 403. Escribir dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1689` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689`
- **Conexiones:** Main desde `op_1689_sort_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1689
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1689_write_1_row_count`, `vc_op_1689_write_1_schema`

### 404. Leer dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1692` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1692`
- **Conexiones:** OnSubjobOk desde `op_1689_write_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1692
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_1689_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_1692_read_1_row_count`, `vc_op_1692_read_1_schema`

### 405. Filtrar filas (IF subsetting): last.Symbol

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1692` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1695`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_1692_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1695 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `input_row.Symbol` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1695 · nombre oficial
- **Esquema:** `Symbol` _(tipos por determinar)_
- **Expresión** (línea 1695): SAS `last.Symbol` → Java `input_row.Symbol`
- **Pruebas:** `vc_op_1695_filter_1_row_count`, `vc_op_1695_filter_1_nulls`, `vc_op_1695_filter_1_empty`

### 406. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1692` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1692`
- **Conexiones:** Main desde `op_1695_filter_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1692_stateful_1_ordering`, `vc_op_1692_stateful_1_duplicates`

### 407. Escribir lastprice

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1692` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1692`
- **Conexiones:** Main desde `op_1692_stateful_1`
- **Propiedades:**
  - `TABLE` = `lastprice` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1692
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1692
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1692
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1692_write_1_row_count`, `vc_op_1692_write_1_schema`

### 408. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1699` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1699`
- **Conexiones:** OnSubjobOk desde `op_1692_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 409. Leer learn.dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1703` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703`
- **Conexiones:** OnSubjobOk desde `op_1699_report_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1703_read_1_row_count`, `vc_op_1703_read_1_schema`

### 410. Ordenar por Symbol, Date

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s1703` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_1703_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `Symbol, Date` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703 · nombre oficial
- **Esquema:** `Symbol`, `Date` _(tipos por determinar)_
- **Pruebas:** `vc_op_1703_sort_1_ordering`

### 411. Escribir dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1703` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703`
- **Conexiones:** Main desde `op_1703_sort_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1703
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1703_write_1_row_count`, `vc_op_1703_write_1_schema`

### 412. Leer dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1706` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706`
- **Conexiones:** OnSubjobOk desde `op_1703_write_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_1703_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_1706_read_1_row_count`, `vc_op_1706_read_1_schema`

### 413. Filtrar filas (IF subsetting): last.Symbol

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1706` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1711`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_1706_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `true` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1711 · nombre oficial
  - `ADVANCED_COND` (Advanced) = `input_row.Symbol` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1711 · nombre oficial
- **Esquema:** `Symbol` _(tipos por determinar)_
- **Expresión** (línea 1711): SAS `last.Symbol` → Java `input_row.Symbol`
- **Pruebas:** `vc_op_1711_filter_1_row_count`, `vc_op_1711_filter_1_nulls`, `vc_op_1711_filter_1_empty`

### 414. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1706` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1711_filter_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1709): SAS `if first.Symbol then N_Days = 0` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1706_compute_1_nulls`, `vc_op_1706_compute_1_dates`, `vc_op_1706_compute_1_numeric`

### 415. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1706` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706`
- **Conexiones:** Main desde `op_1706_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1706_stateful_1_ordering`, `vc_op_1706_stateful_1_duplicates`

### 416. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1706` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1706_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Symbol, N_Days` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706 · nombre oficial
- **Esquema:** `Symbol`, `N_Days` _(tipos por determinar)_
- **Pruebas:** `vc_op_1706_select_columns_1_schema`

### 417. Escribir countit

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1706` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706`
- **Conexiones:** Main desde `op_1706_select_columns_1`
- **Propiedades:**
  - `TABLE` = `countit` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1706
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1706_write_1_row_count`, `vc_op_1706_write_1_schema`

### 418. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1716` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1716`
- **Conexiones:** OnSubjobOk desde `op_1706_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 419. Leer learn.dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1720` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720`
- **Conexiones:** OnSubjobOk desde `op_1716_report_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1720_read_1_row_count`, `vc_op_1720_read_1_schema`

### 420. Ordenar por Symbol, Date

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s1720` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_1720_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `Symbol, Date` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720 · nombre oficial
- **Esquema:** `Symbol`, `Date` _(tipos por determinar)_
- **Pruebas:** `vc_op_1720_sort_1_ordering`

### 421. Escribir dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1720` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720`
- **Conexiones:** Main desde `op_1720_sort_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1720
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1720_write_1_row_count`, `vc_op_1720_write_1_schema`

### 422. Leer dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1723` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723`
- **Conexiones:** OnSubjobOk desde `op_1720_write_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_1720_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_1723_read_1_row_count`, `vc_op_1723_read_1_schema`

### 423. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1723` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1723_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 3 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `FirstPrice`, `Price`, `Diff` _(tipos por determinar)_
- **Expresión** (línea 1730): SAS `Price - FirstPrice` → Java `(input_row.Price - input_row.FirstPrice)`
- **Expresión** (línea 1727): SAS `if first.Symbol and last.Symbol then delete` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1728): SAS `if first.Symbol then FirstPrice = Price` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1729): SAS `if last.Symbol then do` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1723_compute_1_nulls`, `vc_op_1723_compute_1_dates`, `vc_op_1723_compute_1_numeric`

### 424. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1723` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723`
- **Conexiones:** Main desde `op_1723_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1723_stateful_1_ordering`, `vc_op_1723_stateful_1_duplicates`

### 425. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1723` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1723_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Symbol, Price, Diff` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723 · nombre oficial
- **Esquema:** `Symbol`, `Price`, `Diff` _(tipos por determinar)_
- **Pruebas:** `vc_op_1723_select_columns_1_schema`

### 426. Escribir first_last

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1723` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723`
- **Conexiones:** Main desde `op_1723_select_columns_1`
- **Propiedades:**
  - `TABLE` = `first_last` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1723
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1723_write_1_row_count`, `vc_op_1723_write_1_schema`

### 427. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1737` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1737`
- **Conexiones:** OnSubjobOk desde `op_1723_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 428. Leer learn.dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1741` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741`
- **Conexiones:** OnSubjobOk desde `op_1737_report_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1741_read_1_row_count`, `vc_op_1741_read_1_schema`

### 429. Ordenar por Symbol, Date

- **Acción:** add_component · **Componente:** `tSortRow` ![Icono Talend](assets/talend-icons/tSortRow_icon32.png) (sin verificar)
- **Subjob:** `s1741` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tsortrow-standard-properties)
- **Conexiones:** Main desde `op_1741_read_1`
- **Propiedades:**
  - `CRITERIA` (Criteria) = `Symbol, Date` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741 · nombre oficial
- **Esquema:** `Symbol`, `Date` _(tipos por determinar)_
- **Pruebas:** `vc_op_1741_sort_1_ordering`

### 430. Escribir dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1741` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741`
- **Conexiones:** Main desde `op_1741_sort_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1741
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1741_write_1_row_count`, `vc_op_1741_write_1_schema`

### 431. Leer dailyprices

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1744` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744`
- **Conexiones:** OnSubjobOk desde `op_1741_write_1`
- **Propiedades:**
  - `TABLE` = `dailyprices` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_1741_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_1744_read_1_row_count`, `vc_op_1744_read_1_schema`

### 432. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1744` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1744_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Diff` _(tipos por determinar)_
- **Expresión** (línea 1748): SAS `dif(Price)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función dif
- **Expresión** (línea 1747): SAS `if first.Symbol and last.Symbol then delete` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1749): SAS `if not first.Symbol then output` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1744_compute_1_nulls`, `vc_op_1744_compute_1_dates`, `vc_op_1744_compute_1_numeric`

### 433. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1744` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744`
- **Conexiones:** Main desde `op_1744_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1744_stateful_1_ordering`, `vc_op_1744_stateful_1_duplicates`

### 434. Conservar/descartar columnas

- **Acción:** add_component · **Componente:** `tFilterColumns` ![Icono Talend](assets/talend-icons/tFilterColumns_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1744` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfiltercolumns-standard-properties)
- **Conexiones:** Main desde `op_1744_stateful_1`
- **Propiedades:**
  - `SCHEMA` (Schema) = `keep: Symbol, Price, Diff` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744 · nombre oficial
- **Esquema:** `Symbol`, `Price`, `Diff` _(tipos por determinar)_
- **Pruebas:** `vc_op_1744_select_columns_1_schema`

### 435. Escribir first_last

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1744` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744`
- **Conexiones:** Main desde `op_1744_select_columns_1`
- **Propiedades:**
  - `TABLE` = `first_last` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1744
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1744_write_1_row_count`, `vc_op_1744_write_1_schema`

### 436. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1754` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1754`
- **Conexiones:** OnSubjobOk desde `op_1744_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 437. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1759` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1759`
- **Conexiones:** OnSubjobOk desde `op_1754_report_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 438. Invocar macro %print_n

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s1771` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1771`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1759_report_1`
- **Propiedades:**
  - `PROCESS` (Job) = `print_n` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1771 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `learn.bicycles, 4` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1771 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %print_n (definida en real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas)

### 439. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1774` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1774`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_1771_macro_call_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** PROC MEANS: mapear estadísticas concretas a tAggregateRow
- **Pendientes:**
  - Mapear las estadísticas de PROC MEANS a operaciones de agregación
- **Pruebas:** `vc_op_1774_aggregate_1_aggregates`, `vc_op_1774_aggregate_1_numeric`

### 440. Leer summary

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1780` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1780`
- **Conexiones:** OnSubjobOk desde `op_1774_aggregate_1`
- **Propiedades:**
  - `TABLE` = `summary` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1780
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_1780_read_1_row_count`, `vc_op_1780_read_1_schema`

### 441. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s1780` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1782`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_1780_read_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1782 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 442. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s1780` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1783`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_1782_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1783 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 443. Asignar variable desde datos

- **Acción:** add_component · **Componente:** `tSetGlobalVar` ![Icono Talend](assets/talend-icons/tSetGlobalVar_icon32.png) (sin verificar) · alternativas: `tJava`, `tFlowToIterate`
- **Subjob:** `s1780` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1784`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/global-variable/tsetglobalvar)
- **Conexiones:** Main desde `op_1783_set_variable_1`
- **Propiedades:**
  - `VARIABLES` (Variables) = `KEY=None` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1784 · nombre oficial
- **Pendientes:**
  - Origen del valor y alcance de la variable

### 444. Leer learn.fitness

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1787` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787`
- **Conexiones:** OnSubjobOk desde `op_1784_set_variable_1`
- **Propiedades:**
  - `TABLE` = `fitness` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1787_read_1_row_count`, `vc_op_1787_read_1_schema`

### 445. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1787` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1787_read_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `3 asignaciones, 0 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `P_TimeMile`, `P_RestPulse`, `R_MaxPulse` _(tipos por determinar)_
- **Expresión** (línea 1789): SAS `round(100*TimeMile/&GrandTime)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función round
- **Expresión** (línea 1790): SAS `round(100*RestPulse/&GrandRest)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función round
- **Expresión** (línea 1791): SAS `round(100*MaxPulse/&GrandMax)` → _sin traducción automática_
  - ⚠ Sin traducción automática: función round
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1787_compute_1_nulls`, `vc_op_1787_compute_1_dates`, `vc_op_1787_compute_1_numeric`

### 446. Escribir compute_percents

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1787` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787`
- **Conexiones:** Main desde `op_1787_compute_1`
- **Propiedades:**
  - `TABLE` = `compute_percents` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1787
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1787_write_1_row_count`, `vc_op_1787_write_1_schema`

### 447. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1795` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1795`
- **Conexiones:** OnSubjobOk desde `op_1787_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 448. Leer learn.inventory

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1800` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801`
- **Conexiones:** OnSubjobOk desde `op_1795_report_1`
- **Propiedades:**
  - `TABLE` = `inventory` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1801_read_1_row_count`, `vc_op_1801_read_1_schema`

### 449. Filtrar filas (WHERE): Price gt 20

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1800` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_1801_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `Price > 20` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `Price` _(tipos por determinar)_
- **Expresión** (línea 1801): SAS `Price gt 20` → Java `(input_row.Price > 20)`
- **Pruebas:** `vc_op_1801_filter_1_row_count`, `vc_op_1801_filter_1_nulls`, `vc_op_1801_filter_1_empty`

### 450. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s1800` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1801_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1801
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_op_1801_project_1_schema`

### 451. Leer learn.sales

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1807` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808`
- **Conexiones:** OnSubjobOk desde `op_1801_project_1`
- **Propiedades:**
  - `TABLE` = `sales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1808_read_1_row_count`, `vc_op_1808_read_1_schema`

### 452. Filtrar filas (WHERE): Region eq 'North'

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](assets/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1807` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `op_1808_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = `&&` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808 · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = `Region == 'North'` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808 · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = `false` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808 · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Esquema:** `Region` _(tipos por determinar)_
- **Expresión** (línea 1808): SAS `Region eq 'North'` → Java `input_row.Region.equals("North")`
- **Pruebas:** `vc_op_1808_filter_1_row_count`, `vc_op_1808_filter_1_nulls`, `vc_op_1808_filter_1_empty`

### 453. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s1807` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1808_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `Name, TotalSales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `Name`, `TotalSales` _(tipos por determinar)_
- **Pruebas:** `vc_op_1808_project_1_schema`

### 454. Escribir n_sales (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1807` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808`
- **Conexiones:** Main desde `op_1808_project_1`
- **Propiedades:**
  - `TABLE` = `n_sales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1808
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1808_write_1_row_count`, `vc_op_1808_write_1_schema`

### 455. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1815` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1815`
- **Conexiones:** OnSubjobOk desde `op_1808_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 456. Leer learn.left

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821`
- **Conexiones:** OnSubjobOk desde `op_1815_report_1`
- **Propiedades:**
  - `TABLE` = `left` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1821_read_1_row_count`, `vc_op_1821_read_1_schema`

### 457. Leer learn.right

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821`
- **Propiedades:**
  - `TABLE` = `right` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1821_read_2_row_count`, `vc_op_1821_read_2_schema`

### 458. Unir (inner join): learn.left, learn.right

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s1820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1821_read_1`, Lookup desde `op_1821_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Inner Join` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `left.Subj = right.Subj` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
- **Esquema:** `Subj` _(tipos por determinar)_
- **Expresión** (línea 1821): SAS `on left.Subj = right.Subj` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_op_1821_join_1_duplicates`, `vc_op_1821_join_1_row_count`, `vc_op_1821_join_1_nulls`

### 459. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s1820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1821_join_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `LeftSubj, Height, Weight, RightSubj, Salary` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `LeftSubj`, `Height`, `Weight`, `RightSubj`, `Salary` _(tipos por determinar)_
- **Pruebas:** `vc_op_1821_project_1_schema`

### 460. Escribir both (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1820` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821`
- **Conexiones:** Main desde `op_1821_project_1`
- **Propiedades:**
  - `TABLE` = `both` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1821
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1821_write_1_row_count`, `vc_op_1821_write_1_schema`

### 461. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1833` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1833`
- **Conexiones:** OnSubjobOk desde `op_1821_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 462. Leer learn.left

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1855` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856`
- **Conexiones:** OnSubjobOk desde `op_1833_report_1`
- **Propiedades:**
  - `TABLE` = `left` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1856_read_1_row_count`, `vc_op_1856_read_1_schema`

### 463. Leer learn.right

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1855` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856`
- **Propiedades:**
  - `TABLE` = `right` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1856_read_2_row_count`, `vc_op_1856_read_2_schema`

### 464. Unir (full join): learn.left, learn.right

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s1855` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1856_read_1`, Lookup desde `op_1856_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Full outer: tMap no lo soporta directamente` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `left.Subj = right.Subj` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
- **Esquema:** `Subj` _(tipos por determinar)_
- **Expresión** (línea 1856): SAS `on left.Subj = right.Subj` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_op_1856_join_1_duplicates`, `vc_op_1856_join_1_row_count`, `vc_op_1856_join_1_nulls`

### 465. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s1855` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1856_join_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `LeftSubj, Height, Weight, RightSubj, Salary` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `LeftSubj`, `Height`, `Weight`, `RightSubj`, `Salary` _(tipos por determinar)_
- **Pruebas:** `vc_op_1856_project_1_schema`

### 466. Escribir both (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1855` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856`
- **Conexiones:** Main desde `op_1856_project_1`
- **Propiedades:**
  - `TABLE` = `both` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1856
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1856_write_1_row_count`, `vc_op_1856_write_1_schema`

### 467. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1868` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1868`
- **Conexiones:** OnSubjobOk desde `op_1856_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 468. Leer learn.left

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1872` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873`
- **Conexiones:** OnSubjobOk desde `op_1868_report_1`
- **Propiedades:**
  - `TABLE` = `left` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1873_read_1_row_count`, `vc_op_1873_read_1_schema`

### 469. Leer learn.right

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1872` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873`
- **Propiedades:**
  - `TABLE` = `right` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1873_read_2_row_count`, `vc_op_1873_read_2_schema`

### 470. Unir (left join): learn.left, learn.right

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJoin`
- **Subjob:** `s1872` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1873_read_1`, Lookup desde `op_1873_read_2`
- **Propiedades:**
  - `Join model` (Editor del componente (no es un parámetro plano)) = `Left Outer Join` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
  - `Match model` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
  - `Expression key` (Editor del componente (no es un parámetro plano)) = `left.Subj = right.Subj` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
- **Esquema:** `Subj` _(tipos por determinar)_
- **Expresión** (línea 1873): SAS `on left.Subj = right.Subj` → _sin traducción automática_
  - ⚠ Mapear las claves del ON en la tabla de join de tMap
- **Pendientes:**
  - Columnas clave y tipos en ambos lados
- **Pruebas:** `vc_op_1873_join_1_duplicates`, `vc_op_1873_join_1_row_count`, `vc_op_1873_join_1_nulls`

### 471. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s1872` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1873_join_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `LeftSubj, Height, Weight, RightSubj, Salary` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `LeftSubj`, `Height`, `Weight`, `RightSubj`, `Salary` _(tipos por determinar)_
- **Pruebas:** `vc_op_1873_project_1_schema`

### 472. Escribir both (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1872` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873`
- **Conexiones:** Main desde `op_1873_project_1`
- **Propiedades:**
  - `TABLE` = `both` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1873
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1873_write_1_row_count`, `vc_op_1873_write_1_schema`

### 473. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1885` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1885`
- **Conexiones:** OnSubjobOk desde `op_1873_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 474. Leer learn.first

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1889` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890`
- **Conexiones:** OnSubjobOk desde `op_1885_report_1`
- **Propiedades:**
  - `TABLE` = `first` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1890_read_1_row_count`, `vc_op_1890_read_1_schema`

### 475. Leer learn.second

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1889` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890`
- **Propiedades:**
  - `TABLE` = `second` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1890_read_2_row_count`, `vc_op_1890_read_2_schema`

### 476. Concatenar entradas

- **Acción:** add_component · **Componente:** `tUnite` ![Icono Talend](assets/talend-icons/tUnite_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1889` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/tunite-standard-properties)
- **Conexiones:** Main desde `op_1890_read_1`
- **Pendientes:**
  - Esquemas compatibles entre entradas
- **Pruebas:** `vc_op_1890_union_1_row_count`

### 477. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s1889` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1890_union_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_op_1890_project_1_schema`

### 478. Escribir third (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1889` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890`
- **Conexiones:** Main desde `op_1890_project_1`
- **Propiedades:**
  - `TABLE` = `third` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1890
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1890_write_1_row_count`, `vc_op_1890_write_1_schema`

### 479. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1898` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1898`
- **Conexiones:** OnSubjobOk desde `op_1890_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 480. Leer learn.blood

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s1902` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903`
- **Conexiones:** OnSubjobOk desde `op_1898_report_1`
- **Propiedades:**
  - `TABLE` = `blood` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería learn es de tipo BASE en c:\books\learning: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_op_1903_read_1_row_count`, `vc_op_1903_read_1_schema`

### 481. Agregar

- **Acción:** add_component · **Componente:** `tAggregateRow` ![Icono Talend](assets/talend-icons/tAggregateRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `s1902` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/taggregaterow-standard-properties)
- **Conexiones:** Main desde `op_1903_read_1`
- **Propiedades:**
  - `GROUPBYS` (Group by) = _por configurar_ — regla mappings · nombre oficial
  - `OPERATIONS` (Operations) = `MeanRBC = mean(RBC); MeanWBC = mean(WBC)` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903 · nombre oficial
- **Esquema:** `Subject`, `RBC`, `WBC`, `MeanRBC`, `MeanWBC`, `Percent_RBC`, `Percent_WBC` _(tipos por determinar)_
- **Pruebas:** `vc_op_1903_aggregate_1_aggregates`, `vc_op_1903_aggregate_1_numeric`

### 482. Escribir percentages (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s1902` · **Confianza:** high · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903`
- **Conexiones:** Main desde `op_1903_aggregate_1`
- **Propiedades:**
  - `TABLE` = `percentages` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903
  - `DATA_ACTION` = `INSERT` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1903
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_1903_write_1_row_count`, `vc_op_1903_write_1_schema`

### 483. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `s1915` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1915`
- **Conexiones:** OnSubjobOk desde `op_1903_write_1`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

### 484. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1919` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1921`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1915_report_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1921_read_file_1_row_count`, `vc_op_1921_read_file_1_nulls`

### 485. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1919` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1919`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1919_inline_data_1_row_count`

### 486. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1919` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1919`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1921_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 1 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1919
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1922): SAS `if not prxmatch("/[A-Z]\d\d\d/",Plate_No) then 
      put "Plate number " Plate_No "does not conform to pattern"` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1919_compute_1_nulls`, `vc_op_1919_compute_1_dates`, `vc_op_1919_compute_1_numeric`

### 487. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `s1919` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1919`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `op_1919_compute_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_op_1919_write_file_1_row_count`

### 488. Leer archivo externo

- **Acción:** add_component · **Componente:** `tFileInputDelimited` ![Icono Talend](assets/talend-icons/tFileInputDelimited_icon32.png) (sin verificar) · alternativas: `tFileInputPositional`, `tFileInputExcel`
- **Subjob:** `s1935` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1939`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileinputdelimited-standard-properties) · variantes: `tFileInputARFF`, `tFileInputExcel`, `tFileInputFullRow`, `tFileInputJSON`, `tFileInputLDIF`, `tFileInputMail`, `tFileInputPositional`, `tFileInputProperties`
- **Conexiones:** OnSubjobOk desde `op_1919_write_file_1`
- **Propiedades:**
  - `FILENAME` (File name/Stream) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `HEADER` (Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta del archivo, delimitador y codificación
  - Esquema (ancho fijo o delimitado)
- **Pruebas:** `vc_op_1939_read_file_1_row_count`, `vc_op_1939_read_file_1_nulls`

### 489. Datos incrustados (datalines)

- **Acción:** add_component · **Componente:** `tFixedFlowInput` ![Icono Talend](assets/talend-icons/tFixedFlowInput_icon32.png) (sin verificar)
- **Subjob:** `s1935` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1935`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput-standard-properties)
- **Propiedades:**
  - `VALUES` (Values) = _por configurar_ — regla mappings · nombre oficial
- **Supuestos:** Datos incrustados en el programa
- **Pendientes:**
  - Confirmar los datos incrustados
- **Pruebas:** `vc_op_1935_inline_data_1_row_count`

### 490. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s1935` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1935`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_1939_read_file_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `0 asignaciones, 2 condicionales` — SAS real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1935
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Expresión** (línea 1938): SAS `if _n_ = 1 then Return = prxparse("/\d\d\d\.\d\d\d\.\d\d\d\d/")` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Expresión** (línea 1940): SAS `if not prxmatch(Return,Phone) then 
      put "Phone number " Phone "does not conform to pattern"` → _sin traducción automática_
  - ⚠ Condicional IF/ELSE: traducir a expresión ternaria o bloque de tMap/tJavaRow
- **Supuestos:** Lógica condicional: revisar orden de evaluación y valores missing
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_1935_compute_1_nulls`, `vc_op_1935_compute_1_dates`, `vc_op_1935_compute_1_numeric`

### 491. Lógica con estado entre filas (RETAIN/FIRST./LAST./ARRAY/hash)

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tSortRow + tAggregateRow`, `tJavaRow`, `tMap con variables`
- **Subjob:** `s1935` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1935`
- **Conexiones:** Main desde `op_1935_compute_1`
- **Supuestos:** Estado entre filas: no hay traducción directa a un componente; requiere diseño manual
- **Pendientes:**
  - Diseño manual de la lógica con estado entre filas (RETAIN/FIRST./LAST.)
- **Pruebas:** `vc_op_1935_stateful_1_ordering`, `vc_op_1935_stateful_1_duplicates`

### 492. Escribir archivo externo

- **Acción:** add_component · **Componente:** `tFileOutputDelimited` ![Icono Talend](assets/talend-icons/tFileOutputDelimited_icon32.png) (sin verificar) · alternativas: `tFileOutputPositional`, `tFileOutputExcel`
- **Subjob:** `s1935` · **Confianza:** medium · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1935`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/delimited/tfileoutputdelimited-standard-properties) · variantes: `tFileOutputARFF`, `tFileOutputExcel`, `tFileOutputJSON`, `tFileOutputLDIF`, `tFileOutputPositional`, `tFileOutputProperties`, `tFileOutputRaw`, `tFileOutputXML`
- **Conexiones:** Main desde `op_1935_stateful_1`
- **Propiedades:**
  - `FILENAME` (File Name) = _por configurar_ — regla mappings · nombre oficial
  - `FIELDSEPARATOR` (Field Separator) = _por configurar_ — regla mappings · nombre oficial
  - `INCLUDEHEADER` (Include Header) = _por configurar_ — regla mappings · nombre oficial
  - `ENCODING` (Encoding) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Ruta y formato del archivo de salida
- **Pruebas:** `vc_op_1935_write_file_1_row_count`

## Definición de macro auxiliar `%print_n`(dsn, nobs)

### 1. Salida de reporte

- **Acción:** manual_decision · **Componente:** `ninguno` (sin verificar) · alternativas: `tLogRow`, `tFileOutputDelimited`
- **Subjob:** `m:print_n:s1767` · **Confianza:** low · **Origen SAS:** `real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1767`
- **Supuestos:** Salida de reporte: decidir si se migra
- **Pendientes:**
  - Decidir si el reporte se migra o se descarta

## Sin resolver

- dataset_dynamic &dsn (real/learning-sas-by-example/Example_code/Solutions_to_Odd_Numbered_problems.sas:1767) — nombre de dataset con macrovariables

## Casos de validación

- `vc_op_53_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_53_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_52_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_52_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_52_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_52_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_52_write_1_schema` (schema): Esquema destino
- `vc_op_63_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_63_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_75_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_75_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_74_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_74_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_74_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_74_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_74_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_74_write_1_schema` (schema): Esquema destino
- `vc_op_128_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_128_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_127_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_127_write_1_schema` (schema): Esquema destino
- `vc_op_144_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_144_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_143_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_143_write_1_schema` (schema): Esquema destino
- `vc_op_158_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_158_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_157_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_157_write_1_schema` (schema): Esquema destino
- `vc_op_178_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_178_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_177_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_177_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_177_write_1_schema` (schema): Esquema destino
- `vc_op_201_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_201_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_200_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_200_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_200_write_1_schema` (schema): Esquema destino
- `vc_op_217_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_217_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_222_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_237_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_237_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_236_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_236_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_236_write_1_schema` (schema): Esquema destino
- `vc_op_262_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_262_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_268_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_268_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_267_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_267_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_267_write_1_schema` (schema): Esquema destino
- `vc_op_272_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_280_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_280_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_294_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_321_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_321_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_320_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_320_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_320_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_320_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_320_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_320_write_1_schema` (schema): Esquema destino
- `vc_op_354_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_354_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_354_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_354_write_1_schema` (schema): Esquema destino
- `vc_op_381_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_381_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_380_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_380_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_380_write_1_schema` (schema): Esquema destino
- `vc_op_400_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_400_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_400_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_400_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_400_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_400_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_400_write_1_schema` (schema): Esquema destino
- `vc_op_422_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_422_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_421_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_421_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_421_write_1_schema` (schema): Esquema destino
- `vc_op_436_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_436_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_436_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_436_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_436_write_1_schema` (schema): Esquema destino
- `vc_op_448_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_448_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_448_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_448_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_448_write_1_schema` (schema): Esquema destino
- `vc_op_463_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_463_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_461_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_461_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_461_write_1_schema` (schema): Esquema destino
- `vc_op_479_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_479_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_475_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_475_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_475_write_1_schema` (schema): Esquema destino
- `vc_op_496_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_496_write_1_schema` (schema): Esquema destino
- `vc_op_513_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_513_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_512_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_512_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_512_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_512_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_512_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_512_write_1_schema` (schema): Esquema destino
- `vc_op_530_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_530_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_529_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_529_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_529_write_1_schema` (schema): Esquema destino
- `vc_op_546_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_546_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_546_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_546_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_546_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_546_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_546_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_546_write_1_schema` (schema): Esquema destino
- `vc_op_553_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_564_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_564_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_578_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_578_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_577_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_577_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_577_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_577_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_577_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_577_write_1_schema` (schema): Esquema destino
- `vc_op_593_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_593_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_593_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_593_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_593_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_593_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_593_write_1_schema` (schema): Esquema destino
- `vc_op_603_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_603_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_603_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_603_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_603_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_603_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_603_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_603_write_1_schema` (schema): Esquema destino
- `vc_op_614_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_614_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_616_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_616_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_616_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_614_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_614_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_614_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_614_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_614_write_1_schema` (schema): Esquema destino
- `vc_op_624_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_624_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_627_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_627_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_627_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_624_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_624_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_624_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_624_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_624_write_1_schema` (schema): Esquema destino
- `vc_op_635_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_635_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_637_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_637_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_637_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_635_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_635_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_635_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_635_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_635_write_1_schema` (schema): Esquema destino
- `vc_op_635_write_2_row_count` (row_count): Filas escritas iguales
- `vc_op_635_write_2_schema` (schema): Esquema destino
- `vc_op_662_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_662_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_662_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_662_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_662_union_1_row_count` (row_count): Suma de filas de las entradas (UNION sin ALL elimina duplicados)
- `vc_op_662_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_662_write_1_schema` (schema): Esquema destino
- `vc_op_666_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_666_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_666_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_666_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_666_write_1_schema` (schema): Esquema destino
- `vc_op_675_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_675_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_681_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_681_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_681_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_681_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_681_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_681_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_681_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_681_write_1_schema` (schema): Esquema destino
- `vc_op_693_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_693_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_693_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_693_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_693_write_1_schema` (schema): Esquema destino
- `vc_op_697_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_697_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_697_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_697_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_697_write_1_schema` (schema): Esquema destino
- `vc_op_701_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_701_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_701_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_701_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_701_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_701_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_701_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_701_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_701_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_701_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_701_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_701_write_1_schema` (schema): Esquema destino
- `vc_op_716_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_716_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_716_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_716_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_716_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_716_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_716_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_716_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_716_write_1_schema` (schema): Esquema destino
- `vc_op_725_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_725_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_725_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_725_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_725_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_725_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_725_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_725_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_725_write_1_schema` (schema): Esquema destino
- `vc_op_734_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_734_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_734_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_734_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_734_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_734_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_734_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_734_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_734_write_1_schema` (schema): Esquema destino
- `vc_op_745_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_745_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_745_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_745_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_745_write_1_schema` (schema): Esquema destino
- `vc_op_749_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_749_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_749_rename_1_schema` (schema): Nombres de columna finales
- `vc_op_749_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_749_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_749_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_749_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_749_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_749_write_1_schema` (schema): Esquema destino
- `vc_op_755_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_755_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_755_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_755_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_755_write_1_schema` (schema): Esquema destino
- `vc_op_759_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_759_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_759_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_759_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_759_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_759_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_759_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_759_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_759_write_1_schema` (schema): Esquema destino
- `vc_op_771_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_771_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_771_rename_1_schema` (schema): Nombres de columna finales
- `vc_op_771_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_771_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_771_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_771_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_771_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_771_write_1_schema` (schema): Esquema destino
- `vc_op_777_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_777_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_777_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_777_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_777_write_1_schema` (schema): Esquema destino
- `vc_op_781_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_781_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_781_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_781_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_781_write_1_schema` (schema): Esquema destino
- `vc_op_785_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_785_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_785_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_785_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_785_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_785_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_785_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_785_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_785_write_1_schema` (schema): Esquema destino
- `vc_op_796_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_796_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_796_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_796_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_796_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_796_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_796_write_1_schema` (schema): Esquema destino
- `vc_op_810_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_810_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_810_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_810_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_810_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_810_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_810_write_1_schema` (schema): Esquema destino
- `vc_op_820_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_820_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_820_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_820_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_820_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_820_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_820_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_820_write_1_schema` (schema): Esquema destino
- `vc_op_837_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_837_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_837_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_846_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_846_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_846_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_846_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_846_write_1_schema` (schema): Esquema destino
- `vc_op_856_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_856_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_865_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_865_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_865_rename_1_schema` (schema): Nombres de columna finales
- `vc_op_865_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_865_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_865_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_865_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_865_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_865_write_1_schema` (schema): Esquema destino
- `vc_op_883_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_883_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_883_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_883_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_883_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_883_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_883_write_1_schema` (schema): Esquema destino
- `vc_op_902_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_902_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_902_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_902_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_902_write_1_schema` (schema): Esquema destino
- `vc_op_936_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_936_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_936_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_936_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_936_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_936_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_936_write_1_schema` (schema): Esquema destino
- `vc_op_947_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_947_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_947_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_947_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_947_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_947_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_947_select_columns_2_schema` (schema): Solo las columnas esperadas
- `vc_op_947_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_947_write_1_schema` (schema): Esquema destino
- `vc_op_964_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_964_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_964_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_964_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_964_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_964_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_964_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_964_write_1_schema` (schema): Esquema destino
- `vc_op_975_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_975_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_975_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_975_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_975_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_975_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_975_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_975_write_1_schema` (schema): Esquema destino
- `vc_op_986_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_986_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_988_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_988_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_988_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_986_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_986_write_1_schema` (schema): Esquema destino
- `vc_op_1003_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1003_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1003_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1003_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1003_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1003_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1003_write_1_schema` (schema): Esquema destino
- `vc_op_1003_write_2_row_count` (row_count): Filas escritas iguales
- `vc_op_1003_write_2_schema` (schema): Esquema destino
- `vc_op_1021_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1021_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1021_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1021_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1021_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1021_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1021_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1021_write_1_schema` (schema): Esquema destino
- `vc_op_1032_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1032_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1032_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1032_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1032_write_1_schema` (schema): Esquema destino
- `vc_op_1043_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1043_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1043_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1043_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1043_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1043_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1043_write_1_schema` (schema): Esquema destino
- `vc_op_1057_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1057_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1057_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1057_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1057_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1057_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1057_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1057_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1057_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1057_write_1_schema` (schema): Esquema destino
- `vc_op_1076_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1076_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1072_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1072_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1072_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1072_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1072_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1072_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1072_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1072_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1072_write_1_schema` (schema): Esquema destino
- `vc_op_1212_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1212_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1224_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1224_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1224_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_1224_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1224_write_1_schema` (schema): Esquema destino
- `vc_op_1230_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1230_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1242_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1242_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1254_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1262_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1262_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1272_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1272_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1279_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1279_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1279_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1279_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1279_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1279_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1279_select_columns_2_schema` (schema): Solo las columnas esperadas
- `vc_op_1279_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1279_write_1_schema` (schema): Esquema destino
- `vc_op_1279_select_columns_3_schema` (schema): Solo las columnas esperadas
- `vc_op_1279_write_2_row_count` (row_count): Filas escritas iguales
- `vc_op_1279_write_2_schema` (schema): Esquema destino
- `vc_op_1279_select_columns_4_schema` (schema): Solo las columnas esperadas
- `vc_op_1279_write_3_row_count` (row_count): Filas escritas iguales
- `vc_op_1279_write_3_schema` (schema): Esquema destino
- `vc_op_1279_write_4_row_count` (row_count): Filas escritas iguales
- `vc_op_1279_write_4_schema` (schema): Esquema destino
- `vc_op_1309_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1309_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1314_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1322_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1322_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1329_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1329_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1335_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1341_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1341_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1348_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1348_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1355_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1355_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1363_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1368_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1368_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1379_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1379_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1394_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1394_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1410_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1414_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1414_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1414_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_1414_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1414_write_1_schema` (schema): Esquema destino
- `vc_op_1417_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1417_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1438_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1438_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1454_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1454_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1463_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1463_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1469_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1469_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1512_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1512_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1511_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1511_write_1_schema` (schema): Esquema destino
- `vc_op_1523_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1523_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1522_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1522_write_1_schema` (schema): Esquema destino
- `vc_op_1535_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1535_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1535_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1535_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1535_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1535_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1535_write_1_schema` (schema): Esquema destino
- `vc_op_1535_write_file_1_row_count` (row_count): Mismas filas
- `vc_op_1548_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1548_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1547_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1547_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1547_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1547_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1547_write_1_schema` (schema): Esquema destino
- `vc_op_1561_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1561_write_1_schema` (schema): Esquema destino
- `vc_op_1574_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1574_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1573_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1573_write_1_schema` (schema): Esquema destino
- `vc_op_1585_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1593_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1593_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1600_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1606_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1606_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1606_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1606_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1606_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1606_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1606_write_1_schema` (schema): Esquema destino
- `vc_op_1617_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1627_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1627_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1626_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1626_write_1_schema` (schema): Esquema destino
- `vc_op_1636_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1636_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1636_rename_1_schema` (schema): Nombres de columna finales
- `vc_op_1636_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1636_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1636_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1636_write_1_schema` (schema): Esquema destino
- `vc_op_1642_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1647_format_definition_1_schema` (schema): Valores formateados iguales para todo el rango
- `vc_op_1660_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1660_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1660_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1660_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1660_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1660_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1660_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1660_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1660_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1660_write_1_schema` (schema): Esquema destino
- `vc_op_1689_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1689_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1689_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_1689_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1689_write_1_schema` (schema): Esquema destino
- `vc_op_1692_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1692_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1695_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_1695_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_1695_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_1692_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1692_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1692_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1692_write_1_schema` (schema): Esquema destino
- `vc_op_1703_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1703_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1703_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_1703_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1703_write_1_schema` (schema): Esquema destino
- `vc_op_1706_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1706_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1711_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_1711_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_1711_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_1706_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1706_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1706_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1706_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1706_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1706_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1706_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1706_write_1_schema` (schema): Esquema destino
- `vc_op_1720_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1720_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1720_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_1720_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1720_write_1_schema` (schema): Esquema destino
- `vc_op_1723_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1723_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1723_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1723_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1723_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1723_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1723_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1723_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1723_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1723_write_1_schema` (schema): Esquema destino
- `vc_op_1741_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1741_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1741_sort_1_ordering` (ordering): Solo si el orden forma parte del contrato; SAS ordena missing primero
- `vc_op_1741_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1741_write_1_schema` (schema): Esquema destino
- `vc_op_1744_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1744_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1744_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1744_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1744_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1744_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1744_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1744_select_columns_1_schema` (schema): Solo las columnas esperadas
- `vc_op_1744_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1744_write_1_schema` (schema): Esquema destino
- `vc_op_1774_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1774_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1780_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1780_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1787_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1787_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1787_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1787_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1787_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1787_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1787_write_1_schema` (schema): Esquema destino
- `vc_op_1801_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1801_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1801_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_1801_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_1801_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_1801_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_1808_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1808_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1808_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_op_1808_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_op_1808_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_op_1808_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_1808_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1808_write_1_schema` (schema): Esquema destino
- `vc_op_1821_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1821_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1821_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1821_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1821_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_1821_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_1821_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_1821_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_1821_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1821_write_1_schema` (schema): Esquema destino
- `vc_op_1856_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1856_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1856_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1856_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1856_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_1856_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_1856_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_1856_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_1856_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1856_write_1_schema` (schema): Esquema destino
- `vc_op_1873_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1873_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1873_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1873_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1873_join_1_duplicates` (duplicates): Claves duplicadas en ambos lados (MERGE y JOIN difieren)
- `vc_op_1873_join_1_row_count` (row_count): Filas sin pareja en cada lado
- `vc_op_1873_join_1_nulls` (nulls): Claves nulas no deben emparejarse (o sí, según SAS)
- `vc_op_1873_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_1873_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1873_write_1_schema` (schema): Esquema destino
- `vc_op_1890_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1890_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1890_read_2_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1890_read_2_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1890_union_1_row_count` (row_count): Suma de filas de las entradas (UNION sin ALL elimina duplicados)
- `vc_op_1890_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_1890_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1890_write_1_schema` (schema): Esquema destino
- `vc_op_1903_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_1903_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_1903_aggregate_1_aggregates` (aggregates): Sumas, conteos y promedios por grupo iguales; AVG/SUM ignoran missing en SAS
- `vc_op_1903_aggregate_1_numeric` (numeric): Tolerancia numérica y redondeo
- `vc_op_1903_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_1903_write_1_schema` (schema): Esquema destino
- `vc_op_1921_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1921_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1919_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1919_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1919_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1919_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1919_write_file_1_row_count` (row_count): Mismas filas
- `vc_op_1939_read_file_1_row_count` (row_count): Mismas filas leídas, incluidas filas inválidas
- `vc_op_1939_read_file_1_nulls` (nulls): Campos vacíos y missing se cargan igual que en SAS
- `vc_op_1935_inline_data_1_row_count` (row_count): Mismas filas
- `vc_op_1935_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_1935_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_1935_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_1935_stateful_1_ordering` (ordering): Resultado depende del orden de entrada: probar con datos desordenados y con claves repetidas
- `vc_op_1935_stateful_1_duplicates` (duplicates): Grupos de una sola fila y de muchas filas
- `vc_op_1935_write_file_1_row_count` (row_count): Mismas filas

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
