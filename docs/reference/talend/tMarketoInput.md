<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketoinput · versión 8.0 -->
# tMarketoInput

Last updated: 9/30/2026

Retrieves lead records, activity history, lead changes, and custom object related
data from Marketo.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMarketoInput Standard properties

These properties are used to configure tMarketoInput running
in the Standard Job framework.

The Standard
tMarketoInput component belongs to two families: Business and Cloud.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Connection Component | Select the component whose connection details will be used to set up the connection to Marketo from the drop-down list. |
| Endpoint address | Enter the API Endpoint URL of the Marketo Web Service. The API Endpoint URL can be found on the Marketo Admin > Web Services panel. |
| Client access ID | Enter the client ID for the access to the Marketo Web Service.  The client ID and client secret key can be found on the Marketo Admin > LaunchPoint panel, by clicking View Details for the service to be accessed. You can also contact Marketo Support via support@marketo.com for further information. |
| Secret key | Enter the client secret key for the access to the Marketo Web Service.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   The schema of this component is predefined and it will be different according to the API mode selected, the operation chosen or the custom object specified.  Note that when the API mode is changed, you need to refresh the schema columns manually by switching back and forth the components in the Connection Component drop-down list (only when reusing the connection created by a tMarketoConnection component) and changing the operation to be performed in the Operation drop-down list.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Note that the dynamic schema feature for this component is only supported in the REST API mode. |
| Operation | Select one of the following operations to be performed from the drop-down list.   * getLead: This operation   retrieves a single lead record. * getMultipleLeads: This   operation retrieves a batch of lead records that match the specified   lead selector search condition. * getLeadActivity: This   operation retrieves the activity history that matches the specified   search condition. * getLeadChanges: This   operation retrieves data value changes and new lead activities after   a given time. * CustomObject: Select this item to perform   specific action on a custom object. This item is available only in   the REST API mode. * Company: This operation retrieves the   company. also referred to as an account, that a person belongs to. * Opportunity: This operation retrieves the   opportunity that is associated with a lead or contact and a company. * OpportunityRole: This operation retrieves the   specific role within an opportunity. |
| Mappings | Complete this table to map the column names of the component schema with the column names in Marketo. By default, the column names in Column name fields are the same as what they are in the schema.  Note that because some column names in Marketo may contain blank space, which is not allowed in the component schema, you need to specify the corresponding column fields in the Marketo column name column. If the defined column names in schema are the same as column names in Marketo, it is not necessary to set the columns mapping.  This table is not available when `CustomObject` is selected from the Operation list in the REST API mode. |
| Lead selector | Select one of the following lead selector types from the drop-down list.   * LeadKeySelector: Select this   type to retrieve lead records that are identified by the specified   lead key. * StaticListSelector: Select   this type to retrieve lead records that are members of the given   static list. With this option selected, you need to specify the   static list by its name or id. To do this, select   `STATIC_LIST_NAME` or   `STATIC_LIST_ID` from the List   param drop-down list and then enter the key value of   the name or id in the List param value field. * LastUpdateAtSelector: Select   this type to retrieve lead records that were updated on specific   dates. This item is available only in the SOAP API mode.   This list is available only when `getMultipleLeads` is selected from the Operation list. |
| Lead key type | Select a field by which you want to query the lead from the drop-down list. This list is available when:   * `getLead` is selected from the Operation list, or * `getMultipleLeads` is selected from the   Operation list and   `LeadKeySelector` is selected from the   Lead selector list, or * `getLeadActivity` is selected from the   Operation list in the   SOAP API mode. |
| Lead key value | Specify the value of the field by which you want to query the lead. This field is available when:   * `getLead` is selected from the Operation list, or * `getLeadActivity` is selected from the   Operation list in the   SOAP API mode, or * `getMultipleLeads` is selected from the   Operation list and   `LeadKeySelector` is selected from the   Lead Selector list. |
| Set Include Types | Select this check box and in the Activity table displayed, specify the types of activity you want to retrieve by clicking the [+] button to add as many rows as needed, each row for an activity type, then clicking the right side of each cell and selecting an activity type from the drop-down list. This check box is available when:   * `getLeadActivity` is selected from the   Operation list, or * `getLeadChanges` is selected from the   Operation list in the SOAP API mode. |
| Set Exclude Types | Select this check box and in the Activity table displayed, specify the types of activity you do not want to retrieve by clicking the [+] button to add as many rows as needed, each row for an activity type, then clicking the right side of each cell and selecting an activity type from the drop-down list. This check box is available when:   * `getLeadActivity` is selected from the   Operation list, or * `getLeadChanges` is selected from the   Operation list in the SOAP API mode. |
| Oldest update date | Specify the time of the earliest update to retrieve only the leads updated since the specified time.  It supports the time format that Marketo supports. For the supported time format, see <http://developers.marketo.com/documentation/soap/getmultipleleads/>.  This field is available only in the SOAP API mode when `getMultipleLeads` is selected from the Operation list and `LastUpdateAtSelector` is selected from the Lead selector list. |
| Latest update date | Specify the time of the latest update to retrieve only the leads updated before the specified time.  It supports the time format that Marketo supports. For the supported time format, see <http://developers.marketo.com/documentation/soap/getmultipleleads/>.  This field is available only in the SOAP API mode when `getMultipleLeads` is selected from the Operation list and `LastUpdateAtSelector` is selected from the Lead selector list. |
| Oldest create date | Type in the time of the earliest creation to retrieve only the data since the specified time. It supports the time format that Marketo supports.  This field is available only in the SOAP API mode when `getLeadChanges` is selected from the Operation list. |
| Latest creation date | Type in the time of the latest creation to retrieve only the data before the specified time. It supports the time format that Marketo supports.  This field is available only in the SOAP API mode when `getLeadChanges` is selected from the Operation list.  Note that Oldest create date and Latest creation date can be specified together or separately. |
| Field list | Enter the comma separated list of field names.  This field is available when `getLeadChanges` is selected from the Operation list in the REST API mode. |
| Since DateTime | Specify the timestamp used to filter results to only include leads with activity since then.  This field is available when `getLeadActivity` or `getLeadChanges` is selected from the Operation list in the REST API mode. |
| Action | Select the operation to be performed on the specified custom object.   * describe: Returns the metadata regarding a   given custom object. * list: Returns a list of custom object types   available in the target instance, along with id and deduplication   information for each type. With this option selected, you need to   specify a comma-separated list of names to filter types in the   CustomObject names field. This   property is available only when   CustomObject is selected from the   Operation drop-down list. * get: Retrieves a list of custom objects   records based on filter and set of values.   This field is available only when CustomObject, Company, Opportunity or OpportunityRole is selected from the Operation drop-down list. |
| Fetch schema | Click this button to retrieve the schema of the specified custom object.  This button is available only when `CustomObject` is selected from the Operation list and `get` is selected from the Action list. |
| Filter type | Specify the field to filter on. Searchable fields can be retrieved by performing a describe action with the custom object.  This field is available only when `CustomObject` is selected from the Operation list and `get` is selected from the Action list. |
| Filter values | Specify a comma-separated list of field values to match against.  This field is available only when `CustomObject` is selected from the Operation list and `get` is selected from the Action list. |
| Batch size | Specify the number of records to be processed in each batch.  This field is available when:   * `getMultipleLeads` is selected from the   Operation list and   `StaticListSelector` or   `LastUpdateAtSelector` is selected from   the Lead Selector   list. * `getLeadActivity` or   `getLeadChanges` is selected from the   Operation list. * `CustomObject` is selected from the   Operation list and   `get` is selected from the   Action list. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| API Mode | Select the Marketo API mode, either `REST API` (default) or `SOAP API`.  For more information about the Marketo REST API, see <http://developers.marketo.com/documentation/rest/>.  For more information about the Marketo SOAP API, see <http://developers.marketo.com/documentation/soap/>. |
| Timeout | Enter the timeout value (in milliseconds) for the connection to the Marketo Web Service before terminating the attempt. |
| Max reconnection attempts | Enter the maximum number of reconnect attempts to the Marketo Web Service before giving up. |
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
| **Usage rule** | This component is usually used as a start component of a Job or subJob and it always needs an output link. |

**Related concepts**  

* [Transmitting data with Marketo using REST API](tmarketoinput-tmarketoconnection-tlogrow-transmitting-data-with-marketo-using-rest-api-standard-component-here-is)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-transmitting-data-with-marketo-using-rest-api-standard-component-here-is -->
# Transmitting data with Marketo using REST API

Last updated: 9/30/2026

Here is an example of using Talend components to connect to Marketo, insert
several lead records into Marketo, then retrieve these records from Marketo and display them
on the console.

### In this section

* [Setting up the Job for data transmission with Marketo using REST API](/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-setting-up-job-for-data-transmission-with-marketo-using-rest-api-standard-component-add)
* [Connecting to Marketo using REST API](/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-connecting-to-marketo-using-rest-api-before)
* [Inserting lead records into Marketo using REST API](/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-inserting-lead-records-into-marketo-using-rest-api-standard-component)
* [Retrieving lead records from Marketo using REST API](/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-retrieving-lead-records-from-marketo-using-rest-api-standard-component)
* [Executing the Job to transmit data with Marketo using REST API](/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-executing-job-to-transmit-data-with-marketo-using-rest-api-standard-component-press)

**Related reference**  

* [tMarketoInput](tmarketoinput "Retrieves lead records, activity history, lead changes, and custom object related data from Marketo.")
* [tMarketoConnection](tmarketoconnection "Opens a connection to Marketo that can then be reused by other Marketo components.")
* [tMarketoOutput](tmarketooutput "Writes lead records or custom object records from the incoming data flow into Marketo.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-connecting-to-marketo-using-rest-api-before -->
# Connecting to Marketo using REST API

Last updated: 9/30/2026

## Before you begin

Before connecting to Marketo using the REST API endpoint, you need to make sure a
custom service, which provides credentials to authenticate with Marketo and allows
you to access the data in Marketo, has been created and associated with a single
API-only user by your Marketo administrator. For more information about the Marketo
Custom Service, see [Custom Services](http://developers.marketo.com/rest-api/custom-services/).

## Procedure

1. Double-click the tMarketoConnection component to open
   its Basic settings view.
2. In the Endpoint address
   field, enter the REST API endpoint URL that can be found on the Marketo
   Admin > Web Services panel.
3. In the Client Access ID and Secret key fields, enter the client Id and
   client secret required to access Marketo.

   The client Id and client secret can be found on the Marketo Admin > LaunchPoint panel, by clicking View Details for
   the service to be accessed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-executing-job-to-transmit-data-with-marketo-using-rest-api-standard-component-press -->
# Executing the Job to transmit data with Marketo using REST API

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the
   Job.

   As shown above, the inserted lead records in Marketo are retrieved and
   displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-inserting-lead-records-into-marketo-using-rest-api-standard-component -->
# Inserting lead records into Marketo using REST API

Last updated: 9/30/2026

## Procedure

1. Double-click the first tFixedFlowInput component to open its Basic settings view.
2. Click the [...] button
   next to Edit schema to open the schema
   dialog box.
3. In the schema dialog box, select the `id`
   and `Status` columns that don't need input values and click
   the  button to remove them. Then click OK to save the settings and close the schema
   dialog box.
4. In the Mode area, select
   Use Inline Content(delimited file)
   and enter the following input data in the Content field.

   ```
   dev@talend.com;Peter;Wang
   doc@talend.com;Judy;Zhang
   dev@talend.com;Nick;Liu
   dev@talend.com;Mark;Zhao
   doc@talend.com;Alex;Sun
   ```
5. Double-click the tMarketoOutput component to open its Basic settings view.
6. From the Connection Component drop-down list, select the
   component whose connection details will be used to set up the connection to
   Marketo, `tMarketoConnection_1` in this example.
7. From the Operation
   drop-down list, select SyncMultipleLeads
   to insert multiple lead records.
8. From the Operation type drop-down list, select
   createDuplicate to allow duplicated
   leads to be created.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-retrieving-lead-records-from-marketo-using-rest-api-standard-component -->
# Retrieving lead records from Marketo using REST API

Last updated: 9/30/2026

## Procedure

1. Double-click the second tFixedFlowInput component to open its Basic settings view.
2. Click the 
   button next to Edit schema and in the
   schema dialog box displayed, define the schema by adding one column
   `mail` of String
   type. Then click OK to save the changes
   and close the schema dialog box.
3. In the Mode area, select
   Use Inline Table. Then click the
    button twice
   below the table displayed to add two rows and fill each row with respective
   values. In this example, two email values `dev@talend.com`
   and `doc@talend.com` are added so that the lead records
   identified by these email values can be retrieved.
4. Double-click the tMarketoInput component to open its Basic settings view.
5. From the Connection Component drop-down list, select the
   component whose connection details will be used to set up the connection to
   Marketo, `tMarketoConnection_1` in this example.
6. Select getMultipleLeads
   from the Operation drop-down list to
   retrieve a batch of lead records.
7. Select LeadKeySelector from the Lead
   selector drop-down list, and select email
   from the Lead key type list and
   `email` from the Lead key values
   list to retrieve the leads identified by the email values passed from the second
   tFixedFlowInput component.
8. Double-click the tLogRow
   component to open its Basic settings
   view.
9. In the Mode area, select
   Table (print values in cells of a
   table) for better readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketoinput-tmarketoconnection-tlogrow-setting-up-job-for-data-transmission-with-marketo-using-rest-api-standard-component-add -->
# Setting up the Job for data transmission with Marketo using REST API

Last updated: 9/30/2026

## Procedure

1. Add a tMarketoConnection component, two
   tFixedFlowInput components, a
   tMarketoOutput component, a tMarketoInput component, and a tLogRow component by typing their names on the
   design workspace or dropping them from the Palette.
2. Make sure `REST` is selected from the
   API Mode drop-down list on the Advanced
   settings view of tMarketoOutput and
   tMarketoInput.
3. Connect the first tFixedFlowInput component to the tMarketoOutput component using a Row > Main connection.
   In the pop-up dialog box, click Yes so
   that the first tFixedFlowInput component
   can get the schema from the target tMarketoOutput component.
4. Connect the second tFixedFlowInput component to the tMarketoInput component using a Row > Main
   connection. In the pop-up dialog box, click No and the second tFixedFlowInput component will not get the schema from the
   target tMarketoInput component.
5. Connect the tMarketoInput component to the tLogRow component using a Row > Main
   connection.
6. Connect the tMarketoConnection component to the first
   tFixedFlowInput component using a
   Trigger > On Subjob Ok
   connection.
7. Do the same to connect the first tFixedFlowInput component to the second tFixedFlowInput component.
