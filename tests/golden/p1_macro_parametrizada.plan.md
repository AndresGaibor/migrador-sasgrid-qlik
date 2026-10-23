# Job `job_p1_macro_parametrizada`

- **Programa SAS:** `p1_macro_parametrizada.sas` (sha256 `2b04d3a17bfa`)
- **Instrucciones:** 5 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Pasos

### 1. Invocar macro %extraer_mes

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s13` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:13`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/system/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `extraer_mes` — SAS p1_macro_parametrizada.sas:13 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `tabla=ventas, desde=1, hasta=12` — SAS p1_macro_parametrizada.sas:13 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %extraer_mes (definida en p1_macro_parametrizada.sas)

## Definición de macro auxiliar `%extraer_mes`(tabla, desde, hasta)

### 1. Leer dwh.&tabla.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:extraer_mes:s5` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:extraer_mes:op_6_read_1_row_count`, `vc_m:extraer_mes:op_6_read_1_schema`

### 2. Filtrar filas (WHERE): month(fecha) = &m.

- **Acción:** add_component · **Componente:** `tFilterRow` ![Icono Talend](/talend-icons/tFilterRow_icon32.png) (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:extraer_mes:s5` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/processing/tfilterrow-standard-properties)
- **Conexiones:** Main desde `m:extraer_mes:op_6_read_1`
- **Propiedades:**
  - `LOGICAL_OP` (Logical operator used to combine conditions) = _por configurar_ — regla mappings · nombre oficial · opciones: OR, AND
  - `CONDITIONS` (Conditions) = _por configurar_ — regla mappings · nombre oficial
  - `USE_ADVANCED` (Use advanced mode) = _por configurar_ — regla mappings · nombre oficial
  - `ADVANCED_COND` (Advanced) = _por configurar_ — regla mappings · nombre oficial
- **Expresión** (línea 6): SAS `month(fecha) = &m.` → _sin traducción automática_
  - ⚠ Sin traducción automática: función month
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:extraer_mes:op_6_filter_1_row_count`, `vc_m:extraer_mes:op_6_filter_1_nulls`, `vc_m:extraer_mes:op_6_filter_1_empty`

### 3. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:extraer_mes:s5` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:extraer_mes:op_6_filter_1`
- **Propiedades:**
  - `Output columns` (Editor del componente (no es un parámetro plano)) = `*` — SAS p1_macro_parametrizada.sas:6
  - `Expressions` (Editor del componente (no es un parámetro plano)) = _por configurar_ — regla mappings
- **Pruebas:** `vc_m:extraer_mes:op_6_project_1_schema`

### 4. Escribir work.&tabla._&mm. (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:extraer_mes:s5` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Conexiones:** Main desde `m:extraer_mes:op_6_project_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p1_macro_parametrizada.sas:6
  - `DATA_ACTION` = `INSERT` — SAS p1_macro_parametrizada.sas:6
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:extraer_mes:op_6_write_1_row_count`, `vc_m:extraer_mes:op_6_write_1_schema`

## Sin resolver

- dataset_dynamic dwh.&tabla. (p1_macro_parametrizada.sas:5) — nombre de dataset con macrovariables
- dataset_dynamic work.&tabla._&mm. (p1_macro_parametrizada.sas:5) — nombre de dataset con macrovariables

## Casos de validación

- `vc_m:extraer_mes:op_6_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:extraer_mes:op_6_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:extraer_mes:op_6_filter_1_row_count` (row_count): Filas que cumplen el filtro igual a SAS
- `vc_m:extraer_mes:op_6_filter_1_nulls` (nulls): Filas con valores missing en las columnas del filtro (SAS trata missing numérico como menor que cualquier número)
- `vc_m:extraer_mes:op_6_filter_1_empty` (empty): Entrada vacía produce salida vacía
- `vc_m:extraer_mes:op_6_project_1_schema` (schema): Columnas y tipos de salida
- `vc_m:extraer_mes:op_6_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:extraer_mes:op_6_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
