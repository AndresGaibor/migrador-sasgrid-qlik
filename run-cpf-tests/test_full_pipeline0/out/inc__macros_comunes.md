# Job `job_macros_comunes`

- **Programa SAS:** `inc/macros_comunes.sas` (sha256 `642b77561864`)
- **Instrucciones:** 2 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Pasos

## Definición de macro auxiliar `%limpiar_texto`(var)

## Definición de macro auxiliar `%cargar`(tabla, destino)

### 1. Leer dwh.&tabla.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `m:cargar:s7` · **Confianza:** high · **Origen SAS:** `inc/macros_comunes.sas:7`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
  - Librería o sistema de origen no determinable (nombre dinámico)
- **Pruebas:** `vc_m:cargar:op_7_read_1_row_count`, `vc_m:cargar:op_7_read_1_schema`

### 2. Escribir &destino..&tabla.

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `m:cargar:s7` · **Confianza:** high · **Origen SAS:** `inc/macros_comunes.sas:7`
- **Conexiones:** Main desde `m:cargar:op_7_read_1`
- **Propiedades:**
  - `TABLE` = _por configurar_ — regla mappings
  - `TABLE_ACTION` = `DROP_CREATE` — SAS inc/macros_comunes.sas:7
  - `DATA_ACTION` = `INSERT` — SAS inc/macros_comunes.sas:7
  - `CONNECTION` = _por configurar_ — regla mappings
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Librería o sistema de origen no determinable (nombre dinámico)
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_m:cargar:op_7_write_1_row_count`, `vc_m:cargar:op_7_write_1_schema`

## Sin resolver

- dataset_dynamic dwh.&tabla. (inc/macros_comunes.sas:7) — nombre de dataset con macrovariables
- dataset_dynamic &destino..&tabla. (inc/macros_comunes.sas:7) — nombre de dataset con macrovariables

## Casos de validación

- `vc_m:cargar:op_7_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_m:cargar:op_7_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_m:cargar:op_7_write_1_row_count` (row_count): Filas escritas iguales
- `vc_m:cargar:op_7_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
