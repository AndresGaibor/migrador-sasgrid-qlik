<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest · versión 8.0 -->
# tRESTRequest

Last updated: 9/30/2026

Receives GET/POST/PUT/PATCH/DELETE requests from the clients on the server
end.

tRESTRequest accepts the HTTP and/or HTTPS
requests from the clients and supports GET, POST, PUT, PATCH and DELETE HTTP
methods.

Information noteNote:

To enable the HTTPS support, you have to generate a keystore and add some
HTTPS security configuration properties in the *org.ops4j.pax.web.cfg* file of your Runtime container before deploying the
service on it. For more information, see [HTTP configuration](/talend/r/en-US/8.0/esb-container-administration-guide/http-configuration).

## tRESTRequest Standard properties

These properties are used to configure
tRESTRequest running in the Standard Job framework.

The
Standard
tRESTRequest component belongs to the ESB family.

*This component is relevant only when used with one of the 
Talend
 solutions with ESB, as it should be used with the Service Repository node and the Data Service creation related wizard(s).*

## Basic settings

| Properties | Description |
| --- | --- |
| API Definition / Definition | Click [...] to browse to the API definition file to initialize your component endpoint, API mappings and documentation from your API definition.  The output flow values in the API mapping are used in generated Java code, therefore they need to be camel case compliant. Output flow values are taken or computed from the API definition with these priorities:  * operationId, which is the best practice. Even though operationId is not   a mandatory field in OAS specification, it is recommended to use it at   API design time. * summary (Name in Talend API Designer), which will be converted and truncated in 120 characters to supported   format. * operation method and path, which will be computed with the same   constraint as summary. |
| REST Endpoint | Fill this field with the service path where the REST service is accessible. For Data Service deployments in Talend Runtime Container (ESB Runtime), do not include hostname:port in this field.  The default endpoint value for a new component is "/restservice/v1". This value is meant as an example. Replace it with your own path value. You can define the endpoint path using context variables. |
| REST API Mapping | Click the [+] button beneath the mapping table to add lines to specify HTTP request:  Output Flow: Click the [...] button to specify the name of an output flow and set the schema for that output flow in the dialog box afterwards.  The schema is not mandatory, so if you do not need to pass additional parameters to the tRESTRequest component, you can leave the schema empty. However, you will have to populate the schema if you have URI Path parameters set in the URI Pattern field or if you need to add optional request parameters such as URI Query, HTTP Header or Form parameters, to the URI specified in the REST Endpoint field.  Add a schema with the name *body* to get the request body of POST and PUT methods. It supports Document, String, and Byte types.  If you specify URI parameters in the output flow schema, you might need to define what type of parameter it is in the Comment field of the schema. By default, if you leave the Comment field empty, the parameter is considered as a Path parameter. Below is a list of supported Comment values:  * empty or *path* corresponds to the default   @PathParam, * *query* corresponds to @QueryParam, * *form* corresponds to @FormParam, * *header* corresponds to   @HeaderParam. * *matrix* corresponds to   @MatrixParam. * *multipart* corresponds to the CXF   specific @Multipart, representing the request body. It can   be used only with POST and PUT HTTP methods.  For example, add a column *number* and enter *query* in the   Comment field to get the number parameter in   the request. Add a column with the same name as the header and enter   *header* in the Comment field to fetch   the HTTP header.  You can not use API operation names with special characters, for   example - or $ in the   Column column as these operation names will   be used as Java identifiers in generated code.  If you have installed the R2022-02 Talend Studio Monthly update or a later one delivered by Talend, you can use any character for parameter names by adding   (param-name) behind parameter type in the   Comment column. This mechanism avoids   failures when importing APIs from the Talend API Designer in a data service. If special characters are used in the API   designer, they are replaced in the Column   column to be Java compliant and real parameter name is added to the   Comment column. For more information about   Talend Studio Monthly update, check with your administrator.   Information noteNote: We recommend you to set the default values of your optional parameters (Header, Query, Form). To do so, fill in the Default columns of the schema.  HTTP Verb: Select a HTTP method (GET/POST/PUT/PATCH/DELETE/OPTIONS/HEAD) from the list.  URI pattern: Fill this field with REST-ful URIs that describe the resource.  Consumes: Select the format type of the consume content that the component will use from XML or JSON, XML, JSON, Form, Multipart and Any in the list when the HTTP method is POST, PUT, or PATCH.  Produces: When the HTTP method is GET, POST, PUT, PATCH, or DELETE, select the format type of the produce content that the component will use from XML or JSON, XML, JSON, HTML and Any, or select <oneway> in the list to accept one way requests.  Streaming: Select this check box to stream the response data by chunks so that the large volumes of data can be processed efficiently. |
| Security | Select this check box to enable the security option for the current service. Select the security scheme from:   * Basic HTTP: The simplest technique for enforcing   access controls to web resources using standard fields in the HTTP   header. * JWT Bearer Token: The open and standardized method   for storing and exchanging data in JSON format. * SAML Token: An XML-based, open-standard data format   for exchanging authentication and authorization data between an identity   provider and a service provider. * Open ID Connect: An extension for OAuth2 which allows   Clients to verify the identity of the End-User based on the authentication   performed by an Authorization Server, as well as to obtain basic profile   information about the End-User in an interoperable and REST-like manner. For   more information, see [Talend Identity and Access   Management](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/talend-identity-and-access-management) and [Managing ESB Resources and   authorizations](/talend/r/en-US/8.0/administration-center-user-guide/managing-esb-resources-and-authorizations). |
| JWT configuration | JWT configuration options appear when JWT Bearer Token is selected in the Security list. In the Keystore Type list, select:  * Java Keystore (\*.jks) to provide a local Java   keystore file, * PKCS12 Keystore (\*.p12, \*.pfx) to provide a local   keystore file in PKCS12 format, * JSON Web Key Sets (JWKS) to provide the URL of   the online key sets.  For the Java Keystore (\*.jks) or PKCS12 Keystore (\*.p12, \*.pfx) keystore type, you need to enter the location of the keystore file and the associated password in the Keystore File and Keystore Password fields respectively. You can also set the Keystore Alias and Audience as needed.  For the JSON Web Key Sets (JWKS) keystore type, you need to specify the URL of the online key sets in the JWKS URL field. You can also set the Audience as needed. |
| Use Service Locator | Select this check box to enable the Service Locator. It maintains the availability of the service to help meet demands and service level agreements (SLAs). Specify the Service namespace and the Service name in the corresponding fields. |
| Use Service Activity Monitor | Select this check box to enable the Service Activity Monitor. It captures events and stores this information to facilitate in-depth analysis of service activity and track-and-trace of messages throughout a business transaction. This can be used to analyze service response times, identify traffic patterns, perform root cause analysis and more. |
| Use Authorization | Select this check box to enable authorized call. This option appears when SAML Token is selected in the Security list.  For more information about the management of user roles and rights, see [Managing ESB Resources and authorizations](/talend/r/en-US/8.0/administration-center-user-guide/managing-esb-resources-and-authorizations) and [Talend Identity and Access Management](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/talend-identity-and-access-management). |
| Use Business Correlation | Select this check box to enable the correlation option so that chained service calls will be grouped under the same correlation ID. tRESTRequest will extract the correlation ID from the request header and store it in the component variable for further use in the flow.  If this option is not enabled on the client side, a correlation ID will be generated automatically in tRESTRequest. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Log messages | Select this check box to log the message exchange between the service provider and the consumer. |
| Expose OpenAPI documentation | Select this checkbox to activate documentation of an API implementation. When this option is enabled, deployed REST service offers the following endpoints to access API documentation:  * http://host:port/[component\_endpoint]/openapi.json: API   documentation as raw text (JSON file as OpenAPI 3.0.1 format). * http://host:port/[component\_endpoint]/api-docs: A UI with   API documentation and opportunity to test API operations.   If this option is enabled and the REST service is built as a Microservice, you can activate or deactivated API documentation by adding the exposeOpenApi=[true/false] parameter in the application.properties configuration file inside the Microservice JAR, or using the -DexposeOpenApi=[true/false] parameter in the command when running the Microservice. Information noteNote: This option is available only if you have installed the R2025-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  To use this feature in Talend Runtime, you need to install Talend Runtime 8.0.1-R2025-10 patch or a later one and execute command feature:install cxf-rs-description-openapi-v3 inside the Runtime console. For more information, see [Starting Talend Runtime with console](https://help.qlik.com/talend/en-US/esb-container-administration-guide/8.0/starting-talend-runtime-with-console) and [Feature Scope](https://help.qlik.com/talend/en-US/esb-container-administration-guide/8.0/feature-scope). |
| Wrap JSON Request | Select this check box to wrap the JSON request with a *root* element. |
| Attributes to Elements | Select this check box to exclude @ in the response attribute. |
| Convert JSON values to String in response | Select this check box to convert the JSON values to string format in the response. |
| JAXRS properties | This option appears when JWT Bearer Token is selected in the Security list in the Basic settings tab. Click [+] to add as many properties as needed to the table. In the Property Name field, you can either select the property from the drop-down list, or enter a property name that is not available in the list. Enter the value of the property in the Property Value field. For more information on the JAXRS properties, see the [Apache CXF documentation](https://cxf.apache.org/docs/jax-rs-jose.html#JAXRSJOSE-Configuration). |
| Service Locator Customer Properties | This option appears when Use Service Locator  is enabled in the Basic settings tab. Click [+] to add as many properties as needed to the table. Enter the name and the value of each property in the Property Name field and the Property Value field respectively to identify the service. |
| Service Activity Customer Properties | This option appears when Use Service Activity Monitor is enabled in the Basic settings tab. Click [+] to add as many properties as needed to the table. Enter the name and the value of each property in the Property Name field and the Property Value field respectively to identify the service. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  URI: the URI of the REST request. This is a Flow variable and it returns a string.  URI\_BASE: the base URI of the REST request. This is a Flow variable and it returns a string.  URI\_ABSOLUTE: the absolute URI of the REST request. This is a Flow variable and it returns a string.  HTTP\_METHOD: the http method. This is a Flow variable and it returns a string.  ATTACHMENT\_HEADERS: the attachment headers from the REST request. This is a Flow variable and it returns a list of attachment header values.  ATTACHMENT\_FILENAMES: the attachment filenames from the REST request. This is a Flow variable and it returns all attachment filenames.  PRINCIPAL\_NAME: the principal name of the REST request. This is a Flow variable and it returns a string.  CORRELATION\_ID: the correlation ID by which chained service calls will be grouped. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers the possibility that a Talend Job can be wrapped as a service, with the ability to input a request to a service into a Job and return the Job result as a service response.  The tRESTRequest component should be used with the tRESTResponse component to provide a Job result as a response, in case of a request-response communication style. |
| Limitation | Using context variables for dynamic endpoint or Service Locator namespace works in Talend Studio only. It is not supported in Talend Runtime. |

**Related concepts**  

* [Using a REST service to accept HTTP POST requests and send responses](trestrequest-trestclient-tlogrow-using-rest-service-to-accept-http-post-requests-and-send-responses-standard-component-esb-this)
* [Using a REST service to accept HTTP POST requests in an HTML form](trestrequest-trestresponse-txmlmap-tjavarow-using-rest-service-to-accept-http-post-requests-in-html-form-standard-component-esb-this)
* [Using a REST service to accept HTTP POST requests](use-rest-accept-http-post)
* [Using a REST service to accept HTTP GET requests and send responses](trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-using-rest-service-to-accept-http-get-requests-and-send-responses-standard-component-esb-this)
* [Using URI Query parameters to explore the data of a database](trestrequest-trestresponse-tfixedflowinput-tmysqloutput-using-uri-query-parameters-to-explore-data-of-database-standard-component-esb-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-using-rest-service-to-accept-http-post-requests-and-send-responses-standard-component-esb-this -->
# Using a REST service to accept HTTP POST requests and send responses

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario describes how to build a REST service that accepts HTTP POST requests of
Document type from the client, processes it and sends the response
back. To do this, two Jobs are built: one to create the REST service and the other to
call it.

### In this section

* [Creating the REST service Job](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-creating-rest-service-job-standard-component-esb-drag)
* [Creating the consumer Job](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-creating-consumer-job-standard-component-esb-drag)

**Related reference**  

* [tRESTClient](trestclient "Interacts with RESTful Web service providers by sending HTTP and HTTPS requests using CXF (JAX-RS) getting the corresponding responses.")
* [tRESTRequest](trestrequest "Receives GET/POST/PUT/PATCH/DELETE requests from the clients on the server end.")
* [tRESTResponse](trestresponse "Returns a specific HTTP status code to the client end as a response to the HTTP and/or HTTP requests.")

**Related information**  

* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)
* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-using-uri-query-parameters-to-explore-data-of-database-standard-component-esb-this -->
# Using URI Query parameters to explore the data of a database

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario describes how to use URI query parameters in tRESTRequest to explore data of a database, and send the response via
the tRESTResponse.

To do so, you can create two subJobs linked together by an OnSubjobOk connection; this way the two subJobs will be
executed sequentially. For more information on Trigger connection, see [Trigger connections for a Job](/talend/r/en-US/8.0/studio-user-guide/trigger-connections-for-job). The first subJob
will create and populate the database and the second one will allow to explore the database
through the REST service.

### In this section

* [Creating the first subJob](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-creating-first-subjob-standard-component-esb-to-do)
* [Creating the second subJob](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-creating-second-subjob-standard-component-esb-the)
* [Connecting the two subJobs](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-connecting-two-subjobs-standard-component-esb-now)
* [Saving and executing the Job](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-saving-and-executing-job-standard-component-esb-save)

**Related reference**  

* [tRESTRequest](trestrequest "Receives GET/POST/PUT/PATCH/DELETE requests from the clients on the server end.")
* [tRESTResponse](trestresponse "Returns a specific HTTP status code to the client end as a response to the HTTP and/or HTTP requests.")

**Related information**  

* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)
* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput)
* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)
* [tFlowToIterate](/talend/en-US/components/8.0/orchestration/tflowtoiterate)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-using-rest-service-to-accept-http-post-requests-in-html-form-standard-component-esb-this -->
# Using a REST service to accept HTTP POST requests in an HTML form

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario describes how to upload data to a REST service using HTTP POST in a HTML
form file. To do so, a Job is created to accept HTTP POST requests using the tRESTRequest component.

A predefined HTML form *UploadFile.html* is used to upload data to
the REST service:

```
<form action="http://localhost:8088/UserInfo" method="post" enctype="multipart/form-data">
	<input type="file" name="id" />
	<button>upload</button>
</form>
```

The *customer.xml* that contains a user ID will be uploaded:

```
  <customer>
    <id>100</id>
  </customer>
```

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-setting-up-job-standard-component-esb-drop)
* [Configuring the tRESTRequest component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-trestrequest-component-standard-component-esb)
* [Configuring the tJavaRow component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-tjavarow-component-standard-component-esb-connect)
* [Configuring the tXMLMap component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-txmlmap-component-standard-component-esb-connect)
* [Configuring the tRESTResponse component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-trestresponse-component-standard-component-esb-connect)
* [Saving and executing the Job](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-saving-and-executing-job-standard-component-esb-save)
* [Deploying the Job in a Talend Runtime Container](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-deploying-job-in-talend-runtime-container-standard-component-esb-before)

**Related reference**  

* [tRESTRequest](trestrequest "Receives GET/POST/PUT/PATCH/DELETE requests from the clients on the server end.")
* [tRESTResponse](trestresponse "Returns a specific HTTP status code to the client end as a response to the HTTP and/or HTTP requests.")

**Related information**  

* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)
* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tJavaRow](/talend/en-US/components/8.0/java-custom-code/tjavarow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-using-rest-service-to-accept-http-get-requests-and-send-responses-standard-component-esb-this -->
# Using a REST service to accept HTTP GET requests and send responses

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario describes the process of accepting an HTTP request from the client,
processing it and sending the response back.

### In this section

* [Configuring the tRESTRequest component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-trestrequest-component-standard-component-esb-drop)
* [Configuring the first tXMLMap component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-first-txmlmap-component-standard-component-esb-connect)
* [Configuring the second tXMLMap component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-second-txmlmap-component-standard-component-esb-connect)
* [Configuring the tRESTResponse component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-trestresponse-component-standard-component-esb-connect)
* [Saving and executing the Job](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-saving-and-executing-job-standard-component-esb-save)

**Related reference**  

* [tRESTRequest](trestrequest "Receives GET/POST/PUT/PATCH/DELETE requests from the clients on the server end.")
* [tRESTResponse](trestresponse "Returns a specific HTTP status code to the client end as a response to the HTTP and/or HTTP requests.")

**Related information**  

* [tExtractJSONFields](/talend/en-US/components/8.0/processing/textractjsonfields)
* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-creating-consumer-job-standard-component-esb-drag -->
# Creating the consumer Job

Last updated: 9/30/2026

Drag and drop the following components from the Palette onto the design workspace: a tFixedFlowInput, a tXMLMap, a
tRESTClient and a tLogRow.

### In this section

* [Configuring the tFixedFlowInput component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-tfixedflowinput-component-standard-component-esb)
* [Configuring the tXMLMap component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-txmlmap-component-standard-component-esb-connect)
* [Configuring the tRESTClient component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-trestclient-component-standard-component-esb)
* [Saving and executing the Job](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-saving-and-executing-job-standard-component-esb-save)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-creating-rest-service-job-standard-component-esb-drag -->
# Creating the REST service Job

Last updated: 9/30/2026

Drag and drop the following components from the Palette onto the design workspace: a tRESTRequest, a tXMLMap and a
tRESTResponse.

### In this section

* [Configuring the tRESTRequest component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-trestrequest-component-standard-component-esb)
* [Configuring the body of the response](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-body-of-response-standard-component-esb-connect)
* [Configuring the tRESTResponse component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-trestresponse-component-standard-component-esb-connect)
* [Launching the service](/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-launching-service-standard-component-esb-save)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-connecting-two-subjobs-standard-component-esb-now -->
# Connecting the two subJobs

Last updated: 9/30/2026

## About this task

Now that the two subJobs are created, you can connect them together:

## Procedure

1. Right-click the tFixedFlowInput
   component of the first subJob.
2. Select Trigger > OnSubjobOk on the list.
3. Click the tRESTRequest component of
   the second subJob.

## Results

This way, when executing the job, the second subJob will be executed only if the
first one's execution succeeded.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-creating-first-subjob-standard-component-esb-to-do -->
# Creating the first subJob

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput from the Misc family and tMysqlOutput from the Databases > Mysql
   family.
2. Link tFixedFlowInput to tMysqlOutput using a Row > Main
   connection.
3. Double-click tFixedFlowInput
   to display its Basic settings view:
4. Click the [...] button next
   to Edit schema to open the schema
   editor.
5. In the schema editor, click the [+]
   button three times to add three lines and set them as displayed in the above
   screenshot.
6. Click Ok.
7. Back to tFixedFlowInput
   Basic settings view, in the Mode area, select the Use
   inline table option.
8. Under the inline table, click the [+]
   button three times to add three rows in the table.
9. In the inline table, click the *id* field
   of the first row and type in *1*.
10. Click the *firstname* field of the first
    row, press Ctrl+Space to display the
    autocompletion list and select the TalendDataGenerator.getFirstName() variable in the
    list.
11. Click the *lastname* field of the first
    row, press Ctrl+Space to display the
    autocompletion list and select the TalendDataGenerator.getLastName() variable in the
    list.
12. Do the same for the two following rows to obtain the settings displayed in
    the screenshot.
13. Double-click tMysqlOutput to
    display its Basic settings view:
14. From the Property Type list, leave
    Built-in and fill in the Host, Port,
    Database, Username and Password
    fields manually. If you centralized your connection information to the
    database in the Metadata > DB Connections node of the Repository, you can select Repository from the list and the fields will be
    automatically filled in.

    For more information about storing metadata, see [Managing metadata in Talend Studio](/talend/r/en-US/8.0/studio-user-guide/managing-metadata-in-studio).
15. In the Table field, type in the name of
    the table in which the data will be loaded, for example: *users*.
16. From the Action on table list, select
    Drop table if exists and create, select
    Insert from the Action on data list.
17. Click Sync columns to retrieve the schema
    coming from the previous component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-creating-second-subjob-standard-component-esb-the -->
# Creating the second subJob

Last updated: 9/30/2026

The following components are used as displayed in the first screenshot:

* tRESTRequest and tRESTResponse from the ESB >
  REST family,
* tFlowToIterate from the Orchestration family,
* tMysqlInput from the Databases > Mysql family,
* tXMLMap from the Processing family.

### In this section

* [Configuring the tRESTRequest component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-trestrequest-component-standard-component-esb-to-do)
* [Configuring the tMysqlInput component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-tmysqlinput-component-standard-component-esb-to-do)
* [Configuring the tXMLMap component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-txmlmap-component-standard-component-esb)
* [Configuring the tRESTResponse component](/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-trestresponse-component-standard-component-esb-connect)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-saving-and-executing-job-standard-component-esb-save -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Save the Job and press F6 to execute
   it.
2. Go to your browser if you want to test the service. 

   For example, use the URI query ?to=2 to retrieve the data of
   the two first users.

   The HTTP request for a user ID is accepted by the REST service
   and the HTTP response is sent back to the server.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-tjavarow-component-standard-component-esb-connect -->
# Configuring the tJavaRow component

Last updated: 9/30/2026

## Procedure

1. Connect tRESTRequest to tJavaRow using the Row > UserInfo
   connection.
2. Double-click tJavaRow in the design
   workspace to display its Basic settings
   view.
3. Enter the following code in the Code box
   to convert the message into Document type and print it in the
   console.

   ```
   String  result = new String(input_row.id,0,input_row.id.length);

   routines.system.Document doc = new routines.system.Document();

   doc.setDocument(org.dom4j.DocumentHelper.parseText(result));

   output_row.id = doc;

   System.out.println(result);
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-trestrequest-component-standard-component-esb -->
# Configuring the tRESTRequest component

Last updated: 9/30/2026

## Procedure

1. Double-click tRESTRequest in the design
   workspace to display its Basic settings
   view.
2. In the REST Endpoint field, keep the
   default URI *"http://localhost:8088/"* where the REST-ful
   web service will be accessible for requests.
3. Click the [+] button to add one line in
   the REST API Mapping table.
4. Select the newly-added line and click the [...] button in the Output
   Flow column to add a schema for the output flow. Give the
   name for the schema *UserInfo* in this scenario. 

   The schema editor opens. Click the [+]
   button to add a new line *id* of byte[] type
   and enter *multipart* in the Comment field. Click OK to
   save the schema.
5. Back to tRESTRequest
   Basic settings view, select POST from the list in the HTTP Verb column.
6. Fill the field in the URI Pattern column
   with *"/UserInfo"*.
7. Select Multipart in the Consumes list. Keep the default settings of the
   other options.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-trestresponse-component-standard-component-esb-connect -->
# Configuring the tRESTResponse component

Last updated: 9/30/2026

## Procedure

1. Connect tXMLMap to a tRESTResponse using Row > response
   connection.

   The schema defined in tXMLMap is
   retrieved in tRESTResponse
   automatically.
2. Select OK(200) from the Return status code list.
3. Leave the rest of the settings as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-configuring-txmlmap-component-standard-component-esb-connect -->
# Configuring the tXMLMap component

Last updated: 9/30/2026

## Procedure

1. Connect tJavaRow to tXMLMap using the Row >
   Main connection.
2. Double-click tXMLMap in the design
   workspace to open the Map Editor.
3. Click the [+] button on the bottom left
   to add a column *id* of Document type for
   the input.
4. Right-click the root node of the input
   table and select Rename in the contextual
   menu and rename it *customer*.
5. Create a sub-element to the *customer* node by
   selecting Create Sub-Element in the
   contextual menu. Name the sub-element as *id* in the
   pop-up dialog box.
6. Click the [+] button on the top right to
   add an output and name it as *response*.
7. Click the [+] button on the bottom right
   to add a column *body* of Document type for
   the output.
8. Right-click the root node of the input
   table and select Rename in the contextual
   menu and rename it *customer*.
9. Create a sub-element to the *customer* node by
   selecting Create Sub-Element in the
   contextual menu. Name the sub-element as *id* in the
   pop-up dialog box.
10. Select the *id* column from the input
    table and drop it onto the Expression field
    of the *id* node of the output
    table.
11. Click OK to save the settings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-deploying-job-in-talend-runtime-container-standard-component-esb-before -->
# Deploying the Job in a Talend Runtime Container

Last updated: 9/30/2026

## Before you begin

Before deploying the Job, first start a Talend Runtime Container, and
make sure all its Infrastructure Services have been started. For more information, see
[Starting and stopping Talend ESB infrastructure
services](/talend/r/en-US/8.0/esb-container-administration-guide/starting-and-stopping-talend-esb-infrastructure-services).

## Procedure

1. Click the Kill button in the execution
   console to stop it.
2. In the Repository tree view, right-click the Job and select
   Build Job to open the Build Job
   dialog box.
3. In the To archive file field, browse to the directory where
   you want to save your built Job.
4. Select OSGI Bundle For ESB in the Build
   Type list.
5. Click Finish.

   The Job is built to the specified directory, as a
   trestrequest-0.1.jar file.
6. Copy the trestrequest-0.1.jar file, and paste it into the deploy
   folder of the Talend Runtime Container. The service starts
   directly.
7. Run the *UploadFile.html* using a web browser.
8. Click the Browse button to navigate to
   the *customer.xml* that contains the user ID and click
   upload.
9. The HTTP POST request is accepted by the REST service and the user ID is
   sent back to the server.

   You can also view the response in the page source.
10. The content of the input file is shown in the Talend Runtime Container window.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-saving-and-executing-job-standard-component-esb-save -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Save the Job and press F6 to execute
   it.
2. Run the *UploadFile.html* using a web browser.
3. Click the Browse button to navigate to
   the *customer.xml* that contains the user ID and click
   upload.
4. The HTTP POST request is accepted by the REST service and the user ID is
   sent back to the server.

   You can also view the response in the page source.
5. The content of the input file is printed in the execution console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-tjavarow-setting-up-job-standard-component-esb-drop -->
# Setting up the Job

Last updated: 9/30/2026

Drop the following components from the Palette
onto the design workspace: a tRESTRequest, a
tJavaRow, a tXMLMap and a tRESTResponse.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-first-txmlmap-component-standard-component-esb-connect -->
# Configuring the first tXMLMap component

Last updated: 9/30/2026

## Procedure

1. Connect tRESTRequest to a tXMLMap using the Row > GetOneUser
   connection.
2. Double-click tXMLMap in the design workspace
   to open the Map Editor.
3. Click the [+] button on the top right to add
   an output and name it as *ResponseUsers*.
4. Click the [+] button on the bottom right to
   add two columns for the output.

   Name the first column as *body* and set the Type to Document.

   Name the second column as *string* and set the Type to String.
5. Right-click on the node root and select
   Create Sub-Element to create a sub-element.
   Name the sub-element as *foo* in the popup dialog box.
6. Right-click on the *foo* node created in the previous step
   and select As loop element.
7. Select the *id* column of the *GetOneUser* table to the left and drop it onto the
   Expression field of the *foo* node of the *ResponseUsers* table to the right.
8. Click OK to save the settings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-second-txmlmap-component-standard-component-esb-connect -->
# Configuring the second tXMLMap component

Last updated: 9/30/2026

## Procedure

1. Connect tRESTRequest to the other tXMLMap using the Row > GetUserNumber
   connection.
2. Double-click the first tXMLMap in the design
   workspace to open the Map Editor.
3. Click the [+] button on the top right to add
   an output and name it as *ResponseUserNumber*.
4. Click the [+] button on the bottom right to
   add one column for the output.

   Name the first column as *body* and set the Type to Document.
5. Right-click on the node root and select
   Create Sub-Element to create a sub-element.
   Name the sub-element as *number* in the popup dialog
   box.
6. Right-click on the *number* node created in the previous
   step and select As loop element.
7. Select the *string* column of the *GetUserNumber* table to the left and drop it onto
   the Expression field of the *number* node of the *ResponseUserNumber* table to the right.
8. Click OK to save the settings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-trestrequest-component-standard-component-esb-drop -->
# Configuring the tRESTRequest component

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: a tRESTRequest, two tXMLMap and
   two tRESTResponse.
2. Double-click tRESTRequest in the design
   workspace to display its Basic settings
   view.
3. Fill the REST Endpoint field with the URI
   location where the REST-ful web service will be accessible for requests. For
   example, *"http://192.168.0.235:8088/user"*.

   Information noteNote:

   If you want your service to be available on both HTTP and HTTPS,
   fill the field with a relative path. For example, if you type in *"/test"*, your service will be available on both *http://<DefaultHTTPEnpointAddress>/test* and *https://<DefaultHTTPSEnpointAddress>/test*, provided
   that you have configured your Runtime container to support HTTPS. For more
   information, see [HTTP configuration](/talend/r/en-US/8.0/esb-container-administration-guide/http-configuration).
4. Click the [+] button to add one line in the
   REST API Mapping table.
5. Select the newly-added line and click the [...] button in the Output Flow
   column to add a schema for the output flow.

   In this scenario, the output flow will be named as
   *GetOneUser*.

   Then click the [+] button to add a new line
   *id* to the schema in the dialog box.
6. Click OK to save the schema.
7. Select GET from the list in the HTTP Verb column.
8. Fill the field in the URI Pattern column with
   "/{id}/".
9. In the same way, add another line in the REST API
   Mapping table and name this schema *GetUserNumber*. Add a line *string* of String type to the
   schema. Enter *query* in the Comment field to get the number parameter in the
   request.

   Select GET from the list in the HTTP Verb column. Fill the field in the URI Pattern column with
   "/number".


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-configuring-trestresponse-component-standard-component-esb-connect -->
# Configuring the tRESTResponse component

Last updated: 9/30/2026

## Procedure

1. Connect tXMLMap to a tRESTResponse using Row >
   ResponseUsers connection.

   The schema defined in tXMLMap is retrieved in
   tRESTResponse automatically.
2. Select OK(200) from the Return status code list.
3. Leave the rest of the settings as they are.
4. Connect tRESTRequest to the other tRESTResponse using the Row > GetUserNumber
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-txmlmap-trestresponse-txmlmap-saving-and-executing-job-standard-component-esb-save -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Save the Job and press F6 to execute
   it.
2. Go to your browser if you want to test the service.

   The HTTP request for a user id is accepted by the REST service and the HTTP
   response is sent back to the server.
3. Repeat this step and type in *http://localhost:8088/user/number?string=123* in the address bar.
   Press Enter.

   You can see that *123* is returned in the
   response.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-tfixedflowinput-component-standard-component-esb -->
# Configuring the tFixedFlowInput component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput in the
   design workspace to display its Basic
   settings view.
2. Click Edit schema to show the schema
   editor. In the schema editor, click the [+] button to add two columns of String
   type, *id* and *name*.Click
   Ok to close the schema
   editor.
3. Back to tFixedFlowInput
   Basic settings view, in the Mode area, select the Use Inline Content option.
4. In the Content box, enter the
   *id* and *name* of three
   users, for example:

   ```
   1;ford
   2;smith
   3;thomson
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-trestclient-component-standard-component-esb -->
# Configuring the tRESTClient component

Last updated: 9/30/2026

## Procedure

1. Double-click the tRESTClient
   component to open its Basic settings
   view.
2. Fill the URL field with the URL of
   the REST service built in the service Job, *"http://localhost:8088/"*.
3. Fill the Relative Path
   with the *"UserInfo"*.
4. From the HTTP Method list, select
   POST.
5. Leave the rest of the settings as they are.
6. Connect tRESTClient to tLogRow using the Row > Response
   connection. Keep the default settings of the tLogRow to monitor the message exchanges.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-txmlmap-component-standard-component-esb-connect -->
# Configuring the tXMLMap component

Last updated: 9/30/2026

## Procedure

1. Connect tFixedFlowInput to tXMLMap using the Row > Main
   connection.
2. Connect tXMLMap to tRESTClient using the Row > Main
   connection, and name the output flow *request* in
   this example.
3. Double-click tXMLMap in the design
   workspace to open the Map
   Editor.
4. Right-click on the node root in the
   output table and select Create
   Sub-Element. Name the sub-element as
   *person* in the popup dialog box.
5. Right-click on the *person* node created in the
   previous step and select As loop
   element.
6. Create two sub-elements to the *person* node by
   selecting Create Sub-Element in the
   contextual menu, *id*, and *name*
   in this use case.
7. Select the *id* column from the input
   table and drop it onto the Expression
   field of the *id* node of the output
   table.
8. Select the *name* column from the
   input table and drop it onto the Expression field of the *name* node in the output table.
9. Click OK to save the settings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-saving-and-executing-job-standard-component-esb-save -->
# Saving and executing the Job

Last updated: 9/30/2026

Save the Job and press F6 to execute it. The
user information is shown in the console, including *id*,
*name*, and *company*. The name of the
user has been converted to upper case.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-body-of-response-standard-component-esb-connect -->
# Configuring the body of the response

Last updated: 9/30/2026

## Procedure

1. Connect tRESTRequest to tXMLMap using the Row > UserInfo
   connection.
2. Double-click tXMLMap in the design
   workspace to open the Map
   Editor.
3. Right-click on the root node of the
   input table and select Create
   Sub-Element. Name the sub-element as
   *person* in the popup dialog box.
4. Right-click on the *person* node created in the
   previous step and select As loop
   element.
5. Create two sub-elements to the *person* node by
   selecting Create Sub-Element in the
   contextual menu, *id* and *name*
   in this use case.
6. Click the [+] button on the top right
   to add an output and name it as *Response*.
7. Click the [+] button on the bottom
   right to add a column *body* of Document
   type for the output.
8. Right-click the node root in the
   output table and select Create
   Sub-Element. Name the sub-element as
   *person* in the popup dialog box.
9. Right-click the *person* node created in the
   previous step and select As loop
   element.
10. Create three sub-elements to the *person* node by
    selecting Create Sub-Element in the
    contextual menu, *id*, *name* and
    *company* in this use case.
11. Select the *id* column from the input
    table and drop it onto the Expression
    field of the *id* node of the output
    table.
12. Select the *name* column from the
    input table and drop it onto the Expression field of the *name* node in the output table.

    Click the Expression field of the
    *name* node in the output table,
    and click [...] in this field to show
    the Expression Builder wizard.

    In the Expression area, enter
    StringHandling.UPCASE([UserInfo.body:/root/person/name])
    to convert the name of the user to upper case. Click OK to close the wizard.

    For further information about using the Expression Builder, see [Writing code using the Expression Builder](/talend/r/en-US/8.0/studio-user-guide/writing-code-using-expression-builder).
13. In the Expression field of the
    *company* node, enter
    *"Talend"*.
14. Click OK to save the settings.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-trestrequest-component-standard-component-esb -->
# Configuring the tRESTRequest component

Last updated: 9/30/2026

## Procedure

1. Double-click tRESTRequest in the
   design workspace to display its Basic
   settings view.
2. In the REST Endpoint field, keep the
   default URI *"http://localhost:8088/"* where the
   REST-ful web service will be accessible for requests.
3. Click the [+] button to add one line
   in the REST API Mapping table.
4. Select the newly-added line and click the [...] button in the Output
   Flow column to add a schema for the output flow. Give the
   name for the schema *UserInfo* in this scenario. 

   The schema editor opens. Click the [+] button to add a new line *body*
   of Document type and click OK to save the schema.
5. Back to tRESTRequest
   Basic settings view, select POST from the list in the HTTP Verb column.
6. Fill the field in the URI Pattern
   column with *"/UserInfo"*. Keep the default settings
   of the other options.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-configuring-trestresponse-component-standard-component-esb-connect -->
# Configuring the tRESTResponse component

Last updated: 9/30/2026

## Procedure

1. Connect tXMLMap to a tRESTResponse using Row > Response
   connection.

   The schema defined in tXMLMap is
   retrieved in tRESTResponse
   automatically.
2. Select OK(200) from the Return status code list.
3. Leave the rest of the settings as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestclient-tlogrow-launching-service-standard-component-esb-save -->
# Launching the service

Last updated: 9/30/2026

Save the Job and press F6 to execute it. The
service is started.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-tmysqlinput-component-standard-component-esb-to-do -->
# Configuring the tMysqlInput component

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. Double-click tMysqlInput to
   display its Basic settings
   view:
2. From the Property Type list,
   leave Built-in and fill in the
   Host, Port, Database,
   Username and Password fields manually. If you
   centralized your connection information to the database in the
   Metadata > DB Connections node of the Repository, you can select Repository from the list and the fields
   will be automatically filled in.

   For more information about storing metadata, see [Managing metadata in Talend Studio](/talend/r/en-US/8.0/studio-user-guide/managing-metadata-in-studio).
3. Leave the Schema list as
   Built-in and click the
   [...] button next to the
   Edit schema field.
4. In the schema editor, define the schema exactly like the one of
   the tFixedFlowInput.
5. In the Table Name field, fill in
   the name of the table in which the data are stored: *users*.
6. Leave the Query Type list as
   Built-in and fill in the
   Query field with the following
   SQL query allowing to explore the database data with the URI query
   set in the tRESTRequest component: 

   "select \* from users where id >= " + globalMap.get("getUsers.from") + " and id <= " + globalMap.get("getUsers.to")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-trestrequest-component-standard-component-esb-to-do -->
# Configuring the tRESTRequest component

Last updated: 9/30/2026

## About this task

To do this, proceed as follows:

## Procedure

1. Double-click tRESTRequest in the
   design workspace to display its Basic
   settings view:
2. Fill the REST Endpoint field with
   the URI location where the REST-ful web service will be accessible
   for requests. For example, *"http://localhost:8088/users"*.
3. Click the [+] button to add one
   line in the REST API Mapping
   table.
4. Select the newly-added line and click the [...] button in the Output
   Flow column to add a schema for the output
   flow.
5. In the dialog box, name the output flow *getUsers*. A schema editor dialog box appears.
6. In the schema editor, click the [+] button twice to add two lines and set them as
   displayed in the above screenshot.
7. Click OK.
8. Back to tRESTRequest
   Basic settings view, select
   GET from the list in the
   HTTP Verb column.
9. Leave the URI Pattern column as
   is.
10. Use the corresponding link to connect to the following component: connect tRESTRequest to tFlowToIterate using Row > getUsers connection.
11. Leave the tFlowToIterate settings
    as is.
12. Connect tFlowToIterate to
    tMysqlInput using Row > Iterate connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-trestresponse-component-standard-component-esb-connect -->
# Configuring the tRESTResponse component

Last updated: 9/30/2026

## Procedure

1. Connect tXMLMap to tRESTResponse using Row > ResponseUsers
   connection.
2. The schema defined in tXMLMap is
   retrieved in tRESTResponse
   automatically. Leave the other settings as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-rest/trestrequest-trestresponse-tfixedflowinput-tmysqloutput-configuring-txmlmap-component-standard-component-esb -->
# Configuring the tXMLMap component

Last updated: 9/30/2026

## Procedure

1. Right-click tMysqlInput, hold and
   drag to tXMLMap to connect the two
   components together.
2. Double-click tXMLMap in the design
   workspace to open the Map Editor.
3. Click the [+] button on the top right
   to add an output and name it as *ResponseUsers*.
4. Click the [+] button on the bottom
   right to add two columns for the output. 

   Name the first column as *body* and
   set the Type to Document.

   Name the second column as *string*
   and set the Type to String.
5. Right-click on the root node, select
   Rename in the list and rename it
   *users*
6. Right-click on the users node and
   select Create Sub-Element to create a
   sub-element. Name the sub-element *user* in the popup
   dialog box.
7. Right-click on the *user* node created in the
   previous step and select As loop
   element.
8. Select the *id* column of the
   *row2* table to the left and drop
   it onto the *user* node of the
   *ResponseUsers* table to the
   right.
9. In the Selection dialog box, select
   the Create as attribute of target node
   option and click OK.
10. Select the *firstname* and *lastname* columns of the *row2* table to the left and drop it onto the
    *user* node of the *ResponseUsers* table to the right.
11. In the Selection dialog box, select
    the Create as sub-element of target
    node option and click OK.
12. Click the wrench icon on the top of the *ResponseUsers* table to open the setting panel.
13. Set the All in one feature as
    true, this way all XML data is
    outputted in one single flow.
14. Click OK to save the settings.
