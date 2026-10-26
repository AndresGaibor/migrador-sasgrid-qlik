<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/parquet/tfileinputparquet · versión 8.0 -->
# tFileInputParquet

Last updated: 9/30/2026

Extracts records from a given Parquet format file and sends the data to
the next component for further processing.

### In this section

* [tFileInputParquet Standard properties](/talend/en-US/components/8.0/parquet/tfileinputparquet-standard-properties)
* [tFileInputParquet properties for Apache Spark Batch](/talend/en-US/components/8.0/parquet/tfileinputparquet-properties-for-apache-spark-batch)
* [tFileInputParquet properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/parquet/tfileinputparquet-properties-for-apache-spark-streaming)

**Related concepts**  

* [Processing Parquet data using Snowflake components](processing-parquet-data-using-snowflake-components "This scenario shows the way to load data from a Parquet file into a Snowflake table and to retrieve the data from the Snowflake table.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/parquet/tfileinputparquet-properties-for-apache-spark-batch -->
# tFileInputParquet properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileInputParquet running in the Spark Batch Job framework.

The Spark Batch
tFileInputParquet component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component does not support the Object type and the   List type.  Spark automatically infers   data types for the columns in a PARQUET schema. In a Talend Job for Apache Spark, the Date type is inferred   and stored as int96.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  If the path you set points to a folder, this component will read all of the files stored in that folder, for example, /user/talend/in; if sub-folders exist, the sub-folders are automatically ignored unless you define the property spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive to be true in the Advanced properties table in the Spark configuration tab.  * Depending on the filesystem to be used, properly configure the corresponding   configuration component placed in your Job, for example, a   tHDFSConfiguration component for HDFS, a   tS3Configuration component for S3 and a   tAzureFSConfiguration for Azure Storage and Azure Data Lake   Storage.  If you want to specify more than one files or directories in this field, separate each path using a comma (,).  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Read binary as string | Select this check box to set spark.sql.parquet.binaryAsString to true, when needed. |
| Merge schema | Select this check box to allow Talend Studio to merge multiple Parquet files with different schemas that can be mutually compatible. For more information, see [Schema Merging](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#schema-merging) from the official Spark documentation. |
| Read dates in local timezone | Select this check box to use the local timezone of your Spark session. If you leave this check box cleared, the UTC timezone is used. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/parquet/tfileinputparquet-standard-properties -->
# tFileInputParquet Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileInputParquet running in the Standard
Job framework.

The Standard
tFileInputParquet component belongs to the File family.

Information noteNote: If you are using a Windows platform, make sure [Hadoop Winutils](https://github.com/cdarlint/winutils) and
[Microsoft Visual C++ 2010 Service Pack 1 Redistributable Package MFC Security
Update](https://www.microsoft.com/en-us/download/details.aspx?id=26999) are installed before using this component. The two links also give the installation information.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| File name | Name or path to the input file and/or the variable to be used.  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Use external Hadoop dependencies | Select this check box to use external Hadoop dependencies and enter the path in the File name field respecting the following format: `"file:///path/input.parquet"`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  FILE\_PATH: the path pointing to the folder or the file being processed on Box. This is a Flow variable and it returns a string.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Use this component to retrieve data from parquet files. This component also passes retrieved data to the subsequent component. |
