<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tnetsuitev2019input · versión 8.0 -->
# tNetSuiteInput (v2019/2021/2025)

Last updated: 9/30/2026

Invokes the NetSuite SOAP service and retrieves data according to the conditions
you specify by leveraging NetSuite v2019/2021/2025 features.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tNetSuiteInput (v2019/2021/2025) Standard properties

These properties are used to configure tNetSuiteInput running in
the Standard Job framework.

The Standard
tNetSuiteInput component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote:

* This component is named tNetSuiteV2019Input if you do not install the
  8.0.1-R2023-02 Talend Studio
  monthly update or a later one delivered by Talend.
* This component is incorporated into the tNetSuiteInput component if you have
  installed the 8.0.1-R2023-02 Talend Studio
  monthly update or a later one delivered by Talend. To access this component in this case, select NetSuite
  SOAP from the Version drop-down list in the
  Basic settings view of the tNetSuiteInput component and
  click Apply. For more information, check with your
  administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Version | Select the NetSuite component you want to use from the drop-down list: NetSuite Deprecated for the NetSuite version 2019 component and Netsuite SOAP for the NetSuite version 2019/2021/2025 component. Click the Apply button to validate your selection.  Information noteNote: The Version drop-down list and the Apply button are available only when you have installed the 8.0.1-R2023-02 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Information noteWarning: The schema is created based on the NetSuite service fields (which vary with the Record type selected) when you click Guess schema. For a schema created in this way, you can remove schema columns that are not needed. However, to avoid possible execution errors, do not try to rename any schema columns. |
| Guess schema | Click this button to retrieve the schema from the data object specified. Information noteNote: Make sure you have set the record type in Record type before clicking this button. |
| API version | Select the version of the NetSuite API you are connecting to. |
| Account | Enter your NetSuite web services account number (also called account ID). |
| Login type | Select the login type: `Basic` or `Token-based`. |
| E-mail and Password | Enter your user credentials to access the NetSuite SOAP service.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only.  These two fields are available when `Basic` is selected from the Login type drop-down list. |
| Role ID | Enter your NetSuite role ID.  This field is available when `Basic` is selected from the Login type drop-down list. |
| Application ID | Enter the NetSuite application ID generated for your account.  An application ID is required starting from NetSuite version 2015 and above. You can find your application ID or create a new one on NetSuite's Manage Integration page.  This field is available when `Basic` is selected from the Login type drop-down list. |
| Consumer key and Consumer secret | Enter the consumer key and consumer secret generated in your NetSuite account.  To enter the consumer secret, click the [...] button next to the Consumer secret field to bring out the Enter a new password dialog box, enter the consumer secret in the text field, and click OK. Note that you can enter the consumer secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter consumer secrets in the Java   mode only.  These two fields are available when `Token-based` is selected from the Login type drop-down list. |
| Token ID and Token secret | Enter the token ID and token secret generated in your NetSuite account.  To enter the token secret, click the [...] button next to the Token secret field to bring out the Enter a new password dialog box, enter the token secret in the text field, and click OK. Note that you can enter the token secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter token secrets in the Java mode   only.  These two fields are available when `Token-based` is selected from the Login type drop-down list. |
| Record type | Click the [...] button next to the field to open a dialog box, and then select a record type you want to retrieve or select the Use custom object check box and specify a custom record type in the Object Name field. |
| Search conditions | Define search conditions to match fields for data retrieval. Click the [+] button to add as many rows as you need, each row for a condition, and define each of your conditions:  * Field: Select a field to search   based on the condition. * Operator: Enter an operator for   the field search condition. Check [Platform Enumerations](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N3471338.html) for a full list of   supported search operators.  Information noteNote: Search operators are case-sensitive. * Search value: Enter the value for   the field search condition. * Additional search value: Enter the   second value for the field search condition, if relevant depending on the   operator you select. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Set WSDL log level | Select the level of logging for the WSDL SOAP envelopes sent to NetSuite when executing your Job. By default, logs are disabled.  * Disabled: No WSDL logging is performed. * Debug: Logs SOAP envelopes at the debug level (key   debug information). * Trace: Logs SOAP envelopes at the trace level   (detailed information, including request and response payloads).   If you select Debug or Trace, ensure that the corresponding log level is enabled in the Advanced settings of the Run tab as well before executing your Job. If you select a higher log level like Info in the Run tab, the corresponding Debug or Trace logs will not be displayed in the Run console. |
| Enable customizations | Select this check box to instruct the component to retrieve customizations - custom record types and custom fields. With this option enabled, custom record types will be retrieved and can be selected in the Record Type dialog box, and custom fields will be retrieved and included into the schema.  This option is enabled by default. You can disable it if you don't need custom record types or custom fields.  Information noteNote: Transactional custom body fields for these transactions are not supported: Assembly Unbuild, Bin Putaway Worksheet, Bin Transfer, Paycheck, and Work Order. |
| Body fields only | Select this check box to retrieve only body fields; clear this check box to retrieve body fields and sublist values.  See [bodyFieldsOnly](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4170181850.html) for related information.  Information noteNote:  * Be sure to clear this check box if you also want to retrieve sublist values   in addition to values in the body fields. * Selecting this check box improves the performance significantly. |
| Page size | Enter the number of records to retrieve per page when the component reads data from NetSuite. The default value is `100`. Increase this value to reduce the number of SOAP requests for large datasets, or decrease it if your NetSuite tenant has stricter limits.  Information noteNote: This option applies only to NetSuite SOAP components. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component in a  Talend  flow and it requires an output component. |
| Limitation | The NetSuite components do not support the Microservice and OSGI build types yet. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/netsuite/tnetsuiteinput -->
# tNetSuiteInput

Last updated: 9/30/2026

Invokes the NetSuite SOAP service and retrieves data according to the conditions
you specify.

Information noteNote:

* This component works with two tNetSuiteInput components: one for NetSuite version
  2019 databases and the other for NetSuite version 2019/2021/2025 databases.
* This component is available only when you have installed
  the 8.0.1-R2023-02 Talend Studio monthly
  update or a later one delivered by Talend. For
  more information, check with your administrator.

## tNetSuiteInput Standard properties

These properties are used to configure tNetSuiteInput running in
the Standard Job framework.

The Standard
tNetsuiteInput component belongs to the Business and the Cloud families.

## Basic settings

This component serves as an entry point for the NetSuite version 2019 databases and
NetSuite version 2019/2021/2025 databases. To configure this component, select a
NetSuite database version from the Version drop-down list and
click Apply on its Basic settings view.

* Select NetSuite Deprecated from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite version 2019 database.
  See [tNetSuiteInput (v2019)](/talend/en-US/components/8.0/netsuite/tnetsuiteinput-deprecated) for information about the component
  options.
* Select NetSuite SOAP from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite database that is of
  version 2019, 2021 or 2025. See [tNetSuiteInput (v2019/2021/2025)](/talend/en-US/components/8.0/netsuite/tnetsuitev2019input) for information about the component
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
