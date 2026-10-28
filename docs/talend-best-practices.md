# Buenas prácticas de Talend

El portal revisa cada Job aplicado contra estas reglas y las devuelve en `best_practices` del resultado de
aplicación (Job padre e hijos). Son recomendaciones: no cambian el estado `applied` o `partially_applied`.
Los errores de Studio se informan aparte, en `design_errors`.

Las reglas viven en `src/sas_grid_migrator/talend_adapter/best_practices.py`. Un identificador no se reutiliza ni
se cambia de significado.

| Regla | Severidad | Qué comprueba | Cómo se corrige |
| ----- | --------- | ------------- | --------------- |
| `BP-CTX-01` | warning | `FILENAME`, `DIRECTORY`, `HOST`, `PORT`, `DBNAME` o `URL` con un valor fijo | Variable de contexto (`context.nombre`), con un grupo por entorno (Dev, Test, Prod) |
| `BP-SEC-01` | error | `PASS`, `PASSWORD` o `PASSPHRASE` en claro | Variable de contexto de tipo contraseña; el mensaje nunca incluye el valor |
| `BP-DB-01` | warning | Dos o más accesos a base de datos sin un componente de conexión | `t<Base>Connection` al inicio, accesos con "usar conexión existente", y commit y cierre al final |
| `BP-ERR-01` | info | Job de dos o más componentes sin `tDie`, `tWarn`, `tLogCatcher`, `tStatCatcher`, `tFlowMeterCatcher`, `tAssertCatcher` ni conexión de error | Conexión `OnSubjobError` a `tDie` o `tWarn`, y `tLogCatcher` para registrar |
| `BP-SIZE-01` | warning | Más de 20 componentes en un Job | Dividir en Jobs hijo con `tRunJob` |
| `BP-NAME-01` | info | El nombre del Job no empieza por `job_` | Renombrarlo, por ejemplo `job_carga_clientes` |
| `BP-NAME-02` | warning | El Job o una carpeta suya se llama `tests`, `target` o `src` | Renombrarlo: con Git, esos nombres impiden subir los cambios |

## Fuente

Los umbrales y los nombres salen de la guía oficial de buenas prácticas del ciclo de vida de Talend
([Designing Jobs, Routes or Data Services](https://help.qlik.com/talend/en-US/software-dev-lifecycle-best-practices-guide/7.3/designing-jobs-routes-or-data-services)):
prefijos `job_`, `route_`, `service_`, `test_`, `pub_` y `task_`; nombres de componentes con significado; contextos para
conexiones, hosts y puertos y para pasar de Desarrollo a QA y Producción; "evita más de 20 componentes en un Job"; flujo de
izquierda a derecha y subjobs de arriba abajo; y la prohibición de `tests`, `target` y `src` como nombre de Job o de carpeta
en proyectos con Git. La guía no cubre el manejo de errores, el registro ni las conexiones a base de datos más allá de los
metadatos: esas reglas (`BP-ERR-01`, `BP-DB-01`) vienen de la práctica general de Talend.

## Qué se espera de un Job migrado

- Todo lo que cambia por entorno va en contexto; el Job no se edita para pasar de Dev a Prod.
- Ninguna credencial dentro del Job.
- Una conexión de base de datos por Job y por base, con commit y cierre explícitos.
- Un fallo termina el Job con un mensaje (`tDie`) o queda registrado (`tLogCatcher`); nunca pasa en silencio.
- Jobs pequeños (hasta 20 componentes): lo que en SAS es una macro o un `%include` se convierte en un Job hijo.

## Estado actual del generador (fixtures SAS P0 y P1, Studio 8.0.1)

- Los pendientes de datos (rutas, esquemas, expresiones) se conservan en una variable de contexto `migration_todo_*` y
  no se escriben valores inventados, así que `BP-CTX-01` y `BP-SEC-01` no se disparan.
- El generador añade manejo de errores a cada Job con componentes (`error_handling` en `build_apply_spec`, activo
  en el API): un `tLogCatcher` conectado a un `tLogRow` en una fila propia, que registra cualquier fallo, y un
  `tDie` con mensaje "Fallo en el Job <nombre>" por `SUBJOB_ERROR` desde el primer componente de entrada sin flujo
  entrante. Studio solo admite ese enlace desde un componente que inicia un subjob (no desde un `tMap` ni un filtro),
  así que, si la lectura aún está por determinar y el Job no tiene un inicio así, solo se añade el registro.
  Con eso `BP-ERR-01` no salta en los Jobs generados.

## Programas grandes

Un programa SAS de miles de líneas (por ejemplo, todos los ejemplos de un libro en un solo archivo) genera cientos de componentes
en un único Job. Studio tarda minutos en montarlo, la guía de Talend recomienda no pasar de 20 y, si agota el tiempo, el montaje
queda a medias. Por eso el API aplica dos controles, con `TALEND_MAX_COMPONENTS` (200 por defecto):

- **Por encima del tope, el Job se parte solo.** Los componentes se agrupan por conexión (un flujo de datos nunca se corta entre dos
  Jobs) y los grupos se empaquetan en Jobs hijo `<job>_p01`, `<job>_p02`… de hasta 17 componentes de trabajo, que con su manejo de
  errores quedan en 20. El Job padre pasa a ser una cadena de `tRunJob` unidos por `OnSubjobOk`, y cada hijo se lleva las
  instrucciones de sus pasos. `instructions.split` del padre lista los hijos.
- **Si un flujo conectado es mayor que el tope**, no se puede partir sin cortarlo: la vista previa marca `ready: false` y la aplicación
  responde 422 con el nombre y el tamaño del Job.

El tiempo que el portal espera a Studio crece con el tamaño: 30 s más 1,5 s por componente (padre e hijos).

## Pendiente de validar con el equipo

Estas reglas salen de la práctica general de Talend, no de una convención del cliente. Conviene contrastarlas con
la convención de nombres, carpetas y contextos que use el equipo, y ajustar los umbrales (por ejemplo, `MAX_COMPONENTS`).
