# Convenciones de los Jobs generados

El cliente no tiene convenciones, así que estas son **las del portal**. Son obligatorias para todo lo que se genere y se
comprueban en `tests/support/spec_invariants.py`. Se pueden cambiar en un solo sitio (este documento y esa prueba), no job a job.

## 1. Estructura de un Job

Un programa SAS es un Job. Su forma es siempre la misma:

```
tPrejob ──► [conexiones]  tDBConnection por cada libname/motor, con variables de contexto
   │        [contexto]    tContextLoad solo si el entorno lo pide
   └──► subjob "<Etiqueta 1>" ──► subjob "<Etiqueta 2>" ──► ...      (OnSubjobOk entre ellos)
tPostjob ─► [cierre]      tDBCommit y tDBClose de cada conexión del prejob; tChronometerStop
errores   ─► tLogCatcher ─► tLogRow  (+ tDie si el subjob es crítico)      (ya implementado: BP-ERR-01)
```

- **Un subjob por bloque `/* Etiqueta: X */`** de SAS Studio (si no hay etiquetas, uno por paso `DATA`/`PROC`). El nombre
  del subjob es la etiqueta, normalizada.
- **Conexiones solo en el prejob y cierre solo en el postjob.** Los componentes de datos usan la conexión compartida
  (`USE_EXISTING_CONNECTION`), nunca abren la suya. Un `libname` de base de datos = una conexión; un `libname` de carpeta no
  abre nada (es solo un directorio de contexto).
- **Fallo = parar y registrar.** Un subjob crítico (escribe datos, borra, carga) termina con `tDie` en `SUBJOB_ERROR`; uno de
  apoyo (reportes, medición) solo registra con `tWarn`.
- **Macro con parámetros = Job hijo** con las variables como contexto y `tRunJob`. Una **macro sin parámetros que se repite**
  (el mismo patrón en muchos programas) = **joblet**.
- **Lo repetido va a un joblet**, nunca se copia: «soltar tabla si existe y crearla», «contar filas y registrar», el manejo
  de errores y la medición de tiempo.

## 2. Contexto y variables

- **Todo lo que cambia entre entornos va a contexto**: servidor, puerto, base, esquema, usuario, rutas de archivos y carpetas.
  Nada de eso se escribe en un componente.
- **Grupos de contexto: `DEV`, `TEST`, `PROD`.** El portal genera los tres con los mismos nombres de variable; `DEV` lleva
  los valores conocidos y los otros quedan vacíos hasta que alguien los complete.
- **Nombres**: `<ambito>_<objeto>_<atributo>` en minúsculas, por ejemplo `db_lz_host`, `db_lz_user`, `db_lz_password`,
  `path_in_base`, `sas_param_<nombre>` para una macrovariable de SAS. Una macrovariable `&x` es `context.sas_param_x`.
- **Contraseñas**: tipo `Password`, vacías en el Job y nunca en claro. Si el SAS trae una clave literal, el portal la redacta
  y la reporta (`docs/security.md`); jamás pasa al Job ni a un informe.
- **Variables que el programa calcula** (`%let x = %sysfunc(...)`, `call symput`) = `tSetGlobalVar` y `globalMap.get`, no contexto.

## 3. Nombres

| Qué | Regla | Ejemplo |
| --- | ----- | ------- |
| Job | `<proyecto>_<programa>`, identificador Java, ≤ 60 caracteres, único en el proyecto | `finanzas_cod2` |
| Carpeta del Job | `Process/<proyecto>/<carpeta del programa>/` sin `src`, `tests` ni `target` | `Process/finanzas/lz` |
| Subjob | la etiqueta normalizada (sin acentos, sin espacios) | `importar_homologacion` |
| Componente | `t<Tipo>_<n>` (único) y etiqueta `<subjob> · <operación>` | `tFilterRow_4`, «acura · filtrar» |
| Conexión | `row_<n>_<m>` si es de datos; en un `tMap`, el nombre de la conexión es el de su tabla | `row_3_1` |
| Joblet | `JL_<patrón>` en `Joblet/<proyecto>/` | `JL_drop_create_tabla` |
| Contexto | ver la sección 2 | `db_lz_host` |

## 4. Elección de componentes

Se usa **el componente más específico que existe** (hay más de mil en el catálogo; el valor está en no caer siempre en
`tMap`). Una expresión Java dentro de un componente es el último recurso, no el primero.

| SAS | Componente | Configuración |
| --- | ---------- | ------------- |
| `WHERE`, `IF` simple | `tFilterRow` | tabla `CONDITIONS`; modo avanzado solo si no cabe |
| Columnas a conservar o quitar | `tFilterColumns` | esquema de salida |
| Renombrar | `tMap` o esquema del siguiente componente | sin Java |
| Calcular columnas | `tMap` | expresiones; con la rutina `SasFunctions` |
| `PROC SORT`, `NODUPKEY` | `tSortRow`, `tUniqRow` | tablas `CRITERIA` y `UNIQUE_KEY` |
| `MERGE BY`, `JOIN ... ON` | `tJoin` | tabla `JOIN_KEY`; `tMap` solo con varias salidas o lookups complejos |
| `PROC MEANS/SUMMARY/FREQ`, `GROUP BY` | `tAggregateRow` | `GROUPBY` y `OPERATIONS` |
| `UNION`, `SET a b` | `tUnite` | un flujo por tabla |
| `PROC TRANSPOSE`, arrays | `tNormalize`, `tDenormalize` | columna y separador |
| `DATALINES` | `tFixedFlowInput` | esquema y filas completas |
| `PROC FORMAT` | `tMap` con lookup, `tReplace` o `tFixedFlowInput` + `tJoin` | tabla de valores |
| `PROC IMPORT`/`INFILE` (CSV) | `tFileInputDelimited`; Excel: `tFileInputExcel` | ruta por contexto, esquema, cabecera |
| `PROC EXPORT`/`FILE PUT` | `tFileOutputDelimited`, `tFileOutputExcel` | ruta por contexto |
| `LIBNAME` de base de datos | `tDBConnection` (o el del motor: `tImpalaConnection`, `tOracleConnection`...) | en el prejob |
| Lectura/escritura en base de datos | `tDBInput`, `tDBOutput` (o el del motor) | conexión compartida; esquema |
| `PROC SQL` *pass-through* (`execute`, `connect to`) | `tDBRow`, `tDBInput` | SQL literal o variable de contexto |
| `PROC DELETE`, `PROC DATASETS DELETE` | `tDBRow` con `DROP TABLE IF EXISTS`, o `tFileDelete` | |
| `PROC APPEND` | `tDBOutput` con acción `INSERT` | |
| `%INCLUDE` estático | `tRunJob` | Job hijo del archivo incluido |
| `%DO i=1 %TO n` | `tLoop` o `tFlowToIterate` + `tRunJob` | contador como variable |
| `X`, `SYSTASK` | `tSystem` | |
| `PUT`/`%PUT` de seguimiento | `tLogRow`, `tWarn` | |
| Medición de tiempo (`%sysfunc(datetime())`) | `tChronometerStart`, `tChronometerStop` | |
| Estado entre filas (`RETAIN`, `FIRST.`/`LAST.`, `LAG`) | variables del `tMap`, `tSortRow`, `tAggregateSortedRow` | si no cabe, `tJavaRow` marcado `needs_review` |
| Lo no traducible | `tJavaRow` solo como último recurso, con el SAS original en comentario | `needs_review` |

## 5. Esquemas y tipos

- El esquema sale del **catálogo de entorno** (`environment.json`) y se propaga por el plan; nunca se inventa.
- Tipos SAS → Talend: numérico → `id_Double` (o `id_Integer`/`id_Long` si el catálogo lo dice), carácter → `id_String`
  con su longitud, fecha SAS → `id_Date` con patrón `yyyy-MM-dd`. La fecha SAS cuenta días desde 1960; la rutina
  `SasFunctions` hace la conversión.
- **Valor perdido de SAS = `null`.** Las comparaciones y la aritmética pasan por `SasFunctions`.

## 6. Qué queda siempre como pendiente

Solo lo que el SAS y el catálogo no pueden dar: una credencial, una ruta de entorno, un tipo ambiguo, código dinámico.
Cada pendiente lleva su motivo y su línea de origen. Nada se rellena con un valor supuesto.
