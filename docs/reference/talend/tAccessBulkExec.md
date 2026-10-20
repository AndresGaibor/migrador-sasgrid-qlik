<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/access/taccessbulkexec · versión 8.0 -->
# tAccessBulkExec

Last updated: 9/30/2026

Offers gains in performance when carrying out Insert operations in an Access
database.

The tAccessOutputBulk and
tAccessBulkExec components are generally used together to output
data to a delimited file and then to perform various actions on the file in an Access
database, in a two step process. These two steps are fused together in the tAccessOutputBulkExec component, detailed in a separate
section. The advantage of using a two step process is that it makes it possible to carry
out transformations on the data before loading it in the database.

This component executes an Insert action on the data
provided.

## tAccessBulkExec Standard properties

These properties are used to configure tAccessBulkExec running in the Standard Job framework.

The Standard
tAccessBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .   * Built-in: No property data is   stored centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| File Name | Browse to the delimited file to be loaded into your database. |
| Create directory if does not exist | Select this check box to have the directories specified in the File Name field created if the directories do not exist. |
| Append | Select this check box to append the data to the file. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-in: The schema is created and   stored locally for this component only. For more information about a   component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists and is stored in the   Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Include header | Select this check box to include the column header. |
| Use text enclosure | Select this check box to enclose the text with characters. You can specify the character used to enclose the text in the Field enclosure field. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is to be used along with tAccessOutputBulk component. Used together, they can offer gains in performance while feeding an Access database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | If you are using an ODBC driver, make sure that your JVM and ODBC versions match up: both 64-bit or 32-bit. |
