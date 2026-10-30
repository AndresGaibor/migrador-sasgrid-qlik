# Job `job_p2_codigo_dinamico`

- **Programa SAS:** `p2_codigo_dinamico.sas` (sha256 `d7a2b64f8e9e`)
- **Instrucciones:** 4 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Conexiones a crear

- `dwh` (BASE, /data/dwh) → por_determinar (metadatos de archivo o base de datos). Crear la conexión en Talend; no se copian credenciales

## Pasos

### 1. Leer work.tablas_a_procesar

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`
- **Subjob:** `s2` · **Confianza:** high · **Origen SAS:** `p2_codigo_dinamico.sas:2`
- **Propiedades:**
  - `TABLE` = `tablas_a_procesar` — SAS p2_codigo_dinamico.sas:2
  - `QUERY` = _por configurar_ — regla mappings
  - `CONNECTION` = _por configurar_ — regla mappings
- **Supuestos:** Dataset temporal (WORK): dentro del mismo subjob conviene una conexión Main; entre subjobs, tHashOutput/tHashInput o archivo temporal
- **Pendientes:**
  - Formato físico o sistema de origen del dataset
  - Esquema y tipos de columnas
- **Pruebas:** `vc_op_2_read_1_row_count`, `vc_op_2_read_1_schema`

### 2. Código generado dinámicamente

- **Acción:** manual_decision · **Componente:** `por_determinar` (sin verificar) · alternativas: `tRunJob con contexto`, `tFlowToIterate + tRunJob`
- **Subjob:** `s2` · **Confianza:** low · **Origen SAS:** `p2_codigo_dinamico.sas:4`
- **Conexiones:** Main desde `op_2_read_1`
- **Supuestos:** CALL EXECUTE: documentar el código que genera
- **Pendientes:**
  - Documentar el código que genera CALL EXECUTE y decidir diseño

### 3. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:bucle:s14` · **Confianza:** low · **Origen SAS:** `p2_codigo_dinamico.sas:14`
- **Conexiones:** OnSubjobOk desde `op_4_dynamic_code_1`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino
  - Librería dwh es de tipo BASE en /data/dwh: Talend no lee .sas7bdat directamente; confirmar si existe copia en base de datos o archivo

### 5. Detiene el Job ante un error de componente

- **Acción:** add_component · **Componente:** `tDie` ![Icono Talend](/talend-icons/tDie_icon32.png) (sin verificar)
- **Subjob:** `recomendado` · **Confianza:** high · **Origen SAS:** `p2_codigo_dinamico.sas:2`
- **Conexiones:** OnComponentError desde `m:bucle:op_14_maintenance_1`

## Sin resolver

- dataset_dynamic dwh.&&t&i. (p2_codigo_dinamico.sas:14) — nombre de dataset con macrovariables
- macro procesar (p2_codigo_dinamico.sas:4) — sin definición en el proyecto

## Casos de validación

- `vc_op_2_read_1_row_count` (row_count): Mismo número de filas leídas que en SAS
- `vc_op_2_read_1_schema` (schema): Mismos nombres y tipos de columna

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
