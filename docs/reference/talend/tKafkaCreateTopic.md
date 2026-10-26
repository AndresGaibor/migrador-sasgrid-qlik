<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/kafka/tkafkacreatetopic · versión 8.0 -->
# tKafkaCreateTopic

Last updated: 9/30/2026

Creates a Kafka topic that the other Kafka components can use.

This component allows you to visually issue the command to create a topic with various topic-level properties.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tKafkaCreateTopic Standard properties

These properties are used to configure tKafkaCreateTopic running in the Standard Job framework.

The Standard
tKafkaCreateTopic component belongs to the Internet family.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Version | Select the version of the Kafka cluster to be used.  If you have installed the 8.0.1-R2024-02 Talend Studio Monthly update or a later one delivered by Talend, the Kafka 2.4.x version and previous versions are deprecated. |
| Action on topic | Select how a topic is created.  * Create topic: it creates a topic. If this topic   exists already, the entire Job is stopped. * Create topic if not exists: it creates a topic   when this topic does not exist. If this topic exists, the Job skip the   creation to move to the next step. * Alter topic: it updates the configuration of an   existing topic. If the topic does not exist, the operation fails and the   Job stops. |
| Topic name | Enter the name of the topic to be created. |
| Broker list | Enter the addresses of the broker nodes of the Kafka cluster to be used.  The form of this address should be *hostname:port*. This information is the name and the port of the hosting node in this Kafka cluster.  If you need to specify several addresses, separate them using a comma (*,*). |
| Replication factor | Enter the number of the replicas to be created for the logs (the message sets) of the topic partitions. |
| Number of partitions | Enter the number of partitions to be created for the topic. |
| Set topic retention time (ms) | Select this checkbox to define the maximum time in milliseconds during which the contents of the topic are retained.  At the end of the time, the contents are removed or compacted depending on the policy you define in the Topic properties table in the Advanced settings view. |
| Use SSL/TLS | Select this checkbox to enable the SSL or TLS encrypted connection.  Information noteNote: This option is available when you have installed the 8.0.1-R2022-10 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Set keystore | Select this checkbox to enable the SSL or TLS encrypted connection via a tSetKeystore component.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  This checkbox is available when you select the Use SSL/TLS checkbox.  Information noteNote: This option is available when you have installed the 8.0.1-R2022-10 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use Kerberos authentication | If the Kafka cluster to be used is secured with Kerberos, select this checkbox to display the related parameters to be defined:   * JAAS configuration path: enter the   path, or browse to the JAAS configuration file to be used by the Job to   authenticate as a client to Kafka.  This JAAS file describes how the clients, the Kafka-related   Jobs in terms of *Talend*, can connect to the Kafka broker nodes, using either the kinit mode or   the keytab mode. The JAAS file must be stored in the machine where these   Jobs are executed.  *Talend*, Kerberos or Kafka does not provide this JAAS file. You need to create   it by following the explanation in [Configuring Kafka   client](http://kafka.apache.org/documentation.html#security_sasl_clientconfig) depending on the security strategy of your   organization. * Kafka brokers principal name: enter   the primary part of the Kerberos principal you defined for the brokers when   you were creating the broker cluster. For example, in this principal *kafka/kafka1.hostname.com@EXAMPLE.COM*, the primary   part to be used to fill in this field is *kafka*. * Set kinit command path: Kerberos   uses a default path to its kinit executable. If you have changed this path,   select this checkbox and enter the custom access path.  If you leave this checkbox clear, the default path is   used. * Set Kerberos configuration path:   Kerberos uses a default path to its configuration file, the *krb5.conf* file (or *krb5.ini*   in Windows) for Kerberos 5 for example. If you have changed this path,   select this checkbox and enter the custom access path to the Kerberos   configuration file.  If you leave this checkbox clear, a given strategy is applied   by Kerberos to attempt to find the configuration information it requires.   For details about this strategy, see the *Locating the   krb5.conf Configuration File* section in [Kerberos requirements](http://docs.oracle.com/javase/7/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html).   For further information about how a Kafka cluster is secured with Kerberos, see [Authenticating using SASL](http://kafka.apache.org/documentation.html#security_sasl).  This checkbox is available since Kafka 0.9.0.1. |
| Set kinit command path | Select this checkbox to use the kinit command to log in to the Kerberos authentication and enter the path to this command. |
| Set kerberos configuration path | Select this checkbox to use the krb5.conf file to authenticate to Kerberos and enter the path to this file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Topic properties | Add the Kafka topic properties you need to customize to this table.  For more information about the topic-level properties you can define in this table, see the section describing the [topic-level configuration](http://kafka.apache.org/documentation.html#topic-config) from the official Kafka documentation. |
| Kafka properties | Add the Kafka Admin properties you need to customize to this table. For example, you can use this table to specify SSL configuration by providing the following properties and associated values:  * "security.protocol" property with "SSL"   value * "ssl.truststore.location" property with   "context.ssl\_trustore\_location" value * "ssl.truststore.password" property with   "context.ssl\_password" value  For more information about the Kafka Admin properties you can define in this table, see [Admin Configs](https://kafka.apache.org/documentation/#adminclientconfigs) from the official Kafka documentation.  This property is only available when you use Kafka 3.2.x version. |
| Timeout (ms) | Specify the amount of time in milliseconds you want Talend Studio to wait for:  * the connection to Kafka, for Kafka 2.4.x onwards versions * the session of and connection to ZooKeeper, for Kafka 2.2.1 backwards   versions   The default value is 10000 milliseconds.  Information noteNote: This option is available when you have installed the 8.0.1-R2022-11 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used standalone to create a topic that the other Kafka components can use in the other Jobs or subJobs. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Analyzing a Twitter flow in near real-time (deprecated)](tkafkainput-tkafkacreatetopic-thdfsconfiguration-ts3configuration-analyzing-twitter-flow-in-near-real-time-spark-stream-component-in-this)
