<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-seda/cseda · versión 8.0 -->
# cSEDA

Last updated: 9/30/2026

Produces and consumes messages asynchronously in different threads within a single
CamelContext.

cSEDA provides asynchronous SEDA
behavior, so that messages are exchanged on a BlockingQueue and
consumers are invoked in a separate thread from the producer within
a single CamelContext.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cSEDA Standard properties

These properties are used to configure cSEDA running in the Standard Job framework.

The Standard
cSEDA component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| When using as a start component in a Route: |  |
| Name | Type in any string that uniquely identifies the endpoint. |
| Specify maximum capacity size | Select this check box to set the maximum number of messages that the SEDA queue can hold. Specify the number in the Size field. |
| Concurrent consumers | Specify the number of concurrent threads processing exchanges. |
| Wait for task to complete | Specify whether the caller should wait for the asynchronous task to complete or not before continuing. Select from Always, Never or IfReplyExpected. The default option is IfReplyExpected which means the caller will only wait if the message is Request-Reply based. For more information about this option, see the site <http://camel.apache.org/async.html>. |
| Timeout | Specify the time in milliseconds before a SEDA producer will stop waiting for an asynchronous task to complete. You can disable this option by using 0 or a negative value. |
| Use multiple consumers | Specifies whether multiple consumers are allowed. If enabled, you can use cSEDA for Publish-Subscribe messaging, which means you can send a message to the SEDA queue and have each consumer receive a copy of the message. When enabled, this option should be specified on every consumer endpoint. |
| Limit concurrent consumers | Whether to limit the number of concurrent consumers to the maximum of 500. By default, an exception will be thrown if a SEDA endpoint is configured with a greater number. |
| Block when full | Whether a thread that sends messages to a full SEDA queue will block until the queue's capacity is no longer exhausted. By default, an exception will be thrown stating that the queue is full. By enabling this option, the calling thread will block instead and wait until the message can be accepted. |
| Poll timeout | Specify the timeout in milliseconds used when polling. When a timeout occurs, the consumer can check whether it is allowed to continue running. Setting a low value allows the consumer to react more quickly upon shutdown. |
| When using as a middle or end component in a Route: |  |
| Use Exist cSEDA | Click [...] and select the corresponding consumer in the dialog box. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Arguments | This option is available only when cSEDA is used as a start component in the Route. Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/seda.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSEDA is used as a start, middle, or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Using cSEDA, cVM and cDirect to produce and consume messages separately](cseda-cvm-ctimer-clog-using-cseda-cvm-and-cdirect-to-produce-and-consume-messages-separately)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-using-cseda-cvm-and-cdirect-to-produce-and-consume-messages-separately -->
# Using cSEDA, cVM and cDirect to produce and consume messages separately

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, we will use a cTimer component to
trigger a message exchange. The message is routed to a cSEDA, a cVM and a cDirect sequentially with a message body set for each of
them, which is then consumed in another thread.

We will create a Route Resource to define the repeat count of the message exchange
(the number of times the message should be sent), which will be used by the cTimer component.

### In this section

* [Creating a Route Resource and calling it in the Route](/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-creating-route-resource-and-calling-it-in-route)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-viewing-code-and-executing-route)

**Related reference**  

* [cSEDA](cseda "Produces and consumes messages asynchronously in different threads within a single CamelContext.")
* [cVM](cvm "Produces and consumes messages asynchronously in different threads across CamelContext. You can use this mechanism to communicate across Web applications.")

**Related information**  

* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cDirect](/talend/en-US/mediation-components/8.0/mediation-direct/cdirect)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click Starter in the design workspace
   to display its Basic settings view in the
   Component tab.
2. In the Repeat field, enter
   `"{{repeat.count}}"` that is defined in the Route
   resource.
3. Double-click Set\_body\_SEDA in the design
   workspace to display its Basic settings view in
   the Component tab.
4. Select SIMPLE in the Language list. 

   In Expression field, enter
   the `"to cSEDA"` as the message body.

   Repeat this step to set the message body in
   Set\_body\_VM and Set\_body\_Direct as
   `"to cVM"` and `"to cDirect"`
   respectively.

   Set\_body\_VM:

   Set\_body\_Direct:
5. Double-click SEDA\_producer to display its
   Basic settings view in the Component tab.
6. Click [...] and select
   SEDA\_consumer in the Select a
   Node: wizard, which will consume the message that is sent to
   SEDA\_producer.

   Repeat this step to select the node
   VM\_consumer for VM\_producer.

   Select the node Direct\_consumer for
   VM\_producer.
7. Double-click SEDA\_consumer to display its
   Basic settings view in the Component tab.
8. In the Name field, type in
   `"seda"` to identify this endpoint. Keep the default settings
   of the other options.

   Repeat this step to give the name `"vm"` to
   VM\_consumer.

   Give the name `"direct"` to
   Direct\_consumer.
9. Double-click Monitor\_SEDA to display its
   Basic settings view in the Component tab.
10. Select INFO in the Level list and select Specify
    output log message. In the Message field, enter `"log cSEDA:${body}"` to
    print the message body in the console.

    Repeat this step to specify the output message for
    Monitor\_VM and Monitor\_Direct as
    `"log cVM:${body}"` and `"log
    cDirect:${body}"` respectively.
11. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-creating-route-resource-and-calling-it-in-route -->
# Creating a Route Resource and calling it in the Route

Last updated: 9/30/2026

## Procedure

1. From the repository tree view, right-click the Resources node and select Create
   Resource from the context menu.
2. The New Route Resource wizard
   opens. In the Name field, type in a
   name for the Resource, for example, *SetRepeatCount*.
   Click Finish to close the
   wizard.
3. Enter repeat.count=2 in the design workspace to set the
   repeat count.
4. Press Ctrl+S to save your Route
   Resource.
5. Right-click the Route from the repository tree view and select
   Manage Route Resources from the
   context menu.

   The Manage Route Resources wizard
   is opened.
6. Click Add and select
   *SetRepeatCount* from the Resources tree view in
   the dialog. Click OK.

   The *SetRepeatCount* Route Resource is added in the
   table.
7. Click OK to close the wizard.

   For more information about creating and using Route Resources, see
   [Using Route Resources](/talend/r/en-US/8.0/studio-user-guide/using-route-resources).
8. Click the Spring tab on the lower
   half of the design workspace of the Route.
9. Enter the following code in this view to call the Route Resource you
   just created.

   ```
   <bean id="properties" class="org.apache.camel.component.properties.PropertiesComponent">   
       <property name="location" value="classpath:SetRepeatCount.properties"/>  
   </bean>
   ```

   For more information about using Spring configuration in a Route,
   see [Using Spring configuration](/talend/r/en-US/8.0/studio-user-guide/using-spring-configuration).


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cTimer, two cSEDA, two cVM, two
   cDirect, three cSetbody, and three cLog
   components onto the design workspace.
2. Link the components using the Row >
   Route connection as shown above.
3. Label the components to better identify their roles in the Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-seda/cseda-cvm-ctimer-clog-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to look at the generated code.

   As shown in the code, a message Route is built from
   "Starter\_cTimer\_1", set the message body "to cSEDA" by "cSetBody\_1", and sent to cSEDA\_2, which is
   mapped to "SEDA\_consumer\_cSEDA\_1". The message is
   then sent to cVM\_2, cDirect\_2 sequentially which is mapped to its corresponding consumer
   with a new message body. On the consumer side, the message body from each consumer is logged by the corresponding
   monitor.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: The message that is sent to
   SEDA\_producer, VM\_producer, and
   Direct\_producer is consumed by
   SEDA\_consumer, VM\_consumer, and
   Direct\_consumer respectively. The message exchange is
   triggered twice as set in the Route Resource
   SetRepeatCount.
