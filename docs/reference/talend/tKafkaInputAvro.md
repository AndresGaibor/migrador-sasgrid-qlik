<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkafkainputavro · versión 8.0 -->
# tKafkaInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Transmits Avro-formatted messages you need to process to its following component
in the Job you are designing.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

tKafkaInputAvro is a generic message broker that transmits messages in
the
AVRO
format to the Job that runs transformations over these
messages.This component
cannot handle AVRO messages created by the avro-tools libraries.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tKafkaInputAvro properties for Apache Spark Streaming

These properties are used to configure tKafkaInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tKafkaInputAvro component belongs to the Messaging family.

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
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields. |
| Broker list | Enter the addresses of the broker nodes of the Kafka cluster to be used.  The form of this address should be *hostname:port*. This information is the name and the port of the hosting node in this Kafka cluster.  If you need to specify several addresses, separate them using a comma (*,*). |
| Starting offset | Select the starting point from which the messages of a topic are consumed.  In Kafka, the sequential ID number of a message is called *offset*. From this list, you can select From beginning to start consumption from the oldest message of the entire topic, or select From latest to start from the latest message that has been consumed by the same consumer group and of which the offset is tracked by Spark within Spark checkpoints.  Note that in order to enable the component to remember the position of a consumed message, you need to activate the Spark Streaming checkpointing in the Spark Configuration tab in the Run view of the Job.  Each consumer group has its own counter to remember the position of a message it has consumed. For this reason, once a consumer group starts to consume messages of a given topic, a consumer group recognizes the latest message only with regard to the position where this group stops the consumption, rather than to the entire topic. Based on this principle, the following behaviors can be expected:   * A topic has for example *100* messages. If a   consumer group has stopped the consumption at the message of the offset *50*, then when you select From   latest, the same consumer group restarts from the offset *51*. * If you create a new consumer group or reset an existing consumer group, which, in   either case, means this group has not consumed any message of this topic, then when   you start it from latest, this new group starts and waits for the offset *101*. |
| Topic name | Enter the name of the topic from which tKafkaInput receives the feed of messages. |
| Group ID | Enter the name of the consumer group to which you want the current consumer (the tKafkaInput component) to belong.  This consumer group will be created at runtime if it does not exist at that moment.  This property is available only when you are using Spark 2.0 or the Hadoop distribution to be used is running Spark 2.0. If you do not know the Spark version you are using, ask the administrator of your cluster for details. |
| Set number of records per second to read from each Kafka partition | Enter this number within double quotation marks to limit the size of each batch to be sent for processing.  For example, if you put *100* and the batch value you define in the Spark configuration tab is *2* seconds, the size from a partition for each batch is *200* messages.  If you leave this checkbox clear, the component tries to read all the available messages in one second into one single batch before sending it, potentially resulting in Job that stops responding in case of a huge quantity of messages. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  This property is available only when you are using Spark 2.0 or the Hadoop distribution to be used is running Spark 2.0. If you do not know the Spark version you are using, ask the administrator of your cluster for details.  The TrustStore file and any used KeyStore file must be stored locally on every single Spark node that is hosting a Spark executor. |
| Use Kerberos authentication | If the Kafka cluster to be used is secured with Kerberos, select this checkbox to display the related parameters to be defined:   * JAAS configuration path: enter the   path, or browse to the JAAS configuration file to be used by the Job to   authenticate as a client to Kafka.  This JAAS file describes how the clients, the Kafka-related   Jobs in terms of *Talend*, can connect to the Kafka broker nodes, using either the kinit mode or   the keytab mode. The JAAS file must be stored in the machine where these   Jobs are executed.  *Talend*, Kerberos or Kafka does not provide this JAAS file. You need to create   it by following the explanation in [Configuring Kafka   client](http://kafka.apache.org/documentation.html#security_sasl_clientconfig) depending on the security strategy of your   organization. * Kafka brokers principal name: enter   the primary part of the Kerberos principal you defined for the brokers when   you were creating the broker cluster. For example, in this principal *kafka/kafka1.hostname.com@EXAMPLE.COM*, the primary   part to be used to fill in this field is *kafka*. * Set kinit command path: Kerberos   uses a default path to its kinit executable. If you have changed this path,   select this checkbox and enter the custom access path.  If you leave this checkbox clear, the default path is   used. * Set Kerberos configuration path:   Kerberos uses a default path to its configuration file, the *krb5.conf* file (or *krb5.ini*   in Windows) for Kerberos 5 for example. If you have changed this path,   select this checkbox and enter the custom access path to the Kerberos   configuration file.  If you leave this checkbox clear, a given strategy is applied   by Kerberos to attempt to find the configuration information it requires.   For details about this strategy, see the *Locating the   krb5.conf Configuration File* section in [Kerberos requirements](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html).   For further information about how a Kafka cluster is secured with Kerberos, see [Authenticating using SASL](http://kafka.apache.org/documentation.html#security_sasl).  This check box is available since Kafka 0.9.0.1. |
| Use Schema Registry | Select this check box to use Confluent Schema Registry and to display the related parameters to be defined:  * URL: enter the Schema Registry instance URL. * Basic authentication: select this check box and   enter your credentials in the Username and   Password. * Use the keystore of Kafka broker: select this   check box to enable the SSL or TLS encrypted connection using the same   tSetKeystore component used by the Kafka broker. This checkbox is   available when you select the Use SSL/TLS check   box and clear the Set schema registry   keystore. * Set schema registry keystore: select this check   box to enable the SSL or TLS encrypted connection. Then you need to use   the tSetKeystore component in the same Job to   specify the encryption information.  For more information about Schema Registry, see the [Confluent documentation](https://docs.confluent.io/platform/current/schema-registry/index.html).  This option is available when you have installed the 8.0.1-R2022-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Kafka properties | Add the Kafka consumer properties you need to customize to this table. For example, you can set a specific *zookeeper.connection.timeout.ms* value to avoid *ZkTimeoutException*.  For further information about the consumer properties you can define in this table, see the section describing the consumer configuration in Kafka's documentation in <http://kafka.apache.org/documentation.html#consumerconfigs>. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs.  In the implementation of the current component in Spark, the Kafka offsets are automatically managed by Spark itself, that is to say, instead of being committed to ZooKeeper or Kafka, the offsets are tracked within Spark checkpoints. For more information about this implementation, see the [Direct approach](http://spark.apache.org/docs/latest/streaming-kafka-integration.html) section in the Spark documentation. |

**Related concepts**  

* [Retrieving information from schema registry](retrieving-information-from-schema-registry "This scenario explains how to retrieve flight information from schema registry using tKafkaInputAvro in your Spark Streaming Jobs.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tkafkainputavro -->
# tKafkaInputAvro (deprecated)

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Transmits Avro-formatted messages you need to process to its following component
in the Job you are designing.

Information noteDeprecation: Spark Streaming is deprecated beginning with the R2026-09 release.
Use Spark Structured Streaming instead.

tKafkaInputAvro is a generic message broker that transmits messages in
the
AVRO
format to the Job that runs transformations over these
messages.This component
cannot handle AVRO messages created by the avro-tools libraries.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tKafkaInputAvro properties for Apache Spark Streaming

These properties are used to configure tKafkaInputAvro running in the Spark Streaming Job framework.

The Spark Streaming
tKafkaInputAvro component belongs to the Messaging family.

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
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields. |
| Broker list | Enter the addresses of the broker nodes of the Kafka cluster to be used.  The form of this address should be *hostname:port*. This information is the name and the port of the hosting node in this Kafka cluster.  If you need to specify several addresses, separate them using a comma (*,*). |
| Starting offset | Select the starting point from which the messages of a topic are consumed.  In Kafka, the sequential ID number of a message is called *offset*. From this list, you can select From beginning to start consumption from the oldest message of the entire topic, or select From latest to start from the latest message that has been consumed by the same consumer group and of which the offset is tracked by Spark within Spark checkpoints.  Note that in order to enable the component to remember the position of a consumed message, you need to activate the Spark Streaming checkpointing in the Spark Configuration tab in the Run view of the Job.  Each consumer group has its own counter to remember the position of a message it has consumed. For this reason, once a consumer group starts to consume messages of a given topic, a consumer group recognizes the latest message only with regard to the position where this group stops the consumption, rather than to the entire topic. Based on this principle, the following behaviors can be expected:   * A topic has for example *100* messages. If a   consumer group has stopped the consumption at the message of the offset *50*, then when you select From   latest, the same consumer group restarts from the offset *51*. * If you create a new consumer group or reset an existing consumer group, which, in   either case, means this group has not consumed any message of this topic, then when   you start it from latest, this new group starts and waits for the offset *101*. |
| Topic name | Enter the name of the topic from which tKafkaInput receives the feed of messages. |
| Group ID | Enter the name of the consumer group to which you want the current consumer (the tKafkaInput component) to belong.  This consumer group will be created at runtime if it does not exist at that moment.  This property is available only when you are using Spark 2.0 or the Hadoop distribution to be used is running Spark 2.0. If you do not know the Spark version you are using, ask the administrator of your cluster for details. |
| Set number of records per second to read from each Kafka partition | Enter this number within double quotation marks to limit the size of each batch to be sent for processing.  For example, if you put *100* and the batch value you define in the Spark configuration tab is *2* seconds, the size from a partition for each batch is *200* messages.  If you leave this checkbox clear, the component tries to read all the available messages in one second into one single batch before sending it, potentially resulting in Job that stops responding in case of a huge quantity of messages. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  This property is available only when you are using Spark 2.0 or the Hadoop distribution to be used is running Spark 2.0. If you do not know the Spark version you are using, ask the administrator of your cluster for details.  The TrustStore file and any used KeyStore file must be stored locally on every single Spark node that is hosting a Spark executor. |
| Use Kerberos authentication | If the Kafka cluster to be used is secured with Kerberos, select this checkbox to display the related parameters to be defined:   * JAAS configuration path: enter the   path, or browse to the JAAS configuration file to be used by the Job to   authenticate as a client to Kafka.  This JAAS file describes how the clients, the Kafka-related   Jobs in terms of *Talend*, can connect to the Kafka broker nodes, using either the kinit mode or   the keytab mode. The JAAS file must be stored in the machine where these   Jobs are executed.  *Talend*, Kerberos or Kafka does not provide this JAAS file. You need to create   it by following the explanation in [Configuring Kafka   client](http://kafka.apache.org/documentation.html#security_sasl_clientconfig) depending on the security strategy of your   organization. * Kafka brokers principal name: enter   the primary part of the Kerberos principal you defined for the brokers when   you were creating the broker cluster. For example, in this principal *kafka/kafka1.hostname.com@EXAMPLE.COM*, the primary   part to be used to fill in this field is *kafka*. * Set kinit command path: Kerberos   uses a default path to its kinit executable. If you have changed this path,   select this checkbox and enter the custom access path.  If you leave this checkbox clear, the default path is   used. * Set Kerberos configuration path:   Kerberos uses a default path to its configuration file, the *krb5.conf* file (or *krb5.ini*   in Windows) for Kerberos 5 for example. If you have changed this path,   select this checkbox and enter the custom access path to the Kerberos   configuration file.  If you leave this checkbox clear, a given strategy is applied   by Kerberos to attempt to find the configuration information it requires.   For details about this strategy, see the *Locating the   krb5.conf Configuration File* section in [Kerberos requirements](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html).   For further information about how a Kafka cluster is secured with Kerberos, see [Authenticating using SASL](http://kafka.apache.org/documentation.html#security_sasl).  This check box is available since Kafka 0.9.0.1. |
| Use Schema Registry | Select this check box to use Confluent Schema Registry and to display the related parameters to be defined:  * URL: enter the Schema Registry instance URL. * Basic authentication: select this check box and   enter your credentials in the Username and   Password. * Use the keystore of Kafka broker: select this   check box to enable the SSL or TLS encrypted connection using the same   tSetKeystore component used by the Kafka broker. This checkbox is   available when you select the Use SSL/TLS check   box and clear the Set schema registry   keystore. * Set schema registry keystore: select this check   box to enable the SSL or TLS encrypted connection. Then you need to use   the tSetKeystore component in the same Job to   specify the encryption information.  For more information about Schema Registry, see the [Confluent documentation](https://docs.confluent.io/platform/current/schema-registry/index.html).  This option is available when you have installed the 8.0.1-R2022-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Kafka properties | Add the Kafka consumer properties you need to customize to this table. For example, you can set a specific *zookeeper.connection.timeout.ms* value to avoid *ZkTimeoutException*.  For further information about the consumer properties you can define in this table, see the section describing the consumer configuration in Kafka's documentation in <http://kafka.apache.org/documentation.html#consumerconfigs>. |
| Use hierarchical mode | Select this check box to map the binary (including hierarchical) Avro schema to the flat schema defined in the schema editor of the current component. If the Avro message to be processed is flat, leave this check box clear.  Once selecting it, you need set the following parameter(s):   * Local path to the avro   schema: browse to the file which defines the   schema of the Avro data to be processed. * Mapping: create the map   between the schema columns of the current component and the data stored   in the hierarchical Avro message to be handled. In the   Node column, you need to   enter the JSON path pointing to the data to be read from the   Avro message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component, along with the Spark Streaming component Palette it belongs to, appears only when you are creating a Spark Streaming Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs.  In the implementation of the current component in Spark, the Kafka offsets are automatically managed by Spark itself, that is to say, instead of being committed to ZooKeeper or Kafka, the offsets are tracked within Spark checkpoints. For more information about this implementation, see the [Direct approach](http://spark.apache.org/docs/latest/streaming-kafka-integration.html) section in the Spark documentation. |

**Related concepts**  

* [Retrieving information from schema registry](retrieving-information-from-schema-registry "This scenario explains how to retrieve flight information from schema registry using tKafkaInputAvro in your Spark Streaming Jobs.")
