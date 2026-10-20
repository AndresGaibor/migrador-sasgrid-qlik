<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/vertica/tverticacommit · versión 8.0 -->
# tVerticaCommit

Last updated: 9/30/2026

Commits in one go a global transaction using a unique connection instead of doing
that on every row or every batch and thus provides gain in performance.

## tVerticaCommit Standard properties

These properties are used to configure tVerticaCommit running in
the Standard Job framework.

The Standard
tVerticaCommit component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Component List | Select the component in which the relevant reused connection is configured. |
| Close Connection | Select this check box to close the database connection once the component has performed its task.  Clear this check box to continue to use the selected connection once the component has performed its task.  If this component is linked to your Job via a Row > Main connection, your data will be committed row by row. In this case, do not select the Close connection check box or your connection will be closed before the end of the first row commit. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tVertica\* components, especially with the tVerticaConnection and tVerticaRollback components.  Talend Studio and the Vertica database create very fast and affordable data warehouse and data mart applications. For more information about how to configure *Talend Studio* to connect to Vertica, see [Talend and HP Vertica Tips and Techniques](https://www.vertica.com/kb/Vertica-Integration-with-Talend-Connection-Guide/Content/Partner/Vertica-Integration-with-Talend-Connection-Guide.htm). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
