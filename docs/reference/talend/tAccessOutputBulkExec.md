<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/access/taccessoutputbulkexec · versión 8.0 -->
# tAccessOutputBulkExec

Last updated: 9/30/2026

Executes an Insert action on the data provided, in an Access database.

The tAccessOutputBulk and
tAccessBulkExec components are generally used together to output
data to a delimited file and then to perform various actions on the file in an Access
database, in a two step process. These two steps are fused together in
tAccessOutputBulkExec.

As a dedicated component, tAccessOutputBulkExec improves performance
during Insert operations in an Access database.

## tAccessOutputBulkExec Standard properties

These properties are used to configure tAccessOutputBulkExec running in the Standard Job framework.

The Standard
tAccessOutputBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .   * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| File Name | Name of the file to be processed. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Create directory if does not exist | Select this check box to create the as yet non existant file directory specified in the File Name field. |
| Append | Select this check box to append new rows to the end of the file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Include header | Select this check box to include the column header to the file. |
| Use text enclosure | Select this check box to enclose the text with characters. You can specify the character used to enclose the text in the Field enclosure field. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded in the database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | If you are using an ODBC driver, make sure that your JVM and ODBC versions match up: both 64-bit or 32-bit. |
