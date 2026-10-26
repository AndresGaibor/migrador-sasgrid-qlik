<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradataoutput · versión 8.0 -->
# tTeradataOutput

Last updated: 9/30/2026

Executes the action defined on the table and/or on the data contained in the table,
based on the flow incoming from the preceding component in the job.

tTeradataOutput writes, updates, makes
changes or suppresses entries in a database.

### In this section

* [tTeradataOutput Standard properties](/talend/en-US/components/8.0/teradata/tteradataoutput-standard-properties)
* [tTeradataOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/teradata/tteradataoutput-properties-for-apache-spark-batch)
* [tTeradataOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/teradata/tteradataoutput-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradataoutput-properties-for-apache-spark-batch -->
# tTeradataOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tTeradataOutput running in the Spark Batch Job framework.

The Spark Batch
tTeradataOutput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, the Job stops.  Update: Make changes to existing entries.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted.  Delete: Remove entries corresponding to the input flow. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error using a Row > Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  This is intended to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Use batch per partition | Select this check box to activate the batch mode for data processing. |
| Batch size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tTeradataConfiguration component present in the same Job to connect to Oracle. You need to select the Use an existing configuration check box and then select the tTeradataConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradataoutput-standard-properties -->
# tTeradataOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure
tTeradataOutput running in the Standard Job framework.

The
Standard
tTeradataOutput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | Information noteNote: The Action on table list will not be available if you select the Enable parallel execution check box in the Advanced settings view.  On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted. |
| Create | This is not visible by default, until you choose to create a table from the Action on table drop-down list. The table to be created may be:  * SET TABLE: tables which do not allow to   duplicate. * MULTI SET TABLE: tables allowing duplicate   rows. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, the Job stops.  Update: Make changes to existing entries. Information noteNote: In cases where all the schema columns are set as keys, this action yields an error and the Job fails.  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Update or insert: Update the record with the given reference. If the record does not exist, a new record would be inserted. Information noteNote: In cases where all the schema columns are set as keys, this action yields a warning message and the Job continues.  Delete: Remove entries corresponding to the input flow.  Information noteWarning: *It is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the Update and Delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column names you want to use as a base for the Update operation. Do the same in the Key in delete column for the Delete operation.*  Information noteNote: The dynamic schema feature can be used in the following modes: Insert; Update; Insert or update; Update or insert; Delete. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  This is intended to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Commit every | Enter the number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and, above all, better performance at execution.  This option is not available if you have selected the Use an existing connection check box in the Basic settings view.  Information noteNote: If you have selected Drop and create table, Create table, Create table if does not exist or Drop table if exists and create from the Action on table list in the Basic settings view, you need to enter *0* in this field to ensure the validity of the SQL statements. For more information about the validity of the SQL statements in Teradata Database, see [teradata](https://docs.teradata.com/search/all?query=load+and+unload+utilities). |
| Additional Columns | This option is not offered if you create (with or without drop) the DB table. This option allows you to call SQL functions to perform actions on columns, which are not insert, nor update or delete actions, or action that require particular preprocessing.  Name: Type in the name of the schema column to be altered or inserted as new column  SQL expression: Type in the SQL statement to be executed in order to alter or insert the relevant column data.  Position: Select Before, Replace or After following the action to be performed on the reference column.  Reference column: Type in a column of reference that the tDBOutput can use to place or replace the new or altered column. |
| Query band | Select this check box to use the Teradata Query Banding feature to add metadata to the query to be processed, such as the user running the query. This can help you, for example, identify the origin of this query.  Once selecting the check box, the Query Band parameters table is displayed, in which you need to enter the metadata information to be added. This information takes the form of key/value pairs, for example, *DpID* in the Key column and *Finance* in the Value column.  This check box actually generates the SET QUERY\_BAND FOR SESSION statement with the key/value pairs declared in the Query Band parameters table. For further information about this statement, see the [Teradata documentation](https://docs.teradata.com/search/all?query=End+logging+syntax).  This check box is not available when you have selected the Using an existing connection check box. In this situation, if you need to use the Query Band feature, set it in the Advanced settings tab of the Teradata connection component to be used. |
| Use field options | Select this check box to customize a request, especially when there is double action on data. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Use Batch | Select this check box to activate the batch mode for data processing. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.   * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a Teradata database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
