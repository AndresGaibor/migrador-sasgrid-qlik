<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsqlrow · versión 8.0 -->
# tSqlRow

Last updated: 9/30/2026

Performs SQL queries over input datasets.

tSqlRow registers
input RDDs (Resilient Distributed Datasets) as tables and applies queries on these
tables.

### In this section

* [tSqlRow properties for Apache Spark Batch](/talend/en-US/components/8.0/processing/tsqlrow-properties-for-apache-spark-batch)
* [tSqlRow properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/processing/tsqlrow-properties-for-apache-spark-streaming)

**Related concepts**  

* [Performing download analysis using a Spark Batch Job](tcacheout-textractdelimitedfields-ts3configuration-performing-download-analysis-using-spark-batch-job-spark-batch-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/processing/tsqlrow-properties-for-apache-spark-batch -->
# tSqlRow properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tSqlRow running in the Spark Batch Job framework.

The Spark Batch
tSqlRow component belongs to the Processing family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  With dynamic schema, you can read and query complex schema in Parquet files (containing struct and map for example) with the tSQLRow component using Spark SQL. |
| SQL context | Select the query languages you want tSqlRow to use.   * SQL Spark Context: the Spark native query language. * SQL Hive Context: the Hive query language supported by Spark.  In SQL Hive Context, tSqlRow does not allow you to use Hive metastore. If you need to read or write data to Hive metastore, use tHiveInput or tHiveOutput instead and in this situation, you need to design your Job differently.  For further information about the Spark supported Hive query statements, see [Supported Hive features](https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#supported-hive-features). * Spark Session: the Spark Session query language. Availability-note[Beta](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-beta) Beta content  Information noteNote: Select Spark Session when   using the Databricks Serverless runtime. This option is required   for compatibility with Databricks Serverless on AWS and   Azure. |
| Query | Enter your query paying particularly attention to properly sequence the fields in order to match the schema definition.  The tSqlRow component uses the label of its input link to name the registered table that stores the datasets from the same input link. For example, if a input link is labeled to *row1*, this *row1* is automatically the name of the table in which you can perform queries. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Register UDF jars | Add the Spark SQL or Hive SQL UDF (user-defined function) jars you want tSqlRow to use. If you do not want to call your UDF using its FQCN (Fully-Qualified Class Name), you must define a function alias for this UDF in the Temporary UDF functions table and use this alias. It is recommended to use the alias approach, as an alias is often more practical to use to call a UDF from the query.  Once you add one row to this table, click it to display the [...] button and then click this button to display the jar import wizard. Through this wizard, import the UDF jar files you want to use. |
| Temporary UDF functions | Complete this table to give each imported UDF class a temporary function name to be used in the query in tSqlRow.  If you have selected SQL Spark Context from the SQL context list, the UDF output type column is displayed. In this column, you need to select the data type of the output of the Spark SQL UDF to be used. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an intermediate step.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
