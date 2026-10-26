<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms · versión 8.0 -->
# cJMS

Last updated: 9/30/2026

Exchanges messages between a Route and a JMS provider.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cJMS Standard properties

These properties are used to configure cJMS running in the Standard Job framework.

The Standard
cJMS component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| URI/Type | Select the messaging type, either queue or topic. |
| URI/Destination | Type in a name for the JMS queue or topic. |
| ConnectionFactory | Click the [...] button and select a JMS connection factory to be used for handling messages or enter the name of the corresponding cMQConnectionFactory component directly in the field. |

## Advanced settings

| Properties | Description |
| --- | --- |
| URI Options | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding value field and enter a value. See the site <http://camel.apache.org/jms.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cJMS can be a start, middle or end component in a Route. It has to be used with the cMQConnectionFactory component, which creates a connection to a MQ server. For more information about cMQConnectionFactory, see [cMQConnectionFactory](/talend/en-US/components/8.0/mediation-amqp/cmqconnectionfactory). |
| Limitation | n/a |

**Related concepts**  

* [Sending and receiving a message from a JMS queue](cjms-cmqconnectionfactory-cfile-cprocessor-sending-and-receiving-message-from-jms-queue)
* [Sending and receiving a scheduled delivery of messages from a JMS Queue using Camel Quartz](cmqconnectionfactory-cjms-csetbody-cmessagingendpoint-sending-and-receiving-scheduled-delivery-of-messages-from-jms-queue-using-camel-quartz)
* [Setting up a JMS local transaction](cjms-cmqconnectionfactory-cprocessor-cconfig-setting-up-jms-local-transaction)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cfile-cprocessor-sending-and-receiving-message-from-jms-queue -->
# Sending and receiving a message from a JMS queue

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cJMS component sends messages
from the local file system to a message queue in one sub-route, and the messages are
then consumed by another cJMS component in the other
sub-route.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cfile-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cfile-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cfile-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cJMS](cjms "Exchanges messages between a Route and a JMS provider.")
* [cMQConnectionFactory](cmqconnectionfactory "Encapsulates a set of configuration parameters to connect to a MQ server. The connection can be called by multiple cAMQP, cJMS, cMQTT, cRabbitMQ, or cWMQ components in a Route.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-setting-up-jms-local-transaction -->
# Setting up a JMS local transaction

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a local transaction with three steps is performed to send,
test, and consume a JMS message:

1. The first Route is used to send a "hello world!"
   message to feed the queue.hello JMS queue.
2. The second Route is used to test the received JMS message. This message
   is redelivered six times to the queue.hello queue and is then moved
   to the Dead Letter JMS queue. The Route is programmed to throw an
   exception every time an exchange is processed by the Route.
3. The last Route is used to consume the "hello world!"
   message from the Dead Letter JMS queue.

In this use case, the local ActiveMQ server is used to handle messages between
different Routes. The ActiveMQ server needs to be started before executing the Routes. For
more information on installing and launching ActiveMQ server, see the Apache website <http://activemq.apache.org/index.html>.

### In this section

* [Sending a message to the queue.hello JMS queue](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-sending-message-to-queue.hello-jms-queue)
* [Testing the received message](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-testing-received-message)
* [Consuming the message from the DeadLetter JMS queue](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-consuming-message-from-deadletter-jms-queue)

**Related reference**  

* [cJMS](cjms "Exchanges messages between a Route and a JMS provider.")
* [cMQConnectionFactory](cmqconnectionfactory "Encapsulates a set of configuration parameters to connect to a MQ server. The connection can be called by multiple cAMQP, cJMS, cMQTT, cRabbitMQ, or cWMQ components in a Route.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cConfig](/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cfile-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory component to
   display its Basic settings view in the
   Component tab.
2. From the MQ Server list, select
   an MQ server. In this use case, the default ActiveMQ server is used to handle the
   messages. 

   In the Broker URI field, type
   in the URI of the message broker. Here the default URI
   `"vm://localhost?broker.persistent=false"` is used.
3. In the message producer sub-route, double-click the cFile component to display its Basic
   settings view.
4. Define the properties of the cFile
   component. 

   In this use case, simply specify the path to the folder that holds the
   source file to be sent as electronic message, and leave the other parameters
   as they are.
5. Double-click the cJMS component
   labeled `Message_producer` to display its Basic settings view.
6. From the Type list, select queue to send the messages to a JMS queue.

   In the Destination field, type
   in a name for the JMS queue, `"queue.hello"` in this use
   case.

   Double-click the [...] button next to ConnectionFactory. Select the MQ connection
   factory that you have just configured in the dialog box and click OK.
7. Switch to the message consumer sub-route, and double-click the
   cJMS component labeled
   `Message_consumer` to display its Basic settings view.
8. Configure the message consumer using exactly the same parameters as in the
   message producer.
9. Double-click the cProcessor
   component to display its Basic settings
   view.
10. In the Code area, customize the code as
    shown below to display the file names of the consumed messages on the
    Run console.

    ```
    System.out.println("Message consumed: "+
    exchange.getIn().getHeader("CamelFileName"));
    ```
11. Press Ctrl+S to save your Routes.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cfile-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, expand the Connectivity/Messaging folder, and drop a cMQConnectionFactory component onto the design
   workspace to specify the JMS connection factory for handling
   messages.
2. From the Connectivity folder, drop one cFile and two cJMS components onto the design workspace.
3. From the Custom folder, drop a cProcessor component onto the design workspace.
4. Connect the cFile component to a
   cJMS component using a Row > Route
   connection as the message producer sub-route.
5. Connect the other cJMS component to the
   cProcessor component using a Row > Route
   connection as the message consumer sub-route.
6. Label the components properly for better identification of their
   functionalities.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cfile-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code. 

   In the partially shown code, a message route is built from the
   File\_source\_cFile\_1
   .to the cJMS\_1 which then sends the message to a
   message queue via a broker identified by
   vm://localhost?broker.persistent=false. The message
   from the Message\_consumer\_cJMS\_2 is processed
   by cProcessor\_1.
2. Click the Run button in the Run view to launch the execution of your Route.
   You can also press F6 to execute it. 

   RESULT: The message is received by the consumer, as shown on the Run console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-consuming-message-from-deadletter-jms-queue -->
# Consuming the message from the *DeadLetter* JMS queue

Last updated: 9/30/2026

### In this section

* [Arranging the flow of the message](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-arranging-flow-of-message)
* [Configuring how the message is processed](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-configuring-how-message-is-processed)
* [Launching the execution of the Route](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-launching-execution-of-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-sending-message-to-queue.hello-jms-queue -->
# Sending a message to the queue.hello JMS queue

Last updated: 9/30/2026

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-configuring-components)
* [Executing the Route](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-testing-received-message -->
# Testing the received message

Last updated: 9/30/2026

### In this section

* [Linking the components](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-linking-components)
* [Defining the settings of the components](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-defining-settings-of-components)
* [Running the Route](/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-running-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-arranging-flow-of-message -->
# Arranging the flow of the message

Last updated: 9/30/2026

## Procedure

1. From the Palette, drop the three following components
   onto the design workspace: one cMQConnectionFactory, one cJMS and one cProcessor
   component.
2. Connect the cJMS component to the
   cProcessor component using a Row > Route
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-configuring-how-message-is-processed -->
# Configuring how the message is processed

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory component to
   display its Basic settings view in the
   Component tab.
2. From the MQ Server list, select an MQ
   server. In this use case, we use the default ActiveMQ server to handle the
   messages.
3. In the Broker URI field, type in Active
   MQ's default URI of the localhost server: *"tcp://localhost:61616"*.
4. Double-click the cJMS
   component labeled *DeadLetterQueueJMS* to display its
   Basic settings view.
5. From the Type list, select queue to send the messages to a JMS queue.

   In the Destination field, type in a name
   for the JMS queue, *"ActiveMQ.DLQ"* in this
   use case (the default *Dead Letter* Queue
   in ActiveMQ).

   Double-click the [...] button next to ConnectionFactory. Select the MQ connection
   factory that you have just configured in the dialog box and click OK.
6. Double-click the cProcessor component
   labeled *PrintMsg* to display its
   Basic settings view in the Component tab, and customize the code in the
   Code area to display the received
   message intercepted on the console.

   ```
   System.out.println("AMQ Receive: "+ 
   exchange.getIn().getBody(String.class));
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-launching-execution-of-route -->
# Launching the execution of the Route

Last updated: 9/30/2026

## Procedure

Click the Run button in the Run view to launch the execution of your Route.
You can also press F6 to execute it. 

RESULT: The "hello world!" message that was in the
Dead Letter queue is consumed, as shown in the Run console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory component labeled
   *AMQ\_Send\_ConnectionFactory* to display
   its Basic settings view in the Component tab.
2. From the MQ Server list, select an MQ
   server. In this use case, we use the default ActiveMQ server to handle the
   messages.
3. In the Broker URI field, type in Active
   MQ's default URI of the localhost server: *"tcp://localhost:61616"*.
4. Double-click the cConfig component, which
   is labeled *DatasetConfig*, to display its
   Basic settings view in the Component tab and set its parameters.
5. Write a piece of code in the Code field
   to register the dataset instance *hello*
   into the registry, as shown below. 

   ```
   org.apache.camel.component.dataset.SimpleDataSet dataset = new 
   org.apache.camel.component.dataset.SimpleDataSet(1);
   dataset.setDefaultBody("Test Data: hello world!");
   org.apache.camel.impl.SimpleRegistry registry = new  
   org.apache.camel.impl.SimpleRegistry();
        registry.put("hello",dataset);
   camelContext.setRegistry(registry);
   ```
6. Double-click the cMessagingEndpoint component, which is labeled *SimpleDatasetGen*, to display its Basic
   settings view in the Component
   tab and set its parameters.
7. In the URI field, enter
   *dataset:hello* between the quotation marks.
8. Double-click the cJMS
   component labeled *AMQ\_Send* to display its Basic settings view.
9. From the Type list, select queue to send the message to a JMS queue.

   In the Destination field, type in a name
   for the JMS queue, *"queue.hello"* in this
   use case.

   Double-click the [...] button next to ConnectionFactory. Select the MQ connection
   factory that you have just configured in the dialog box and click OK.
10. Double-click the cProcessor component
    labeled *PrintSendMsg* to display its
    Basic settings view in the Component tab, and customize the code in the
    Code area to display the sent message
    intercepted on the console.

    ```
    System.out.println("AMQ Send: "+
    exchange.getIn().getBody(String.class));
    ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drop the five following components
   onto the design workspace: one cMQConnectionFactory, one cConfig, one cMessagingEndpoint, one cJMS and one cProcessor
   component.
2. Connect the cMessagingEndpoint component
   to the cJMS using a Row > Route
   connection.
3. Connect the cJMS component to the
   cProcessor component using a Row > Route
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-executing-route -->
# Executing the Route

Last updated: 9/30/2026

## Procedure

Click the Run button in the Run view to launch the execution of your Route.
You can also press F6 to execute it. 

RESULT: One "hello world!" message is sent to the
JMS Queue, as shown in the Run console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-defining-settings-of-components -->
# Defining the settings of the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cMQConnectionFactory component labeled
   `AMQ_Rev_ConnectionFactory` to display its Basic settings view in the Component tab.
2. From the MQ Server list, select
   an MQ server. In this use case, the default ActiveMQ server is used to handle the
   messages. 

   Select the Use transaction
   check box.
3. In the Broker URI field, type in
   Active MQ's default URI of the localhost server:
   `"tcp://localhost:61616"`.
4. Double-click the cJMS component
   labeled `AMQ_Rev` to display its Basic
   settings view.
5. From the Type list, select queue to send the messages to a JMS queue.

   In the Destination field, type
   in a name for the JMS queue, `"queue.hello"` in this use
   case.

   Double-click the [...] button next to ConnectionFactory. Select the MQ connection
   factory that you have just configured in the dialog box and click OK.
6. Double-click the first cProcessor component labeled `PrintRevMsg` to
   display its Basic settings view in the
   Component tab, and customize the code in the
   Code area to display the received message
   intercepted on the console.

   ```
   System.out.println("AMQ Receive: "+
   exchange.getIn().getBody(String.class));
   ```
7. Double-click the second cProcessor component labeled `ThrowEx` to
   display its Basic settings view in the
   Component tab, and customize the code in the
   Code area to throw the Force
   fail exception every time an exchange is processed by the Route.

   ```
   throw new Exception("Force fail")
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-linking-components -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drop the four following components
   onto the design workspace: one cJMS, two
   cProcessor components and one cMQConnectionFactory.
2. Connect the cJMS component to the first
   cProcessor using a Row > Route
   connection.
3. Connect the first cProcessor component to
   the second cProcessor component using a
   Row > Route connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-jms/cjms-cmqconnectionfactory-cprocessor-cconfig-running-route -->
# Running the Route

Last updated: 9/30/2026

## Procedure

Click the Run button in the Run view to launch the execution of your Route.
You can also press F6 to execute it. 

RESULT: The "hello world!" message is tested and a
rollback transaction is performed. Once the message redelivery attempts exceeds six
times, the pending message is sent to the Dead Letter JMS
Queue.
