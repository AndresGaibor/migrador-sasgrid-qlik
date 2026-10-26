<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveoutput · versión 8.0 -->
# tHiveOutput

Last updated: 9/30/2026

Connects to a given Hive database and writes the data it receives into a given Hive
table or a directory in HDFS.

Hive allows you to access external tables from Spark but does not support ACID
transactions.

When ACID is enabled on the Hive side, a Spark Job cannot delete
or update a table and unless data is compacted, this Job cannot correctly read
aggregated data from a Hive table, either. This is a known limitation described in
the [Spark bug tracking system](https://issues.apache.org/jira/browse/SPARK-15348).

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tHiveOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/hive/thiveoutput-properties-for-apache-spark-batch)
* [tHiveOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/hive/thiveoutput-properties-for-apache-spark-streaming)
* [tHiveOutput properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/hive/thiveoutput-properties-for-apache-spark-structured-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveoutput-properties-for-apache-spark-batch -->
# tHiveOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tHiveOutput running in the Spark Batch Job framework.

The Spark Batch
tHiveOutput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

Information noteImportant:
Talend does not support the import of schema for complex data types
such as array, struct, and map.

## Basic settings

| Properties | Description |
| --- | --- |
| Hive storage configuration | Select the tHiveConfiguration component from which you want Spark to use the configuration details to connect to Hive.  If you are running your Spark Job on Spark Universal with Yarn Cluster mode, this property is not available. The Hive storage configuration directly comes from the XML files inside the Hadoop configuration JAR file. For more information, see [Defining Yarn cluster connection parameters with Spark Universal](/talend/r/en-US/8.0/studio-user-guide/defining-yarn-cluster-connection-parameters-with-spark-universal). |
| HDFS Storage configuration | Select the tHDFSConfiguration component from which you want Spark to use the configuration details to connect to a given HDFS system and transfer the dependent jar files to this HDFS system. This field is relevant only when you are using an on-premises distribution.  If you are running your Spark Job on Spark Universal with Yarn Cluster mode, this property is not available. The HDFS storage configuration directly comes from the XML files inside the Hadoop configuration JAR file. For more information, see [Defining Yarn cluster connection parameters with Spark Universal](/talend/r/en-US/8.0/studio-user-guide/defining-yarn-cluster-connection-parameters-with-spark-universal). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Output source | Select the type of the output data you want tHiveOutput to change:   * Hive table: the Database field, the Table name field, the Table format list and the Enable   Hive partitions check box are displayed. You need to enter   the related information about the Hive database to be connected to and the   Hive table you need to modify.  By default, the format of the output data is JSON, but you can   change it to ORC or Parquet by selecting the corresponding option from the   Table format list. |
| Save mode | Select the type of changes you want to make regarding the target Hive table:  * Create: creates the target Hive table and writes data   in this table. * Append: adds data to an existing table. * Overwrite: overwrites the data of the existing   table. * Create if it does not exist: creates a Hive table   and adds data in it if there is no existing table. If there is an existing   table, the input data is not saved. This property is available when you   have installed the 8.0.1-R2024-03 Studio Monthly or a later one provided   by Talend. For more information, check with your administrator. |
| Enable Hive partitions | Select the Enable Hive partitions check box and in the Partition keys table, define partitions for the Hive table you are creating or changing. In the Partition keys table, select columns from the input schema of tHiveOutput to use as partition keys.  Bear in mind that:  * When the Save mode to be used is   `Append`, meaning that you are   adding data to an existing Hive table, the partition columns   you select in the Partition keys   table must be already partition keys of the Hive table to be   updated. * A partitioned Hive table created by tHiveOutput can only be read   by tHiveInput due to Spark specific   limitations. If you need to read your partitioned table   through Hive itself, it is recommended to use   tHiveRow or   tHiveCreateTable in a Standard Job to   create this table and then use tHiveOutput to append data to it. * Defining columns as partition keys does not alter your data   but only create subfolders using the partition keys and put   data in them. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Sort columns alphabetically | Select this check box to sort the schema columns in the alphabetical order. If you leave this check box clear, these columns stick to the order defined in the schema editor. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component should use a tHiveConfiguration component present in the same Job to connect to Hive.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hive/thiveoutput-properties-for-apache-spark-structured-streaming -->
# tHiveOutput properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tHiveOutput running in
the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tHiveOutput component belongs to the Databases family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

Information noteImportant:
Talend does not support the import of schema for complex data types such as
array, struct, and map.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the file path and the schema will be set.   * Built-In: The file path and the schema will be   set locally for this component. * Repository: The file details stored centrally   in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   file to be reused, and all related properties will be automatically   filled in. |
| External table | Select this check box to write data to an external Hive table. When selected, the Table property changes to Path, and Spark writes data directly in the configured format without using Hive's table management. |
| Table / Path | When External table is cleared, enter the name of the Hive table to write to. When External table is selected, enter the path to the output directory. |
| Format | Select the file format for the output data. The default format is parquet. |
| Output mode | Append: adds rows to the output table without modifying existing rows. Information noteRestriction: In Spark Structured Streaming Jobs, tHiveOutput supports only the Append output mode. The Complete and Update modes are not supported for file-based sinks in Structured Streaming. |
| Checkpoint location | Enter the path to the directory where Spark stores the checkpoint data for this streaming query. Checkpointing enables fault tolerance and allows a failed query to resume from where it stopped. |
| Set trigger | Select this check box to configure how often the streaming query processes data. When selected, choose one of the following trigger types:  * Available now: processes all available data in a   single batch, then stops the query. * Fixed interval: runs the query at a fixed time   interval. Enter the interval duration in the field that appears, for example   `10 seconds`. |
| Set query name | Select this check box to assign a name to the streaming query. In the Query name field, enter the name. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used as an end component and requires an input link.  This component should use a tHiveConfiguration component present in the same Job to connect to Hive.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |
