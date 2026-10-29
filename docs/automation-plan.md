# Plan de automatización: del 8 % al 80 % y después al 100 %

Plan para que varios agentes lleven el portal de «genera borradores con pendientes» a «migra casi todo sin intervención».
Está pensado para ejecutarse por paquetes de trabajo (WP) independientes. Léelo entero una vez; después trabaja solo tu WP.

## 1. Objetivo y cómo se mide

- **Paso automatizado** = un paso del plan que no deja ningún pendiente (ni componente, ni esquema, ni expresión, ni origen o
  destino de datos). Se mide con `uv run python tools/automation_metrics.py`.
- **Paso verificado** = además, su Job compila, se ejecuta y da los mismos datos que SAS (WP Q1 y Q2). Automatizado **no**
  es lo mismo que correcto: son dos métricas y las dos cuentan.
- **80 %** = el 80 % de los pasos del corpus real sin pendientes. **100 %** = cada paso queda automatizado **o** clasificado con
  su motivo y un stub generado: ningún hueco silencioso. No se promete traducir cualquier SAS imaginable.

### Línea base (medida con `tools/automation_metrics.py`, 28/10/2026)

| Corpus | Programas | Pasos | Automatizados | Sin esquema | Expresiones |
| ------ | --------- | ----- | ------------- | ----------- | ----------- |
| `real` | 50 | 2 063 | **8,1 %** | 1 749 | 627 |
| `synthetic` | 120 | 429 | **16,8 %** | 303 | 95 |

Pasos con pendientes por operación en el corpus real (las demás operaciones están por debajo de 40):

| Operación | Pasos | Con pendientes | Qué falta |
| --------- | ----- | -------------- | --------- |
| `write` | 413 | 413 | sistema y tabla de destino; acción sobre la tabla |
| `read` | 264 | 264 | formato físico o sistema de origen; esquema y tipos |
| `report` | 238 | 238 | decidir si el reporte se migra o se descarta |
| `read_file` | 206 | 206 | ruta, delimitador, codificación y esquema |
| `compute` | 178 | 178 | tipos de las columnas calculadas; expresiones sin traducir |
| `inline_data` | 161 | 161 | confirmar los datos incrustados (están en el propio SAS) |
| `aggregate` | 117 | 104 | estadísticas de PROC MEANS/FREQ |
| `macro_call` | 62 | 62 | Job hijo que implementa la macro |
| `format_definition` | 51 | 51 | lógica de rangos y `OTHER` |
| `unsupported` | 45 | 45 | diseño manual |
| `join` / `filter` | 75 | 59 | claves, condiciones |

### Techo estimado (no es una promesa)

Contando qué operaciones se podrían resolver del todo: **sin información del entorno** (datos incrustados, reportes con una
política, estadísticas, formatos, filtros) el techo ronda el **36 %**; **con un catálogo de entorno** (WP5) y esquemas
propagados (WP7) sube a cerca del **89 %**. Lo que queda (macros, estado entre filas, código dinámico) es el 11 % de la fase 4.
La conclusión de diseño: **el cuello de botella no es el parser, es la información que el SAS no trae** (esquemas,
formatos físicos, destinos). Por eso el catálogo de entorno es el paquete más importante.

## 2. Reglas para los agentes

1. Lee `AGENTS.md` y `docs/agent-guide.md`. Un WP por agente. Trabaja solo en lo tuyo y no toques archivos ajenos: revisa
   `git status` antes de editar.
2. **Nunca inventes un valor.** Un dato que no está en el SAS ni en el catálogo de entorno sigue siendo un pendiente con su
   motivo. Automatizar es rellenar con lo que se sabe, no adivinar (principio del README).
3. **Primero la prueba.** Cada regla nueva entra con una prueba que falla sin ella. Las reglas de mapeo viven en
   `rules/mappings/talend-components.json`; el planificador en `src/sas_grid_migrator/migration_planner/`.
4. **Mide antes y después** con `tools/automation_metrics.py` y anota las dos cifras en `docs/progress.md`. Un WP que no
   baja la métrica que declara no está terminado.
5. Si tu WP cambia **lo que se escribe a Studio**, pasa `scripts/verify_in_studio.py` con `migration_matrix` y un corpus
   real (guía en `docs/production-readiness.md`). Los avisos que Studio muestra al cargar un Job no salen en Problemas.
6. Si tocas `mcp/talend-mcp/`: MCP primero, luego el portal (`docs/mcp-subtree.md`). Un commit del MCP no toca nada fuera de
   `mcp/talend-mcp/` salvo `contract/` y sus pruebas. Una tool nueva del portal exige manifiesto, preset y prueba de contrato.
7. Commits y push solo cuando el usuario lo autorice (`AGENTS.md`); este plan no lo autoriza por sí mismo. Di al terminar qué
   repos tocaste y qué quedó sin empujar.
8. **Definición de hecho** de un WP: pruebas nuevas en verde; `uv run pytest -q`, y `bun test` + `bun run typecheck` en
   `apps/web` y en `mcp/talend-mcp`; métricas antes/después; `docs/` actualizada; entrada en `docs/progress.md`.

## 3. Dependencias

```
WP0 ──(base para todos)
WP2, WP3, WP4  ── independientes entre sí ── fase 1
WP5 ──► WP6 ──► Q1 ──► Q2
WP7 ──► WP6 (esquemas de intermedios)      WP8 ── independiente
WP7 + WP8 ──► WP9 ──► WP10        WP6 ──► WP11        WP12 y WP13 al final
```

Se pueden lanzar a la vez: **WP0, WP2, WP3, WP4, WP5 (diseño) y WP8**.

## 4. Fase 0: medir

**WP0 · Trinquete de métricas.** Entregable: `tests/golden/automation_baseline.json` generado con
`tools/automation_metrics.py --json` sobre un árbol limpio, y una prueba que falla si `automated_percent` de `real` o
`synthetic` baja más de 0,5 puntos (y pide actualizar la base cuando sube). Aceptación: la prueba corre en el CI y en
`uv run pytest`. Basta un agente y media jornada.

**WP1 · Piloto con programas reales del cliente (necesita a una persona).** Conseguir 5 a 10 programas (uno por perfil P0/P1/P2),
la convención de nombres de Jobs y carpetas del cliente, y cómo salen sus datos. Entregable: carpeta fuera de Git (`.gitignore`)
y su informe de métricas. Sin esto el 80 % se mide solo sobre fixtures públicos.

## 5. Fase 1: sin información del entorno (≈8 % → 36 %)

**WP2 · Datos incrustados.** 161 pasos `inline_data`. `datalines`/`cards` traen las filas y los nombres de columna: generar
`tFixedFlowInput` con el esquema y las filas completas, sin pendiente. Aceptación: `inline_data` pasa de 161 pasos con
pendientes a 0 en `real`; el Job aplica en Studio con `verify_in_studio.py`.

**WP3 · Reportes.** 238 pasos `report` (PROC PRINT, REPORT, TABULATE). Definir una política por proyecto (`descartar` |
`exportar a CSV` | `tLogRow`) con un valor por defecto documentado, y aplicarla sin pendiente. Aceptación: `report` en 0 pasos
con pendientes con la política por defecto; la política se cambia desde la configuración del proyecto y se refleja en el plan.

**WP4 · Estadísticas, formatos, orden y duplicados.** PROC MEANS/SUMMARY/FREQ → `tAggregateRow` con agrupación y funciones
completas (los nombres de las columnas de salida salen de las estadísticas pedidas); `PROC FORMAT` → `tMap` con lookup o
`tReplace`; `NODUPKEY` → `tUniqRow`; `PROC SORT` con varias claves. Aceptación: `aggregate` y `format_definition` bajan
a menos del 10 % de pasos con pendientes; pruebas por cada estadística.

## 6. Fase 2: entorno y esquemas (≈36 % → 70 %)

**WP5 · Catálogo de entorno.** Un fichero por proyecto (`environment.json`, con esquema JSON versionado) que dice, una sola vez
por entorno: cada **librería** (`libname`) → conexión (BD, carpeta de archivos o SAS7BDAT) y cada **dataset** → tabla o
archivo, formato (delimitador, cabecera, codificación, ancho fijo), columnas y tipos. Las credenciales **nunca** van en claro:
solo el nombre de la variable de contexto. Entregables: modelo y persistencia en `src/sas_grid_migrator/`, endpoints en
`apps/api/`, carga y edición en la web, e importadores:
(a) CSV/JSON manual; (b) SAS7BDAT con `pyreadstat` (esquema y exportación a CSV); (c) `PROC CONTENTS`/`DICTIONARY.COLUMNS`
exportados; (d) `INFORMATION_SCHEMA` de una BD con conexión de solo lectura; (e) archivos de muestra (infieren delimitador,
cabecera y tipos). Aceptación: un catálogo de ejemplo para `learning-sas-by-example` (los 205 pasos que hoy dicen «librería BASE:
Talend no lee .sas7bdat») y un informe de cuántos datasets del corpus quedan cubiertos. **Necesita decisiones del usuario**
(sección 9).

**WP6 · Lecturas y escrituras desde el catálogo.** Con el catálogo, `read`, `write` y `read_file` salen configurados: el
componente por tecnología (`tFileInputDelimited`, `tDBInput`, etc.), el grupo de contexto de conexión por librería, el esquema
en el componente y la acción sobre la tabla (`SAS reemplaza el dataset completo` → un valor por defecto configurable,
nunca implícito). Aceptación: `read`, `write` y `read_file` bajan de 883 pasos con pendientes a los que el catálogo no cubra;
el Job de `ts-sas-legacy-analytics` aplica y compila con un catálogo de ejemplo.

**WP7 · Propagación de esquemas.** El esquema de salida de cada paso se calcula desde sus entradas y su operación
(`select`/`keep`/`drop`/`rename`/`compute`/`join`/`aggregate`/`sort`/`set`/`merge`/`transpose`) y rellena `schema_columns` y
«Tipos de las columnas calculadas» (178 pasos). Aceptación: «sin esquema» baja de 1 749 a menos de 300 en `real` con
catálogo; casos de prueba por operación, incluida la precisión de los tipos numéricos.

## 7. Fase 3: expresiones y lógica (≈70 % → 85 %)

**WP8 · Traductor de expresiones SAS → Java de Talend.** Hoy se traduce un subconjunto conservador (627 expresiones en el
corpus real). Entregable: tabla de funciones con pruebas «SAS → Java esperado» para `strip`, `trim`, `upcase`, `substr`, `scan`,
`index`, `cats`/`cat`, `compress`, `input`/`put` con formatos, `coalesce`, `missing`, `sum`, `round`, `intnx`, `intck`, `mdy`,
`datepart`, `today` y operadores. Dos reglas semánticas obligatorias: **missing** (SAS propaga el valor perdido en aritmética) y
**fechas** (época 1960 frente a 1970). Aceptación: porcentaje de expresiones traducidas del corpus real, medido y subido
al trinquete; lo que no se traduce sigue como pendiente con el motivo.

**WP9 · Joins, merge, filtros y `PROC SQL`.** Claves y tipos de join en `tMap`/`tJoin`, condiciones con WP8, `SELECT` con
`GROUP BY`/`CASE`/subconsultas; cuando el origen es una BD, SQL directo en `tDBInput` (pass-through). Aceptación: `join` y
`filter` en 0 pasos con pendientes cuando las columnas se conocen.

## 8. Fase 4: lo difícil (≈85 % → techo; 100 % clasificado)

**WP10 · Estado entre filas.** `RETAIN`, `FIRST.`/`LAST.`, `LAG`, arrays → patrones sobre variables de `tMap` y
`tSortRow`/`tAggregateSortedRow`; si no cabe, una plantilla `tJavaRow` con el pseudocódigo SAS en comentarios y estado
`needs_review`.

**WP11 · Macros.** `macro_call` → Job hijo o joblet parametrizado con contexto y `tRunJob`; `%LET` global → variable de
contexto. Los `%INCLUDE` estáticos ya se resuelven.

**WP12 · Lo no automatizable, sin huecos silenciosos.** `CALL EXECUTE`, includes dinámicos, `DICTIONARY.*`, `X`/`SYSTASK`, hash
dinámico: cada caso queda clasificado, con un stub generado y listado por Job en el informe («esto requiere a una persona,
por esto»). Es lo que permite decir 100 % sin mentir.

**WP13 · Orquestación Grid.** `sasgsub` y similares → ejecución en paralelo con `tRunJob` o plan en Talend Management
Console. Depende de la decisión sobre el destino (sección 9). El catálogo Grid hoy tiene 0 entradas `supported`.

## 9. Pistas de calidad y de operación

| Id | Qué | Aceptación |
| -- | --- | ---------- |
| Q1 | **Compilar y ejecutar.** Tras aplicar, `talend_job_verify` sobre los Jobs sin pendientes, con datos de muestra. | Informe por Job: compila, ejecuta, avisos. |
| Q2 | **Equivalencia.** Entrada de muestra + salida **dorada** de SAS (la entrega el cliente en CSV; no hay SAS en el CI). Compara filas, esquema, suma de control por columna, tolerancia numérica y fechas. | Un Job solo pasa a `verificado` si el informe pasa. |
| Q3 | **Puerta de Studio en cada liberación.** `verify_in_studio.py` sobre todos los corpus, con el vigilante de diálogos. | 0 errores inesperados y 0 diálogos. |
| Q4 | E2E web con Playwright (nunca se ha ejecutado). | Recorrido ZIP → plan → aplicar → exportar en verde. |
| Q5 | **Git de Talend Cloud.** Subir desde Studio los Jobs creados offline y comprobar que no se pierden carpetas (`src`, `tests`, `target` ya se evitan). | Commit y push de un lote de prueba, sin pérdidas. |
| Q6 | CI: fijar la versión de `bun` (hoy `latest`), añadir `ruff`, correr el trinquete de WP0. | CI verde y reproducible. |
| O1 | **Reinicio automático de Studio** entre tandas cuando la memoria pase del 75 % (el preflight ya avisa; la herramienta `talend_studio_restart` existe). | Un lote de 500 Jobs sin intervención. |
| O2 | **Deshacer un lote**: borrar los Jobs que creó, con su registro en el estado del proyecto. | Botón y endpoint con prueba. |
| O3 | **Despliegue y seguridad**: un analista por máquina o un servidor compartido; autenticación y auditoría de lo creado; credenciales solo por contexto (`docs/security.md`). | Decisión escrita y pruebas. |
| O4 | Manual de instalación y solución de problemas (Studio + bridge + MCP + portal). | Un analista nuevo lo sigue sin ayuda. |

## 10. Decisiones que necesita del usuario

1. **Programas reales del cliente** (WP1) y su convención de nombres.
2. **De dónde salen los esquemas:** ¿pueden exportar `PROC CONTENTS`, dar acceso de solo lectura a las BD o entregar los
   SAS7BDAT? Define qué importadores de WP5 se construyen primero.
3. **Política de reportes** (WP3): descartar, exportar a CSV o registrar.
4. **Acción por defecto al escribir** («SAS reemplaza el dataset completo»): ¿recrear la tabla, truncarla o añadir?
5. **Destino de la orquestación Grid** (WP13): Talend Management Console o ejecución local.
6. **Modelo de despliegue** (O3).

## 11. Hitos y criterios de salida

| Hito | Automatizados (`real`) | Se cumple cuando |
| ---- | ---------------------- | ---------------- |
| H0 | 8 % | WP0 en el CI |
| H1 | ≥ 35 % | WP2, WP3 y WP4 cerrados |
| H2 | ≥ 65 % | WP5, WP6 y WP7, con el catálogo de un caso real |
| H3 | ≥ 80 % | WP8 y WP9; Q1 en verde para los Jobs sin pendientes |
| H4 | ≥ 85 % y 100 % clasificado | WP10 a WP12; Q2 sobre los programas del piloto |

**Producción** exige H3 más Q1, Q2 (al menos sobre los programas del piloto), Q3, Q5, O1 y O3. El 80 % de automatización
sin verificación de equivalencia no es producción.

## 12. Entrega entre agentes

Al terminar un WP, añade a `docs/progress.md` una entrada con: id del WP, qué se hizo, métricas antes y después (copia la
salida de `tools/automation_metrics.py`), qué quedó fuera y qué repos tocaste sin empujar. El siguiente agente parte de esa
entrada y del código, no de la conversación.

## 13. Primer código real del cliente (28/10/2026)

El cliente entregó dos programas reales (`Cod1.txt` y `Cod2.txt`, unas 27 700 líneas). Viven **fuera de Git**: tienen servidores,
rutas y una clave. Se analizaron con el portal; esto es lo medido y lo que cambió.

| Medida | Valor |
| ------ | ----- |
| Sentencias reconocidas | 11 305 (52 sin reconocer, el 0,5 %) |
| Tiempo | análisis 2,4 s, planes 6,4 s |
| Pasos de los planes | 3 095 (antes de ignorar las macros auxiliares de SAS Studio: 3 550) |
| Automatizados | **16,8 %** (14,6 % antes de esa limpieza) |

**El perfil no se parece a los fixtures.** Es orquestación por macros: 970 llamadas, 337 definiciones, 1 606 `%let` y 1 096
sentencias de control (`%do`/`%if`). Usa SQL *pass-through* contra Impala (137 conexiones; 65 `execute` y 33 `select ... from
connection to`), y el SQL de los `execute` se construye en una macrovariable en tiempo de ejecución. Hay `%syslput`/`rsubmit`
(sesión remota), 40 `%include` de una biblioteca corporativa de macros **que no se entregó** (1 111 referencias sin resolver) y
629 marcas `/* Etiqueta: ... */`, que son los nodos de un flujo de SAS Studio.

**Corregido a partir de estos archivos** (con sus pruebas):
- Un `.txt` con código SAS se importa como SAS por su contenido (antes se ignoraba como documento).
- `proc pwencode in='...'` llevaba una clave en claro al `analysis.json`: ahora se redacta. En Talend no llegaba.
- SAS Studio antepone un carácter invisible (U+200B) al exportar: ya no se pega al primer comentario.
- `%web_drop_table` y `%web_open_table` (455 de las 712 llamadas a macro) no son lógica: dejan de generar pasos.

**Paquetes nuevos que salen de este código:**

| Id | Qué | Fase |
| -- | --- | ---- |
| WP14 | Las marcas `Etiqueta:` como nombres de subjob y de componente: trazabilidad directa al flujo de SAS Studio y nombres de Job con sentido para el cliente. | 1 |
| WP15 | SQL *pass-through*: `connect to impala` + `execute`/`select ... from connection to` → `tImpalaRow`/`tImpalaInput` (o `tDBRow`/`tDBInput`) con el SQL literal; cuando el SQL está en una macrovariable, variable de contexto y pendiente trazado. | 2 |
| WP16 | Lista de dependencias no entregadas (los `%include` sin resolver) como entregable del informe: «pide estos archivos al cliente». Sin ellos, las macros no se pueden expandir. | 1 |
| WP17 | `%syslput`/`rsubmit`/`signon` (sesión remota) → variables de contexto o descarte documentado. | 1 |
| WP18 | Bucles de macro (`%do i=1 %to N`) → `tLoop` o `tFlowToIterate`, con el cuerpo como Job hijo. | 4 |

**Decisión que necesita del usuario:** los archivos que incluye el código (la biblioteca de macros) y confirmar que
Impala es el motor de datos del cliente.

## 14. Traducir a componentes, no a Java: arquitectura y reparto

**La unidad de traducción es el componente de Talend Studio con su configuración**, no una expresión. Una expresión Java solo
aparece donde Studio la guarda como Java (`tMap`, `tFilterRow` avanzado). El catálogo tiene más de mil componentes: la
traducción usa **el más específico que exista** (`docs/conventions.md`, sección 4) y la forma del Job es siempre la de las
convenciones: prejob con las conexiones, un subjob por etiqueta, postjob que cierra, errores con `tLogCatcher`/`tDie`, todo lo
que cambia por entorno en contexto, y joblets para lo repetido.

### Cómo lo hacen los conversores profesionales, y cómo lo hacemos nosotros

| Etapa profesional | Aquí |
| ----------------- | ---- |
| Preprocesar y normalizar | Hecho: `.txt` por contenido, carácter invisible, redacción de claves, macros auxiliares de SAS Studio |
| Árbol de análisis + repositorio de patrones | El IR y el planificador, más **recetas** en datos (`rules/recipes/`, WP-A2): patrón SAS → componentes + parámetros + tablas |
| Biblioteca de ejecución para la semántica | **Ninguna propia**: rutinas de sistema de Talend (`StringHandling`, `TalendDate`, `Mathematical`, `Relational`) y Java nativo con guardas de nulo. No hay nada que instalar |
| Registrar lo no traducido para revisión | Informe de traducción (WP-A5): lo no traducido, ordenado por frecuencia, alimenta las recetas |
| Validar contra la salida de SAS | Arnés de equivalencia (Q2) con salidas doradas |

### Estado a 28/10/2026 (lo ya hecho en esta sesión)

Commiteado antes: plan, métrica `tools/automation_metrics.py`. Commiteado en `5fc0045`: importar `.txt` como SAS y quitar el
carácter invisible (con prueba); redactar `proc pwencode` (con prueba); ignorar `%web_drop_table`/`%web_open_table` (con
prueba); `talend_translator.py`, el traductor de gramática completa (funciones de varios argumentos, `CASE`, `IN`, `BETWEEN`,
`IS MISSING`, `.`, formatos, fechas), que emite **solo rutinas de sistema de Talend y Java nativo**, **detrás del interruptor
`SGM_TALEND_EXPRESSIONS=1`, apagado por defecto**; `docs/conventions.md`. A4 en curso:
`tests/unit/test_talend_translator.py` fija el Java esperado por función y una prueba de contrato comprueba que cada llamada
emitida existe en las rutinas de Studio 8.0 (nada propio que instalar). **Falta**: comprobar en Studio que el Java emitido
compila (B1) y sustituir por componentes lo que hoy sale como expresión. **No enciendas el interruptor hasta que B1 lo haya
comprobado.**

### Avance medido (28/10/2026, segunda tanda)

`real`: **8,1 % → 27,2 %** de pasos automatizados (2 063 → 1 903 pasos: los 160 `read_file` que eran el mismo paso que un
`datalines` dejan de duplicarse). `synthetic`: 16,8 % → 22,0 %. Sin esquema en `real`: 1 749 → 1 497. Con el catálogo de
entorno de ejemplo (`rules/environment/learning-sas-by-example.json`, que solo cubre dos datasets): 28,3 %. Hecho, con
pruebas:

| Paquete | Qué se hizo | Pasos con pendientes |
| ------- | ----------- | -------------------- |
| WP3 | Política de reportes del proyecto (`log` por defecto → `tLogRow`; `csv`; `discard`), en `Settings.report_policy` y en el planificador | `report` 238 → **0** |
| WP2 | `datalines`/`cards`: el lexer conserva las filas, el parser las lleva al IR y el planificador arma `tFixedFlowInput` con esquema y filas. Entrada por columnas (`@1`, `#2`), filas que no cuadran con el `INPUT` o bloque sin `INPUT` siguen como pendiente con su motivo | `inline_data` 161 → **99** |
| WP7 (parte) | El tipo de una columna calculada sale de la expresión (aritmética → `Double`, texto → `String`, comparación → `Boolean`, fecha → `Date`); solo queda pendiente lo que no se puede tipar | `compute` 178 → **111** |
| WP4 (parte) | `PROC MEANS/SUMMARY/FREQ` → `tAggregateRow` con los grupos de `CLASS`/`BY`, las estadísticas pedidas y los nombres del `OUTPUT OUT=`; `PROC FORMAT` de valores sueltos → tabla de lookup sin pendiente, y los formatos con rangos, comparaciones, `OTHER` o clave vacía siguen pendientes con el motivo | `aggregate` 104 → **75**; `format_definition` 51 → **44** |
| WP7 (condicionales) | `IF cond THEN x = a; ELSE x = b;` → ternaria de `tMap` cuando la condición y los valores se traducen; lo que no, deja de contar como automatizado y queda pendiente con su motivo. Antes, 55 pasos llevaban un condicional sin traducir y aun así contaban | `compute` 111 → **165** (el número sube porque deja de mentir) |
| WP5 + WP6 (parte) | Catálogo de entorno: modelo, validación, esquema versionado y ejemplo. Con catálogo, `read`/`write` toman tabla, columnas y tipos y dejan de pedirlos; la acción al escribir pasa a ser del proyecto (`SGM_TABLE_ACTION`, por defecto `drop_create`) | `write` y `read` sin pendientes para los datasets del catálogo; `sin componente` 757 → **552** con el ejemplo |

Lo que falta para el 80 % sigue siendo lo que depende del **catálogo de entorno** (WP5/WP6/WP7): `write` 413, `read` 264,
`read_file` 46 y los 1 527 pasos sin esquema. Sin ese catálogo el techo es el 36 % de la sección 1, y para construirlo hacen
falta las decisiones de la sección 10 (de dónde salen los esquemas). Después: `aggregate` 104, `macro_call` 62,
`format_definition` 51 y `unsupported` 45.

### Reparto: dos agentes, sin pisarse

- **Agente A (núcleo Python): `src/sas_grid_migrator/**`, `rules/**`, `tests/` de Python.** Decide *qué* se genera.
- **Agente B (MCP, Studio y producto): `mcp/talend-mcp/**`, `apps/**`, `scripts/**`, `contract/**`.** Hace que Studio *lo
  escriba y lo valide*. El contrato entre los dos es la plantilla de `talend_jobs_create_batch`: si A necesita un campo nuevo,
  B lo añade primero al MCP y al manifiesto `contract/portal-tools.json`, y A lo usa después.

**Agente A (yo, el que escribe esto) hace, en este orden:**

| Id | Entregable | Aceptación |
| -- | ---------- | ---------- |
| A1 | **Estructura de Job por convención**: prejob con las conexiones (una por `libname` de base de datos), un subjob por `Etiqueta:`, postjob que confirma y cierra, `tLogCatcher`/`tDie`, contexto `DEV`/`TEST`/`PROD`. En el planificador y en `offline_payload.py`. | Cada Job generado cumple `docs/conventions.md` (prueba en `spec_invariants.py`) |
| A2 | **Recetas** en datos, `rules/recipes/*.json`: patrón SAS → componentes, parámetros y tablas, para los ~60 componentes de la sección 4 de las convenciones. Se validan contra el catálogo (`rules/talend/components.json`). | Una receta con un componente o parámetro que no existe falla la prueba |
| A3 | **Traducción dentro de la configuración**: `WHERE` → tabla `CONDITIONS`; `ON` → tabla `JOIN_KEY` de `tJoin`; `PROC SORT` → `CRITERIA`; `NODUPKEY` → `UNIQUE_KEY`; `MEANS/FREQ` → `GROUPBY`/`OPERATIONS`; asignaciones y `IF/THEN/ELSE` → expresiones de `tMap` con rutinas de Talend; `tJava` solo como último recurso | Los filtros, joins, orden y agregados salen sin pendiente cuando las columnas se conocen |
| A4 | Pruebas de `talend_translator.py` por función, con el Java esperado, y sustituir lo que pueda ser un componente (`tReplace`, `tConvertType`, `tExtractRegexFields`) por el componente | Cada función del mapeo tiene su prueba; `tJava` solo en el último recurso |
| A5 | **Informe de traducción**: qué no se tradujo, por qué y cuántas veces; endpoint y exportación | Lista ordenada por frecuencia, con archivo y línea |
| A6 | Catálogo de entorno y propagación de esquemas (WP5 a WP7 de este plan) | Como en las secciones 6 y 9 |

**Agente B hace, en este orden:**

| Id | Entregable | Aceptación |
| -- | ---------- | ---------- |
| B1 | **Comprobar en Studio el Java que emite el traductor**: un Job de prueba por cada función del mapeo (`StringHandling`, `TalendDate`, `Mathematical`, `Relational`), compilado con `talend_job_verify`. Es lo que permite encender `SGM_TALEND_EXPRESSIONS` | Todas compilan; las que no, se corrigen en el mapeo |
| B2 | **Escribir en Studio lo que A genera**: `tPrejob`/`tPostjob` con sus disparadores, conexiones compartidas, **joblets** (crear y usar offline), grupos de contexto `DEV`/`TEST`/`PROD`, `tLogCatcher`/`tDie`, `tRunJob` con contexto. Extender `talend_jobs_create_batch` y su esquema | `verify_in_studio.py` sin errores ni diálogos con Jobs de la estructura nueva |
| B3 | **Comprobar la configuración de cada componente** contra sus definiciones: parámetros, tablas, conectores; rechazar antes de escribir (hecho para las conexiones: `comprobar-conexiones.ts`) | `INVALID_COMPONENT` con el motivo |
| B4 | **Cobertura de componentes**: `talend_studio_coverage` sobre los que usan las recetas | Informe de cuáles se crean, configuran y compilan |
| B5 | **Compilar, ejecutar y comparar** (Q1 y Q2) con `talend_job_verify` y salidas doradas | Informe por Job |
| B6 | **Web**: pantalla del catálogo de entorno, del informe de traducción y de la política de reportes | Recorrido E2E (Q4) |
| B7 | Operación: reinicio automático entre tandas, deshacer un lote, Git de Talend Cloud, manual (O1 a O4, Q5, Q6) | Según la sección 9 |

### Reglas del reparto

1. **A y B no editan los mismos archivos.** Si hace falta, el que necesita deja una petición en `docs/progress.md` con el
   formato del campo y el otro la atiende.
2. **MCP primero**: un cambio del MCP se commitea y se publica (`docs/mcp-subtree.md`) antes de que A lo use.
3. **Interruptores, no regresiones**: lo que aún no está comprobado en Studio (hoy, el traductor de expresiones) va apagado
   por defecto.
4. Cada entrega: pruebas rápidas del área, entrada en `docs/progress.md`, y avisar de lo que queda sin empujar.
5. **No se mide nada de más.** La métrica es `tools/automation_metrics.py` y se corre al cerrar cada paquete, no antes.
