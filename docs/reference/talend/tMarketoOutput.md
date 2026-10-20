<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketooutput · versión 8.0 -->
# tMarketoOutput

Last updated: 9/30/2026

Writes lead records or custom object records from the incoming data flow into
Marketo.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMarketoOutput Standard properties

These properties are used to configure tMarketoOutput running in the Standard Job framework.

The Standard
tMarketoOutput component belongs to
two
families: Business and
Cloud.

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
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   The schema of this component is predefined and it will be different according to the API mode selected, the operation chosen or the custom object specified.  Note that when the API mode is changed, you need to refresh the schema columns manually by switching back and forth the components in the Connection Component drop-down list (only when reusing the connection created by a tMarketoConnection component) and changing the operation to be performed in the Operation drop-down list.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Note that the dynamic schema feature for this component is only supported in the REST API mode. |
| Operation | Select an operation that allows you to synchronize data between Marketo and another external system.   * syncLead: Insert or update (upsert) a single   lead record. * syncMultipleLeads: Insert or update (upsert)   multiple lead records. * deleteLeads (for REST only): Delete a list of   leads. * syncCustomObjects (for REST only): Insert,   update, or upsert custom object records to the target instance. * deleteCustomObjects (for REST only): Delete a   set of custom object records. * syncCompanies: Insert or update (upsert) a   list of companies. * deleteCompanies: Delete a list of   companies. * syncOpportunities: Insert or update (upsert)   a list of opportunities. * deleteOpportunities: Delete a list of   opportunities. * syncOpportunityRoles: Insert or update   (upsert) a list of opportunity roles. * deleteOpportunityRoles: Delete a list of   opportunity roles. |
| Operation type | Select a type of sync operation to be performed from the drop-down list.   * createOnly: creates new leads. * updateOnly: updates existing leads. * createOrUpdate: creates new leads, or   updates the leads if they already exist. * createDuplicate: creates new leads. If   they already exist, then creates duplicated leads.   This list is available only in the REST API mode when `syncLead` or `syncMultipleLeads` is selected from the Operation list. |
| Lookup field | Select the lookup field that will be used to find the duplicate.  This list is available only in the REST API mode when `syncLead` or `syncMultipleLeads` is selected from the Operation list. |
| Mappings | Complete this table to map the column names of the component schema with the column names in Marketo. By default, the column names in Column name fields are the same as what they are in the schema.  Note that because some column names in Marketo may contain blank space, which is not allowed in the component schema, you need to specify the corresponding column fields in the Marketo column name column. If the defined column names in schema are the same as column names in Marketo, it is not necessary to set the columns mapping.  This table is available only in the SOAP API mode. |
| De-duplicate lead record on email address | Select this check box to de-duplicate records using email address.  Clear this check box to create another record which contains the same email address. |
| Delete leads in batch | Select this check box to delete the leads in batch.  This check box is available only when `deleteLeads` is selected from the Operation list. |
| Batch Size | Specify the number of records to be processed in each batch.  This field is available when:   * `syncMultipleLeads` is selected from the   Operation list, or * `deleteLeads` is selected from the   Operation list and the Delete   leads in batch check box is selected. |
| Sync method | Select a type of sync operation to be performed from the drop-down list.   * createOnly: Create new custom objects,   companies, opportunities or opportunity roles. * updateOnly: Updates existing custom objects,   companies, opportunities or opportunity roles. * createOrUpdate: Create new custom objects,   companies, opportunities or opportunity roles, or updates them if   they already exist.   This list is available only when `syncCustomObjects`, `syncCompanies`, `syncOpportunities` or `syncOpportunityRoles` is selected from the Operation list. |
| Custom object name | Specify the name of the custom object.  This field is available only when `syncCustomObjects` or `deleteCustomObjects` is selected from the Operation list. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. But note that no error rows can be collected when syncing or deleting leads in batch. |

## Advanced settings

| Properties | Description |
| --- | --- |
| API Mode | Select the Marketo API mode, either `REST API` (default) or `SOAP API`.  For more information about the Marketo REST API, see <http://developers.marketo.com/documentation/rest/>.  For more information about the Marketo SOAP API, see <http://developers.marketo.com/documentation/soap/>. |
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
| **Usage rule** | This component is usually used as an end component of a Job or subJob and it always needs an input link. |

**Related concepts**  

* [Transmitting data with Marketo using REST API](tmarketoinput-tmarketoconnection-tlogrow-transmitting-data-with-marketo-using-rest-api-standard-component-here-is)
