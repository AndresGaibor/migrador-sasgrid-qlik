<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforceeinsteinbulkexec · versión 8.0 -->
# tSalesforceEinsteinBulkExec

Last updated: 9/30/2026

Loads data into Salesforce Analytics Cloud from a local
file.

## tSalesforceEinsteinBulkExec Standard properties

These properties are used to configure tSalesforceEinsteinBulkExec
running in the Standard Job framework.

The Standard
tSalesforceEinsteinBulkExec component belongs to the Business and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The connection fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| User Name and Password | Enter the Web service authentication details.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| End Point | Enter the WebService URL required to connect to Salesforce. For example, *https://login.salesforce.com/services/Soap/u/37.0*. Note that the version in the URL should be 32.0 or later. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * For the fields of numeric type (for example, byte, short,   int, long, float, double, and BigDecimal), their length and precision   values need to be specified. The default length and precision values are   *10* and *2*, and you can   also specify their custom values in the schema editor. * For the fields of date type, you need to specify the   format of the date in the schema editor. For more information about the   supported date format, see [Analytics Cloud External Data Format   Reference](http://www.salesforce.com/us/developer/docs/bi_dev_guide_ext_data_format/bi_dev_guide_ext_data_format.pdf).   The Schema list and the Editor schema button disappear if the Custom JSON Metadata check box is selected.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Operation | Select an operation to perform on the dataset:   * Append: Append all data to the   dataset. Create a dataset if it does not exist. * Upsert: Insert or update rows in   the dataset. Create a dataset if it does not exist. * Overwrite: Create a new dataset   with the given data, and replace dataset if it already exists. * Delete: Delete the rows from the   dataset.   Information noteNote:  * A metadata JSON file is required for the Append, Upsert, and Delete operations. * The data and metadata for the Append and Upsert operations must match the dataset on which the   operation is happening. All columns, dimensions, and measures must   match exactly. * The Append   operation is not allowed if you specify any column as the primary   key. * You must specify one (and only one) column as the   primary key on which the Upsert   or Delete operation is based.   You can do that by clicking Edit   schema and selecting the check box next to the column   you want to set as the primary key. * The metadata for the Delete operation must be a subset of the dataset   columns. |
| Name | Type in the name of the dataset into which the data will be loaded. |
| CSV File | Specify the path to the local CSV file to be loaded. |

## Advanced settings

| Properties | Description |
| --- | --- |
| CSV Encoding | Enter the encoding type of the CSV file.  This field is not visible when the Custom JSON Metadata check box is selected. |
| Fields Delimiter | Enter the character that separates the field values in the CSV file.  This field is not visible when the Custom JSON Metadata check box is selected. |
| Fields Enclosed By | Enter the character used to enclose the field values in the CSV file.  This field is not visible when the Custom JSON Metadata check box is selected. |
| Line Terminated By | Enter the character indicating the end of a line.  This field is not visible when the Custom JSON Metadata check box is selected. |
| Auto Generate JSON Metadata Description | Select this check box to generate the JSON metadata description automatically. |
| Header | Specify the number of lines to ignore in the CSV file.  This field is available only when the Auto Generate JSON Metadata Description check box is cleared. |
| Unique API Name | Specify the unique API name for the object in the JSON metadata description.  This field is available only when the Auto Generate JSON Metadata Description check box is cleared. |
| Label | Specify the display name for the object in the JSON metadata description.  This field is available only when the Auto Generate JSON Metadata Description check box is cleared. |
| Fully Qualified Name | Specify the full path that uniquely identifies the record in the JSON metadata description.  This field is available only when the Auto Generate JSON Metadata Description check box is cleared. |
| Custom JSON Metadata | Select this check box to use a customized JSON metadata file.  This check box is available only when the Auto Generate JSON Metadata Description check box is cleared. |
| JSON Metadata | Specify the path to the customized JSON metadata file.  This field is available only when the Custom JSON Metadata check box is selected. |
| Generate JSON in File | Select this check box to write the JSON metadata description into a local file.  This check box is not visible when the Custom JSON Metadata check box is selected. |
| Generated JSON Folder | Specify the directory where you want to store the generated JSON metadata file.  This field is available only when the Generate JSON in File check box is selected. |
| Retrieve Upload Status | Select this check box to retrieve the status of the data upload. |
| Time to wait for server answer (seconds) | Specify the amount of time in seconds to wait for the upload status response from the server.  This field is available only when the Retrieve Upload Status check box is selected. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a standalone component. |
