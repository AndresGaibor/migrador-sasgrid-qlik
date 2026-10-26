<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter · versión 8.0 -->
# cDynamicRouter

Last updated: 9/30/2026

Routes a message or messages to different endpoints on specified
conditions.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cDynamicRouter Standard properties

These properties are used to configure cDynamicRouter running in the Standard Job framework.

The Standard
cDynamicRouter component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Bean class | Enter the name of the bean class to be used for the dynamic router. |
| Specify the method | Select this check box to specify the method to be used which is defined in the bean class. |
| Ignore Invalid Endpoints | Select this check box to ignore unresolved endpoint URIs. Clear the check box to throw an exception when endpoint URIs are not valid. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cDynamicRouter is used as a middle or end component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Routing files conditionally to different file paths](cdynamicrouter-cmessagingendpoint-cprocessor-cfile-routing-files-conditionally-to-different-file-paths)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter-cmessagingendpoint-cprocessor-cfile-routing-files-conditionally-to-different-file-paths -->
# Routing files conditionally to different file paths

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, three file messages containing people information are routed to
different endpoints according to the city names they contain.

The following is an extract of the example XML files used in this use case:

Message\_1.xml:

```
<person>
  <firstName>Ellen</firstName>
  <lastName>Ripley</lastName>
  <city>Washington</city>
</person>
```

Message\_2.xml:

```
<person>
  <firstName>Peter</firstName>
  <lastName>Green</lastName>
  <city>London</city>
</person>
```

Message\_3.xml:

```
<person>
  <firstName>Alice</firstName>
  <lastName>Yang</lastName>
  <city>Beijing</city>
</person>
```

A predefined JavaBean, *setDynaURI*, is called in this use case to return endpoint URIs according to the city
name contained in each message, so that the message containing the city name *Washington* will be routed to endpoint *Washington* and so forth.

For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).

```
package beans;

import org.apache.camel.Exchange;
import org.apache.camel.Header;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class setDynaURI {

 public String setURI(Document document,
      @Header(Exchange.SLIP_ENDPOINT) String previous) {
    if(previous!=null){
     return null;
    }
  NodeList cities = document.getDocumentElement().getElementsByTagName(
    "city");
  Element city = (Element) cities.item(0);
  String textContent = city.getTextContent();
   return "direct:"+textContent;
  } 
}
```

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter-cmessagingendpoint-cprocessor-cfile-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter-cmessagingendpoint-cprocessor-cfile-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter-cmessagingendpoint-cprocessor-cfile-viewing-code-and-executing-route)

**Related reference**  

* [cDynamicRouter](cdynamicrouter "Routes a message or messages to different endpoints on specified conditions.")

**Related information**  

* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter-cmessagingendpoint-cprocessor-cfile-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the input cFile component to
   display its Basic settings view in the
   Component tab and set its properties. 

   In this use case, simply specify the input file path and leave the other
   parameters as they are.
2. Double-click the cDynamicRouter component
   to display its Basic settings view in the
   Component tab.
3. In the Bean class field, type in the name
   of the predefined Java bean. Leave the Specify the
   method check box unselected as there is only one method in
   the Java bean and leave the Ignore Invalid
   Endpoints check box unselected if you want the component to
   throw an exception when endpoint URIs are not valid.
4. Double-click the first cMessagingEndpoint component, which is labeled
   `Washington`, to display its Basic
   settings view in the Component
   tab, and type in the URI in the URI field for
   the destination of your message. 

   Here, this component is used to retrieve the message routed to the
   URI `direct:Washington`, as shown below.
5. Repeat this step to set the endpoint URIs for the other two
   cMessagingEndpoint components:
   `direct:London` and `direct:Beijing`
   respectively.
6. Double-click the first cProcessor component, which is labeled
   `Monitor_Washington`, to display its Basic settings view in the Component tab.
7. In the Code box, customize the
   code to display the file name of the message routed to the endpoint
   `Washington` on the console.

   ```
   System.out.println("Message on endpoint Washington: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```
8. Repeat these steps to configure the other two cProcessor components to display the file names of the
   messages routed to the endpoints `London` and
   `Beijing` respectively.
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter-cmessagingendpoint-cprocessor-cfile-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, expand the Connectivity folder, and drop one cFile and three cMessagingEndpoint components onto the design workspace.
2. Expand the Routing folder, and drop a
   cDynamicRouter component onto the
   design workspace.
3. Expand the Custom folder, and drop three cProcessor components onto the design
   workspace.
4. Label the components for better identification of their respective
   functionality.
5. Right-click the cFile component, select
   Row > Route from the contextual menu and click the cDynamicRouter component.
6. Repeat this operation to connect the cMessagingEndpoint components to the cProcessor components.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-dynamic-router/cdynamicrouter-cmessagingendpoint-cprocessor-cfile-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, the incoming message from the endpoint
   Message\_source is routed by .dynamicRouter to
   endpoints the URIs of which are dynamically set according to
   beans.setDynaURI.class.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. 

   You can also press F6 to execute it.

   RESULT: The source messages are routed to different endpoints based on the
   city names contained in the messages.
