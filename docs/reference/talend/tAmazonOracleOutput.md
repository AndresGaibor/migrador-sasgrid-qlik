<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-oracle/tamazonoracleoutput · versión 8.0 -->
# tAmazonOracleOutput

Last updated: 9/30/2026

Writes, updates, makes changes or suppresses entries in a database.

tAmazonOracleOutput executes the action defined on the table and/or on
the data contained in the table, based on the flow incoming from the preceding component
in the Job.

## tAmazonOracleOutput Standard properties

These properties are used to configure
tAmazonOracleOutput running in the Standard Job framework.

The
Standard
tAmazonOracleOutput component belongs to the Cloud and the Databases
families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository. * Built-in: No property   data stored centrally. * Repository: Select the   repository file in which the properties are stored. The fields that   follow are completed automatically using the data   retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers:  Oracle SID: Select this connection type to uniquely identify a particular database on a system. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Oracle schema | Name of the Oracle schema. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | Information noteNote: The Action on table list will not be available if you select the Enable parallel execution check box in the Advanced settings view.  On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted.  Information noteWarning: If you select the Use an existing connection check box and select an option other than None from the Action on table list, a commit statement will be generated automatically before the data update/insert/delete operation. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, job stops.  Update: Make changes to existing entries. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Delete: Remove entries corresponding to the input flow.  Information noteWarning: *It is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the Update and Delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column names you want to use as a base for the Update operation. Do the same in the Key in delete column for the Delete operation.*  Information noteNote: The dynamic schema feature can be used in the following modes: Insert; Update; Insert or update; Update or insert; Delete. |
| Schema and Edit schema | * A schema is a row   description, i.e. it defines the number of fields to be processed and   passed on to the next component. The schema is either Built-in or stored   remotely in the Repository.    This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use alternate schema | Select this option to use a schema other than the one specified by the component that establishes the database connection (that is, the component selected from the Component list drop-down list in Basic settings view). After selecting this option, provide the name of the desired schema in the Schema field.  This option is available when Use an existing connection is selected in Basic settings view. |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Override any existing NLS\_LANG environment variable | Select this check box to override variables already set for a NLS language environment. |
| Commit every | Enter the number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and, above all, better performance at execution. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |
| Additional Columns | * This option is not   offered if you create (with or without drop) the DB table. This option   allows you to call SQL functions to perform actions on columns, which   are not insert, nor update or delete actions, or action that require   particular preprocessing. * Name: Type in the name   of the schema column to be altered or inserted as new   column. * SQL expression: Type in   the SQL statement to be executed in order to alter or insert the   relevant column data. * Position: Select   Before,   Replace or   After   following the action to be performed on the reference   column. * Reference column: Type   in a column of reference that the tDBOutput can use to place or replace   the new or altered column. |
| Use field options | Select this check box to customize a request, especially when there is double action on data. |
| Use Hint Options | Select this check box to activate the hint configuration area which helps you optimize a query's execution. In this area, parameters are:  - HINT: specify the hint you need, using the syntax ```  /*+ */. ``` - POSITION: specify where you put the hint in a SQL statement.  - SQL STMT: select the SQL statement you need to use. |
| Convert columns and table to uppercase | Select this check box to set the names of columns and table in upper case. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use Batch | Select this check box to activate the batch mode for data processing. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Support null in "SQL WHERE" statement | Select this check box to validate null in "SQL WHERE" statement. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  Information noteWarning: * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a Oracle database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For such an example, see [Retrieving data in error with a Reject link](/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
