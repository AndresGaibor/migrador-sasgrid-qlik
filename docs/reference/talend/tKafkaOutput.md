<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kafka/tkafkaoutput · versión 8.0 -->
# tKafkaOutput

Last updated: 9/30/2026

Publishes messages into a Kafka system.

This component receives messages serialized into byte arrays by its preceding component and issues these messages into a given Kafka system.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tKafkaOutput Standard properties](/talend/en-US/components/8.0/kafka/tkafkaoutput-standard-properties)
* [tKafkaOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/kafka/tkafkaoutput-properties-for-apache-spark-streaming)
* [tKafkaOutput properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/kafka/tkafkaoutput-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Reading and writing Avro data from Kafka using Standard Jobs](writing-and-reading-avro-data-from-kafka-using-a-standard-job)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kafka/tkafkaoutput-properties-for-apache-spark-structured-streaming -->
# tKafkaOutput properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Use these properties to configure tKafkaOutput running in
the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tKafkaOutput component belongs to the Messaging family.

This component is available in Talend Real-Time Big Data Platform and Talend Data Fabric.

Information noteImportant: For Spark Streaming Jobs, Talend Studio does not
support a specific version of Kafka but relies on a Kafka broker version compatibility
provided by Spark. The Kafka broker version supported depends on the Spark version you use.
For each Spark version, Talend Studio supports
the targeted Kafka broker version provided by Spark. As of today Talend Studio relies on
Spark compatibility statement, and therefore supports Kafka broker version 0.10.0 onwards.
For more information, see [Spark Streaming + Kafka Integration Guide](https://spark.apache.org/docs/latest/streaming-kafka-integration.html) on the official Spark
documentation.

## Basic settings

| Properties | Description |
| --- | --- |
| Configuration component | Select the tKafkaConfiguration component to use for the Kafka connection settings. |
| Topic name | Enter the name of the topic you want to publish messages to. This topic must already exist. |
| Partition | Enter the partition number to be used from the topic.  Information noteNote: If you leave this field blank, Kafka selects the partition according to its producer partitioning behavior. If you enter a value greater than 0, the component verifies that the Kafka topic has a partition range that includes the specified value. |
| Key | Enter the message key to assign to the Kafka records.  Information noteNote: If you leave this field blank, the key defaults to null. |
| Compress the data | Select the Compress the data check box to compress the output data. |
| Set checkpoint location | Enter the path to the directory where Spark stores the checkpoint data for this streaming query.  Checkpointing enables fault tolerance and allows a failed query to resume from where it stopped. |
| Set trigger | Select this check box to configure how often the streaming query processes data. The available trigger types are:  * Continuous: processes data continuously. * Available now: processes all available data in a   single batch, then stops the query. * Fixed interval: runs the query at a fixed time   interval. Enter the interval duration in the field that appears. |
| Output mode | Select the output mode from the drop-down list:  * Append: adds new rows without modifying existing   rows. * Update: writes only the rows that were updated   since the last trigger. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Kafka properties | Add the Kafka new producer properties you need to customize to this table.  For more information about the new producer properties you can define in this table, see the section describing the [new producer configuration](https://kafka.apache.org/documentation.html#newproducerconfigs) from the official Kafka documentation. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an end component and requires an input link.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kafka/tkafkaoutput-standard-properties -->
# tKafkaOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure tKafkaOutput running in the Standard Job framework.

The Standard
tKafkaOutput component belongs to the Internet family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Input type | Select the type of messages to be read by Kafka from the drop-down list:  * byte[]: the component receives messages serialized   into byte arrays. * ProducerRecord: the component receives messages   serialized as key/value pair. The message key and the message value can be   serialized as Avro.   This property is available since Kafka 2.2.1. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Note that the schema of this component is read-only. It stores the messages to be published. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Version | Select the version of the Kafka cluster to be used.  If you have installed the 8.0.1-R2024-02 Talend Studio monthly update or a later one delivered by Talend, the Kafka 2.4.x version and previous versions are deprecated. |
| Broker list | Enter the addresses of the broker nodes of the Kafka cluster to be used.  The form of this address should be *hostname:port*. This information is the name and the port of the hosting node in this Kafka cluster.  If you need to specify several addresses, separate them using a comma (*,*). |
| Topic name | Enter the name of the topic you want to publish messages to. This topic must already exist.  This property is only available when you select Byte[] from the Input type dropdown list. |
| Compress the data | Select the Compress the data check box to compress the output data. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  This checkbox is available since Kafka 0.9.0.1. |
| Set keystore | Select this checkbox to enable the SSL or TLS encrypted connection via a tSetKeystore component. Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  This checkbox is available when you select the Use SSL/TLS checkbox.  Information noteNote: This option is available when you have installed the 8.0.1-R2022-05 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use Kerberos authentication | If the Kafka cluster to be used is secured with Kerberos, select this checkbox to display the related parameters to be defined:   * JAAS configuration path: enter the   path, or browse to the JAAS configuration file to be used by the Job to   authenticate as a client to Kafka.  This JAAS file describes how the clients, the Kafka-related   Jobs in terms of *Talend*, can connect to the Kafka broker nodes, using either the kinit mode or   the keytab mode. The JAAS file must be stored in the machine where these   Jobs are executed.  *Talend*, Kerberos or Kafka does not provide this JAAS file. You need to create   it by following the explanation in [Configuring Kafka   client](http://kafka.apache.org/documentation.html#security_sasl_clientconfig) depending on the security strategy of your   organization. * Kafka brokers principal name: enter   the primary part of the Kerberos principal you defined for the brokers when   you were creating the broker cluster. For example, in this principal *kafka/kafka1.hostname.com@EXAMPLE.COM*, the primary   part to be used to fill in this field is *kafka*. * Set kinit command path: Kerberos   uses a default path to its kinit executable. If you have changed this path,   select this checkbox and enter the custom access path.  If you leave this checkbox clear, the default path is   used. * Set Kerberos configuration path:   Kerberos uses a default path to its configuration file, the *krb5.conf* file (or *krb5.ini*   in Windows) for Kerberos 5 for example. If you have changed this path,   select this checkbox and enter the custom access path to the Kerberos   configuration file.  If you leave this checkbox clear, a given strategy is applied   by Kerberos to attempt to find the configuration information it requires.   For details about this strategy, see the *Locating the   krb5.conf Configuration File* section in [Kerberos requirements](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html).   For further information about how a Kafka cluster is secured with Kerberos, see [Authenticating using SASL](http://kafka.apache.org/documentation.html#security_sasl).  This checkbox is available since Kafka 0.9.0.1. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Kafka properties | Add the Kafka new producer properties you need to customize to this table.  For more information about the new producer properties you can define in this table, see the section describing the [new producer configuration](https://kafka.apache.org/documentation.html#newproducerconfigs) from the official Kafka documentation. |
| Set Headers | Select this checkbox to add headers to messages to be sent. This feature is available to Kafka 1.1.0 onwards. |
| Use schema registry | Select this checkbox to use Confluent Schema Registry and to display the related parameters to be defined:  * URL: enter the Schema Registry instance URL. * Basic authentication: select this checkbox and enter   your credentials in the Username and   Password. * Set schema registry keystore: select this checkbox to   enable the SSL or TLS encrypted connection. Then you need to use the   tSetKeystore component in the same Job to specify   the encryption information. This checkbox is not available when you already   set a tSetKeystore in the Basic settings view of the   component because Kafka SSL configuration is reused for schema registry. * Key serializer and Value   serializer: select the schema format to use for the key and   value from the dropdown list. The default Custom   serializer is   org.apache.kafka.common.serialization.ByteArraySerializer.   For more information about Schema registry, see the [Confluent documentation](https://docs.confluent.io/platform/current/schema-registry/index.html).  This option is only available when you select ProducerRecord from the Input type dropdown list in the Basic settings view.  Information noteNote: This option is available when you have installed the 8.0.1-R2022-01 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use transaction | Select this checkbox to enable Kafka transactional mode and provide exactly-once delivery guarantees. When selected, the following parameters are displayed:   * Transaction ID: Enter a unique identifier for this   transactional producer. The value maps to the Kafka   transactional.id producer property and must be unique   per producer instance. * Transaction timeout (ms): Enter the maximum time, in   milliseconds, that a transaction can remain open before the broker aborts   it. The value must be greater than 0. The default value is   60000. * Commit every (messages): Enter the number of   messages after which the component commits the current transaction and   begins a new one. The value must be greater than 0. The default value is   1000.   When a send error or transaction timeout occurs, the component aborts the current transaction. If Die on error is not selected, the component starts a new transaction from the next message. Consumers configured with isolation.level=read\_committed, such as a tKafkaInput component with Isolation level set to read\_committed, read only committed messages.  Information noteNote: This option is available when you have installed the 8.0.1-R2026-05 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| NB\_ERRORS | The number of rows processed with errors. This is an After variable and it returns an integer. |
| NB\_SUCCESS | The number of rows successfully processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is an end component. It requires a tJavaRow or tJava component to transform the incoming data into serialized byte arrays.  The following sample shows how to construct a statement to perform this transformation:  ``` output_row.serializedValue = input_row.users.getBytes(); ```  In this code, the *output\_row* variable represents the schema of the data to be output to tKafkaOutput and *output\_row.serializedValue* the single read-only column of that schema; the *input\_row* variable represents the schema of the incoming data and *input\_row.users* the input column called *users* to be transformed to byte arrays by the *getBytes()* method. |
