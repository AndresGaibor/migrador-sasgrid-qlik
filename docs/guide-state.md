# Estado estructurado de la guía

Cada paso de un plan tiene un estado de guía (lo que el desarrollador hace con él) separado del
estado de decisión (`status`: propuesto, pendiente, verificado, validado_manualmente, descartado).

## Campos por paso (JSON de `JobPlan.steps[]` y `children[].steps[]`)

| Campo | Tipo | Significado |
| --- | --- | --- |
| `guide_status` | `"pending" \| "in_progress" \| "completed" \| "blocked"` | Estado de la guía. Por defecto `pending`. |
| `field_done` | `{ [nombre_campo: string]: boolean }` | Campos de la guía marcados como hechos. Vacío si no hay ninguno. |

Los dos campos los rellena el servidor al leer el plan (`load_plans`); no se escriben en
`plans.json`.

## Compatibilidad con el texto legado

Antes el estado se guardaba como texto en `note`, con el formato que escribe
`apps/web/src/guide-progress.ts`:

```text
[Estado de guía: pendiente|en_progreso|completado|bloqueado]
[Motivo de bloqueo: ...]
[Nota de trabajo: ...]
```

Cuando un paso no tiene estado estructurado, `guide_status` se lee del texto legado con esta
equivalencia:

| Texto legado | `guide_status` |
| --- | --- |
| `pendiente` | `pending` |
| `en_progreso` | `in_progress` |
| `completado` | `completed` |
| `bloqueado` | `blocked` |

Sin texto legado, se deriva del `status` de decisión: `verificado` o `validado_manualmente` →
`completed`; `descartado` → `blocked`; el resto → `pending`. La función es
`sas_grid_migrator.migration_planner.service.legacy_guide_status`.

Si el paso tiene estado estructurado guardado, ese valor gana sobre el texto legado. El campo
`note` no se modifica: la web puede seguir escribiéndolo mientras migra.

## Endpoint de escritura

```http
PATCH /api/projects/{project_id}/plans/{program}/steps/{step_id}/guide
Content-Type: application/json

{ "guide_status": "in_progress", "field_done": { "FILENAME": true } }
```

- Ambos campos son opcionales. Lo que no se envía se conserva.
- `field_done` se fusiona con lo guardado: las claves nuevas sobrescriben y las demás se conservan.
- Respuesta `200`: `{ "step_id", "guide_status", "field_done" }` (estado completo tras guardar).
- `422`: paso inexistente o `guide_status` fuera de los cuatro valores.
- Persistencia: tabla SQLite `guide_state` (clave `project_id, program, step_id`). Se borra con el
  proyecto.

## Relación con otros estados

- `guide_status` no cambia `status`, ni al revés. Marcar `completed` no equivale a `verificado`
  ni a `validado_manualmente`: la verificación en Studio y la equivalencia siguen siendo pruebas
  aparte.
- El estado de guía y el texto `note` se guardan por separado; regenerar el plan conserva ambos si
  el paso sigue existiendo.
