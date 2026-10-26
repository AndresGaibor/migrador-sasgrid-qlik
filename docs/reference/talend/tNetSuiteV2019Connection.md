<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/tnetsuitev2019connection · versión 8.0 -->
# tNetSuiteConnection (v2019/2021/2025)

Last updated: 9/30/2026

Creates a connection to a NetSuite SOAP server by leveraging NetSuite
v2019/2021/2025 features so that other NetSuite components in the Job can reuse the
connection.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tNetSuiteConnection (v2019/2021/2025) Standard properties

These properties are used to configure tNetSuiteConnection
running in the Standard Job framework.

The Standard
tNetSuiteConnection component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote:

* This component is named tNetSuiteV2019Connection if you do not install the
  8.0.1-R2023-02 Talend Studio
  monthly update or a later one delivered by Talend.
* This component is incorporated into the tNetSuiteConnection component if you have
  installed the 8.0.1-R2023-02 Talend Studio
  monthly update or a later one delivered by Talend. To access this component in this case, select NetSuite
  SOAP from the Version drop-down list in the
  Basic settings view of the tNetSuiteConnection component
  and click Apply. For more information, check with your
  administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Version | Select the NetSuite component you want to use from the drop-down list: NetSuite Deprecated for the NetSuite version 2019 component and Netsuite SOAP for the NetSuite version 2019/2021/2025 component. Click the Apply button to validate your selection.  Information noteNote: The Version drop-down list and the Apply button are available only when you have installed the 8.0.1-R2023-02 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Property Type | Select the way the connection details will be set.  * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component. You need to click the   [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection properties   will be automatically filled in. |
| API version | Select the version of the NetSuite API you are connecting to. |
| Account | Enter your NetSuite web services account number (also called account ID). |
| Login type | Select the login type: `Basic` or `Token-based`. |
| E-mail and Password | Enter your user credentials to access the NetSuite SOAP service.  To enter the password, click the [...] button next to the Password field to bring out the Enter a new password dialog box, enter the password in the text field, and click OK. Note that you can enter the password either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter passwords in the Java mode   only.  These two fields are available when `Basic` is selected from the Login type drop-down list. |
| Role ID | Enter your NetSuite role ID.  This field is available when `Basic` is selected from the Login type drop-down list. |
| Application ID | Enter the NetSuite application ID generated for your account.  An application ID is required starting from NetSuite version 2015 and above. You can find your application ID or create a new one on NetSuite's Manage Integration page.  This field is available when `Basic` is selected from the Login type drop-down list. |
| Consumer key and Consumer secret | Enter the consumer key and consumer secret generated in your NetSuite account.  To enter the consumer secret, click the [...] button next to the Consumer secret field to bring out the Enter a new password dialog box, enter the consumer secret in the text field, and click OK. Note that you can enter the consumer secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter consumer secrets in the Java   mode only.  These two fields are available when `Token-based` is selected from the Login type drop-down list. |
| Token ID and Token secret | Enter the token ID and token secret generated in your NetSuite account.  To enter the token secret, click the [...] button next to the Token secret field to bring out the Enter a new password dialog box, enter the token secret in the text field, and click OK. Note that you can enter the token secret either in a JSON string in the pure password mode or as a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. Information noteNote:  * The two password modes are available only when you have installed the   8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend. For more information, check with your administrator. * If the 8.0.1-R2022-05 Talend Studio   monthly update or a later one delivered by Talend   is not installed, you can enter token secrets in the Java mode   only.  These two fields are available when `Token-based` is selected from the Login type drop-down list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Set WSDL log level | Select the level of logging for the WSDL SOAP envelopes sent to NetSuite when executing your Job. By default, logs are disabled.  * Disabled: No WSDL logging is performed. * Debug: Logs SOAP envelopes at the debug level (key   debug information). * Trace: Logs SOAP envelopes at the trace level   (detailed information, including request and response payloads).   If you select Debug or Trace, ensure that the corresponding log level is enabled in the Advanced settings of the Run tab as well before executing your Job. If you select a higher log level like Info in the Run tab, the corresponding Debug or Trace logs will not be displayed in the Run console. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other NetSuite components. |
| Limitation | The NetSuite components do not support the Microservice and OSGI build types yet. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/netsuite/tnetsuiteconnection -->
# tNetSuiteConnection

Last updated: 9/30/2026

Opens a connection to a NetSuite database to be reused in the subsequent subJob or
subJobs.

Information noteNote:

* This component works with two tNetSuiteConnection components: one for NetSuite
  version 2019 databases and the other for NetSuite version 2019/2021/2025 databases.
* This component is available only when you have installed
  the 8.0.1-R2023-02 Talend Studio monthly
  update or a later one delivered by Talend. For
  more information, check with your administrator.

## tNetSuiteConnection Standard properties

These properties are used to configure tNetSuiteConnection
running in the Standard Job framework.

The Standard
tNetSuiteConnection component belongs to the Business family.

## Basic settings

This component serves as an entry point for the NetSuite version 2019 databases and
NetSuite version 2019/2021/2025 databases. To configure this component, select a
NetSuite database version from the Version drop-down list and
click Apply on its Basic settings view.

* Select NetSuite Deprecated from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite version 2019 database.
  See [tNetSuiteConnection (v2019)](/talend/en-US/components/8.0/netsuite/tnetsuiteconnection-deprecated) for information about component
  options.
* Select NetSuite SOAP from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite database that is of
  version 2019, 2021 or 2025. See [tNetSuiteConnection (v2019/2021/2025)](/talend/en-US/components/8.0/netsuite/tnetsuitev2019connection) for information about the
  component options.

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
