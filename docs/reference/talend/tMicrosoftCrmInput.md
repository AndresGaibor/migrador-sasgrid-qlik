<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput · versión 8.0 -->
# tMicrosoftCrmInput

Last updated: 9/30/2026

Extracts data from a Microsoft Dynamics CRM or a
Microsoft Dynamics 365 CRM database based on conditions set on
specific columns.

## tMicrosoftCrmInput Standard properties

These properties are used to configure tMicrosoftCrmInput running in the Standard Job framework.

The Standard
tMicrosoftCrmInput component belongs to the Business family.

Information noteNote: Unless otherwise noted, CRM in this document refers to Microsoft
Dynamics CRM or Microsoft Dynamics 365
CRM, depending on the CRM version used.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Authentication Type | Select the authentication type that corresponds to your specific CRM deployment model.  * ON\_PREMISE: the CRM is installed in-house on the   customer's own servers, and licensing is purchased along with any   necessary infrastructure. * ONLINE: the customer accesses the CRM as part of a   cloud-based subscription service, hosted by Microsoft in their data   centers. |
| CRM Version | Select the version of the ON-PREMISE CRM database, `CRM 2016 (deprecated)`, or `CRM 2018`.  ON-PREMISE 2016 is implemented using Apache Olingo OData 4.0 libraries. For more information, see <http://olingo.apache.org/doc/odata4/index.html>. |
| Mode | Select the ON-PREMISE CRM2016 authentication mode, `NTLM` or `OAUTH 2.0`.  This option is available when `ON_PREMISE` is selected from the Authentication Type drop-down list and `CRM 2016` is selected from the CRM Version drop-down list. |
| Flow | Select the authentication flow to obtain the authentication token: Authorizationcode or Resource Owner Password Credentials.  This option is available when you select ON\_PREMISE from the Authentication Type drop-down list, CRM 2016 from the CRM Version drop-down list, and OAUTH 2.0 from the Mode drop-down list. Before the Resource Owner Password Credentials (ROPC) authentication flow gets available, the Authentication Code flow is used to obtain the token. See [Microsoft identity platform and OAuth 2.0 Resource Owner Password Credentials](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth-ropc) for information about ROPC.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-11 Talend Monthly update or a later one delivered by Talend Studio. For more information, check with your administrator. |
| API Version | Select the API version of the ONLINE CRM database, `v2007 (deprecated)`, `v2011 (deprecated)`, `v2016 (odata)`, or `v2018`.  ONLINE 2016 and 2018 are implemented using MS Dynamics WebAPI v8.1 (2016) and v9.1 (2018). For more information, see <https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/use-microsoft-dynamics-365-web-api?view=dynamics-ce-odata-9>.  You must set the Service Root URL to WebAPI v9.1 or higher when you select v2018 (use v8.1 when selecting v2016) as defined in the default value.  This option is available if ONLINE is selected from the Authentication Type drop-down list.  Information noteNote: API version 2007 and version 2011 are tagged as deprecated in accordance with Microsoft products and services lifecycle information if you have installed the 8.0.1-R2022-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Registered application type | Select the type of your application, either `Native App` or `Web App with delegated permissions`.  This option is available for CRM ONLINE 2016 and 2018. |
| Microsoft WebService URL | The Web Service URL of an on-premise CRM server.  This option is available for CRM ON-PREMISE 2011. |
| OrganizeName | The name of the organization that needs to access the CRM database.  This option is available for CRM ON-PREMISE 2011, ONLINE 2007, and ONLINE 2011. |
| Username and Password | The user authentication data required to access the CRM database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Domain | The domain name of the server on which the CRM database is hosted.  This option is available for CRM ON-PREMISE 2011 and 2016. |
| Host | The IP address of the CRM database server.  This option is available for CRM ON-PREMISE 2011, ON-PREMISE 2016, and ONLINE 2007. |
| Port | The listening port number of the CRM database server.  This option is available for CRM ON-PREMISE 2011. |
| Organization Wsdl URL | The WSDL URL of the Organization Service.  This option is available for CRM ON-PREMISE 2015. |
| Security Service URL | The URL of the Security Token Service.  This option is available for CRM ON-PREMISE 2015. |
| Trust Certificate | The path to the Trust Certificate file.  This option is available for CRM ON-PREMISE 2015. |
| Discovery service endpoint | The CRM online discovery service endpoint.  Because Microsoft regional Discovery service has been deprecated, make sure to use this endpoint URL to replace the one in this field: `https://globaldisco.crm.dynamics.com/api/discovery/v2.0/Instances`.  See topic Error code: DynamicsFailedToConnect at [Troubleshoot Azure Data Factory connectors](https://docs.microsoft.com/en-us/azure/data-factory/connector-troubleshoot-guide) and [Modify your code to use global Discovery Service](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/discovery-orgsdk-to-webapi) for related information.  This option is available for CRM ONLINE 2011. |
| Service Root URL | The root URL of the service to be connected.  This option is available for CRM ON-PREMISE 2016, ONLINE 2016 and 2018. |
| Application ID | The unique client ID that Azure AD assigns to your application when registering the application in the Azure portal. Note that the default client ID displayed in this field is for testing purpose. You need to apply a client ID of your own in actual use. For information on applying a client ID, see [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).  This option is available for Microsoft CRM ONLINE 2011, 2016, and 2018. |
| Application secret | The access key for your web application. For more information about how to get its value, see [Granting permissions to the application](/talend/en-US/components/8.0/microsoft-crm/granting-permissions-to-application).  This option is available when `Web App with delegated permissions` is selected from the Registered application type drop-down list. |
| Token endpoint | Enter the URL of the endpoint to retrieve the authentication token from.  This field is available when Resource Owner Password Credentials is selected from the Flow drop-down list. |
| OAuth authorization endpoint | The OAuth authorization endpoint to be used for the OAuth discovery. For more information, see [Endpoints](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols#endpoints).  This option is available for Microsoft CRM ONLINE 2011, 2016, and 2018.  This option is not available if Resource Owner Password Credentials is selected from the Flow drop-down list. |
| Redirect URL | Enter the OAuth 2.0 redirect URL.  This field is not available if `OAUTH 2.0` is not selected from the Mode drop-down list or Resource Owner Password Credentials is selected from the Flow drop-down list. |
| Time out (second) | The number of seconds to wait for a reply message from the CRM server before closing the connection to it. |
| Entity/EntitySet | Select the relevant entity/entity set from the list or select `CustomEntity`/`CustomEntitySet` from the list, and then in the Custom Entity Name field displayed, specify the entity/entity set name and define the schema for the custom entity/entity set. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   The schema of this component is related to the specified entity. |
| Custom filter | Select this check box and in the field displayed, specify the search criteria that uses the standard OData query functions such as contains, endswith, and startswith. For more information about the supported query functions, see the description of Standard query functions on [Query Data using the Web API](https://msdn.microsoft.com/en-us/library/gg334767.aspx#bkmk_filter).  This option is available for CRM ON-PREMISE 2016, ONLINE 2016 and 2018. |
| Logical operator used to combine conditions | Select the logical operator used to combine the conditions defined in Conditions table.   * And: the record will be included   in the result set when all of the conditions are met. * Or: the record will be included   in the result set when any of the conditions is met. |
| Conditions | Click the [+] button to add as many conditions as needed and specify the following parameters for each condition:   * Input column: Click in the cell   and select the column of the input schema on which the condition   is to be set. * Operator: Click in the cell and   select the operator used to compare the value for the input   column with the value defined in the Value column. The values for   this parameter are: `Equal`, `NotEqual`, `GreaterThan`, `LessThan`, `GreaterEqual`, `LessEqual`, and `Like`. * Value: Type in the value   between quotes if needed. If you are using CRM ONLINE or   ON-PREMISE version 2016 (or a later version), to filter data   using a column that is an ID (for example,   salesorderid), you need to enter an   expression in this field that converts the ID into a Java UUID,   such as   java.util.UUID.fromString("*your\_salesorderid*"). |
| Order by | Select this check box and in the table displayed, specify the column(s) based on which the retrieved data will be sorted in ascending or descending order. Multiple sort columns can be specified and the hierarchy of the sorting is based on the order of the columns specified. That is to say, the retrieved data will be sorted by the first column and then that ordered list is sorted by the second column, and so on.  This option is available for CRM ON-PREMISE 2016, ONLINE 2016 and 2018. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Reuse Http Client | Select this check box to retain the current connection or clear it to release the connection.  This option is not available for CRM ON-PREMISE 2015. |
| Max number of reconnection attempts | The maximum number of reconnect attempts to the CRM database after the token is expired. If the value is set to `0` or less than `0`, no reconnect attempt will be made.  This option is available for CRM ON-PREMISE 2016, ONLINE 2011, 2016, and 2018. |
| Force OAuth resource | Select this option to use an OAuth resource other than the default. Enter the OAuth resource URL in the Resource field. If this option is not selected, the resource will be the host of the Service Root URL option from the Basic settings view.  This field is available when `OAUTH 2.0` is selected from the Mode drop-down list. |
| Expand entity | Retrieve expanded entity properties and write the properties to dedicated columns. Expanded entity properties are written in columns as JSON strings.  To retrieve and write specific properties of an expanded entity to a column, add a row in the table by clicking the plus button under the table, select from the drop-down list the expandable column that references the expanded entity in Expandable column, enter the desired properties of the expanded entity in the OData query option column, and select the destination column from the drop-down list in Destination column column.  Information noteNote: The name of an expandable column begins with \_ and ends with \_value.  You can specify one or multiple properties in the OData query option column in the format of `$select={property_1_name},{property_2_name},...`. At least one property needs to be provided. To retrieve and write all the properties of the expanded entity, enter `$select=*` in this column. See [How to build an OData Service with Olingo V4 Part 5.2: System Query Options: $select, $expand](https://olingo.apache.org/doc/odata4/tutorials/sqo_es/tutorial_sqo_es.html) for related information.  This field is available with the Authentication Type of `ON_PREMISE` (CRM 2016 required) and `ONLINE` (API version 2016 and higher required). |
| Custom headers | Add header-value pairs to HTTP requests to achieve specific purposes (for example, to specify the maximum number of pages that can be retrieved at each call). See [Compose HTTP requests and handle errors](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors) for more information.  To add an header-value pair, add a new line by clicking the plus button under the table and enter the header name and value in the corresponding columns.  This option is available for CRM ON-PREMISE 2016, ONLINE 2016 and 2018. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as a start component of a Job or subJob and it always needs an output link. |
| Limitation | tMicrosoftCrmInput (both ONLINE 2016 and ON-PREMISE 2016) doesn't support retrieving data of the write-only properties. The corresponding schema columns for the write-only properties have been removed from the predefined schema. |

**Related concepts**  

* [Writing data in a Microsoft Dynamics CRM database and putting conditions on columns to extract specified rows](tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-writing-data-in-microsoft-crm-database-and-putting-conditions-on-columns-to-extract-specified-rows-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-writing-data-in-microsoft-crm-database-and-putting-conditions-on-columns-to-extract-specified-rows-standard-component-this -->
# Writing data in a Microsoft Dynamics CRM database and putting conditions on columns to extract specified rows

Last updated: 9/30/2026

This scenario describes a four-component Job which aims at writing the data
included in a delimited input file in a custom entity in a Microsoft Dynamics CRM database.
It then extracts specified rows to an output file using the conditions set on certain input
columns.

Information noteWarning:

If you want to write in a CustomEntity in a Microsoft Dynamics CRM
database, make sure to name the columns in accordance with the naming rule set by
Microsoft, that is "name\_columnname" all in lower case.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-setting-up-job-standard-component-drop)
* [Configuring tFileInputDelimited](/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tfileinputdelimited-standard-component)
* [Configuring tMicrosoftCrmOutput](/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tmicrosoftcrmoutput-standard-component)
* [Configuring tMicrosoftCrmInput](/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tmicrosoftcrminput-standard-component)
* [Configuring tFileOutputDelimited](/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tfileoutputdelimited-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-executing-job-standard-component-save)

**Related reference**  

* [tMicrosoftCrmInput](tmicrosoftcrminput "Extracts data from a Microsoft Dynamics CRM or a Microsoft Dynamics 365 CRM database based on conditions set on specific columns.")
* [tMicrosoftCrmOutput](tmicrosoftcrmoutput "Writes data into a Microsoft Dynamics CRM database or a Microsoft Dynamics 365 CRM database.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tfileinputdelimited-standard-component -->
# Configuring tFileInputDelimited

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputDelimited to display
   its Basic settings view and define its
   properties.
2. Set the Property Type to Repository if you have stored the input file
   properties centrally in the Metadata node in
   the Repository tree view. Otherwise, select
   Built-In and fill the fields that follow
   manually. In this example, property is set to Built-In.
3. Click the [...] button next to the File name/Stream
   field and browse to the delimited file that holds the input data. The input file
   in this example contains the following columns: *new\_id*,
   *new\_status*, *new\_firstname*,
   *new\_email*, *new\_city*,
   *new\_initial* and
   *new\_zipcode*.
4. In the Basic settings view, define the
   Row Separator allowing to identify the end
   of a row. Then define the Field Separator used
   to delimit fields in a row.
5. If needed, define the header, footer and limit number of processed rows in the
   corresponding fields. In this example, the header, footer and limits are not
   set.
6. Click Edit schema to open a
   dialog box where you can define the input schema you want to write in the Microsoft
   Dynamics CRM database.
7. Click OK to close the dialog box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tfileoutputdelimited-standard-component -->
# Configuring tFileOutputDelimited

Last updated: 9/30/2026

## Procedure

1. Double-click tFileOutputdelimited to display
   the component Basic settings view and define
   its properties.
2. Set Property Type to Built-In and then click the [...] button next to the File
   Name field and browse to the output file.
3. Set row and field separators in the corresponding fields.
4. Select the Append check box if you want to
   add the new rows at the end of the records.
5. Select the Include Header check box if the
   output file includes a header.
6. Click Sync columns to retrieve the schema
   from the preceding component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tmicrosoftcrminput-standard-component -->
# Configuring tMicrosoftCrmInput

Last updated: 9/30/2026

## Procedure

1. Double-click tMicrosoftCrmInput to display
   the component Basic settings view and define
   its properties.
2. Set the Property Type to Repository if you have stored the input file
   properties centrally in the Metadata node in
   the Repository tree view. Otherwise, select
   Built-In and fill the fields that follow
   manually. In this example, property is set to Built-In.
3. Enter the Microsoft Web Service URL as well as the user name and
   password in the corresponding fields and enter the name that is given the right to
   access the Microsoft Dynamics CRM database in the OrganizeName field.
4. In the Domain field, enter
   the domain name of the server on which the Microsoft Dynamics CRM database is hosted,
   and then enter the host IP address and the listening port number in the corresponding
   fields.
5. In the Time out field, set the amount of time
   (in seconds) after which the Job will time out.
6. In the Entity list, select the one among
   those offered you want to connect to. In this example,
   *CustomEntity* is selected.
7. The Schema is then automatically set
   according to the entity selected. But you can modify it according to your needs.
   In this example, you should set the schema manually since you want to access a
   custom entity. Copy the seven-column schema from tMicrosoftCrmOutput and paste it in the schema dialog box in
   tMicrosoftCrmInput.
8. Click OK to close the dialog box. You will be
   prompted to propagate changes. Click Yes in the
   popup message.
9. In the Basic settings view, select And or Or as the
   logical operator you want to use to combine the conditions you set on the input
   columns. In this example, we want to set two conditions on two different input
   columns and we use And as the logical
   operator.
10. In the Condition area, click the plus button
    to add as many lines as needed and then click in each line in the Input column list and select the column you want to
    set condition on. In this example, we want to set conditions on two columns,
    *new\_city* and *new\_id*. We want to
    extract all customer rows whose city is equal to "New York" and whose id is
    greater than 2.
11. Click in each line in the Operator list and
    select the operator to bind the input column with its value, in this example
    Equal is selected for
    *new\_city* and Greater
    Than for *new\_id*.
12. Click in each line in the Value list and set
    the column value, New York for *new\_city* and
    2 for *new\_id* in this example. You can use
    a fixed or a context value in this field.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-configuring-tmicrosoftcrmoutput-standard-component -->
# Configuring tMicrosoftCrmOutput

Last updated: 9/30/2026

## Procedure

1. Double-click tMicrosoftCrmOutput to display
   the component Basic settings view and define
   its properties.
2. Enter the Microsoft Web Service URL as well as the user name and password in
   the corresponding fields.
3. In the OrganizeName field,
   enter the name that is given the right to access the Microsoft Dynamics CRM
   database.
4. In the Domain field, enter
   the domain name of the server on which Microsoft Dynamics CRM database is hosted, and
   then enter the host IP address and the listening port number in the corresponding
   fields.
5. In the Action list, select
   the operation you want to carry on. In this example, we want to insert data in a
   custom entity in the Microsoft Dynamics CRM database.
6. In the Time out field, set the amount of time
   (in seconds) after which the Job will time out.
7. In the Entity list, select one among those
   offered. In this example, *CustomEntity* is selected.

   Information noteNote:

   If *CustomEntity* is selected, a Custom Entity Name field displays where you need to enter a
   name for the custom entity.

   The Schema is then automatically set
   according to the entity selected. If needed, click Edit
   schema to display a dialog box where you can modify this schema
   and remove the columns that you do not need in the output.
8. Click Sync columns to retrieve the schema
   from the preceding component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-executing-job-standard-component-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Save the Job and press F6 to execute it.

## Results

Only customers who live in New York city and those whose "id" is
greater than 2 are listed in the output file you stored locally.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette to the design workspace: tFileInputDelimited, tFileOutputDelimited, tMicrosoftCrmInput, and tMicrosoftCrmOutput.
2. Connect tFileInputDelimited to tMicrosoftCrmOutput using a Row > Main
   connection.
3. Connect tMicrosoftCrmIntput to tFileOutputDelimited using a Row > Main
   connection.
4. Connect tFileInputDelimited to tMicrosoftCrmInput using Trigger > OnSubjobOk
   connection.
