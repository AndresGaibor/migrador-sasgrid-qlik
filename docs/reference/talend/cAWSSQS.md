<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs · versión 8.0 -->
# cAWSSQS

Last updated: 9/30/2026

Sends and receives messages to/from Amazon's Simple Queue Service
(SQS). The AWS SQS FIFO Feature for Queues are supported.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cAWSSQS Standard properties

These properties are used to configure cAWSSQS running in the Standard Job framework.

The Standard
cAWSSQS component belongs to the AWS and Connectivity families.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select an AWS connection component from the list to reuse the connection details you already defined. |
| Queue Name | Enter the name of the queue to send message to or receive message from. When the cAWSSQS is used as a producer, the queue will be created if it does not exist. Queue names must be 1-80 characters in length and be composed of alphanumeric characters, hyphens (-), and underscores (\_). |
| The following options are available only when the cAWSSQS is used as a Producer: |  |
| Delay (in seconds) | Specify the amount of time to delay the first delivery of all messages added to this queue. |
| Wait Time (0 to 20 seconds) | Specify the maximum amount of time in seconds (0 to 20) that a long polling receive call will wait for a message to become available before returning an empty response. |
| The following options are available only when the cAWSSQS is used as a Consumer: |  |
| Delete Message / After Read (processed by route) | Select this check box to delete the message from the queue after it is read and processed by the Route. |
| Delete Message / If Filtered (matched by filter) | Select this check box to delete the messages from the queue that are filtered in the Route, even if the exchange fails to get through a filter. |
| Allow Multiple Threads | Select this check box to allow multiple threads to poll the SQS queue to increase throughput. When this option is enabled, you need to specify the maximum number of concurrent consumers and objects that can be retrieved in one poll in the Concurrency Number and Max Messages Per Poll fields respectively. |
| Extend Message Visibility | Select this check box to enable a scheduled background task to keep extending the message visibility on SQS. This is needed if it takes a long time to process the message. When this option is enabled, you need to set the duration in seconds that the received messages are hidden from subsequent retrieve requests in the Visibility Timeout field. For more information, see the site <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html>. |
| Request Attribute / All | Select this check box to retrieve the standard Amazon SQS attributes along with each message. For more information about the Amazon SQS attributes, see [ReceiveMessage > Request Parameters](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html). |
| Request Attribute / Approximate First Receive Timestamp | Select this check box to retrieve the ApproximateFirstReceiveTimestamp attribute only along with each message. For more information about the Amazon SQS attributes, see [ReceiveMessage > Request Parameters](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html). |
| Request Attribute / Approximate Receive Count | Select this check box to retrieve the ApproximateReceiveCount attribute only along with each message. For more information about the Amazon SQS attributes, see [ReceiveMessage > Request Parameters](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html). |
| Request Attribute / Sender ID | Select this check box to retrieve the SenderId attribute only along with each message. For more information about the Amazon SQS attributes, see [ReceiveMessage > Request Parameters](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html). |
| Request Attribute / Sent Timestamp | Select this check box to retrieve the SentTimestamp attribute only along with each message. For more information about the Amazon SQS attributes, see [ReceiveMessage > Request Parameters](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html). |

## Advanced settings

| Properties | Description |
| --- | --- |
| AWS Account ID (Queue Owner) | Specify the queue owner's AWS account ID when you need to connect the queue with different account owner. |
| Queue Configuration / Attributes | Set the optional queue attributes in the corresponding table. Click [+] as many times as required to add attributes to the table. Then click the corresponding Value field and enter a value. The following attributes are available:  * Default Visibility Timeout(in seconds): The   default visibility timeout for the queue in seconds. * Max Message Size(in bytes): The maximum message   size in bytes that an SQS message can contain for the queue. * Message Retention Period(in seconds): The period   in seconds that a message will be retained by SQS for the queue. * Receive Message Wait Time(in seconds): The   duration in seconds that the ReceiveMessage action call will wait until a   message is in the queue to include in the response. * Message GroupId Strategy(for FIFO queue): To send   messages to FIFO queue of Amazon SQS, you have to specify the value of   this attribute from the following to set the Message Group ID:   + useConstant: The Message Group ID is the fixed     string CamelSingleMessageGroup.   + useExchangeId: The Message Group ID is the camel     exchangeId, for example,     ID-xldai-PC-1545104566148-0-1.   + usePropertyValue: The Message Group ID is     specified from the Camel property     CamelAwsMessageGroupId. * Message DeduplicationId Strategy(for FIFO queue):   This attribute is optional for sending messages to FIFO queue of Amazon   SQS. Specify the value of this attribute from the following for how   messages are deduplicated:   + useExchangeId: the messages are deduplicated by     exchangeId.   + useContentBasedDeduplication: the messages are     deduplicated by message content. |
| Request Message Attribute | This option is only available when cAWSSQS is used as a Consumer. Select this check box and add the attribute to be retrieved along with each message. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAWSSQS can be a start, middle or end component in a Route. It has to be used with the cAWSConnection component, which creates a connection to Amazon SNS service. For more information about cAWSConnection, see [cAWSConnection](/talend/en-US/components/8.0/mediation-amazon-s3/cawsconnection). |
| Limitation | n/a |

**Related concepts**  

* [Sending messages to and receiving messages from Amazon's SQS queue](cawssqs-cawsconnection-cmessagefilter-clog-sending-messages-to-and-receiving-messages-from-amazon-s-sqs-queue)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-sending-messages-to-and-receiving-messages-from-amazon-s-sqs-queue -->
# Sending messages to and receiving messages from Amazon's SQS queue

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario will show you how to use the cAWSSQS
component to send messages to and consume messages from an SQS queue. To do this, two
Routes are built, a message producer Route, and a consumer Route. Messages are sent to
the SQS queue in the producer Route and then consumed in the consumer Route.

You must have a valid Amazon Web Services developer account, and be signed up to use
Amazon SQS. For more information, see [Amazon SQS](http://aws.amazon.com/sqs).

### In this section

* [Building the producer Route](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-building-producer-route)
* [Building the consumer Route](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-building-consumer-route)

**Related reference**  

* [cAWSSQS](cawssqs "Sends and receives messages to/from Amazon's Simple Queue Service (SQS). The AWS SQS FIFO Feature for Queues are supported.")
* [cAWSConnection](cawsconnection "Establishes a connection to Amazon Web Services for data storage and retrieval.")

**Related information**  

* [cMessageFilter](/talend/en-US/mediation-components/8.0/mediation-filter/cmessagefilter)
* [cTimer](/talend/en-US/mediation-components/8.0/mediation-orchestration/ctimer)
* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cLog](/talend/en-US/mediation-components/8.0/mediation-logs-and-errors/clog)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-building-consumer-route -->
# Building the consumer Route

Last updated: 9/30/2026

### In this section

* [Arranging the flow of the message](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-arranging-flow-of-message)
* [Configuring how the message is processed](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-configuring-how-message-is-processed)
* [Executing the Route](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-building-producer-route -->
# Building the producer Route

Last updated: 9/30/2026

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-configuring-components)
* [Viewing the code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-viewing-code-and-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-arranging-flow-of-message -->
# Arranging the flow of the message

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cAWSConnection, a cAWSSQS, a cMessageFilter
   and a cLog component onto the design
   workspace.
2. Link the cAWSSQS to cMessageFilter with the Row
   > Route connection and cMessageFilter to cLog with the Row >
   Filter connection.
3. Label the components for better identification of their roles.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-configuring-how-message-is-processed -->
# Configuring how the message is processed

Last updated: 9/30/2026

## Procedure

1. Configure the cAWSConnection using the
   same properties as in the producer Route.
2. Double-click the cAWSSQS component to display its
   Basic settings view in the Component tab.
3. In the Connection list, select the
   cAWSConnection component to connect to
   Amazon's SQS service. 

   In the Queue Name field, enter the name
   of the queue to consume the message from.

   Select the Delete Message / After Read
   check box and clear the If Filtered check
   box to delete the messages that are read and keep those that are not
   consumed.
4. Double-click the cMessageFilter component
   to display its Basic settings view in the
   Component tab.
5. Select Simple from the
   Language list and enter `"${body}
   == 'hello'"` in the Expression
   field to sort out messages with hello as the message body.
6. Keep the default settings of the cLog component to
   log the message exchanges.
7. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-executing-route -->
# Executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message flow from sqsconsumer\_cAWSSQS\_3, is filtered by
   sqsconsumer\_cMessageFilter\_1, and then routed to
   sqsconsumer\_cLog\_1.
2. Press F6 to execute the Route. The messages with the
   body hello are consumed and are printed in the console.
3. In the SQS Web Console, you can see that there are now 3 three messages left in the queue
   **talend-com-tesb-camel-sqs**.
   The two messages with the body hello have been consumed and
   deleted as configured in the cAWSSQS
   component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cAWSConnection component to display its
   Basic settings view in the Component tab.
2. In the Access Key and Secret Key fields, enter the authentication
   credentials of your AWS account. For how to get your Access Key and Access
   Secret, see [Access keys (access key ID
   and secret access key)](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys).
3. Double-click the cTimer labeled
   *repeat=2* to open its Basic
   settings view in the Component tab.
4. In the Repeat field, enter 2 to generate
   the message exchange twice. Keep the default settings of the other
   options.
5. Configure the cTimer labeled
   *repeat=3* in the same way to generate the message
   exchange three times.
6. Double-click the cSetBody component labeled
   *body=hello* to open its Basic
   settings view in the Component tab.
7. Select CONSTANT from the Language list and type in *hello* in the
   Expression field as the message
   body.
8. Configure the cSetBody labeled
   *body=world* in the same way to set the message body
   as *world*.
9. Double-click the cAWSSQS labeled
   *Producer\_1* to open its Basic
   settings view in the Component tab.
10. In the Connection list, select the
    cAWSConnection component that you have
    just configured to connect to Amazon's SQS service. 

    In the Queue Name field, type in the name of the SQS
    queue to send the messages.
11. Configure the cAWSSQS labeled
    *Producer\_2* with the same properties to send the
    messages to the same queue.
12. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a cAWSConnection, two cTimer,
   two cSetBody, two cAWSSQS components onto the design workspace.
2. Label the components for better identification of their roles and link
   them with the Row > Route connection as shown above.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-sqs/cawssqs-cawsconnection-cmessagefilter-clog-viewing-code-and-executing-route -->
# Viewing the code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, in the first sub-route, the message flow from
   sqsproducer\_cTimer\_1 is given a payload by
   sqsproducer\_cSetBody\_1 and then sent to
   sqsproducer\_cAWSSQS\_1. The second sub-route is in the same
   way.
2. Press F6 to execute the Route. The logs of the message
   exchange are printed in the console. The warn message shows that header
   fireTime is not put into the message attribute.
3. In the SQS Web Console, you can see that there are now 5 messages in the queue
   *talend-com-tesb-camel-sqs*.
