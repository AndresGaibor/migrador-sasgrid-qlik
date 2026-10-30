# Cobertura SAS

Clasificación definitiva en `rules/sas/`. Esta matriz se llena con el corpus real.

| Prioridad | Construcciones | Salida esperada |
| --------- | -------------- | --------------- |
| P0 | `LIBNAME`, `DATA`, `SET`, `KEEP`, `DROP`, `RENAME`, `WHERE`, `IF/THEN/ELSE`, `PROC SQL` (SELECT/JOIN/WHERE/GROUP BY), `PROC SORT`, `%LET`, `%MACRO`/`%MEND`, `%INCLUDE` estático | Instrucciones concretas y pruebas básicas si origen, destino y tipos están identificados |
| P1 | `MERGE ... BY`, `FIRST.`/`LAST.`, `RETAIN`, arrays, formatos/informats, funciones de fecha, missing, macros parametrizadas, joins con reglas particulares | Traducción propuesta con advertencias y casos de prueba específicos |
| P2 | `CALL EXECUTE`, código dinámico, `X`/`SYSTASK`, macros no resolubles, PROCs especializados, dependencias externas | Sin conversión automática: documentar lógica, datos faltantes y decisiones manuales |

## Fontanería y fusión

Qué se migra como paso y qué queda en `JobPlan.not_migrated` (detalle y ejemplos en
[pipeline-fusion.md](pipeline-fusion.md)):

- **Se funde en un `tMap`**: `WHERE`/`IF` (filtro de salida), cálculos, `RENAME`, `KEEP`/`DROP` y
  `PROC SQL` de proyección. Un `filter` o `select_columns` aislado conserva `tFilterRow` o
  `tFilterColumns`.
- **Deduplicado**: `PROC SORT NODUPKEY` y `NODUP` → `tUniqRow`. NODUPKEY usa la clave del `BY`; NODUP
  deja la clave pendiente.
- **No genera paso (fontanería)**: `x`/comandos del shell, `sleep`/`until`, `%put`, `datetime()`,
  borrado de WORK, troceo por lotes, espera, control de errores,
  conteos (`select count(*)`) y `call symputx` de un DATA step. Cada caso tiene su equivalente Talend
  en `not_migrated`.

## Corpus inicial (`tests/fixtures/sas/`)

No se encontró código SAS real en el host. El corpus es sintético, escrito para cubrir la matriz, salvo `p0_ejemplo_basico.sas` (de `qlikdojo`). Reemplazar/ampliar con programas reales anonimizados cuando existan. Cada archivo declara `priority: Px` en su primera línea.

| Fixture | Prioridad | Cubre |
| ------- | --------- | ----- |
| `p0_ejemplo_basico.sas` | P0 | DATA step con filtro/cálculo, PROC SQL group by |
| `p0_clientes_activos.sas` | P0 | LIBNAME, SET con RENAME, WHERE, IF/ELSE, KEEP/DROP, PROC SORT NODUPKEY |
| `p0_resumen_sql.sas` | P0 | `%LET`, PROC SQL inner/left join, group by, having `calculated` |
| `inc/macros_comunes.sas` + `p0_macro_include.sas` | P0 | `%MACRO` con posicional/clave, `%INCLUDE` estático |
| `p1_merge_first_last.sas` | P1 | PROC FORMAT, MERGE BY con `in=`, RETAIN, ARRAY, FIRST./LAST., missing, `intck`, `put` |
| `p1_macro_parametrizada.sas` | P1 | `%DO`, `%IF`, nombres de tabla generados por macro |
| `p2_codigo_dinamico.sas` | P2 | `CALL EXECUTE`, `X`, `SYSTASK`, `&&t&i.` |
| `grid/ejecutar_lote.sh` | P1 | Envío Grid con dependencias entre trabajos (opciones ilustrativas) |

## Corpus real (`tests/fixtures/sas/real/`)

50 programas de 6 repositorios públicos con licencia permisiva (ver `real/SOURCES.md`). Frecuencia de construcciones (archivos, de 50):

| Construcción | Archivos | Construcción | Archivos |
| ------------ | -------- | ------------ | -------- |
| `%macro` | 33 | `proc format` | 5 |
| `proc sql` | 29 | `proc means/summary` | 5 |
| `data` step | 29 | `array` | 5 |
| `%sysfunc` | 28 | `merge` | 4 |
| `%include` | 19 | `proc sort` | 4 |
| `libname` | 19 | `retain` | 3 |
| `infile`/`filename` | 7 | `first.`/`last.` | 2 |
| `proc datasets` | 7 | `systask` | 2 |
| `&&` (indirección) | 6 | `call execute` | 0 |

Lectura: PROC SQL, macros, `%include`, `libname` y `%sysfunc` dominan; `%sysfunc` (no listado en la matriz original) es P1 y debe resolverse en `macro_resolver`. `proc datasets`, `proc format` y `infile/filename` son prioridades nuevas a clasificar en `rules/sas/`. Los lotes banca/seguros (`ts-sas-legacy-analytics/BatchJobs`, `Config/autoexec.sas`) sirven de base para el análisis Grid (F3).

## Documentación de referencia local

PDFs oficiales SAS 9.4 en `~/code/javascript/qlikdojo/packages/web/public/descargas/sas-grid/`. Tres de ellos convertidos a Markdown en `docs/reference/sas/` (ignorados por git; ver su README).
