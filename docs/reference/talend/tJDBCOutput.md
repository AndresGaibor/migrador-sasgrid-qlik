<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcoutput · versión 8.0 -->
# tJDBCOutput

Last updated: 9/30/2026

Executes the action defined on the data contained in the table, based on the flow
incoming from the preceding component in the Job.

tJDBCOutput writes, updates, makes changes or suppresses
entries in any type of database connected to a JDBC API.

This component can be used to write data to a RDS MariaDB, a RDS PostgreSQL or a RDS SQLServer database.

### In this section

* [tJDBCOutput Standard properties](/talend/en-US/components/8.0/jdbc/tjdbcoutput-standard-properties)
* [tJDBCOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/jdbc/tjdbcoutput-properties-for-apache-spark-batch)
* [tJDBCOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/jdbc/tjdbcoutput-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcoutput-properties-for-apache-spark-batch -->
# tJDBCOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJDBCOutput running in the Spark Batch
Job framework.

The Spark Batch
tJDBCOutput component belongs to the Databases family.

This component can be used to write data to a RDS MariaDB, a RDS PostgreSQL or a RDS SQLServer database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`.  If you are using Spark V1.3, this URL should contain the authentication information, such as:  ``` jdbc:mysql://XX.XX.XX.XX:3306/Talend?user=ychen&password=talend ``` |
| Driver JAR | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Class Name | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| Username and Password | Enter the authentication information to the database you need to connect to.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available only for Spark V1.4. and onwards. |
| Table name | Name of the table to be written. Note that only one table can be written at a time. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Action on data | Select an action to be performed on data of the table defined.   * Insert:   Add new entries to the table. * Update:   Make changes to existing entries. * Insert or   update: Insert a new record. If the record with the given reference   already exists, an update would be made. * Update or   insert: Update the record with the given reference. If the record does   not exist in the index pool, a new record would be inserted. * Delete:   Remove entries corresponding to the input flow.   The following actions are only available if you use your component with Dataset API:   * Append: Add data to the existing table if   data already exists. * Overwrite: Overwrites the data in the   existing table. * ErrorIfExists: Show an exception if data   already exists. * Ignore: Leave the existing file as is if data   already exists. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Left protected char and Right protected char | Enter the symbol reserved by the database you are using, the left part in Left protected char and the right part in Right protected char, so that tJDBCOutput can generate SQL expressions with this reserved symbol properly placed.  For example, if you are using Oracle, double quotation marks (") are reserved for object names and so you need to enter the left and the right marks in these fields, respectively. Then at runtime, tJDBCOutput places double quotations marks around object names such as a table name. |
| Additional Columns | * This option allows you to call SQL functions to perform actions on columns,   provided that these are not insert, update or delete actions, or actions that require   pre-processing. This option is not available if you have just created the database table (even   if you delete it beforehand). Click the [+] button under   the table to add column(s), and set the following parameters for each column. * Name: Type in the name of the schema column to be altered   or inserted. * SQL expression: Type in the SQL statement to be executed in   order to alter or insert the data in the corresponding column. * Position: Select Before,   Replace or After,   depending on the action to be performed on the reference column. * Reference column: Type in a reference column that the   current component can use to locate or replace the new column, or the column to be   modified. |
| Use field options | Select the check box for the corresponding column to customize a request, particularly if multiple actions are being carried out on the data.   * Key in update: Select the check box for   the corresponding column based on which the data is updated. * Key in delete: Select the check box for   the corresponding column based on which the data is deleted. * Updatable: Select the check box if the   data in the corresponding column can be updated. * Insertable: Select the check box if the   data in the corresponding column can be inserted. |
| Use Batch | Select this check box to activate the batch mode for data processing.  This check box is available only when the Insert, the Update or the Delete option is selected from the Action on data list in the Basic settings view. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available only when the Use batch mode check box is selected. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tJDBCConfiguration component present in the same Job to connect to a database. You need to drop a tJDBCConfiguration component alongside this component and configure the Basic settings of this component to use tJDBCConfiguration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcoutput-standard-properties -->
# tJDBCOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure tJDBCOutput running in the Standard Job framework.

The Standard
tJDBCOutput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Component list | Select the component that opens the database connection to be reused by this component. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`. |
| Drivers | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Driver Class | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| User Id and Password | The database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Enter the name of the table into which data will be written. |
| Data Action | Select an action to be performed on data of the table defined.   * Insert: Add   new entries to the table. If duplicates are found, the Job stops. * Update:   Make changes to existing entries. * Insert or   update: Insert a new record in the index pool. If the record with the   given reference already exists, an update would be made. * Update or   insert: Update the record with the given reference. If the record does   not exist in the index pool, a new record would be inserted. * Delete:   Remove entries corresponding to the input flow.   Information noteWarning: It is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). For an advanced use, click the Advanced settings view where you can simultaneously define primary keys for the Update and Delete operations. To do that: Select the Use field options check box and then in the Key in update column, select the check boxes next to the column names you want to use as a base for the Update operation. Do the same in the Key in delete column for the Delete operation. |
| Clear data in table | Select this check box to clear data in the table before performing the action defined. Note that this option conflicts with the Enable parallel execution option: these two options should not be enabled concurrently. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess Schema | Click this button to generate schema columns based on the settings of database table columns. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This property is not available when other connection component is selected from the Connection Component dropdown list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Commit every | Specify the number of rows to be processed before committing batches of rows together into the database.  This option ensures transaction quality (but not rollback) and, above all, better performance at executions.  When used with an existing JDBC connection, tJDBCOutput ignores this option at runtime. |
| Additional Columns | This option allows you to call SQL functions to perform actions on columns, which are not insert, update or delete actions, or actions that require particular preprocessing. It is not offered if you create (with or without drop) the database table.   * Name: The name of the schema column to be inserted, or the   name of the schema column used to replace an existing column. * SQL expression: The SQL statement to be executed in order to   insert or replace relevant column. * Position: Select `Before`,   `After`, or `Replace` according to the   action to be performed on the reference column. * Reference column: The name of the reference column that can   be used to locate the new column to be inserted or that will be replaced. |
| Use field options | Select this check box and in the Fields options table displayed, select the check box for the corresponding column to customize a request, particularly if multiple actions are being carried out on the data.   * Key in update: Select the check box for the   corresponding column based on which data is updated. * Key in delete: Select the check box for the   corresponding column based on which data is deleted. * Updatable: Select the check box if data in the   corresponding column can be updated. * Insertable: Select the check box if data in   the corresponding column can be inserted. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use batch | Select this check box to activate the batch mode for data processing, and in the Batch Size field displayed, specify the number of records to be processed in each batch. |
| Use query timeout | Select this option to set a timeout period for the query or the batch query. The Job will be terminated if the query or the batch query is timed out. You can set the timeout period (in seconds) in the Timeout field.  Information noteNote:  * It varies with the driver implementations whether this option applies to an   individual SQL statement or a set of SQL statements (that is, a batch   query). Refer to your driver vendor documentation for details. * This option is available only when you have installed the R2021-12   Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing by treating multiple data flows simultaneously. This feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. With this check box selected, you need to specify the number of parallel executions desired in the Number of parallel executions field displayed.  Information noteNote:  * When parallel execution is enabled, it is not possible to use global   variables to retrieve return values. * This option conflicts with the Clear data in   table option: these two options should not be enabled   concurrently. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| NB\_LINE\_INSERTED | The number of rows inserted. This is an After variable and it returns an integer. |
| NB\_LINE\_UPDATED | The number of rows updated. This is an After variable and it returns an integer. |
| NB\_LINE\_DELETED | The number of rows deleted. This is an After variable and it returns an integer. |
| NB\_LINE\_REJECTED | The number of rows rejected. This is an After variable and it returns an integer. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the database query and covers all of the SQL queries possible.  This component must be used as an output component. It allows you to carry out actions on a table or on the data of a table in a JDBC database. It also allows you to create a reject flow using a Row > Rejects link to filter data in error. For an example of tMysqlOutput in use, see [Retrieving data in error with a Reject link](/talend/en-US/components/8.0/mysql/tmysqloutput-tmap-tfileoutputdelimited-tfileinputdelimited-retrieving-data-in-error-with-reject-link-standard-component-this). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
