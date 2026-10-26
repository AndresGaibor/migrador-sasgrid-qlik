<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler · versión 8.0 -->
# cThrottler

Last updated: 9/30/2026

Limits the number of messages flowing to a specific endpoint in order to prevent
it from getting overloaded.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cThrottler Standard properties

These properties are used to configure cThrottler running in the Standard Job framework.

The Standard
cThrottler component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Request per period | The number of messages allowed to pass cThrottler within the defined time period. |
| Set time period | Select this check box to set the value of the time period (in milliseconds) and enable throttling. |
| Use asynchronous delaying | If this check box is selected, any messages that are delayed will be routed asynchronously using a scheduled thread pool. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Being a middle component, cThrottler allows you to limit the number of messages flowing to a specific endpoint in order to prevent it from getting overloaded. |
| Connections | * throttler: Select this link to route   the throttled messages to the next endpoint. * Route: Select this link to route all the messages   from the sender to the next endpoint. |
| Limitation | n/a |

**Related concepts**  

* [Throttling the message flow](cthrottler-cfile-cprocessor-cprocessor-throttling-message-flow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler-cfile-cprocessor-cprocessor-throttling-message-flow -->
# Throttling the message flow

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cThrottler component is used to
reduce the number of messages flowing out within a time period.

To build the Route, do the following.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler-cfile-cprocessor-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler-cfile-cprocessor-cprocessor-configuring-components)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler-cfile-cprocessor-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cThrottler](cthrottler "Limits the number of messages flowing to a specific endpoint in order to prevent it from getting overloaded.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler-cfile-cprocessor-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click Read\_Output to open its
   Basic settings view in the Component tab.
2. In the Path field, type in the
   path to the source message, for example, `"E:/data/output"`.
   Keep the default settings for other fields.
3. Double-click cThrottler to open its
   Basic settings view in the Component tab.
4. In the Request per period
   field, type in the number of messages allowed to pass the throttler per period, for
   example, `1`.

   In the Set time period field,
   type in the value of the period, for example, `8000`.
5. Double-click Print\_File\_Name to open its
   Basic settings view in the Component tab.
6. In the Code box, enter the code below to
   get the name of the message that passes the throttler.

   ```
   System.out.println("The file that passes throttler is: "+exchange.getIn().getHeader("CamelFileName"));
   ```
7. Double-click Print\_File\_Content to open
   its Basic settings view in the Component tab.
8. In the Code box, enter the code below to
   get the content of the message that passes the throttler.

   ```
   System.out.println("The content of " +exchange.getIn().getHeader("CamelFileName")+ " is: "
   +exchange.getIn().getBody(String.class));
   ```
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler-cfile-cprocessor-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drag and drop the components from the Palette onto the workspace: cThrottler, cFile and two
   cProcessor. Change the label of the
   cFile component to Read\_Output. Change the labels of the two
   cProcessor components to Print\_File\_Name and Print\_File\_Content.
2. Link Read\_Output to cThrottler using a Row >
   Route connection.
3. Link cThrottler to Print\_File\_Name using a Row
   > Throttler connection, and to Print\_File\_Content using a Row > Route
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-throttler/cthrottler-cfile-cprocessor-cprocessor-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the messages from Read\_Output go through
   throttling at cThrottler\_1, with only (1) message
   allowed to leave the throttler within each timePeriodMillis(8000).
   Meanwhile, the filename and the content of the throttled message are printed out
   via the two processors.
2. Press F6 to execute the Route.

   As shown below, *File\_A.txt* was delivered
   within the first time period while in the second period, *File\_B.txt* was delivered as well.
