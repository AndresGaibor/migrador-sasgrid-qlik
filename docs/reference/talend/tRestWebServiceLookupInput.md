<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trestwebservicelookupinput · versión 8.0 -->
# tRestWebServiceLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Retrieves messages from a REpresentational State Transfer (REST) Web service
provider and gets responses accordingly.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tRestWebServiceLookupInput properties for Apache Spark Streaming

These properties are used to configure tRestWebServiceLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tRestWebServiceLookupInput component belongs to the Webservice family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is read-only. You can click Edit schema to view the schema.  This read-only *payload* column is used to carry the body of the retrieved message. |
| URL | Enter the URL address of the REST Web server to be invoked. |
| HTTP Method | From this list, select an HTTP method that describes the desired action. The specific meanings of the HTTP methods are subject to definitions of your Web service provider. Listed below are the generally accepted HTTP methods:   * GET: retrieves data from the server end based on   the given parameters. |
| HTTP Headers | Enter the name-value pair(s) for HTTP headers to define the parameters of the requested HTTP operation.  For the specific definitions of HTTP headers, consult your REST Web service provider. For reference information, visit [en.wikipedia.org/wiki/List\_of\_HTTP\_headers](http://en.wikipedia.org/wiki/List_of_HTTP_headers). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/trestwebservicelookupinput -->
# tRestWebServiceLookupInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Retrieves messages from a REpresentational State Transfer (REST) Web service
provider and gets responses accordingly.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tRestWebServiceLookupInput properties for Apache Spark Streaming

These properties are used to configure tRestWebServiceLookupInput running in the Spark Streaming Job framework.

The Spark Streaming
tRestWebServiceLookupInput component belongs to the Webservice family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is read-only. You can click Edit schema to view the schema.  This read-only *payload* column is used to carry the body of the retrieved message. |
| URL | Enter the URL address of the REST Web server to be invoked. |
| HTTP Method | From this list, select an HTTP method that describes the desired action. The specific meanings of the HTTP methods are subject to definitions of your Web service provider. Listed below are the generally accepted HTTP methods:   * GET: retrieves data from the server end based on   the given parameters. |
| HTTP Headers | Enter the name-value pair(s) for HTTP headers to define the parameters of the requested HTTP operation.  For the specific definitions of HTTP headers, consult your REST Web service provider. For reference information, visit [en.wikipedia.org/wiki/List\_of\_HTTP\_headers](http://en.wikipedia.org/wiki/List_of_HTTP_headers). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
