<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer · versión 8.0 -->
# cLoadBalancer

Last updated: 9/30/2026

Distributes the messages it received to multiple endpoints according to the load
balancing policy.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cLoadBalancer Standard properties

These properties are used to configure cLoadBalancer running in the Standard Job framework.

The Standard
cLoadBalancer component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Strategy | Select between Random, Round Robin, Sticky, Topic, Failover, and Custom. Each method is described below. |
| Random | The receiving endpoint is chosen randomly at each exchange. |
| Round Robin | Messages are distributed according to the round robin method which distributes the load evenly. |
| Sticky | * Language: Select the language of the   expression to use in the Expression field   to distribute the messages from None,   Bean, Constant, CorrelationID,   EL, Groovy, Header, JoSQL, JSonPath, JXPath,   MVEL, OGNL, PHP, Property, Python, Ruby, Simple, SpEL,   SQL, XPath, and XQuery.  For more information about how to use the languages to create an expression, see   the site <http://camel.apache.org/languages.html>. * Expression: Type in the   expression that will be used to calculate a correlation key that will determine   the endpoint to choose. |
| Topic | Select this option to send all the messages to all the endpoints. |
| Failover | * Basic mode: By default, the   failover load balancing always sends the messages to the first endpoint. If the   first endpoint fails, the messages are sent to subsequent endpoints. * Specify exceptions: Specify   the exceptions to which the failover should react to in the Exception table. * Use with Round robin: Select   this option to use failover with advanced options.  From the Maximum failover   attempt list, select the number of attempt to be   proceed before giving up the transfer:  -Attempt forever: always attempts to   transfer the messages and always try to failover.  -Never failover: gives up   immediately the transfer of messages and never try to   failover.  -A number of   attempts: attempts *n* number of   time to transfer messages, specify that number in the Number of attempts   field.  Inherit error   handler: Select *true* if you want   Camel error handler to be used. If you select   *false*, the load balancer will immediately   failover when an exception is thrown.  Use Round robin: Select   *true* if you want to combine failover with   round robin. Failover load balancing with round robin mode   distributes the load evenly between the services, and it provides   automatic failover. |
| Custom | Load balancer: Type in the name of your custom load balancer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cLoadBalancer is used as a middle component in a Route. |
| Connections | * Load Balance: Select this link to route   messages to the next endpoint according to the selected load-balancing strategy. * Route: Select this link to route all the   messages from the sender to the next endpoint. |
| Limitation | n/a |

**Related concepts**  

* [Distributing messages to receiver endpoints based on round robin](cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-distributing-messages-to-receiver-endpoints-based-on-round-robin)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-distributing-messages-to-receiver-endpoints-based-on-round-robin -->
# Distributing messages to receiver endpoints based on round robin

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cLoadBalancer component is used
to distribute four messages evenly to two receiving endpoints in accordance with the
round robin load balancing method.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-configuring-components-and-connections)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cLoadBalancer](cloadbalancer "Distributes the messages it received to multiple endpoints according to the load balancing policy.")

**Related information**  

* [cJavaDSLProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cjavadslprocessor)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component to open
   its Basic Settings view in the Component tab.
2. In the Path field, specify the file path
   to message source.
3. From the Encoding list, select the
   encoding type of your message files. Leave the other parameters as they
   are.
4. Double-click the cLoadBalancer
   component to open its Basic Settings view in the
   Component tab, and select the load balancing
   method you want to use from the Strategy list.
   In this scenario, the default Round robin method
   is used.
5. Double-click the cJavaDSLProcessor component labeled
   `To_Receiver_A` to open its Basic
   Settings view in the Component
   tab, and enter URI of the first receiver between the double quotation marks in the
   Code area, `direct:a` in
   this example.

   Repeat this step to define the URI of the other receiver,
   `direct:b`, in the cJavaDSLProcessor component labeled
   `To_Receiver_B`.
6. Double-click the cMessagingEndpoint component labeled
   `Receiver_A` to open its Basic
   Settings view in the Component
   tab, and enter URI of the first receiver between the double quotation marks in the
   URI field, `direct:a` in
   this example.

   Repeat this step to define the URI of the other receiver,
   `direct:b`, in the cMessagingEndpoint component labeled
   `Receiver_B`.
7. Double-click the cProcessor
   component labeled `Monitor_A` to open its Basic Settings view in the Component tab, and customize the code in the Code area to display the file names of the messages routed to
   `Receiver_A` on the console:

   ```
   System.out.println("Message on Receiver_A: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```

   Repeat this step to customize the code in the cProcessor component
   labeled Monitor\_B to display the file names of the messages routed to
   Receiver\_B on the console.
8. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

This scenario requires one cFile component as the
message sender, one cLoadBalancer component to
distribute the messages to two different receivers in a load balancing manner, two
cJavaDSLProcessor components to define the URIs
of the receivers, two cMessagingEndpoint components
to retrieve the messages routed to the two receivers, and two cProcessor components to display the effect of round robin load
balancing.

## Procedure

1. From the Connectivity folder of the
   Palette, drop one cFile component and two cMessagingEndpoint components onto the workspace, and label
   them according to their roles in the Route: *Sender*, *Receiver\_A*, and
   *Receiver\_B* respectively.
2. From the Routing folder, drop a cLoadBalancer component onto the design
   workspace, and label it *Load\_balancer*.
3. From the Core folder, drop two cJavaDSLProcessor components onto the design
   workspace, and label them according to their roles in the Route: *To\_Receiver\_A* and *To\_Receiver\_B* respectively.
4. From the Custom folder, drop two
   cProcessor components onto the design
   workspace, and label them according to their roles in the Route: *Monitor\_A*, and *Monitor\_B* respectively.
5. Link the cFile component to the cLoadBalancer component using a Row > Route
   connection.
6. Link cLoadBalancer to each of the two
   cJavaDSLProcessor components using a
   Row > Load
   Balance connection.
7. Link each of the two cMessagingEndpoint
   components to the corresponding cProcessor
   component using a Row > Route connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-load-balancer/cloadbalancer-cjavadslprocessor-cmessagingendpoint-cprocessor-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code: 

   As shown above, while messages are routed from the source endpoint
   .to the destination endpoints, routing load balancing is
   implemented according to the .roundRobin() method by
   cLoadBalancer\_1.
2. Press F6 to run your Route.

   RESULT: Of the four messages from the sender, two are routed to *Receiver\_A* and two are routed to *Receiver\_B* in a round robin manner.
