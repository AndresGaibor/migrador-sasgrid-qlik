<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip · versión 8.0 -->
# cRoutingSlip

Last updated: 9/30/2026

Routes the message consecutively through a series of processing steps, with the
sequence of steps unknown at design time and variable for each message.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cRoutingSlip Standard properties

These properties are used to configure cRoutingSlip running in the Standard Job framework.

The Standard
cRoutingSlip component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Header name | Type in name of the message header as defined in the preceding cSetHeader component, *mySlip* by default. The header should carry a list of endpoint URIs you wish each message to be routed to. |
| URI delimiter | Delimiter used to separate multiple endpoint URIs carried in the message header, comma (,) by default. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cRoutingSlip is used as a middle or end component of a sub-route. It always follows a cSetHeader component, which sets a header to each message to carry a list of endpoint URIs. |

**Related concepts**  

* [Routing a message consecutively to a series of endpoints](croutingslip-csetheader-cmessagingendpoint-cfile-routing-message-consecutively-to-series-of-endpoints)
* [Routing each message conditionally to a series of endpoints](croutingslip-csetheader-routing-each-message-conditionally-to-series-of-endpoints)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-cmessagingendpoint-cfile-routing-message-consecutively-to-series-of-endpoints -->
# Routing a message consecutively to a series of endpoints

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, messages from a file system is routed consecutively to a series of
endpoints according to the URIs carried in the message header.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-cmessagingendpoint-cfile-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-cmessagingendpoint-cfile-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-cmessagingendpoint-cfile-viewing-code-and-executing-route)

**Related reference**  

* [cRoutingSlip](croutingslip "Routes the message consecutively through a series of processing steps, with the sequence of steps unknown at design time and variable for each message.")

**Related information**  

* [cSetHeader](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-routing-each-message-conditionally-to-series-of-endpoints -->
# Routing each message conditionally to a series of endpoints

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, which is based on the previous scenario, each message from a file
system is routed consecutively to different endpoints according to the city name it
contains.

All files used in this use case are named after the city name they contain. The
following are the extracts of two examples:

Beijing.xml:

```
<person>
    <firstName>Nicolas</firstName>
    <lastName>Yang</lastName>
    <city>Beijing</city>
</person>
```

Paris.xml:

```
<person>
  <firstName>Pierre</firstName>
  <lastName>Dupont</lastName>
  <city>Paris</city>
</person>
```

A predefined JavaBean, *setEndpoints*, is called in this use case to return endpoint URIs according to
the city name contained in each message, so that the messages will be routed as
follows:

* The message containing the city name *Paris* will be routed
  first to endpoint *a*, then to endpoint
  *b*, and finally to endpoint *c*.
* The message containing the city name *Beijing* will be
  routed first to endpoint *c*, then to endpoint
  *a*, and finally to endpoint *b*.
* Any other messages will be routed to endpoint *b* and then
  to endpoint *c*.

For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).

```
package beans;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class setEndpoints {
	public String helloExample(Document document) {
		NodeList cities = document.getDocumentElement().getElementsByTagName(
				"city");
		Element city = (Element) cities.item(0);
		String textContent = city.getTextContent();
		if ("Paris".equals(textContent)) {
			return "direct:a,direct:b,direct:c";
		} else if ("Beijing".equals(textContent)) { 
			return "direct:c,direct:a,direct:b";
		} else
			return "direct:b,direct:c";
	}
}
```

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-viewing-code-and-executing-route)

**Related reference**  

* [cRoutingSlip](croutingslip "Routes the message consecutively through a series of processing steps, with the sequence of steps unknown at design time and variable for each message.")

**Related information**  

* [cSetHeader](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-cmessagingendpoint-cfile-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component, which
   is labeled *Sender*, to display its Basic settings view in the Component tab.
2. In the Path field, fill in or browse to the path to the
   folder that holds the source files *Beijing.xml*, *London.xml*,
   *Paris.xml*, and *Washington.xml*.

   From the Encoding list, select the
   encoding type of your source files. Leave the other parameters as they
   are.
3. Double-click the cSetHeader component,
   which is labeled *Set\_endpoints*, to
   display its Basic settings view in the
   Component tab.
4. Click [+] to add a row to the Headers table.

   In the Name field, type in the name of
   the header you want to add to each message.

   In this use case, we simply use *mySlip*, which is the
   default value filled in the Header name
   field of the cRoutingSlip component.
5. From the Language list box, select the Constant or Simple, and in the Value
   field, type in the URIs you wish the message to be routed consecutively to,
   separated by a comma, which is the default value of the URI delimiter field of the cRoutingSlip component.

   In this use case, we want the message to be routed first to endpoint
   *c*, then to endpoint *a*, and
   finally to endpoint *b*.
6. Double-click the cRoutingSlip component,
   which is labeled *Routing\_slip*, to
   display its Basic settings view in the
   Component tab, and define the message
   header in the Header name field and the URI
   delimiter in the URI delimiter field. 

   In this use case, we simply use the default settings.
7. Double-click the cMessagingEndpoint
   component labeled *Endpoint\_a* to display its Basic settings view in the Component tab, and type in the URI in the URI field for the destination of your messages. 

   Here, we want to use this component to retrieve the message routed to the
   URI *direct:a*.

   Repeat this step to set the endpoint URIs in the other cMessagingEndpoint components:
   *direct:b* and *direct:c*
   respectively.
8. Double-click the cProcessor component,
   which is labeled *Monitor\_a*, to display
   its Basic settings view in the Component tab, and customize the code so that the
   console will display information the way you wish.

   Here, we want to use this component to monitor the messages routed to the
   connected endpoint *a* and display the file name, so we
   customize the code accordingly, as follows:

   ```
   System.out.println("Message received on endpoint a: "+ 
   exchange.getIn().getHeader("CamelFileName"));
   ```

   Repeat this step to customize the code for the other two cProcessor components, for messages routed to the
   connected endpoints *b* and *c*
   respectively.

   ```
   System.out.println("Message received on endpoint b: "+ 
   exchange.getIn().getHeader("CamelFileName"));
   ```

   ```
   System.out.println("Message received on endpoint c: "+ 
   exchange.getIn().getHeader("CamelFileName"));
   ```
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-cmessagingendpoint-cfile-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

This use case requires a cFile component as the
message sender, a cSetHeader component to define a
series of endpoints, a cRoutingSlip component to
route messages to the endpoints consecutively, three cMessagingEndpoint components to retrieve messages routed to the
endpoints, and three cProcessor components to
monitor messages routed to the connected messaging endpoints.

## Procedure

1. From the Palette, expand the Connectivity folder, drop one cFile and three cMessagingEndpoint components onto the design workspace, and
   label them to better identify their roles in the Route, as shown
   above.
2. From the Core folder, drop a cSetHeader component onto the design workspace, and label it
   to better identify its role in the Route.
3. From the Routing folder, drop a cRoutingSlip component onto the design workspace,
   and label it to better identify its role in the Route.
4. From the Custom folder, drop three cProcessor components onto the design workspace, and label
   them to better identify their roles in the Route.
5. Right-click the cFile component, select
   Row > Route from the contextual menu and click the cSetHeader component.
6. Right-click the cSetHeader component,
   select Row > Route from the contextual menu and click the cRoutingSlip component.
7. Repeat this operation to connect the cMessagingEndpoint components to the corresponding cProcessor components.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-cmessagingendpoint-cfile-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   In this partially shown code, messages from the sender are given a header
   according to .setHeader, which carries a list of URIs
   ("direct:c,direct:a,direct:b"), and then routed in the slip
   pattern according by cRoutingSlip\_1.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. 

   You can also press F6 to execute it.

   RESULT: The source file messages are routed consecutively to the defined
   endpoints: *c*, then *a*, and then
   *b*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## About this task

In this scenario, you only need to configure the cSetHeader component to call the predefined Java Bean, and
keep the settings of all the other components are they are in the previous scenario.

## Procedure

1. Double-click the cSetHeader component to
   display its Basic settings view in the
   Component tab.
2. Select Bean from the Language list box, and in the Value field, specify the Java Bean that will return the
   endpoint URIs. In this use case, type in: 

   `beans.setEndpoints`
3. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

In this scenario, we will reuse the Route set up in the previous scenario, without
adding or removing any components or modifying any connections.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-routing-slip/croutingslip-csetheader-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   In this partially shown code, messages from the sender are given a header
   according to .setHeader, which carries a list of URIs returned
   by the beans.setEndpoints.class, and then routed to the
   cRoutingSlip\_1.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. 

   You can also press F6 to execute it.

   RESULT: The sources are routed consecutively to the defined endpoints: the
   message containing the city name *Beijing* is routed
   first to endpoint *c*, then to endpoint
   *a*, and finally to endpoint *b*;
   the message containing the city name *Paris* is routed
   first to endpoint *a*, then to endpoint
   *b*, and finally to endpoint *c*;
   the other messages are routed to endpoint *b* and then to
   endpoint *c*.
