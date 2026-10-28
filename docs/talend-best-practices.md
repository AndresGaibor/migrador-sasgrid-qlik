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
| `BP-SIZE-01` | warning | Más de 30 componentes en un Job | Dividir en Jobs hijo con `tRunJob` |

## Qué se espera de un Job migrado

- Todo lo que cambia por entorno va en contexto; el Job no se edita para pasar de Dev a Prod.
- Ninguna credencial dentro del Job.
- Una conexión de base de datos por Job y por base, con commit y cierre explícitos.
- Un fallo termina el Job con un mensaje (`tDie`) o queda registrado (`tLogCatcher`); nunca pasa en silencio.
- Jobs pequeños: lo que en SAS es una macro o un `%include` se convierte en un Job hijo.

## Estado actual del generador (fixtures SAS P0 y P1, Studio 8.0.1)

- Los pendientes de datos (rutas, esquemas, expresiones) se conservan en una variable de contexto `migration_todo_*` y
  no se escriben valores inventados, así que `BP-CTX-01` y `BP-SEC-01` no se disparan.
- El generador añade manejo de errores a cada Job con componentes (`error_handling` en `build_apply_spec`, activo
  en el API): un `tLogCatcher` conectado a un `tLogRow` en una fila propia, que registra cualquier fallo, y un
  `tDie` con mensaje "Fallo en el Job <nombre>" por `SUBJOB_ERROR` desde el primer componente de entrada sin flujo
  entrante. Studio solo admite ese enlace desde un componente que inicia un subjob (no desde un `tMap` ni un filtro),
  así que, si la lectura aún está por determinar y el Job no tiene un inicio así, solo se añade el registro.
  Con eso `BP-ERR-01` no salta en los Jobs generados.

## Pendiente de validar con el equipo

Estas reglas salen de la práctica general de Talend, no de una convención del cliente. Conviene contrastarlas con
la convención de nombres, carpetas y contextos que use el equipo, y ajustar los umbrales (por ejemplo, `MAX_COMPONENTS`).
