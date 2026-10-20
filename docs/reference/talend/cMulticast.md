<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast · versión 8.0 -->
# cMulticast

Last updated: 9/30/2026

Routes messages to a number of endpoints at one go and process them in different
ways.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cMulticast Standard properties

These properties are used to configure cMulticast running in the Standard Job framework.

The Standard
cMulticast component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| URIS | Add as many lines as needed in the URIs table to define the endpoints to route the message(s) to. |
| Use ParallelProcessing | Select this check box to multicast the message(s) to the specified endpoints simultaneously. |
| set timeout | Select this check box and set a timeout in the Timeout field, in milliseconds. If cMulticast fails to send and process all the messages within the set timeframe, it breaks out and continues.  Note that this check box appears only when the Use ParallelProcessing check box is selected. |
| Use Aggregation Strategy | Select this check box to refer to a predefined Java bean or select a predefined aggregation strategy for assembling the messages from the message source into a single outgoing message.  * UseOriginalAggregationStrategy: Use the original   exchange. * UseLatestAggregationStrategy: Use the latest   exchange. * GroupedMessageAggregationStrategy: Aggregate all   messages into a single combined exchange holding all the aggregated   messages in a list of messages as the message body. * GroupedExchangeAggregationStrategy: Aggregate all   exchanges into a single combined exchange holding all the aggregated   exchanges in a list of exchanges as the message body. * GroupedBodyAggregationStrategy: Aggregate body of   input messages into a single combined exchange holding all the aggregated   bodies in a list of objects as the message body.   Information noteNote: The predefined aggregation strategies are available only if you have installed the R2024-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  By default, the last message acts as the outgoing message. |
| Stop On Exception | Select this check box to stop the processing immediately when an exception occurred. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cMulticast can be used as a middle or end component in a Route. |
| Connections | * Route: Select this link to route the   message(s) from the sender to the next endpoint. * EndBlock: Select this link to route the   message(s) from the end block of the Route to the next endpoint. |
| Limitation | n/a |

**Related concepts**  

* [Route a message to multiple endpoints and set a new body for each](cmulticast-cprocessor-cfile-csetbody-route-message-to-multiple-endpoints-and-set-new-body-for-each)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast-cprocessor-cfile-csetbody-route-message-to-multiple-endpoints-and-set-new-body-for-each -->
# Route a message to multiple endpoints and set a new body for each

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cMulticast component is used to
route a message to two endpoints. The source message and the message on each endpoint is
then set a new body. The cProcessor component is used
to monitor the messages.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast-cprocessor-cfile-csetbody-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast-cprocessor-cfile-csetbody-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast-cprocessor-cfile-csetbody-viewing-code-and-executing-route)

**Related reference**  

* [cMulticast](cmulticast "Routes messages to a number of endpoints at one go and process them in different ways.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast-cprocessor-cfile-csetbody-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component
   labeled `Source_file` to open its Basic
   settings view in the Component
   tab.
2. In the Path field, fill in or
   browse to the path where the source file Hello.txt is located.
   Keep the default settings for other fields.
3. Double-click the cMulticast
   component labeled `Multicast` to open its Basic settings view in the Component tab.
4. In the URIS table, click the
   plus button to add two lines and specify the URIs of the endpoints where the message
   will be sent, `"direct:a"` and `"direct:b"`
   in this use case.
5. Double-click the cMessagingEndpoint component labeled `direct_a`to open its Basic settings view in
   the Component tab.
6. In the URI field, enter the
   endpoint URI, `"direct:a"` in this use case. 

   Repeat this step to set the endpoint URI for
   `direct_b` as `"direct:b"`.
7. Double-click the cProcessor
   component labeled `Monitor_source` to open its Basic settings view in the Component tab.
8. In the Code box, enter the code below to
   print the source message in the console.

   ```
   System.out.println("The source message is: " + exchange.getIn().getBody(String.class));
   ```

   Repeat this step to customize the code of Monitor\_endblock, Monitor\_direct\_a, and Monitor\_direct\_b as shown below to print the message of each
   endpoint.

   Monitor\_endblock:

   ```
   System.out.println("The endblock message is: " + exchange.getIn().getBody(String.class));
   ```

   Monitor\_direct\_a:

   ```
   System.out.println("direct a just downloaded: "+exchange.getIn().getBody(String.class));
   ```

   Monitor\_direct\_b:

   ```
   System.out.println("direct b just downloaded: "+exchange.getIn().getBody(String.class));
   ```
9. Double-click the cSetBody
   component labeled `Set_new_body` to open its Basic settings view in the Component tab.
10. Select SIMPLE in the Language list.

    In the Expression field, enter
    `"New message"` as the new message body.

    Repeat this step to set the message body for
    `direct:a` and `direct:b` as
    `"message A"` and `"message B"`
    respectively.
11. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast-cprocessor-cfile-csetbody-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, expand the Connectivity folder. Drag and drop a cFile and two cMessagingEndpoint components onto the design
   workspace.
2. From the Routing folder, drag and drop a
   cMulticast component onto the design
   workspace.
3. From the Custom folder, drag and drop four cProcessor components onto the design
   workspace.
4. From the Core folder, drag and drop three cSetBody components onto the design
   workspace.
5. Label the components as shown above to better identify their roles in the
   Route.
6. Right-click the cMulticast component,
   select Row > EndBlock in the context menu and click the cProcessor component labeled Monitor\_endblock.
7. Right-click the cFile component, select
   Row > Route in the context menu and click the cMulticast component. Repeat this step to link
   the rest components in the Route as shown above using the Row > Route
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-multicast/cmulticast-cprocessor-cfile-csetbody-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   In the partially shown code, the source message is routed from
   "Source\_file\_cFile\_1"
   .to
   direct:a and direct:b
   via "cMulticast\_1". The message is then processed by
   "cProcessor\_1" and given the message body "New message" by "cSetBody\_3". The .end block of the Route
   is processed by "cProcessor\_2". The message from
   "direct\_a\_cMessagingEndpoint\_1" is set the message
   body "message A" by "cSetBody\_1" and processed by "cProcessor\_3". The message from direct:b
   is processed similarly.
2. Click the Run view to display it
   and click the Run button to launch the execution
   of your Route. You can also press F6 to execute
   it.

   RESULT: The source file message is Hello world!.
   The message routed to direct:a and direct:b is set
   the message body message A and message B
   respectively. The end block message of this Route is New message
   that is set by the component labeled Set\_new\_body.
