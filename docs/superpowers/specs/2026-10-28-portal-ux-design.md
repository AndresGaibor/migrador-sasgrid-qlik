# Mejora de UI/UX y utilidad del portal: diseño y hoja de ruta

Fecha: 2026-10-28. Estado: aprobado el alcance de la fase 1 por la persona dueña del repo; las demás fases se
diseñan cuando les toque (cada una es un subsistema con su propio diseño y plan).

## Intención

El portal hoy lleva a una persona de «ZIP con SAS» a «Jobs creados en Talend Studio», pero:

- los nombres de Job, carpeta y proyecto los decide el portal y no se pueden cambiar;
- el traductor de expresiones SAS → Talend no se ve ni se puede corregir;
- el flujo es lineal pero la interfaz son 7 pestañas sin una guía de «qué sigue»;
- lo que el SAS no trae (esquemas, destinos, formatos) no tiene dónde capturarse. `docs/automation-plan.md` lo identifica
  como el cuello de botella de la automatización.

El objetivo es que quien migra pueda **decidir y corregir desde el portal** (nombres, expresiones, políticas) y siempre sepa
**qué sigue**, sin que el portal invente valores (principio del README).

## Objetivos, no objetivos, anti-objetivos

- Objetivo: las 50 opciones de la propuesta del 2026-10-28, en el orden de las fases de abajo.
- No objetivo: ejecutar, compilar o publicar Jobs. El portal sigue creando y leyendo (`AGENTS.md`).
- No objetivo: reemplazar Talend Studio como editor de Jobs.
- Anti-objetivo: que una edición manual (nombre, expresión) deje al portal con un plan inconsistente: hijos que apuntan a
  un nombre viejo, hash de revisión que no cambia, o un renombrado que se pierde al regenerar guías.
- Anti-objetivo: que un valor sugerido se presente como dato. Las sugerencias llevan marca y requieren aceptación.

## Decisiones de diseño (mías salvo que se indique)

1. **Las ediciones humanas son capas sobre el plan, no cambios al plan.** Viven en SQLite (como `step_state`) y se
   superponen en `load_plans`. Así sobreviven a «Actualizar guías» y todo lo que consume el plan (preflight, apply, lote,
   exportaciones) las ve sin cambios. *Consecuencia*: nunca se escribe a `plans.json` un plan ya superpuesto.
2. **Plantilla de nombres global** (tabla de ajustes del portal), no por proyecto. Por defecto `job_{programa}`, que es lo
   que el código hace hoy. `docs/conventions.md` dice `<proyecto>_<programa>`; el código manda y el documento se corrige.
3. **Una expresión editada a mano conserva `requires_semantic_validation=True`.** Editar no la vuelve «más automática»;
   solo cambia el texto. Se marca `talend_edited` y se muestra la insignia «editada».
4. **Cada edición de expresión guarda el SAS original** y solo se aplica si coincide: si al regenerar cambia el orden de
   expresiones, la edición no cae en otra por error.
5. **Las ediciones se bloquean (409) mientras haya un lote o una creación de Talend activos**, porque cambian el hash de
   revisión que la persona ya confirmó.
6. **Renombrar un Job ya creado en Studio no lo renombra en Studio.** El portal avisa; el Job viejo queda y el nuevo se
   creará en la siguiente aplicación. (Renombrar en Studio sería una tool nueva del MCP: fuera de la fase 1.)
7. **Pendientes agrupados por texto exacto**, sin clasificar por palabras clave: es lo único que no inventa categorías.

## Hoja de ruta: las 50 opciones por fase

Numeración de la propuesta del 2026-10-28.

| Fase | Contenido | Opciones | Documento |
| ---- | --------- | -------- | --------- |
| **1** | Nombres + traductor visible + centro de mando | 1, 2, 3, 8, 9, 10, 19, 20 | `plans/2026-10-28-portal-ux-fase1.md` |
| 2 | Base de UI: partir `PlansTab.tsx`, tokens y modo oscuro, estados vacíos/errores, canal de eventos en vez de sondeos, accesibilidad | 48, 49, 50 | por escribir |
| 3 | Resto de nombres e identidad: carpeta destino, proyecto renombrable y con descripción, subjobs y etiquetas, tags y responsable, historial de cambios | 4, 5, 6, 7, 47 | por escribir |
| 4 | Traductor y decisiones: casos de ejemplo, diff SAS/Talend, pendientes en bloque, cobertura, interruptor del traductor, sugerencias | 11, 12, 13, 14, 15, 16 | por escribir |
| 5 | Entorno y políticas (WP5 y WP3 del plan de automatización): catálogo de entorno editable e importadores, política de reportes y de acción sobre tablas | 17, 18 | **diseño propio** |
| 6 | Navegación y flujo: búsqueda global, tarjetas de proyecto, re-subir ZIP con diff, duplicar, atajos, retomar, Plan en 3 pantallas, kanban | 21 a 28 | por escribir |
| 7 | Mesa de trabajo del Job: vista dividida SAS/Talend, diagrama, índice lateral, abrir en Studio, aplicar un Job con diff, notas e historial, casos de validación, asignación | 29 a 38 | **diseño propio** |
| 8 | Dependencias y análisis: grafo interactivo, ruta recomendada, mapa de calor, impacto, estimación de esfuerzo | 39 a 43 | por escribir |
| 9 | Exportar y reportar: informe ejecutivo, Excel/Jira y ZIP del servidor, enlace de solo lectura | 44, 45, 46 | por escribir |

**Por qué la fase 2 va antes que las demás:** las fases 3 a 7 tocan todas `PlansTab.tsx` (490 líneas con JSX de una sola
línea). Partirlo primero evita conflictos y hace cada fase más pequeña. La fase 1 no lo toca: su código nuevo va en
archivos nuevos y en `PlansTab.tsx` solo se añade el montaje de dos componentes.

**Dependencias:** 5 antes de 13 y 16 (necesitan el catálogo para proponer tipos); 3 antes de 47 (la auditoría registra
renombres); 7 después de 2; 44 y 45 después de 19 y 20.

## Fase 1: alcance exacto

| # | Qué entrega | Dónde se ve |
| - | ----------- | ----------- |
| 1 | Nombre del Job editable: identificador Java, ≤ 60 caracteres, único sin distinguir mayúsculas, con la carpeta destino a la vista | Cabecera de la guía del Job |
| 2 | Descripción del Job editable (va a la propiedad `description` del Job en Studio y a las exportaciones) | Cabecera de la guía y lista de Jobs |
| 3 | Renombrado masivo (prefijo, sufijo, buscar y reemplazar, regex) con tabla «antes → después» y errores por fila; se aplica todo o nada | Botón «Renombrar Jobs» en la lista del plan |
| 8 | Plantilla de nombres con `{proyecto}`, `{carpeta}`, `{programa}` y ejemplo en vivo; se aplica al generar guías | Configuración |
| 9 | Laboratorio del traductor: pegas SAS y ves Java de Talend, columnas, avisos y motor | Sidebar, ruta `#/traductor` |
| 10 | Editar la expresión traducida en cada paso, con «editada» y «volver a la traducción automática» | Tarjeta de paso |
| 19 | Barra de avance de 6 etapas y un botón «Siguiente acción» | Resumen del proyecto |
| 20 | «Qué falta»: pendientes agrupados por motivo, con los Jobs y pasos afectados y salto directo | Resumen del proyecto |

Fuera de la fase 1: cambiar la carpeta destino (opción 4), aceptar sugerencias (16), ejecutar el traductor sobre datos de
ejemplo (11), y renombrar en Studio.

## Restricciones

- Repositorio con trabajo ajeno sin commitear en `apps/api/main.py` y `src/sas_grid_migrator/persistence/store.py`
  (reintento de análisis, 2026-10-28). La fase 1 se ejecuta en un worktree desde `main` y se rebasa al final.
- Commits y push solo cuando la persona dueña lo pida (`AGENTS.md`).
- Si cambia el contrato con el MCP, va en los tres sitios (`AGENTS.md`, «Regla de oro»). La fase 1 no debería cambiarlo:
  `description` ya viaja en `to_mcp_arguments`.
- Textos de la interfaz en español, como el resto del portal.

## Qué queda a criterio de quien construya

Estilos visuales de los componentes nuevos (seguir `styles.css` y los componentes de `components/ui`); copy exacto de los
mensajes que no estén fijados en el plan; nombres internos de CSS.
