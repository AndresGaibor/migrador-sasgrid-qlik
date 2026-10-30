# Fusión a corriente

El planificador ya no traduce cada operación SAS a su propio componente. Un programa se convierte en
una corriente de pocos pasos: lectura, un `tMap` que hace el filtrado y los cálculos, `tUniqRow` si
hay deduplicado, escritura. La fontanería de SAS (ejecución de comandos, esperas, mensajes, tiempos,
borrado de temporales, troceado por lotes) no genera pasos: queda registrada con su equivalente Talend.

La regla de diseño: Talend pasa datos de un componente a otro por los conectores del Job; lo que SAS
hace con datasets intermedios se resuelve en la corriente, no con escrituras y lecturas intermedias.

## Capas

| Capa | Dónde | Qué decide |
| --- | --- | --- |
| 1. Etiquetado en el IR | `intermediate_representation/` (builder y `repetition.py`) | Cada operación tiene un tipo. Las llamadas a macros de fontanería pasan a tipo `infrastructure` (`plumbing.tag_macro_calls`), con su clasificación dentro de `details.plumbing`. |
| 2. Fontanería | `migration_planner/plumbing.py` | `plumbing_of(op)` clasifica comandos del sistema (`x`, `sleep`/`until`), `%put`, cálculo de tiempos con `datetime()`, macros de control de ambiente, borrado de WORK, `symputx`, troceo por lotes, espera, control de errores y conteo. `plumbing_macros` marca macros enteras como fontanería si ≥70 % de su cuerpo lo es. |
| 3. Fusión a corriente | `migration_planner/pipeline.py` (`build_flow`) y `fusion.py` (`merge_tmap`) | Qué pasos existen y cómo se conectan. Las cadenas fila a fila (`filter`, `compute`, `rename`, `select_columns`, `project`) se funden en un `tMap`. Un intermedio leído por varios grupos se reparte con un `tMap` de varias salidas. |
| 4. Estructura de Jobs | `migration_planner/job_structure.py` | Partes por tamaño, Job padre con `tRunJob` cuando hace falta, y como mucho 3 pasos recomendados por Job: el `tDie` de error y, si hay base de datos, una conexión compartida y su cierre. |

La fontanería se registra en `JobPlan.not_migrated`. Las capas 2 y 3 nunca escriben el mismo caso: si
una operación es fontanería, no entra en la corriente.

### Capa 2: qué es fontanería

| Categoría | Ejemplo SAS | Equivalente Talend registrado |
| --- | --- | --- |
| `shell_auxiliar` | `x 'echo ...';` | `tSystem` solo si el comando es imprescindible |
| `espera` | `sleep`/`until` en el shell, `sleep()` en un paso | El Job continúa con `OnSubjobOk` |
| `mensajes` | `%put`, macros que solo escriben en el log | `tLogRow` o los logs del Job |
| `medicion` | `datetime()` en un paso | `tStatCatcher` |
| `entorno` | macro de control de ambiente (DEV/QA/PROD) | Variables de contexto por ambiente |
| `limpieza_datasets` | `proc datasets ... delete` sobre WORK | Sin equivalente: el flujo no crea el temporal |
| `troceado_lotes` | troceo por rangos de observaciones (`firstobs`/`obs` con macro variables) | Batch size o escritura por bloques del componente de salida |
| `conteo` | `select count(*)` sin alias | `tFlowMeter` y `tStatCatcher`; `tDie` si no coinciden |
| `variables_control` | `call symputx(...)` en un DATA step | Variable de contexto, o `tJava` si se calcula en ejecución |

### Capa 3: la corriente

- **Dataset intermedio**: lo escribe un único grupo SAS del programa y solo lo leen grupos posteriores.
  No genera escritura ni lectura: el flujo pasa directo al consumidor.
- **Cadena fusionable**: `filter`, `compute`, `rename`, `select_columns` y `project` consecutivas se
  funden en un `tMap` (`merge_tmap`). El filtro va en `Output filter`; los cálculos y renombres en
  expresiones de columna; KEEP/DROP en el esquema de salida. Una operación que lee una columna que la
  misma cadena ya calculó no se funde: la cadena se parte.
- **Reparto**: un intermedio con dos o más lectores genera un `tMap` con una salida FLOW por lector.
  No se usa `tReplicate`: el catálogo del MCP no declara sus salidas y Studio rechaza esas conexiones.
- **Operación sola**: conserva su componente (p. ej. un `filter` sin otros cálculos sigue siendo
  `tFilterRow`; un `select_columns` solo, `tFilterColumns`). Son los casos excepcionales.
- **Conexiones**: `Main` desde la fuente de la cadena; en un `join`, `Lookup` para la segunda entrada;
  `OnSubjobOk` solo entre grupos sin datos en común.
- **Dedupe**: `PROC SORT NODUPKEY` y `NODUP` pasan a `tUniqRow` por clave única. NODUPKEY usa la clave del
  `BY`; NODUP compara todas las columnas, así que la clave queda pendiente, no inventada.

### Capa 4: estructura

Cada Job (principal o hijo) recomienda como máximo 3 pasos. Ya no hay `tPrejob`, `tPostjob`, `tWarn`
ni `tLogCatcher` recomendados: el aviso y el log son responsabilidad del Job, no pasos fijos.

## Contrato JSON de los campos nuevos

`JobPlan.not_migrated` es una lista de `NotMigrated`:

```json
{
  "category": "troceado_lotes",
  "lines": [10, 14],
  "what": "macro %troceo no se migra: troceado de tablas en lotes",
  "reason": "Reparte la carga en trozos para que el SAS no se quede sin memoria; no es lógica de negocio.",
  "talend_equivalent": "Talend carga el conjunto completo: el componente de salida usa Batch size o escritura por bloques."
}
```

| Campo | Significado |
| --- | --- |
| `category` | Familia de la fontanería (tabla anterior). |
| `lines` | Líneas SAS donde aparece. |
| `what` | Qué es, en español. |
| `reason` | Por qué no hace falta migrarlo. |
| `talend_equivalent` | Qué hace Talend en su lugar. Nunca vacío. |

`PlanStep.fused_from` es la lista de ids de las operaciones SAS que forman un `tMap` fusionado
(`fused_tmap`). Permite seguir un paso hasta el código SAS de origen.

`PlanStep.why` explica en una frase por qué existe el paso. Es obligatorio en los pasos recomendados.

El esquema completo está en `schemas/migration-plan.schema.json` (generado con
`JobPlan.model_json_schema()`).

## Ejemplo real: `p0_clientes_activos`

Antes (golden de `HEAD`): 11 pasos, uno por operación SAS.

```text
 1. Leer dwh.clientes                          por_determinar
 2. Renombrar columnas                         tMap
 3. Filtrar filas (WHERE estado='A' and ...)   tFilterRow
 4. Calcular columnas (IF/ELSE)                tMap
 5. Conservar/descartar columnas               tFilterColumns
 6. Conservar/descartar columnas               tFilterColumns
 7. Escribir stg.clientes_activos              por_determinar
 8. Leer stg.clientes_activos                  por_determinar
 9. Ordenar por cliente_id                     tSortRow
10. Eliminar duplicados                        por_determinar
11. Escribir stg.clientes_activos_ord          por_determinar
```

Después (`tests/golden/p0_clientes_activos.plan.md`): lectura, un tMap, `tUniqRow`, escritura y el `tDie`.

```text
1. Leer dwh.clientes                  por_determinar  (tFileInputDelimited como alternativa)
2. Transformar en un solo tMap        tMap            Output filter: estado == "A" && saldo > 0
                                                      Output columns: id → cliente_id
                                                      Expresión segmento: IF/ELSE → ternario Java
3. Eliminar duplicados                tUniqRow        UNIQUE_KEY = cliente_id
4. Escribir stg.clientes_activos_ord  por_determinar  (tFileOutputDelimited como alternativa)
5. Detiene el Job ante un error       tDie            OnComponentError desde la escritura
```

Lo que cambió: el filtro, los cálculos y los KEEP/DROP están en el mismo `tMap`, con su línea SAS en
cada expresión. El `SORT` previo al `NODUPKEY` se elimina porque `tUniqRow` conserva la primera fila por
clave; la nota de la golden lo indica para validar. Las pruebas de equivalencia siguen en el plan.

## Límites conocidos

- **Dos tuberías en la misma línea**: el IR toma `step = s{línea}`, así que dos `DATA`/`PROC` en una
  misma línea caen en un mismo grupo. Un grupo se trata como una cadena lineal, y los filtros de dos
  salidas distintas se pueden fundir en un único `AND`. Está reproducido pero **sin corregir**: un corte
  del grupo en cada lectura posterior a una escritura cambió el cableado del corpus real (duplicó
  reparto y conexiones, y el MCP rechazó `tFileInputDelimited_6`). Hace falta un id de paso por sentencia
  en el IR, no un corte en el planificador. Los programas con una sentencia por línea no se ven afectados.
- `call symputx` de un valor calculado en un DATA step se clasifica como `variables_control`: no genera
  paso y queda en `not_migrated`. Si la macro variable se usa después, debe revisarse que su valor llegue
  a un contexto del Job.

## Composición SQL (`migration_planner/sql_compose.py`)

Una sentencia `create table w as select ...` que solo lee la sentencia siguiente del programa no necesita
ser un paso propio: su consulta entra en la consumidora como CTE. `compose_items` se ejecuta en
`planner.plan_program` **antes** de `fold_elt` (el ELT necesita la consulta ya compuesta) y de `build_flow`.

- **Qué se compone:** cadenas de `create table ... as select` donde la intermedia tiene un único escritor y un
  único lector (R56 en `translation-rules.md`). Una cadena de tres sentencias da una consulta con dos CTE.
- **Dos niveles que deben coincidir:** el texto (`compose_statements`: CTE en orden de dependencias, referencias
  reescritas con un tokenizador que ignora literales y comentarios) y las operaciones IR (`compose_items`: las
  operaciones de la productora pasan a la consumidora con su mismo paso y evidencia, y la escritura de la
  intermedia desaparece). Así el ELT y la fusión ven un único grupo SQL.
- **Diccionario de funciones:** `rules/sas/sql-functions.json`. `portable` = SQL estándar; `translated` = equivalente
  por motor (se renombra al componer); `sas_only` = la sentencia no se compone. Las palabras clave de SQL no van
  en el diccionario.
- **Qué no se compone** (motivo en `not_migrated`, categoría `composicion_sql`, agrupado por motivo): funciones
  solo SAS, `calculated`, `into :x`, macro variables, `order by`/`intersect`/`except` en la productora, intermedias
  compartidas con otro programa o macro, un JOIN o UNION con tablas que no son todas de un mismo motor, y una
  escritura intermedia que cambia una tabla que la productora lee.
- **Medida (script de referencia de 24.801 líneas, sin LIBNAME de motor):** 350 sentencias `create table`; 130 intermedias
  con un único lector; 15 compuestas en el planificador; el resto, por JOIN en WORK (88), funciones solo SAS, o
  pass-through `connection to`. Pasos de nivel superior: 915 sin composición, 913 con ella (con hijos: 971 y 969).
  Sin LIBNAME de motor, el ELT (un solo Row por cadena) no se activa; ese es el caso en el que la composición
  reduce más pasos y no se da en ese script.
- **Límite conocido:** un JOIN dentro de una cadena WORK no se puede cablear: `build_flow` solo conecta un JOIN
  cuando es el primer paso del grupo. Hasta que el JOIN admita entrada desde la cadena, esas consultas quedan
  como pasos separados.

## Plegado de regiones largas repetidas

Después de la fusión a corriente y antes de repartir el Job (`fold_regions`, `migration_planner/regions.py`),
los tramos de pasos que se repiten con cualquier longitud a partir de 9 pasos se pliegan en un joblet: la
copia más larga conserva sus pasos y cada copia restante pasa a un paso de uso. Los detalles (huella,
parámetros, divergencias) están en [joblets.md](joblets.md#regiones-largas-repetidas-migration_plannerregionspy).

Decisión: el plegado va antes de `apply_structure` para que la partición en Jobs vea la secuencia ya
plegada. Los pasos de los joblets de ventana (`attach_joblets`) no entran en una región (ya tienen
`joblet_id`), y una copia que pierde todos sus pasos no genera ocurrencia en un joblet de ventana.

Medido en el programa grande de referencia: el Job principal pasa de 1.060 a 835 pasos reales y el plan
visible de 1.253 a 996 (con hijos). La métrica «pasos con joblets contados una vez» pasa de 579 a 627: el
cuerpo de la región largo cuenta entero, mientras que los joblets de ventana ya contaban cada familia
una vez, así que el plegado no ahorra en esa métrica. Está abierto decidir si se deja activo; para
desactivarlo basta quitar la llamada a `fold_regions` en `planner.plan_program`.

## ELT, copia de vuelta y transferencias remotas (reglas R45, R46, R23, R50, R04, R13)

Se aplican antes de `build_flow`, en `plan_program`:

- **ELT** (`migration_planner/elt.py`, `fold_elt`): un grupo SQL (un `create table`/`insert into` y sus
  lecturas, joins, filtros, agregados) cuyas tablas son todas de librerías del mismo motor con componente
  Row se sustituye por un único `sql_passthrough`. El componente es el Row del motor (tOracleRow...). Se
  omite si el SQL usa funciones o macro variables solo SAS (`monotonic`, `input`, `&`...). Los librefs se
  traducen al esquema del libname (`schema=`) cuando lo hay.
- **Lectura pass-through** (builder, `_passthrough_reads`): `from connection to <motor> (...)` produce una
  lectura con la consulta en QUERY (tOracleInput...).
- **Copia de vuelta** (`migration_planner/copy_back.py`, `fold_copy_back`): el bloque
  `data T; set X; ...; run; data X; set T; run;` se funde en una escritura en sitio sobre X. X se encadena
  como un intermedio. `build_flow` emite la escritura de un intermedio solo si ningún grupo posterior lo
  lee (si no, sería el sumidero final y perdería el resultado).
- **Transferencias** (`intermediate_representation/remote.py`): `proc export` a local + `proc upload` a la
  ruta remota se funden en una escritura directa a la ruta remota. `signon/rsubmit/waitfor/signoff` se
  registran como `sesion_remota` en `not_migrated` (el parser no emite operaciones para ellos).

Límites conocidos:
- Versiones (`migration_planner/versions.py`): cada escritura de un dataset es una versión nueva y cada
  lectura apunta a la vigente. Una reescritura en sitio se funde en el grupo que produce la versión que
  reescribe; las asignaciones que leen una columna ya calculada se sustituyen por su expresión (no hay
  sección Var). Una versión con más de 4 consumidores se materializa con tHashOutput/tHashInput (excepción
  a «sin tHash», solo para alto fan-out). Las expresiones que el traductor no soporta quedan pendientes
  dentro del tMap.
- El texto SQL de un `create`/`insert` (`details["sql"]`) no entra en la huella de los joblets
  (`repetition._POSITION_KEYS`): lo describen ya las operaciones de la consulta.
