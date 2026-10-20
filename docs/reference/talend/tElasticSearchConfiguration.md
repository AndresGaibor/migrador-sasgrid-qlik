<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elasticsearch/telasticsearchconfiguration · versión 8.0 -->
# tElasticSearchConfiguration

Last updated: 9/30/2026

Enables the reuse of the connection configuration to Elasticsearch in the same
Job.

tElasticSearchConfiguration provides Elasticsearch connection
information for the Elasticsearch components used in the same Spark Job. The Spark cluster
to be used reads this configuration to eventually connect to Elasticsearch.

### In this section

* [tElasticSearchConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/elasticsearch/telasticsearchconfiguration-properties-for-apache-spark-batch)
* [tElasticSearchConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/elasticsearch/telasticsearchconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elasticsearch/telasticsearchconfiguration-properties-for-apache-spark-batch -->
# tElasticSearchConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure
tElasticSearchConfiguration running in the Spark
Batch Job framework.

The Spark Batch
tElasticSearchConfiguration component belongs to the ElasticSearch family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Nodes | Enter the location of the cluster hosting the Elasticsearch system to be used. |
| Transport addresses and Cluster name | Enter empty double quotation marks ("") in these fields. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| User authentication | If the Elasticsearch system to be used requires authentication information, select this check box and enter the credentials. |
| Configuration | Add the parameters accepted by Elasticsearch to perform more customized actions.  For example, enter *es.mapping.id* in the Key column and *true* in the Value column to make the document field/property name contain the document ID. Note that you must put double quotation marks around the entered information.  For a list of the parameters you can use, see <https://www.elastic.co/guide/en/elasticsearch/hadoop/master/configuration.html>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  Drop tElasticSearchConfiguration along with the Elasticsearch-related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime.  * Note that the Talend components   support the Elasticsearch 6.4.x version for Spark Streaming Jobs, and Elasticsearch 7.x and   8.x versions for Spark Batch Jobs.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
