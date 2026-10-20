<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp · versión 8.0 -->
# cAMQP

Last updated: 9/30/2026

Exchanges messages between a Route and a JMS provider using the AMQP
broker.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cAMQP Standard properties

These properties are used to configure cAMQP running in the Standard Job framework.

The Standard
cAMQP component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| URI/Type | Select the messaging type, either queue or topic. |
| URI/Destination | Type in a name for the message queue or topic in the message broker. |
| ConnectionFactory | Click [...] and select an MQ connection factory to be used for handling messages. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Parameters | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/amqp.html> for available options.  Be sure to set the clientId parameter to a unique value if you need to deploy multiple Routes using this component to Runtime. Otherwise the Routes will throw exception in Runtime. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAMQP can be a start, middle or end component in a Route. It has to be used with the cMQConnectionFactory component, which creates a connection to a MQ server. For more information about cMQConnectionFactory, see [cMQConnectionFactory](/talend/en-US/components/8.0/mediation-amqp/cmqconnectionfactory). |
| Limitation | n/a |

**Related concepts**  

* [Sending messages to and receiving messages from an AMQP broker](camqp-cmqconnectionfactory-clog-csetbody-sending-messages-to-and-receiving-messages-from-amqp-broker)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-sending-messages-to-and-receiving-messages-from-amqp-broker -->
# Sending messages to and receiving messages from an AMQP broker

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario will show you how to use the cAMQP component
to send messages to and consume messages from a JMS Queue or Topic. To do this, two
Routes are built, a message producer Route, and a consumer Route. Messages are sent to
the AMQP broker in the producer Route and then consumed in the consumer Route.

In this use case, Apache ActiveMQ is used as the message broker which supports the AMQP 1.0
protocol. You need to launch the ActiveMQ server before executing the Route. For more
information about installing and launching ActiveMQ server, see the site <http://activemq.apache.org/index.html>.

### In this section

* [Building the producer Route](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-building-producer-route)
* [Building the consumer Route](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-building-consumer-route)

**Related reference**  

* [cAMQP](camqp "Exchanges messages between a Route and a JMS provider using the AMQP broker.")
* [cMQConnectionFactory](cmqconnectionfactory "Encapsulates a set of configuration parameters to connect to a MQ server. The connection can be called by multiple cAMQP, cJMS, cMQTT, cRabbitMQ, or cWMQ components in a Route.")

**Related information**  

* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-building-consumer-route -->
# Building the consumer Route

Last updated: 9/30/2026

### In this section

* [Adding components to arrange the flow](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-adding-components-to-arrange-flow)
* [Configuring how the message is processed](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-configuring-how-message-is-processed)
* [Executing the Route](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-building-producer-route -->
# Building the producer Route

Last updated: 9/30/2026

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-configuring-components)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-viewing-code-and-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-adding-components-to-arrange-flow -->
# Adding components to arrange the flow

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a cMQConnectionFactory, a cAMQP, and a cLog component
   onto the design workspace.
2. Label the components for better identification of their roles and link
   them with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-configuring-how-message-is-processed -->
# Configuring how the message is processed

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory
   component to display its Basic settings
   view in the Component tab.
2. From the MQ Server list, select AMQP 1.0 to handle messages. Keep the default
   settings of the other options.
3. Double-click the cAMQP component to
   display its Basic settings view in the
   Component tab.
4. Specify the same URI Type and Destination in the consumer cAMQP component as in the producer.

   In the ConnectionFactory field. click
   [...] and select the MQ connection
   factory that you have just configured to handle messages.
5. Keep the default settings of the cLog component to
   log the message exchanges.
6. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-executing-route -->
# Executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message flow is routed from cAMQP\_1 to
   cLog\_1.
2. Press F6 to execute the Route. The logs of the message
   exchange are printed in the console.
3. In the ActiveMQ Web Console, you can see that the messages in
   *myqueue* have been consumed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory component to
   display its Basic settings view in the
   Component tab.
2. From the MQ Server list, select AMQP 1.0 to handle messages. Keep the default
   settings of the other options.
3. Double-click the cTimer component to open its Basic settings view in the Component tab.
4. In the Repeat field, enter
   `5` to generate the message exchange five times. Keep the
   default settings of the other options.
5. Double-click the cSetBody component to
   open its Basic settings view in the
   Component tab.
6. Select SIMPLE from the Language drop-down list and type in `"Hello
   world"` in the Expression field as
   the message body.
7. Double-click the cAMQP component to open its Basic settings view in the Component tab.
8. From the Type list, select queue or topic to send the
   messages to a JMS queue or topic. In this use case, queue is used.

   In the Destination field, type in
   a name for the queue, for example `"myqueue"`.

   In the ConnectionFactory field, click [...] and select the MQ connection factory that
   you have just configured to handle messages.
9. Keep the default settings of the cLog component to
   log the message exchanges.
10. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a cMQConnectionFactory, a cTimer, a cSetBody, a
   cAMQP, and a cLog component onto the design workspace.
2. Label the components for better identification of their roles and link
   them with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amqp/camqp-cmqconnectionfactory-clog-csetbody-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message flow from cTimer\_1 is given a payload by
   cSetBody\_1 and then sent to cAMQP\_1 and
   cLog\_1.
2. Press F6 to execute the Route. The logs of the message
   exchange are printed in the console.
3. In the ActiveMQ Web Console, you can see that the message queue
   *myqueue*has been created.
