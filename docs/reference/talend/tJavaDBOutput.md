<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/javadb/tjavadboutput · versión 8.0 -->
# tJavaDBOutput

Last updated: 9/30/2026

Executes the action defined on the table and/or on the data contained in the table,
based on the flow incoming from the preceding component in the Job.

tJavaDBOutput writes, updates, makes changes or suppresses entries in a
database.

## tJavaDBOutput Standard properties

These properties are used to configure
tJavaDBOutput running in the Standard Job framework.

The
Standard
tJavaDBOutput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or Repository   . * Built-in: No property   data stored centrally. * Repository: Select the   repository file in which the properties are stored. The fields that   follow are completed automatically using the data   retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Framework | Select your Java database framework on the list |
| Database | Name of the database |
| DB root path | Browse to your database root. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, Job stops.  Update: Make changes to existing entries. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Delete: Remove entries corresponding to the input flow.  Information noteWarning: *It is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the Update and Delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column names you want to use as a base for the Update operation. Do the same in the Key in delete column for the Delete operation.* |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Commit every | Enter the number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and, above all, better performance at execution. |
| Additional Columns | * This option is not   offered if you create (with or without drop) the DB table. This option   allows you to call SQL functions to perform actions on columns, which   are not insert, nor update or delete actions, or action that require   particular preprocessing. * Name: Type in the name   of the schema column to be altered or inserted as new   column * SQL expression: Type in   the SQL statement to be executed in order to alter or insert the   relevant column data. * Position: Select   Before,   Replace or   After   following the action to be performed on the reference   column. * Reference column: Type   in a column of reference that the tDBOutput can use to place or replace   the new or altered column. |
| Use field options | Select this check box to customize a request, especially when there is double action on data. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a Java database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For an example of tMysqlOutput in use, see [Retrieving data in error with a Reject link](/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
