# Job `job_p1_macro_parametrizada`

- **Programa SAS:** `p1_macro_parametrizada.sas` (sha256 `2b04d3a17bfa`)
- **Instrucciones:** 4 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.m` ← SAS `m` (&m en p1_macro_parametrizada.sas:6)

## Conexiones a crear

- `dwh` (BASE, /data/dwh) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer dwh.&tabla.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`
- **Subjob:** `m:extraer_mes:s5` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería dwh es de tipo BASE en /data/dwh: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo
- **Pruebas:** `vc_m:extraer_mes:op_6_read_1_row_count`, `vc_m:extraer_mes:op_6_read_1_schema`

### 2. Transformar en un solo tMap: Filtrar filas (WHERE): month(fecha) = &m.; Seleccionar/calcular columnas

- **Acción:** add_component · **Componente:** `tMap` ![Icono Talend](/talend-icons/tMap_icon32.png) (sin verificar)
- **Subjob:** `m:extraer_mes:s5` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tmap/tmap-standard-properties)
- **Conexiones:** Main desde `m:extraer_mes:op_6_read_1`
- **Propiedades:**
  - `Output filter` = `(((input_row.fecha == null ? null : TalendDate.getPartOfDate("MONTH", input_row.fecha)) == context.m))` — SAS fusionado
  - `Output columns` = `*` — SAS fusionado
- **Esquema:** `fecha` _(tipos por determinar)_
- **Expresión** (línea 6): SAS `month(fecha) = &m.` → Java `((input_row.fecha == null ? null : TalendDate.getPartOfDate("MONTH", input_row.fecha)) == context.m)`
  - ⚠ Filtro de salida del tMap: Macrovariable &m → context.m (crear variable de contexto)
  - ⚠ Filtro de salida del tMap: year/month/day(): sobre un Date de Talend; con fecha SAS numérica validar la conversión de época
- **Pruebas:** `vc_m:extraer_mes:op_6_filter_1_row_count`, `vc_m:extraer_mes:op_6_filter_1_nulls`, `vc_m:extraer_mes:op_6_filter_1_empty`, `vc_m:extraer_mes:op_6_project_1_schema`

### 3. Escribir work.&tabla._&mm. (reemplaza)

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`
- **Subjob:** `m:extraer_mes:s5` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Conexiones:** Main desde `m:extraer_mes:tmap_op_6_filter_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p1_macro_parametrizada.sas:6
  - `DATA_ACTION` = `INSERT` — SAS p1_macro_parametrizada.sas:6
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
- **Pruebas:** `vc_m:extraer_mes:op_6_write_1_row_count`, `vc_m:extraer_mes:op_6_write_1_schema`

### 5. Detiene el Job ante un error de componente

- **Acción:** add_component · **Componente:** `tDie` ![Icono Talend](/talend-icons/tDie_icon32.png) (sin verificar)
- **Subjob:** `recomendado` · **Confianza:** high · **Origen SAS:** `p1_macro_parametrizada.sas:6`
- **Conexiones:** OnComponentError desde `m:extraer_mes:op_6_write_1`

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
