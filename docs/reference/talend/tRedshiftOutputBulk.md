<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftoutputbulk · versión 8.0 -->
# tRedshiftOutputBulk

Last updated: 9/30/2026

Prepares a delimited/CSV file that can be used by tRedshiftBulkExec to feed Amazon Redshift.

The tRedshiftOutputBulk and tRedshiftBulkExec components can be used together in a two step process
to load data to Amazon Redshift from a delimited/CSV file on Amazon S3. In the first
step, a delimited/CSV file is generated. In the second step, this file is used in the
INSERT statement used to feed Amazon Redshift. These two steps are fused together in the
tRedshiftOutputBulkExec component. The advantage of
using two separate steps is that the data can be transformed before it is loaded to
Amazon Redshift.

This component receives data from the preceding component,
generates a single delimited/CSV file and then uploads the file to
Amazon S3.

## tRedshiftOutputBulk Standard properties

These properties are used to configure tRedshiftOutputBulk running in the Standard Job framework.

The Standard
tRedshiftOutputBulk component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Data file path at local | Specify the local path to the file to be generated.  Note that the file is generated on the same machine where Talend Studio is installed or where the Job using this component is deployed. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Compress the data file | Select this check box and select a compression type from the list displayed to compress the data file.  This check box disappears when the Append the local file check box is selected. |
| Encrypt | Select this check box to generate and upload the data file to Amazon S3 using client-side encryption. In the Encryption key field displayed, enter the encryption key used to encrypt the file.  By default, this check box is cleared and the data file will be uploaded to Amazon S3 using server-side encryption.  Information noteNote: This option is available when Use an existing S3 connection is not selected.  For more information about the client-side and server-side encryption, see [Protecting Data Using Encryption](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html). |
| Use an existing S3 connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Credential provider | Specify the way to obtain AWS security credentials: Static credentials or Inherit credentials from AWS role.   * Static credentials: Use access key   and secret key as the AWS security credentials. * Inherit credentials from AWS role: Obtain AWS security   credentials from your EMR instance metadata. To use this option, the Amazon EMR   cluster must be started and your Job must be running on this cluster. For more   information, see [Using an IAM Role to Grant Permissions to Applications   Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). This option enables you to develop   your Job without having to put any AWS keys in the Job, thus easily comply with   the security policy of your organization. |
| Access Key | Specify the Access Key ID that uniquely identifies an AWS Account. For how to get your Access Key and Access Secret, visit [Getting Your AWS Access Keys](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/get-aws-keys.html).  Information noteNote: This option is available when Use an existing S3 connection is not selected or `Inherit credentials from AWS role` is not selected from the Credential provider drop-down list. |
| Secret Key | Specify the Secret Access Key, constituting the security credentials in combination with the access Key.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  Information noteNote: This option is available when Use an existing S3 connection is not selected or `Inherit credentials from AWS role` is not selected from the Credential provider drop-down list. |
| Assume Role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session.  Ensure that access to this role has been granted to your user account by the trust policy associated to this role. If you are not certain about this, ask the owner of this role or your AWS administrator.  Information noteNote: This option is available when Use an existing S3 connection is not selected.  * ARN: the Amazon Resource Name (ARN) of the role to   assume. You can find this ARN name on the Summary   page of the role to be used on your AWS portal, for example, this role   ARN could read like   `am:aws:iam::[aws_account_number]:role/[role_name]`. Role session name: enter the   name you want to use to uniquely identify your assumed role session. This   name can contain upper- and lower-case alphanumeric characters with no   spaces. You can also include underscores or any of the following characters:   =,.@-. * Session duration   (minutes): the duration (in minutes) for which you want   the assumed role session to be active. This duration cannot exceed the   maximum duration which your AWS administrator has set. The duration   defaults to 3600 seconds if you give it no value.  For an example about an IAM role and its related policy types, see [Create and Manage AWS IAM Roles](https://aws.amazon.com/blogs/security/now-create-and-manage-aws-iam-roles-more-easily-with-the-updated-iam-console/) from the AWS documentation. |
| Region | Specify the AWS region by selecting or entering a region name between double quotation marks (e.g. *"us-east-1"*). For more information about the AWS Region, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).  Information noteNote: This option is available when Use an existing S3 connection is not selected. |
| Bucket | Type in the name of the Amazon S3 bucket, namely the top level folder, to which the file is uploaded.  The bucket and the Redshift database to be used must be in the same region on Amazon. This could avoid the S3ServiceException errors known to Amazon. For further information about these errors, see [S3ServiceException Errors](https://docs.aws.amazon.com/redshift/latest/dg/s3serviceexception-error.html). |
| Key | Type in an object key to assign to the file uploaded to Amazon S3. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Field Separator | Enter the character used to separate fields. |
| Text enclosure | Select the character in a pair of which the fields are enclosed. |
| Delete local file after putting it to s3 | Select this check box to delete the local file after being uploaded to Amazon S3. By default, this check box is selected. |
| Create directory if not exists | Select this check box to create the directory specified in the Data file path at local field if it does not exist. By default, this check box is selected. |
| Encoding | Select an encoding type for the data in the file to be generated. |
| Config client | Select this check box to configure client parameters for Amazon S3. Click the [+] button below the table displayed to add as many rows as needed, each row for a client parameter, and set the following attributes for each parameter:   * Client Parameter: Click the cell and   select a parameter from the drop-down list. * Value: Enter the value for the   corresponding client parameter.   For information about S3 client parameters, go to [Client Configuration](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/section-client-configuration.html). |
| STS Endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This checkbox is available only when the Assume role checkbox is selected. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with the tRedshiftBulkExec component to feed Amazon Redshift with a delimited/CSV file. Used together they offer gains in performance while feeding Amazon Redshift. |

**Related concepts**  

* [Loading/unloading data to/from Amazon S3](tredshiftinput-tredshiftbulkexec-ts3get-loading-unloading-data-to-from-amazon-s3-standard-component-this)
