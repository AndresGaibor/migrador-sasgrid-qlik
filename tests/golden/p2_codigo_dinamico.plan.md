# Job `job_p2_codigo_dinamico`

- **Programa SAS:** `p2_codigo_dinamico.sas` (sha256 `d7a2b64f8e9e`)
- **Estado:** needs_review · **Pasos:** 6 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.n` ← SAS `n` = `3` (%LET de primer nivel)
- `context.t1` ← SAS `t1` = `ventas` (%LET de primer nivel)
- `context.t2` ← SAS `t2` = `pagos` (%LET de primer nivel)
- `context.t3` ← SAS `t3` = `clientes` (%LET de primer nivel)

## Pasos

### 1. Leer work.tablas_a_procesar

- **Acción:** add_component · **Componente:** `por_determinar` (sin verificar) · alternativas: `tFileInputDelimited`, `tDBInput`
- **Subjob:** `s2` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p2_codigo_dinamico.sas:2`
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
- **Subjob:** `s2` · **Estado:** pendiente · **Confianza:** low · **Origen SAS:** `p2_codigo_dinamico.sas:4`
- **Conexiones:** Main desde `op_2_read_1`
- **Supuestos:** CALL EXECUTE: documentar el código que genera
- **Pendientes:**
  - Documentar el código que genera CALL EXECUTE y decidir diseño

### 3. Comando del sistema operativo

- **Acción:** add_component · **Componente:** `tSystem` ![Icono Talend](/talend-icons/tSystem_icon32.png) (sin verificar)
- **Subjob:** `s7` · **Estado:** pendiente · **Confianza:** low · **Origen SAS:** `p2_codigo_dinamico.sas:7`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tsystem)
- **Conexiones:** OnSubjobOk desde `op_4_dynamic_code_1`
- **Propiedades:**
  - `COMMAND` (Command) = `x 'cp /data/out/reporte.csv /archivo/historico/'` — SAS p2_codigo_dinamico.sas:7 · nombre oficial
- **Supuestos:** Comando del SO: mover a orquestación
- **Pendientes:**
  - Moverlo a la orquestación o confirmar necesidad

### 4. Comando del sistema operativo

- **Acción:** add_component · **Componente:** `tSystem` ![Icono Talend](/talend-icons/tSystem_icon32.png) (sin verificar)
- **Subjob:** `s8` · **Estado:** pendiente · **Confianza:** low · **Origen SAS:** `p2_codigo_dinamico.sas:8`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/tsystem)
- **Conexiones:** OnSubjobOk desde `op_7_os_command_1`
- **Propiedades:**
  - `COMMAND` (Command) = `systask command "gzip /data/out/reporte.csv" wait` — SAS p2_codigo_dinamico.sas:8 · nombre oficial
- **Supuestos:** Comando del SO: mover a orquestación
- **Pendientes:**
  - Moverlo a la orquestación o confirmar necesidad

### 5. Invocar macro %bucle

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `s17` · **Estado:** pendiente · **Confianza:** high · **Origen SAS:** `p2_codigo_dinamico.sas:17`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/trunjob)
- **Conexiones:** OnSubjobOk desde `op_8_os_command_1`
- **Propiedades:**
  - `PROCESS` (Job) = `bucle` — SAS p2_codigo_dinamico.sas:17 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = _por configurar_ — regla mappings · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %bucle (definida en p2_codigo_dinamico.sas)

## Job hijo / joblet para `%bucle`()

### 1. Mantenimiento de datasets

- **Acción:** add_component · **Componente:** `tDBRow` (sin verificar) · alternativas: `ninguno`
- **Subjob:** `m:bucle:s14` · **Estado:** pendiente · **Confianza:** low · **Origen SAS:** `p2_codigo_dinamico.sas:14`
- **Propiedades:**
  - `QUERY` = _por configurar_ — regla mappings
- **Pendientes:**
  - Decidir si la operación de mantenimiento aplica en el destino

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
