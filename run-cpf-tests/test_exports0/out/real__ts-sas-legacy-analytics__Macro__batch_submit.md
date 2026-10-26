# Job `job_batch_submit`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Macro/batch_submit.sas` (sha256 `709c781094e4`)
- **Instrucciones:** 4 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.config` ← SAS `config` (&config en real/ts-sas-legacy-analytics/Macro/batch_submit.sas:169)
- `context.file` ← SAS `file` (&file en real/ts-sas-legacy-analytics/Macro/batch_submit.sas:169)
- `context.log` ← SAS `log` (&log en real/ts-sas-legacy-analytics/Macro/batch_submit.sas:173)
- `context.lst` ← SAS `lst` (&lst en real/ts-sas-legacy-analytics/Macro/batch_submit.sas:173)
- `context.path` ← SAS `path` (&path en real/ts-sas-legacy-analytics/Macro/batch_submit.sas:173)
- `context.sas` ← SAS `sas` (&sas en real/ts-sas-legacy-analytics/Macro/batch_submit.sas:169)

## Pasos

## Definición de macro auxiliar `%batch_submit`(FILE, CONFIG)

### 1. Invocar macro %dump_mvars

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:batch_submit:s168` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/batch_submit.sas:168`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `dump_mvars` — SAS real/ts-sas-legacy-analytics/Macro/batch_submit.sas:168 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `sas file path config` — SAS real/ts-sas-legacy-analytics/Macro/batch_submit.sas:168 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %dump_mvars (definida en real/ts-sas-legacy-analytics/Macro/batch_submit.sas)

### 2. Comando del sistema operativo

- **Acción:** add_component · **Componente:** `tSystem` ![Icono Talend](assets/talend-icons/tSystem_icon32.png) (sin verificar)
- **Subjob:** `m:batch_submit:s169` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/batch_submit.sas:169`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/system/tsystem)
- **Conexiones:** OnSubjobOk desde `m:batch_submit:op_168_macro_call_1`
- **Propiedades:**
  - `COMMAND` (Command) = `systask command " ""&sas"" -config ""&config"" -sysin ""&file"" " nowait` — SAS real/ts-sas-legacy-analytics/Macro/batch_submit.sas:169 · nombre oficial
- **Supuestos:** Comando del SO: mover a orquestación
- **Pendientes:**
  - Moverlo a la orquestación o confirmar necesidad

### 3. Invocar macro %dump_mvars

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:batch_submit:s172` · **Confianza:** high · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/batch_submit.sas:172`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Conexiones:** OnSubjobOk desde `m:batch_submit:op_169_os_command_1`
- **Propiedades:**
  - `PROCESS` (Job) = `dump_mvars` — SAS real/ts-sas-legacy-analytics/Macro/batch_submit.sas:172 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `sas file path log lst` — SAS real/ts-sas-legacy-analytics/Macro/batch_submit.sas:172 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %dump_mvars (definida en real/ts-sas-legacy-analytics/Macro/batch_submit.sas)

### 4. Comando del sistema operativo

- **Acción:** add_component · **Componente:** `tSystem` ![Icono Talend](assets/talend-icons/tSystem_icon32.png) (sin verificar)
- **Subjob:** `m:batch_submit:s173` · **Confianza:** low · **Origen SAS:** `real/ts-sas-legacy-analytics/Macro/batch_submit.sas:173`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/system/tsystem)
- **Conexiones:** OnSubjobOk desde `m:batch_submit:op_172_macro_call_1`
- **Propiedades:**
  - `COMMAND` (Command) = `systask command " ""&sas"" -sysin ""&file"" -log ""&log"" -print ""&lst"" -sasinitialfolder ""&path"" " nowait` — SAS real/ts-sas-legacy-analytics/Macro/batch_submit.sas:173 · nombre oficial
- **Supuestos:** Comando del SO: mover a orquestación
- **Pendientes:**
  - Moverlo a la orquestación o confirmar necesidad

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
