<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput · versión 8.0 -->
# tMysqlOutput

Last updated: 9/30/2026

Writes, updates, makes changes or suppresses entries in a database.

tMysqlOutput executes the action defined on the table
and/or on the data contained in the table, based on the flow incoming from the preceding
component in the Job.

### In this section

* [tMysqlOutput Standard properties](/talend/en-US/components/8.0/mysql/tmysqloutput-standard-properties)
* [tMysqlOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/mysql/tmysqloutput-properties-for-apache-spark-batch)
* [tMysqlOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/mysql/tmysqloutput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Controlling the data definition language via tMysqlOutput when creating a table](controlling-data-definition-language-via-tmysqloutput "This scenario shows how to create a MySQL table with an AUTO_INCREMENT column and a UNIQUE one with tMysqlOutput component.")
* [Getting the ID for the last inserted record with tMysqlLastInsertId](tmysqlconnection-tmysqllastinsertid-tlogrow-getting-id-for-last-inserted-record-with-tmysqllastinsertid-standard-component-the)
* [Inserting a column and altering data using tMysqlOutput](tmysqloutput-tmap-trowgenerator-trowgenerator-inserting-column-and-altering-data-using-tmysqloutput-standard-component-this)
* [Inserting data in mother/daughter tables](tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the)
* [Populating a MySQL data warehouse](tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-populating-mysql-data-warehouse-standard-component-enterprise-the)
* [Removing and regenerating a MySQL table index](tmysqlrow-tmysqloutput-trowgenerator-tlogrow-removing-and-regenerating-mysql-table-index-standard-component-this)
* [Retrieving data in error with a Reject link](tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this)
* [Sharing a database connection between a parent Job and child Job](tmysqlconnection-tmysqlinput-tlogrow-sharing-database-connection-between-parent-job-and-child-job-standard-component-this)
* [Updating a database table using tMysqlOutput in a Big Data Streaming Job](tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-updating-database-table-using-tmysqloutput-in-big-data-streaming-job-this)
* [Updating data using tMysqlOutput](tmysqloutput-tfileinputdelimited-updating-data-using-tmysqloutput-standard-component-this)
* [Writing dynamic columns from a source file to a database](writing-dynamic-columns-from-source-file-to-database)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-properties-for-apache-spark-batch -->
# tMysqlOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMysqlOutput running in the Spark Batch Job framework.

The Spark Batch
tMysqlOutput component belongs to the Databases family.

This component can also be used to write data to a RDS Aurora or a RDS MySQL
database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| DB Version | Select the MySQL version you are using.  When the database to be used is RDS Aurora, you need to select Mysql 5 (deprecated).  Information noteNote: MySQL 5 has been removed from Talend Studio 8.0 R2026-04. Use MySQL 8.0 or later. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. |
| Use Batch per partition | Select this check box to activate the batch mode for data processing.  Information noteNote: This check box is available only when you have selected, the Update or the Delete option in the Action on data field. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tMysqlConfiguration component present in the same Job to connect to MySQL. You need to select the Use an existing connection check box and then select the tMysqlConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-standard-properties -->
# tMysqlOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure
tMysqlOutput running in the Standard Job framework.

The
Standard
tMysqlOutput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| DB Version | Select the MySQL version you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the database server IP address. |
| Port | Enter the listening port number of DB server. |
| Database | Enter the name of the database. |
| Username and Password | Enter the DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | On the table defined, you can perform one of the following operations: Default: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted.  Truncate table: The table content is quickly deleted. However, you will not be able to rollback the operation. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, the Job stops.  Update: Make changes to existing entries. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Delete: Remove entries corresponding to the input flow.  Replace: Add new entries to the table. If an old row in the table has the same value as a new row for a PRIMARY KEY or a UNIQUE index, the old row is deleted before the new row is inserted.  Insert or update on duplicate key or unique index: Add entries if the inserted value does not exist or update entries if the inserted value already exists and there is a risk of violating a unique index or primary key. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert Ignore: Add only new rows to prevent duplicate key errors.  Information noteWarning: *You must specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the update and delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column name on which you want to base the update operation. Do the same in the Key in delete column for the deletion operation.*  Information noteNote: The dynamic schema feature can be used in the following modes: Insert; Update; Insert or update; Update or insert; Delete. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  Information noteWarning: If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This checkbox is not available when the Use an existing connection checkbox is selected. |
| Die on error | This check box is selected by default. Clear the check box to skip the row in error and complete the process for error-free rows. If needed, you can retrieve the rows in error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use alternate schema | Select this option to use a schema other than the one specified by the component that establishes the database connection (that is, the component selected from the Component list drop-down list in Basic settings view). After selecting this option, provide the name of the desired schema in the Schema field.  This option is available when Use an existing connection is selected in Basic settings view. |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Extend Insert | Select this check box to carry out a bulk insert of a defined set of lines instead of inserting lines one by one. The gain in system performance is considerable.  Number of rows per insert: enter the number of rows to be inserted per operation. Note that the higher the value specified, the lower performance levels shall be due to the increase in memory demands.  Information noteNote: This option is not compatible with the Reject link. You should therefore clear the check box if you are using a Row > Rejects link with this component.  Information noteWarning: If you are using this component with tMysqlLastInsertID, ensure that the Extend Insert check box in Advanced settings is not selected. Extend Insert allows for batch loading, however, if the check box is selected, only the ID of the last line of the last batch will be returned. |
| Use Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Commit every | Specify the number of rows to be included in the batch before it is committed to the DB. This option ensures transaction quality (but not rollback) and, above all, a higher performance level. |
| Additional Columns | * This option is not   available if you have just created the DB table (even if you delete it   beforehand). This option allows you to call SQL functions to perform   actions on columns, provided that these are not insert, update or delete   actions, or actions that require pre-processing. * Name: Type in the name   of the schema column to be altered or inserted. * SQL expression: Type in   the SQL statement to be executed in order to alter or insert the data in   the corresponding column. * Position: Select   Before,   Replace or   After,   depending on the action to be performed on the reference   column. * Reference column: Type   in a reference column that   tMysqlOutput can use to locate or replace the new   column, or the column to be modified. |
| Use field options | Select this check box to customize a request, particularly if multiple actions are being carried out on the data. |
| Use Hint Options | Select this check box to activate the hint configuration area which helps you optimize a query's execution. In this area, parameters are: - HINT: specify the hint you need, using the syntax /\*+ \*/.  - POSITION: specify where you put the hint in a SQL statement.  - SQL STMT: select the SQL statement you need to use. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use duplicate key update mode insert | Updates the values of the columns specified, in the event of duplicate primary keys.: Column: Between double quotation marks, enter the name of the column to be updated.  Value: Enter the action you want to carry out on the column.  Information noteNote: To use this option you must first select the Insert mode in the Action on data list in the Basic Settings view. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  Information noteWarning: * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a MySQL database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For an example of tMysqlOutput in use, see [Retrieving data in error with a Reject link](/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-tfileinputdelimited-updating-data-using-tmysqloutput-standard-component-this -->
# Updating data using tMysqlOutput

Last updated: 9/30/2026

This Java scenario describes a two-component Job that updates data in a MySQL table
according to that in a delimited file.

* Drop tFileInputDelimited and
  tMysqlOutput (displayed as
  tDBOutput\_1) from the Palette onto the design workspace.
* Connect the two components together using a Row
  Main link.

* Double-click tFileInputDelimited to display
  its Basic settings view and define the
  component properties.
* From the Property Type list, select Repository if you have already stored the metadata of
  the delimited file in the Metadata node in the
  Repository tree view. Otherwise, select
  Built-In to define manually the metadata of
  the delimited file.

  For more information about storing metadata, see [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).

* Click the [...] button next to the File name/Stream field and browse to the source
  delimited file that contains the modifications to propagate in the MySQL table.

  In this example, we use the *customer\_update* file that
  holds four columns: *id*, *CustomerName*,
  *CustomerAddress* and *idState*. Some
  of the data in these four columns is different from that in the MySQL
  table.

* Define the row and field separators used in the source file in the
  corresponding fields.
* If needed, set Header, Footer and Limit.

  In this example, Header is set to 1 since the
  first row holds the names of columns, therefore it should be ignored. Also, the
  number of processed lines is limited to 2000.
* Click the [...] button next to Edit Schema to open a dialog box where you can
  describe the data structure of the source delimited file that you want to pass to the
  component that follows.

* Select the Key check box(es) next to the
  column name(s) you want to define as key column(s).

Information noteNote:

It is necessary to define at least one column as a key column for the Job to be
executed correctly. Otherwise, the Job is automatically interrupted and an error
message displays on the console.

* In the design workspace, double-click tDBOutput\_1 to open its Basic
  settings view where you can define its properties.

* Click Sync columns to retrieve the schema of
  the preceding component. If needed, click the [...] button next to Edit schema to open a dialog box where you can check
  the retrieved schema.
* From the Property Type list, select Repository if you have already stored the connection
  metadata in the Metadata node in the Repository tree view. Otherwise, select Built-In to define manually the connection
  information.

  For more information about storing metadata, see [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).
* Fill in the database connection information in the corresponding
  fields.
* In the Table field, enter the name of the
  table to update.
* From the Action on table list, select the
  operation you want to perform, Default in this
  example since the table already exists.
* From the Action on data list, select the
  operation you want to perform on the data, Update in this example.
* Save your Job and press F6 to execute it.

Using you DB browser, you can verify if the MySQL table, *customers,*has been modified according to the delimited file.

In the above example, the database table has always the four columns
*id*, *CustomerName*,
*CustomerAddress* and *idState*, but certain
fields have been modified according to the data in the delimited file used.

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this -->
# Retrieving data in error with a Reject link

Last updated: 9/30/2026

This scenario describes a four-component Job that carries out migration
from a customer file to a MySQL database table and redirects data in error towards a CSV
file using a Reject link.

* In the Repository, select
  the customer file metadata that you want to migrate and drop it onto the
  workspace. In the Components dialog box,
  select tFileInputDelimited and click
  OK. The component properties will be
  filled in automatically.
* If you have not stored the information about your customer
  file under the Metadata node in the
  Repository. Drop a tFileInputDelimited component from the family
  File > Input, in the Palette,
  and fill in its properties manually in the Component tab.
* From the Palette, drop a
  tMap from the Processing family onto the workspace.
* In the Repository, expand
  the Metadata node, followed by the
  Db Connections node and select the
  connection required to migrate your data to the appropriate database. Drop it
  onto the workspace. In the Components
  dialog box, select tMysqlOutput and click
  OK. The database connection
  properties will be automatically filled in.
* If you have not stored the database connection details under the
  Db Connections node in the Repository, drop a tMysqlOutput from the Databases family in the Palette and fill in its properties manually in the Component tab.

For more information, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata).

* From the Palette, select
  a tFileOutputDelimited from the
  File > Output family, and drop it onto the workspace.
* Link the customers
  component to the tMap component, and the
  tMap and Localhost with a Row
  Main link. Name this second link *out*.
* Link the Localhost to the
  tFileOutputDelimited using a
  Row > Reject link.
* Double-click the customers component to display the Component view.

* In the Property Type
  list, select Repository and
  click the [...] button  in order to
  select the metadata containing the connection to your file. You can also select
  the Built-in mode and fill in the fields
  manually.
* Click the [...] button
  next to the File Name field, and fill in
  the path and the name of the file you want to use.
* In the Row and Field Separator fields, type in between inverted
  commas the row and field separator used in the file.
* In the Header, Footer and Limit fields, type in the number of headers and footers to
  ignore, and the number of rows to which processing should be limited.
* In the Schema list, select
  Repository and click the [...] button in order to select the schema of
  your file, if it is stored under the Metadata node in the Repository. You can also click the [...] button next to the Edit
  schema field, and set the schema manually.

The schema is as follows:

* Double-click the tMap
  component to open its editor.

* Select the *id*, *CustomerName*, *CustomerAddress*, *idSate*, *id2*, *RegTime* and *RegisterTime* columns on the table on
  the left and drop them on the out table,
  on the right.

* In the Schema editor
  area, at the bottom of the tMap editor,
  in the right table, change the length of the CustomerName column to *28* to create an
  error. Thus, any data for which the length is greater than 28 will create
  errors, retrieved with the Reject
  link.
* Click OK.
* In the workspace, double-click the output Localhost component to display its Component  view.

* In the Property Type list,
  select Repository and click the
  [...] button to select the connection
  to the database metadata. The connection details will be automatically filled
  in. You can also select the Built-in mode
  and set the fields manually.
* In the Table field, type
  in the name of the table to be created. In this scenario, we call it *customers\_data*.
* In the Action on data
  list, select the Create table
  option.
* Click the Sync columns
  button to retrieve the schema from the previous component.
* Make sure the Die on
  error check box isn't selected, so that the Job can be executed
  despite the error you just created.
* Click the Advanced
  settings tab of the Component view to set the advanced parameters of the
  component.

* Deselect the Extend
  Insert check box which enables you to insert rows in batch,
  because this option is not compatible with the Reject link.
* Double-click the tFileOutputDelimited
  component to set its properties in the Component view.

* Click the [...] button next
  to the File name/Stream field to fill in the
  path and name of the output file.
* Click the Sync columns
  button to retrieve the schema of the previous component.
* Save your Job and press F6 to execute it.

The data in error are sent to the delimited file, as well as the error
type met. Here, we have: Data truncation.

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-trowgenerator-trowgenerator-inserting-column-and-altering-data-using-tmysqloutput-standard-component-this -->
# Inserting a column and altering data using tMysqlOutput

Last updated: 9/30/2026

This Java scenario is a three-component Job that aims at creating random data using a
tRowGenerator, duplicating a column to be altered
using the tMap component, and eventually altering the
data to be inserted based on an SQL expression using the tMysqlOutput component.

* Drop the following components from the Palette onto the design workspace: tRowGenerator, tMap and
  tMySQLOutput.
* Connect tRowGenerator, tMap, and tMysqlOutput using
  the Row Main link.

* In the design workspace, select tRowGenerator to display its Basic
  settings view.

* Click the [...] button next to Edit schema to define the data to pass on to the
  tMap component, two columns in this
  scenario, *name* and *random\_date*.

* Click OK to close the dialog box.
* Click the [...] button next to RowGenerator Editor to open the editor and define the
  data to be generated.

* Click in the corresponding Functions fields
  and select a function for each of the two columns, getFirstName for
  the first column and getrandomDate for the second column.
* In the Number of Rows for Rowgenerator
  field, enter 10 to generate ten first name rows and click Ok to close the editor.
* Double-click the tMap component to open the
  Map editor. The Map editor opens displaying the input metadata of the tRowGenerator component.

* In the Schema editor panel of the Map
  editor, click the plus button of the output table to add two rows and define the
  first as *random\_date* and the second as
  *random\_date1*.

In this scenario, we want to duplicate the *random\_date* column and
adapt the schema in order to alter the data in the output component.

* In the Map editor, drag the *random\_date* row from the
  input table to the *random\_date* and *random\_date1*rows in the output table.

* Click OK to close the editor.
* In the design workspace, double-click the tMysqlOutput component to display its Basic settings view and set its parameters.

* Set Property Type to Repository and then click the [...] button to open the
  Repository content dialog box and select
  the correct DB connection. The connection details display automatically in the
  corresponding fields.

  Information noteNote:

  If you have not stored the DB connection details in the Metadata entry in the Repository, select Built-in
  on the property type list and set the connection detail manually.
* Click the [...] button next to the Table
  field and select the table to be altered, *Dates* in this
  scenario.
* On the Action on table list, select
  Drop table if exists and create, select
  *Insert* on the Action on
  data list.
* If needed, click Sync columns to synchronize
  with the columns coming from the tMap
  component.
* Click the Advanced settings tab to display
  the corresponding view and set the advanced parameters.

* In the Additional Columns area, set the
  alteration to be performed on columns.

  In this scenario, the *One\_month\_later* column replaces
  *random\_date\_1*. Also, the data itself gets altered using
  an SQL expression that adds one month to the randomly picked-up date of the
  *random\_date\_1* column. ex: 2007-08-12 becomes
  2007-09-12.

  -Enter *One\_Month\_Later* in the Name cell.

  -In the SQL expression cell, enter the
  relevant addition script to be performed, "adddate(Random\_date, interval 1
  month)" in this scenario.

  -Select Replace on the Position list.

  -Enter *Random\_date1* on the Reference column list.

Information noteNote:

For this Job we duplicated the *random\_date\_1* column in the DB
table before replacing one instance of it with the
*One\_Month\_Later* column. The aim of this workaround was to
be able to view upfront the modification performed.

* Save your Job and press F6 to execute
  it.

The new *One\_month\_later* column replaces the
*random\_date1* column in the DB table and adds one month to each
of the randomly generated dates.

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-updating-database-table-using-tmysqloutput-in-big-data-streaming-job-this -->
# Updating a database table using tMysqlOutput in a Big Data Streaming Job

Last updated: 9/30/2026

This scenario applies only to Talend Real-Time Big Data Platform and
Talend Data Fabric.

This scenario describes a Big Data Streaming Job that updates data in specific
rows of a MySQL table once every five seconds.

### In this section

* [Establishing the Job](/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-establishing-job-create)
* [Selecting the Spark mode](/talend/en-US/components/8.0/mysql/selecting-spark-mode-spark-batch?id=3596)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/mysql/configuring-connection-to-file-system-to-be-used-by-spark?id=3598)
* [Configure the Job](/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-configure-job-open)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-executing-job-save)

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-configure-job-open -->
# Configure the Job

Last updated: 9/30/2026

## Procedure

1. Open the Basic settings view of
   tRowGenerator.
2. Define the schema for the table. 

   In this case, two columns are added:
   * Num, type integer, set as the key column
   * Cities, type string and length 20
3. Propagate the schema to the next component.
4. In RowGenerator Editor dialog box, set functions as
   follows.

   * Num: `Numeric.sequence`, with both start
     value and step set to
     `1`
   * Cities: `TalendDataGenerator.getUsCity()`
   * Number of Rows for RowGenerator:
     `10`

   Information noteNote: These settings specify to generate 10 rows of data at a time, with the
   Num values from 1 to 10.
5. Set Input repetition interval to
   `5000`.
6. Open the Basic settings view of
   tMysqlOutput.
7. Set the database table parameters. In this example, database is locally
   installed.

   Information noteNote: To make sure the table is updated properly, it is recommended to select
   None for the Action on
   table option and Update for the
   Action on data option.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-establishing-job-create -->
# Establishing the Job

Last updated: 9/30/2026

## Procedure

1. Create a Big Data Streaming Job.
2. Drop tRowGenerator and
   tMysqlOutput from the Palette onto the design
   workspace.
3. Connect the two components using a Row > Main connection.

   tHDFSConfiguration is used in this scenario by Spark to connect
   to the HDFS system where the jar files dependent on the Job are transferred.

   In the Spark
   Configuration tab in the Run
   view, define the connection to a given Spark cluster for the whole Job. In
   addition, since the Job expects its dependent jar files for execution, you must
   specify the directory in the file system to which these jar files are
   transferred so that Spark can access these files:
   * Yarn mode (Yarn client or Yarn cluster):
     + When using Google Dataproc, specify a bucket in the
       Google Storage staging bucket
       field in the Spark configuration
       tab.
     + When using HDInsight, specify the blob to be used for Job
       deployment in the Windows Azure Storage
       configuration area in the Spark
       configuration tab.
     + When using Altus, specify the S3 bucket or the Azure
       Data Lake Storage for Job deployment in the Spark
       configuration tab.
     + When using on-premises distributions, use
       the configuration component corresponding to the file system
       your cluster is using. Typically, this system is HDFS and so
       use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
   * Standalone mode: use the
     configuration component corresponding to the file system your cluster is
     using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

     If you are using Databricks without any configuration component present
     in your Job, your business data is written directly in DBFS (Databricks
     Filesystem).

   Prerequisite: ensure that the Spark cluster has been
   properly installed and is running.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-executing-job-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Save the Job.
2. Press F6 to execute it. 

   The data in row 1 through row 10 of the database table is updated once
   every five seconds.
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-standard-properties · versión 8.0 -->
# tMysqlOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure
tMysqlOutput running in the Standard Job framework.

The
Standard
tMysqlOutput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| DB Version | Select the MySQL version you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the database server IP address. |
| Port | Enter the listening port number of DB server. |
| Database | Enter the name of the database. |
| Username and Password | Enter the DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | On the table defined, you can perform one of the following operations: Default: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted.  Truncate table: The table content is quickly deleted. However, you will not be able to rollback the operation. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, the Job stops.  Update: Make changes to existing entries. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Delete: Remove entries corresponding to the input flow.  Replace: Add new entries to the table. If an old row in the table has the same value as a new row for a PRIMARY KEY or a UNIQUE index, the old row is deleted before the new row is inserted.  Insert or update on duplicate key or unique index: Add entries if the inserted value does not exist or update entries if the inserted value already exists and there is a risk of violating a unique index or primary key. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert Ignore: Add only new rows to prevent duplicate key errors.  Information noteWarning: *You must specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the update and delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column name on which you want to base the update operation. Do the same in the Key in delete column for the deletion operation.*  Information noteNote: The dynamic schema feature can be used in the following modes: Insert; Update; Insert or update; Update or insert; Delete. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  Information noteWarning: If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This checkbox is not available when the Use an existing connection checkbox is selected. |
| Die on error | This check box is selected by default. Clear the check box to skip the row in error and complete the process for error-free rows. If needed, you can retrieve the rows in error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use alternate schema | Select this option to use a schema other than the one specified by the component that establishes the database connection (that is, the component selected from the Component list drop-down list in Basic settings view). After selecting this option, provide the name of the desired schema in the Schema field.  This option is available when Use an existing connection is selected in Basic settings view. |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Extend Insert | Select this check box to carry out a bulk insert of a defined set of lines instead of inserting lines one by one. The gain in system performance is considerable.  Number of rows per insert: enter the number of rows to be inserted per operation. Note that the higher the value specified, the lower performance levels shall be due to the increase in memory demands.  Information noteNote: This option is not compatible with the Reject link. You should therefore clear the check box if you are using a Row > Rejects link with this component.  Information noteWarning: If you are using this component with tMysqlLastInsertID, ensure that the Extend Insert check box in Advanced settings is not selected. Extend Insert allows for batch loading, however, if the check box is selected, only the ID of the last line of the last batch will be returned. |
| Use Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Commit every | Specify the number of rows to be included in the batch before it is committed to the DB. This option ensures transaction quality (but not rollback) and, above all, a higher performance level. |
| Additional Columns | * This option is not   available if you have just created the DB table (even if you delete it   beforehand). This option allows you to call SQL functions to perform   actions on columns, provided that these are not insert, update or delete   actions, or actions that require pre-processing. * Name: Type in the name   of the schema column to be altered or inserted. * SQL expression: Type in   the SQL statement to be executed in order to alter or insert the data in   the corresponding column. * Position: Select   Before,   Replace or   After,   depending on the action to be performed on the reference   column. * Reference column: Type   in a reference column that   tMysqlOutput can use to locate or replace the new   column, or the column to be modified. |
| Use field options | Select this check box to customize a request, particularly if multiple actions are being carried out on the data. |
| Use Hint Options | Select this check box to activate the hint configuration area which helps you optimize a query's execution. In this area, parameters are: - HINT: specify the hint you need, using the syntax /\*+ \*/.  - POSITION: specify where you put the hint in a SQL statement.  - SQL STMT: select the SQL statement you need to use. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use duplicate key update mode insert | Updates the values of the columns specified, in the event of duplicate primary keys.: Column: Between double quotation marks, enter the name of the column to be updated.  Value: Enter the action you want to carry out on the column.  Information noteNote: To use this option you must first select the Insert mode in the Action on data list in the Basic Settings view. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  Information noteWarning: * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a MySQL database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For an example of tMysqlOutput in use, see [Retrieving data in error with a Reject link](/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput -->
# tMysqlOutput

Last updated: 9/30/2026

Writes, updates, makes changes or suppresses entries in a database.

tMysqlOutput executes the action defined on the table
and/or on the data contained in the table, based on the flow incoming from the preceding
component in the Job.

### In this section

* [tMysqlOutput Standard properties](/talend/en-US/components/8.0/mysql/tmysqloutput-standard-properties)
* [tMysqlOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/mysql/tmysqloutput-properties-for-apache-spark-batch)
* [tMysqlOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/mysql/tmysqloutput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Controlling the data definition language via tMysqlOutput when creating a table](controlling-data-definition-language-via-tmysqloutput "This scenario shows how to create a MySQL table with an AUTO_INCREMENT column and a UNIQUE one with tMysqlOutput component.")
* [Getting the ID for the last inserted record with tMysqlLastInsertId](tmysqlconnection-tmysqllastinsertid-tlogrow-getting-id-for-last-inserted-record-with-tmysqllastinsertid-standard-component-the)
* [Inserting a column and altering data using tMysqlOutput](tmysqloutput-tmap-trowgenerator-trowgenerator-inserting-column-and-altering-data-using-tmysqloutput-standard-component-this)
* [Inserting data in mother/daughter tables](tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the)
* [Populating a MySQL data warehouse](tmysqlinput-tmysqloutput-tmap-tmysqloutput-tmap-populating-mysql-data-warehouse-standard-component-enterprise-the)
* [Removing and regenerating a MySQL table index](tmysqlrow-tmysqloutput-trowgenerator-tlogrow-removing-and-regenerating-mysql-table-index-standard-component-this)
* [Retrieving data in error with a Reject link](tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this)
* [Sharing a database connection between a parent Job and child Job](tmysqlconnection-tmysqlinput-tlogrow-sharing-database-connection-between-parent-job-and-child-job-standard-component-this)
* [Updating a database table using tMysqlOutput in a Big Data Streaming Job](tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-updating-database-table-using-tmysqloutput-in-big-data-streaming-job-this)
* [Updating data using tMysqlOutput](tmysqloutput-tfileinputdelimited-updating-data-using-tmysqloutput-standard-component-this)
* [Writing dynamic columns from a source file to a database](writing-dynamic-columns-from-source-file-to-database)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-properties-for-apache-spark-batch -->
# tMysqlOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tMysqlOutput running in the Spark Batch Job framework.

The Spark Batch
tMysqlOutput component belongs to the Databases family.

This component can also be used to write data to a RDS Aurora or a RDS MySQL
database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| DB Version | Select the MySQL version you are using.  When the database to be used is RDS Aurora, you need to select Mysql 5 (deprecated).  Information noteNote: MySQL 5 has been removed from Talend Studio 8.0 R2026-04. Use MySQL 8.0 or later. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. |
| Use Batch per partition | Select this check box to activate the batch mode for data processing.  Information noteNote: This check box is available only when you have selected, the Update or the Delete option in the Action on data field. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tMysqlConfiguration component present in the same Job to connect to MySQL. You need to select the Use an existing connection check box and then select the tMysqlConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this -->
# Retrieving data in error with a Reject link

Last updated: 9/30/2026

This scenario describes a four-component Job that carries out migration
from a customer file to a MySQL database table and redirects data in error towards a CSV
file using a Reject link.

* In the Repository, select
  the customer file metadata that you want to migrate and drop it onto the
  workspace. In the Components dialog box,
  select tFileInputDelimited and click
  OK. The component properties will be
  filled in automatically.
* If you have not stored the information about your customer
  file under the Metadata node in the
  Repository. Drop a tFileInputDelimited component from the family
  File > Input, in the Palette,
  and fill in its properties manually in the Component tab.
* From the Palette, drop a
  tMap from the Processing family onto the workspace.
* In the Repository, expand
  the Metadata node, followed by the
  Db Connections node and select the
  connection required to migrate your data to the appropriate database. Drop it
  onto the workspace. In the Components
  dialog box, select tMysqlOutput and click
  OK. The database connection
  properties will be automatically filled in.
* If you have not stored the database connection details under the
  Db Connections node in the Repository, drop a tMysqlOutput from the Databases family in the Palette and fill in its properties manually in the Component tab.

For more information, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata).

* From the Palette, select
  a tFileOutputDelimited from the
  File > Output family, and drop it onto the workspace.
* Link the customers
  component to the tMap component, and the
  tMap and Localhost with a Row
  Main link. Name this second link *out*.
* Link the Localhost to the
  tFileOutputDelimited using a
  Row > Reject link.
* Double-click the customers component to display the Component view.

* In the Property Type
  list, select Repository and
  click the [...] button  in order to
  select the metadata containing the connection to your file. You can also select
  the Built-in mode and fill in the fields
  manually.
* Click the [...] button
  next to the File Name field, and fill in
  the path and the name of the file you want to use.
* In the Row and Field Separator fields, type in between inverted
  commas the row and field separator used in the file.
* In the Header, Footer and Limit fields, type in the number of headers and footers to
  ignore, and the number of rows to which processing should be limited.
* In the Schema list, select
  Repository and click the [...] button in order to select the schema of
  your file, if it is stored under the Metadata node in the Repository. You can also click the [...] button next to the Edit
  schema field, and set the schema manually.

The schema is as follows:

* Double-click the tMap
  component to open its editor.

* Select the *id*, *CustomerName*, *CustomerAddress*, *idSate*, *id2*, *RegTime* and *RegisterTime* columns on the table on
  the left and drop them on the out table,
  on the right.

* In the Schema editor
  area, at the bottom of the tMap editor,
  in the right table, change the length of the CustomerName column to *28* to create an
  error. Thus, any data for which the length is greater than 28 will create
  errors, retrieved with the Reject
  link.
* Click OK.
* In the workspace, double-click the output Localhost component to display its Component  view.

* In the Property Type list,
  select Repository and click the
  [...] button to select the connection
  to the database metadata. The connection details will be automatically filled
  in. You can also select the Built-in mode
  and set the fields manually.
* In the Table field, type
  in the name of the table to be created. In this scenario, we call it *customers\_data*.
* In the Action on data
  list, select the Create table
  option.
* Click the Sync columns
  button to retrieve the schema from the previous component.
* Make sure the Die on
  error check box isn't selected, so that the Job can be executed
  despite the error you just created.
* Click the Advanced
  settings tab of the Component view to set the advanced parameters of the
  component.

* Deselect the Extend
  Insert check box which enables you to insert rows in batch,
  because this option is not compatible with the Reject link.
* Double-click the tFileOutputDelimited
  component to set its properties in the Component view.

* Click the [...] button next
  to the File name/Stream field to fill in the
  path and name of the output file.
* Click the Sync columns
  button to retrieve the schema of the previous component.
* Save your Job and press F6 to execute it.

The data in error are sent to the delimited file, as well as the error
type met. Here, we have: Data truncation.

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-tfileinputdelimited-updating-data-using-tmysqloutput-standard-component-this -->
# Updating data using tMysqlOutput

Last updated: 9/30/2026

This Java scenario describes a two-component Job that updates data in a MySQL table
according to that in a delimited file.

* Drop tFileInputDelimited and
  tMysqlOutput (displayed as
  tDBOutput\_1) from the Palette onto the design workspace.
* Connect the two components together using a Row
  Main link.

* Double-click tFileInputDelimited to display
  its Basic settings view and define the
  component properties.
* From the Property Type list, select Repository if you have already stored the metadata of
  the delimited file in the Metadata node in the
  Repository tree view. Otherwise, select
  Built-In to define manually the metadata of
  the delimited file.

  For more information about storing metadata, see [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).

* Click the [...] button next to the File name/Stream field and browse to the source
  delimited file that contains the modifications to propagate in the MySQL table.

  In this example, we use the *customer\_update* file that
  holds four columns: *id*, *CustomerName*,
  *CustomerAddress* and *idState*. Some
  of the data in these four columns is different from that in the MySQL
  table.

* Define the row and field separators used in the source file in the
  corresponding fields.
* If needed, set Header, Footer and Limit.

  In this example, Header is set to 1 since the
  first row holds the names of columns, therefore it should be ignored. Also, the
  number of processed lines is limited to 2000.
* Click the [...] button next to Edit Schema to open a dialog box where you can
  describe the data structure of the source delimited file that you want to pass to the
  component that follows.

* Select the Key check box(es) next to the
  column name(s) you want to define as key column(s).

Information noteNote:

It is necessary to define at least one column as a key column for the Job to be
executed correctly. Otherwise, the Job is automatically interrupted and an error
message displays on the console.

* In the design workspace, double-click tDBOutput\_1 to open its Basic
  settings view where you can define its properties.

* Click Sync columns to retrieve the schema of
  the preceding component. If needed, click the [...] button next to Edit schema to open a dialog box where you can check
  the retrieved schema.
* From the Property Type list, select Repository if you have already stored the connection
  metadata in the Metadata node in the Repository tree view. Otherwise, select Built-In to define manually the connection
  information.

  For more information about storing metadata, see [Managing metadata in Talend Studio](https://help.qlik.com/talend/en-US/studio-user-guide/8.0/managing-metadata-in-studio).
* Fill in the database connection information in the corresponding
  fields.
* In the Table field, enter the name of the
  table to update.
* From the Action on table list, select the
  operation you want to perform, Default in this
  example since the table already exists.
* From the Action on data list, select the
  operation you want to perform on the data, Update in this example.
* Save your Job and press F6 to execute it.

Using you DB browser, you can verify if the MySQL table, *customers,*has been modified according to the delimited file.

In the above example, the database table has always the four columns
*id*, *CustomerName*,
*CustomerAddress* and *idState*, but certain
fields have been modified according to the data in the delimited file used.

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-trowgenerator-trowgenerator-inserting-column-and-altering-data-using-tmysqloutput-standard-component-this -->
# Inserting a column and altering data using tMysqlOutput

Last updated: 9/30/2026

This Java scenario is a three-component Job that aims at creating random data using a
tRowGenerator, duplicating a column to be altered
using the tMap component, and eventually altering the
data to be inserted based on an SQL expression using the tMysqlOutput component.

* Drop the following components from the Palette onto the design workspace: tRowGenerator, tMap and
  tMySQLOutput.
* Connect tRowGenerator, tMap, and tMysqlOutput using
  the Row Main link.

* In the design workspace, select tRowGenerator to display its Basic
  settings view.

* Click the [...] button next to Edit schema to define the data to pass on to the
  tMap component, two columns in this
  scenario, *name* and *random\_date*.

* Click OK to close the dialog box.
* Click the [...] button next to RowGenerator Editor to open the editor and define the
  data to be generated.

* Click in the corresponding Functions fields
  and select a function for each of the two columns, getFirstName for
  the first column and getrandomDate for the second column.
* In the Number of Rows for Rowgenerator
  field, enter 10 to generate ten first name rows and click Ok to close the editor.
* Double-click the tMap component to open the
  Map editor. The Map editor opens displaying the input metadata of the tRowGenerator component.

* In the Schema editor panel of the Map
  editor, click the plus button of the output table to add two rows and define the
  first as *random\_date* and the second as
  *random\_date1*.

In this scenario, we want to duplicate the *random\_date* column and
adapt the schema in order to alter the data in the output component.

* In the Map editor, drag the *random\_date* row from the
  input table to the *random\_date* and *random\_date1*rows in the output table.

* Click OK to close the editor.
* In the design workspace, double-click the tMysqlOutput component to display its Basic settings view and set its parameters.

* Set Property Type to Repository and then click the [...] button to open the
  Repository content dialog box and select
  the correct DB connection. The connection details display automatically in the
  corresponding fields.

  Information noteNote:

  If you have not stored the DB connection details in the Metadata entry in the Repository, select Built-in
  on the property type list and set the connection detail manually.
* Click the [...] button next to the Table
  field and select the table to be altered, *Dates* in this
  scenario.
* On the Action on table list, select
  Drop table if exists and create, select
  *Insert* on the Action on
  data list.
* If needed, click Sync columns to synchronize
  with the columns coming from the tMap
  component.
* Click the Advanced settings tab to display
  the corresponding view and set the advanced parameters.

* In the Additional Columns area, set the
  alteration to be performed on columns.

  In this scenario, the *One\_month\_later* column replaces
  *random\_date\_1*. Also, the data itself gets altered using
  an SQL expression that adds one month to the randomly picked-up date of the
  *random\_date\_1* column. ex: 2007-08-12 becomes
  2007-09-12.

  -Enter *One\_Month\_Later* in the Name cell.

  -In the SQL expression cell, enter the
  relevant addition script to be performed, "adddate(Random\_date, interval 1
  month)" in this scenario.

  -Select Replace on the Position list.

  -Enter *Random\_date1* on the Reference column list.

Information noteNote:

For this Job we duplicated the *random\_date\_1* column in the DB
table before replacing one instance of it with the
*One\_Month\_Later* column. The aim of this workaround was to
be able to view upfront the modification performed.

* Save your Job and press F6 to execute
  it.

The new *One\_month\_later* column replaces the
*random\_date1* column in the DB table and adds one month to each
of the randomly generated dates.

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-updating-database-table-using-tmysqloutput-in-big-data-streaming-job-this -->
# Updating a database table using tMysqlOutput in a Big Data Streaming Job

Last updated: 9/30/2026

This scenario applies only to Talend Real-Time Big Data Platform and
Talend Data Fabric.

This scenario describes a Big Data Streaming Job that updates data in specific
rows of a MySQL table once every five seconds.

### In this section

* [Establishing the Job](/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-establishing-job-create)
* [Selecting the Spark mode](/talend/en-US/components/8.0/mysql/selecting-spark-mode-spark-batch?id=3596)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/mysql/configuring-connection-to-file-system-to-be-used-by-spark?id=3598)
* [Configure the Job](/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-configure-job-open)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-executing-job-save)

**Related concepts**  

* [tMysqlOutput](tmysqloutput "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-configure-job-open -->
# Configure the Job

Last updated: 9/30/2026

## Procedure

1. Open the Basic settings view of
   tRowGenerator.
2. Define the schema for the table. 

   In this case, two columns are added:
   * Num, type integer, set as the key column
   * Cities, type string and length 20
3. Propagate the schema to the next component.
4. In RowGenerator Editor dialog box, set functions as
   follows.

   * Num: `Numeric.sequence`, with both start
     value and step set to
     `1`
   * Cities: `TalendDataGenerator.getUsCity()`
   * Number of Rows for RowGenerator:
     `10`

   Information noteNote: These settings specify to generate 10 rows of data at a time, with the
   Num values from 1 to 10.
5. Set Input repetition interval to
   `5000`.
6. Open the Basic settings view of
   tMysqlOutput.
7. Set the database table parameters. In this example, database is locally
   installed.

   Information noteNote: To make sure the table is updated properly, it is recommended to select
   None for the Action on
   table option and Update for the
   Action on data option.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-establishing-job-create -->
# Establishing the Job

Last updated: 9/30/2026

## Procedure

1. Create a Big Data Streaming Job.
2. Drop tRowGenerator and
   tMysqlOutput from the Palette onto the design
   workspace.
3. Connect the two components using a Row > Main connection.

   tHDFSConfiguration is used in this scenario by Spark to connect
   to the HDFS system where the jar files dependent on the Job are transferred.

   In the Spark
   Configuration tab in the Run
   view, define the connection to a given Spark cluster for the whole Job. In
   addition, since the Job expects its dependent jar files for execution, you must
   specify the directory in the file system to which these jar files are
   transferred so that Spark can access these files:
   * Yarn mode (Yarn client or Yarn cluster):
     + When using Google Dataproc, specify a bucket in the
       Google Storage staging bucket
       field in the Spark configuration
       tab.
     + When using HDInsight, specify the blob to be used for Job
       deployment in the Windows Azure Storage
       configuration area in the Spark
       configuration tab.
     + When using Altus, specify the S3 bucket or the Azure
       Data Lake Storage for Job deployment in the Spark
       configuration tab.
     + When using on-premises distributions, use
       the configuration component corresponding to the file system
       your cluster is using. Typically, this system is HDFS and so
       use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
   * Standalone mode: use the
     configuration component corresponding to the file system your cluster is
     using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

     If you are using Databricks without any configuration component present
     in your Job, your business data is written directly in DBFS (Databricks
     Filesystem).

   Prerequisite: ensure that the Spark cluster has been
   properly installed and is running.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutput-trowgenerator-thdfsconfiguration-thdfsconfiguration-executing-job-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Save the Job.
2. Press F6 to execute it. 

   The data in row 1 through row 10 of the database table is updated once
   every five seconds.
