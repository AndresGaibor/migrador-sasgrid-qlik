# Catálogo de reglas de traducción SAS a Talend

Estado a 2026-10-29. Consolida los cuatro análisis de patrones de `docs/analysis/`:

- `cod1-patrones.md`: 37 patrones (programa 1, 2.904 líneas).
- `cod2-patrones-tramo1.md`: 28 patrones (programa 2, líneas 1 a 8.300).
- `cod2-patrones-tramo2.md`: 29 patrones (programa 2, líneas 8.301 a 16.600).
- `cod2-patrones-tramo3.md`: 22 patrones (programa 2, líneas 16.601 a 24.801).

Los 116 patrones se deduplican en **55 reglas** (R01 a R55). El estado de cada regla se ha comprobado leyendo `src/sas_grid_migrator/` (working tree de `main`, con cambios sin commit). Las referencias a `C1` y `T1`/`T2`/`T3` apuntan a esos análisis. Las cifras son las de cada análisis; las sumas entre tramos son aproximadas. Los ahorros en pasos de Talend son estimaciones.

---

## 1. Principios

1. **Corriente única.** Lo que SAS hace con datasets intermedios se resuelve con conectores entre componentes del mismo Job, no con escrituras y lecturas intermedias.
2. **Un tMap absorbe lo fila a fila.** Filtros, renombres, cálculos, conversiones, validaciones y salidas múltiples van en un único tMap por corriente. Un componente aislado solo si no hay nada que fundir.
3. **ELT cuando origen y destino son la misma base de datos.** El join, el filtro y la agregación se empujan al motor con `tImpalaInput` o `tImpalaRow`. No se trae la tabla a SAS para devolverla.
4. **La fontanería no se migra.** Shell, esperas, sesiones remotas, troceo, temporales, trazas, cabeceras de IDE y conteos sin consumidor se descartan y se registran en `not_migrated` con su equivalente.
5. **Joblet para la repetición real, no para la copia.** Las copias idénticas de macros se colapsan primero. Un joblet solo si queda un bloque de lógica de datos repetido con parámetros.
6. **Parámetros en contexto, nunca literales.** Entorno, DSN, umbrales, códigos de negocio y listas van a grupos de contexto o a tablas de reglas. Las credenciales van a variables de tipo password y su valor nunca se copia.
7. **Validaciones explícitas.** Un fallo no puede ser silencioso: los rechazos llevan motivo, los conteos de control tienen `tDie` y los errores de conversión son rechazos.
8. **Advertir, no corregir.** Cuando el SAS tiene un error probable (predicado invertido, rama muerta, join que multiplica filas), el migrador lo marca como aviso y no lo traduce en silencio.

---

## 2. Catálogo de reglas

Convención de estado: **implementada** (existe y funciona en el código), **parcial** (existe una parte) o **pendiente** (no existe en el código).

### Grupo A. Descarte de fontanería

#### R01. Wrappers de IDE y metadatos de generación
- **Firma:** llamadas `%web_drop_table(x)` y `%web_open_table(x)` alrededor de cada paso; cabeceras "Código de la tarea generado por..."; `TITLE`/`FOOTNOTE` generados; comentarios `/* Etiqueta: ... */`.
- **Capa:** lexer (comentarios) y planificador (descarte).
- **Diseño Talend:** ninguno. La etiqueta pasa a descripción o nombre de componente; las cabeceras no se copian.
- **Frecuencia y ahorro:** C1: 4 bloques de query y 10 cabeceras. T1: 126 + 125 `%web_*`, 102 cabeceras, 7 `TITLE`. T2: 48 pares, 91 cabeceras, 163 etiquetas. T3: 50 + 50 `%web_*`, 22 cabeceras, 157 etiquetas. Ahorro: 0 pasos Talend; elimina todo ese ruido del IR.
- **Estado:** parcial. `migration_planner/plumbing.py` (`_STUDIO_HELPER_PREFIX = "web_"`) clasifica `%web_*` como fontanería. Los comentarios no entran al IR. `TITLE`/`FOOTNOTE` no tienen tratamiento explícito (no verificado).
- **Variantes:** `%web_open_table` sin `%web_drop_table`; cabeceras con otro generador; `FOOTNOTE` con usuario y servidor.
- **Riesgos:** `%web_drop_table` también borra la tabla: confirmar que no hay limpieza necesaria. Las cabeceras contienen usuario y servidor: no copiar. Algunas etiquetas describen reglas de negocio: conservarlas como descripción.
- **Prueba:** un bloque `%web_drop_table(WORK.a); proc sql; create table WORK.a as select ...; quit; %web_open_table(WORK.a);` produce el mismo IR que el SQL sin envoltorios, y la etiqueta aparece como descripción del componente.

#### R02. Trazas, medición y conteos sin consumidor
- **Firma:** `%put` (sin efecto sobre datos), macro de tiempos con `datetime()`, `options` de depuración (`mprint`, `symbolgen`, `mlogic`), `select count(*)` sin alias ni destino.
- **Capa:** planificador (`plumbing`).
- **Diseño Talend:** `tStatCatcher` y `tFlowMeter` para medición; `tLogRow` solo si hace falta un registro.
- **Frecuencia y ahorro:** C1: 101 `%put`, 52 `options`, 4 llamadas a `%tiempos`, 4 `count(*)`. T1: 6 `%tiempos`, 18 `datetime`, 28 `options`. T2: 99 `%put`, 12 `%tiempos`. T3: 12 `%tiempos`. Ahorro: 0 pasos Talend.
- **Estado:** implementada. `plumbing.py`: `_PUT`, `_DATETIME`, `_count_only` (conteo sin alias), categoría `medicion`, `entorno` y `conteo`.
- **Variantes:** `%put` con `&=variable`; `options nosource`; `count(*)` con alias que sí alimenta una tabla (no es fontanería: pasa a R41).
- **Riesgos:** `mprint` y `symbolgen` en producción pueden escribir datos en el log. Un `%put` con una credencial expone el valor.
- **Prueba:** un programa con `%put`, `datetime()` y `options mprint;` no produce ningún paso; `not_migrated` contiene las tres entradas con `talend_equivalent` no vacío.

#### R03. Orquestación de sistema operativo
- **Firma:** `x "comando";` o `call system(...)` dentro de un bucle; `call sleep(n)`; bucle `until`/`while` que cuenta procesos con `ps`; sentencias `insert into tabla_comandos values("sh ...")`.
- **Capa:** planificador (`plumbing`).
- **Diseño Talend:** dependencia de ejecución entre Jobs con `OnSubjobOk`; `tRunJob` para ejecutar hijos; `tSystem` solo si el comando es imprescindible.
- **Frecuencia y ahorro:** C1: 4 tablas de comandos, 4 lanzadores, 4 sondeos, 4 exclusiones por `ps`. T2: 13 bloques de carga con shell (§23). T3: 11 bloques de carga (P01). Ahorro: 0 pasos si el Job queda en una sola ejecución síncrona.
- **Estado:** parcial. `plumbing.py`: `_SHELL_POLL`, `_SLEEP_CALL`, categorías `shell_auxiliar` y `espera`. La tabla de comandos (`insert ... "sh ..."`) y el bucle que recorre esa tabla no se detectan como conjunto.
- **Variantes:** `system()`, `pipe` a `ps`, `sleep` sin argumentos, `waitfor`.
- **Riesgos:** el sondeo puede no terminar nunca. `x` no devuelve código de salida a SAS, así que el error solo aparece en logs.
- **Prueba:** un bucle de tres `x "script &i";` con `call sleep(2,1);` entre ellos genera solo el `tRunJob` o el `OnSubjobOk` del Job, sin pasos de shell.

#### R04. Sesiones remotas y transferencias por sesión
- **Firma:** `options remote=... comamid=tcp`; `signon usuario pass=...`; `rsubmit servidor wait=no; ... endrsubmit;`; `waitfor _all_ sesion1 ...`; `signoff`; `proc upload` y `proc download` dentro de un `rsubmit`.
- **Capa:** IR (nodo de sesión remota) y planificador.
- **Diseño Talend:** sin sesión. Lectura y escritura directa a la ruta del Remote Engine (`tFileInputDelimited` con ruta UNC, `tFileOutputDelimited` a ruta de red). Si el motor no ve la ruta, `tFileFetch` o `tSFTPGet`.
- **Frecuencia y ahorro:** C1: 16 tokens `rsubmit`/`signon`. T1: 10 `signon` y 4 descargas por `rsubmit`. T2: 13 bloques de partición por sesiones (§23). T3: 22 pares de export y upload por sesión. Ahorro: 10 a 40 bloques de fontanería según el programa.
- **Estado:** parcial. `planner.py` (`_remote_session_entries`) registra `signon`, `rsubmit`, `waitfor`, `signoff` y `options remote=` como `sesion_remota` en `not_migrated`. `proc download` no tiene tratamiento (no se traduce a tFileFetch/tSCP).
- **Variantes:** sesiones con `wait=yes`; `sessio&i` generadas en un bucle; sesión única para toda la ejecución.
- **Riesgos:** la contraseña va en la sesión (ver R14). La copia local que deja la descarga puede quedar como residuo; si la descarga falla, el siguiente paso lee un archivo viejo sin error.
- **Prueba:** un `rsubmit` que solo ejecuta `proc download` seguido de `proc import` del mismo nombre se traduce a un `tFileInputDelimited` sobre la ruta de origen, sin paso intermedio.

#### R05. Troceado por ventanas de filas
- **Firma:** `firstobs=`/`obs=` con macro variables dentro de un bucle de bloques; `ceil(total/n)` o `int((_n_-1)/n)+1`; conteo previo con `attrn(nlobs)`.
- **Capa:** planificador (`plumbing`, categoría `troceado_lotes`).
- **Diseño Talend:** ninguno. El componente de salida usa "Batch size" o "Commit every". Si el destino exige fichero, `tFileOutputDelimited` con "Split output in several files".
- **Frecuencia y ahorro:** C1: 4 llamadas activas (y 4 variantes comentadas). T1: 6 bloques de partición por sesiones. T2: 13 bloques con `firstobs`/`obs`. T3: 11 bloques (se solapa con R04 y R06). Ahorro: el bucle completo y su contador.
- **Estado:** implementada. `plumbing.py`: `_CHUNKING`, `_ROW_CHUNK`, categoría `troceado_lotes`.
- **Variantes:** `obs=` sin `firstobs=`; `_n_` con módulo; paginación con `firstobs` sobre tabla de base de datos.
- **Riesgos:** paginar sin `ORDER BY` no es determinista; no replicarlo con SQL. Una tabla sin filas debe ser un `tDie` (ver R18).
- **Prueba:** un DATA step con `set src (firstobs=&ini obs=&fin)` dentro de un `%do` se marca como `troceado_lotes` y no genera paso.

#### R06. Macro completa de carga o transferencia como fontanería
- **Firma:** macro cuyo cuerpo es al menos un 70 % fontanería: sesiones, `ps`, `sleep`, troceo, `drop` previo, comandos, conteos; o que entrega una tabla a un motor externo mediante comando.
- **Capa:** planificador (`plumbing_macros`) e IR (`MacroIR.transfer_table`).
- **Diseño Talend:** ninguno como macro. La carga real es un `tImpalaOutput` (ver R51).
- **Frecuencia y ahorro:** C1: 4 copias del programa de carga (unas 2.500 líneas). T1: 6 copias de 289 líneas (unas 1.730 líneas). T2: 13 cabeceras y 12 bundles completos (3.552 líneas, 43 %). T3: 11 bloques (unas 3.440 líneas, 42 %). Ahorro: el grueso del código del programa.
- **Estado:** implementada. `plumbing.py` (`MACRO_SHARE = 0.7`, `plumbing_macros`); `intermediate_representation/models.py` (`MacroIR.transfer_table`).
- **Variantes:** macros con nombre `_v2`, `_v3`; macro que llama a otra macro de fontanería.
- **Riesgos:** la macro externa puede tener efecto que no se ve en el archivo (no verificable sin su código). Un 70 % es un umbral; una macro mixta necesita revisión.
- **Prueba:** una macro con `%do` sobre filas, `call system` y `sleep` se clasifica como fontanería; una macro con dos `proc sql` de datos no se clasifica.

#### R07. Borrado de temporales de trabajo
- **Firma:** `proc delete data=work.x`; `proc datasets lib=work ... delete`; bloques `%if &syserr. eq 0 %then %do; ... drop ...; %end;`.
- **Capa:** planificador (`plumbing`).
- **Diseño Talend:** ninguno. Un flujo no crea el temporal. Si hay transacción, `tDBConnection` con `tDBCommit` y `tDBRollback` en `onSubjobError`.
- **Frecuencia y ahorro:** C1: 4 bloques de limpieza. T1: 82 bloques de copia de vuelta con `proc delete` (ver R23). T2: 63 copias con borrado. T3: 33 `proc delete`. Ahorro: el borrado completo.
- **Estado:** implementada. `plumbing.py` categoría `limpieza_datasets` (borrado de datasets en WORK).
- **Variantes:** `proc datasets ... delete`; `drop table` de una tabla de trabajo en la base (ver R08).
- **Riesgos:** condicionar el borrado a `&syserr` no detecta fallos de la base de datos. Un `proc delete` sobre una librería permanente con el mismo nombre que el temporal borra datos reales.
- **Prueba:** `proc delete data=work.t; run;` no genera paso y figura en `not_migrated` con categoría `limpieza_datasets`.

#### R08. DROP previo del destino
- **Firma:** `execute (drop table if exists lib.t purge) by motor;` o `connect to motor` seguido de `drop table` antes de una carga.
- **Capa:** planificador (`plumbing`), traductor (acción de tabla).
- **Diseño Talend:** la acción de tabla del componente de salida ("Drop and create table" o "Truncate table") sustituye el DDL. Un `tImpalaRow` solo si el DDL no es de carga.
- **Frecuencia y ahorro:** C1: 4 llamadas a `deleteTableLZ` y 12 bloques de conexión. T2: 13 bloques (§24). T3: 65 `drop table` (incluye la limpieza de LZ). Ahorro: 1 DDL por carga.
- **Estado:** parcial. `plumbing.py:142` clasifica `DROP TABLE` en un `sql_passthrough` como `limpieza_tablas` y su equivalente es la acción de tabla. El planificador no pone esa acción en el componente de salida.
- **Variantes:** `drop table ... purge`; `execute by`; DROP dentro de una macro de carga (lo cubre R06).
- **Riesgos:** `purge` es irreversible. Si la carga falla después, el destino queda vacío. El DROP sin condición de éxito puede borrar tablas que el reporte necesita.
- **Prueba:** un `execute (drop table if exists lib.t purge) by motor; execute (create table ...) by motor;` produce un `tImpalaOutput` con acción Drop and create y ningún `tImpalaRow` de DDL.

#### R09. Copias idénticas de macros
- **Firma:** la misma definición `%macro x ... %mend x;` aparece dos o más veces con el mismo cuerpo, o con el mismo cuerpo salvo nombres de tabla.
- **Capa:** IR (`builder.py`, colapso por huella).
- **Diseño Talend:** una sola definición. Las copias se registran como `copies` y `duplicate_lines`.
- **Frecuencia y ahorro:** C1: 4 copias del programa completo. T1: 6 copias del bundle. T2: 13 cabeceras de bundle. T3: 11 bloques. Ahorro: el 60 % a 80 % de las líneas de cada programa (estimación).
- **Estado:** implementada. `intermediate_representation/builder.py` (`first_by_fingerprint`, `original.copies += 1`) y `models.py` (`copies`, `duplicate_lines`).
- **Variantes:** copias con un `%let` duplicado; copias con DSN distinto (ver R13); copias con nombre `_v2` por cuerpo distinto (R52).
- **Riesgos:** una copia que difiera en una condición de negocio no debe colapsarse sin revisión; la comparación de huella debe ignorar nombres de tabla y espacios, no lógica.
- **Prueba:** dos definiciones idénticas de la misma macro producen una `MacroIR` con `copies == 2` y `duplicate_lines` con la línea de la segunda.

#### R10. Bloque de lógica repetido en el programa (joblet)
- **Firma:** la misma secuencia de operaciones (mismo orden de tipos, mismas conexiones) aparece en varias ramas o segmentos del programa, cambiando solo nombres de tabla o literales.
- **Capa:** planificador (`joblets.py`).
- **Diseño Talend:** un joblet con parámetros de tabla y de literal. Si la repetición es de segmento completo, preferir un Job parametrizado con `tFlowToIterate` (ver R16).
- **Frecuencia y ahorro:** C1: ninguna necesaria (lista fija). T1: 3 segmentos casi idénticos y 6 consultas de partición. T3: 3 poblaciones con el mismo pipeline (sufijos). Ahorro: 1 bloque por segmento repetido.
- **Estado:** implementada con límites. `joblets.py` propone joblets por forma, con `JOBLET_MIN_OCCURRENCES = 2` y `JOBLET_MIN_OPERATIONS = 3`. No detecta repeticiones dentro de macros ni con pasos intercalados.
- **Variantes:** repetición con literal distinto (parámetro); repetición con diferencia en una condición (no colapsar sin revisión).
- **Riesgos:** un joblet que oculta una diferencia de negocio. SAS usa la última definición de una macro, no la primera.
- **Prueba:** tres secuencias `filter`/`compute` idénticas salvo un literal producen un joblet con ese literal como parámetro.

### Grupo B. Parámetros, entorno y dependencias

#### R11. Parámetro sin valor (placeholder)
- **Firma:** `%let x = $x;`, `%let c = %str($c);`, `encoding=$encoding` dentro de una llamada; `%put NOTE- ... = $modo;`.
- **Capa:** macro resolver y reglas de contexto.
- **Diseño Talend:** variable de contexto con valor por defecto explícito; validación en `tPreJob` (`tJava` que lanza excepción si falta, con `tDie`).
- **Frecuencia y ahorro:** C1: 28 placeholders. Ahorro: ninguno en pasos; evita una ejecución sin valores.
- **Estado:** parcial. `migration_planner/context_rules.py` detecta placeholders y los propone como contexto con `needs_value` cuando no hay valor. La validación de obligatorios en `tPreJob` no está verificada.
- **Variantes:** `%str($x)`; placeholder dentro de una cadena; placeholder de credencial (R14).
- **Riesgos:** un valor real que empieza por `$` (una clave, por ejemplo) se confunde con un placeholder.
- **Prueba:** `%let x = $x;` produce una variable de contexto `x` con `needs_value`, y ninguna asignación de valor.

#### R12. Selector de entorno por código
- **Firma:** `%macro ambiente; %if &m_ambiente eq D %then %let dsn=A; %else %if ... C ... %else %if ... P ...; %mend;`
- **Capa:** macro resolver y reglas de contexto.
- **Diseño Talend:** grupos de contexto `Dev`, `Cert`, `Prod`, con DSN o host, esquema y rutas. El entorno se elige al ejecutar.
- **Frecuencia y ahorro:** C1: 4 bloques. T1: 6 copias. T2: 13 selectores. T3: 11 bloques. Ahorro: todas las cadenas `%if`.
- **Estado:** implementada. `context_rules.py`: `ENVIRONMENT_ALIASES`, `environment_chains`, `environment_groups`, `environment_parameters`.
- **Variantes:** `m_ambiente` que viene de un `%include` externo; alias en otro idioma (`DESA`, `QA`, `PROD`); código de ambiente de dos letras.
- **Riesgos:** si ninguna rama coincide, la variable queda sin valor y el fallo aparece más tarde en SQL. El código no valida la variable.
- **Prueba:** una cadena `%if` de tres ramas sobre la misma variable produce un grupo de contexto con tres entornos y el valor de la variable en cada uno.

#### R13. Motor o DSN literal dentro de una consulta
- **Firma:** `connect to motor (dsn=NOMBRE)` o `execute (...) by motor` con un DSN escrito a mano, aunque el programa tenga un selector de entorno (R12).
- **Capa:** IR (nodo de conexión) y reglas de contexto.
- **Diseño Talend:** todas las conexiones salen del contexto activo (`tImpalaConnection` con variables de contexto). Ninguna conexión con DSN literal.
- **Frecuencia y ahorro:** T1: 12 consultas con DSN fijo. T2: 12 DSN fijos. T3: varias conexiones con DSN fijo (el análisis cita al menos cuatro líneas). Ahorro: 0 pasos. Es un riesgo de escritura en producción desde un entorno de prueba.
- **Estado:** parcial. `planner.py` (`_literal_dsn_warnings`) avisa en `unresolved` de cada DSN literal cuando el programa tiene selector de entorno. Pendiente: que el DSN de la conexión salga del contexto activo (tImpalaConnection con variables de contexto) y el aviso con severidad en el plan.
- **Variantes:** DSN por variable (correcto); DSN por literal que coincide con producción; DSN en una macro distinta de la que define el selector.
- **Riesgos:** alto. Un programa de certificación escribe en producción.
- **Prueba:** un programa con selector de tres entornos y una consulta con DSN de producción escrito a mano genera un aviso de alta severidad y ninguna conexión literal en el Job.

#### R14. Credenciales embebidas
- **Firma:** `proc pwencode in=...`; `signon ... pass="literal"` o `pass=` con una variable; `%let clave = <valor>` con nombre de clave o contraseña.
- **Capa:** IR (nodo de credencial), reglas de contexto y avisos.
- **Diseño Talend:** variable de contexto de tipo password o secreto del Remote Engine. Nunca el valor codificado.
- **Frecuencia y ahorro:** C1: 1 placeholder de clave. T1: 10 `signon` y 1 `pwencode`. T3: 22 `pass=` en sesiones. Ahorro: 0 pasos. Es un riesgo de seguridad.
- **Estado:** implementada. `context_rules.py` (`SECRET_NAME`, `pwencode`); `migration_planner/planner.py` (~1465: aviso "Credencial en claro o cifrada ... el valor no se copia al plan"); `domain/redaction.py`.
- **Variantes:** `pass=` con variable de entorno; `pwencode` sin `pass=`; clave en `%let` de primer nivel.
- **Riesgos:** `pwencode` es ofuscación, no cifrado: el valor debe tratarse como comprometido y rotarse.
- **Prueba:** un `%let` con nombre que contiene `pass` produce una variable de contexto password sin valor en el plan.

#### R15. Literales de negocio en filtros y fórmulas
- **Firma:** constantes en `where` o en expresiones sin nombre: un código (`= 9902`), un umbral (`>= 1129560`), un rango, una lista (`in (1.0, 3.0)`).
- **Capa:** traductor de expresiones y reglas de contexto.
- **Diseño Talend:** variables de contexto con nombre de negocio, o una tabla de reglas como lookup (ver R37).
- **Frecuencia y ahorro:** T1: 16 apariciones de un mismo código, 4 reglas con otro código, umbral en 2 líneas. T2: umbrales y rangos NID (§5, §22). T3: rangos de tipo de documento (P04). Ahorro: 0 pasos; evita cambios en varios sitios.
- **Estado:** pendiente. `migration_planner/expressions.py` traduce los literales tal cual; no los extrae a contexto.
- **Variantes:** el mismo valor escrito como `1.0` y `1`; literales de fecha; literales de texto con espacios finales.
- **Riesgos:** cambiar un valor en un solo sitio. El tipo (texto frente a número) cambia la comparación.
- **Prueba:** `where x = 9902` y `where y <> 9902` producen una variable de contexto `codigo_negocio` usada en ambas.

#### R16. Lista en macro variable e iteración
- **Firma:** `%do %while (%scan(&lista, &i, "|") ne); ... %end;`; secuencia `%let dataset1 = ...; ... %let dataset10 = ...;`; `select nombre into :tablas separated by "|"`.
- **Capa:** macro resolver, IR (operación de iteración), planificador.
- **Diseño Talend:** lista en contexto o `tFixedFlowInput` consumida por `tFlowToIterate` con `tRunJob` por elemento.
- **Frecuencia y ahorro:** C1: 8 bucles `%scan`, 30 asignaciones numeradas. Ahorro: 8 bucles y las asignaciones.
- **Estado:** pendiente. No existe `tFlowToIterate` en el planificador; el tipo de conexión `Iterate` solo está mapeado en `talend_adapter/apply_spec.py:129`.
- **Variantes:** lista separada por comas; lista con elementos vacíos (`archivo_1 = ;`); lista descubierta de un catálogo (R17).
- **Riesgos:** si un elemento contiene el separador, la lista se rompe. Una lista vacía no ejecuta el bucle y no avisa.
- **Prueba:** `%do %while (%scan(&l,&i,"|") ne)` sobre una lista de tres nombres produce un flujo de tres filas con `tFlowToIterate`.

#### R17. Parámetro leído de una fila
- **Firma:** `select col into :m from tabla_control;` seguido de uso de `&m`; `call symputx('nombre', valor)` dentro de un DATA step.
- **Capa:** IR (`set_variable`, `builder.py:419`), planificador.
- **Diseño Talend:** `tPreJob` con un `tImpalaInput` o `tFileInputDelimited` de una fila que escribe en contexto (`tJava` o `tContextLoad`).
- **Frecuencia y ahorro:** T1: 22 `INTO`, 11 de año, mes y día. T2: 6 `INTO` (3 pares de fecha, §27). C1: 33 `symputx`. Ahorro: 1 DATA step por parámetro.
- **Estado:** parcial. El `SELECT INTO` se conserva como `set_variable` en el IR. `symputx` dentro de un DATA step se clasifica como `variables_control` (`plumbing.py`) y no genera paso. No se genera el `tPreJob` con lectura de la fila.
- **Variantes:** `into :m1 - :mn` (varias filas); `symputx` con `'G'`; `ranuni` para identificadores.
- **Riesgos:** `into` con más de una fila asigna la última sin error. Hay que validar que hay exactamente una fila (R18).
- **Prueba:** `select a into :m from t;` con una variable que se usa después produce un parámetro de contexto y un paso de lectura de una fila.

#### R18. Precondición y gate de continuación
- **Firma:** `if conteo = 0 then abort cancel;` en un DATA step de control; comprobación `fileexist` con `%else %put WARNING`; `if variable no válida then ...` sobre un valor de ambiente.
- **Capa:** IR (condición de aborto), planificador.
- **Diseño Talend:** `tPreJob` con `tJava` que lanza excepción y `tDie`; `tFileExist` para ficheros obligatorios.
- **Frecuencia y ahorro:** T1: 2 gates de cero filas (P22). T3: 1 comprobación de existencia de tabla (P19). C1: 4 guardas de fichero. Ahorro: 0 pasos; convierte el aviso en error.
- **Estado:** parcial. `job_structure.py` añade `tDie` de error por Job. El gate de cero filas y el aviso de fichero no se generan como precondición.
- **Variantes:** `abort` sin condición; `%abort cancel`; comprobación de existencia de tabla con `SHOW TABLES`.
- **Riesgos:** un aviso que no detiene el Job degrada en silencio (ver R52 y el aviso A-08).
- **Prueba:** `if n = 0 then abort;` sobre un conteo produce un `tDie` en el `tPreJob` con el disparador `Run if`.

#### R19. Inclusión de utilidades externas
- **Firma:** `%include "<ruta absoluta>.sas";`; macros usadas que no están definidas en el archivo.
- **Capa:** macro resolver (`resolver.py`) e ingestión (`ingestion/importer.py`).
- **Diseño Talend:** las utilidades se sustituyen por routines Java o por contexto. No se migra un código que no se ha visto.
- **Frecuencia y ahorro:** C1: 10 `%include` y 7 macros externas sin definir. T1: 6 `%include` de configuración de entorno (una por copia, P24). T2: 1 (§26). T3: un `%include` por bloque de entorno (11 bloques). Ahorro: 0 pasos; marca la dependencia.
- **Estado:** parcial. Las rutas se resuelven con `resolver.py`; `dependency_graph/` modela dependencias. El tratamiento de una dependencia no resuelta no se ha verificado en un caso real.
- **Variantes:** `%include` relativo; `%include` de un fichero con varias macros; macro llamada pero no definida.
- **Riesgos:** sin el código de la utilidad, la semántica no se puede confirmar. Por ejemplo, la validación de entorno o la exportación.
- **Prueba:** un `%include` a una ruta absoluta sin fichero disponible produce una dependencia `no resuelta` y bloquea la traducción de las macros que la usan.

### Grupo C. Lógica fila a fila

#### R20. WHERE e IF de subconjunto
- **Firma:** `where ...;` en DATA step; `if condicion;` (subsetting); `create table ... as select ... where ...` sobre una sola tabla.
- **Capa:** IR (`filter`) y fusión.
- **Diseño Talend:** `Output filter` del tMap; `tFilterRow` solo si el filtro es lo único de la corriente.
- **Frecuencia y ahorro:** T1: 8 pares de filtros (ver R33). T2: unos 15 filtros puros (aprox.). C1: 1 bloque de filtro por entidad. Ahorro: 1 componente por filtro.
- **Estado:** implementada. `builder.py` (`add("filter", ...)`); `fusion.py` (`Output filter`).
- **Variantes:** `if` sin `then` en un MERGE (determina el tipo de join, no es filtro, `builder.py`); `where` con `and`/`or` mezclados; `where` con `is missing`.
- **Riesgos:** con un valor nulo, `= k` y `<> k` son falsos a la vez (ver R33 y A-06).
- **Prueba:** `data b; set a; where x > 0; run;` produce un tMap con `Output filter` `row.x > 0`.

#### R21. Proyección, renombrado y KEEP/DROP
- **Firma:** `keep`, `drop`, `rename=`; `select a.col1 as nuevo1 ... from ...` sin `where` ni `join`.
- **Capa:** IR (`select_columns`, `rename`, `project`) y fusión.
- **Diseño Talend:** esquema de salida del tMap, sin componente.
- **Frecuencia y ahorro:** T1: 19 pasos de "Organizar campos" y "Orden campos". C1: proyecciones dentro de cada bloque. Ahorro: 1 componente por paso.
- **Estado:** implementada. `fusion.py` (`select_columns`, `rename`, `project`); `migration_planner/pipeline.py` (`build_flow`).
- **Variantes:** `select *` (depende del orden de columnas); alias que no coincide con el nombre de la columna en una unión (R39).
- **Riesgos:** un alias mal escrito en una unión por nombre crea una columna nueva sin error.
- **Prueba:** `data b(keep=x rename=(y=z)); set a; run;` produce un tMap con dos columnas de salida y ningún `tFilterColumns`.

#### R22. Cadena de transformaciones fila a fila
- **Firma:** varios DATA steps o `create table` consecutivos sobre la misma corriente, cada uno con filtro, cálculo o renombre, y cada uno leído solo por el siguiente.
- **Capa:** planificador (`pipeline.py`, `fusion.py`).
- **Diseño Talend:** un único tMap por corriente; una cadena que no se puede fundir se parte.
- **Frecuencia y ahorro:** T1: la mayor parte de los 28 patrones. T2: 63 pasos de mutación se funden en cadenas (ver R23). T3: 21 etiquetas "Validar" son filtros sucesivos. Ahorro: el grueso de los pasos de datos.
- **Estado:** implementada. `pipeline.py` (`build_flow`); `fusion.py` (`merge_tmap`). Un intermedio con varios lectores se reparte con un tMap de varias salidas.
- **Variantes:** una operación que lee una columna que la cadena ya calculó no se funde (la cadena se parte); dos operaciones en la misma línea de origen (límite conocido, ver `docs/pipeline-fusion.md`).
- **Riesgos:** la fusión depende de que la columna calculada no se vuelva a leer en la misma pasada.
- **Prueba:** una cadena `filter`, `compute` y `rename` consecutivas produce un único tMap con `fused_from` con las tres operaciones.

#### R23. Mutación en sitio mediante tabla temporal (copia de vuelta)
- **Firma:** `data work.tmp; set X; col = expr; run; data X; set work.tmp; run; proc delete data=work.tmp; run;`. Variante: `set X(rename=(col=col_old))` con `drop col_old`.
- **Capa:** IR (fusión del par de DATA steps) y planificador.
- **Diseño Talend:** una asignación de columna en el tMap; sin temporal ni copia.
- **Frecuencia y ahorro:** T1: 82 bloques de copia de vuelta (65 con `input(left(...))`). T2: 63 pasos de mutación. T3: 11 entre conciliación, limpieza de texto y conversión de tipo. C1: no aplica. Ahorro: 2 DATA steps y un `proc delete` por asignación, en el total de los programas: más de 150 bloques.
- **Estado:** parcial. `migration_planner/copy_back.py` funde el bloque (también con `format`, `set X(rename=...)` y `drop` de la columna renombrada) en una escritura en sitio sobre X. `migration_planner/versions.py` encadena N bloques seguidos al grupo productor de X en un único tMap: las asignaciones que leen una columna ya calculada se sustituyen por su expresión, y una reasignación reemplaza a la anterior. Pendiente: varios bloques sobre una tabla externa siguen escribiendo cada uno (el último bloque es la salida real); las expresiones SAS que el traductor no soporta (p. ej. `input(left(x), 10.)`) quedan como expresión pendiente dentro del tMap.
- **Variantes:** copia de vuelta con `rename=` y `drop`; copia de vuelta de varias columnas; copia sin asignación (solo reordena columnas, no es conversión).
- **Riesgos:** si la expresión lee la columna que se reescribe, el orden cambia el resultado. Un DATA step de dos pasos legítimo (con `set` de otra tabla) no es copia.
- **Prueba:** `data w; set x; c = c*2; run; data x; set w; run; proc delete data=w; run;` produce un único tMap sobre `x` con `c = row.c * 2` y ningún temporal.

#### R24. Conversión de tipo
- **Firma:** `input(left(x), n.)` para texto a número; `put(x, Zn.)` para número a texto con ceros; `input(...)` seguido de `put(...)` (ciclo); `cast(x as ...)` en pass-through.
- **Capa:** traductor de expresiones y esquema de salida.
- **Diseño Talend:** tipo declarado en el esquema de salida del tMap (`Long`, `Integer`, `BigDecimal` o `String`); expresión de conversión con `trim`; el error de conversión va al flujo de rechazo.
- **Frecuencia y ahorro:** T1: 65 `input(left(...))`, 21 con `compress`, 15 conversiones consecutivas por fichero. T2: 11 `put`/`input` (§5). T3: 2 bloques (P10). Ahorro: copia de vuelta incluida en R23.
- **Estado:** parcial. `talend_translator.py` (`_input`, `_put`): `input` numérico se convierte con `Mathematical.REAL` y avisa "comprobar el informato"; `put` con `Zn` se convierte con `LPAD`. No hay tipo `Long`/`BigDecimal` en el esquema ni flujo de rechazo.
- **Variantes:** `input` con formato de fecha (ya cubierto por `_date_pattern`); `put` con `$`; conversión con longitud distinta en dos ramas.
- **Riesgos:** `input()` sin error devuelve missing si el texto no es numérico; un conversor Java lanza excepción. Hay que tratarlo como rechazo (ver A-09).
- **Prueba:** `x = input(left(v), 8.);` produce una columna `Long` con `trim` y un rechazo para el valor no numérico.

#### R25. Expresiones SAS de uso general
- **Firma:** `ifn`, `ifc`, `cat`, `cats`, `catx`, `substr`, `substrn`, `compress`, `round`, `int`, `length`, `missing`, `coalesce`, `between`, `in`, `is missing`, `like`.
- **Capa:** traductor de expresiones (`expressions.py`, `talend_translator.py`).
- **Diseño Talend:** expresión Java en la columna del tMap, con `StringHandling`, `Mathematical` y `ternario`.
- **Frecuencia y ahorro:** transversal a todos los patrones; cada expresión es un componente evitado si se funde.
- **Estado:** implementada. `talend_translator.py` (`_FUNCS` y `_guard`); `expressions.py` (`_FUNCTIONS`, `_FUNCTION_WARNINGS`).
- **Variantes:** función no soportada (queda como pendiente con motivo); `cat` que no quita espacios finales; `catx` con separador que omite vacíos.
- **Riesgos:** los blancos finales de SAS y los nulos de Java no son equivalentes (ver A-06 y A-09). `missing < 0` es verdadero en SAS.
- **Prueba:** `ifc(x = "", "x", x)` produce `x == null || x.isEmpty() ? ...`.

#### R26. Sustitución condicional: valor por defecto, coalesce y saneado
- **Firma:** `ifc(x = "", valor, x)`; `case when x = 0 or x = . then respaldo else x end`; `ifn(x < 0, 0, x)` sobre varias columnas (clamp); asignación de constante a columna nueva.
- **Capa:** traductor de expresiones y reglas de contexto (para el valor por defecto).
- **Diseño Talend:** expresión ternaria en el tMap; el valor por defecto va a contexto, no como literal repetido.
- **Frecuencia y ahorro:** T2: 21 clamps (7 columnas en 3 productos), 9 `ifc` de valor por defecto, 6 constantes (§4, §7). T1: 4 coalesce por CASE. T3: 3 bloques de imputación de ubicación (P06). Ahorro: una expresión por columna, sin pasos.
- **Estado:** implementada. `ifn`, `ifc`, `coalesce` y `coalescec` en `talend_translator.py`. El valor por defecto en contexto requiere R10 de reglas de contexto (parcial).
- **Variantes:** `coalesce` sobre cadena vacía; `ifn` con missing (A-06); clamp a cero de varias columnas (función auxiliar).
- **Riesgos:** un cero tratado como vacío (si cero es un valor válido en el origen, se pierde). `ifn(x<0,0,x)` convierte missing en 0 (cambia el conteo de no nulos).
- **Prueba:** `ifn(x < 0, 0, x)` sobre una columna con valores negativos, cero, positivos y missing: el aviso de missing se emite.

#### R27. Redondeo de SAS
- **Firma:** `round(x)` o `round(x, unidad)`; `format x best32.` asociado.
- **Capa:** traductor de expresiones.
- **Diseño Talend:** `BigDecimal.setScale(0, RoundingMode.HALF_UP)` (equivale al redondeo de SAS en los empates, incluidos negativos).
- **Frecuencia y ahorro:** T3: 24 llamadas a `ROUND` en 2 bloques (P11). T1 y T2: sin casos propios. Ahorro: 0 pasos.
- **Estado:** implementada. `talend_translator.py` (`_round`): ``-Math.round(-x)`` para negativos.
- **Variantes:** `round` con unidad; `round` sobre missing; `format` que cambia el tipo de salida.
- **Riesgos:** `Math.round` de Java lleva los empates hacia arriba (`-2.5` a `-2`), distinto de SAS (`-3`).
- **Prueba:** `round(-2.5)` produce `-3`.

#### R28. Partición de texto por longitudes acumuladas
- **Firma:** `substrn(catx(...), 1, l1)`; el segundo campo empieza en `l1 + 1`, el tercero en `l1 + l2 + 2`, y así sucesivamente; `substr(x, 1, 2)` y `substr(x, 3, 3)` para código de ubicación.
- **Capa:** traductor (rutina Java).
- **Diseño Talend:** rutina Java que devuelve los campos de una sola llamada, con las longitudes como entrada.
- **Frecuencia y ahorro:** T2: 12 pasos (§8) de cuatro campos en 3 productos. Ahorro: 12 pasos a 1 rutina.
- **Estado:** pendiente. `talend_translator.py` traduce `substrn` y `cats` en expresiones sueltas; no detecta la cadena acumulada ni genera la rutina.
- **Variantes:** longitud acumulada con desplazamiento de 1 o de 2; posición fija sobre un código.
- **Riesgos:** `substr` de posición fija falla si el código es más corto. Si la longitud es missing, toda la cadena es missing.
- **Prueba:** tres `substrn` en cadena, cada uno con la longitud del anterior más uno, producen una rutina con tres salidas y un test con nombre vacío.

#### R29. Normalización de texto con expresión regular y transliteración
- **Firma:** `prxchange('s/[^A-Za-z0-9, ]//', -1, ktranslate(x, 'AEIOU...', 'ÁÉÍÓÚ...'))`; `prxmatch` para validar caracteres.
- **Capa:** traductor (rutina Java).
- **Diseño Talend:** rutina `normalizaTexto(String)` con `Normalizer` (NFD) y una expresión regular explícita.
- **Frecuencia y ahorro:** T2: 3 bloques (§9). T3: 3 bloques con copia de vuelta (P09). Ahorro: 3 bloques y 3 copias a 1 rutina.
- **Estado:** pendiente. `prxchange`, `prxmatch` y `ktranslate` no están en `talend_translator.py`.
- **Variantes:** regex con clase de caracteres distinta; mapa de transliteración parcial; texto con codificación latin1.
- **Riesgos:** la codificación del origen cambia qué caracteres son tildes. Las expresiones regulares de SAS (PRX) y de Java no son idénticas en todo.
- **Prueba:** un texto con tilde, eñe y símbolo produce el mismo resultado en la rutina que en el SAS de referencia.

#### R30. Cálculo con vector de pesos (checksum)
- **Firma:** la misma secuencia de constantes (por ejemplo, 12 pesos decrecientes) aplicada a los dígitos de un campo, seguida de `mod(suma, 11)` y una regla de resto (`si resto > 1 entonces 11 - resto`).
- **Capa:** traductor (rutina Java).
- **Diseño Talend:** rutina `calcularDigito(String)` con el vector de pesos como constante; llamada desde el tMap con su condición (solo para el tipo que aplica).
- **Frecuencia y ahorro:** T2: 3 bloques (§20), con 2 sobrescrituras de la columna (ver R32). Ahorro: 3 expresiones largas a 1 rutina.
- **Estado:** pendiente. No hay detección de vectores de pesos ni de la regla de resto.
- **Variantes:** módulo 10 y 11; pesos distintos; el resultado se escribe en el mismo campo de entrada.
- **Riesgos:** `input(..., w1.)` devuelve missing si el carácter no es un dígito, y el resultado es missing sin error. Una versión de un motor puede tener una guarda de longitud que la otra no tiene.
- **Prueba:** un campo de 12 dígitos con un resultado conocido produce el dígito esperado en la rutina.

#### R31. Recodificación por tabla de códigos
- **Firma:** `x = ifn(x = "CC", 1, ifn(x = "CE", 2, ifn(x = "TI", 4, .)))`; `join` a una tabla de homologación con clave interna y código externo.
- **Capa:** traductor (lookup).
- **Diseño Talend:** `tMap` con lookup a una tabla de referencia (`tFileInputDelimited`), con su rechazo para el código no encontrado.
- **Frecuencia y ahorro:** T2: 1 `ifn` anidado (§6). T3: 3 bloques de homologación (P08). T1: catálogos Excel usados como lookup (P13). Ahorro: una cadena de `ifn` a una tabla.
- **Estado:** parcial. Los `join` con referencia se convierten en `Lookup` (`pipeline.py`); una cadena `ifn` anidada no se convierte en tabla.
- **Variantes:** `case` con literales; `homologación` con condición `or x = 0`.
- **Riesgos:** un cambio de tipo con el mismo nombre (texto a número) puede romper pasos que esperan texto. Un join con `or` puede generar producto cartesiano (ver A-10).
- **Prueba:** `ifn` anidado con tres códigos produce una tabla de tres filas y un lookup con rechazo.

#### R32. Constante incondicional sobre una columna calculada
- **Firma:** `x = 0;` o `x = "";` en un paso propio, sobre una columna que otro paso calcula; el mismo nombre aparece con dos asignaciones en el flujo.
- **Capa:** lint (detector), no traducción.
- **Diseño Talend:** no se traduce como paso. Si la intención es un valor por defecto, se convierte en condición explícita (ver R26).
- **Frecuencia y ahorro:** T2: 2 casos (§21). Ahorro: 0. Es un riesgo de decisión de negocio.
- **Estado:** pendiente. No hay detector de asignación literal incondicional sobre columna ya calculada.
- **Variantes:** constante sobre una columna de un registro concreto; constante en un paso etiquetado como "calcula campo".
- **Riesgos:** alto para el reporte: todos los registros afectados salen con valor 0 sin condición.
- **Prueba:** una columna calculada por una expresión y después `x = 0;` produce un aviso y ningún cambio en el tMap.

### Grupo D. Enrutamiento, joins y validación

#### R33. Partición complementaria por predicado
- **Firma:** dos consultas o pasos sobre la misma fuente con predicados que se excluyen (`x = k` y `x <> k`; `a in (...)` y `a = k`; `k1 between` y `k1 not between`); la misma lista de columnas en las dos.
- **Capa:** IR (grupo de particiones) y planificador (reparto).
- **Diseño Talend:** un tMap con N salidas, cada una con su `Output filter`. Un solo recorrido del origen.
- **Frecuencia y ahorro:** T1: 8 pares (16 apariciones). T2: 6 pares (§14). T3: 4 pares (P14). C1: 4 consultas por valor (P02). Ahorro: N-1 lecturas del origen.
- **Estado:** parcial. `pipeline.py` reparte un intermedio con varios lectores en un tMap con salida por lector. No detecta que los predicados son complementarios ni avisa del residuo.
- **Variantes:** tres o más valores (`case`); predicados de rango; el origen se lee dos veces con el mismo filtro.
- **Riesgos:** un valor nulo no cumple `= k` ni `<> k`; se pierde en silencio (ver A-06). Hace falta una salida de resto.
- **Prueba:** `x = 1` y `x <> 1` sobre la misma fuente producen un tMap con dos salidas y una tercera salida de resto con `x == null`.

#### R34. Enriquecimiento por join con referencia
- **Firma:** `left join ref on a.k = ref.k` o `inner join ref on a.k = ref.k`, con `ref` una tabla de referencia (fichero o base).
- **Capa:** IR (`join`) y planificador (`Lookup`).
- **Diseño Talend:** tMap con `Lookup`. "Load once" para referencias pequeñas; "Reload at each row" para grandes. "Unique match" si la clave es única. Si la referencia es grande, el join va al motor (R46).
- **Frecuencia y ahorro:** T1: 19 `left join` y 24 `inner join`. T2: 10 `connection to` con join en el motor. T3: joins a catálogos en la cadena de validación (P03). Ahorro: 1 componente de join por unión.
- **Estado:** parcial. `pipeline.py` convierte el `join` en `Lookup` para las entradas adicionales. No hay comprobación de unicidad de la clave de referencia.
- **Variantes:** join con clave compuesta; join con `cast` en ambos lados; join con `or`.
- **Riesgos:** una clave no única multiplica filas en silencio (ver A-10). Un join con `cast` en ambos lados puede impedir el índice del motor.
- **Prueba:** `left join` con clave única en la referencia produce un `Lookup` con `Unique match`; con clave repetida, avisa.

#### R35. Anti-join y semi-join por pertenencia
- **Firma:** `left join ref on ... where ref.k is missing` (anti); `inner join` de una tabla derivada de filtro sobre la fuente completa (semi); `where b.col is missing` tras `left join`.
- **Capa:** IR (`join` + `filter`), traductor (Lookup con rechazo).
- **Diseño Talend:** tMap con `Lookup`, `Join: Inner` y salida de rechazo (`Catch lookup inner join rejects`). Un solo paso en lugar de dos.
- **Frecuencia y ahorro:** T1: 39 `is missing` en joins (aprox., particiones en 3 bloques). T2: 1 anti-join y 3 semi-joins (§13). T3: un anti-join ("Identificar diferencias", P03). Ahorro: 1 join y 1 filtro por partición.
- **Estado:** pendiente. El tipo de conexión `Reject` existe en `talend_adapter/apply_spec.py:126` y `migration_planner/models.py:36`, pero el planificador no genera el flujo de rechazo.
- **Variantes:** anti-join con clave compuesta; semi-join que se comporta como filtro (no es filtro: trae todas las relaciones de cada clave, ver A-11).
- **Riesgos:** el anti-join con una columna con nulos reales da falsos positivos. El semi-join no es un filtro por fila.
- **Prueba:** `left join` seguido de `where r.k is missing` produce un tMap con salida de coincidencias y salida de rechazo sin join adicional.

#### R36. Validación campo a campo
- **Firma:** `col is missing or ...` (nulo); `col not between a and b` (rango); `col in (...)` (dominio); `(col = 0) or col is missing`.
- **Capa:** traductor de expresiones y planificador (salida de rechazo).
- **Diseño Talend:** expresión booleana por regla en el tMap con un motivo por regla; `tSchemaComplianceCheck` para tipo, longitud y nulidad obligatoria.
- **Frecuencia y ahorro:** T1: 39 `is missing`, 13 `not between`, 19 `between`. T3: 7 validaciones por población (P03). Ahorro: 1 consulta de rechazo por regla.
- **Estado:** parcial. `talend_translator.py` traduce `is missing` (l. 200), `between` (l. 219) e `in`; `not in`, `not between` y `like` también (l. 204, 228). No hay salida de rechazo con motivo.
- **Variantes:** rango abierto (un solo límite); dominio como lista; nulo en una sola columna.
- **Riesgos:** `not between` con nulo no selecciona la fila: la validación se pierde para los nulos si no hay regla de nulidad aparte (ver A-06).
- **Prueba:** tres reglas (nulo, rango, dominio) sobre la misma tabla producen tres expresiones en el tMap y un motivo por cada una en la salida de rechazo.

#### R37. Validación por tabla de reglas
- **Firma:** un bloque por valor de código con un rango distinto (`where t = 1 and n between a and b`); una lista de frases prohibidas con `contains` o `=`; longitud mínima; una regla por tipo de documento.
- **Capa:** IR (tabla de reglas), traductor (lookup a tabla de reglas).
- **Diseño Talend:** tabla de reglas (`tipo`, `minimo`, `maximo`, `modo`, `texto`, `tipo_regla`) cargada como lookup; una sola expresión en el tMap que aplica la regla del tipo de la fila.
- **Frecuencia y ahorro:** T2: 99 cláusulas `when` de dirección (§10). T3: 12 consultas más 2 uniones (P04). T1: 6 consultas por tipo (P09). Ahorro: 6 a 12 consultas y una unión por cada conjunto de reglas.
- **Estado:** pendiente. `contains` no se traduce (no está en `_FUNCS`). No hay tabla de reglas ni lookup por tipo.
- **Variantes:** regla que es lista (`in`) o que es rango; regla con `contains` sensible a mayúsculas; regla con `like` sin comodines.
- **Riesgos:** `contains` marca como inconsistente cualquier texto que contenga la subcadena (falso positivo); `like` sin comodines es igualdad exacta. Las listas no son iguales entre poblaciones: el mismo dato se valida de forma distinta.
- **Prueba:** una tabla de tres reglas por tipo con rangos y un lookup produce el mismo resultado que las tres consultas de referencia.

#### R38. Motivo de rechazo y unión de rechazos
- **Firma:** columna constante `motivo = 'TEXTO'` en cada consulta de rechazo; `CASE` con el motivo; las salidas de rechazo se apilan después.
- **Capa:** traductor (salida de rechazo con motivo) y planificador (`tUnite`).
- **Diseño Talend:** cada salida de rechazo del tMap lleva el motivo como columna calculada (no constante); un `tUnite` junta los rechazos con esquema común.
- **Frecuencia y ahorro:** T1: 13 asignaciones constantes de motivo (P06). T3: cadena de validación con motivo (P03). T2: 6 consultas de incidencia (§18). Ahorro: una copia por motivo.
- **Estado:** pendiente. Depende de R35 y R36 (no se genera la salida de rechazo). `tUnite` existe para unión de flujos (R39).
- **Variantes:** motivo que depende de la primera regla que falla (orden de reglas); motivo repetido en dos textos distintos.
- **Riesgos:** el motivo repetido en cada pipeline (cambiar un texto en varios sitios); un rechazo sin motivo es un fallo silencioso.
- **Prueba:** dos reglas con motivo distinto producen un rechazo con la columna `motivo` calculada y un `tUnite` que junta ambos.

#### R39. Unión de flujos con esquema parecido
- **Firma:** `select * from a outer union corr select * from b;`; `union all` con literal de origen; `set a b;` con varias entradas.
- **Capa:** IR (`union`) y planificador (`tUnite`).
- **Diseño Talend:** `tUnite` con esquema común. Las columnas que faltan en una rama se rellenan con `null` en el esquema o con un tMap previo.
- **Frecuencia y ahorro:** T1: 28 `outer union corr` y 2 `union all`. T2: 6 (§19). T3: 20 usos. Ahorro: 1 componente por unión.
- **Estado:** parcial. `sas_parser/sql.py` reconoce `outer union`; `builder.py` (~398) emite `union`; `planner.py` (~717) avisa de `union` sin `all`. El planificador mapea a `tUnite` ("Concatenar entradas"). No hay aviso de alineación por nombre ni de columna que falta.
- **Variantes:** `outer union corr` con columna extra en una rama; `union` sin `all` (distinto: quita duplicados); `set` con `by` (intercala ordenado).
- **Riesgos:** `corr` alinea por nombre: un nombre distinto crea una columna nueva sin error. `tUnite` no quita duplicados, como `outer union corr`.
- **Prueba:** dos flujos con las mismas columnas más una columna extra en uno: el `tUnite` tiene el esquema de la unión y avisa de la columna que no existe en la otra rama.

#### R40. Deduplicación por clave
- **Firma:** `proc sort ... nodupkey by k`; `proc sort ... nodup`; `select distinct ...`; `row_number() over (partition by k order by ...) ... where rn = 1`; `group by k having count(*) > 1`.
- **Capa:** IR (`dedupe`) y planificador (`tUniqRow`, `tAggregateRow`).
- **Diseño Talend:** `tUniqRow` con la clave (y "keep first" si el orden no importa); para el exceso de duplicados, `tAggregateRow` con conteo y tMap.
- **Frecuencia y ahorro:** T1: 7 `distinct` y 9 `group by`. T2: 2 ventanas `row_number` y 1 `nodupkey` (§11). Ahorro: 1 paso de orden y 1 de deduplicación.
- **Estado:** parcial. `builder.py` (~472, ~479) emite `dedupe` para `nodupkey` y `nodup`; `pipeline.py` (`_drop_redundant_sorts`) quita el `sort` previo cuando el `nodupkey` tiene la misma clave. `nodup` (todas las columnas) deja la clave pendiente. La ventana `row_number` no tiene tratamiento.
- **Variantes:** ventana sin orden total (el primero no está definido); `distinct` sobre todas las columnas (puede borrar duplicados legítimos).
- **Riesgos:** el orden de un `nodupkey` sin orden total es arbitrario. El `distinct` oculta duplicados que deberían contarse (ver R43).
- **Prueba:** `proc sort nodupkey by k; run;` precedido de `proc sort by k` produce un tUniqRow sin sort intermedio y una nota sobre el orden.

#### R41. Agregado por clave y conteo de incidencias
- **Firma:** `select k, count(*), sum(x) from t group by k;`; `select count(col) as 'etiqueta'n from t;`; `count(*) as n` sin `group by` que alimenta una tabla.
- **Capa:** IR (`aggregate`) y planificador (`tAggregateRow`).
- **Diseño Talend:** `tAggregateRow` con operación `count` o `sum` y agrupación por clave; el conteo de incidencias va a un `tFileOutputDelimited` o `tLogRow`.
- **Frecuencia y ahorro:** T1: 9 `group by`. T2: 6 contadores de incidencia (§17). C1: 4 `count(*)` sin consumidor (ver R02). Ahorro: 1 tabla intermedia por agregado.
- **Estado:** implementada. `planner.py` (`aggregate`, `GROUPBYS`, `_AGG`) emite `tAggregateRow`; `plumbing.py` (`_count_only`) descarta el conteo sin alias.
- **Variantes:** `count(col)` no cuenta nulos; etiqueta con espacios (nombre de columna especial); `sum` de missing.
- **Riesgos:** `count(col)` depende de la columna elegida (nulos). Dos etiquetas para el mismo concepto en el mismo reporte.
- **Prueba:** `select k, count(*) as n from t group by k;` produce un `tAggregateRow` con `GROUPBYS = k` y una columna `n`.

#### R42. Agregado y reunión de vuelta por umbral
- **Firma:** `select k, sum(a) as s from t group by k` seguido de `inner join` del agregado al detalle con `where s >= umbral`.
- **Capa:** IR (ventana por clave) y traductor (lookup a agregado).
- **Diseño Talend:** `tAggregateRow` por clave y un tMap con `Lookup` al agregado (cargado una vez); el umbral en contexto.
- **Frecuencia y ahorro:** T1: 2 casos con un umbral regulatorio (P16). Ahorro: 1 join y 1 tabla intermedia por caso.
- **Estado:** pendiente. Compone R41 y R34; no hay regla de ventana por clave.
- **Variantes:** umbral sobre dos sumas con `or`; agregado que se reúne por otra clave.
- **Riesgos:** el umbral es un literal (R15). El orden de saneamiento antes del agregado cambia el resultado.
- **Prueba:** suma por clave con umbral produce un tAggregateRow y un Lookup con filtro de salida sobre el umbral de contexto.

#### R43. Señal de incidencia por OR de condiciones
- **Firma:** `where (a < 0) or (b < 0) or (c < 0) ...`; `where (a >= 0) or (b >= 0) ...` (al menos una no negativa).
- **Capa:** traductor (bandera) y planificador (`tFilterRow` o salida del tMap).
- **Diseño Talend:** columna `flag` en el tMap (`row.a < 0 || row.b < 0 ...`) y filtro por la bandera hacia el control.
- **Frecuencia y ahorro:** T2: 3 bloques con 7 columnas (§15). T3: 2 bloques de negativos (P16) y 3 de monetarios (P17). Ahorro: el árbol de `or` a una bandera.
- **Estado:** parcial. `or` se traduce en `talend_translator.py`; no hay bandera ni regla que detecte un OR de la misma comparación sobre columnas distintas.
- **Variantes:** `or` con literal distinto por columna; conjunción con `and` (que se lee como "todos").
- **Riesgos:** un `or` con missing cuenta como negativo (`missing < 0` es verdadero). Dos reglas con `or` y `and` sobre las mismas columnas pueden contradecirse (ver A-12).
- **Prueba:** `where a < 0 or b < 0` produce una bandera en el tMap con `row.a < 0 || row.b < 0` y un filtro sobre la bandera.

#### R44. Conciliación de conteo y saldo
- **Firma:** `select count(*) from ...` y `select sum(x) from ...` en tablas de una fila, unidas por producto cartesiano (`from a, b, c`) sin condición; fórmula `diferencia = total - (parte1 + parte2 - repetidos)`.
- **Capa:** IR (nodo de conciliación) y planificador (`tAggregateRow`, `tJavaRow`, `tDie`).
- **Diseño Talend:** `tAggregateRow` por etapa (count y sum); un `tJavaRow` calcula las diferencias; `tDie` si la diferencia no es cero.
- **Frecuencia y ahorro:** T1: 14 `sum` y 15 `count`, 6 fórmulas (P17). T2: 3 cruces y 6 diferencias (§16). T3: 6 `concil` y 20 `count` (P12). C1: 4 conteos de control (P25). Ahorro: los cruces cartesianos y el `%put` de la diferencia.
- **Estado:** pendiente. Los conteos con alias se traducen como `aggregate` (R41), pero no hay control de diferencia ni `tDie`. El cruce cartesiano se trata como un `join` implícito (`builder.py`, "Join por coma") sin ningún control de filas vacías.
- **Variantes:** conteo con `count(col)` (no cuenta nulos); conciliación de registros con repetidos; fórmula distinta por población.
- **Riesgos:** el cruce cartesiano desaparece en silencio si una de las filas-resumen está vacía. El SAS solo imprime `ERROR` y no aborta (ver A-12).
- **Prueba:** un conteo de la entrada, un conteo de la salida y una diferencia distinta de cero producen un `tDie` con mensaje.

### Grupo E. SQL y motor (ELT)

#### R45. Pass-through de ejecución
- **Firma:** `proc sql; connect to motor (...); execute (...) by motor; disconnect from motor; quit;` con DDL o DML.
- **Capa:** IR (`sql_passthrough`) y planificador (`_engine_component`).
- **Diseño Talend:** `tImpalaRow` (o el Row del motor) con el SQL tal cual, en el contexto de conexión del Job.
- **Frecuencia y ahorro:** T1: 28 `connect to`, 19 `execute by`. T2: 48 `connect to impala` (incluye DDL de limpieza). T3: 49 `connect to`, 79 pass-through (incluye lectura, ver R46). C1: 12 bloques. Ahorro: 1 conexión por bloque (la conexión se comparte en el Job).
- **Estado:** implementada (ELT). `planner.py` asigna el componente Row del motor (`@engine.row` en `rules/mappings/talend-components.json`: tOracleRow, tTeradataRow, tMysqlRow...); el ELT de `migration_planner/elt.py` funde `create table <lib>.x as select ...` de un mismo motor en un solo `sql_passthrough`. Los Row documentados en `rules/talend/official-component-inventory.json` se aceptan (`job_structure.official_inventory_names`), porque el snapshot de paneles no los trae.
- **Variantes:** `execute (...)` con el motor al final; `execute by motor` sin paréntesis; `connect` y `disconnect` sueltos (la conexión la pone la estructura del Job).
- **Riesgos:** el DSN es literal (R13). Un `;` dentro del paréntesis puede romper el motor (ver A-24). Dialectos mezclados (ver A-23).
- **Prueba:** `execute (create table t as select ...) by motor;` produce un `tImpalaRow` con el SQL.

#### R46. Pass-through de lectura (ELT)
- **Firma:** `create table w as select * from connection to motor (select ...);`; `select count(*) into :m from connection to motor (show tables ...)`.
- **Capa:** IR y traductor (tImpalaInput).
- **Diseño Talend:** `tImpalaInput` con la consulta exacta (JOIN, CAST y ORDER BY dentro del motor). Sin ida y vuelta por el motor de SAS.
- **Frecuencia y ahorro:** T1: 9 `from connection to`. T2: 10 `connection to` (§12). T3: parte de los 79 pass-through. Ahorro: una lectura y una escritura intermedia por bloque.
- **Estado:** implementada. `intermediate_representation/builder.py` (`_passthrough_reads`) emite una lectura `passthrough` por `connection to <motor> (...)`; `planner.py` le asigna el componente de entrada del motor (tOracleInput...) con la consulta en QUERY. El caso "misma base, sin paso SAS intermedio" (`create table lib.x as select * from connection to ...`) aún no se funde en un Row.
- **Variantes:** lectura con `count` a macro variable (ver R17); lectura de catálogo con join y cast; lectura con `show tables` para comprobar existencia.
- **Riesgos:** un join con clave no única en el motor multiplica filas (A-10). El `cast` en ambos lados impide el índice.
- **Prueba:** `create table w as select * from connection to motor (select a.x, b.y from t a left join u b on a.k = b.k);` produce un `tImpalaInput` con la consulta tal cual y un `tMap` de salida.

#### R47. Ordenación posicional
- **Firma:** `order by 3 asc, 1 asc;` al final de un `create table ... as select`.
- **Capa:** traductor.
- **Diseño Talend:** `tSortRow` con las columnas nombradas, solo si el formato lo exige.
- **Frecuencia y ahorro:** T2: 34 `order by` (§29), en su mayoría posicionales. T3: 2 posicionales (P14). Ahorro: 0 pasos si el destino no exige orden.
- **Estado:** pendiente. `order by` aparece en `sql.py` y en `planner.py`, pero no hay tratamiento de posiciones numéricas.
- **Variantes:** `order by` con nombre; `order by` dentro de una subconsulta (costoso, sin uso).
- **Riesgos:** añadir una columna antes de la posición 3 cambia el orden sin error.
- **Prueba:** `order by 2;` sobre un `select` de tres columnas se traduce a `tSortRow` por el nombre de la columna 2.

#### R56. Composición de sentencias SQL en una consulta
- **Firma:** `create table w as select ...;` seguido de `create table t as select ... from w ...;`, donde `w` es un intermedio que solo lee esa sentencia. Una cadena de tres o más sentencias del mismo tipo es una sola consulta.
- **Capa:** planificador, antes del ELT (R45) y de la fusión a corriente. Módulo `migration_planner/sql_compose.py` (`compose_items`, `compose_statements`); las funciones SQL y su traducción por motor están en `rules/sas/sql-functions.json`.
- **Diseño Talend:** la cadena compuesta es una consulta `create table t as with w_cte as (select ...) select ... from w_cte`. Si todas sus tablas son de un mismo motor con componente Row, `elt.py` la convierte en UN `tXxxRow` con la consulta en QUERY. Si las tablas son WORK, la productora pasa al mismo grupo de la consumidora y sus operaciones se funden en un tMap, sin paso propio para la intermedia.
- **Estado:** implementada para los casos de arriba. Condiciones: la intermedia la escribe una sola sentencia y la lee una sola sentencia (con dos referencias en esa sentencia se usa un CTE compartido); no es tabla compartida con otro programa o macro; la sentencia consumidora sin JOIN ni UNION, salvo que todas sus tablas sean de un mismo motor; las funciones tienen estado `portable` o `translated` para el motor; no hay macro variables, `calculated`, `into :x`, ni ORDER BY, INTERSECT o EXCEPT en la productora; ninguna sentencia entre las dos escribe una tabla que la productora lee.
- **Motivos de rechazo:** se registran en `not_migrated` con categoría `composicion_sql`, agrupados por motivo. Los más frecuentes en el corpus de referencia: JOIN con tablas WORK (no se cablea el alias de la intermedia dentro del tMap) y funciones solo SAS (`cats`, `input`, `put`).
- **Riesgos:** las tablas de motor que el programa crea y lee dentro de sí misma se tratan como intermedias. Si otro proceso fuera del programa las lee, la composición las elimina: revisar antes de desplegar. El CTE de un motor que no admita WITH en `create table ... as` debe validarse en el dialecto concreto.
- **Prueba:** `tests/unit/test_sql_compose.py` (cadena de tres sentencias, CTE compartido, funciones y construcciones solo SAS, macro variables, ORDER BY, un Row por motor, determinismo).

### Grupo F. Ficheros y destino

#### R48. Lectura de Excel
- **Firma:** `proc import datafile='...xlsx' dbms=excelcs out=work.x replace; sheet=''; run;`
- **Capa:** IR (`read_file`) y traductor.
- **Diseño Talend:** `tFileInputExcel` con ruta de contexto, cabecera en la fila 1, todas las columnas como `String` y un tMap posterior que tipa.
- **Frecuencia y ahorro:** T1: 5 `PROC IMPORT EXCELCS`. Ahorro: 0 pasos; el catálogo se lee una vez y se usa como lookup (R34).
- **Estado:** pendiente. `builder.py` (~509) reconoce `import` como `read_file`; no distingue Excel ni genera `tFileInputExcel`.
- **Variantes:** `dbms=xlsx`; hoja vacía (la primera hoja); columnas en otro orden.
- **Riesgos:** `sheet=''` toma la primera hoja sin avisar. Un cambio de orden de columnas no genera error.
- **Prueba:** `proc import datafile='x.xlsx' dbms=excelcs ...` produce un `tFileInputExcel` con la ruta de contexto.

#### R49. Lectura delimitada sin cabecera
- **Firma:** `proc import datafile='...' out=work.x dbms=dlm replace; delimiter=';'; getnames=no; run;`
- **Capa:** IR (`read_file`) y traductor.
- **Diseño Talend:** `tFileInputDelimited` con separador, cabecera 0 y esquema explícito con nombres de negocio desde el primer paso.
- **Frecuencia y ahorro:** T1: 4 `PROC IMPORT DBMS=DLM` sin cabecera. Elimina el renombrado posterior (R21).
- **Estado:** parcial. `builder.py` (~509) y `planner.py` (~876-881) tratan `read_file`; no se genera el esquema explícito con `getnames=no`.
- **Variantes:** delimitador por nombre (`coma`, `pipe`); codificación del fichero; extracto con columnas posicionales `VARn`.
- **Riesgos:** sin cabecera, la posición es la única referencia; un cambio en el extracto rompe el mapeo sin error.
- **Prueba:** `proc import ... dbms=dlm; delimiter=';'; getnames=no;` produce un `tFileInputDelimited` con separador `;` y cabecera 0.

#### R50. Escritura a fichero y copia a ruta remota
- **Firma:** `proc export data=work.x outfile='...' dbms=dlm replace;` seguido de `rsubmit ... proc upload infile=... outfile='\\servidor\...'; endrsubmit;`.
- **Capa:** IR (`write_file`) y planificador.
- **Diseño Talend:** `tFileOutputDelimited` que escribe directamente en la ruta UNC del contexto, sin export local ni subida. Si hace falta copia local, `tFileCopy`.
- **Frecuencia y ahorro:** T3: 22 pares export y upload. Ahorro: 22 pares de sentencias y la sesión de subida (R04).
- **Estado:** implementada para el par export + upload exacto. `intermediate_representation/remote.py` funde `proc export outfile=A` + `proc upload infile=A outfile=B` en un `write_file` a B; la subida queda como `transferencia_remota` en `not_migrated`. Sin par exacto, la subida sigue sin traducir.
- **Variantes:** export sin subida; subida de varios ficheros en el mismo `rsubmit`; ruta con separador de Windows.
- **Riesgos:** credenciales de la sesión (R14). Rutas UNC y servidor en el código (pasan a contexto).
- **Prueba:** un `proc export` seguido de `proc upload` al mismo nombre produce un `tFileOutputDelimited` a la ruta de contexto y ninguna sesión.

#### R51. Carga a tabla destino
- **Firma:** `create table lib.t as select ...` o `insert into lib.t select ...`; carga por bloques con `proc append`; carga por comando externo (R06).
- **Capa:** IR (`write`, con modo `replace` o `append`, `builder.py` ~425-431) y planificador.
- **Diseño Talend:** `tImpalaOutput` (o `tDBOutput`) en modo lote con "Batch size" y "Commit every"; la acción de tabla (R08) sustituye el DDL previo.
- **Frecuencia y ahorro:** C1: 4 escrituras por carga. T1: 6 puntos de escritura. T3: 11 bloques de carga (P01). Ahorro: 1 escritura por carga; el troceo se elimina (R05).
- **Estado:** parcial. El IR conserva el modo `replace` o `append`. No se ha verificado que el planificador genere `tImpalaOutput` con la acción de tabla correspondiente.
- **Variantes:** `proc append base= data=` con la misma tabla (datos de prueba: descartar); escritura a fichero (R50).
- **Riesgos:** sin transacción, un fallo a mitad deja la tabla parcial (ver R08 y R07).
- **Prueba:** `create table lib.t as select ...;` produce un `tImpalaOutput` con acción de tabla "Drop and create".

### Grupo G. Avisos de calidad del código

#### R52. Definiciones de macro divergentes
- **Firma:** dos `%macro` con el mismo nombre y cuerpo distinto; llamadas que usan la última definición.
- **Capa:** IR (`builder.py`, ~684).
- **Diseño Talend:** no se fusionan. Cada definición distinta es un Job hijo o una variante `_v2`, con aviso.
- **Frecuencia y ahorro:** C1: 4 copias con cambios (P05). T1: 6 copias con un `%let` duplicado. T2: 13 bundles con diferencias de DSN y de rutas. Ahorro: 0. Es un aviso.
- **Estado:** implementada. `builder.py` (~684): "Otra definición de %x con cuerpo distinto ... SAS usa la última definición compilada; confirmar cuál aplica."
- **Variantes:** diferencia de un solo literal; diferencia de una condición de negocio.
- **Riesgos:** una corrección que se aplica a una copia y no a las demás.
- **Prueba:** dos `%macro` con el mismo nombre y cuerpos distintos producen dos variantes `_v2` y un aviso.

#### R53. Semántica de missing en comparaciones
- **Firma:** `x < 0` (verdadero si x es missing); pares complementarios sin residuo (`= k` y `<> k`); `not between` con nulo; `in` sobre una columna sin tipo.
- **Capa:** traductor de expresiones (`expressions.py`, avisos).
- **Diseño Talend:** aviso con la línea y la regla; la salida de resto (R33) o el control de nulo explícito.
- **Frecuencia y ahorro:** T2: clamp en 21 columnas (R26). T1: 8 pares complementarios (R33). Ahorro: 0. Es un aviso de calidad.
- **Estado:** parcial. `expressions.py` avisa de `ifn`/`ifc` con missing, `missing()` y `in` sobre columna sin tipo (`unsafe_comparison`). No detecta los pares complementarios sin residuo.
- **Variantes:** `is missing` frente a `= ''` en texto (vacío y nulo no son iguales en Java).
- **Riesgos:** cambia el conteo de no nulos; un registro desaparece de las dos salidas.
- **Prueba:** un par `x = 1` y `x <> 1` sin salida de resto produce el aviso de residuo.

#### R54. Conversión que devuelve missing sin error
- **Firma:** `input(texto, n.)` sobre texto no numérico; `put` de un missing; longitudes distintas para la misma columna en dos pasos (`8.` frente a `20.`).
- **Capa:** traductor de expresiones.
- **Diseño Talend:** la conversión falla al rechazo (R24) y se avisa de la longitud inconsistente.
- **Frecuencia y ahorro:** T1: 65 conversiones. T2: 11. Ahorro: 0. Es un aviso.
- **Estado:** parcial. `talend_translator.py` (`_input`) avisa de la conversión numérica con `Mathematical.REAL`; no detecta longitudes inconsistentes en una columna.
- **Variantes:** `input` a fecha con formato no reconocido; `put` a texto con ancho menor que el valor.
- **Riesgos:** un valor truncado o missing pasa sin error al reporte.
- **Prueba:** la misma columna convertida con `8.` y `20.` en dos pasos produce el aviso de longitud.

#### R55. Join con clave no única
- **Firma:** `left join` o `inner join` a una referencia donde la clave puede repetirse (varias direcciones por cliente); join con `or` en la condición; join por coma sin condición.
- **Capa:** IR (`join`) y planificador (`Lookup`).
- **Diseño Talend:** `Lookup` con `Unique match` solo si la unicidad se comprueba; si no, desduplicar la referencia antes (R40) o avisar.
- **Frecuencia y ahorro:** T1: 43 uniones. T2: joins al maestro de clientes sin desduplicar (§12). T3: join con `or` (P08). Ahorro: 0. Es un aviso de corrección.
- **Estado:** pendiente. No hay comprobación de unicidad de la clave de la referencia ni del `or`.
- **Variantes:** clave compuesta con una parte repetida; join de tipo de cuenta por una columna que no es la clave.
- **Riesgos:** multiplica filas en silencio; el SAS no avisa.
- **Prueba:** un `left join` a una referencia con clave repetida en los datos de prueba produce aviso y el recuento de filas duplicadas.

---

## 3. Tabla priorizada

Orden por impacto y esfuerzo. Impacto: bloques SAS que desaparecen en Cod1 y Cod2, estimación a partir de los conteos de cada análisis. Esfuerzo: S (pequeño), M (medio), L (grande). Las 12 primeras reglas pendientes o parciales forman la **siguiente tanda**. Las filas marcadas con `*` son las de la siguiente tanda.

| Prioridad | Regla | Impacto (estimación) | Esfuerzo | Capa | Estado |
|---|---|---|---|---|---|
| 1 * | R01 Wrappers de IDE | Muy alto: más de 250 llamadas y cabeceras; 0 pasos | S | lexer, planificador | parcial |
| 2 * | R23 Mutación en sitio con temporal | Muy alto: más de 150 bloques | M | IR, planificador | parcial |
| 3 * | R13 DSN literal | Riesgo muy alto (producción); 0 pasos | S | IR, contexto | pendiente |
| 4 * | R50 Export y copia remota | Alto: 22 pares | S | IR, traductor | parcial |
| 5 * | R45 Pass-through de ejecución | Alto: decenas de bloques | S | IR, planificador | parcial |
| 6 * | R39 Unión con esquema parecido | Alto: unas 56 uniones | S | IR, planificador | parcial |
| 7 * | R34 Join con referencia | Alto: más de 40 joins | S | IR, planificador | parcial |
| 8 * | R04 Sesiones remotas | Alto: decenas de sesiones | M | IR | pendiente |
| 9 * | R46 Pass-through de lectura | Alto: 10 a 79 lecturas | M | IR, traductor | pendiente |
| 10 * | R33 Partición complementaria | Alto: 18 pares | M | IR, planificador | parcial |
| 11 * | R36 Validación campo a campo | Alto: más de 70 reglas | M | traductor | parcial |
| 12 * | R37 Validación por tabla de reglas | Alto: más de 110 consultas y cláusulas | M | IR, traductor | pendiente |
| 13 | R35 Anti y semi-join con rechazo | Alto: decenas de particiones | M | traductor | pendiente |
| 14 | R38 Motivo y unión de rechazos | Medio-alto | M | traductor | pendiente |
| 15 | R03 Orquestación de SO | Alto: 16 bloques en C1, 13 en T2 | S | planificador | parcial |
| 16 | R07 Borrado de temporales | Alto: más de 100 bloques | S | planificador | implementada |
| 17 | R06 Macro de carga como fontanería | Muy alto: miles de líneas | S | planificador | implementada |
| 18 | R05 Troceado por ventanas | Alto | S | planificador | implementada |
| 19 | R09 Copias idénticas de macros | Alto: el 60 % a 80 % del programa | S | IR | implementada |
| 20 | R02 Trazas y conteos | Medio-alto: más de 100 `%put` | S | planificador | implementada |
| 21 | R12 Selector de entorno | Alto: unos 30 selectores | S | contexto | implementada |
| 22 | R14 Credenciales | Riesgo muy alto | S | contexto, avisos | implementada |
| 23 | R20 WHERE e IF | Medio | S | IR, tMap | implementada |
| 24 | R22 Cadena fila a fila | Muy alto | M | planificador | implementada |
| 25 | R21 Proyección y renombrado | Medio: 19 pasos | S | tMap | implementada |
| 26 | R41 Agregado por clave | Medio | S | traductor | implementada |
| 27 | R40 Deduplicación | Medio | S | IR, planificador | parcial |
| 28 | R24 Conversión de tipo | Alto: 65 `input` | M | traductor | parcial |
| 29 | R43 OR de incidencia | Medio | S | traductor | parcial |
| 30 | R10 Joblet de bloque repetido | Medio | M | planificador | implementada (límites) |
| 31 | R44 Conciliación | Medio-alto (control) | M | traductor, tDie | pendiente |
| 32 | R17 Parámetro de una fila | Medio: 22 `into` | S | contexto | parcial |
| 33 | R16 Listas e iteración | Medio | M | planificador | pendiente |
| 34 | R15 Literales de negocio | Medio | M | contexto | pendiente |
| 35 | R11 Placeholders | Medio: 28 | S | contexto | parcial |
| 36 | R19 Utilidades `%include` | Medio | S | macro resolver | parcial |
| 37 | R08 DROP previo | Medio | S | traductor | parcial |
| 38 | R51 Carga a destino | Medio | S | traductor | parcial |
| 39 | R49 Lectura delimitada | Bajo-medio | S | traductor | parcial |
| 40 | R48 Lectura Excel | Bajo | S | traductor | pendiente |
| 41 | R25 Expresiones SAS | Transversal | S | traductor | implementada |
| 42 | R26 Valor por defecto y clamp | Medio | S | traductor | implementada |
| 43 | R27 Redondeo | Bajo | S | traductor | implementada |
| 44 | R28 Partición por longitudes | Medio: 12 pasos | M | rutina | pendiente |
| 45 | R29 Normalización de texto | Bajo | S | rutina | pendiente |
| 46 | R30 Checksum | Medio: 3 bloques | M | rutina | pendiente |
| 47 | R31 Recodificación | Bajo | S | lookup | parcial |
| 48 | R42 Agregado con umbral | Bajo, alto impacto regulatorio | M | lookup | pendiente |
| 49 | R47 Orden posicional | Bajo-medio: 34 `order by` | S | traductor | pendiente |
| 50 | R18 Gate y precondición | Bajo | S | tPreJob | parcial |
| 51 | R32 Constante incondicional | Bajo, riesgo alto | S | lint | pendiente |
| 52 | R52 Macros divergentes | Bajo (aviso) | S | IR | implementada |
| 53 | R53 Semántica de missing | Bajo (aviso) | S | traductor | parcial |
| 54 | R54 Conversión con missing | Bajo (aviso) | S | traductor | parcial |
| 55 | R55 Join con clave no única | Bajo (aviso), riesgo alto | M | IR, planificador | pendiente |

Resumen de estado: 16 implementadas, 22 parciales, 17 pendientes.

---

## 4. Diseño objetivo agregado

### Cod1 (programa de carga masiva)
- **Lo que queda:** un Job de carga con el contexto del entorno (R12, R14), una precondición (R11, R18) y una corriente por entidad.
- **Componentes:** `tImpalaInput` (lectura de la fuente, R46 si es ELT), un `tMap` por entidad (R20 con `Output filter`, R33 como salidas), `tImpalaOutput` en modo lote con acción de tabla (R51, R08), `tAggregateRow` y `tJavaRow` con `tDie` para la conciliación de conteos (R44), y `tDie` de error.
- **Conteo esperado:** 1 Job, unos 20 a 25 componentes, sin macros, sin shell, sin sesiones y sin troceo. Coincide con la estimación del análisis (unos 23 componentes).
- **Lo que no pasa:** las cuatro copias del programa (R09) y las 6 macros de fontanería (R06).

### Cod2 (programa de conciliación regulatoria)
Los tres análisis de tramo proponen entre 3 y 5 Jobs cada uno, con un joblet en dos de ellos. Unidos, la estructura queda así (diseño propio, no del análisis):

1. **J00 Orquestador.** `tPreJob` con gate (R18), entorno (R12) y lectura de parámetros de una fila (R17). `tFlowToIterate` sobre la lista de segmentos (R16) con `tRunJob` hacia J10. Después J30 y J40.
2. **J10 Segmento (un solo Job, lanzado una vez por segmento).** Los tres segmentos tienen el mismo pipeline (T3, conclusión 2). Se parametriza con `context.segmento` y una tabla de reglas por segmento (tipo de cuenta, reglas de número de documento, listas de frases). Dentro:
   - Lectura ELT (R46) con el join y el cast en el motor, y lectura de catálogos Excel (R48) o delimitados (R49) como lookup (R34).
   - Un tMap grande con: filtros de salida (R20), clamp, default y coalesce (R26), partición de texto (R28, rutina), normalización (R29, rutina), checksum (R30, rutina), recodificación (R31), conversión (R24), validación de ubicación (R37), validación de documento (R37), razón social (R26) y bandera de incidencia (R43).
   - Salidas: sabana (con partición complementaria, R33), rechazos por motivo (R35, R38) y bandera de incidencias.
   - `tUnite` de rechazos (R39).
   - Un joblet solo si queda un bloque de lógica repetido dentro del Job (R10). Con los tres segmentos en un Job parametrizado, no hace falta.
3. **J30 Control.** `tAggregateRow` por etapa (R41), un `tJavaRow` con las diferencias (R44) y `tDie` si una no es cero.
4. **J40 Salida y carga.** `tFileOutputDelimited` directo a la ruta UNC del contexto (R50), un `tImpalaOutput` por tabla de carga con acción de tabla (R51, R08). Sin troceo (R05), sin sesiones (R04), sin shell (R03).

**Conteo esperado para Cod2 (estimación):** 4 Jobs (J00, J10, J30, J40), 1 joblet como máximo, unos 30 a 40 componentes en total. Es una estimación: los tres análisis proponen unos 20, 20 y 28 componentes por tramo, y el número final depende de la validación de cada regla.

**Conjunto de los dos programas (estimación):** unos 5 Jobs y unos 50 a 65 componentes. El mínimo ideal de un Job solo se alcanza con Cod1.

### Cómo se parametrizan los segmentos repetidos
- Un valor de contexto por segmento (`segmento`), y una tabla de reglas con las diferencias: nombres de columna de salida, listas de frases, rangos, códigos de tipo de cuenta.
- Las diferencias que son de negocio, no de nombre, no se parametrizan en silencio. Por ejemplo, una validación que existe en un segmento y en otro no, o una fórmula de conciliación distinta. Se registran como aviso (R52, A-07) y se deciden antes de migrar.
- La divergencia de nombres de columna entre segmentos (un campo de motivo llamado de dos formas) se unifica en la tabla de reglas y el aviso queda registrado.

---

## 5. Avisos de migración

Lista genérica de avisos que el migrador debe emitir. No se copian al Job; cada uno aparece en el plan con su línea SAS. Entre paréntesis, la regla donde se detecta y su estado.

- **A-01. Credencial embebida.** Contraseña codificada (`pwencode`) o literal en una sesión o en una variable. Detectable por nombre de variable y por el token `pwencode`. Acción: rotar y no copiar el valor. (R14, implementada)
- **A-02. Conexión a entorno fijo.** Un DSN o host escrito a mano dentro de un programa que tiene selector de entorno; el programa puede escribir en producción desde otro entorno. Detectable por comparación del DSN literal con la rama del selector. (R13, pendiente)
- **A-03. Selector de entorno sin rama.** La variable de entorno puede no coincidir con ninguna rama; el valor queda vacío y el fallo aparece más tarde. Detectable en la cadena `%if`. (R12, implementada; la validación en tPreJob, pendiente)
- **A-04. Predicado probablemente invertido.** En una familia de validaciones con la misma plantilla, un miembro usa `between` y los demás `not between`. Detectable por la comparación de plantillas entre bloques hermanos. (R37, pendiente)
- **A-05. Rama muerta.** Una condición con dos límites excluyentes (`x < a and x > b` con `a` menor que `b`) nunca se cumple. Detectable con análisis de rangos sobre literales. (R36, pendiente)
- **A-06. Missing en comparaciones.** `x < 0` es verdadero si `x` es missing; `= k` y `<> k` excluyen el nulo a la vez; `not between` excluye el nulo. Detectable en las expresiones y en los pares complementarios sin residuo. (R53, parcial)
- **A-07. Divergencia entre copias.** Dos bloques casi iguales con un literal, una columna, un `distinct` o una condición distintos. Detectable con la huella normalizada y su diferencia. (R09 y R52, implementadas)
- **A-08. Fallo silencioso que solo se imprime.** Un control que escribe un `ERROR` en el log y no aborta; un `abort` que no deja código de salida; un gate sin `tDie`. Detectable por `%put` con `ERROR` sin cambio de flujo. (R18 y R44, parcial y pendiente)
- **A-09. Conversión que devuelve missing.** `input` o conversión numérica sobre texto no numérico; longitud distinta de la misma columna en pasos distintos. Detectable por la función y por la comparación de formatos entre pasos. (R54, parcial)
- **A-10. Join que multiplica filas.** Una referencia con clave repetida, un join con `or` en la condición o un join por coma sin condición. Detectable en la condición y en la unicidad de la clave cuando se conoce. (R55, pendiente)
- **A-11. Semi-join que se usa como filtro.** Un join con una tabla derivada de filtro trae todas las filas que comparten la clave, no solo las del filtro. Detectable por el patrón de tabla derivada más join a la fuente. (R35, pendiente)
- **A-12. Conciliación sin control.** Un cruce cartesiano de filas-resumen sin `tDie`; si una fila-resumen está vacía, la conciliación desaparece. Detectable por `count` o `sum` sin `group by` en un `from` con varias tablas. (R44, pendiente)
- **A-13. Borrado tras fallo sin condición válida.** Un `drop ... purge` o un `proc delete` que se ejecuta según una variable que no refleja el fallo real de la base. Detectable por la condición del `if` anterior al borrado. (R07 y R08, implementadas parcial)
- **A-14. Nombre de columna distinto en una unión.** Dos ramas de una unión por nombre con el mismo concepto y distinto nombre; la unión crea dos columnas. Detectable comparando los nombres de columna de los flujos de `tUnite`. (R39, parcial)
- **A-15. Orden posicional.** `order by n` cambia si se modifica la lista de columnas. Detectable por `order by` con números. (R47, pendiente)
- **A-16. Código que no se ejecuta.** Macros definidas y no llamadas; llamadas comentadas. Detectable por el grafo de llamadas. (R19, parcial)
- **A-17. Determinismo de la ventana.** Una ventana `row_number` o un `nodupkey` cuyo orden no es total; el primero de cada grupo no está definido. Detectable si el `order by` de la ventana es igual a la partición. (R40, parcial)
- **A-18. Dialectos mezclados.** El mismo cast con dos tipos distintos (`varchar(n)` frente a `string`) o un `like` sin comodines frente a `contains` en otro motor. Detectable por tokens propios de cada motor. (R45, parcial)
- **A-19. Punto y coma dentro de un pass-through.** Un `;` antes del paréntesis de cierre de un `execute` o de un `connection to` puede romper el motor. Detectable por el texto del pass-through. (R45, parcial)
- **A-20. Ramas vacías.** Una rama de validación con solo un comentario: si se activa, la consulta es inválida. Detectable por ramas sin sentencias. (R18, parcial)
- **A-21. Datos de cabecera.** Usuario, servidor y rutas en comentarios generados; no deben copiarse. Detectable por la cabecera de generación. (R01, parcial)
- **A-22. Ruta o servidor fijo.** Rutas absolutas y nombres de servidor en el código; pasan a contexto. Detectable por rutas absolutas en literales. (R13 y R50, pendiente)
- **A-23. Diferencia en codificación.** Un fichero leído en otra codificación cambia qué caracteres son tildes en un `ktranslate`. Detectable por el texto de la expresión y la codificación del origen. (R29, pendiente)
- **A-24. Regla con dos valores para la misma cosa.** La misma regla de negocio con dos literales o dos longitudes en dos sitios. Detectable por la comparación de literales de un mismo campo. (R15, pendiente)

### Trazabilidad de los hallazgos en el corpus (para verificar)
Estas instancias están en los análisis y sirven para validar los avisos sobre los programas reales. No se traducen.
- Cod1 L881-882 (A-01): placeholder de clave en la llamada de exportación.
- Cod2 T1 L77 (A-01): `pwencode`; T3 P02 (A-01): 22 sesiones con `pass=`.
- Cod2 T1 L3237-3239 y L6780 (A-07 y A-06): etiquetas de inconsistencia con texto distinto por población.
- Cod2 T1 L7032 frente a la validación de tipo de cuenta de las otras poblaciones (A-07): columna de motivo con nombre distinto.
- Cod2 T1 L8004-8006 (A-09): longitud `8.` frente a `20.` para la misma columna.
- Cod2 T1 L6137 frente a L3621 (A-10): join por relación frente a join por cuenta, uno produce producto cartesiano.
- Cod2 T1 L2668-2669 y L5184-5185 (A-19): `;` dentro del pass-through.
- Cod2 T2 L15744 y L15030 (A-04 y R32): sobrescritura de un campo calculado con cero.
- Cod2 T2 L16109 frente a L16148-16229 (A-04): la validación de un tipo usa `between` y las demás `not between`.
- Cod2 T2 L15028-15031 (R32): placeholder sobre una columna que después se recalcula.
- Cod2 T3 L17870 y 17897, 21043 y 21070, 22208 y 22236 (A-05): condición de rango imposible.
- Cod2 T3 L17791-17794 y 20963-20968 (alias ambiguo): nombres de tabla usados donde ya hay alias.
- Cod2 T3 L23605-23608 (A-10): join con `or` que puede generar producto cartesiano.
- Cod2 T3 L17051-17058 frente a L17789-17794 (A-07): dos anti-joins con clave distinta.

---

## Anexo. Método y limitaciones

- Los conteos vienen de los análisis (búsqueda con `grep` sobre cada tramo). Las sumas entre tramos son aproximadas porque cada análisis usa su propio criterio para contar bloques y apariciones.
- Los estados se comprobaron en `src/sas_grid_migrator/` leyendo los ficheros indicados. No se ejecutaron pruebas nuevas. Una regla marcada como implementada tiene el código que lo indica; no significa que cubra todas las variantes de la columna "Variantes".
- Los ahorros en pasos son estimaciones. Las líneas de código fuente de los programas no se han medido en Talend.
- Pruebas existentes que cubren áreas de este catálogo (para ampliar, no para duplicar): `tests/unit/test_pipeline_fusion.py` (R20 a R22), `test_macro_dedupe.py` (R09), `test_joblets.py` (R10), `test_expressions_functions.py` y `test_talend_translator.py` (R24 a R27, R36), `test_security.py` (R14), `test_sas_studio_helpers.py` (R01), `test_planner.py` y `test_component_migration_coverage.py` (R41, R45, R51).
- Caso sintético genérico de cada regla: las pruebas de este catálogo describen un SAS mínimo con nombres genéricos (`a`, `b`, `k`, `x`). No se han creado ficheros de prueba en esta tarea.
