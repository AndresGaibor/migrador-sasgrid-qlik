<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput · versión 8.0 -->
# tMomOutput

Last updated: 9/30/2026

Adds a message to a Message-Oriented Middleware system queue in order for it to be
fetched asynchronously.

tMomOutput makes it possible to set up asynchronous communications via a
MOM server.

For further information, see [https://help.talend.com/r/en-US/8.0/studio-user-guide/messaging-brokers-supported-by-talend-messaging-components](/talend/r/en-US/8.0/studio-user-guide/messaging-brokers-supported-by-talend-messaging-components).

## tMomOutput Standard properties

These properties are used to configure tMomOutput running in the
Standard Job framework.

The Standard
tMomOutput component belongs to the Internet
family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Failover | Select this check box to use the ActiveMQ failover transport. For more information about the failover transport, see [Failover Transport Reference](http://activemq.apache.org/failover-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list and the Static Discovery check box is cleared. |
| Static Discovery | Select this check box to use the ActiveMQ static transport discovery mechanism. For more information about the static transport, see [Static Transport Reference](http://activemq.apache.org/static-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list and the Failover check box is cleared. |
| URI parameters | Enter the URI parameters.  This field is available only when the Failover or Static Discovery check box is selected. |
| MQ Server | Select the type of the MQ server(s) to be connected from the list: ActiveMQ or WebSphere MQ. According to the server type selected, the parameters required differ slightly. |
| Use SSL Transport | Select this check box to use the ActiveMQ SSL transport. For more information about the SSL transport, see [SSL Transport Reference](http://activemq.apache.org/ssl-transport-reference.html).  This check box is available only when ActiveMQ is selected from the MQ server list. |
| Host | Enter the host name or IP address of the MQ server. |
| Port | Enter the listening port of the MQ server. |
| Username and Password | Enter the user authentication credentials.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Channel | Specify the name of the channel through which the connection is established. The default value is *DC.SVRCONN*.  This field is available only when WebSphere MQ is selected from the MQ server list. |
| To | Type in the message destination, respecting the syntax required by the server; this must include the type and name of the target folder, e.g.: queue/A or topic/testtopic. Note that this field is case-sensitive.  This field is available only when ActiveMQ is selected from the MQ Server list. |
| Message Type | Select the message type: either Topic or Queue.  This list is available only when ActiveMQ is selected from the MQ Server list. |
| Message Body Type | Select the message body type: Text Message, Bytes Message or Map Message. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields that will be processed and passed on to the next component.  In the context of tMomOutput usage, the schema is read-only but will change according to the incoming schema. Only one-column schema is expected by the server to contain the Messages. |
| QueueManager | Specify the name of the queue manager to which the connection is established.  This field is available only when WebSphere MQ is selected from the MQ server list. |
| MessageQueue | Enter the name of the message queue into which message queueing applications can put messages.  This field is available only when WebSphere MQ is selected from the MQ server list. |
| Set Transacted | Select this check box to transact the session. For further information about this parameter, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>.  Note that selecting this check box will ignore the settings in the Acknowledgement Mode list in the Advanced settings view of tMomInput. |
| Is using message id to set | Select this check box to set messages according to their ids.  This check box is available only when Text Message or Bytes Message is selected from the Message Body Type list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional options | Define the additional transport options in the table. This table is available only if you select the Failover or Static Discovery check box in the Basic settings view.   * Option name: the name of the   option. * Option value: the value of the   option.   For example, enter *maxReconnectAttempts* in the Option name field and then *0* in the Option value field so that no attempt is made to retry the connection when no server is available.  For more information about the failover transport options, see [Failover Transport Reference](http://activemq.apache.org/failover-transport-reference.html).  For more information about the static discovery transport options, see [Static Transport Reference](http://activemq.apache.org/static-transport-reference.html). |
| Delivery Mode | Select a delivery mode supported by JMS:  Not Persistent: This delivery mode does not require that the message be logged to stable storage.  Persistent: This delivery mode requires that the message be logged to stable storage as part of the client's send operation.  For further information about the delivery modes, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>.  (Available when ActiveMQ is selected in the MQ Server list.) |
| Set Jms Header | Select this check box to send the Jms headers through the mapping from Jms fields onto MQ Series fields on the MQ server. When this check box is checked, you can specify the header name and the header value in the line(s) you added by clicking the plus button in the Parameters table. For further information about the usage of Jms headers, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>.  (Available when ActiveMQ is selected in the MQ Server list.) |
| Set Jms Properties | Select this check box to send the Jms properties mapped onto MQMD fields on the MQ server. When this check box is checked, you can specify the property name, the property type and the property value in the line(s) you added by clicking the plus button in the Parameters table. For further information about the usage of Jms properties, see <https://publib.boulder.ibm.com/iseries/v5r2/ic2924/books/csqzaw07.pdf>.  (Available when ActiveMQ is selected in the MQ Server list.) |
| Use format | Select this check box to specify the WebSphere message format in the WebSphere Message Format field. The default format is *MQSTR*.  For further information about WebSphere message format, see <http://publib.boulder.ibm.com/infocenter/wtxdoc/v8r2m0/index.jsp?topic=/com.ibm.websphere.dtx.adapibmmq.doc/references/r_ibmmq_Message_Format_FORMAT.htm>.  (Available when WebSphere MQ is selected in the MQ Server list.) |
| Set MQMD Fields | Select this check box to enable the Parameters table in which you can specify the value of the MQMD fields.  This check box is available only when WebSphere MQ is selected from the MQ Server list. |
| Parameters | Specify the value of the MQMD fields.  * Field Name: Select an MQMD   field from the list. * Field Value: Enter the value of   the corresponding MQMD field.  This table is available only when the Set MQMD Fields check box is selected.  For more information about the MQMD fields, see [Fields for MQMD](http://www-01.ibm.com/support/knowledgecenter/SSFKSJ_7.0.1/com.ibm.mq.csqzak.doc/fr13050_.htm). |
| Include Header | Select this check box to specify the header of the message:  MQRFH2 fixed Portion: Select this check box and click the plus button to add one or more lines to specify the Version, Encoding, Format, Flags, NameValueCCSID and CodedCharSetId as needed for the fixed portion of MQRFH2 header.  MCD folder: Select this check box and click the plus button to add one or more lines to specify the field name and the value for the properties that describe the format of the message.  JMS folder: Select this check box and click the plus button to add one or more lines to specify the field name and the value for the transportation of JMS header fields and JMSX properties.  USR folder: Select this check box and click the plus button to add one or more lines to specify the field name and the value for the transportation of application-defined properties associated with the message.  For further information about MQRFH2 header, see <http://publib.boulder.ibm.com/infocenter/wmbhelp/v6r1m0/index.jsp?topic=%2Fcom.ibm.etools.mft.doc%2Faq06920_.htm>.  Available when WebSphere MQ is selected in the MQ Server list. |
| Set Cipher Suite | Select this check box to enable the Cipher Suite list from which you can specify the Cipher Suite to be used with WebSphere MQ SSL.  For further information about Cipher Suite, see [CipherSpecs and their equivalent CipherSuites supported by IBM WebSphere MQ](https://www.ibm.com/support/knowledgecenter/SSFKSJ_7.1.0/com.ibm.mq.doc/ja34740_.htm).  Available when WebSphere MQ is selected in the MQ Server list. |
| Custom Cipher Suite | Select this check box to allow you to custome Cipher Suite.  IBM Cipher Mappings: Use the IBM Java Cipher Suite to IBM MQ Cipher Spec Mappings.  Oracle Cipher Mappings: Use the Oracle Cipher Suite to IBM MQ Cipher Spec Mappings. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component must be linked to an input or intermediary component. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your MQ Server connection dynamically from multiple connections planned in your Job.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Make sure the relevant Websphere MQ or ActiveMQ server is launched.  This component requires installation of its related jar files. |

**Related concepts**  

* [Asynchronous communication via a MOM server](tmomoutput-tmominput-tlogrow-trowgenerator-asynchronous-communication-via-mom-server-standard-component-this)
* [Transmitting XML files via a MOM server](tmomoutput-tmominput-tfileinputxml-tlogrow-transmitting-xml-files-via-mom-server-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-transmitting-xml-files-via-mom-server-standard-component-this -->
# Transmitting XML files via a MOM server

Last updated: 9/30/2026

This scenario describes a five-component Job composed of two subJobs that sends
XML files from a local folder to a MOM queue, and then fetches the files from the MOM queue
and displays the contents of the files on the console.

### In this section

* [Dropping and links the components](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-dropping-and-links-components-standard-component-from)
* [Configuring the first subJob](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-first-subjob)
* [Configuring the second subJob](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-second-subjob-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tMomOutput](tmomoutput "Adds a message to a Message-Oriented Middleware system queue in order for it to be fetched asynchronously.")
* [tMomInput](tmominput "Fetches a message from a queue on a Message-Oriented Middleware (MOM) system and passes it on to the next component.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputXML](/talend/en-US/components/8.0/xml-connectors/tfileinputxml)
* [tFileList](/talend/en-US/components/8.0/tfilelist/tfilelist)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tlogrow-trowgenerator-asynchronous-communication-via-mom-server-standard-component-this -->
# Asynchronous communication via a MOM server

Last updated: 9/30/2026

This scenario is made of two Jobs. The first Job posts messages on a JBoss server
queue and the second Job fetches the message from the server.

### In this section

* [Configuring and executing the first Job](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tlogrow-trowgenerator-configuring-and-executing-first-job-standard-component-in)
* [Configuring and executing the second Job](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tlogrow-trowgenerator-configuring-and-executing-second-job-standard-component-then-se)

**Related reference**  

* [tMomOutput](tmomoutput "Adds a message to a Message-Oriented Middleware system queue in order for it to be fetched asynchronously.")
* [tMomInput](tmominput "Fetches a message from a queue on a Message-Oriented Middleware (MOM) system and passes it on to the next component.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-first-subjob -->
# Configuring the first subJob

Last updated: 9/30/2026

### In this section

* [Configuring the input components](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-input-components-standard-component)
* [Configuring the tMomOutput component](/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-tmomoutput-component-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-second-subjob-standard-component -->
# Configuring the second subJob

Last updated: 9/30/2026

## Procedure

1. Double-click the tMomInput component to
   open its Basic settings view.
2. Set the basic parameters of the component using the same settings you have
   done in the tMomOutput component, including
   the MQ server details, login authentication details, channel, message body
   type, queue manager and message queue.
3. Click the [...] button next to Edit schema to open the Schema dialog box.
4. From the Type list for the message column, select Document to handle XML format files, and then click
   OK to close the dialog box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-dropping-and-links-components-standard-component-from -->
# Dropping and links the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drop the following
   components one after another onto the design workspace: tFileList, tFileInputXML, tMomOutput,
   tMomInput, and tLogRow.
2. Connect tFileList to tFileInputXML using a Row > Iterate link, and
   connect tFileInputXML to tMomOutput using a Row > Main link to form the
   first subJob. This subJob will read each XML file in a given folder and send
   it to a MOM queue.
3. Connect tMomInput to tLogRow using a Row > Main link to form the
   second subJob. This subJob will fetch the XML files from MOM queue and
   display the file contents on the console.
4. Connect tFileInputXML to tMomInput using a Trigger > On Component Ok
   connection to link the two subJobs.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The XML files in the specified folder are written to the message queue and
   then retrieved from the queue. The contents of the files are displayed on
   the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tlogrow-trowgenerator-configuring-and-executing-first-job-standard-component-in -->
# Configuring and executing the first Job

Last updated: 9/30/2026

## About this task

In the first Job, a string message is created using a tRowGenerator and put on an ActiveMQ server using a tMomOutput. An intermediary tLogRow component displays the flow being passed.

## Procedure

1. Drop the three components required for the first Job from the Palette onto the design workspace and right-click
   to connect them using a Main row
   link.
2. Double-click on tRowGenerator to set the
   schema to be randomly generated.
3. Set just one column called *message*. This is the
   message to be put on the MOM queue.
4. This column is of String type and is
   nullable. To produce the data, use a preset function which concatenates
   randomly chosen ascii characters to form a 6-char string. This function is
   getAsciiRandomString. (Java version). Click the Preview
   button to view a random sample of data generated.
5. Set the Number of rows to be generated to
   *10*.

   Click OK to validate.
6. The tLogRow is only used to display a
   intermediary state of the data to be handled. In this example, it doesn't
   require any specific configuration.
7. Then select the tMomOutput
   component.
8. In this case, the MQ server to be used is
   ActiveMQ.

   In the Host and Port fields, and the Username
   and Password fields, fill in the relevant connection
   information.
9. Select the Message type from the list.
   The message can be of Queue or Topic type. In this example, select the Queue type from the list.
10. In the To field, type in the
    message source information strictly respecting the syntax expected by the server.
    This should match the Message Type you selected, such as: "queue/A". 

    Information noteNote: The message name is case-sensitive, therefore queue/A and Queue/A
    are different.
11. Then click Sync Columns to pass on the
    schema from the preceding component. The schema being read-only, it cannot
    be changed. The data posted onto the MQ comes from the first schema column
    encountered.
12. Press F6 to execute the Job and view the
    data flow being passed on in the console, thanks to the tLogRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tlogrow-trowgenerator-configuring-and-executing-second-job-standard-component-then-se -->
# Configuring and executing the second Job

Last updated: 9/30/2026

## About this task

Then set the second Job in order to fetch the queuing messages from the MOM
server.

## Procedure

1. Drop the tMomInput component and a
   tLogRow from the Palette to the design workspace.
2. Select the tMomInput to set the
   parameters.
3. Select the MQ server from the list. In
   this example, an ActiveMQ server is used.
4. Set the server Host and Port information.
5. Set the Message From and the Message Type to match the source and type
   expected by the messaging server.
6. The Schema is read-only and is made of
   two columns: From and Message.
7. Select the Keep listening check box and
   set the verification frequency to *5* seconds.

   Information noteNote: When using the Keep
   Listening option, you'll need to kill the Job to end it.
8. No need to change any default setting from the tLogRow.
9. Save the Job and run it (when launching for the first time or if you
   killed it on a previous run).

   The messages fetched on the server are displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-input-components-standard-component -->
# Configuring the input components

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileList component
   to open its Basic settings view.
2. In the Directory field, enter the
   path to the directory to read XML files from, or browse to the path by
   clicking the [...] button next to the
   field.
3. Select Use Glob Expressions as
   Filemask check box, add a new line in the Files field by clicking the [+] button, and enter "\*.xml" as
   the file mask so that all XML files in the directory will be used. Keep
   all the other settings as they are.
4. Double-click the tFileInputXML
   component to open its Basic settings
   view.
5. Click the [...] button next to
   Edit schema to open the Schema dialog box.
6. Click the [+] button to add a column,
   give it a name, *message* in this
   example, and select Document from the
   Type list to handle XML format
   files. Then, click OK to close the
   dialog box.
7. In the File name/Stream field, press
   Ctrl+Space to access the global
   variable list, and select tFileList\_1.CURRENT\_FILEPATH to
   loop on the context files' directory.
8. In in the Loop XPath query fields,
   enter "/" to define the root as the loop node of the input
   files' structure; in the Mapping table,
   fill the XPath query column with
   "." to extract all data from context node of the source
   files, and select the Get Nodes check
   box to build a Document type data flow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mom/tmomoutput-tmominput-tfileinputxml-tlogrow-configuring-tmomoutput-component-standard-component -->
# Configuring the tMomOutput component

Last updated: 9/30/2026

## Procedure

1. Double-click the tMomOutput component
   to open its Basic settings view.
2. Select WebSphere MQ from the
   MQ server list, and enter the host
   name or IP address of the MQ server and the port number.
3. Enter the login authentication information in the Username and Password fields, and enter the channel name of the
   transmission queue in the Channel
   field.
4. As we are handling file messages, select Text
   Message from the Message Body
   Type list.
5. Click Sync columns to retrieve the
   schema structure from the preceding component.
6. Fill in the queue manager and message queue details in the
   corresponding fields, and leave the other settings as they are.
