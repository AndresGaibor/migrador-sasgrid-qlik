<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy · versión 8.0 -->
# tS3Copy

Last updated: 9/30/2026

Copies an Amazon S3 object from a source bucket to a destination
bucket.

## tS3Copy Standard properties

These properties are used to configure tS3Copy running in the Standard Job framework.

The Standard
tS3Copy component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Credential provider | Specify the way to obtain AWS security credentials.   * Static credentials: Use access   key and secret key as the AWS security   credentials. * Inherit credentials from AWS role: Obtain AWS   security credentials from your EMR instance metadata. To use this option,   the Amazon EMR cluster must be started and your Job must be running on this   cluster. For more information, see [Using an IAM Role to Grant Permissions to Applications   Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). This option enables you to   develop your Job without having to put any AWS keys in the Job, thus easily   comply with the security policy of your organization. * Web identity token: Use Web token for establishing   the Amazon S3 connection. * Profile credentials or inherit from AWS role: Use   credentials stored in a file (known as profile configuration file) as the   AWS security credentials or inherit AWS security credentials from the AWS   role.  AWS security credentials can be grouped in profiles in profile   configuration files. A profile configuration file can contain one or   multiple profiles. You can optionally specify the profile configuration   file in the Profile path field and specify the   profile to be used in the Profile name field.  If the Profile path field and the   Profile name filed are left empty,   <user folder>/.aws/credentials will be used   as the profile configuration file and the profile named   default will be used.  In cases of EC2 instances, if the profile (the specified or the default profile) does not exist,   the component will try to inherit the AWS security credentials from the   AWS role.   This option can work as a dynamic parameter and be assigned a value using a context variable.  Information noteNote: tRedshiftBulkExec, tRedshiftOutputBulk, and tRedshiftOutputBulkExec support S3 connections that are established with Credential Provider being Static Credentials or Inherit credentials from AWS role only. |
| Assume Role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session.  Ensure that access to this role has been granted to your user account by the trust policy associated to this role. If you are not certain about this, ask the owner of this role or your AWS administrator.  * ARN: the Amazon Resource Name (ARN) of the role to   assume. You can find this ARN name on the Summary   page of the role to be used on your AWS portal, for example, this role   ARN could read like   `am:aws:iam::[aws_account_number]:role/[role_name]`. Role session name: enter the   name you want to use to uniquely identify your assumed role session. This   name can contain upper- and lower-case alphanumeric characters with no   spaces. You can also include underscores or any of the following characters:   =,.@-. * Session duration   (minutes): the duration (in minutes) for which you want   the assumed role session to be active. This duration cannot exceed the   maximum duration which your AWS administrator has set. The duration   defaults to 3600 seconds if you give it no value.  For an example about an IAM role and its related policy types, see [Create and Manage AWS IAM Roles](https://aws.amazon.com/blogs/security/now-create-and-manage-aws-iam-roles-more-easily-with-the-updated-iam-console/) from the AWS documentation. |
| Region | Specify the AWS region by selecting or entering a region name between double quotation marks (e.g. *"us-east-1"*). For more information about the AWS Region, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region). |
| Bucket | Specify the name of the source bucket that contains the object to be copied. If using Express One Zone (S3 directory buckets), you must specify the full bucket name in the format `<bucketBaseName>--<availabilityZoneID>--x-s3`, as required by AWS. For more information, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html).  Information noteNote:  * The support of S3 Express One Zone comes with the 8.0.1-R2026-01   Talend Studio monthly update or a later one delivered by Talend. * Directory buckets require specific permissions. Standard credentials and   proper IAM permissions are required. Refer to [Authorizing Regional endpoint API operations with   IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) for more information. |
| Source key | Specify the path to the object to be copied. Information noteWarning: This field must not start with a slash (/). |
| Destination Bucket | Specify the name of the destination bucket to which the object will be copied. |
| Destination Key | Specify the path to the destination object, using slash (/) to separate folders in the path. If:   * you only specify a file name in this field, the file will be in the bucket; * the path contains folders that do not exist, the folders will be created; * the file already exists, it will be overwritten.   Information noteWarning: This field must not start with a slash (/). |
| Server-side encryption | Select this check box to enable server-side encryption with Amazon S3-Managed Encryption Keys (SSE-S3) and use the 256-bit Advanced Encryption Standard (AES-256) cipher to encrypt your data.  For more information about the server-side encryption, see [Protecting Data Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html). |
| Use KMS | Select this check box to enable server-side encryption with AWS KMS-Managed Keys (SSE-KMS) instead of Amazon S3-Managed Encryption Keys (SSE-S3).  This property is available when the Server-side encryption check box is selected. |
| Server-side encryption ID | Specify your own customer master key (CMK) that is created in the IAM console using AWS Key Management Service for SSE-KMS encryption. If not specified, the default CMK, which is created the first time you add an SSE-KMS encrypted object to the defined bucket in your region, will be used for SSE-KMS encryption.  This property is available when the Use KMS check box is selected. |
| Die on error | Select this checkbox to stop the execution of the Job when an error occurs. Clear the checkbox to skip any rows on error and complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Use a custom region endpoint | Select this checkbox to use a custom endpoint and in the field displayed, specify the URL of the custom endpoint to be used. This option can work as a dynamic parameter and be assigned a value using a context variable. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| Specify STS endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This checkbox is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| Config client | Select this checkbox and specify the client parameter(s) by clicking the [+] button to add as many rows as needed, each row for a client parameter, and then setting the value of the following fields for each parameter:  * Client Parameter: Click the cell   and select the client parameter from the list. * Value: Enter the value for the   selected parameter.   This checkbox is available only when the Use an existing connection checkbox is cleared.  For related information, read [the AWS documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/section-client-configuration.html). |
| Canned access control | Select an option from the drop-down list to grant a predefined permission for the current resource. See [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) for information about canned ACL. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a standalone component. |

**Related concepts**  

* [Copying an S3 object from one bucket to another](ts3copy-ts3connection-tlogrow-copying-s3-object-from-one-bucket-to-another-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-copying-s3-object-from-one-bucket-to-another-standard-component-this -->
# Copying an S3 object from one bucket to another

Last updated: 9/30/2026

This scenario describes a Job that uploads a new object to an existing empty S3 bucket
*bucket-src*, then copies the object from
the bucket *bucket-src* to another existing empty
S3 bucket *bucket-dst*, finally lists the object in
the bucket *bucket-dst* to see whether the object
is successfully copied.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-setting-up-job-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tS3Copy](ts3copy "Copies an Amazon S3 object from a source bucket to a destination bucket.")
* [tS3Connection](ts3connection "Establishes a connection to Amazon S3 to store and retrieve data.")
* [tS3Put](ts3put "Uploads data onto Amazon S3 from a local file or from cache memory via the streaming mode.")
* [tS3List](ts3list "Lists the files on Amazon S3 based on the bucket/file prefix settings.")

**Related information**  

* [tIterateToFlow](/talend/en-US/components/8.0/orchestration/titeratetoflow)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Creating a connection to Amazon S3](/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-creating-connection-to-amazon-s3-standard-component)
* [Uploading an object to an Amazon S3 bucket](/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-uploading-object-to-amazon-s3-bucket-standard-component)
* [Copying the uploaded object to another Amazon S3 bucket](/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-copying-uploaded-object-to-another-amazon-s3-bucket-standard-component)
* [Listing the object in the destination bucket](/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-listing-object-in-destination-bucket-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the
   Job.
2. Press F6 to run the
   Job.

   As shown above, the uploaded object has been copied to the
   destination bucket successfully.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-setting-up-job-standard-component-create -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tS3Connection component, a tS3Put component, a tS3Copy component, a
   tS3List component,
   a tIterateToFlow component,
   and a tLogRow component by
   typing their names on the design workspace or dropping them
   from the Palette.
2. Link the tS3List component to
   the tIterateToFlow
   component using a Row >
   Iterate
   connection.
3. Link the tIterateToFlow
   component to the tLogRow
   component using a Row >
   Main
   connection.
4. Link the tS3Connection
   component to the tS3Put
   component using a Trigger >
   On Subjob Ok
   connection.
5. Do the same to link the tS3Put component to the tS3Copy component and the
   tS3Copy component
   to the tS3List
   component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-copying-uploaded-object-to-another-amazon-s3-bucket-standard-component -->
# Copying the uploaded object to another Amazon S3 bucket

Last updated: 9/30/2026

## Procedure

1. Double-click the tS3Copy
   component to open its Basic
   settings view on the Component tab.
2. Select the Use an existing
   connection check box to reuse the Amazon
   S3 connection information you have defined in the tS3Connection
   component.
3. In the Bucket field in the
   Source
   Configuration area, enter the name of the
   bucket which contains the object to be copied. In this
   example, it is *bucket-src*.
4. In the Key field in the
   Source
   Configuration area, enter the key of the
   object to be copied. In this example, it is *tS3Copy\_icon32\_src.png*.
5. In the Bucket field in the
   Destination
   Configuration area, enter the name of the
   bucket to which the object will be copied. In this example,
   it is the empty one *bucket-dst* that already exists in Amazon
   S3.
6. In the Key field in the
   Destination
   Configuration area, enter the new key for
   the object after being copied to the destination bucket. In
   this example, it is *tS3Copy\_icon32\_dst.png*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-creating-connection-to-amazon-s3-standard-component -->
# Creating a connection to Amazon S3

Last updated: 9/30/2026

## Procedure

1. Double-click the tS3Connection component to open its
   Basic settings view
   on the Component
   tab.
2. In the Access Key and
   Secret Key fields,
   enter the authentication credentials required to access
   Amazon S3.
3. From the Region drop-down
   list, select an AWS region where the object will be uploaded
   and copied. In this example, we keep the default
   setting.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-listing-object-in-destination-bucket-standard-component -->
# Listing the object in the destination bucket

Last updated: 9/30/2026

## Procedure

1. Double-click the tS3List
   component to open its Basic
   settings view on the Component tab.
2. Select the Use an existing
   connection check box to reuse the Amazon
   S3 connection information you have defined in the tS3Connection
   component.
3. Clear the List all buckets
   objects check box, and then click the
   [+] button to add
   one row in the Bucket table
   displayed and set the value for each column. In this
   example, *bucket-dst* for
   the Bucket name column and
   empty value for the Key
   prefix column, this way only the objects
   in the *bucket-dst* bucket
   will be listed.
4. Double-click the tIterateToFlow component to open its
   Basic settings view
   on the Component
   tab.
5. Click the [...] button next
   to Edit schema and in the
   pop-up schema dialog box define the schema by adding one
   column *ObjectList* of
   String type.
6. Click OK to save the changes
   and in the pop-up dialog box click Yes to accept the propagation.
7. Double-click the tLogRow
   component to open its Basic
   settings view on the Component tab.
8. In the Mode area, select
   Table (print values in cells
   of a table) for better readability of the
   result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3copy-ts3connection-tlogrow-uploading-object-to-amazon-s3-bucket-standard-component -->
# Uploading an object to an Amazon S3 bucket

Last updated: 9/30/2026

## Procedure

1. Double-click the tS3Put
   component to open its Basic
   settings view on the Component tab.
2. Select the Use an existing
   connection check box to reuse the Amazon
   S3 connection information you have defined in the tS3Connection
   component.
3. In the Bucket field, enter
   the name of the S3 bucket where the object will be uploaded.
   In this example, it is *bucket-src* that already exists in Amazon
   S3.
4. In the Key field, enter the
   key for the object to be uploaded. In this example, it is
   *tS3Copy\_icon32\_src.png*.
5. In the File field, browse to
   or enter the path to the object to be uploaded. In this
   example, it is *D:/tS3Copy\_icon32.png*.
