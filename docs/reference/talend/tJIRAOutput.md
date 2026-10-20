<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput · versión 8.0 -->
# tJIRAOutput

Last updated: 9/30/2026

Inserts, updates, or deletes the issue or project information in JIRA.

## tJIRAOutput Standard properties

These properties are used to configure tJIRAOutput running in the Standard Job framework.

The Standard
tJIRAOutput component belongs to the Business family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  Note that the schema of this component is empty by default and you need to click Edit schema to manually set it depending on your needs:  * If you selected Insert in the Output   Action list, add a single column json of String type. * If you selected Update in the Output   Action list, add two columns id and   json of String type. * If you selected Delete in the Output   Action list, add a single column id of   String type. |
| Jira version | Select one of the following Jira API versions:  * Jira Server (v2) is Jira on-premises and uses the   REST API v2. * Jira Cloud (v3) is Jira Cloud and uses the REST   API v3. Cloud-specific considerations:   + Rate limits: Jira Cloud may return HTTP 429 (Too Many     Requests) responses when API rate limits are exceeded. Your     integration should detect these responses and implement retry     logic with exponential backoff, respecting any     Retry-After header provided.   + JQL limits: Jira Cloud enforces a JQL length limit (~5000     characters). Only GET requests are supported for queries     approaching this limit.   + Permissions and scopes: Access depends on Jira Cloud     permissions. Missing permissions can cause authentication or     authorization failures.   + Validation errors: When using Jira Cloud v3, request bodies     must be constructed according to the [Atlassian Document Format     (ADF) schema](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/). Payloads compatible with v2 will not     work as-is with v3; make sure that JSON payloads, including ADF     content, match the expected structure and field requirements.     Otherwise, Jira will return validation errors for malformed or     incorrectly formatted requests.   + The Jira API is asynchronous, so tJiraOutput may confirm     success before the ticket is actually created. If your Job     requires the ticket immediately, allow for a delay before it     appears in Jira. |
| Authentication options | Select one of the following authentication methods depending on the server version and security requirements:   * If you selected Jira Server (v2):   + Basic: Specify the username and password     to access JIRA.  To enter the password, click the [...] button     next to the password field, enter the password in double quotes in the pop-up dialog box,     and click OK to save the settings.   + Personal Access Token: To enter the JIRA     personal access token, click the [...] button next to the     Token field, paste the token, and click     OK to save the settings. * If you selected Jira Cloud (v3):   + Email and Token:     Specify the email address to access JIRA, as well as the JIRA     API token. Click the [...] button next to     the Token field, paste the token, and     click OK to save the settings. |
| User Id and Password | Specify the user authentication data used to access JIRA.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Resource type | Select the JIRA resource from the drop-down list, either Issue or Project. |
| Output action | Select an operation to be performed from the dropdown list.  * Create: create new issue or   project information into JIRA.  When using the ISSUE\_ID and   ISSUE\_KEY global variables, two new columns are   populated after successful Create operations:   id and key. * Update: modify existing issue or   project information in JIRA. * Delete: remove issue or project   data in JIRA corresponding to the input flow. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Delete subtasks | Select this checkbox to delete the subtask(s). This checkbox is available only when ISSUE is selected from the JIRA resource dropdown list and Delete is selected from the Output Action dropdown list. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

A Flow variable functions during the execution of a component
while an After variable functions after the execution of the component.

To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from
it.

For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox. |
| ISSUE\_ID | ISSUE\_ID: the internal identifier of the JIRA issue created by the component. This is an After variable and it returns a string. |
| ISSUE\_KEY | ISSUE\_KEY: the key of the JIRA issue created by the component. This is an After variable and it returns a string. |
| NB\_LINE | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer. |
| NB\_REJECT | NB\_REJECT: the number of rows rejected. This is an After variable and it returns an integer. |
| NB\_SUCCESS | NB\_SUCCESS: the number of rows successfully processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an end component of a Job or subJob and it always needs an input link. |

**Related concepts**  

* [Creating an issue in JIRA application](tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-creating-issue-in-jira-application-standard-component "Here is an example of using Talend components to create a new issue in JIRA application, then retrieve the information of the new issue from JIRA application, finally extract the information needed based on the JSONPath query and write the extracted information into a JSON file.")
* [Updating an issue in JIRA application](tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-updating-issue-in-jira-application-standard-component "Here is an example of using Talend components to update an existing issue in JIRA application, then retrieve the information of the updated issue from JIRA application, finally extract the information needed based on the JSONPath query and write the extracted information into a JSON file.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-creating-issue-in-jira-application-standard-component -->
# Creating an issue in JIRA application

Last updated: 9/30/2026

Here is an example of using Talend components to create a new
issue in JIRA application, then retrieve the information of the new issue from JIRA
application, finally extract the information needed based on the JSONPath query and write the
extracted information into a JSON file.

### In this section

* [Setting up a Job for creating an issue in JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-setting-up-job-for-creating-issue-in-jira-application-standard-component-a)
* [Creating a new issue in JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-creating-new-issue-in-jira-application-standard-component)
* [Retrieving the new issue information from JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-retrieving-new-issue-information-from-jira-application-standard-component)
* [Executing the Job to create an issue in JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-executing-job-to-create-issue-in-jira-application-standard-component-press)

**Related reference**  

* [tJIRAOutput](tjiraoutput "Inserts, updates, or deletes the issue or project information in JIRA.")
* [tJIRAInput](tjirainput "Retrieves the issue information based on a JQL query or retrieve the project information based on a specified project ID from JIRA.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)
* [tFileOutputJSON](/talend/en-US/components/8.0/json/tfileoutputjson)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-updating-issue-in-jira-application-standard-component -->
# Updating an issue in JIRA application

Last updated: 9/30/2026

Here is an example of using Talend components to update an
existing issue in JIRA application, then retrieve the information of the updated issue from
JIRA application, finally extract the information needed based on the JSONPath query and write
the extracted information into a JSON file.

### In this section

* [Creating a Job for updating an issue in JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-creating-job-for-updating-issue-in-jira-application-standard-component-a)
* [Updating an issue in JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-updating-issue-in-jira-application-standard-component?id=2868)
* [Retrieving the updated issue information from JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-retrieving-updated-issue-information-from-jira-application-standard-component)
* [Executing the Job to update an issue in JIRA application](/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-executing-job-to-update-issue-in-jira-application-standard-component-press)

**Related reference**  

* [tJIRAOutput](tjiraoutput "Inserts, updates, or deletes the issue or project information in JIRA.")
* [tJIRAInput](tjirainput "Retrieves the issue information based on a JQL query or retrieve the project information based on a specified project ID from JIRA.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)
* [tFileOutputJSON](/talend/en-US/components/8.0/json/tfileoutputjson)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-creating-new-issue-in-jira-application-standard-component -->
# Creating a new issue in JIRA application

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited component to open
   its Basic settings view.
2. In the File name/Stream field, specify the path to the
   JSON file used to create the issue.

   In this example, a simple JSON file
   `D:/JiraComponents/issue_create.json` will be used
   to insert a new issue under the project with the key
   `DOC` and the data in this file reads as
   follows:

   ```
   {"fields": {
       "issuetype": {
           "id": "10001",
           "name": "Task"
       },
       "project": {
           "key": "DOC",
           "name": "Documentation"
       },
       "description": "Create an issue under the DOC project",
       "summary": "Add the documentation for new components tJIRA***"
   }}
   ```

   Note that the tJIRAOutput component now only supports
   creating project/issue in JIRA application with the single line JSON file,
   so you need to join all lines in the input JSON file into one line before
   executing the Job.

   For more information about the types of issues, see the JIRA official
   documentation [Issue types](https://confluence.atlassian.com/adminjiracloud/issue-types-844500742.html).

   For more information about how to find the id for issue types, see the JIRA
   official documentation [Finding the Id for Issue
   Types](https://confluence.atlassian.com/display/JIRA050/Finding+the+Id+for+Issue+Types).
3. Double-click the tJIRAOutput component to open its
   Basic settings view.
4. In the Host URL, User Id, and
   Password fields, specify the user authentication
   information required to access the JIRA application.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-executing-job-to-create-issue-in-jira-application-standard-component-press -->
# Executing the Job to create an issue in JIRA application

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.
3. Open the JSON file issue\_info.json generated.

   Note that all extracted issue information is displayed in one line in the
   generated JSON file, and you can use some editor tool to format and indent
   the data into an organized manner for better display of the result.

   As shown above, a new issue with the key `DOC-2` has
   been created, and the desired information for each issue in the project
   `DOC` has been successfully extracted and written
   into the JSON file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-retrieving-new-issue-information-from-jira-application-standard-component -->
# Retrieving the new issue information from JIRA application

Last updated: 9/30/2026

## Procedure

1. Double-click the tJIRAInput component to open its
   Basic settings view.
2. Select `Issue` from the JIRA
   resource drop-down list.
3. In the JQL field, enter the JQL query used to retrieve
   issues in JIRA application.

   In this example, the query is `project = DOC ORDER BY created
   DESC`. All issues under the project `DOC`
   will be retrieved and they will be sorted by the creation date in descending
   order.
4. Double-click the tExtracJSONFields component to open its
   Basic settings view.
5. Click the [...] button next to Edit
   schema, and in the schema dialog box displayed, define the
   schema by adding five columns of String type, `id`,
   `key`, `project`,
   `description`, and `summary`,
   which will hold the corresponding information of each issue retrieved.

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
   `$.fields.project.key` for the
   `project` column,
   `$.fields.description` for the
   `description` column, and
   `$.fields.summary` for the
   `summary` column.
9. Double-click the tFileOutputJSON component to open its
   Basic settings view.
10. In the File Name field, specify the path to the file
    into which the extracted issue information will be written,
    `D:/JiraComponents/issue_info.json` in this example.
    And in the Name of data block field, enter the name of
    the data block, `issue` in this example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-setting-up-job-for-creating-issue-in-jira-application-standard-component-a -->
# Setting up a Job for creating an issue in JIRA application

Last updated: 9/30/2026

## Before you begin

A project with the key `DOC` has been created in JIRA
application and only one issue with the key `DOC-1` has already
been created under this project.

## Procedure

1. Create a new Job and add a tFileInputDelimited
   component, a tJIRAOutput component, a
   tJIRAInput component, a
   tExtractJSONFields component, and a
   tFileOutputJSON component to the Job.
2. Double-click the tJIRAOutput component to open its
   Basic settings view.
3. Select `Issue` from the JIRA
   resource drop-down list and `Insert` from
   the Output Action drop-down list to insert an
   issue.
4. Link the tFileInputDelimited component to the
   tJIRAOutput component using a Row > Main connection. In the pop-up dialog box, click
   Yes to let the
   tFileInputDelimited component get the schema of the
   tJIRAOutput component.
5. Do the same to link the tJIRAInput component to the
   tExtractJSONFields component and the
   tExtractJSONFields component to the
   tFileOutputJSON component.
6. Link the tFileInputDelimited component to the
   tJIRAInput component using a Trigger >  On Subjob Ok connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-creating-job-for-updating-issue-in-jira-application-standard-component-a -->
# Creating a Job for updating an issue in JIRA application

Last updated: 9/30/2026

## Before you begin

A project with the key `DOC` has been created in JIRA
application and an issue with the key `DOC-2` as shown below
has already been created under this project.

## Procedure

1. Create a new Job and add a tFileInputDelimited
   component, a tJIRAOutput component, a
   tJIRAInput component, a
   tExtractJSONFields component, and a
   tFileOutputJSON component to the Job.
2. Double-click the tJIRAOutput component to open its
   Basic settings view.
3. Select `Issue` from the JIRA
   resource drop-down list and `Update` from
   the Output Action drop-down list to update an
   issue.
4. Link the tFileInputDelimited component to the
   tJIRAOutput component using a Row > Main connection. In the pop-up dialog box, click
   Yes to let the
   tFileInputDelimited component get the schema of the
   tJIRAOutput component.
5. Do the same to link the tJIRAInput component to the
   tExtractJSONFields component and the
   tExtractJSONFields component to the
   tFileOutputJSON component.
6. Link the tFileInputDelimited component to the
   tJIRAInput component using a Trigger >  On Subjob Ok connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-executing-job-to-update-issue-in-jira-application-standard-component-press -->
# Executing the Job to update an issue in JIRA application

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.
3. Open the JSON file issue\_info\_update.json generated.

   Note that all extracted issue information is displayed in one line in the
   generated JSON file, and you can use some editor tool to format and indent
   the data into an organized manner for better display of the result.

   As shown above, the issue with the key `DOC-2` has been
   updated, and the desired information for the issue has been successfully
   extracted and written into the JSON file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/jira/tjiraoutput-tjirainput-tfileinputdelimited-tfileoutputjson-retrieving-updated-issue-information-from-jira-application-standard-component -->
# Retrieving the updated issue information from JIRA application

Last updated: 9/30/2026

## Procedure

1. Double-click the tJIRAInput component to open its
   Basic settings view.
2. Select `Issue` from the JIRA
   resource drop-down list.
3. In the JQL field, enter the JQL query used to retrieve
   the issue in JIRA application.

   In this example, the query is `project = DOC AND issuekey =
   DOC-2`. The issue with the key `DOC-2` under
   the project `DOC` will be retrieved.
4. Double-click the tExtracJSONFields component to open its
   Basic settings view.
5. Click the [...] button next to Edit
   schema, and in the schema dialog box displayed, define the
   schema by adding five columns of String type, `id`,
   `key`, `project`,
   `description`, and `summary`,
   which will hold the corresponding information of each issue retrieved.

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
   `$.fields.project.key` for the
   `project` column,
   `$.fields.description` for the
   `description` column, and
   `$.fields.summary` for the
   `summary` column.
9. Double-click the tFileOutputJSON component to open its
   Basic settings view.
10. In the File Name field, specify the path to the file
    into which the extracted issue information will be written,
    `D:/JiraComponents/issue_info_update.json` in this
    example. And in the Name of data block field, enter the
    name of the data block, `issue` in this example.
