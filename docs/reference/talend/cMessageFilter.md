<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter · versión 8.0 -->
# cMessageFilter

Last updated: 9/30/2026

Filters the content of messages according to the specified criterion and routes the
filtered messages to the specified output channel. All messages that do not match the
criteria will be dropped.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cMessageFilter Standard properties

These properties are used to configure cMessageFilter running in the Standard Job framework.

The Standard
cMessageFilter component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Language | Select the language of the expression you use to filter your messages from None, Bean, Constant, CorrelationID, EL, Groovy, Header, JoSQL, JSonPath, JXPath, MVEL, OGNL, PHP, Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  For more information about how to use the languages to create an expression, see the site <http://camel.apache.org/languages.html>. |
| Expression | Type in the expression to use to filter the messages. |
| Add Namespaces | This option appears when XPath is selected in the Language list.  Select this check box to add namespaces for the Xpath expression. Click [+] to add as many namespaces as required to the table and define the prefix and URI in the corresponding columns. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cMessageFilter is used as a middle component in a Route. |
| Connections | * Filter: Select this link to route the   filtered messages to the next endpoint. * Route: Select this link to route all the   messages from the sender to the next endpoint. |
| Limitation | n/a |

**Related concepts**  

* [Filtering messages according to a criterion](cmessagefilter-cfile-cprocessor-cprocessor-filtering-messages-according-to-criterion)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter-cfile-cprocessor-cprocessor-filtering-messages-according-to-criterion -->
# Filtering messages according to a criterion

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this use case, we filter XML messages that are sent from the sending endpoint according
to a defined criterion: only the XML files in which the value of the
*city* node is *Paris* are sent to a folder
named *Paris\_only*.

Of the four XML files used in this scenario, *Message\_1.xml* and *Message\_4.xml*
contain the city name of *Paris*. The following is an
example:

```
<person>
  <firstName>Pierre</firstName>
  <lastName>Dupont</lastName>
  <city>Paris</city>
</person>
```

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter-cfile-cprocessor-cprocessor-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter-cfile-cprocessor-cprocessor-configuring-components-and-connections)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter-cfile-cprocessor-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cMessageFilter](cmessagefilter "Filters the content of messages according to the specified criterion and routes the filtered messages to the specified output channel. All messages that do not match the criteria will be dropped.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter-cfile-cprocessor-cprocessor-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component labeled
   *Sender* to open its Basic settings view in the Component tab.
2. In the Path field, specify the file path
   to message source.
3. From the Encoding list, select the
   encoding type of your message files. Leave the other parameters as they
   are.
4. Double-click the cMessageFilter component
   to open its Basic settings view in the
   Component tab.
5. Select the language of the expression you want to use to filter your
   messages, and enter an expression to define a criterion according to which
   you want to filter your messages. 

   In this scenario, we want to sort out the XML files containing a city node
   with the value of Paris, so we select XPath
   from the Language list, and fill the in the
   Expression field with this expression:
   "/person[city='Paris']".
6. Double-click the cFile component labeled
   *Paris\_only* to open its Basic settings view in the Component view, and specify the path for the messages
   meeting the filter criterion in the Path
   field. 

   Repeat this step to define the path for all the messages from the sender
   in the cFile component labeled *Unfiltered*.
7. Double-click the cProcessor component labeled *Monitor\_Paris* to open its Basic settings view in the Component view, and customize the code in the Code area to display the file names of the
   messages that meet the filter criterion on the console:

   ```
   System.out.println("Message sent to folder Paris_only: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```

   Repeat this step to customize the code in the cProcessor
   component labeled *Monitor\_Unfiltered* to
   display the file names of all the messages from the sender.
8. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter-cfile-cprocessor-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

This scenario requires one cMessageFilter
component to filter the messages from the sender, one cFile component as the message sender, one cFile component to receiver the messages containing *Paris*, one cFile
component to receiver all the messages from the sender, and two cProcessor components to monitor the messages routed to
the two receivers.

## Procedure

1. From the Connectivity folder of the Palette, drop three cFile components onto the design workspace, and label them
   *Sender*, *Paris\_only*, and *Unfiltered* respectively to better identify their
   roles.
2. From the Routing folder, drop a cMessageFilter component onto the design workspace, and
   label it *Filter*.
3. From the Custom folder, drop two cProcessor components onto the design workspace, and label
   them *Monitor\_Paris* and *Monitor\_Unfiltered* respectively.
4. Right-click the cFile component labeled
   *Sender*, select Row > Route from the
   contextual menu and click the cMessageFilter component.
5. Right-click the cMessageFilter component,
   select Row > Filter from the contextual menu and click the cFile component labeled *Paris\_only*. This endpoint will retrieve the messages that
   meet the defined criterion.
6. Right-click the cMessageFilter component,
   select Row > Route from the contextual menu and click the cFile component labeled *Unfiltered*. This endpoint will collect all the messages,
   including those meeting the filter criterion. This connection is
   optional.
7. Right-click the cFile component labeled
   *Paris\_only*, select Row > Route from
   the contextual menu and click the cProcessor component labeled *Monitor\_Paris*. Repeat this step to connect the cFile component labeled *Unfiltered* to the cProcessor component labeled *Monitor\_Unfiltered*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter-cfile-cprocessor-cprocessor-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. To have a look at the generated code, click the Code tab at the bottom of the design workspace.

   As shown in this piece of code, messages from the sender are filtered by
   cMessageFilter\_1 according to
   .xpath("/person[city='Paris']") and the messages matching
   the filter are send .to the endpoint Paris\_only,
   while all messages are sent .to the endpoint
   Unfiltered.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. 

   You can also press F6 to execute it.

   RESULT: The messages are filtered according to the defined criterion and the messages
   containing "*Paris*" are redirected to the *Paris\_only* folder, all the messages, including
   those containing "*Paris*", are sent to the *Unfiltered* folder.
