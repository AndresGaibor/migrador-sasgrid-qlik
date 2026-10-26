<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-kinesis/cawskinesis · versión 8.0 -->
# cAWSKinesis

Last updated: 9/30/2026

Consumes messages from and produces messages to Amazon Kinesis
Service.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

Information noteNote: This component is available only if you have installed the R2024-12 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cAWSKinesis Standard properties

These properties are used to configure cAWSKinesis running in
the Standard Job framework.

The Standard
cAWSKinesis component belongs to the AWS and
Connectivity families.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select an AWS Kinesis connection component from the list to reuse the connection details you already defined. |
| Stream Name | Enter the name of the stream. |
| Camel AWS Kinesis Partition Key | This option is available only when cAWSKinesis is used as a Producer.  Specify which shard in the stream the data record is assigned to. |
| Iterator Type | This option is available only when cAWSKinesis is used as a Consumer.  Select where in the Kinesis stream to start getting records from:  * AT\_SEQUENCE\_NUMBER: Start getting records from the position denoted by a   specific sequence number. Enter the sequence number in the   Sequence Number field. * AFTER\_SEQUENCE\_NUMBER: Start getting records right after the position   denoted by a specific sequence number. Enter the sequence number in the   Sequence Number field. * TRIM\_HORIZON: Start getting records at the last untrimmed record in the   shard, which is the oldest data record in the shard. * LATEST: Start getting records just after the most recent record in the   shard, so that you always read the most recent data in the shard. * AT\_TIMESTAMP: Start getting records from the position denoted by a   specific timestamp. Enter the timestamp in the   Timestamp field. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAWSKinesis can be a start, middle or end component in a Route. It has to be used with the cAWSConnection component, which creates a connection to Amazon Web Services. For more information about cAWSConnection, see [cAWSConnection](/talend/en-US/components/8.0/mediation-amazon-s3/cawsconnection). |
| Limitation | n/a |

**Related concepts**  

* [Sending messages to and receiving messages from Amazon Kinesis Service](sending-messages-to-and-receiving-messages-from-amazon-kinesis-service)
