<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmqttinput · versión 8.0 -->
# tMQTTInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Acts as consumer of a MQTT topic to stream messages from this topic.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

tMQTTInput
subscribes to a given MQTT topic, reads messages from this topic and constructs RDDs out
of these messages and then send them to its following component.

## tMQTTInput properties for Apache Spark Streaming

These properties are used to configure tMQTTInput running in the Spark Streaming Job framework.

The Spark Streaming
tMQTTInput component belongs to the Messaging family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Broker URL | Enter the location of the MQTT broker to be used to route the published messages to the subscriber (the tMQTTInput component). |
| Topic | Enter the topic you want tMQTTInput to subscribe to. |
| QoS | Enter, without quotation marks around, the numeric level of QoS (Quality of Service) to be assigned to the message to be used.  This quality level indicates how responsive you want MQTT to be to the message delivery request:  * *0*: it means a message may not be delivered or   is delivered only once. * *1*: it means a message is delivered at least   once. * *2*: it means a message is delivered exactly   once.  For further explanation about the different levels of QoS, see <http://www-01.ibm.com/support/knowledgecenter/SSFKSJ_8.0.0/com.ibm.mq.dev.doc/q029090_.htm>. |
| Include topic column | Select this check box to add a *topic* column to the schema to send the name of the topic along with its messages to the following component. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is read-only. You can click Edit schema to view the schema.  This read-only *payload* column is used to carry the body of the MQTT message to be processed.  The input message body can use very different data formats. For example, if its format is JSON, you need to use tExtractJSONField following tMQTTInput to extract the data to be processed from this body. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Encoding | Select the encoding from the list or select Custom and define it manually.  This encoding is used by tMQTTInput to decode the input message arrays. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  At runtime, the tMQTTInput component keeps listening to the topic and reads new messages once they are buffered in this topic.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tmqttinput -->
# tMQTTInput (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Acts as consumer of a MQTT topic to stream messages from this topic.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

tMQTTInput
subscribes to a given MQTT topic, reads messages from this topic and constructs RDDs out
of these messages and then send them to its following component.

## tMQTTInput properties for Apache Spark Streaming

These properties are used to configure tMQTTInput running in the Spark Streaming Job framework.

The Spark Streaming
tMQTTInput component belongs to the Messaging family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Broker URL | Enter the location of the MQTT broker to be used to route the published messages to the subscriber (the tMQTTInput component). |
| Topic | Enter the topic you want tMQTTInput to subscribe to. |
| QoS | Enter, without quotation marks around, the numeric level of QoS (Quality of Service) to be assigned to the message to be used.  This quality level indicates how responsive you want MQTT to be to the message delivery request:  * *0*: it means a message may not be delivered or   is delivered only once. * *1*: it means a message is delivered at least   once. * *2*: it means a message is delivered exactly   once.  For further explanation about the different levels of QoS, see <http://www-01.ibm.com/support/knowledgecenter/SSFKSJ_8.0.0/com.ibm.mq.dev.doc/q029090_.htm>. |
| Include topic column | Select this check box to add a *topic* column to the schema to send the name of the topic along with its messages to the following component. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is read-only. You can click Edit schema to view the schema.  This read-only *payload* column is used to carry the body of the MQTT message to be processed.  The input message body can use very different data formats. For example, if its format is JSON, you need to use tExtractJSONField following tMQTTInput to extract the data to be processed from this body. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Encoding | Select the encoding from the list or select Custom and define it manually.  This encoding is used by tMQTTInput to decode the input message arrays. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  At runtime, the tMQTTInput component keeps listening to the topic and reads new messages once they are buffered in this topic.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
