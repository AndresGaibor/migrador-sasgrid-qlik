<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/telasticsearchlookupinput · versión 8.0 -->
# tElasticSearchLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a Elasticsearch query with a strictly defined order which must correspond
to the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tElasticSearchLookupInput properties for Apache Spark Streaming

These properties are used to configure tElasticSearchLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tElasticSearchLookupInput component belongs to the ElasticSearch family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Transport addresses | Enter the addresses of the Elasticsearch nodes you need the component to connect to.  Different from tElasticSearchOutput which uses Elasticsearch Node Client, tElasticSearchLookupInput uses Elasticsearch Transport Client to connect to the Elasticsearch cluster. This allows tElasticSearchLookupInput to quickly create multiple connections to the cluster.  For further information about the Elasticsearch Node Client and the Elasticsearch Transport Client, see <https://www.elastic.co/guide/en/elasticsearch/guide/current/_transport_client_versus_node_client.html>. |
| Cluster name | Enter the name the Elasticsearch cluster to be used.  For further information about the Elasticsearch Node Client and the Elasticsearch Transport Client, see <https://www.elastic.co/guide/en/elasticsearch/guide/current/_transport_client_versus_node_client.html>. |
| Index | Enter the name of the index you want to read documents from.  An index is the largest unit of storage in the Elasticsearch system. |
| Type | Enter the name of the type the documents to be read belong to.  For example, *blogpost\_en* and *blogpost\_fr* can be two types that represent given English blog posts and French blog posts, respectively.  You can dynamically uses the values of a given column to be document types. If you need to do so, enter the name of that column into a pair of braces (*{}*), for example, *{blog\_author}*. |
| Query | Enter the Elasticsearch query to be performed by this component.  In editing queries, you need to use the syntax required by Elasticsearch along with escape characters required by Java, and put the query in double quotation marks.  For example, in the Elasticsearch documentation, an example query reads as follows:  ``` es.query = { "query" : { "term" : { "user" : "costinl" } } } ```  In this Query field, you should write the same query in the following way:  ``` "{ \"query\" : { \"term\" : {\"user\" : \"costinl\" } } }" ```  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Scroll time | Enter the time duration (in milliseconds) through which an input batch is progressively loaded from Elasticsearch.  This duration is useful only in case your query is bringing in huge batches. But since tMap in the Streaming mode reloads data at each row, an appropriately written query should avoid producing huge batches. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| Configuration | Add the parameters accepted by Elasticsearch to perform more customized actions.  For example, enter *es.mapping.id* in the Key column and *true* in the Value column to make the document field/property name contain the document ID. Note that you must put double quotation marks around the entered information.  For a list of the parameters you can use, see <https://www.elastic.co/guide/en/elasticsearch/hadoop/master/configuration.html>. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  Place a tElasticSearchConfiguration component in the same Job to connect to Elasticsearch. Then you need to select the Use an existing configuration check box and then select the tElasticSearchConfiguration component to be used.  * Note that the Talend components   support the Elasticsearch 6.4.x version for Spark Streaming Jobs, and Elasticsearch 7.x and   8.x versions for Spark Batch Jobs.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/telasticsearchlookupinput -->
# tElasticSearchLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Executes a Elasticsearch query with a strictly defined order which must correspond
to the schema definition.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

It passes on the extracted data to tMap in order to
provide the lookup data to the main flow. It must be directly connected to a tMap component and requires this tMap to use Reload at each row or Reload at each row (cache) for the lookup flow.

## tElasticSearchLookupInput properties for Apache Spark Streaming

These properties are used to configure tElasticSearchLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tElasticSearchLookupInput component belongs to the ElasticSearch family.

The component in this framework is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields. |
| Use an existing configuration | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Transport addresses | Enter the addresses of the Elasticsearch nodes you need the component to connect to.  Different from tElasticSearchOutput which uses Elasticsearch Node Client, tElasticSearchLookupInput uses Elasticsearch Transport Client to connect to the Elasticsearch cluster. This allows tElasticSearchLookupInput to quickly create multiple connections to the cluster.  For further information about the Elasticsearch Node Client and the Elasticsearch Transport Client, see <https://www.elastic.co/guide/en/elasticsearch/guide/current/_transport_client_versus_node_client.html>. |
| Cluster name | Enter the name the Elasticsearch cluster to be used.  For further information about the Elasticsearch Node Client and the Elasticsearch Transport Client, see <https://www.elastic.co/guide/en/elasticsearch/guide/current/_transport_client_versus_node_client.html>. |
| Index | Enter the name of the index you want to read documents from.  An index is the largest unit of storage in the Elasticsearch system. |
| Type | Enter the name of the type the documents to be read belong to.  For example, *blogpost\_en* and *blogpost\_fr* can be two types that represent given English blog posts and French blog posts, respectively.  You can dynamically uses the values of a given column to be document types. If you need to do so, enter the name of that column into a pair of braces (*{}*), for example, *{blog\_author}*. |
| Query | Enter the Elasticsearch query to be performed by this component.  In editing queries, you need to use the syntax required by Elasticsearch along with escape characters required by Java, and put the query in double quotation marks.  For example, in the Elasticsearch documentation, an example query reads as follows:  ``` es.query = { "query" : { "term" : { "user" : "costinl" } } } ```  In this Query field, you should write the same query in the following way:  ``` "{ \"query\" : { \"term\" : {\"user\" : \"costinl\" } } }" ```  The result of the query must contain only records that match join key you need to use in tMap. In other words, you must use the schema of the main flow to tMap to construct the SQL statement here in order to load only the matched records into the lookup flow.  This approach ensures that no redundant records are loaded into memory and outputted to the component that follows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Scroll time | Enter the time duration (in milliseconds) through which an input batch is progressively loaded from Elasticsearch.  This duration is useful only in case your query is bringing in huge batches. But since tMap in the Streaming mode reloads data at each row, an appropriately written query should avoid producing huge batches. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |
| Configuration | Add the parameters accepted by Elasticsearch to perform more customized actions.  For example, enter *es.mapping.id* in the Key column and *true* in the Value column to make the document field/property name contain the document ID. Note that you must put double quotation marks around the entered information.  For a list of the parameters you can use, see <https://www.elastic.co/guide/en/elasticsearch/hadoop/master/configuration.html>. |
| Connection pool | In this area, you configure, for each Spark executor, the connection pool used to control the number of connections that stay open simultaneously. The default values given to the following connection pool parameters are good enough for most use cases.   * Max total number of connections: enter the maximum number   of connections (idle or active) that are allowed to stay open simultaneously.  The default number is *8*. If you enter *-1*, you allow unlimited number of open connections at the same   time. * Max waiting time (ms): enter the maximum amount of time   at the end of which the response to a demand for using a connection should be returned by   the connection pool. By default, it is -1, that is to say, infinite. * Min number of idle connections: enter the minimum number   of idle connections (connections not used) maintained in the connection pool. * Max number of idle connections: enter the maximum number   of idle connections (connections not used) maintained in the connection pool. |
| Evict connections | Select this check box to define criteria to destroy connections in the connection pool. The following fields are displayed once you have selected it.   * Time between two eviction runs: enter the time interval   (in milliseconds) at the end of which the component checks the status of the connections and   destroys the idle ones. * Min idle time for a connection to be eligible to   eviction: enter the time interval (in milliseconds) at the end of which the idle   connections are destroyed. * Soft min idle time for a connection to be eligible to   eviction: this parameter works the same way as Min idle   time for a connection to be eligible to eviction but it keeps the minimum number   of idle connections, the number you define in the Min number of idle   connections field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  Place a tElasticSearchConfiguration component in the same Job to connect to Elasticsearch. Then you need to select the Use an existing configuration check box and then select the tElasticSearchConfiguration component to be used.  * Note that the Talend components   support the Elasticsearch 6.4.x version for Spark Streaming Jobs, and Elasticsearch 7.x and   8.x versions for Spark Batch Jobs.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
