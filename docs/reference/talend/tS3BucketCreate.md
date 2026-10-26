<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-s3/ts3bucketcreate · versión 8.0 -->
# tS3BucketCreate

Last updated: 9/30/2026

Creates a bucket on Amazon S3.

"Bucket" is a term used by AWS for top level folders on S3, which
can contain sub folders and store all your data (objects).

## tS3BucketCreate Standard properties

These properties are used to configure tS3BucketCreate running in the Standard Job framework.

The Standard
tS3BucketCreate component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Credential provider | Specify the way to obtain AWS security credentials.   * Static credentials: Use access   key and secret key as the AWS security   credentials. * Inherit credentials from AWS role: Obtain AWS   security credentials from your EMR instance metadata. To use this option,   the Amazon EMR cluster must be started and your Job must be running on this   cluster. For more information, see [Using an IAM Role to Grant Permissions to Applications   Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). This option enables you to   develop your Job without having to put any AWS keys in the Job, thus easily   comply with the security policy of your organization. * Web identity token: Use Web token for establishing   the Amazon S3 connection. * Profile credentials or inherit from AWS role: Use   credentials stored in a file (known as profile configuration file) as the   AWS security credentials or inherit AWS security credentials from the AWS   role.  AWS security credentials can be grouped in profiles in profile   configuration files. A profile configuration file can contain one or   multiple profiles. You can optionally specify the profile configuration   file in the Profile path field and specify the   profile to be used in the Profile name field.  If the Profile path field and the   Profile name filed are left empty,   <user folder>/.aws/credentials will be used   as the profile configuration file and the profile named   default will be used.  In cases of EC2 instances, if the profile (the specified or the default profile) does not exist,   the component will try to inherit the AWS security credentials from the   AWS role.   This option can work as a dynamic parameter and be assigned a value using a context variable.  Information noteNote: tRedshiftBulkExec, tRedshiftOutputBulk, and tRedshiftOutputBulkExec support S3 connections that are established with Credential Provider being Static Credentials or Inherit credentials from AWS role only. |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session. |
| Region | Specify the AWS region by selecting or entering a region name between double quotation marks (e.g. *"us-east-1"*). For more information about the AWS Region, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region). |
| Bucket | Enter the name of the bucket, namely the top level folder, to create. |
| Die on error | This checkbox is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |
| Use a custom region endpoint | Select this checkbox to use a custom endpoint and in the field displayed, specify the URL of the custom endpoint to be used. This option can work as a dynamic parameter and be assigned a value using a context variable. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| Specify STS endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This checkbox is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| Config client | Select this checkbox and specify the client parameter(s) by clicking the [+] button to add as many rows as needed, each row for a client parameter, and then setting the value of the following fields for each parameter:  * Client parameter: Click the cell   and select the client parameter from the list. * Value: Enter the value for the   selected parameter.   This checkbox is available only when the Use an existing connection check box is cleared.  For related information, read [the AWS documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/section-client-configuration.html). |
| Canned access control | Select an option from the drop-down list to grant a predefined permission for the current resource. See [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) for information about canned ACL. |
| Directory bucket | Select this checkbox to create a directory bucket. When selected, you must specify the desired Availability zone in the field provided. Directory buckets are buckets that exist in a single availability zone for higher performance and lower latency. The list of available zones depends on the selected region. For more information, see [Working with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html), and [S3 Express One Zone Availability Zones and Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Endpoints.html#w895aac16c29c11b7c15).  Information noteNote:  * The support of S3 Express One Zone comes with the 8.0.1-R2026-01   Talend Studio monthly update or a later one delivered by Talend. * Directory buckets require specific permissions. Standard credentials and   proper IAM permissions are required. Refer to [Authorizing Regional endpoint API operations with   IAM](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) for more information. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used alone or with other S3 components, e.g. tS3BucketExist. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Verifing the absence of a bucket, creating it and listing all the S3 buckets](ts3bucketlist-ts3bucketexist-tlogrow-verifing-absence-of-bucket-creating-it-and-listing-all-s3-buckets-standard-component-in-this)
