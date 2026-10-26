# Configuración global de Talend Studio

**Objetivo documental:** Talend Studio 8.0, versión R2026-09. **Fuentes oficiales consultadas:** 1 de octubre de 2026. Esta guía reúne las áreas globales y de proyecto del apéndice oficial; no sustituye la verificación de módulos/licencias instalados ni los pasos específicos por componente.

## Cómo distinguir los ajustes

- **Preferencias de Studio:** se abren en **Window → Preferences**. Qlik indica que varias preferencias se guardan como valores por defecto para Jobs nuevos.
- **Ajustes del proyecto:** se abren desde **Project Settings** o **File → Edit Project Properties**. Incluyen, entre otros, Palette, Job settings y Job version management; el conjunto completo puede importarse/exportarse como XML.
- **Workspace:** cambia la organización de la Palette y los paneles de Studio.

## Ajustes del proyecto

Personaliza los ajustes del proyecto actual en el árbol de **Project Settings**. Para trasladar el conjunto completo a otro proyecto, usa **Export** (genera XML) e **Import** (aplica el XML seleccionado).

[Customizing project settings — Talend Studio 8.0 R2026-09](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/customizing-project-settings) · actualizado 1 de octubre de 2026.

## Preferencias de Talend Studio

La página oficial de preferencias contiene estos 23 temas. Algunas preferencias corresponden a funcionalidades/productos concretos —por ejemplo, ESB, Metadata Bridge o Usage Data Collector— y pueden no aparecer en todas las instalaciones.

[Setting Talend Studio preferences — Talend Studio 8.0 R2026-09](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/setting-talend-studio-preferences) · actualizado 1 de octubre de 2026.

### Entorno y diseño

- [Java Interpreter path (Talend)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/java-interpreter-path-talend)
- [Changing the theme in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/changing-the-theme-in-studio)
- [Keeping perspective in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/keeping-perspective-in-studio)
- [Designer preferences (Talend → Appearance)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/designer-preferences-talend-appearance)
- [Palette preferences (Talend → Palette Settings)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/palette-preferences-talend-palette-settings)
- [Performance preferences (Talend → Performance)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/performance-preferences-talend-performance)

### Repositorios, proyecto y documentación

- [Artifact repository connection preferences](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/artifact-repository-connection-preferences-talend-artifact-repository)
- [Artifact repository for libraries preferences](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/artifact-repository-for-libraries-preferences)
- [Project reference preferences (Talend → Repository)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/project-reference-preferences-talend-repository)
- [Documentation preferences (Talend → Documentation)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/documentation-preferences-talend-documentation)
- [Metadata Bridge preferences (Talend → Import/Export)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/metadata-bridge-preferences-talend-import-export)
- [Language preferences (Talend → Internationalization)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/language-preferences-talend-internationalization)

### Componentes, ejecución y desarrollo

- [Changing specific component settings](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/how-to-change-specific-component-settings-talend-components)
- [Debug and Job execution preferences (Talend → Run/Debug)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/debug-and-job-execution-preferences-talend-run-debug)
- [Configuring remote execution](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/configuring-remote-execution-talend-run-debug)
- [Schema preferences (Talend → Specific Settings)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/schema-preferences-talend-specific-settings)
- [SQL Builder preferences (Talend → Specific Settings)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/sql-builder-preferences-talend-specific-settings)
- [REST Service preferences (Talend → ESB)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/rest-service-preferences-talend-esb)

### Seguridad, actualizaciones y telemetría

- [Configuring a custom Job artifact signature](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/configuring-custom-java-keystore-for-artifact-signature)
- [Configuring SSL in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/ssl-settings-preferences-talend-ssl)
- [Configuring update repositories](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/configuring-update-repositories)
- [Usage Data Collector preferences](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/usage-data-collector-preferences-talend-usage-data-collector)
- [Authentication-enabled HTTPS proxy for an Azure storage connection](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/setting-authentication-enabled-https-proxy-for-azure-storage-connection)

## Workspace y Repository tree

- [Customizing the workspace](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/customizing-workspace): disposición de Palette y paneles.
- [Filtering entries listed in the Repository tree view](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/filtering-entries-listed-in-repository-tree-view)
- [Displaying recently modified entries in the Repository tree view](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/displaying-recently-modified-entries-in-the-repository-tree-view)
- [Displaying favorite entries in the Repository tree view](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/displaying-favorite-entries-in-the-repository-tree-view)

## SQL, modelado y referencia

- [Using SQL templates](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/using-sql-templates)
- [SQL template writing rules](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/sql-template-writing-rules)
- [Regular expressions](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/regular-expressions)
- [Data synonym dictionaries](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/data-synonym-dictionaries)
- [Physical Data Model (PDM)](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/physical-data-model-pdm)
- [Talend Studio shortcuts](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/talend-studio-shortcuts)

## Índice oficial

El apéndice organiza las 12 áreas anteriores. Úsalo como índice para detectar cambios en una revisión futura:

[Appendices — Talend Studio User Guide 8.0 R2026-09](https://help.qlik.com/talend/en-US/studio-user-guide/8.0-R2026-09/appendices) · actualizado 1 de octubre de 2026.
