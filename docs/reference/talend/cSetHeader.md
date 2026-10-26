<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader · versión 8.0 -->
# cSetHeader

Last updated: 9/30/2026

Sets headers or customizes the default headers, if any, on each message sent to it
for subsequent message processing.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cSetHeader Standard properties

These properties are used to configure cSetHeader running in the Standard Job framework.

The Standard
cSetHeader component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| New headers to set | * Click [+] to add as many headers   as required to the table. * Name: Type in a name for the   message header.  The header name *CorrelationID* is reserved.   The value of this header will be overridden by the correlation ID of   the message if it exist. * Language: Select the language of the   expression you use from None, Bean, Constant, CorrelationID,   EL, Groovy, Header,   JoSQL, JSonPath, JXPath,   MVEL, OGNL, PHP, Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  Select Bean if you want to call a   predefined Java Bean to return the header value.  Select CorrelationID to   use the existing correlation ID of the message as the header value if the   correlation ID is available in the closest cSOAP connected to this component. For more information about   the cSOAP component, see [cSOAP](/talend/en-US/components/8.0/mediation-apache-cxf/csoap). * Value: Type in the expression to   set the value of the message header, or the Bean class that will   return a value for the message header, in the form of   *beans.BEAN\_NAME*.  If CorrelationID is   selected in the Language list, this field   is grayed out. The existing correlation ID from the closest cSOAP connected to this component will be set as   the header value. For more information about the cSOAP component, see [cSOAP](/talend/en-US/components/8.0/mediation-apache-cxf/csoap). |
| Cleanup order | Select the order of header removal and addition from Remove before adding new headers and Remove after adding new headers. Information noteNote: This option is available only if you have installed the R2025-08 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Headers to remove | * Click [+] to add as many headers as   required to the table. Information noteNote: This option is available only if you have installed   the R2022-05 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. * Name: Type in the name of the message header to be removed.   You can either enter the exact header name or use the wildcard character   \*. For example, enter \* to remove all the   headers, or Camel\* to remove all headers starting with   Camel. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSetHeader is used as a middle component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Splitting a message and renaming the sub-messages according to contained information](csetheader-cfile-csplitter-cprocessor-splitting-message-and-renaming-sub-messages-according-to-contained-information)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader-cfile-csplitter-cprocessor-splitting-message-and-renaming-sub-messages-according-to-contained-information -->
# Splitting a message and renaming the sub-messages according to contained information

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a file message containing people information is split into
sub-messages. Each sub-messages is renamed according the city name it contains, and then
routed to another endpoint.

The following is the example XML file used in this use case:

```
<people>
    <person>
        <firstName>Pierre</firstName>
        <lastName>Dubois</lastName>
        <city>Paris</city>
    </person>
    <person>
        <firstName>Nicolas</firstName>
        <lastName>Yang</lastName>
        <city>Beijing</city>
    </person>
    <person>
        <firstName>Ellen</firstName>
        <lastName>Ripley</lastName>
        <city>Washington</city>
    </person>
</people>
```

A predefined JavaBean, *setFileNames*, is called by the cSetHeader component used in this use case to define a file name for
each message according to the city name it contains. For more information about creating
and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).

```
package beans;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class setFileNames {
	public String getCityName(Document document) {
		NodeList cities = document.getDocumentElement().getElementsByTagName(
				"city");
		Element city = (Element) cities.item(0);
		String textContent = city.getTextContent();
			return textContent+".xml";
		}
}
```

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader-cfile-csplitter-cprocessor-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader-cfile-csplitter-cprocessor-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader-cfile-csplitter-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cSetHeader](csetheader "Sets headers or customizes the default headers, if any, on each message sent to it for subsequent message processing.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cSplitter](/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader-cfile-csplitter-cprocessor-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component labeled
   *Sender* to display its Basic settings view in the Component tab.
2. In the Path field, fill in or browse to
   the path to the folder that holds the source files. 

   From the Encoding list, select the
   encoding type of your source files.

   In the FileName field, type in the file
   name of the source message. You can skip this step if the source folder
   contains only one file.
3. Repeat steps 1 and 2 above to define the output file path and
   encoding type in the Basic settings view of the
   other cFile component, which is labeled
   `Receiver`. Leave the FileName field blank.
4. Double-click the cSplitter component to
   display its Basic settings view in the
   Component tab. 

   In this use case, to split the message into sub-messages at each *person* node of the XML file, select XPath in the Language list and
   type in `"/people/person"` in the Expression field.
5. Double-click the cSetHeader component,
   which is labeled *Set\_file\_name* to display
   its Basic settings view in the Component tab.
6. Click [+] to add a row to the Headers table.

   In the Name field, type in the name of
   the header you want to give to the messages.

   Here, to define the file name for each incoming message, fill in
   "CamelFileName" as the header name.

   Select Bean in the Language field and type in the name of the predefined Java
   Bean in the Value field,
   beans.setFileNames.class in this use case.
7. Double-click the cProcessor
   component to display its Basic settings view in
   the Component tab, and customize the code so
   that the console will display information the way you want.

   In this use case, to display the file name each message routed to
   the receiving endpoint, customize the code as follows:

   ```
   System.out.println("File received: "+ 
   exchange.getIn().getHeader("CamelFileName"));
   ```
8. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader-cfile-csplitter-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

This use case uses two cFile components, one as
the message sender and the other as the receiver, a cSplitter component to split the source message into sub-messages, a
cSetHeader component to rename each
sub-message, and a cProcessor component to display
the file name of each message routed to the receiver.

## Procedure

1. From the Palette, expand the Connectivity folder, and drop two cFile components onto the design workspace.
2. From the Routing folder, drop a cSplitter component onto the design workspace,
   between the two cFile components.
3. From the Core folder, drop a cSetHeader component onto the design workspace, between the
   cSplitter component and the receiving
   cFile component.
4. Right-click the first cFile component,
   select Row > Route from the contextual menu and click the cSplitter component.
5. Right-click the cSplitter component,
   select Row > Split from the contextual menu and click the cSetHeader component.
6. Right-click the cSetHeader component,
   select Row > Route from the contextual menu and click the second
   cFile component.
7. Right-click the second cFile component,
   select Row > Route from the contextual menu and click the cProcessor component.
8. Label the components to better identify their roles in the Route, as shown
   above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader-cfile-csplitter-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to look at the generated code.

   As shown in the code, a message Route is built from one endpoint .to
   another, and while in routing, the source message is split according to the condition
   xpath("/people/person") by cSplitter\_1, and each sub-message is given a header named CamelFileName, the value of which is returned by .method(beans.setFileNames.class).
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: The source file message is split into sub-messages and each
   sub-message is renamed after the city name it contains and routed to the
   receiving endpoint.
