<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmominput · versión 8.0 -->
# tMomInput

Last updated: 9/30/2026

Fetches a message from a queue on a Message-Oriented Middleware (MOM) system and
passes it on to the next component.

tMomInput makes it possible to set up asynchronous communications via a
MOM server.

For further information, see [https://help.talend.com/r/en-US/8.0/studio-user-guide/messaging-brokers-supported-by-talend-messaging-components](/talend/r/en-US/8.0/studio-user-guide/messaging-brokers-supported-by-talend-messaging-components).

## tMomInput Standard properties

These properties are used to configure tMomInput running in the Standard Job framework.

The Standard
tMomInput component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Keep Listening | Select this check box to keep the MOM server listening for and fetching new messages.  This check box is not visible when ActiveMQ or WebSphere MQ is selected from the MQ server list and the receive number of messages check box is selected. |
| Sleeping time (in sec) | Specify the timeout interval (in seconds) within which the next message must be received.  This field is available in any one of the following situations:  * ActiveMQ is selected   from the MQ server list   and the Keep Listening   check box is cleared. * ActiveMQ is selected   from the MQ server list   and the receive number of   messages and Timeout for receiver check boxes are   selected. |
| receive number of messages | Select this check box to set the maximum number of messages that can be received.  This check box is available when ActiveMQ or WebSphere MQ is selected from the MQ server list and the Keep Listening check box is cleared. |
| maximum messages | Enter the maximum number of messages you can receive.  This field is available only when the receive number of messages check box is selected. |
| Timeout for receiver | Select this check box and specify the timeout interval for the receiver in the Sleeping time (in sec) field.  This check box is available only when the receive number of messages check box is selected. |
| Failover | Select this check box to use the ActiveMQ failover transport. For more information about the failover transport, see [Failover Transport Reference](http://activemq.apache.org/failover-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list and the Static Discovery check box is cleared. |
| Static Discovery | Select this check box to use the ActiveMQ static transport discovery mechanism. For more information about the static transport, see [Static Transport Reference](http://activemq.apache.org/static-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list and the Failover check box is cleared. |
| URI parameters | Enter the URI parameters.  This field is available only when the Failover or Static Discovery check box is selected. |
| MQ server | Select the type of the MQ server(s) to be connected from the list: ActiveMQ or WebSphere MQ. According to the server type selected, the parameters required differ slightly. |
| Use SSL Transport | Select this check box to use the ActiveMQ SSL transport. For more information about the SSL transport, see [SSL Transport Reference](http://activemq.apache.org/ssl-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list. |
| Host | Enter the host name or IP address of the MQ server. |
| Port | Enter the listening port of the MQ server. |
| Username and Password | Enter the user authentication credentials.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Channel | Specify the name of the channel through which the connection is established. The default value is *DC.SVRCONN*.  This field is available only when WebSphere MQ is selected from the MQ server list. |
| Message From | Type in the message source, exactly as expected by the server; this must include the type and name of the source. e.g.: queue/A or topic/testtopic  Note that the field is case-sensitive.  This field is available only when ActiveMQ is selected from the MQ Server list. |
| Message Type | Select the message type, either Topic or Queue.  This field is available only when ActiveMQ is selected from the MQ Server list. |
| Message Body Type | Select the message body type: Text Message, Bytes Message or Map Message. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields that will be processed and passed on to the next component.  In the context of tMomInput usage, the schema is comprised of two columns: From and Message, and the column names are read only. |
| QueueManager | Specify the name of the queue manager to which the connection is established.  This field is available only when WebSphere MQ is selected from the MQ server list. |
| MessageQueue | Enter the name of the message queue into which message queueing applications can put messages.  This field is available only when WebSphere MQ is selected from the MQ server list. |
| Is using message id to fetch | Select this check box to fetch messages according to their IDs.  This check box is available only when Text Message or Bytes Message is selected from the Message Body Type list. |
| Commit (delete message after read from the queue) | Select this check box to force a commit after reading each message from the queue.  This check box is available only when WebSphere MQ is selected from the MQ server list and the Browse message check box in the Advanced settings view is cleared. |
| Backout messages to input queue | Select this check box to put the message back into the queue after reading it.  This check box and the Browse message check box in the Advanced settings view enable you to read messages non-destructively from the queue. For further information, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>.  This check box is available only when WebSphere MQ is selected from the MQ server list and the Keep Listening, Commit (delete message after read from the queue) and Browse message check boxes are cleared. |
| Backout messages to backout queue (when backoutCount of message reach the threshold value) | Select this check box to backout the messages to the backout queue defined in the Websphere MQ manager when the backout count reaches the configured threshold which is a property of the queue in the Websphere MQ server.  This check box is available only when WebSphere MQ is selected from the MQ server list and the Keep Listening, Commit (delete message after read from the queue) and Browse message check boxes are cleared. |
| Set Transacted | Select this check box to transact the session. For further information about this parameter, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>.  Information noteNote: Selecting this check box will ignore the settings in the Acknowledgement Mode list in the Advanced settings view of tMomInput.  This check box is available only when ActiveMQ is selected from the MQ server list. |
| start server | Select this check box to force a start of the ActiveMQ server.  This check box is available only when ActiveMQ is selected from the MQ server list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional options | Define the additional transport options in the table. This table is available only if you select the Failover or Static Discovery check box in the Basic settings view.   * Option name: the name of the   option. * Option value: the value of the   option.   For example, enter *maxReconnectAttempts* in the Option name field and then *0* in the Option value field so that no attempt is made to retry the connection when no server is available for the failover mode.  For more information about the failover transport options, see [Failover Transport Reference](http://activemq.apache.org/failover-transport-reference.html).  For more information about the static discovery transport options, see [Static Transport Reference](http://activemq.apache.org/static-transport-reference.html). |
| Acknowledgement Mode | Select an acknowledgement mode from the list to indicate that the client will acknowledge any messages it receives:  Auto Acknowledge: With this acknowledgement mode, the client automatically acknowledges a message when it has either successfully returned from a call to receive,or the message listener it has called to process the message successfully returns.  Client Acknowledge: With this acknowledgement mode, the client acknowledges a message by calling a message's acknowledge method.  Dups OK Acknowledge: This acknowledgement mode instructs the session to lazily acknowledge the delivery of messages.  For further information about the usage of Jms headers, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>. Information noteNote: If the Set Transacted check box of tMomOutput is selected, Acknowledgement Mode will be ignored. This check box is enabled when the MQ server is ActiveMQ. |
| Get Jms Header | Select this check box to receive the Jms headers through the mapping from Jms fields onto MQ Series fields. When this check box is checked, you can specify the Jms header and the corresponding reference column name in the line(s) you added by clicking the plus button in the Parameters table. For further information about the usage of Jms headers, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>. Information noteNote: This check box is enabled when the MQ server is ActiveMQ. |
| Get Jms Properties | Select this check box to receive the Jms properties mapped to MQMD fields. When this check box is checked, you can specify the property name, the property type and the reference column name in the line(s) you added by clicking the plus button in the Parameters table. For further information about the usage of Jms properties, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>.  (Available when ActiveMQ is selected in the MQ Server list.) |
| Browse message | Select this check box to disable Commit (delete message after read from the queue) check box and Backout messages to input queue check box in the Basic settings view and open the queue to browse messages.  Information noteNote: This check box and the Backout messages to input queue check box in the Basic settings view enable you to read messages non-destructively from the queue. Browse message check box is visible only when the MQ server is WebSphere MQ with the Backout messages to input queue check box cleared. For further information, see <http://publib.boulder.ibm.com/infocenter/wmqv7/v7r0m0/index.jsp?topic=%2Fcom.ibm.mq.java.doc%2Fcom%2Fibm%2Fmq%2FMQC.html/>. |
| Get MQMD Fields | Select this check box to set one or more message descriptors by adding new fields for MQMD(message queuing message descriptor) in the Parameters table:  Field Name: Select one or more message descriptors from the list to retrieve header information of the message.  Reference Column Name: The header and properties information of the message.  For further information, see <http://publib.boulder.ibm.com/infocenter/wmqv7/v7r0m0/index.jsp?topic=%2Fcom.ibm.mq.csqzak.doc%2Ffr13040_.htm/>.  (Available when WebSphere MQ is selected in the MQ Server list.) |
| Include Header | Select this check box to specify the header of the message:  MQRFH2 fixed Portion: Select this check box and click the plus button to add one or more lines to specify the Version, Encoding, Format, Flags, NameValueCCSID and CodedCharSetId as needed for the fixed portion of MQRFH2 header.  MCD folder: Select this check box and click the plus button to add one or more lines to specify the fields and the reference column names for the properties that describe the format of the message.  JMS folder: Select this check box and click the plus button to add one or more lines to specify the fields and the reference column names for the transportation of JMS header fields and JMSX properties.  USR folder: Select this check box and click the plus button to add one or more lines to specify the fields and the reference column names for the transportation of application-defined properties associated with the message.  For further information about MQRFH2 header, see <http://publib.boulder.ibm.com/infocenter/wmbhelp/v6r1m0/index.jsp?topic=%2Fcom.ibm.etools.mft.doc%2Faq06920_.htm>.  Available when WebSphere MQ is selected in the MQ Server list. |
| Set Cipher Suite | Select this check box to enable the Cipher Suite list from which you can specify the Cipher Suite to be used with WebSphere MQ SSL.  For further information about Cipher Suite, see [CipherSpecs and their equivalent CipherSuites supported by IBM WebSphere MQ](https://www.ibm.com/support/knowledgecenter/SSFKSJ_7.1.0/com.ibm.mq.doc/ja34740_.htm) .  Available when WebSphere MQ is selected in the MQ Server list. |
| Custom Cipher Suite | Select this check box to allow you to custome Cipher Suite.  IBM Cipher Mappings: Use the IBM Java Cipher Suite to IBM MQ Cipher Spec Mappings.  Oracle Cipher Mappings: Use the Oracle Cipher Suite to IBM MQ Cipher Spec Mappings. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used as a start component. It must be linked to an output component. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your MQ Server connection dynamically from multiple connections planned in your Job.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Make sure the relevant ActiveMQ or Websphere MQ server is launched.  This component requires installation of its related jar files. |

**Related concepts**  

* [Asynchronous communication via a MOM server](tmomoutput-tmominput-tlogrow-trowgenerator-asynchronous-communication-via-mom-server-standard-component-this)
* [Transmitting XML files via a MOM server](tmomoutput-tmominput-tfileinputxml-tlogrow-transmitting-xml-files-via-mom-server-standard-component-this)
