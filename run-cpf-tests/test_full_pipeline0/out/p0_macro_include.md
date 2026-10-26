# Job `job_p0_macro_include`

- **Programa SAS:** `p0_macro_include.sas` (sha256 `ff64d9348ed2`)
- **Instrucciones:** 3 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Orquestación

- Depende de (datos): `inc/macros_comunes.sas`

## Pasos

### 1. Invocar macro %cargar

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s5` · **Confianza:** high · **Origen SAS:** `p0_macro_include.sas:5`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `cargar` — SAS p0_macro_include.sas:5 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `clientes` — SAS p0_macro_include.sas:5 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %cargar (definida en inc/macros_comunes.sas)

### 2. Leer work.clientes

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s7` · **Confianza:** high · **Origen SAS:** `p0_macro_include.sas:7`
- **Conexiones:** OnSubjobOk desde `op_5_macro_call_1`
- **Propiedades:**
  - `TABLE` = `clientes` — SAS p0_macro_include.sas:7
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_7_read_1_row_count`, `vc_op_7_read_1_schema`

### 3. Escribir work.clientes_norm

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileOutputDelimited`, `tDBOutput`
- **Subjob:** `s7` · **Confianza:** high · **Origen SAS:** `p0_macro_include.sas:7`
- **Conexiones:** Main desde `op_7_read_1`
- **Propiedades:**
  - `TABLE` = `clientes_norm` — SAS p0_macro_include.sas:7
  - `TABLE_ACTION` = `DROP_CREATE` — SAS p0_macro_include.sas:7
  - `DATA_ACTION` = `INSERT` — SAS p0_macro_include.sas:7
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Sistema y tabla/archivo de destino
  - Confirmar la acción sobre la tabla: SAS reemplaza el dataset completo
- **Pruebas:** `vc_op_7_write_1_row_count`, `vc_op_7_write_1_schema`

## Casos de validación

- `vc_op_7_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_7_read_1_schema` (schema): Mismos nombres y tipos de columna
- `vc_op_7_write_1_row_count` (row_count): Filas escritas iguales
- `vc_op_7_write_1_schema` (schema): Esquema destino

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
