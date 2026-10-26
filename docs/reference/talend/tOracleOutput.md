<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleoutput · versión 8.0 -->
# tOracleOutput

Last updated: 9/30/2026

Writes, updates, makes changes or suppresses entries in an Oracle database.

tOracleOutput executes the action
defined on the table and/or on the data contained in the table, based on the flow incoming
from the preceding component in the Job.

### In this section

* [tOracleOutput Standard properties](/talend/en-US/components/8.0/oracle/toracleoutput-standard-properties)
* [tOracleOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/oracle/toracleoutput-properties-for-apache-spark-batch)
* [tOracleOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/oracle/toracleoutput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Populating an Oracle data warehouse](toracleoutput-toracleinput-tmap-toracleinput-tmap-populating-oracle-data-warehouse-standard-component-enterprise "The following Java scenario creates a three-component Job that populates a data warehouse. A tOracleInput component reads your client data stored in the CLIENT table. A tMap component allows you to modify this data and the modifications are transmitted to the Leadfact table in the database through a tOracleOutput component.")

**Related tasks**  

* [Using Oracle as a vector database](toracleconnection-toracleinput-toracleoutput-toracleclose-tfileinputdelimited-tmap-tlogrow-using-oracle-as-vector-db-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleoutput-properties-for-apache-spark-batch -->
# tOracleOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tOracleOutput running in the Spark Batch Job framework.

The Spark Batch
tOracleOutput component belongs to the Databases family.

This component can also be used to write data to a RDS Oracle database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Connection type | The available drivers are:   * Oracle OCI: Select this connection type   to use Oracle Call Interface with a set of C-language software APIs that provide   an interface to the Oracle database. * Oracle Custom: Select this connection   type to access a clustered database. With this type of connection, the   Username and the Password fields are deactivated and you need to   enter the connection URL in the URL field   that is displayed.  For further information about the valid form of this URL, see [JDBC Connection   strings](http://www.dba-resources.com/oracle/jdbc-connection-strings-for-oracle-thin-driver/) from the Oracle documentation. * Oracle Service Name: Select this   connection type to use the TNS alias that you give when you connect to the   remote database. * WALLET: Select this connection type to   store credentials in an Oracle wallet. * Oracle SID: Select this connection type   to uniquely identify a particular database on a system. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Oracle schema | Oracle schema name. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:  Default: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted.  Truncate table: The table content is deleted. You do not have the possibility to rollback the operation.  Truncate table with reuse storage: The table content is deleted. You do not have the possibility to rollback the operation. However, it is allowed to reuse the existing storage allocated to the table though the storage is considered empty.  Information noteWarning: If you select the Use an existing connection check box and select an option other than Default from the Action on table list, a commit statement will be generated automatically before the data insert/update/delete operation. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row > Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Use Batch | Select this check box to activate the batch mode for data processing. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tOracleConfiguration component present in the same Job to connect to Oracle. You need to select the Use an existing connection check box and then select the tOracleConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleoutput-standard-properties -->
# tOracleOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure
tOracleOutput running in the Standard Job framework.

The
Standard
tOracleOutput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository   . * Built-in: No property   data stored centrally. * Repository: Select the   repository file in which the properties are stored. The fields that   follow are completed automatically using the data   retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers.   * Oracle OCI: Select this   connection type to use Oracle Call Interface with a set of C-language   software APIs that provide an interface to the Oracle database. * Oracle Custom: Select this connection   type to access a clustered database. * Oracle   Service Name: Select this connection type to use the TNS   alias that you give when you connect to the remote database. * WALLET: Select this connection type to   store credentials in an Oracle wallet. * Oracle   SID: Select this connection type to uniquely identify a   particular database on a system. |
| DB Version | Select the Oracle version in use. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | Information noteNote: The Action on table list will not be available if you select the Enable parallel execution check box in the Advanced settings view.  On the table defined, you can perform one of the following operations.   * Default: No operation   is carried out. * Drop and create table:   The table is removed and created again. * Create   table: The table does not exist and gets created. * Create table if does not exist: The   table is created if it does not exist. * Drop table   if exists and create: The table is removed if it already   exists and created again. * Clear   table: The table content is deleted. * Truncate   table: The table content is deleted. You do not have the   possibility to rollback the operation. * Truncate   table with reuse storage: The table content is deleted.  You do not have the possibility to rollback the operation. However, it   is allowed to reuse the existing storage allocated to the table though   the storage is considered empty.   Information noteWarning: If you select the Use an existing connection check box and select an option other than Default from the Action on table list, a commit statement will be generated automatically before the data insert/update/delete operation. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, job stops.   * Update: Make   changes to existing   entries. Information noteNote: In cases where all the schema   columns are set as keys, this action yields an error and the Job fails. * Insert or   update: Insert a new record. If the record with the given reference   already exists, an update would be   made. Information noteNote: In cases where all the schema   columns are set as keys, this action yields a warning message and the Job   continues. * Update or   insert: Update the record with the given reference. If the record does   not exist, a new record would be   inserted. Information noteNote: In cases where all the schema   columns are set as keys, this action yields a warning message and the Job   continues. * Delete: Remove entries corresponding to   the input flow.   Information noteWarning: It is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the Update and Delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column names you want to use as a base for the Update operation. Do the same in the Key in delete column for the Delete operation.  Information noteNote: The dynamic schema feature can be used in the following modes: Insert; Update; Insert or update; Update or insert; Delete. |
| Schema and Edit schema | * A schema is a row   description, it defines the number of fields to be processed and passed   on to the next component. The schema is either Built-in or stored   remotely in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables.  When   writing data with Oracle Long type using dynamic schema feature, to   avoid data overflow during data type conversion, change the default   length in the length property of the mapping file for the Oracle Long   type or configure the length with dynamic metadata. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row>Rejects link. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This checkbox is not available when the Use an existing connection checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use alternate schema | Select this option to use a schema other than the one specified by the component that establishes the database connection (that is, the component selected from the Component list drop-down list in Basic settings view). After selecting this option, provide the name of the desired schema in the Schema field.  This option is available when Use an existing connection is selected in Basic settings view. |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings view.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Commit every | Enter the number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and, above all, better performance at execution. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Additional Columns | * This option is not   offered if you create (with or without drop) the DB table. This option   allows you to call SQL functions to perform actions on columns, which   are not insert, nor update or delete actions, or actions that require   particular preprocessing. * Name: Type in the name   of the schema column to be altered or inserted as new   column. * SQL expression: Type in   the SQL statement to be executed in order to alter or insert the   relevant column data. * Position: Select   Before,   Replace, or   After   following the action to be performed on the reference   column. * Reference column: Type   in a column of reference that the tDBOutput can use to place or replace   the new or altered column. |
| Use field options | Select this check box to customize a request, especially when there is double action on data. |
| Use Hint Options | Select this check box to activate the hint configuration area which helps you optimize a query's execution. In this area, parameters are:   * HINT: specify the hint you need, using the   syntax /\*+ \*/. * POSITION: specify where you put the hint in a SQL   statement. * SQL   STMT\*: select the SQL statement you need to   use. |
| Convert columns and table to uppercase | Select this check box to set the names of columns and table in upper case. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use Batch Size | Select this check box to activate the batch mode for data processing. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Support null in "SQL WHERE" statement | Select this check box to validate null in "SQL WHERE" statement. |
| Write BLOB values from a different DB | Select this option if the input data contains BLOB objects that are from a database other than the currently connected database. If this option is not selected, this component uses the input Oracle connection configuration to retrieve the input data. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | * NB\_LINE: the number   of rows read by an input component or transferred to an output component. This is an   After variable and it returns an integer. * NB\_LINE\_UPDATED: the number of rows updated.   This is an After variable and it returns an integer. * NB\_LINE\_INSERTED: the number of   rows inserted. This is an After variable and it returns an integer. * NB\_LINE\_DELETED: the   number of rows deleted. This is an After variable and it returns an integer. * NB\_LINE\_REJECTED: the number of rows rejected. This is an After   variable and it returns an integer. * QUERY: the query statement processed. This   is an After variable and it returns a string.   To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all of the SQL queries possible.  Row > Rejects This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in an Oracle database. It also allows you to create a reject flow using a link to filter data in error. For an example of tMysqlOutput in use, see [Retrieving data in error with a Reject link](/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleoutput-toracleinput-tmap-toracleinput-tmap-populating-oracle-data-warehouse-standard-component-enterprise -->
# Populating an Oracle data warehouse

Last updated: 9/30/2026

The following Java scenario creates a three-component Job that populates a data
warehouse. A tOracleInput component reads your client
data stored in the *CLIENT* table. A tMap component allows you to modify this data and the modifications are
transmitted to the *Leadfact* table in the database through a
tOracleOutput component.

### In this section

* [Procedure](/talend/en-US/components/8.0/oracle/toracleoutput-toracleinput-tmap-toracleinput-tmap-procedure-standard-component-enterprise-drop)

**Related concepts**  

* [tOracleInput](toracleinput "Reads an Oracle database and extracts fields based on a query.")
* [tOracleOutput](toracleoutput "Writes, updates, makes changes or suppresses entries in an Oracle database.")

**Related information**  

* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleoutput-toracleinput-tmap-toracleinput-tmap-procedure-standard-component-enterprise-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tOracleInput, tMap, and
   tOracleOutput.
2. Connect the three components using Row Main
   links. Click the link between tMap
   and tOracleOutput and name it
   *leadfact*.
3. Double-click tOracleInput to display its
   Basic settings view and define its
   properties.
4. Set Property Type to Repository and then select the connection to the
   *TALEND* database that holds the information about your
   clients. The connection details will display automatically in the corresponding
   fields.

   Information noteNote:

   If you have not stored the DB connection details in the Metadata entry in the Repository, select
   Built-in in the property type list and
   set the connection details manually.
5. Set Schema to Repository and click the [...] button to select the schema
   of the *CLIENT* table stored in the Metadata folder.
6. In the Table Name field, enter the name of
   the table holding the information you want to modify,
   *CLIENT* in this example.
7. Click Guess Query to retrieve all data from
   your table.
8. Double-click the tMap component to open the
   Map Editor. Notice that the input area to
   the left is already filled with the metadata of the input component.
9. Drag the fields in the input zone to the fields in the *leadfact*table in the output zone.
10. Click OK to validate the operation.
11. In the design workspace, double-click tOracleOutput to display its Basic
    settings view and define its properties.
12. Set Property Type to Repository and then select the *cdc\_data*
    connection to the data warehouse. The connection details will display
    automatically in the corresponding fields

    Information noteNote:

    If you have not stored the data warehouse connection details in the
    Metadata folder in the Repository tree view, select Built-in in the property type list and set the
    connection details manually.
13. In the Table Name field, enter the name of
    the table you want to populate with modified data, *LEADFACT*
    in this example.
14. Save your Job and press F6 to create and
    populate the *LEADFACT* table in the data warehouse.
