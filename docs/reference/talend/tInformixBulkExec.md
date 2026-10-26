<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/informix/tinformixbulkexec · versión 8.0 -->
# tInformixBulkExec

Last updated: 9/30/2026

Executes Insert operations in Informix databases.

tInformixOutputBulk and
tInformixBulkExec are generally used together in a two step
process. In the first step, an output file is generated. In the second step, this file
is used in the INSERT operation used to feed a database. These two steps are fused
together in the tInformixOutputBulkExec component. The advantage of
using two components is that data can be transformed before it is loaded in the
database.

## tInformixBulkExec Standard properties

These properties are used to configure tInformixBulkExec running in the Standard Job framework.

The Standard
tInformixBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Execution Platform | Select the operating system you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | DB server listening port. |
| Database | Name of the database. |
| Schema | Name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Instance | Name of the Informix instance to be used. This information can generally be found in the *SQL hosts* file. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Informix Directory | Informix installation directory, e.g. *" C:\Program Files\IBM\IBM Informix Dynamic Server\11.50\"*. |
| Data file | Name of the file to be loaded. |
| Action on data | On the data of the table defined, you can perform the following operations:  Insert: Add new data to the table. If duplicates are found, the Job stops.  Update: Update the existing table data.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted.  Delete: Delete the entry data which corresponds to the input flow.  Information noteWarning: *You must specify at least one key upon which the Update and Delete operations are to be based. It is possible to define the columns which should be used as the key from the schema, from both the Basic Settings and the Advanced Settings, to optimise these operations.* |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Field terminated by | Character, string or regular expression which separates the fields. |
| Set DBMONEY | Select this check box to define the decimal separator in the Decimal separator field. |
| Set DBDATE | Select the date format that you want to apply. |
| Rows Before Commit | Enter the number of rows to be processed before the commit. |
| Bad Rows Before Abort | Enter the number of rows in error at which point the Job should stop. |
| tStat Catcher Statistics | Select this check box to colelct the log data at component level. |
| Output | Where the output should go. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers database query flexibility and covers all possible DB2 queries which may be required. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The database server/client must be installed on the same machine where Talend Studio is installed or where the Job using tInformixBulkExec is deployed, so that the component functions properly.  This component requires installation of its related jar files. |
