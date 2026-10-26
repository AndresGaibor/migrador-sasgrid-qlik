<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttpclient · versión 8.0 -->
# tHTTPClient

Last updated: 9/30/2026

Accesses a web service provided by an HTTP server. This component allows you to
interact with any web services (such as REST, SOAP, and so on) and authenticate to the web
services. With this component, you can send parameters in URLs, headers, and bodies; you
can also parse the responses to retrieve the information you need from the web
services.

## tHTTPClient Standard properties

These properties are used to configure tHTTPClient running
in the Standard Job framework.

The Standard
tHTTPClient component belongs to the Internet family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote:

* This component is available only when you have installed the 8.0.1-R2023-05 Talend Studio
  monthly update or a later one delivered by Talend.
  For more information, check with your administrator.
* As of today, it is recommended to use the tHTTPClient component over the
  tFileFetch, tHttpRequest, and tREST components.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Guess schema | Click this button to retrieve the schema according to your settings. This button works when Status, headers and body is selected from the Returned content drop-down list or Output key/value pairs is selected and key/value pairs are set in the table under the Output key/value pairs option. When retrieving data from an HTTP server, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Response body format option, the Returned content option, the Extract a sub-part of the JSON option, and the Output key/value pairs option. For more information, see [tHTTPClient: configuration and output](/talend/en-US/components/8.0/http/thttpclient-schema-and-output).  Information noteNote: An error occurs if you click this button while Body is selected from the Returned content drop-down list and JSON is selected from the Response body format drop-down list. This is because the component is designed to generate the schema according to the input configuration only and to prevent the HTTP query execution from consuming or updating data. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  * Built-in: You create and store the schema locally   for this component only. For more information about a component schema in   its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its   Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   The component generates the schema automatically according to the related settings of the component. However, you need to define the schema manually if you select Body from the Returned content drop-down list and JSON from the Response body format drop-down list. In this case, you need to add a column for each of the first-level attributes and set the column type to String for attributes with nested JSON objects.  Here is an example. With JSON selected from the Response body format drop-down list and Body selected from the Returned content drop-down list, the schema needs to have a column of the String type to hold the content of the address node of the following JSON object in the response. ``` {     "id": 1,     "name": "Talend",     "address": {        "city": "San Mateo",        "state": "California",        "zipcode": "94402"     } } ```  You need to add these columns in the schema: id (type Int), name (type String), and address (type String). The component can then extract zipcode from the address column using Data Shaping Selector Language (DSSL) (for example, input.address.zipcode).  By default, the columns in the schema depend on the settings of the Response body format and the Returned content options as follows.   * When the Status, headers, and body entry is selected   from the Returned content drop-down list, the schema   contains three columns: body (type   String), headers (type   String), and status (type   Int). * When the Body entry is selected from the   Returned content drop-down list and   TEXT is selected from the Response body   format drop-down list, the schema contains one column:   body (type String).   When retrieving data from an HTTP server, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Response body format option, the Returned content option, the Extract a sub-part of the JSON option, and the Output key/value pairs option. For more information, see [tHTTPClient: configuration and output](/talend/en-US/components/8.0/http/thttpclient-schema-and-output).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Sync columns | Click this button to retrieve the schema from the preceding component. |
| Base URL | Type in the base URL address of the HTTP server you want to access, for example, `https://www.example.com/v1.0/`. To access a Web service provided by an HTTP server, you need to provide both the base URL address and the path. You can provide the path in the Path field. You can also define a placeholder using the [Data Shaping Selector Language syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language) to have some parts dynamically filled with the value extracted from the incoming record. Example:  Base URL = `"https://{.input.job_url}"` and Path = `"{.input.job_url_path}"` |
| Authentication type | Select one of the following authentication methods depending on the server security requirements:  * No authentication: no authentication is expected to   access the server. * Basic: A username and a password are expected. For   more information, see [RFC 2617](https://www.rfc-editor.org/rfc/rfc2617). * Digest: A username and a password are expected. For   more information, see [RFC 2617](https://www.rfc-editor.org/rfc/rfc2617). * Bearer token: A raw access token is expected. It will   be carried into the HTTP Request header as Authorization: Bearer   <your token>. * NTLM: A username (that may contain a domain name) and   a password are expected. For more information, see [NT LAN Manager (NTLM) Authentication   Protocol](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-nlmp/b38c36ed-2804-4868-a9ff-8dd3182128e4). * API key uses a flexible way to pass an API key token   to the server, including the ability to select where to pass it, its name   and a prefix:   + Destination: Select where the token will be     set: either in an HTTP header with the given name, or in an HTTP query     parameter with the given name (not recommended as the token might be     visible in the logs).   + Name: Enter the name of the header or query     parameter.   + Prefix (optional): Enter the prefix to be added     in front of the token (only if the Destination     is Request header).   + Token: Enter the authentication token. * OAuth 2.0 automatically manages the retrieval and   renewal of the access token against the OAuth server then passes it to the   target endpoint as a bearer token:   + Flow: The OAuth flow you want to execute.     Currently, only the [Client Credentials](https://www.rfc-editor.org/rfc/rfc6749#page-9) flow is supported.   + Authentication mode: For all authentication     methods supported, the flow and scope parameters are set in the body     in the format application/x-www-form-urlencoded, with     keys grant\_type=xxx&scope=xxxx.   + Token endpoint: Enter the authentication token     using the format oauth2/mydomain.com/token.   + Client ID and Client     secret: Enter the client ID and client secret.   + Additional parameters: Enter the additional     attributes you want to add, like the `scope`     attribute for example.   Information noteNote: To enter a password, a token, or a client secret key, click the [...] button next to the corresponding field to bring out the Enter a new password dialog box, enter the password, the token, or the secret key in the text field, and click OK. Note that you can enter either a JSON string in the pure password mode or a Java expression in the Java mode. You can toggle between the two modes by clicking switch to Java mode or switch to pure password mode on the top of the text field. |
| HTTP method | Select one of these HTTP methods to specify the action to be performed: GET, POST, HEAD, OPTIONS, PUT, PATCH, DELETE, or TRACE. To select an HTTP method, click the [...] button next to this field and select the desired HTTP method in the dialog box that appears. |
| Path | Enter the second part of the URL in order to complete the base URL filled in the Base URL field. Base URL and Path are joined with the character / when needed. For example, to search data from the server with the URL of https://jira.talendforge.org/rest/api/2/, type in `search` in this field. Refer to the description on the Base URL field for related information.  You can also define a placeholder using the [Data Shaping Selector Language syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language) to have some parts dynamically filled with the value extracted from the incoming record. Example:  Base URL = `"https://{.input.job_url}"` and Path = `"{.input.job_url_path}"` |
| Path parameters | Select this check box to specify extra parameters needed to complete the base URL or the path in the form of name-value pairs. If the base URL or path contains placeholders, you can add parameters in this table and set the parameter name and parameter value in the following way to replace the placeholders.   * Name: Enter the name of the placeholder to be   replaced. * Value: Enter the value you want to replace the   placeholder with. It can be a static value (for example,   `contactEntity`), a value extracted from the   incoming record (for example, `{.input.entity.id}`),   or a mixture of both (for example,   `version{.input.api.version}`).   For example, with the base URL https://www.example.com and the path /{api\_version}, you can set the path by adding a parameter in this table, setting Name to `api_version` and Value to `v1.0`. |
| Query parameters | Select this option to specify the parameters that will be set in the query URL after the ? character in the form of name=value. The values are automatically encoded.  * Name: Enter the name of the parameter. * Value: Enter the value of the parameter. It can be a   static value (for example, `UUID-1234567`), a value   extracted from the incoming record (for example,   `{.input.user.id}`), or a mixture of both (for   example, `UUID-{.input.user.id}`).   Example: Query parameter name = entityId and query parameter value = UUID-1234567 |
| Request headers | Select this option to define some HTTP request headers as name-value pairs. You can define each header to be either part of the main HTTP query (Main), the authentication query (Authentication, only available with OAuth 2.0 authentication), or both queries (Both).  * Name: Enter the name of the header. * Value: Enter the value of the header. It can be a   static value (for example, `text/html;charset=utf-8`),   a value extracted from the incoming record (for example,   `{.input.meta.content}`), or a mixture of both (for   example,   `text/{.input.document.format};charset={.input.document.charset}`). Note   that headers with an `AUTHENT` value can only be   sent with OAuth 2.0 authentication queries. * Query: Select the query on which this header   configuration will be applied.   Example: Header name = Content-Type and header value = text/html;charset=utf-8 |
| Request body | Select this option if you want to include a message body in the request. |
| Body type | Set the body type by selecting the corresponding option from the drop-down list.  * Text: Enter the body of the message as plain text   in the text frame under the drop-down list. You can define a placeholder   using the [Data Shaping Selector Language   syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language) to have some parts dynamically filled with the value   extracted from the incoming record. Example: ```   id={.input.user.id}   name={.input.user.name}   ``` * JSON: Enter the body of the message in the JSON   format in the text frame under the drop-down list. You can define a   placeholder using the [Data Shaping Selector Language   syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language) to have some parts dynamically filled with the value   extracted from the incoming record. Example: ```   {    "id": "{.input.user.id}",    "name": "{.input.user.name}",    "age": "{.input.user.age}",    }   ``` * XML: Enter the body of the message in the XML   format in the text frame under the drop-down list. You can define a   placeholder using the [Data Shaping Selector Language   syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language) to have some parts dynamically filled with the value   extracted from the incoming record. Example: ```   <user>    <id>{.input.user.id}</id>    <name>{.input.user.name}</name>    <age>{.input.user.age}</age>   </user>   ``` * Form data and   x\_www\_urlencoded: Create the body using a   multipart form with attribute name-value pairs or using a URL encoded   form with attribute name-value pairs. Enter the attribute names and   values in rows of the table under the drop-down list. You can define a   placeholder using the [Data Shaping Selector Language   syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language) to have some parts dynamically filled with the value   extracted from the incoming record. * Binary: Select this option if you want to upload data   files larger than 500MB in chunks. Once selected, the File   path field is displayed to let you specify a local upload   folder.   The Body type drop-down list is available when you select the Request body option. |
| Response body format | Select the response body format from the drop-down list. The right format allows the connector to parse and apply operations to the response. Currently, text and JSON formats are supported.  * Text: Select this format to return a plain text   message. In that case the response payload is not parsed and it will not be   possible to extract a sub-part from it. * JSON: Select this format if the response received has   a JSON format. In that case the payload is translated into correctly parsed   JSON records.   When retrieving data from an HTTP server, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Response body format option, the Returned content option, the Extract a sub-part of the JSON option, and the Output key/value pairs option. For more information, see [tHTTPClient: configuration and output](/talend/en-US/components/8.0/http/thttpclient-schema-and-output). |
| Returned content | Select one of the following two options depending on the data returned by the server.  * Body: If Text is selected   from the Response body format drop-down list, a   record with one string attribute named body is generated and   all the payload is copied in it; If JSON is   selected from the Response body format drop-down   list, a record that represents the hierarchical structure of the parsed   document is generated. Limitation: If the body part in the main flow   exceeds 200MB, the record will be truncated and a warning will be thrown. * Status, headers, and body: A record is generated with   a status attribute (INT type) that contains the HTTP status code, a   headers attribute that is a record with all response headers   as nested attributes, and a body attribute that is either a   simple string containing the full payload as text (if   Text is selected from the Response body   format drop-down list) or a hierarchical object representing   the parsed document (if JSON is selected from the   Response body format drop-down list). Limitation:   If the body part in the main flow exceeds 200MB, the record will be   truncated and a warning will be thrown. * Download file only: Select this option to limit the   returned content in the main flow and only download the HTTP response body   as a file or to cache, without building a record in the main flow to save   resources. This option is intended to be used in conjunction with the   Download attachments property. If the attachment   size is greater than 2GB, use the Download file only   option; the Download attachments option is for   getting attachments smaller than 2GB. Information noteNote: The Download file   only option is available only when you have installed the   8.0.1-R2025-09 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator.   When retrieving data from an HTTP server, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Response body format option, the Returned content option, the Extract a sub-part of the JSON option, and the Output key/value pairs option. For more information, see [tHTTPClient: configuration and output](/talend/en-US/components/8.0/http/thttpclient-schema-and-output).  Information noteNote: This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after selecting an item from this drop-down list. |
| Extract a sub-part of the JSON | Enter the path of a node to select a sub-element of the response. If the element is an array, each element of the array will be looped over. For more information about the syntax for entering the node name, see [Data Shaping Selector Language syntax](/talend/r/en-US/8.0/data-shaping-language-reference-guide/using-data-shaping-selector-language). This field is optional and must remain empty to retrieve the entire JSON response.  Example for the following JSON document: ``` {    "description": "List of some famous geologists",    "content_length": 5,    "author": "A. Smith",    "content":[       {          "name":"Maurice Krafft",          "age":35,          "female":false,          "address":{             "city":"Mulhouse",             "zipcode":68100          }       },       {          "name":"Katia Krafft",          "age":49,          "female":true,          "address":{             "city":"Soultz-Haut-Rhin",             "zipcode":6860          }       },       {          "name":"Pline l'Ancien",          "age":55,          "female":false,          "address":{             "city":"CÃ´me",             "zipcode":22100          }       },       {          "name":"James Hutton",          "age":70,          "female":false,          "address":{             "city":"Ã‰dimbourg",             "zipcode":0          }       },       {          "name":"Aline Peltier",          "age":40,          "female":false,          "address":{             "city":"Saint-Pierre",             "zipcode":97410          }       }    ] } ``` To loop over all the geologists and generate a record for each of the geologists, enter `.content` in the Extract a sub-part of the JSON field. You can also add a filter to retrieve only a subset of the records. For example, you can retrieve information about the geologists that are more than 40 years old by entering `.content{.age>40}` in the Extract a sub-part of the JSON field and the following information will be returned. ``` {"name":"Katia Krafft","age":49.0,"female":true, ... {"name":"Pline l'Ancien","age":55.0,"female":false, ... {"name":"James Hutton","age":70.0,"female":false, ... ``` To retrieve the cities of the geologists that are more than 40 years old, enter `.content{.age > 40}.address.city` in the Extract a sub-part of the JSON field. The following information will be returned. ``` |=-----------------=| |field              | |=-----------------=| |Soultz-Haut-Rhin   | |CÃ´me               | |Ã‰dimbourg          | '-------------------' ``` Note that if the payload of the selector has only one value, it will be named field.  When retrieving data from an HTTP server, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Response body format option, the Returned content option, the Extract a sub-part of the JSON option, and the Output key/value pairs option. For more information, see [tHTTPClient: configuration and output](/talend/en-US/components/8.0/http/thttpclient-schema-and-output).  This field is available if you select JSON from the Response body format drop-down list.  Information noteNote: This field impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after setting this field. |
| Output key/value pairs | Select this option to return key/value pairs instead of the raw body of the HTTP response. To enter a value for a node, add a row in the table by clicking the plus button under the table, enter the name of the node in the Name field, and enter the value in the Value field. The value can be from the component input or from the HTTP response. Enter `"{.input.<dssl_path>}"` in the Value field if the value is from the component input or `"{.response.<dssl_path>}"` if the value is from the HTTP response.  In the example for the Extract a sub-part of the JSON option, you can retrieve the name and city values of the geologists by entering `.content` in the Extract a sub-part of the JSON field and adding the following two key/value pairs in the table.  * `"Name"`:`"{response.name}"` * `"City"`:   `"{response.address.city}"`  When retrieving data from an HTTP server, you can specify the format and content of the data retrieved using the schema, the Guess schema button, the Response body format option, the Returned content option, the Extract a sub-part of the JSON option, and the Output key/value pairs option. For more information, see [tHTTPClient: configuration and output](/talend/en-US/components/8.0/http/thttpclient-schema-and-output).  Information noteNote: This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after setting the key/value pairs in the table under this option. |
| Forward input values | Select this option to pass the values received from the component input to the subsequent component. This option is available when Output key/value pairs is selected. |
| Download attachments | Select this option to save the attachments of the response as a file in a specified directory. You need to type in the path to the directory in the Directory to save field. If the directory specified does not exist, the component will try to create it. Make sure you have the permission to write the directory specified. For a MIME multipart response with attachments, the first part that is not an attachment in the body will be treated as the output record body; the attachment part is marked with Content-Disposition=attachment;... header and the attachment filename is taken from its `name=...` value. If the name field is not provided in header metadata, the file will be named using the service name (that is, the Path value). If no part has the Content-Disposition=attachment header, the first part of the multipart is treated as the body for the output record and other parts are treated as the attachments.  For binary files, the tHTTPClient component will save the HTTP response body into a file as is. If there is no name specified in the Content-Disposition header, the result file will be named after the resource name with a `_0` suffix.  Information noteNote: This option is available only when you have installed the 8.0.1-R2023-05 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use custom attachment name | Select this option if you want to define a custom name for the attachment. You need to type in the file name in the Attachment name field. This option is available when Download attachments is selected.  Information noteNote: This option is available only when you have installed the 8.0.1-R2025-03 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use cache to save file | Select this check box to save the data in the cache.  This option allows you to process the file without saving it on your drive. This is faster and improves performance.  This option is available when Download attachments is selected.  Information noteNote: This option is available only when you have installed the 8.0.1-R2025-03 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |
| Use custom authorization token header | Select this check box to enter a custom authorization token header name. The default header name is `Authorization`. This option is available when OAuth 2.0 is selected in the Authentication type option in the Basic settings of the component. |
| Use custom token prefix | Select this check box to enter a custom token prefix. The default token prefix is `Bearer`. If you do not have a token prefix, leave this field empty. This option is available when OAuth 2.0 is selected in the Authentication type option in the Basic settings of the component. |
| Connection timeout (ms) | Set the timeout period (in milliseconds) for the connector to establish a connection to the server. An error occurs if an attempt to establish a connection fails. |
| Receive timeout (ms) | Set the timeout period (in milliseconds) for receiving response data. An error occurs if no data is received when the read timeout period expires. |
| Bypass server certificate validation | Select this option to prevent the client from validating the server certificate. This option is not recommended in production environments. |
| Use a proxy | Select this option to use an HTTP or a SOCKS proxy.  * Proxy type: Select the type of proxy you want to use:   HTTP or SOCKS. The HTTP   proxy support basic authentication. * Proxy host and Proxy port:   Enter the address and port of the proxy. * Proxy login and Proxy   password: Enter the credentials needed to authenticate to the   proxy. These two fields are available when HTTP is   selected from the Proxy type dropdown list. |
| Retry with exponential backoff | Select this option to automatically retry failed HTTP calls. If selected, HTTP calls are retried if there is a connection error, a timeout, or if the HTTP status code is higher or equal to 400, however no retries are done for 401/403/511 errors which are authentication errors.  * Initial backoff (ms): Enter the duration to wait, in   milliseconds, before the first retry of the HTTP call. * Backoff factor: When an attempt fails, the duration   to wait is multiplied by this factor in order to increase the delay between   each call. If the factor is `1`, all delays will be the   same. * Maximum number of retries: Enter the maximum number   of attempts for a single HTTP query. The initial call should not be included   in this number.   Example for the following configuration:  Intial backoff: `300` ms, Backoff factor: `2`, and Maximum number of retries: `4`  The HTTPClient component does a first GET operation on the server (first call). A connection timeout error is returned, the retry mechanism is activated, and the component waits for 300 milliseconds. A second attempt is then made (first retry). A 503 HTTP response is returned, the wait duration is multiplied by 2, so the component waits for 600 milliseconds. A third attempt is made (second retry). A 500 Internal server error is returned, the wait duration is multiplied by 2, so the component waits for 1200 milliseconds. A fourth attempt is made (third retry), and this time it is successful. No additional attempt is made, and the response is returned. |
| Accept redirections | Select this option to apply the [HTTP Redirection rules](https://www.rfc-editor.org/rfc/rfc7231#page-54) on your resources.  * Maximum number of redirects: Set the maximum number   of redirects that the connector should follow. If there are more   redirections than configured, the last one is returned as the result of the   query. * Redirect only on same host: Enable this option if you   want redirections to be performed only when using the same host. |
| Pagination | Select this option to enable the pagination strategy. For more information about pagination strategy, see Pagination section of [JIRA Server platform REST API reference](https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/). Note that pagination is only compliant with JSON payload and the desired elements must be in an array in the JSON payload.  You need to set the following options for pagination to work properly.   * Pagination strategy: Select the pagination strategy   to be used:   + Offset/limit: This strategy retrieves the     elements starting at a specific position in pages of a specific size.     The offset parameter specifies the beginning     element in terms of the offset from the first element; the     limit parameter specifies the maximum size of     a page in terms of the number of the elements. With this strategy     applied, the pagination stops when the last call returns 0     elements.   + Marker: This strategy uses a "marker" (often     the ID of the last item retrieved) to fetch the next set of results.     The marker acts as a pointer to indicate where the next page of data     starts, allowing the API to return results that come after the marker.     With this strategy applied, the pagination stops when the response     contains the marker element.   + Next link: This strategy provides a "next     link" (or URL) in the response, which the client can use to retrieve     the next set of results. The "next link" includes an offset or a page     number that the client can use to fetch the next page. With this     strategy applied, the pagination stops when the response contains the     next link element. * Location: Specify the way to set the offset and the   limit parameters, which can be Query parameters or   In headers. * Name of the offset: Set the name of the parameter   that will be used as the offset. * Value of the offset: Set the offset. To start from   the first element, set it to 0. You can obtain the offset   of a query from the incoming records using the DSSL expression   '{.input.last\_page\_info.offset}'. * Name of the limit: Set the name of the parameter that   defines the maximum number of elements allowed in a page. * Value of the limit: Set the limit, the maximum number   of elements that can be returned in a page. The pagination will stop when a   page is returned with 0 elements. * Path to elements: Set the path to the JSON array that   contains the desired elements. It must be a JSON array. With   offset/limit strategy applied, the element specified by   this parameter becomes the root regardless of the setting in   Extract a sub-part of the response option. For   instance, with JIRA in the   Preset field, setting Path to   elements to `.issue` retrieves the   issues even if Extract a sub-part of the response is   set to `.key` (assuming that key is an   attribute of the elements present in the issues). * Preset: Select preset configuration for specific   service that supports pagination strategy by selecting the corresponding   service. To select a service, click the [...] button   next to this field and select the service. You can select one of the   following services.   + BOX: see [Offset-based Pagination](https://developer.box.com/guides/api-calls/pagination/offset-based/) for     more information.   + JIRA: see [JIRA Server platform REST API     reference](https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/) for more information.   + OData: see [OData Version 4.01. Part 1:     Protocol](https://docs.oasis-open.org/odata/odata/v4.01/os/part1-protocol/odata-v4.01-os-part1-protocol.html) for more information. * Load selected preset: Click this button to load the   preset configuration selected in the Preset   field.   Information noteNote: The Pagination option is available only when you have installed the 8.0.1-R2023-05 Talend Studio monthly update or a later one delivered by Talend. The Marker and Next link strategies are available from the 8.0.1-R2025-12 Talend Studio monthly update onwards. For more information, check with your administrator. |
| Use cookies | Select this checkbox for the component to load web authentication cookies from a specific directory while requesting the HTTP server. |
| Disable chunked encoding | Select this checkbox to disable Transfer-Encoding: chunked for outgoing HTTP requests with a body. By default (when this option is not selected), the component sends requests with Transfer-Encoding: chunked if the body size is greater than 4096 bytes, and uses Content-Length when the body size is less than 4096 bytes.  When you enable this option, the component ensures that the Transfer-Encoding: chunked header is never sent to the server. Instead, it will consistently use the Content-Length header for all request bodies, regardless of their size.  Information noteNote: The default is disabled (unchecked). Enable this option only if your server does not support chunked encoding in POST/PUT/PATCH requests. |
| HTTP version | Select the HTTP protocol version to be used by the component when sending requests to the server:   * HTTP/1.1 (deprecated): Uses the HTTP/1.1 protocol.   This option is maintained for backward compatibility but is considered   deprecated and may be removed in future releases. * HTTP/2: Uses the HTTP/2 protocol, while maintaining   compatibility with HTTP/1.1 endpoints.   When using multiple tHTTPClient components in the same Job, it is not expected that HTTP/2 and HTTP/1.1 modes can be mixed reliably within a parallel execution. If parallel Job execution with more than one tHTTPClient component is required, ensure that all components are set to use the same HTTP version. Information noteNote: The HTTP/2 option is available only when you have installed the 8.0.1-R2025-11 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Save cookies | Select this checkbox to save web page authentication cookies in a specific directory. This means you will not have to log on to the same website in the future. |
| Cookies directory | Type in the full path to the directory in which you want to either use existing cookies or save cookies, or click [...] and browse to the desired directory. This directory contains a cookies.json file that stores cookie metadata such as name, domain, or expiry information. |
| Normalize the JSON HTTP response | Select this option to normalize inconsistencies in the JSON payload in order for the component to correctly parse these documents:  * Normalize attributes: allows you to convert a value   to the expected data type. * Normalize arrays: allows you to filter on some   elements of a JSON array. Example:  If you configure the component   to retrieve [this JSON document](/talend/en-US/components/8.0/Content/Resources/attachments/thttpclient_company_data.json), these JSON   inconsistencies will be returned in the Job execution console: ```   Some JSON inconsistencies has been identified:   .users.*.addresses is not consistently present in all objects.   .users.*.active is not consistently present in all objects.   .users.*.email is not consistently present in all objects.   .users.*.addresses is an array that contains items of several types: STRING, OBJECT.   .users.*.addresses.*.country is not consistently present in all objects.   .users.*.addresses.*.street is not consistently present in all objects.   .users.*.addresses.*.zipcode is found with varying types: STRING, INT.   Please, have a look to advanced settings JSON normalization to fix it.   ```  To   prevent this, you could for example use the Normalize   attributes option to cast the attribute with the path   .users.\*.addresses as an   ARRAY type, and the attribute with the path   users.\*.addresses.\*.zipcode as an   INT type even though some returned values have   a String type. You could also add a missing attribute, such as   .users.\*.active (here you can cast it as a   BOOLEAN since it returns either   'true' or   'false').  You could also use the   Normalize arrays option to only keep the   OBJECT elements in   .users.\*.addresses even though addresses also   contain some String types.   This option is available when JSON is selected in the Response body format option in the Basic settings of the component. |
| Add attachments | Select this option to add files as attachments to a multipart request. The Files to upload table appears when you select this option, allowing you to set the following parameters:  * Content type: Set the content type of the file   defined by HTTP. See <https://www.w3.org/Protocols/rfc1341/4_Content-Type.html> for   related information. * Encoding: Set the file encoding. * Path to file: Enter the full path to the file to be   uploaded, including the file name. * Attachment name: Set the HTTP-formed ID of the   attachment.   The Add attachments option is available when you select the Request body option and select Form data from the Body type dropdown list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2023-05 Talend Studio monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Force JSON numbers to "Double" type in response body | Select this option if you want to force all JSON numbers to be converted to Double type. Differentiating between Integer and Double numbers is not always possible in JSON. For instance, a geographic location matrix, that should contain only Double, may have one of its item inferred as Integer "[47, -1.567075]". It is error prone, since the connector will try to generate an Integer array, and then will try to add a Double inside. Forcing all numbers to Double will prevent these errors.  This option is available when JSON is selected from the Response body format dropdown list in the Basic settings view. |
| Die on error | Select this option to stop the execution of the Job if the status code of the response is different from 2xx. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox. |
| NB\_LINE | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as intermediate step in a data flow or as an end object in the Job flowchart. |
| **Limitations** | This component cannot be placed immediately after the tRESTRequest component. As a workaround, place a tMap component between the two components to copy the input data to the output. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttpclient-schema-and-output -->
# tHTTPClient: configuration and output

Last updated: 9/30/2026

The output of the tHTTPClient component varies with the settings of the
Response body format option, the Extract a sub-part of
the response option, the Returned content option, and
the Output key/value pairs option. This article lists the output
cases of the tHTTPClient component under different configuration combinations by retrieving
the same content using the following Job.

Information noteNote: Behavior change: From Talend Studio
v8.0.1-R2024-12 onwards, JSON arrays are parsed as arrays. In earlier versions, JSON
arrays were returned as a single string with elements separated by line breaks (\n). If you
have existing Jobs that rely on the previous behavior for single-element JSON arrays, you
can restore the legacy output by setting the following system property to
true:

```
org.talend.components.common.dssldictionary.DSSLDictionary.SINGLE_ELEMENT_NOT_ARRAY
```

This
property is intended for backward compatibility; prefer updating Jobs to handle arrays
where possible.

The following figure shows the base configuration of the tHTTPClient component.

The query response payload is given below.

```
[
  {
    "name": "Peter",
    "age": 40,
    "male": true,
    "addresses": {
       "city": "Nantes",
       "zip": "44000",
       "street": "bd prairie au duc"
    },
    "cars": [
       {"brand": "Ford", "model": "Transit", "km": 123456},
       {"brand": "Renault", "model": "Clio", "km": 87234}
    ]
  }
]
```

* Treating the response as a text string
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - body, type String. Information noteNote: The   Guess schema button works. That is,   you can have the schema generated automatically by clicking   the Guess schema button. |
    | Response Body format | `TEXT` |
    | Returned content | `Body` |
    | Output key/value pairs | Disabled |
  + Output
* Treating the response as a text string and returning status, headers, and body of the response
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - body, type String. - headers, type String. - status, type Int. Information noteNote: The Guess schema button works. That is, you can have the schema generated automatically by clicking the Guess schema button. |
    | Response Body format | `TEXT` |
    | Returned content | `Status, headers, body` |
    | Output key/value pairs | Disabled |
  + Output
* Treating the response as a JSON string and returning the entire response
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - name, type String. - age, type Int. - male, type Boolean. - address, type String (will be a string   representation of a JSON object). - cars, type String (will be a string   representation of a JSON object). Information noteWarning: The Guess schema does not work in this case. You need to create the schema manually. |
    | Response Body format | `JSON` |
    | Extract a sub-part of the response | Empty, `.` (a dot), or `.root` |
    | Returned content | `Body` |
    | Output key/value pairs | Disabled |
  + Output
* Treating the response as a JSON string and returning status, headers, and body of the entire response
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - body, type String (will be a string   representation of a JSON object). - headers, type String (will be a string   representation of a JSON object). - status, type Int. Information noteNote: The Guess schema button works. That is, you can have the schema generated automatically by clicking the Guess schema button. |
    | Response Body format | `JSON` |
    | Extract a sub-part of the response | Empty, `.` (a dot), or `.root` |
    | Returned content | `Status, headers, body` |
    | Output key/value pairs | Disabled |
  + Output
* Treating the response as a JSON string and returning the address information about the first
  sub-element under the root element
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - city, type String. - zip, type String. - street, type String. Information noteWarning: The Guess schema does not work in this case. You need to create the schema manually. |
    | Response Body format | `JSON` |
    | Extract a sub-part of the response | `.root[0].addresses` |
    | Returned content | `Body` |
    | Output key/value pairs | Disabled |
  + Output
* Treating the response as a JSON string and returning the information about the cars of the
  first sub-element under the root element
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - brand, type String. - model, type String. - km, type Int. Information noteWarning: The Guess schema does not work in this case. You need to create the schema manually. |
    | Response Body format | `JSON` |
    | Extract a sub-part of the response | `.root[0].cars` |
    | Returned content | `Body` |
    | Output key/value pairs | Disabled |
  + Output
* Treating the response as a JSON string and returning the information about the sub-elements
  under the root element using key/value pairs
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - name, type String. - full\_address, type String. - first\_car\_brand, type String. Information noteNote: The Guess schema button works. That is, you can have the schema generated automatically by clicking the Guess schema button. |
    | Response Body format | `JSON` |
    | Extract a sub-part of the response | empty, `.` (a dot), or `.root` |
    | Returned content | `Body` |
    | Output key/value pairs | Enabled. |
    | Forward input values | Disabled |
    | Key/value pairs | - `"name"`:   `"{.response.name}"` - `"full_address"`:   `"{.response.addresses.street},   {.response.addresses.zip},   {.response.addresses.city}"` - `"first_car_brand"`:   `"{.response.cars[0].brand}"` |
  + Output
* Treating the response as a JSON string and returning a value of the first sub-element under
  the root element
  + tHTTPClient configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - field, type String. Information noteWarning: The Guess schema does not work in this case. You need to create the schema manually. |
    | Response Body format | `JSON` |
    | Extract a sub-part of the response | `.root[0].name` |
    | Returned content | `Body` |
    | Output key/value pairs | Disabled. |
  + Output


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttpclient-handling-json-array -->
# tHTTPClient: configuration for retrieving specific data from a JSON array

Last updated: 9/30/2026

This article lists configuration combinations for retrieving specific data from a
JSON array using the Extract a sub-part of the response field and
the Output key/value pairs option and the corresponding output. This
article uses the following Job to retrieve and display data. The sub-elements of the
element specified in the Extract a sub-part of the response field
will be retrieved. If the sub-elements form an array, the component will generate one
output record for each of the array elements.

Information noteNote: Behavior change: From Talend Studio
v8.0.1-R2024-12 onwards, JSON arrays are parsed as arrays. In earlier versions, JSON
arrays were returned as a single string with elements separated by line breaks (\n). If you
have existing Jobs that rely on the previous behavior for single-element JSON arrays, you
can restore the legacy output by setting the following system property to
true:

```
org.talend.components.common.dssldictionary.DSSLDictionary.SINGLE_ELEMENT_NOT_ARRAY
```

This
property is intended for backward compatibility; prefer updating Jobs to handle arrays
where possible.

The JSON array in the query response payload is given below.

```
[
  {
    "name": "Peter",
    "age": 40,
    "male": true,
    "addresses": {
       "city": "Nantes",
       "zip": "44000",
       "street": "bd prairie au duc"
    },
    "cars": [
       {"brand": "Ford", "model": "Transit", "km": 123456},
       {"brand": "Renault", "model": "Clio", "km": 87234}
    ]
  },
   {
    "name": "Emma",
    "age": 34,
    "male": true,
    "addresses": {
       "city": "Paris",
       "zip": "75000",
       "street": "bd Saint-Germain"
    },
    "cars": [
       {"brand": "Tesla", "model": "Model 3", "km": 63456},
       {"brand": "Ford", "model": "Mustang Mach-E", "km": 32543},
       {"brand": "Volkswagen", "model": "Golf 8", "km": 43876},
    ]
  }
]
```

The following figure shows the base configuration of the tHTTPClient component.

* Retrieving all the elements under the root element.
  + Configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - name, type String - age, type Int - address, type String |
    | Response body format | `JSON` |
    | Extract a sub-part of the response field | Empty, `.` (a dot), or `.root`  This configuration points to the root element of the JSON array. |
  + Output
* Retrieving a sub-element under the root element.
  + Configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - name, type String - age, type Int - address, type String |
    | Response body format | `JSON` |
    | Extract a sub-part of the response field | `.root[1]`  This configuration points to the second element under the root element of the JSON array. Note that array element index begins from 0. |
  + Output
* Retrieving the information about Emma's cars.
  + Configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - brand, type String - model, type String - km, type Int |
    | Response body format | `JSON` |
    | Extract a sub-part of the response field | `.root[1].cars`  This configuration points to the cars element of Emma, the second element under the root element. |
  + Output
* Retrieving the information about Emma's cars with the values of the km
  elements larger than 40000.
  + Configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - brand, type String - model, type String - km, type Int |
    | Response body format | `JSON` |
    | Extract a sub-part of the response field | `.root[1].cars{.km>40000}`  This configuration points to the cars element of Emma with the values of the km elements larger than 40000. |
  + Output
* Retrieving data using key/value pairs.

  Once the main data is extracted using
  Extract a sub-part of the response field, you can also
  extract values of specific elements to create flat records. To do so, select the
  Output key/value pairs option and add some name/value pairs
  in the table. For a name/value pair, name is the name of a schema column
  and value is an expression pointing to an element of the response. The
  expression can contain some DSSL selectors to retrieve values from the response of
  the HTTP query configured in the connector. In the following example,
  Extract a sub-part of the reponse holds a value of
  `.` (a dot) and the two records, Peter and
  Emma, will be looped.

  + Configuration

    | Configuration item | Setting |
    | --- | --- |
    | Schema columns | - name, type String - age, type Int - address1, type String - address2, type String - first\_car\_brand, type String |
    | Response body format | `JSON` |
    | Extract a sub-part of the response field | `.` (a dot)  This configuration points to the cars element of Emma with the values of the km elements larger than 40000. |
    | Output key/value pairs | Selected, with the name/values pairs shown in the following figure. |
  + Output
