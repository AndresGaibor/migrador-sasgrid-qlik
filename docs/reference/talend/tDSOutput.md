<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tdsoutput · versión 8.0 -->
# tDSOutput / tDataStewardshipTaskOutput

Last updated: 9/30/2026

Connects to Qlik Talend Data Integration or
Talend Data Stewardship and loads data into sprints/campaigns in the form of tasks. The tasks must
have the same schema defined in the sprint/campaign.

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

An authorized sprint/campaign participant can then intervene and resolve the
tasks using the capabilities provided by Talend Data Stewardship.

You can set proxy settings to connect to Talend Data Stewardship by using
the tSetProxy component.

Information noteNote: You can store up to 20 GB of tasks in
Talend Cloud Data Stewardship per
account. For more information, see [Setting the maximum amount of stored
tasks](https://help.qlik.com/talend/en-US/data-stewardship-user-guide/8.0/setting-the-maximum-amount-of-stored-tasks).

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## Standard properties

These properties are used to configure the tDSOutput and
tDataStewardshipTaskOutput components which run in the Standard
Job framework.

The Standard
tDSOutput and tDataStewardshipTaskOutput
components belong to the Data Stewardship family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings to load data into a Qlik Talend Data Integration sprint

| Properties | Description |
| --- | --- |
| Cloud | Select Qlik Data Stewardship and click Apply. |
| Property Type | Either Built-in or Repository.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Once you select a sprint from the Sprint list, tDSOutput becomes aware of the schema defined in the sprint and creates identical schema columns in its basic settings. |
| URL | Enter the address of your Qlik Cloud tenant, for example `https://qcs.us.qlikcloud.com/`. |
| API key | Enter your API key. To generate one, see [Generating an API key](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-generate-api-keys.htm). |
| Sprint | Click [...] and select the sprint from which you want to load data. |
| Priority (optional) | Select any of the priorities. Otherwise, select Custom and set a custom expression in the Custom field that is displayed. If no level is selected, Medium is used by default. |
| Assignee | Select the sprint participant whose tasks you want to create. Otherwise, select No assignee to create the tasks without assigning them to anybody. |
| Tags (optional) | Enter the tag to associate with the tasks you want to load.  You can use the tags to filter the tasks you want to load into the sprint. |

## Advanced settings to load data into a Qlik Talend Data Integration sprint

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Maximum number of retries | Set the number of request retries before throwing a timeout exception and killing the Job. |
| Batch Size | Set the number of lines you want to have in each processed batch.  Do not change the default value unless you are facing performance issues. Increasing the batch size can improve the performance but setting a too high value could cause Job failures. |

## Basic settings to load data into Talend Data Stewardship

| Properties | Description |
| --- | --- |
| Cloud | Select Talend Data Stewardship and click Apply. |
| Property Type | Either Built-in or Repository.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Once you select a campaign from the Find a campaign list, tDSOutput becomes aware of the schema defined in the campaign and creates identical schema columns in its basic settings. The component also adds the TDS\_DUE\_DATE and TDS\_EXTERNAL\_ID columns to the schema:  * TDS\_DUE\_DATE: holds the task due date using the   format: YYYY-MM-DD HH:mm:ss. The due date is   calculated automatically according to the task delay time you define   when creating the campaign in Talend Data Stewardship. If you do not define a delay date for tasks when creating the   campaign, this column stays empty. * TDS\_EXTERNAL\_ID: helps you set an identifier of your   choice on tasks so that you can retrieve them easily from any other   system.  If you do not define an identifier for tasks when creating the Job,   this column stays empty.  In case you select to write the tasks in a MERGING or a GROUPING campaign, the below columns are automatically added to the schema:  * TDS\_GID: holds the group identifier.  This identifier is used by tDSOutput to group   records in tasks. All source records that should be grouped in a   single task must have the same TDS\_GID. * TDS\_MASTER (only for a MERGING   campaign): indicates if the record is a master or a source record.  Two cases to consider:   + If no source record is set as master for a given task, Talend Data Stewardship determines which attributes of matched records to use to     create the master record according to the survivorship rules you     define when creating the campaign. For more information about     survivorship rules, see the section about setting data models     in Merging campaigns in [Talend Data Stewardship     Examples](https://help.qlik.com/talend/en-US/data-stewardship-user-guide/8.0/talend-data-stewardship-examples).   + If more than one source record is set as master for a given     task, Talend Data Stewardship takes the first source set as master to be the master record.     So the best practice is to have either 0 or one master record     per task. * TDS\_SOURCE: holds the name of the source of the   record, if any. * TDS\_RATING (only for a MERGING   campaign): provides a trust score per source record at task creation.   This score overrides the score you define at campaign creation, if   any. It is an integer value, which represents a percentage between 0   and 100. * TDS\_SCORE: provides the calculated distance between   the input and the master records according to the matching   algorithm. * TDS\_CREATION: holds the task creation date. * TDS\_LAST\_UPDATE: holds task last update date. |
| URL | Enter the address to access the Talend Data Stewardship server suffixed with */data-stewardship/*, for example `http://<server_address>:19999/data-stewardship/`.  If you are working with Talend Cloud Data Stewardship, use the URL for the corresponding data center suffixed with */data-stewardship/* to access the application, for example, `https://tds.us.cloud.talend.com/data-stewardship` for the AWS US data center.  For the URLs of available data centers, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Username and Password | Enter the authentication information to log in to Talend Data Stewardship.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  If you are working with Talend Cloud Data Stewardship and if:  * SSO is enabled, enter an access token in the field. * SSO is not enabled, enter in the field either:   + an access token.   + your password (deprecated). |
| Campaign | Click Find a campaign to open a list of all the campaigns available in Talend Data Stewardship, and select the name of the campaign holding the tasks. This is an informative read-only field. |
| Type | A read-only list which shows the campaign type out of the predefined types once the campaign is selected. |
| Override enforcement of data model | Select this checkbox if you want to process data on the Talend Data Stewardship server even if the schema type is not valid, no input validation of the schema is performed. This checkbox is selected by default only for Merging and Resolution campaign types. |
| State | Select from the list the state in the workflow at which you want to create the tasks.  This list displays the names of all the states you define in the campaign workflow. It shows the initial and final states and any validation state you add when creating the campaign in Talend Data Stewardship.  Use the Custom  option if you want to contextualize values in order to define different states depending on different values. For example, you can assign the "New" value to the State field if you want all incoming fields to be checked, and assign the "To validate" value to the same field if you are confident with incoming values and just want them to be validated. |
| Assignee | Select the campaign participant whose tasks you want to create. Otherwise, select No Assignee to create the tasks without assigning them to anybody.  The Custom option allows you to assign tasks dynamically to the data stewards part of the campaign by defining context variables in the field which is displayed. The expected value is the steward's login.  You can use this option to assign the tasks to specific stewards based on a given attribute of the incoming data. For example, you can assign French customers to Jacques Bocuse, a French steward, and US customers to Cale Carolina, a US steward, or assign them based on the customer support level Platinum for the support team lead and Gold for experts. |
| Priority, Choice and Tags | Priority (optional): Select any of the task priorities. Otherwise, select Custom and set a custom expression in the field which is displayed.  If no level is selected, Medium is used by default.  Choice (optional, available only when an ARBITRATION campaign is selected): Select any of the choice options set on the records while defining the campaign in the web application. The default value is No Choice, this enables data stewards to do the work in the web application. However, setting an arbitration choice in the Job is a way to help the steward by pre-selecting the supposedly most relevant choice directly when creating the tasks.  Tags (optional): Enter the tag to associate with the tasks you want to load.  You can use the tag(s) to filter the tasks you want to load into the campaign. |
| Comments (optional) | Select one or several schema columns and enter the comment you want to add to the tasks you want to load.  This table lists by default all the schema columns.  The campaign participant will be able to see the comment any time they place the pointer on the source record column in Talend Data Stewardship. This information can help them making a more informed decision when resolving the task. |

## Advanced settings to load data into Talend Data Stewardship

| Properties | Description |
| --- | --- |
| Campaign ID | Displays the technical name of the campaign once it is selected in the basic settings. However, you can modify the field value to replace it with a context parameter for example and pass context variables to the Job at runtime. This technical name is always used to identify a campaign when the Job communicates with Talend Data Stewardship whatever is the value in the Campaign field. |
| Max tasks per commit | Set the number of the tasks you want to have in each commit.  There are no limits for the batch size in Talend Data Stewardship (on premises).  However, you need to make sure not to exceed 200 tasks per commit in Talend Cloud Data Stewardship, setting higher values causes Job failure. |
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
| Usage Rule | This component is usually used as an end component of a Job or subJob and it always needs an input link. |

**Related concepts**  

* [Assigning tasks dynamically in Talend Data Stewardship](tdatastewardshiptaskoutput-tmap-tfileinputdelimited-tfileinputdelimited-assigning-tasks-dynamically-in-talend-data-stewardship-standard-component-enterprise "When loading data to Talend Data Stewardship, it is possible to dynamically assign the tasks to specific stewards based on a given attribute of the incoming data.")
* [Populating campaigns dynamically using campaign IDs](tdatastewardshiptaskoutput-tmap-tmatchgroup-tfileinputdelimited-populating-campaigns-dynamically-using-campaign-ids "This Job loads tasks into campaigns defined in Talend Data Stewardship using campaign technical names. Context parameter are used to pass technical names as context variables to the Job at runtime.")
* [Populating tasks into the same campaign on different Talend Data Stewardship instances](tdatastewardshiptaskoutput-tmap-tmatchgroup-tfileinputdelimited-populating-tasks-into-same-campaign-on-different-talend-data-stewardship-instances "This Job loads tasks into two campaigns with the same data model on two different Talend Data Stewardship instances. Context variables are used to pass the connection information of each Talend Data Stewardship instance to the Job at runtime.")
* [Writing tasks in a Merging campaign](writing-tasks-merging-campaign "This Job loads tasks into a Merging campaign defined in Talend Data Stewardship according to the criteria you define in the basic settings of the tDataStewardshipTaskOutput component.")
* [Writing tasks in Talend Data Stewardship campaigns](tdatastewardshiptaskoutput-tfileinputdelimited-tmatchgroup-tmap-writing-tasks-in-talend-data-stewardship-campaigns-standard-component-enterprise "This Job loads tasks in different campaigns defined in Talend Data Stewardship. It loads the tasks according to the criteria you define in the basic settings of the tDataStewardshipTaskOutput components.")
