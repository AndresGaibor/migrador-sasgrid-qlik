<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/postgresql/tpostgresqlcommit · versión 8.0 -->
# tPostgresqlCommit

Last updated: 9/30/2026

Commits in one go a global transaction, using a unique connection, instead of doing
that on every row or every batch and thus improves performance.

The tPostgresqlCommit validates the
data processed through the Job into the connected DB

## tPostgresqlCommit Standard properties

These properties are used to configure tPostgresqlCommit running in the Standard Job framework.

The Standard
tPostgresqlCommit component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Component list | Select the tPostgresqlConnection component in the list if more than one connection are planned for the current Job. |
| Close Connection | This checkbox is selected by default. It allows you to close the database connection once the commit is done. Clear this checkbox to continue to use the selected connection once the component has performed its task.  Information noteWarning: If you want to use a Row  *>*  Main connection to link tPostgresqlCommit to your Job, your data will be committed row by row. In this case, do not select the Close connection check box or your connection will be closed before the end of your first row commit. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStat Catcher Statistics | Select this checkbox to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tPostgresql\* components, especially with the tPostgresqlConnection and tPostgresqlRollback components. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
