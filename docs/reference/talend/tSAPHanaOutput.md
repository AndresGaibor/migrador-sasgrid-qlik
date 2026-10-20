<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsaphanaoutput · versión 8.0 -->
# tSAPHanaOutput

Last updated: 9/30/2026

Executes the action defined on the table and/or on the data contained in the
table, based on the flow incoming from the preceding component in the Job.

tSAPHanaOutput writes, updates, makes changes or suppresses entries in a
SAP HANA database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSAPHanaOutput Standard properties

These properties are used to configure tSAPHanaOutput running in the Standard Job framework.

The Standard
tSAPHanaOutput component belongs to the Databases family.

If you have installed the 8.0.1-R2023-01 Talend Studio Monthly
update or a later one delivered by Talend, this
component is available in all Talend
subscription-based products; otherwise it is only available in all Talend products
with Big Data and in Talend Data Fabric.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | Listening port number of database server. |
| Schema | Name of the database schema. |
| Username and Password | Database authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted. |
| Type of table storage | This option is only available if you create (with or without drop) the database table. This option allows you to define the way the data is stored in the table. The following types of table storage organization are available:  * Row: Data is stored   in rows. It is preferable to use this table type if the   majority of table access involves selecting a few   records, with all attributes selected. * Column: Data is   stored in columns. It is preferable to use this table   type if the majority of table access will be through a   large number of tuples, with only a few selected   attributes. * History column:   Creates a table with a particular transaction session   type called *HISTORY*.   Tables with session type *HISTORY* support time travel queries. For   more information on *HISTORY* and time travel queries, see   [HISTORY COLUMN Option (Time Travel)](https://help.sap.com/viewer/4fe29514fd584807ac9f2a04f6754767/2.0.05/en-US/20d56cd075191014b7ea9e4e77477aae.html). * Global temporary: The   table definition and data can be seen by any user and   any connection during the current session. The table is   truncated at the end of the session. * Local temporary: The   table definition and data can only be seen by the user   who created the table during the current session. The   table is truncated at the end of the session. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, the Job stops.  Update: Make changes to existing entries  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted.  Delete: Remove entries corresponding to the input flow.  Note that it is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, see *Use filed options* in the Advanced settings view. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Die on error | This check box is cleared by default. This means that Die on error skips the row when an error is encountered and completes the process for rows without errors. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use alternate schema | Select this option to use a schema other than the one specified by the component that establishes the database connection (that is, the component selected from the Component list drop-down list in Basic settings view). After selecting this option, provide the name of the desired schema in the Schema field.  This option is available when Use an existing connection is selected in Basic settings view. |
| Additional JDBC Parameters | Specify additional connection properties in the database connection you are creating. This option is not available if you have selected Use an existing connection check box in the Basic settings. |
| Commit every | Enter the number of rows to be completed before committing batches of rows together into the database. This option ensures transaction quality (but not rollback) and, above all, better performance at execution. |
| Additional Columns | * This option is not available if you create (with or without drop)   the database table. This option allows you to call SQL functions to   perform actions on columns, which are not insert, nor update   or delete actions, or any other   action that requires particular preprocessing. * Name: Type in the name of the   schema column to be altered or inserted as new column * SQL expression: Type in the SQL   statement to be executed in order to alter or insert the relevant   column data. * Position: Select Before, Replace or After   following the action to be performed on the reference column. * Reference column: Type in a   column of reference that tSAPHanaOutput can use to locate or replace the new   column or the column to be modified. |
| Use field options | Select this check box to customize a request, especially when there is double action on data. In that table, you can define:  Key in update: define the primary key to use in an update operation.  Key in delete: define the primary key to use in a delete operation.  Updatable: define the column(s) to update.  Insertable: define the column(s) to insert. |
| Enable debug mode | Select this check box to display each step during processing entries in a database. |
| Support null in "SQL WHERE" statement | Select this check box to validate null in "SQL WHERE" statement. |
| Use Batch Size | When selected, enables you to define the number of lines in each processed batch.  This option is available only when you do not Use an existing connection in Basic settings. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component must be connected to an Input component. It allows you to carry out actions on a table or on the data of a table in an SAP HANA database. It also allows you to create reject flows using a Row > Reject link to filter erroneous data. |
| **Support** | tSAPHanaOutput should be used to interact with the ERP part of SAP, including S4/HANA. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
