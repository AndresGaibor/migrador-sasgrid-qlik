<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/parquet/tfileoutputparquet · versión 8.0 -->
# tFileOutputParquet

Last updated: 9/30/2026

Receives records from the processing component placed ahead of it and
writes the records into Parquet format files.

### In this section

* [tFileOutputParquet Standard properties](/talend/en-US/components/8.0/parquet/tfileoutputparquet-standard-properties)
* [tFileOutputParquet properties for Apache Spark Batch](/talend/en-US/components/8.0/parquet/tfileoutputparquet-properties-for-apache-spark-batch)
* [tFileOutputParquet properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/parquet/tfileoutputparquet-properties-for-apache-spark-streaming)
* [tFileOutputParquet properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/parquet/tfileoutputparquet-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Processing Parquet data using Snowflake components](processing-parquet-data-using-snowflake-components "This scenario shows the way to load data from a Parquet file into a Snowflake table and to retrieve the data from the Snowflake table.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/parquet/tfileoutputparquet-properties-for-apache-spark-batch -->
# tFileOutputParquet properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tFileOutputParquet running in the Spark Batch Job framework.

The Spark Batch
tFileOutputParquet component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. This component does not support the Object type and the   List type.  Spark automatically infers   data types for the columns in a PARQUET schema. In a Talend Job for Apache Spark, the Date type is inferred   and stored as int96.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder/File | Browse to, or enter the path pointing to the data to be used in the file system.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Action | Select an operation for writing data:  * Create: creates a file and write data in it. * Overwrite: overwrites the file existing in the   directory specified in the Folder field. * Append: add data to the existing file if data   already exists. * Ignore: leave the existing file as is if data   already exists. |
| Compression | By default, the Uncompressed option is active. But you can select the Gzip or the Snappy option to compress the output data. |
| Merge result to single file | Select this check box to merge the final *part* files into a single file and put that file in a specified directory.  Once selecting it, you need to enter the path to, or browse to the folder you want to store the merged file in. This directory is automatically created if it does not exist.  The following check boxes are used to manage the source and the target files:  * Remove source dir: select   this check box to remove the source files after the merge. * Override target file:   select this check box to override the file already existing in the target   location. This option does not override the folder.  If this component is writing merged files with a Databricks cluster, add the following parameter to the Spark configuration console of your cluster: ``` spark.sql.sources.commitProtocolClass org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol ``` This parameter prevents the merge file including the log file automatically generated by the DBIO service of Databricks.  If you select the Define column partition check box from the Advanced settings, you must clear the Remove source dir check box. The partitioning applies only to the unmerged files. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Define column partitions | Select this check box and complete the table that is displayed using columns from the schema of the incoming data. The records of the selected columns are used as keys to partition your data. |
| Sort columns alphabetically | Select this check box to sort the schema columns in the alphabetical order. If you leave this check box clear, these columns stick to the order defined in the schema editor. |
| Do not convert dates to UTC | Select this check box to store the dates using the local timezone of your Spark session. As Parquet does not contain any timezone information, if you leave this check box cleared, the UTC timezone is used by default. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/parquet/tfileoutputparquet-properties-for-apache-spark-structured-streaming -->
# tFileOutputParquet properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tFileOutputParquet
running in the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tFileOutputParquet component belongs to the File family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed. When you create a Spark Structured Streaming Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component does not support the Object type and the List type.  Spark automatically infers data types for the columns in a PARQUET schema. In a Talend Job for Apache Spark, the Date type is inferred and stored as int96. |
| Folder | Browse to or enter the path to the directory where the component writes Parquet files. To write to cloud storage, add the corresponding configuration component to the Job. For example, use tS3Configuration for Amazon S3, tGSConfiguration for Google Cloud Storage, or tAzureFSConfiguration for Azure Data Lake Storage. |
| Checkpoint location | Enter the path to the directory where Spark stores checkpoint data for the streaming query. Checkpointing enables fault tolerance and allows a failed query to resume from where it stopped. To use a cloud storage path, add the corresponding configuration component to the Job. For example, use tS3Configuration for Amazon S3, tGSConfiguration for Google Cloud Storage, or tAzureFSConfiguration for Azure Data Lake Storage. |
| Action | Select the write operation to apply to the output directory:  * Append: adds data to an existing directory, or   creates a new directory if none exists. * Overwrite: clears the existing data in the   Folder directory before writing data. The   checkpoint location is not cleared. |
| Compression | Select the compression format for the output Parquet files. By default, no compression is applied. Select Gzip or Snappy to compress the output data. |
| Set trigger | Select this check box to configure how often the streaming query processes data. When selected, choose one of the following trigger types:  * Available now: processes all available data in a   single batch, then stops the query. * Fixed interval: runs the query at a fixed time   interval. Enter the interval duration in the field that appears, for example   `10 seconds`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Define column partitions | Select this check box and complete the table that is displayed using columns from the schema of the incoming data. The records of the selected columns are used as keys to partition your data. |
| Sort columns alphabetically | Select this check box to sort the schema columns in the alphabetical order. If you leave this check box clear, these columns stick to the order defined in the schema editor. |
| Do not convert dates to UTC | Select this check box to store dates in the local time zone of your Spark session. As Parquet does not contain time zone information, if you leave this check box cleared, Spark uses UTC by default. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/parquet/tfileoutputparquet-standard-properties -->
# tFileOutputParquet Standard properties

Last updated: 9/30/2026

These properties are used to configure tFileOutputParquet running in the Standard
Job framework.

The Standard
tFileOutputParquet component belongs to the File family.

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
| File name | Name or path to the output file and/or the variable to be used.  For further information about how to define and use a variable in a Job, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Action | Select an operation for writing data:  Create: Creates a file and write data in it.  Overwrite: Overwrites the file if it already exists.. |
| Compression | By default, the Uncompressed option is active. But you can select the Gzip or the Snappy option to compress the output data. |
| Use external Hadoop dependencies | Select this check box to use external Hadoop dependencies and enter the path in the File name field respecting the following format: `"file:///path/out.parquet"`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Row group size (in bytes) | Set the row group size in bytes. |
| Page size (in bytes) | Set the page size in bytes. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  FILE\_PATH: the path pointing to the folder or the file being processed on Box. This is a Flow variable and it returns a string.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link. |
