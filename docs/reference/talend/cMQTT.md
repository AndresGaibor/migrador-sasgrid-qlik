<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt · versión 8.0 -->
# cMQTT

Last updated: 9/30/2026

Sends messages to, or consumes messages from MQTT compliant message
brokers.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cMQTT Standard properties

These properties are used to configure cMQTT running in the Standard Job framework.

The Standard
cMQTT component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| ConnectionFactory | This option appears when Use Connection Factory is selected. Click [...] and select a connection factory to be used for handling messages. |
| Topic Name | Type in a name for the message topic in the message broker. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Parameters | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding value field and enter a value. See the site <http://camel.apache.org/amqp.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cMQTT can be a start, middle or end component in a Route. It has to be used with the cMQConnectionFactory component, which creates a connection to a MQ server. For more information about cMQConnectionFactory, see [cMQConnectionFactory](/talend/en-US/components/8.0/mediation-amqp/cmqconnectionfactory). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Sending messages to and receiving messages from an MQTT broker](cmqtt-cmqconnectionfactory-clog-csetbody-sending-messages-to-and-receiving-messages-from-mqtt-broker)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-sending-messages-to-and-receiving-messages-from-mqtt-broker -->
# Sending messages to and receiving messages from an MQTT broker

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario will show you how to use the cMQTT component
to send messages to and consume messages from an MQTT broker. To do this, two Routes are
built, a message producer Route, and a consumer Route. Messages are sent to the MQTT
broker in the producer Route and then consumed in the consumer Route.

In this use case, Apache ActiveMQ is used as the message broker which supports the MQTT
protocol. You need to launch the ActiveMQ server before executing the Route. For more
information about installing and launching ActiveMQ server, see the site <http://activemq.apache.org/index.html>.

### In this section

* [Building the producer Route](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-building-producer-route)
* [Building the consumer Route](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-building-consumer-route)

**Related reference**  

* [cMQTT](cmqtt "Sends messages to, or consumes messages from MQTT compliant message brokers.")
* [cMQConnectionFactory](cmqconnectionfactory "Encapsulates a set of configuration parameters to connect to a MQ server. The connection can be called by multiple cAMQP, cJMS, cMQTT, cRabbitMQ, or cWMQ components in a Route.")

**Related information**  

* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-building-consumer-route -->
# Building the consumer Route

Last updated: 9/30/2026

### In this section

* [Arranging the flow of the message](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-arranging-flow-of-message)
* [Configuring how the message is processed](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-configuring-how-message-is-processed)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-viewing-code-and-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-building-producer-route -->
# Building the producer Route

Last updated: 9/30/2026

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-configuring-components)
* [Viewing the code](/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-viewing-code)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-arranging-flow-of-message -->
# Arranging the flow of the message

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a cMQConnectionFactory, a cMQTT, and a cLog component
   onto the design workspace.
2. Label the components for better identification of their roles and link
   them with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-configuring-how-message-is-processed -->
# Configuring how the message is processed

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory
   component to display its Basic settings
   view in the Component tab.
2. Configure the cMQConnectionFactory
   component as the one in the producer Route to connect to the same MQTT
   broker.
3. Double-click the cMQTT component to
   display its Basic settings view in the
   Component tab.
4. In the ConnectionFactory field, click
   [...] and select the MQ connection
   factory that you have just configured to handle messages.

   Specify the same Topic Name in the
   consumer cMQTT component as in the
   producer.
5. Keep the default settings of the cLog component to
   log the message exchanges.
6. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message flow is routed from cMQTT\_1 to
   cLog\_1.
2. Press F6 to execute the Route. In the execution console
   you can see that there's no message exchange yet.
3. Execute the producer Route. The logs of the message exchange are printed
   in the console.
4. In the consumer Route, the messages are consumed and shown in the execution
   console.
5. In the ActiveMQ Web Console, you can see that the topic
   *mytopic* has been created and the messages are
   consumed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory
   component to display its Basic settings
   view in the Component tab.
2. From the MQ Server list, select MQTT to handle messages. 

   In the Host Name field, keep
   the default value `"127.0.0.1"` as the local ActiveMQ server is
   used as the message broker in this example.

   In the Port field, keep the
   default `1883`.

   Keep the default settings of the other options.
3. Double-click the cTimer component to open
   its Basic settings view in the Component tab.
4. In the Repeat field, enter 5
   to generate the message exchange five times. Keep the default settings of
   the other options.
5. Double-click the cSetBody component to
   open its Basic settings view in the
   Component tab.
6. Select SIMPLE from the
   Language list box and type in
   `"Hello world"` in the Expression field as the message body.
7. Double-click the cMQTT component to open its Basic settings view in the Component tab.
8. In the ConnectionFactory field, click
   [...] and select the MQ connection
   factory that you have just configured to handle messages.

   In the Topic Name field, type
   in a name for the topic, for example `"mytopic"`.
9. Keep the default settings of the cLog component to
   log the message exchanges.
10. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cMQConnectionFactory, a cTimer, a cSetBody, a cMQTT, and a
   cLog component onto the design
   workspace.
2. Label the components for better identification of their roles and link
   them with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-mqtt/cmqtt-cmqconnectionfactory-clog-csetbody-viewing-code -->
# Viewing the code

Last updated: 9/30/2026

## Procedure

Click the Code tab at the bottom of the
design workspace to check the generated code.

As shown above, the message flow from cTimer\_1 is given a payload by
cSetBody\_1 and then sent to cMQTT\_1 and
cLog\_1.
