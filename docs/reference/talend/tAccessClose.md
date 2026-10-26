<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/access/taccessclose · versión 8.0 -->
# tAccessClose

Last updated: 9/30/2026

Closes an active connection to the Access database so as to release occupied
resources.

## tAccessClose Standard properties

These properties are used to configure tAccessClose running in the Standard Job framework.

The Standard
tAccessClose component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Component list | Select the tAccessConnection component in the list if more than one connection is planned for the current Job. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStat Catcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is to be used along with other Access components, especially with tAccessConnection and tAccessCommit. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | If you are using an ODBC driver, you need to work with Java 7, and make sure that your JVM and ODBC versions match up: both 64-bit or 32-bit. |

**Related concepts**  

* [Inserting data in parent/child tables](taccessinput-taccessconnection-tlogrow-inserting-data-in-parent-child-tables-standard-component-the)
