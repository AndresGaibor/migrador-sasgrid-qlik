# Cod2.txt, tramo 1 (líneas 1 a 8300): patrones SAS para migrar a Talend

Fuente: `C:\Users\USUARIO_BISOLUTION1\Downloads\Cod2.txt`, líneas 1 a 8300 (de 24.801). Código exportado de SAS Studio: conciliación y reporte regulatorio de depósitos (cuenta corriente, ahorros y Nequi), con PROC SQL contra Impala, importación de Excel y CSV, sesiones remotas y carga masiva.

Los nombres de tablas, macros y variables aparecen solo entre paréntesis como evidencia. Los nombres de patrón coinciden con los del tramo 2 cuando el patrón es el mismo.

## 0. Alcance, método y cifras

- Leí las líneas 1 a 8300 completas en 17 tramos (1-500, 501-1000, ..., 8001-8300).
- Los conteos salen de `grep -c` sobre las primeras 8300 líneas. Donde cito líneas concretas, las he verificado con `grep -n`.
- Cifras del tramo:
  - 290 bloques etiquetados (`/* Etiqueta: ... */`).
  - 227 pasos DATA y 207 PROC SQL.
  - 82 bloques de copia de vuelta (`data work.temporal` ... `set` ... `proc delete`).
  - 28 macros SAS Studio de vista previa `%web_drop_table` y 125 `%web_open_table`.
  - 6 copias idénticas de la librería de carga masiva (cada una de unas 289 líneas), es decir, unas 1.730 líneas, alrededor del 21 % del tramo.
- Hay 3 segmentos de producto con cadenas casi idénticas: cuenta de ahorros (líneas 1749 a 3828), cuenta corriente (4265 a 6500) y Nequi (6661 a 8156).

## 1. Catálogo de patrones

| ID | Patrón (nombre genérico) | Frecuencia en el tramo | Clasificación | Destino Talend |
|---|---|---|---|---|
| P01 | Importación de hoja Excel a tabla | 5 PROC IMPORT EXCELCS | E/S | tFileInputExcel |
| P02 | Importación de archivo delimitado sin cabecera | 4 PROC IMPORT DBMS=DLM | E/S | tFileInputDelimited |
| P03 | Descarga remota por sesión (RSUBMIT + PROC DOWNLOAD) | 4 | E/S + orquestación | tFileInputDelimited sobre ruta UNC; sin paso intermedio |
| P04 | Sesión remota y credenciales embebidas | 10 signon, 1 pwencode | parametrización/entorno | context con secreto |
| P05 | Copia de vuelta y borrado (tabla temporal) con conversión de tipo | 82 bloques | lógica de datos + fontanería | tMap con tipos de salida |
| P06 | Etiquetado de inconsistencia con constante | 13 | validación | columna constante en tMap |
| P07 | Proyección y renombrado de columnas | 19 pasos "Organizar/Orden" | fontanería | tMap (mapeo de columnas) |
| P08 | Filtro por predicado complementario (cumple / no cumple) | 8 pares, 16 apariciones de la regla de código | lógica de datos | tMap con N salidas con filtro |
| P09 | Partición por valor de código (una consulta por valor) | 6 consultas | validación | tMap multi-salida o tabla de reglas |
| P10 | Validación campo a campo (dominio, rango, nulo) | 13 NOT BETWEEN, 39 IS MISSING | validación | tSchemaComplianceCheck + tMap |
| P11 | Unión de bloques con esquemas parecidos (OUTER UNION CORR) | 28 CORR + 2 UNION ALL | validación/consolidación | tUnite |
| P12 | Deduplicación por clave y exceso de duplicados | 7 DISTINCT, 9 GROUP BY | validación | tUniqRow, tAggregateRow |
| P13 | Enriquecimiento por join con referencia | 19 LEFT, 24 INNER | lógica de datos | tMap con lookup |
| P14 | Semi-join y anti-join en SAS | 39 IS MISSING en joins | lógica de datos | tMap lookup con rechazos |
| P15 | Pass-through SQL a Impala (ELT) | 28 connect, 9 CTAS en conexión, 19 execute | E/S (ELT) | tImpalaInput / tImpalaRow |
| P16 | Agregado por clave y reunión de vuelta por umbral | 2 | lógica de datos/regulatorio | tAggregateRow + tMap lookup |
| P17 | Conciliación de conteo y saldo | 14 SUM, 15 COUNT, 6 fórmulas | validación/reconciliación | tAggregateRow + tJavaRow + tDie |
| P18 | Coalesce manual por CASE | 4 | lógica de datos | expresión en tMap |
| P19 | Derivaciones fila a fila (concatenación de clave, prefijo, recorte a cero) | 2 CAT clave, 2 prefijo, 2 IFN | lógica de datos | expresión en tMap |
| P20 | Fecha de periodo y vigencia | 2 PUT Z2., 2 CAT, 4 comparaciones | validación | expresión en tMap + context |
| P21 | Parámetros de proceso desde tabla de un registro (INTO:) | 22 INTO, 11 de año/mes/día | parametrización | context desde tImpalaInput |
| P22 | Gate de continuación (abort si cero filas) | 2 | orquestación | tPreJob + tDie |
| P23 | Carga masiva particionada a Impala (sesiones SAS + shell + polling) | 6 copias de la librería, 6 puntos de escritura | E/S + orquestación | tImpalaOutput (un job) |
| P24 | Bundle de macros duplicado | 6 copias de 289 líneas | fontanería | eliminar; joblet si queda algo |
| P25 | Selector de entorno por código (D, C, P) y DSN | 6 copias | parametrización | contextos Dev/Cert/Prod |
| P26 | Literales de negocio embebidos | 16 apariciones de 9902, umbral 1129560, rangos NID | parametrización | contexto o tabla de reglas |
| P27 | Trazas, medición y metadatos de ejecución | 6 `%tiempos`, 18 datetime, 28 options | trazas | descartar (stats de Talend) |
| P28 | Fontanería de la interfaz SAS Studio | 126 `%web_drop_table`, 125 `%web_open_table`, 102 cabeceras | fontanería | descartar |

## 2. Patrones

### P01. Importación de hoja Excel a tabla
- **Firma:** `PROC IMPORT DATAFILE='ruta.xlsx' DBMS=EXCELCS OUT=WORK.x REPLACE; TEXTSIZE=32767; PORT=...; SERVER='...'; SHEET=''; RUN;`
- **Frecuencia:** 5 (líneas 6, 16, 81, 108, 134).
- **Evidencia:**
  ```
  6  PROC IMPORT
  7  DATAFILE='\\sbcldwpsgf01\FILE_VSPC_FINANZAS\Homologacion_tpo_dto.xlsx'
  8  DBMS=EXCELCS OUT=WORK.IMPORT_HOMOLOGACION_TPO_DOC REPLACE;
  9  TEXTSIZE=32767;
  12 SHEET='';
  ```
- **Intención:** cargar catálogos de homologación y de códigos (tipo de documento, país, DANE, fechas de validación) que mantiene el área de negocio en Excel.
- **Clasificación:** E/S.
- **Diseño Talend:** tFileInputExcel con ruta de contexto, cabecera en la fila 1, todas las columnas como String y un tMap posterior que tipa. Los catálogos se leen una vez y se usan como lookup (ver P13).
- **Detección:** léxica `PROC IMPORT` con `DBMS=EXCELCS|XLSX`; en AST, nodo de importación con origen de hoja; en IR, fuente de archivo con esquema por posición. Variantes: `PROC IMPORT DBMS=XLSX`, `pandas.read_excel`, `openpyxl`.
- **Riesgos:** `SHEET=''` toma la primera hoja sin avisar. `SERVER` y `PORT` están fijados en el código. Un cambio de hoja o de orden de columnas no genera error.

### P02. Importación de archivo delimitado sin cabecera
- **Firma:** `proc import datafile='...csv' out=WORK.x dbms=dlm replace; delimiter=';'; getnames=NO; run;`
- **Frecuencia:** 4 (líneas 160, 291, 878, 1517).
- **Evidencia:**
  ```
  160 proc import datafile='/work_sasstudio/pcfiles/Base_datos_Nequi.csv' out=WORK.BASE_CLIENTES_NEQUI
  161 dbms=dlm replace;
  162 delimiter=';';
  163 getnames=NO;
  ```
- **Intención:** leer extractos de texto con separador `;` sin encabezado. Los nombres de columna se asignan después (P07), y eso obliga a tipar todo después (P05).
- **Clasificación:** E/S.
- **Diseño Talend:** tFileInputDelimited con separador `;`, cabecera 0 y esquema explícito con nombres de negocio desde el primer paso (se elimina P07 y el tipado se hace en el tMap de entrada).
- **Detección:** `dbms=dlm` + `getnames=NO`. En IR, fuente delimitada con columnas posicionales `VARn`.
- **Riesgos:** sin cabecera, la posición de columna es la única verdad; un cambio en el extracto rompe el mapeo sin error.

### P03. Descarga remota por sesión (RSUBMIT + PROC DOWNLOAD)
- **Firma:** `RSUBMIT server; PROC DOWNLOAD INFILE='\\servidor\ruta\x.csv' OUTFILE='/work_sasstudio/pcfiles/x.csv'; ENDRSUBMIT;` seguido de P02 sobre la ruta local.
- **Frecuencia:** 4 (líneas 150, 281, 868, 1507).
- **Intención:** mover el archivo del recurso compartido de Windows al servidor SAS y luego leerlo.
- **Clasificación:** E/S + orquestación.
- **Diseño Talend:** no hay paso intermedio. tFileInputDelimited lee la ruta UNC desde contexto. Si el motor no ve la ruta, se usa tFileFetch o tSFTPGet en el Remote Engine. Se elimina la copia local.
- **Detección:** `RSUBMIT` + `PROC DOWNLOAD` + `ENDRSUBMIT`; el mismo nombre de archivo aparece en INFILE y en la importación posterior. En IR, descarga y lectura forman un solo nodo de origen.
- **Riesgos:** la copia local deja archivos residuales; si la descarga falla, el siguiente paso lee un archivo viejo sin error.

### P04. Sesión remota y credenciales embebidas
- **Firma:** `%let server=...; OPTIONS REMOTE=server COMAMID=TCP; signon user=&sysuserid pass="&SASPC_PW";` y `proc pwencode in='...';`
- **Frecuencia:** 10 `signon` (4 en descargas y 6 en la librería de carga, una por sesión), 1 `proc pwencode`.
- **Evidencia:** líneas 77 (`proc pwencode`), 148-149 (`signon user=&sysuserid pass="&SASPC_PW";`).
- **Intención:** autenticarse contra el servidor remoto. El `pwencode` es ofuscación, no cifrado.
- **Clasificación:** parametrización/entorno.
- **Diseño Talend:** la contraseña va en un contexto con tipo password o en el repositorio de secretos del Remote Engine. Nunca se migra el valor codificado.
- **Detección:** léxica `pwencode|signon|pass=`; en IR, nodo de credencial con valor literal. No reproducir el valor en la salida del migrador.
- **Riesgos:** la contraseña codificada está en el repositorio. Hay que rotarla y tratarla como secreto comprometido.

### P05. Copia de vuelta y borrado (tabla temporal) con conversión de tipo
- **Firma:** `data work.temporal; format X n.; set T; X=input(left(Xv), n.); run; data T; set work.temporal; run; proc delete data=work.temporal; run;` Variantes: `set T(rename=X=X_old)` con `drop X_old`; y `COMPRESS(input(left(...)))` para texto.
- **Frecuencia:** 82 bloques de copia de vuelta, 65 con `input(left(...))` (21 de ellos con `COMPRESS`), 28 renombres con sufijo `_old`. Dentro de esto, 15 conversiones consecutivas sobre cada uno de los dos archivos de depósitos (líneas 297-792 y 884-1378).
- **Evidencia:**
  ```
  317 data work.temporal;
  318 format NRO_CTA 30.;
  319 set WORK.DBIFTCD;
  320 NRO_CTA=input(left(VAR7), 30.);
  321 run;
  ```
  Y la variante con renombre y longitud 20.:
  ```
  7381 data work.temporal;
  7382 format VAL_CRED_MES 20.;
  7383 set WORK.SABANA_FINAL_AHORROS(rename=VAL_CRED_MES=VAL_CRED_MES_old);
  7384 VAL_CRED_MES=input(left(VAL_CRED_MES_old), 20.);
  ```
- **Intención:** tipar columnas leídas como texto (sin cabecera, P02) a numérico o a longitud fija, y limpiar espacios.
- **Clasificación:** lógica de datos (casting), con fontanería de copia de vuelta.
- **Diseño Talend:** cero componentes extra. El tMap de entrada declara el tipo de cada columna de salida (Integer, Long, BigDecimal o String) y la expresión de conversión, por ejemplo `Long.parseLong(row.VAR7.trim())`. Los errores de conversión van al flujo de rechazo del tMap con código de error.
- **Detección:** léxica `data (\w+)\.temporal;` + `proc delete data=...temporal`. En AST, un DATA step que lee X y escribe X a través del temporal: fusionable. En IR, asignación de tipo en mismo esquema. En el planificador, reemplazar la cadena de pasos por una sola expresión.
- **Riesgos y falsos positivos:**
  - `input()` sin error devuelve missing si el texto no es numérico. Hay que tratarlo como rechazo.
  - Longitudes inconsistentes: el saldo mínimo usa `8.` (línea 8004-8006) mientras el resto usa `20.`. Eso trunca valores.
  - `30.` para números de cuenta puede perder precisión por encima de 15 dígitos.
  - Una copia que solo reordena columnas no es conversión; no la confundir.

### P06. Etiquetado de inconsistencia con constante
- **Firma:** `data work.temporal; set X; INCONSISTENCIA='TEXTO'; run;` (o `('TEXTO') AS INCONSISTENCIA` dentro de un SELECT).
- **Frecuencia:** 13 (`INCONSISTENCIA='...'`), más variantes en PROC SQL.
- **Evidencia:** líneas 3237-3239 (`INCONSISTENCIA='DOC 0 O VACIO FA';`), 6780 (`INCONSISTENCIA='TIPO DE CUENTA INVALIDO';`).
- **Intención:** marcar cada conjunto de rechazos con su motivo antes de consolidarlos (P11).
- **Clasificación:** validación.
- **Diseño Talend:** columna constante en el tMap de cada salida de rechazo. Con esto se elimina el paso de copia.
- **Detección:** léxica `^\s*\w+='[^']+';` dentro de un DATA step que sigue a una validación. En IR, nodo de asignación constante.
- **Riesgos:** los textos de motivo están repetidos en cada pipeline. Un cambio de texto hay que hacerlo en varios sitios. Conviene llevarlos a una tabla de códigos.

### P07. Proyección y renombrado de columnas
- **Firma:** `PROC SQL; CREATE TABLE X AS SELECT A.col1 AS NUEVO1, A.col2 AS NUEVO2 FROM Y A; QUIT;` sin WHERE ni JOIN.
- **Frecuencia:** 19 pasos etiquetados "Organizar campos" u "Orden campos".
- **Evidencia:**
  ```
  1384 CREATE TABLE WORK.DBIFTCS_FORMATO
  1385 AS
  1387 SELECT DBIFTCS.VAR1
  1388 AS ANIO_PROCESO, DBIFTCS.VAR2
  1389 AS MES_PROCESO, DBIFTCS.VAR4
  ```
- **Intención:** poner nombres de negocio a columnas posicionales y fijar el orden de salida.
- **Clasificación:** fontanería (renombrado de esquema).
- **Diseño Talend:** no hay tabla intermedia. El mapeo de columnas va en el tMap que ya existe (P02 + P05) con los nombres correctos desde el origen.
- **Detección:** PROC SQL sin WHERE, sin JOIN y con solo lista de columnas con alias. En IR, nodo de proyección sin predicado; fusionable con el nodo anterior o siguiente.
- **Riesgos:** `SELECT *` dentro de estas proyecciones depende del orden de columnas; y el `OUTER UNION CORR` posterior (P11) alinea por nombre, así que un alias mal escrito crea una columna nueva sin error.

### P08. Filtro por predicado complementario (cumple / no cumple)
- **Firma:** dos consultas sobre la misma fuente con `WHERE X = k` y `WHERE X <> k`, o con predicados que se excluyen entre sí, y la misma lista de columnas en ambas.
- **Frecuencia:** 8 pares. La regla de código aparece 16 veces (`RELACION = 9902` y `<> 9902`). Pares en líneas 2278/2607, 3176/3197, 3474/3490, 4794/5123, 5692/5713, 5990/6006. Pares de rangos en 3572-3573 y 6087-6089.
- **Evidencia:**
  ```
  2276 FROM WORK.SABANA_... REEMPLAZO_NID_EXT_AHO
  2277 WHERE
  2278   ( REEMPLAZO_NID_EXT_AHO.RELACION <> 9902 ) ;
  2605 WHERE
  2606   ( REEMPLAZO_NID_EXT_AHO.RELACION = 9902 ) ;
  ```
- **Intención:** separar registros que pasan la regla de los que no, y tratar cada grupo por separado.
- **Clasificación:** lógica de datos (enrutamiento).
- **Diseño Talend:** un tMap con N salidas, cada una con su filtro en la expresión de salida. Es la forma idiomática y reemplaza las N consultas. Si hay un tercer caso (NULL), va a una salida propia.
- **Detección:** en IR, pares de predicados sobre la misma fuente con la misma proyección. Es un grupo de particiones; el planificador lo convierte en un tMap multi-salida.
- **Riesgos:** un valor NULL no cumple `= k` ni `<> k`, y se pierde en silencio. Hay que tener una salida de "resto". En este tramo la condición de la regla también aparece en dos segmentos (AHO y CTE), con literal repetido.

### P09. Partición por valor de código (una consulta por valor)
- **Firma:** varias consultas `CREATE TABLE ... WHERE t.TIPO = v AND NRO NOT BETWEEN a AND b`, una por valor, unidas después (P11).
- **Frecuencia:** 6 consultas (una por tipo de documento) en 7009-7177.
- **Evidencia:**
  ```
  7011 CREATE TABLE WORK.DOC_INCORRECTOS_TPO8_NEQUI AS
  7034 WHERE t1.TIPO_DOC = 8 AND t1.NRO_DOC NOT BETWEEN 50000000000 AND 59999999999;
  7062 WHERE t1.TIPO_DOC = 7 AND t1.NRO_DOC NOT BETWEEN 4000000000 AND 4999999999;
  ```
- **Intención:** validar el número de documento según el rango permitido para cada tipo.
- **Clasificación:** validación.
- **Diseño Talend:** una tabla de reglas (tipo, mínimo, máximo) cargada como lookup, y un tMap que aplica la regla del tipo de cada fila. Una sola salida de rechazo.
- **Detección:** en IR, varias consultas con el mismo esquema que difieren solo en un literal de tipo y en rangos. Es un bloque parametrizable.
- **Riesgos:** la cadena de cuatro `AND ... NOT BETWEEN` del tipo 4 (líneas 7090-7092) exige estar fuera de los cuatro rangos a la vez. Hay que confirmar que esa es la intención. Los rangos están fijados en el código.

### P10. Validación campo a campo (dominio, rango, nulo)
- **Firma:** `WHERE col IS MISSING OR ...` (lista OR de nulos), `WHERE col NOT BETWEEN a AND b`, `WHERE (col = 0) OR col IS MISSING`.
- **Frecuencia:** 39 `IS MISSING`, 13 `NOT BETWEEN`, 19 `BETWEEN` en total.
- **Evidencia:**
  ```
  3753 WHERE t1.RELACION IS MISSING OR t1.TIPO_CTA IS MISSING OR t1.NRO_CTA IS MISSING OR t1.LLAVE_NOMBRE IS MISSING OR
  3754      t1.TIPO_DOC IS MISSING OR t1.NRO_DOC IS MISSING OR ( t1.GMF IS MISSING AND t1.RELACION = 1000 ) OR
  ```
- **Intención:** asegurar que los campos obligatorios estén llenos, que los códigos estén en dominio y que los importes estén en rango (tipo de cuenta 1 a 5, GMF 1 a 10).
- **Clasificación:** validación/reconciliación.
- **Diseño Talend:** tSchemaComplianceCheck para nulidad, longitud y tipo; después un tMap con las reglas de dominio y rango, y salida de rechazo con el motivo. Las reglas de dominio en una tabla de referencia.
- **Detección:** en IR, nodo de regla por campo con predicado de dominio, rango o nulo. Agrupar las reglas por tabla de salida.
- **Riesgos:** `NOT BETWEEN` con NULL no selecciona la fila; la validación de rango se pierde para nulos si no hay una regla de nulidad aparte. Los rangos y los códigos están fijados en el código.

### P11. Unión de bloques con esquemas parecidos (OUTER UNION CORR)
- **Firma:** `SELECT * FROM A OUTER UNION CORR SELECT * FROM B OUTER UNION CORR SELECT * FROM C;` y `UNION ALL` con literal.
- **Frecuencia:** 28 `OUTER UNION CORR`, 2 `UNION ALL`.
- **Evidencia:**
  ```
  7197 CREATE TABLE WORK.INCONSISTENCIAS_NEQUI AS
  7200 SELECT * FROM WORK.NRO_DOC_VACIOS_NEQUI
  7201  OUTER UNION CORR
  7202 SELECT * FROM WORK.TIPO_CTA_INVALIDO_NEQUI
  ```
- **Intención:** juntar todos los rechazos en una sola lista.
- **Clasificación:** validación/consolidación.
- **Diseño Talend:** tUnite con todos los flujos de rechazo de los tMap de validación.
- **Detección:** en IR, nodo de unión; `CORR` indica alineación por nombre, `UNION ALL` por posición.
- **Riesgos:** `OUTER UNION CORR` alinea por nombre y rellena con missing. Un nombre distinto crea una columna nueva. En NEQUI el campo de motivo se llama `INCONSISTENCIAS` (línea 7032) y en los demás `INCONSISTENCIA`. Esa diferencia hace que la unión tenga dos columnas de motivo.

### P12. Deduplicación por clave y exceso de duplicados
- **Firma:** `SELECT DISTINCT ... ` sobre todas las columnas, o `GROUP BY claves, COUNT(*) AS FRECUENCIA ... WHERE FRECUENCIA > 1`, y `CASE WHEN FRECUENCIA > 2 THEN FRECUENCIA - 2 ELSE 0 END`.
- **Frecuencia:** 7 DISTINCT, 9 GROUP BY.
- **Evidencia:**
  ```
  3335 create table work.CONCILIACION_DUPLICADOS_AHO AS
  3338 SELECT FRECUENCIA,
  3339 CASE
  3340 WHEN FRECUENCIA>2
  3341 THEN FRECUENCIA-2
  ```
- **Intención:** contar cuántos registros sobran por duplicidad, y eliminar duplicados exactos.
- **Clasificación:** validación.
- **Diseño Talend:** tAggregateRow agrupando por claves y contando; tMap para el exceso (`count > 2 ? count - 2 : 0`); tUniqRow para el DISTINCT.
- **Detección:** en IR, nodo de agregado por claves con conteo y filtro por conteo mayor que uno.
- **Riesgos:** `FRECUENCIA - 2` fija que dos ocurrencias son válidas. Esa es una regla de negocio escondida en la fórmula. El DISTINCT sobre todas las columnas puede borrar duplicados legítimos si una columna con datos de auditoría cambia.

### P13. Enriquecimiento por join con referencia (LEFT / INNER JOIN)
- **Firma:** `LEFT JOIN ref ON a.k = ref.k` o `INNER JOIN ref ON a.k = ref.k` donde `ref` viene de una importación o de Impala.
- **Frecuencia:** 19 LEFT JOIN, 24 INNER JOIN.
- **Evidencia:**
  ```
  2096 CAST(B.cod_tipo_doc AS DECIMAL(1,0)) AS CNCDTI,
  2099 FROM proceso_vspc_finanzas.COLUMNAS_DEPOSITOS A
  2100 LEFT JOIN (
  2107 ON A.LLAVE_NOMBRE = B.llave_sistema
  ```
- **Intención:** traer el tipo y número de documento del maestro de clientes, y homologar códigos (tipo de documento contra la tabla de homologación).
- **Clasificación:** lógica de datos.
- **Diseño Talend:** tMap con lookup (modo de carga "Load once" para catálogos pequeños, "Reload at each row" si el maestro es grande), con "Unique match" si la clave es única. Si la referencia es grande, se hace el join dentro de Impala con tImpalaInput (P15).
- **Detección:** en IR, join con clave igual a un dataset de referencia. Si la referencia viene de Impala, se marca como candidato a ELT.
- **Riesgos:** la referencia de cliente se une por `llave_sistema` sin que la clave sea única en el origen. Un LEFT JOIN con clave repetida multiplica filas en silencio. Hay que validar la unicidad antes del join.

### P14. Semi-join y anti-join en SAS (partición por pertenencia)
- **Firma:** `LEFT JOIN X ON ... WHERE X.k IS MISSING` (anti) o `INNER JOIN X ON ...` que deja solo coincidentes (semi).
- **Frecuencia:** 39 `IS MISSING` en el tramo; las uniones de partición están en 1404-1447, 2696-2731 y 8282.
- **Evidencia:**
  ```
  1443 LEFT JOIN WORK.PQTE_AFC PQTE_AFC
  1444 ON
  1445   ( DBIFTCS_FORMATO.NRO_CTA = PQTE_AFC.NRO_CTA )
  1446 WHERE PQTE_AFC.NRO_CTA IS MISSING ;
  ```
- **Intención:** separar registros que tienen o no tienen correspondencia (por ejemplo, firmas autorizadas vigentes o no).
- **Clasificación:** lógica de datos.
- **Diseño Talend:** tMap con lookup y dos salidas: "match" y "rechazo" (Catch lookup inner join rejection). No hace falta un segundo join.
- **Detección:** en IR, LEFT JOIN seguido de filtro IS MISSING sobre la clave del lado derecho. Es un anti-join.
- **Riesgos:** igual que P13 (clave repetida). Además, si el lado derecho es un resultado intermedio, el join se repite en cada segmento.

### P15. Pass-through SQL al motor (ELT)
- **Firma:** `connect to IMPALA (DSN=...); create table WORK.x as select * from connection to IMPALA (SELECT ...); disconnect ...;` o `execute (...) by impala;`.
- **Frecuencia:** 28 `connect to`, 9 `from connection to`, 19 `execute by` o `execute (...)`.
- **Evidencia:**
  ```
  189 connect to IMPALA (DSN = IMPALAP);
  190 EXECUTE BY IMPALA (
  191 create table proceso_vspc_finanzas.mcdq stored as parquet as
  192 select i.cod_tipo_doc,
  ...
  209 where i.YEAR=&ANIO. AND i.MONTH=&MES. and i.ingestion_day=&MDAY.)
  ```
  Y la agregación en el motor:
  ```
  3282 proc sql;
  3283 connect to IMPALA (DSN = IMPALAP);
  3284 create table WORK.FRECUENCIA_REGISTROS_AHO as
  3287     count(*) as FRECUENCIA,
  ```
- **Intención:** hacer el join, el filtro por periodo y la agregación en Impala, donde están los datos.
- **Clasificación:** E/S (ELT).
- **Diseño Talend:** tImpalaInput con la consulta en el motor (ELT), tImpalaRow para DDL (`CREATE TABLE ... AS SELECT`). No se trae la tabla a SAS para volver a escribirla.
- **Detección:** léxica `connect to <motor>`, `connection to`, `execute ... by`. En IR, nodo de consulta remota con dialecto del motor; el migrador debe conservar el texto SQL tal cual.
- **Riesgos:**
  - Dentro del pass-through hay un `;` antes del paréntesis de cierre (líneas 2668-2669 y 5184-5185). Puede fallar en el motor.
  - Dialectos mezclados: `CAST(... AS VARCHAR(30))` en un bloque y `AS STRING` en otro (2084 frente a 4600).
  - `ORDER BY` dentro de consultas que alimentan otros pasos es costoso y no se usa.
  - Hay tablas de trabajo que se borran con `drop table ... purge` (P23).

### P16. Agregado por clave y reunión de vuelta por umbral
- **Firma:** `SELECT clave, SUM(a) AS s1, SUM(b) AS s2 FROM X GROUP BY clave` seguido de `INNER JOIN` del agregado al detalle con filtro `s1 >= umbral OR s2 >= umbral`.
- **Frecuencia:** 2 (líneas 8210-8236 y su equivalente), con umbral 1129560.
- **Evidencia:**
  ```
  8212 SELECT CONSOLIDADO_SIN_NEGATIVOS.NRO_DOC, SUM(CONSOLIDADO_SIN_NEGATIVOS.VAL_CRED_MES)
  8213 AS SUMA_MOV_CRED, SUM(CONSOLIDADO_SIN_NEGATIVOS.FIN_SALDO_CTA)
  8232 WHERE
  8234   ( SUMA_SALDOS_POR_NRO_DOC.SUMA_MOV_CRED >= 1129560 ) OR
  ```
- **Intención:** identificar a los documentos cuyo movimiento o saldo supera el umbral de la norma y luego llevar esa marca a cada registro del detalle.
- **Clasificación:** lógica de datos (regulatorio).
- **Diseño Talend:** tAggregateRow agrupado por documento y sumas; tMap con lookup a ese agregado (cargado una vez) y filtro en la salida. El umbral en contexto.
- **Detección:** en IR, agregado seguido de join de vuelta a la fuente original por la misma clave. Patrón de "ventana por clave".
- **Riesgos:** el umbral es literal. La suma incluye valores ya saneados a cero (P19); cambiar el orden de saneamiento cambia el resultado. Hay un `GROUP BY` con la misma columna dos veces (línea 8216), que no altera el resultado pero indica copia.

### P17. Conciliación de conteo y saldo (control totals)
- **Firma:** `SELECT SUM(x) AS s FROM T` y `SELECT COUNT(k) AS n FROM T` en tablas de una fila, unidas por producto cartesiano (`FROM A, B, C ...` sin WHERE), y luego fórmulas `DIF = total - (parte1 + parte2 + ... - repetidos)`.
- **Frecuencia:** 14 SUM, 15 COUNT. Fórmulas en 4087, 4117, 6603, 6633, 7305, 7335.
- **Evidencia:**
  ```
  4063 SELECT VALIDACION_NRO_REGISTROS_AHO.NRO_REGISTROS, CUENTA_INCONS_CORR_DEP_AHO...
  4064 FROM WORK.VALIDACION_NRO_REGISTROS_AHO VALIDACION_NRO_REGISTROS_AHO, WORK.CUENTA_INCONS_CORR_DEP_AHO ...
  4087 CONCILIACION_REG=NRO_REGISTROS-(NRO_REG_SABANA_FINAL+NRO_REGISTROS_INCONS_CORREGIDOS+...-INCONS_REPETIDAS);
  4117 CONCILIACION_SALDOS=SUMA_SALDO_INICIAL-(SUMA_SALDO_FINAL_DEP_AHO+SUMA_SALDO_INCONS_DEP_AHO);
  ```
- **Intención:** demostrar que todos los registros de entrada están en una salida (sabana, incidencia, duplicado) y que la suma de saldos cuadra.
- **Clasificación:** validación/reconciliación.
- **Diseño Talend:** tAggregateRow por cada flujo (count y sum); tJavaRow o tMap que calcula las diferencias en una sola fila; tJava que lanza error con tDie si la diferencia no es cero, o tAssert. El resultado de conciliación se escribe a una tabla de control.
- **Detección:** en IR, varios agregados de una fila unidos sin condición, y una fórmula sobre sus columnas. Es un nodo de conciliación.
- **Riesgos:** el producto cartesiano solo es correcto si cada tabla tiene exactamente una fila. Si una tabla queda vacía, la conciliación da cero y pasa sin error. La fórmula de conciliación de registros resta los repetidos al final; hay que validar esa identidad con el área.

### P18. Coalesce manual por CASE
- **Firma:** `CASE WHEN (x = 0 OR x = .) THEN fallback ELSE x END AS y`.
- **Frecuencia:** 4 (2 por cada pipeline de cuenta de ahorros y corriente).
- **Evidencia:**
  ```
  2117 CASE
  2118 WHEN(CNCDTI=0 OR CNCDTI=.) THEN TIPO_DOC
  2119 ELSE CNCDTI
  2120 END AS TIPO_DOC_CNAME,
  ```
- **Intención:** usar el dato del maestro si existe; si no, el dato original.
- **Clasificación:** lógica de datos.
- **Diseño Talend:** expresión en tMap: `(row.cncdti == null || row.cncdti == 0) ? row.tipo_doc : row.cncdti`.
- **Detección:** en IR, CASE con condición de nulo o cero y rama de respaldo; es un coalesce.
- **Riesgos:** el cero se trata como vacío. Si cero es un valor válido en el maestro, se pierde.

### P19. Derivaciones fila a fila (concatenación de clave, prefijo, recorte a cero)
- **Firma:** `CAT(a, b, c, d)` para clave compuesta; `CASE WHEN (cond) THEN substr(COMPRESS(put(x,15.)),2,8) ELSE ... END` para quitar prefijo; `IFN(x < 0, 0, x)` para recorte.
- **Frecuencia:** 2 `CAT` de clave compuesta, 2 derivaciones de prefijo, 2 `IFN` de recorte a cero.
- **Evidencia:**
  ```
  2148 CONCAT=CAT(LLAVE_NOMBRE, NRO_CTA, NRO_DOC_CNAME, RELACION);
  2193 WHEN ((TIPO_DOC=2) AND (NRO_DOC between 300000000 AND 399999999))
  2194 THEN substr(COMPRESS(put(NRO_DOC,15.)),2,8)
  8176 VAL_CRED_MES=IFN(VAL_CRED_MES<0, 0, VAL_CRED_MES);
  ```
- **Intención:** construir la clave de cruce, quitar el primer dígito a documentos extranjeros con un prefijo conocido, y poner a cero los saldos negativos.
- **Clasificación:** lógica de datos.
- **Diseño Talend:** expresiones en tMap: `StringBuilder` o `+` para la clave; `(x<0)?0:x` para el recorte; `substring` para el prefijo.
- **Detección:** en IR, asignaciones con funciones de cadena o condicionales sobre una sola fila.
- **Riesgos:** `CAT` no quita espacios finales; `CATX` sí. El recorte a cero cambia las sumas posteriores (P16, P17). El prefijo está fijado por un rango de números.

### P20. Fecha de periodo y vigencia
- **Firma:** `PUT(MES, Z2.)` para mes con cero a la izquierda; `CAT(AÑO, MES_VIG)` para `yyyymm`; `input(left(FECHA), 6.)` para pasar a número; comparaciones con `&FECHA_VALIDACION`.
- **Frecuencia:** 2 `PUT(..., Z2.)`, 2 `CAT(AÑO, ...)`, 4 comparaciones con la fecha de validación.
- **Evidencia:**
  ```
  1665 MES_VIG=PUT(MES, Z2.);
  1703 FECHA_VALIDACION=CAT(AÑO, MES_VIG);
  2777 WHERE FECHA_VIG < &FECHA_VALIDACION;
  2790 WHERE FECHA_VIG >= &FECHA_VALIDACION;
  ```
- **Intención:** comprobar que la sabana corresponde al periodo de proceso y separar firmas vigentes de no vigentes.
- **Clasificación:** validación.
- **Diseño Talend:** expresión en tMap: `String.format("%d%02d", anio, mes)` y comparación con `context.fechaValidacion`; tFilterRow o tMap multi-salida para vigentes y no vigentes.
- **Detección:** en IR, asignación de periodo y filtro contra variable de proceso (P21).
- **Riesgos:** `AÑO` tiene una letra no ASCII; se referencia con `'AÑO'n` en un join (1640) y sin comillas en otro (1703). Hay que confirmar que los dos apuntan a la misma columna. La comparación de texto contra número depende del tipo.

### P21. Parámetros de proceso desde tabla de un registro (INTO:)
- **Firma:** `SELECT col INTO :macro FROM tabla_de_control;`
- **Frecuencia:** 22 `INTO`, 11 de año, mes y día, 4 de la fecha de validación.
- **Evidencia:**
  ```
  169 SELECT AÑO INTO: ANIO FROM WORK.VALIDACION_FECHA;
  170 SELECT MES INTO: MES FROM WORK.VALIDACION_FECHA;
  171 SELECT DIA INTO: DIA FROM WORK.VALIDACION_FECHA;
  ```
- **Intención:** leer el periodo de proceso una vez y usarlo en todas las consultas posteriores.
- **Clasificación:** parametrización.
- **Diseño Talend:** tImpalaInput o tFileInputDelimited de una fila, después tJava o tContextLoad que asigna el valor a una variable de contexto. Si el flujo se repite por segmento, se usa tFlowToIterate.
- **Detección:** en IR, asignación de macro-variable desde una consulta de una fila. Es una dependencia de datos del paso siguiente.
- **Riesgos:** si la tabla tiene más de una fila, SAS asigna la última sin error. Hay que validar que hay exactamente una fila (P22).

### P22. Gate de continuación (abort si cero filas)
- **Firma:** `Data _null_; set CONTEO; if NRO_REGISTROS=0 THEN abort CANCEL; run;`
- **Frecuencia:** 2 (líneas 1709-1712 y 4225-4228).
- **Evidencia:**
  ```
  1709 Data _null_;
  1710 Set WORK.VALIDACION_NRO_REGISTROS_AHO;
  1711 if NRO_REGISTROS=0 THEN abort CANCEL;
  ```
- **Intención:** no continuar con la carga si el conteo de la fuente es cero.
- **Clasificación:** orquestación.
- **Diseño Talend:** tPreJob o un subjob con tJava que lanza excepción si el conteo es cero, con el disparador "Run if" y tDie.
- **Detección:** en IR, nodo de condición de aborto sobre un conteo.
- **Riesgos:** `abort CANCEL` en lote no siempre deja un código de salida útil; hay que comprobarlo en el planificador.

### P23. Carga masiva particionada a Impala (sesiones SAS + shell + polling)
- **Firma:** macro `split2` (abre sesiones `signon sessioN`, `rsubmit ... wait=no`, `waitfor _all_`), `create_commands` (inserta comandos `sh bulkload_generic.sh` en una tabla), `executeBulkload` (ejecuta con `x "&comando"` y `call sleep(2,1)`), `waitForBulkLoads` (espera con `ps -fea | grep` en bucle), `delProcessTables` (`drop table if exists ... purge`), `deleteTableLZ` (drop antes de cargar).
- **Frecuencia:** 6 copias de la librería (cada una 289 líneas), 6 puntos de escritura (líneas 1749, 2283, 2848, 4265, 4799, 5364) que la invocan. `split2` aparece 6 veces, `bulkload_generic` 6 veces.
- **Evidencia:**
  ```
  1902 data pwork.&tbltmp.&sessio.;
  1903 set wliborg.&tabla_origen. (&firstobs &obs);
  1916 waitfor _all_
  1964 insert into &cmdt. values("sh &wpathpgmbl.&wpgmbl. &workpath. &tablaW. &libdes. &tablaW. &tbldes_lz. &");
  1973 x " nroproc=5; until [ $nroproc -eq 0 ]; do nroproc=$( ps -fea | grep -i &wpgmbl. ... ) ; done ";
  ```
- **Intención:** cargar tablas de más de 1,5 millones de filas a Impala en trozos, en paralelo, con un script externo por trozo.
- **Clasificación:** E/S + orquestación.
- **Diseño Talend:** un solo job con tFileOutputDelimited o tImpalaOutput en modo lote con tamaño de lote configurado. Si el volumen lo exige, tParallelize o varias instancias del job en el Remote Engine. La librería de macros no se migra. El drop previo es un tImpalaRow.
- **Detección:** en IR, nodo de carga con partición por filas y ejecución externa. Léxicamente, `signon sessio`, `rsubmit ... wait=no`, `waitfor _all_` y `x "sh ..."`.
- **Riesgos:** el polling por `ps` es frágil. La búsqueda de tablas por `contains` del nombre puede coincidir con otras tablas. Un trozo que falla deja estado parcial, aunque `delProcessTables` solo borra cuando `syserr=0`. `sleep` fijo introduce latencia sin control.

### P24. Bundle de macros duplicado
- **Firma:** el mismo grupo de macros (`ambiente`, `delProcessTables`, `split2`, `create_commands`, `waitForBulkLoads`, `executeBulkload`, `execImpalaQuery`, `deleteTableLZ`, `tiempos`) repetido seis veces.
- **Frecuencia:** 6 copias. `%macro ambiente` aparece en 1772, 2306, 2871, 4288, 4822 y 5387. `%macro tiempos` en 2052, 2586, 3151, 4568, 5102 y 5667.
- **Evidencia:** cada copia empieza con `%include "/data/Programas_SAS/activenodelzcode.sas";` (líneas 1769, 2303, 2868, 4285, 4819, 5384) y tiene la misma estructura.
- **Intención:** la misma fontanería de carga, repetida por cada escritura (P23).
- **Clasificación:** fontanería.
- **Diseño Talend:** se elimina. Si queda lógica común, un joblet único.
- **Detección:** en el resolver de macros, mismo cuerpo de macro definido varias veces con el mismo nombre; cuerpos idénticos byte a byte salvo nombres de tabla.
- **Riesgos:** cualquier cambio hay que hacerlo seis veces. Esto es un candidato a error de copia (ya hay una copia con un `%let` duplicado, líneas 2041-2044).

### P25. Selector de entorno por código (D, C, P) y DSN
- **Firma:** `%macro ambiente; %if &m_ambiente eq D %then %do; %let lz_dsn=IMPALA; ... %end; ... %mend;`
- **Frecuencia:** 6 (una por copia de P24).
- **Evidencia:**
  ```
  1773 %if &m_ambiente eq D %then
  1777 %let lz_dsn=IMPALA;
  1783 %let lz_dsn=IMPALAC;
  1789 %let lz_dsn=IMPALAP;
  ```
- **Intención:** elegir el origen de datos según el entorno (desarrollo, certificación, producción).
- **Clasificación:** parametrización/entorno.
- **Diseño Talend:** contextos Dev, Cert y Prod con el DSN de Impala; el job se ejecuta con el contexto elegido.
- **Detección:** macro con rama `%if` sobre una variable de entorno y asignaciones de DSN en cada rama.
- **Riesgos:** la variable `m_ambiente` viene de un archivo externo que no está en el tramo. Hay que conseguirlo para la migración.

### P26. Literales de negocio embebidos
- **Firma:** constantes numéricas o de texto en filtros y fórmulas: `RELACION = 9902`, `RELACION = 1000`, `>= 1129560`, rangos de NID, `'CTA NEQUI'`, `TIPO_CTA IN (1.0, 3.0, 4.0, 5.0)`.
- **Frecuencia:** 16 apariciones del código 9902; 1000 en 4 reglas; umbral 1129560 en 2 líneas.
- **Evidencia:**
  ```
  8234 ( SUMA_SALDOS_POR_NRO_DOC.SUMA_MOV_CRED >= 1129560 ) OR
  8297 ( SABANA_CUMPLE_NORMA.TIPO_CTA IN ( 1.0, 3.0, 4.0, 5.0 ) ) AND
  ```
- **Intención:** reglas de negocio de la norma y de la relación de productos.
- **Clasificación:** parametrización.
- **Diseño Talend:** variables de contexto o una tabla de reglas cargada como lookup.
- **Detección:** léxica, literales numéricos o de texto dentro de WHERE o expresiones de negocio sin nombre.
- **Riesgos:** el mismo valor puede aparecer escrito de distinta forma (`1.0` y `1`). Si cambia la norma, hay que cambiar cada aparición.

### P27. Trazas, medición y metadatos de ejecución
- **Firma:** `%macro tiempos; %put INICIO: &hi.; %put FINAL: %sysfunc(strip(%sysfunc(datetime(), datetime20.))); %mend;`, `options symbolgen mprint source;`, `%put &=workpath;`.
- **Frecuencia:** 6 `%tiempos`, 18 `datetime`, 28 `options`.
- **Intención:** registrar el inicio y fin de la carga.
- **Clasificación:** trazas/medición.
- **Diseño Talend:** se descarta. Talend registra tiempos con tStatCatcher y tFlowMeter, y los logs del job.
- **Detección:** léxica `datetime(|%put|options (sym|m)`.
- **Riesgos:** ninguno funcional. `mprint` en producción puede imprimir datos en el log.

### P28. Fontanería de la interfaz SAS Studio
- **Firma:** `%web_drop_table(WORK.x);` antes de cada `CREATE TABLE` y `%web_open_table(WORK.x);` después; cabeceras de tarea (`Código de la tarea generado por SAS Studio ...`); `TITLE "$outputDSName"`; `FOOTNOTE1 "Generated by the SAS System ..."`.
- **Frecuencia:** 126 `%web_drop_table`, 125 `%web_open_table`, 102 cabeceras "Generado el", 7 `TITLE "$outputDSName"`.
- **Evidencia:**
  ```
  235 %web_drop_table(WORK.COLUMNAS_BASE_NEQUI);
  252 %web_open_table(WORK.COLUMNAS_BASE_NEQUI);
  ```
- **Intención:** ninguna de negocio. Sirve para borrar y reconstruir la tabla de trabajo y para mostrarla en la interfaz de SAS Studio.
- **Clasificación:** fontanería.
- **Diseño Talend:** se descarta. Talend no necesita borrar la tabla intermedia porque no existe.
- **Detección:** léxica `%web_(drop|open)_table`, `Common Query Services`, `Generado por`. Es el filtro más seguro para eliminar código antes de traducir.
- **Riesgos:** `%web_drop_table` es también un borrado. Hay que confirmar que no se usa como limpieza en un camino que el migrador deba conservar.

## 3. Diseño objetivo del tramo en Talend (estimación)

Las 290 etiquetas se reducen a tres Jobs y un joblet, que reemplazan la estructura por segmento.

1. **J00_Orquestador**: tPreJob con P22 (gate) y P25 (contexto de entorno). tFlowToIterate sobre los segmentos (AHO, CTE, NEQUI) con tRunJob hacia J10. Después tRunJob hacia J20.
2. **J10_Ingesta_y_Validacion** (una ejecución por segmento, con el contexto del segmento):
   - 5 tFileInputExcel (catálogos, P01) y 4 tFileInputDelimited con ruta UNC (P02, P03), sin descarga intermedia.
   - tImpalaInput para el periodo de proceso (P21) y para el maestro de clientes (P15, ELT).
   - tMap de tipado (P05) con lookup a catálogos (P13) y reglas de dominio y rango en tabla de referencia (P09, P10).
   - tMap multi-salida con filtro por regla (P08): válidos, rechazos por motivo (P06).
   - joblet JL_Validacion_Segmento (P10 + P12) si se quiere reutilizar la regla.
   - tUnite de los rechazos (P11) y tAggregateRow para conteos y sumas (P17).
   - tJavaRow con las fórmulas de conciliación (P17) y tDie si no cuadra.
3. **J20_Carga_Impala**: tImpalaRow con drop previo (P23), tImpalaOutput en modo lote con la sabana final de cada segmento.

Conteo esperado: 3 Jobs (1 orquestador y 2 de trabajo), 1 joblet, unos 20 componentes distintos (5 tFileInputExcel, 4 tFileInputDelimited, 2 tImpalaInput, 2 tImpalaRow, 1 tImpalaOutput, 3 tMap, 1 tUnite, 1 tAggregateRow, 1 tUniqRow, 1 tJavaRow, 1 tDie, 1 tPreJob, 1 tFlowToIterate, 1 tRunJob), y unos 40 nodos en total. Ninguna macro, ninguna copia de vuelta, ningún shell, ningún polling.

## 4. Tabla patrón → capa de implementación → prioridad

Prioridad = frecuencia × impacto (A alta, M media, B baja). "Descartar" significa que el migrador elimina el patrón sin traducirlo.

| Patrón | Capa de implementación | Prioridad | Motivo |
|---|---|---|---|
| P05 Copia de vuelta y conversión de tipo | IR (fusionar en tMap) + traductor | A | 82 bloques, cero componentes en destino |
| P23 Carga masiva particionada | macro resolver (colapsar 6 copias) + planificador (una escritura tImpalaOutput) | A | ~1.730 líneas de duplicado |
| P24 Bundle de macros duplicado | macro resolver (deduplicar) | A | elimina la copia |
| P15 Pass-through ELT | parser SQL (detectar connection) + traductor a tImpalaInput | A | evita traer datos a SAS |
| P08 Filtro complementario | IR (agrupar predicados) + planificador (tMap multi-salida) | A | 8 pares, 16 apariciones |
| P10 Validación campo a campo | IR (reglas) + traductor (tSchemaComplianceCheck, tMap) | A | calidad de datos |
| P13 y P14 Join y anti-join | IR (join con referencia) + traductor (tMap lookup con rechazo) | A | 43 uniones |
| P17 Conciliación | IR (agregados de una fila) + traductor (tAggregateRow, tJavaRow, tDie) | A | control de cierre |
| P11 OUTER UNION CORR | traductor (tUnite) | M-A | 30 uniones |
| P26 Literales de negocio | IR (extraer constantes a contexto) | M | cambios de norma |
| P25 Selector de entorno | macro resolver + contextos | M | migración de entornos |
| P04 Credenciales | contexto secreto (traductor) | A | seguridad, valor comprometido |
| P01 y P02 Excel y CSV | traductor (tFileInputExcel, tFileInputDelimited) | M | E/S básica |
| P03 Descarga remota | traductor (ruta UNC o tFileFetch) | M | elimina copia local |
| P09 Partición por código | IR (bloque parametrizable) + tabla de reglas | M | 6 consultas |
| P12 Deduplicación | traductor (tAggregateRow, tUniqRow) | M | |
| P07 Proyección y renombrado | IR (fusionar con paso vecino) | M | 19 pasos |
| P18 y P19 Derivaciones fila a fila | traductor (expresiones en tMap) | M | |
| P20 Fecha y vigencia | traductor (expresión + contexto) | M | |
| P21 INTO macro-variables | IR (dependencia de datos) + contexto | M | 22 apariciones |
| P16 Agregado por umbral | traductor (tAggregateRow + tMap lookup) | M | dos apariciones, alto impacto |
| P06 Etiqueta constante | traductor (columna constante en tMap) | B-M | 13 apariciones |
| P22 Gate | traductor (tPreJob, tDie) | B | 2 apariciones |
| P27 Trazas | descartar | B | |
| P28 Fontanería SAS Studio | descartar | A (para filtrar) | 250 apariciones, sin valor de negocio |

## Conclusiones principales del tramo

1. **El tramo es un proceso repetido en tres segmentos y una librería de carga copiada seis veces.** Las cadenas de ahorros, corriente y Nequi son casi idénticas. La librería de carga ocupa unas 1.730 líneas (21 %). Migrar a un job parametrizado por segmento con iteración evita tres cadenas casi iguales y las seis copias de macros.
2. **La conversión de tipo con copia de vuelta son 82 bloques que en Talend no requieren componentes.** Cada conversión se vuelve una expresión tipada en el tMap de entrada. Hay que tratar los errores de `input()` como rechazos, porque hoy pasan como missing en silencio. Y hay que unificar longitudes: el saldo mínimo usa `8.` (línea 8004-8006) mientras el resto usa `20.`.
3. **La validación se resuelve con una salida por regla y uniones de rechazos.** Las 16 apariciones del código 9902 y los pares complementarios (P08) se convierten en un tMap multi-salida. Los 28 `OUTER UNION CORR` son un tUnite. Los `LEFT JOIN ... IS MISSING` son un lookup con rechazo. Hay que cuidar la salida de "resto" para no perder NULL.
4. **El tramo ya empuja SQL a Impala (28 conexiones), pero mezcla el trabajo.** Trae datos a SAS para unirlos y devolverlos. El migrador debe conservar el SQL en tImpalaInput y evitar leer, transformar y escribir. Hay que validar que la clave de referencia del maestro de clientes es única antes del join (P13), porque si no multiplica filas.
5. **Hay divergencias y riesgos concretos en el código fuente, que el migrador debe señalar y no copiar.**
   - La validación de tipo de cuenta de Nequi usa la columna `INCONSISTENCIAS` (7032) y las demás usan `INCONSISTENCIA`.
   - El join de tipo de cuenta de cuenta corriente va por `RELACION` (6137), mientras que el de ahorros va por `NRO_CTA` (3621). El primero produce un producto cartesiano por relación.
   - El pass-through tiene un `;` antes de cerrar el paréntesis (2668-2669 y 5184-5185).
   - La contraseña está codificada con `pwencode` (línea 77). Hay que tratarla como comprometida y no migrar el valor.
