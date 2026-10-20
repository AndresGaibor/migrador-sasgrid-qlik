<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns · versión 8.0 -->
# cAWSSNS

Last updated: 9/30/2026

Sends messages to an Amazon's Simple Notification topic.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cAWSSNS Standard properties

These properties are used to configure cAWSSNS running in the Standard Job framework.

The Standard
cAWSSNS component belongs to the AWS and Connectivity families.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select an AWS connection component from the list to reuse the connection details you already defined. |
| Topic | Specify the name of the topic on Amazon's Simple Notification Service (SNS) to send message to. |
| Subject | Specify a subject for the message. It can be overridden by the message header CamelAwsSnsSubject. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding Value field and enter a value. See the site <https://camel.apache.org/components/3.11.x/aws2-sns-component.html> for available options. Information noteNote: This option is available only if you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAWSSNS can only be an end component in a Route. It has to be used with the cAWSConnection component, which creates a connection to Amazon Web services. For more information about cAWSConnection, see [cAWSConnection](/talend/en-US/components/8.0/mediation-amazon-s3/cawsconnection). |
| Limitation | n/a |

**Related concepts**  

* [Sending messages to Amazon's SNS topic](cawssns-cawsconnection-ctimer-csetbody-sending-messages-to-amazon-s-sns-topic)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns-cawsconnection-ctimer-csetbody-sending-messages-to-amazon-s-sns-topic -->
# Sending messages to Amazon's SNS topic

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario will show you how to use the cAWSSNS
component to send message to the Amazon's SNS topic.

You must have a valid Amazon Web Services developer account, and be signed up to use
Amazon's SNS. For more information, see [Amazon SNS](http://aws.amazon.com/sns).

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns-cawsconnection-ctimer-csetbody-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns-cawsconnection-ctimer-csetbody-configuring-components)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns-cawsconnection-ctimer-csetbody-viewing-code-and-executing-route)

**Related reference**  

* [cAWSSNS](cawssns "Sends messages to an Amazon's Simple Notification topic.")
* [cAWSConnection](cawsconnection "Establishes a connection to Amazon Web Services for data storage and retrieval.")

**Related information**  

* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns-cawsconnection-ctimer-csetbody-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cAWSConnection component to
   display its Basic settings view in the
   Component tab.
2. In the Access Key and Secret Key fields, enter the authentication credentials of your
   AWS account. For how to get your Access Key and Access Secret, see [Access keys (access key ID and
   secret access key)](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).
3. Double-click the cTimer component to open its
   Basic settings view in the Component tab.
4. In the Repeat field, enter 1 to generate the
   message exchange one time. Keep the default settings of the other
   options.
5. Double-click the cSetBody component to open
   its Basic settings view in the Component tab.
6. Select CONSTANT from the
   Language drop-down list and type in
   `"Hello world"` in the Expression field as the message body.
7. Double-click the cAWSSNS component to open
   its Basic settings view in the Component tab.
8. In the Connection list, select the cAWSConnection component that you have just
   configured to connect to Amazon's SNS service. 

   In the Topic field, enter the
   name of the topic to send message to, `"talend-com-tesb-sns"` in
   this use case.

   In the Subject field, give a
   subject for the message, for example `"Talend"`.
9. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns-cawsconnection-ctimer-csetbody-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a cAWSConnection, a cTimer, a cSetBody, and a
   cAWSSNS component onto the design
   workspace.
2. Label the components for better identification of their roles and link them
   with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sns/cawssns-cawsconnection-ctimer-csetbody-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message flow from sns\_cTimer\_1 is given a payload by
   sns\_cSetBody\_1 and then sent to
   sns\_cAWSSNS\_1.
2. Press F6 to execute the Route. The logs of
   the message exchange are printed in the console.
3. An email address has already subscribed to the SNS topic as shown below. For more
   information about how to subscribe to a topic, see the site <http://docs.aws.amazon.com/sns/latest/dg/SubscribeTopic.html>.

   An notification of the message is sent to the Email address:
