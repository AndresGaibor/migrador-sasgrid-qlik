<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tnetsuitev2019output · versión 8.0 -->
# tNetSuiteOutput (v2019/2021/2025)

Last updated: 9/30/2026

Invokes the NetSuite SOAP service and inserts, updates, or removes data on the
NetSuite SOAP server by leveraging NetSuite v2019/2021/2025 features.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tNetSuiteOutput (v2019/2021/2025) Standard properties

These properties are used to configure tNetSuiteOutput running
in the Standard Job framework.

The Standard
tNetSuiteOutput component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote:

* This component is named tNetSuiteV2019Output if you do not install the
  8.0.1-R2023-02 Talend Studio
  monthly update or a later one delivered by Talend.
* This component is incorporated into the tNetSuiteOutput component if you have
  installed the 8.0.1-R2023-02 Talend Studio
  monthly update or a later one delivered by Talend. To access this component in this case, select NetSuite
  SOAP from the Version drop-down list in the
  Basic settings view of the tNetSuiteOutput component and
  click Apply. For more information, check with your
  administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Version | Select the NetSuite component you want to use from the drop-down list: NetSuite Deprecated for the NetSuite version 2019 component and Netsuite SOAP for the NetSuite version 2019/2021/2025 component. Click the Apply button to validate your selection.  Information noteNote: The Version drop-down list and the Apply button are available only when you have installed the 8.0.1-R2023-02 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  Information noteWarning: The schema of this component is prefilled with columns corresponding to the NetSuite service fields, which vary depending on the Record Type selected. You can delete columns that are not relevant to your operation, but do not rename any schema columns or this may cause execution errors. |
| API version | Select the version of the NetSuite API you are connecting to. |
| Account | Enter your NetSuite web services account number (also called account ID). |
| Login type | Select the login type: `Basic` or `Token-based`. |
| E-mail and Password | Enter your user credentials to access the NetSuite SOAP service.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only.  These two fields are available when `Basic` is selected from the Login type drop-down list. |
| Role ID | Enter your NetSuite role ID.  This field is available when `Basic` is selected from the Login type drop-down list. |
| Application ID | Enter the NetSuite application ID generated for your account.  An application ID is required starting from NetSuite version 2015 and above. You can find your application ID or create a new one on NetSuite's Manage Integration page.  This field is available when `Basic` is selected from the Login type drop-down list. |
| Consumer key and Consumer secret | Enter the consumer key and consumer secret generated in your NetSuite account.  To enter the consumer secret, click the [...] button next to the Consumer secret field to bring out the Enter a new password dialog box, enter the consumer secret in the text field, and click OK. Note that you can enter the consumer secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter consumer secrets in the Java   mode only.  These two fields are available when `Token-based` is selected from the Login type drop-down list. |
| Token ID and Token secret | Enter the token ID and token secret generated in your NetSuite account.  To enter the token secret, click the [...] button next to the Token secret field to bring out the Enter a new password dialog box, enter the token secret in the text field, and click OK. Note that you can enter the token secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter token secrets in the Java mode   only.  These two fields are available when `Token-based` is selected from the Login type drop-down list. |
| Record type | Click the [...] button next to the field to open a dialog box, and then select a record type you want to retrieve or select the Use custom object check box and specify a custom record type in the Object Name field. |
| Action | Select an action to perform from the list.  * Add: Adds a new record to your   data. If a duplicate is found and the Die on   error check box is selected, the Job stops; if the   Die on error check box is   cleared, the duplicate is ignored and the Job continues. * Update: Makes changes to an   existing record.  If the record corresponding to the specified Internal ID   does not exist, and the Die on   error check box is selected, the Job stops.  To use this option, the *InternalId*   column must exist in the schema and set as Key. * Upsert: Updates the record   corresponding to the specified ID, or inserts a new record if it does not   exist.  To use this option, a column for record ID must exist in the schema and   set as Key. * Delete: Removes an existing   record.  If the record corresponding to the specified Internal ID   does not exist and the Die on   error check box is selected, the Job stops.  To use this option, the *InternalId*   column must exist in the schema and set as Key. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Set WSDL log level | Select the level of logging for the WSDL SOAP envelopes sent to NetSuite when executing your Job. By default, logs are disabled.  * Disabled: No WSDL logging is performed. * Debug: Logs SOAP envelopes at the debug level (key   debug information). * Trace: Logs SOAP envelopes at the trace level   (detailed information, including request and response payloads).   If you select Debug or Trace, ensure that the corresponding log level is enabled in the Advanced settings of the Run tab as well before executing your Job. If you select a higher log level like Info in the Run tab, the corresponding Debug or Trace logs will not be displayed in the Run console. |
| Max batch size | Specify the maximum number of records that can be processed in a batch. |
| Enable customizations | Select this check box to instruct the component to retrieve customizations - custom record types and custom fields. With this option enabled, custom record types will be retrieved and can be selected in the Record Type dialog box, and custom fields will be retrieved and included into the schema.  This option is enabled by default. You can disable it if you don't need custom record types or custom fields.  Information noteNote: Transactional custom body fields for these transactions are not supported: Assembly Unbuild, Bin Putaway Worksheet, Bin Transfer, Paycheck, and Work Order. |
| Use native upsert | Select this check box to use the Upsert operation provided by NetSuite. To use NetSuite's Upsert operation, the ExternalId column must exist in the schema and set as Key.  This option is available when `Upsert` is selected from the Action list in Basic settings.  By default, for compatibility reasons, this option is enabled and the component performs the Add or Update action for an upsert depending on whether the record ID is specified. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  CURRENT\_INTERNALID: The internal ID of the record currently inserted or processed. This is a Flow variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an end component in a  Talend  flow and it requires an input component. |
| Limitation | The NetSuite components do not support the Microservice and OSGI build types yet. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/netsuite/tnetsuiteoutput -->
# tNetSuiteOutput

Last updated: 9/30/2026

Invokes the NetSuite SOAP service and inserts, updates, or removes data on the
NetSuite SOAP server.

Information noteNote:

* This component works with two tNetSuiteOutput components: one for NetSuite version
  2019 databases and the other for NetSuite version 2019/2021/2025 databases.
* This component is available only when you have installed
  the 8.0.1-R2023-02 Talend Studio monthly
  update or a later one delivered by Talend. For
  more information, check with your administrator.

## tNetSuiteOutput Standard properties

These properties are used to configure tNetsuiteOutput running
in the Standard Job framework.

The Standard
tNetsuiteOutput component belongs to the Business
and the Cloud families.

## Basic settings

This component serves as an entry point for the NetSuite version 2019 databases and
NetSuite version 2019/2021 databases. To configure this component, select a NetSuite
database version from the Version drop-down list and click
Apply on its Basic settings view.

* Select NetSuite Deprecated from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite version 2019
  database. See [tNetSuiteOutput (v2019)](/talend/en-US/components/8.0/netsuite/tnetsuiteoutput-deprecated)
  for information about the component options.
* Select NetSuite SOAP from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite database that is of
  version 2019, 2021 or 2025. See [tNetSuiteOutput (v2019/2021/2025)](/talend/en-US/components/8.0/netsuite/tnetsuitev2019output) for information about the component
  options.

Information noteNote:

* For Jobs that contain tNetsuiteV2019Connection, tNetsuiteV2019Input, and
  tNetsuiteV2019Output components, the NetSuite components will be replaced by the
  corresponding NetSuite SOAP components when the Jobs are migrated, with the
  options set.
* For Jobs that contain NetSuite components that marked as deprecated,
  the NetSuite components will be replaced with legacy NetSuite components when the
  Jobs are migrated. In such Jobs, legacy NetSuite components can be switched to the
  new NetSuite components where some options will be pre-filled to aid the
  migration.
