<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm · versión 8.0 -->
# cDirectVM

Last updated: 9/30/2026

Produces and consumes messages synchronously in different threads within a
single CamelContext and across CamelContexts in the same JVM. You can use this mechanism
to communicate across Web applications.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cDirectVM Standard properties

These properties are used to configure cDirectVM running in the Standard Job framework.

The Standard
cDirectVM component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| When using as a start component in a Route: |  |
| Endpoint Name | Type in any string that uniquely identifies the endpoint. |
| When using as a middle or end component in a Route: |  |
| Select From Existing(s) | Click this radio button to select an existing consumer. Click [...] beside the Consumer field to show the existing consumer(s) and select the one to consume the message. |
| Input Endpoint Name | Click this radio button to enter the name of the consumer in the Endpoint Name field. |
| Block if Consumer is not active | Select this check box to let the producer block if the consumer is not active in the Timeout period. |
| Timeout | This option appears when the block is enabled. Specify the time in milliseconds before the producer stops waiting for the consumer to become active. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cDirectVM is used as a start, middle, or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Direct and synchronous messaging within the same JVM](cdirectvm-ctimer-csetheader-cprocessor-direct-and-synchronous-messaging-within-same-jvm)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-direct-and-synchronous-messaging-within-same-jvm -->
# Direct and synchronous messaging within the same JVM

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a message exchange is triggered in one sub-route and synchronously
consumed in another sub-Route using the Direct-VM mechanism. At the consumer end, the
message content is processed and displayed on the console.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-configuring-components)
* [Executing the Route](/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-executing-route)

**Related reference**  

* [cDirectVM](cdirectvm "Produces and consumes messages synchronously in different threads within a single CamelContext and across CamelContexts in the same JVM. You can use this mechanism to communicate across Web applications.")

**Related information**  

* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetHeader](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Configuring the first sub-route](/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-configuring-first-sub-route)
* [Configuring the second sub-route](/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-configuring-second-sub-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drag and drop the
   following components onto the design workspace: a cTimer, a cSetHeader, a
   cSetBody, two cDirectVM, and a cProcessor.
2. Link the cTimer, the cSetHeader, the cSetBody and the first cDirectVM components using Row > Route connections to
   form a sub-route.
3. Link the other cDirectVM component to the
   cProcessor component using a Row > Route
   connection to form another sub-route.
4. Label the components to better identify their roles in the Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-executing-route -->
# Executing the Route

Last updated: 9/30/2026

Click the Run view and click the Run button to launch your Route. You can also press
F6 to execute it.

RESULT: The message generated in the first sub-route is consumed synchronously in
the consumer endpoint and displayed on the console after processing. The message
exchange is triggered once as configured.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-configuring-first-sub-route -->
# Configuring the first sub-route

Last updated: 9/30/2026

## Procedure

1. Double-click the cTimer component
   (labeled *Starter* in this example) to
   display its Basic settings view on the
   Component tab.
2. In the Repeat field, enter *1* so that the message exchange is triggered
   only once. Leave the other settings as they are.
3. Double-click the cSetHeader component (labeled
   *Set\_message\_headers* in this example)
   to display its Basic settings view on the
   Component tab.
4. Click the [+] button to add two headers
   in the Headers table, and then give each
   header a name and a value.

   In this example, we name the headers *Name* and *Company*
   respectively, and enter *Bill* and
   *Talend* as their values.
5. Double-click the cSetBody component
   (labeled *Set\_message\_body* in this
   example) to display its Basic settings view
   on the Component tab.
6. Select SIMPLE from the Language list as we will trigger a simple text
   message exchange in this example.
7. In the Expression field, enter *Hi there* in double quotation marks as the
   content of the message body.
8. Double-click the first cDirectVM
   component (labeled *D-VM\_producer* in this
   example) to display its Basic settings view
   on the Component tab.
9. Select an existing consumer endpoint, or specify the name of the consumer
   endpoint. 

   In this example, we will name the consumer endpoint *dvm*, so select the Input Endpoint
   Name option, and enter the name of the consumer endpoint
   *dvm* in the Endpoint Name field.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-direct/cdirectvm-ctimer-csetheader-cprocessor-configuring-second-sub-route -->
# Configuring the second sub-route

Last updated: 9/30/2026

## Procedure

1. Double-click the second cDirectVM component (labeled `D-VM_consumer` in
   this example) to display its Basic settings view
   on the Component tab.
2. In the Endpoint Name field,
   enter `dvm` in double quotation marks to name the
   endpoint.
3. Double-click the cProcessor
   (labeled `Show_message` in this example) component to display
   its Basic settings view.
4. In the Code area, enter the following
   code to display the content of the message headers and the message
   body:

   ```
   exchange.getOut().setHeader("header1",exchange.getIn().getHeader("Name"));
   exchange.getOut().setHeader("header2",exchange.getIn().getHeader("Company"));
   exchange.getOut().setBody(exchange.getIn().getBody(String.class));
   System.out.println();
   System.out.println("Message for "+exchange.getOut().getHeader("header1")
   +" of "+exchange.getOut().getHeader("header2")+":");
   System.out.println(exchange.getOut().getBody(String.class));
   ```
