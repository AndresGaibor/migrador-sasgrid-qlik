<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kudu/tkuduconfiguration · versión 8.0 -->
# tKuduConfiguration

Last updated: 9/30/2026

Enables the reuse of the connection configuration to Cloudera Kudu in the same
Job.

tKuduConfiguration provides Kudu
connection information for the Kudu components used in the same Spark
Job. The Spark cluster to be used reads this configuration to eventually
connect to Kudu.

## tKuduConfiguration properties for Apache Spark Batch

These properties are used to configure tKuduConfiguration running in the Spark Batch Job framework.

The Spark Batch
tKuduConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Server connection | Click the [+] button to add as many rows as the Kudu masters you need to use, each row for a master. Then enter the locations and the listening ports of the master nodes of the Kudu service to be used.  This component supports only the Apache Kudu service installed on Cloudera.  For compatibility information between Apache Kudu and Cloudera, see the related Cloudera documentation: [Compatibility Matrix for Apache Kudu](https://www.cloudera.com/documentation/enterprise/release-notes/topics/rn_consolidated_pcm.html#pcm_kudu). |
| Kudu version | Select the version of Kudu used by your cluster from the drop-down list. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  Use it only when you need to connect to a Cloudera Kudu cluster. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |

**Related concepts**  

* [Writing and reading data from Cloudera Kudu using a Spark Batch Job](tkuduoutput-tkuduconfiguration-tmap-writing-and-reading-data-from-cloudera-kudu-using-spark-batch-job-the "In this scenario, you create a Spark Batch Job using the Kudu components to partition and write data in a Kudu table and then read some of the data from Kudu.")
