# SAS Grid: soporte, análisis y migración

Esta guía reúne el comportamiento que el proyecto reconoce hoy, las referencias para verificar
SAS Grid y una lista práctica para preparar una migración. No es una guía de administración de
SAS Grid ni afirma que los comandos de cada instalación sean intercambiables.

## Resumen ejecutivo

- El proyecto analiza estáticamente SAS y scripts; **no ejecuta** SAS, SASGSUB, comandos del
  sistema operativo ni tareas del scheduler.
- El análisis de Grid trata de reconstruir **orquestación** (qué programa se envía, en qué orden,
  con qué condición y parámetros). No equivale a convertir la lógica de datos del programa.
- La versión y el proveedor Grid del entorno objetivo no están identificados en este repositorio.
  Las recomendaciones del catálogo siguen siendo parciales, salvo detecciones explícitamente no
  soportadas.
- El catálogo contiene 10 patrones de prueba: 7 `partial` y 3 `unsupported`; 0 `supported`. Los
  conteos son patrones, no porcentaje de compatibilidad con SAS Grid.
- La referencia consultada es *Grid Computing in SAS 9.4, Fifth Edition*. Sus reglas no deben
  atribuirse automáticamente a SAS Viya, a todas las versiones 9.4, ni a cualquier scheduler.

## Referencia oficial descargada

El PDF se conserva solo en la máquina local en
`docs/reference/sas/gridref-9.4-fifth-edition.pdf`; Git lo ignora por copyright. Consulta el
[índice local de referencias](reference/sas/README.md) si el archivo no está en tu clon. La descarga
es el documento oficial de SAS:

- [Página oficial y tabla de contenido](https://go.documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/gridref/titlepage.htm)
- [PDF oficial](https://documentation.sas.com/api/docsets/gridref/9.4/content/gridref.pdf?locale=en)
- Copia local: *Grid Computing in SAS 9.4, Fifth Edition*, 374 páginas.
- Descargada el 28-10-2026; SHA-256: `03754A5123020617EACD0D314366D5B6736E43DF1C025F3F2ACA949DEFE817F7`.

La guía versionada aquí resume solo lo necesario para el proyecto; consultar el manual para
configuración, permisos, topología y opciones completas. Secciones útiles por página impresa:

| Tema | Sección del manual | Páginas impresas |
| --- | --- | ---: |
| Arquitectura y conceptos SAS Grid | Parte 1, capítulos 1–2 | 1–58 |
| Administración y monitoreo | Parte 2, capítulos 3–5 | 59–116 |
| SAS Grid Manager for Platform / LSF | Parte 4, capítulos 8–10 | 167–218 |
| Grid Manager for Hadoop | Parte 5, capítulo 11 | 219–242 |
| Uso de SASGSUB | Capítulo 13 | 243–268 |
| Reinicio y recuperación | Capítulo 15 | 279–284 |
| Comandos SASGSUB | Capítulo 17 | 305–327 |
| Opciones por proveedor | Apéndices 1–3 | 329–340 |

Los números son los impresos en el manual (no el índice de página del lector PDF). La paginación o
el contenido pueden cambiar en otras ediciones.

## Conceptos que conviene separar

1. **Programa SAS:** el código que procesa datos. Su semántica se analiza en el parser, IR y
   planificador de migración; requiere pruebas de equivalencia propias.
2. **SASGSUB:** utilidad cliente de SAS Grid Manager para enviar programas, comandos o sesiones,
   revisar estado, recuperar resultados y terminar trabajos. Puede seguir procesando aunque el
   cliente que envió el trabajo ya no permanezca activo (manual, pp. 305–306).
3. **Proveedor Grid:** determina opciones de recursos y colas. El manual distingue SAS Workload
   Orchestrator, SAS Grid Manager for Platform (integrado con LSF) y SAS Grid Manager for Hadoop.
   Sus opciones no son una sintaxis universal.
4. **Scheduler externo:** por ejemplo Control-M o LSF llamado directamente desde scripts. Una
   etiqueta o comentario con su nombre no constituye la definición ejecutable del calendario,
   dependencias, alertas o reintentos.
5. **Talend:** la migración puede representar programas como Jobs hijos y dependencias como
   orquestación, pero hay que validar explícitamente condiciones, parámetros, fallos, reintentos,
   calendario y manejo de resultados en la plataforma objetivo.

## SASGSUB: referencia breve para analizar scripts

La forma documentada para enviar un programa en batch es, de forma esquemática:

```text
SASGSUB -GRIDSUBMITPGM <programa.sas> [argumentos comunes] [argumentos batch] [opciones Grid]
```

La sintaxis completa depende de argumentos comunes, batch y Grid Job; no es una gramática de
shell completa. No ejecutar ejemplos de esta guía sin cotejarlos con el `sasgsub.cfg`, versión,
plataforma y política del entorno destino.

| Forma | Significado documentado | Consecuencia para migración |
| --- | --- | --- |
| `-GRIDSUBMITPGM archivo.sas` | Envía un programa SAS en batch. La ruta tiene restricciones documentadas (manual, p. 307). | Resolver ruta, dependencias y ubicación compartida/staging; el analizador solo busca candidatos estáticos. |
| `-GRIDJOBNAME nombre` | Nombre visible del trabajo; por defecto se usa el nombre del programa (p. 325). | Puede servir como evidencia/etiqueta, no define por sí solo un Job Talend ni una clave estable. |
| `-GRIDJOBOPTS "queue=..."` | Pasa opciones al proveedor Grid; opciones y valores dependen del proveedor (p. 325 y apéndices 329–340). | Identificar el proveedor antes de interpretar `queue`, recursos, prioridad o reintentos. |
| `-GRIDOPTSET conjunto` | Selecciona un Grid Options Set (p. 325). | Obtener su configuración efectiva y sus overrides; el texto del script puede no contener todos los valores. |
| `-GRIDWAIT` | Espera que termine el trabajo; no devuelve resultados y conserva el directorio (p. 324). | Modelar sincronización y timeout/fallo, no solo una flecha entre Jobs. |
| `-GRIDWAITRESULTS` | Espera y devuelve resultados, incluido directorio, log y listing (p. 324). | Definir dónde se guardan/consumen los resultados y quién los limpia. |
| `-GRIDWAITLOGLIST` / `-GRIDWAITNORESULTS` / `-GRIDWAITRESULTSNOLOG` | Espera y varía recuperación y eliminación de archivos/directorio (pp. 324–325). | No dar por equivalentes distintas políticas de retención. |
| `-GRIDWAITTIMEOUT n` | Limita la espera, en segundos, cuando se usa con las opciones de espera indicadas (p. 324). | Traducir como timeout solo después de verificar política, acción al vencer y estado final del trabajo. |
| `-GRIDWATCHOUTPUT` | Muestra salida durante el monitoreo; terminar el cliente no necesariamente termina el job (p. 325). | Distinguir desconexión/observación del cliente de cancelación del proceso remoto. |
| `-GRIDWORK`, `-GRIDWORKREM`, `-GRIDFILESIN`, `-GRIDSTAGECMD`, `-GRIDSTAGEHOST` | Controlan directorio de trabajo compartido y/o staging de archivos (pp. 323–324). | Inventariar archivos, rutas, permisos y estrategia de staging; no asumir filesystem compartido. |
| `-GRIDRESTARTOK` | Permite reejecución/reinicio en escenarios configurados; los detalles dependen de provider/queue (p. 307 y capítulo 15). | Identificar idempotencia, checkpoints, efectos parciales y política real de reintentos. |

### `-GRIDQUEUE` y `queue=...` no son la misma forma

En la edición citada, `-GRIDQUEUE` no aparece como argumento SASGSUB en la sintaxis del capítulo
17. El manual sí documenta `-GRIDJOBOPTS` y muestra `queue=...` como opción del proveedor. Por
ejemplo, distingue `queue` para SAS Workload Orchestrator (p. 330) de `queue` para Platform/LSF
(p. 334), con defaults y semánticas diferentes. Esto **no demuestra** que `-gridqueue` sea
inválido en todas las versiones o wrappers locales; significa que no se debe tratar como opción
confirmada de SASGSUB sin identificar producto, versión y capa de wrapper.

El fixture `tests/fixtures/sas/grid/ejecutar_lote.sh` mantiene formas ilustrativas. No se cambió
automáticamente: primero hay que obtener ejemplos sanitizados del entorno real.

## Estado de soporte del proyecto

La fuente de verdad es [`rules/sas/grid_catalog.json`](../rules/sas/grid_catalog.json); cada patrón
se prueba con fixtures y el analizador de `src/sas_grid_migrator/grid_analysis/analyzer.py`.

| Patrón del catálogo | Estado | Qué se conserva | Qué falta validar |
| --- | --- | --- | --- |
| `sasgsub.submit` | `partial` | Programa y evidencia de línea. | Sintaxis real, variables/rutas y dependencias de despliegue. |
| `sasgsub.job_options` | `partial` | Nombre, queue/wait reconocidos por el parser actual. | Formas reales y proveedor; especialmente `-gridqueue` ilustrativo. |
| `sasgsub.unverified_options` | `unsupported` | Detección de variantes de opciones sin asignarles semántica. | Producto, versión y traducción de cada opción. |
| `sasgsub.missing_option_value` | `unsupported` | Opción incompleta y su ubicación. | Valor original; nunca inferirlo. |
| `sasgsub.set_parameters` | `partial` | Parámetros literales simples. | Expansión de shell/macros, espacios y conexión con contextos Talend. |
| `sas_batch.sysin` | `partial` | Invocación SAS batch y programa candidato. | Runtime, opciones, dependencias y semántica de parámetros. |
| `sas_macro_step.include_dispatch` | `partial` | Dispatch macro estáticamente resoluble. | Defaults, valores dinámicos y efectos laterales. |
| `shell.inferred_sequence` | `partial` | Orden y condición simple de éxito en casos probados. | Ramas, subshells, `set -e`, retries, traps y manejo de errores general. |
| `scheduler.control_m` | `partial` | Comentario/cabecera de calendario como evidencia. | Export/definición autoritativa del scheduler; no se parsea Control-M. |
| `scheduler.lsf` | `unsupported` | Detección de `bsub`/`bjobs`. | Opciones, IDs, estados, dependencias y semántica del LSF destino. |

`partial` significa que una forma de fixture se analiza con cautela, no que el caso esté listo
para producción. `unsupported` significa detección sin conversión automática segura.

## Qué no se deduce del texto del script

Pedir también configuración/documentación operativa: un script puede heredar valores de
`sasgsub.cfg`, servidor lógico Grid, Grid Options Set, configuración de queue, perfil del usuario,
variables de entorno, macros, sistema de archivos compartido o scheduler externo. Confirmar como
mínimo:

- versión exacta de SAS 9.4 (incluido maintenance release) y cliente SASGSUB;
- proveedor Grid instalado/activo y versión: SAS Workload Orchestrator, Platform/LSF, Hadoop u
  otro wrapper;
- sistema operativo del cliente y de los nodos; rutas compartidas, mapeos y staging;
- configuración efectiva de `sasgsub.cfg`, servidor lógico, options sets, queue y overrides;
- credenciales, identidad efectiva, permisos y acceso a datos/secretos (sin exportar secretos);
- definición exportada del scheduler externo y calendarios, zona horaria, festivos y SLA;
- política de retorno, códigos SAS, estados, timeout, cancelación, alerta, reintento y requeue;
- archivos de entrada/salida, ubicación, retención, limpieza, logs y ownership;
- `SYSIN`, `SYSPARM`, `-SET`, `-GRIDSASOPTS`, macros, variables de shell y valores dinámicos;
- locks, checkpoints, restartability, idempotencia y efectos externos de ejecutar dos veces;
- límites de recursos (queue, prioridad, CPU, memoria, tiempo) y restricciones de concurrencia.

Solicitar ejemplos sanitizados; retirar nombres de host/usuario, credenciales, rutas sensibles,
datos personales y parámetros secretos. No subir salidas o logs de producción al corpus de pruebas.

## Procedimiento recomendado para migrar una cadena Grid

1. **Inventariar sin ejecutar:** recopilar scripts, programas SAS referenciados, includes, macros,
   configuraciones y definición de scheduler; guardar ruta y hash del origen.
2. **Confirmar el entorno:** llenar la lista anterior con evidencia del administrador SAS/Grid y del
   scheduler. Registrar de qué fuente proviene cada dato y marcar incógnitas.
3. **Reconstruir el grafo:** identificar tareas, orden, dependencias por éxito/fallo, parámetros,
   artefactos intercambiados, calendarios y ramas. Revisar manualmente toda inferencia de shell.
4. **Separar procesamiento y control:** migrar la lógica SAS de cada programa en su Job; modelar
   dependencias entre Jobs en el orquestador objetivo. Una dependencia Grid no es conexión de filas.
5. **Diseñar el contrato del Job:** documentar contextos de entrada, outputs, códigos/estados,
   idempotencia, archivos, timeout, retry, cancelación, notificaciones y credenciales seguras.
6. **Comparar ejecución controlada:** usar datos sintéticos o una copia autorizada y no productiva;
   cotejar recuento, esquema, valores, errores, outputs, orden, reintentos y recuperación. No afirmar
   equivalencia por el hecho de que ambos Jobs terminen con éxito.
7. **Revisar operación y rollback:** validar scheduler, permisos, carga, observabilidad, ventana,
   coexistencia/rollback y aprobación del responsable antes de producción.

Para equivalencia del procesamiento, seguir además
[`equivalence-testing.md`](equivalence-testing.md); para construcciones SAS,
[`sas-coverage.md`](sas-coverage.md). El analizador de Grid no reemplaza esos controles.

## Cómo aportar cobertura al repositorio

1. Añadir un fixture pequeño y sanitizado a `tests/fixtures/sas/grid/` que muestre una sola forma
   nueva, con comentario de prioridad y procedencia/versión.
2. Añadir o ajustar un ID en `rules/sas/grid_catalog.json`; actualizar conteos y límites.
3. Agregar pruebas del parser/análisis que validen campos y evidencia de línea. Incluir variantes
   incompletas, quoting, continuaciones y errores si son pertinentes.
4. No convertir la categoría a `supported` hasta que la sintaxis esté confirmada para una versión
   nombrada, el análisis se pruebe end-to-end y la recomendación se valide con el comportamiento
   destino.
5. Conservar el PDF/documentos protegidos solo localmente; versionar únicamente notas propias,
   enlaces, citas breves necesarias y fixtures de autoría del proyecto.

## Fuentes

- SAS Institute, [*Grid Computing in SAS 9.4, Fifth Edition*](https://go.documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/gridref/titlepage.htm), en particular capítulo 17 y apéndices 1–3.
- [PDF oficial de SAS](https://documentation.sas.com/api/docsets/gridref/9.4/content/gridref.pdf?locale=en); descarga local opcional descrita en [`docs/reference/sas/README.md`](reference/sas/README.md).
- Contrato implementado: [`rules/sas/grid_catalog.json`](../rules/sas/grid_catalog.json), [`analyzer.py`](../src/sas_grid_migrator/grid_analysis/analyzer.py) y fixtures en [`tests/fixtures/sas/grid/`](../tests/fixtures/sas/grid/).
- Estado del proyecto y pendientes: [`docs/progress.md`](progress.md), [`docs/architecture.md`](architecture.md).
