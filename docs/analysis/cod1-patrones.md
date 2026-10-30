# Análisis de patrones: Cod1.txt (2.904 líneas)

Fuente: `C:\Users\USUARIO_BISOLUTION1\Downloads\Cod1.txt`. Las líneas citadas son del archivo original. Los nombres de tablas, macros y rutas aparecen solo como evidencia.

## 0. Visión general

El archivo contiene un programa de carga masiva de tablas SAS a un destino Impala (landing zone, LZ) más dos transferencias a S3, todo repetido por entidad:

- Bloque de preparación de datos de prueba (líneas 1-119).
- Cuatro copias idénticas del programa de carga (ACURA 136-769, BMW 899-1531, CHEVROLET 1612-2245, JAGUAR 2262-2895). Un `diff` confirma que difieren solo en un salto de línea (líneas 605-606). Son unas 2.500 de 2.904 líneas.
- Exportación a S3 (879-882) e importación desde S3 (1593-1595).
- Cierre con temporizador (2897-2902).

Hay 19 marcadores `/* Etiqueta: ... */` (tareas de SAS Studio concatenadas en serie). Las macros `ambiente`, `exportar_s3`, `importar_s3`, `countTableSas`, `countTableLz`, `showMessage`, `web_drop_table`, `web_open_table` y `select_bucket_s3*.sas` no están definidas en el archivo. Se resuelven fuera (vía `%include` o en el entorno de ejecución). El migrador no puede verificar su comportamiento con este archivo solo.

Conteos verificados con búsqueda: `options no...` 52; `%showMessage` 40; `%put` 101; `symputx` 33; `%include` 10; `sleep` 4; `filename ... pipe` 8; tokens `rsubmit/signon` 16; `ceilz` 8; `NO TIENE REGISTROS` 8; placeholders `$nombre` 28.

---

## Patrones

### P01. Preparación de datos de prueba por auto-append
- **Firma estructural:** `proc datasets ... delete` de una tabla en una librería permanente; `data WORK.x; set sashelp.x; run;`; `%macro` con `%do i=1 %to 15` y dentro `proc append base=WORK.t data=WORK.t`.
- **Frecuencia y líneas:** 1 vez, líneas 6-30.
  ```
  proc datasets lib=GCIDLL01 nolist;
  delete cars_poc;
  %macro append_all;
  %do i=1 %to 15;
  proc append
  base=WORK.cars_poc
  data=WORK.cars_poc;
  ```
- **Intención:** generar volumen artificial (el comentario indica 14.024.704 filas). Cada append a sí misma duplica: 428 x 2^15 = 14.024.704 si la fuente tiene 428 filas.
- **Clasificación:** fontanería (arnés de prueba).
- **Diseño Talend:** no migrar. Si hiciera falta volumen de prueba, `tRowGenerator` en un Job de pruebas aparte.
- **Detección:** `proc append` con `base=` igual a `data=`; bucle macro que solo repite append.
- **Riesgos:** el `proc datasets delete` apunta a la librería `GCIDLL01`, mientras la tabla de trabajo está en `WORK`. Puede borrar una tabla permanente homónima sin efecto sobre la de trabajo. No tiene sentido migrarlo.

### P02. Segmentación por valor en tablas intermedias con proyección fija
- **Firma estructural:** `PROC SQL; CREATE TABLE WORK.X AS SELECT <15 columnas fijas> FROM WORK.SRC WHERE (SRC.col = 'valor'); QUIT;`. El mismo `SELECT` se repite cambiando solo el literal. Cabecera generada por el generador visual de consultas.
- **Frecuencia y líneas:** 4 veces. Líneas 42-49 y 58-65, 74-81, 100-107.
  ```
  PROC SQL;
  CREATE TABLE WORK.ACURA
  AS
  SELECT CARS_POC.Make, CARS_POC.Model, CARS_POC.Type, ... CARS_POC.Length
  FROM WORK.CARS_POC CARS_POC
  WHERE
     ( CARS_POC.Make = 'Acura' ) ;
  ```
- **Intención:** partir la fuente en un subconjunto por valor de categoría, para transferir cada subconjunto a su destino.
- **Clasificación:** lógica de datos (filtro y proyección) con E/S intermedia.
- **Diseño Talend:** un `tDBInput` con `SELECT` de las 15 columnas y `WHERE col IN (...)` (proyección y filtro en la base de datos). Luego `tMap` con una salida por valor (filtro en la salida, p. ej. `row1.Make.equals("Acura")`). Cada salida va a su `tImpalaOutput`. Sin tablas intermedias. Si la lista de valores es dinámica, `tFlowToIterate` sobre la lista de valores con un `tDBInput` parametrizado por contexto (leer la fuente cuatro veces; preferible una sola lectura).
- **Detección:** en el IR, `CREATE TABLE ... AS SELECT` con `WHERE` de igualdad sobre una columna con literal; familia de sentencias con la misma proyección y la misma fuente, y literal distinto. Variantes: `WHERE col IN`, `between`, `is null`, `like`, opción de dataset `(where=...)`, `DATA step` con `subsetting if`/`where`, `create view`, SQL pass-through (`connect to oracle/teradata/...`).
- **Riesgos:** la comparación de cadenas en SAS es sensible a espacios finales y a mayúsculas según opciones. La comparación Java de Talend no ignora espacios finales. Si la proyección difiere entre tablas, no agrupar. Si los valores vienen de datos, no fijar la lista en código.

### P03. Cabecera de query generada por el generador visual (comentario)
- **Firma:** comentario "Código de query generado para SAS Studio por ..." justo antes de cada `PROC SQL` de P02.
- **Frecuencia:** 4 (líneas 40, 56, 72, 98).
- **Intención:** solo trazabilidad del origen de la sentencia.
- **Clasificación:** fontanería.
- **Diseño Talend:** no migrar.
- **Detección:** texto del comentario; también forma de `%web_*` (ver P19).
- **Riesgos:** ninguno.

### P04. Recuento de control sin consumidor
- **Firma:** `proc sql; select count (*) from WORK.X; quit;` sin salida ni comparación posterior.
- **Frecuencia:** 4 (líneas 85-88, 90-93, 111-114, 116-119).
  ```
  /* Etiqueta: CONTADOR_ACURA */
  proc sql;
  select count (*) from WORK.ACURA;
  quit;
  ```
- **Intención:** ver el número de filas en el log de SAS Studio.
- **Clasificación:** trazas/medición.
- **Diseño Talend:** no migrar el conteo como paso. Para trazabilidad, `tStatCatcher` o `tFlowMeter`, o el log del Job.
- **Detección:** `count(*)` cuyo resultado no alimenta ninguna macro variable ni tabla usada después.
- **Riesgos:** cada `count(*)` recorre la tabla completa; si se usara como puerta de validación, sí tendría valor (ver P21).

### P05. Réplica del programa de carga por entidad
- **Firma:** bloque de ~634 líneas (macros `split3_`, `split3`, `split2`, `create_commands`, `waitForBulkLoads`, `executeBulkload`, `execImpalaQuery`, `deleteTableLZ`, `checkForErrors`, `capturaCampos`, `comparaRegistros`, `tiempos`, `mainProgram`) redefinido completo en cada copia, con una sola entidad distinta.
- **Frecuencia:** 4 copias: 136-769, 899-1531, 1612-2245, 2262-2895. Cada copia termina en `%mainProgram;` (769, 1531, 2245, 2895).
- **Intención:** cargar cada tabla de marca a LZ con la misma lógica.
- **Clasificación:** orquestación (estructura repetida).
- **Diseño Talend:** un único Job parametrizado por contexto, con el mismo grafo para todas las entidades (ver sección A). Si las entidades fueran dinámicas, `tFlowToIterate` sobre la lista, o un joblet reutilizado.
- **Detección:** en el IR, clonado de bloques: mismo esqueleto de sentencias que solo cambia un token de nombre de tabla (comprobable comparando el texto con el nombre sustituido, como hizo el diff).
- **Riesgos:** cualquier corrección hay que aplicarla cuatro veces. `comparaRegistros` tiene la tabla fija en cada copia (627, 1390, 2103, 2753).

### P06. Cabecera de tarea SAS Studio y bloque de inicio de sesión
- **Firma:** (a) comentario con metadatos de generación (usuario, servidor, plataforma, versión, navegador, cliente web); (b) bloque `TITLE`, `FOOTNOTE`, `filename _all_ clear`, `ods ... close`, `options ...`, `%include` y `%global`.
- **Frecuencia:** (a) 6 (121-134, 771-784, 884-897, 1533-1546, 1597-1610, 2247-2260); (b) 4 (137-148, 899-911, 1612-1624, 2262-2274).
- **Intención:** metadatos y limpieza de la sesión web de SAS Studio.
- **Clasificación:** fontanería.
- **Diseño Talend:** no migrar. Los metadatos van a la documentación del Job.
- **Detección:** comentarios "Código de la tarea generado por", "INICIA CÓDIGO", `ods html close`, `filename _all_ clear`.
- **Riesgos:** los metadatos contienen usuario y nombres de servidor internos. No deben copiarse al Job.

### P07. Inclusión de utilidades externas
- **Firma:** `%include "<ruta>.sas";`.
- **Frecuencia:** 10 (146-147, 786, 909-910, 1548, 1622-1623, 2272-2273).
- **Intención:** reutilizar macros comunes (mensajes, conteos, S3, entorno).
- **Clasificación:** fontanería/reutilización. Riesgo de dependencia no resuelta.
- **Diseño Talend:** las macros de utilidad se reemplazan por routines Java y por contexto. No se migra su código sin conocerlo.
- **Detección:** `%include` con ruta absoluta: marcar como "dependencia externa no resuelta" y exigir su código antes de traducir.
- **Riesgos:** el comportamiento real de `countTableLz`, `exportar_s3`, etc. es desconocido. Este archivo no basta.

### P08. Selección de entorno por código de ambiente
- **Firma:** `%macro ambiente; %if &m_ambiente eq D %then %let lz_dsn=IMPALA; %else %if ... C ... %else %if ... P ...; %mend; %ambiente;`.
- **Frecuencia:** 4 (150-171, 913-934, 1626-1647, 2276-2297).
- **Intención:** apuntar al mismo destino lógico en desarrollo, certificación o producción.
- **Clasificación:** parametrización/entorno.
- **Diseño Talend:** grupos de contexto `Dev`, `Cert`, `Prod` con el DSN o host de Impala. El entorno se elige al ejecutar. Un `tJava` de precondición comprueba que el código de ambiente es válido, y falla con `tDie` si no lo es.
- **Detección:** cadena `%if` de igualdades sobre una misma variable, cada rama asigna una conexión distinta.
- **Riesgos:** `m_ambiente` no se define en el archivo. Si no coincide ninguna rama, `lz_dsn` queda sin valor y el fallo aparece más tarde en SQL.

### P09. Parámetros de tarea no instanciados (placeholders)
- **Firma:** `%let x = $x;`, `%let cols = %str($cols);`, `encoding=$encoding`, `clave=$clave`, `%put NOTE- ... = $modo_xlsx;`.
- **Frecuencia:** 28 ocurrencias. Ejemplos: 820 `%let num_datasets = opt4;`, 827 `%let dataset5 = $dataset5;`, 859 `%let cols_unlocked = %str($cols_unlocked);`, 881-882 `encoding=$encoding, encriptar=$encriptar, ... tipo_clave=$tipo_clave, clave=$clave);`.
- **Intención:** valores que la UI de SAS Studio debería inyectar. Aquí quedan como texto literal.
- **Clasificación:** parametrización/entorno.
- **Diseño Talend:** cada parámetro se convierte en variable de contexto con valor por defecto explícito. Si falta valor, `tJava` lanza error. Las credenciales (`clave`) van a un almacén seguro del entorno de ejecución, nunca como literal migrado.
- **Detección:** `%let x = $x;` (valor igual al nombre con `$`) y `$nombre` en llamadas a macros.
- **Riesgos:** falso positivo si un valor real empieza por `$` (p. ej. una clave). Con los valores literales el programa no funcionaría tal cual; el archivo no es ejecutable sin la UI.

### P10. Arreglo emulado con variables numeradas
- **Firma:** `%let dataset1 = ...; ... %let dataset10 = ...;` y lo mismo para `archivo_N` y `hoja_N`.
- **Frecuencia:** 1 bloque de 30 asignaciones (822-856). Algunas vacías (`archivo_1 = ;`, 835-838).
- **Intención:** lista de datasets a exportar, con su nombre de fichero y hoja.
- **Clasificación:** parametrización.
- **Diseño Talend:** lista en contexto o en un `tFixedFlowInput`, consumida por `tFlowToIterate`. El nombre de fichero se deriva del nombre de tabla si está vacío.
- **Detección:** secuencias de `%let` con índice numérico creciente.
- **Riesgos:** huecos en la numeración; los vacíos cambian el comportamiento por defecto y la macro externa lo decide.

### P11. Traducción de nombre de delimitador a carácter
- **Firma:** `%macro resolver_delimitador(valor=, out=)` con cadena `if coma/punto_coma/pipe/tab`.
- **Frecuencia:** 2 definiciones y llamadas con `valor=coma` (816 y 1579).
- **Intención:** convertir una opción de negocio en el separador real.
- **Clasificación:** parametrización.
- **Diseño Talend:** campo "Field separator" con el carácter literal (`,`, `;`, `|`, `\t`). Si es parametrizable, variable de contexto. No hace falta macro.
- **Detección:** macro cuyo cuerpo es una tabla de correspondencias texto a literal.
- **Riesgos:** valor desconocido deja el separador vacío sin error. La llamada usa siempre `coma`: la macro es plegable a constante.

### P12. Normalización de lista de columnas
- **Firma:** `data _null_; v=symget(...); v=compress(v,' '); call symputx(...,v,'G');`.
- **Frecuencia:** 1 (862-867).
  ```
  /* Quitar espacios: A, B -> A,B */
  v=symget('cols_unlocked');
  v=compress(v, ' ');
  ```
- **Intención:** tolerar espacios en la lista de columnas que introduce el usuario.
- **Clasificación:** parametrización/validación de entrada.
- **Diseño Talend:** trim en la carga del contexto (`tJava` o expresión en la configuración). No hace falta componente.
- **Detección:** `compress(x, ' ')` sobre macro variable de lista.
- **Riesgos:** el significado de "columnas desbloqueadas" depende de la macro externa de exportación; no verificable aquí.

### P13. Captura de lista de campos con respaldo a todas las columnas
- **Firma:** `%if %symexist(x) %then %symdel x;` `%global x;` si el valor está vacío, `proc sql ... into :w_columns separated by "-" from dictionary.columns where libname eq ... and memname eq ...`, y si no, `compress`.
- **Frecuencia:** 4 (591-623, 1354-1386, 2067-2099, 2717-2749). Sentencia de diccionario en 606-608:
  ```
  select name into: w_columns separated by "-" from dictionary.columns where
  libname eq %upcase("&wlibre_origen") and memname eq %upcase("&wtabsrc");
  ```
- **Intención:** transferir todas las columnas salvo que se indique un subconjunto.
- **Clasificación:** lógica de datos/parametrización.
- **Diseño Talend:** el esquema (schema) del componente define las columnas. Un subconjunto se obtiene con un `tMap` que descarta columnas.
- **Detección:** consulta al diccionario de metadatos seguida de unión con separador.
- **Riesgos:** el separador `-` rompe nombres de columna que contengan guion. Depende de que la tabla exista en la sesión.

### P14. Exportación de datasets a S3 en CSV
- **Firma:** `%exportar_s3(num_datasets=..., folder=..., formato=csv, delimiter=..., encoding=..., encriptar=..., cols_unlocked=..., tipo_clave=..., clave=...);`.
- **Frecuencia:** 1 llamada (879-882), con 4 datasets.
- **Intención:** publicar cuatro tablas como CSV en un bucket, opcionalmente cifradas.
- **Clasificación:** E/S (destino S3).
- **Diseño Talend:** por cada salida: `tDBInput` (o la salida del `tMap` de P02) → `tFileOutputDelimited` (separador, codificación, cabecera) → `tS3Put`. `tS3Configuration` una vez. Cifrado opcional con `tEncryptFiles`. Clave desde contexto seguro.
- **Detección:** llamada a macro con `folder=` y `formato=` y bucle implícito sobre el número de datasets.
- **Riesgos:** el número de datasets y los nombres se pasan por variables globales (contrato implícito con la macro). Credenciales en placeholders (P09).

### P15. Importación de CSV desde S3 a WORK
- **Firma:** `%importar_s3(s3_file=..., folder=..., formato=csv, tabla=, library=WORK, delimiter=..., encoding=..., header=si, sheet=...);`.
- **Frecuencia:** 1 (1593-1595).
- **Intención:** traer de vuelta un fichero del bucket. No está claro si es validación de ida y vuelta.
- **Clasificación:** E/S (origen S3).
- **Diseño Talend:** `tS3Get` → `tFileInputDelimited` (cabecera 1, separador) → `tImpalaOutput` o `tDBOutput`. Solo si se confirma que hace falta.
- **Detección:** macro con `s3_file=` y `library=WORK`.
- **Riesgos:** `tabla=` vacío: el nombre de destino lo decide la macro. Puede sobrescribir una tabla de trabajo homónima (`WORK.BMW`).

### P16. Troceado por ventanas de filas
- **Firma (activa, `split3`):** `%sysfunc(open)` + `attrn NLOBS` para contar filas; `%sysfunc(ceilz(total/N))` para calcular bloques; `%do i=1 %to num` con `%sysevalf` para `inicio` y `fin`; `data work.prefix&i; set src (firstobs=&inicio obs=&fin); run;`.
- **Frecuencia:** 4 llamadas activas (740, 1503, 2216, 2866), con `wsplit=3500000` (684). Ventanas en 334-338:
  ```
  data work.&prefix.&i (compress=binary);
  set &tabla_origen (firstobs=&inicio obs=&fin);
  run;
  ```
- **Variantes no invocadas:** `split3_` (un solo `DATA step` con `chunk_id=int((_N_-1)/N)+1` y `if chunk_id=&j then output ...`, líneas 259-266) y `split2` (sesiones SAS remotas `signon/rsubmit/waitfor`, 359-455). `split3_` nunca se llama; `split2` aparece comentada (743, 1505, 2219, 2869).
- **Intención:** partir la tabla en fragmentos de hasta 3,5 millones de filas para que la carga de cada fragmento sea manejable.
- **Clasificación:** E/S (preparación) / fontanería.
- **Diseño Talend:** no migrar el troceado. `tImpalaOutput` con "Batch size" y "Commit every". Si el destino exige fichero, `tFileOutputDelimited` con "Split output in several files" y "Rows in each output file = 3500000". Carga con `tImpalaLoad` si la versión de Studio lo soporta (verificar).
- **Detección:** `firstobs=`/`obs=` dentro de un bucle de bloques; `int((_N_-1)/N)+1`; `ceil` sobre número de filas.
- **Riesgos:** con una fuente de base de datos sin orden fijo, paginar con firstobs equivale a OFFSET, no determinista. No replicarlo con SQL. La comprobación de tabla vacía (`NO TIENE REGISTROS`, 8 apariciones: 4 en la variante activa y 4 en `split2`, que no se invoca) aborta con `%abort cancel`; en Talend equivale a un `tDie` si la fuente llega sin filas.

### P17. Descubrimiento de tablas por prefijo de nombre
- **Firma:** `proc contents data=work._all_ out=contents; proc sort ... nodupkey by memname; proc sql ... select memname into :tablas separated by "|" ... where upcase(memname) like upcase("&prefix.%") order by memname;`.
- **Frecuencia:** 4 (líneas 343-352 en la copia 1; equivalente en las demás).
- **Intención:** reconstruir la lista de tablas creadas por el troceado.
- **Clasificación:** orquestación/fontanería.
- **Diseño Talend:** no hace falta: la lista de fragmentos sale del propio flujo, sin descubrirla en el catálogo.
- **Detección:** `proc contents data=work._all_` seguido de `select memname into :macro separated by`.
- **Riesgos:** `like` trata `_` como comodín de un carácter; el prefijo contiene guiones bajos y puede coincidir con otras tablas. `contains` o `=` son más seguros.

### P18. Iteración sobre lista delimitada por "|"
- **Firma:** `%do %while (%scan(&lista, &i, "|") ne); %let x=%scan(&lista,&i); ... %let i=%eval(&i+1); %end;`.
- **Frecuencia:** 8 (4 en `delProcessTables`, líneas 187, 950, 1663, 2313; 4 en `create_commands`, 475, 1238, 1951, 2601).
- **Intención:** procesar cada elemento de la lista de tablas.
- **Clasificación:** orquestación.
- **Diseño Talend:** `tFlowToIterate` sobre el flujo de elementos, o `tFileList`. Sin bucle macro.
- **Detección:** `%do %while` con `%scan(...,i,"sep") ne` como condición.
- **Riesgos:** si un elemento contiene el separador, la lista se rompe. Si la lista está vacía, el bucle no ejecuta y no hay aviso.

### P19. Tabla de comandos de SO
- **Firma:** `data &cmdt.; length cmdbl $5000; stop; run;` (tabla vacía con estructura) seguido de `proc sql; insert into &cmdt. values("sh <script> <args> &");`.
- **Frecuencia:** 4 (463-480, 1226-1247, 1939-1960, 2589-2610). El `insert` es la línea 479.
- **Intención:** crear una lista de trabajos de carga, uno por fragmento, que luego se ejecuta.
- **Clasificación:** orquestación.
- **Diseño Talend:** no hace falta; el grafo ya contiene un trabajo por fragmento o por tabla.
- **Detección:** `data ...; stop; run;` seguido de inserciones de cadenas que empiezan por `sh`.
- **Riesgos:** la cadena en `values("...")` se rompe con comillas o caracteres especiales en las rutas. El `&` final lanza en segundo plano.

### P20. Lanzador de procesos de SO con escalonamiento
- **Firma:** `%do i=1 %to &numreg; data _null_; set cmd(obs=&i); call symputx('comando', cmdbl,'G'); run; data _null_; x "&comando"; run; data _null_; call sleep(2,1); run; %end;`.
- **Frecuencia:** 4 (líneas 501-517 y equivalentes). Pausa de 2 s en 514-516.
  ```
  x "&comando";
  ...
  /* Espera de 2 segundos entre ejecucion para evitar bloqueos */
  call sleep(2, 1);
  ```
- **Intención:** arrancar las cargas en paralelo sin saturar el destino.
- **Clasificación:** orquestación (paralelismo).
- **Diseño Talend:** `tParallelize` (con número máximo de hilos, si el Job lo necesita) o `tRunJob` iterado. Si hay un solo `tImpalaOutput` con batch, no hace falta paralelismo.
- **Detección:** comando `x` o `system` dentro de un bucle sobre una tabla de comandos, con `sleep`.
- **Riesgos:** no hay límite de concurrencia. El `x` del SO no devuelve código de salida al paso de SAS; el resultado solo se ve en logs (P24).

### P21. Espera activa por sondeo de procesos
- **Firma:** `x " nroproc=5; until [ $nroproc -eq 0 ]; do nroproc=$( ps -fea | grep ... | wc -l ); done ";`.
- **Frecuencia:** 4 (491, 1254, 1967, 2617).
- **Intención:** barrera: no continuar hasta que terminen todas las cargas.
- **Clasificación:** orquestación (sincronización).
- **Diseño Talend:** la ejecución síncrona de `tRunJob`/`tParallelize` ya espera. `onSubjobOk` o `tPostJob` para el siguiente paso. Sin sondeo.
- **Detección:** bucle `until`/`while` que cuenta procesos con `ps` y `grep`.
- **Riesgos:** sondeo sin pausa (ocupa CPU) y sin límite de tiempo: puede no terminar nunca. La línea de `ps` puede contar el propio comando.

### P22. Exclusión mutua por inspección de procesos
- **Firma:** `filename ex_pcs pipe "ps -eo ... | grep ... | grep -iw <tabla> | grep -iw <libreria>";` leído con `infile ... end=eof;` y un `symputx('numreg', _n_)` solo en `eof`; después `%if not %symexist(numreg)` decide si continúa.
- **Frecuencia:** 4 (715-735, 1478-1498, 2191-2211, 2841-2861). Aviso en 756.
- **Intención:** impedir que dos ejecuciones escriban la misma tabla destino a la vez.
- **Clasificación:** validación/orquestación.
- **Diseño Talend:** una sola ejecución por tarea en el planificador (TMC o externo). Si hiciera falta un bloqueo de datos, una tabla de control en la base de datos. No inspeccionar procesos.
- **Detección:** `filename ... pipe "ps ..."` seguido de lectura de líneas y bandera de existencia.
- **Riesgos:** falsos positivos (otro usuario con el mismo nombre de proceso) y falsos negativos. La bandera depende de cómo se comporta `end=eof` con un pipe vacío. Carrera entre la comprobación y el arranque.

### P23. Carga masiva por script externo con argumentos posicionales
- **Firma:** la cadena de P19 invoca `bulkload_generic.sh` con diez argumentos posicionales (ruta, directorio de trabajo, tabla, librería, tabla, tabla LZ, identificador de ejecución, campos, `&`).
- **Frecuencia:** 4 (líneas 479, 1242, 1955, 2605).
- **Intención:** insertar los datos en la LZ de Impala con herramienta de carga masiva.
- **Clasificación:** E/S (destino).
- **Diseño Talend:** `tImpalaOutput` (acción sobre tabla: "Drop and create" o "Truncate") con "Batch size" y "Commit every". Si la carga masiva con ficheros es necesaria, `tImpalaLoad` (verificar disponibilidad en la versión de Studio).
- **Detección:** invocación de script con argumentos posicionales que incluyen nombres de tabla destino.
- **Riesgos:** el script no está en el archivo; sus efectos son desconocidos. Argumentos posicionales frágiles.

### P24. Ejecución y lectura de logs de error
- **Firma:** `find <logs> -type f -iname '*<id>*' | xargs grep -H -n -C 4 'ERROR:'` por `filename ... pipe`; `proc sql ... count(outcmd) into :numprocess`; si > 0, lectura y `symputx('wsyserr', 1099)`.
- **Frecuencia:** 4 (541-542, 578-583 y equivalentes). Sentinel 1099 también en 1346, 2059, 2709.
- **Intención:** detectar fallos de las cargas en paralelo leyendo los logs de cada una.
- **Clasificación:** validación/trazas.
- **Diseño Talend:** los errores de cada componente son nativos: "Die on error" en `tImpalaOutput`, `tDie`, `onComponentError` con `tLogCatcher`. No hay que buscar en logs.
- **Detección:** `grep` de `'ERROR:'` por pipe y sentinel numérico asignado con `symputx`.
- **Riesgos:** el sentinel `wsyserr` solo lo lee la comparación de P25. Ningún paso aborta el Job con fallo. Ver la conclusión 4.

### P25. Reconciliación de conteos que solo informa
- **Firma:** `%countTableSas(t_ori=...)`; `%countTableLz(cmdcountlz=select count(1) ...)`; `%if &srcnrows. ne &cntreglz. %then %put ERROR%str(:) ...;`.
- **Frecuencia:** 4 (625-638, 1388-1401, 2101-2114, 2751-2764).
- **Intención:** verificar que la carga tiene el mismo número de filas que el origen.
- **Clasificación:** validación/reconciliación.
- **Diseño Talend:** `tAggregateRow` (conteo) en el flujo de origen; `tDBInput` con conteo sobre la tabla destino; `tJava` que compara y lanza excepción; `tDie` si difieren. Como un único Job con `onSubjobOk`.
- **Detección:** dos conteos seguidos de comparación con sólo `%put` en la rama de diferencia.
- **Riesgos:** solo compara conteos, no contenido. El `ERROR` no aborta ni marca fallo. La tabla está fija en cada copia.

### P26. Guarda de existencia de archivo con advertencia
- **Firma:** `%if %sysfunc(fileexist("&f.")) %then ... %else %put WARNING: ...;`.
- **Frecuencia:** 4 (697-711, 1460-1474, 2173-2187, 2823-2837).
- **Intención:** cargar un parámetro opcional si existe.
- **Clasificación:** validación.
- **Diseño Talend:** `tFileExist` en el `tPreJob`, con `tDie` si es obligatorio.
- **Detección:** `fileexist` seguido de `%else` que solo escribe un aviso.
- **Riesgos:** el Job continúa sin el parámetro: degradación silenciosa.

### P27. Carga de catálogo de errores no usado
- **Firma:** `%let wt_errslz=param_err_lz;` y `proc import datafile=... out=&wt_errslz. dbms=DLM replace;`.
- **Frecuencia:** 4 cargas (701-705 y equivalentes). La tabla `param_err_lz` no se referencia en ningún otro punto del archivo (búsqueda confirmada).
- **Intención:** cargar un catálogo de errores. En este archivo no se usa.
- **Clasificación:** parametrización (sin uso efectivo aquí).
- **Diseño Talend:** no migrar mientras no se confirme su uso. Si se usa en un `tMap` con `lookup`, convertirlo a `tFileInputDelimited` como tabla de búsqueda.
- **Detección:** importación de un CSV a una tabla que nunca se lee.
- **Riesgos:** puede estar consumido por una macro externa (`checkForErrors` no lo usa). Confirmar antes de eliminar.

### P28. Limpieza de temporales condicionada a éxito
- **Firma:** `%if &syserr. eq 0 %then %do; ... loop de drop ...; %end; %else %do; drop de destino + proc delete del temporal actual; %end;`.
- **Frecuencia:** 4 (173-225, 936-988, 1649-1701, 2299-2351).
- **Intención:** en éxito, borrar temporales de SAS y de LZ. En fallo, borrar el destino para no dejar datos parciales.
- **Clasificación:** E/S (limpieza) / fontanería.
- **Diseño Talend:** sin temporales no hay que borrar nada. Parcialidad: transacción con `tDBConnection` + `tDBCommit` y `tDBRollback` en `onSubjobError`. Sustituye al borrado manual.
- **Detección:** condición sobre `syserr` seguida de drops y `proc delete`.
- **Riesgos:** usa `&syserr` y no el sentinel `wsyserr` de P24, así que tras un fallo de carga externa puede llegar a `syserr=0` y borrar temporales. En la rama `%else`, `&j` (línea 218) no se inicializa en esa ejecución. Verificar en un caso real.

### P29. Borrado previo del destino con drop ... purge
- **Firma:** `%macro deleteTableLZ(lib,table); %execImpalaQuery(drop table if exists &lib..&table purge); %mend;` llamado antes de la carga (745, 1507, 2221, 2871).
- **Frecuencia:** 4 llamadas y 4 definiciones. Con P28 hay 12 bloques `connect to impala` en total.
- **Intención:** recarga completa de la tabla destino.
- **Clasificación:** E/S (destino).
- **Diseño Talend:** `tImpalaOutput` con "Action on table = Drop and create table" (o "Truncate table").
- **Detección:** `drop table if exists ... purge` mediante pass-through (`connect to <motor>` + `execute by` + `disconnect`).
- **Riesgos:** `purge` es irreversible. Si la carga falla después, el destino queda vacío (no hay transacción).

### P30. Ejecución de SQL pass-through
- **Firma:** `proc sql; connect to impala (DSN=&lz_DSN.); execute (...) by impala; disconnect from impala; quit;`.
- **Frecuencia:** 12 bloques (3 por copia: 2 en P28 y 1 en `execImpalaQuery`).
- **Intención:** ejecutar DDL en el motor destino.
- **Clasificación:** E/S (destino).
- **Diseño Talend:** `tImpalaRow` para DDL puntual (o la acción de `tImpalaOutput`).
- **Detección:** `connect to <motor> (...)` seguido de `execute`.
- **Riesgos:** depende del DSN del entorno (P08).

### P31. Mensajería de progreso y trazas
- **Firma:** `%showMessage(msg=...)` (40 llamadas), `%put NOTE/ERROR/WARNING` (101), `putlog " >>>>> " ...`.
- **Frecuencia:** ver conteos de la sección 0.
- **Intención:** informar del avance en el log.
- **Clasificación:** trazas.
- **Diseño Talend:** log del Job y `tLogRow`/`tWarn` solo donde haga falta.
- **Detección:** llamadas de mensajes sin efecto sobre datos.
- **Riesgos:** ninguno si se elimina; ojo con los `ERROR` que no abortan (P25).

### P32. Medición de tiempos
- **Firma:** `%tiempos(&hi)` con `datetime()` y `putn(... datetime20.)`/`time.`; temporizador de inicio `%let _timer_start = %sysfunc(datetime());` (3) y final `dur = datetime() - &_timer_start;` (2899-2902).
- **Frecuencia:** 4 llamadas a `%tiempos` (752, 1514, 2228, 2878) y 1 par de temporizador.
- **Intención:** medir la duración de la carga.
- **Clasificación:** trazas/medición.
- **Diseño Talend:** `tStatCatcher` o duración de la ejecución del Job (TMC).
- **Detección:** diferencias de `datetime()` impresas.
- **Riesgos:** ninguno.

### P33. Puente de data step a macro variable
- **Firma:** `data _null_; ... call symputx('nombre', valor, 'G'); run;` para pasar un valor calculado a `%let`.
- **Frecuencia:** 33 `symputx`. Ejemplos: 463-466 (identificador), 667 (`pidexecution`), 1-línea de `t_campos`, `cols_unlocked`, `comando`, `numreg`.
- **Intención:** calcular en SAS lo que la macro no puede.
- **Clasificación:** fontanería.
- **Diseño Talend:** no hace falta: el valor se pasa por contexto o por el flujo.
- **Detección:** `call symputx` dentro de `data _null_`.
- **Riesgos:** ninguno en migración; oculta dependencias entre macros.

### P34. Estado compartido por macro variables globales
- **Firma:** `%global a b c ...;`, `%symexist`/`%symdel` como guardas de reinicio.
- **Frecuencia:** 148, 230, 362, 595-600 y equivalentes por copia.
- **Intención:** pasar estado entre macros.
- **Clasificación:** fontanería.
- **Diseño Talend:** flujo de datos y contexto.
- **Detección:** `%global` seguido de uso en otras macros.
- **Riesgos:** dependencias implícitas entre macros.

### P35. Identificadores de ejecución y nombres derivados
- **Firma:** generación de 10 letras aleatorias con `ranuni(0)` (656-668); `wprefix=grdtare_%substr(&pid,1,5)_&sysuserid.`; `%scan(WORK.X, 1, '.')` y `%scan(..., -1, '.')` para separar librería y tabla; `cmdtable&id`.
- **Frecuencia:** 5 generaciones de id y 4 juegos de descomposición de nombre por copia.
- **Intención:** unicidad de ejecución y nombres temporales.
- **Clasificación:** fontanería.
- **Diseño Talend:** UUID de `java.util.UUID` o variable de ejecución del Job.
- **Detección:** `ranuni` en un `data _null_`.
- **Riesgos:** `ranuni(0)` depende de la hora; dos ejecuciones simultáneas pueden colisionar.

### P36. Silenciado de opciones SAS de diagnóstico
- **Firma:** `options nosyntaxcheck nosymbolgen nosource nosource2 nomlogic nomprint nonotes;` al inicio de cada macro.
- **Frecuencia:** 52.
- **Intención:** reducir ruido en el log.
- **Clasificación:** fontanería.
- **Diseño Talend:** no migrar.
- **Detección:** `options no...` repetidas.
- **Riesgos:** ninguno en la migración.

### P37. Código muerto y alternativas no invocadas
- **Firma:** macros definidas y nunca llamadas (`split3_`, `split2`), llamada comentada (`/*%split2(...);*/`), variables asignadas y no usadas (`libtmp`, `tabdes`, `wlibtemp`, `wpathdata`).
- **Frecuencia:** `split3_` 4 definiciones y 0 llamadas; `split2` 4 definiciones y llamada comentada 4 veces; 4 bloques de variables sin uso.
- **Intención:** alternativas de troceado y paralelismo descartadas.
- **Clasificación:** fontanería.
- **Diseño Talend:** no migrar.
- **Detección:** definición de macro sin llamada en el archivo.
- **Riesgos:** la macro externa puede llamarlas; confirmar antes de borrar en el migrador.

---

## A. Diseño objetivo del programa completo

**Un Job** (`J_Carga_Marcas_LZ`) con contexto por entorno.

- **Contexto:** `env` (D/C/P), DSN o host y puerto de Impala por entorno, esquema destino `PROCESO`, lista de valores de marca, bucket y carpeta S3 (`FILE_GCIA_DLLO_SERV_DE_INFORM/`), separador `,`, codificación, cabecera `true`, bandera de cifrado, clave (en almacén seguro, no literal).
- **tPreJob:** `tJava` que valida `env` y las variables obligatorias. Si falla, `tDie`.
- **Subjob principal (carga):** `tDBInput` (`SELECT` de las 15 columnas filtrado por la lista de marcas) → `tMap` con una salida por marca → cuatro `tImpalaOutput` (acción "Drop and create", batch, "Die on error").
- **Subjob de reconciliación (onSubjobOk):** `tAggregateRow` (conteo por marca en origen, guardado en `globalMap`) y `tDBInput` con `UNION ALL` de conteos en destino → `tJava` que compara → `tDie` si difiere.
- **Subjob de exportación S3 (opcional):** desde las mismas salidas del `tMap`, cuatro `tFileOutputDelimited` → cuatro `tS3Put`, con `tS3Configuration` una vez. Cifrado con `tEncryptFiles` si aplica.
- **Subjob de importación S3 (solo si se confirma):** `tS3Get` → `tFileInputDelimited` → `tImpalaOutput`.
- **Errores:** `onComponentError` → `tDBRollback` (si hay transacción) → `tDie`.
- **Sin:** troceado, tabla de comandos, lanzador, sondeo de procesos, inspección de `ps`, búsqueda de errores en logs, temporales, drop manual previo, macros de utilidad, cronómetro manual.
- **Concurrencia:** una ejecución por tarea en el planificador (TMC), no en código.
- **Joblets:** ninguno necesario con lista fija. Si la lista de marcas fuera dinámica: `tFlowToIterate` con un sub-Job de carga de una marca.

**Conteo esperado:** 1 Job; aproximadamente 23 componentes (2 de precondición, 6 de carga, 4 de reconciliación, 9 de exportación S3, 2 de error). Más 3 si se mantiene la importación S3. Frente a los 4 programas de ~634 líneas, varias decenas de macros y ~19 tareas de Studio.

---

## B. Tabla resumen: patrón → capa → prioridad

Capas: lexer (limpieza de texto), parser (sentencias SAS), resolución de macros, IR (operaciones), traductor (componentes Talend), planificador (orden y concurrencia).

| # | Patrón | Capa | Prioridad | Motivo |
|---|---|---|---|---|
| P05 | Réplica del programa por entidad | IR (agrupar clones) + planificador | Alta | ~2.500 líneas, colapsa en un Job |
| P02 | Segmentación por valor con proyección fija | IR (familia de filtros) → traductor (`tMap` multisalida) | Alta | 4 extracciones + 4 conteos |
| P16 | Troceado por ventanas | Traductor (eliminar; `tImpalaOutput` batch) | Alta | Elimina 3 macros y el bucle |
| P19, P20, P21, P22, P23 | Tabla de comandos, lanzador, sondeo, exclusión, script | Planificador (eliminar) + traductor (`tImpalaOutput`) | Alta | Elimina el grueso de la orquestación |
| P28, P29, P30 | Limpieza y drop previo, pass-through | Traductor (acción de tabla, transacción) | Alta | Elimina pasos de SQL manual |
| P24, P25 | Errores por grep y conteos que solo informan | Traductor (`tDie`, `tAggregateRow`, `tJava`) | Alta | Corrige fallos silenciosos |
| P14, P15 | Exportación e importación S3 | Traductor (`tS3Put`, `tS3Get`) | Media | Requiere confirmar el destino de la importación |
| P08 | Entorno por código D/C/P | Resolución de macros → contexto | Media | Un contexto por entorno |
| P11 | Delimitador | Resolución de macros (plegado) → literal | Media | Constante plegable |
| P09 | Placeholders `$nombre` | Resolución de macros → contexto con validación | Media | Riesgo de credenciales |
| P07 | `%include` | Resolución de macros (marcar como dependencia) | Media | Sin ella el comportamiento es desconocido |
| P10 | Arreglo numerado | Traductor (lista en contexto + `tFlowToIterate`) | Media | Parametrización |
| P13 | Captura de columnas | Traductor (schema del componente) | Media | Sustituido por metadatos |
| P12 | Normalización de lista | Traductor (trim en contexto) | Baja | Trivial |
| P17, P18 | Descubrimiento por prefijo, iteración por "\|" | Planificador (eliminar) / traductor (`tFlowToIterate`) | Media | Desaparecen con el grafo |
| P26, P27 | Guarda de fichero, catálogo sin uso | Traductor (`tFileExist`) / revisar uso | Baja | Verificar antes de decidir |
| P01 | Datos de prueba | Lexer (descartar) | Baja | Arnés, no producción |
| P03, P04, P06, P31, P32, P36 | Cabeceras, conteos sin consumidor, trazas, medición, silenciado | Lexer (descartar) | Baja | Fontanería |
| P31, P33, P34, P35, P37 | Puente symputx, globales, identificadores, código muerto | Lexer / resolución de macros (descartar) | Baja | Fontanería |
| P03 | Acciones UI de Studio (`web_drop_table`/`web_open_table`, 4+4 apariciones) junto a P02 | Lexer (descartar) | Baja | Fontanería |

---

## Conclusiones principales

1. **Más del 80 % del archivo es repetición.** El programa de carga aparece cuatro veces idéntico salvo el nombre de la tabla. Un Job con una salida de `tMap` por marca, o un `tFlowToIterate`, colapsa todo.
2. **La mayoría de los pasos son orquestación de SAS sobre SO e Impala** (troceado, tabla de comandos, lanzador, sondeo, inspección de procesos, grep de logs, temporales, drop previo). Talend lo resuelve con `tImpalaOutput` (acción de tabla, batch, die on error), `tDBRollback`, `tDie` y el planificador. Se eliminan más de 20 pasos.
3. **La lógica de negocio real es pequeña:** cuatro filtros por marca, dos transferencias S3, un conteo de reconciliación, la selección de entorno, el separador y la lista de columnas. Cabe en un Job de unos 23 componentes.
4. **La validación es débil y hay riesgos de borrado.** La reconciliación solo imprime `ERROR`; el sentinel de error no aborta; la limpieza usa `syserr` en vez del sentinel, así que puede borrar temporales tras un fallo externo; en la rama `%else` de `delProcessTables`, `&j` no se inicializa. El diseño objetivo debe hacer los fallos explícitos (`tDie`, `onComponentError`, rollback), no replicar esto.
5. **Dependencias no resueltas y placeholders.** Hay al menos siete macros externas y 28 placeholders `$nombre` sin valor real (incluida una clave). El migrador debe marcar estas dependencias, convertir los parámetros en contexto con validación y nunca migrar credenciales como literales. Sin el código de las macros externas, la semántica de exportación e importación no puede confirmarse.
