<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/informix/tinformixrollback · versión 8.0 -->
# tInformixRollback

Last updated: 9/30/2026

Prevents involuntary transaction commits by canceling transactions in connected
databases.

tInformixRollback is closely related to
tInformixCommit and tInformixConnection. They are
generally used together to execute transactions.

## tInformixRollback Standard properties

These properties are used to configure tInformixRollback running in the Standard Job framework.

The Standard
tInformixRollback component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Component list | Select the tInformixConnection component from the list if you plan to add more than one connection to the Job. |
| Close Connection | Clear this check box if you want to continue to use the connection once the component has completed its task. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component must be used with other Informix components, particularly tInformixConnection and tInformixCommit. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
