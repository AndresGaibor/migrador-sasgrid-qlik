# Validación en Talend Studio

**Estado: pendiente. No se declara equivalencia real.**

## Entorno detectado

- Producto en disco: Talend Studio Lite.
- Versión indicada en `.eclipseproduct`: `8.0.1.20260820_0911-patch` (patch `R2026-08v1`).
- Ruta instalada: `C:\Talend\8.0.1\studio`.
- Evidencia local: `C:\Talend\8.0.1\studio\.eclipseproduct` y el plugin de branding `org.talend.rcp.branding.generic_8.0.3.20260601_1447`.
- Fecha de inspección: 2026-10-19.
- Línea de documentación del catálogo: Talend Studio 8.0 R2026-09. La instalación detectada es R2026-08v1; no se presume paridad mensual.

## Ejecución y resultado

No se creó ni ejecutó un proyecto o Job de prueba, y no se verificó la disponibilidad de componentes, los parámetros en Studio ni el comportamiento en ejecución. La validación quedó bloqueada porque el runtime de automatización de escritorio requerido no pudo inicializar (faltaba la ruta de sus kernel assets) y los dispositivos de escritorio conectados estaban offline. Tampoco se confirmó el acceso a un workspace o licencia.

Por tanto, el resultado de Studio es **no ejecutado / pendiente**. Las referencias oficiales del catálogo y el smoke E2E de la web no sustituyen esta comprobación. No se afirma compatibilidad de ejecución ni equivalencia semántica del 100%.

## Casos para la siguiente ejecución

Cuando haya acceso interactivo a Studio y a un workspace de prueba, registrar captura y resultado por componente recomendado usado en las guías. Empezar por un caso de transformación `tMap` y uno de entrada/salida de archivo, anotar la versión exacta que muestra Studio, comprobar que los componentes aparecen en Jobs Standard, revisar las propiedades documentadas y ejecutar el Job con datos sintéticos. No importar ni generar archivos nativos `.item` desde esta validación sin un diseño aparte.
