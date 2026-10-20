<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-rabbitmq/crabbitmq · versión 8.0 -->
# cRabbitMQ

Last updated: 9/30/2026

Sends messages to, or consumes messages from RabbitMQ compliant message
brokers.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cRabbitMQ Standard properties

These properties are used to configure cRabbitMQ running in the
Standard Route framework.

The Standard
cRabbitMQ component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| ConnectionFactory | Select a connection factory to be used for handling messages. |
| Exchange name | Type in the name of the exchange that the produced message will be sent to or the consumed message queue will be bound to. |
| Exchange type | Select the type of the exchange from direct, topic, fanout, and headers. This option is available when the Auto declare check box is selected. |
| Routing key | Enter the value of the routing key. When cRabbitMQ is used as a consumer, this option is available when the Auto declare check box is selected. |
| Queue names | Enter the name of the queue(s) to use for consuming or producing messages. Multiple queue names can be separated by comma. When cRabbitMQ is used as a producer, this option is available when the Auto declare check box is selected. |
| Auto declare | Select this check box to auto-declare binding between exchange, queue and routing key. When cRabbitMQ is used as a consumer, this option is enabled by default. Information noteNote: This option is available only if you have installed the R2025-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Parameters | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding value field and enter a value. See the site <https://camel.apache.org/components/latest/spring-rabbitmq-component.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cRabbitMQ can be a start, middle or end component in a Route. It has to be used with the cMQConnectionFactory component, which creates a connection to a MQ server. For more information about cMQConnectionFactory, see [cMQConnectionFactory](/talend/en-US/components/8.0/mediation-rabbitmq/cmqconnectionfactory). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Sending messages to and receiving messages from RabbitMQ service](sending-messages-to-and-receiving-messages-from-rabbitmq-service)
