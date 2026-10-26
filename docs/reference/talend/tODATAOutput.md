<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/todataoutput · versión 8.0 -->
# tODataOutput

Last updated: 9/30/2026

Inserts, updates, or deletes data from an OData web service.

For a quick introduction on using this component in your Job, see the
following video:

## tODataOutput Standard properties

These properties are used to configure tODataOutput running in
the Standard Job framework.

The Standard
tODataOutput component belongs to the Internet family.

The component in this framework is available in all
subscription-based Talend
products.

* This component is available only when you have installed the 8.0.1-R2024-01 Talend Studio
  monthly update or a later one delivered by Talend. For
  more information, check with your administrator.
* This component only supports OData version 4.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.   * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its   Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess schema | Click this button to retrieve the schema according to your settings. This button works when Status, headers and body is selected from the Returned content drop-down list or Output key/value pairs is selected and key/value pairs are set in the table under the Output key/value pairs option.  When retrieving data from OData, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Entity set option, the, Specify entity key option, the $filter/search/select/expand option, and the Return type option. |
| Root URL | Type in the URL address identifying the root of the OData service you want to access, for example, `https://services.odata.org/V4/xxx`. For more information, see [Service Root URL](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752336). |
| Authentication type | Select one of the following authentication methods depending on the server security requirements:   * No authentication: no authentication is expected to   access the server. * Basic: A username and a password are expected. For   more information, see [RFC 2617](https://www.rfc-editor.org/rfc/rfc2617). * Digest: A username and a password are expected. For   more information, see [RFC 2617](https://www.rfc-editor.org/rfc/rfc2617). * Bearer token: A raw access token is expected. It   will be carried into the request header as Authorization: Bearer   <your token>. * NTLM: A username (that may contain a domain name)   and a password are expected. For more information, see [NT LAN Manager (NTLM) Authentication   Protocol](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-nlmp/b38c36ed-2804-4868-a9ff-8dd3182128e4). * API key uses a flexible way to pass an API key token   to the server, including the ability to select where to pass it, its name   and a prefix:   + Destination: Select where the token will be     set: either in a header with the given name, or in a query parameter     with the given name (not recommended as the token might be visible in     the logs).   + Name: Enter the name of the header or query     parameter.   + Prefix (optional): Enter the prefix to be     added in front of the token (only if the     Destination is Request     header).   + Token: Enter the authentication token. * OAuth 2.0 automatically manages the retrieval and   renewal of the access token against the OAuth server then passes it to the   target endpoint as a bearer token:   + Flow: The OAuth flow you want to execute.     Currently, only the [Client Credentials](https://www.rfc-editor.org/rfc/rfc6749#page-9) flow is supported.   + Authentication mode: For all authentication     methods supported, the flow and scope parameters are set in the body     in the format application/x-www-form-urlencoded, with     keys grant\_type=xxx&scope=xxxx.   + Token endpoint: Enter the authentication token     using the format oauth2/mydomain.com/token.   + Client ID and Client     secret: Enter the client ID and client secret.   + Scopes: Enter the scope. If not set, the scope     key is not added in the body form.   Information noteTip: To enter a password, a token, or a client secret key, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the password, the token, or the secret key in the text field, and click OK. Note that you can enter either a JSON string in the pure password mode or a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. |
| Entity set | Enter or select the specific entity set you would like to retrieve from the service. For more information, see [Addressing Entities](https://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752340).  Information noteTip: To visualize all available entity sets, click the [...] button next to the corresponding field to bring out the Retrieve values dialog box, and click Run in background. A new dialog box opens with all the retrieved entity sets you can select. Note that you can also provide a Custom value by selecting the Use custom value check box.  This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after setting the key/value pairs in the table under this option. |
| Output action | Select an operation to be performed from the drop-down list.   * Insert: Inserts new records in the previously   defined entity set. * Update: Modifies existing records in the   previously defined entity set. The available update types are   Patch (updates existing records with modified   properties), or Replace (overwrites existing   records with new ones). * Delete: Deletes existing records in the previously   defined entity set. |
| Specify the request configuration | Select this option to configure your request.  * Key value: Enter the existing value you want to   update or delete. This option is only available if you select either   Update or Delete from   the Output action list. * Request body: Enter the body of the message you   want to include in the request. The format needs to match the format   selected in the Request body format field. JSON   example: ```   {    "id": "184",    "lastname": "Truce",    "age": "37",    }   ```  This option is only available if you select   either Insert or Update   from the Output action list.  XML example: ```   <user>    <id>184</id>    <name>Truce</name>    <age>37</age>   </user>   ``` * Request body format: Set the body format by   selecting the corresponding option. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |
| Use custom authorization token header | Select this check box to enter a custom authorization token header name. The default header name is `Authorization`. This option is available when OAuth 2.0 is selected in the Authentication type option in the Basic settings of the component. |
| Use custom token prefix | Select this check box to enter a custom token prefix. The default token prefix is `Bearer`. If you do not have a token prefix, leave this field empty. This option is available when OAuth 2.0 is selected in the Authentication type option in the Basic settings of the component. |
| Connection timeout (ms) | Set the timeout period (in milliseconds) for the connector to establish a connection to the server. An error occurs if an attempt to establish a connection fails. |
| Receive timeout (ms) | Set the timeout period (in milliseconds) for receiving response data. An error occurs if no data is received when the read timeout period expires. |
| Use a proxy | Select this option to use an HTTP or a SOCKS proxy.   * Proxy type: Select the type of proxy you want to   use: HTTP or SOCKS. The HTTP   proxy support basic authentication. * Proxy host and Proxy port:   Enter the address and port of the proxy. * Proxy login and Proxy   password: Enter the credentials needed to authenticate to the   proxy. These two fields are available when HTTP is   selected from the Proxy type drop-down list. |
| Accept header and Headers | Use these options to define some request headers as name-value pairs.  Talend supports If-Match headers. For more information see [If-Match](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-odata/c3569037-0557-4769-8f75-a91ffcd7b05b). |
| Use custom URL parameters | Select this check box to specify the parameters that will be set in the query URL after the ? character in the form of name-value pairs. |
| Body charset | Enter the encoding type of the requested body.  This option is only available if the Insert/Update option and the Specify the request check box are selected in the basic settings. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox. |
| NB\_LINE | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as intermediate step in a data flow or as an end object in the Job flowchart. |

**Related tasks**  

* [Inserting and updating data using OData web services](tfixedflowinput-todatainput-todataoutput-tlogrow-retrieving-and-updating-data-standard-component "The following Job demonstrates how to insert data into an OData service using fixed data, then update inserted records using tODataInput and tODataOutput components.")
