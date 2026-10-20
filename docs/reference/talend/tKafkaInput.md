<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kafka/tkafkainput · versión 8.0 -->
# tKafkaInput

Last updated: 9/30/2026

Transmits messages you need to process to the components that follow in the Job you
are designing.

tKafkaInput is a generic message broker that
transmits messages to the Job that runs transformations over these messages.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tKafkaInput Standard properties](/talend/en-US/components/8.0/kafka/tkafkainput-standard-properties)
* [tKafkaInput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/kafka/tkafkainput-properties-for-apache-spark-streaming)
* [tKafkaInput properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/kafka/tkafkainput-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Analyzing a Twitter flow in near real-time (deprecated)](tkafkainput-tkafkacreatetopic-thdfsconfiguration-ts3configuration-analyzing-twitter-flow-in-near-real-time-spark-stream-component-in-this)
* [Reading and writing Avro data from Kafka using Standard Jobs](writing-and-reading-avro-data-from-kafka-using-a-standard-job)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kafka/tkafkainput-properties-for-apache-spark-structured-streaming -->
# tKafkaInput properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tKafkaInput running
in the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tKafkaInput component belongs to the Messaging family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Configuration component | Select the tKafkaConfiguration component to use for the Kafka connection settings. |
| Starting offset | Select the starting point from which the messages of a topic are consumed.  In Kafka, the sequential ID number of a message is called *offset*. From this list, you can select From beginning to start consumption from the oldest message of the entire topic, or select From latest to start from the latest message that has been consumed by the same consumer group and of which the offset is tracked by Spark within Spark checkpoints.  Each consumer group has its own counter to remember the position of a message it has consumed. For this reason, once a consumer group starts to consume messages of a given topic, a consumer group recognizes the latest message only with regard to the position where this group stops the consumption, rather than to the entire topic. Based on this principle, the following behaviors can be expected:   * A topic has for example *100* messages. If a   consumer group has stopped the consumption at the message of the offset *50*, then when you select From   latest, the same consumer group restarts from the offset *51*. * If you create a new consumer group or reset an existing consumer group, which, in   either case, means this group has not consumed any message of this topic, then when   you start it from latest, this new group starts and waits for the offset *101*. |
| Topic name | Enter the name of the topic from which tKafkaInput receives the feed of messages. |
| Group ID | Enter the name of the consumer group to which you want the current consumer (the tKafkaInput component) to belong.  This consumer group will be created at runtime if it does not exist at that moment.  This property is available only when you are using Spark 2.0 or the Hadoop distribution to be used is running Spark 2.0. If you do not know the Spark version you are using, ask the administrator of your cluster for details. |
| Set number of records per second to read from each Kafka partition | Select this check box to set the maximum number of records read from each Kafka partition per trigger. In the field that appears, enter the maximum number of records. |
| Enable watermarking | Select this check box to activate watermarking and select the time mode to be used:  * Event time: Select to use a timestamp column   representing when each event occurred, then select the column in the   Watermark column (timestamp) drop-down list. * Processing time: Select to use the time when Spark   reads each record.   In the Watermark delay field, specify how long Spark waits for late data before finalizing each window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Do not fail on data loss | Select this check box to allow the streaming query to continue processing when Kafka offsets are missing — for example, because topics were deleted or offsets are out of range. If cleared, the query stops with an error. |
| Kafka properties | Add the Kafka consumer properties you need to customize to this table. For example, you can set a specific *zookeeper.connection.timeout.ms* value to avoid *ZkTimeoutException*.  For further information about the consumer properties you can define in this table, see the section describing the consumer configuration in Kafka's documentation in <http://kafka.apache.org/documentation.html#consumerconfigs>. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kafka/tkafkainput-standard-properties -->
# tKafkaInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tKafkaInput running in the Standard Job framework.

The Standard
tKafkaInput component belongs to the Internet family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Note that the schema of this component is read-only. It stores the messages sent from the message producer. |
| Output type | Select the type of data to be sent to the next component from the dropdown list:  * String: the component sends messages serialized into   strings. * byte[]: the component sends messages serialized into   byte arrays. * ConsumerRecord: the component sends messages   serialized as key/value pair. The message key and the message value can be   serialized as Avro.   Typically, using String is recommended, because tKafkaInput can automatically translate the Kafka byte[] messages into strings to be processed by the Job. However, in case that the format of Kafka messages is not known to tKafkaInput, such as *Protobuf*, you can select byte[] and then use a Custom code component such as tJavaRow to deserialize the messages into strings so that the other components of the same Job can process these messages. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Version | Select the version of the Kafka cluster to be used.  If you have installed the 8.0.1-R2024-02 Talend Studio monthly update or a later one delivered by Talend, the Kafka 2.4.x version and previous versions are deprecated. |
| Broker list | Enter the addresses of the broker nodes of the Kafka cluster to be used.  The form of this address should be *hostname:port*. This information is the name and the port of the hosting node in this Kafka cluster.  If you need to specify several addresses, separate them using a comma (*,*).  This field is available since Kafka 0.9.0.1. |
| Topic name | Enter the name of the topic from which tKafkaInput receives the feed of messages. |
| Use partition offset | Select this checkbox to specify the partition to read from (Partition), and define the starting offset for message retrieval (Offset). |
| Consumer group ID | Enter the name of the consumer group to which you want the current consumer (the tKafkaInput component) to belong.  This consumer group will be created at runtime if it does not exist at that moment. |
| Reset offsets on consumer group | Select this checkbox to clear the offsets saved for the consumer group to be used so that this consumer group is handled as a new group that has not consumed any messages. |
| New consumer group starts from | Select the starting point from which the messages of a topic are consumed.  In Kafka, the increasing ID number of a message is called *offset*. When a new consumer group starts, from this list, you can select beginning to start consumption from the oldest message of the entire topic, or select latest to wait for a new message.  Note that the consumer group takes into account only the offset-committed messages to start from.  Each consumer group has its own counter to remember the position of a message it has consumed. For this reason, once a consumer group starts to consume messages of a given topic, a consumer group recognizes the latest message only with regard to the position where this group stops the consumption, rather than to the entire topic. Based on this principle, the following behaviors can be expected:   * If you are resuming an existing consumer group, this option determines the   starting point for this consumer group only if it does not already have a committed   starting point. Otherwise, this consumer group starts from this committed starting   point. For example, a topic has *100* messages. If   an existing consumer group has successfully processed 50 messages, and has committed   their offsets, then the same consumer group restarts from the offset *51*. * If you create a new consumer group or reset an existing consumer group, which, in   either case, means this group has not consumed any message of this topic, then when   you start it from latest, this new group starts and waits for the offset *101*. |
| Auto-commit offsets | Select this checkbox to make tKafkaInput automatically save its consumption state at the end of each given time interval. You need to define this interval in the Interval field that is displayed.  Note that the offsets are committed only at the end of each interval. If your Job stops in the middle of an interval, the message consumption state within this interval is not committed. |
| Stop after a maximum total duration (ms) | Select this checkbox and in the pop-up field, enter the duration (in milliseconds) at the end of which tKafkaInput stops running. |
| Stop after receiving a maximum number of messages | Select this checkbox and in the pop-up field, enter the maximum number of messages you want tKafkaInput to receive before it automatically stops running. |
| Stop after maximum time waiting between messages (ms) | Select this checkbox and in the pop-up field, enter the waiting time (in milliseconds) by tKafkaInput for a new message. If tKafkaInput does not receive any new message when this waiting time meets its end, it automatically stops running. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  This checkbox is available since Kafka 0.9.0.1. |
| Set keystore | Select this checkbox to enable the SSL or TLS encrypted connection via a tSetKeystore component.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  This checkbox is available when you select the Use SSL/TLS checkbox.  Information noteNote: This option is available when you have installed the 8.0.1-R2022-05 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use Kerberos authentication | If the Kafka cluster to be used is secured with Kerberos, select this checkbox to display the related parameters to be defined:   * JAAS configuration path: enter the   path, or browse to the JAAS configuration file to be used by the Job to   authenticate as a client to Kafka.  This JAAS file describes how the clients, the Kafka-related   Jobs in terms of *Talend*, can connect to the Kafka broker nodes, using either the kinit mode or   the keytab mode. The JAAS file must be stored in the machine where these   Jobs are executed.  *Talend*, Kerberos or Kafka does not provide this JAAS file. You need to create   it by following the explanation in [Configuring Kafka   client](http://kafka.apache.org/documentation.html#security_sasl_clientconfig) depending on the security strategy of your   organization. * Kafka brokers principal name: enter   the primary part of the Kerberos principal you defined for the brokers when   you were creating the broker cluster. For example, in this principal *kafka/kafka1.hostname.com@EXAMPLE.COM*, the primary   part to be used to fill in this field is *kafka*. * Set kinit command path: Kerberos   uses a default path to its kinit executable. If you have changed this path,   select this checkbox and enter the custom access path.  If you leave this checkbox clear, the default path is   used. * Set Kerberos configuration path:   Kerberos uses a default path to its configuration file, the *krb5.conf* file (or *krb5.ini*   in Windows) for Kerberos 5 for example. If you have changed this path,   select this checkbox and enter the custom access path to the Kerberos   configuration file.  If you leave this checkbox clear, a given strategy is applied   by Kerberos to attempt to find the configuration information it requires.   For details about this strategy, see the *Locating the   krb5.conf Configuration File* section in [Kerberos requirements](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html).   For further information about how a Kafka cluster is secured with Kerberos, see [Authenticating using SASL](http://kafka.apache.org/documentation.html#security_sasl).  This checkbox is available since Kafka 0.9.0.1. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Kafka properties | Add the Kafka consumer properties you need to customize to this table. For example, you can set a specific *zookeeper.connection.timeout.ms* value to avoid *ZkTimeoutException*.  You can also set security properties such as SSL encryption with ssl.truststore.location or ssl.keystore.location.  For further information about the consumer properties you can define in this table, see the section describing the consumer configuration in Kafka's documentation in <http://kafka.apache.org/documentation.html#consumerconfigs>. |
| Apply security properties after advanced Kafka properties | Select this checkbox to take first into account the security properties set in the Kafka properties table from the Advanced settings view rather than the security properties set in the tSetKeyStore component when the Use SSL/TLS checkbox from the Basic settings view is selected. |
| Isolation level | Select the isolation level that controls which messages the consumer reads from Kafka:   * read\_uncommitted: Reads all messages, including   messages from transactions that are still in progress or have been aborted.   This is the default behavior. * read\_committed: Reads only messages from committed   transactions and non-transactional messages. Messages from open or aborted   transactions are not visible.   Select read\_committed when consuming from topics written by a transactional producer, such as a tKafkaOutput component with the Use transaction option enabled.  Information noteNote: This option is available when you have installed the 8.0.1-R2026-05 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Timeout precision(ms) | Enter the time duration in millisecond at the end of which you want a timeout exception to be returned if no message is available for consumption.  The value *-1* indicates that no timeout is set. |
| Use schema registry | Select this checkbox to use Confluent Schema Registry and to display the related parameters to be defined:  * URL: enter the Schema Registry instance URL. * Basic authentication: select this checkbox and enter   your credentials in the Username and   Password. * Set schema registry keystore: select this checkbox to   enable the SSL or TLS encrypted connection. Then you need to use the   tSetKeystore component in the same Job to specify   the encryption information. This checkbox is not available when you already   set a tSetKeystore in the Basic settings view of the   component because Kafka SSL configuration is reused for schema registry. * Key deserializer and Value   deserializer: select the schema format to use for the key and   value from the dropdown list. The default Custom   serializer is   org.apache.kafka.common.serialization.ByteArraySerializer.   For more information about Schema Registry, see the [Confluent documentation](https://docs.confluent.io/platform/current/schema-registry/index.html).  This option is only available when you select ConsumerRecord from the Output type dropdown list in the Basic settings view.  Information noteNote: This option is available when you have installed the 8.0.1-R2022-01 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Load the offset with the message | Select this checkbox to output the offsets of the consumed messages to the next component. When selecting it, a read-only column called *offset* is added to the schema.  This property is only available when you select String or byte[] from the Output type dropdown list in the Basic settings view. |
| Custom encoding | You may encounter encoding issues when you process the stored data. In that situation, select this check box to display the Encoding list.  Select the encoding from the list or select Custom and define it manually.  This property is only available when you select String or byte[] from the Output type dropdown list in the Basic settings view. |
| tStatCatcher Statistics | Select this checkbox to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link. When the Kafka topic it needs to use does not exist, it can be used along with the tKafkaCreateTopic component to read the topic created by the latter component. |
