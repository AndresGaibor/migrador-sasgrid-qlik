<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate · versión 8.0 -->
# cAggregate

Last updated: 9/30/2026

Combines a number of messages together into a single message.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cAggregate Standard properties

These properties are used to configure cAggregate running in the Standard Job framework.

The Standard
cAggregate component belongs to the Routing family.

## Basic settings

| Properties | Description |
| --- | --- |
| Language | Select the language of the expression you want to use to filter your messages, from None, Bean, CONSTANT, ESBCorrelationID, EL, GROOVY, HEADER, JoSQL, JSonPath, JXPATH, MVEL, OGNL, PHP, PROPERTY, PYTHON, RUBY, SIMPLE, SpEL, SQL, XPATH, and XQUERY.  Select CorrelationID to use the existing correlation ID of the message as the correlation key if the correlation ID is available in the closest cSOAP connected to this component. For more information about the cSOAP component, see [cSOAP](/talend/en-US/components/8.0/mediation-apache-cxf/csoap). |
| Correlation expression/Expression | Type in the expression that evaluates the correlation key to be used for the aggregation.  This field disappears when CorrelationID is selected in the Language list. In this case, the existing correlation ID from the closest cSOAP connected to this component will be used. For more information about the cSOAP component, see [cSOAP](/talend/en-US/components/8.0/mediation-apache-cxf/csoap). |
| Correlation expression/Add Namespaces | This option appears when XPath is selected in the Language list.  Select this check box to add namespaces for the Xpath expression. Click [+] to add as many namespaces as required to the table and define the prefix and URI in the corresponding columns. |
| Strategy | Specify a Java bean to use as the aggregation strategy or select a predefined aggregation strategy.  * UseOriginalAggregationStrategy: Use the original   exchange. * UseLatestAggregationStrategy: Use the latest   exchange. * GroupedMessageAggregationStrategy: Aggregate all   messages into a single combined exchange holding all the aggregated messages   in a list of messages as the message body. * GroupedExchangeAggregationStrategy: Aggregate all   exchanges into a single combined exchange holding all the aggregated   exchanges in a list of exchanges as the message body. * GroupedBodyAggregationStrategy: Aggregate body of   input messages into a single combined exchange holding all the aggregated   bodies in a list of objects as the message body.   Information noteNote: The predefined aggregation strategies are available only if you have installed the R2024-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Completion conditions/Number of messages | Select this check box to specify the number of messages to aggregate per batch before the aggregation is complete.  Information noteNote: By default, this check box is selected and the number of messages is set to *3*. If you clear this check box, and at least one of the other four completion conditions is met, all the messages retrieved will be aggregated in one batch. |
| Completion conditions/Inactivity timeout (in milliseconds) | Select this check box to specify the time (in milliseconds) that an aggregated exchange should be inactive before it is complete. This option can be set as either a fixed value or using an Expression which allows you to evaluate a timeout dynamically.  Information noteNote: You can not use this option together with Scheduled interval. Only one of them can be used at a time. |
| Completion conditions/Scheduled interval (in milliseconds) | Select this check box to specify a repeating period (in milliseconds) by which the aggregator will complete all current aggregated exchanges.  Information noteNote: You cannot use this option together with Inactivity timeout. Only one of them can be used at a time. |
| Completion conditions/Predicate matched | Select this check box to specify a predicate to indicate when an aggregated exchange is complete. |
| Completion conditions/Batch consumer | Select this check box to aggregate all files consumed from a file endpoint in a given poll. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Check completion before aggregating | Select this check box to check for completion when a new incoming exchange has been received. This option influences the behavior of the Predicate matched option as the exchange being passed in changes accordingly. When this option is disabled, the exchange passed in the predicate is the *aggregated* exchange which means any information you may store on the aggregated exchange from the aggregation strategy is available for the predicate. When this option is enabled, the exchange passed in the predicate is the *incoming* exchange, which means you can access data from the incoming exchange. |
| Close correlation group | Select this check box to indicate that if a correlation key has already been completed, then any new exchanges with the same correlation key will be denied. When using this option, enter a number in the Maximum bound field to keep that last number of closed correlation keys. |
| Ignore invalid correlation key | Select this check box to ignore the invalid correlation key which could not be evaluated to a value. By default Camel will throw an Exception on encountering an invalid correlation key. |
| Group arriving exchange | Select this check box to group all aggregated exchanges into a single combined holder class that holds all the aggregated exchanges. As a result only one exchange is being sent out from the aggregator. This option can be used to combine many incoming exchanges into a single output exchange. |
| Use persistence | Select this check box to plug in your own implementation of the repository which keeps track of the current in-flight aggregated exchanges. By default, Camel uses a memory based implementation. |
| Repository | This field appears when the Use persistence check box is selected. The repository is AggregationRepository or RecoverableAggregationRepository.  AggregationRepository: The default repository used by Camel which is a memory based implementation. Enter the name of the repository in the field.  RecoverableAggregationRepository: RecoverableAggregationRepository is a JDBC based AggregationRepository which persists the aggregated messages on the fly. This ensures that you will not loose messages. Enter the name of the repository in the field.  With this repository selected, the following options appear:  Recovery/Use recovery: Select this check box to recover failed aggregated exchanges and have them resubmitted automatically. In the Recovery interval field, enter the interval (in milliseconds) to scan for failed exchanges to recover and resubmit. By default this interval is 5000 milliseconds. In the Dead letter channel field, enter an endpoint URI for a Dead Letter Channel where exhausted recovered exchanges will be moved. In the Maximum redeliveries field, enter the maximum number of redelivery attempts for a given recovered exchange. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAggregate is used as a middle or end component in a Route. |
| Connections | Aggregate: select this link to route messages to the next endpoint according to the selected aggregation strategy.  Route: select this link to route all the messages from the sender to the next endpoint. |

**Related concepts**  

* [Aggregating three messages into one](caggregate-cprocessor-cfile-cfile-aggregating-three-messages-into-one)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-aggregating-three-messages-into-one -->
# Aggregating three messages into one

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, the cAggregate component combines
three messages from the local file system into one and prints the messages in the
console. A Java bean will be used as the aggregation strategy.

### In this section

* [Creating a Java bean as the aggregation strategy](/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-creating-java-bean-as-aggregation-strategy)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-viewing-code-and-executing-route)

**Related reference**  

* [cAggregate](caggregate "Combines a number of messages together into a single message.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cFile component,
   which is labeled `File_source`, to display its Basic settings view in the Component tab.
2. In the Path field, browse to or enter the
   input file path, and leave the other parameters as they are. 

   In this scenario, there are four text files in the specified
   directory: a.txt, b.txt,
   c.txt and d.txt, the contents of which
   are This is a!, This is b!, This is
   c!, and This is d! respectively.
3. Double-click the cAggregate
   component, which is labeled `Aggregator`, to display its
   Basic settings view in the Component tab.
4. In the Language field, select Constant or Simple as the expression language.

   In the Expression field, enter the
   expression `"getBody(String.class)"` to retrieve the body of the
   message.

   In the Strategy field, enter the
   name of the Java bean `AggregateBody` you just created.

   Select the Number of messages check
   box and type in `2` in the field.
5. Double-click the cProcessor
   component labeled `Monitor_before` to display its Basic settings view in the Component tab.
6. In the Code box, customize the code as
   follows so that the Run console displays
   the message contents before an aggregation takes place:

   ```
   System.out.println("Before aggregation: "+
   exchange.getIn().getBody(String.class));
   ```
7. In the same way, configure the cProcessor component labeled `Monitor_after` so
   that the Run console displays the message contents after an aggregation takes place: 

   ```
   System.out.println("After aggregation: "+
   exchange.getIn().getBody(String.class));
   ```
8. Press Ctrl+S to save your
   Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-creating-java-bean-as-aggregation-strategy -->
# Creating a Java bean as the aggregation strategy

Last updated: 9/30/2026

## About this task

To aggregate the messages, we will use a Java bean that will help us build an
aggregation strategy.

## Procedure

1. From the repository tree view, expand the Code node and right click the Beans node. In the contextual menu, select Create Bean.
2. The New Bean wizard opens. In the Name field, type in a name for the bean, for
   example, *AggregateBody*. Click Finish to close the wizard.
3. Type in the codes as shown in the figure below. In this use case, we just
   want to aggregate all messages into a single message.

   ```
   package beans;

   import org.apache.camel.Exchange;
   import org.apache.camel.AggregationStrategy;

   public class AggregateBody implements AggregationStrategy{

   	public Exchange aggregate(Exchange oldEx, Exchange newEx) {
   		if(oldEx==null){
   			return newEx;
   		}
   		String oldBody = oldEx.getIn().getBody(String.class);
   		String newBody = newEx.getIn().getBody(String.class);
   		newEx.getIn().setBody(oldBody+newBody);
   		return newEx;
   	}
   }
   ```
4. Press Ctrl+S to save your bean.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, expand the Connectivity folder, and drop a cFile component onto the design workspace.
2. Expand the Routing folder, and drop a
   cAggregate component onto the design
   workspace.
3. Expand the Custom folder, and drop two cProcessor components onto the design
   workspace.
4. Right-click the cFile component, select
   Row > Route from the contextual menu and click the first cProcessor component.
5. Repeat this operation to connect the first cProcessor component to the cAggregate component.
6. Right-click the cAggregate component,
   select Row > Aggregate from the contextual menu and click the second
   cProcessor component.
7. Label all the components to better identify their functionality, as shown
   above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-aggregate/caggregate-cprocessor-cfile-cfile-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, a message from the
   File\_source endpoint is routed via
   cProcessor\_1 and then aggregated according to the condition
   .aggregate.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your route. You can also press F6 to execute it. 

   RESULT: The four messages are aggregated in two batches, two messages
   combined into one each batch.
