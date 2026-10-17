# Informe de piloto

Fecha: 2026-10-17. Alcance: 50 programas reales de repositorios con licencia permisiva (ver `tests/fixtures/sas/real/SOURCES.md`) más 8 fixtures sintéticos. **No es un piloto con producción**: no había programas propios disponibles; sirve para medir cobertura y madurez, no para cerrar la migración de un cliente.

## Resultados (corpus real, 50 programas)

| Métrica | Valor |
| ------- | ----- |
| Sentencias | 7 139 (2 sin reconocer; 163 fragmentos de macro contados aparte) |
| Hallazgos | P1: 1 303 · P2: 219 |
| Constructos P0 más frecuentes | `data_step` 402, `macro_let` 346, `macro_call` 168, `macro_def` 80, `proc:sql` 75 |
| Datasets / aristas de datos | 358 / 15 (2 ciclos entre scripts de muestra que comparten nombres de tabla) |
| Elementos sin resolver | 429 (macros, includes y datasets dinámicos) |
| Tareas Grid detectadas | 6 (repositorio de banca/seguros con `sasgsub` y cabeceras Control-M) |
| Planes / pasos | 50 / 2 483 |
| Jobs `proposed` / `needs_review` | 2 / 48 |
| Pasos sin componente decidido (`por_determinar`) | 878 (35 %) |
| Pasos con pendientes | 2 261 (91 %) |

Componentes candidatos más usados: `tMap` 300, `tRunJob` 229, `tFixedFlowInput` 214, `tFileInputDelimited` 213, `tAggregateRow` 118.

## Lectura

- El parser cubre prácticamente todo el corpus; lo que falta no es sintaxis sino **información externa**: formato físico de los datasets, esquemas y librerías que solo existen en el entorno SAS. Por eso la mayoría de los pasos quedan con pendientes: es esperado.
- Los pasos de lectura/escritura dominan el trabajo humano; `tMap`/`tAggregateRow`/`tSortRow` salen con propiedades razonables para revisar.
- Un 35 % de pasos sin componente son lecturas cuyo origen no se puede deducir del código SAS (BASE vs base de datos).

## Limitaciones conocidas

- Sin servidor talend-mcp vivo (el clon revisado no arranca): ningún componente figura como `verificado`; los nombres de componente y propiedad son candidatos.
- Traducción de expresiones limitada a un subconjunto conservador; el resto queda `sin traducción automática`.
- No hay generación de `.item`, ejecución de SAS ni comparación de datos (por diseño).
- La orquestación Grid es inferida de scripts y macros; la planificación real (Control-M) solo se extrae de comentarios de cabecera.

## Rendimiento

Sobre 2 320 programas (40 copias del corpus, 21 MB): importación 0,6 s, análisis 17 s, dependencias 10 s, IR + planes 25 s. Crece algo más que linealmente; para lotes mayores conviene paralelizar el parseo por archivo.

## Siguiente paso recomendado

Ejecutar este flujo con 3–5 programas reales del cliente (uno por perfil P0/P1/P2), construir sus Jobs, validar con `docs/equivalence-testing.md` y ajustar `rules/mappings/talend-components.json` con los nombres reales de componentes y propiedades observados en esos Jobs.
