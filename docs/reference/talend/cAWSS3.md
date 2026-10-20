<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-amazon-s3/cawss3 · versión 8.0 -->
# cAWSS3

Last updated: 9/30/2026

Stores and retrieves objects from/to Amazon's Simple Storage Service
(S3)

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cAWSS3 Standard properties

These properties are used to configure cAWSS3 running in the Standard Job framework.

The Standard
cAWSS3 component belongs to the AWS and Connectivity families.

## Basic settings

| Properties | Description |
| --- | --- |
| Connection | Select an AWSS3 connection component from the list to reuse the connection details you already defined. |
| Bucket Name | Specify the name of the bucket, namely the top level folder, on Amazon's S3 service. |
| The following options are available only when the cAWSS3 is used as a Producer: |  |
| Storage Class | Select from Standard, Standard - Infrequent Access and Reduced Redundancy. For more information about storage classes, see the site <http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html>. |
| Delete After Write | Select this check box to delete the local file object after it is uploaded to the S3 service. |
| Multi Part Upload | Select this check box to upload the file with multi part format, and specify part size in the corresponding field. The default size is 25M. |
| Message Headers | Set the message headers in the corresponding table. Click [+] as many times as required to add message headers to the table. Then click the corresponding Value field and enter a value. See the site <https://camel.apache.org/components/latest/> for more information.  Be sure to set the CamelAwsS3Key header which will be used as the name of the S3 file. |
| Use User Defined Headers | Select this check box to set user defined headers in the corresponding table. Click [+] as many times as required to add message headers to the table. Then click the corresponding Value field and enter a value. Note that user defined headers must start with x-amz-meta-. |
| The following options are available only when the cAWSS3 is used as a Consumer: |  |
| File Name | Specify the name of the file to be consumed. |
| Max Messages Per Poll | The maximum number of objects that can be retrieved in one poll. |
| Prefix | Specify the prefix of files so that only files with that prefix will be consumed. |
| Delete After Read | Select this check box to delete the object from the S3 service after it has been retrieved. |
| Include Body | Select this check box to include the exchange body in the content of the file. Otherwise only the headers will be set with the S3 object metadata and the body will be null. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced | Set the optional parameters in the corresponding table. Click [+] as many times as required to add parameters to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/aws-s3.html> for available options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cAWSS3 can be a start, middle or end component in a Route. It has to be used with the cAWSConnection component, which creates a connection to Amazon Web Services. For more information about cAWSConnection, see [cAWSConnection](/talend/en-US/components/8.0/mediation-amazon-s3/cawsconnection). |
| Limitation | n/a |

**Related concepts**  

* [Sending messages to and receiving messages from Amazon's S3 service](cawsconnection-cawss3-cfile-cprocessor-sending-messages-to-and-receiving-messages-from-amazon-s-s3-service)
