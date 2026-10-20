<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tamazonmysqloutput · versión 8.0 -->
# tAmazonMysqlOutput

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Writes, updates, makes changes or suppresses entries in a database.

tAmazonMysqlOutput executes the action defined on the
table and/or on the data contained in the table, based on the flow incoming from the
preceding component in the Job.

## tAmazonMysqlOutput Standard properties

These properties are used to configure
tAmazonMysqlOutput running in the Standard Job framework.

The
Standard
tAmazonMysqlOutput component belongs to the Cloud and the Databases
families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

Information noteImportant: This component is deprecated since Talend Studio 8.0
R2024-12 and removed from Talend Studio 8.0
R2026-04 onwards.

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository. * Built-in: No property   data stored centrally. * Repository: Select the   repository file in which the properties are stored. The fields that   follow are completed automatically using the data   retrieved. |
| DB Version | Select the version of the MySQL database. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted.  Truncate table: The table content is quickly deleted. However, you will not be able to rollback the operation. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, the Job stops.  Update: Make changes to existing entries. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Delete: Remove entries corresponding to the input flow.  Replace: Add new entries to the table. If an old row in the table has the same value as a new row for a PRIMARY KEY or a UNIQUE index, the old row is deleted before the new row is inserted.  Insert or update on duplicate key or unique index: Add entries if the inserted value does not exist or update entries if the inserted value already exists and there is a risk of violating a unique index or primary key. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert Ignore: Add only new rows to prevent duplicate key errors.  Information noteWarning: *You must specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the update and delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column name on which you want to base the update operation. Do the same in the Key in delete column for the deletion operation.*  Information noteNote: The dynamic schema feature can be used in the following modes: Insert; Update; Insert or update; Update or insert; Delete. |
| Schema and Edit schema | * A schema is a row   description, i.e. it defines the number of fields to be processed and   passed on to the next component. The schema is either Built-in or stored   remotely in the Repository.    This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Die on error | This check box is selected by default. Clear the check box to skip the row in error and complete the process for error-free rows. If needed, you can retrieve the rows in error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Extend Insert | Select this check box to carry out a bulk insert of a defined set of lines instead of inserting lines one by one. The gain in system performance is considerable.    Number of rows per insert: enter the number of rows to be inserted per operation. Note that the higher the value specidied, the lower performance levels shall be due to the increase in memory demands.  Information noteNote: This option is not compatible with the Reject link. You should therefore clear the check box if you are using a Row > Rejects link with this component.  Information noteWarning: *If you are using this component with tMysqlLastInsertID, ensure that the Extend Insert check box in Advanced Settings is not selected. Extend Insert allows for batch loading, however, if the check box is selected, only the ID of the last line of the last batch will be returned*. |
| Use Batch | Select this check box to activate the batch mode for data processing.  Information noteNote: This check box is available only when you have selected, the Update or the Delete option in the Action on data field. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Commit every | Number of rows to be included in the batch before it is committed to the DB. This option ensures transaction quality (but not rollback) and, above all, a higher performance level. |
| Additional Columns | * This option is not   available if you have just created the DB table (even if you delete it   beforehand). This option allows you to call SQL functions to perform   actions on columns, provided that these are not insert, update or delete   actions, or actions that require pre-processing. * Name: Type in the name   of the schema column to be altered or inserted. * SQL expression: Type in   the SQL statement to be executed in order to alter or insert the data in   the corrsponding column. * Position: Select   Before,   Replace or   After,   depending on the action to be performed on the reference   column. * Reference column: Type   in a reference column that   tAmazonMysqlOutput can use to locate or replace the new   column, or the column to be modified. |
| Use field options | Select this check box to customize a request, particularly if multiple actions are being carried out on the data. |
| Use Hint Options | Select this check box to activate the hint configuration area which helps you optimize a query's execution. In this area, parameters are:  - HINT: specify the hint you need, using the syntax ```  /*+ */. ``` - POSITION: specify where you put the hint in a SQL statement.  - SQL STMT: select the SQL statement you need to use. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use duplicate key update mode insert | Updates the values of the columns specified, in the event of duplicate primary keys.:  Column: Between double quotation marks, enter the name of the column to be updated.  Value: Enter the action you want to carry out on the column.    Information noteNote: To use this option you must first of all select the Insert mode in the Action on data list found in the Basic Settings view. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  Information noteWarning: * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a MySQL database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For an example of tAmazonMysqlOutput in use, see . |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tamazonmysqloutput -->
# tAmazonMysqlOutput

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Writes, updates, makes changes or suppresses entries in a database.

tAmazonMysqlOutput executes the action defined on the
table and/or on the data contained in the table, based on the flow incoming from the
preceding component in the Job.

## tAmazonMysqlOutput Standard properties

These properties are used to configure
tAmazonMysqlOutput running in the Standard Job framework.

The
Standard
tAmazonMysqlOutput component belongs to the Cloud and the Databases
families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

Information noteImportant: This component is deprecated since Talend Studio 8.0
R2024-12 and removed from Talend Studio 8.0
R2026-04 onwards.

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository. * Built-in: No property   data stored centrally. * Repository: Select the   repository file in which the properties are stored. The fields that   follow are completed automatically using the data   retrieved. |
| DB Version | Select the version of the MySQL database. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted.  Truncate table: The table content is quickly deleted. However, you will not be able to rollback the operation. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, the Job stops.  Update: Make changes to existing entries. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Delete: Remove entries corresponding to the input flow.  Replace: Add new entries to the table. If an old row in the table has the same value as a new row for a PRIMARY KEY or a UNIQUE index, the old row is deleted before the new row is inserted.  Insert or update on duplicate key or unique index: Add entries if the inserted value does not exist or update entries if the inserted value already exists and there is a risk of violating a unique index or primary key. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert Ignore: Add only new rows to prevent duplicate key errors.  Information noteWarning: *You must specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the update and delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column name on which you want to base the update operation. Do the same in the Key in delete column for the deletion operation.*  Information noteNote: The dynamic schema feature can be used in the following modes: Insert; Update; Insert or update; Update or insert; Delete. |
| Schema and Edit schema | * A schema is a row   description, i.e. it defines the number of fields to be processed and   passed on to the next component. The schema is either Built-in or stored   remotely in the Repository.    This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Die on error | This check box is selected by default. Clear the check box to skip the row in error and complete the process for error-free rows. If needed, you can retrieve the rows in error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Extend Insert | Select this check box to carry out a bulk insert of a defined set of lines instead of inserting lines one by one. The gain in system performance is considerable.    Number of rows per insert: enter the number of rows to be inserted per operation. Note that the higher the value specidied, the lower performance levels shall be due to the increase in memory demands.  Information noteNote: This option is not compatible with the Reject link. You should therefore clear the check box if you are using a Row > Rejects link with this component.  Information noteWarning: *If you are using this component with tMysqlLastInsertID, ensure that the Extend Insert check box in Advanced Settings is not selected. Extend Insert allows for batch loading, however, if the check box is selected, only the ID of the last line of the last batch will be returned*. |
| Use Batch | Select this check box to activate the batch mode for data processing.  Information noteNote: This check box is available only when you have selected, the Update or the Delete option in the Action on data field. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Commit every | Number of rows to be included in the batch before it is committed to the DB. This option ensures transaction quality (but not rollback) and, above all, a higher performance level. |
| Additional Columns | * This option is not   available if you have just created the DB table (even if you delete it   beforehand). This option allows you to call SQL functions to perform   actions on columns, provided that these are not insert, update or delete   actions, or actions that require pre-processing. * Name: Type in the name   of the schema column to be altered or inserted. * SQL expression: Type in   the SQL statement to be executed in order to alter or insert the data in   the corrsponding column. * Position: Select   Before,   Replace or   After,   depending on the action to be performed on the reference   column. * Reference column: Type   in a reference column that   tAmazonMysqlOutput can use to locate or replace the new   column, or the column to be modified. |
| Use field options | Select this check box to customize a request, particularly if multiple actions are being carried out on the data. |
| Use Hint Options | Select this check box to activate the hint configuration area which helps you optimize a query's execution. In this area, parameters are:  - HINT: specify the hint you need, using the syntax ```  /*+ */. ``` - POSITION: specify where you put the hint in a SQL statement.  - SQL STMT: select the SQL statement you need to use. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use duplicate key update mode insert | Updates the values of the columns specified, in the event of duplicate primary keys.:  Column: Between double quotation marks, enter the name of the column to be updated.  Value: Enter the action you want to carry out on the column.    Information noteNote: To use this option you must first of all select the Insert mode in the Action on data list found in the Basic Settings view. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  Information noteWarning: * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a MySQL database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For an example of tAmazonMysqlOutput in use, see . |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
