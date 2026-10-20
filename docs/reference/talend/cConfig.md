<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig · versión 8.0 -->
# cConfig

Last updated: 9/30/2026

Sets the CamelContext using Java code.

## cConfig Standard properties

These properties are used to configure cConfig running in the Standard Job framework.

The Standard
cConfig component belongs to the Custom family.

## Basic settings

| Properties | Description |
| --- | --- |
| Code | Type in the Java code you want to implement. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use MDC Logging | Select this check box to enable the use of MDC logging.  To be able to use this option, you need to open the Log4j view in the Project Settings dialog box by clicking File > Edit Project Properties on the toolbar of the Talend Studio main window. Select the Activate log4j in components check box to activate the log4j feature. Then change the ConversionPattern in the log4j template to add your custom MDC property like %X{mdcPropertyName}.  To show the MDC information in the log, use the cLog component and a cProcessor before and after the cLog. In the cProcessor before the cLog, enter the code org.apache.log4j.MDC.put("Key", "Value"); to add the custom property. In the cProcessor after the cLog, enter the code org.apache.log4j.MDC.remove("Key"); to remove the MDC property.  For more information about how to activate Log4j in components and how to customize Log4j configuration, see [Activating and configuring Log4j](/talend/r/en-US/8.0/studio-user-guide/studio-configure-log4j) in the Talend Studio User Guide.  For more information about MDC logging, see the website <http://camel.apache.org/mdc-logging.html>.  For more information about the cLog component, see [cLog](/talend/en-US/components/8.0/mediation-logs-and-errors/clog). |
| Imports | Enter the Java code that helps to import, if necessary, external libraries used in the Code box. |
| Dependencies | Click [+] to add the library or libraries that are required by the CamelContext or Typeconverter Registry to Talend Studio.  Click [...] in the Lib Path field to show the Module dialog box. For more information, see the tLibraryLoad component. Information noteNote: It is recommended to use the camel-activemq-alldep jar instead of activemq-all jar to work with Apache ActiveMQ. |
| Check | Click this button to check the version of the libraries that are added to the Route in the Talend Artifact Repository. The libraries are listed in the table below, with the versions shown in the Update To column. If the version of the local library is the same as in the Talend Artifact Repository, a √ is shown in the Status column. If the version of the local library is older than in the Talend Artifact Repository, a × is shown in the Status column, and the check box in the Sync column is selected by default. |
| Sync | Select the check box in the Sync column of the table for the libraries that you want to update and click the Sync button to download and install the newer version from the Talend Artifact Repository into Talend Studio. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cConfig cannot be added directly in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Implementing a dataset from the Registry](cconfig-cmessagingendpoint-cprocessor-cprocessor-implementing-dataset-from-registry)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig-cmessagingendpoint-cprocessor-cprocessor-implementing-dataset-from-registry -->
# Implementing a dataset from the Registry

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, an instance of dataset is added in the Registry and implemented by a
cMessagingEndpoint component.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig-cmessagingendpoint-cprocessor-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig-cmessagingendpoint-cprocessor-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig-cmessagingendpoint-cprocessor-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cConfig](cconfig "Sets the CamelContext using Java code.")

**Related information**  

* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig-cmessagingendpoint-cprocessor-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cConfig
   component, which is labeled *Create\_dataset*, to display its
   Basic settings view in the Component tab and set its parameters.
2. Write a piece of code in the Code field to register the dataset instance *foo*
   into the registry, as shown below. 

   ```
   SimpleDataSet dataset = new SimpleDataSet(1);
   String messageBody = "testbody";
   dataset.setDefaultBody(messageBody);
   registry.put("foo", dataset);
   ```
3. Double-click the input cMessagingEndpoint component, which is labeled *Read\_dataset*, to display its Basic
   settings view in the Component
   tab.
4. In the URI field, enter
   `dataset:foo` between the quotation marks.
5. Double-click the cProcessor
   component, which is labeled *Monitor*, to display its Basic settings view in the Component tab.
6. In the Code box, customize the code as
   follows so that the Run console displays
   the message contents:

   ```
   System.out.println("Message content: "+ 
   exchange.getIn().toString());
   ```
7. Press Ctrl+S to save your
   Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig-cmessagingendpoint-cprocessor-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, expand the Custom folder, and drop a cConfig component onto the design workspace.
2. Expand the Connectivity folder, and drop a cMessagingEndpoint component onto the design
   workspace.
3. Expand the Custom folder, and drop a cProcessor component onto the design
   workspace.
4. Right-click the input cMessagingEndpoint
   component, select Row > Route from the contextual menu and click the
   cProcessor component.
5. Label the components to better identify their functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-camelcontext/cconfig-cmessagingendpoint-cprocessor-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom
   of the design workspace to read the generated code. 

   As shown in the code, a message route is built from the endpoint identified byRead\_dataset and cProcessor\_1 gets the
   message content and displays it on the console.
2. Click the Run view to display it
   and click the Run button to launch the execution
   of your Route. You can also press F6 to execute
   it. 

   RESULT: The message content is printed in the console.
