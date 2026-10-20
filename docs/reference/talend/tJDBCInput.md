<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcinput · versión 8.0 -->
# tJDBCInput

Last updated: 9/30/2026

Reads any database using a JDBC API connection and extracts fields based on a
query.

tJDBCInput executes a database query
with a strictly defined order which must correspond to the schema definition. Then it
passes on the field list to the next component via a Main row link.

### In this section

* [tJDBCInput Standard properties](/talend/en-US/components/8.0/jdbc/tjdbcinput-standard-properties)
* [tJDBCInput properties for Apache Spark Batch](/talend/en-US/components/8.0/jdbc/tjdbcinput-properties-for-apache-spark-batch)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcinput-properties-for-apache-spark-batch -->
# tJDBCInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tJDBCInput running in the Spark Batch Job
framework.

The Spark Batch
tJDBCInput component belongs to the Databases family.

This component also allows you to connect and read data from a RDS MariaDB, a RDS PostgreSQL or a RDS SQLServer database.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| JDBC URL | The JDBC URL of the database to be used. For example, the JDBC URL for the Amazon Redshift database is `jdbc:redshift://endpoint:port/database`.  If you are using Spark V1.3, this URL should contain the authentication information, such as:  ``` jdbc:mysql://XX.XX.XX.XX:3306/Talend?user=ychen&password=talend ``` |
| Driver JAR | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Class Name | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`. |
| Username and Password | Enter the authentication information to the database you need to connect to.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available only for Spark V1.4. and onwards. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Type in the name of the table from which you need to read data.  This field is only available when you select Table from the Read from drop-down list. |
| Read from | Select the type of the source of the data to be read.  * Table:   tJDBCInput   reads the data of the table you specify in the Table name field. * Query:   tJDBCInput   reads the result of the query you write in the Query field. |
| Query type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  If you are using Spark V2.0 onwards, the Spark SQL does not recognize the prefix of a database table anymore. This means that you must enter only the table name without adding any prefix that indicates for example the schema this table belongs to.  For example, if you need to perform a query in a table *system.mytable*, in which the *system* prefix indicates the schema that the *mytable* table belongs to, in the query, you must enter *mytable* only.  You can use pushdown predicate in the query to filter the data from the database. Spark supports the following operators:  * `Filter` * `Limit`  These fields are only available when you select Query from the Read from drop-down list. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Guess schema | Click the Guess schema button to retrieve the table schema. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Spark SQL JDBC parameters | Add the JDBC properties supported by Spark SQL to this table. For a list of the user configurable properties, see [JDBC to other database](https://spark.apache.org/docs/latest/sql-programming-guide.html#jdbc-to-other-databases).  This component automatically set the *url*, *dbtable* and *driver* properties by using the configuration from the Basic settings tab. |
| Trim all the String/Char columns | Select this check box to remove leading whitespace and trailing whitespace from all String/Char columns. |
| Trim column | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |
| Enable partitioning | Select this check box to read data in partitions.  Define, in double quotation marks, the following parameters to configure the partitioning:  * Partition column: the numeric column   used as partition key. * Lower bound of the partition stride   and Upper bound of the partition   stride: enter the upper bounds and the lower bound to determine   the partition stride. These bounds do not filter the table rows. All rows in   the table are partitioned and returned. * Number of partitions: the number of   partitions into which the table rows are split. Each Spark worker handles only   one of the partitions at a time.  The average size of the partitions is the result of the difference between the upper bound and the lower bound divided by the number of partitions, that is to say, (upperBound - lowerBound)/partitionNumber, while the first and the last partitions also include all the other rows that are not contained in the other partitions.  For example, to partition 1000 rows into 4 partitions, if you enter 0 for the lower bound and 1000 for the upper bound, each partition will contain 250 rows and so the partitioning is even. If you enter 250 for the lower bound and 750 for the upper bound, the second and the third partition will each contain 125 rows and the first and the last partitions each 375 rows. With this configuration, the partitioning is skewed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tJDBCConfiguration component present in the same Job to connect to a database. You need to drop a tJDBCConfiguration component alongside this component and configure the Basic settings of this component to use tJDBCConfiguration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jdbc/tjdbcinput-standard-properties -->
# tJDBCInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tJDBCInput running in the Standard Job framework.

The Standard
tJDBCInput component belongs to the Databases family.

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
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Table | Enter the name of the table from which data will be retrieved. |
| Query Type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.   * Built-In: Fill in the query statement in the Query field manually or click the [...] button next to the Query field to build the statement graphically using the SQLBuilder. * Repository: Select the relevant query stored in the Repository by clicking the [...] button next to it and in the pop-up Repository Content dialog box, select the query to be used, and the Query field will be automatically filled in.   If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected. |
| Guess Query | Click this button to generate query in the Query field based on the defined table and schema. |
| Guess Schema | Click this button to generate schema columns based on the query defined in the Query field. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  This property is not available when other connection component is selected from the Connection Component dropdown list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use cursor | Select this check box to specify the number of rows you want to work with at any given time. This option optimises performance. |
| Trim all the string/CHAR columns | Select this check box to remove leading whitespace and trailing whitespace from all String/Char columns. |
| Check column to trim | Select the check box for corresponding column to remove leading whitespace and trailing whitespace from it.  This property is not available when the Trim all the String/Char columns check box is selected. |
| Enable Mapping File for Dynamic | Select this check box to use the specified metadata mapping file when reading data from a dynamic type column. This check box is cleared by default.  With this check box selected, you can specify the metadata mapping file to use by selecting a type of database from the Mapping File drop-down list.  For more information about metadata mapping files, see [Accessing mapping files and defining type mappings](/talend/r/en-US/8.0/studio-user-guide/accessing-mapping-files-and-defining-type-mappings). |
| Use PreparedStatement | Select this check box if you want to query the database using a prepared statement. In the Set PreparedStatement Parameters table displayed, specify the value for each parameter represented by a question mark `?` in the SQL statement defined in the Query field.   * Parameter Index: the position of the parameter in the SQL   statement. * Parameter Type: the data type of the parameter. * Parameter Value: the value of the parameter.   For a related use case of this property, see [Using PreparedStatement objects to query data](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this). |
| Allow special character in dynamic table name | Select this option to use the actual column names of the input table in the dynamic column. This option prevents special characters (for example, `$`) in the input table column names from being converted into `_` in the dynamic column.  This option is selected by default. |
| Use query timeout | Select this option to set a timeout period for the query or the batch query. The Job will be terminated if the query or the batch query is timed out. You can set the timeout period (in seconds) in the Timeout field.  Information noteNote:  * It varies with the driver implementations whether this option applies to an   individual SQL statement or a set of SQL statements (that is, a batch   query). Refer to your driver vendor documentation for details. * This option is available only when you have installed the R2021-12   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for any database using a JDBC connection. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
