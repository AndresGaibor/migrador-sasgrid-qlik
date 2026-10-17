# Job `job_p1_macro_parametrizada`

- **Programa SAS:** `p1_macro_parametrizada.sas` (sha256 `527e5bc7c423`)
- **Estado:** needs_review · **Pasos:** 5 · **Reglas:** v1
- **Aviso:** componentes y propiedades son candidatos; ninguno está verificado contra Talend salvo marca explícita.

## Pasos

### 1. Invocar macro %extraer_mes

- **Acción:** add_component · **Componente:** `tRunJob` (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s13` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:13`
- **Propiedades (nombres candidatos):**
  - `PROCESS` = `extraer_mes` — SAS p1_macro_parametrizada.sas:13
  - `CONTEXT_PARAMS` = `tabla=ventas, desde=1, hasta=12` — SAS p1_macro_parametrizada.sas:13
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %extraer_mes (definida en p1_macro_parametrizada.sas)

## Job hijo / joblet para `%extraer_mes`(tabla, desde, hasta)

### 1. Leer dwh.&tabla.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:extraer_mes:s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Propiedades (nombres candidatos):**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:extraer_mes:op_6_read_1_row_count`, `vc_m:extraer_mes:op_6_read_1_schema`

### 2. Filtrar filas (WHERE): month(fecha) = &m.

- **Acción:** add_component · **Componente:** `tFilterRow` (sin verificar) · alternativas: `tMap`
- **Subjob:** `m:extraer_mes:s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Conexiones:** Main desde `m:extraer_mes:op_6_read_1`
- **Propiedades (nombres candidatos):**
  - `LOGICAL_OP` = _por configurar_ — regla mappings
  - `CONDITIONS` = _por configurar_ — regla mappings
  - `USE_ADVANCED` = _por configurar_ — regla mappings
  - `ADVANCED_COND` = _por configurar_ — regla mappings
- **Expresión** (línea 6): SAS `month(fecha) = &m.` → _sin traducción automática_
  - ⚠ Sin traducción automática: función month
- **Pendientes:**
  - Traducir la condición manualmente (no hay traducción automática segura)
- **Pruebas:** `vc_m:extraer_mes:op_6_filter_1_row_count`, `vc_m:extraer_mes:op_6_filter_1_nulls`, `vc_m:extraer_mes:op_6_filter_1_empty`

### 3. Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` (sin verificar)
- **Subjob:** `m:extraer_mes:s5` · **Estado:** propuesto · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Conexiones:** Main desde `m:extraer_mes:op_6_filter_1`
- **Propiedades (nombres candidatos):**
  - `Output columns` = `*` — SAS p1_macro_parametrizada.sas:6
  - `Expressions` = _por configurar_ — regla mappings
- **Pruebas:** `vc_m:extraer_mes:op_6_project_1_schema`

### 4. Escribir work.&tabla._&mm. (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:extraer_mes:s5` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Conexiones:** Main desde `m:extraer_mes:op_6_project_1`
- **Propiedades (nombres candidatos):**
  - `TABLE` = _por configurar_ — regla mappings
  - `ACTION_ON_TABLE` = _por configurar_ — regla mappings
  - `ACTION_ON_DATA` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
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
