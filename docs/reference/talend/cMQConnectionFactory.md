<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/cmqconnectionfactory · versión 8.0 -->
# cMQConnectionFactory

Last updated: 9/30/2026

Encapsulates a set of configuration parameters to connect to a MQ server. The
connection can be called by multiple cAMQP, cJMS, cMQTT,
cRabbitMQ, or cWMQ components
in a Route.

## cMQConnectionFactory Standard properties

These properties are used to configure cMQConnectionFactory
running in the Standard Job framework.

The Standard
cMQConnectionFactory component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| MQ Server | Select an MQ server from ActiveMQ, RabbitMQ, WebSphere MQ Jms, WebSphere MQ Native, AMQP 1.0, MQTT, or Customized.  Information noteNote: The RabbitMQ option is available only when you have installed the 8.0.1-R2025-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  The connection to the WebSphere MQ native server can also be configured in a properties file. For more information, see [Configuring connection to the WebSphere MQ native server in a properties file](/talend/en-US/components/8.0/mediation-amqp/cmqconnectionfactory-cmqconnectionfactory-configuring-connection-to-websphere-mq-native-server-in-properties-file).  For more information on connecting to WebSphere MQ, see [Connecting to Websphere MQ](/talend/r/en-US/8.0/esb-service-developer-guide/connecting-to-websphere-mq). |
| Use Transaction (for ActiveMQ, WebSphere MQ Jms, and Customized only) | Select this check box to enable local transaction in the Route that consumes messages from the MQ server. If exception occurs in the Route, the message in the message broker will be sent to the dead letter queue after the maximumRedeliveries configured for the Redelivery Policy, and will not be consumed by the Route. For more information, see the site <http://camel.apache.org/transactional-client.html>. |
| Broker URI (for ActiveMQ only) | Type in the URI of the message broker.  For intra-Route message handling, you can simply use the default URI `vm://localhost?broker.persistent=false` for ActiveMQ. Information noteWarning: If you try to set the Broker URI parameter with `"{{activemq_url}}"`, you may have the following error message: ``` Invalid broker URI: {{activemq_url}} ``` After configuring a property component, you can use the Camel property syntax {{...}} directly in most Talend components. However, there are a few exceptions. The cMQConnectionFactory component is one of those exceptions where you can not directly use the {{...}} syntax.  Instead of using `"{{activemq_url}}"`, call the Camel resolvePropertyPlaceholders method, as shown below: ``` camelContext.resolvePropertyPlaceholders("{{activemq_url}}") ``` |
| HTTP Transport (for ActiveMQ only) | Select this check box to enable the HTTP based connection to the ActiveMQ broker. |
| Use PooledConnectionFactory (for ActiveMQ only) | Select this check box to use PooledConnectionFactory. |
| Max Connections (for ActiveMQ only) | Specify the maximum number of connections of the PooledConnectionFactory. This field is available only when the Use PooledConnectionFactory check box is selected. |
| Max Active (for ActiveMQ only) | Specify the maximum number of sessions per connection. This field is available only when the Use PooledConnectionFactory check box is selected. |
| Idle Timeout (in ms) (for ActiveMQ only) | Specify the maximum waiting time (in milliseconds) before the connection breaks. This field is available only when the Use PooledConnectionFactory check box is selected. |
| Expiry Timeout (in ms) (for ActiveMQ only) | Specify the time (in milliseconds) before the connection breaks since it is used for the first time. The default value is 60000. The expiry is disabled if 0 is specified. This field is available only when the Use PooledConnectionFactory check box is selected. |
| Host Name (for RabbitMQ, WebSphere MQ Jms, WebSphere MQ Native, AMQP 1.0 and MQTT only) | Type in the name or IP address of the host on which the IBM WebSphere MQ server or the MQTT broker is running. For WebSphere MQ Jms, WebSphere MQ Native and AMQP 1.0, the default is "localhost". For MQTT, the default is `127.0.0.1`.  For AMQP 1.0, the Host Name can be set as either a standard single IP address or host name, or a failover URL, for example `"failover:(amqp://localhost:5672)"`. |
| Port (for RabbitMQ, WebSphere MQ Jms, WebSphere MQ Native, AMQP 1.0 and MQTT only) | Type in the port of the MQ server.  * For WebSphere MQ Jms and WebSphere MQ   Native, the default is `1414`. * For AMQP 1.0, the default is   `5672`. The value of the port will be ignored if   the Host Name is a failover URL. * For MQTT, the default is   `1883`. |
| Virtual Host (for RabbitMQ only) | Specify the virtual host to be used for publishing or receiving messages.  Information noteNote: This option is available only when you have installed the 8.0.1-R2025-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Transport Type (for WebSphere MQ Jms only) | Select a type of message transport between the IBM WebSphere MQ server and the WebSphere MQ broker from Bindings, Bindings then Client, and Client. |
| Queue Manager (for WebSphere MQ Jms only) | Type in the name of the queue manager, or specify the name of the IBM WebSphere MQ server to find a queue manager. |
| Channel (for WebSphere MQ Jms and WebSphere MQ Native only) | Specify the name of the channel through which the connection is established. For WebSphere MQ Jms, the default is SYSTEM.DEF.SVRCONN. For WebSphere MQ Native, the default is channel.name. |
| Name (for WebSphere MQ Native only) | Specify the name of the queue manager to which the connection is established. |
| Use Authentication (for ActiveMQ, WebSphere MQ Jms, WebSphere MQ Native, AMQP 1.0, and MQTT only) | Select this check box and provide the username and password for the MQ server to validate the access permission. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. For WebSphere MQ Native server, provide the CCSID (Coded Character Set Identifier) in addition that defines a numeric ordering of characters. For more information about CCSID, see the site <http://www-01.ibm.com/software/globalization/cdra/appendix_c.html>. |
| Dependencies (for WebSphere MQ Jms, WebSphere MQ Native and Customized only) | Specify additional libraries required by the MQ broker. |
| Use SSL (for AMQP 1.0 and MQTT only) | Select this check box to connect to the MQ server over the SSL protocol. For MQTT, specify the TrustStore file containing the list of certificates that the MQ server trusts and enter the password used to check the integrity of the TrustStore data. |
| Auto Reconnect (for MQTT only) | Select this check box to reconnect to the server if the connection is lost. |
| Connection timeout (for MQTT only) | This maximum time interval in seconds that the the client will wait for the network connection to the MQTT server to be established, 30 by default. |
| Max Reconnect Delay (for MQTT only) | The maximum time in milliseconds between attempts to re-establish an initial or failed connection, 128000 by default. |
| MQTT version (for MQTT only) | Select the MQTT version to connect with, 3.1.1 by default. |
| Quality of Service (for MQTT only) | The MQTT Quality of Service to use for message exchanges. It can be one of AtMostOnce, AtLeastOnce or ExactlyOnce. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cMQConnectionFactory can be added directly in a Route without any input or output component linked. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules).  To use the WebSphere MQ Native server, you need to download the com.ibm.mq.jar, com.ibm.mq.commonservices.jar, com.ibm.mq.headers.jar, com.ibm.mq.jmqi.jar and connector.jar from the IBM website and add them to the Dependencies list. |
