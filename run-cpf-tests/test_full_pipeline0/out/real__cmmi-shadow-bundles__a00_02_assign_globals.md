# Job `job_a00_02_assign_globals`

- **Programa SAS:** `real/cmmi-shadow-bundles/a00_02_assign_globals.sas` (sha256 `784bbb044b7c`)
- **Instrucciones:** 1 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.log_path` ← SAS `log_path` (&log_path en real/cmmi-shadow-bundles/a00_02_assign_globals.sas:123)

## Pasos

## Definición de macro auxiliar `%a00_02_assign_globals`()

### 1. Invocar macro %mkdirs

- **Acción:** add_component · **Componente:** `tRunJob` ![Icono Talend](assets/talend-icons/tRunJob_icon32.png) (sin verificar) · alternativas: `Joblet`
- **Subjob:** `m:a00_02_assign_globals:s123` · **Confianza:** high · **Origen SAS:** `real/cmmi-shadow-bundles/a00_02_assign_globals.sas:123`
- **Referencia:** [documentación](https://help.qlik.com/talend/en-US/components/8.0/orchestration/trunjob-standard-properties)
- **Propiedades:**
  - `PROCESS` (Job) = `mkdirs` — SAS real/cmmi-shadow-bundles/a00_02_assign_globals.sas:123 · nombre oficial
  - `CONTEXTPARAMS` (Context Param) = `&log_path.` — SAS real/cmmi-shadow-bundles/a00_02_assign_globals.sas:123 · nombre oficial
- **Pendientes:**
  - Job o joblet hijo que implementa la macro
  - Crear/identificar el Job hijo para %mkdirs (definida en real/cmmi-shadow-bundles/a00_01_utility_macros.sas)

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
