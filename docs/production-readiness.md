# Puesta en producción

Qué comprueba el portal antes de que un proyecto SAS llegue a Talend, cómo se verifica contra tu Studio y qué hacer cuando
algo falla. El objetivo: que un proyecto real se rompa **en estas puertas** y no al aplicarlo.

## Las tres puertas

| Puerta | Qué prueba | Necesita Studio | Dónde corre |
| ------ | ---------- | --------------- | ----------- |
| Pruebas unitarias e integración (`uv run pytest`, `bun test` en `mcp/talend-mcp`) | Reglas del generador, del adaptador y del MCP | No | CI en cada push |
| **Puerta del corpus** (`tests/integration/test_corpus_gate.py`) | Cada programa SAS del repositorio: invariantes del Job, `inputSchema` real del MCP y `dryRun` offline real | No | CI en cada push |
| **Proyectos hostiles** (`tests/integration/test_adversarial_projects.py`) | Nombres con acentos, espacios o 180 caracteres, carpetas `src`/`tests`/`target`, `%include` circular, archivos vacíos o binarios | No | CI en cada push |
| **Verificación en Studio** (`scripts/verify_in_studio.py`) | Aplica un proyecto de verdad y lee los problemas que marca Studio | Sí | A mano, antes de un despliegue |

### Invariantes de un Job (`tests/support/spec_invariants.py`)

Cada Job generado debe cumplir, para cualquier proyecto: nombre de Job y de componente válidos (identificadores), nombre de
Job de hasta 60 caracteres y único en el proyecto, carpeta bajo `Process/` sin `..`, sin segmentos `src`/`tests`/`target`
(con Git, Talend no sube los cambios) y de longitud acotada por los límites de ruta de Windows, nodos sin repetir,
conexiones entre nodos que existen, nombres de conexión y de variable de contexto únicos, pasos de instrucciones que apuntan
a componentes que existen, ninguna contraseña en claro y como mucho `TALEND_MAX_COMPONENTS` componentes por Job.

## Verificar un proyecto contra tu Studio

```bash
# Studio abierto con el Bridge instalado (bun run bridge:install en mcp/talend-mcp)
uv run python scripts/verify_in_studio.py ruta/a/los/sas --folder Process/VerificacionPortal
```

Importa la carpeta como un proyecto, la planifica, la aplica por el mismo flujo de lote que la interfaz y lee los problemas
de cada Job. Falla (código 1) si algún Job termina `failed` o `conflict`, o tiene un error de Studio que no sea un pendiente
esperado de un borrador (`must have at least one value`, `No schema has been defined yet`, falta de un módulo). Al terminar
borra de Studio los Jobs que creó (`--keep` los conserva). Código 2: no se pudo hablar con Studio.

Para que la verificación sea fiable, usa un Studio **recién reiniciado** o un proyecto de pruebas: Studio conserva en
memoria información de los Jobs que se crearon y borraron con el mismo nombre durante la sesión, y `job_problems` puede
devolver errores de un Job anterior (se vio con `job_02_load_accounts` tras decenas de pruebas seguidas; el mismo spec con
otro nombre salió limpio).

## Cómo se escribe un Job

1. **Offline primero** (`TALEND_APPLY_MODE=auto`, por defecto). El MCP escribe el `.item` y el `.properties` directamente: 0,2-0,3 s
   por Job frente a 4-9 s en vivo, y el Job nace sin los errores de `tMap`, `tFilterRow` o `tRunJob` que produce montar los
   nodos uno a uno por la API de Studio. Antes de escribir, el adaptador valida **todo el árbol** (el Job y sus hijos) con
   `dryRun`: si algo falla no queda nada a medias.
2. **Studio en vivo** solo si el Job lleva el `mapper` de un `tMap` (Studio lo configura al conectarlo) o si el offline falla;
   el resultado lleva entonces un aviso con el motivo. `TALEND_APPLY_MODE=live` fuerza siempre Studio en vivo.
3. Lo que el modo offline traduce con la definición de cada componente (el XML de tu instalación de Studio): el **valor** de las
   listas (`AND` → `&&`), el tipo de campo real, las filas de los parámetros `TABLE` (condiciones de `tFilterRow`), el valor por
   defecto de las listas que nadie pidió y el enlace de `tRunJob` con el id del Job hijo.
4. Un borrador cuyo componente no está en el catálogo local se omite con sus conexiones y se avisa; el resto del Job se crea.

## Límites y qué hacer cuando se alcanzan

| Situación | Qué ocurre | Qué hacer |
| --------- | ---------- | --------- |
| Programa de más de `TALEND_MAX_COMPONENTS` componentes (200) | Se parte solo en Jobs hijo de hasta 17 componentes unidos por `tRunJob` | Nada; si un flujo conectado es mayor que el tope, la vista previa lo marca `ready: false` y hay que dividir el programa SAS |
| Mismo nombre de Job en otra carpeta | El MCP lo rechaza (Talend exige nombres únicos) y el Job pasa a Studio en vivo, que lo informa como conflicto | Renombrar el programa SAS o aplicar en un proyecto Talend distinto |
| Ruta del workspace larga en Windows | Studio puede fallar al compilar con rutas de más de 260 caracteres | Activar las rutas largas de Windows o acortar `TALEND_APPLY_FOLDER`; las carpetas y nombres ya se acotan |
| Studio con la interfaz ocupada | El MCP espera a que se libere entre un Job y el siguiente y atiende los diálogos conocidos | Si persiste, cerrar editores (`talend_bridge_close_saved_editors`) o reiniciar Studio |

## Defectos que estas puertas ya cazaron

Cada uno tiene su prueba, para que no vuelva:

| Defecto | Cómo se manifestaba | Dónde se cubre |
| ------- | ------------------- | -------------- |
| `.item` offline con `xsi:type` sin declarar `xsi` (Jobs con `tMap`) | Studio: "Error when loading the job", un diálogo modal que **bloquea la interfaz**; al borrar el Job quedaba el `.item` huérfano | MCP: `prefijosSinDeclarar` rechaza escribirlo; corpus: `ElementTree` parsea todo lo escrito |
| `ProcessItem.property` apuntaba al `id` de la propiedad y no a su `xmi:id` | Studio no enlazaba el `.item` con el Job | `job-generator-robust.test.ts` y la puerta del corpus |
| Dos Jobs con la misma etiqueta en carpetas distintas | Talend exige nombres únicos; `job_problems` leía uno cualquiera | MCP: `createJobsFromTemplate` lo rechaza |
| `LOGICAL_OP: "AND"` escrito como nombre, no como valor (`&&`) | "has a value (AND) that doesn't exist" | `normalizar-parametros.test.ts` |
| `tRunJob` sin id del hijo | "Parameter (Trabajo) is empty but is required" | `enlazar-trunjob.test.ts` |
| Un Job sin componentes perdía sus variables de contexto | Se escribía vacío en silencio | `job-batch.test.ts` |
| Nombres de Job de 180 caracteres y carpetas `src`/`tests`/`target` | Rutas de Windows demasiado largas; Git no sube esos nombres | `test_naming.py` y `test_adversarial_projects.py` |
| Proyecto Talend recién creado, sin carpeta `process/` | `ENOENT` al enlazar `tRunJob` | `enlazar-trunjob.test.ts` |

## Operación

- **Memoria de Studio.** Tras muchas creaciones seguidas Studio retiene varios GB (llegó al 86 % de 4 GB) y la interfaz tarda en
  responder. `talend_studio_memory` (con `gc: true`) la muestra y fuerza una recolección; si sigue por encima del 70 %, reinicia
  Studio. Mide antes de una verificación larga.
- **No borres archivos de `process/` a espaldas de Studio.** Studio conserva el Job en memoria y puede devolver errores de un Job
  anterior con el mismo nombre. Borra desde Studio o con `scripts/verify_in_studio.py`, que además elimina por ruta lo que Studio
  deja.
- **Diálogos modales.** Un diálogo abierto (un error de carga, un aviso de red de Talend Cloud) bloquea la interfaz y todas las
  llamadas al puente fallan con "hilo de interfaz ocupado". Ciérralo antes de reintentar.
- Un Job escrito offline que Studio aún no ha cargado no se puede borrar desde Studio: refresca el workspace
  (`talend_bridge_refresh_workspace`) o bórralo desde el sistema de archivos.
- Los tests del MCP son herméticos (`mcp/talend-mcp/tests/setup.ts` apunta el puente a un puerto muerto): no dependen de que
  haya un Studio abierto ni de su estado.

## Qué no cubre

- **Equivalencia SAS ↔ Talend**: el portal no ejecuta SAS ni compara datos. Sigue siendo manual (`docs/equivalence-testing.md`).
- Los Jobs salen como **borradores** con pendientes (rutas, esquemas y expresiones SAS que el código no trae). Eso es esperado y
  queda como `partially_applied` con su explicación; no se afirma que estén listos.
- Compilar un borrador incompleto puede fallar: la puerta de Studio comprueba el diseño, no la compilación.
