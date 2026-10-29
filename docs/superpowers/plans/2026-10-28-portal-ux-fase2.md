# Portal UX, fase 2: base de interfaz

**Spec:** [`docs/superpowers/specs/2026-10-28-portal-ux-design.md`](../specs/2026-10-28-portal-ux-design.md) (hoja de ruta de
las 50 opciones). Este plan cubre la fase 2: **48, 49 y 50**.

**Por qué esta fase va antes que las demás:** las fases 3 a 7 tocan `PlansTab.tsx`, que hoy tiene 539 líneas y JSX de una
sola línea. Partirlo primero evita conflictos en cada entrega siguiente. Los sondeos y los estilos repetidos se arreglan
una vez aquí y las fases posteriores heredan la base.

**Fuera de alcance:** cambiar la carpeta destino (4), renombrar en Studio, ejecutar o compilar Jobs, interruptor manual de
tema, rediseño visual. Esta fase no cambia ningún flujo de negocio.

## Estado de partida (verificado el 28/10/2026)

| Hecho | Dato |
| ----- | ---- |
| `apps/web/src/views/PlansTab.tsx` | 539 líneas, 15 funciones, varias con JSX en una sola línea de 300+ caracteres |
| Sondeos con `setInterval` | `ProjectsView` 2 s, `SummaryTab` 1,5 s, `PlansTab` 1,2 s (lote) y 1 s (verificación), `ProjectProcessingStatus` 1,5 s |
| Temas | Un solo `:root` claro; hay colores literales fuera de token (`#fff`, `#cdd3d6`, `#edf1ee`, `#59ac7d`) y `color-scheme: light` |
| Prueba de contrato del archivo | `apps/web/src/views/PlansTab.test.mjs` lee `PlansTab.tsx` como texto y busca allí 40+ cadenas |
| Diálogos | `components/Dialog.tsx` ya usa Radix: foco atrapado, `Escape` y devolución del foco resueltos |
| Suite | `bun test` 81 pruebas, `typecheck` y `build` en verde; `pytest` 680 pasan, 1 omitida y 1 fallo ajeno de catálogo |

## Decisiones

1. **Partición por responsabilidad, no por tamaño.** Los archivos nuevos son `plan-rows.ts` (lógica pura de filas),
   `PlanList.tsx`, `PlanDetail.tsx`, `PlanBatchPanel.tsx` (preflight, confirmación, progreso y filas del lote),
   `PlanSteps.tsx` (pasos, expresiones y verificaciones) y `PlanGrid.tsx`.
2. **La partición no cambia comportamiento.** Solo se mueven símbolos y se ajustan imports. Las 81 pruebas actuales son
   el contrato; ninguna aserción debe cambiar de significado.
3. **`PlansTab.tsx` queda como punto de entrada** de 20 líneas: decide lista o detalle. Nada más.
4. **Canal de eventos con respaldo.** Un `EventSource` por proyecto sustituye los tres sondeos de proyecto; si la conexión
   falla o el navegador no la soporta, se mantiene el sondeo actual. El progreso nunca se queda congelado.
5. **Modo oscuro por tokens y `prefers-color-scheme`**, sin interruptor manual: menos estado que sincronizar y ninguna
   preferencia nueva que persistir. El interruptor, si se pide, es una entrega aparte.
6. **Estados vacíos y errores con dos componentes** (`EmptyState`, `ErrorNotice`) que envuelven lo que hoy se repite a
   mano. `Load` se queda como está.
7. **La prueba `PlansTab.test.mjs` apunta a los archivos nuevos**; las cadenas que exige siguen siendo las mismas. Si una
   cadena se mueve de archivo, se mueve también la lectura, no la aserción.

## Tareas

### Task 1: Partir `PlansTab.tsx` sin cambiar comportamiento

**Files:**
- Create: `apps/web/src/views/plans/plan-rows.ts` (`real`, `visible`, `useDesktopLayout`, `PARENT_PATTERN`), `PlanList.tsx`,
  `PlanDetail.tsx`, `PlanBatchPanel.tsx`, `PlanSteps.tsx`, `PlanGrid.tsx`
- Modify: `apps/web/src/views/PlansTab.tsx` (queda solo `PlansTab`), `apps/web/src/views/PlansTab.test.mjs` (lee los
  archivos nuevos), imports en quien consuma `BatchJobRow` y `GridRecommendations` (hoy exportados desde `PlansTab.tsx`)
- Test: `apps/web/src/views/PlansTab.test.mjs` y la suite existente

**Interfaces:**
- `PlansTab({ id, file })` se conserva igual (lo monta `ProjectView`).
- `PlanList({ id })`, `PlanDetail({ id, file })` se exportan desde sus archivos.
- `PlanBatchPanel({ id, job, path, summary, preflight, batch, batchActive, ... })` recibe estado y callbacks; no llama a
  `useAsync` por su cuenta, para que el sondeo y el lote sigan viviendo en `PlanList`.
- Se conservan las exportaciones `BatchJobRow` y `GridRecommendations` con la misma firma desde sus archivos nuevos.

- [x] **Step 1:** Mover primero lo puro (`plan-rows.ts`) y comprobar `bun test src/views/PlansTab.test.mjs`.
- [x] **Step 2:** Mover `PlanGrid`, `PlanSteps` y `PlanBatchPanel`; ajustar imports; `bun test src/views`.
- [x] **Step 3:** Mover `PlanDetail` y `PlanList`; dejar `PlansTab.tsx` como entrada.
- [x] **Step 4:** Actualizar `PlansTab.test.mjs` para leer `PlanList.tsx`, `PlanDetail.tsx`, `PlanBatchPanel.tsx`,
  `PlanSteps.tsx` y `PlanGrid.tsx`; no cambiar ninguna aserción salvo la ruta del archivo.
- [x] **Step 5:** `cd apps/web && bun test && bun run typecheck && bun run build`. Expected: 81 pruebas, sin errores.
- [ ] **Step 6:** Commit `refactor(web): partir PlansTab en módulos por responsabilidad`.

### Task 2: Canal de eventos del proyecto (SSE)

**Files:**
- Modify: `apps/api/main.py` (ruta de eventos), `apps/web/src/api.ts` (URL del canal), `apps/web/src/hooks.ts` (hook de
  suscripción), `SummaryTab.tsx`, `PlansTab`/`PlanList.tsx`, `components/ProjectProcessingStatus.tsx`
- Create: `apps/web/src/project-events.ts` (hook `useProjectEvents`, con respaldo por sondeo)
- Test: `tests/unit/test_project_events.py` (detector de cambios puro), `apps/web/src/project-events.test.ts` (hook con
  `EventSource` falso y con `EventSource` ausente)

**Interfaces:**
- Python: `project_activity(store, project_id) -> dict` (procesamiento + lote + revisión) y
  `GET /api/projects/{id}/events` que emite `event: activity` con ese JSON y un `: ping` cada 15 s. Si el proyecto no
  existe, 404 antes de abrir el flujo.
- Web: `useProjectEvents(id, onChange: (activity) => void): { connected: boolean }`. Con `connected === false`, quien lo
  use programa su sondeo actual.
- El evento lleva un `revision` incremental; el hook solo llama a `onChange` cuando cambia, para no re-renderizar de más.

- [x] **Step 1:** Prueba del detector puro: dos instantáneas iguales no emiten; un cambio de estado de lote o de
  procesamiento sí.
- [x] **Step 2:** Implementar `project_activity` y la ruta SSE con `StreamingResponse` y `media_type="text/event-stream"`;
  documento `docs/agent-guide.md` actualizado con la ruta.
- [x] **Step 3:** Hook web con `EventSource`, cierre al desmontar y respaldo cuando `typeof EventSource === "undefined"`.
  La lógica pura (`parseActivity`) se prueba con `bun:test`; el hook no se renderiza en esta suite.
- [x] **Step 4:** Sustituir los sondeos de `SummaryTab`, `PlansTab` (lote y verificación) y `ProjectProcessingStatus`; el
  `ProjectsView` de 2 s se queda para otra entrega (es una lista, no un proyecto).
- [x] **Step 5:** `uv run pytest tests/unit/test_project_events.py -q`, `bun test`, `typecheck`. Expected: verde.
- [ ] **Step 6:** Commit `feat: canal de eventos del proyecto en lugar de sondeos`.

**Verificado a mano** (uvicorn + `curl -N`): el flujo responde `text/event-stream`, emite el primer evento al conectar,
emite otro con `revision` mayor al cambiar el estado y deja de consultar cuando el cliente cierra. El primer intento con
`request.is_disconnected()` antes del primer `yield` dejaba el flujo mudo: se sustituyó por la cancelación de Starlette.

### Task 3: Tokens y modo oscuro

**Files:**
- Modify: `apps/web/src/styles.css` (bloque `:root` con tokens semánticos, `@media (prefers-color-scheme: dark)`,
  reemplazo de literales), `index.html` si hace falta `meta name="color-scheme"`
- Test: `apps/web/src/theme.test.mjs` (lee `styles.css` y comprueba que no quedan colores literales en los selectores de
  superficie y que el bloque oscuro define los mismos tokens que el claro)

**Interfaces:** tokens nuevos `--surface`, `--surface-raised`, `--surface-soft`, `--border-strong`, `--focus`, `--on-accent`.
Los existentes (`--bg`, `--fg`, `--muted`, `--line`, `--panel`, `--accent`, `--ok`, `--warn`, `--bad`) se conservan con el
mismo nombre para no romper llamadas.

- [ ] **Step 1:** Prueba que falla: lista de tokens claro y oscuro debe coincidir y ningún selector de superficie usa
  `#fff` directo.
- [ ] **Step 2:** Añadir tokens y bloque oscuro; sustituir literales en `body`, `input`, `button.secondary`, `.panel`,
  `.sidebar`, `.app-header` y diálogos.
- [ ] **Step 3:** `bun test && bun run typecheck && bun run build`; revisar contraste de texto y de `:focus-visible` en
  ambos temas.
- [ ] **Step 4:** Commit `feat(web): tokens de superficie y modo oscuro por preferencia del sistema`.

### Task 4: Estados vacíos y errores unificados

**Files:**
- Create: `apps/web/src/components/EmptyState.tsx`, `apps/web/src/components/ErrorNotice.tsx`
- Modify: `apps/web/src/views/SummaryTab.tsx`, `PlansTab`/`PlanList.tsx`, `ExportTab.tsx`, `DepsTab.tsx`,
  `InventoryTab.tsx` (los `notice` y los vacíos escritos a mano)
- Test: `apps/web/src/components/EmptyState.test.tsx`

**Interfaces:** `EmptyState({ icon, title, children, action })` y `ErrorNotice({ title, error, onRetry })` con
`role="alert"` y el botón «Volver a intentar» deshabilitado mientras `loading`.

- [ ] **Step 1:** Prueba del marcado de ambos componentes (rol, título y acción).
- [ ] **Step 2:** Sustituir los vacíos repetidos; dejar intactos los mensajes con copy propio aprobado (por ejemplo, el
  aviso de «no se ejecutan ni se publican»).
- [ ] **Step 3:** `bun test && bun run typecheck`.
- [ ] **Step 4:** Commit `refactor(web): estados vacíos y errores con dos componentes`.

### Task 5: Accesibilidad pendiente

**Files:**
- Modify: `apps/web/src/views/plans/BulkRename.tsx` (tabla con `scope="col"`, foco al primer campo, `aria-describedby` del
  error), `NamingTemplateCard.tsx` (anuncio del ejemplo con `aria-live` ya presente; revisar que no se anuncie en cada
  tecla), `components/ui/dialog.tsx` (devolución del foco si Radix no la cubre), `styles.css` (objetivos táctiles de 44 px
  en móvil)
- Test: ampliar `BulkRename.test.tsx` y `NamingTemplateCard.test.tsx`

- [ ] **Step 1:** Pruebas de encabezados de tabla y del foco inicial en el diálogo.
- [ ] **Step 2:** Corregir lo que falte; comprobar `Tab` por el diálogo de renombrado y por la tarjeta de plantilla.
- [ ] **Step 3:** `bun test && bun run typecheck`.
- [ ] **Step 4:** Commit `fix(web): accesibilidad del renombrado y de la plantilla de nombres`.

### Task 6: Verificación y cierre

- [ ] **Step 1:** `uv run pytest -q` y `cd apps/web && bun test && bun run typecheck && bun run build`.
- [ ] **Step 2:** `uv run pytest tests/integration/test_mcp_contract.py -q` (no debe cambiar; esta fase no toca el MCP).
- [ ] **Step 3:** Revisión visual en escritorio y móvil con el entorno levantado: Resumen, lista de guías, detalle,
  Configuración y `#/traductor`, en tema claro y oscuro.
- [ ] **Step 4:** `docs/progress.md`: entrada de la fase 2 con cifras reales; marcar la fila 2 de la hoja de ruta.
- [ ] **Step 5:** Informar a la persona dueña (repos tocados, pendientes, sin push). Commit por tarea, no uno solo.

## Criterios de aceptación

1. `PlansTab.tsx` no pasa de 40 líneas y ninguna prueba cambia de significado.
2. Con el servidor de eventos caído, el progreso sigue actualizándose por sondeo y se avisa una sola vez.
3. El tema oscuro no deja texto ilegible ni superficies blancas; ningún token del bloque oscuro falta.
4. El diálogo de renombrado se puede recorrer con teclado y anuncia su error.
5. `bun test` ≥ 81 pruebas y `pytest` con el mismo resultado que hoy (salvo el fallo de catálogo, ajeno).
