<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmaprstreamsinputavro · versión 8.0 -->
# tMapRStreamsInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Transmits messages in the Avro format to the Job that runs transformations over
these messages. Only MapR V5.2 onwards is supported by this component.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tMapRStreamsInputAvro properties for Apache Spark Streaming

These properties are used to configure tMapRStreamsInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tMapRStreamsInputAvro component belongs to the Messaging family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Note that the schema of this component is read-only. It stores the message body sent from the message producer. |
| Starting offset | Select the starting point from which the messages of a topic are consumed.  In MapR Streams, the increasing ID number of a message is called *offset*. When a new consumer group starts, from this list, you can select beginning to start consumption from the oldest message of the entire topic, or select latest to wait for a new message.  Note that the consumer group takes into account only the offset-committed messages to start from.  Each consumer group has its own counter to remember the position of a message it has consumed. For this reason, once a consumer group starts to consume messages of a given topic, a consumer group recognizes the latest message only with regard to the position where this group stops the consumption, rather than to the entire topic. Based on this principle, the following behaviors can be expected:   * If you are resuming an existing consumer group, this option determines the   starting point for this consumer group only if it does not already have a committed   starting point. Otherwise, this consumer group starts from this committed starting   point. For example, a topic has *100* messages. If   an existing consumer group has successfully processed 50 messages, and has committed   their offsets, then the same consumer group restarts from the offset *51*. * If you create a new consumer group or reset an existing consumer group, which, in   either case, means this group has not consumed any message of this topic, then when   you start it from latest, this new group starts and waits for the offset *101*. |
| Topic name | Enter the name of the topic from which tMapRStreamsInput receives the feed of messages. You must enter the name of the stream to which this topic belongs. The syntax is *path\_to\_the\_stream:topic\_name*. |
| Set number of records per second to read from each Kafka partition | Enter this number in double quotation marks to limit the size of each batch to be sent for processing.  For example, if you put *100* and the batch value you define in the Spark configuration tab is *2* seconds, the size from a partition for each batch is *200* messages.  If you leave this check box clear, the component tries to read all the available messages in one second into one single batch before sending it, potentially resulting in Job that stops responding in case of a huge quantity of messages. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Consumer properties | Add the MapR Streams consumer properties you need to customize to this table. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmaprstreamsinputavro -->
# tMapRStreamsInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Transmits messages in the Avro format to the Job that runs transformations over
these messages. Only MapR V5.2 onwards is supported by this component.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

## tMapRStreamsInputAvro properties for Apache Spark Streaming

These properties are used to configure tMapRStreamsInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tMapRStreamsInputAvro component belongs to the Messaging family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Note that the schema of this component is read-only. It stores the message body sent from the message producer. |
| Starting offset | Select the starting point from which the messages of a topic are consumed.  In MapR Streams, the increasing ID number of a message is called *offset*. When a new consumer group starts, from this list, you can select beginning to start consumption from the oldest message of the entire topic, or select latest to wait for a new message.  Note that the consumer group takes into account only the offset-committed messages to start from.  Each consumer group has its own counter to remember the position of a message it has consumed. For this reason, once a consumer group starts to consume messages of a given topic, a consumer group recognizes the latest message only with regard to the position where this group stops the consumption, rather than to the entire topic. Based on this principle, the following behaviors can be expected:   * If you are resuming an existing consumer group, this option determines the   starting point for this consumer group only if it does not already have a committed   starting point. Otherwise, this consumer group starts from this committed starting   point. For example, a topic has *100* messages. If   an existing consumer group has successfully processed 50 messages, and has committed   their offsets, then the same consumer group restarts from the offset *51*. * If you create a new consumer group or reset an existing consumer group, which, in   either case, means this group has not consumed any message of this topic, then when   you start it from latest, this new group starts and waits for the offset *101*. |
| Topic name | Enter the name of the topic from which tMapRStreamsInput receives the feed of messages. You must enter the name of the stream to which this topic belongs. The syntax is *path\_to\_the\_stream:topic\_name*. |
| Set number of records per second to read from each Kafka partition | Enter this number in double quotation marks to limit the size of each batch to be sent for processing.  For example, if you put *100* and the batch value you define in the Spark configuration tab is *2* seconds, the size from a partition for each batch is *200* messages.  If you leave this check box clear, the component tries to read all the available messages in one second into one single batch before sending it, potentially resulting in Job that stops responding in case of a huge quantity of messages. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Consumer properties | Add the MapR Streams consumer properties you need to customize to this table. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Prerequisites | The Hadoop distribution must be properly installed, so as to guarantee the interaction with *Talend Studio*. The following list presents MapR related information for example.   * Ensure that you have installed the MapR client in the machine where   Talend Studio is,   and added the MapR client library to the PATH variable of that machine. According to   MapR's documentation, the library or libraries of a MapR client corresponding to each   OS version can be found under *MAPR\_INSTALL\   hadoop\hadoop-VERSION\lib\native*. For example, the library for Windows is *\lib\native\MapRClient.dll* in the MapR client jar file.  Without adding the specified library or libraries, you may encounter the following   error: no MapRClient in java.library.path. * Set the -Djava.library.path argument,   for example, in the Job Run VM arguments area   of the Run/Debug view in the Preferences dialog box in the Window menu. This argument provides to Talend Studio the   path to the native library of that MapR client. This allows the subscription-based   users to make full use of the Data viewer to   view locally in Talend Studio the   data stored in MapR.   For further information about how to install a Hadoop distribution, see the manuals corresponding to the Hadoop distribution you are using. |
