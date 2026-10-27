# Diseño: checks automáticos de flujos Talend

**Fecha:** 2026-10-27
**Repositorios implicados:** `migrador-sasgrid-qlik` y `talend-mcp`

## Intención

Al crear un Job desde el portal, cada paso de su guía debe quedar marcado automáticamente cuando MCP confirme que la configuración correspondiente está realmente guardada en Talend Studio. El usuario no tendrá que marcar manualmente que añadió un componente o conectó un flujo.

## Situación actual

- El portal guarda el progreso de cada paso cuando alguien cambia el estado en la guía; el lote Talend registra éxito a nivel de Job y no actualiza esos pasos.
- El spec del portal no incluye el modelo `mapper` para `tMap`, aunque MCP ya acepta y aplica `mapper`. Por eso esas operaciones quedan como borradores.
- El éxito de la llamada de creación por sí solo no demuestra que cada flujo esté completo.

## Criterio de completado acordado

Un paso se marca **Verificado en Studio** solo después de leer de nuevo el Job y confirmar el componente esperado, sus parámetros y esquema, el mapper de `tMap` cuando corresponda, y sus conexiones esperadas. Esto comprueba la estructura guardada; **no compila ni ejecuta** el Job. Cambiar el ZIP/especificación invalida las verificaciones asociadas a la revisión anterior.

## Enfoques considerados

1. Marcar pasos como completos cuando la llamada de lote devuelve éxito. Es rápido, pero puede mostrar verde para un `tMap` vacío o para una conexión/esquema incompleto. Se descarta.
2. Configurar las transformaciones que el portal pueda traducir y conciliar cada paso contra el Job leído de Studio. **Enfoque elegido.** Conserva la evidencia por paso, deja pendientes las transformaciones ambiguas y no ejecuta Jobs.
3. Exigir compilación antes del check. No se elige porque el check solicitado mide configuración; la compilación depende también de librerías y del entorno. Puede mostrarse como una verificación aparte en otro cambio.

## Alcance del cambio

- El portal generará `mapper` para un subconjunto explícito y seguro de expresiones SAS (inicialmente asignaciones directas y aritmética simple), con nombres, tipos y expresiones de entrada/salida. No inventará claves ni semántica de joins.
- La identidad del paso SAS se conservará al asociarlo con el componente Talend y la conexión creada.
- Tras aplicar cada Job del lote, MCP/portal leerá el Job guardado y devolverá un resultado por paso: verificado o pendiente, con el motivo. La lista y el progreso de las guías se actualizarán automáticamente al avanzar el lote.
- El estado automático se guardará separado del progreso manual y de las notas existentes. La pantalla mostrará la fuente y la fecha de verificación.
- Al abrir la guía se mostrará de inmediato el último resultado guardado; no se bloqueará la pantalla esperando a Studio. La reconciliación automática ocurre después de aplicar cada Job. La acción existente para volver a comprobar permitirá actualizar el estado bajo demanda.
- Si una lectura falla por falta de conexión, el Job queda como **No verificable** para la revisión actual y no se cuenta como confirmado; se conserva el detalle técnico para reintentar. No se interpreta un fallo de comunicación como evidencia de que Studio borró o cambió el Job.
- El progreso automático contará solo pasos confirmados por lectura de Studio. Las marcas manuales y sus notas se conservan por separado y no se presentan como comprobaciones automáticas.
- Las operaciones no traducidas, los mappers sin configuración y los conflictos no se marcarán completos. Seguirán visibles con una explicación accionable.

## Fuera de alcance

- Ejecutar los Jobs o publicar en Qlik Talend Cloud.
- Marcar un flujo completo solo porque exista el Job, por un recuento de componentes o por una revisión manual.
- Traducir automáticamente cualquier programa SAS o resolver sin datos las conexiones de producción.

## Restricciones y riesgos

- La revisión debe ser de solo lectura después de aplicar; no debe reescribir un Job abierto ni competir con Studio al guardar.
- El estado se liga al proyecto, programa, paso y hash de la especificación. No se reutiliza una marca de una revisión anterior.
- La primera versión solo puede marcar automáticamente los patrones SAS que generen un mapper y una configuración que MCP pueda verificar; otros patrones quedan pendientes en lugar de falsamente verdes.
- El progreso manual y las notas ya guardadas deben conservarse y no confundirse con la verificación automática.

## Criterios de aceptación

1. Después de crear el ZIP de prueba, el portal va marcando automáticamente los pasos de cada Job que MCP aplicó y Studio confirmó mediante lectura posterior.
2. El `tMap` aritmético de la prueba se configura desde el spec y solo se marca cuando sus expresiones y esquema aparecen en el Job leído.
3. Una operación faltante, un enlace ausente o una transformación no soportada permanece pendiente con su motivo; no se marca el Job como completamente verificado.
4. La actualización del progreso no ejecuta los Jobs, no borra notas y no convierte verificaciones manuales anteriores en automáticas.
5. La guía muestra que el check significa “configurado y verificado en Studio”, separándolo de compilación y ejecución.
