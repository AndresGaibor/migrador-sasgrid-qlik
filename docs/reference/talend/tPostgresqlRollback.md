<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/postgresql/tpostgresqlrollback · versión 8.0 -->
# tPostgresqlRollback

Last updated: 9/30/2026

Avoids to commit part of a transaction involuntarily.

The tPostgresqlRollback cancels the transaction commit
in the connected DB.

## tPostgresqlRollback Standard properties

These properties are used to configure tPostgresqlRollback running in the Standard Job framework.

The Standard
tPostgresqlRollback component belongs to the Databases family.

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
| Close Connection | Clear this checkbox to continue to use the selected connection once the component has performed its task. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcherStatistics | Select this checkbox to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tPostgresql\* components, especially with the tPostgresqlConnection and tPostgresqlCommit components. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
