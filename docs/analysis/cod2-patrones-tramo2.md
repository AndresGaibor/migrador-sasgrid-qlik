# Cod2.txt, tramo 2 (líneas 8301 a 16600): patrones SAS para migrar a Talend

## 0. Alcance, método y cifras

- Fuente: `C:\Users\USUARIO_BISOLUTION1\Downloads\Cod2.txt`, líneas 8301 a 16600 (8.300 líneas leídas completas en tramos de 500). Los números de línea citados son los del archivo original.
- Conteos: `grep` sobre el tramo extraído. Son exactos salvo donde se indica "aprox.".
- Contenido del tramo: construcción de las "sabanas" de tres productos (AHO, CTE y NEQUI) para reporte regulatorio: filtros de segmento, saneamiento de negativos, conversiones de tipo, enriquecimiento con datos de cliente en Impala, validación de direcciones y documentos, dígito de verificación, conciliación de conteo y saldo, y carga masiva a Impala.
- Lo que NO aparece en este tramo: `PROC IMPORT`, `PROC EXPORT`, lectura de Excel o CSV, `FILENAME`/`INFILE`, y descarga remota (`download`). El único `rsubmit` es el de partición de carga, no de descarga. Los patrones de tipo (g) "lectura de archivos y descarga remota" quedan sin evidencia en este tramo.

| Métrica en el tramo | Valor |
|---|---|
| Bloques "Código de query generado por Common Query Services" (`%web_drop_table` + PROC SQL + `%web_open_table`) | 48 |
| Cabeceras de metadatos de SAS Studio ("Generado el ...") | 91 |
| Etiquetas `/* Etiqueta: ... */` | 163 |
| Pasos de mutación en lugar: `data work.temporal; set X; ...; run; data X; set work.temporal; run; proc delete` | 63 |
| Clamp de negativos a cero `IFN(campo<0, 0, campo)` | 21 (7 campos x 3 productos) |
| Bundles completos de carga a Impala (macros `%split2`, `%create_commands`, `%executeBulkload`, `%waitForBulkLoads`, `%delProcessTables`, etc.) | 12 completos + 1 cortado al final del tramo (13 cabeceras) |
| Líneas de los 12 bundles completos | 3.552 (43 % del tramo) |
| `connection to` (pass-through SQL a Impala con datos de vuelta) | 10 |
| `connect to impala` (incluye DDL de limpieza dentro de los macros) | 48 |
| Cláusulas `WHEN` de validación de dirección | 99 (en 3 bloques: 39, 39 y 21) |
| Cálculos de dígito de verificación (DV) | 3 bloques (AHO, CTE, NEQUI) + 2 sobrescrituras `DV=0` |
| Bloques de validación de tipo de documento | 6 PROC SQL + 1 `OUTER UNION CORR` + 2 particiones |
| `SELECT ... INTO :macro` | 6 (3 pares de fecha AHO/CTE) |

Patrones distintos identificados: **29**.

---

## 1. Filtro de subconjunto por PROC SQL

1. **Nombre genérico:** Filtro de subconjunto por `WHERE` sobre una sola tabla.
2. **Firma estructural:** `PROC SQL; CREATE TABLE X AS SELECT <lista de columnas> FROM Y WHERE <predicado>; QUIT;`. Predicados simples (`TIPO_CTA = 2`), compuestos (`IN (1.0, 3.0, 4.0, 5.0) AND col <> 'CTA NEQUI'`) o con valores de bandera (`VAL_DIR = 'CONSISTENTE   '`). Con `ORDER BY 3 ASC, 1 ASC` (posicional) en algunos bloques de salida.
3. **Frecuencia y ejemplos:** aprox. 15 de los 48 bloques generados son puro filtro. Ejemplos:
   - L8311-8317: `CREATE TABLE WORK.CUMPLE_NORMA_CTE ... WHERE (SABANA_CUMPLE_NORMA.TIPO_CTA = 2);`
   - L8332-8338: `WHERE ( (TIPO_CTA IN (1.0, 3.0, 4.0, 5.0)) AND (CTA_NEQUI <> 'CTA NEQUI') );`
   - L10686-10694: `WHERE (DIRECCION_CONS_AHO.VAL_DIR = 'CONSISTENTE   ');`
4. **Intención:** Separar la población por segmento de producto o por resultado de validación antes del siguiente paso.
5. **Clasificación:** lógica de datos (filtro). El envoltorio `%web_*` que lo rodea es fontanería (ver patrón 2).
6. **Diseño Talend:** Un único `tMap` con filtro por salida (`Output filter`) o un `tFilterRow` si la condición es simple. Si el origen es la misma tabla que otro filtro, usar un `tMap` con varias salidas en lugar de leer el origen varias veces. El `ORDER BY` posicional se sustituye por `tSortRow` solo si la salida lo exige.
7. **Detección:** Bloque `%web_drop_table(X); PROC SQL; CREATE TABLE X AS SELECT ... WHERE ...`. Como señal de parser: `CREATE TABLE` con `FROM` a un solo origen y sin `JOIN`. Variantes en otros motores: `CREATE VIEW`, `WITH` de CTE, `DataFrame.filter`.
8. **Riesgos y falsos positivos:** Los predicados con `NULL` no cumplen `<>` ni `=` a la vez (ver patrón 14). El literal `'CONSISTENTE   '` con espacios funciona en SAS por el relleno de blancos, pero no en Talend si se compara sin trim. Los `ORDER BY` posicionales dependen del orden de columnas.

---

## 2. Fontanería de la interfaz SAS Studio

1. **Nombre genérico:** Envoltorio de la interfaz gráfica del IDE (drop/open de tablas, cabeceras, etiquetas, títulos).
2. **Firma estructural:** `%web_drop_table(WORK.X);` antes del paso y `%web_open_table(WORK.X);` después. Bloques de comentario `/* Etiqueta: ... */`, cabeceras `/* Código de la tarea generado por SAS Studio ... Generado el ... por 'usuario' ... navegador ... */`, y `TITLE`/`FOOTNOTE`/`options symbolgen ...` en los pasos de escritura.
3. **Frecuencia y ejemplos:** 48 pares drop/open, 91 cabeceras, 163 etiquetas, 39 líneas `TITLE`/`FOOTNOTE`. Ejemplos:
   - L8304-8307: `%web_open_table(WORK.CUMPLE_NORMA_NEQUI);` seguido de `/* Etiqueta: Cumple norma corriente */` y `%web_drop_table(WORK.CUMPLE_NORMA_CTE);`
   - L8395-8401: cabecera de tarea con usuario, servidor, plataforma y navegador.
   - L9645-9647: `TITLE "Tarea para la Importacion desde LZ"; FOOTNOTE1 "Generated by the Grupo BANCOLOMBIA (&SYSUSERID, &SYSSCPL) ...";`
4. **Intención:** Ninguna de negocio. Sirve a la herramienta (ver resultados, auditar quién generó el código) y a la trazabilidad informal.
5. **Clasificación:** fontanería (y trazas, en las etiquetas).
6. **Diseño Talend:** Se descarta por completo. Las etiquetas se convierten en nombres de componente (por ejemplo `tMap_Cumple_CTE`) y el `Etiqueta` en la descripción del componente. Los `%web_open_table` no tienen equivalente.
7. **Detección:** Léxico: `%web_drop_table`, `%web_open_table`, `Código de query generado para SAS Studio`, `Generado el '`, `Etiqueta:`, `TITLE`, `FOOTNOTE`. Es el paso más barato de eliminar en el lexer/parser.
8. **Riesgos y falsos positivos:** Las etiquetas a veces indican intención de negocio ("Campo conciliacion saldos", "Filtro direcciones"); conviene conservarlas como descripción. No eliminar comentarios que contengan reglas (por ejemplo `/*Dejar el primero del grupo*/`, L14104).

---

## 3. Mutación en lugar mediante tabla temporal (copia de vuelta y borrado)

1. **Nombre genérico:** Modificación de una columna de una tabla mediante un DATA step intermedio con copia de vuelta y borrado.
2. **Firma estructural:**
   ```
   data work.temporal; set X; COL = <expresión>; run;
   data X; set work.temporal; run;
   proc delete data=work.temporal; run;
   ```
   Es un patrón de 3 pasos y un temporal para una sola asignación. No hay ninguna razón de datos para el temporal: SAS no permite sobrescribir la tabla de entrada en el mismo paso, y el código lo resuelve así en cada caso.
3. **Frecuencia y ejemplos:** 63 ocurrencias en el tramo. Ejemplos:
   - L8576-8587: `data work.temporal; set WORK.SABANA_FINAL_REPORTAR_NEQUI; VAL_CRED_MES=IFN(VAL_CRED_MES<0, 0, VAL_CRED_MES); run;` y después la copia de vuelta.
   - L9063-9073: mismo patrón sobre `SABANA_FINAL_REPORTAR_AHORROS`.
   - L10506-10516: `CACITY=PUT(input(CACITY1,8.),Z8.);` con la misma copia de vuelta.
   - L14308-14318: `TIPO_DOC_FORM=PUT(TIPO_DOC, Z1.);`
4. **Intención:** Ninguna por sí misma. Es el mecanismo para aplicar cualquier transformación de columna en un proceso SAS que no admite actualizar in place.
5. **Clasificación:** fontanería (el DATA step de paso único y la copia), aplicada a lógica de datos (la expresión de la columna).
6. **Diseño Talend:** Cada uno de los 63 pasos se convierte en una columna del `tMap` central, con su expresión Java en el mismo mapeo. No hay intermedios: un solo flujo que va de origen a salida.
7. **Detección:** Como señal de parser/AST: `DATA X; SET Y; <una asignación>; RUN;` seguido de `DATA Y; SET X; RUN;` y `PROC DELETE DATA=X`. Como señal de IR: nodo DATA con un único asignado y su par de copia de vuelta sobre el mismo nombre. Es fácil de detectar por nombre (`work.temporal`) pero conviene la estructura, porque cambia el nombre.
8. **Riesgos y falsos positivos:** Si la expresión lee la columna que se va a escribir, el orden de los pasos cambia el resultado. El temporal con nombre fijo impide la ejecución en paralelo de dos bloques en la misma sesión. Un falso positivo es un DATA de dos pasos legítimo (por ejemplo, `set` de una tabla distinta con `DROP`).

---

## 4. Saneamiento de negativos a cero (clamp)

1. **Nombre genérico:** Reemplazo de valores negativos por cero en un conjunto fijo de columnas.
2. **Firma estructural:** `COL = IFN(COL < 0, 0, COL);` como asignación única dentro de un patrón de mutación (patrón 3). Sobre 7 columnas: `VAL_CRED_MES`, `NRO_CRED_MES`, `PROM_CRED_MES`, `MED_CRED_MES`, `VAL_DEB_MES`, `NRO_DEB_MES`, `PROM_DEB_MES`.
3. **Frecuencia y ejemplos:** 21 clamps (7 columnas x 3 productos). Ejemplos:
   - L8413: `NRO_CRED_MES=IFN(NRO_CRED_MES<0, 0, NRO_CRED_MES);` (producto NEQUI)
   - L8906: `NRO_CRED_MES=IFN(NRO_CRED_MES<0, 0, NRO_CRED_MES);` (producto AHO)
   - L8766: `PROM_CRED_MES=IFN(PROM_CRED_MES<0, 0, PROM_CRED_MES);` (NEQUI)
   - L9125: `PROM_DEB_MES=IFN(PROM_DEB_MES<0, 0, PROM_DEB_MES);`
   Estos clamps van después de que el patrón 6 ("flag de negativos", patrón 15) ha contado los negativos. Eso significa que la cifra de inconsistencias se mide antes del saneamiento.
4. **Intención:** Las columnas de movimientos (créditos y débitos) no admiten negativos en el reporte; los negativos se tratan como cero tras contarse en la incidencia.
5. **Clasificación:** lógica de datos (regla de negocio).
6. **Diseño Talend:** En el `tMap` de la sabana, una expresión por columna: `row1.VAL_CRED_MES < 0 ? 0 : row1.VAL_CRED_MES`. Si los 7 campos se tratan igual, usar una rutina Java `clampCero(BigDecimal)` para no repetir la expresión. El conteo de incidencias se hace en el mismo flujo antes del clamp, con `tAggregateRow`.
7. **Detección:** Léxico: `IFN(<col> < 0, 0, <col>)` o `MAX(<col>, 0)`. Como señal de IR: la misma columna aparece en el conjunto de columnas con clamp en tres tablas de salida distintas.
8. **Riesgos y falsos positivos:** El clamp no está en `FIN_SALDO_CTA`, aunque sí la suma de saldos en la conciliación. Eso puede ser intencional, pero conviene confirmarlo con negocio. Un `IFN` con `missing` no es negativo: `missing < 0` es verdadero en SAS (los missing numéricos son menores que cualquier número), así que el clamp convierte missing en 0. Eso cambia el conteo de no nulos.

---

## 5. Conversión de tipo y formateo con PUT / INPUT y ceros a la izquierda

1. **Nombre genérico:** Conversión numérico a texto con ancho fijo y ceros a la izquierda, o texto a numérico y de vuelta.
2. **Firma estructural:** `PUT(numero, Z<n>.)` para formatear con ceros; `PUT(INPUT(texto, 8.), Z8.)` para el ciclo texto-número-texto; `INPUT(SUBSTR(...,k,1), w1.)` para leer un dígito. La conversión suele estar dentro de un patrón de mutación (patrón 3), y el resultado sustituye a la columna de origen, lo que es un cambio de tipo en lugar.
3. **Frecuencia y ejemplos:** 8 `PUT` con formato Z, 3 `PUT(INPUT(...))`. Ejemplos:
   - L10011: `NRO_DOC_TEXTO=PUT(nro_doc, Z15.);`
   - L12342: `NRO_DOC_TEXTO=PUT(nro_doc, Z15.);` (CTE, con la misma regla)
   - L14371: `NRO_DOC_FORM=PUT(NRO_DOC, Z15.);` (NEQUI)
   - L14310: `TIPO_DOC_FORM=PUT(TIPO_DOC, Z1.);`
   - L10508: `CACITY=PUT(input(CACITY1,8.),Z8.);`
   Nota: en NEQUI, la misma regla de 15 dígitos aparece también como `LPAD(CAST(A.NRO_DOC AS STRING), 15, '0')` dentro del pass-through (L14812), así que hay dos implementaciones de la misma regla en dos motores.
4. **Intención:** Obtener la clave de documento con ancho fijo (15) para cruzar con el dato de cliente, y el código de ubicación con 8 caracteres para el formato del reporte.
5. **Clasificación:** lógica de datos (conversión de tipo).
6. **Diseño Talend:** En el `tMap`: `String.format("%015d", row1.NRO_DOC)` o `StringUtils.leftPad(String.valueOf(row1.NRO_DOC), 15, '0')`. Si la clave ya viene con `LPAD` desde Impala, no repetirla en Talend: elegir un único lugar (preferible el motor, por ELT) y documentarlo en el contrato del `tImpalaInput`.
7. **Detección:** Léxico: `PUT(`, `INPUT(`, formatos `Z\d+\.`, `w\d+\.`, `\d+\.`. Como señal de IR: columna que aparece como salida de `PUT` y como entrada de `INPUT` en el mismo flujo.
8. **Riesgos y falsos positivos:** `INPUT` sobre texto no numérico devuelve missing y el `PUT` posterior falla silenciosamente (produce `.` o 0). En Java, `BigDecimal` pierde ceros a la izquierda si no se formatea. Las dos reglas (SAS y LPAD) deben ser idénticas en longitud y en relleno.

---

## 6. Recodificación de códigos con IFN anidados

1. **Nombre genérico:** Tabla de equivalencias codificada en un `IFN` anidado, con valor por omisión `missing`.
2. **Firma estructural:** `X = IFN(X="CC", 1, IFN(X="CE", 2, IFN(X="TI", 4, .)));`
3. **Frecuencia y ejemplos:** 1 bloque en el tramo (L14340-14341, `TIPO_DOC` de texto a código numérico, sobre `COLUMNAS_BASE_NEQUI`), más el `PUT(TIPO_DOC, Z1.)` del patrón 5 que cumple la misma función en otro punto. El `IFN` anidado aparece 1 vez en el tramo.
4. **Intención:** Traducir el tipo de documento del origen (texto) al código del formulario regulatorio (numérico).
5. **Clasificación:** lógica de datos (recodificación).
6. **Diseño Talend:** Un `tMap` con una tabla de búsqueda (`tFileInputDelimited` con el CSV de códigos, o un `tMap` con `Lookup` a una tabla de referencia). Es más mantenible que una cadena de `IFN` y el valor por omisión se modela como `Lookup` no encontrado (con `Inner join` o `Catch lookup inner join rejects`).
7. **Detección:** `IFN` anidado (más de un `IFN(` dentro de otro `IFN(`), o `IFN`/`IFC` con literales de texto seguidos de números. Como señal de IR: columna de entrada de tipo texto y salida numérica, con el mismo nombre (`TIPO_DOC`).
8. **Riesgos y falsos positivos:** Un cambio de tipo con el mismo nombre (`TIPO_DOC` de texto a numérico) puede romper pasos posteriores que aún esperan texto. En el tramo, `TIPO_DOC` se usa numérico (`TIPO_DOC = 3`) en la validación de NIT (L16109 y siguientes) y como texto (`TIPO_DOC = "3"`) en el DV de NEQUI (L14915). Esa mezcla es un riesgo real.

---

## 7. Valor por defecto para vacíos y columnas constantes

1. **Nombre genérico:** Imputación de un valor por defecto cuando el campo está vacío, y asignación de constantes a columnas nuevas.
2. **Firma estructural:** `X = IFC(X = "", <valor>, X);` o `X = "<constante>";` o `X = <número>;` en un paso propio.
3. **Frecuencia y ejemplos:**
   - Valor por defecto (dirección): L11798 `DIRECCION_VAL=IFC(DIRECCION="", "Cra 48 26 85 Av Industriales", DIRECCION);` (repetido en AHO, CTE y NEQUI: L14129, L15839).
   - Valor por defecto (departamento, municipio, país): L11828 `DEPARTAMENTO=IFC(CACITY="", "05", SUBSTR(CACITY, 1, 2));`; L11858 `MUNICIPIO=IFC(CACITY="", "001", SUBSTR(CACITY, 3, 3));`; L11888 `PAIS=IFC(CACTRY="", "169", CACTRY);`.
   - Constantes: L14401 `RAZON_SOCIAL="";`, L14447 `DIRECCION="Cra 48 26 85 Av Industriales";`, L14790 `DEPARTAMENTO="05";`, L14863 `MUNICIPIO_NUEVO="001";`, L14962 `PAIS="169";`.
   Hay 6 asignaciones constantes y 9 `IFC` de valor por defecto.
4. **Intención:** Completar el formulario regulatorio cuando el dato no existe (dirección, departamento, municipio, país), con valores por defecto acordados (Cra 48 26 85 Av Industriales, departamento 05, municipio 001, país 169). Las constantes en NEQUI sirven para todos los clientes de ese producto, sin ubicación real.
5. **Clasificación:** lógica de datos (regla de negocio / valor por defecto).
6. **Diseño Talend:** Expresiones en el `tMap`: `row1.DIRECCION == null || row1.DIRECCION.isEmpty() ? "Cra 48 26 85 Av Industriales" : row1.DIRECCION`. Las constantes se fijan como expresión de la salida (`"169"`). Los valores por defecto se parametrizan en `context` (un solo punto de cambio), en vez de literales repetidos.
7. **Detección:** `IFC(<col> = "", <literal>, ...)`, asignación de literal a columna nueva, y literales de código de ubicación (cadenas de dígitos). Como señal de IR: un valor literal se asigna a la misma columna en varios productos.
8. **Riesgos y falsos positivos:** Las constantes en NEQUI (`DEPARTAMENTO="05"`, `PAIS="169"`) sustituyen a datos reales sin condición: no es una imputación, es una asignación global. Confirmar con negocio si es intencional. Los valores por defecto están duplicados por producto: si cambia uno, hay que cambiar tres.

---

## 8. Extracción de subcadenas (posiciones fijas y longitudes acumuladas)

1. **Nombre genérico:** Partición de un código o de un nombre en campos mediante subcadenas en posiciones fijas o con longitudes acumuladas.
2. **Firma estructural:**
   - Posiciones fijas: `SUBSTR(CACITY, 1, 2)` (departamento), `SUBSTR(CACITY, 3, 3)` (municipio), y `CATS(DEPARTAMENTO, MUNICIPIO)` para recomponer.
   - Longitudes acumuladas: `NOMBRE1 = SUBSTRN(CATS(NOMBRE_SIN_ESP), 1, CNLFN1);` y después `NOMBRE2 = SUBSTRN(CATS(SUBSTRN(CATS(NOMBRE_SIN_ESP), CNLFN1 + 1)), 1, CNLFN2);` (cada campo empieza donde terminó el anterior, más 1 de separación).
3. **Frecuencia y ejemplos:**
   - Posiciones fijas: L11828, L11858, L11918 (AHO); L14159, L14189, L14249 (CTE); L15438 `CODIGO_UBICACION=CATS(SUBSTR(DEPARTAMENTO, 1, 2), SUBSTR(MUNICIPIO, 1, 3));`.
   - Longitudes acumuladas (12 pasos en el tramo, 4 campos x 3 productos): L10473-10476 (`NOMBRE1`, AHO), L10534-10537 (`NOMBRE2`), L10587-10591 (`APELLIDO1`, con `CNLFN1 + 1` y `CNLFN2 + 1`), L10671-10676 (`Apellido2`, con tres desplazamientos), L12804-12807 (`NOMBRE1`, CTE), L12865-12868 (`NOMBRE2`, CTE), L12918-12922 (`APELLIDO1`, CTE), L15661-15665 (`APELLIDO1`, NEQUI).
4. **Intención:** Separar el nombre completo del origen (campo único) en primer nombre, segundo nombre, primer apellido y segundo apellido, usando las longitudes de cada parte que trae el maestro de clientes (`CNLFN1`, `CNLFN2`, `CNLLN1`, `CNLLN2`). Y derivar el código de ubicación de departamento y municipio a partir de la ciudad.
5. **Clasificación:** lógica de datos (transformación fila a fila). Es la cadena más larga del tramo.
6. **Diseño Talend:** Un único `tMap` con las cuatro salidas calculadas en una sola expresión por campo. Como la posición de cada campo depende de la longitud del anterior, el cálculo acumulado va en una rutina Java `partirNombre(nombre, l1, l2, l3, l4)` que devuelve un objeto con los cuatro valores. No hay intermedios: `NOMBRE1`, `NOMBRE2`, `APELLIDO1` y `APELLIDO2` salen del mismo `tMap`.
7. **Detección:** Léxico: `SUBSTRN(CATS(`, `CNLFN1 + 1`, `CNLLN1 + 1` (parámetros de longitud acumulada). Como señal de IR: cadena de DATA steps donde cada uno lee la columna que escribió el anterior, y que comparten el mismo conjunto de parámetros de longitud. Esa cadena es un candidato directo a fusionar en un `tMap`.
8. **Riesgos y falsos positivos:** `SUBSTRN` no trunca los blancos finales y `CATS` los elimina: eso cambia el desplazamiento. Si `CNLFN1` es missing, toda la cadena es missing (en SAS `CNLFN1 + 1` es missing). `SUBSTR` de posición fija sobre `CACITY` falla si el código tiene menos de 5 caracteres. Hay una rama alternativa con `IFC(... = "", "05", ...)` que cubre el caso vacío, pero no el caso de longitud corta.

---

## 9. Normalización de texto (tildes y símbolos)

1. **Nombre genérico:** Limpieza de nombres: quitar tildes y eñes con mapeo carácter a carácter, y eliminar símbolos no alfanuméricos con expresión regular.
2. **Firma estructural:** `NOMBRE_SIN_ESP = PRXCHANGE('s/[^A-Z, a-z,0-9, ]//', -1, KTRANSLATE(NOMBRE, "NnAaEeIiOoUuUu ", "ÑñÁáÉéÍíÓóÚúÜü-"));`
3. **Frecuencia y ejemplos:** 3 en el tramo (uno por producto): L10136-10140 (AHO), L12467-12471 (CTE), L15371-15375 (NEQUI). Idéntica expresión en los tres.
4. **Intención:** Nombre limpio para el formulario regulatorio (sin tildes, sin caracteres especiales), que es lo que exige el reporte.
5. **Clasificación:** lógica de datos (normalización).
6. **Diseño Talend:** Rutina Java `normalizaNombre(String s)`: `Normalizer.normalize(s, Normalizer.Form.NFD).replaceAll("\\p{M}", "").replaceAll("[^A-Za-z0-9, ]", "")`. Se invoca desde el `tMap`. Una sola rutina para los tres productos.
7. **Detección:** `PRXCHANGE` o `KTRANSLATE` con literales acentuados. Como señal de IR: función de texto sobre una columna con literal de caracteres de origen y destino de la misma longitud.
8. **Riesgos y falsos positivos:** La codificación del fichero SAS (UTF-8 frente a latin1) cambia qué caracteres son "tildes" para `KTRANSLATE`: un fichero leído en otra codificación no coincide con el mapa. La expresión deja pasar la coma y el espacio, pero no los guiones (el mapa los convierte en espacio). El conjunto de caracteres del regex es explícito: no quita comillas ni apóstrofos.

---

## 10. Validación de texto de dirección por lista de literales y CONTAINS, con bandera

1. **Nombre genérico:** Clasificación de un campo de texto libre como consistente o inconsistente mediante una lista de literales basura, búsquedas de subcadena y reglas de longitud o forma.
2. **Firma estructural:**
   ```
   PROC SQL; CREATE TABLE X AS SELECT ..., CASE
     WHEN DIR CONTAINS 'RECLA' THEN 'INCONSISTENCIA'
     WHEN DIR = 'NA' THEN 'INCONSISTENCIA'
     WHEN LENGTH(DIR) <= 7 THEN 'INCONSISTENCIA'
     WHEN DIR IS MISSING THEN 'INCONSISTENCIA'
     WHEN INPUT(COMPRESS(DIR,' '),32.) <> . THEN 'INCONSISTENCIA'
     ELSE 'CONSISTENTE' END AS VAL_DIR FROM ...;
   ```
   Seguido de un filtro por `VAL_DIR` (patrón 1).
3. **Frecuencia y ejemplos:** 3 bloques de validación (AHO: L10605-10646; CTE: L12936-12977; NEQUI: L15521-15546) con 99 cláusulas `WHEN` en total. Filtros de salida: L10686-10694 (AHO), L15583-15595 (NEQUI).
4. **Intención:** Excluir del reporte direcciones que son marcadores de "sin dato" (`RECLAMA`, `ENTREGA PERSONAL`, `NO INFORMA`, `SIN DIRECCION`, `NA`, `@`, `??????`), o demasiado cortas, o solo numéricas. Lo consistente se queda; lo inconsistente va al control.
5. **Clasificación:** validación (calidad de datos de campo).
6. **Diseño Talend:** En un `tMap` con una tabla de referencia `tFileInputDelimited` (CSV con los literales y el tipo de regla: `contiene`, `igual`, `longitud`, `solo_numeros`). Sustituye 99 cláusulas por datos. Alternativa: rutina Java `esDireccionValida(String)` con una lista en `context`. La salida tiene dos flujos: consistentes (al reporte) e inconsistentes (`tFileOutputDelimited` de control, con el motivo).
7. **Detección:** `CASE WHEN <col> CONTAINS '...' THEN 'INCONSISTENCIA' ... ELSE 'CONSISTENTE'` o un `IFN`/`IFC` anidado con los mismos literales. Como señal de IR: varias cláusulas `WHEN` con el mismo resultado y una columna de bandera posterior filtrada.
8. **Riesgos y falsos positivos:** Las tres listas no son iguales: AHO y CTE tienen literales que NEQUI no tiene (por ejemplo `INFO`, `Sin info`, `Calle no  informa`), y CTE tiene `'Ingenieria y Diseno Informatico'` donde AHO tiene `'Ingenieria y Diseno'`. Esto hace que el mismo dato se valide de forma distinta según el producto. `CONTAINS` es sensible a mayúsculas y `'INFO'` marca como inconsistente cualquier dirección con "INFORMACION" o "INFORMATICA" (falso positivo). La comparación `'CONSISTENTE   '` con blancos depende del relleno de SAS y no es portable.

---

## 11. Deduplicación por clave de negocio (primero del grupo)

1. **Nombre genérico:** Quedarse con una fila por clave de negocio.
2. **Firma estructural:** Dos variantes:
   - SQL con ventana: `row_number() over (partition by nro_cta, llave_nombre ORDER BY nro_cta ASC, llave_nombre ASC) as rn ... where rn = 1` (L11732-11773 AHO; L14063-14104 CTE).
   - Ordenación con eliminación de duplicados: `proc sort data=X out=Y nodupkey equals; by NRO_DOC NRO_CTA; run;` (L15816-15818 NEQUI).
3. **Frecuencia y ejemplos:** 2 `row_number` y 1 `nodupkey` específico del producto en el tramo. El `nodupkey` también aparece dentro de los macros de carga (13 veces, para ordenar la lista de tablas del WORK, no para desduplicar datos de negocio).
4. **Intención:** Evitar que el mismo cliente-cuenta aparezca dos veces en la sabana (por ejemplo, cuando la unión con la tabla de direcciones devuelve varias filas).
5. **Clasificación:** lógica de datos (desduplicación). Con un matiz de E/S: el `row_number` se ejecuta en Impala.
6. **Diseño Talend:** `tUniqRow` con clave `NRO_DOC, NRO_CTA` y "keep first" (si el orden no importa), o mejor, el `row_number` dentro de la consulta `tImpalaInput` con un `ORDER BY` explícito y determinista. Así el resultado no depende del orden físico.
7. **Detección:** `row_number() ... where rn = 1`, `nodupkey`, `DISTINCT` en SQL (8 en el tramo), y `OUTER UNION` que deja filas duplicadas.
8. **Riesgos y falsos positivos:** En AHO y CTE el `ORDER BY` de la ventana es `nro_cta, llave_nombre`: son las mismas columnas de la partición, así que el orden dentro del grupo es arbitrario y el "primero" no está definido. En NEQUI la clave es `NRO_DOC, NRO_CTA` (distinta). Las dos reglas no son equivalentes. El `equals` de `nodupkey` conserva el orden de entrada, pero ese orden viene de un `proc sort` previo o de la base, que no es determinista.

---

## 12. Enriquecimiento por join en el motor (pass-through a Impala)

1. **Nombre genérico:** Lectura de datos de cliente desde una tabla maestra en el motor, con cruce por clave y cast de tipos dentro de la consulta.
2. **Firma estructural:** `proc sql; connect to impala (DSN=...); create table WORK.X as select * from connection to impala (SELECT A.*, CAST(B.col AS VARCHAR(60)) AS ... FROM tabla_A A LEFT JOIN (SELECT ... FROM tabla_maestra) B ON A.clave = B.llave); disconnect from impala; quit;`
3. **Frecuencia y ejemplos:** 10 `connection to` en el tramo (3 de enriquecimiento principal, 3 de cruce de sabana con dirección, 3 de dirección por cliente, 1 de NEQUI con cast de claves). Ejemplos:
   - L9948-9988 (AHO, "Completar nombre"): `LEFT JOIN (SELECT ... FROM proceso_vspc_finanzas.MCDQ) B ON A.LLAVE_NOMBRE = B.llave_sistema`
   - L12306-12319 (CTE, mismo cruce).
   - L14833-14837 (NEQUI): `left join proceso_vspc_finanzas.MCDQ B on CAST(A.NRO_DOC AS BIGINT) = CAST(B.num_doc AS BIGINT) and CAST(A.TIPO_DOC AS INT) = CAST(B.cod_tipo_doc AS INT)`
   - L15398-15402: `INNER JOIN ... MCDQ AS B ON CAST(...) ... where B.cod_tipo_dirp IN ('1', '2')`
4. **Intención:** Traer el nombre, la dirección y la ciudad del cliente desde el maestro (MCDQ) sin bajar el maestro completo a SAS.
5. **Clasificación:** E/S (lectura desde base) con empuje de cálculo al motor (ELT).
6. **Diseño Talend:** Un `tImpalaInput` con la consulta exacta (JOIN y CAST dentro), seguido del `tMap` de transformación. Esto sustituye al ida y vuelta SAS-Impala-SAS que hace el código original (con `connect`, `connection to` y después `create table` en SAS). Si hay que escribir de vuelta, un `tImpalaOutput` o `tImpalaRow` con `CREATE TABLE AS SELECT`.
7. **Detección:** `connect to <motor> (DSN=...)` seguido de `connection to`. Como señal de IR: nodo de conexión con SQL nativo y destino en WORK. Es fácil de detectar por léxico.
8. **Riesgos y falsos positivos:** El `LEFT JOIN` a `MCDQ` sin desduplicar puede multiplicar filas si el maestro tiene más de una fila por clave (por ejemplo, varias direcciones por cliente). Eso se corrige después con la ventana (patrón 11), pero solo en AHO y CTE. En NEQUI el join de claves se hace con `CAST` en ambos lados, lo que puede impedir el uso del índice del motor. El `DSN` está escrito a mano (`DSN=IMPALAP`) en varios pasos, mientras que otros usan la variable de entorno (patrón 26). El SQL del pass-through tiene un `;` dentro del paréntesis (L11397, L13728), lo que en SAS rompe el parseo si no está cerrado bien.

---

## 13. Join en SAS: semi-join y anti-join entre conjuntos ya extraídos

1. **Nombre genérico:** Cruce en SAS de dos conjuntos: semi-join (mantener los que tienen pareja) y anti-join (mantener los que no tienen pareja).
2. **Firma estructural:**
   - Semi-join: `CREATE TABLE A AS SELECT ... FROM B INNER JOIN C ON B.nro = C.nro ORDER BY 3 ASC, 1 ASC;` (L8383-8390, L8535-8540).
   - Anti-join: `FROM A LEFT JOIN B ON A.k = B.k WHERE B.col IS MISSING` (L14880-14906, "Cumplen no clientes").
3. **Frecuencia y ejemplos:** 3 semi-joins (uno por producto) y 1 anti-join (NEQUI). Ejemplos:
   - L8383-8390: `FROM WORK.CUMPLE_NORMA_CTE ... INNER JOIN WORK.FORMATO_SABANA_FINAL_CTE ... ON (CUMPLE_NORMA_CTE.NRO_CTA = FORMATO_SABANA_FINAL_CTE.NRO_CTA) ORDER BY 3 ASC, 1 ASC;`
   - L14902-14906: `from WORK.SABANA_FINAL_REPORTAR_FORM_NEQUI as A left join WORK.SABANA_CLIENTES_NEQUI as B on A.TIPO_DOC = B.tipo_doc and A.NRO_DOC = B.nro_doc where B.NRO_CTA is missing;`
4. **Intención:** Semi-join: traer solo las cuentas del formato final a la sabana de salida. Anti-join: identificar los no clientes del maestro para tratarlos aparte.
5. **Clasificación:** lógica de datos (segmentación por pertenencia).
6. **Diseño Talend:** Un `tMap` con `Lookup` a la tabla de referencia (`Match model: Unique match`, `Join: Inner`) para el semi-join, y `Catch lookup inner join rejects` para el anti-join. Así se obtiene en un paso lo que el SQL hace en dos. Con dos volúmenes muy grandes, `tJoin` (hash) es la alternativa, pero si la tabla de referencia cabe en memoria, `tMap` es la opción mínima.
7. **Detección:** `INNER JOIN` o `LEFT JOIN` entre dos tablas WORK seguido de `WHERE <col> IS MISSING` (anti-join), o `ORDER BY` posicional después de un `JOIN`.
8. **Riesgos y falsos positivos:** Un anti-join con `IS MISSING` solo funciona si la columna de la derecha es la de clave y no tiene nulos reales. El `ORDER BY 3, 1` posicional depende de la lista de columnas: si se cambia el `SELECT`, el orden cambia sin aviso.

---

## 14. Segmentación complementaria por regla (cumple / no cumple)

1. **Nombre genérico:** División de una población en dos conjuntos complementarios por una regla de producto o de tipo de cuenta, con lecturas separadas del mismo origen.
2. **Firma estructural:** Dos PROC SQL con el mismo `FROM` y predicados opuestos: `WHERE (CTA_NEQUI = 'CTA NEQUI')` frente a `WHERE (CTA_NEQUI <> 'CTA NEQUI')`, o `TIPO_CTA = 2` frente a `TIPO_CTA IN (1.0, 3.0, 4.0, 5.0)`.
3. **Frecuencia y ejemplos:** 6 pares de segmentación (cumple/no cumple por tipo de cuenta, y NEQUI frente a ahorros). Ejemplos:
   - L8332-8338: `WHERE ((TIPO_CTA IN (1.0, 3.0, 4.0, 5.0)) AND (CTA_NEQUI <> 'CTA NEQUI'))` (ahorros).
   - L8480-8484: `WHERE ((NO_CUMPLE_NORMA.TIPO_CTA IN (1.0, 3.0, 4.0, 5.0)) AND (NO_CUMPLE_NORMA.CTA_NEQUI = 'CTA NEQUI'))` (NEQUI).
   - L8501-8505: `... AND (NO_CUMPLE_NORMA.CTA_NEQUI <> 'CTA NEQUI')` (ahorros, complemento).
4. **Intención:** Separar la población de cada producto para reportarla por separado, con el mismo criterio de cumplimiento.
5. **Clasificación:** lógica de datos (segmentación).
6. **Diseño Talend:** Un único `tMap` con varias salidas, cada una con su `Output filter` (`row1.TIPO_CTA == 2`, `row1.CTA_NEQUI == "CTA NEQUI"`). Un solo recorrido del origen.
7. **Detección:** Dos `CREATE TABLE` seguidos con el mismo `FROM` y predicados que se contradicen. Como señal de IR: dos nodos de filtro con el mismo origen y predicados complementarios.
8. **Riesgos y falsos positivos:** Con `NULL` en `CTA_NEQUI`, tanto `<>` como `=` son falsos: la fila no entra en ninguno de los dos conjuntos. El tramo no lo corrige. El `IN` con literales `1.0, 3.0` compara números; si el tipo en origen es texto, no coincide. La división "cumple/no cumple" necesita un tercer conjunto para el residuo.

---

## 15. Detección de signo inválido en varias columnas (OR de umbrales) y tabla de incidencias

1. **Nombre genérico:** Marcar filas con algún valor negativo en un conjunto de columnas, y sacar el detalle de las incidencias.
2. **Firma estructural:** `WHERE ((( (A < 0) OR (B < 0) ) OR (C < 0)) OR ...)` con 7 columnas en un árbol de `OR` anidados (L8355-8372), seguido de una tabla de detalle obtenida con `SELECT DISTINCT ... INNER JOIN ... ORDER BY 3 ASC, 1 ASC` (L8618-8627).
3. **Frecuencia y ejemplos:** 3 bloques `CAMPOS_NEG_DEP_*` (AHO, CTE, NEQUI) y 3 bloques `INCONS_DEP_CAMPOS_NEGATIVOS_*`. Ejemplos:
   - L8358-8371 (CTE): `( ( (CUMPLE_NORMA_CTE.VAL_CRED_MES < 0) OR (CUMPLE_NORMA_CTE.NRO_CRED_MES < 0) ) OR ...)`
   - L8429-8447 (NEQUI): mismo árbol sobre `CUMPLE_NORMA_NEQUI`.
   - L8618-8627: `SELECT DISTINCT FORMATO_SABANA_FINAL_CTE.RELACION, ... FROM WORK.CAMPOS_NEG_DEP_CTE INNER JOIN WORK.FORMATO_SABANA_FINAL_CTE ON (...NRO_CTA...) ORDER BY 3 ASC, 1 ASC;`
4. **Intención:** Identificar las cuentas que traen algún campo de movimiento negativo, para revisarlas en la incidencia (y después sanear, patrón 4).
5. **Clasificación:** validación.
6. **Diseño Talend:** Un `tMap` con una columna `flag_neg = row1.A < 0 || row1.B < 0 || ...` (o una rutina `tieneNegativo(...)`), seguido de un `tFilterRow` por la bandera hacia el control. Es el mismo flujo que el clamp: flag antes del saneamiento, en el mismo recorrido.
7. **Detección:** Árbol de `OR` con el mismo operador `< 0` repetido sobre columnas distintas. Como señal de IR: N comparaciones con el mismo operador y literal, unidas por `OR`.
8. **Riesgos y falsos positivos:** Un `OR` con `missing` (`missing < 0` es verdadero en SAS) cuenta como negativo, lo que puede inflar la incidencia. El `DISTINCT` oculta filas duplicadas que deberían contarse, pues el conteo de incidencias de los patrones 17 y 16 se hace sobre la tabla distinta.

---

## 16. Conciliación de conteo y saldo por cruce de resúmenes

1. **Nombre genérico:** Conciliación entre totales: conteo y suma de saldo de tres conjuntos, y diferencias calculadas entre ellos.
2. **Firma estructural:**
   - Resumen: `SELECT COUNT(col) AS N, SUM(FIN_SALDO_CTA) AS SUMA FROM X;` (una fila).
   - Cruce: `CREATE TABLE C AS SELECT A.N, B.N, C.N, A.SUMA, ... FROM A, B, C, D;` (producto cartesiano de filas-resumen, una sola fila).
   - Diferencias: `data ...; set C; CONCILIACION_REG = NRO_REG_SABANA_FINAL - (REGISTROS_SABANA_REPORTAR + NO_CUMPLE); run;` y `CONCILIACION_SALDOS = SUMA_SALDO_FINAL_DEP_AHO - (SUMA_SABANA_FINAL + SUMA_NO_CUMPLEN);`.
3. **Frecuencia y ejemplos:** 3 resúmenes de conteo y suma por producto (`CUENTA_NO_CUMPLE_*`, `CUENTA_SABANA_REPORTAR_*`, `CUENTA_SABANA_FINAL_*`), 3 cruces de conciliación y 6 diferencias (`CONCILIACION_REG` y `CONCILIACION_SALDOS` por producto). Ejemplos:
   - L8516-8521: `SELECT COUNT(NO_CUMPLE_NORMA_NEQUI.NRO_CTA) AS NO_CUMPLE, SUM(NO_CUMPLE_NORMA_NEQUI.FIN_SALDO_CTA) AS SUMA_NO_CUMPLEN FROM WORK.NO_CUMPLE_NORMA_NEQUI ...;`
   - L9235-9239: `CREATE TABLE WORK.CONCILIACION_REPORTAR_CTE AS SELECT ... FROM WORK.CUENTA_SABANA_FINAL_CTE, WORK.CUENTA_SABANA_REPORTAR_CTE, WORK.CUENTA_NO_CUMPLE_CTE, WORK.SUMA_SALDO_CTE_FINAL_DEPOSITOS;`
   - L9291: `CONCILIACION_REG=NRO_REG_SABANA_FINAL-(REGISTROS_SABANA_REPORTAR+NO_CUMPLE);`
   - L9335: `CONCILIACION_SALDOS=SUMA_SALDO_FINAL_DEP_AHO-(SUMA_SABANA_FINAL+SUMA_NO_CUMPLEN);`
4. **Intención:** Demostrar que el total de cuentas y de saldo del reporte cuadra con el origen menos los no cumplidos. Un valor distinto de cero indica que se pierde o se duplica información.
5. **Clasificación:** validación / reconciliación.
6. **Diseño Talend:** Los conteos y sumas van en `tAggregateRow` (`count`, `sum` sobre `FIN_SALDO_CTA`) en el flujo de cada conjunto. El cruce de una sola fila y las diferencias van en un `tMap` que recibe las filas-resumen (o en `tJavaRow`). Si la diferencia no es cero, `tDie` detiene el Job con el mensaje. Así la conciliación no genera tablas: solo un control.
7. **Detección:** `COUNT(...)` y `SUM(...)` sin `GROUP BY` en un `PROC SQL`; cruce con coma (`FROM A, B, C`) entre resúmenes; diferencias con `- (x + y)` en un DATA step. Como señal de IR: nodo de agregación sin claves seguido de una operación binaria entre salidas de agregación.
8. **Riesgos y falsos positivos:** El cruce con coma es un producto cartesiano: si una de las filas-resumen no devuelve fila (conjunto vacío), toda la conciliación desaparece en silencio, sin error. `COUNT(col)` no cuenta nulos, así que el conteo depende de la columna elegida. Las sumas de la diferencia usan `FIN_SALDO_CTA` pero la de origen usa `SUMA_SALDO_FINAL_DEP_AHO` con otra regla: conviene confirmar que son la misma magnitud.

---

## 17. Recuento de incidencias para el reporte

1. **Nombre genérico:** Contador de registros con incidencia por tipo, para la hoja de control.
2. **Firma estructural:** `SELECT COUNT(TABLA.NRO_CTA) AS 'CAMPOS NEGATIVOS DEP'n FROM WORK.INCONS_...;` (con etiqueta entre comillas).
3. **Frecuencia y ejemplos:** 6 contadores de incidencia en el tramo (`CUENTA_CAMPOS_NEG_*` y `CUENTA_NO_CUMPLE_*`). Ejemplos:
   - L8553-8554: `SELECT COUNT(CAMPOS_NEG_DEP_NEQUI.NRO_CTA) AS 'CAMPOS NEGATIVOS NEQUI'n FROM WORK.CAMPOS_NEG_DEP_NEQUI;`
   - L8707-8713: `SELECT COUNT(INCONS_DEP_CAMPOS_NEGATIVOS_CTE.NRO_CTA) AS 'CAMPOS NEGATIVOS DEP'n ...`
4. **Intención:** Número de filas con incidencia que se muestra al usuario.
5. **Clasificación:** reporte.
6. **Diseño Talend:** `tAggregateRow` con `count` sobre el flujo de incidencias, a `tFileOutputDelimited` o a `tLogRow`. No requiere tabla intermedia.
7. **Detección:** `COUNT(...) AS '<etiqueta>'n` sobre una tabla de incidencias. Léxico: el alias con comillas simples y `n` final (nombre de columna SAS con espacios).
8. **Riesgos y falsos positivos:** La etiqueta contiene espacios y se exporta con ese nombre, lo que obliga a un nombre de columna especial en el destino. Hay dos etiquetas distintas para el mismo concepto ("CAMPOS NEGATIVOS DEP" y "CAMPOS NEGATIVOS NEQUI"). Conviene unificarlas.

---

## 18. Validación de rango de documento por tipo, con unión y partición por atributo

1. **Nombre genérico:** Catálogo de reglas de validación por tipo de documento: una consulta por tipo con rango válido, y una unión de las incidencias con partición posterior por atributo de relación.
2. **Firma estructural:** Un `PROC SQL` por tipo: `CREATE TABLE DOC_INCORRECTOS_TPOn_AHO AS SELECT <30 columnas>, ('NID INCORRECTO') AS INCONSISTENCIAS FROM ... WHERE (TIPO_DOC = n AND NRO_DOC [NOT] BETWEEN lo AND hi);`. Después `OUTER UNION CORR` de todas, y dos filtros complementarios por `RELACION`: `<> 1000` y `= 1000`.
3. **Frecuencia y ejemplos:** 6 validaciones (tipos 1, 2, 3, 4, 7 y 8, solo en AHO dentro del tramo), 1 unión, 2 particiones. Ejemplos:
   - L16108-16109 (tipo 1): `WHERE ( t1.TIPO_DOC = 1 AND t1.NRO_DOC BETWEEN 100000000 AND 999999999);`
   - L16148 (tipo 7): `WHERE t1.TIPO_DOC = 7 AND t1.NRO_DOC NOT BETWEEN 4000000000 AND 4999999999;`
   - L16226-16229 (tipo 4): cuatro `NOT BETWEEN` sobre rangos distintos, unidos por `AND`, para que una fila sea incorrecta solo si está fuera de los cuatro rangos.
   - L16311-16330: `SELECT * FROM WORK.DOC_INCORRECTOS_TPO1_AHO OUTER UNION CORR SELECT * FROM ... TPO2 ... TPO8;`
   - L16345 y L16361: `WHERE DOC_INCORRECTOS_AHO.RELACION <> 1000` frente a `= 1000`.
4. **Intención:** Marcar documentos cuyo número no corresponde al tipo (NIT, cédula, extranjería, etc.), y separar el control de "titulares" (`RELACION = 1000`) del de "FA y COT" (el resto).
5. **Clasificación:** validación (campo a campo, con regla de rango por tipo) y enrutamiento de la salida.
6. **Diseño Talend:** Una tabla de reglas `tFileInputDelimited` (tipo, mínimo, máximo, `modo`: `dentro` o `fuera`). Un `tMap` con `Lookup` por tipo calcula la bandera `NID_INCORRECTO`, y la salida se divide en dos flujos con `Output filter` (`row1.RELACION != 1000` y `row1.RELACION == 1000`). Así desaparecen las 6 consultas, la unión y las 2 particiones: la regla es un dato y la división es de salida, no de tabla. Si hay que mantener un solo control consolidado, un `tUnite` (unión de flujos) reemplaza el `OUTER UNION`.
7. **Detección:** `BETWEEN` o `NOT BETWEEN` sobre una columna con un literal de tipo en el mismo `WHERE`. Varios `PROC SQL` con la misma lista de columnas y un literal constante en una columna nueva. Como señal de IR: N nodos de filtro con el mismo esquema de salida y una unión final.
8. **Riesgos y falsos positivos:**
   - Probable inversión de predicado: el tipo 1 usa `BETWEEN` (marca como incorrecto a los números dentro del rango válido, L16109), mientras los demás tipos usan `NOT BETWEEN`. Debe verificarse con negocio antes de dar por bueno el control.
   - El tipo 2 solo tiene la cota inferior (`NRO_DOC > 99999999`, L16307), sin límite superior.
   - La validación se hace solo para AHO en este tramo. Si CTE y NEQUI no tienen validación equivalente, es una asimetría de control.
   - `RELACION <> 1000` y `RELACION = 1000` excluyen las filas con `RELACION` nulo, que se pierden en ambas salidas.

---

## 19. Unión de bloques con esquemas parecidos (OUTER UNION CORR)

1. **Nombre genérico:** Apilar flujos con columnas casi iguales, alineando por nombre y rellenando las que faltan.
2. **Firma estructural:** `SELECT <lista> FROM A OUTER UNION CORR SELECT <lista> FROM B;`
3. **Frecuencia y ejemplos:** 6 `OUTER UNION CORR` en el tramo (1 de clientes NEQUI más no clientes, con una columna `DIRECCION` extra en la segunda rama, L15987-16056; 6 en la unión de validaciones de documento, L16311-16330).
4. **Intención:** Juntar en una sola sabana los clientes con información y los no clientes, y en el control, todas las incidencias de documento.
5. **Clasificación:** lógica de datos (unión).
6. **Diseño Talend:** `tUnite` con el esquema de salida común. Las columnas que faltan en una rama se rellenan con `null` en el esquema del `tUnite`, sin SQL. Si una rama tiene `DIRECCION` y la otra no, en Talend se añade la columna a la rama que no la tiene con un `tMap` previo, o se fija en el esquema.
7. **Detección:** Palabra clave `OUTER UNION` (con o sin `CORR`) o `UNION` en SQL con esquemas de columnas distintas. Como señal de IR: dos nodos de proyección con conjuntos de columnas casi iguales alimentando un nodo de unión.
8. **Riesgos y falsos positivos:** `CORR` alinea por nombre, no por posición, así que un renombrado silencioso en una rama produce una columna `null` sin error. La rama de no clientes incluye `DIRECCION` y la de clientes no, lo que es correcto pero debe documentarse en el esquema.

---

## 20. Cálculo del dígito de verificación (DV) módulo 11 ponderado

1. **Nombre genérico:** Dígito de verificación con pesos fijos sobre los dígitos de un número de identificación tributaria (NIT), módulo 11.
2. **Firma estructural:** Pesos fijos 53, 47, 43, 41, 37, 29, 23, 19, 17, 13, 7, 3 aplicados a los dígitos 4 a 15 de `NRO_DOC_TEXTO` (la cadena de 15 caracteres): `resto = MOD(suma, 11)`; si `resto > 1` entonces `DV = 11 - resto`, si no `DV = resto`. Solo para `TIPO_DOC = 3`; para los demás tipos, `DV = 0`.
3. **Frecuencia y ejemplos:**
   - Bloque SQL (AHO) L10024-10079. La suma ponderada aparece 3 veces en el mismo `CASE` (una para la condición, dos para el resultado con `11 - resto` y el resultado `resto`). L10034-10045: `WHEN (MOD(((INPUT(SUBSTR(SUBSTR(NRO_DOC_TEXTO,4),1,1),w1.)*53) + (INPUT(SUBSTR(SUBSTR(NRO_DOC_TEXTO,4),2,1),w1.)*47) + ...`
   - Bloque SQL (CTE) L12355-12408: el mismo cálculo.
   - Bloque DATA (NEQUI) L14910-14941: `sum_pesos = input(substr(num,1,1),1.)*53 + ... ; resto = mod(sum_pesos, 11); if resto > 1 then DV = 11 - resto; else DV = resto;`
   - Sobrescrituras `DV=0` en L15028-15031 y L15742-15745 (ver patrón 21).
4. **Intención:** Calcular el dígito de verificación del NIT para el formulario regulatorio. La regla es la oficial de la DIAN para NIT, y la misma en los tres productos.
5. **Clasificación:** lógica de datos (cálculo). Se puede tratar también como validación, porque el dígito verifica el número.
6. **Diseño Talend:** Rutina Java `dvNit(String nro15)`: recorre los 12 dígitos con el vector de pesos, calcula `MOD 11` y devuelve el DV. Se llama desde el `tMap`: `row1.TIPO_DOC == 3 ? dvNit(row1.NRO_DOC_TEXTO) : 0`. Una sola función para los tres productos.
7. **Detección:** Una constante con la secuencia `53, 47, 43, 41, 37, 29, 23, 19, 17, 13, 7, 3` es señal única y fuerte. Como señal de IR: la misma expresión repetida más de dos veces dentro de un mismo nodo, y la misma secuencia de pesos en varios nodos.
8. **Riesgos y falsos positivos:** `INPUT(... , w1.)` devuelve missing si el carácter no es dígito, y entonces `MOD` devuelve missing y el DV queda missing sin error. En la versión NEQUI hay una guarda `length(num) >= 12` que no existe en las versiones SQL: con menos de 12 caracteres, NEQUI deja `DV=0` y SQL calcula sobre una cadena incompleta. Las tres versiones no son idénticas en los casos borde. El DV se calcula en un DATA step (NEQUI) y en un PROC SQL (AHO y CTE), y el resultado de NEQUI pasa después por la sobrescritura `DV=0` (patrón 21), aunque solo para no clientes.

---

## 21. Sobrescritura de un campo calculado por un valor constante (stub)

1. **Nombre genérico:** Paso placeholder que reasigna un campo calculado a un valor constante, sin condición.
2. **Firma estructural:** `DATA work.temporal; set X; DV = 0; run;` seguido de la copia de vuelta (patrón 3).
3. **Frecuencia y ejemplos:** 2 en el tramo. L15028-15031 (`DV=0;` sobre `COLUMNAS_BASE_NEQUI`, etiquetado "Crea campo dv") y L15742-15745 (`DV=0;` sobre `INFO_CLIENTES_NEQUI` para crear `SABANA_FINAL_NO_COMUN_NEQUI`, etiquetado "Calcula DV"). Mismo patrón con texto en L14400-14402 (`RAZON_SOCIAL="";`).
4. **Intención:** En el primer caso, dejar la columna creada para que exista en el formato; en el segundo, poner el DV de los no clientes a cero (no hay dato del maestro para calcularlo).
5. **Clasificación:** lógica de datos (placeholder). Riesgo, no regla de negocio explícita.
6. **Diseño Talend:** No se traduce como paso. En el `tMap`, la columna de no clientes se fija a `0` con una condición explícita (`row1.ES_CLIENTE ? dvNit(...) : 0`), y se documenta. Nunca como una asignación incondicional.
7. **Detección:** Asignación de literal a una columna que el mismo proyecto calcula en otro paso. Como señal de IR: columna escrita dos veces en el flujo, la segunda con constante.
8. **Riesgos y falsos positivos:** Es el punto más sensible del tramo para el reporte. En el segundo caso, todos los no clientes salen con `DV=0`, lo que puede ser intencional (sin dato de maestro) o un placeholder pendiente. Hay que decidir y documentar antes de migrar. El primer caso (sobre `COLUMNAS_BASE_NEQUI`) no altera el resultado porque después la columna pasa a `FORMATO_BD_CLIENTES_NEQUI` y de ahí a `INFO_CLIENTES_NEQUI`, donde el segundo paso la vuelve a fijar.

---

## 22. Campo condicional por regla de negocio (razón social con rango de NIT)

1. **Nombre genérico:** Rellenar un campo solo si una combinación de condiciones se cumple.
2. **Firma estructural:** `RAZON_SOCIAL = IFC((A=0 AND B=0 AND C=0 AND D=0) OR (TIPO_DOC = 3 AND NRO_DOC > 799999999 AND NRO_DOC < 1000000000), NOMBRE_SIN_ESP, "");`
3. **Frecuencia y ejemplos:** 3 en el tramo (uno por producto). Ejemplos: L10717-10719 (AHO), L13048-13050 (CTE), L15767-15769 (NEQUI).
4. **Intención:** La razón social aplica a personas jurídicas (NIT en el rango 800000000 a 999999999) o a los registros sin ningún componente de nombre de persona natural. A las personas naturales no se les pone razón social.
5. **Clasificación:** lógica de datos (regla condicional).
6. **Diseño Talend:** Expresión ternaria en el `tMap`: `(row1.CNLFN1 == 0 && ... ) || (row1.TIPO_DOC == 3 && row1.NRO_DOC > 799999999L && row1.NRO_DOC < 1000000000L) ? row1.NOMBRE_SIN_ESP : ""`.
7. **Detección:** `IFC(` o `IF ... THEN` con `TIPO_DOC = 3` y un rango de `NRO_DOC` con literales de 9 dígitos. Como señal de IR: condición compuesta sobre el mismo par de columnas en tres productos.
8. **Riesgos y falsos positivos:** Los límites (800000000 excluido, 999999999 incluido o no) no están documentados; el código usa `>` y `<` estrictos, lo que excluye 799999999 y 1000000000 pero no 800000000 ni 999999999 (dependiendo de la lectura). Comparar `NRO_DOC` (numérico) con literal sin `L`: en Talend, Java requiere `long` para comparar con literales de ese tamaño.

---

## 23. Carga masiva a Impala por partición de filas, sesiones remotas y shell externo con polling

1. **Nombre genérico:** Carga de una tabla SAS grande a Impala en paralelo, por trozos de filas en sesiones remotas, con un script de shell y espera por proceso.
2. **Firma estructural:** Un macro `%split2(lib, tabla, n, prefijo)` que: (a) cuenta filas con `open/attrn NLOBS`; (b) calcula `num_splits = ceil(n_obs / n)`; (c) para cada trozo hace `signon sessio&i`, `%syslput` de variables, `rsubmit sessio&i wait=no` con `data pwork.trozo&i; set wliborg.tabla (firstobs= obs=); newVar=int(ranuni(_n_)*1000); run; endrsubmit`; (d) `waitfor _all_`. Después `%create_commands` escribe el comando shell en una tabla; `%executeBulkload` ejecuta `x "&comando"` con `call sleep(2,1)` entre cada uno; `%waitForBulkLoads` hace `x "until [ nroproc -eq 0 ]; ... ps -fea | grep ..."` para esperar a que terminen.
3. **Frecuencia y ejemplos:** 13 bundles (12 completos en el tramo). Ejemplos:
   - L9730-9736: cabecera de `%macro split2`, cuenta de filas y cálculo del número de trozos.
   - L9778-9785: `rsubmit sessio&i wait=no ... data pwork.&tbltmp.&sessio.; set wliborg.&tabla_origen. (&firstobs &obs); newVar=int(ranuni(_n_) * 1000); run;`
   - L9796-9800: `waitfor _all_ %do i=1 %to &num_splits; sessio&i %end;`
   - L9853: `x " nroproc=5; until [ $nroproc -eq 0 ]; do nroproc=$( ps -fea | grep -i &wpgmbl. | ... | wc -l ); done ";`
   - L9884: `call sleep(2, 1);`
4. **Intención:** Cargar tablas de varios millones de filas en Impala (el archivo de `wsplit` es 1.500.000 filas por trozo) sin que una sola sesión SAS sea el cuello de botella.
5. **Clasificación:** E/S (carga) con orquestación (sesiones, espera, shell).
6. **Diseño Talend:** Un `tImpalaOutput` (o un `tImpalaRow` con `INSERT OVERWRITE ... SELECT` o `LOAD DATA` tras subir el fichero con un `tHDFSPut`) en vez de cualquier paso de trozos. Si el volumen exige paralelismo, `tParallelize` con varias ramas. El sondeo de procesos desaparece: el componente espera al terminar. Un `tDie` ante error. El ciclo de comandos se sustituye por un solo componente.
7. **Detección:** `rsubmit` con `wait=no` seguido de `waitfor _all_`; `signon`/`signoff`; `%syslput`; `x "` con el mismo comando de shell y el literal `sleep`. Como señal de IR: nodo de orquestación de sesiones remotas con carga de partición.
8. **Riesgos y falsos positivos:**
   - La columna `newVar=int(ranuni(_n_)*1000)` se añade a cada trozo y no se usa en el resto del flujo; si la carga trae todas las columnas del trozo, esa columna aleatoria acaba en la tabla de Impala.
   - El sondeo con `ps -fea | grep` depende de nombres de proceso y puede no terminar si el proceso queda colgado (`nroproc` siempre sumaria algo).
   - `set ... (firstobs= obs=)` sin `ORDER BY` no garantiza un reparto determinista de filas entre trozos.
   - Rutas fijas (`/data/Programas_SAS/source/`, `/home_sas/`) y el nombre de servidor `sasgridcomp1` van en el código.
   - Falso positivo: un `rsubmit` que solo ejecuta una consulta en el servidor remoto (sin carga) es otro patrón.

---

## 24. Limpieza de tablas de destino antes de cargar (drop before load) y limpieza condicionada por código de error

1. **Nombre genérico:** Borrar la tabla de destino en Impala antes de cargar, y borrar las tablas temporales de WORK solo si no hubo error.
2. **Firma estructural:** `proc sql; connect to impala (DSN=...); execute (drop table if exists <lib>.<tabla> purge) by impala; disconnect from impala; quit;` (macro `%deleteTableLZ`), y `%if &syserr. eq 0 %then %do; ... %do %while (%scan(&tablas, &j, "|") ne); ...; proc delete data=work.&tablaj; run; ... %end;` (macro `%delProcessTables`).
3. **Frecuencia y ejemplos:** 13 bundles con 2 macros cada uno (`%deleteTableLZ` y `%delProcessTables`). Ejemplos:
   - L9699-9701 (dentro de `%delProcessTables`): `proc delete data=work.&tablaj; run;`
   - L9695 y L9725-9727: `execute by impala (drop table if exists &libdes..&tablaj. purge);`
   - L9901: `%execImpalaQuery(drop table if exists &lib..&table purge);`
4. **Intención:** Garantizar que la carga reemplaza la tabla completa (sin datos viejos) y no deja basura en WORK tras un proceso exitoso.
5. **Clasificación:** orquestación (y E/S, por el DDL).
6. **Diseño Talend:** `tImpalaRow` con `DROP TABLE IF EXISTS ... PURGE` en un `tPreJob` (o antes del `tImpalaOutput` con "Truncate" o "Drop and create table"). La limpieza de WORK no existe en Talend: no hay tablas intermedias que borrar.
7. **Detección:** `drop table if exists`, `proc delete`, `%syserr`, `%scan(... "|")`. Como señal de IR: DDL en un bloque de macro, antes de la carga.
8. **Riesgos y falsos positivos:** En `%delProcessTables` la rama `%else` usa `%sysfunc(lowcase(proceso))` sin `&`, de modo que compara con el texto "proceso" fijo, no con la variable; el `&libdes..&tbldes_lz.` de esa rama depende de una variable que se define por cada bundle. `%syserr` no es un indicador fiable de carga exitosa de Impala: solo refleja errores de SAS, no de la base. Un `drop` sin `IF EXISTS` correcto puede borrar algo mal nombrado.

---

## 25. Bundle de macros duplicado (candidato a joblet)

1. **Nombre genérico:** Bloque de definición de macros idéntico repetido por tabla, con solo el nombre de la tabla cambiado.
2. **Firma estructural:** Bajo la cabecera `TITLE "Tarea para la Importacion desde LZ"`, un bloque de unos 296 líneas que define `%ambiente`, `%delProcessTables`, `%split2`, `%create_commands`, `%waitForBulkLoads`, `%executeBulkload`, `%execImpalaQuery`, `%deleteTableLZ`, `%tiempos`, y después asigna `%let wpathdata`, `%let wtabsrc`, `%let tbldes_lz`, `%let wprefix` y llama a `%split2`, `%create_commands`, `%deleteTableLZ`, `%executeBulkload`, `%waitForBulkLoads`, `%delProcessTables`, `%tiempos`. Solo cambian las variables de origen y destino.
3. **Frecuencia y ejemplos:** 13 cabeceras (12 bundles completos) de 296 líneas cada uno, 3.552 líneas en total (43 % del tramo). Ejemplos de la cabecera repetida: L9645, L10160, L10740, L11053, L11419, L11977, L12491, L13071, L13384, L13750, L14475, L15058, L16382. Los `%macro split2` aparecen 13 veces, idénticos salvo el nombre de la tabla que llama al bundle.
4. **Intención:** Ninguna distinta a la del patrón 23. Es un copia y pega de la tarea de carga de cada tabla.
5. **Clasificación:** fontanería (duplicación), con orquestación de carga.
6. **Diseño Talend:** Un joblet `JL_CargaImpala` con parámetros de contexto (`tabla_origen`, `tabla_destino`, `libreria`, `entorno`). El Job principal llama al joblet en un bucle (`tFlowToIterate` sobre la lista de tablas, o 13 `tRunJob` si se prefiere explícito). Esto reduce 3.552 líneas a un componente de carga con 13 invocaciones, o a un único `tFlowToIterate`. El detalle de implementación (sesiones, sondeo) desaparece con el patrón 23.
7. **Detección:** Huella de texto normalizada: quitar los nombres de tabla y comparar bloques de N líneas (hash). Como señal de parser: el mismo conjunto de nombres de `%macro` definido más de una vez con el cuerpo idéntico. Como señal de IR: N nodos de carga con la misma subestructura y solo cambian dos parámetros.
8. **Riesgos y falsos positivos:** Las copias no son idénticas del todo: hay diferencias de `DSN` (algunas tareas usan `IMPALAP` escrito a mano, otras `&lz_DSN`), y de rutas. Eso se detecta solo con diff entre bundles. Un error en una copia (como `sysfunc(lowcase(proceso))` sin `&`, patrón 24) se reproduce en las trece. Un bundle que parezca duplicado pero difiera en una condición de negocio no debe colapsarse sin revisar.

---

## 26. Selector de entorno por código (D, C, P) y DSN

1. **Nombre genérico:** Elección del destino (desarrollo, certificación, producción) por una variable de código, mediante una cadena de `%if`.
2. **Firma estructural:** `%macro ambiente; %if &m_ambiente eq D %then %do; %let lz_dsn=IMPALA; %end; %else %if &m_ambiente eq C %then %do; %let lz_dsn=IMPALAC; %end; %else %if &m_ambiente eq P %then %do; %let lz_dsn=IMPALAP; %end; %mend;` Más `%include "/data/Programas_SAS/activenodelzcode.sas";` que define `m_ambiente`.
3. **Frecuencia y ejemplos:** 13 selectores (uno por bundle). Ejemplos: L9652-9672, L10167-10187, L11060-11080. Además, DSN fijo en 12 consultas (por ejemplo L9944 `connect to impala (DSN=IMPALAP);`, L11352 `connect to IMPALA (DSN = IMPALAP);`, L14804, L15382).
4. **Intención:** Un mismo código sirve para los tres entornos, cambiando un código de una variable.
5. **Clasificación:** parametrización / entorno.
6. **Diseño Talend:** Contextos de Talend (`Default`, `Certi`, `Prod`) con variables `IMPALA_DSN`, `IMPALA_HOST`, `IMPALA_DB`. Un `tImpalaConnection` que lee del contexto. Sustituye las 13 cadenas `%if` y las 12 escrituras fijas de DSN por una sola fuente. Todo el DSN se toma del contexto activo.
7. **Detección:** `%if &<variable> eq <letra>` con asignaciones de nombre de DSN; `%include` de un fichero de entorno; literales `DSN=` fijos en consultas. Como señal de IR: la misma dependencia de DSN en varios nodos, algunos con variable y otros con literal.
8. **Riesgos y falsos positivos:** Las consultas con `DSN=IMPALAP` escrito a mano apuntan siempre a producción, aunque el resto del proceso se ejecute en certificación. Eso es un riesgo real de escritura en producción desde un entorno de prueba. El `%include` de un fichero externo impide saber qué define `m_ambiente` sin acceder al servidor.

---

## 27. Parámetros de fecha desde una tabla de un registro

1. **Nombre genérico:** Leer un registro de una tabla de control y pasar sus campos a variables macro (año, mes, día).
2. **Firma estructural:** `%GLOBAL ANIO; %GLOBAL MES; %GLOBAL DIA; proc sql; SELECT AÑO INTO: ANIO FROM WORK.VALIDACION_FECHA; SELECT MES INTO: MES FROM ...; SELECT DIA INTO: DIA FROM ...;`
3. **Frecuencia y ejemplos:** 2 bloques (AHO L11717-11726 y CTE L14048-14057), 6 `SELECT INTO`. Ejemplo: L11724 `SELECT AÑO INTO: ANIO FROM WORK.VALIDACION_FECHA;`
4. **Intención:** Fechar la sabana con la fecha de proceso (año, mes, día del corte).
5. **Clasificación:** parametrización.
6. **Diseño Talend:** Un `tFileInputDelimited` o `tImpalaInput` de un registro, leído en `tPreJob` y guardado en `context.ANIO`, `context.MES`, `context.DIA`. Un `tJavaRow` puede convertir el valor. No existe equivalente de `SELECT INTO`.
7. **Detección:** `SELECT <col> INTO: <macro> FROM <tabla>` con una sola fila esperada. Como señal de IR: variable macro asignada desde una consulta.
8. **Riesgos y falsos positivos:** Si la tabla tiene más de una fila, `SELECT INTO` asigna la última sin error. Las variables `ANIO`, `MES`, `DIA` no se usan en el tramo: no se encuentra referencia posterior dentro de estas líneas. Conviene verificar en el resto del archivo antes de eliminarlas. El nombre `AÑO` contiene una eñe, lo que exige que el código sea texto UTF-8 en el servidor.

---

## 28. Trazas, medición y metadatos de ejecución

1. **Nombre genérico:** Impresión de tiempos, de variables y de opciones de depuración en el log.
2. **Firma estructural:** `%macro tiempos; options nosymbolgen nosource nosource2; %put INICIO: &hi.; %put FINAL: %sysfunc(strip(%sysfunc(datetime(), datetime20.))); %mend;`, `options symbolgen mlogic mprint source2;`, y `%put &=workpath;`.
3. **Frecuencia y ejemplos:** 99 `%put`, 12 llamadas a `%tiempos`, 13 bloques de `options` de depuración. Ejemplos: L9932-9940 (macro de tiempos), L9678 (`options nosyntaxcheck source symbolgen source2 mlogic mprint;`), L9803 (`%put &=workpath;`).
4. **Intención:** Medir la duración de cada carga y registrar en el log qué se ejecutó.
5. **Clasificación:** trazas / medición.
6. **Diseño Talend:** Se descarta el código de depuración. La medición se hace con `tStatCatcher` (estadísticas del Job) y `tFlowMeter` (filas por flujo), y el registro con `tLogRow` o `tWarn`. No hay equivalente de `%put`.
7. **Detección:** `%put`, `options ... mlogic mprint`, `datetime()`, `%tiempos`. Léxico, sin ambigüedad.
8. **Riesgos y falsos positivos:** Las opciones de depuración (`mprint`, `mlogic`, `symbolgen`) dejan trazas de macro sensibles en el log (rutas, variables de usuario). Un `%put &lz_dsn` puede registrar credenciales de DSN si la variable contiene más que un nombre. Eliminar estas trazas es correcto, pero conservar el tiempo de carga como métrica.

---

## 29. Orden posicional de salida (ORDER BY n)

1. **Nombre genérico:** Ordenación de salida por posición de columna, no por nombre.
2. **Firma estructural:** `ORDER BY 3 ASC, 1 ASC;` al final de un `CREATE TABLE ... AS SELECT ...`.
3. **Frecuencia y ejemplos:** 34 `ORDER BY` en el tramo, muchos posicionales. Ejemplos: L8390 y L8808 (`ORDER BY 3 ASC, 1 ASC;` tras `INNER JOIN` de paquete), L8679.
4. **Intención:** Ordenar el paquete de salida por número de cuenta (columna 3) y por relación (columna 1), que es el orden que pide el formato.
5. **Clasificación:** lógica de datos (orden de salida). Es un requisito del formato.
6. **Diseño Talend:** `tSortRow` solo si el formato exige orden, con las columnas nombradas (`NRO_CTA`, `RELACION`), no por posición. Si el orden lo fija el destino (por ejemplo, un fichero que se lee en orden), conviene confirmar que se mantiene.
7. **Detección:** `ORDER BY <número>` sin nombre de columna. Léxico.
8. **Riesgos y falsos positivos:** Un cambio en el `SELECT` (añadir o quitar una columna antes de la 3) cambia el orden sin error. Es un riesgo de mantenimiento, no de cálculo.

---

## (A) Diseño objetivo del tramo en Talend

Con el mínimo de Jobs y componentes, el tramo se resuelve con 4 Jobs y unos 20 componentes distintos, frente a los 48 bloques SQL, los 63 pasos de mutación con copia de vuelta y los 13 bundles de carga del original.

| Job | Qué hace | Componentes (conteo) |
|---|---|---|
| `J00_Parametros` | Lee la fecha de proceso (patrón 27) y la deja en `context`. | `tImpalaInput` (1), `tJavaRow` (1) |
| `J10_Sabana_Producto` | Una sola ejecución por producto (AHO, CTE, NEQUI), parametrizada con `context.producto`. Lee la sabana de origen con el JOIN y el CAST ya resueltos en Impala (patrón 12), y aplica en un único `tMap`: clamp de negativos (4), partición de nombre (8), normalización (9), DV (20), valores por defecto y constantes (7), recodificación (6), conversión de tipo (5), validación de dirección (10, rutina o tabla de reglas), validación de documento (18, tabla de reglas), razón social (22) y la bandera de incidencias (15). Las salidas del `tMap` son: sabana (con `Output filter` para cumple/no cumple, patrón 14), rechazos de dirección y documento, e incidencias. | `tImpalaInput` (1), `tMap` (1, con 4 a 5 salidas), `tUniqRow` (1, si no se resuelve en Impala), `tAggregateRow` (1, conteo y suma para la conciliación), `tImpalaOutput` (1), `tFileOutputDelimited` (2, incidencias y control), rutinas Java (`dvNit`, `partirNombre`, `normalizaNombre`, `esDireccionValida`). |
| `J20_Control` | Conciliación (patrón 16) y contadores de incidencia (patrón 17). Si la diferencia no es cero, detiene el proceso. | `tFileInputDelimited` (1, si hay resúmenes en fichero) o `tAggregateRow` (1), `tMap` (1), `tDie` (1), `tLogRow` (1) |
| `J30_Carga_Cierre` | Limpieza de la tabla de destino antes de la carga (patrón 24) y, si el volumen lo exige, carga de partición (patrón 23) como joblet. | `tImpalaRow` (1, drop y create), `tImpalaOutput` o `tImpalaRow` (1), `tStatCatcher` (1, medición) |

Orden de ejecución: `J00` y después `J10` tres veces (un `tFlowToIterate` sobre la lista de productos, o tres `tRunJob`), `J20`, y `J30`. Se mantiene un solo joblet de carga (`JL_CargaImpala`) en lugar de 13 bundles.

Conteo esperado: 4 Jobs, 1 joblet, unos 20 componentes distintos y 4 rutinas Java. Las 48 consultas, las 63 copias de temporal, los 13 bundles, los 91 bloques de cabecera, los 163 comentarios de etiqueta y las 99 llamadas `%put` desaparecen como código; sus intenciones se conservan en los nombres de componentes, en los contextos y en las rutinas.

---

## (B) Tabla patrón a capa de implementación, con prioridad

Capas de la herramienta: **lexer/parser** (tokens y comentarios), **macro resolver** (`%let`, `%macro`, `%include`, `%if`, resolución de variables), **IR** (pasos DATA, PROC SQL, pass-through, sesiones remotas), **traductor** (IR a componentes Talend) y **planificador** (agrupación en Jobs, detección de joblets y orden).

Prioridad: frecuencia multiplicada por impacto en el resultado del diseño. ALTA si reduce de forma directa el número de Jobs o componentes, o si evita una regla incorrecta; MEDIA si mejora la calidad; BAJA si solo elimina ruido.

| # | Patrón | Capa de implementación | Frecuencia (tramo) | Prioridad |
|---|---|---|---|---|
| 25 | Bundle de macros duplicado (joblet) | Macro resolver (resolución de copias) + planificador (joblet) | 13 bundles, 3.552 líneas | ALTA |
| 23 | Carga masiva por partición, sesiones remotas y shell | IR (sesiones remotas) + traductor (`tImpalaOutput` o `tImpalaRow`) | 13 | ALTA |
| 2 | Fontanería de interfaz (drop/open, cabeceras, etiquetas, TITLE) | Lexer/parser (descarte) | 48 + 91 + 163 | ALTA (reduce ruido) |
| 3 | Mutación en lugar con temporal | IR (fusión de DATA en nodo de transformación) | 63 | ALTA |
| 4 | Clamp de negativos | Traductor (expresión en `tMap`) | 21 | ALTA |
| 12 | Enriquecimiento por join en Impala (pass-through) | IR (SQL nativo) + traductor (`tImpalaInput`) | 10 | ALTA |
| 8 | Partición de nombre por longitudes acumuladas | Traductor (rutina) + IR (cadena de DATA a un nodo) | 12 | ALTA |
| 10 | Validación de dirección (literales, CONTAINS) | Traductor (tabla de reglas o rutina) | 99 WHEN | MEDIA-ALTA (calidad) |
| 18 | Validación de documento por tipo, unión y partición | Traductor (tabla de reglas, `tMap` con salidas) + planificador | 6 + 1 + 2 | MEDIA-ALTA (posible error de predicado) |
| 20 | Cálculo de DV módulo 11 | Traductor (rutina Java) + detector de expresiones repetidas | 3 bloques | MEDIA |
| 16 | Conciliación de conteo y saldo | Traductor (`tAggregateRow`, `tDie`) + planificador (control) | 9 | MEDIA |
| 14 | Segmentación cumple / no cumple | Traductor (`tMap` con varias salidas) | 6 pares | MEDIA |
| 13 | Semi-join y anti-join en SAS | Traductor (`tMap` con Lookup y rechazos) | 4 | MEDIA |
| 11 | Deduplicación por clave | Traductor (`tUniqRow` o ventana en Impala) + detector de criterios | 3 | MEDIA |
| 15 | Signo inválido en N campos | Traductor (flag en `tMap`) | 6 | MEDIA |
| 7 | Valores por defecto y constantes | Traductor (expresión en `tMap`, `context`) | 9 + 6 | MEDIA |
| 5 | Conversión de tipo con PUT / INPUT | Traductor (rutina de formato) | 11 | MEDIA |
| 6 | Recodificación con IFN anidado | Traductor (`tMap` con Lookup) | 1 | BAJA-MEDIA |
| 9 | Normalización de texto | Traductor (rutina Java) | 3 | MEDIA-BAJA |
| 21 | Sobrescritura por constante (stub) | Detector de riesgo (lint), no traducción | 2 | MEDIA (decisión de negocio) |
| 22 | Campo condicional con rango de NIT | Traductor (expresión ternaria) | 3 | MEDIA |
| 1 | Filtro de subconjunto con WHERE | Traductor (`tFilterRow` o filtro de salida de `tMap`) | aprox. 15 | MEDIA (se absorbe en el `tMap`) |
| 17 | Recuento de incidencias | Traductor (`tAggregateRow`) | 6 | BAJA-MEDIA |
| 19 | Unión con OUTER UNION CORR | Traductor (`tUnite`) | 6 | BAJA-MEDIA |
| 24 | Drop antes de carga y limpieza de WORK | Traductor (`tImpalaRow` en `tPreJob`) | 13 | MEDIA |
| 26 | Selector de entorno por código y DSN fijo | Macro resolver (contextos Talend) + detector de DSN fijo | 13 + 12 | ALTA (riesgo en producción) |
| 27 | Parámetros de fecha desde tabla | Traductor (`tPreJob` y `context`) | 2 | MEDIA |
| 29 | Orden posicional | Traductor (`tSortRow` con nombres) + detector | 34 | BAJA |
| 28 | Trazas y medición | Lexer/parser (descarte) + traductor (`tStatCatcher`, `tFlowMeter`) | 99 + 12 | BAJA (ruido) |

---

## Conclusiones principales del tramo

1. El 43 % del tramo (3.552 de 8.300 líneas) son 12 copias del mismo bundle de carga a Impala, con 13 cabeceras en total. Solo cambian el nombre de la tabla de origen y de destino. Un joblet parametrizado reemplaza ese bloque. Es el candidato de mayor impacto y el más fácil de detectar por huella de texto.

2. La cadena de transformaciones fila a fila (clamp, partición de nombre, normalización, DV, valores por defecto, conversión de tipo, validación de dirección y de documento) ocupa unos 63 pasos DATA y PROC SQL con copia de vuelta y borrado de temporales. Todo eso cabe en un único `tMap` por producto, con rutinas Java para el cálculo y tablas de reglas para la validación, sin datasets intermedios.

3. El tramo contiene al menos tres puntos que requieren verificación de negocio antes de migrar:
   - La validación de tipo 1 usa `BETWEEN` (L16109), mientras los demás tipos usan `NOT BETWEEN`: probable inversión que marca como incorrectos números válidos.
   - El DV de los no clientes de NEQUI se fija a 0 (L15744), y el mismo patrón aparece en L15030. Es un placeholder que altera un campo calculado.
   - Las tres listas de validación de dirección no son iguales entre productos, y las reglas de deduplicación (`row_number` por cuenta y llave en AHO y CTE, `nodupkey` por documento y cuenta en NEQUI) tampoco. El mismo dato se trata de forma distinta según el producto.

4. El patrón de ida y vuelta con el motor (SAS a Impala para el enriquecimiento, y de vuelta a SAS para la transformación, y otra vez a Impala para la carga) se resuelve con el ELT del `tImpalaInput` más un único `tMap`, sin bajar datos a SAS. El pass-through del tramo ya hace el JOIN y el CAST en el motor; lo que sobra es el paso intermedio de WORK.

5. Alrededor del 50 % del tramo es fontanería o trazas (cabeceras, etiquetas, drop/open de tablas, `%put`, `%tiempos`, opciones de depuración, macros de entorno repetidos). Se descarta por completo en la migración, salvo lo que aporta valor: el parámetro de fecha (`context`), el control de conciliación (`tDie`) y la medición (`tStatCatcher`). Los DSN fijos (`DSN=IMPALAP`) en consultas de otros entornos son un riesgo a corregir con contextos.

---

Limitaciones: el tramo no contiene `PROC IMPORT`, lectura de Excel o CSV, ni descarga remota. Los patrones de tipo (g) quedan sin evidencia en este tramo y deben buscarse en el resto del archivo. Las variables `ANIO`, `MES` y `DIA` no se referencian dentro de las líneas 8301 a 16600. Los números de este documento son conteos del tramo; el total del archivo puede diferir.
