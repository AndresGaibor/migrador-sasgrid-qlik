<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tachyon/ttachyonconfiguration · versión 8.0 -->
# tTachyonConfiguration

Last updated: 9/30/2026

Defines a connection to Tachyon storage system and enables the reuse of the
configuration in the same Job.

You define a connection to Tachyon in tTachyonConfiguration and configure the file system
related components to reused this connection. At runtime, the Spark
cluster to be used reads this configuration to connect to
Tachyon.

### In this section

* [tTachyonConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/tachyon/ttachyonconfiguration-properties-for-apache-spark-batch)
* [tTachyonConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/tachyon/ttachyonconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tachyon/ttachyonconfiguration-properties-for-apache-spark-batch -->
# tTachyonConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tTachyonConfiguration running in the Spark Batch Job framework.

The Spark Batch
tTachyonConfiguration component belongs to the Storage family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Tachyon master URI | Enter the address of the master server of the Tachyon cluster to be used.  This information can be found in the *conf/tachyon-env.sh* file of your Tachyon system.  For details about the version compatibility between Tachyon and Spark, see Tachyon documentation at <http://tachyon-project.org/documentation/Running-Spark-on-Tachyon.html>. |
| UnderFS username | Enter the credential required by the file system (underlayer storage system in terms of Tachyon) used by your Tachyon cluster. The default file system is HDFS.  This information can be found in the *conf/tachyon-env.sh* file of your Tachyon system. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  You need to drop tTachyonConfiguration along with the file system related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
