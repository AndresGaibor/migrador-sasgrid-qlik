# Job `job_createtableasselect`

- **Programa SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas` (sha256 `a074b8775d89`)
- **Instrucciones:** 13 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `mydblib` (BASE) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s25` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:25`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 2. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s26` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:26`
- **Conexiones:** OnSubjobOk desde `op_25_maintenance_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 3. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `s27` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:27`
- **Conexiones:** OnSubjobOk desde `op_26_maintenance_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

### 4. Calcular columnas (asignaciones y condicionales)

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar) · alternativas: `tJavaRow`
- **Subjob:** `s31` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:31`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** OnSubjobOk desde `op_27_maintenance_1`
- **Propiedades:**
  - `Expressions` (Editor del componente (no es un parámetro plano)) = `1 asignaciones, 0 condicionales` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:31
  - `Var table` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Esquema:** `ts` _(tipos por determinar)_
- **Expresión** (línea 33): SAS `datetime()` → _sin traducción automática_
  - ⚠ Sin traducción automática: función datetime
- **Pendientes:**
  - Tipos de las columnas calculadas
- **Pruebas:** `vc_op_31_compute_1_nulls`, `vc_op_31_compute_1_dates`, `vc_op_31_compute_1_numeric`

### 5. Escribir mydblib.ts_STRING

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s31` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:31`
- **Conexiones:** Main desde `op_31_compute_1`
- **Propiedades:**
  - `TABLE` = `ts_string` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:31
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:31
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:31
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería mydblib es de tipo BASE: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_31_write_1_row_count`, `vc_op_31_write_1_schema`

### 6. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s41` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:42`
- **Conexiones:** OnSubjobOk desde `op_31_write_1`
- **Supuestos:** SQL pass-through: el SQL se ejecuta en el motor externo
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 7. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s41` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:43`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_42_unsupported_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:43
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_op_43_project_1_schema`

### 8. Escribir mydblibsas (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s41` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:43`
- **Conexiones:** Main desde `op_43_project_1`
- **Propiedades:**
  - `TABLE` = `mydblibsas` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:43
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:43
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:43
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_43_write_1_row_count`, `vc_op_43_write_1_schema`

### 9. Leer mydblibsas

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s49` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:49`
- **Conexiones:** OnSubjobOk desde `op_43_write_1`
- **Propiedades:**
  - `TABLE` = `mydblibsas` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:49
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_43_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_49_read_1_row_count`, `vc_op_49_read_1_schema`

### 10. Lógica sin traducción definida

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar)
- **Subjob:** `s60` · **Confianza:** low · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:61`
- **Conexiones:** OnSubjobOk desde `op_49_read_1`
- **Supuestos:** SQL pass-through: el SQL se ejecuta en el motor externo
- **Pendientes:**
  - Documentar la lógica y decidir el diseño manualmente

### 11. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](assets/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `s60` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:62`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `op_61_unsupported_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:62
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_op_62_project_1_schema`

### 12. Escribir ysas (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s60` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:62`
- **Conexiones:** Main desde `op_62_project_1`
- **Propiedades:**
  - `TABLE` = `ysas` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:62
  - `TABLE_ACTION` = `DROP_CREATE` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:62
  - `DATA_ACTION` = `INSERT` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:62
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_62_write_1_row_count`, `vc_op_62_write_1_schema`

### 13. Leer ysas

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s68` · **Confianza:** high · **Origen SAS:** `real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:68`
- **Conexiones:** OnSubjobOk desde `op_62_write_1`
- **Propiedades:**
  - `TABLE` = `ysas` — SAS real/sas-access-samples/SAS_Foundation/Hadoop/createTableAsSelect.sas:68
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal; Dataset producido antes en este programa (op_62_write_1): puede sustituirse por una conexión directa o un tHashOutput
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_68_read_1_row_count`, `vc_op_68_read_1_schema`

## Casos de validación

- `vc_op_31_compute_1_nulls` (nulls): Cálculos con valores missing (SAS propaga missing en aritmética)
- `vc_op_31_compute_1_dates` (dates): Fechas calculadas (epoch 1960 vs 1970)
- `vc_op_31_compute_1_numeric` (numeric): Redondeo y precisión
- `vc_op_31_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_31_write_1_schema` (schema): Esquema destino
- `vc_op_43_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_43_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_43_write_1_schema` (schema): Esquema destino
- `vc_op_49_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_49_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_62_project_1_schema` (schema): Columnas y tipos de salida
- `vc_op_62_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_62_write_1_schema` (schema): Esquema destino
- `vc_op_68_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_68_read_1_schema` (schema): Mismos nombres y tipos de columna

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
