"""Umbrales y familias de componentes que comparten el planificador y las buenas prácticas.

Fuente única: `best_practices.check_job_arguments` y `job_structure` importan de aquí; no
dupliques estos valores en otros módulos.
"""

import re

# Máximo de componentes por Job, pasos recomendados incluidos. La guía de Talend habla de
# "evita más de 20"; el portal usa 25 como umbral de partición (antes 20 en best_practices).
MAX_COMPONENTS_PER_JOB = 25

# Pasos recomendados por Job (conexión y cierre si hay base de datos, error, conteo). Como máximo
# tres: el resto se descarta en job_structure (la traducción de SAS no se llena de infraestructura).
MAX_RECOMMENDED_PER_JOB = 3

# Reserva por Job para pasos recomendados al repartir pasos en Jobs hijos.
INFRA_RESERVE = MAX_RECOMMENDED_PER_JOB

# Joblets (bloques repetidos): un bloque se propone como joblet si aparece en al menos
# JOBLET_MIN_OCCURRENCES sitios distintos y cada aparición tiene al menos JOBLET_MIN_OPERATIONS
# operaciones. JOBLET_MAX_WINDOW_STEPS limita cuántos pasos SAS consecutivos se comparan a la vez.
JOBLET_MIN_OCCURRENCES = 2
JOBLET_MIN_OPERATIONS = 3
JOBLET_MAX_WINDOW_STEPS = 8

# Regiones largas repetidas (`regions.py`): tramos de pasos del Job principal que se repiten con
# cualquier longitud, tolerando pequeñas divergencias entre copias.
# Longitud mínima de una región, en pasos. Los bloques de hasta JOBLET_MAX_WINDOW_STEPS los ve ya
# `joblets.py` (ventanas); por eso la región empieza justo después para no pisar esa detección.
REGION_MIN_STEPS = JOBLET_MAX_WINDOW_STEPS + 1
REGION_MIN_OCCURRENCES = 2  # copias mínimas
REGION_MIN_SIMILARITY = 0.85  # similitud mínima de cada copia con el cuerpo (1 - divergencia)
REGION_MAX_DIVERGENCE = 0.15  # divergencia máxima tolerada al extender una alineación
REGION_MAX_GAP = 25  # pasos distintos que puede saltar una alineación para volver a coincidir
REGION_SEED_STEPS = 5  # pasos iguales consecutivos que siembran una alineación
REGION_MAX_SEED_OCCURRENCES = 40  # semillas más frecuentes que esto son genéricas: se ignoran
REGION_MAX_PARAMETERS = 60  # más parámetros que esto: la región no se pliega

DATABASE_FAMILIES = (
    "DB|Mysql|Oracle|Postgresql|Mssql|Teradata|Snowflake|Redshift|Vertica|Netezza|"
    "Db2|Informix|Sybase|MariaDB|SingleStore|Greenplum|Impala|Hive"
)
DATABASE_ACCESS = re.compile(
    rf"^t(?:{DATABASE_FAMILIES})(?:Input|Output|Row|SP|BulkExec|OutputBulk|OutputBulkExec)$"
)
DATABASE_CONNECTION = re.compile(rf"^t(?:{DATABASE_FAMILIES})Connection$")
DATABASE_CLOSE = re.compile(rf"^t(?:{DATABASE_FAMILIES})Close$")
