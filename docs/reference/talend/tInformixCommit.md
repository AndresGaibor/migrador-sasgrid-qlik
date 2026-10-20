<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/informix/tinformixcommit · versión 8.0 -->
# tInformixCommit

Last updated: 9/30/2026

Makes a global commit just once instead of commiting every row or batch of rows
separately.

This component improves performance and is closely related to
tInformixConnection and tInformixRollback. They are
generally used to execute transactions together.

tInformixCommit validates data processed in a Job from a connected
database.

## tInformixCommit Standard properties

These properties are used to configure tInformixCommit running in the Standard Job framework.

The Standard
tInformixCommit component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Component list | If there is more than one connection in the Job, select tInformixConnection from the list. |
| Close connection | This check box is selected by default. It means that the database conenction will be closed once the commit has been made. Clear the check box to continue using the connection once the component has completed its task.  Information noteWarning: *If you are using a Row > Main type connection to link tInformixCommit to your Job, your data will be committed row by row. If this is the case, do not select this check bx otherwise the conenction will be closed before the commit of your first row is finalized.* |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used along with Informix components, particularly tInformixConnection and tInformixRollback. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
