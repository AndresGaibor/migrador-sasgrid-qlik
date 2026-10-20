<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept · versión 8.0 -->
# cIntercept

Last updated: 9/30/2026

Intercepts each message sub-route and redirects it in another sub-route without
modifying the original one. When this detour is complete, message routing to the originally
intended target endpoints continues. This can be useful at testing time to simulate error
handling.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cIntercept Standard properties

These properties are used to configure cIntercept running in the Standard Job framework.

The Standard
cIntercept component belongs to the Exception Handling family.

## Basic settings

| Properties | Description |
| --- | --- |
| Intercept type | Select the intercept type from:  * Any: Intercepts every processing step as they   happen during routing. * From: Intercepts only the incoming step. * To: Intercepts only when an exchange is about to   be sent to the given endpoint. |
| Component filter | This option is available when the From or To intercept type is selected. Enter the component name if you want to only intercept specific components. The component filter supports endpoint pattern matching by the following rules in the given order:  1. match by exact URI name 2. match by wildcard 3. match by regular expression |
| Send to original endpoint | This option is available when the To intercept type is selected. When enabled, the message will be sent to the original endpoint. If this checkbox is cleared, the message will not be sent to the original intended destination. |
| Send to additional endpoint | This endpoint is available when the To intercept type is selected. If you want to send the message to additional endpoint, select this checkbox and specify the additional endpoint in the After URI field. When this option is enabled, the message will be sent to the original endpoint as well even if the Send to original endpoint option is disabled. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cIntercept is a start component of a sub-route. |
| Connections | * Row / Route: Select the   Route link to intercept all the messages of all the   sub-routes listened to by the cIntercept. * Trigger / When: Select the   When link to filter the messages to intercept and   click the Component view.  In the Type list, select the type of language you will   use to declare your condition.  In the Condition field, type in the condition that will   be used to filter the messages.  All the messages that do not match this condition are dropped by default or can   be retrieved with the Otherwise link to a different   channel. |
| Limitation | To keep the original sub-routes untouched, cIntercept only be used in a separate sub-route. |

**Related concepts**  

* [Intercepting subRoutes from given component](cintercept-cfile-cprocessor-cstop-intercepting-subroutes-from-given-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept-cfile-cprocessor-cstop-intercepting-subroutes-from-given-component -->
# Intercepting subRoutes from given component

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, message from given component is intercepted and routed along
a new sub-route, which is then terminated before the original sub-route continues.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept-cfile-cprocessor-cstop-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept-cfile-cprocessor-cstop-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept-cfile-cprocessor-cstop-viewing-code-and-executing-route)

**Related reference**  

* [cIntercept](cintercept "Intercepts each message sub-route and redirects it in another sub-route without modifying the original one. When this detour is complete, message routing to the originally intended target endpoints continues. This can be useful at testing time to simulate error handling.")
* [cLog](clog "Logs message exchanges in a Route.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cStop](/talend/en-US/mediation-components/8.0/mediation-orchestration/cstop)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept-cfile-cprocessor-cstop-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## About this task

In this scenario, the cStop component
stops the sub-route on which it is dropped before it completes and does not have
properties to set.

## Procedure

1. Double-click the cIntercept component to display its
   Basic settings view in the Component
   tab.
2. Select the From intercept type and enter
   `"file*"` in the Component filter
   field to intercept messages from the component with the name matching the
   file\* pattern.
3. Double-click the cProcessor
   component, to display its Basic settings view in
   the Component tab.
4. Customize the code in the Code area to display
   the CamelFileName header of the intercepted message on the
   console:

   ```
   System.out.println("Message intercepted: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```
5. Double-click the first cTimer component to display its
   Basic settings view in the Component
   tab.
6. Enter `1` in the Repeat field to
   trigger one message exchange.
7. Double-click the first cSetBody component to display its
   Basic settings view in the Component
   tab.
8. Select Constant from the Language
   list and enter `"Hello World!"` in the
   Expression field as the message body.
9. Double-click the first cFile
   component to display its Basic settings view in
   the Component tab.
10. Specify the path to the source file in the Path field and enter the file name in the
    fileName field.
11. Double-click the second cFile
    component to display its Basic settings view in
    the Component tab.
12. Specify the path to write the file to in the Path field and enter the file name in the
    fileName field.
13. Keep the default settings of the cLog components to log the
    message exchanges.
14. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept-cfile-cprocessor-cstop-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cIntercept, a
   cProcessor, a cTimer, a
   cSetBody, two cFile, and two
   cLog components onto the design workspace.
2. Link the components with the Row
   > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/cintercept-cfile-cprocessor-cstop-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in this piece of code, cIntercept
   intercepts messages from "file\*". cStop
   terminates message routing before the message is routed from
   cFile to the next endpoint.
2. Click the Run view and click the
   Run button to launch the execution of your
   Route. You can also press F6 to execute
   it.

   The file sent from cFile is caught by
   cIntercept and monitored by
   cProcessor. The original sub-route is terminated before the
   message is sent to the next endpoint.
