<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec · versión 8.0 -->
# tSalesforceOutputBulkExec

Last updated: 9/30/2026

Bulk-loads data in a given file into a Salesforce object.

The tSalesforceOutputBulk
and tSalesforceBulkExec components are used together
in a two step process. In the first step, an output file is generated. In the second
step, this file is used to feed the Salesforce database. These two steps are fused
together in the tSalesforceOutputBulkExec component.
The advantage of using two separate steps is that the data can be transformed before it
is loaded into Salesforce.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSalesforceOutputBulkExec Standard properties

These properties are used to configure tSalesforceOutputBulkExec running in the Standard Job framework.

The Standard
tSalesforceOutputBulkExec component belongs to the Business and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Component list | Select the component that opens the database connection to be reused by this component. |
| Connection type | Select the type of the connection from the drop-down list. The connection properties will vary according to the connection type you choose.   * Basic (deprecated): This option uses the legacy   username, password, and security token ("SOAP API login()") to authenticate   with Salesforce. Salesforce will retire support for SOAP API login() in API   versions 31.0 through 64.0 starting with the Summer ‘27 release, and it is   not available in API versions 65.0 and later. As such, Basic authentication   is deprecated and may stop working in the near future regardless of the   selected API version. * OAuth: This option uses OAuth (Open Authorization)   2.0 protocol to authenticate the user with the Json Web Token   Flow OAuth 2.0 authentication flow type. To use this option,   you need to create a connected app in Salesforce to configure a Salesforce   authentication provider.  For more information about the OAuth authentication flow, see [Authenticate Apps with OAuth](https://help.salesforce.com/articleView?id=remoteaccess_authenticate.htm&type=5).  For more information about how to create a connected app in Salesforce, see   [Create a Connected App](https://help.salesforce.com/articleView?id=connected_app_create.htm&type=5). |
| User Id | The Salesforce username.  This property is available only when the Basic connection type is selected. |
| Password | The Salesforce password associated with the username.  This property is available only when the Basic connection type is selected. |
| Security Token | The Salesforce security token. For more information, see [Reset Your Security Token](https://help.salesforce.com/articleView?id=user_security_token.htm&type=5).  This property is available only when the Basic connection type is selected. |
| Mutual authentication | Select this option to enable mutual authentication for establishing connections to Salesforce. For more information about mutual authentication in Salesforce, see [Set Up a Mutual Authentication Certificate](https://help.salesforce.com/s/articleView?id=sf.security_keys_uploading_mutual_auth_cert.htm&type=5).  If you are using this option:  * On the component side, use a [tSetKeystore](/talend/r/en-US/8.0/components/keystore/tsetkeystore) component to   provide the mutual authentication keystore and keystore password. * On the metadata side, go to Window > Preferences > Talend > Security > SSL, and set the corresponding keystore configuration.  By default, this option is not selected. |
| Mutual auth keystore (Deprecated) | Enter the path to the mutual authentication keystore file, a password protected file containing keys and certificates.  This option is deprecated, it is recommended to use a [tSetKeystore](/talend/r/en-US/8.0/components/keystore/tsetkeystore) component to provide the mutual authentication keystore and keystore password.  This option is available when both the Basic connection type and the Mutual authentication check box are selected. |
| Mutual auth keystore password | Enter the password for the mutual authentication keystore file.  This option is available when both the Basic connection type and the Mutual authentication check box are selected. |
| Issuer | The OAuth Consumer Key, generated when your connected app is created and shown in the connected app detail page in Salesforce. For more information, see [Create a Connected App](https://help.salesforce.com/articleView?id=connected_app_create.htm&type=5).  This property is available only when the OAuth connection type is selected. |
| Subject | The Salesforce username.  This property is available only when the OAuth connection type is selected. |
| Audience | Json Web Token audience.  You can set your own Json Web Token audience.  This property is available only when the OAuth connection type is selected. |
| Expiration time (in seconds) | The expiration time of the assertion (in seconds) within five minutes.  This property is available only when the OAuth connection type is selected. |
| Key store | The path to the keystore file in Java Keystore (JKS) format.  The keystore file can be generated by creating a certificate signed by Salesforce and then exporting it to keystore. For more information, see [Generate a Self-Signed Certificate](https://help.salesforce.com/articleView?id=security_keys_creating.htm&type=5).  This property is available only when the OAuth connection type is selected. |
| Key store password | The keystore password.  This property is available only when the OAuth connection type is selected. |
| Certificate alias | The unique name of the certificate signed by Salesforce.  This property is available only when the OAuth connection type is selected. |
| Client Id | The OAuth Consumer Key, generated when your connected app is created and shown in the connected app detail page in Salesforce. For more information, see [Create a Connected App](https://help.salesforce.com/articleView?id=connected_app_create.htm&type=5).  This property is available only when the OAuth Implicit Flow type is selected. |
| Client Secret | The OAuth Consumer Secret, generated when your connected app is created and shown in the connected app detail page in Salesforce. For more information, see [Create a Connected App](https://help.salesforce.com/articleView?id=connected_app_create.htm&type=5).  This property is available only when the OAuth Implicit Flow type is selected. |
| Callback Host | The host value in the OAuth authentication callback URL that is defined during the creation of a connected app and will be shown in the API (Enable OAuth Settings) area of the connected app detail page in Salesforce.  This property is available only when the OAuth Implicit Flow type is selected. |
| Callback Port | The port value in the OAuth authentication callback URL that is defined during the creation of a connected app and will be shown in the API (Enable OAuth Settings) area of the connected app detail page in Salesforce.  This property is available only when the OAuth Implicit Flow type is selected. |
| Token File | The path to the token file that stores the refresh token used to get the access token without authorization.  This property is available only when the OAuth Implicit Flow type is selected. |
| Module Name | Click the [...] button next to the field and in the dialog box displayed, select the module that will be used or select the Use custom object check box and specify the module name in the Object Name field. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Output Action | Select one of the following operations to be performed from the drop-down list.   * INSERT: insert one or more new records into   Salesforce. * UPDATE: update one or more existing records in   Salesforce. * UPSERT: create new records or update existing   records. In the Upsert Key Column field displayed,   specify the key column for the upsert operation. By selecting   Output upsert column, a column named   UpsertColumnValue will be added to the output   schema. The column holds upsert key values and thus can be used to monitor   the upsert key. You can select Output upsert column   if the upsert key is a variable. * DELETE: delete one or more records in Salesforce. |
| Bulk File Path | Specify the path to the file that stores the data to be processed. |
| Append | Select this check box to append new data at the end of the file if it already exists, instead of overwriting the existing data. |
| Ignore Null | Select this check box to ignore NULL values. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Salesforce URL | The Webservice URL required to connect to Salesforce.  Information noteWarning: Due to a [breaking change](https://help.salesforce.com/s/articleView?id=release-notes.rn_security_mutual_authentication.htm&release=246&type=5) in the latest versions of Salesforce, if you use the Basic connection type with mutual authentication, you need to adjust the endpoint to prevent errors while running the Job. Example: `https://MyDomainName.my.salesforce.com:8443/services/Soap/u/version` |
| API version | The Salesforce API version.  This property is available only when the OAuth connection type is selected. |
| Need compression | Select this check box to activate SOAP message compression, which can result in increased performance levels. |
| Trace HTTP message | Select this check box to output the HTTP interactions on the console. |
| Client Id | Enter the ID of the real user to differentiate between those who use the same account and password to access the Salesforce website. |
| Timeout | Enter the intended number of query timeout in milliseconds in Salesforce. |
| Use Proxy | Select this check box to use a SOCKS proxy server, and in the Host, Port, User Id, and Password fields displayed, specify the connection parameters of the SOCKS proxy server.  Information noteNote: To use a proxy of any allowed type (including HTTP proxy, HTTPS proxy, and SOCKS proxy), use the tSetProxy component. |
| Bulk API V2 | Select this check box to create a Bulk API V2 Job, and then select a type of field delimiter from the Column Delimiter drop-down list and a way of line ending from the Line Ending drop-down list respectively for CSV data.  Compared with Bulk API V1, Bulk API v2 simplifies the way of processing data.  This property is available only when the OAuth connection type is selected. |
| Relationship mapping for upsert | Click the [+] button to add lines as needed and specify the external ID fields in the input flow, the lookup relationship fields in the upsert module, the lookup module as well as the external ID fields in the lookup module.   * Column name of Talend Schema: the name of the external ID field in the input flow. It   refers to the fields in the schema of the preceding component. Such columns are   intended to match against the external ID fields specified in the   External id name column, which are the fields of the   lookup module specified in the Module name column. * Lookup relationship field name: the name of the lookup   relationship field. It refers to the lookup relationship fields of the module   specified in the Module Name field in the Basic   settings view and is intended to establish relationship with the   lookup module specified in the Module name column in this   table. You can enter built-in relationship fields and custom relationship fields.   For information about how to define the lookup relationship fields and how to   provide their correct names in the Lookup relationship field   name field, go to the Salesforce website and launch the Salesforce   Data Loader application for proper actions and information. * Module   name: the name of the lookup module. * Polymorphic: select this check box when and only when   polymorphic fields are used for relationship mapping. You will get an error if you   keep this check box cleared for a polymorphic field or select it for a field that   is not polymorphic. For more information about the polymorphic fields, search   `polymorphic` at <http://www.salesforce.com/us/developer/docs/api_asynch/>. * External   id name: the name of the external ID field in the lookup module   specified in the Module name column.   This property is available only when UPSERT is selected from the Output Action drop-down list. |
| Concurrency Mode | Select the concurrency mode for the Job.   * Parallel: process batches in parallel mode. * Serial: process batches in serial mode. |
| Rows to Commit | Specify the number of lines per data batch to be processed. |
| Bytes to Commit | Specify the number of bytes per data batch to be processed. |
| Wait Time Check Batch State | Specify the wait time (in milliseconds) for checking whether the batches in a Job have been processed until all batches are finally processed. |
| Safety Switch | Clear this check box if the length of any column of the module to be queried is longer than 100,000 characters. By default, this check box is selected to prevent excessive memory usage.  This property is available when Bulk or BulkV2 is selected from the Query Mode drop-down list. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded into Salesforce. |
| Limitation | The bulk data to be processed in Salesforce should be in .csv format. |
| Limitation | If you change the component schema or any of the following parameters — Output Action, Upsert Key Column, or Output upsert column — click Guess Schema on Schema MAIN and Reject Schema to refresh the output schemas accordingly.  Information noteNote: This behavior will be improved in a future release to support automatic schema updates. |

**Related concepts**  

* [Inserting bulk data into Salesforce](tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-inserting-bulk-data-into-salesforce-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-inserting-bulk-data-into-salesforce-standard-component-this -->
# Inserting bulk data into Salesforce

Last updated: 9/30/2026

This scenario describes a four-component Job that bulk-loads data in a file
into Salesforce, performs the intended action on the data, and ends up with displaying the Job
execution results on the console.

The content of the input file SalesforceAccount.txt used
in this example is as follows:

```
Name;ParentId;Phone;Fax
Burlington Textiles Corp of America;;(336) 222-7000;(336) 222-8000
Dickenson plc;; (785) 241-6200;(785) 241-6201
GenePoint;;(650) 867-3450;(650) 867-9895
Edge Communications;talend;(512) 757-6000;(512) 757-9000
Grand Hotels & Resorts Ltd;talend;(312) 596-1000;(312) 596-1500
```

### In this section

* [Setting up the Job for inserting bulk data into Salesforce](/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-setting-up-job-for-inserting-bulk-data-into-salesforce-standard-component-create)
* [Configuring the Job for inserting bulk data into Salesforce](/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-configuring-job-for-inserting-bulk-data-into-salesforce-standard-component)
* [Executing the Job to insert bulk data into Salesforce](/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-executing-job-to-insert-bulk-data-into-salesforce-standard-component-press)

**Related reference**  

* [tSalesforceOutputBulkExec](tsalesforceoutputbulkexec "Bulk-loads data in a given file into a Salesforce object.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-configuring-job-for-inserting-bulk-data-into-salesforce-standard-component -->
# Configuring the Job for inserting bulk data into Salesforce

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited component to open its Basic settings view.
2. In the File name/Stream
   field, browse to or enter the path to the input data file. In this example, it
   is D:/SalesforceAccount.txt.
3. Click the [...] button
   next to Edit schema and in the pop-up
   schema dialog box, define the schema by adding four columns
   `Name`, `ParentId`,
   `Phone` and `Fax` of String type.
   When done, click OK to save the changes
   and close the dialog box.
4. Double-click the tSalesforceOutputBulkExec component to open its Basic settings view.
5. In the User Id,
   Password and Security Key fields, enter the user
   authentication information required to access Salesforce.
6. Click the [...] button
   next to the Module Name field and in the
   pop-up dialog box, select the object you want to access. In this example, it is
   `Account`.
7. In the Bulk File Path
   field, browse to or enter the path to the CSV file that stores the data for bulk
   processing. The bulk file to be processed must be in csv format.
8. Double-click the first tLogRow component to open its Basic
   settings view.
9. In the Mode area, select
   Table (print values in cells of a
   table) for better readability of the results.
10. Do the same to configure the second tLogRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-executing-job-to-insert-bulk-data-into-salesforce-standard-component-press -->
# Executing the Job to insert bulk data into Salesforce

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the
   Job.

   On the console of the Run view, you
   can check the execution result.

   In the `tLogRow_1` table, you can read the data inserted
   into Salesforce.

   In the `tLogRow_2` table, you can read the rejected data
   due to the incompatibility with the Account objects you have accessed.

   Note that if you want to transform the input data before loading them into
   Salesforce, you need to use tSalesforceOutputBulk and tSalesforceBulkExec in cooperation to achieve this
   purpose.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/salesforce/tsalesforceoutputbulkexec-tlogrow-tfileinputdelimited-tfileinputdelimited-setting-up-job-for-inserting-bulk-data-into-salesforce-standard-component-create -->
# Setting up the Job for inserting bulk data into Salesforce

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tFileInputDelimited component, a tSalesforceOutputBulkExec component, and two tLogRow components by typing their names on the
   design workspace or dropping them from the Palette.
2. Link the tFileInputDelimited component to the tSalesforceOutputBulkExec component using a Row > Main connection.
3. Link the tSalesforceOutputBulkExec component to the first tLogRow component using a Row > Main connection.
4. Link the tSalesforceOutputBulkExec
   component to the second tLogRow component
   using a Row > Reject connection.
