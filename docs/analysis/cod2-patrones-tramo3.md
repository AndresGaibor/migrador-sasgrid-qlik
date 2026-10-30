# Cod2.txt, tramo 16601-24801: patrones SAS y diseño objetivo en Talend

Fuente: `C:\Users\USUARIO_BISOLUTION1\Downloads\Cod2.txt`, líneas 16601 a 24801 (8.201 líneas), leídas completas en tramos de 500 líneas. Los conteos se hicieron con grep sobre una copia del tramo. Los números de línea son los del archivo original.

Limitaciones del tramo:
- Empieza a mitad de una macro. Las líneas 16601-16625 son el final de `%macro executeBulkload` de un bloque anterior.
- Las tablas de catálogo (`WORK.IMPORT_CODIGOS_DANE`, `IMPORT_CODIGOS_PAIS`, `IMPORT_HOMOLOGACION_TPO_DOC`, `HOMOLOGACION_TPO_DTO_NEQUI`) y las de origen (`SABANA_COMPLETA_*`, `DOC_INCOR_*`) se usan aquí pero se crean fuera del tramo.
- No hay lectura de ficheros en el tramo (`PROC IMPORT` = 0) ni descarga remota. Solo hay escritura: exportación y subida a una ruta de red.

Nota de privacidad: los comentarios de cabecera contienen nombres de usuario y de servidor. No deben copiarse al migrador.

---

## Cifras del tramo

| Métrica | Valor |
|---|---|
| Etiquetas `/* Etiqueta: ... */` (un "paso" lógico cada una) | 157 |
| `PROC SQL` | 179 |
| `DATA step` (incluye copias de vuelta) | 104 |
| `CASE` / `IS MISSING` / `CATS(` / `LIKE` | 102 / 101 / 87 / 76 |
| Sentencias pass-through a Impala (`connect to`, `connection to`, `execute`) | 49 / 79 |
| `DROP TABLE ... PURGE` / `proc delete` | 65 / 33 |
| `OUTER UNION CORR` / `COUNT(` / `ROUND(` | 20 / 20 / 24 |
| `%web_drop_table` / `%web_open_table` (wrapper de SAS Studio) | 50 / 50 |
| Cabeceras de "Código de la tarea generado por SAS Studio" | 22 |
| `proc export` + `PROC UPLOAD` (pares de exportación y subida) | 22 + 22 |
| Bloques de carga bulk por particiones (macro `split2`) | 11 (~313 líneas cada uno, ~3.440 líneas, 42% del tramo) |
| Poblaciones con pipeline idéntico (sufijos `_AHO`, `_CTE`, `_NEQUI`) | 3 |

Se identifican **22 patrones**. Varios aparecen repetidos con pequeñas variaciones (patrones P01, P02, P03, P04, P05, P06, P07, P08, P22). Esas repeticiones son candidatas a un único job parametrizado o a un joblet.

---

## Patrones

### P01. Carga masiva particionada a la base (bulk-load por sesiones remotas, shell y espera)

1. **Nombre genérico:** carga por particiones con sesiones paralelas y script externo.
2. **Firma estructural:** un juego de macros copiado en cada bloque. `split2` calcula `num_splits = ceil(n / wobs)`, abre `signon sessioN`, pasa variables con `%syslput`, ejecuta `rsubmit ... wait=no` con `data pwork.T set origen (firstobs obs)`, y cierra con `waitfor _all_`. Después `create_commands` escribe en una tabla de comandos `insert into ... values("sh script ...")`. `executeBulkload` ejecuta cada comando con `x "&comando"` y `call sleep(2,1)`. `waitForBulkLoads` hace un bucle de `ps -fea | grep` hasta que termina. `deleteTableLZ` y `delProcessTables` limpian.
3. **Frecuencia y ejemplos:** 11 bloques idénticos salvo la tabla origen y destino.
   - 16608-16617: `set &cmdt.(obs=&i)`, `call symputx('comando', cmdbl, 'G')`, `x "&comando";`.
   - 16847-16849: `data pwork.&tbltmp.&sessio.; set wliborg.&tabla_origen. (&firstobs &obs); newVar=int(ranuni(_n_) * 1000);`
   - 16862-16865: `waitfor _all_ %do i=1 %to &num_splits; sessio&i %end; ;`
   - 16909: `insert into &cmdt. values("sh &wpathpgmbl.&wpgmbl. &workpath. &tablaW. &libdes. &tablaW. &tbldes_lz. &");`
   - 16918: `x " nroproc=5; until [ $nroproc -eq 0 ]; do nroproc=$( ps -fea | grep -i &wpgmbl. ... ); done ";`
4. **Intención:** volcar una tabla de SAS a la zona de aterrizaje en Impala, en trozos de 1,5 millones de filas, para acelerar la carga.
5. **Clasificación:** E/S más fontanería de paralelismo.
6. **Diseño Talend mínimo:**
   - Un único job genérico con contexto (`tabla_origen`, `tabla_destino`).
   - Fuente en Impala: `tImpalaInput` y `tImpalaOutput` con acción Create o Drop-and-create.
   - Fuente en fichero: `tFileInputDelimited` y `tImpalaOutput`. Si el catálogo MCP confirma que existe, `tImpalaLoad`. Si no, `tImpalaRow` con `LOAD DATA`.
   - No se emulan sesiones ni espera por `ps`. La ejecución síncrona de `tRunJob` sustituye a la espera.
   - Tres componentes en total, más la conexión.
7. **Detección:**
   - Léxica: `%macro` con nombres `split`, `bulk`, `load`; `x "..."`; `signon`, `rsubmit`, `waitfor`; `call sleep`.
   - AST: `DATA _null_` con `x "&macro"` dentro de `%do`.
   - Resolución de macros: expandir `%syslput` y la tabla de comandos.
   - IR: marcar el nodo como "carga por particiones" sin semántica de negocio y descartarlo, conservando solo origen y destino.
   - Variantes: `LOAD DATA` de Hive, `COPY` de Redshift o PostgreSQL, `bcp`. Mismo rol.
8. **Riesgos y falsos positivos:**
   - Si la base admite carga directa, el split no hace falta.
   - La espera por `ps | grep` puede dar falsos positivos por coincidencia de nombres.
   - El borrado de temporales solo ocurre si `&syserr. eq 0`. Si el job falla a mitad, quedan residuos.
   - No replicar rutas `/home_sas` ni nombres de servidor.

---

### P02. Exportación a CSV y copia a ruta de red (export + signon + RSUBMIT PROC UPLOAD)

1. **Nombre genérico:** exportar a fichero delimitado y subir a recurso remoto.
2. **Firma estructural:** `proc export data=WORK.X outfile="/ruta/X.csv" dbms=dlm replace; delimiter=';'; run;`, seguido de `%let server=...; OPTIONS REMOTE=server COMAMID=TCP; signon user=&sysuserid pass="&SASPC_PW"; RSUBMIT server; PROC UPLOAD INFILE=... OUTFILE="\\servidor\recurso\X.csv"; endrsubmit; signoff;`.
3. **Frecuencia y ejemplos:** 22 pares.
   - 24264-24276: `proc export data=WORK.FA_NO_VIGENTES_AHO outfile="/work_sasstudio/pcfiles/FA_NO_VIGENTES_AHO.csv"`; `dbms=dlm replace;`; `signon user=&sysuserid pass="&SASPC_PW";`; `RSUBMIT server;`; `PROC UPLOAD INFILE=...`.
   - 24349-24363 y 24502-24516: mismo par para `INCONS_INCORREC_TIT` y `INCONS_INCORREC_TIT_CTE`.
4. **Intención:** entregar los resultados de conciliación a una carpeta compartida del área.
5. **Clasificación:** E/S (salida) más fontanería (el fichero ya está en el mismo nodo; `signon` y `RSUBMIT` solo lo copian).
6. **Diseño Talend mínimo:**
   - Cada resultado se escribe directamente en la ruta UNC del contexto con `tFileOutputDelimited` (separador `;`, codificación fija). No hay exportación local ni subida.
   - Los 22 pares se sustituyen por unos pocos outputs parametrizados por población (ver sección A).
   - Si hace falta una copia por disco local, `tFileCopy`.
   - Credenciales: contexto o secreto cifrado de TMC/Studio, nunca texto plano.
7. **Detección:**
   - Léxica: `proc export` seguido de `PROC UPLOAD` con el mismo nombre de fichero.
   - AST: par consecutivo export-upload con el mismo `outfile`/`INFILE`.
   - IR: nodo de salida con destino remoto. Emparejar por nombre.
8. **Riesgos:**
   - Contraseña en la sesión (`pass="&SASPC_PW"`), 22 ocurrencias. Es un riesgo de seguridad a tratar como secreto.
   - Servidor y rutas UNC escritos en el código. Pasan a contexto.
   - No hay lectura de ficheros ni descarga remota en el tramo. Si aparece después, es un patrón distinto (PROC IMPORT o `tFileInputExcel`).

---

### P03. Cadena de validación por reglas (filtros SQL sucesivos sobre tablas intermedias)

1. **Nombre genérico:** validación en cascada, una tabla por regla.
2. **Firma estructural:** `CREATE TABLE FINAL_VALIDAR_X AS SELECT ... FROM previa t1 [LEFT|INNER JOIN catálogo] WHERE (regla)`. El `FROM` apunta siempre a la tabla del paso anterior. Orden en cada población: tipo de documento (join a homologación), número de documento, DV, nombres, ubicación, cuenta y GMF, monetarios, conteo.
3. **Frecuencia y ejemplos:** 21 etiquetas `Validar ...`, siete por población, más "Identificar diferencias" en AHO. Ejemplos:
   - 22657-22659: `( SABANA_CLIENTES_CTE.'CODIGO DIAN'n = IMPORT_HOMOLOGACION_TPO_DOC.'CODIGO DIAN'n ) OR SABANA_CLIENTES_CTE.tipo_doc = 0;`
   - 22715: `WHERE ( t1.DV NOT IS MISSING AND t1.TIPO_DOC = 31 ) OR ( t1.TIPO_DOC NOT = 31 AND t1.DV = 0 );`
   - 22753-22757: nombres con `PRXMATCH('/[^A-Z,a-z, ]/', t1.NOMBRE1) = 0 AND ...`
   - 22795-22798: `WHERE ( ( t1.PAIS = '169' AND LENGTH(t1.DIRECCION) >= 8 AND t2.CODIGO_DANE NOT IS MISSING ) OR ...`
   - 22871-22872: `WHERE t1.VAL_CRED_MES >= 0 OR t1.NRO_CRED_MES >= 0 OR ...`
4. **Intención:** quedarse solo con registros con identificación, ubicación y montos válidos para el reporte regulatorio. Los rechazados se reportan por tipo de incidencia.
5. **Clasificación:** validación y reconciliación (lógica de datos).
6. **Diseño Talend mínimo:**
   - Un job parametrizado por población (`context.poblacion` con valores AHO, CTE, NEQUI; `tiene_FA` como booleano).
   - Flujo: `tImpalaInput` con el SQL de lectura (joins de catálogo si son baratos, es decir, ELT) y después `tMap`.
   - Dentro del `tMap`: lookups de homologación, DANE y PAÍS (Load Once). Las reglas van como expresiones Java booleanas con nombre: DV, regex de nombres con `Pattern`, longitud, `contains` sobre lista de frases prohibidas, rangos de cuenta y GMF, y monetarios.
   - Dos salidas: válidos y rechazados. El rechazado lleva una columna `motivo` calculada, no constante.
   - `tAggregateRow` para contadores por motivo.
   - Cada "Validar X" del SAS es una expresión, no un componente. `tFilterRow` solo si la regla no necesita lookup.
   - Un solo `tMap` por población, con 3 lookups.
7. **Detección:**
   - Léxica: secuencia de `PROC SQL` donde cada `FROM` es la tabla creada en el paso anterior.
   - AST: cadena lineal de nodos `CREATE ... AS SELECT ... FROM previo ... WHERE`.
   - IR: agrupar la cadena en un pipeline de validación con reglas combinadas en AND, y colapsar los nodos intermedios que solo alimentan al siguiente.
   - Variantes: `DATA step` con `IF ... THEN DELETE;`, o `WHERE` de PROC SQL.
8. **Riesgos y falsos positivos:**
   - "Validar tipo doc" es un INNER JOIN. Además de filtrar, descarta filas sin catálogo. En `tMap` eso es un lookup con rechazo, con semántica distinta.
   - La condición `OR tipo_doc = 0` dentro del join puede multiplicar filas (ver P08).
   - "Validar monetarios" usa OR. Ver P17.
   - "Identificar diferencias" es un anti-join, no un filtro de regla.
   - El orden de las reglas solo importa para el motivo de rechazo (la primera que falla).

---

### P04. Validación de tipo y número de documento por rangos (una consulta por tipo, luego unión)

1. **Nombre genérico:** validación de identificación por tipo con rangos de valores permitidos.
2. **Firma estructural:** seis `PROC SQL` (uno por tipo: 8, 1, 2, 3, 4, 7). Cada uno hace `CREATE TABLE DOC_INCORRECTOS_TPOn AS SELECT t1.*, ('NID INCORRECTO') AS INCONSISTENCIAS FROM base t1 WHERE tipo = n AND nro NOT BETWEEN a AND b`. Después un `OUTER UNION CORR` de los seis.
3. **Frecuencia y ejemplos:** 12 consultas (6 en CTE, 6 en NEQUI) más 2 uniones.
   - 19283: `WHERE t1.TIPO_DOC = 8 AND t1.NRO_DOC NOT BETWEEN 50000000000 AND 59999999999;`
   - 19322: `WHERE ( t1.TIPO_DOC = 1 AND t1.NRO_DOC BETWEEN 100000000 AND 999999999);`
   - 19400: `WHERE t1.TIPO_DOC = 3 AND t1.NRO_DOC NOT BETWEEN 600000000 AND 999999999;`
   - 19439-19442: tipo 4 con cuatro condiciones `( t1.TIPO_DOC = 4 AND t1.NRO_DOC NOT BETWEEN ... ) AND ( ... )`.
   - 21923: mismo `BETWEEN` del tipo 1 en la población NEQUI.
4. **Intención:** detectar identificaciones con formato imposible para su tipo.
5. **Clasificación:** validación.
6. **Diseño Talend mínimo:**
   - Una tabla de reglas `tipo, minimo, maximo, modo` (`tFileInputDelimited` o tabla de Impala).
   - En el `tMap` de P03, un lookup por `tipo_doc` que aplica el rango. El tipo 4, con varios rangos, son varias filas de la tabla de reglas.
   - Sustituye 12 consultas y 2 uniones por una expresión. No hace falta leer la base otra vez.
7. **Detección:**
   - Léxica: `WHERE TIPO_DOC = n AND NRO_DOC ... BETWEEN` repetido con `n` distinto.
   - Resolución: asignar cada consulta a su tipo.
   - IR: tabla de reglas tipo → rangos.
   - Variante: `DATA step` con `if tipo = n and not (x between a and b) then ...`.
8. **Riesgos y falsos positivos:**
   - **Probable inversión lógica.** La regla del tipo 1 usa `BETWEEN` (positivo) en las líneas 19322 y 21923, mientras las demás usan `NOT BETWEEN`. Con esa lectura, un documento válido se marcaría como incorrecto. Verificar con datos antes de migrar.
   - El tipo 4 usa cuatro `NOT BETWEEN` unidos con AND. Eso significa "fuera de todos los rangos", que es correcto solo si los rangos no se solapan. Conservar esa semántica en la tabla de reglas.
   - El tipo 2 solo tiene límite inferior (`> 99999999`).

---

### P05. Normalización condicional de nombres y razón social según tipo de documento

1. **Nombre genérico:** sustitución por placeholder o vaciado de campos, según tipo de documento y rango de número.
2. **Firma estructural:** `CASE` anidados por columna. Si tipo distinto de 3 y campo nulo, `'SN'`. Si tipo 3 con número en un rango y campo no nulo, `''`. Si tipo 3 con número en otro rango y campo nulo, `'SN'`. En otro caso, el valor original. Razón social invierte la lógica.
3. **Frecuencia y ejemplos:** 3 bloques de unos 100 líneas (AHO, CTE, NEQUI).
   - 17859-17861: `(CASE WHEN((t1.TIPO_DOC ^= 3) AND(t1.APELLIDO1 IS MISSING)) THEN 'SN'`
   - 17870: `WHEN((t1.TIPO_DOC = 3) AND (NRO_DOC < 799999999) AND (NRO_DOC > 1000000000) AND( t1.APELLIDO1 IS MISSING))`
   - 21032-21034 y 22197-22199: mismo bloque en CTE y NEQUI.
4. **Intención:** cumplir el formato del reporte para personas jurídicas y naturales, con placeholder cuando falta el nombre.
5. **Clasificación:** lógica de datos (limpieza y normalización).
6. **Diseño Talend mínimo:**
   - En el mismo `tMap` de P03, una expresión ternaria por columna.
   - El valor `"SN"` y los rangos NID van a contexto, no literales.
   - Sin componente adicional.
7. **Detección:**
   - AST: `CASE WHEN` con condiciones sobre `tipo_doc` y rangos sobre `nro_doc`, con `AS <misma columna>`.
   - IR: mapeo columna → expresión, reutilizable.
8. **Riesgos y falsos positivos:**
   - **Rama muerta.** La condición `NRO_DOC < 799999999 AND NRO_DOC > 1000000000` es siempre falsa, porque ningún número cumple ambas. Aparece en las líneas 17870, 17897, 21043, 21070, 22208 y 22236. No se debe migrar como lógica viva. Confirmar cuál era la intención.
   - `NRO_DOC` se usa sin calificar (sin alias). Funciona, pero hay que resolverlo en el parser.

---

### P06. Imputación de valores por defecto en ubicación (dirección, departamento, municipio, país)

1. **Nombre genérico:** sustitución de ubicación inválida por valores de defecto.
2. **Firma estructural:** `CASE WHEN (predicado de inválido) THEN constante ELSE col END` para cuatro columnas, con el mismo predicado repetido. El predicado combina: DANE nulo con país `'169'`, país no catalogado, dirección de menos de 8 caracteres, texto `'recla'`, `'info'`, `'sin dir'` o `'sin info'`, y dirección vacía.
3. **Frecuencia y ejemplos:** 3 bloques.
   - AHO, en Impala: 19036 `((t2.CODIGO_DANE IS NULL) AND (t1.PAIS='169'))`; 19039 `OR (UPPER(t1.DIRECCION) LIKE ('recla'))`; 19044 `THEN 'Cra 48 26 85 Av Industriales'`; 19058 `THEN '05'`; 19080 `THEN '001'`; 19101 `ELSE t1.PAIS`.
   - CTE, en Impala: 21540-21545 con el mismo predicado.
   - NEQUI, en SAS: 22389-22401 con `CONTAINS` en lugar de `LIKE`.
   - Línea 22394: `OR (UPPER(t1.DIRECCION) CONTAINS UPPER('recla'))`.
4. **Intención:** no dejar ubicación vacía o errónea en el reporte. Se asigna una dirección genérica y una ubicación por defecto.
5. **Clasificación:** lógica de datos (imputación).
6. **Diseño Talend mínimo:**
   - Una variable booleana `invalidaUbicacion` en el `tMap`, reutilizada en las cuatro columnas.
   - Las constantes (dirección genérica, departamento `'05'`, municipio `'001'`, país `'169'`) van a contexto.
   - Lookups DANE y PAÍS en el mismo `tMap`.
   - Si la base es el origen y el volumen lo exige, el mismo SQL puede ir como `tImpalaInput` (ELT).
7. **Detección:**
   - AST: el mismo predicado repetido en varias columnas, con constantes literales en `THEN`.
   - IR: imputación con lista de defaults.
8. **Riesgos y falsos positivos:**
   - **Semántica distinta entre motores.** En la versión Impala, `LIKE ('recla')` no tiene comodines, así que es igualdad exacta. En la versión SAS, `CONTAINS` busca subcadena. No son equivalentes (líneas 19039-19041 frente a 22394-22396).
   - Las listas de frases no coinciden entre versiones: la versión Impala busca `'sin info'` (19040, 19054) y la versión SAS no siempre la incluye.
   - Un registro imputado ya no es inválido en las validaciones posteriores. Hay dos ramas, una antes y otra después de la imputación (ver P07). No unificarlas sin revisar.
   - En Impala, `''` no es `NULL`. En SAS, un carácter vacío sí es missing. Hay que tratarlo al migrar.

---

### P07. Validación de ubicación contra catálogos (DANE y PAÍS) y reglas de texto

1. **Nombre genérico:** registro de ubicación inválida mediante anti-filtro con catálogos.
2. **Firma estructural:** `SELECT DISTINCT ... FROM base t1 LEFT JOIN catálogo_DANE t2 ON (...) LEFT JOIN catálogo_PAIS t3 ON (...) WHERE (DANE nulo AND pais='169') OR (código de ubicación presente AND pais distinto de '169' AND pais catalogado) OR pais no catalogado OR LENGTH(dirección) < 8 OR CONTAINS(...)`.
3. **Frecuencia y ejemplos:** 3 bloques "Reg ubicacion invalida" (18007, 21479, 22332) y 3 bloques "Validar ubicacion" (22760, 23383, 23709).
   - 18042-18043: `LEFT JOIN WORK.IMPORT_CODIGOS_DANE t2 ON (t1.CODIGO_UBICACION = t2.CODIGO_DANE)`
   - 18044-18047: `WHERE ( t2.CODIGO_DANE IS MISSING AND t1.PAIS = '169' ) OR ... OR LENGTH(t1.DIRECCION) < 8 OR UPPER(t1.DIRECCION) CONTAINS UPPER('recla') OR ...`
   - 22795-22798: `WHERE ( ( t1.PAIS = '169' AND LENGTH(t1.DIRECCION) >= 8 AND t2.CODIGO_DANE NOT IS MISSING ) OR ...`
4. **Intención:** marcar registros con código DANE, país o dirección no válidos.
5. **Clasificación:** validación y reconciliación.
6. **Diseño Talend mínimo:**
   - Lookups DANE y PAÍS en un `tMap` (Load Once, modelo de coincidencia única).
   - La condición de error es un booleano. Va como parte de la cadena de P03, no como flujo aparte.
   - El motivo sale de la condición, no es constante.
7. **Detección:**
   - AST: `LEFT JOIN` a catálogo más `IS MISSING` en el `WHERE` equivale a "no encontrado en catálogo".
   - `CONTAINS UPPER(...)` con lista de cadenas es una lista de términos prohibidos.
   - `LENGTH(...) < 8` es una longitud mínima.
   - IR: regla de catálogo con tabla y clave.
8. **Riesgos y falsos positivos:**
   - En SAS, un carácter vacío es missing, y `LENGTH(missing) = 0`. En Impala, `''` no es nulo. El predicado `< 8` sobre una dirección vacía tiene resultado distinto según el motor.
   - Algunos catálogos se unen en la rama Impala con `t3.CODIGO_PAIS` y en la SAS con `t3.'Codigo_Pais'n`. Es el mismo catálogo con distinto nombre de columna. Verificar que el catálogo sea el mismo.

---

### P08. Homologación por tabla de equivalencias (código interno a código DIAN)

1. **Nombre genérico:** traducción de código mediante catálogo (lookup de código).
2. **Firma estructural:** `INNER JOIN catálogo ON (tipo_doc = clave)` y `CASE WHEN tipo_doc = 0 AND LENGTH(CATS(nro_doc)) = 10 THEN 0 ELSE catálogo.CODIGO_DIAN END`.
3. **Frecuencia y ejemplos:** 3 bloques "Homologar tpo doc" (19129, 21648, 22493).
   - 19141-19146: `CASE WHEN SABANA_CORREGIR_UBICACION_AHO.tipo_doc = 0 AND LENGTH(CATS(...nro_doc)) = 10 THEN 0 ELSE IMPORT_HOMOLOGACION_TPO_DOC.'CODIGO DIAN'n END`.
   - 19176-19179: `INNER JOIN WORK.IMPORT_HOMOLOGACION_TPO_DOC ... ON ( SABANA_CORREGIR_UBICACION_AHO.tipo_doc = IMPORT_HOMOLOGACION_TPO_DOC.CNAME ) ;`
   - 23605-23608: `ON ( SABANA_CLIENTES_AHO.CODIGO_DIAN = IMPORT_HOMOLOGACION_TPO_DOC.'CODIGO DIAN'n ) OR SABANA_CLIENTES_AHO.tipo_doc = 0;`
4. **Intención:** convertir el tipo de documento interno al código de la DIAN.
5. **Clasificación:** lógica de datos (catalogación).
6. **Diseño Talend mínimo:**
   - Lookup en el `tMap` de P03, con `Return only one row` si el catálogo puede tener duplicados.
   - Expresión: `row.tipo == 0 && String.valueOf(row.nro).length() == 10 ? 0 : lookup.codigo_dian`.
   - Las filas sin coincidencia van a la salida de rechazo con motivo "sin homologar".
7. **Detección:** `JOIN` a tabla con prefijo `HOMOLOGACION`/`IMPORT_HOMOLOGACION` y `CASE` con 0 y longitud 10.
8. **Riesgos y falsos positivos:**
   - **Join por campo posiblemente equivocado.** La línea 19179 une por `CNAME`, que parece columna de nombre y no de código. Verificar.
   - **Join con OR.** Las líneas 23605-23608 unen con `CODIGO_DIAN = ... OR tipo_doc = 0`. Para las filas con tipo 0, la condición es verdadera para todas las filas del catálogo: se genera producto cartesiano. El `DISTINCT` del paso puede ocultarlo, pero no siempre. Es un riesgo de duplicación real.

---

### P09. Limpieza de caracteres especiales con copia de vuelta (temporal, reemplazo y borrado)

1. **Nombre genérico:** normalización de texto con transliteración y regex, con copia de vuelta.
2. **Firma estructural:** `data work.temporal; set X; Y = PRXCHANGE('s/[^A-Z, a-z,0-9, ]//', -1, KTRANSLATE(Y, 'NnAaEeIiOoUuUu ', 'ÑñÁáÉéÍíÓóÚúÜü-')); run; data X; set work.temporal; run; proc delete data=work.temporal; run;`
3. **Frecuencia y ejemplos:** 3 bloques "Eliminar caracter especial".
   - 17822-17823: `DIRECCION_SIN_ESP=PRXCHANGE('s/[^A-Z, a-z,0-9, ]//', -1, KTRANSLATE(DIRECCION,`
   - 17826-17831: `data WORK.SABANA_SIN_DOC_INCORRECTOS_AHO; set work.temporal; run; proc delete data=work.temporal; run;`
   - 20995-20996 y 22160-22161: mismo código en CTE y NEQUI.
4. **Intención:** quitar tildes, ñ y símbolos de la dirección para el fichero regulatorio.
5. **Clasificación:** limpieza de texto (lógica de datos) más fontanería de copia.
6. **Diseño Talend mínimo:**
   - Una expresión en `tMap`, o mejor una rutina de Talend (`normalizarDireccion`) reutilizable.
   - Mapa de transliteración explícito (Ñ a N, á a a, etc.) y `replaceAll` con la clase de caracteres permitida.
   - Sin tabla temporal, sin copia, sin borrado.
7. **Detección:** `PRXCHANGE`, `KTRANSLATE` o regex equivalente, con asignación a la misma variable y el patrón copia-borrado.
8. **Riesgos y falsos positivos:**
   - La clase de caracteres contiene comas y espacios repetidos. La coma sobrevive en la salida; verificar si era intencional.
   - Los caracteres acentuados dependen de la codificación. En SAS con latin1 y en Java con UTF-8, el mismo mapa puede comportarse distinto. Probar con datos reales.
   - Sintaxis regex de SAS (PRX) y de Java no son idénticas en todo.

---

### P10. Conversión de texto a número con copia de vuelta y renombrado

1. **Nombre genérico:** casting por reasignación con variable temporal.
2. **Firma estructural:** `data work.temporal; format X 15.; set T(rename=(X=X_old)); X = input(left(X_old), 15.); drop X_old; run; data T; set work.temporal; run; proc delete data=work.temporal; run;`
3. **Frecuencia y ejemplos:** 2 bloques, sobre `TIPO_DOC` y `NRO_DOC` de `SABANA_FINAL_INFO_NEQUI`.
   - 21786-21790: `data work.temporal; format TIPO_DOC 15.; set WORK.SABANA_FINAL_INFO_NEQUI(rename=TIPO_DOC=TIPO_DOC_old); TIPO_DOC=input(left(TIPO_DOC_old), 15.); drop TIPO_DOC_old;`
   - 21820-21824: mismo patrón con `NRO_DOC`.
4. **Intención:** convertir a numérico después de cargar el texto, para validar y comparar.
5. **Clasificación:** transformación de tipo (lógica de datos) más fontanería de copia.
6. **Diseño Talend mínimo:**
   - El tipo se declara en el esquema de salida del `tMap` (Long). Sin copia.
   - Si el valor no es numérico, `tSchemaComplianceCheck` o un `try/catch` en expresión envía a rechazo.
7. **Detección:** `input(...)` con `rename=` y `drop` del original, más la copia de vuelta.
8. **Riesgos y falsos positivos:**
   - **Diferencia de comportamiento.** `input()` de SAS devuelve missing sin error si el texto no es numérico. `Long.parseLong` en Java lanza excepción y corta el job salvo que se capture. Hay que decidir si el registro se rechaza o se deja vacío.
   - `left()` en SAS quita espacios por la izquierda y no por la derecha. Usar `trim` o `strip` según el caso.

---

### P11. Redondeo y formato de métricas (ROUND por columna más FORMAT BEST32)

1. **Nombre genérico:** redondeo a entero de métricas monetarias y conteos.
2. **Firma estructural:** `DATA X; SET Y; col = ROUND(col); FORMAT col BEST32.; ... RUN;` con doce pares de columnas.
3. **Frecuencia y ejemplos:** 2 bloques, 24 llamadas a `ROUND`.
   - 23103-23104: `FIN_SALDO_CTA=ROUND(FIN_SALDO_CTA); FORMAT FIN_SALDO_CTA BEST32.;`
   - 24110-24111: mismo patrón en AHO.
4. **Intención:** montos y conteos enteros en el reporte.
5. **Clasificación:** formato de salida.
6. **Diseño Talend mínimo:**
   - En el `tMap`: `BigDecimal.setScale(0, RoundingMode.HALF_UP)`.
   - El `FORMAT BEST32` no se modela; se fija con el tipo del esquema (Long o Integer).
   - Sin componente adicional.
7. **Detección:** `ROUND` repetido sobre una lista de columnas numéricas, con `FORMAT` asociado.
8. **Riesgos y falsos positivos:**
   - **Diferencia en negativos.** `ROUND` de SAS redondea la mitad alejándose de cero: `ROUND(-2.5) = -3`. `Math.round` de Java redondea hacia arriba en la mitad: `Math.round(-2.5) = -2`. `RoundingMode.HALF_UP` de Java sí redondea alejándose de cero en los empates, igual que SAS. Usar ese modo.
   - Hay saldos negativos (P16), así que la diferencia es real.

---

### P12. Conciliación de conteos y saldos (COUNT en varias tablas, cruce de una fila y diferencia)

1. **Nombre genérico:** conteo de control y cuadre entre etapas.
2. **Firma estructural:**
   - `CREATE TABLE CUENTA_X AS SELECT COUNT(t.key) AS n FROM X t;`
   - `CREATE TABLE CONCILIACION AS SELECT a.n, b.n, c.n, d.n FROM A a, B b, C c, D d;` sin condición de unión, lo que produce un producto cartesiano de una fila.
   - `DATA ...; CONCILIACION = INICIAL - (FINAL + POR_CORREGIR + FA); RUN;` con copia de vuelta (patrón P09).
3. **Frecuencia y ejemplos:** 6 cálculos `CONCILIACION=`, 20 `COUNT(` y unas 14 etiquetas de conteo.
   - 19192-19194: `SELECT COUNT(SABANA_CLIENTES_AHO.LLAVE_NOMBRE) AS SABANA_FINAL_CLIENTES_AHO FROM WORK.SABANA_CLIENTES_AHO`
   - 19212: `FROM WORK.CUENTA_SABANA_COMPLETA_AHO CUENTA_SABANA_COMPLETA_AHO, WORK.CUENTA_SABANA_FINAL_CLI_AHO ..., WORK.CUENTA_FA_DOC_INCOR_AHO ...;`
   - 19235: `CONCILIACION=REG_SABANA_INICIAL-(REG_SABANA_FINAL+REG_POR_CORREGIR+REG_FA_INCORR);`
   - 23147 y 24095: mismo cálculo en CTE y AHO.
4. **Intención:** verificar que ningún registro se pierde entre la sabana inicial, la final, los pendientes de corrección y los documentos incorrectos.
5. **Clasificación:** reconciliación.
6. **Diseño Talend mínimo:**
   - `tAggregateRow` con operación count y sin agrupar, en cada etapa: entrada, válidos, rechazos.
   - `tMap` con la fórmula de diferencia.
   - Salida a `tFileOutputDelimited` y trazas con `tStatCatcher` o `tFlowMeter`.
   - Si el cuadre debe abortar, `tDie`. El SAS no lo hace: solo lo reporta.
7. **Detección:**
   - Léxica: `COUNT(` en `CREATE TABLE` sin `GROUP BY`, y `FROM` con varias tablas sin condición de unión.
   - IR: nodo de cuadre con operandos (conteos) y fórmula.
8. **Riesgos y falsos positivos:**
   - El cruce cartesiano solo funciona si cada conteo tiene exactamente una fila. Si una tabla queda vacía, el resultado es cero filas y el cuadre desaparece sin aviso.
   - La fórmula cambia por población: CTE resta FA, NEQUI no tiene FA, AHO resta FA pero el orden de los términos varía.
   - `COUNT(col)` no cuenta nulos. Si la columna contada es nula en algún registro, el conteo baja. NEQUI cuenta `NRO_CTA` (línea 22518) y otros cuentan `LLAVE_NOMBRE`.
   - El código no comprueba que la diferencia sea cero.

---

### P13. Consolidación por unión de incidencias (OUTER UNION CORR)

1. **Nombre genérico:** unión de conjuntos con el mismo esquema, por nombre de columna.
2. **Firma estructural:** `CREATE TABLE T AS SELECT * FROM A OUTER UNION CORR SELECT * FROM B [OUTER UNION CORR SELECT * FROM C ...];`
3. **Frecuencia y ejemplos:** 20 usos.
   - 19487-19492: unión de los seis tipos de documento (CTE).
   - 22086-22092: unión equivalente (NEQUI).
   - 23860-23865: `CREATE TABLE WORK.SABANA_CONSOLIDADA_NEQUI_AHO AS SELECT * FROM WORK.FINAL_VALIDAR_MONETARIOS_AHO OUTER UNION CORR SELECT * FROM WORK.FINAL_VALIDAR_MONETARIOS_NEQUI;`
   - 24580-24586: consolidación de documentos incorrectos de las tres poblaciones.
4. **Intención:** juntar incidencias de varios validadores en un único reporte.
5. **Clasificación:** E/S y consolidación.
6. **Diseño Talend mínimo:**
   - `tUnite` con esquema común. Si una rama no tiene alguna columna, un `tMap` previo la rellena con valor por defecto.
   - En la cadena de P03, un único `tUnite` de rechazos con columna `motivo` sustituye a las seis consultas.
7. **Detección:** `OUTER UNION CORR`. Es sintaxis de SAS; `CORR` significa unir por nombre de columna.
8. **Riesgos y falsos positivos:**
   - `OUTER UNION CORR` no elimina duplicados (a diferencia de `UNION`). `tUnite` tampoco. Mantener la semántica.
   - Un esquema estricto en Talend falla si falta una columna. Rellenarla antes.

---

### P14. Partición de resultado por población y semi-join de vuelta por clave

1. **Nombre genérico:** separar cuentas por país y relación, y recuperar todas las filas de esas cuentas.
2. **Firma estructural:** `T1 = SELECT ... FROM S WHERE (pais <> '169' AND relacion = 1000)`. `R_ext = SELECT S.* FROM S INNER JOIN T1 ON S.nro_cta = T1.nro_cta ORDER BY ...`. Igual para la rama nacional con `pais = '169'`.
3. **Frecuencia y ejemplos:** 4 pares de consultas (dos en CTE, dos en AHO) y 5 etiquetas "Titulares".
   - 23169-23173: `WHERE ( ( SABANA_CTE_FINAL.PAIS <> '169' ) AND ( SABANA_CTE_FINAL.relacion = 1000 ) ) ;`
   - 23224-23227: `INNER JOIN WORK.SABANA_TIT_EXT_CTE SABANA_TIT_EXT_CTE ON ( SABANA_CTE_FINAL.nro_cta = SABANA_TIT_EXT_CTE.nro_cta ) ORDER BY NRO_CTA ASC, RELACION ASC;`
   - 24219-24222: `INNER JOIN WORK.SABANA_TIT_EXT_AHO ... ORDER BY 14 ASC, 1 ASC;`
4. **Intención:** listar por separado titulares extranjeros y nacionales, con todas las relaciones de cada cuenta.
5. **Clasificación:** lógica de datos (ruteo).
6. **Diseño Talend mínimo:**
   - `tUniqRow` (o `tAggregateRow` agrupado) sobre `nro_cta` del filtro, para obtener la lista de cuentas.
   - `tMap` con lookup de esa lista sobre la fuente completa.
   - Dos salidas a `tFileOutputDelimited`.
   - No duplicar la base.
7. **Detección:** `INNER JOIN` de una tabla derivada de filtro con la fuente completa, por clave y sin condición adicional, es un semi-join. Se detecta también por `ORDER BY` posicional.
8. **Riesgos y falsos positivos:**
   - **Semántica crítica.** `R_ext` no es un filtro por fila. Trae todas las relaciones de cuentas que son titulares extranjeros, no solo las de `relacion = 1000`. Un `tFilterRow` sobre la fila sería incorrecto.
   - **Divergencia.** La rama CTE extranjera no lleva `DISTINCT` (línea 23205), pero la AHO extranjera sí (24216), y las dos nacionales también (23241 y 24235). Decidir cuál es el comportamiento correcto.
   - **`ORDER BY` posicional** (`14 ASC, 1 ASC`, línea 24222; también línea 17079). Es frágil si cambia el orden de columnas. Resolver por nombre.

---

### P15. Totales por columna y agregación de totales

1. **Nombre genérico:** suma de columnas numéricas por conjunto.
2. **Firma estructural:** `CREATE TABLE TOTAL AS SELECT SUM(a) FORMAT=BEST20. AS A, SUM(b) ... FROM X;` con doce sumas, sin `GROUP BY`.
3. **Frecuencia y ejemplos:** 4 bloques.
   - 24615-24620: `CREATE TABLE WORK.TOTAL_EXTERIOR AS SELECT SUM(RESULTADO_AHO_EXT.FIN_SALDO_CTA) FORMAT=BEST20. AS FIN_SAL_CTA, ...`
   - 24635-24639: total nacional.
   - 24691-24696: total corriente.
   - 24748-24752: total de ahorros.
4. **Intención:** totales de control para el reporte.
5. **Clasificación:** reporte.
6. **Diseño Talend mínimo:**
   - `tAggregateRow` con operación `sum` por columna, agrupado por una columna de etiqueta (ahorro, corriente, exterior, nacional).
   - `tUnite` para juntar.
   - Uno o dos componentes.
7. **Detección:** `SUM(...)` repetido sobre una lista de columnas, sin `GROUP BY`, con `FORMAT=BEST20`.
8. **Riesgos y falsos positivos:**
   - `SUM` en SAS ignora missing. En Talend, `sum` sobre un valor nulo puede dar nulo o fallar según el tipo. Usar valor por defecto antes de agregar.
   - Para montos, `BigDecimal` en lugar de `double`.

---

### P16. Detección de saldos o créditos negativos (filtro de incidencias por signo)

1. **Nombre genérico:** filtro de valores negativos.
2. **Firma estructural:** `CREATE TABLE SOB_X AS SELECT cols FROM X WHERE (saldo < 0) OR (credito < 0);`
3. **Frecuencia y ejemplos:** 2 bloques (24655-24670 y 24729-24744). Además hay exportaciones de "campos negativos" (24314-24329, 24467-24482).
   - 24666-24669: `WHERE ( ( AHORROS.fin_saldo_cta < 0 ) OR ( AHORROS.val_cred_mes < 0 ) ) ;`
4. **Intención:** revisar saldos negativos que no deberían reportarse.
5. **Clasificación:** validación y reporte.
6. **Diseño Talend mínimo:**
   - `tFilterRow` con la condición `fin_saldo_cta < 0 || val_cred_mes < 0`.
   - O una salida del `tMap` de P03.
7. **Detección:** `WHERE` con `< 0` sobre columnas numéricas del mismo esquema, repetido en varios `SOB_*`.
8. **Riesgos y falsos positivos:** el `OR` significa que basta un campo negativo para que el registro sea incidencia. Confirmar esa intención.

---

### P17. Validación monetaria con disyunción de no negatividad

1. **Nombre genérico:** "al menos un monto no negativo".
2. **Firma estructural:** `WHERE a >= 0 OR b >= 0 OR c >= 0 ...` sobre siete columnas de montos.
3. **Frecuencia y ejemplos:** 3 bloques "Validar monetarios".
   - 22871-22872: `WHERE t1.VAL_CRED_MES >= 0 OR t1.NRO_CRED_MES >= 0 OR t1.PROM_CRED_MES >= 0 OR ...`
   - 23494-23495 y 23838-23839: mismo patrón en NEQUI y AHO.
4. **Intención (presumida):** los montos deben ser no negativos.
5. **Clasificación:** validación.
6. **Diseño Talend mínimo:** no migrar el `OR` sin confirmación. Si la intención es que todos los montos sean no negativos, es un `AND`.
7. **Detección:** `WHERE` con varias comparaciones del mismo operador sobre columnas de montos unidas con `OR`. Cruzar con la etiqueta "Validar monetarios".
8. **Riesgos y falsos positivos:**
   - **Conflicto con P16.** P16 marca como incidencia cualquier registro con un negativo. P17 acepta cualquier registro con al menos un no negativo. Un registro con saldo negativo y crédito cero pasa la validación de P17 y sale como incidencia en P16.
   - No es un patrón para generalizar. Es una regla dudosa que hay que confirmar con negocio.

---

### P18. Pass-through SQL a Impala (ELT) con CASE, CTE y JOIN

1. **Nombre genérico:** transformación empujada a la base de datos.
2. **Firma estructural:** `proc sql; connect to impala (DSN=...); create table WORK.X as select * from connection to impala (SELECT ... CASE ... LEFT JOIN catalogo ... ORDER BY ...); disconnect from impala; quit;`
3. **Frecuencia y ejemplos:** 49 `connect to impala` y 79 usos de `connection to`, `execute` o `execute by`. Transformaciones reales en Impala: 19016-19126 (AHO) y 21522-21632 (CTE). Cuatro placeholders vacíos (17045 y similares).
   - 19019-19021: `connect to IMPALA (DSN = IMPALAP); create table WORK.SABANA_CORREGIR_UBICACION_AHO as select * from connection to IMPALA`
   - 19118-19120: `FROM proceso_vspc_finanzas.SABANA_CORR_NOM_AHO t1 LEFT JOIN proceso_vspc_finanzas.FORMATO_CODIGO_DANE t2 ON (...)`
   - 17009-17013: `connect to impala (dsn=IMPALAP); select count(*) into :existe from connection to impala (SHOW TABLES IN ... LIKE 'doc_incor_fa_aho');`
4. **Intención:** aplicar reglas de ubicación cerca de los datos.
5. **Clasificación:** E/S (fuente SQL) y ELT.
6. **Diseño Talend mínimo:**
   - `tImpalaConnection` más `tImpalaInput` con la consulta. Si la lógica es SQL puro (CASE, LEFT JOIN a catálogo), se queda en el SQL.
   - Si hay lógica Java, `tImpalaInput` alimenta un `tMap`.
   - Para salida, `tImpalaOutput`.
7. **Detección:** `connection to <motor>`, `execute (...) by <motor>`, `DSN=...`, y dialecto específico (`LIKE`, `CAST(... AS VARCHAR(200))`, `ORDER BY`).
8. **Riesgos y falsos positivos:**
   - **DSN fijo en producción.** Varias conexiones usan `dsn=IMPALAP` literal (por ejemplo, 17009, 17023, 19019, 21525), en lugar de `&lz_DSN`. Eso ignora la macro de entorno (`%ambiente`, D, C o P). En desarrollo o certificación, el código escribe en producción. Es el hallazgo más importante de este tramo.
   - **Placeholders vacíos.** La rama Impala de obtener sin incorrectos tiene solo un comentario (17045, 17782, 20219, 20956). Si se activa, la consulta es inválida.
   - **Esquema fijo** `proceso_vspc_finanzas` en código, no en contexto.
   - **LIKE sin comodines** (ver P06).

---

### P19. Verificación de existencia de tabla y bifurcación por fuente (Impala o WORK)

1. **Nombre genérico:** fallback de fuente según existencia.
2. **Firma estructural:** `select count(*) into :existe from connection to impala (SHOW TABLES IN esquema LIKE 'nombre'); %let fuente = ...; %if &fuente = impala %then %do; proc sql; create table ... select * from connection to impala(...); %end; %else %do; proc sql; create table ... from WORK.X ...; %end;`
3. **Frecuencia y ejemplos:** 4 bloques, 8 usos de `SHOW TABLES`.
   - 17012: `SHOW TABLES IN proceso_vspc_finanzas LIKE 'doc_incor_fa_aho'`
   - 17029-17036: `%if &existe > 0 %then %do; %let fuente = impala; ... %else %do; %let fuente = sas;`
   - 17045: `/* Aquí va tu lógica con CTE y JOIN en LZ */` (placeholder).
   - 17766-17773: el mismo bloque con `INCONS_INCORREC_TIT`.
4. **Intención:** usar la tabla de Impala si ya existe; si no, la de WORK.
5. **Clasificación:** orquestación (decisión en tiempo de ejecución) más fontanería.
6. **Diseño Talend mínimo:**
   - Elegir una fuente de forma fija, sin bifurcación.
   - Si la bifurcación es real: un `tImpalaRow` con `SHOW TABLES` y un subjob condicionado con `tRunJob` por disparador `If`.
   - Dos o tres componentes.
7. **Detección:** `SHOW TABLES` seguido de `%if` sobre una macro variable que elige la fuente.
8. **Riesgos y falsos positivos:**
   - **Rama no implementada.** La rama Impala tiene solo un comentario. Si el flag vale `impala`, la tabla queda vacía o la consulta falla.
   - `into :existe` reutiliza el mismo nombre de macro en varios bloques. Riesgo de confusión.

---

### P20. Limpieza de temporales (DROP TABLE PURGE en Impala y proc delete en WORK)

1. **Nombre genérico:** limpieza de intermedios al final.
2. **Firma estructural:** `proc sql; connect to impala (DSN=...); execute (drop table if exists esquema.T purge) by impala; ... disconnect from impala; quit;` y `proc delete data=work.T; run;`.
3. **Frecuencia y ejemplos:** 65 `drop table`, 33 `proc delete`. Un bloque de 34 sentencias "Borrar tablas LZ".
   - 22575-22580: `execute (drop table if exists proceso_vspc_finanzas.COLUMNAS_DEPOSITOS purge) by impala;` y cinco más.
   - 22605-22606: `execute (drop table if exists proceso_vspc_finanzas.MCDQ purge) by impala;`
4. **Intención:** no dejar tablas intermedias en la zona de aterrizaje.
5. **Clasificación:** fontanería.
6. **Diseño Talend mínimo:**
   - Si el diseño no crea intermedios, no hay nada que borrar (cero componentes).
   - Si hace falta limpiar staging, un `tImpalaRow` que itere la lista de nombres con `tFlowToIterate`.
7. **Detección:** `drop table if exists ... purge` y `proc delete` repetidos sobre una lista.
8. **Riesgos y falsos positivos:**
   - `PURGE` es irreversible.
   - El bloque "Borrar tablas LZ" no tiene condición de éxito. Si el proceso falla a medias, puede borrar tablas que el reporte necesita.

---

### P21. Fontanería y trazas del generador (SAS Studio)

1. **Nombre genérico:** envoltorio de SAS Studio, cabeceras, medición de tiempos y metadatos.
2. **Firma estructural:**
   - Bloque de comentario "Código de la tarea generado por SAS Studio ..." con usuario, servidor, navegador y versión.
   - `%web_drop_table(WORK.X);` ... `%web_open_table(WORK.X);`
   - `TITLE`, `FOOTNOTE`, `FOOTNOTE1 "Generated by ..."`, `options symbolgen nomlogic nomprint source;`
   - `%macro tiempos` con `%put INICIO` y `%put FINAL` (fecha con `datetime()`).
   - `/* Etiqueta: ... */` antes de cada paso.
3. **Frecuencia y ejemplos:** 22 cabeceras, 50 `%web_drop_table` y 50 `%web_open_table`, 12 `%tiempos`, 157 etiquetas.
   - 16680-16681: `%web_drop_table(WORK.CUENTA_FA_DOC_INCOR_AHO);`
   - 16997-17003: `%macro tiempos; options nosymbolgen nosource nosource2; %put INICIO: &hi. ; %put FINAL : ...; %mend tiempos;`
   - 17121: `* Código de la tarea generado por SAS Studio 3.8`
4. **Intención:** integración con el visor de SAS Studio y medición de tiempos. No tiene lógica de datos.
5. **Clasificación:** fontanería y trazas/medición.
6. **Diseño Talend mínimo:**
   - Descarte total.
   - Las trazas pasan a `tStatCatcher` o `tFlowMeter`. Los `%put` se reemplazan por `tLogRow` si hace falta.
   - Las etiquetas `/* Etiqueta: X */` se usan como nombres de subjob o de componente, sin copiar el texto.
7. **Detección:** comentario "Código de la tarea generado", `%web_*`, `TITLE`/`FOOTNOTE`, `%put` de tiempos.
8. **Riesgos y falsos positivos:** las cabeceras contienen datos personales (usuario y servidores). No portarlas.

---

### P22. Selección de entorno por macro (D, C, P) e include de configuración

1. **Nombre genérico:** parametrización de entorno mediante macro y fichero incluido.
2. **Firma estructural:** `%include "/data/Programas_SAS/activenodelzcode.sas";` seguido de `%macro ambiente; %if &m_ambiente eq D %then %do; %let lz_dsn=IMPALA; %end; %else %if &m_ambiente eq C %then ... IMPALAC ...; %else %if &m_ambiente eq P %then ... IMPALAP ...; %mend;`
3. **Frecuencia y ejemplos:** 11 bloques con `%macro ambiente`, uno por bloque "Escritura".
   - 16717-16724: `%macro ambiente; %if &m_ambiente eq D %then %do; %let lz_dsn=IMPALA; %end;`
   - 16730-16734: rama P, `%let lz_dsn=IMPALAP;`
   - 16714: `%include "/data/Programas_SAS/activenodelzcode.sas";`
4. **Intención:** cambiar de entorno sin tocar el código.
5. **Clasificación:** parametrización y entorno.
6. **Diseño Talend mínimo:**
   - Un grupo de contexto por entorno (DEV, CERT, PROD) con DSN, rutas y credenciales.
   - Sin `%include`.
   - El job se lanza con el contexto adecuado.
7. **Detección:** `%macro` con `%if` sobre una letra de entorno y `%let` de DSN; `%include` de fichero de configuración.
8. **Riesgos y falsos positivos:**
   - **Bypass del entorno.** Como se indica en P18, la macro existe, pero varias conexiones usan `IMPALAP` directamente. La macro no protege.
   - El fichero incluido queda fuera del tramo; no se puede verificar su contenido.

---

## Riesgos transversales a revisar antes de migrar

1. **DSN fijo** (P18, P22): conexiones literales a producción en lugar de `&lz_DSN`.
2. **Credenciales en el código** (P02): `pass="&SASPC_PW"` en 22 sesiones. Tratar como secreto.
3. **Inversión probable en validación de tipo 1** (P04): `BETWEEN` donde las demás usan `NOT BETWEEN` (líneas 19322 y 21923).
4. **Rama muerta en normalización de nombres** (P05): `NRO_DOC < 799999999 AND NRO_DOC > 1000000000` es siempre falsa.
5. **LIKE frente a CONTAINS** (P06): mismo intento de búsqueda de palabras con semántica distinta según el motor.
6. **Validación monetaria con OR** (P17) en conflicto con P16.
7. **Semi-join no reproducible como filtro** (P14): `R_ext` trae todas las relaciones de cada cuenta.
8. **Join con OR que puede duplicar** (P08): líneas 23605-23608.
9. **Alias ambiguo en SQL** (P19 y anti-join): en 17791-17794 y 20963-20968 se usan los nombres de tabla donde ya hay alias. Probable error de resolución en SAS. Verificar en el log.
10. **Anti-join con clave distinta**: una versión une por `LLAVE_NOMBRE` y `RELACION` (17051-17058), otra solo por `NRO_CTA` (17789-17794). El resultado depende de cuál se ejecute.
11. **Placeholders vacíos** en ramas Impala (P18 y P19).
12. **`''` frente a `NULL`** entre Impala y SAS (P06, P07).
13. **`ROUND` de SAS frente a `Math.round` de Java** (P11). Usar `HALF_UP` de `BigDecimal`.
14. **Copia de vuelta con borrado de temporal** (P09, P10, P12): patrón que el migrador debe colapsar, no traducir.

---

## (A) Diseño objetivo del tramo en Talend

Pipeline del tramo, en orden:

1. **J1_Carga_Origen** (job genérico, reemplaza P01 y P20). Tres componentes: `tImpalaConnection`, `tImpalaInput`, `tImpalaOutput`. Se llama 11 veces o una vez por tabla con `tFlowToIterate`.
2. **J2_Validacion_Poblacion** (un job, lanzado tres veces con `context.poblacion` = AHO, CTE, NEQUI mediante `tRunJob` en bucle). Reemplaza P03, P04, P05, P06, P07, P08, P10, P13 (parte), P17, y la mayoría de las 21 etiquetas "Validar". Componentes:
   - `tImpalaConnection` (1)
   - `tImpalaInput` con SQL de lectura (1)
   - `tFileInputDelimited` para la tabla de reglas NID (1)
   - `tMap` principal con lookups de homologación, DANE y PAÍS, expresiones de normalización, imputación y validación, y dos salidas (1)
   - `tAggregateRow` para contadores (1)
   - `tUnite` para rechazos con motivo (1)
   - `tFileOutputDelimited` para válidos y rechazados (2)
   - Total aproximado: 9.
3. **J3_Ruteo_Titulares** (reemplaza P14). Componentes: `tUniqRow`, `tMap` con lookup de cuentas, dos `tFileOutputDelimited`. Aproximadamente 4 o 5.
4. **J4_Totales_Conciliacion** (reemplaza P12, P15, P16). Componentes: `tAggregateRow` (sumas y conteos, 2 o 3), `tMap` con la fórmula de diferencia, `tFilterRow` para negativos (2), `tUnite` para totales (1), `tFileOutputDelimited` (2). Aproximadamente 9.
5. **Orquestador** (reemplaza las llamadas en secuencia y P19). `tRunJob` en bucle sobre poblaciones, y `tRunJob` secuencial para J1, J2, J3, J4 con disparador `OnSubjobOk`. Aproximadamente 2 o 3.

Conteo esperado: **4 jobs más un orquestador, unos 28 componentes**. No hay joblets obligatorios. Un joblet opcional `JL_NormalizarDireccion` si la rutina no basta.

Comparación con el SAS del tramo: unos **316 pasos** (179 `PROC SQL`, 104 `DATA step`, 22 exportaciones y 11 cargas). Los 22 pares de exportación y subida se convierten en salidas directas a la ruta de red; la fontanería (cabeceras, `%web_*`, `%put`, `signon`, `RSUBMIT`, `ps`) queda en cero componentes.

---

## (B) Tabla patrón, capa de implementación y prioridad

Capas: lexer (L), parser (P), resolución de macros (M), IR, traductor (T), planificador (PL).

Prioridad: 1 = alta (imprescindible o descarte inmediato), 2 = media, 3 = baja.

| Patrón | Capa(s) | Frecuencia | Impacto | Prio. |
|---|---|---|---|---|
| P03 Cadena de validación | IR (pipeline de reglas), PL (fusión de nodos), T (tMap con rechazo) | 21 etiquetas, 3 cadenas | Muy alto | 1 |
| P18 Pass-through Impala y DSN | P (`connection to`), M (resolver DSN), T (tImpalaInput) | 49 connect, 79 pass-through | Muy alto (ELT y entorno) | 1 |
| P01 Carga por particiones | L (macros), M (expandir `%syslput`), IR (nodo de fontanería), T (origen a destino) | 11 bloques, ~42% del tramo | Alto | 1 (descarte) |
| P02 Export y subida | P (par export-upload), IR (destino), PL (salidas parametrizadas) | 22 pares | Alto | 1 |
| P21 Fontanería y trazas | L y P (descarte de cabeceras, `%web_*`, `%put`) | 50+50, 22, 12, 157 | Medio (ruido) | 1 (descarte) |
| P20 Limpieza de temporales | PL (eliminar), T (tImpalaRow iterado) | 65 drop, 33 delete | Bajo | 1 (descarte) |
| P12 Conciliación de conteos | IR (nodo de cuadre), T (tAggregateRow + tMap) | 6 cálculos, 20 COUNT | Alto (control) | 2 |
| P04 Validación por tipo y rango | IR (tabla de reglas), T (lookup) | 12 consultas + 2 uniones | Alto (riesgo BETWEEN) | 2 |
| P07 Ubicación contra catálogo | IR (lookup), T (lookup en tMap) | 6 bloques | Alto | 2 |
| P06 Imputación de ubicación | IR (defaults en contexto), T, detector de LIKE frente a CONTAINS | 3 bloques | Alto (divergencia de motor) | 2 |
| P05 Normalización de nombres | P (CASE por columna), IR (mapeo columna a expresión), T (ternario) | 3 bloques | Medio-alto (rama muerta) | 2 |
| P13 OUTER UNION CORR | T (tUnite) | 20 usos | Bajo-medio, pero volumen alto | 2 |
| P09 Limpieza de texto con copia | PL (detectar copia-borrado), T (rutina o expresión) | 3 bloques | Medio | 2 |
| P10 Casting con copia | PL (copia-borrado), T (tipos en esquema) | 2 bloques | Medio | 2 |
| P14 Partición y semi-join | IR (semi-join explícito), PL | 4 pares | Alto (semántica) | 2 |
| P08 Homologación | IR (lookup), T (lookup en tMap) | 3 bloques | Medio (join con OR) | 2 |
| P17 Monetarios con OR | Validación (marcar, no traducir sin confirmar) | 3 bloques | Alto (conflicto con P16) | 2 (marcar) |
| P11 ROUND y FORMAT | T (BigDecimal HALF_UP) | 2 bloques, 24 ROUND | Medio (diferencias de redondeo) | 3 |
| P19 Fallback por existencia | PL (rama), IR | 4 bloques | Medio (rama vacía) | 3 |
| P16 Negativos | T (tFilterRow) | 2 bloques | Bajo | 3 |
| P15 Sumas | T (tAggregateRow) | 4 bloques | Bajo | 3 |
| P22 Entorno por macro | M (`%ambiente`, `%include`), T (contexto por entorno) | 11 bloques | Alto (riesgo de producción) | 1 |

Orden sugerido de implementación: primero las reglas de descarte (P01, P20, P21, P22 como contexto), después la cadena de validación (P03) con sus lookups (P04, P05, P06, P07, P08), luego el pass-through (P18) con el DSN resuelto por contexto, y por último la conciliación y los totales (P12, P13, P14, P15, P16).

---

## Conclusiones principales

1. **El tramo es mayoritariamente fontanería y repetición.** Once bloques de carga idénticos ocupan unas 3.440 de 8.201 líneas. Los 22 pares de exportación y subida son el mismo patrón con otro nombre. En Talend se reducen a un job genérico y a salidas directas a ruta de red, sin componentes de fontanería.
2. **Las tres poblaciones son el mismo pipeline con sufijo distinto.** AHO, CTE y NEQUI tienen la misma cadena de validación, normalización e imputación. Se migran como un job con `context.poblacion` y un solo `tMap` por población, no como tres copias. Hay diferencias reales entre ellas (NEQUI no tiene FA, la fórmula de conciliación cambia) que deben quedar en contexto y no como copias divergentes.
3. **La cadena de validación fila a fila se colapsa en un `tMap`.** Las 21 etiquetas "Validar" son filtros sucesivos sobre tablas intermedias. Pueden ser una sola pasada con lookups, expresiones con nombre y dos salidas (válidos y rechazados con motivo). El pass-through a Impala se reserva para la lectura inicial y los catálogos, que es el caso ELT idiomático.
4. **Hay reglas que no deben migrarse tal cual.** La validación de tipo 1 parece invertida (BETWEEN frente a NOT BETWEEN). La normalización de nombres tiene una rama siempre falsa. La validación monetaria usa OR en conflicto con P16. El semi-join de titulares no es un filtro por fila. Y el DSN de varias conexiones es fijo en `IMPALAP`, lo que ignora el entorno. Todo esto debe confirmarse con negocio antes de migrar.
5. **El patrón "copia de vuelta con temporal y borrado" aparece 11 veces** (6 conciliaciones, 3 limpiezas de texto, 2 conversiones de tipo), y el migrador debe colapsarlo, no traducirlo. Es el patrón de mayor fricción: parece lógica pero es solo una asignación en sitio. Detectarlo en el planificador y reemplazarlo por una expresión en el `tMap` reduce datasets intermedios y evita falsos positivos.
