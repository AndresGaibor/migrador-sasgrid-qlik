<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jms/tmessaginginput · versión 8.0 -->
# tMessagingInput

Last updated: 9/30/2026

Fetches messages from a queue on a Message-Oriented middleware (MOM) system and
passes the messages on to the next component.

The tMessagingInput component makes it possible to set up asynchronous
communications via a MOM server.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

Information noteNote: This component is available only when you have installed the 8.0.1-R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## tMessagingInput Standard properties

These properties are used to configure tMessagingInput
running in the Standard Job framework.

The Standard
tMessagingInput component belongs to the Messaging family.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.  * Built-In: No property data stored centrally. * Repository: Select the repository file in which the   properties are stored. The database connection related fields that follow   are completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| JMS Provider | Select the type of the MQ server(s) to be connected from the drop-down list: ActiveMQ (JMS v1), ActiveMQ Artemis (JMS v2), or WebSphere MQ. |
| Server URL | Enter the URL of the MQ server. MQ server URL needs to be in specific format. That is, `tcp://localhost:61616` (for ActiveMQ and ActiveMQ Artemis MQ servers) or `localhost(1414)` (for WebSphere MQ servers), as prompted in the field. |
| Use Specified User Identity | If you have to log in, select the check box and type in your username and password in the corresponding fields. To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. |
| Durable subscription | Select this check box to enable the durable subscription.  * Client ID: enter the client ID for the durable   subscription. * Subscriber name: enter the subscriber name for the   durable subscription. |
| Destination type | Select the message type, either: Topic or Queue. |
| Destination | Type in the message source (a queue name or a topic name), exactly as expected by the server; this must include the type and name of the source. For example, `queue/A` or `topic/testtopic`. Note that this field is case-sensitive. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to have the component generating the schema according to the settings provided. |
| Message selector | Enter an expression to filter the messages received. You can use JMS properties or JMS header fields in the expression. See [Producer](https://doc.akka.io/docs/alpakka/current/jms/producer.html) for information about JMS properties and JMS header fields. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Max records | Specify the maximum number of messages to received. A value of `-1` does not limit the number of received messages. |
| Max duration time (ms) | Specify the maximum duration time for receiving messages in milliseconds. A value of `-1` specifies to receive messages permanently. |
| Acknowledge mode | Select the acknowledge mode from the drop-down list: Auto acknowledge, Client acknowledge, DUPS ok acknowledge, Session/Transaction, or Do not acknowledge. |
| Advanced context properties | Set other properties as needed. To set a property in this table, click the plus button underneath the table to add a line, enter the property name in the Key column and enter the value in the Value column. This table supports global variables and context variables. Refer to [Configure JMS producers](https://doc.akka.io/docs/alpakka/current/jms/producer.html) for information about properties of ActiveMQ and ActiveMQ Artemis MQ servers; refer to [WebSphere MQ connector properties](https://www.ibm.com/docs/en/iis/11.5?topic=connector-websphere-mq-properties) for information about properties of WebSphere MQ servers. Information noteNote: If you are using a WebSphere MQ JMS provider, you need to set the mandatory properties (that is, CHANNEL and QUEUE\_MANAGER) in this table. |
| Allow JMS properties | Select this option to have the JMSProperties column added in the schema when you click Guess schema button in the Basic settings view, so as to retrieve JMS properties as well. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used as an input component. It must be linked to an output component. |
| Limitations | * This component supports ActiveMQ (JMS v1), ActiveMQ Artemis (JMS v2), and WebSphere MQ servers. * This component only supports TextMessage objects. |
