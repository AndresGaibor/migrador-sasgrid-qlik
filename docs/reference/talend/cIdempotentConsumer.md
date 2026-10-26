<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer · versión 8.0 -->
# cIdempotentConsumer

Last updated: 9/30/2026

Identifies messages that have already been sent to the receiver and eliminates
them. Messages are still sent by the sender but are ignored by the receiver at the
delivery stage.

cIdempotentConsumer deduplicates
messages and thereby prevents the receiving message endpoint from
receiving duplicate messages.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cIdempotentConsumer Standard properties

These properties are used to configure cIdempotentConsumer running in the Standard Job framework.

The Standard
cIdempotentConsumer component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Repository Type | Message identifiers need to be stored in a repository. For new incoming messages, identifiers are checked against the ones stored in the repository to identify and drop duplicates. There are two ways to store them:  Memory: messages identifiers are stored temporarily.  Information noteWarning: *The in-memory storage mode can easily run out of memory and does not work in a clustered environment.*  File: messages identifiers are stored in a file. Specify the path to this file in the File store field. |
| File store | Specify the path and name of the file storing messages identifiers. |
| Cache Size | Type in the size of the cache, namely the number of message identifiers to store. |
| Use language | Select this check box if you want to specify the language used in the Predicate field to specify the identifier of the messages. In the Language list, select from None, Bean, Constant, CorrelationID, EL, Groovy, Header, JoSQL, JSonPath, JXPath, MVEL, OGNL, PHP, Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  For more information about how to use the languages to create an expression, see the site <http://camel.apache.org/languages.html>. |
| Predicate | Type in the expression to use to specify the identifier of the messages. |
| Add Namespaces | This option appears when XPath is selected in the Language list.  Select this check box to add namespaces for the Xpath expression. Click [+] to add as many namespaces as required to the table and define the prefix and URI in the corresponding columns. |
| Eager | Select this check box to detect duplicate messages even when messages are currently in progress; clear it to detect duplicates only when messages have successfully been processed.  By default, this check box is selected. |
| SkipDuplicate | Select this check box to drop duplicates; clear it to ignore duplicates so that all messages will be continued.  By default, this check box is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cIdempotentConsumer is used as a middle component in a Route. |
| Connections | * idemp: The idemp link   retrieves messages deduplicated by the cIdempotentConsumer   component. * Route: As an optional link, the   Route link retrieves all messages from the message   sender. |
| Limitation | n/a |

**Related concepts**  

* [Deduplicating messages while routing them](cidempotentconsumer-cprocessor-cfile-cfile-deduplicating-messages-while-routing-them)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer-cprocessor-cfile-cfile-deduplicating-messages-while-routing-them -->
# Deduplicating messages while routing them

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, duplicated messages are filtered and only the unique one is routed to the
destination.

Three XML files that have the same content, as shown below, are used in this use
case.

```
<people>
	<person id="8">
		<firstName>Ellen</firstName>
		<lastName>Ripley</lastName>
		<city>Washington</city>
	</person>
</people>
```

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer-cprocessor-cfile-cfile-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer-cprocessor-cfile-cfile-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer-cprocessor-cfile-cfile-viewing-code-and-executing-route)

**Related reference**  

* [cIdempotentConsumer](cidempotentconsumer "Identifies messages that have already been sent to the receiver and eliminates them. Messages are still sent by the sender but are ignored by the receiver at the delivery stage.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer-cprocessor-cfile-cfile-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile
   component, which is labeled `Source`, to display its Basic settings view in the Component tab.
2. In the Path field, specify the file path to the message source. 

   From the Encoding list, select the encoding type of your source files, and leave all the other parameters as they are.
3. Double-click the cIdempotentComsumer component, which is labeled
   `Deduplicator`, to display its Basic
   settings view in the Component
   tab.
4. From the Repository Type list, select between Memory and File to specify where the message identifiers will be stored before the deduplication process. For this scenario, select File.

   In the File store field, specify the location of the file storing message identifiers.

   In the Expression field, enter
   an expression to filter the messages. In this scenario, enter the following
   expression to filter the messages according to the *person* node
   of the XML files: `xpath("/people/person")`, and leave all the
   other parameters as they are. Alternatively, you can select the Use language check box, select XPath from the Language list,
   and enter `"/people/person"` in the Predicate field.
5. Double-click the cProcessor
   component labeled `Unique` to display its Basic settings view in the Component tab.
6. In the Code area, customize the code to
   display the file name of the message that passes the deduplication:

   ```
   System.out.println("Message consumed on Unique: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```
7. Repeat these steps to configure the other cProcessor component, which is labeled *All*, to display the file names of all the
   messages coming from the source: 

   ```
   System.out.println("Message consumed on All: "+
   exchange.getIn().getHeader("CamelFileName"));
   ```
8. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer-cprocessor-cfile-cfile-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

This use case requires one cFile component, one
cIdempotentComsumer component, and two
cProcessor components.

## Procedure

1. From the Palette, expand the Connectivity folder, select the cFile component, and drop it onto the design workspace as
   the message source component.
2. Expand the Routing folder, select the
   cIdempotentComsumer component and drop
   it onto the design workspace as the message deduplicator.
3. Expand the Custom folder, drop two cProcessor components onto the design workspace, one as the
   consumer for deduplicated messages and another for all messages.
4. Right-click the cFile component, select
   Row > Route from the contextual menu and click the cIdempotentComsumer component.
5. Right-click the cIdempotentComsumer
   component, select Row > idemp from the contextual menu and click the
   cProcessor component on the top.
6. Connect the cIdempotentComsumer component
   to the other cProcessor component using a
   Row > Route connection. This optional connection will retrieve all
   the messages coming from the source.
7. Label the components to better identify their roles in the Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cidempotentconsumer-cprocessor-cfile-cfile-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to view the generated code.

   In this partially shown piece of code, messages from the Source
   are filtered according to the expression
   xpath("/people/person") and deduplicated by
   cIdempotentConsumer\_1.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: When several files have the same content, only the first one is
   routed to the receiving endpoint.
