<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsapodataoutput · versión 8.0 -->
# tSAPODataOutput

Last updated: 9/30/2026

Inserts, updates, or deletes data from an SAP OData web service.

## tSAPODataOutput Standard properties

These properties are used to configure
tSAPODataOutput running in the Standard Job
framework.

The Standard
tSAPODataOutput component belongs to the Business family.

The component in this framework is available in all
subscription-based Talend
products.

This component is available only when you have installed the 8.0.1-R2025-06 Talend Studio monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.   * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its   Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings.  When retrieving data from OData, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Entity set option, the, Specify entity key option, the $filter/search/select/expand option, and the Return type option. |
| Root URL | Type in the URL address identifying the base URL of the SAP OData service you want to access, that is to say the host and port of the SAP server. |
| Username and Password | Enter the credentials used as basic authentication to access the server. Information noteTip: To enter a password, a token, or a client secret key, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the password, the token, or the secret key in the text field, and click OK. Note that you can enter either a JSON string in the pure password mode or a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. |
| Path | Enter the catalog service path.  Example:  Root URL = http://<server>:<port> and Path = `/sap/opu/odata4/IWFND/config/default/iwfnd/CATALOGSERVICE` |
| Guess catalog service path | Click this button to retrieve the default path of the SAP OData catalog service. For more information, see [Catalog service](https://help.sap.com/doc/saphelp_nw74/7.4.16/en-US/7c/a326519eff236ee10000000a445394/content.htm?no_cache=true). |
| OData V4 parameters (optional) | Specify the extra parameters needed to fine-tune your request to the service:  * Search by API group ID: Use this field to filter   the list on the API group identifiers by adding an asterisk (\*) at the   beginning or end of the value. * Search by API description: Use this field to   filter the list on the API descriptions by adding an asterisk (\*) at the   beginning or end of the value. * API group ID: Select the identifier of the group   you want to retrieve. This list is populated based on the two previous   parameters.   For more information, see [The Groups and related API](https://help.sap.com/docs/SAP_JAM_COLLABORATION/9981b6fb8453459d8103a04d674ebe0f/cc2bb683ad4a445b95e296be924ea3f0.html). |
| OData V2 parameters (optional) | Specify the extra parameters needed to fine-tune your request to the service:  * Search by service ID: Use this field to filter on   the service identifiers by adding an asterisk (\*) at the beginning or end   of the value. * Search by service description: Use this field to   filter the list on the service descriptions by adding an asterisk (\*) at   the beginning or end of the value. * Search by service type: Use this field to filter   the list on the service types by adding an asterisk (\*) at the beginning   or end of the value. * Search by service version: Use this field to   filter the list on the service versions by adding an asterisk (\*) at the   beginning or end of the value. * Search by service author: Use this field to filter   the list on the service authors by adding an asterisk (\*) at the   beginning or end of the value. |
| Service URL | Select a service URL from the list. Values are either based on the selected API group (for OData v4) or generated using the filter parameters (for OData v2). |
| Entity set | Enter or select the specific entity set you want to retrieve from the service. For more information, see [Addressing Entities](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752340). Information noteTip: To visualize all available entity sets, click the [...] button next to the corresponding field to bring out the Retrieve values dialog box, and click Run in background. A new dialog box opens with all the retrieved entity sets you can select. Note that you can also provide a Custom value by selecting the Use custom value check box.  This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after setting the key/value pairs in the table under this option. |
| Output action | Select an operation to be performed from the drop-down list.   * Insert: Inserts new records in the previously   defined entity set. * Update: Modifies existing records in the   previously defined entity set. The available update types are   Patch (updates existing records with modified   properties), or Replace (overwrites existing   records with new ones). * Delete: Deletes existing records in the previously   defined entity set. |
| Specify the request configuration | Select this option to configure your request.  * Key value: Enter the existing value you want to   update or delete. This option is only available if you select either   Update or Delete from   the Output action list. * Request body: Enter the body of the message you   want to include in the request. The format needs to match the format   selected in the Request body format field. JSON   example: ```   {    "id": "184",    "lastname": "Truce",    "age": "37",    }   ```  This option is only available if you select   either Insert or Update   from the Output action list.  XML example: ```   <user>    <id>184</id>    <name>Truce</name>    <age>37</age>   </user>   ``` * Request body format: Set the body format by   selecting the corresponding option. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |
| Connection timeout (ms) | Set the timeout period (in milliseconds) for the connector to establish a connection to the server. An error occurs if an attempt to establish a connection fails. |
| Receive timeout (ms) | Set the timeout period (in milliseconds) for receiving response data. An error occurs if no data is received when the read timeout period expires. |
| Use a proxy | Select this option to use an HTTP or a SOCKS proxy.  * Proxy type: Select the type of proxy you want to use:   HTTP or SOCKS. The HTTP   proxy support basic authentication. * Proxy host and Proxy port:   Enter the address and port of the proxy. * Proxy login and Proxy   password: Enter the credentials needed to authenticate to the   proxy. These two fields are available when HTTP is   selected from the Proxy type drop-down list. |
| Body charset | Enter the encoding type of the requested body. This option is only available if the Insert/Update option and the Specify the request check box are selected in the basic settings. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox. |
| NB\_LINE | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an end component of a Job or subJob and it always needs an input link. |
| **Limitation** | * You cannot currently use header parameters in the tSAPOData components.   Specifically, there are no dedicated fields for specifying SAP parameters   such as sap-client (SAP Client ID) and   sap-language (SAP Language) within these   components. * Entities with multiple primary keys are not officially supported. However,   update (PATCH/REPLACE) and delete   operations can be performed using a raw request with a custom key string   format (Example:   BankCountry='AT',BankInternalID='15500'). |

**Related tasks**  

* [Inserting and updating records in an SAP OData dataset](tfixedflowinput-tmap-tsapodatainput-tlogrow-tsapodataoutput-inserting-and-updating-records-in-sapodata-dataset-standard-component)
