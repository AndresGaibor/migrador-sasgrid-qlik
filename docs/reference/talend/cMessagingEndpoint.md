<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint · versión 8.0 -->
# cMessagingEndpoint

Last updated: 9/30/2026

Allows two applications to communicate by either sending or receiving messages.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cMessagingEndpoint Standard properties

These properties are used to configure cMessagingEndpoint running in the Standard Job framework.

The Standard
cMessagingEndpoint component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| URI | URI of the messages to send or receive. It can be of different format:  -File: "file:/",  -Database: "jdbc:/",  -Protocols: "ftp:/", "http:/"  -etc.  You can add parameters to the URI using the generic URI syntax, for example:  "file:/directoryName?option=value&option=value"  For more information on the different components that can be used in cMessagingEndpoint, see Apache Camel's Website: <http://camel.apache.org/components.html>. Information noteNote: If you have installed the R2023-08 Talend Studio Monthly update or a later one delivered by Talend, the operationName is mandatory in Salesforce URI. All consumer URIs now use the subscribe operation. For example:  * salesforce:subscribe:<topic\_name>, * salesforce:subscribe:event/<event\_name> * salesforce:subscribe:data/ChangeEvents |

## Advanced settings

| Properties | Description |
| --- | --- |
| Dependencies | By default, the camel core supports the following components: bean, browse, class, dataset, direct, file, language, log, mock, properties, ref, seda, timer, vm.  To use other components, you have to provide the dependencies corresponding to those components in the cMessagingEndpoint component. To do so:  Click the plus button to add new lines in the Camel component list. In the line added, select the component you want to use in cMessagingEndpoint. For more information about the commonly used Camel components, see [Commonly used Camel components](/talend/en-US/components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cmessagingendpoint-commonly-used-camel-components). Information noteNote: To work with Apache ActiveMQ, you can add camel-activemq in the Camel component list without selecting the Use a custom component check box. |
| Use a custom component | If you want to use a custom component, select this check box and click the [...] button to upload a jar file with your own component.    Information noteNote: All the transitive dependencies of this custom component should be included in the jar file. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as sending and/or receiving message endpoint according to its position in the Route. |
| Limitation | n/a |

**Related concepts**  

* [Moving files from one message endpoint to another](cmessagingendpoint-moving-files-from-one-message-endpoint-to-another)
* [Sending files to another message endpoint](cmessagingendpoint-sending-files-to-another-message-endpoint)
* [Using an XQuery endpoint to filter messages](cmessagingendpoint-cprocessor-cfile-cfile-using-xquery-endpoint-to-filter-messages)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-using-xquery-endpoint-to-filter-messages -->
# Using an XQuery endpoint to filter messages

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, we will use a cMessagingEndpoint
component to call a Route Resource as an XQuery parser to extract messages from the
local file system.

The following sample XML file is used in this scenario:

```
<people>
  <person id="8">
    <firstName>Ellen</firstName>
    <lastName>Ripley</lastName>
    <city>Washington</city>
  </person>  
  <person id="9">
    <firstName>Peter</firstName>
    <lastName>Green</lastName>
    <city>London</city>
  </person>
</people>
```

### In this section

* [Creating a Route Resource](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-creating-route-resource)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-viewing-code-and-executing-route)

**Related reference**  

* [cMessagingEndpoint](cmessagingendpoint "Allows two applications to communicate by either sending or receiving messages.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-moving-files-from-one-message-endpoint-to-another -->
# Moving files from one message endpoint to another

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario uses two cMessagingEndpoint components
to read and move files from one endpoint to another.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-dropping-and-linking-components?id=444)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-viewing-code-and-executing-route)

**Related reference**  

* [cMessagingEndpoint](cmessagingendpoint "Allows two applications to communicate by either sending or receiving messages.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-sending-files-to-another-message-endpoint -->
# Sending files to another message endpoint

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario accesses FTP service and transfers files from one endpoint to
another.

### In this section

* [Dropping and linking components](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-dropping-and-linking-components?id=448)
* [Configuring cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-configuring-cmessagingendpoint)
* [Checking the message exchange](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-checking-message-exchange)

**Related reference**  

* [cMessagingEndpoint](cmessagingendpoint "Allows two applications to communicate by either sending or receiving messages.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component to open
   its Basic settings view in the Component tab.
2. In the Path field, specify the path where
   the source file *people.xml* is located.
3. Right-click the Route from the repository tree view and select Manage Route Resources from the context
   menu.

   The Manage Route Resources wizard is
   opened.
4. In the Manage Route Resources wizard,
   click Add and select *SampleXquery* from the Resources tree view in
   the dialog. Click OK.

   The *SampleXquery* Route Resource is
   added in the table of the Manage Route
   Resources wizard.
5. Select the *SampleXquery* from the Route
   Resources list and click Copy Path. Click
   OK to close the wizard.
6. Double-click the cMessagingEndpoint
   component to display its Basic settings
   view in the Component tab.
7. In the URI field, enter *xquery:* and paste the path of the Route
   Resource *SampleXquery* that we just copied
   in double quotation marks.
8. Click the Advanced settings tab, add the
   Camel component saxon in the Dependencies list. For more information about
   Xquery, see Apache Camel's Website:
   <http://camel.apache.org/xquery-endpoint.html>.
9. Double-click the cProcessor component to
   open its Basic settings view in the
   Component tab.
10. In the Code area, enter the following
    code to display the messages intercepted on the console:

    ```
    System.out.println(exchange.getIn().getBody(String.class));
    ```
11. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-creating-route-resource -->
# Creating a Route Resource

Last updated: 9/30/2026

## Procedure

1. From the repository tree view, right-click the Resources node and select Create
   Resource from the context menu.
2. The New Route Resource wizard opens. In
   the Name field, type in a name for the
   Resource, for example, *SampleXquery*. Click Finish to close the wizard.
3. Enter the following code in the editor to extract the
   *firstName* and *lastName* of all
   the *person* elements.

   ```
   declare namespace ns0="http://com.sap/b";
   <people>
   {
   for $p in /people//person
   return
               <person>
               <firstName>{$p/firstName/text()}</firstName>
               <lastName>{$p/lastName/text()}</lastName>
               </person>
   }
   </people>
   ```
4. Press Ctrl+S to save your Route
   Resource.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Connectivity folder of the
   Palette, drag and drop a cFile and a cMessagingEndpoint component onto the design
   workspace.
2. From the Custom folder, drag and drop a
   cProcessor component onto the design
   workspace.
3. Link the components with the Row >
   Route connection as shown above.
4. Label the components for better identification of their
   functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-cprocessor-cfile-cfile-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. To have a look at the generated code, click the Code tab at the bottom of the design workspace.

   As shown in the code above, the message is routed from
   Message\_source\_cFile\_1
   .to
   cMessagingEndpoint\_1 and then processed by
   cProcessor\_1.
2. In the Run view, click the Run button to launch the execution of your Route.
   You can also press F6 to execute it. 

   RESULT: The *firstName* and
   *lastName* of all the *person*
   elements of the source file is printed in the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the component labeled *Sender* to open its Basic
   settings view in the Component tab.
2. In the URI field, type in the URI of the
   messages you want to route. 

   Type in `"file:///"` and the path to the folder
   containing the files.
3. Double-click the component labeled *Receiver* to open its Basic
   settings view in the Component tab.
4. In the URI field, type in the URI of the
   folder where you want to route your message. 

   Type in `"file:///"` and the path to the folder
   to which the files will be sent.
5. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Core folder of the Palette, drag and drop two cMessagingEndpoint components onto the design workspace, one
   as the message sender and the other as the message receiver, and label them
   *Sender* and *Receiver* respectively to better identify their roles in the
   Route.
2. Right-click the component labeled *Sender*, select Row >
   Route in the menu and drag to the
   *Receiver* to link them together with a
   route link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. To have a look at the generated code, click the Code tab at the bottom of the design workspace.

   The code shows the from and .to corresponding to
   the two endpoints: from for the sending one and
   .to for the receiving one.
2. In the Run view, click the Run button to launch the execution of your Route. 

   You can also press F6 to execute it.

   RESULT: The files are moved from their original folder to the target one.
   Furthermore, a new .camel folder is created
   in the source folder containing the consumed files. This is Camel's default
   behavior. Thus, the files will not be processed endlessly but they are
   backed up in case of problems.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-checking-message-exchange -->
# Checking the message exchange

Last updated: 9/30/2026

## Procedure

1. To have a look at the generated code, click the Code tab at the bottom of the design workspace.

   In this part of code, we can see a route represented by from
   and .to, corresponding to the sending and receiving
   endpoints.
2. In the Run view, click the Run button to launch the execution of your Route. 

   You can also press F6 to execute it.

   RESULT: The message is sent (copied) to the receiving endpoint.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint-configuring-cmessagingendpoint -->
# Configuring cMessagingEndpoint

Last updated: 9/30/2026

## Procedure

1. Double-click the component labeled *Sender* to display its Basic
   settings view in the Component tab.
2. In the URI field, type in the URI of the
   message you want to route. 

   Here, we are using an FTP component:
   ftp://indus@degas/remy/camel with URI specific parameters
   authenticating the FTP connection:
   ?username=indus&password=indus.
3. For the FTP component to work in Camel, click the Advanced settings tab of cMessagingEndpoint, click the [+] button to add a Camel component in the Dependencies table, and select
   *ftp* from the Camel
   component list to activate the FTP component.
4. Double-click the component labeled *Receiver* to open its Basic
   settings view in the Component tab.
5. In the URI field, type in the URI of the
   folder to which you want your message to be routed. 

   As we are handling files, type in *"file:///"* and the
   path to the folder to which the files will be sent.
6. Press Ctrl+S to save your Route.
