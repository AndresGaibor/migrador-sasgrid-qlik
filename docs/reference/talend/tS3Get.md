<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3get · versión 8.0 -->
# tS3Get

Last updated: 9/30/2026

Retrieves a file from Amazon S3.

## tS3Get Standard properties

These properties are used to configure tS3Get running in the Standard Job framework.

The Standard
tS3Get component belongs to the Cloud family.

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
| Bucket | Specify the name of the source bucket, namely the top level folder, on the S3 server. If using Express One Zone (S3 directory buckets), you must specify the full bucket name in the format `<bucketBaseName>--<availabilityZoneID>--x-s3`, as required by AWS. For more information, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html).  Information noteNote:  * The support of S3 Express One Zone comes with the 8.0.1-R2026-01   Talend Studio monthly update or a later one delivered by Talend. * Directory buckets require specific permissions. Standard credentials and   proper IAM permissions are required. Refer to [Authorizing Regional endpoint API operations with   IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) for more information. |
| Key | Specify the path to the file saved on the S3 server. Information noteWarning: This field must not start with a slash (/). |
| File | Enter the name of the file to be saved locally. |
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
| Enable accelerate mode | Select this checkbox to enable fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. To take it into account, you should enable this acceleration mode on the S3 bucket in advance. |
| Use Select | Select this checkbox to customize the way to retrieve a file from Amazon S3. * File Type: Type of the file to be retrieved * Query: Query to be used for retrieving the   file. * Compressed Type: Compression type of the file to   be compressed * Header Type and Field   Separator: Header type and field separator to be used for   retrieving the file |
| S3 CSV Input Options | Select this checkbox to configure the CSV file input settings. This property is available only when you select the Use Select checkbox. |
| Configure Output | Select this checkbox to configure the settings used to output files. This property is available only when you select the Use Select checkbox. |
| JSON Record Delimiter | Set the delimiter used to separate JSON records. This property is available only when you select JSON from the Output Type dropdown list. |
| Add the InputStream in Global variables | Select this checkbox to add InputStream into global variables so that other components in the Job can use this input data. This property is available only when you select the Use Select checkbox. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |
| RECORDS\_INPUTSTREAM | The input stream being processed. This is an After variable and it returns a record. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used alone or with other S3 components, e.g. tS3Connection. Currently, there is no component for directly retrieving data from an S3 object in a standard Job. To retrieve data from an S3 object through a standard Job, you can download the S3 object as a file using the tS3Get component and then retrieve data from the file using a file input component. See [Retrieving data from an S3 object](retrieving-data-from-an-s3-object.html) for related information. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Exchange files with Amazon S3](ts3put-ts3get-ts3connection-exchange-files-with-amazon-s3-standard-component-in-this)
* [Retrieving data from an S3 object in Talend Studio](ts3get-tfileinputdelimited-tlogrow-tlogrow-retrieving-data-from-s3-object-in-studio-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3get-tfileinputdelimited-tlogrow-tlogrow-retrieving-data-from-s3-object-in-studio-standard-component-this -->
# Retrieving data from an S3 object in Talend Studio

Last updated: 9/30/2026

This scenario retrieves data from a CSV file stored in an S3
bucket. This is achieved by first downloading the file using the tS3Get component and then
reading data from the downloaded file using tFileInputDelimited.

The following gives the Job for this purpose.

This scenario retrieves data from the file customers.csv. The following lists the data stored in the CSV
file.

```
1;Griffith Paving and Sealcoatin;talend@apres91;03/11/2006
2;Bill's Dive Shop;511 Maple Ave. Apt.1B;19/11/2004
3;Childress Child Day Care;662 Lyons Circle;16/02/2005
4;Facelift Kitchen and Bath;220 Vine Ave.;22/08/2002
5;Terrinni & Son Auto and Truck;770 Exmoor Rd.;28/06/2001
6;Kermit the Pet Shop;1860 Parkside Ln.;17/08/2003
7;Tub's Furniture Store;807 Old Trail Rd.;27/08/2000
8;Toggle & Myerson Ltd;618 Sheriden rd.;24/03/2006
9;Childress Child Day Care;788 Tennyson Ave.;10/09/2001
10;Elle Hypnosis and Therapy Cent;2032 Northbrook Ct.;11/01/1977
```

### In this section

* [Linking the components](/talend/en-US/components/8.0/amazon-s3/ts3get-tfileinputdelimited-tlogrow-tlogrow-linking-components-standard-component-launch)
* [Configuring the components](/talend/en-US/components/8.0/amazon-s3/ts3get-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/amazon-s3/ts3get-tfileinputdelimited-tlogrow-tlogrow-executing-job-standard-component-press)

**Related reference**  

* [tS3Get](ts3get "Retrieves a file from Amazon S3.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3get-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tS3Get to
   open its Basic settings view.
   1. Enter your access key and secret key in the
      corresponding fields.
   2. Enter the name of the S3 bucket where the CSV file resides in the Bucket field.
   3. Enter the name of the CSV file in the Key
      field.
   4. Enter the path and the filename which you want to save
      the downloaded file in the File
      field.
   5. Leave other options as they are.

   Information noteNote: All the parameters mentioned above need to be given in double quotation
   marks.
2. Double-click tFileInputDelimited to open its
   Basic settings view.
   1. Click the […]
      button next to Edit schema and
      add four columns in the schema editor: `ID`, type `Integer`; `Name`, type
      `String`; `Address`, type `String`, and `RegTime`, type `Date` and format of `dd/MM/yyyy`.
   2. Click Yes when prompted to propagated the changes. 

      This propagates the schema to the tLogRow
      component.
   3. Enter the path and the filename of the downloaded file in the
      File name/Stream field.

      The path and the filename provided in this filed need to be the same
      as those provided in substep d in the previous step.
   4. Leave other options as they are.
3. Double-click tLogRow to open its
   Basic settings view.

   Select Table (print values in cells of a
   table) for a better display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3get-tfileinputdelimited-tlogrow-tlogrow-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   As shown above, the data in the CSV file is listed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3get-tfileinputdelimited-tlogrow-tlogrow-linking-components-standard-component-launch -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. Launch Talend Studio and
   create an empty Job.
2. Drop tS3Get, tFileInputDelimited, and tLogRow onto the workspace.
3. Link tS3Get to tFileInputDelimited using a Trigger > OnSubjobOK connection.
4. Link tFileInputDelimited to
   tLogRow using a Row > Main
   connection.
