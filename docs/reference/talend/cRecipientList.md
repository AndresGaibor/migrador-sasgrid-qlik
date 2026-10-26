<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist · versión 8.0 -->
# cRecipientList

Last updated: 9/30/2026

Routes messages to a number of dynamically specified recipients.

cRecipientList can also process the message before
sending it to the recipients and assemble the replies from the sub-messages into a
single outgoing message.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cRecipientList Standard properties

These properties are used to configure cRecipientList running in the Standard Job framework.

The Standard
cRecipientList component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Language | Select the expression language from None, Bean, Constant, CorrelationID, EL, Groovy, Header, JoSQL, JSonPath, JXPath, MVEL, OGNL, PHP, Property, Python, Ruby, Simple, SpEL, SQL, XPath, and XQuery.  For more information about how to use the languages to create an expression, see the site <http://camel.apache.org/languages.html>. |
| Expression | Type in the expression that returns multiple endpoints. |
| Use Result Class Type | This option appears when XPath is selected in the Language list. Select this check box to set the result type of the sub-messages in the field that appears. |
| Add Namespaces | This option appears when XPath is selected in the Language list.  Select this check box to add namespaces for the Xpath expression. Click [+] to add as many namespaces as required to the table and define the prefix and URI in the corresponding columns. |
| Use Delimiter | Select this check box to customize the separator for the Expression. Enter the characters, strings or regular expressions to be used as the separator in the Delimiter field. |
| Use Strategy | Select this check box to refer to an aggregation strategy to assemble the replies from the sub-messages into a single outgoing message from the recipient list. Enter the ID of the aggregation strategy in the field or select a predefined aggregation strategy.  * UseOriginalAggregationStrategy: Use the original   exchange. * UseLatestAggregationStrategy: Use the latest   exchange. * GroupedMessageAggregationStrategy: Aggregate all   messages into a single combined exchange holding all the aggregated messages   in a list of messages as the message body. * GroupedExchangeAggregationStrategy: Aggregate all   exchanges into a single combined exchange holding all the aggregated   exchanges in a list of exchanges as the message body. * GroupedBodyAggregationStrategy: Aggregate body of   input messages into a single combined exchange holding all the aggregated   bodies in a list of objects as the message body.   Information noteNote: The predefined aggregation strategies are available only if you have installed the R2024-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Parallel Processing | Select this check box to send the message to the recipients simultaneously. |
| Use ExecutorService | This option appears when Parallel Processing is enabled. Select this check box to use a custom thread pool for parallel processing. Specify the thread pool in the ExecutorService field. |
| Stop On Exception | Select this check box to stop processing immediately when an exception occurred. |
| Ignore Invalid Endpoints | Select this check box to ignore invalid endpoints. |
| Streaming | Select this check box to process the sub-message replies in the order that the replies are received from each recipient. If this option is disabled, the replies will be processed in the same order as specified by the Expression. |
| Timeout | Specify a total timeout in millisecond. If the message is not routed to the recipients and processed within the given time frame, the timeout triggers and the recipient list breaks out. |
| Use On-Prepare Processor | Select this check box to use a custom processor to prepare the copy of the exchange that each recipient will receive. Enter the ID of the processor in the next field. You can use the cBeanRegister to register a Java bean as a processor. |
| Share Unit of Work | Select this check box to share the unit of work between the parent exchange and each recipient exchange. See the same option of cSplitter for more information. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cRecipientList is used as a middle component in a Route. |
| Limitation | n/a |

**Related concepts**  

* [Routing a message to multiple recipients](crecipientlist-csetheader-cfile-cprocessor-routing-message-to-multiple-recipients)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist-csetheader-cfile-cprocessor-routing-message-to-multiple-recipients -->
# Routing a message to multiple recipients

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cRecipientList component is used
to route a message to a list of recipients.

To build the Route, do the following.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist-csetheader-cfile-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist-csetheader-cfile-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist-csetheader-cfile-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cRecipientList](crecipientlist "Routes messages to a number of dynamically specified recipients.")

**Related information**  

* [cSetHeader](/talend/en-US/components/8.0/mediation-setheader/csetheader)
* [cFile](/talend/en-US/components/8.0/mediation-file/cfile)
* [cMessagingEndpoint](/talend/en-US/components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cProcessor](/talend/en-US/components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist-csetheader-cfile-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click cFile to open its Basic settings view in the Component tab.
2. In the Path field, type in the
   path to the source message, for example, `"E:/data/input"`. Keep
   other default settings unchanged.
3. Double-click cSetHeader to open its
   Basic settings view in the Component tab.
4. Click [+]  to add a row to the Headers table.

   In the Name field, enter the
   header name, for example, `"ListOfRecipients"`.

   In the Language list, select *Constant*.

   In the Value field, enter the
   endpoint URIs, for example, `"direct:a,direct:b"`.
5. Double-click cRecipientList to open its
   Basic settings view in the Component tab.
6. In the Language list, select Header. 

   In the Expression field,
   enter the name of the header that contains the recipients list, that is,
   `"ListOfRecipients"`.
7. Double-click Recipient\_A to open its
   Basic settings view in the Component tab and define the URI of recipient
   A.

   Perform the same operation to Recipient\_B to define the URI of recipient B.
8. Double-click Print\_File\_Name\_A to open
   its Basic settings view in the Component tab and enter the code below to print
   out the message received by Recipient\_A.System.out.println("Recipient\_a just downloaded:"+exchange.getIn().getHeader("CamelFileName"));

   Perform the same operation to Print\_File\_Name\_B and type in the code below in its code
   box:

   ```
   System.out.println("Recipient_b just downloaded:"+exchange.getIn().getHeader("CamelFileName"));
   ```
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist-csetheader-cfile-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drag and drop the components from the Palette onto the workspace: cFile, cSetHeader,
   cRecipientList, two cMessagingEndpoint and two cProcessor. Change the label of the cFile component to Read\_Input. Change the labels of the two cMessagingEndpoint components to Recipient\_A and Recipient\_B. Change the labels of the two cProcessor components to Print\_File\_Name\_A and Print\_File\_Name\_B.
2. Link Read\_Input to cSetHeader using a Row >
   Route connection.
3. Link cSetHeader to cRecipientList using a Row
   > Route connection.
4. Link Recipient\_A to Print\_File\_Name\_A using a Row > Route
   connection.
5. Link Recipient\_B to Print\_File\_Name\_B using a Row > Route
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-recipient-list/crecipientlist-csetheader-cfile-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the Route gets the message from Read\_Input\_cFile\_1, and .setHeader("ListOfRecipients") using .constant("direct:a,direct:b"). Then, cRecipientList\_1 reads .header("ListOfRecipients") and routes the message to the recipients
   included in it.
2. Press F6 to execute the Route.

   The message is sent to recipients included in the header.
