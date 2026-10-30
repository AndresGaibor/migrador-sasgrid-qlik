# Joblets propuestos

Un joblet es un bloque de componentes que se repite en el programa SAS (o en varias macros) y que
conviene crear una sola vez en Talend Studio para reutilizarlo. El planificador propone los joblets
en `JobPlan.joblets` y marca los pasos que los forman con `PlanStep.joblet_id`.

El portal solo propone; no crea ni modifica joblets en Studio.

## Cuándo se propone

- Un bloque es **repetido** si aparece en al menos `JOBLET_MIN_OCCURRENCES` sitios (2) y cada
  aparición tiene al menos `JOBLET_MIN_OPERATIONS` operaciones (3). Ambos umbrales están en
  `src/sas_grid_migrator/migration_planner/limits.py`.
- Hay dos orígenes de bloques:
  - **macro**: cada cuerpo de `%macro`. Las copias idénticas pegadas en el programa cuentan como
    apariciones (`kind: "macro"`); las variantes con el mismo nombre (`_v2`, `_v3`…) también.
  - **sequence**: pasos SAS consecutivos del programa principal (`kind: "sequence"`). Se elige el
    bloque que más pasos cubre (apariciones × pasos); un paso ya usado no entra en otro bloque.
- No se proponen bloques que solo orquestan (llamadas a macros, `%let`/`call symput`, `include`,
  comandos del sistema): no tienen lógica de datos que convertir.
- Tampoco se proponen macros de fontanería (troceo por lotes, esperas, conteos, control de
  errores, carga por comando). Son fontanería de SAS: no generan Job hijo ni joblet y quedan en
  `JobPlan.not_migrated`. Ver [pipeline-fusion.md](pipeline-fusion.md).
- Un bloque se compara por **forma**, no por texto: el mismo orden de tipos de operación, las mismas
  conexiones de entrada y salida, ignorando nombres de tablas y literales. Los espacios sobrantes
  no cuentan.

## Parámetros

- Cada dataset que cambia entre apariciones es un parámetro de tipo tabla (`tabla_entrada_N` o
  `tabla_salida_N`). Los datasets que no cambian siguen fijos en el joblet.
- Los literales que cambian (expresiones, columnas, condiciones) se agrupan en el menor número de
  parámetros posible: si todos se explican con un mismo reemplazo de palabras (p. ej. el alias
  `CUMPLE_NORMA_CTE` por `CUMPLE_NORMA_AHORROS` en cuarenta expresiones), ese reemplazo es **un**
  parámetro. Si no hay un reemplazo consistente, cada literal que cambia es un parámetro propio.

## Contrato JSON

`JobPlan.joblets` es una lista de `JobletPlan`:

```json
{
  "id": "joblet-01",
  "name": "jl_ConversionTipo",
  "title": "Conversión de tipo con input()/put() (5 apariciones)",
  "kind": "sequence",
  "occurrences": [
    {
      "job": "job_conversion_tipo_p01",
      "label": "pasos s2–s8",
      "step_ids": ["op_2_read_1", "op_2_compute_1", "..."],
      "values": {"expresion_var7": "VAR7", "expresion_30": "30", "columna_destino_nro_cta": "NRO_CTA"},
      "usage_steps": ["En job_conversion_tipo_p01, sustituye los componentes ... por el joblet jl_ConversionTipo.", "..."]
    }
  ],
  "parameters": [
    {"name": "expresion_var7", "context_variable": "context.expresion_var7", "example_values": ["VAR7", "VAR8", "VAR9"]}
  ],
  "components": ["por_determinar", "tMap", "por_determinar"],
  "inputs": ["tabla_entrada_1"],
  "outputs": ["tabla_salida_1"],
  "trigger_inputs": ["inicio"],
  "why": "El mismo bloque de 6 operaciones aparece 5 veces (...). Solo cambian 3 valor(es) ...",
  "creation_steps": ["Repository › Joblet Designs › clic derecho › Create Joblet.", "..."],
  "operation_count": 6
}
```

| Campo | Significado |
| --- | --- |
| `id` | Estable dentro del plan: `joblet-01`, `joblet-02`… (es el valor de `PlanStep.joblet_id`). |
| `name` | Nombre en Talend: `jl_<Rol>`. El rol es el nombre de la macro (`jl_Filtro`) o un rol de negocio (`ConversionTipo`, `Cruce`, `Filtro`…). Si choca, sufijo `_2`, `_3`. |
| `title` | Título legible en español. |
| `kind` | `"macro"` o `"sequence"`. |
| `occurrences[].job` | Job donde aparece: programa o parte (`job_part`) para secuencias; Job hijo para macros. |
| `occurrences[].label` | Origen: `pasos s2–s8` o `macro %x (línea 12)`. |
| `occurrences[].step_ids` | Pasos del plan que forman esta aparición. |
| `occurrences[].values` | Valor concreto de cada parámetro en esta aparición. |
| `occurrences[].usage_steps` | Cómo usar el joblet en el Job, en español. |
| `parameters[]` | `name`, `context_variable` (`context.<name>`) y `example_values` (hasta 5 valores distintos). |
| `components` | `component_candidate` de cada paso del bloque, en el orden del plan. Puede incluir `por_determinar`. |
| `inputs` / `outputs` | Nombres de los Input y Output (tablas de entrada y de salida). |
| `trigger_inputs` | Nombres de los Trigger Input. Hoy siempre `["inicio"]`. |
| `why` | Por qué se propone, en español. |
| `creation_steps` | Pasos en Studio para crear el joblet (Repository › Joblet Designs › clic derecho › Create Joblet, Input/Output/Trigger Input, contexto, uso). |
| `operation_count` | Operaciones por aparición. |

En cada `PlanStep` del plan (y de sus hijos), `joblet_id` es `null` o el `id` del joblet que lo
forma.

## Regiones largas repetidas (`migration_planner/regions.py`)

Los joblets de arriba solo ven bloques de hasta `JOBLET_MAX_WINDOW_STEPS` (8) pasos y dejan listados
todos los pasos de cada aparición. Las regiones largas se plegan antes, sobre la secuencia de pasos del
Job principal ya fusionada (`fold_regions`, después de `collapse_undefined_macros` y antes de
`apply_structure`, para que la partición en Jobs vea el plegado).

- **Huella por paso**: tipo de componente, tipo de operación, acción, forma de las conexiones (tipo y
  distancia al paso origen), forma abstracta de propiedades y expresiones (identificadores a `ID`,
  cadenas a `S`, números a `#`; palabras SAS se conservan) y número de columnas.
- **Búsqueda**: semillas de 5 pasos iguales, extensión hacia los dos lados con re-enganche de hasta 25
  pasos distintos (`REGION_MAX_GAP`) y comprobación con `difflib.SequenceMatcher`. Después se barren las
  posiciones que empiezan igual que el cuerpo, porque una copia con un paso extra no siempre entra por la
  extensión. Umbrales en `limits.py`: `REGION_MIN_STEPS` (9), `REGION_MIN_SIMILARITY` (0,85),
  `REGION_MAX_DIVERGENCE` (0,15), `REGION_MAX_PARAMETERS` (60).
- **Cuerpo y copias**: el cuerpo es la copia más larga. Sus pasos se quedan en el plan con `joblet_id`
  (cuentan una vez). Cada copia restante se sustituye por UN paso `Usa el joblet <nombre> (valores)`
  con `joblet_id`, `component_candidate` `por_determinar` y alternativa `Joblet`.
- **Parámetros**: un sub-token de identificador que cambia de forma consistente entre copias (p. ej. el
  segmento de negocio) es UN parámetro `identificador_<sub-token>`. Un literal que cambia es un parámetro
  por posición (`valor_pasoN_<campo>`). Un paso que solo está en algunas copias es un parámetro booleano
  `paso_opcional_N`. Si los reemplazos de sub-tokens no son coherentes entre copias, todo pasa a literal.
- **Divergencias**: una copia con pasos extra, o con pasos de otra forma, se avisa en `JobletPlan.why`
  («Divergencia entre copias») y en `JobPlan.unresolved`; el plan queda en `needs_review`.
- **Límites**: solo nivel superior (un joblet de región no se anida en otro); no entra en las copias
  dentro de macros (`children`); una variable de contexto usada solo en una copia puede quedar sin
  parámetro si no es un sub-token ni un literal de la posición.

Joblets de región y de ventana comparten el contrato JSON; `kind` es `"sequence"` en ambos.

## Qué no cubre

- No detecta bloques repetidos dentro de macros (solo el cuerpo completo de cada macro). Las
  repeticiones con pasos intercalados solo se ven si la alineación de regiones las encuentra
  (similitud >= 0,85).
- No decide si una variante `_v2` de macro es la que SAS usa en la ejecución: SAS usa la última
  definición compilada. La nota de la macro lo indica.
- Los componentes de cada paso son candidatos del planificador; un `por_determinar` sigue siendo
  una decisión pendiente, igual que fuera de un joblet.

## Métrica de pasos con joblets contados una vez

Un joblet cuenta sus pasos una vez: los del cuerpo más un paso por cada uso. Los pasos de las demás
apariciones que aún conservan sus pasos no cuentan. El helper `_counted_once` de las pruebas de
carga por transferencia implementa esta regla. La versión anterior contaba cada joblet como un único paso y daba cifras
optimistas.

Medido en el programa grande de referencia (24.801 líneas), con el plegado de regiones activo:

| Métrica | Sin plegado de regiones | Con plegado |
| --- | --- | --- |
| Pasos del plan visibles (Job principal + hijos) | 1.253 | 996 |
| Pasos reales del Job principal (sin recomendados) | 1.060 | 835 |
| Pasos con joblets contados una vez | 579 | 627 |

El plegado baja la lista visible y los pasos reales, pero sube la métrica «contados una vez»: los
joblets de ventana ya cuentan cada familia de copias una vez (en la primera aparición que encuentran),
y un cuerpo de región largo cuenta entero. El potencial medido de regiones de nivel superior es de unos
250 pasos ahorrados sobre 1.060; con criterios más laxos (huella gruesa, similitud 0,70) no sube. Ver
la nota de decisión en `pipeline-fusion.md`.
