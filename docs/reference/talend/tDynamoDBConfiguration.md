<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-dynamodb/tdynamodbconfiguration · versión 8.0 -->
# tDynamoDBConfiguration

Last updated: 9/30/2026

Stores connection information and credentials to be reused by other DynamoDB
components.

You define the connection to a DynamoDB database in tDynamoDBConfiguration and configure the
other DynamoDB components to reuse this configuration. At runtime, the
Spark executors read this configuration in order to connect to
DynamoDB.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

### In this section

* [tDynamoDBConfiguration properties for Apache Spark Batch](/talend/en-US/components/8.0/amazon-dynamodb/tdynamodbconfiguration-properties-for-apache-spark-batch)
* [tDynamoDBConfiguration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/amazon-dynamodb/tdynamodbconfiguration-properties-for-apache-spark-streaming)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-dynamodb/tdynamodbconfiguration-properties-for-apache-spark-batch -->
# tDynamoDBConfiguration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDynamoDBConfiguration running in the Spark Batch Job framework.

The Spark Batch
tDynamoDBConfiguration component belongs to the Storage and the Databases families.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Inherit credentials from AWS role | Select this checkbox to leverage the instance profile credentials. These credentials can be used on Amazon EC2 instances, and are delivered through the Amazon EC2 metadata service. To use this option, your Job must be running within Amazon EC2 or other services that can leverage IAM Roles for access to resources. For more information, see [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). |
| Access key | Enter the access key ID that uniquely identifies an AWS Account. For further information about how to get your Access Key and Secret Key, see [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html).  Information noteNote: This option is available when Use an existing connection and  Inherit credentials from AWS role are cleared. |
| Secret key | Enter the secret access key, constituting the security credentials in combination with the access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  Information noteNote: This option is available when Use an existing connection and  Inherit credentials from AWS role are cleared. |
| Region | Specify the AWS region by selecting a region name from the list. For more information about the AWS Region, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region). |
| Use End Point | Select this check box and in the field displayed, specify the Web service URL of the DynamoDB database service. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  The configuration in a tDynamoDBConfiguration component applies only on the DynamoDB related components in the same Job. In other words, the DynamoDB components used in a child or a parent Job that is called via tRunJob cannot reuse this configuration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
