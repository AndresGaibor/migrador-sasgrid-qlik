<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketolistoperation · versión 8.0 -->
# tMarketoListOperation

Last updated: 9/30/2026

Adds/removes one or more leads to/from a list in Marketo. Also, it helps you verify
the existence of one or more leads in a list in Marketo.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMarketoListOperation Standard properties

These properties are used to configure tMarketoListOperation running in the Standard Job framework.

The Standard
tMarketoListOperation component belongs to
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
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Note that the dynamic schema feature for this component is only supported in the REST API mode. |
| Operation | Select an operation to be performed from the drop-down list.   * addTo: This operation   adds one or more leads to a list. * isMemberOf: This   operation verifies whether the specific leads exist in the   list. * removeFrom: This   operation removes one or more leads from a list. |
| Add or remove many prospects | Select this check box to add multiple leads to or remove multiple leads from a list.  This check box is available only when `addTo` or `removeFrom` is selected from the Operation list. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection if the Add or remove many prospects check box is cleared. |

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
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |

**Related concepts**  

* [Adding a lead record to a Marketo list using SOAP API](tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-adding-lead-record-to-marketo-list-using-soap-api-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-adding-lead-record-to-marketo-list-using-soap-api-standard-component-the -->
# Adding a lead record to a Marketo list using SOAP API

Last updated: 9/30/2026

The following scenario describes a three-component Job that adds a lead
record into a specified list in Marketo using SOAP API.

### In this section

* [Setting up the Job for adding a lead record to a Marketo list](/talend/en-US/components/8.0/marketo/tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-setting-up-job-for-adding-lead-record-to-marketo-list-standard-component-create)
* [Configuring the Job for adding a lead record to a Marketo list](/talend/en-US/components/8.0/marketo/tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-configuring-job-for-adding-lead-record-to-marketo-list-standard-component)
* [Executing the Job to add a lead record to a Marketo list](/talend/en-US/components/8.0/marketo/tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-executing-job-to-add-lead-record-to-marketo-list-standard-component-press)

**Related reference**  

* [tMarketoListOperation](tmarketolistoperation "Adds/removes one or more leads to/from a list in Marketo. Also, it helps you verify the existence of one or more leads in a list in Marketo.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-configuring-job-for-adding-lead-record-to-marketo-list-standard-component -->
# Configuring the Job for adding a lead record to a Marketo list

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowInput component to open its Basic settings view.
2. Click the [...] button
   next to Edit schema to view its
   schema.
3. In the Mode area, select
   Use Inline Table, and then click the
   [+] button to add one row and fill
   the row with respective values. In this example, these values are: *MKTOLISTNAME* for ListKeyType, *Test\_Comp\_QA* for ListKeyValue, *IDNUM* for
   LeadKeyType and *9300203* for LeadKeyValue.
4. Double-click the tMarketoListOperation component to open its Basic settings view.
5. In the Endpoint address
   field, enter the Marketo SOAP API endpoint URL that can be found on the Marketo Admin > Web Services panel.
6. In the Client Access ID and Secret key fields, enter the user ID and
   encryption key required to access Marketo.
7. From the Operation list,
   select addTo to add the lead with the ID
   `9300203` into the list
   `Test_Comp_QA`.
8. Double-click the tLogRow
   component to open its Basic settings
   view.
9. Click the Sync columns
   button to synchronize the schema with the input schema.
10. In the Mode area, select
    Table (print values in cells of a
    table) for better readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-executing-job-to-add-lead-record-to-marketo-list-standard-component-press -->
# Executing the Job to add a lead record to a Marketo list

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save
   the Job.
2. Press F6 or click
   Run on the Run tab to run the Job.

   As shown above, the result of the operation is displayed on the Run console.
3. Double-check the result in Marketo.

   The lead with the ID `9300203` in
   Marketo is added into the list `Test_Comp_QA`.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/marketo/tmarketolistoperation-tfixedflowinput-tlogrow-tlogrow-setting-up-job-for-adding-lead-record-to-marketo-list-standard-component-create -->
# Setting up the Job for adding a lead record to a Marketo list

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tFixedFlowInput component, a tMarketoListOperation component, and a tLogRow component by typing their names in the
   design workspace or dropping them from Palette.
2. Double-click the tMarketoListOperation component and on the
   Component tab click Advanced settings to open its advanced settings view, then
   select `SOAP` from the API Mode
   drop-down list.
3. Connect tFixedFlowInput to
   tMarketoListOperation using a
   Row > Main connection. In the pop-up dialog box, click Yes to get the schema from the target
   component.
4. Connect tMarketoListOperation to tLogRow using a Row >
   Main connection.
