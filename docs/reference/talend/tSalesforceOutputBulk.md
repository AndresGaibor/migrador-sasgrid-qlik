<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulk · versión 8.0 -->
# tSalesforceOutputBulk

Last updated: 9/30/2026

Generates the file to be processed by the tSalesforceBulkExec component for bulk
processing.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

The tSalesforceOutputBulk
and tSalesforceBulkExec components are used together
in a two step process. In the first step, an output file is generated. In the second
step, this file is used to feed the Salesforce database. These two steps are fused
together in the tSalesforceOutputBulkExec component.
The advantage of using two separate steps is that the data can be transformed before it
is loaded into Salesforce.

## tSalesforceOutputBulk Standard properties

These properties are used to configure tSalesforceOutputBulk
running in the Standard Job framework.

The Standard
tSalesforceOutputBulk component belongs to the Business and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Bulk File Path | Specify the path to the file to be generated. |
| Append | Select this check box to append new data at the end of the file if it already exists, instead of overwriting the existing data. |
| Ignore Null | Select this check box to ignore NULL values. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Relationship mapping for upsert | Click the [+] button to add lines as needed and specify the external ID fields in the input flow, the lookup relationship fields in the upsert module, the lookup module as well as the external ID fields in the lookup module.   * Column name of Talend Schema: the name of the external ID field in the input flow. It   refers to the fields in the schema of the preceding component. Such columns are   intended to match against the external ID fields specified in the   External id name column, which are the fields of the   lookup module specified in the Module name column. * Lookup relationship field   name: the name of the lookup relationship field. It refers   to the lookup relationship fields of the module specified in the   Module Name   field in the Basic   settings view of the tSalesforceBulkExec component and is   intended to establish relationship with the lookup module specified in   the Module name   column in this table. You can enter built-in relationship fields and   custom relationship fields. For information about how to define the   lookup relationship fields and how to provide their correct names in the   Lookup relationship field   name field, go to the Salesforce website and launch the   Salesforce Data Loader application for proper actions and   information. * Module   name: the name of the lookup module. * Polymorphic: select this check box when and only when   polymorphic fields are used for relationship mapping. You will get an error if you   keep this check box cleared for a polymorphic field or select it for a field that   is not polymorphic. For more information about the polymorphic fields, search   `polymorphic` at <http://www.salesforce.com/us/developer/docs/api_asynch/>. * External   id name: the name of the external ID field in the lookup module   specified in the Module name column. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with the tSalesforceBulkExec component. Used together, they gain performance while feeding or modifying information in Salesforce.com. |
