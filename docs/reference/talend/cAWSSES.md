<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses · versión 8.0 -->
# cAWSSES

Last updated: 9/30/2026

Sends emails with Amazon's Simple Email Service (SES).

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cAWSSES Standard properties

These properties are used to configure cAWSSES running in the Standard Job framework.

The Standard
cAWSSES component belongs to the AWS and Connectivity families.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select an AWS connection component from the list to reuse the connection details you already defined. |
| Subject | Specify the email subject. It can be overriden by the CamelAwsSesSubject header. |
| From | Specify the sender's email address. It can be overriden by the CamelAwsSesFrom header. |
| To | Specify one or more destination email addresses. It can be overriden by the CamelAwsSesTo header. |
| Return Path | Specify the email address to which bounce notifications are to be forwarded. It can be overriden by the CamelAwsSesReturnPath header. |
| Reply to Addresses | Specify the reply-to email address(es) for the message. It can be overriden by the CamelAwsSesReplyToAddresses header. |
| Message Headers | Set the message headers in the corresponding table. Click [+] as many times as required to add message headers to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/aws-ses.html> for available headers. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/aws-ses.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAWSSES can be a start, middle or end component in a Route. It has to be used with the cAWSConnection component, which creates a connection to Amazon Web Services. For more information about cAWSConnection, see [cAWSConnection](/talend/en-US/components/8.0/mediation-amazon-s3/cawsconnection). |
| Limitation | n/a |

**Related concepts**  

* [Sending Email using the cAWSSES component](cawsses-cawsconnection-ctimer-cprocessor-sending-email-using-cawsses-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses-cawsconnection-ctimer-cprocessor-sending-email-using-cawsses-component -->
# Sending Email using the cAWSSES component

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario will show you how to use the cAWSSES
component to send emails with Amazon's SES service.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses-cawsconnection-ctimer-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses-cawsconnection-ctimer-cprocessor-configuring-components)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses-cawsconnection-ctimer-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cAWSSES](cawsses "Sends emails with Amazon's Simple Email Service (SES).")
* [cAWSConnection](cawsconnection "Establishes a connection to Amazon Web Services for data storage and retrieval.")

**Related information**  

* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses-cawsconnection-ctimer-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cAWSConnection component to display its
   Basic settings view in the Component tab.
2. In the Access Key and Secret Key fields, enter the authentication credentials.
3. Double-click the cTimer component to open its
   Basic settings view in the Component tab.
4. In the Repeat field, enter
   `1` to generate the message exchange one time. Keep the
   default settings of the other options.
5. Double-click the cSetBody component to open
   its Basic settings view in the Component tab.
6. Select CONSTANT from the
   Language drop-down list and type in
   `"Hello world"` in the Expression field as the message body.
7. Double-click the cAWSSES component to open its Basic settings view in the Component tab.
8. In the Connection list, select the cAWSConnection component that you have just
   configured to connect to Amazon SES service. 

   In the Subject field, enter the
   email subject, for example, `"Hello"` in this use case.

   In the From and To fields, enter the sender's email address and the destination
   email address respectively.

   In the Return Path field, enter the email
   address to which bounce notifications are to be forwarded.

   In the Reply To field, enter the email address to receive
   replies.
9. Double-click the cProcessor component to
   display its Basic settings view in the
   Component tab.
10. In the Code box, enter the following code to
    print the CamelAwsSesMessageId in the execution
    console:System.out.println("CamelAwsSesMessageId: "+exchange.getIn().getHeader("CamelAwsSesMessageId"));
11. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses-cawsconnection-ctimer-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a cAWSConnection, a cTimer, a
   cSetBody, a cAWSSES, and a cProcessor
   component onto the design workspace.
2. Label the components for better identification of their roles and link them
   with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-ses/cawsses-cawsconnection-ctimer-cprocessor-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message flow from sesproducer\_cTimer\_1 is
   given a payload by sesproducer\_cSetBody\_1. Then it is sent to
   sesproducer\_cAWSSES\_1 and processed by
   sesproducer\_cProcessor\_1.
2. Press F6 to execute the Route. The logs of
   the message exchange are printed in the console.
3. An email is sent to the destination address.
4. When replying the email, the destination is the email address specified in the To field of the cAWSSES component.
