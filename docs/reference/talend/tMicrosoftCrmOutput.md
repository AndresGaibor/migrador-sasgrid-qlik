<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/microsoft-crm/tmicrosoftcrmoutput · versión 8.0 -->
# tMicrosoftCrmOutput

Last updated: 9/30/2026

Writes data into a Microsoft Dynamics CRM database or a
Microsoft Dynamics 365 CRM database.

## tMicrosoftCrmOutput Standard properties

These properties are used to configure tMicrosoftCrmOutput running in the Standard Job framework.

The Standard
tMicrosoftCrmOutput component belongs to the Business family.

Information noteNote: Unless otherwise noted, CRM in this document refers to Microsoft
Dynamics CRM or Microsoft Dynamics 365 CRM, depending on
the CRM version used.

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
| Action | Select the action you want to perform on the CRM data, insert, update, or delete.  The CRM data could not be updated with NULL value for CRM ONLINE 2016 because of a limitation from Apache. For more information about the limitation, see <https://issues.apache.org/jira/browse/OLINGO-1114>. |
| Time out (second) | The number of seconds to wait for a reply message from the CRM server before closing the connection to it. |
| Entity/EntitySet | Select the relevant entity/entity set from the list or select `CustomEntity`/`CustomEntitySet` from the list, and then in the Custom Entity Name field displayed, specify the entity/entity set name and define the schema for the custom entity/entity set. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  The schema of this component is related to the specified entity. |
| Lookup Type Mapping | Complete this table to map the lookup property with its related entity type or entity set value.   * Input   column: the schema column name of the lookup   property. * Type: the   related entity type for the corresponding lookup property. It is   not available for ON-PREMISE 2016 and ONLINE 2016. * Reference   entityset: the name of the related entity set   for the corresponding lookup property. It is available only for   ON-PREMISE 2016 and ONLINE 2016. Refer to [Web API EntityType   Reference](https://msdn.microsoft.com/en-us/library/mt608066.aspx) for more information about the entity set   of the lookup property for each entity.   This option is not available for CRM ON-PREMISE 2015. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Reuse Http Client | Select this check box to retain the current connection or clear it to release the connection.  This option is not available for CRM ON-PREMISE 2015. |
| Transform empty lookup string values to NULL | Select this check box and the empty lookup string will be written into the CRM database as the NULL value.  This option is available for CRM ON-PREMISE 2016, ONLINE 2011, 2016, and 2018. |
| Ignore Null | Select this check box to ignore NULL values in the input data. |
| Max number of reconnection attempts | The maximum number of reconnect attempts to the CRM database after the token is expired. If the value is set to `0` or less than `0`, no reconnect attempt will be made.  This option is available for CRM ON-PREMISE 2016, ONLINE 2011, 2016, and 2018. |
| Custom headers | Add header-value pairs to HTTP requests to achieve specific purposes (for example, to specify the maximum number of pages that can be retrieved at each call). See [Compose HTTP requests and handle errors](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors) for more information.  To add an header-value pair, add a new line by clicking the plus button under the table and enter the header name and value in the corresponding columns.  This option is available for CRM ON-PREMISE 2016, ONLINE 2016 and 2018. |
| Return representation | Select this option to add a Prefer header with the return=representation preference, which retrieves data from created or updated entities. The data is returned in JSON strings. You need also to select a column from the Output column to hold the retrieved data.  See [HTTP headers](https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/compose-http-requests-handle-errors) for more information.  This option is available for CRM ON-PREMISE 2016, ONLINE 2016 and 2018. |
| Force OAuth resource | Select this option to use an OAuth resource other than the default. Enter the OAuth resource URL in the Resource field. If this option is not selected, the resource will be the host of the Service Root URL option from the Basic settings view.  This field is available when `OAUTH 2.0` is selected from the Mode drop-down list. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as an end component of a Job or subJob and it always needs an input link. |

**Related concepts**  

* [Writing data in a Microsoft Dynamics CRM database and putting conditions on columns to extract specified rows](tmicrosoftcrminput-tmicrosoftcrmoutput-tfileinputdelimited-tfileoutputdelimited-writing-data-in-microsoft-crm-database-and-putting-conditions-on-columns-to-extract-specified-rows-standard-component-this)
