<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-sqs/tsqsqueueattributes · versión 8.0 -->
# tSQSQueueAttributes

Last updated: 9/30/2026

Gets attributes for a specified Amazon SQS (Simple Queue Service) queue.

## tSQSQueueAttributes Standard properties

These properties are used to configure tSQSQueueAttributes running
in the Standard Job framework.

The Standard tSQSQueueAttributes component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Credential provider | Specify the way to obtain AWS security credentials: Static credentials, Inherit credentials from AWS role, or Provider credentials or inherit from AWS role.   * Static credentials: Use access key   and secret key as the AWS security credentials. * Inherit credentials from AWS role: Obtain AWS security   credentials from your EMR instance metadata. To use this option, the Amazon EMR   cluster must be started and your Job must be running on this cluster. For more   information, see [Using an IAM Role to Grant Permissions to Applications   Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). This option enables you to develop   your Job without having to put any AWS keys in the Job, thus easily comply with   the security policy of your organization. * Provider credentials or inherit from AWS role: Obtain   AWS security credentials from provider credentials or from your EMR instance   metadata. You can specify the profile configuration file in the   Profile path field and specify the profile in the   Profile name field.   Information noteNote: This drop-down list is available only when you have installed the R2023-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session.  Ensure that access to this role has been granted to your user account by the trust policy associated to this role. If you are not certain about this, ask the owner of this role or your AWS administrator.  * ARN: the Amazon Resource Name (ARN) of the role to   assume. You can find this ARN name on the Summary   page of the role to be used on your AWS portal, for example, this role   ARN could read like   `am:aws:iam::[aws_account_number]:role/[role_name]`. Role session name: enter the   name you want to use to uniquely identify your assumed role session. This   name can contain upper- and lower-case alphanumeric characters with no   spaces. You can also include underscores or any of the following characters:   =,.@-. * Session duration   (minutes): the duration (in minutes) for which you want   the assumed role session to be active. This duration cannot exceed the   maximum duration which your AWS administrator has set. The duration   defaults to 3600 seconds if you give it no value.  For an example about an IAM role and its related policy types, see [Create and Manage AWS IAM Roles](https://aws.amazon.com/blogs/security/now-create-and-manage-aws-iam-roles-more-easily-with-the-updated-iam-console/) from the AWS documentation. |
| Region | Specify the AWS region by selecting a region name from the list or entering a region between double quotation marks (for example *"us-east-1"*) in the list. For more information on AWS Regions, see [AWS Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html). |
| Queue (Name or URL) | Specify the name or the URL of the queue whose attribute information will be retrieved. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is read-only and predefined with a couple of columns that describe the attributes for the specified queue. You can click the [...] button next to Edit schema to view its schema. For more information on each attribute, see [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any error and continue the Job execution process. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Use a custom region endpoint | Select this check box to use a custom endpoint and in the field displayed, specify the URL of the custom endpoint to be used. This option can work as a dynamic parameter and be assigned a value using a context variable. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| Specify STS endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This service allows you to request temporary, limited-privilege credentials for the AWS user authentication. Therefore, you still need to provide the access key and secret key to authenticate the AWS account to be used.  For a list of the STS endpoints you can use, see [AWS Security Token Service](https://docs.aws.amazon.com/general/latest/gr/rande.html#sts_region). For further information about the STS temporary credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). Both articles are from the AWS documentation.  This checkbox is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| Config client | Select this check box and in the table displayed specify the client configuration parameters. Click the [+] button below the table to add as many rows as needed, each row for a client configuration parameter, and set the value of the following attributes for each parameter:  * Client parameter: click the cell   and select a parameter from the drop-down list. * Value: enter the value for the   corresponding parameter. |

## Global variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as a start component of a Job or subJob and it always needs an output link. |

**Related concepts**  

* [Delivering messages to an Amazon SQS queue](tsqsqueuecreate-tsqsoutput-tlogrow-delivering-messages-to-amazon-sqs-queue-standard-component-the "Here's an example of using Talend components to create an Amazon SQS (Simple Queue Service) queue, then deliver a couple of messages to the queue, finally get and display the attributes of the queue on the console.")
