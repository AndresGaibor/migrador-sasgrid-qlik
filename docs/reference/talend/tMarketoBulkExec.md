<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketobulkexec · versión 8.0 -->
# tMarketoBulkExec

Last updated: 9/30/2026

Imports leads or custom objects into Marketo from a local file in the REST API
mode.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMarketoBulkExec Standard properties

These properties are used to configure tMarketoBulkExec running in
the Standard Job framework.

The Standard
tMarketoBulkExec component belongs to two families:
Business and Cloud.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Connection component | Select the component whose connection details will be used to set up the connection to Marketo from the drop-down list. |
| Endpoint address | Enter the API Endpoint URL of the Marketo Web Service. The API Endpoint URL can be found on the Marketo Admin > Web Services panel. |
| Client access ID | Enter the client ID for the access to the Marketo Web Service.  The client ID and client secret key can be found on the Marketo Admin > LaunchPoint panel, by clicking View Details for the service to be accessed. You can also contact Marketo Support via support@marketo.com for further information. |
| Secret key | Enter the client secret key for the access to the Marketo Web Service.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Schema and Edit schema | A schema is a row description that defines the number of fields (columns) to be processed and passed on to the next component.  The schema of this component is predefined and it will be slightly different according to the type of the data (`Leads` or `CustomObjects`) to be imported. You can click  next to Edit schema to view its schema.   * batchId: the id of the batch. * importId (for `Leads` only): the id   of the import. * importTime (for `CustomObjects`   only): the time spent on the batch. * message: the status message of the batch. * numOfLeadsProcessed/numOfObjectsProcessed:   the number of rows processed so far. * numOfRowsFailed: the number of rows failed so far. * numOfRowsWithWarning: the number of rows with a warning so   far. * objectApiName (for `CustomObjects`   only): the API name of the custom object. * operation (for `CustomObjects` only):   the bulk operation type. * status: the status of the batch. * failuresLogFile: the log for the failures. * warningsLogFile: the log for the warnings. |
| Import to | Select the type of the data to be imported, either `Leads` or `CustomObjects`. |
| File format | Select the type of the file containing the data to be imported, `csv`, `tsv` or `ssv`. |
| Lookup field | Select the lookup field that will be used for deduplication.  This property is available only when `Leads` is selected from the Import to drop-down list. |
| List Id | Specify the ID of the static list to import to.  This property is available only when `Leads` is selected from the Import to drop-down list. |
| Partition name | Specify the name of the lead partition to import to.  This property is available only when `Leads` is selected from the Import to drop-down list. |
| CustomObject name | Specify the API name of the custom object.  This property is available only when `CustomObjects` is selected from the Import to drop-down list. |
| Bulk file path | Specify the path to the file containing the data to be imported. |
| Poll wait time in seconds | Specify the amount of time (in seconds) for polling for the data. |
| Batch log download path | Specify the path to the batch log file(s) to be downloaded, including the failures log file and the warnings log file.  When importing leads, the failures log file will be named bulk\_leads\_<batchId>\_failures.csv and the warnings log file will be named bulk\_leads\_<batchId>\_warnings.csv.  When importing custom objects, the failures log file will be named bulk\_customobjects\_<customObjectName>\_  <batchId>\_failures.csv and the warnings log file will be named bulk\_customobjects\_<customObjectName>\_  <batchId>\_warnings.csv . |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| API Mode | Specify the Marketo API mode. Note that only the REST API mode is available to use for this component.  For more information about the Marketo REST API, see <http://developers.marketo.com/documentation/rest/>. |
| Timeout | Enter the timeout value (in milliseconds) for the connection to the Marketo Web Service before terminating the attempt. |
| Max reconnection attemps | Enter the maximum number of reconnect attempts to the Marketo Web Service before giving up. |
| Attempt interval time | Enter the time period (in milliseconds) between subsequent reconnection attempts. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NUMBER\_CALL | The number of calls. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component or as a start component of a Job or subJob. |
