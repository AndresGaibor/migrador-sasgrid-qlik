<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3list · versión 8.0 -->
# tS3List

Last updated: 9/30/2026

Lists the files on Amazon S3 based on the bucket/file prefix settings.

## tS3List Standard properties

These properties are used to configure tS3List running in the Standard Job framework.

The Standard
tS3List component belongs to the Cloud family.

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
| List all bucket objects | Select this check box to list all the files on the S3 server. Key prefix: Enter the prefix of files to be listed. This way, only files with that prefix will be listed. |
| Bucket | Click the [+] button to add one or more lines for defining the buckets and file prefixes. Bucket name: Enter the name of the bucket, namely the top level folder, whose files will be listed.  Key prefix: Enter the prefix of files to be listed.  Not available when List all bucket objects is selected. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Use a custom region endpoint | Select this check box to use a custom endpoint and in the field displayed, specify the URL of the custom endpoint to be used. This option can work as a dynamic parameter and be assigned a value using a context variable. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| Specify STS endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This service allows you to request temporary, limited-privilege credentials for the AWS user authentication. Therefore, you still need to provide the access key and secret key to authenticate the AWS account to be used.  For a list of the STS endpoints you can use, see [AWS Security Token Service](https://docs.aws.amazon.com/general/latest/gr/rande.html#sts_region). For further information about the STS temporary credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). Both articles are from the AWS documentation.  This checkbox is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| Config client | Select this check box and specify the client parameter(s) by clicking the [+] button to add as many rows as needed, each row for a client parameter, and then setting the value of the following fields for each parameter:  * Client parameter: Click the cell   and select the client parameter from the list. * Value: Enter the value for the   selected parameter.   This check box is available only when the Use an existing connection check box is cleared.  For related information, read [the AWS documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/section-client-configuration.html). |
| Get owner information | Select this check box to retrieve the owner of the S3 bucket. To use this operation, you must have s3:GetObjectAcl permissions. |

## Global Variables

| Variables | Description |
| --- | --- |
| CURRENT\_BUCKET\_NAME | The current bucket name. This is a Flow variable and it returns a string. |
| CURRENT\_ETAG | The hexadecimal MD5 Hash value (128-bit) of the content of the current object. This is a Flow variable and it returns a string. |
| CURRENT\_KEY | The current key. This is a Flow variable and it returns a string. |
| CURRENT\_LASTMODIFIED | The date the current file was last modified. This is a Flow variable and it returns a date (in the format of MM-DD-YYYY). |
| CURRENT\_OWNER | The owner name of the current object. This is a Flow variable and it returns a string. |
| CURRENT\_OWNER\_ID | The owner's AWS ID of the current object. This is a Flow variable and it returns a string. |
| CURRENT\_SIZE | The size of the current file (in bytes). This is a Flow variable and it returns an integer number. |
| CURRENT\_STORAGECLASS | The storage class used for the current object. This is a Flow variable and it returns a string. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |
| NB\_BUCKET | The number of buckets. This is an After variable and it returns an integer. |
| NB\_BUCKET\_OBJECT | The number of objects in all buckets. This is an After variable and it returns an integer. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used alone or with other S3 components, e.g. tS3Delete. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Copying an S3 object from one bucket to another](ts3copy-ts3connection-tlogrow-copying-s3-object-from-one-bucket-to-another-standard-component-this)
* [Listing files with the same prefix from a bucket](ts3list-ts3connection-tlogrow-listing-files-with-same-prefix-from-bucket-standard-component-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3list-ts3connection-tlogrow-listing-files-with-same-prefix-from-bucket-standard-component-in-this -->
# Listing files with the same prefix from a bucket

Last updated: 9/30/2026

In this scenario, tS3List is used to
list all the files in a bucket which have the same prefix.

There are such files in this bucket:

For how to create a bucket and put files into it, see [Verifing the absence of a bucket, creating it and listing all the
S3 buckets](/talend/en-US/components/8.0/amazon-s3/ts3bucketlist-ts3bucketexist-tlogrow-verifing-absence-of-bucket-creating-it-and-listing-all-s3-buckets-standard-component-in-this)  and [Exchange files with Amazon S3](/talend/en-US/components/8.0/amazon-s3/ts3put-ts3get-ts3connection-exchange-files-with-amazon-s3-standard-component-in-this).

### In this section

* [Linking the components](/talend/en-US/components/8.0/amazon-s3/ts3list-ts3connection-tlogrow-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/amazon-s3/ts3list-ts3connection-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/amazon-s3/ts3list-ts3connection-tlogrow-executing-job-standard-component-press)

**Related reference**  

* [tS3Connection](ts3connection "Establishes a connection to Amazon S3 to store and retrieve data.")
* [tS3List](ts3list "Lists the files on Amazon S3 based on the bucket/file prefix settings.")
* [tS3Close](ts3close "Shuts down a connection to Amazon S3, thus releasing the network resources.")

**Related information**  

* [tIterateToFlow](/talend/en-US/components/8.0/orchestration/titeratetoflow)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3list-ts3connection-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tS3Connection to open its
   Basic settings view.
2. In the Access Key and Secret Key fields, enter the authentication
   credentials.
3. Double-click tS3List to open its
   Basic settings view.
4. Select the Use existing connection check
   box to reuse the connection.
5. In the Bucket area, click the [+] button to add one line.
6. In the Bucket name and Key prefix fields, enter the bucket name and file
   prefix.

   This way, only files with the specified prefix will be listed.
7. Double-click tIterateToFlow to open its
   Basic settings view.
8. Click Edit schema to open the schema
   editor. 

   Click the [+] button to add one column,
   namely *file\_list* of the String
   type.

   Click Ok to validate the setup and close
   the schema editor.
9. In the Mapping area, press Ctrl + Space in the Value field to choose the variable *tS3List\_1\_CURRENT\_KEY*.
10. Double-click tLogRow to open its
    Basic settings view.

    Select Table (print values in cells of a
    table) for a better display of the results.
11. Double-click tS3Close to open its
    Basic settings view.

    There is no need to select a connection component as the only one is
    selected by default.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3list-ts3connection-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, only the files with the prefix *"in"* are listed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3list-ts3connection-tlogrow-linking-components-standard-component-drop -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Drop tS3Connection, tS3List, tIterateToFlow,
   tLogRow and tS3Close onto the workspace.
2. Link tS3Connection to tS3List using the OnSubjobOk trigger.
3. Link tS3List to tIterateToFlow using the Row >
   Iterate connection.
4. Link tIterateToFlow to tLogRow using the Row >
   Main connection.
5. Link tS3List to tS3Close using the OnSubjobOk trigger.
