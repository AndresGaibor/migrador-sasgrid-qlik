<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3put · versión 8.0 -->
# tS3Put

Last updated: 9/30/2026

Uploads data onto Amazon S3 from a local file or from cache memory via the
streaming mode.

## tS3Put Standard properties

These properties are used to configure tS3Put running in the Standard Job framework.

The Standard
tS3Put component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Credential provider | Specify the way to obtain AWS security credentials.   * Static credentials: Use access   key and secret key as the AWS security   credentials. * Inherit credentials from AWS role: Obtain AWS   security credentials from your EMR instance metadata. To use this option,   the Amazon EMR cluster must be started and your Job must be running on this   cluster. For more information, see [Using an IAM Role to Grant Permissions to Applications   Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). This option enables you to   develop your Job without having to put any AWS keys in the Job, thus easily   comply with the security policy of your organization. * Web identity token: Use Web token for establishing   the Amazon S3 connection. * Profile credentials or inherit from AWS role: Use   credentials stored in a file (known as profile configuration file) as the   AWS security credentials or inherit AWS security credentials from the AWS   role.  AWS security credentials can be grouped in profiles in profile   configuration files. A profile configuration file can contain one or   multiple profiles. You can optionally specify the profile configuration   file in the Profile path field and specify the   profile to be used in the Profile name field.  If the Profile path field and the   Profile name filed are left empty,   <user folder>/.aws/credentials will be used   as the profile configuration file and the profile named   default will be used.  In cases of EC2 instances, if the profile (the specified or the default profile) does not exist,   the component will try to inherit the AWS security credentials from the   AWS role.   This option can work as a dynamic parameter and be assigned a value using a context variable.  Information noteNote: tRedshiftBulkExec, tRedshiftOutputBulk, and tRedshiftOutputBulkExec support S3 connections that are established with Credential Provider being Static Credentials or Inherit credentials from AWS role only. |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session.  Ensure that access to this role has been granted to your user account by the trust policy associated to this role. If you are not certain about this, ask the owner of this role or your AWS administrator.  * ARN: the Amazon Resource Name (ARN) of the role to   assume. You can find this ARN name on the Summary   page of the role to be used on your AWS portal, for example, this role   ARN could read like   `am:aws:iam::[aws_account_number]:role/[role_name]`. Role session name: enter the   name you want to use to uniquely identify your assumed role session. This   name can contain upper- and lower-case alphanumeric characters with no   spaces. You can also include underscores or any of the following characters:   =,.@-. * Session duration   (minutes): the duration (in minutes) for which you want   the assumed role session to be active. This duration cannot exceed the   maximum duration which your AWS administrator has set. The duration   defaults to 3600 seconds if you give it no value.  For an example about an IAM role and its related policy types, see [Create and Manage AWS IAM Roles](https://aws.amazon.com/blogs/security/now-create-and-manage-aws-iam-roles-more-easily-with-the-updated-iam-console/) from the AWS documentation. |
| Region | Specify the AWS region by selecting or entering a region name between double quotation marks (e.g. *"us-east-1"*). For more information about the AWS Region, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region). |
| Client-side encryption | Select this check box and from the Key type drop-down list displayed, select one of the following three options for encrypting the data on the client-side before sending to Amazon S3. For more information, see [Protecting Data Using Client-Side Encryption](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html).  * KMS-managed customer   master key: use a KMS-managed customer master key (CMK)   for the client-side data encryption. In the Key field, you need   to specify the AWS KMS customer master key ID (CMK ID). * Symmetric Master   Key: use a symmetric master key (256-bit AES secret key)   for the client-side data encryption.    + Algorithm: select the algorithm     associated with the key from the list. By default, there is only     one algorithm named AES.   + Encoding: select the encoding     type associated with the key from the list, either Base64     or X509.   + Key or Key     file: specify the key or the path to the file that     stores the key. * Asymmetric Master   Key: use an asymmetric master key (a 1024-bit RSA key   pair) for the client-side data encryption.    + Algorithm: select the algorithm     associated with the key from the list. By default, there is only     one algorithm named RSA.   + Public key file: specify the     path to the public key file.   + Private key file: specify the     path to the private key file. |
| Bucket | Specify the name of the bucket, namely the top level folder, on the S3 server. If using Express One Zone (S3 directory buckets), you must specify the full bucket name in the format `<bucketBaseName>--<availabilityZoneID>--x-s3`, as required by AWS. For more information, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html).  Information noteNote:  * The support of S3 Express One Zone comes with the 8.0.1-R2026-01   Talend Studio monthly update or a later one delivered by Talend. * Directory buckets require specific permissions. Standard credentials and   proper IAM permissions are required. Refer to [Authorizing Regional endpoint API operations with   IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) for more information. |
| Key | Specify the path to the file that will hold the uploaded data on the S3 server, using slash (/) to separate folders in the path.  * If you only specify a file name in this field, the file will be in the   bucket. * If the path contains folders that do not exist, the folders will be   created. * If the file already exists, it will be overwritten.   Information noteWarning: This field must not start with a slash (/). |
| File or stream | Enter the path to the local file to be uploaded or the input stream from which data will be uploaded.  For an example of how to use stream, see [Reading data from a remote file in streaming mode](/talend/en-US/components/8.0/delimited/tfileinputdelimited-tfilefetch-tsleep-tlogrow-reading-data-from-remote-file-in-streaming-mode-standard-component-this). |
| Server-side encryption | Select this check box to enable server-side encryption with Amazon S3-Managed Encryption Keys (SSE-S3) and use the 256-bit Advanced Encryption Standard (AES-256) cipher to encrypt your data.  For more information about the server-side encryption, see [Protecting Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html). |
| Use KMS | Select this check box to enable server-side encryption with AWS KMS-Managed Keys (SSE-KMS) instead of Amazon S3-Managed Encryption Keys (SSE-S3).  This property is available when the Server-side encryption check box is selected. |
| Server-side encryption ID | Specify your own customer master key (CMK) that is created in the IAM console using AWS Key Management Service for SSE-KMS encryption. If not specified, the default CMK, which is created the first time you add an SSE-KMS encrypted object to the defined bucket in your region, will be used for SSE-KMS encryption.  This property is available when the Use KMS check box is selected. |
| Die on error | This checkbox is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |
| Use a custom region endpoint | Select this checkbox to use a custom endpoint and in the field displayed, specify the URL of the custom endpoint to be used. This option can work as a dynamic parameter and be assigned a value using a context variable. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| Specify STS endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This service allows you to request temporary, limited-privilege credentials for the AWS user authentication. Therefore, you still need to provide the access key and secret key to authenticate the AWS account to be used.  For a list of the STS endpoints you can use, see [AWS Security Token Service](https://docs.aws.amazon.com/general/latest/gr/rande.html#sts_region). For further information about the STS temporary credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). Both articles are from the AWS documentation.  This checkbox is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| Config client | Select this checkbox and specify the client parameter(s) by clicking the [+] button to add as many rows as needed, each row for a client parameter, and then setting the value of the following fields for each parameter:  * Client Parameter: Click the cell   and select the client parameter from the list. * Value: Enter the value for the   selected parameter.   This checkbox is available only when the Use an existing connection checkbox is cleared.  For related information, read [the AWS documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/section-client-configuration.html). |
| Enable Accelerate Mode | Select this checkbox to enable fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. To take it into account, you should enable this acceleration mode on the S3 bucket in advance. This option can work as a dynamic parameter and be assigned a value using a context variable. |
| Multipart threshold (MB) | Specify the multipart threshold (in MB). A file will be uploaded in parts if its size is larger than the multipart threshold. Note that this setting has no effect in the streaming mode. |
| Part size (Mb) | Specify the part size (in MB) when uploading an object in parts. Part size is in the range 5MB to 5GB. A value less than `5` uploads the object with the part size of 5MB. For an object that is less than 5GB in size, you can have it uploaded without being divided into parts by setting this option to a large enough value.  For information about S3 multipart upload, see [Multipart Upload Overview](http://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html). |
| Canned access control | Select an option from the drop-down list to grant a predefined permission for the current resource. See [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) for information about canned ACL. |
| Enable object lock | Select this option to enable the Amazon S3 Object lock feature. With this option enabled, you need also to select a retention mode (Governance or Compliance) from the Retention mode dropdown list and set a retention period in the Retention period field.  For information about the Amazon S3 Object lock feature, retention mode, and retention period, see [Protecting data with Amazon S3 Object Lock](https://aws.amazon.com/blogs/storage/protecting-data-with-amazon-s3-object-lock/). |
| Set object tags | Select this checkbox to set object tags in the form of key-value pairs. These tags will be added to S3 objects when uploading them to the predefined bucket. For more information, see [Categorizing your storage using tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html). |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used alone or with other S3 components, e.g. tS3Connection. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Copying an S3 object from one bucket to another](ts3copy-ts3connection-tlogrow-copying-s3-object-from-one-bucket-to-another-standard-component-this)
* [Exchange files with Amazon S3](ts3put-ts3get-ts3connection-exchange-files-with-amazon-s3-standard-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-exchange-files-with-amazon-s3-standard-component-in-this -->
# Exchange files with Amazon S3

Last updated: 9/30/2026

In this scenario, tS3Put is used to send a
file to the Amazon S3 server while tS3Get is used to get
that file.

### In this section

* [Linking the components](/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-executing-job-standard-component-press)

**Related reference**  

* [tS3Connection](ts3connection "Establishes a connection to Amazon S3 to store and retrieve data.")
* [tS3Put](ts3put "Uploads data onto Amazon S3 from a local file or from cache memory via the streaming mode.")
* [tS3Get](ts3get "Retrieves a file from Amazon S3.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tS3Connection to open its
   Basic settings view.
2. In the Access Key and Secret Key fields, enter the authentication
   credentials.
3. Double-click tS3Put to open its Basic settings view.
4. Select the Use existing connection check
   box to reuse the connection.
5. In the Bucket field, enter the bucket
   name.
6. In the Key field, enter the name of the
   file to be saved on the S3 server.
7. In the File field, enter the file to be
   uploaded to the S3 server.
8. Double-click tS3Get to open its Basic settings view.
9. Select the Use existing connection check
   box to reuse the connection.
10. In the Bucket field, enter the bucket
    name.
11. In the Key field, enter the name of the
    file to be retrieved from the S3 server.
12. In the File field, enter the local name
    of the retrieved file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.
3. Go to the S3 web console.

   As shown above, the file has been put on to the S3 server.
4. Refresh the S3 Browser client.

   This shows that the S3 Put action was performed successfully.
5. Go to the folder where the retrieved file is saved locally.

   As shown above, the remote file is retrieved to the local disk, proof that
   the S3 Get action was performed successfully.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tS3Connection, tS3Put and tS3Get onto the
   workspace.
2. Link tS3Connection to tS3Put using the OnSubjobOk trigger.
3. Link tS3Put to tS3Get using the OnSubjobOk
   trigger.
