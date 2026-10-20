<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter · versión 8.0 -->
# cMessageRouter

Last updated: 9/30/2026

Creates different channels for each filtered message type according to specified
conditions so that messages can later on be treated more accurately in each new
channel.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cMessageRouter Standard properties

These properties are used to configure cMessageRouter running in the Standard Job framework.

The Standard
cMessageRouter component belongs to the Routing family.

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cMessageRouter is used as a middle component in a Route. It can only have one input channel but multiple output channels. Messages can be outputted through either a When, Otherwise or Route types of connection. |
| Connections | * Row / Route: Select this link to pass on all   the messages to the next component. * Trigger / When: Select the   When link and click the   Component view.  In the Type list, select the type of language you will   use to declare your condition from none,   bean, constant,   correlation, el,   groovy, header,   sql, jsonpath,   jxpath, mvel,   ognl, php,   property, python,   ruby, simple,   Spel, sql,   xpath, and xquery.  Append endChoice(): If the When   link is followed by a cMessageFilter or   cLoadBalancer and so on, there will be a compile   error. This is because once there is such a component there, the flow type will   change from choice() to loadbalance(), which can not be followed by a   When or Otherwise link. Select   this check box to change the flow type back from loadbalance() to choice().  In the Condition field, type in the condition that will   be used to filter the messages.  All the messages that do not match this condition are retrieved with the   Otherwise link to a different channel or dropped if   an Otherwise link does not present.  Information noteNote: There can be more than one When link in a Route. * Trigger / Otherwise: This link   automatically retrieves the messages that do not match the   When conditions.  Information noteNote: There can be only one Otherwise link, which is   optional, in a Route. |
| Limitation | It is recommended not to put any message handling after the When or the Otherwise link. Always use a Mock/Direct endpoint to replace them and make a new Route to handle the messages. |

**Related concepts**  

* [Routing messages according to a criterion](cmessagerouter-cmessagingendpoint-cfile-clog-routing-messages-according-to-criterion)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter-cmessagingendpoint-cfile-clog-routing-messages-according-to-criterion -->
# Routing messages according to a criterion

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this use case, we route XML messages that are sent from the sending endpoint according to a defined criterion: those XML files in which the value of the *city* node is *Paris* are sent to a folder named *Paris\_only*, and other messages are sent to a folder named *Other\_cities*.

Of
the four XML files used in this scenario, *Message\_1.xml* and *Message\_4.xml*
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

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter-cmessagingendpoint-cfile-clog-dropping-and-linking-components)
* [Configuring the components and connections](/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter-cmessagingendpoint-cfile-clog-configuring-components-and-connections)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter-cmessagingendpoint-cfile-clog-viewing-code-and-executing-route)

**Related reference**  

* [cMessageRouter](cmessagerouter "Creates different channels for each filtered message type according to specified conditions so that messages can later on be treated more accurately in each new channel.")

**Related information**  

* [cFile](/talend/en-US/mediation-components/8.0/mediation-file/cfile)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter-cmessagingendpoint-cfile-clog-configuring-components-and-connections -->
# Configuring the components and connections

Last updated: 9/30/2026

## About this task

The cMessageRouter component does not have any
property as it filters and routes the messages from one endpoint to others based on
the conditions set in its When
connection(s).

## Procedure

1. Double-click the cFile component labeled
   *Sender* to open its Basic settings view in the Component tab.
2. In the Path field, specify the file path to message source.

   From the Encoding list, select the encoding type of your message files. Leave the other parameters as they are.
3. In the design workspace, click the When
   connection you created and click the Component view to define a filter against which messages
   will be routed.
4. In the Type list, select xpath because the format of the messages used is XML.

   In the Condition field, type in "/person[city='Paris']" to retrieve only those messages in which the value of the *city* node is *Paris*.
5. Double-click the cMessagingEndpoint component labeled *directParis* to open its Basic settings view in the Component tab.
6. In the URI field, enter the endpoint URI, for example, *"direct:Paris"* to receive the filtered message.
7. Repeat these steps to set the endpoint URI of the cMessagingEndpoint components labeled *directOthers* as *"direct:Others"*. Set the endpoint URIs of the cMessagingEndpoint components labeled *directParisRoute* and *directOthersRoute* as *"direct:Paris"* and *"direct:Others"* respectively.
8. Double-click the cFile component labeled *Receiver\_Paris* to open its Basic settings view in the Component tab, and specify the path for the messages meeting the filter criterion in the Path field. 

   Repeat this step to define the path for all the other messages from the sender in the cFile component labeled *Receiver\_Others*.
9. Double-click the cLog component labeled *Monitor\_Paris* to open its Basic settings view in the Component tab.
10. Select INFO in the Level list. Select the Specify output log message option and enter the following code in the Message field to display the filename of the message sent to the specified directory.

    ```
    Message sent to folder Paris_only: ${header.CamelFileNameOnly}
    ```

    Repeat this step to customize the message in the cLog component labeled *Monitor\_Others* to display the filename of the message sent to the specified directory.
11. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter-cmessagingendpoint-cfile-clog-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Connectivity folder of the Palette, drop three cFile and four cMessagingEndpoint components onto the design workspace, and
   label them *Sender*, *Receiver\_Paris*, and *Receiver\_Others*, *directParis*, *directOthers*, *directParisRoute*, and *directOthersRoute* respectively to better identify their
   roles.
2. From the Routing folder, drop a cMessageRouter component onto the design
   workspace, and label it *Message\_router*.
3. From the Miscellaneous folder, drop two cLog components onto the design workspace, and label them *Monitor\_Paris* and *Monitor\_Others* respectively.
4. Right-click the cFile component labeled
   *Sender*, select Row > Route from the
   contextual menu and click the cMessageRouter component.
5. Right-click the cMessageRouter component, select Trigger > When from the contextual menu and click the cMessagingEndpoint component labeled *directParis*. This endpoint will retrieve the messages that meet the defined criterion.
6. Right-click the cMessageRouter component, select Trigger > Otherwise from the contextual menu and click the cMessagingEndpoint component labeled *directOthers*. This endpoint will collect all the messages that do not meet the filter criterion.
7. Right-click the cMessagingEndpoint component labeled *directParis*, select Row > Route from the contextual menu and click the cFile component labeled *Receiver\_Paris*. Repeat this operation to link the component labeled *Receiver\_Paris* to *Monitor\_Paris*, *directOthersRoute* to *Receiver\_Others*, and *Receiver\_Others* to *Monitor\_Others* respectively using the Row > Route connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-filter/cmessagerouter-cmessagingendpoint-cfile-clog-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, the messages are routed according to conditions initialized with the .choice() piece of code. The filter you defined is initialized with the .when() piece of code, and the non filtered messages are routed through the .otherwise() piece of code.
2. Click the Run button in the Run view or press F6 to execute your Route. 

   RESULT: The files containing "*Paris*" are sent to a folder named *Paris\_only*, and the other messages are sent in a folder called *Other\_cities*.
