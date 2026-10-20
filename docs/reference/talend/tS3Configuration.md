<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration · versión 8.0 -->
# tS3Configuration

Last updated: 9/30/2026

Reuses the connection configuration to S3 in the same Job. The Spark
cluster to be used reads this configuration to eventually connect to S3.

Multiple tS3Configuration components are allowed per Job.

### In this section

* [tS3Configuration properties for Apache Spark Batch](/talend/en-US/components/8.0/amazon-s3/ts3configuration-properties-for-apache-spark-batch)
* [tS3Configuration properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/amazon-s3/ts3configuration-properties-for-apache-spark-streaming)
* [tS3Configuration properties for Apache Spark Structured Streaming](/talend/en-US/components/8.0/amazon-s3/ts3configuration-properties-for-apache-spark-structured-streaming)

**Related concepts**  

* [Writing and reading data from S3 (Databricks on AWS)](ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-writing-and-reading-data-from-s3-databricks-on-aws-the "In this scenario, you create a Spark Batch Job using tS3Configuration and the Parquet components to write data on S3 and then read the data from S3.")
* [Writing server-side KMS encrypted data on EMR](ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-writing-server-side-kms-encrypted-data-on-emr "If the AWS SSE-KMS encryption (at-rest encryption) service is enabled to set Default encryption to protect data on the S3A system of your EMR cluster, select the SSE-KMS option in tS3Configuration when writing data to that S3A system.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-properties-for-apache-spark-batch -->
# tS3Configuration properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tS3Configuration running in the Spark
Batch Job framework.

The Spark Batch
tS3Configuration component belongs to the Storage family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Access Key | Enter the access key ID that uniquely identifies an AWS Account. For further information about how to get your Access Key and Secret Key, see [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html). |
| Secret Key | Enter the secret access key, constituting the security credentials in combination with the access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Hadoop S3 version | Select the Hadoop version you are using from the drop-down list. If the cluster has S3 libraries, select Use cluster's libraries to avoid conflicts by uploading non aligned dependencies. If the cluster does not have S3 libraries, select the version that matches the Hadoop libraries on the cluster.  This parameter is not available when the Spark Job is running on Spark Universal in Databricks, Local, or Standalone modes. |
| File System | Select the file system type from the drop-down list:  * S3A File System to use the standard Hadoop connector   for accessing Amazon S3. * EMR File System to leverage Amazon EMR's connector   with features like Consistent View and advanced AWS integration.   This field is only available when you have selected the Inherit credentials from AWS check box. |
| Use EMRFS consistent view | Select this check box to use the EMR File System (EMRFS) consistent view. This option allows EMR clusters to check for list and read-after-write consistency for Amazon S3 objects that are written by or synced with EMRFS. Information noteNote: Avoid alternatively switching the consistent view on and off on a single bucket, as it might create inconsistency errors. If this issue occurs, you can fix the inconsistencies using the sync command in the EMRFS CLI. For more information, see [EMRFS CLI Reference](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emrfs-cli-reference.html).  This feature is available when you are using the Amazon EMR 5.29 distribution. |
| EMRFS metadata table | Enter the name of the metadata DynamoDB table to be used. Information noteNote: The default metadata table name is EmrFSMetadata.  This field is only available when you have selected the Use EMRFS consistent view check box. |
| Bucket name | Enter the bucket name and its folder you need to use. You need to separate the bucket name and the folder name using a slash (/). |
| Temp folder | Enter the location of the temp folder in S3. This folder will be automatically created if it has not existed by the time of the execution. |
| Inherit credentials from AWS | Select this check box to obtain AWS security credentials from your IAM role. This option is available for Amazon EMR and Databricks on AWS clusters. To use this option, the cluster must be started and your Job must be running on this cluster. For more information, see [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) . This option enables you to develop your Job without having to put any AWS keys in the Job, thus easily comply with the security policy of your organization. |
| Use SSE encryption | Select this check box to use the SSE-KMS encryption service enabled on AWS to read or write the encrypted data on S3. On the EMR side, the SSE-KMS service must have been enabled with the Default encryption feature and a customer managed CMK specified for the encryption.  For further information about the AWS SSE-KMS encryption, see [Protecting Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) from the AWS documentation.  For further information about how to enable the Default Encryption feature for an Amazon S3 bucket, see [Default encryption](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/default-bucket-encryption.html) from the AWS documentation.  This property is available only when you are using Amazon EMR distributions. |
| Bucket encryption | Select the default encryption you used for your bucket from the drop-down list:  * aws:kms: server side encryption with AWS KMS-Managed   Keys (SSE-KMS) * SSE-S3: server side encryption with Amazon S3-Managed   Keys (SSE-S3)  This property is available only when you are using Amazon EMR distributions. |
| Use 'in-transit' encryption | Select this check box to enable the encryption of data in transit.  Information noteNote: The in-transit encryption is selected by default. If you deactivate this option, you do not have to set up a KMS encrypted EMR cluster.  This property is available only when you are using Amazon EMR distributions with SSE-KMS encryption. |
| Assume role | Select this check box to make your Job temporarily assume a role and the permissions associated with this role.  Ensure that access to this role has been granted to your user account by the trust policy associated to this role. If you are not certain about this, ask the owner of this role or your AWS administrator.  After selecting this check box, specify the parameters the administrator of the AWS system to be used defined for this role.  * ARN: the Amazon Resource Name (ARN) of the role to   assume. You can find this ARN name on the Summary   page of the role to be used on your AWS portal, for example, this role   ARN could read like   `am:aws:iam::[aws_account_number]:role/[role_name]`. Role session name: enter the   name you want to use to uniquely identify your assumed role session. This   name can contain upper- and lower-case alphanumeric characters with no   spaces. You can also include underscores or any of the following characters:   =,.@-. * Session duration   (minutes): the duration (in minutes) for which you want   the assumed role session to be active. This duration cannot exceed the   maximum duration which your AWS administrator has set. The duration   defaults to 3600 seconds if you give it no value.  The External ID parameter is required only if your AWS administrator or the owner of this role has defined an external ID when they set up a trust policy for this role.  * Policy:   enter an IAM policy in JSON format that you want to use as a   session policy. Use session policies to limit the permissions of   the session. The resulting session's permissions are the   intersection of the role's identity-based policy and the session   policies. * Policy   ARNs: enter the Amazon Resource Names (ARNs) of   the IAM managed policies that you want to use as managed session   policies. Use managed session policies to limit the permissions   of the session. The policies must exist in the same account as   the role. The resulting session's permissions are the   intersection of the role's identity-based policy and the session   policies. * Serial   Number: when you assume a role, the trust policy   of this role might require Multi-Factor Authentication (MFA). In   this case, you must indicate the identification number of the   hardware or virtual MFA device that is associated with the user   who assumes the role. * Tags:   list session tags in the form of key-value pairs. You can then   use these session tags in policies to allow or deny access to   requests. * Token   Code: when you assume a role, the trust policy   of this role might require Multi-Factor Authentication (MFA). In   this case, you must indicate a token code. This token code is a   time-based one-time password produced by the MFA device. * Transitive Tag   Keys: list session tags in the form of key-value   pairs that you want to persist to the next role in a role   chain.  In addition, if the AWS administrator has enabled the STS endpoints for given regions you want to use for better response performance, use the Set STS region check box or the Set STS endpoint check box in the Advanced settings tab.  This check box is available only for the following distributions Talend supports:  * CDH 5.10 and onwards (including the dynamic support for the latest   Cloudera distributions) * HDP 2.5 and onwards * EMR 5.15 and onwards * CDP Private Cloud Base 7.1  This check box is also available when you are using Spark V1.6 and onwards in the Local Spark mode in the Spark configuration tab. |
| KMS key id | Enter the ID of the customer managed CMK you want to use for the encryption. Information noteNote: You can either use one of the following format:  * arn:aws:kms:region:account-id:key/key-id * key-id  The KMS key id field is only available when you select the Use SSE encryption check box. This feature is available when you are using Amazon EMR distribution with Spark. |
| Set region | Select this check box and select the region to connect to.  This feature is available when you are using one of the following distributions with Spark:  * Amazon   EMR V4.5 and up to V5.15. EMR uses EMRFS from V5.29 * MapR   V5.0 and onwards * Hortonworks Data Platform V2.4 and onwards * Cloudera V5.8 and onwards. For Cloudera V5.8, the Spark version must be   2.0. * Cloudera   Altus |
| Set endpoint | Select this check box and in the Endpoint field that is displayed, enter the Amazon region endpoint you need to use. For a list of the available endpoints, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).  If you leave this check box clear, the endpoint will be the default one defined by your Hadoop distribution, while this check box is not available when you have selected the Set region check box and in this situation the value selected from the Set region list is used.  This feature is available when you are using one of the following distributions with Spark:  * Amazon   EMR V4.5 and up to V5.15. EMR uses EMRFS from V5.29 * MapR   V5.0 and onwards * Hortonworks Data Platform V2.4 and onwards * Cloudera V5.8 and onwards. For Cloudera V5.8, the Spark version must be   2.0. * Cloudera   Altus |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set region and Set endpoint | If the AWS administrator has enabled the STS endpoints for the regions you want to use for better response performance, select the Set region check box and then select the regional endpoint to be used.  If the endpoint you want to use is not available in this regional endpoint list, clear the Set region check box, then select the Set endpoint check box and enter the endpoint to be used.  This service allows you to request temporary, limited-privilege credentials for the AWS user authentication. Therefore, you still need to provide the access key and secret key to authenticate the AWS account to be used.  For a list of the STS endpoints you can use, see [AWS Security Token Service](https://docs.aws.amazon.com/general/latest/gr/rande.html#sts_region). For further information about the STS temporary credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). Both articles are from the AWS documentation. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used with no need to be connected to other components.  Multiple tS3Configuration components are allowed per Job. The Assume Role option can be added to multiple tS3Configuration components.  You need to drop tS3Configuration along with the file system related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-properties-for-apache-spark-structured-streaming -->
# tS3Configuration properties for Apache Spark Structured Streaming

Last updated: 9/30/2026

[Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

These properties are used to configure tS3Configuration running
in the Spark Structured Streaming Job framework.

The Spark Structured Streaming
tS3Configuration component belongs to the Storage family.

The streaming version of this component is available in Talend Real-Time Big Data Platform and in
Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Access Key | Enter the access key ID that uniquely identifies an AWS Account. For further information about how to get your Access Key and Secret Key, see [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html). |
| Secret Key | Enter the secret access key, constituting the security credentials in combination with the access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Bucket name | Select this check box to specify an S3 bucket name, then enter the name in the field that appears. |
| Temp Folder | Enter the location of the temp folder in S3. This folder will be automatically created if it has not existed by the time of the execution. |
| Assume Role | Select this check box to make the Job temporarily assume an AWS IAM role and its associated permissions. Then specify the following parameters:  * Role ARN: enter the Amazon Resource Name of the   role to assume. * Role session name: enter a name to identify the   assumed-role session. * Session duration (minutes, 15mins~1hour): enter the   duration of the session in minutes. * External ID: enter the external ID if the trust   policy of the role requires one. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set region | Select this check box and select the region to connect to.  This setting appears only when Assume Role is enabled. |
| Set endpoint | Select this check box and enter the Amazon S3 endpoint to use in the Endpoint field.  If you leave this check box clear, the default endpoint is used. This setting appears only when Assume Role is enabled. |
| Set region and Set endpoint | If the AWS administrator has enabled the STS endpoints for the regions you want to use for better response performance, select the Set region check box and then select the regional endpoint to be used.  If the endpoint you want to use is not available in this regional endpoint list, clear the Set region check box, then select the Set endpoint check box and enter the endpoint to be used.  This service allows you to request temporary, limited-privilege credentials for the AWS user authentication. Therefore, you still need to provide the access key and secret key to authenticate the AWS account to be used.  For a list of the STS endpoints you can use, see [AWS Security Token Service](https://docs.aws.amazon.com/general/latest/gr/rande.html#sts_region). For further information about the STS temporary credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). Both articles are from the AWS documentation. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used with no need to be connected to other components.  Multiple tS3Configuration components are allowed per Job. The Assume Role option can be added to multiple tS3Configuration components.  You need to drop tS3Configuration along with the file system related subJob to be run in the same Job so that the configuration is used by the whole Job at runtime.  This component, along with the Spark Structured Streaming component Palette it belongs to, appears only when you are creating a Spark Structured Streaming Job. |
| Spark Connection | You need to use the Structured Streaming Configuration tab in the Run view to define the connection to a Spark cluster for the whole Job.  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-writing-and-reading-data-from-s3-databricks-on-aws-the -->
# Writing and reading data from S3 (Databricks on AWS)

Last updated: 9/30/2026

In this scenario, you create a Spark Batch Job using
tS3Configuration and the Parquet components to write data on
S3 and then read the data from S3.

This scenario applies only to subscription-based Talend products
with Big Data.

The sample data reads as
follows:

```
01;ychen
```

This data contains a user name and the ID number distributed to this user.

Note that the sample data is created for demonstration purposes only.

### In this section

* [Design the data flow of the Job working with S3 and Databricks on AWS](/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-design-data-flow-of-job-working-with-s3-and-databricks-on-aws-in?id=256)
* [Defining the Azure Databricks connection parameters for Spark Jobs](/talend/en-US/components/8.0/amazon-s3/tazurefsconfiguration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-defining-azure-databricks-connection-parameters-for-spark-jobs-enter?id=257)
* [Configuring the connection to the S3 service to be used by Spark](/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-configuring-connection-to-s3-service-to-be-used-by-spark?id=258)
* [Write the sample data to S3](/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-write-sample-data-to-s3?id=259)
* [Reading the sample data from S3](/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-reading-sample-data-from-s3?id=260)

**Related information**  

* [tS3Configuration](/talend/en-US/components/8.0/amazon-s3/ts3configuration)
* [tFileInputParquet](/talend/en-US/components/8.0/parquet/tfileinputparquet)
* [tFileOutputParquet](/talend/en-US/components/8.0/parquet/tfileoutputparquet)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-writing-server-side-kms-encrypted-data-on-emr -->
# Writing server-side KMS encrypted data on EMR

Last updated: 9/30/2026

If the AWS SSE-KMS encryption (at-rest encryption) service is
enabled to set Default encryption to protect data
on the S3A system of your EMR cluster, select the SSE-KMS option in tS3Configuration when writing data to that S3A
system.

The sample data used in this scenario is about different types of
incidents that people reported occurring on Paris streets within one
day.

```
1;226 rue marcadet, 75018 Paris;abandoned object;garbage on the street
2;2 rue marcadet, 75018 Paris;shift and damage;direction sign damaged
3;45 boulevard de la villette, 75010 Paris; abandoned object; suspicious package
4;10 rue emile lepeu, 75011 Paris;graffiti and improper poster;graffiti
5;27 avenue emile zola, 75015 Paris;shift and damage;deformed road
```

The sample data is used for demonstration purposes only.

The Job calculates the occurrence of each incident type.

Prerequisites:

* The S3 system to be used is S3A.
* The SSE-KMS encryption service on AWS is enabled with the
  Default encryption feature and a
  customer managed CMK has been specified for it.
* The EMR cluster to be used is created with SSE-KMS and the
  EMR\_EC2\_DefaultRole role has been added to the above-mentioned CMK.
* The administrator of your EMR cluster has granted the appropriate
  rights and permissions to the AWS account you are using in your Jobs.
* Your EMR cluster has been properly set up and is running.
* A Talend JobServer has
  been deployed on an instance within the network of your EMR cluster, such as the
  instance for the master of your cluster.

All these operations are done on the AWS side.

* In Talend Studio or
  in Talend Administration Center,
  define the Talend JobServer as
  the execution server of your Jobs.

Ensure that the client machine on which the Talend Jobs are executed can
recognize the host names of the nodes of the Hadoop cluster to be used. For this purpose, add
the IP address/hostname mapping entries for the services of that Hadoop cluster in the
hosts file of the client machine.

If this is the first time your EMR cluster is set up to run with Talend Jobs,
see [Amazon EMR - Getting Started](/talend/r/en-US/8.0/amazon-emr-getting-started).

### In this section

* [Designing the flow of the data to write and encrypt onto EMR](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-designing-flow-of-data-to-write-and-encrypt-onto-emr-in?id=262)
* [Configuring the connection to the HDFS file system of your EMR cluster](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-configuring-connection-to-hdfs-file-system-of-your-emr-cluster?id=263)
* [Configuring the connection to S3 to be used to store the business data](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-configuring-connection-to-s3-to-be-used-to-store-business-data?id=264)
* [Loading the sample data about street incidents to the Job](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-loading-sample-data-about-street-incidents-to-job.?id=265)
* [Calculating the incident occurrence](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-calculating-incident-occurrence?id=266)
* [Writing the aggregated data about street incidents to EMR](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-writing-aggregated-data-about-street-incidents-to-emr?id=267)
* [Defining the EMR connection parameters](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-defining-emr-connection-parameters-spark-batch-component-enter?id=268)
* [Running the Job to write KMS encrypted data to EMR](/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-running-job-to-write-kms-encrypted-data-to-emr-press?id=269)

**Related concepts**  

* [tS3Configuration](ts3configuration "Reuses the connection configuration to S3 in the same Job. The Spark cluster to be used reads this configuration to eventually connect to S3.")

**Related information**  

* [tFileOutputParquet](/talend/en-US/components/8.0/parquet/tfileoutputparquet)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tAggregateRow](/talend/en-US/components/8.0/processing/taggregaterow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-configuring-connection-to-s3-service-to-be-used-by-spark -->
# Configuring the connection to the S3 service to be used by Spark

Last updated: 9/30/2026

## Procedure

1. Double-click tS3Configuration to open its Component view.

   Spark uses this component to connect to the S3 system in which your Job writes
   the actual business data. If you place neither
   tS3Configuration nor any other configuration
   component that supports Databricks on AWS, this business data is written in the
   Databricks Filesystem (DBFS).

   ### Example
2. In the Access key and the Secret
   key fields, enter the keys to be used to authenticate to
   S3.
3. In the Bucket name field, enter the name of the bucket
   and the folder in this bucket to be used to store the business data, for
   example, mybucket/myfolder. This folder is created on the
   fly if it does not exist but the bucket must already exist at runtime.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-design-data-flow-of-job-working-with-s3-and-databricks-on-aws-in -->
# Design the data flow of the Job working with S3 and Databricks on AWS

Last updated: 9/30/2026

## Procedure

1. In the Integration
   perspective of Talend Studio,
   create an empty Spark Batch Job from the Job Designs node in
   the Repository tree view.
2. In the workspace, enter the name of the component to be used and select this
   component from the list that appears. In this scenario, the components are
   tS3Configuration,
   tFixedFlowInput,
   tFileOutputParquet,
   tFileInputParquet and
   tLogRow.

   The tFixedFlowInput component is used to load the
   sample data into the data flow. In the real-world practice, you could use the
   File input components, as well as the processing components, to design a
   sophisticated process to prepare your data to be processed.
3. Connect tFixedFlowInput to tFileOutputParquet using the Row > Main link.
4. Connect tFileInputParquet to tLogRow using the Row > Main link.
5. Connect tFixedFlowInput to tFileInputParquet using the Trigger > OnSubjobOk link.
6. Leave tS3Configuration alone without any
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-reading-sample-data-from-s3 -->
# Reading the sample data from S3

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputParquet to open its
   Component view.

   ### Example
2. Select the Define a storage configuration component
   check box and then select the tS3Configuration
   component you configured in the previous steps.
3. Click the [...] button next to Edit
   schema to open the schema editor.
4. Click the [+] button to add the schema columns for
   output as shown in this image.

   ### Example
5. Click OK to validate these changes and accept the
   propagation prompted by the pop-up dialog box.
6. In the Folder/File field, enter the name of the folder
   from which you need to read data. In this scenario, it is
   `sample_user`.
7. Double-click tLogRow to open its
   Component view and select the Table radio button to present the result in a table.
8. Press 
   F6
    to run this Job.

## Results

Once done, you can find your Job on the Job page on the Web UI
of your Databricks cluster and then check the execution log of your Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-tfileinputparquet-tfileoutputparquet-tfixedflowinput-write-sample-data-to-s3 -->
# Write the sample data to S3

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowIput component to
   open its Component view.

   ### Example
2. Click the [...] button next to Edit schema to open the schema editor.
3. Click the [+] button to add the schema
   columns as shown in this image.

   ### Example
4. Click OK to validate these changes and accept
   the propagation prompted by the pop-up dialog box.
5. In the Mode area, select the Use Inline
   Content radio button and paste the previously mentioned sample data
   into the Content field that is displayed.
6. In the Field separator field, enter a
   semicolon (*;*).
7. Double-click the tFileOutputParquet component to
   open its Component view.

   ### Example
8. Select the Define a storage configuration component
   check box and then select the tS3Configuration component
   you configured in the previous steps.
9. Click Sync columns to ensure that
   tFileOutputParquet has the same schema as
   tFixedFlowInput.
10. In the Folder/File field, enter the name of the S3
    folder to be used to store the sample data. For example, enter
    /sample\_user, then as you have specified
    my\_bucket/my\_folder to use in
    tS3Configuration to store the business data on S3,
    the eventual directory on S3 becomes
    my\_bucket/my\_folder/sample\_user.
11. From the Action drop-down list, select
    Create if the sample\_user folder
    does not exist yet; if this folder already exists, select
    Overwrite.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-calculating-incident-occurrence -->
# Calculating the incident occurrence

Last updated: 9/30/2026

## Procedure

1. Double-click tAggregateRow to open its
   Component view.

   ### Example
2. Click the [...] button next to Edit schema to open the schema editor.
3. On the output side (right), click the [+]
   button twice to add two rows and in the Column column, rename them to `incident_type` and `incident_number`, respectively.

   ### Example
4. In the Type column of the `incident_number` row of the output side, select `Integer`.
5. Click OK to validate these changes and accept
   the propagation prompted by the pop-up dialog box.
6. In the Group by table, add one row by
   clicking the [+] button and configure
   this row as follows to group the outputted data:

   * Output column:
     select the columns from the output schema to be used as the
     conditions to group the outputted data. In this example, it is the
     `incident_type` from the output schema.
   * Input column
     position: select the columns from the input schema
     to send data to the output columns you have selected in the
     Output
     column column. In this scenario, it is the
     `incident_type` column from the input schema.
7. In the Operations table, add one row by clicking the [+] button once and configure this
   row as follows to calculate the occurrence of each incident type: 

   * Output column:
     select the column from the output schema to store the calculation
     results. In this scenario, it is `incident_number`.
   * Function: select
     the function to be used to process the incoming data. In this
     scenario, select `count`. It counts the frequency of each
     incident.
   * Input column
     position: select the column from the input schema to
     provide the data to be processed. In this scenario, it is `incident_type`.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-configuring-connection-to-hdfs-file-system-of-your-emr-cluster -->
# Configuring the connection to the HDFS file system of your EMR cluster

Last updated: 9/30/2026

## Procedure

1. Double-click tHDFSConfiguration to open its Component view.

   Spark uses this component to connect to the HDFS system to
   which the jar files dependent on the Job are transferred.
2. If you have defined the HDFS connection metadata under the
   Hadoop cluster node in Repository, select Repository from the Property
   type drop-down list and then click the [...] button to select the HDFS connection you
   have defined from the Repository content
   wizard.

   For further information about setting up a reusable HDFS connection, see
   [Centralizing HDFS metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-hdfs-metadata).

   If you complete this step, you can skip the following steps
   about configuring tHDFSConfiguration
   because all the required fields should have been filled automatically.
3. In the Version area,
   select the Hadoop distribution you need to connect to and its version.
4. In the NameNode URI
   field, enter the location of the machine hosting the NameNode service of the
   cluster.  If you are using WebHDFS, the location should be
   webhdfs://masternode:portnumber; WebHDFS with SSL is not
   supported yet.
5. In the Username field,
   enter the authentication information used to connect to the HDFS system to be
   used. Note that the user name must be the same as you have put in the Spark configuration tab.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-configuring-connection-to-s3-to-be-used-to-store-business-data -->
# Configuring the connection to S3 to be used to store the business data

Last updated: 9/30/2026

## Procedure

1. Double-click tS3Configuration to open its Component view.

   Spark uses this component to connect to the S3 system to which the business data is stored. In this scenario, the sample data about the street incidents is written and ecrypted on S3.
2. Select the Inherit credentials from
   AWS role check box and the Use
   SSE-KMS encryption
3. Enter the access credentials of the AWS account to be used.
   * If allowed by the security policy of your organization, in the Access Key and the Secret Key fields, enter the credentials.

     If you do not know the credentials to be used, contact the administrator of your AWS system or check [Getting Your AWS Access
     Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html) from the AWS documentation.
   * If the security policy of your organization does not allow you to expose the credentials in a client application, select Inherit credentials from AWS role to obtain the role-based temporary AWS security credentials from your EMR instance metadata. An IAM role must have been specified to associate with this EMR instance.

     For further information about using an IAM role to grant permissions, see [Using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) from the AWS documentation.
4. Select Use SSE encryption check box to enable the Job to verify and use the SSE-KMS encryption service of your cluster.
5. In the Bucket name field, enter the name of the bucket to be used to store the sample data. This bucket must have existed when you launch your Job. For example, enter `my_bucket/my_folder`.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-defining-emr-connection-parameters-spark-batch-component-enter -->
# Defining the EMR connection parameters

Last updated: 9/30/2026

Complete the EMR connection configuration in the Spark
configuration tab of the Run view of your Job.
This configuration is effective on a per-Job basis.

The information in this section is only for users who have subscribed to
Talend Data Fabric
or to any Talend product
with Big Data.

## Procedure

1. Enter the basic configuration information:

   | Use local timezone | Select this check box to let Spark use the local time zone provided by the system. Information noteNote: * If you clear this check box, Spark use UTC time zone. * Some components also have the Use local timezone for   date check box. If you clear the check box from the   component, it inherits time zone from the Spark configuration. |
   | Use dataset API in migrated components | Select this check box to let the components use Dataset (DS) API instead of Resilient Distributed Dataset (RDD) API: * If you select the check box, the components inside the Job run with   DS which improves performance. * If you clear the check box, the components inside the Job run with   RDD which means the Job remains unchanged. This ensures the backwards   compatibility. This check box is selected by default, but if you import a Job from 7.3 backwards, the check box will be cleared as those Jobs run with RDD.  Information noteImportant: If your Job contains tDeltaLakeInput and tDeltaLakeOutput components, you must select this check box. |
   | Use timestamp for dataset components | Select this check box to use java.sql.Timestamp for dates. Information noteNote: If you leave this check box clear, java.sql.Timestamp or java.sql.Date can be used depending on the pattern. |
2. Enter the basic connection information to EMR:

   | Yarn client | Talend Studio runs the Spark driver to orchestrate how the Job should be performed and then send the orchestration to the Yarn service of a given Hadoop cluster so that the Resource Manager of this Yarn service requests execution resources accordingly.  If you are using the Yarn client mode, you need to set the following parameters in their corresponding fields (if you leave the check box of a service clear, then at runtime, the configuration about this parameter in the Hadoop cluster to be used will be ignored):  * In the Resource managerUse datanode   field, enter the address of the ResourceManager service of the Hadoop cluster to   be used. * Select the Set resourcemanager   scheduler address check box and enter the Scheduler address in   the field that appears. * Select the Set jobhistory   address check box and enter the location of the JobHistory   server of the Hadoop cluster to be used. This allows the metrics information of   the current Job to be stored in that JobHistory server. * Select the Set staging   directory check box and enter this directory defined in your   Hadoop cluster for temporary files created by running programs. Typically, this   directory can be found under the *yarn.app.mapreduce.am.staging-dir* property in the configuration files   such as *yarn-site.xml* or *mapred-site.xml* of your distribution. * If you are accessing the Hadoop cluster running with Kerberos security,   select this checkbox, then, enter the Kerberos principal names for the Resource   Manager service and the Job History service in the displayed fields. This enables   you to use your username to authenticate against the credentials stored in Kerberos.   These principals can be found in the configuration files of your distribution, such   as in *yarn-site.xml* and in *mapred-site.xml*.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains   pairs of Kerberos principals and encrypted keys. You need to enter the principal to   be used in the Principal field and the access   path to the keytab file itself in the Keytab   field. This keytab file must be stored in the machine in which your Job actually   runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily   the one a principal designates but must have the right to read the keytab file being   used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this   situation, ensure that *user1* has the right to read the keytab   file to be used. * The User name field is available when you   are not using Kerberos to authenticate. In the User   name field, enter the login username for your distribution. If you leave   it empty, the username of the machine hosting Talend Studio will   be used. * If the Spark cluster cannot recognize the machine in which the Job is   launched, select this Define the driver hostname or IP   address check box and enter the host name or the IP address of   this machine. This allows the Spark master and its workers to recognize this   machine to find the Job and thus its driver.  Note that in this situation, you also need to add the name and the IP   address of this machine to its *host* file. |
   | Yarn cluster | The Spark driver runs in your Yarn cluster to orchestrate how the Job should be performed.  If you are using the Yarn cluster mode, you need to define the following parameters in their corresponding fields (if you leave the check box of a service clear, then at runtime, the configuration about this parameter in the Hadoop cluster to be used will be ignored):  * In the Resource managerUse datanode   field, enter the address of the ResourceManager service of the Hadoop cluster to   be used. * Select the Set resourcemanager   scheduler address check box and enter the Scheduler address in   the field that appears. * Select the Set jobhistory   address check box and enter the location of the JobHistory   server of the Hadoop cluster to be used. This allows the metrics information of   the current Job to be stored in that JobHistory server. * Select the Set staging   directory check box and enter this directory defined in your   Hadoop cluster for temporary files created by running programs. Typically, this   directory can be found under the *yarn.app.mapreduce.am.staging-dir* property in the configuration files   such as *yarn-site.xml* or *mapred-site.xml* of your distribution. * Set path to custom Hadoop   configuration JAR: if you are using   connections defined in Repository to   connect to your Cloudera or Hortonworks cluster, you can   select this check box in the   Repository wizard and in the   field that is displayed, specify the path to the JAR file   that provides the connection parameters of your Hadoop   environment. Note that this file must be accessible from the   machine where you Job is launched.  This kind of Hadoop configuration JAR file is   automatically generated when you build a big data Job from Talend Studio. This JAR file is by default named with this   pattern: ```   hadoop-conf-[name_of_the_metadata_in_the_repository]_[name_of_the_context].jar   ``` You   can also download this JAR file from the web console of your cluster or   simply create a JAR file yourself by putting the configuration files in   the root of your JAR file. For example: ```   hdfs-sidt.xml   core-site.xml   ```  The parameters from your custom JAR file override the parameters   you put in the Spark configuration field.   They also override the configuration you set in the   configuration components such as   tHDFSConfiguration or   tHBaseConfiguration when the related   storage system such as HDFS, HBase or Hive are native to Hadoop.   But they do not override the configuration set in the   configuration components for the third-party storage system such   as tAzureFSConfiguration. * If you are accessing the Hadoop cluster running with Kerberos security,   select this checkbox, then, enter the Kerberos principal names for the Resource   Manager service and the Job History service in the displayed fields. This enables   you to use your username to authenticate against the credentials stored in Kerberos.   These principals can be found in the configuration files of your distribution, such   as in *yarn-site.xml* and in *mapred-site.xml*.  If you need to use a Kerberos keytab file to log in, select Use a keytab to authenticate. A keytab file contains   pairs of Kerberos principals and encrypted keys. You need to enter the principal to   be used in the Principal field and the access   path to the keytab file itself in the Keytab   field. This keytab file must be stored in the machine in which your Job actually   runs, for example, on a Talend JobServer.  Note that the user that executes a keytab-enabled Job is not necessarily   the one a principal designates but must have the right to read the keytab file being   used. For example, the username you are using to execute a Job is *user1* and the principal to be used is *guest*; in this   situation, ensure that *user1* has the right to read the keytab   file to be used. * The User name field is available when you   are not using Kerberos to authenticate. In the User   name field, enter the login username for your distribution. If you leave   it empty, the username of the machine hosting Talend Studio will   be used. * Select the Wait for the Job to   complete check box to make Talend Studio or,   if you use Talend JobServer,   your Job JVM keep monitoring the Job until the execution of the Job is over. By   selecting this check box, you actually set the   spark.yarn.submit.waitAppCompletion property to be true.   While it is generally useful to select this check box when running a Spark Batch Job,   it makes more sense to keep this check box clear when running a Spark Streaming   Job. |

   Ensure that the username in the Yarn
   client mode is the same one you put in
   tS3Configuration, the component used to provide S3 connection
   information to Spark.
3. With the Yarn client mode, the Property type list is displayed to allow you to select an
   established Hadoop connection from the Repository, on
   the condition that you have created this connection in the Repository. Then Talend Studio will
   reuse that set of connection information for this Job.
4. If you need to launch from Windows, it is recommended to specify where
   the *winutils.exe* program to be used is stored.

   * If you know where to find your *winutils.exe* file and you want to use it, select the Define the Hadoop home directory check box
     and enter the directory where your *winutils.exe* is
     stored.
   * Otherwise, leave this check box clear, Talend Studio generates one by itself and automatically uses it for this Job.
5. In the Spark "scratch" directory
   field, enter the directory in which Talend Studio
   stores in the local system the temporary files such as the jar files to be
   transferred. If you launch the Job on Windows, the default disk is *C:*. As a result, if you leave */tmp* in this field, this
   directory is *C:/tmp*.

## Results

* After the connection is configured, you can tune
  the Spark performance, although not required, by following the process explained in:
  + [Tuning Spark for Apache Spark Batch Jobs](/talend/r/en-US/8.0/components/spark-batch/tuning-spark-for-apache-spark-batch-jobs-spark-batch-component) for Spark Batch Jobs.
  + [Tuning Spark for Apache Spark Streaming Jobs](/talend/r/en-US/8.0/components/spark-streaming/tuning-spark-for-apache-spark-streaming-jobs-spark-stream-component) for Spark Streaming Jobs.
* It is recommended to activate the Spark logging and
  checkpointing system in the Spark configuration tab of the Run view of your Spark
  Job, in order to help debug and resume your Spark Job when issues arise:
  + [Logging and checkpointing the activities of your Apache Spark Job](/talend/r/en-US/8.0/components/spark-batch/logging-and-checkpointing-activities-of-your-apache-spark-job-spark-batch-component-if-you).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-designing-flow-of-data-to-write-and-encrypt-onto-emr-in -->
# Designing the flow of the data to write and encrypt onto EMR

Last updated: 9/30/2026

Link the components to construct the data flow.

## Procedure

1. In the Integration
   perspective of Talend Studio,
   create an empty Spark Batch Job from the Job Designs node in
   the Repository tree view.
2. In the workspace, enter the name of the component to be used and select this
   component from the list that appears. In this scenario, the components are
   tHDFSConfiguration (labeled `emr_hdfs`), tS3Configuration, tFixedFlowInput, tAggregateRow and tFileOutputParquet.

   The tFixedFlowInput component is used to load
   the sample data into the data flow. In the real-world practice, use the input component specific to the data format or the source system to be used instead of tFixedFlowInput.
3. Connect tFixedFlowInput, tAggregateRow and
   tFileOutputParquet using the Row > Main link.
4. Leave the tHDFSConfiguration component and the tS3Configuration component alone
   without any connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-loading-sample-data-about-street-incidents-to-job. -->
# Loading the sample data about street incidents to the Job

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display its
   Basic settings view.

   ### Example
2. Click the [...] button next to Edit
   Schema to open the schema editor.

   ### Example
3. Click the [+] button to add four columns, namely
   `id`, `address`,
   `incident_type` and `description`.
4. Click Ok to close the schema editor and accept
   propagating the changes when prompted by the system.
5. In the Mode area, select the Use Inline Content(delimited file) radio button to display the Content area and enter the sample data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-running-job-to-write-kms-encrypted-data-to-emr-press -->
# Running the Job to write KMS encrypted data to EMR

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. In the Run tab, click Run to execute the Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3configuration-thdfsconfiguration-tfixedflowinput-tfileoutputparquet-writing-aggregated-data-about-street-incidents-to-emr -->
# Writing the aggregated data about street incidents to EMR

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileOutputParquet component to
   open its Component view.

   ### Example
2. Select the Define a storage
   configuration component check box and then select the tS3Configuration component you configured in the
   previous steps.
3. Click Sync columns to
   ensure that tFileOutputParquet retrieve the
   schema from the output side of tAggregateRow.
4. In the Folder/File
   field, enter the name of the folder to be used to store the aggregated data in
   the S3 bucket specified in tS3Configuration. For example,
   enter /sample\_user, then at runtime, the folder called
   `sample_user` at the root of the bucket is used to
   store the output of your Job.
5. From the Action
   drop-down list, select Create if the
   folder to be used does not exist yet in the bucket to be used; if this folder
   already exists, select Overwrite.
6. Click Run to open its view and then click the
   Spark Configuration tab to display its view
   for configuring the Spark connection.
7. Select the Use local mode check box to test your Job locally before eventually submitting it to the remote Spark cluster.

   In local mode, Talend Studio
   builds the Spark environment in itself on the fly in order to run the Job in. Each
   processor of the local machine is used as a Spark worker to perform the
   computations.
8. In this mode, your local file system is used; therefore, deactivate the
   configuration components such as tS3Configuration or
   tHDFSConfiguration that provides connection
   information to a remote file system, if you have placed these components
   in your Job.
9. In the Component view of tFileOutputParquet, change the file path in the Folder/File field to a local directory and adapt the action to be taken on the Action drop-down list, that is to say, creating a new folder or overwriting the existing one.
10. On the Run tab, click Basic
    Run and in this view, click Run to execute your Job locally to test its design
    logic.
11. When your Job runs successfully, clear the Use local
    mode check box in the Spark Configuration
    view of the Run tab, then in the design workspace of your
    Job, activate the configuration components and revert the changes you just made
    in tFileOutputParquet for the local test.
