<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow · versión 8.0 -->
# tMysqlRow

Last updated: 9/30/2026

Executes the stated SQL query on the specified MySQL database.

Depending on the nature of the query and the database, tMysqlRow acts on the actual DB structure or on the data (although
without handling data). The SQLBuilder tool helps you write easily your SQL
statements.

tMysqlRow is the specific component for MySQL database
query. It implements a flow in the Job design although it doesn't provide output.

## tMysqlRow Standard properties

These properties are used to configure tMysqlRow running in the Standard Job framework.

The Standard
tMysqlRow component belongs to the Databases family.

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
| DB Version | Select the MySQL version that you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Name of the table to be processed. |
| Query type | * Either Built-in or   Repository   . * Built-in: Fill in manually the   query statement or build it graphically using SQLBuilder * Repository: Select the relevant   query stored in the Repository. The Query field gets accordingly   filled in. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row > Rejects link. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This checkbox is not available when the Use an existing connection checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Propagate QUERY's recordset | Select this check box to insert the result of the query in a COLUMN of the current flow. Select this column from the use column list.  Information noteNote: This option allows the component to have a different schema from that of the preceding component. Moreover, the column that holds the QUERY's recordset should be set to the type of *Object* and this component is usually followed by tParseRecordSet. |
| Use PreparedStatement | Select this check box if you want to query the database using a PreparedStatement. In the Set PreparedStatement Parameter table, define the parameters represented by "?" in the SQL instruction of the Query field in the Basic Settings tab.  Parameter Index: Enter the parameter position in the SQL instruction.  Parameter Type: Enter the parameter type.  Parameter Value: Enter the parameter value.    Information noteNote: This option is very useful if you need to execute the same query several times. Performance levels are increased |
| Commit every | Number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and above all better performance on executions. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query and covers all possible SQL queries. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Combining two flows for selective output](tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-combining-two-flows-for-selective-output-standard-component-in-this)
* [Removing and regenerating a MySQL table index](tmysqlrow-tmysqloutput-trowgenerator-tlogrow-removing-and-regenerating-mysql-table-index-standard-component-this)
* [Using PreparedStatement objects to query data](tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-combining-two-flows-for-selective-output-standard-component-in-this -->
# Combining two flows for selective output

Last updated: 9/30/2026

In this scenario, a flow generated by tFixedFlowInput is combined with a flow from the Mysql database. The source
flow contains *id* and *age* fields while the Mysql
table contains *id* and *name*. We want to retrieve
the *age* data of the source flow and combine it with the *id* and *name* records from the Mysql table based on
*id* matching. One thing that is worth noting is that the input schema
is different from the output one at tMysqlRow in the
Job.

### In this section

* [Linking the components](/talend/en-US/components/8.0/mysql/tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-executing-job-standard-component-press)

**Related reference**  

* [tMysqlRow](tmysqlrow "Executes the stated SQL query on the specified MySQL database.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tParseRecordSet](/talend/en-US/components/8.0/db-generic/tparserecordset)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tmysqloutput-trowgenerator-tlogrow-removing-and-regenerating-mysql-table-index-standard-component-this -->
# Removing and regenerating a MySQL table index

Last updated: 9/30/2026

This scenario describes a four-component Job that removes a table index,
applies a select insert action onto a table then regenerates the index.

### In this section

* [Linking the components](/talend/en-US/components/8.0/mysql/tmysqlrow-tmysqloutput-trowgenerator-tlogrow-linking-components-standard-component-select)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlrow-tmysqloutput-trowgenerator-tlogrow-configuring-components-standard-component-select)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlrow-tmysqloutput-trowgenerator-tlogrow-executing-job-standard-component-press)

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related reference**  

* [tMysqlRow](tmysqlrow "Executes the stated SQL query on the specified MySQL database.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this -->
# Using PreparedStatement objects to query data

Last updated: 9/30/2026

This scenario describes a four component Job which allows you to link a table
column with a client file. The MySQL table contains a list of all the American States along
with the State ID, while the file contains the customer information including the ID of the
State in which they live. We want to retrieve the name of the State for each client, using an
SQL query. In order to process a large volume of data quickly, we use a PreparedStatement
object which means that the query is executed only once rather than against each row in turn.
Then each row is sent as a parameter. Note that PreparedStatement object can also be used in
avoiding SQL injection.

For this scenario, we use a file and a database for which we have already
stored the connection and properties in the Rerpository metadata. For
further information concerning the creation of metadata in delimited files, the creation of
database connection metadata and the usage of metadata, see [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).

### In this section

* [Linking the components](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-linking-components-standard-component-in)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-executing-job-standard-component-press)

**Related reference**  

* [tMysqlRow](tmysqlrow "Executes the stated SQL query on the specified MySQL database.")

**Related information**  

* [tParseRecordSet](/talend/en-US/components/8.0/db-generic/tparserecordset)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Select Use Inline Content (delimited
   file) in the Mode
   area.

   In the Content field, enter the data to
   be transferred:

   ```
   1;30
   2;20
   ```
3. Double-click the [...] button next to
   Edit schema to open the schema editor. 

   Click the [+] button to add two columns,
   namely *id* and *age*, with the type of *Integer*.

   Click Ok to close the editor.
4. Double-click tMysqlRow to open its
   Basic settings view.
5. In the Host and Port fields, enter the connection details.

   In the Database field, enter the database
   name.

   In the Username and Password fields, enter the authentication details.

   In the Query field, enter the SQL query
   to retrieve the *id* and *name* data from the Mysql table *employee*: "select id, name from employee
   WHERE id=?".

   The question mark, "?", represents the parameter to be set in
   the Advanced settings tab.
6. Click the [...] button next to Edit schema to open the schema editor.
7. Click the [+] button to add two columns
   in the right part, namely *recordset* and
   *age*, with the type of *Object* and *Integer*. Note that *recordset* is intended to hold the query results of the Mysql
   table, namely the *id* and *name* fields.

   Click OK to close the editor.
8. Click the Advanced settings tab for
   further setup.
9. Select the Propagate QUERY's recordset
   check box and choose *recordset* from the
   use column list to insert the query
   results in that column.

   Select the Use PreparedStatement check
   box and define the parameter used in the query in the Set PreparedStatement Parameters table.
10. Click on the [+] button to add a line. 

    In the Parameter Index cell, enter the
    parameter position in the SQL instruction. Enter "*1*" as
    we are only using one parameter in this example.

    In the Parameter Type cell, enter the
    type of parameter. Here, the parameter is an integer. Hence, select
    Int from the list.

    In the Parameter Value cell, enter the
    parameter value. Here, we want to retrieve the *id* and *name* from the
    *employee* table based on the *id* value from the source flow. Hence, enter
    *row3.id*.
11. Double-click tParseRecordSet to open its
    Basic settings view.

    From the Prev. Comp. Column list, select
    the column to parse, namely *recordset*.
12. Click the [...] button next to Edit schema to open the schema editor.

    Click the [+] button to add three columns
    in the right part, namely *id*, *name* and *age*, with the type of *Integer*, *String* and *Integer*. Note that the *id* and *name* fields are
    intended to hold the parsed data of *recordset*.

    Click OK to close the editor.

    In the Attribute table, in the Value fields which correspond to *id* and *name*,
    enter the name of the column in the Mysql table to be retrieved, namely
    *"id"* and *"name"*.
13. Double-click tLogRow to open its
    Basic settings view.

    In the Mode area, select Table (print values in cells of a table for
    better display.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tfixedflowinput-tparserecordset-tlogrow-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tFixedFlowInput, tMysqlRow, tParseRecordSet and tLogRow
   onto the workspace.
2. Rename tFixedFlowInput as source\_flow, tMysqlRow as insert\_recordset, tParseRecordSet as parse\_recordset and tLogRow
   as show\_combined\_flow.
3. Link tFixedFlowInput to tMysqlRow using a Row > Main
   connection.
4. Link tMysqlRow to tParseRecordSet using a Row
   > Main connection.
5. Link tParseRecordSet to tLogRow using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tmysqloutput-trowgenerator-tlogrow-configuring-components-standard-component-select -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Select the tDBRow\_1 to fill
   in the DB Basic settings.
2. In Property type as well in
   Schema, select the relevant DB entry in the
   list.

   The DB connection details and the table schema are accordingly
   filled in.
3. Propagate the properties and schema details onto the other components of
   the Job.

   The query being stored in the Metadata
   area of the Repository, you can also select
   Repository in the Query type field and the relevant query entry.
4. If you didn't store your query in the Repository, type in the following SQL statement to alter the database
   entries: drop index <index\_name> on <table\_name>.
5. Select tDBRow\_2 component,
   check the DB properties and schema.
6. Type in the SQL statement to recreate an index on the table using the
   following statement: create index <index\_name> on <table\_name>
   (<column\_name>)

   The tRowGenerator component is used to
   generate automatically the columns to be added to the DB output table
   defined.
7. Select the tDBOutput\_1
   component and fill in the DB connection properties either from
   the Repository or manually the DB connection details are specific for this use
   only. The table to be fed is named: *comprehensive*.
8. The schema should be automatically inherited from the data flow
   coming from the tRowGenerator. Edit the schema
   to check its structure and check that it corresponds to the schema expected on the DB
   table specified.

   The Action on table is *None* and the Action on
   data is *Insert*.

   No additional Columns is required for this job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tmysqloutput-trowgenerator-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the job.

   If you manage to watch the action on DB data, you can notice that the
   index is dropped at the start of the Job and recreated at the end of the
   insert action.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tmysqloutput-trowgenerator-tlogrow-linking-components-standard-component-select -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Select and drop the following components onto the design workspace:
   tMysqlRow (x2), tRowGenerator, and tMysqlOutput.
2. Link the first tMysqlRow to tRowGenerator using an OnComponentOk connection.
3. Link tRowGenerator to tMysqlOutput using a Row > Main
   connection.
4. Link tRowGenerator to the second
   tMysqlRow using an OnSubjobOk connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputDelimited to open its Basic
   settings view.
2. In the Schema list, select Built-in so that you can modify the component's
   schema. Then click on [...] next to the
   Edit schema field to add a column into
   which the name of the State will be inserted.
3. Click on the [+] button
   to add a column to the schema. Rename this column *LabelStateRecordSet* and select Object from the Type list.
   Click OK to save your
   modifications.
4. From the Palette, select the
   tMysqlRow, tParseRecordSet and
   tFileOutputDelimited components and drop them onto the
   workspace.
5. Double-click tMysqlRow
   to set its properties in the Basic
   settings tab of the Component
   view.
6. In the Property Type
   list, select Repository and click on the
   [...] button to select a database
   connection from the metadata in the Repository. The DB Version, Host, Port, Database, Username and
   Password fields are completed
   automatically. If you are using the Built-in mode, complete these fields manually.
7. From the Schema list, select Built-in to set the schema properties manually
   and add the *LabelStateRecordSet* column, or click
   directly on the Sync columns button to
   retrieve the schemma from the preceding component.
8. In the Query field,
   enter the SQL query you want to use. Here, we want to retrieve the names of the
   American States from the *LabelState* column of the MySQL
   table, *us\_state*: "SELECT
   LabelState FROM us\_state WHERE idState=?". The question mark,
   "?", represents the parameter to be set in the
   Advanced settings tab.
9. Click Advanced settings
   to set the components advanced properties.
10. Select the Propagate QUERY's
    recordset check box and select the *LabelStateRecordSet* column from the use
    column list to insert the query results in that column.
11. Select the Use PreparedStatement check box and define
    the parameter used in the query in the Set PreparedStatement
    Parameters table.
12. Click on the [+] button to add a parameter.
    1. In the Parameter Index cell, enter the parameter
       position in the SQL instruction. Enter "*1*" as we are only using
       one parameter in this example.
    2. In the Parameter Type cell, enter the type of
       parameter. Here, the parameter is a whole number, hence, select
       Int from the list.
    3. In the Parameter Value cell, enter the parameter
       value. Here, we want to retrieve the name of the State based on the
       State ID for every client in the input file. Hence, enter "
       row1.idState".
13. Double-click tParseRecordSet to set its properties in the Basic settings tab of the Component view.
    1. From the Prev. Comp. Column list, select the
       preceding components column for analysis. In this example, select
       *LabelStateRecordSet*.
    2. Click on the Sync columns button to retrieve the
       schema from the preceding component. The Attribute
       table is automatically completed with the schema
       columns.
    3. In the Attribute table, in the
       Value field which corresponds to the
       *LabelStateRecordSet*, enter the name of the column containing the
       State names to be retrieved and matched with each client, within double
       quotation marks. In this example, enter "*LabelState*".
14. Double-click tFileOutputDelimited to set its properties in the Basic settings tab of the Component view.
    1. In the File Name field, enter the access path
       and name of the output file.
    2. Click Sync columns to retrieve the schema from
       the preceding component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run
   it.

## Results

A column containing the name of the American State corresponding to each client is
added to the file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-linking-components-standard-component-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the Repository, expand the Metadata and File
   delimited nodes.
2. Select the metadata which corresponds to the client file and slide the
   metadata onto the workspace. Here, we are using the
   *customers* metadata.
3. Double-click tFileInputDelimited in the
   Components dialog box to add
   tFileInputDelimited to the workspace,
   with the relevant fields filled by the metadata file.
4. Drop tMysqlRow, tParseRecordSet and tFileOutputDelimited onto the workspace.
5. Link tFileInputDelimited to tMysqlRow using a Row > Main
   connection.
6. Link tMysqlRow to tParseRecordSet using a Row
   > Main connection.
7. Link tParseRecordSet to tFileOutputDelimited using a Row > Main
   connection.
