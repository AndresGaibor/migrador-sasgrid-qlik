<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/elasticsearch/telasticsearchinput · versión 8.0 -->
# tElasticSearchInput

Last updated: 9/30/2026

Reads documents from a given Elasticsearch system based on a user-defined
query.

tElasticSearchInput reads Elasticsearch documents from the Elasticsearch
system based on user-defined queries, translates the documents into RDDs (Resilient
Distributed Datasets) and sends the RDDs to the Job.

Only one query is allowed per tElasticSearchInput.

## tElasticSearchInput properties for Apache Spark Batch

These properties are used to configure tElasticSearchInput running in the Spark Batch Job framework.

The Spark Batch
tElasticSearchInput component belongs to the ElasticSearch family.

This component is available in all Talend products
with Big Data and in Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of the data outputted by this component is read-only, *id\_document* and *json\_document*. The *json\_document* column contains the body of the documents read from ElasticSearch. If you need to explore data from this *json\_document* column, you have to use tExtractJSONFields to extract the data to be used. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Nodes | Enter the location of the cluster hosting the Elasticsearch system to be used. |
| Index | Enter the name of the index you want to read documents from.  An index is the largest unit of storage in the Elasticsearch system. |
| Type | Enter the name of the type the documents to be read belong to.  For example, *blogpost\_en* and *blogpost\_fr* can be two types that represent given English blog posts and French blog posts, respectively.  You can dynamically uses the values of a given column to be document types. If you need to do so, enter the name of that column into a pair of braces (*{}*), for example, *{blog\_author}*. |
| Query | Enter the Elasticsearch query to be performed by this component.  In editing queries, you need to use the syntax required by Elasticsearch along with escape characters required by Java, and put the query in double quotation marks.  For example, in the Elasticsearch documentation, an example query reads as follows:  ``` es.query = { "query" : { "term" : { "user" : "costinl" } } } ```  In this Query field, you should write the same query in the following way:  ``` "{ \"query\" : { \"term\" : {\"user\" : \"costinl\" } } }" ``` |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| Configuration | Add the parameters accepted by Elasticsearch to perform more customized actions.  For example, enter *es.mapping.id* in the Key column and *true* in the Value column to make the document field/property name contain the document ID. Note that you must put double quotation marks around the entered information.  For a list of the parameters you can use, see <https://www.elastic.co/guide/en/elasticsearch/hadoop/master/configuration.html>. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  Place a tElasticSearchConfiguration component in the same Job to connect to Elasticsearch. Then you need to select the Use an existing configuration check box and then select the tElasticSearchConfiguration component to be used.  * Note that the Talend components   support the Elasticsearch 6.4.x version for Spark Streaming Jobs, and Elasticsearch 7.x and   8.x versions for Spark Batch Jobs.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
