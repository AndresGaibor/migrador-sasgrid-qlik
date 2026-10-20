<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delta-lake/tdeltalakeinput · versión 8.0 -->
# tDeltaLakeInput

Last updated: 9/30/2026

Extracts the latest version or a given snapshot of records from the Delta Lake layer
of your Data Lake system and sends the data to the next component for further processing.

### In this section

* [tDeltaLakeInput Standard properties](/talend/en-US/components/8.0/delta-lake/tdeltalakeinput-standard-properties)
* [tDeltaLakeInput properties for Apache Spark Batch](/talend/en-US/components/8.0/delta-lake/tdeltalakeinput-properties-for-apache-spark-batch)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delta-lake/tdeltalakeinput-properties-for-apache-spark-batch -->
# tDeltaLakeInput properties for Apache Spark Batch

Last updated: 9/30/2026

Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta)

Beta content

These properties are used to configure tDeltaLakeInput running in the Spark Batch Job framework.

The Spark Batch
tDeltaLakeInput component belongs to the Technical family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define how to save the dataset | Select the dataset storage:  * Metastore: retrieves data in table format from a   metastore. * Unity Catalog: retrieves data in table format   from Unity Catalog. Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta) Beta content  Information noteNote: Select Unity Catalog when using the Databricks Serverless runtime. This option is required for compatibility with Databricks Serverless on AWS and Azure. * Files: retrieves data in delta format from   files. * Query: retrieves data from SQL queries. |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tS3Configuration component in the Job, you can select it to write the result in a given S3 storage system.  This field is available only when you select Files from the Define the source of the dataset drop-down list in the Basic settings view. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. Spark automatically infers   data types for the columns in a PARQUET schema. In a Talend Job for Apache Spark, the Date type is inferred   and stored as int96.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Database | Enter, in double quotation marks, the name of the Delta Lake database to be used. This field is available only when you select Metastore from the Define the source of the dataset drop-down list in the Basic settings view. |
| Table | Enter, in double quotation marks, the name of the table to be used. This field is available only when you select Metastore from the Define the source of the dataset drop-down list in the Basic settings view. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will read all of the files stored in that folder, for example, /user/talend/in; if sub-folders exist, the sub-folders are automatically ignored unless you define the property spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive to be true in the Advanced properties table in the Spark configuration tab.  * Depending on the filesystem to be used, configure the corresponding configuration   component placed in your Job, for example, a tS3Configuration component   for S3 and a tAzureFSConfiguration for Azure Storage and Azure Data   Lake Storage.  If you want to specify more than one files or directories in this field, separate each path using a comma (,).  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used.  This field is available only when you select Files from the Define the source of the dataset drop-down list in the Basic settings view. |
| SQL Query | Enter the SQL query you want to use to retrieve data. This field is available only when you select SQL Query from the Define the source of the dataset drop-down list in the Basic settings view. |
| Specify Time Travel timestamp | Select this check box to read a given timestamp-defined snapshot of the datasets to be used. The format used by Deltalake is yyyy-MM-dd HH:mm:ss.  Delta Lake systematically creates slight differences between the upload time of a file and the metadata timestamp of this file. Bear in mind these differences when you need to filter data.  This property is only available if you select Files from the Define how to save the dataset drop-down list. |
| Specify Time Travel version | Select this check box to read a versioned snapshot of the datasets to be used. This property is only available if you select Files from the Define how to save the dataset drop-down list. |
| Define how to read the dataset > Unity Catalog | When you retrieve dataset from Unity Catalog, you need to specify the Unity Catalog related information in the following parameters:  * Catalog: enter the name of the catalog to be   used. * Schema: enter the name of the schema to be   used. * Table: enter the name of the table to be used. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This Delta Lake layer is built on top of your Data Lake system, thus to be connected as part of your Data Lake system using the configuration component corresponding to your Data Lake system, for example, tAzureFSConfiguration. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the Google     Storage staging bucket field in the Spark     configuration tab.   + When using HDInsight, specify the blob to be used for Job deployment     in the Windows Azure Storage configuration area     in the Spark configuration tab.   + When using Altus, specify the S3 bucket or the Azure Data Lake Storage     for Job deployment in the Spark configuration     tab.   + When using on-premises distributions, use the configuration component     corresponding to the file system your cluster is using. * Standalone mode: use the configuration component   corresponding to the file system your cluster is using.  If you are using Databricks without any configuration component present in your   Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delta-lake/tdeltalakeinput-standard-properties -->
# tDeltaLakeInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tDeltaLakeInput running in the Standard Job framework.

The Standard
tDeltaLakeInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend
products.

If you have installed the 8.0.1-R2023-05 Talend Studio Monthly
update or a later one delivered by Talend, this
component generates error messages because of the conflicts between Log4j2 and Delta Lake
driver. You can prevent such kind of error messages by adding
EnableArrow=0 in the JDBC URL field.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved.   This property is not available when a connection component is selected with the Use an existing connection option. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings. |
| JDBC URL | The JDBC URL of the Delta Lake database to be used, which begins with `jdbc:spark://` (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the JDBC URL of the Delta Lake database begins with `jdbc:databricks//` (already presented).  See section Configure JDBC URL at [JDBC and ODBC drivers and configuration parameters](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#id7) for related information.  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks//`. |
| Drivers | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. The driver JAR SparkJDBC42-2.6.14.1018.jar is used for the Delta Lake databases (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the `databricks-jdbc-{version_number}.jar` driver will be used (already presented).  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver).  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update the driver and other related settings manually for existing Jobs to make sure `databricks-jdbc-{version_number}.jar` is used. |
| Driver class | Enter the class name for the specified driver between double quotation marks. For the `SparkJDBC42-2.6.14.1018.jar` driver, the name to be entered is `com.simba.spark.jdbc.Driver` (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the `databricks-jdbc-{version_number}.jar` driver will be used and the driver class to be entered is `com.databricks.client.jdbc.Driver` (already presented).  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update driver class and other related settings manually for existing Jobs to make sure the driver class `com.databricks.client.jdbc.Driver` is used. |
| User Id and Password | The database user authentication data. See section Username and password authentication at [JDBC and ODBC drivers and configuration parameters](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#id7) for related information.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Table | Enter the name of the table from which data will be retrieved. |
| Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.   * Built-In: Fill in the query statement in the Query field manually or click the [...] button next to the Query field to build the statement graphically using the SQLBuilder. * Repository: Select the relevant query stored in the Repository by clicking the [...] button next to it and in the pop-up Repository Content dialog box, select the query to be used, and the Query field will be automatically filled in.   If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected.  This component supports vector search capabilities, you can use this option to specify the query condition using the vector index previously created in Databricks.  For more information on vector searches in Databricks, see the corresponding [Databricks documentation](https://www.databricks.com/blog/introducing-databricks-vector-search-public-preview). |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Use cursor | Select this check box to specify the number of rows you want to work with at any given time. This option optimises performance. |
| Trim all the string/CHAR columns | Select this check box to remove leading whitespace and trailing whitespace from all String/Char columns. |
| Check column to trim | Select the check box for corresponding column to remove leading whitespace and trailing whitespace from it.  This property is not available when the Trim all the String/Char columns check box is selected. |
| Enable mapping file for dynamic | Select this check box to use the specified metadata mapping file when reading data from a dynamic type column. This check box is cleared by default.  With this check box selected, you can specify the metadata mapping file to use by selecting a type of database from the Mapping File drop-down list.  For more information about metadata mapping files, see [Accessing mapping files and defining type mappings](/talend/r/en-US/8.0/studio-user-guide/accessing-mapping-files-and-defining-type-mappings). |
| Allow special character in dynamic table name | Select this option to use the actual column names of the input table in the dynamic column. This option prevents special characters (for example, `$`) in the input table column names from being converted into `_` in the dynamic column.  This option is selected by default. |
| Use PreparedStatement | Select this check box if you want to query the database using a prepared statement. In the Set PreparedStatement Parameters table displayed, specify the value for each parameter represented by a question mark `?` in the SQL statement defined in the Query field.   * Parameter Index: the position of the parameter in the SQL   statement. * Parameter Type: the data type of the parameter. * Parameter Value: the value of the parameter.   For a related use case of this property, see [Using PreparedStatement objects to query data](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this). |
| Query timeout | Select this check box to set a timeout period for the query in seconds. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | * tDeltaLakeInput covers all possible SQL queries for   any database using a Delta Lake connection. * tDeltaLakeInput supports query vector capabilities,   you can use it to perform actions on vector embeddings. For more information   on vector search, see the corresponding [Databricks documentation](https://www.databricks.com/blog/introducing-databricks-vector-search-public-preview). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
