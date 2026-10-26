<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer · versión 8.0 -->
# cDelayer

Last updated: 9/30/2026

Delays the delivery of messages.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cDelayer Standard properties

These properties are used to configure cDelayer running in the Standard Job framework.

The Standard
cDelayer component belongs to the Orchestration family.

## Basic settings

| Properties | Description |
| --- | --- |
| Time to wait (in ms) | Fill this field with an integer (in milliseconds) to define the time to wait before sending the message to the subsequent endpoint. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used in the middle of a Route. |
| Limitation | n/a |

**Related concepts**  

* [Using cDelayer to delay message routing](cdelayer-cfile-cprocessor-cprocessor-using-cdelayer-to-delay-message-routing)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer-cfile-cprocessor-cprocessor-using-cdelayer-to-delay-message-routing -->
# Using cDelayer to delay message routing

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cDelayer component is used to delay the
routing of each message to the target endpoint by 20 seconds.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer-cfile-cprocessor-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer-cfile-cprocessor-cprocessor-configuring-components)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer-cfile-cprocessor-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cDelayer](cdelayer "Delays the delivery of messages.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer-cfile-cprocessor-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the first cFile
   component, which is labeled `Read`, to open its Basic settings view in the Component tab.
2. In the Path field, enter or
   browse to the path to the source files, and leave the other parameters as they
   are.
3. Repeat these steps to define the target folder in property settings
   of the second cFile component, which is labeled
   `Write`.
4. Double-click the first cProcessor component, which is labeled
   `Read_monitor`, to open its Basics
   settings view in the Component
   tab.
5. In the Code area, customize the code to display the time
   each message is read from the source:

   ```
   Date date=new Date();
   SimpleDateFormat formatter = new SimpleDateFormat("HH:mm:ss");
   String s = formatter.format(date);
   System.out.println("\nMessage "+
   exchange.getIn().getHeader("CamelFileName")+
   " read at "+(s));
   ```
6. Repeat these steps to configure the second cProcessor component, which is labeled
   `Write_monitor`, to display the time each message is written
   to the target:

   ```
   Date date=new Date();
   SimpleDateFormat formatter = new SimpleDateFormat("HH:mm:ss");
   String s = formatter.format(date);
   System.out.println("Message "+
   exchange.getIn().getHeader("CamelFileName")+ " written at "+(s));
   ```
7. Double-click the cDelayer
   component, which is labeled `Delay_timer`, to open its
   Basic settings view in the Component tab.
8. In the Time to wait (in ms) field, enter
   the number of milliseconds by which you want to delay message delivery. Note
   that the value must be a positive integer.

   In this use case, each message needs to be delivered after a
   20-second delay.
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer-cfile-cprocessor-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

This use case requires one cDelayer component,
two cFile components, and two cProcessor components.

## Procedure

1. From the Connectivity folder of the Palette, drop two cFile components onto the design workspace, one to read
   files from a local folder and the other to write the files to another local
   folder.
2. From the Custom folder of the Palette, drop two cProcessor components onto the design workspace, one next to
   the reading component to monitor messages read from the source file folder,
   and the other next to the writing component to monitor messages written to
   the target file folder.
3. From the Orchestration folder of the Palette, drop one cDelayer component onto the design workspace, between the
   message reading monitor component and the message writing component.
4. Connect the components using Row >
   Route connections.
5. Label the components to better identify their roles in the Route, as shown
   above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-orchestration/cdelayer-cfile-cprocessor-cprocessor-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to have a look at the generated code.

   As shown in the code, a 20-second delay is implemented according to
   .delay(20000) in the message routing from the
   Read endpoint .to the Write
   endpoint.
2. Press F6 to execute the Route.

   RESULT: Each message read from the source folder is routed to the target folder after a
   20-second delay.
