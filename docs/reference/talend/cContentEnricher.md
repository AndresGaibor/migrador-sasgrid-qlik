<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher · versión 8.0 -->
# cContentEnricher

Last updated: 9/30/2026

Uses a consumer or producer to obtain additional data, respectively intended for
event messaging and request/reply messaging.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cContentEnricher Standard properties

These properties are used to configure cContentEnricher running in the Standard Job framework.

The Standard
cContentEnricher component belongs to the Transformation family.

## Basic settings

| Properties | Description |
| --- | --- |
| Resource URI | This refers to the destination to which a message will be delivered if using a producer is selected; it refers to the source from which a message will be obtained if using a consumer is selected. |
| Using a producer | Select this check box to use a producer to provide additional data, that is to say sending a message to the defined URI. |
| Using a consumer | Select this check box to use a consumer to obtain additional data, that is to say requesting a message from the defined URI. |
| Use Aggregation Strategy | Select this check box to define the aggregation strategy for assembling the basic message and the additional data. |
| Specify timeout | This area appears when *Using a consumer* is selected. The timeout options are as follows:  Wait until a message arrive: the component keeps waiting for a message.  Immediately polls the message: the component immediately polls from the defined URI.  Waiting at most until the timeout triggers: select this check box to type in a timeout value in Millis. The component waits for the message only within the defined time period. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cContentEnricher allows you to use a consumer or producer to obtain additional data, respectively intended for event message messaging and request/reply messaging. |
| Limitation | n/a |

**Related concepts**  

* [Receiving messages from a list of URLs](ccontentenricher-csplitter-cjavadslprocessor-csetheader-receiving-messages-from-list-of-urls)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-receiving-messages-from-list-of-urls -->
# Receiving messages from a list of URLs

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, we will use the Camel component HTTP4 and the cContentEnricher component to retrieve messages from a list of URLs. To
do this, we need to build two sub-routes, one to read a file with a list of URLs and
send the messages to the local file system, the other to retrieve the messages on these
URLs.

In this use case, we will take a list of URLs on the local Tomcat server as the
example. So we need to start Apache Tomcat before executing the Route.

A TXT file URLlist is used to provide the list of URLs, as shown
below.

```
docs/introduction.html
docs/setup.html
```

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-viewing-code-and-executing-route)

**Related reference**  

* [cContentEnricher](ccontentenricher "Uses a consumer or producer to obtain additional data, respectively intended for event messaging and request/reply messaging.")

**Related information**  

* [cSplitter](/talend/en-US/mediation-components/8.0/mediation-splitter/csplitter)
* [cJavaDSLProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cjavadslprocessor)
* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cSetHeader](/talend/en-US/mediation-components/8.0/mediation-setheader/csetheader)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

Press Ctrl+S to save your Route.

### In this section

* [Configuring the first sub-route](/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-configuring-first-sub-route)
* [Configuring the second sub-route](/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-configuring-second-sub-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drag and drop a
   cSplitter, a cJavaDSLProcessor, a cContentEnricher, two cFile, two cMessagingEndpoint,
   and three cSetHeader components onto the
   design workspace.
2. Label the components properly for better identification of their roles and
   link them using the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code. 

   As shown above, a message route is built from the URLlist to
   the retrievedFiles via the .split,
   .log, .enrich, and .setHeader.
   The other message route is built from fetchURL to
   http4Endpoint via two .setHeader.
2. Press F6 to execute the Route. 

   RESULT: The split message is printed on the Run console.

   The messages from the list of URLs are saved in defined directory of the
   local file system.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-configuring-first-sub-route -->
# Configuring the first sub-route

Last updated: 9/30/2026

## Procedure

1. Double-click the URLlist component to
   display its Basic settings view in the
   Component tab.
2. In the Path field, browse to the file
   path where the URL list file is saved.

   In the FileName field, enter
   the filename `URLlist.txt`.
3. Double-click the cSplitter component to
   display its Basic settings view in the
   Component tab.
4. Select None in the Language list. In the Expression field, enter the code
   `body(String.class).tokenize("\r\n")` to split the message in
   each row into sub-messages.

   Information noteNote:

   This piece of code is for Windows only. For Unix, change it to
   `body(String.class).tokenize("\n")`, and for Mac,
   `body(String.class).tokenize("\r")`.
5. Double-click the cJavaDSLProcessor component to display its Basic settings view in the Component tab.
6. In the Code area, enter the code
   `.log("splitterOutput: ${body}")` to get the split message
   body.
7. Double-click the cContentEnricher component display its Basic settings view in the Component tab.
8. Select using a producer to use a producer
   to provide additional data and send the message to a defined URI.

   In the Resource URI field,
   enter `"direct:fetchURL"` where the message will be delivered.
9. Double-click the setFileName
   component to display its Basic settings
   view in the Component tab.
10. Click [+] to add a row to the Headers table.

    In the Name field, enter
    `org.apache.camel.Exchange.FILE_NAME` to define the file name
    for each incoming message.

    Select Simple in the Language list.

    In the Value field, enter
    `"${header.CamelHttpPath}"` to get the URI's path of the
    incoming message.
11. Double-click the retrievedFiles component
    to display its Basic settings view in the
    Component tab.
12. In the Path field, browse to the
    destination file path where you want the messages to be saved.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-content-enricher/ccontentenricher-csplitter-cjavadslprocessor-csetheader-configuring-second-sub-route -->
# Configuring the second sub-route

Last updated: 9/30/2026

## Procedure

1. Double-click the fetchURL component to
   display its Basic settings view in the
   Component tab.
2. In the URI field, enter
   `"direct:fetchURL"` that is defined in the cContentEnricher component.
3. Double-click the setURI
   component to display its Basic settings
   view in the Component tab.
4. Click [+] to add a row to the Headers table.

   In the Name field, enter
   `org.apache.camel.Exchange.HTTP_URI` to define the HTTP URI
   of each message.

   Select Simple in the Language list.

   In the Value field, enter
   `"http://localhost:8080"` of the local Tomcat server.
5. Double-click the setPATH
   component to display its Basic settings
   view in the Component tab.
6. Click [+] to add a row to the Headers table.

   In the Name field, enter
   `org.apache.camel.Exchange.HTTP_PATH` to define the HTTP path
   of each message.

   Select Simple in the Language list.

   In the Value field, enter
   `"${body}"` that is split from the original message.
7. Double-click the http4Endpoint component
   to display its Basic settings view in the
   Component tab.
8. In the URI field, enter
   `"http4:localhost:8080"` to consuming HTTP resources on the
   local Tomcat server.
9. Click the Advanced settings
   view. Click  at the bottom of the Dependencies list to add a row and select
   http4 from the drop-down list. For more information about
   HTTP4, see <http://camel.apache.org/http4.html>.
