<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters · versión 8.0 -->
# cPipesAndFilters

Last updated: 9/30/2026

Splits message routing into a series of independent processing stages.

cPipesAndFilters divides message
processing into a sequence of independent endpoint instances, which can then be chained
together.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cPipesAndFilters Standard properties

These properties are used to configure cPipesAndFilters running in the Standard Job framework.

The Standard
cPipesAndFilters component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| URI list | Click the plus button to add new lines for URIs that identify endpoints. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cPipesAndFilters is usually used in the middle of a Route. |
| Limitation | n/a |

**Related concepts**  

* [Using cPipesAndFilters to process the task in sequence](cpipesandfilters-cfile-cmessagingendpoint-cprocessor-using-cpipesandfilters-to-process-task-in-sequence)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters-cfile-cmessagingendpoint-cprocessor-using-cpipesandfilters-to-process-task-in-sequence -->
# Using cPipesAndFilters to process the task in sequence

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cPipesAndFilters component is
used so that messages sent from the sender endpoint undergo stage A and stage B. Upon
completion of both stages, the messages are routed to a file system, which is the
receiver endpoint for the messages.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters-cfile-cmessagingendpoint-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters-cfile-cmessagingendpoint-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters-cfile-cmessagingendpoint-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cPipesAndFilters](cpipesandfilters "Splits message routing into a series of independent processing stages.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters-cfile-cmessagingendpoint-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component
   labeled `Sender` to open its Basic
   settings view in the Component
   tab.
2. In the Path field, fill in or browse to
   the path to the folder that holds the source files.
3. From the Encoding list, select the
   encoding type of your source files. Leave the other parameters as they
   are.
4. Repeat these steps to define the path to the output files and the
   output encoding type in the Basic settings view
   of the cFile component labeled
   `Receiver`.
5. Double-click the cPipesAndFilters
   component to open its Basic settings view
   in the Component tab.
6. Click the plus button to add two lines to the URI list table, and fill the first line with
   `"direct:a"` and the second line with
   `"direct:b"` to define the URIs of stage A and stage B that
   the messages will undergo.
7. Double-click the cMessagingEndpoint component labeled `Stage_A`
   to configure the component in its Basic settings
   view and define the URI of stage A.

   Repeat this step to define the URI of stage B in the Basic settings view of the cMessagingEndpoint component labeled
   `Stage_B`.
8. Double-click the cProcessor
   component labeled `Monitor_Receiver` to open its Basic settings view, and customize the code in the
   Code area to display the file names of the
   messages received on Receiver, as follows:

   ```
   System.out.println("Message sent to Receiver: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```

   Repeat this step to customize the code in the other two cProcessor components to display the file names of the
   messages received on stage A and stage B respectively:

   ```
   System.out.println("Message sent to stage A: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```

   ```
   System.out.println("Message sent to stage B: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters-cfile-cmessagingendpoint-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Connectivity folder of the Palette, drop two cFile components onto the design workspace, one as the
   message sender and the other as the message receiver, and label them
   *Sender* and *Receiver* respectively to better identify their roles in the
   Route.
2. From the Routing folder, drop one cPipesAndFilters component onto the design workspace,
   between the two cFile components.
3. From the Core folder, drop two cMessagingEndpoint components onto the design workspace, one
   as the endpoint of stage A and the other as the endpoint of stage B, and
   label them *Stage\_A* and *Stage\_B* respectively to better identify their
   roles in the Route.
4. From the Custom folder, drop three cProcessor components onto the design workspace to monitor
   messages received on the receiver, stage A and stage B endpoints
   respectively, and label them *Monitor\_Receiver*, *Monitor\_stage\_A*, and *Monitor\_stage\_B* respectively to better identify their roles
   in the Route.
5. Right-click the cFile component labeled
   *Sender*, select Row > Route from the
   contextual menu, and click the cPipesAndFilters component.

   Repeat this step to set up the rest Row >
   Route connections, as shown
   above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cpipesandfilters-cfile-cmessagingendpoint-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, messages sent from
   Sender are redirected to endpoints identified by
   direct:a and direct:b by
   cPipesAndFilters\_1 before being routed to
   Receiver.
2. Press F6 to run your Route.

   RESULT: The message delivery goes through *stage A* and
   then *stage B* before reaching *Receiver*.
