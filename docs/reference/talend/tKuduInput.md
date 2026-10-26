<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduinput · versión 8.0 -->
# tKuduInput

Last updated: 9/30/2026

Retrieves data from a Cloudera Kudu table and sends them to the component that
follows for transformation.

## tKuduInput properties for Apache Spark Batch

These properties are used to configure tKuduInput running in the Spark Batch Job framework.

The Spark Batch
tKuduInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Server connection | Click the [+] button to add as many rows as the Kudu masters you need to use, each row for a master. Then enter the locations and the listening ports of the master nodes of the Kudu service to be used.  This component supports only the Apache Kudu service installed on Cloudera.  For compatibility information between Apache Kudu and Cloudera, see the related Cloudera documentation: [Compatibility Matrix for Apache Kudu](https://www.cloudera.com/documentation/enterprise/release-notes/topics/rn_consolidated_pcm.html#pcm_kudu). |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Kudu version | Select the version of Kudu used by your cluster from the drop-down list. |
| Kudu table | Specify the name of the table from which you need to read data. |
| Query mode | Select the mode you want to use to read data from the table:  * Use scan: select this radio box to scan the whole   Kudu table. * Use query: select this radio box to display the   Query fields table. Then complete this table to   build the queries to be used. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Limit | Enter, without double quotation marks, the number of rows you want to display after the scan or the query of your Kudu table. This number does not change the number of rows to be actually scanned or queried. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |

**Related concepts**  

* [Writing and reading data from Cloudera Kudu using a Spark Batch Job](tkuduoutput-tkuduconfiguration-tmap-writing-and-reading-data-from-cloudera-kudu-using-spark-batch-job-the "In this scenario, you create a Spark Batch Job using the Kudu components to partition and write data in a Kudu table and then read some of the data from Kudu.")
