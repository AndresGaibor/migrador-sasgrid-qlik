<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkinesisinputavro · versión 8.0 -->
# tKinesisInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Acts as consumer of an Amazon Kinesis stream to pull messages from this Kinesis
stream.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

Using the Kinesis Client Library (KCL) provided by Amazon, tKinesisInputAvro consumes Avro-formatted
data from a given Amazon Kinesis stream (an ordered sequence of data
records), constructs an RDD out of this data and sends the RDD to its
following components.

## tKinesisInputAvro properties for Apache Spark Streaming

These properties are used to configure tKinesisInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tKinesisInputAvro component belongs to the Messaging family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields. |
| Access key | Enter the access key ID that uniquely identifies an AWS Account. For further information about how to get your Access Key and Secret Key, see [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html). |
| Secret key | Enter the secret access key, constituting the security credentials in combination with the access Key.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Stream name | Enter the name of the Kinesis stream you want tKinesisInput to pull data from. |
| Endpoint URL | Enter the endpoint of the Kinesis service to be used. For example, *https://kinesis.us-east-1.amazonaws.com*. More valid Kinesis endpoint URLs can be found at <http://docs.aws.amazon.com/general/latest/gr/rande.html#ak_region>. |
| Explicitly set authentication parameters | Select this check box to use the explicit authentication mechanism to connect to Kinesis. Note that this mechanism is supported by Spark V1.4+ only.  Since this security mechanism requires the AWS Region parameter to be explicitly set, you need to enter the region value to be used in the Region field that is displayed. For example, *us-west-2*.  It is recommended to use the explicit authentication to gain better security when the Spark version you are using supports this mechanism. With this check box selected, the access credentials are provided directly to Kinesis.  While if you leave this check box clear, an older authentication mechanism is used. This way, the access credentials are used by Spark as context variables for Kinesis connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Checkpoint interval | Enter the time interval (in millisecond) at the end of which tKinesisInput saves the position of its read in the Kinesis stream.  Data records in a Kinesis stream are grouped into partitions (shards in terms of Kinesis) and indexed with sequence numbers. A sequence number uniquely identifies the position of a record. For further information about the terms used by Amazon in Kinesis, see <http://docs.aws.amazon.com/kinesis/latest/dev/key-concepts.html>. |
| Initial position stream | Select the starting position to read data from the stream in the absence of the Kinesis checkpoint information.  * Start with the oldest data: starts from the   beginning of the stream within the limit of 24 hours. * Start after the most recent data: starts at   the position after the latest data of the stream. |
| Storage level | Select how you want the received data to be cached. For further information about the different levels, see <https://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence>. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  At runtime, this component keeps listening to the stream and reads new messages once they are buffered in this stream.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkinesisinputavro -->
# tKinesisInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Acts as consumer of an Amazon Kinesis stream to pull messages from this Kinesis
stream.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

Using the Kinesis Client Library (KCL) provided by Amazon, tKinesisInputAvro consumes Avro-formatted
data from a given Amazon Kinesis stream (an ordered sequence of data
records), constructs an RDD out of this data and sends the RDD to its
following components.

## tKinesisInputAvro properties for Apache Spark Streaming

These properties are used to configure tKinesisInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tKinesisInputAvro component belongs to the Messaging family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields. |
| Access key | Enter the access key ID that uniquely identifies an AWS Account. For further information about how to get your Access Key and Secret Key, see [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html). |
| Secret key | Enter the secret access key, constituting the security credentials in combination with the access Key.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Stream name | Enter the name of the Kinesis stream you want tKinesisInput to pull data from. |
| Endpoint URL | Enter the endpoint of the Kinesis service to be used. For example, *https://kinesis.us-east-1.amazonaws.com*. More valid Kinesis endpoint URLs can be found at <http://docs.aws.amazon.com/general/latest/gr/rande.html#ak_region>. |
| Explicitly set authentication parameters | Select this check box to use the explicit authentication mechanism to connect to Kinesis. Note that this mechanism is supported by Spark V1.4+ only.  Since this security mechanism requires the AWS Region parameter to be explicitly set, you need to enter the region value to be used in the Region field that is displayed. For example, *us-west-2*.  It is recommended to use the explicit authentication to gain better security when the Spark version you are using supports this mechanism. With this check box selected, the access credentials are provided directly to Kinesis.  While if you leave this check box clear, an older authentication mechanism is used. This way, the access credentials are used by Spark as context variables for Kinesis connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Checkpoint interval | Enter the time interval (in millisecond) at the end of which tKinesisInput saves the position of its read in the Kinesis stream.  Data records in a Kinesis stream are grouped into partitions (shards in terms of Kinesis) and indexed with sequence numbers. A sequence number uniquely identifies the position of a record. For further information about the terms used by Amazon in Kinesis, see <http://docs.aws.amazon.com/kinesis/latest/dev/key-concepts.html>. |
| Initial position stream | Select the starting position to read data from the stream in the absence of the Kinesis checkpoint information.  * Start with the oldest data: starts from the   beginning of the stream within the limit of 24 hours. * Start after the most recent data: starts at   the position after the latest data of the stream. |
| Storage level | Select how you want the received data to be cached. For further information about the different levels, see <https://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence>. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  At runtime, this component keeps listening to the stream and reads new messages once they are buffered in this stream.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
