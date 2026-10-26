<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/tbedrockclient · versión 8.0 -->
# tBedrockClient

Last updated: 9/30/2026

Establishes a connection to Amazon Bedrock to store and retrieve data.

## tBedrockClient Standard properties

These properties are used to configure tBedrockClient running in the
Standard Job framework.

The Standard
tBedrockClient component belongs to the AI family.

Information noteNote: This component is available only when you have installed the 8.0.1-R2025-12 Talend Studio
monthly update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its   Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Credential provider | Specify the way to obtain AWS security credentials.   * Static credentials: Use access   key and secret key as the AWS security   credentials. * Inherit credentials from AWS role: Obtain AWS   security credentials from your EMR instance metadata. To use this option,   the Amazon EMR cluster must be started and your Job must be running on this   cluster. For more information, see [Using an IAM Role to Grant Permissions to Applications   Running on Amazon EC2 Instances](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). This option enables you to   develop your Job without having to put any AWS keys in the Job, thus easily   comply with the security policy of your organization. * Web identity token: Use Web token for establishing   the Amazon Bedrock connection. * Profile credentials or inherit from AWS role: Use   credentials stored in a file (known as profile configuration file) as the   AWS security credentials or inherit AWS security credentials from the AWS   role.  AWS security credentials can be grouped in profiles in profile   configuration files. A profile configuration file can contain one or   multiple profiles. You can optionally specify the profile configuration   file in the Profile path field and specify the   profile to be used in the Profile name field.  If the Profile path field and the   Profile name filed are left empty,   <user folder>/.aws/credentials will be used   as the profile configuration file and the profile named   default will be used.  In cases of EC2 instances, if the profile (the specified or the default   profile) does not exist, the component will try to inherit the AWS   security credentials from the AWS role. * API keys: Use Amazon Bedrock API keys to   authenticate to the Amazon Bedrock API. For more information, see [How Amazon Bedrock API keys   work](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-how.html).   This option can work as a dynamic parameter and be assigned a value using a context variable.  Information noteNote: tRedshiftBulkExec, tRedshiftOutputBulk, and tRedshiftOutputBulkExec support S3 connections that are established with Credential Provider being Static Credentials or Inherit credentials from AWS role only. |
| Assume role | If you temporarily need some access permissions associated to an AWS IAM role that is not granted to your user account, select this checkbox to assume that role. Then specify the values for the following parameters to create a new assumed role session.  Ensure that access to this role has been granted to your user account by the trust policy associated to this role. If you are not certain about this, ask the owner of this role or your AWS administrator.  * ARN: the Amazon Resource Name (ARN) of the role to   assume. You can find this ARN name on the Summary   page of the role to be used on your AWS portal, for example, this role   ARN could read like   `am:aws:iam::[aws_account_number]:role/[role_name]`. Role session name: enter the   name you want to use to uniquely identify your assumed role session. This   name can contain upper- and lower-case alphanumeric characters with no   spaces. You can also include underscores or any of the following characters:   =,.@-. * Session duration   (minutes): the duration (in minutes) for which you want   the assumed role session to be active. This duration cannot exceed the   maximum duration which your AWS administrator has set. The duration   defaults to 3600 seconds if you give it no value.  For an example about an IAM role and its related policy types, see [Create and Manage AWS IAM Roles](https://aws.amazon.com/blogs/security/now-create-and-manage-aws-iam-roles-more-easily-with-the-updated-iam-console/) from the AWS documentation. |
| Region | Specify the AWS region by selecting or entering a region name between double quotation marks (e.g. *"us-east-1"*).  Note that some model IDs are not available in certain regions. For more information about model and region compatibility, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/en_us/bedrock/latest/userguide/models-supported.html). |
| Model ID | To select one of the available Amazon Bedrock models, click the [...] button next to the field. In the dialog box displayed, select the model that will be used or select the Use custom value check box and specify the model name in the Custom value field. For more information about Amazon Bedrock models, see [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/en_us/bedrock/latest/userguide/models-supported.html). |
| Request template | Enter the request parameter and value in JSON format. Example: { "inputText": "which city is the capital of China?" } |
| Extract a sub-part of the response | Enter the path of a node to select a sub-element of the response. If the element is an array, each element of the array will be looped over. For more information about the syntax for entering the node name, see [Data Shaping Selector Language syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language). This field is optional and must remain empty to retrieve the entire response. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |
| Use a custom region endpoint | Select this checkbox to use a custom endpoint and in the field displayed, specify the URL of the custom endpoint to be used. This option can work as a dynamic parameter and be assigned a value using a context variable. |
| Signing region | Select the AWS region of the STS service. If the region is not in the list, you can enter its name between double quotation marks. The default value is us-east-1.  This dropdown list is available only when the Assume role checkbox is selected. |
| Enable path style access | Select this option to enable path-style access. Click [Path-Style Requests](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html#path-style-access) for related information. Note that buckets created after September 30, 2020 will support only virtual hosted-style requests. Path-style requests will continue to be supported for buckets created on or before this date. This option is available when Use a custom region endpoint is selected.  This option can work as a dynamic parameter and be assigned a value using a context variable.  Information noteWarning: Path-style access cannot work with the accelerate mode. So, make sure Enable Accelerate Mode is cleared when selecting this option. |
| Specify STS endpoint | Select this check box to specify the AWS Security Token Service (STS) endpoint from which to retrieve the session credentials. For example, enter `sts.amazonaws.com`.  This service allows you to request temporary, limited-privilege credentials for the AWS user authentication. Therefore, you still need to provide the access key and secret key to authenticate the AWS account to be used.  For a list of the STS endpoints you can use, see [AWS Security Token Service](https://docs.aws.amazon.com/general/latest/gr/rande.html#sts_region). For further information about the STS temporary credentials, see [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html). Both articles are from the AWS documentation.  This checkbox is available only when the Assume role checkbox is selected. |
| External ID | If the administrator of the account to which the role belongs provided you with an external ID, enter its value here. The External Id is a unique identifier that allows a limited set of users to assume the role.  This field is available only when the Assume role checkbox is selected. |
| Serial number | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate the identification number of the hardware or virtual MFA device that is associated with the user who assumes the role.  This field is available only when the Assume role checkbox is selected. |
| Token code | When you assume a role, the trust policy of this role might require Multi-Factor Authentication (MFA). In this case, you must indicate a token code. This token code is a time-based one-time password produced by the MFA device.  This field is available only when the Assume role checkbox is selected. |
| Tags | List session tags in the form of key-value pairs. You can then use these session tags in policies to allow or deny access to requests.  Transitive: select this checkbox to indicate that a tag will persist to the next role in a role chain.  For more information about tags, see [Passing Session Tags in AWS STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining)  This field is available only when the Assume role checkbox is selected. |
| IAM policy ARNs | Enter the Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. Use managed session policies to limit the permissions of the session. The policies must exist in the same account as the role. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role checkbox is selected. |
| Policy | Enter an IAM policy in JSON format that you want to use as a session policy. Use session policies to limit the permissions of the session. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies.  For more information about session policies, see the corresponding section in [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)  This field is available only when the Assume role check box is selected. |
| Config client | Select this checkbox and specify the client parameter(s) by clicking the [+] button to add as many rows as needed, each row for a client parameter, and then setting the value of the following fields for each parameter:  * Client Parameter: Click the cell   and select the client parameter from the list. * Value: Enter the value for the   selected parameter.   For related information, read [the AWS documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/section-client-configuration.html). |
| Check S3 Accessibility | Leave this checkbox selected so that the component verifies the credentials to be used for this connection request to S3 before proceeding with further actions. It is recommended to use the default By Account Owner option for this verification. The By Bucket Configuration option employs an old verification approach which can significantly increase your network load in some circumstances. Information noteTroubleshooting:  * If your connection check fails, make sure one of these two methods   are activated on S3: s3:ListAllMyBuckets, or   s3:GetBucketLogging. * If you get an Access denied error, try either to clear the   Assume Role option in the Basic   settings, or leave the Assume   Role selected and select the By Bucket   Configuration method. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related tasks**  

* [Analyzing business intelligence questions using Amazon Bedrock](tbedrockclient-tlogrow-analyzing-business-questions "This Job uses the tBedrockClient component to send a business intelligence question to Amazon Bedrock using the Titan Text Lite model to generate insights, and displays the AI-generated answer in the console.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ai/tbedrockclient-tlogrow-analyzing-business-questions -->
# Analyzing business intelligence questions using Amazon Bedrock

Last updated: 9/30/2026

This Job uses the tBedrockClient component to send a business intelligence question to Amazon Bedrock using the Titan Text Lite model to generate insights, and displays the AI-generated answer in the console.

## Before you begin

Before running this Job, ensure you have:

* An active AWS account with Amazon Bedrock enabled.
* Amazon Bedrock API keys configured in your AWS account. For more information, see [How Amazon Bedrock API keys work](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-how.html).
* Access to the amazon.titan-text-lite-v1 model in your AWS region.
* Your AWS access key and secret key stored securely.

## Linking the components

### Procedure

1. Create a new Standard Job and add the following components by typing their names
   in the design workspace or dragging them from the Palette:
   tBedrockClient, and
   tLogRow.
2. Connect tBedrockClient to tLogRow
   using a Row > FLOW
   connection.

## Configuring the components

### Procedure

1. Double-click tBedrockClient to open its
   Component view.
2. In the Basic settings tab, configure the following parameters:

   * In the Credential provider list, select
     API keys.

     Make sure the API key is set as an
     environment variable. For more information, see [Use an Amazon Bedrock API
     key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-use.html).
   * In the Region field, select or enter your AWS region (for example, `"us-east-1"`).
   * In the Model ID field, click the
     [...] button and select
     amazon.titan-text-lite-v1 from the list.
   * In the Request template field, enter the following
     JSON:

     ```
     {
       "inputText": "As a Qlik analytics expert, provide a detailed answer to this question: What are the top 3 key performance indicators (KPIs) that a SaaS company should track to measure customer success?"
     }
     ```
3. Click Edit schema and define the following output column:

   * `content` (String)

   This column will store the AI-generated answer from Amazon Bedrock.
4. Click OK to close the schema editor and OK to close the component view.
5. Double-click tLogRow to open its
   Component view.
6. In the Basic settings tab, set the
   Mode as Vertical.
7. Click OK to close the component view.

## Executing the Job

### Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to execute the Job.

### Results

The Job sends the business intelligence question to Amazon Bedrock using the Titan
Text Lite model with a Qlik Analytics expert context, and displays the AI-generated
detailed answer in the console.

The console output displays the detailed AI-generated answer identifying the top
three customer success KPIs with explanations tailored for Qlik Analytics users.

**Related reference**  

* [tBedrockClient](tbedrockclient "Establishes a connection to Amazon Bedrock to store and retrieve data.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
