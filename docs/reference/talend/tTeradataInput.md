<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatainput · versión 8.0 -->
# tTeradataInput

Last updated: 9/30/2026

Executes a DB query with a strictly defined order which must correspond to the
schema definition.

tTeradataInput reads a database and
extracts fields based on a query. It passes on the field list to the next component via a
Main row link.

### In this section

* [tTeradataInput Standard properties](/talend/en-US/components/8.0/teradata/tteradatainput-standard-properties)
* [tTeradataInput properties for Apache Spark Batch](/talend/en-US/components/8.0/teradata/tteradatainput-properties-for-apache-spark-batch)

**Related concepts**  

* [Loading data into a Teradata database](tteradatatptexec-tteradatainput-tlogrow-loading-data-into-teradata-database-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatainput-properties-for-apache-spark-batch -->
# tTeradataInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tTeradataInput running in the Spark Batch Job framework.

The Spark Batch
tTeradataInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Table Name | Type in the name of the table from which you need to read data.  This field is only available when you select Table from the Read from drop-down list. |
| Read from | Select the type of the source of the data to be read.  * Table: tTeradataInput reads the   data of the table you specify in the Table name   field. * Query: tTeradataInput reads the   result of the query you write in the Query   field. |
| Query type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  If you are using Spark V2.0 onwards, the Spark SQL does not recognize the prefix of a database table anymore. This means that you must enter only the table name without adding any prefix that indicates for example the schema this table belongs to.  For example, if you need to perform a query in a table *system.mytable*, in which the *system* prefix indicates the schema that the *mytable* table belongs to, in the query, you must enter *mytable* only.  You can use push down predicate in the query to filter the data from the database. Spark supports the `Filter`operator.  These fields are only available when you select Query from the Read from drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters. |
| Spark SQL JDBC parameters | Add the JDBC properties supported by Spark SQL to this table. For a list of the user configurable properties, see [JDBC to other database](https://spark.apache.org/docs/latest/sql-programming-guide.html#jdbc-to-other-databases).  This component automatically set the *url*, *dbtable* and *driver* properties by using the configuration from the Basic settings tab. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Enable partitioning | Select this check box to read data in partitions.  Define, in double quotation marks, the following parameters to configure the partitioning:  * Partition column: the numeric column   used as partition key. * Lower bound of the partition stride   and Upper bound of the partition   stride: enter the upper bounds and the lower bound to determine   the partition stride. These bounds do not filter the table rows. All rows in   the table are partitioned and returned. * Number of partitions: the number of   partitions into which the table rows are split. Each Spark worker handles only   one of the partitions at a time.  The average size of the partitions is the result of the difference between the upper bound and the lower bound divided by the number of partitions, that is to say, (upperBound - lowerBound)/partitionNumber, while the first and the last partitions also include all the other rows that are not contained in the other partitions.  For example, to partition 1000 rows into 4 partitions, if you enter 0 for the lower bound and 1000 for the upper bound, each partition will contain 250 rows and so the partitioning is even. If you enter 250 for the lower bound and 750 for the upper bound, the second and the third partition will each contain 125 rows and the first and the last partitions each 375 rows. With this configuration, the partitioning is skewed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tTeradataConfiguration component present in the same Job to connect to Oracle. You need to select the Use an existing configuration check box and then select the tTeradataConfiguration component to be used.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatainput-standard-properties -->
# tTeradataInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tTeradataInput running in the Standard Job framework.

The Standard
tTeradataInput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Table name | Browse to, or enter the name of the table to be used. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  *If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected.* |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Query band | Select this check box to use the Teradata Query Banding feature to add metadata to the query to be processed, such as the user running the query. This can help you, for example, identify the origin of this query.  Once selecting the check box, the Query Band parameters table is displayed, in which you need to enter the metadata information to be added. This information takes the form of key/value pairs, for example, *DpID* in the Key column and *Finance* in the Value column.  This check box actually generates the SET QUERY\_BAND FOR SESSION statement with the key/value pairs declared in the Query Band parameters table. For further information about this statement, see the [Teradata documentation](https://docs.teradata.com/search/all?query=End+logging+syntax).  This check box is not available when you have selected the Using an existing connection check box. In this situation, if you need to use the Query Band feature, set it in the Advanced settings tab of the Teradata connection component to be used. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for Teradata databases. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
