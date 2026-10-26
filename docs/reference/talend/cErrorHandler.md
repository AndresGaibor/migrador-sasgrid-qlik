<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler · versión 8.0 -->
# cErrorHandler

Last updated: 9/30/2026

Processes errors in the message routing.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cErrorHandler Standard properties

These properties are used to configure cErrorHandler running in the Standard Job framework.

The Standard
cErrorHandler component belongs to the Exception Handling family.

## Basic settings

| Properties | Description |
| --- | --- |
| Default Handler | * This error handler does not support a dead letter queue and will   return exceptions back to the caller. * Set Maximum Redeliveries: select   this check box to set the number of redeliveries in the Maximum Redeliveries (int) field. * Set Redelivery Delay: select this   check box to set the initial redelivery delay (in milliseconds) in   the Redelivery Delay (long)   field. * Set Retry Attempted Log Level:   select this check box to select the log level in the Level list for log messages when retries   are attempted. * Asynchronized Delayed Redelivery:   select this check box to allow asynchronous delayed   redelivery. * More Configurations by Code:   select this check box to enter codes in the Code box for further configuration. |
| Dead Letter | * This handler supports attempting to redeliver the message exchange   a number of times before sending it to a dead letter   endpoint. * Dead Letter Uri: select this   check box to define the endpoint of the dead letter queue.  Other parameters share the same meaning as those of the default   handler. |
| Logging Handler | * This handler logs the exceptions. * Set Logger Name: select this   check box to give a name to the logger in the Name field. * Set Log Level: select this check   box to decide the log level from the Level list. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cErrorHandler is used separately or as a middle or end component in a Route. If this component is used separately, it will handle errors in all sub-routes. If this component is used in the middle or end of a sub-route, it will only handle exceptions that happen in the components of this sub-route, either before or after the cErrorHandler. |
| Limitation | n/a |

**Related concepts**  

* [Logging the exception thrown during a client/server talk](cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-logging-exception-thrown-during-client-server-talk)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-logging-exception-thrown-during-client-server-talk -->
# Logging the exception thrown during a client/server talk

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a Jetty server is started before a client browser requests access to it.
Then an exception is thrown at the server side and logged by cErrorHandler.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-viewing-code-and-executing-route)

**Related reference**  

* [cErrorHandler](cerrorhandler "Processes errors in the message routing.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click cErrorHandler to open its Basic settings view in the Component tab.
2. Select Logging Handler to log the exceptions that are
   thrown.
3. Double-click cMessagingEndpoint to open its Basic settings view in the Component tab.
4. In the Uri field, enter
   `jetty:http://localhost:8889/service` to specify the Jetty
   server.
5. Click Advanced settings for
   further setup.
6. In the Dependencies table, click
   the [+] button to add a line and select
   jetty from the Camel
   component list.
7. Double-click cProcessor to
   open its Basic settings view in the
   Component tab.
8. In the Code box, enter
   `throw new Exception("server side error")` to throw an
   exception.
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the
   workspace: cMessagingEndpoint, cErrorHandler and cProcessor, labeled as Jetty\_Server, Error\_Handler
   and Throw\_Exception respectively.
2. Link cMessagingEndpoint and cProcessor using a Row >
   Route connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cerrorhandler-cprocessor-cmessagingendpoint-cmessagingendpoint-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the design workspace
   to check the generated code.

   As shown above, the route starts from the endpoint Jetty\_Server
   and throws the exception of server side error via
   cProcessor\_1.
2. Press F6 to execute the Route.

   The Jetty server has started.
3. Launch an Internet browser and enter
   http://localhost:8889/service (the Jetty server URI
   configured above) in the address bar to access the server.

   As shown above, the request failed due to the server error.
4. Go to Talend Studio and
   check the results in the Run tab.

   As shown above, cErrorHandler
   has logged the exception at the level of *ERROR*.
