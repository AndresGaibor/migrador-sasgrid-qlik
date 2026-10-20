<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient · versión 8.0 -->
# tRESTClient

Last updated: 9/30/2026

Interacts with RESTful Web service providers by sending HTTP and HTTPS requests
using CXF (JAX-RS) getting the corresponding responses.

This component integrates well with *Talend Runtime* to get HTTPS support, with more QoS features to be supported in time.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tRESTClient Standard properties

These properties are used to configure tRESTClient running in the Standard Job framework.

The Standard
tRESTClient component belongs to the ESB family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| URL | Type in the URL address of the REST server to be invoked. When the Use Service Locator  check box is selected, this field will not show and the URL of the REST server will be obtained from the Service Locatorserver automatically. |
| Relative Path | Enter the relative path of the REST server to be invoked.  For example, if you want to access http://localhost:8888/services/Customers/list:  If Use Service Locator  is disabled: You can enter any of the first part of the address in the URL field, and the second part in the Relative Path field. For example, you can enter http://localhost:8888 in URL and /services/Customers/list in Relative Path. You can also enter the full path of the REST server in URL and leave Relative Path blank.  If Use Service Locator  is enabled: The URL part will be given by the Service Locator. In this case, you need to know the URL part, and specify the rest part in Relative Path. This depends on the service you request. For example, on tRESTRequest, you specify REST Endpoint as http://localhost:8888/services and enable Use Service Locator. Then, if you want to use this service, on tRESTClient side, you should specify /customers/list in Relative Path. Information noteWarning: When using relative path, you should specify at least one sub-directory in the URL field instead of only host:port to avoid compiling issues. For example, use http://localhost:8888/services instead of http://localhost:8888. |
| HTTP Method | From this list, select an HTTP method that describes the desired action. The specific meanings of the HTTP methods are subject to definitions of your Web service provider. Listed below are the generally accepted HTTP method definitions:  - GET: retrieves data from the server end based on the given parameters.  - POST: uploads data to the server end based on the given parameters.  - PUT: updates data based on the given parameters, or if the data does not exist, creates it.  - PATCH: modifies data partially based on the given parameters.  - DELETE: removes data based on the given parameters. |
| Content Type | Select XML, JSON, or FORM according to the media type of the content to be uploaded to the server end.  This list appears only when you select the POST, PUT, or PATCH HTTP method. |
| Accept Type | Select the media type the client end is prepared to accept for the response from the server end.  Available options are XML, JSON, and ANY. When ANY is selected, the response message can be of any type and will be transformed into a string. |
| Query parameters | Specify the URI query parameters in the form of name-value pairs.  This option is mostly used with the GET method. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields that will be processed and passed on to the next component.  This component uses three built-in, read-only schemas.  Click Edit Schema to view the schema structure.  Information noteWarning: *Changing the schema type may result in loss of the schema structure and therefore failure of the component.* |
| Input Schema | Schema for the input data. This schema contains two columns:  - body: stores the content of structured input data  - string: stores the input content when it is, or is handled as, a string. |
| Response Schema | Schema for server response. This schema is passed onto the next component via a Row > Response link, and it contains three columns:  - statusCode: stores the HTTP status code from the server end.  - body: stores the content of a structured response from the server end.  - string: stores the response content from the server end when it is, or is handled as, a string. |
| Error Schema | Schema for error information. This schema is passed onto the next component via a Row > Error link, and it contains two columns:  - errorCode: stores the HTTP status code from the server end when an error occurs during the invocation process. The specific meanings of the errors codes are subject to definitions of your Web service provider. For reference information, visit [en.wikipedia.org/wiki/List\_of\_HTTP\_status\_codes](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes).  - errorMessage: stores the error message corresponding the error code. |
| Use Service Locator | Select this check box to enable the Service Locator. It maintains the availability of the service to help meet demands and service level agreements (SLAs). Specify the Service namespace and the Service name in the corresponding fields. |
| Use Service Activity Monitor | Select this check box to enable the Service Activity Monitor. It captures events and stores this information to facilitate in-depth analysis of service activity and track-and-trace of messages throughout a business transaction. This can be used to analyze service response times, identify traffic patterns, perform root cause analysis and more. |
| Use Authentication | Select this check box if authentication is required on the REST server end. Select the authentication type from:   * Basic HTTP: Fill the   Username and   Password fields with your   credentials. * HTTP Digest: Fill the   Username and   Password fields with your   credentials. * SAML Token (ESB runtime only): Fill the   Username and   Password fields with your   credentials. * OAuth2 Bearer: Fill the Bearer   Token field with a base64-encoded credential   string. * Open ID Connect: Fill the   Username and Password   fields with your credentials. For more information, see [Talend Identity and Access Management](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/talend-identity-and-access-management) and [Managing ESB Resources and authorizations](/talend/r/en-US/8.0/administration-center-user-guide/managing-esb-resources-and-authorizations).   To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use Authorization | Select this check box to enable authorized call. Specify the client's role in the Role field. This option appears when SAML Token (ESB runtime only) is selected in the Use Authentication list.  For more information about the management of user roles and rights, see [Managing ESB Resources and authorizations](/talend/r/en-US/8.0/administration-center-user-guide/managing-esb-resources-and-authorizations) and [Talend Identity and Access Management](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/talend-identity-and-access-management). |
| Use Business Correlation | Select this check box to create a correlation ID in this component.  You can specify a correlation ID in the Correlation Value field. In this case the correlation ID will be passed on to the service it calls so that chained service calls will be grouped under this correlation ID. If you leave this field empty, this value will be generated automatically at runtime.  When this option is enabled, tRESTClient will also extract the correlation ID from the response header and store it in the component variable for further use in the flow. |
| Check Server Identity | Select this check box to verify the match between the hostname of the URL and the Common Name (CN) on the server certificate. If they mismatch, an error java.io.IOException: HTTPS hostname wrong will be returned. |
| Re-use SSL connection | This option is disabled by default. When enabled, if the same server is called multiple times in a Job, SSL configuration will be created once and reused for every other calls.  Note that this option does not support having query parameters set in the URL or Relative Path fields. To have this option working correctly, all query parameters must be added to the Query parameters table. |
| Die on error | This check box is selected to kill the Job when an error occurs. Clear the check box to skip the row on error and complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Log messages | Select this check box to log the message exchange between the service provider and the consumer. |
| Follow redirects | Select this check box to follow auto-redirects. |
| Allow non-same host redirects | This option appears when Follow redirects is enabled. Select this check box to allow redirects on different host. |
| Maintain session | This option appears when Follow redirects is enabled. Select this check box to enable sharing session cookies in case of multiple redirects. Session cookies will be collected and available for further processing in the same way as other cookies after message exchange is finished. Information noteNote: This option is available only if you have installed the R2022-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Enable WebClient Operation Reporting | If this check box is selected, a CXF endpoint property will be set on the client side which may be used by some outgoing CXF metrics interceptors, to track requests to services using their URL's.  The property set is org.apache.cxf.resource.operation.name and it contains service URL together with the HTTP method name, for example GET:http: //example.com:8080/service/.  If this check box is not selected, the property will not be set and some metrics will not be counted, which may increase the performance. |
| Convert Response To DOM Document | Select this check box to convert the response from the server to document type.  Clear this check box if you want the response to be handled as a string. |
| Convert Types To Strings | This option appears when Content Type is JSON, or Accept Type is JSON or any. Select this check box to convert all values in JSON to string between quotation marks. For example, with this option enabled, the JSON data:  ```  "root": {       "test": 111     } ```  will be changed to:  ``` "root": {       "test": "111"     } ``` |
| Drop JSON Request Root | This option appears when HTTP Method is POST, PUT or PATCH and Content Type is JSON. Select this check box to drop root JSON elements. |
| Wrap JSON Response | This option appears and is enabled by default when JSON is selected from the Accept Type list in the Basic settings view.  With this check box selected, the response is wrapped with a *root* element. Clear this check box to remove the *root* element from the response. |
| Force HTTP version to 1.1 | tRESTClient uses HTTP version 1.2 by default. Select this check box to enable version 1.1 if the target HTTP server only supports HTTP 1.1.  Information noteNote: This option is available only if you have installed the R2025-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| HTTP Headers | Type in the name-value pair(s) for HTTP headers to define the parameters of the requested HTTP operation.  For the specific definitions of HTTP headers, consult your REST Web service provider. For reference information, visit [en.wikipedia.org/wiki/List\_of\_HTTP\_headers](http://en.wikipedia.org/wiki/List_of_HTTP_headers). |
| Disable chunked encoding | This option appears when HTTP Method is POST, PUT or PATCH. Select this check box to disable encoding the payload as chunks. |
| Service Locator Customer Properties | This option appears when Use Service Locator  is enabled in the Basic settings tab. Click [+] to add as many properties as needed to the table. Enter the name and the value of each property in the Property Name field and the Property Value field respectively to identify the service. |
| Service Activity Customer Properties | This option appears when Use Service Activity Monitor is enabled in the Basic settings tab. Click [+] to add as many properties as needed to the table. Enter the name and the value of each property in the Property Name field and the Property Value field respectively to identify the service. |
| Connection timeout | Set the amount of time, in seconds, that the client will attempt to establish a connection before it times out. If set to *0*, the client will continue to attempt to open a connection indefinitely. (default: 30)  This option does not work in Talend Runtime. For ESB Deployments to Talend Runtime, this parameter will have no effect. In the configuration file <TalendRuntimePath>/container/etc/org.apache.cxf.http.conduits-common.cfg, you need a URL which covers you service, for example, url = http://.\* to handle both HTTP and HTTPS requests, and specify the client.ConnectionTimeout parameter in milliseconds in this HTTP Conduit file. If you need to use the Receive timeout option, specify the client.ReceiveTimeout in milliseconds too. |
| Receive timeout | Set the amount of time, in seconds, that the client will wait for a response before it times out. If set to *0*, the client will wait indefinitely. (default: 60)  This option works similarly to the Connection timeout option. For how to use it after the component is deployed in Talend Runtime, see the Connection timeout option. |
| Use HTTP proxy | Select this check box if you are using a proxy server. Once selected, you need to provide the connection details: host, port, username and password. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  HEADERS: the HTTP response headers. This is a Flow variable and it returns a list of HTTP response header values.  CORRELATION\_ID: the correlation ID by which chained service calls will be grouped. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a RESTful Web service client to communicate with a RESTful service provider, with the ability to input a request to a service into a Job and return the Job result as a service response. Depending on the actions to perform, it usually works as a start or middle component in a Job or subJob. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to turn on or off the Log messages, Use Authentication or Use HTTP proxy option dynamically at runtime. You can add three rows in the table to set all options.  Once a dynamic parameter is defined, the corresponding option becomes highlighted and unusable in the Basic settings view or Advanced settings view.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Connections | Outgoing links:  Row: Response; Error.  Trigger: On Subjob Ok; On Subjob Error; Run if; On Component Ok; On Component Error.    Incoming links:  Row: Main; Reject.  Trigger: Run if; On Subjob Ok; On Subjob Error; On component Ok; On Component Error.  For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Limitation | Using context variables for dynamic endpoint or Service Locator namespace works in Talend Studio only. It is not supported in Talend Runtime. |

**Related concepts**  

* [Building a JSON document with tXMLMap to call a REST service](trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-building-json-document-with-txmlmap-to-call-rest-service-standard-component "This scenario describes how to build a JSON document with the tXMLMap component as input request for a REST call.")
* [Getting user information by interacting with a RESTful service](trestclient-txmlmap-tlogrow-tlogrow-getting-user-information-by-interacting-with-restful-service-standard-component-this)
* [Using a REST service to accept HTTP POST requests and send responses](trestrequest-trestclient-tlogrow-using-rest-service-to-accept-http-post-requests-and-send-responses-standard-component-esb-this)
* [Updating user information by interacting with a RESTful service](trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-updating-user-information-by-interacting-with-restful-service-standard-component-this)
* [Using context variables in REST endpoint URLs in Data Services](trestclient-using-context-variables-in-rest-endpoint-urls-in-data-services-context)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-building-json-document-with-txmlmap-to-call-rest-service-standard-component -->
# Building a JSON document with tXMLMap to call a REST service

Last updated: 9/30/2026

This scenario describes how to build a JSON document with the tXMLMap component as
input request for a REST call.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-setting-up-job-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-components-standard-component)
* [Running the Job and checking the result](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-running-job-and-checking-result-standard-component-press)

**Related reference**  

* [tRESTClient](trestclient "Interacts with RESTful Web service providers by sending HTTP and HTTPS requests using CXF (JAX-RS) getting the corresponding responses.")

**Related information**  

* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-updating-user-information-by-interacting-with-restful-service-standard-component-this -->
# Updating user information by interacting with a RESTful service

Last updated: 9/30/2026

This scenario describes a three-component Job that updates the information of a list
of users to a remote database through a REST service using the HTTP POST method. When
executed, the Job displays the client-server message exchange information on the
Run console.

The user information to be updated to the server is stored in a CSV file, which looks
like the following:

```
id;first_name;last_name
1;John;Smith
2;Martin;Reagan
3;James;White
4;Jenny;Jackson
5;Robert;Thomson
```

Prerequisites:

You need to get the service-related information from your REST service
provider including the URL, the resource path, and the data structure, and make necessary
modifications in the scenario configurations accordingly.

### In this section

* [Creating the Job and adding components](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-creating-job-and-adding-components-standard-component-create)
* [Setting up the components](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-setting-up-components-standard-component)
* [Running the Job to check the information](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-running-job-to-check-information-standard-component-press)

**Related reference**  

* [tRESTClient](trestclient "Interacts with RESTful Web service providers by sending HTTP and HTTPS requests using CXF (JAX-RS) getting the corresponding responses.")

**Related information**  

* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-getting-user-information-by-interacting-with-restful-service-standard-component-this -->
# Getting user information by interacting with a RESTful service

Last updated: 9/30/2026

This scenario describes a three-component Job that retrieves user information
based on the user ID from a REST service via HTTP GET and displays the retrieved user
information, as well as the message exchange between the client and the server, on the
Run console.

Prerequisites:

You need to get from your REST service provider the URL, the data structure,
and the required parameters of the REST service you are going to call and make necessary
modifications in the scenario configurations accordingly.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-setting-up-job-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tRESTClient](trestclient "Interacts with RESTful Web service providers by sending HTTP and HTTPS requests using CXF (JAX-RS) getting the corresponding responses.")

**Related information**  

* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-using-context-variables-in-rest-endpoint-urls-in-data-services-context -->
# Using context variables in REST endpoint URLs in Data Services

Last updated: 9/30/2026

Context variables are supported in REST service provider and consumer endpoints in Data
Services. This allows you to run multiple interacting services locally in Talend Studio, while having the endpoints contextualized so
that you can deploy services to various environment using a different context.

You can use context variables in the endpoint URL of tRESTRequest,
tRESTClient and cREST, either an absolute or
relative path.

For example, the following context variables are defined in Talend Studio.

| Context | Value |
| --- | --- |
| context.full\_a | http://localhost:8090/services/customers |
| context.full\_b | http://localhost:8090/customers |
| context.full\_c | http://localhost:8090/any/customers |
| context.url\_a | /customers |
| context.url\_b | /services/customers |
| context.port\_a | 8090 |
| context.port\_b | 8091 |

If you specify the endpoint URL with the context variables, the service will
be exposed at the following addresses.

| Endpoint | Studio | Runtime | Microservice(app/docker) |
| --- | --- | --- | --- |
| context.full\_a | http://localhost:8090/services/customers | http://localhost:8090/services/customers | http://localhost:8090/services/customers |
| context.full\_b | http://localhost:8090/customers | http://localhost:8090/customers | http://localhost:8090/customers |
| context.full\_c | http://localhost:8090/any/customers | http://localhost:8090/any/customers | http://localhost:8090/any/customers |
| context.url\_a | http://localhost:8090/customers | http://localhost:8040/services/customers | http://localhost:8065/services/customers |
| context.url\_b | http://localhost:8090/services/customers | http://localhost:8040/services/customers | http://localhost:8065/services/customers |
| "http://localhost:"+ context.port\_b + context.url\_b | http://localhost:8091/services/customers | http://localhost:8091/services/customers | http://localhost:8091/services/customers |
| context.url\_a + "/rest" | http://localhost:8090/customers/rest | http://localhost:8040/services/customers/rest | http://localhost:8065/services/customers/rest |
| "http://localhost:8090" + context.url\_a + "/" + System.getProperty("user.name") | http://localhost:8090/customers/<DynamicOSLoginUserName> | http://localhost:8040/services/customers/<DynamicOSLoginUserName> | http://localhost:8065/services/customers/<DynamicOSLoginUserName> |

Information noteNote: If the endpoints contains a Java code like
System.getProperty, user should set this properties before
running the bundle in Talend Runtime or
Microservice. Otherwise there will be an error as the properties are missing.

### In this section

* [Choosing service endpoint by context in Talend Runtime](/talend/en-US/components/8.0/esb-rest/trestclient-choosing-service-endpoint-by-context-in-talend-runtime)

**Related reference**  

* [tRESTClient](trestclient "Interacts with RESTful Web service providers by sending HTTP and HTTPS requests using CXF (JAX-RS) getting the corresponding responses.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Configuring the tFixedFlowInput component](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-tfixedflowinput-component-standard-component)
* [Configuring the tXMLMap component](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-txmlmap-component-standard-component-esb)
* [Configuring the tRESTClient component](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-trestclient-component-standard-component-esb)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-running-job-and-checking-result-standard-component-press -->
# Running the Job and checking the result

Last updated: 9/30/2026

Press Ctrl+S to save your Job, and press
F6 to execute it.

The console displays the response:

If you enter the REST service URL in your Web browser, `https://api.predic8.de/shop/products/154` in
this example, you should see the information like the following:


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-setting-up-job-standard-component-create -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Create a Job and add the following components to the
   Job by typing their names in the design workspace or dropping them from the
   Palette: a tFixedFlowInput, a tXMLMap, a
   tRESTClient, and two tLogRow.
2. Label the components to best describe the actions to perform.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-creating-job-and-adding-components-standard-component-create -->
# Creating the Job and adding components

Last updated: 9/30/2026

## Procedure

1. Create a Job and add the following components by typing their names in the
   design workspace or drop them from the Palette: 
   * tFileInputDelimited, to read user
     information of a local file,
   * tXMLMap, to adapt the input
     structure to the REST service structure, and
   * tRESTClient, used to call the
     REST service to send data to the remote database.
2. Connect the tFileInputDelimited to the
   tXMLMap using a Row > Main
   connection.
3. Connect the tXMLMap to the tRESTClient using a Row > Main connection, and
   give the output flow a name, *request* in
   this example.
4. Label the components to best describe the actions to perform.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-running-job-to-check-information-standard-component-press -->
# Running the Job to check the information

Last updated: 9/30/2026

Press Ctrl+S to save your Job, and press
F6 to execute it.

The console displays the client-server exchange information:

The console of the server Job displays the exchange information and the database
update result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-setting-up-components-standard-component -->
# Setting up the components

Last updated: 9/30/2026

### In this section

* [Configuring the input data and the structure mappings](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-input-data-and-structure-mappings-standard-component)
* [Configuring the service call](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-service-call-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Configuring the service call](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-configuring-service-call-standard-component)
* [Mapping the service structure and displaying the retrieved user information](/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-mapping-service-structure-and-displaying-retrieved-user-information-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run console to
   launch the Job. 

   The console shows that the tRESTClient
   component successfully reads the user information from the server end
   corresponding to the specified user ID.

   If you selected XML in the Accept Type list of the tRESTClient component, the execution result will be:

   If you selected JSON in the Accept Type list of the tRESTClient component, the execution result will be:


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: 
   * tRESTClient, used to call the
     REST service and retrieve user information from the server
     end,
   * tXMLMap, used to adapt the tree
     structure of the REST service, and
   * tLogRow, to display the retrieved
     user information on the Run
     console.
2. Connect the tRESTClient to the tXMLMap using a Row > Response
   connection.
3. Connect the tXMLMap to the tLogRow using a Row > Main connection, and
   give it a name, *out* in this
   example.
4. Label the components to best describe the actions to perform.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-choosing-service-endpoint-by-context-in-talend-runtime -->
# Choosing service endpoint by context in Talend Runtime

Last updated: 9/30/2026

This section will show you how to choose a service endpoint by context in Talend Studio and Talend Runtime.

### In this section

* [Defining REST service endpoint with context](/talend/en-US/components/8.0/esb-rest/trestclient-defining-rest-service-endpoint-with-context-in-this)
* [Executing the service in Talend Studio](/talend/en-US/components/8.0/esb-rest/trestclient-executing-service-in-talend-studio-when)
* [Deploying the service into Runtime by ESB Conductor in Talend Administration Center](/talend/en-US/components/8.0/esb-rest/trestclient-deploying-service-into-runtime-by-esb-conductor-in-talend-administration-center-if-you)
* [Deploy into Runtime by coping KAR/JAR into deploy folder](/talend/en-US/components/8.0/esb-rest/trestclient-deploy-into-runtime-by-coping-kar-jar-into-deploy-folder-if-you)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-tfixedflowinput-component-standard-component -->
# Configuring the tFixedFlowInput component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to display its
   Basic settings view.
2. Click the [...] button next to Edit
   Schema to open the schema editor.
3. Click the [+] button to add two columns, namely
   `name` and `price`.
4. Click OK to close the schema
   editor and accept propagating the changes when prompted by the system.
5. In the Mode area, select the Use Single
   Table option.

   The four defined columns display in the Values panel of the Basic
   settings view of tFixedFlowInput.
6. In the Value cell of each column, give the value
   `"Wildberries"` to `name` and
   `4.99` to `price`.
7. Connect the tFileInputDelimited to the tXMLMap using a Row > Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-trestclient-component-standard-component-esb -->
# Configuring the tRESTClient component

Last updated: 9/30/2026

## Procedure

1. Double-click the tRESTClient
   component to open its Basic settings
   view.
2. Fill the URL field with the
   URL of the REST service that the request will be sent to,
   `"https://api.predic8.de/shop/v2/products/"`.
3. From the HTTP Method list, select
   POST.
4. From the Content Type list, select
   JSON.
5. From the Accept Type list, select
   any.
6. In the Advanced settings view, select the Drop JSON Request Root check box to drop the root JSON
   element.
7. Connect tRESTClient to the
   tLogRow components using the Row > Response and Row >
   Error connections respectively.
8. Keep the default settings of the tLogRow to
   monitor the message exchanges.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-txmlmap-component-standard-component-esb -->
# Configuring the tXMLMap component

Last updated: 9/30/2026

## Procedure

1. Double-click tXMLMap in
   the design workspace to open the Map
   Editor.
2. Click the [+] button on
   the top right to add an output and name it as
   `Json_post`.
3. Click the [+] button on the bottom
   right to add two columns for the output. 

   Name the first column as `body` and set the
   Type to Document.

   Name the second column as `string` and set
   the Type to String.
4. Right-click on the root node, and select As
   loop element.
5. Right-click on the root
   node, and select Create Sub-Element to
   create a sub-element. Name the sub-element `name` in the
   popup dialog box.
6. Repeat the previous step to create sub-element
   `price`.
7. Select the `name` column of the input
   table to the left and drop it onto the `name` node of the
   output table to the right.
8. Repeat the previous step to map the input and the output tables as shown
   above.
9. Click the wrench icon on the top of the output table to open
   the setting panel.
10. Set the All in one feature as
    true, this way all XML data is
    outputted in one single flow.
11. Click OK to save the settings.
12. Right-click the tXMLMap component and select Row > Json\_post to link to the
    tRESTClient component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-input-data-and-structure-mappings-standard-component -->
# Configuring the input data and the structure mappings

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Basic settings
   view.
2. Specify the input file in the File name
   field, fill the Header field with 1 to skip
   the header row, and keep the rest parameters as they are.
3. Click the [...] button next to Edit schema to open the Schema dialog box, and edit the input schema as
   follows:
   * *id*, type Integer, 2 characters
     long, set as the key column
   * *first\_name*, type String
   * *last\_name*, type String
4. Double-click the tXMLMap component to
   open the Map Editor.
5. Rename the *root* node in the output
   table: right-click the node, select Rename
   from the contextual menu, and specify a new name in the pop-up dialog box,
   *user* in this example.
6. Select all the three columns in the input table and drop them onto the
   *user* node, and select the Create as sub-element of target node option from
   the pop-up dialog box to set these columns as sub-elements of the *user* node. When done, click OK to validate the mappings and close the Map
   Editor.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tfileinputdelimited-tfileinputdelimited-configuring-service-call-standard-component -->
# Configuring the service call

Last updated: 9/30/2026

## Procedure

1. Double-click the tRESTClient component to
   open its Basic settings view.
2. Fill the URL field with the URI location
   where the REST service is accessible,
   "http://localhost:8088/users" in this example.
3. In the Relative Path field, enter the
   resource path, "/post/" + row1.id+ "/" + row1.first\_name + "/" +
   row1.last\_name in this example. This will send the data from the
   input row to the server end via the resource path.
4. From the HTTP Method list, select
   GET to send an HTTP request for
   retrieving the existing records.

   From the Accept Type list, select the
   type the client end is prepared to accept for the response from the server
   end, XML.
5. In the Advanced settings view of the
   tRESTClient component, select the
   Log messages check box to log the
   message exchange information with the server.

   Leave the rest of the settings as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-configuring-service-call-standard-component -->
# Configuring the service call

Last updated: 9/30/2026

## Procedure

1. Double-click the tRESTClient component to
   open its Basic settings view.
2. Fill the URL field with the URL of the
   REST service you are going to invoke, *"http://localhost:8088/users"* in this example. Note that the
   URL provided in this use case is for demonstration purposes only and not a
   live address.
3. From the HTTP Method list, select
   GET to send an HTTP request for
   retrieving the existing records.

   From the Accept Type list, select the
   type the client end is prepared to accept for the response from the server
   end, XML. Leave the rest of the settings as
   they are.
4. Click the [+] button beneath the
   Query parameters table to add two
   parameters, *from* and *to*, and set both parameters to *2*, to get the information of the user with the
   ID of *2*.

   Alternatively, you can query the information of the user with the ID of 2
   by adding *?from=2&to=2* to the service
   URL.
5. In the Advanced settings view of the
   tRESTClient component, select the
   Log messages and the Convert Response To DOM Document check boxes to
   log the message exchange to the server and convert the response from the
   server to document type.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-txmlmap-tlogrow-tlogrow-mapping-service-structure-and-displaying-retrieved-user-information-standard-component -->
# Mapping the service structure and displaying the retrieved user information

Last updated: 9/30/2026

## Procedure

1. Double-click the tXMLMap component to
   open the Map Editor.
2. If you selected XML in the Accept Type list of the tRESTClient component, define the input XML tree structure
   according to the service structure.
   1. In the input table, right-click the default *root* node of the *body* column, select Rename from the contextual menu, and
      rename it to *users*.
   2. Right-click the *users* node,
      select Create Sub-Element from the
      contextual menu, and create sub-element named *user*. Set *user* as the loop element because the XML structure
      of the Web service to be invoked is looped on this element.
   3. Right-click the *user* node,
      select Create Attribute from the
      contextual menu, and enter *id* in
      the Create New Attribute dialog
      box to create an attribute named *id* for the *user*
      node.
   4. Right-click the *user* node
      again, select Create Sub-Element
      from the contextual menu, and enter *first\_name* in the Create New
      Element dialog box to create an sub-element named
      *first\_name* for the *user* node.

      Repeat this operation to create another sub-element under the
      *user* node, *last\_name*.
   5. Drop the *id*, *first\_name* and *last\_name* columns from the input table to the output
      table, and then click OK to
      validate the mapping and close the Map Editor.

   If you selected JSON in the Accept Type list of the tRESTClient component, the response from the server end will
   be sent back in JSON format and converted to document type. In this example,
   the converted response structure looks like the following:

   ```
   <root>
       <users>
           <user>
               <id>2</id>
               <first_name>Theodore</first_name>
               <last_name>Harding</last_name>
           </user>
       </users>
   </root>
   ```

   Note that the <root> element is removed if the Wrap JSON Response check box is cleared in the
   Advanced settings of the tRESTClient component.

   Define the input XML tree structure accordingly and map it with the output
   data flow in a similar manner as described above.
3. Double-click the tLogRow component to
   open its Basic settings view.
4. Click the Sync columns button to make
   sure the component schema is synchronized with the output schema of the
   tXMLMap component.
5. In the Mode field, select the Table option to display the GET result in table
   cells.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-defining-rest-service-endpoint-with-context-in-this -->
# Defining REST service endpoint with context

Last updated: 9/30/2026

In this use case, a relative URL is set for the service in Talend Studio, /services/{Name}.

Name is given different values in the
following contexts.

| Context | Value |
| --- | --- |
| Default | contacts |
| dev | dev/contacts |
| test | test/contacts |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-deploy-into-runtime-by-coping-kar-jar-into-deploy-folder-if-you -->
# Deploy into Runtime by coping KAR/JAR into deploy folder

Last updated: 9/30/2026

If you deploy the service into Talend Runtime by coping the KAR/JAR into <TalendRuntimePath>/deploy folder, you can change the service endpoint by
creating a configuration file in <TalendRuntimePath>/etc
called <JobName>.cfg which contains a single line, for
example:

```
context = Default
```

The service will be available in the following endpoints in different context.

| Context | Available endpoint |
| --- | --- |
| Default | http://localhost:8040/services/contacts |
| dev | http://localhost:8040/services/dev/contacts |
| test | http://localhost:8040/services/test/contacts |

In order to ensure that the service starts in the correct context, you need
create the <JobName>.cfg file with the correct context
setting before putting the KAR/JAR file into the <TalendRuntimePath>/deploy folder.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-deploying-service-into-runtime-by-esb-conductor-in-talend-administration-center-if-you -->
# Deploying the service into Runtime by ESB Conductor in Talend Administration Center

Last updated: 9/30/2026

If you deploy the service into Talend Runtime from the ESB conductor in Talend Administration Center, you can change the service endpoint by choosing different context in the
ESB Conductor.

| Context | Available endpoint |
| --- | --- |
| Default | http://localhost:8040/services/contacts |
| dev | http://localhost:8040/services/dev/contacts |
| test | http://localhost:8040/services/test/contacts |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestclient-executing-service-in-talend-studio-when -->
# Executing the service in Talend Studio

Last updated: 9/30/2026

When executing the service in Talend Studio, the service will be available in the following endpoints in different
context.

| Context | Available endpoint |
| --- | --- |
| Default | http://localhost:8090/services/contacts |
| dev | http://localhost:8090/services/dev/contacts |
| test | http://localhost:8090/services/test/contacts |
