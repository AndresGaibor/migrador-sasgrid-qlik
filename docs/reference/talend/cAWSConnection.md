<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-s3/cawsconnection · versión 8.0 -->
# cAWSConnection

Last updated: 9/30/2026

Establishes a connection to Amazon Web Services for data storage and
retrieval.

## cAWSConnection Standard properties

These properties are used to configure cAWSConnection running in the Standard Job framework.

The Standard
cAWSConnection component belongs to the AWS and Connectivity families.

## Basic settings

| Properties | Description |
| --- | --- |
| Access Key | The Access Key ID that uniquely identifies an AWS Account. For how to get your Access Key and Access Secret, see [Access keys (access key ID and secret access key)](http://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys). |
| Secret Key | The Secret Access Key, constituting the security credentials in combination with the access Key. To enter the secret key, click [...] next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Inherit credentials from AWS role | Select this check box to obtain AWS security credentials from Amazon EC2 instance metadata. To use this option, the Amazon EC2 instance must be started and your Route must be running on Amazon EC2. For more information, see [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) , [Instance Metadata and User Data](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html), and [IAM Roles for Amazon EC2](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html). |
| Region | Select the way the AWS region will be specified.  * Pick in the list: Select a region name from the   list. * Custom: Enter a region between double quotation   marks, for example `"us-east-1"`, in the field. You can   also use context parameters to specify the AWS region, for example,   context.AWSRegion. For more information about AWS   Regions, see [AWS Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html).   Information noteNote: From Talend 8.0 onwards, DEFAULT is removed from the Region list. You need to select an explicit region to match the one in your AWS account. When you import a Route built from a 7.x Talend Studio, the DEFAULT region will be replaced by US-EAST-1. You need to change it if it is not correct for your AWS account. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Config Client | Select this check box to set the optional parameters for your AWS client in the corresponding table. Click [+] as many times as required and add the available parameters from the list to the table. Then click the corresponding Value field and enter a value. See the site [Class ClientConfiguration](http://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html) for more information. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAWSConnection cannot be added directly in a Route. |

**Related concepts**  

* [Sending messages to and receiving messages from Amazon Kinesis Service](sending-messages-to-and-receiving-messages-from-amazon-kinesis-service)
