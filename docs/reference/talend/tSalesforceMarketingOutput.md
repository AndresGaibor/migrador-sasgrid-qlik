<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforcemarketingoutput · versión 8.0 -->
# tSalesforceMarketingOutput

Last updated: 9/30/2026

Inserts, updates, upserts, or deletes data in a Salesforce Marketing Cloud object.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSalesforceMarketingOutput Standard properties

These properties are used to configure tSalesforceMarketingOutput running in the Standard Job framework.

The Standard
tSalesforceMarketingOutput component belongs to the Business and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The connection fields that follow   are completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| Object type | Click the [...] button next to the field and in the dialog box displayed, select the object type on which the operation will be performed or select the Use custom value check box and specify an object type manually in the Custom value field. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a module and is recommended to be used for this purpose only; it is not recommended for the use of creating modules. |
| Guess schema | Click this button to retrieve the schema from the table. |
| Operation type | Select the operation to be performed from the drop-down list.   * Create: Create a new object in Salesforce Marketing   Cloud. * Delete: Delete an existing object in Salesforce   Marketing Cloud. * Perform: Perform an action on an existing object in   Salesforce Marketing Cloud. If you select this operation type, you need to   select the corresponding action to perform in the   Action field. The available actions depend on the   selected object type, and you can also enter an action value manually. * Schedule: Schedule an action on an existing object   in Salesforce Marketing Cloud. If you select this operation type, you need   to select or enter the corresponding action and scheduling details such as   start and end date, occurrence, recurrence, interval, etc. * Update: Update an existing object type in Salesforce   Marketing Cloud. |
| SOAP elements | Specify the SOAP elements in the form of element path-value pairs. You can select the Element path ID in the list generated from the incoming schema, and you can use JSON format, plain text, and context variables in the Value field.  Example:  Element path = `/name` and Value = `{.name}`  or  Element path = `/characterSet` and Value = `UTF-8` |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Max batch size | Set the maximum number of rows allowed in each batch. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| NB\_SUCCESS | The number of rows successfully processed. This is an After variable and it returns an integer. |
| NB\_REJECT | The number of rows rejected. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Limitation | The Salesforce Marketing Cloud components do not support the Microservice build type yet. |
