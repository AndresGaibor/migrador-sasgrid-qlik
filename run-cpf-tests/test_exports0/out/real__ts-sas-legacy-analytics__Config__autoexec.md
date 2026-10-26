# Job `job_autoexec`

- **Programa SAS:** `real/ts-sas-legacy-analytics/Config/autoexec.sas` (sha256 `9f1f13cd17b3`)
- **Instrucciones:** 0 · **Reglas:** v1
- **Aviso:** los esquemas y propiedades son candidatos derivados de fuentes comunitarias. El enlace oficial solo acredita la referencia documental; `verificado` requiere contraste con un Job real.

## Variables de contexto

- `context.ABORT_ON_ERR` ← SAS `ABORT_ON_ERR` = `Y` (%LET de primer nivel)
- `context.ARCHIVE_PATH` ← SAS `ARCHIVE_PATH` = `/data/sas/archive` (%LET de primer nivel)
- `context.BASE_PATH` ← SAS `BASE_PATH` = `/data/sas` (%LET de primer nivel)
- `context.CURR_DT` ← SAS `CURR_DT` = `%sysfunc(today(), date9.)` (%LET de primer nivel)
- `context.CURR_YM` ← SAS `CURR_YM` = `%sysfunc(today(), yymmn6.)` (%LET de primer nivel)
- `context.EMAIL_DL` ← SAS `EMAIL_DL` = `sas-ops@corp.internal` (%LET de primer nivel)
- `context.EMAIL_ONCALL` ← SAS `EMAIL_ONCALL` = `oncall-data@corp.internal` (%LET de primer nivel)
- `context.ENVIRONMENT` ← SAS `ENVIRONMENT` = `PROD` (%LET de primer nivel)
- `context.FY_START` ← SAS `FY_START` = `%sysfunc(intnx(year, %sysfunc(today()), 0, B), date9.)` (%LET de primer nivel)
- `context.LOG_PATH` ← SAS `LOG_PATH` = `/data/sas/logs` (%LET de primer nivel)
- `context.MAX_OBS_WARN` ← SAS `MAX_OBS_WARN` = `10000000` (%LET de primer nivel)
- `context.PREV_YM` ← SAS `PREV_YM` = `%sysfunc(intnx(month, %sysfunc(today()), -1), yymmn6.)` (%LET de primer nivel)
- `context.REPORT_PATH` ← SAS `REPORT_PATH` = `/data/sas/reports/output` (%LET de primer nivel)

## Pasos

# Checklist de equivalencia SAS vs Talend

- [ ] Conteo de registros
- [ ] Esquema y tipos
- [ ] Missing / nulos
- [ ] Duplicados y claves
- [ ] Numéricos y fechas
- [ ] Orden (solo si es parte del contrato)
- [ ] Agregaciones, joins y filtros
- [ ] Datos vacíos o inválidos
