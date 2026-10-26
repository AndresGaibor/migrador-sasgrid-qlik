<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/avro/tavrooutput · versión 8.0 -->
# tAvroOutput

Last updated: 9/30/2026

Receives data flows from the processing component placed ahead of it and writes
the data into Avro format files in a given distributed file system.

### In this section

* [tAvroOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/avro/tavrooutput-properties-for-apache-spark-batch)
* [tAvroOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/avro/tavrooutput-properties-for-apache-spark-streaming)
* [tAvroOutput properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/avro/tavrooutput-properties-for-apache-spark-structured-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/avro/tavrooutput-properties-for-apache-spark-batch -->
# tAvroOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tAvroOutput running in the Spark Batch Job framework.

The Spark Batch
tAvroOutput component belongs to the File family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property type | * Either Built-In or Repository. * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored.  The properties are stored centrally under the Hadoop   Cluster node of the Repository   tree.  The fields that come after are pre-filled in using the fetched   data.  For more information about the Hadoop   Cluster node, see [Managing Hadoop connection metadata](/talend/r/en-US/8.0/studio-user-guide/managing-hadoop-metadata). |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Folder | Browse to, or enter the path pointing to the data to be used in the file system.  This path must point to a folder rather than a file.  The button for browsing does not work with the Spark Local mode; if you are using the other Spark Yarn modes that Talend Studio supports with your distribution, ensure that you have properly configured the connection in a configuration component in the same Job. Use the configuration component depending on the filesystem to be used. |
| Action | Select an operation for writing data:  Create: Creates a file and write data in it.  Overwrite: Overwrites the file existing in the directory specified in the Folder field. |
| Compression | Select the Compress data blocks check box to compress the output data.  Hadoop provides different compression formats that help reduce the space needed for storing files and speed up data transfer. When reading a compressed file, Talend Studio needs to uncompress it before being able to feed it to the input flow. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use output schema compatible with AvroKeyValueOutputFormat | Select this check box to define a hierarchical key/value schema for the Avro file to be written. According to this schema, the current component embeds the columns of the input row into an output record with two fields, named *key* and *value*.  For this purpose, you need to specify the columns of the output data to be used as key fields in the table that is displayed.  For example, the following data is an Avro record written with this key/value structure:  ``` {    "key" : { "key1" : 1,  "key2" :  "Canada"},    "value" : { "value1" :  "maple syrup",  "value2" : 2015} } ``` |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/avro/tavrooutput-properties-for-apache-spark-structured-streaming -->
# tAvroOutput properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tAvroOutput running in
the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tAvroOutput component belongs to the File family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Define a storage configuration component | Select the configuration component to be used to provide the configuration information for the connection to the target file system such as HDFS.  If you leave this check box clear, the target file system is the local system.  The configuration component to be used must be present in the same Job. For example, if you have dropped a tHDFSConfiguration component in the Job, you can select it to write the result in a given HDFS system. |
| Property Type | Select the way the file path and the schema will be set.   * Built-In: The file path and the schema will be   set locally for this component. * Repository: The file details stored centrally   in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   file to be reused, and all related properties will be automatically   filled in. |
| Schema and Edit schema | A schema is a row description. It defines the fields (columns) processed by the component. When you create a Spark Job, avoid the reserved word `line` when naming fields.   * Built-In: create and store the schema locally for   this component only. * Repository: reuse a schema created and stored in   the Repository across projects and Job designs.   Click Edit schema to modify the schema. If you modify a Repository schema, the available options include:   * View schema: view the schema without modifying it. * Change to built-in property: change the schema to   Built-in for local changes. * Update repository connection: modify the Repository   schema and choose whether to propagate the changes to other Jobs. |
| Folder | Browse to or enter the path to the directory where the component writes Avro files. This path must point to a folder, not a file. To write to cloud storage, add the corresponding configuration component to the Job. For example, use tS3Configuration for Amazon S3, tGSConfiguration for Google Cloud Storage, or tAzureFSConfiguration for Azure Data Lake Storage. |
| Checkpoint location | Enter the path to the directory where Spark stores checkpoint data for the streaming query. Checkpointing enables fault tolerance and allows a failed query to resume from where it stopped. To use a cloud storage path, add the corresponding configuration component to the Job. For example, use tS3Configuration for Amazon S3, tGSConfiguration for Google Cloud Storage, or tAzureFSConfiguration for Azure Data Lake Storage. |
| Action | Select the write operation to apply to the output directory:  * Append: adds data to an existing directory, or   creates a new directory if none exists. * Overwrite: clears the existing data in the   Folder directory, then creates the output files   and writes data to them. The checkpoint location is not cleared. |
| Compression | Select this check box to compress the output data blocks, then select a compression codec from the drop-down list, for example Snappy or Deflate. If cleared, the output data is uncompressed. |
| Set trigger | Select this check box to configure how often the streaming query processes data. When selected, choose one of the following trigger types:  * Available now: processes all available data in a   single batch, then stops the query. * Fixed interval: runs the query at a fixed time   interval. Enter the interval duration in the field that appears, for example   `10 seconds`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Write empty batches | Select this check box to allow the Job to write an empty batch when the incoming micro-batch contains no data. This check box is selected by default. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |
