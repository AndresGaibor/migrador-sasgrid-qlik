<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tdsdelete · versión 8.0 -->
# tDSDelete / tDataStewardshipTaskDelete

Last updated: 9/30/2026

Connects to Qlik Talend Data Integration or
Talend Data Stewardship and deletes the data stored in sprints/campaigns.

Information noteAttention: From Talend Studio 8.0
R2025-12, the tDataStewardshipTask\* components are replaced by the
tDS\* components:

* tDataStewardshipTaskInput becomes
  tDSInput.
* tDataStewardshipTaskOutput becomes
  tDSOutput.
* tDataStewardshipTaskDelete becomes
  tDSDelete.

These components let you connect Talend Studio
to [Qlik Talend Data Integration](https://help.qlik.com/en-US/cloud-services/csh/client/qdi_stewardship_create_job) and [Talend Data Stewardship](https://help.qlik.com/talend/en-US/data-stewardship-user-guide/Cloud/talend-cloud-data-stewardship-introduction).

All the tasks to be deleted must belong to the same sprint/campaign and must have the same
schema. However, data is deleted permanently and can not be recovered.

You can set proxy settings to connect to Talend Data Stewardship by using
the tSetProxy component.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## Standard properties

These properties are used to configure the tDSDelete and
tDataStewardshipTaskDelete components which run in the Standard
Job framework.

The Standard
tDSDelete and
tDataStewardshipTaskDelete components belong to the Data Stewardship family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings to delete data from Qlik Talend Data Integration

| Properties | Description |
| --- | --- |
| Cloud | Select Qlik Data Stewardship and click Apply. |
| Property Type | Either Built-in or Repository.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| URL | Enter the address of your Qlik Cloud tenant, for example `https://qcs.us.qlikcloud.com/`. |
| API key | Enter your API key. To generate one, see [Generating an API key](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-generate-api-keys.htm). |
| Sprint | Click [...] and select the sprint from which you want to delete the data. |
| Column with ID | This option is available until Talend Studio 8.0 R2026-07. From Talend Studio 8.0 R2026-08, this option depends on the Delete by ID checkbox. |
| Delete by ID | This option is available from Talend Studio 8.0 R2026-08. Select the checkbox to enable the Column with ID dropdown list and select the column from which you want to delete the resolved records.  The choices available correspond to the column names provided by the input component you use in the Job with tDSDelete. |
| States | This option is available from Talend Studio 8.0 R2026-08. Click  to select one or more states in the workflow to delete the corresponding records. |
| Assignee | This option is available from Talend Studio 8.0 R2026-08. Click  to select the sprint participant whose records you want to delete. |
| Priority | This option is available from Talend Studio 8.0 R2026-08. Click  to select one or more priorities to delete records with those priorities. |
| Tags | This option is available from Talend Studio 8.0 R2026-08. Click  to enter one or more tags to delete records with those tags. You must enter the tag labels in double quotes. |

## Advanced settings to delete data from Qlik Talend Data Integration

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Max batch Size | Set the number of lines you want to have in each processed batch.  Do not change the default value unless you are facing performance issues. Increasing the batch size can improve the performance but setting a too high value could cause Job failures. |
| Maximum number of retries | Set the number of request retries before throwing a timeout exception and killing the Job. |

## Basic settings to delete data from Talend Data Stewardship

| Properties | Description |
| --- | --- |
| Cloud | Select Talend Data Stewardship and click Apply. |
| Property Type | Either Built-in or Repository.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   The columns below are automatically added to the schema of this component and are read-only. They give the task metadata.  * *TDS\_ID* : task identifier. * *TDS\_STATE* : current state of the   task. * *TDS\_ASSIGNEE* : task assignee. * *TDS\_CREATION* : task creation date. * *TDS\_LAST\_UPDATE*: task last update   date. * *TDS\_LAST\_UPDATED\_BY* : identifier of   the user who last updated the task. * *TDS\_PRIORITY*: numeric value which   represents the priority level of the task in the web application. Each   numeric value is retrieved from a text value as below:    + Very     Low = 0   + Low =     1   + Medium     = 2   + High =     3   + Very     High = 3 The No Priority is set by default to Medium = 2. * *TDS\_TAGS*: the tag(s) assigned to   the task retrieved as a list of comma-separated values. * *TDS\_ARBITRATION*: (Available only   when anARBITRATION   campaign is selected) the choice assigned to the task in enumeration   values. * *TDS\_ARBITRATION\_LABEL*: (Available only when an ARBITRATION or a GROUPING campaign is selected) the choice   assigned to the task as displayed in Talend Data Stewardship. * *TDS\_MASTER*: (Available only when a   MERGING   campaign is selected) indicator to whether the record is a master   record. * *TDS\_SOURCE*: (Available only when a   MERGING   campaign is selected) name of the source of the record. * *TDS\_SCORE*: (Available only when a GROUPING or a MERGING campaign is selected) the calculated   distance between the input and the master record according to the matching   algorithm. * *TDS\_RATING*: (Available only when a MERGING campaign is selected) provides the   trust score per source record you set at task creation. This score overrides   the score you define at campaign creation, if any. It is an integer value,   which represents a percentage between 0 and 100. * *TDS\_EXTERNAL\_ID*: helps you set an Identifier of your choice on tasks   so that you can retrieve them easily from any other system. |
| URL | Enter the address to access the Talend Data Stewardship server suffixed with */data-stewardship/*, for example `http://<server_address>:19999/data-stewardship/`.  If you are working with Talend Cloud Data Stewardship, use the URL for the corresponding data center suffixed with */data-stewardship/* to access the application, for example, `https://tds.us.cloud.talend.com/data-stewardship` for the AWS US data center.  For the URLs of available data centers, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Username and Password | Enter the authentication information to log in to Talend Data Stewardship.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  If you are working with Talend Cloud Data Stewardship and if:  * SSO is enabled, enter an access token in the field. * SSO is not enabled, enter in the field either:   + an access token.   + your password (deprecated). |
| Campaign | Click Find a campaign to open a list of all the campaigns available in Talend Data Stewardship, and select the name of the campaign holding the tasks. This is an informative read-only field. |
| Type | A read-only list which shows the campaign type out of the predefined types once the campaign is selected. |
| Override enforcement of data model | Select this checkbox if you want to process data on the Talend Data Stewardship server even if the schema type is not valid, no input validation of the schema is performed. |
| State | Select from the list the state of the tasks you want to delete.  This list displays the names of all the states you define in the campaign workflow. It shows the initial and final states and any validation state you add when creating the campaign in Talend Cloud Data Stewardship. This list enables you to filter the tasks by their states and delete them whether they are new or resolved, or whether they are in any of the validation states you define in the campaign workflow.  Use the Any State option to delete all tasks whatever is their state.  Use the Custom option to specify different states of the tasks to be deleted separated by commas, for example `"New,toValidate1,toValidate2"`. You must enter the exact label of the state you define in the workflow. |
| Assignee | Select the campaign participant whose tasks you want to delete.  No Assignee deletes the tasks which are not assigned to any data steward, while Any Assignee deletes the tasks without taking any assignee into account.  Custom enables you to set a custom expression in the field which is displayed to filter the tasks you want to process according to specific needs. |
| Priority, Choice and Tags | Priority (optional): Select any of the task priorities.  Any Priority deletes all tasks whatever is their priority, while Custom enables you to set a custom expression in the field which is displayed.  Choice (optional, available only when an ARBITRATION campaign is selected): Select any of the choice options set on the tasks in the campaign.  No Choice deletes the tasks for which no choice has been selected by data stewards, while Any Choice deletes all tasks whatever is the selected choice.  Tags (optional): Select any of the tags assigned to the tasks in the campaign. |
| Query | Enter the query statement you want to use to filter the tasks to process.  The condition is composed of a field name, an operator and a value. When referencing record data, the name of the field must be prefixed by record.. You should use simple quotes around strings, and precede quotes within the string with a backslash. For example: to filter tasks by assignee and first name value when having a *FirstName* field in the record, use `assignee='user1@talend.com'` in the Assignee field and `'De\'wayne'` in the Query field.  For more information, see [The query language used with data stewardship components and the REST API](/talend/r/en-US/7.3/data-stewardship-user-guide/tql-with-tds-components-api). |
| Delete by ID | Select this check box if you want to delete a task by providing its identifier through an input schema using the tFixedFlowInput component for example.  Input field of task ID: From the drop-down list, select the schema column that corresponds to the task identifier field. The choices available correspond to the column names provided by the input component you use in the Job with tDSDelete. |

## Advanced settings to delete data from Talend Data Stewardship

| Properties | Description |
| --- | --- |
| Campaign ID | Displays the technical name of the campaign once it is selected in the basic settings. However, you can modify the field value to replace it with a context parameter for example and pass context variables to the Job at runtime. This technical name is always used to identify a campaign when the Job communicates with Talend Data Stewardship whatever is the value in the Campaign field. |
| HTTP client configuration | Connect Timeout: Set the time in milliseconds (ms) you want to wait before the connection attempt fails and the Job is killed.  Request Timeout: Set the time in milliseconds (ms) you want to wait before the request attempt fails and the Job is killed.  The value `0` is interpreted as infinite waiting time. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global variables

| Variable | Description |
| --- | --- |
| NB\_LINE | The number of messages processed. This is an After variable and it returns an integer. |
| NB\_REJECT | The number of rows rejected. This is an After variable and it returns an integer. |
| NB\_SUCCESS | The number of rows successfully processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage Rule | This component can be used as a standalone component or as a start component of a Job or subJob. |

**Related concepts**  

* [Deleting tasks from Talend Data Stewardship](tdatastewardshiptaskdelete-tlogrow-deleting-tasks-from-talend-data-stewardship-standard-component-enterprise "This Job deletes the tasks stored in Talend Data Stewardship according to the criteria you define in the basic settings of the tDataStewardshipTaskDelete components.")
