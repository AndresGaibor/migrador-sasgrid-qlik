<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap · versión 8.0 -->
# cWireTap

Last updated: 9/30/2026

Wiretaps messages to a user defined URI while they are sent to their original
endpoint. cWireTap also allows you to populate a new message to
this wiretap URI concurrently.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cWireTap Standard properties

These properties are used to configure cWireTap running in the Standard Job framework.

The Standard
cWireTap component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| URI | The endpoint URI to send the wire tapped message. |
| Populate new exchange | Select this check box to populate a new message to the wiretap URI. |
| Populate Type | * This option appears when the Populate new   exchange check box is selected. The Populate Type is either Expression or Processor. * Expression: Using expression   allows you to set the message body of the new exchange.  Language: Select the language of the   expression you want to use to set the message body from None, Bean,   Constant, CorrelationID, EL,   Groovy, Header, JoSQL, JSonPath, JXPath, MVEL, OGNL, PHP,   Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  For more information about how to use the languages to create an expression, see   the site <http://camel.apache.org/languages.html>.  Expression TXT: Enter the expression to set the   message body. * Processor: Using   processor gives you full power to specify how the exchange is populated   as you can set properties, headers and so on to the message with a piece   of Java code in the Code field. |
| Copy the original message | Select this check box to create a copy of the original exchange, which will be the totally the same as the original one. If this check box is not selected, only a new exchange with the same endpoint name will be created. The message body and headers are null.  The exchange pattern is InOnly for both conditions. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cWireTap can be a middle component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Wiretapping a message in a Route](cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-wiretapping-message-in-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-wiretapping-message-in-route -->
# Wiretapping a message in a Route

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cWireTap component is used to route a
message to a separate endpoint while it is routed to the ultimate destination.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-dropping-and-linking-components?id=603)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-configuring-components?id=604)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-viewing-code-and-executing-route?id=605)

**Related reference**  

* [cWireTap](cwiretap "Wiretaps messages to a user defined URI while they are sent to their original endpoint. cWireTap also allows you to populate a new message to this wiretap URI concurrently.")

**Related information**  

* [cJavaDSLProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cjavadslprocessor)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile
   component labeled `Source` to display its Basic settings view in the Component tab.
2. In the Path field, browse to
   or enter the input file path. In this use case, there is a
   Hello.txt file in the specified file path, which contains the
   content Hello World!. Leave the other parameters as they are.
3. Double-click the cWireTap
   component to display its Basic settings
   view in the Component tab.
4. Enter `"direct:a"` in the URI field to route the wiretapped message to this
   endpoint. 

   Select the Populate new
   exchange check box, select Processor as the populate type, and then enter the following code in
   the Code box to display the file name of the
   wiretapped message and its content on the console:

   ```
   System.out.println("\nMessage wiretapped: "+
   exchange.getIn().getHeader("CamelFileName"));
   System.out.println("Message content: "+
   exchange.getIn().getBody(String.class)+"\n");
   ```
5. Double-click the cJavaDSLProcessor component to display its Basic settings view in the Component tab.
6. In the Code field, enter the
   Java code `.to("direct:b")` to define the URI of the endpoint to
   route the original message to.
7. Double-click the cMessagingEndpoint component labeled
   `Endpoint_a` to display its Basic
   settings view in the Component
   tab. Enter `"direct:a"` in the URI field to retrieve the message routed to this endpoint.

   Repeat this operation to set the endpoint URI for *Endpoint\_b*.
8. Double-click the cProcessor
   component labeled `Monitor_a` to display its Basic settings view in the Component tab. Enter the following code in the Code box to display the file name of the message routed
   to *Endpoint\_a*. 

   ```
   System.out.println("Message on endpoint a: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```

   Then, configure the other cProcessor
   component in the same way to display the file name of the message routed to *Endpoint\_b*.
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, expand the Connectivity folder, and drop a cFile and two cMessagingEndpoint components onto the design
   workspace.
2. Expand the Routing folder, and drop a
   cWireTap component onto the design
   workspace.
3. Expand the Core folder, and drop a
   cJavaDSLProcessor components onto the
   design workspace.
4. Expand the Custom folder, and drop and
   two cProcessor components onto the design
   workspace.
5. Right-click the cFile component, select
   Row > Route from the contextual menu and click the cWireTap component.
6. Repeat this operation to connect the components as shown above.
7. Label the components to better identify their functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-wiretap/cwiretap-cfile-cjavadslprocessor-cmessagingendpoint-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to look at the generated code.

   In this partially shown code, any message from the endpoint Source will be
   wiretapped by .wireTap and routed to "direct:a". The fine name and content of each wiretapped
   message will be displayed on the console. The original message will be routed .to an endpoint identified by the URI "direct:b", which is defined in cJavaDSLProcessor\_1.
2. Click the Run view to display it and click the Run button to launch the execution of your Route.
   You can also press F6 to execute it. 

   RESULT: The source message is wiretapped and routed to endpoint *a* as well as being routed to endpoint *b*.
