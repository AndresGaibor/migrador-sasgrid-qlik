<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elasticsearch/telasticsearchoutput · versión 8.0 -->
# tElasticSearchOutput

Last updated: 9/30/2026

Writes datasets into a given Elasticsearch system.

tElasticSearchOutput receives RDDs
(Resilient Distributed Datasets) from its preceding component and writes
(update or insert) them into Elasticsearch, a real-time distributed
search and analytics engine, by translating the contents of these
datasets into Elasticsearch documents.

### In this section

* [tElasticSearchOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/elasticsearch/telasticsearchoutput-properties-for-apache-spark-batch)
* [tElasticSearchOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/elasticsearch/telasticsearchoutput-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elasticsearch/telasticsearchoutput-properties-for-apache-spark-batch -->
# tElasticSearchOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tElasticSearchOutput running in the Spark Batch Job framework.

The Spark Batch
tElasticSearchOutput component belongs to the ElasticSearch family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Nodes | Enter the location of the cluster hosting the Elasticsearch system to be used. |
| Index | Enter the name of the index in which you want to write documents.  An index is the largest unit of storage in the Elasticsearch system. |
| Type | Enter the name of the type the documents to be written belong to.  For example, *blogpost\_en* and *blogpost\_fr* can be two types that represent given English blog posts and French blog posts, respectively.  You can dynamically uses the values of a given column to be document types. If you need to do so, enter the name of that column into a pair of braces (*{}*), for example, *{blog\_author}*. |
| Output document | Select how the document is written into Elasticsearch.  * JAVABEAN: if you select this option,   tElasticsearchOutput directly uses the   input schema to construct the JSON strings to be written.  For example, if a record with its schema reads as follows    ```   id name age   1  user 18   ```    the document outputted by   this JAVABEAN option is *{"id":1,"name":"user","age":18}*. * JSON: with this option, a read-only json\_document column is automatically added to the   output schema to receive JSON strings (documents in terms of Elasticsearch) from   its preceding components. This means you need to use tWriteJSONField in the same Job to construct JSON strings before   outputting them to tElasticsearchOutput. The   other columns of the schema can be used as metadata of these JSON   documents.  Since tWriteJSONField allows you to construct   JSON trees of different complexities, you can thus manage how the JSON strings   to be written should look like. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Document metadata | Complete this table to select the input columns to be used to provide metadata for each document. This table is typically used along with the json\_document option from the Output document drop-down list in the Basic settings view.  The Column column is automatically fed with the columns of the input schema. Then in the As metadata column, you need to select the check box(es) that correspond to the column(s) to be used.  In the Metadata type column, select which type of document metadata each column is used to provide.  For further information about the metadata types of an Elasticsearch document, see <https://www.elastic.co/guide/en/elasticsearch/guide/current/_document_metadata.html>. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| Configuration | Add the parameters accepted by Elasticsearch to perform more customized actions.  For example, enter *es.mapping.id* in the Key column and *true* in the Value column to make the document field/property name contain the document ID. Note that you must put double quotation marks around the entered information.  For a list of the parameters you can use, see <https://www.elastic.co/guide/en/elasticsearch/hadoop/master/configuration.html>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  Place a tElasticSearchConfiguration component in the same Job to connect to Elasticsearch. Then you need to select the Use an existing configuration check box and then select the tElasticSearchConfiguration component to be used.  * Note that the Talend components   support the Elasticsearch 6.4.x version for Spark Streaming Jobs, and Elasticsearch 7.x and   8.x versions for Spark Batch Jobs.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
