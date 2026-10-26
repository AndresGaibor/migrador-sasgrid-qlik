<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist · versión 8.0 -->
# tSQSQueueList

Last updated: 9/30/2026

Iterates and lists the URL of Amazon SQS (Simple Queue Service)
queues in a specified region.

## tSQSQueueList Standard properties

These properties are used to configure tSQSQueueList running in the
Standard Job framework.

The Standard tSQSQueueList component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  The schema of this component is predefined with the following columns. You can click the [...] button next to Edit schema to view its schema and edit the schema by adding some customized attributes for the messages to be delivered.   * Body: the body of the message to be delivered. * MessageGroupId: the specific message group that   the message belongs to. Available only when the Use FIFO   queues (first-in-first-out) check box is selected. * MesssageDeduplicationId: the token used for   deduplication of the message. Available only when the Use FIFO   queues (first-in-first-out) check box is selected and the   Use Content Based Deduplication check box is   cleared. * MessageID: the message ID of a message that is   passed to the SQS queue. Available only when the Use batch   mode check box is cleared. This column only appears in the   output main row that connects the subsequent component. See [Amazon SQS queue and message identifiers](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-message-identifiers.html) for   related information.   For more information on each predefined column, see [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html). |
| Credential provider | Specify the way to obtain AWS security credentials: Static credentials, Inherit credentials from AWS role, or Provider credentials or inherit from AWS role.   * Static credentials: Use access key   and secret key as the AWS security credentials. * Inherit credentials from AWS role: Obtain AWS security   credentials from your EMR instance metadata. To use this option, the Amazon EMR   cluster must be started and your Job must be running on this cluster. For more   information, see [Using an IAM Role to Grant Permissions to Applications   Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). This option enables you to develop   your Job without having to put any AWS keys in the Job, thus easily comply with   the security policy of your organization. * Provider credentials or inherit from AWS role: Obtain   AWS security credentials from provider credentials or from your EMR instance   metadata. You can specify the profile configuration file in the   Profile path field and specify the profile in the   Profile name field.   Information noteNote: This drop-down list is available only when you have installed the R2023-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session.  Ensure that access to this role has been granted to your user account by the trust policy associated to this role. If you are not certain about this, ask the owner of this role or your AWS administrator.  * ARN: the Amazon Resource Name (ARN) of the role to   assume. You can find this ARN name on the Summary   page of the role to be used on your AWS portal, for example, this role   ARN could read like   `am:aws:iam::[aws_account_number]:role/[role_name]`. Role session name: enter the   name you want to use to uniquely identify your assumed role session. This   name can contain upper- and lower-case alphanumeric characters with no   spaces. You can also include underscores or any of the following characters:   =,.@-. * Session duration   (minutes): the duration (in minutes) for which you want   the assumed role session to be active. This duration cannot exceed the   maximum duration which your AWS administrator has set. The duration   defaults to 3600 seconds if you give it no value.  For an example about an IAM role and its related policy types, see [Create and Manage AWS IAM Roles](https://aws.amazon.com/blogs/security/now-create-and-manage-aws-iam-roles-more-easily-with-the-updated-iam-console/) from the AWS documentation. |
| Region | Specify the AWS region by selecting a region name from the list or entering a region between double quotation marks (for example *"us-east-1"*) in the list. For more information on AWS Regions, see [AWS Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html). |
| Queue name prefix | Enter the prefix to filter the queues whose names start with the specified value. Only the Amazon SQS queues whose names begin with this prefix will be listed. Leave this field empty to list all queues. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Config client | Select this check box and in the table displayed specify the client configuration parameters. Click the [+] button below the table to add as many rows as needed, each row for a client configuration parameter, and set the value of the following attributes for each parameter:  * Client parameter: click the cell   and select a parameter from the drop-down list. * Value: enter the value for the   corresponding parameter. |
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
| CURRENT\_QUEUE\_NAME | The URL of the queue being processed. This is a Flow variable and it returns a string. |
| NB\_QUEUE | The number of queues processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as a start component of a Job or subJob and it always needs an output link. |

**Related concepts**  

* [Listing Amazon SQS queues in an AWS region](tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-listing-amazon-sqs-queues-in-aws-region-standard-component "Here's an example of using Talend components to iterate and list the URLs of all Amazon SQS (Simple Queue Service) queues in an AWS region.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-listing-amazon-sqs-queues-in-aws-region-standard-component -->
# Listing Amazon SQS queues in an AWS region

Last updated: 9/30/2026

Here's an example of using Talend components
to iterate and list the URLs of all Amazon SQS (Simple Queue Service) queues in an AWS
region.

### In this section

* [Creating a Job for listing Amazon SQS queues](/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-creating-job-for-listing-amazon-sqs-queues-standard-component-create)
* [Opening a connection to access Amazon SQS](/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-opening-connection-to-access-amazon-sqs-standard-component)
* [Listing all Amazon SQS queues in an AWS region](/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-listing-all-amazon-sqs-queues-in-aws-region-standard-component)
* [Executing the Job to list Amazon SQS queues](/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-executing-job-to-list-amazon-sqs-queues-standard-component-press)

**Related reference**  

* [tSQSConnection](tsqsconnection "Opens a connection to Amazon Simple Queue Service that can then be reused by other SQS components.")
* [tSQSQueueList](tsqsqueuelist "Iterates and lists the URL of Amazon SQS (Simple Queue Service) queues in a specified region.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tIterateToFlow](/talend/en-US/components/8.0/orchestration/titeratetoflow)
* [tJava](/talend/en-US/components/8.0/java-custom-code/tjava)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-creating-job-for-listing-amazon-sqs-queues-standard-component-create -->
# Creating a Job for listing Amazon SQS queues

Last updated: 9/30/2026

Create a Job to open a connection to access Amazon SQS, then iterate
and list the URLs of all Amazon SQS queues in a specified region, finally display the
total number of the queues in the region.

Prerequisites: You must create several Amazon SQS
queues in an AWS region in order to replicate this scenario. In this example, four
queues `talend`, `talend-dev`,
`talend-doc` and `talend-qa` have been
created in the region `Asia Pacific (Tokyo)` as shown in below
figure.

## Procedure

1. Create a new Job and add a tSQSConnection component, a tSQSQueueList component, a tIterateToFlow component, a tLogRow component, and a tJava component by typing their names in the design workspace
   or dropping them from the Palette.
2. Link the tSQSQueueList
   component to the tIterateToFlow component
   using a Row > Iterate connection.
3. Link the tIterateToFlow
   component to the tLogRow component using a
   Row > Main connection.
4. Link the tSQSConnection
   component to the tSQSQueueList component
   using a Trigger > OnSubjobOk connection.
5. Link the tSQSQueueList
   component to the tJava component using a
   Trigger > OnSubjobOk connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-executing-job-to-list-amazon-sqs-queues-standard-component-press -->
# Executing the Job to list Amazon SQS queues

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the
Job for listing Amazon SQS queues, you can then execute the Job and verify the Job
execution result.

## Procedure

1. Press Ctrl + S to save the
   Job.
2. Press F6 to execute the
   Job.

   As shown above, the URLs of all queues in the `Asia
   Pacific (Tokyo)` region and the total number of the queues are
   displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-listing-all-amazon-sqs-queues-in-aws-region-standard-component -->
# Listing all Amazon SQS queues in an AWS region

Last updated: 9/30/2026

Configure the tSQSQueueList
component, the tIterateToFlow component, the
tLogRow component, and the tJava component to list the URLs of all Amazon SQS queues
in an AWS region and display the total number of the queues in the region on the console
of Talend Studio.

## Procedure

1. Double-click the tSQSQueueList component to open its Basic settings view.
2. Specify the connection details required to access Amazon SQS. In
   this example, select the Use an existing
   connection check box and from the Component List drop-down list displayed, select the connection
   component to reuse its connection details you have already defined.
3. Double-click the tIterateToFlow component to open its Basic settings view.
4. Click the  button next to Edit schema to open the schema dialog box.
5. Click the  button to add one String type column
   `CurrentQueueURL` that will hold the URLs of the queues
   to be listed. When done, click OK to close
   the dialog box.
6. In the Mapping table, set
   the value for the `CurrentQueueURL` column. In this
   example, the value is set to
   `((String)globalMap.get("tSQSQueueList_1_CURRENT_QUEUE_NAME"))`,
   which is the value of the global variable
   `CURRENT_QUEUE_NAME` for the tSQSQueueList component.

   Note that you can fill the value by pressing Ctrl + Space to access the global variables list
   and then selecting `tSQSQueueList_1_CURRENT_QUEUE_NAME`
   from the list.
7. Double-click the tLogRow
   component to open its Basic settings view,
   and then select Table (print values in cells of a
   table) in the Mode area for
   better readability of the result.
8. Double-click the tJava
   component to open its Basic settings
   view.
9. In the Code field, enter the
   following code to display the total number of the queues in the region.

   ```
   System.out.println("The number of queues: " + ((Integer)globalMap.get("tSQSQueueList_1_NB_QUEUE")));
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-sqs/tsqsqueuelist-tsqsconnection-titeratetoflow-tjava-opening-connection-to-access-amazon-sqs-standard-component -->
# Opening a connection to access Amazon SQS

Last updated: 9/30/2026

Configure the tSQSConnection
component to open a connection to access Amazon SQS.

## Procedure

1. Double-click the tSQSConnection
   component to open its Basic settings view.
2. In the Access key and Secret key fields, specify the authentication
   information required to access Amazon SQS.
3. Select an AWS region available for Amazon SQS from the Region list. In this example, it is `Asia
   Pacific (Tokyo)`.
