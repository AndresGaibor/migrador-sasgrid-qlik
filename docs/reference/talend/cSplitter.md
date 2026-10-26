<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter · versión 8.0 -->
# cSplitter

Last updated: 9/30/2026

Splits a message into several sub-messages so that they can be
handled and treated differently in individual routes.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cSplitter Standard properties

These properties are used to configure cSplitter running in the Standard Job framework.

The Standard
cSplitter component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Language | Select the language of the expression you want to use to split your messages, from None, Constant, EL, Groovy, Header, JoSQL, JSonPath, JXPath, MVEL, OGNL, PHP, Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  For more information about how to use the languages to create an expression, see the site <http://camel.apache.org/languages.html>. |
| Correlation expression/Expression | Type in the expression to use to split the messages. |
| Correlation expression/Use Result Class Type | This option appears when XPath is selected in the Language list.  Select this check box to set the result type of the sub-messages in the field that appears. The default native XML objects org.w3c.dom.NodeList will be used if not specified. |
| Correlation expression/Add Namespaces | This option appears when XPath is selected in the Language list.  Select this check box to add namespaces for the Xpath expression. Click [+] to add as many namespaces as required to the table and define the prefix and URI in the corresponding columns. |
| Use Strategy | Select this check box to refer to an aggregation strategy to assemble the replies from the sub-messages into a single outgoing message from the splitter. Enter the ID of the aggregation strategy or select a predefined aggregation strategy.  * UseOriginalAggregationStrategy: Use the original   exchange. * UseLatestAggregationStrategy: Use the latest   exchange. * GroupedMessageAggregationStrategy: Aggregate all   messages into a single combined exchange holding all the aggregated messages   in a list of messages as the message body. * GroupedExchangeAggregationStrategy: Aggregate all   exchanges into a single combined exchange holding all the aggregated   exchanges in a list of exchanges as the message body. * GroupedBodyAggregationStrategy: Aggregate body of   input messages into a single combined exchange holding all the aggregated   bodies in a list of objects as the message body.   Information noteNote: The predefined aggregation strategies are available only if you have installed the R2024-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  The sub-message replies will be aggregated in the order they come back if Streaming is enabled. If not, the sub-message replies will be aggregated in the same order as they were split. |
| Parameters/Parallel Processing | Select this check box to process the sub-messages concurrently. The caller thread will wait until all sub-messages have been fully processed before it continues. |
| Parameters/Stop on Exception | Select this check box to stop processing immediately when an exception occurs. |
| Parameters/Streaming | Select this check box to split the message in a streaming fashion, which means it will split the input message in chunks. It is recommended to enable this option when processing big messages. |
| Parameters/Share Unit of Work | Select this check box to share the unit of work between the parent exchange and each split exchange. For more information and an use case of this option, see the site <http://camel.apache.org/splitter.html>. |
| Parameters/Timeout | Specify a total timeout in millisecond. If the message is not split and processed within the given time frame, the timeout triggers and the splitter breaks out. If you have installed the R2023-05 Talend Studio Monthly update or a later one delivered by Talend, you can use context variables of String or Long type in the Timeout parameter. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSplitter is used as a middle component in a Route. |
| Connections | * split: Select this link to route the split   messages to the next endpoint. * Route: Select this link to route all the messages   from the sender to the next endpoint. |
| Limitation | n/a |

**Related concepts**  

* [Using cSplitter to split a message and aggregate replies from sub-messages](csplitter-cdirect-csetbody-ctimer-using-csplitter-to-split-message-and-aggregate-replies-from-sub-messages)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter-cdirect-csetbody-ctimer-using-csplitter-to-split-message-and-aggregate-replies-from-sub-messages -->
# Using cSplitter to split a message and aggregate replies from sub-messages

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, the cSplitter component
is used to split a message and aggregate the replies from sub-messages.

A predefined JavaBean, *AppendAggregator* will be called to as the strategy to aggregate the replies
from sub-messages. For more information about creating and using JavaBeans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).

```
package beans;
import org.apache.camel.Exchange;
import org.apache.camel.processor.aggregate.AggregationStrategy;

public class AppendAggregator implements AggregationStrategy {

	public Exchange aggregate(Exchange oldEx, Exchange newEx) {
		if(oldEx==null){
			return newEx;
		}
		String oldBody = oldEx.getIn().getBody(String.class);
		String newBody = newEx.getIn().getBody(String.class);
		newEx.getIn().setBody(oldBody + "\n" + newBody);
		return newEx;
	}
}
```

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter-cdirect-csetbody-ctimer-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter-cdirect-csetbody-ctimer-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter-cdirect-csetbody-ctimer-viewing-code-and-executing-route)

**Related reference**  

* [cSplitter](csplitter "Splits a message into several sub-messages so that they can be handled and treated differently in individual routes.")

**Related information**  

* [cDirect](/talend/en-US/mediation-components/8.0/mediation-direct/cdirect)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)
* [cBeanRegister](/talend/en-US/mediation-components/8.0/mediation-bean/cbeanregister)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter-cdirect-csetbody-ctimer-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## Procedure

1. Double-click the cBeanRegister component
   labeled *appendAggregator* to display its
   Basic settings view in the Component tab.
2. In the Id field, enter
   "appendAggregator". Select the Simple option and in the Class
   Name field, enter the name of the predefined Java bean,
   beans.AppendAggregator in this scenario, which will be
   called later by the cSplitter
   component.
3. Double-click the cTimer component labeled
   *Starter* to display its Basic settings view in the Component tab.
4. In the Repeat field, enter 1
   to trigger the message exchange. Keep the default settings of the other
   options.
5. Double-click the cSetbody component
   labeled *Set\_body* to display its Basic settings view in the Component tab.
6. Select SIMPLE in the Language list and enter "thing1, thing2,
   thing3" in the Expression field
   as the message body.
7. Configure the cSetbody component labeled
   *Set\_new\_body* in the same way to set
   new body to the sub-messages. In the Expression field, enter \*\*\* SPLIT: ${body} to
   add *\*\*\* SPLIT:*  before the old message body.
8. Double-click the cSplitter component to
   display its Basic settings view in the
   Component tab.
9. In this use case, we want to split the message body into sub-messages
   using , as the separator.

   Select Simple in the Language list and enter ${body} in
   the Expression field.

   Select the Use Strategy check box. In the
   Strategy field, enter the Id of the
   preregistered Java bean *appendAggregator*, which will be
   used to aggregate the replies from sub-messages.
10. Double-click the cDirect component
    labeled *directA\_sender* to display its
    Basic settings view in the Component tab.
11. Click [...] and select the *directA\_receiver* node to receive the
    sub-messages.
12. Double-click the cDirect component
    labeled *directA\_receiver* to display its
    Basic settings view in the Component tab.
13. In the Name field, type in
    "directA" to identify this endpoint.
14. Keep the default settings of the cLog
    components labeled *Log\_Finished* and
    *Log\_Split*. *Log\_Finished* will
    log the aggregated replies from sub-messages. *Log\_Split*
    will log the sub-messages.
15. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter-cdirect-csetbody-ctimer-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, expand the Custom folder. Drag and drop a cBeanRegister component onto the design workspace.
2. From the Orchestration folder, drag and drop a cTimer components onto the design
   workspace.
3. From the Core folder, drag and drop two cSetBody and two cDirect components onto the design workspace.
4. From the Routing folder, drag and drop a
   cSplitter component onto the design
   workspace.
5. From the Miscellaneous folder, drag and
   drop two cLog components onto the design
   workspace.
6. Label the components to better identify their roles in the Route as shown
   above.
7. Right-click the cSplitter component,
   select Row > Split from the contextual menu and click the cDirect component labeled
   *directA\_sender*.
8. Right-click the cSplitter component
   again, select Row > Route from the contextual menu and click the cLog component labeled
   *Log\_Finished*.
9. In the same way, link the other components in the Route using the
   Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter-cdirect-csetbody-ctimer-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to look at the generated code.

   As shown in the code, the message Route is built from one endpoint .to
   another. The message sent to cSplitter\_1 is split by
   the method .split().simple("${body}") and the replies
   from the sub-messages are aggregated by the method .aggregationStrategyRef("appendAggregator").
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: The source message is split into sub-messages using ,
   as the separator and each sub-message is given a new message body. The
   replies from the sub-messages are aggregated then into a single outgoing
   message from the cSplitter
   component.
