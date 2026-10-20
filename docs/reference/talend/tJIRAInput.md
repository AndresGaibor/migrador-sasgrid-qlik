<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjirainput · versión 8.0 -->
# tJIRAInput

Last updated: 9/30/2026

Retrieves the issue information based on a JQL query or retrieve the project
information based on a specified project ID from JIRA.

## tJIRAInput Standard properties

These properties are used to configure tJIRAInput running in the
Standard Job framework.

The Standard
tJIRAInput component belongs to the Business family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Note that the schema of this component is empty by default, and you need to click Guess schema to retrieve it. The schema is a single column *json* of String type that stores the issue or project information in JSON format. |
| Jira URL | Specify the URL used to access JIRA. |
| Jira version | Select one of the following Jira API versions:  * Jira Server (v2) is Jira on-premises and uses the   REST API v2. * Jira Cloud (v3) is Jira Cloud and uses the REST   API v3. Cloud-specific considerations:   + Rate limits: Jira Cloud may return HTTP 429 (Too Many     Requests) responses when API rate limits are exceeded. Your     integration should detect these responses and implement retry     logic with exponential backoff, respecting any     Retry-After header provided.   + JQL limits: Jira Cloud enforces a JQL length limit (~5000     characters). Only GET requests are supported for queries     approaching this limit.   + Permissions and scopes: Access depends on Jira Cloud     permissions. Missing permissions can cause authentication or     authorization failures.   + Validation errors: When using Jira Cloud v3, request bodies     must be constructed according to the [Atlassian Document Format     (ADF) schema](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/). Payloads compatible with v2 will not     work as-is with v3; make sure that JSON payloads, including ADF     content, match the expected structure and field requirements.     Otherwise, Jira will return validation errors for malformed or     incorrectly formatted requests. |
| Authentication options | Select one of the following authentication methods depending on the server version and security requirements:   * If you selected Jira Server (v2):   + Basic: Specify the username and password     to access JIRA.  To enter the password, click the [...] button     next to the password field, enter the password in double quotes in the pop-up dialog box,     and click OK to save the settings.   + Personal Access Token: To enter the JIRA     personal access token, click the [...] button next to the     Token field, paste the token, and click     OK to save the settings. * If you selected Jira Cloud (v3):   + Email and Token:     Specify the email address to access JIRA, as well as the JIRA     API token. Click the [...] button next to     the Token field, paste the token, and     click OK to save the settings. |
| JIRA resource | Select the JIRA resource from the drop-down list, either Issue or Project. |
| Use JQL query | In the JQL query field, specify the JQL (JIRA Query Language) query based on which you will search for issues in JIRA. Do not enter the query in double quotes. For more information about the JQL, see [the Jira documentation](https://confluence.atlassian.com/jirasoftwareserver072/advanced-searching-829057400.html).  If left empty, all issues from the defined JIRA account are retrieved.  This field is available only when Issue is selected from the Resource type drop-down list. |
| Issue ID | Enter the ID of the specific issue you want to retrieve from JIRA.  This field is available only when Issue is selected from the Resource type drop-down list. |
| Project ID | Enter the ID of the specific project you want to retrieve from JIRA.  This field is available only when Project is selected from the Resource type drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Batch size | Specify the number of issues to be processed in each batch.  This field is available only when ISSUE is selected from the Jira resource drop-down list. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component of a Job or subJob and it always needs an output link. |
| **Limitation** | This component doesn't support retrieving the comments of issues from JIRA. |

**Related concepts**  

* [Creating an issue in JIRA application](tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-creating-issue-in-jira-application-standard-component "Here is an example of using Talend components to create a new issue in JIRA application, then retrieve the information of the new issue from JIRA application, finally extract the information needed based on the JSONPath query and write the extracted information into a JSON file.")
* [Retrieving the project information from JIRA application](tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-retrieving-project-information-from-jira-application-standard-component "Here is an example of using Talend components to retrieve the information of a project from JIRA application, extract the information needed based on the JSONPath query, and finally write the extracted information into a JSON file.")
* [Updating an issue in JIRA application](tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-updating-issue-in-jira-application-standard-component "Here is an example of using Talend components to update an existing issue in JIRA application, then retrieve the information of the updated issue from JIRA application, finally extract the information needed based on the JSONPath query and write the extracted information into a JSON file.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-retrieving-project-information-from-jira-application-standard-component -->
# Retrieving the project information from JIRA application

Last updated: 9/30/2026

Here is an example of using Talend components to retrieve the
information of a project from JIRA application, extract the information needed based on the
JSONPath query, and finally write the extracted information into a JSON file.

### In this section

* [Creating a Job for retrieving the project information from JIRA application](/talend/en-US/components/8.0/jira/tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-creating-job-for-retrieving-project-information-from-jira-application-standard-component-a)
* [Configuring the Job for retrieving the project information from JIRA application](/talend/en-US/components/8.0/jira/tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-configuring-job-for-retrieving-project-information-from-jira-application-standard-component)
* [Executing the Job to retrieve the project information from JIRA application](/talend/en-US/components/8.0/jira/tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-executing-job-to-retrieve-project-information-from-jira-application-standard-component-press)

**Related reference**  

* [tJIRAInput](tjirainput "Retrieves the issue information based on a JQL query or retrieve the project information based on a specified project ID from JIRA.")

**Related information**  

* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)
* [tFileOutputJSON](/talend/en-US/components/8.0/json/tfileoutputjson)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-configuring-job-for-retrieving-project-information-from-jira-application-standard-component -->
# Configuring the Job for retrieving the project information from JIRA application

Last updated: 9/30/2026

## Procedure

1. Double-click the tJIRAInput component to open its
   Basic settings view.
2. In the Host URL, User Id, and
   Password fields, specify the user authentication
   information required to access the JIRA application.
3. Select `Project` from the JIRA
   resource drop-down list, in the Project
   ID field displayed, enter the key of the project, whose
   information will be retrieved. In this example, it is
   `DOC`.
4. Double-click the tExtractJSONFields component to open
   its Basic settings view.
5. Click the [...] button next to Edit
   schema, and in the schema dialog box displayed, define the
   schema by adding six columns of String type, `id`,
   `key`, `name`,
   `description`, `assigneeType`, and
   `ProjectTypeKey`, which will hold the corresponding
   information of the specified project.

   When done, click OK to save the changes and close the
   dialog box.
6. Select the JSON field to be extracted from the JSON
   field drop-down list. In this example, it is
   `json`, which is passed from the
   tJIRAInput component.
7. In the Loop Jsonpath query field, specify the path to
   the node on which the loop is based. In this example, it is
   `$`, which is the root node of the JSON field.
8. In the Mapping table, the Column
   cells are automatically filled with the schema columns, and you need to specify
   the corresponding JSON node that holds the desired data for each schema column.
   In this example, `$.id` for the `id`
   column, `$.key` for the `key` column,
   `$.name` for the `name` column,
   `$.description` for the
   `description` column,
   `$.assigneeType` for the
   `assigneeType` column, and
   `$.projectTypeKey` for the
   `projectTypeKey` column.
9. Double-click the tFileOutputJSON component to open its
   Basic settings view.
10. In the File Name field, specify the path to the file
    into which the extracted project information will be written,
    `D:/JiraComponents/project_info.json` in this example.
    And in the Name of data block field, enter the name of
    the data block, `project` in this example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-creating-job-for-retrieving-project-information-from-jira-application-standard-component-a -->
# Creating a Job for retrieving the project information from JIRA application

Last updated: 9/30/2026

## Before you begin

A project with the key `DOC` has been created in JIRA
application.

## Procedure

1. Create a new Job and add a tJIRAInput component, a
   tExtractJSONFields component, and a
   tFileOutputJSON component to the Job.
2. Link the tJIRAInput component to the
   tExtractJSONFields component using a Row > Main connection.
3. Link the tExtractJSONFields component to the
   tFileOutputJSON component using a Row > Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjirainput-textractjsonfields-tfileoutputjson-tfileoutputjson-executing-job-to-retrieve-project-information-from-jira-application-standard-component-press -->
# Executing the Job to retrieve the project information from JIRA application

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.
3. Open the JSON file project\_info.json generated.

   Note that all extracted project information is displayed in one line in the
   generated JSON file, and you can use some editor tool to format and indent
   the data into an organized manner for better display of the result.

   As shown above, the desired project information has been successfully
   extracted and written into the JSON file.
