<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer · versión 8.0 -->
# tESBConsumer

Last updated: 9/30/2026

Calls the defined method from the invoked Web service and returns the class as
defined, based on the given parameters.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tESBConsumer Standard properties

These properties are used to configure tESBConsumer running in the Standard Job framework.

The Standard
tESBConsumer component belongs to the ESB family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Service configuration | Description of Web service bindings and configuration. The Endpoint field gets filled in automatically upon completion of the service configuration. |
| Input Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created and   stored locally for this component only. Related topic: see [Setting a Built-in schema in Jobs](/talend/r/en-US/8.0/studio-user-guide/setting-built-in-schema-in-job). * Repository: The schema already exists   and is stored in the Repository, hence can be reused. Related topic: see [Setting a repository schema in a   Job](/talend/r/en-US/8.0/studio-user-guide/setting-repository-schema-in-job). |
| Response Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created and   stored locally for this component only. Related topic: see [Setting a Built-in schema in Jobs](/talend/r/en-US/8.0/studio-user-guide/setting-built-in-schema-in-job). * Repository: The schema already exists   and is stored in the Repository, hence can be reused. Related topic: see [Setting a repository schema in a   Job](/talend/r/en-US/8.0/studio-user-guide/setting-repository-schema-in-job). |
| Fault Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created and   stored locally for this component only. Related topic: see [Setting a Built-in schema in Jobs](/talend/r/en-US/8.0/studio-user-guide/setting-built-in-schema-in-job). * Repository: The schema already exists   and is stored in the Repository, hence can be reused. Related topic: see [Setting a repository schema in a   Job](/talend/r/en-US/8.0/studio-user-guide/setting-repository-schema-in-job). |
| Use Service Registry | This option is only available if you subscribed to Talend Enterprise ESB solutions.  Select this check box to enable the Service Registry. It provides dynamic endpoint lookup and allows services to be redirected based upon information retrieved from the registry. It works in runtime only.  Enter the authentication credentials in the Username and Password field.  If SAML token is registered in the service registry, you need to specify the client's role in the Role field. You can also select the Propagate Credentials check box to make the call on behalf of an already authenticated user by propagating the existing credentials. You can enter the username and the password to authenticate via STS to propagate using username and password, or provide the alias, username and the password to propagate using certificate. For more information, see the Use Authentication option. Select the Encryption/Signature body check box to enable XML Encryption/XML Signature. For more information, see [XKMS service](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/xkms-service).  In the Correlation Value field, specify a correlation ID or leave this field empty. For more information, see the Use Business Correlation option.  For more information about how to set up and use the Service Registry, see [Setting up ESB Service Registry](/talend/r/en-US/8.0/administration-center-user-guide/setting-up-esb-service-registry) and [Service Registry](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/service-registry). |
| Use Service Locator | Maintains the availability of the service to help meet demands and service level agreements (SLAs).  This option will not show if the Use Service Registry  check box is selected. |
| Use Service Activity Monitor | Captures events and stores this information to facilitate in-depth analysis of service activity and track-and-trace of messages throughout a business transaction. This can be used to analyze service response times, identify traffic patterns, perform root cause analysis and more.  This option is disabled when the Use Service Registry  check box is selected if you subscribed to Talend Enterprise ESB solutions. |
| Use Authentication | Select this check box to enable the authentication option. Select from Basic HTTP, HTTP Digest, Username Token, and SAML Token (ESB runtime only). Enter a username and a password in the corresponding fields as required. Authentication with Basic HTTP, HTTP Digest, and Username Token work in both Talend Studio and Talend Runtime. Authentication with the SAML Token works in runtime only.  When SAML Token (ESB runtime only) is selected, you can either provide the user credentials to send the request or make the call on behalf of an already authenticated user by propagating the existing credentials. Select from:  -: Enter the username and the password in the corresponding fields to access the service.  Propagate using U/P: Enter the user name and the password used to authenticate against STS.  Propagate using Certificate: Enter the alias and the password used to authenticate against STS.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  This option will not show if the Use Service Registry  check box is selected. |
| Use Authorization | This option is only available if you subscribed to Talend Enterprise ESB solutions.  Select this check box to enable authorized call. Specify the client's role in the Role field. This option appears when SAML Token (ESB runtime only) is selected in the Use Authentication list.  For more information about the management of user roles and rights, see [Managing ESB Resources and authorization](/talend/r/en-US/8.0/administration-center-user-guide/managing-esb-resources-and-authorizations) and [Talend Identity and Access Management](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/talend-identity-and-access-management). |
| Encryption/Signature body | Select this check box to enable XML Encryption/XML Signature. For more information, see [XKMS service](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/xkms-service).  This option appears when SAML Token (ESB runtime only) is selected in the Use Authentication list. |
| Use Business Correlation | Select this check box to create a correlation ID in this component.  You can specify a correlation ID in the Correlation Value field. In this case the correlation ID will be passed on to the service it calls so that chained service calls will be grouped under this correlation ID. If you leave this field empty, this value will be generated automatically at runtime.  When this option is enabled, tESBConsumer will also extract the correlation ID from the response header and store it in the component variable for further use in the flow.  This option will be enabled automatically when the Use Service Registry  check box is selected. |
| Use GZip Compress | Select this check box to compress the incoming messages into GZip format before sending. |
| Die on error | Select this check box to kill the Job when an error occurs. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Log messages | Select this check box to log the message exchange between the service provider and the consumer. |
| Service Locator Custom Properties | This table appears when Use Service Locator  is selected. You can add as many lines as needed in the table to customize the relevant properties. Enter the name and the value of each property between double quotation marks in the Property Name field and the Property Value field respectively. |
| Service Activity Custom Properties | This table appears when Use Service Activity Monitor is selected. You can add as many lines as needed in the table to customize the relevant properties. Enter the name and the value of each property between double quotation marks in the Property Name field and the Property Value field respectively. |
| Connection time out(second) | Set a value in seconds for Web service connection time out.  This option only works in Talend Studio. To use it after the component is deployed in runtime:   1. Create a configuration file with the name    org.apache.cxf.http.conduits-<endpoint\_name>.cfg    in the <TalendRuntimePath>/container/etc/    folder. 2. Specify the url of the Web service and the    client.ConnectionTimeout parameter in    milliseconds in the configuration file. If you need to use the    Receive time out option,    specify the client.ReceiveTimeout in milliseconds    too. The url can be a full endpoint address or a    regular expression containing wild cards, for example:  ```    url = http://localhost:8040/*    client.ConnectionTimeout=10000000    client.ReceiveTimeout=20000000    ```  , in which http://localhost:8040/\* matches all URLs starting with    http://localhost:8040/. |
| Receive time out(second) | Set a value in seconds for server answer.  This option only works in Talend Studio. For how to use it after the component is deployed in runtime, see the Connection time out option. |
| Disable Chunking | Select this check box to disable encoding the payload as chunks. In general, chunking will perform better as the streaming can take place directly. But sometimes the payload is truncated with chunking enabled. If you are getting strange errors when trying to interact with a service, try turning off chunking to see if that helps. |
| Trust server with SSL/TrustStore file and TrustStore password | Select this check box to validate the server certificate to the client via an SSL protocol and fill in the corresponding fields:  TrustStore file: Enter the path (including filename) to the certificate TrustStore file that contains the list of certificates that the client trusts.  TrustStore password: Enter the password used to check the integrity of the TrustStore data. |
| Use http proxy/Proxy host, Proxy port, Proxy user, and Proxy password | Select this check box if you are using a proxy server and fill in the necessary information.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| HTTP Headers | Click [+] as many times as required to add the name-value pair(s) for HTTP headers to define the parameters of the requested HTTP operation. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  CORRELATION\_ID: the correlation ID by which chained service calls will be grouped. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  HTTP\_RESPONSE\_CODE: HTTP response status code. This is an After variable and it returns an Integer.  HTTP\_HEADERS: the set of HTTP headers from response. This is a Flow variable and it returns map object java.util.Map<String, java.util.List<?>>. Header name is represented by map key. Header values are represented by java.util.List<?>.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as an intermediate component. It requires to be linked to an output component. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to turn on or off the Use Authentication or Use HTTP proxy option dynamically at runtime. You can add two rows in the table to set both options.  Once a dynamic parameter is defined, the corresponding option becomes highlighted and unusable in the Basic settings view or Advanced settings view.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | A JDK is required for this component to operate. |

**Related concepts**  

* [Requesting airport names based on country codes](tesbconsumer-tesbproviderfault-tmap-requesting-airport-names-based-on-country-codes-standard-component-esb-this)
* [Returning Hello world response](tesbconsumer-tesbproviderrequest-tfixedflowinput-returning-hello-world-response-standard-component-esb-the)
* [Sending a message without expecting a response](tesbconsumer-tesbproviderrequest-tlogrow-tfixedflowinput-sending-message-without-expecting-response-standard-component-esb-the)
* [Using tESBConsumer with custom SOAP Headers](tesbconsumer-txmlmap-tfixedflowinput-tlogrow-using-tesbconsumer-with-custom-soap-headers-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-requesting-airport-names-based-on-country-codes-standard-component-esb-this -->
# Requesting airport names based on country codes

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario involves two Jobs, one as the data service provider and the
other as data service consumer. The former listens to the requests from the consumer via
tESBProviderRequest, matches the country code
wrapped in the request against a MySQL database table that has the country code/airport
pairs via tMap, and finally returns the correct
airport name via tESBProviderResponse or if no
matches are found, the error message via tESBProviderFault. The Consumer sends requests to the Provider and
receives the airport information or error reminders via tESBConsumer.

### In this section

* [Building the data service provider to publish a service](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-building-data-service-provider-to-publish-service-standard-component-esb-the-data)
* [Building the data service consumer to request the service](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-building-data-service-consumer-to-request-service-standard-component-esb-built)

**Related reference**  

* [tESBConsumer](tesbconsumer "Calls the defined method from the invoked Web service and returns the class as defined, based on the given parameters.")
* [tESBProviderFault](tesbproviderfault "Serves a Talend Job cycle result as a Fault message of the Web service in case of a request response communication style.")
* [tESBProviderRequest](tesbproviderrequest "Wraps Talend Job as web service.")
* [tESBProviderResponse](tesbproviderresponse "Serves a Talend Job cycle result as a response message.")

**Related information**  

* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderrequest-tfixedflowinput-returning-hello-world-response-standard-component-esb-the -->
# Returning Hello world response

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a provider Job and a consumer Job are needed. The Jobs,
which are built upon the components under the ESB/Web Services family, act as the
implementations of web services defined in the Services node of the Repository.

* On the Repository tree view, right-click the
  Services node and from the contextual menu, select
  Create Service.
* In the pop-up wizard, enter `ServiceRequest` in the
  Name field and click
  Next.
* Select the Create new WSDL option.
* Click Finish to validate this creation. The
  service opens in the design workspace.
* Right-click the port `ServiceRequestPort` in the WSDL
  skeleton and select Show properties. In the
  Address field, specify the address where you want the
  service to be published, for example,
  `http://127.0.0.1.8088/esb/provider`.
* Click the portType `ServiceRequestPortType` in the WSDL
  skeleton. Change its name to
  `TEST_ProviderJobSoapBinding`.
* Click the operation `ServiceRequestOperation` in the WSDL
  skeleton. Change its name to
  `invoke(anyType):anyType`.
* Save the WSDL file.The newly defined Web service displays under the
  Services node of the Repository
  view.
* Under the Services node, right-click `ServiceRequest
  0.1` and select Import WSDL Schemas.This option
  imports the WSDL metadata from the service into the Repository,
  under the Metadata > File XML, which
  allows you to share the operation details across services and other components.

The provider Job consists of a tESBProviderRequest, a tESBProviderResponse, a tXMLMap, and two tLogRow components.

* Drop the following components from the Palette onto the design
  workspace: a tESBProviderRequest, a tESBProviderResponse, a
  tXMLMap, and
  two tLogRow.
* In the design workspace, double-click tESBProviderRequest\_1 to
  display its Component
  view and set its Basic
  settings.

* Select Repository from the Property Type list and
  click the [...] button to choose the service, to the
  granularity of port name and operation.

* Click OK.
* Click the [...] button next to Edit schema to view its
  schema.

* Connect tESBProviderRequest\_1 to tLogRow\_1.
* Double-click tLogRow\_1 to display its Component view and set
  its Basic
  settings.

* Click the [...] button next to Edit schema and define
  the schema as follow.

* Connect tLogRow\_1 to tXMLMap\_1.
* Connect tXMLMap\_1 to tLogRow\_2 and name this row as *payload*.
* In the design workspace, double-click tXMLMap\_1 to open the
  Map
  Editor.
* On the lower right part of the map editor, click
  the plus button to add one row to the *payload* table and name this row as *payload*.
* In the Type column of this *payload* row, select Document as the data type. The
  corresponding XML root is added automatically to the top
  table on the right side which represents the output
  flow.
* In the *payload* table,
  right-click *root* to open the
  contextual menu.
* From the contextual menu, select Create Sub-Element and
  type in *response* in the popup dialog
  box.
* Right-click the *response*
  node and select As loop
  element from the contextual menu.
* Repeat this operation to create a sub-element *request* of the *root* node in the input table and
  set the *request* node as loop
  element.
* Click the *request* node in
  the input table and drop it to the Expression column in the
  row of the *response* node in the
  output table.

* Click OK
  to validate the mapping and close the map editor.
* In the design workspace, double-click tLogRow\_2 to display its
  Component
  view and set its Basic
  settings.

* Click the [...] button next to Edit schema and define
  the schema as follow.

* Connect tLogRow\_2 to tESBProviderResponse\_1.
* In the design workspace, double-click tESBProviderResponse\_1
  to open its Component
  view and set its Basic
  settings.

* Click the [...] button next to Edit schema and define
  the schema as follow.

* Save the provider Job.

The consumer Job consists of a tFixedFlowInput, a tXMLMap, a tESBConsumer, and two tLogRow components.

* Drop the following components from the Palette onto the design
  workspace: a tFixedFlowInput, a tXMLMap, a tESBConsumer, and two
  tLogRow.
* Double-click tFixedFlowInput\_1 in the design
  workspace to display its Component view and set its Basic settings.

* Click the [...] button next to Edit schema.

* Click the plus button to add a new line of string
  type and name it *payloadString*.
* Click OK.
* In the Number of
  rows field, set the number of rows as *1*.
* In the Mode area, select Use Single Table and
  input world in quotations
  into the Value
  field.
* Connect tFixedFlowInput to tXMLMap.
* Connect tXMLMap to tESBConsumer and name this row as *payload*.
* In the design workspace, double-click tXMLMap\_1 to open the
  Map
  Editor.
* In the *payload* table,
  right-click *root* to open the
  contextual menu.
* From the contextual menu, select Create Sub-Element and
  type in *request* in the popup dialog
  box.
* Right-click the *request*
  node and select As loop
  element from the contextual menu.
* Click the *payloadstring*
  node in the input table and drop it to the Expression column in the
  row of the *request* node in the output
  table.

* Click OK
  to validate the mapping and close the Map Editor.
* Start the Provider Job. In the executing log you
  can see:

  ```
  ...
  web service [endpoint: http://127.0.0.1:8088/esb/provider] published
  ...
  ```
* In the tESBConsumer\_1
  Component view, set
  its Basic
  settings.

* Click the [...] button next to the Service Configuration to
  open the editor.

* In the WSDL field, type in: *http://127.0.0.1:8088/esb/provider/?WSDL*
* Click the Refresh button to retrieve port name
  and operation name.
* Click OK.
* In the Basic
  settings of the tESBConsumer, set the
  Input Schema
  as follows:

* Set the Response
  Schema as follows:

* Set the Fault
  Schema as follows:

* Connect tESBConsumer\_1 to tLogRow\_1 and tLogRow\_2.
* In the design workspace, double-click tLogRow\_1 to display its
  Component
  view and set its Basic
  settings.

* Click the [...] button next to Edit Schema and define
  the schema as follow.

* In the Job Design, double-click tLogRow\_2 to display its
  Component
  view and set its Basic
  settings.

* Click the [...] button next to Edit Schema and define
  the schema as follow:

* Save the consumer Job.
* Run the provider Job. In the execution log you
  will see:

  2011-04-21
  15:28:26.874:INFO::jetty-7.2.2.v20101205

  2011-04-21 15:28:27.108:INFO::Started

  SelectChannelConnector@127.0.0.1:8088

  web service [endpoint:
  http://127.0.0.1:8088/esb/provider] published
* Run the consumer Job. In the execution log of
  the Job you will see:

  ```
  Starting job CallProvider at 15:29 21/04/2011.

  [statistics] connecting to socket on port 3690
  [statistics] connected
  TEST_ProviderJob
  TEST_ProviderJobSoapBingding
  |
  {http://talend.org/esb/service/job}TEST_ProviderJob
  {http://talend.org/esb/service/job}TEST_ProviderJobSoapBinding
  invoke
  [tLogRow_2] payload: <?xml version="1.0" encoding="UTF-8"?>
  <response xmlns="http://talend.org/esb/service/job">Hello, world!</response>
  [statistics] disconnected
  Job ConsumerJob ended at 15:29 21/04/2011. [exit code=0]
  ```
* In the provider's log you will see the trace
  log:

  ```
  [tLogRow_1] payload: <?xml version="1.0" encoding="UTF-8"?>
  <request>world</request>
  ### world
  [tLogRow_2] content: world
  [tLogRow_3] payload: <?xml version="1.0" encoding="UTF-8"?>
  <response xmlns="http://talend.org/esb/service/job">Hello, world!</response>
  web service [endpoint: http://127.0.0.1:8088/esb/provider] unpublished
  [statistics] disconnected
  Job ProviderJob ended at 15:29 21/04/2011. [exit code=0]
  ```

**Related reference**  

* [tESBConsumer](tesbconsumer "Calls the defined method from the invoked Web service and returns the class as defined, based on the given parameters.")
* [tESBProviderRequest](tesbproviderrequest "Wraps Talend Job as web service.")
* [tESBProviderResponse](tesbproviderresponse "Serves a Talend Job cycle result as a response message.")

**Related information**  

* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderrequest-tlogrow-tfixedflowinput-sending-message-without-expecting-response-standard-component-esb-the -->
# Sending a message without expecting a response

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a provider Job and a consumer Job are needed. The Jobs,
which are built upon the components under the ESB/Web Services family, act as the
implementations of web services defined in the Services node of the Repository.

* On the Repository tree view, right-click the
  Services node and from the contextual menu, select
  Create Service.
* In the pop-up wizard, enter `ServiceRequest` in the
  Name field and click Next.
* Select the Create new WSDL option.
* Click Finish to validate this creation. The service opens in the
  design workspace.
* Right-click the port `ServiceRequestPort` in the WSDL skeleton and
  select Show properties. In the Address
  field, specify the address where you want the service to be published, for example,
  `http://127.0.0.1.8088/esb/provider`.
* Click the portType `ServiceRequestPortType` in the WSDL skeleton.
  Change its name to `TEST_ProviderJobSoapBinding`.
* Click the operation `ServiceRequestOperation` in the WSDL
  skeleton. Change its name to `invoke(anyType):anyType`.
* Save the WSDL file.The newly defined Web service displays under the
  Services node of the Repository view.
* Under the Services node, right-click `ServiceRequest
  0.1` and select Import WSDL Schemas.This option
  imports the WSDL metadata from the service into the Repository,
  under the Metadata > File XML, which
  allows you to share the operation details across services and other components.

The provider Job consists of a tESBProviderRequest, a tXMLMap, and two
tLogRow components.

* Drop the following components from the Palette onto the design workspace: a tESBProviderRequest, a tXMLMap, and
  two tLogRow.
* Double-click tESBProviderRequest\_1
  in the design workspace to display its Component
  view and set its Basic settings.

* Select Repository from the
  Property Type list and click the [...] button
  to choose the service, to the granularity of port name and operation.

* Click OK.

* Click the [...] button next to Edit
  schema to view the schema of tESBProviderRequest\_1.

* Click OK.
* Connect tESBProviderRequest\_1 to
  tLogRow\_1.
* Double-click tLogRow\_1 in the
  design workspace to display its Component view and
  set its Basic settings.

* Click the [...] button next to Edit
  schema. and define the schema as follow.

* Connect tLogRow\_1 to tXMLMap\_1.
* Connect tXMLMap\_1 to tLogRow\_2 and name this row as *payload*.
* In the design workspace, double-click tXMLMap\_1 to open the Map
  Editor.
* On the lower right part of the map editor, click the plus button to add
  one row to the *payload* table and name this row as *payload*.
* In the Type column of this *payload* row, select Document
  as the data type. The corresponding XML root is added automatically to the top table on
  the right side which represents the output flow.
* In the *payload* table, right-click *root* to open the contextual menu.
* From the contextual menu, select Create
  Sub-Element and type in *response* in the popup dialog
  box.
* Right-click the *response* node and select
  As loop element from the contextual menu.
* Repeat this operation to create a sub-element *request* of the *root* node in the input table and set the *request* node as loop element.
* Click the *request* node in the input table and drop
  it to the Expression column in the row of the *response* node in the output table.

* Click OK to validate the mapping
  and close the map editor.
* Double-click tLogRow\_2 in the
  design workspace to display its Component view and
  set its Basic settings.

* Click the [...] button next to Edit
  Schema and define the schema as follow.

* Save the Job.

The consumer Job consists of a tFixedFlowInput, a tXMLMap, a tESBConsumer, and two tLogRow
components.

* Drop the following components from the Palette onto the design workspace: a tFixedFlowInput, a tXMLMap, a
  tESBConsumer, and two tLogRow.
* Double-click tFixedFlowInput\_1 in
  the design workspace to display its Component view
  and set its Basic settings.

* Edit the schema of the tFixedFlowInput\_1 component.

* Click the plus button to add a new line of string type and name it *payloadString*.
* Click OK.
* In the Number of rows field, set
  the number of rows as *1*.
* In the Mode area, select
  Use Single Table and input world in quotations into the Value field.
* Connect tFixedFlowInput\_1 to
  tXMLMap\_1.
* Connect tXMLMap\_1 to tESBConsumer\_1 and name this row as *payload*.
* In the design workspace, double-click tXMLMap\_1 to open the Map
  Editor.
* In the output table, right-click the *root* node to
  open the contextual menu.
* From the contextual menu, select Create
  Sub-Element and type in *request* in the popup dialog
  box.
* Right-click the *request* node and select As loop element from the contextual menu.
* Click the *payloadstring* node in the input table
  and drop it to the Expression column in the row of
  the *request* node in the output table.

* Click OK to validate the mapping
  and close the Map Editor.
* Start the Provider Job. In the executing log you can see:

  ```
  ...
  web service [endpoint: http://127.0.0.1:8088/esb/provider] published
  ...
  ```
* In the tESBConsumer\_1
  Component view, set its Basic settings.

* Click the [...] button next to the Service
  Configuration to open the editor.

* In the WSDL field, type in: *http://127.0.0.1:8088/esb/provider?WSDL*.
* Click the Refresh button to retrieve port name and operation name.
* Click OK.
* In the Basic settings of the
  tESBConsumer, set the Input Schema as follow:

* Set the Response Schema as
  follow:

* Set the Fault Schema as
  follow:

* Connect tESBConsumer\_1 to
  tLogRow\_1 and tLogRow\_2.
* In the design workspace, double-click the tLogRow\_1 component to display its Component view and set its Basic
  settings.

* Click the [...] button next to Edit
  Schema and define the schema as follow:

* In the Job Design, double-click tLogRow\_2 to display its Component
  view and set its Basic settings.

* Click the [...] button next to Edit
  Schema and define the schema as follow.

* Save the Job.
* Run the provider Job. In the execution log you will see:

  INFO: Setting the server's publish address to be
  http://127.0.0.1:8088/esb/provider

  2011-04-21 14:14:36.793:INFO::jetty-7.2.2.v20101205

  2011-04-21 14:14:37.856:INFO::Started

  SelectChannelConnector@127.0.0.1:8088

  web service [endpoint: http://127.0.0.1:8088/esb/provider] published
* Run the consumer Job. In the execution log of the Job you will see:

  ```
  Starting job CallProvider at 14:15 21/04/2011.

  [statistics] connecting to socket on port 3942
  [statistics] connected
  TEST_ESBProvider2
  TEST_ESBProvider2SoapBingding
  |
  [tLogRow_2] payloadString: <request>world</request>
  {http://talend.org/esb/service/job}TEST_ESBProvider2
  {http://talend.org/esb/service/job}TEST_ESBProvider2SoapBinding
  invoke
  [tLogRow_1] payload: null
  [statistics] disconnected
  Job CallProvider2 ended at 14:16 21/04/2011. [exit code=0]
  ```
* In the provider's log you will see the trace log:

  ```
  web service [endpoint: http://127.0.0.1:8088/esb/provider]
  published
  [tLogRow_1] payload: <?xml version="1.0" encoding="UTF-8"?>
  <request>world</request>
  ### world
  [tLogRow_2] content: world
  [tLogRow_3] payload: <?xml version="1.0" encoding="UTF-8"?>
  <response xmlns="http://talend.org/esb/service/job">Hello, world!</response>
  web service [endpoint: http://127.0.0.1:8088/esb/provider] unpublished
  [statistics] disconnected
  Job ESBProvider2 ended at 14:16 21/04/2011. [exit code=0]
  ```

**Related reference**  

* [tESBConsumer](tesbconsumer "Calls the defined method from the invoked Web service and returns the class as defined, based on the given parameters.")
* [tESBProviderRequest](tesbproviderrequest "Wraps Talend Job as web service.")

**Related information**  

* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-using-tesbconsumer-with-custom-soap-headers-standard-component-this -->
# Using tESBConsumer with custom SOAP Headers

Last updated: 9/30/2026

This scenario is similar to the previous one. It describes a Job that uses a
tESBConsumer component to retrieve a valid email
address with custom SOAP headers in the request message.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-components-standard-component-the)
* [Executing the Job](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-executing-job-standard-component-click)

**Related reference**  

* [tESBConsumer](tesbconsumer "Calls the defined method from the invoked Web service and returns the class as defined, based on the given parameters.")

**Related information**  

* [tXMLMap](/talend/en-US/components/8.0/txmlmap/txmlmap)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-building-data-service-consumer-to-request-service-standard-component-esb-built -->
# Building the data service consumer to request the service

Last updated: 9/30/2026

Built upon tESBConsumer, the consumer Job sends
two requests that contain the country codes to the Web service for the relevant
airport names. If wrong country code is wrapped in the request, the error message
will be returned. The country codes and the MySQL database records are as
follows:

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-dropping-and-linking-components-standard-component-esb-drop)
* [Configuring the components](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-configuring-components-standard-component-esb)
* [Executing the Job](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-executing-job-standard-component-esb-press)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-building-data-service-provider-to-publish-service-standard-component-esb-the-data -->
# Building the data service provider to publish a service

Last updated: 9/30/2026

From the Services node of the Repository tree
view, you are able to define the Web service by creating a WSDL file or by importing an
existing WSDL file.

In this scenario, we will create a new WSDL file to define the airport Web service.

### In this section

* [Defining the Web service](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-defining-the-web-service.dita)
* [Assigning a Job to the defined service](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-assigning-job-to-defined-service-standard-component-esb)
* [Adding components to arrange the data flow](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-adding-components-to-arrange-data-flow-standard-component-esb-drop)
* [Configuring how requests are processed](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-configuring-how-requests-are-processed-standard-component-esb)
* [Publishing the service to listen to requests](/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-publishing-service-to-listen-to-requests-standard-component-esb-press)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-components-standard-component-the -->
# Configuring the components

Last updated: 9/30/2026

The tLogRow components will monitor the exchanges
from the response and fault messages and does not need any configuration. Press
Ctrl+S to save your Job.

### In this section

* [Configuring the tESBConsumer component](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-tesbconsumer-component-standard-component-in-this)
* [Configuring the tFixedFlowInput components](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-tfixedflowinput-components-standard-component)
* [Configuring the tXMLMap components in the input flow](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-txmlmap-components-in-input-flow-standard-component-data)
* [Configuring the tMap component](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-tmap-component-standard-component-in)
* [Configuring the tXMLMap component in the output flow](/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-txmlmap-component-in-output-flow-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: a tESBConsumer, a tMap, two
   tFixedFlowInput, three tXMLMap, and two tLogRow.
2. Connect each of the tFixedFlowInput with
   a tXMLMap using the Row > Main
   connection.
3. Right-click the first tXMLMap, select
   Row > \*New
   Output\* (Main) from the contextual menu and click tMap. Enter *payload* in the
   popup dialog box to name this row.

   Repeat this operation to connect another tXMLMap to tMap and name
   the output row *header*.
4. Right-click the tMap component, select
   Row > \*New
   Output\* (Main) from the contextual menu and click the
   tESBConsumer component. Enter
   *request* in the popup dialog box to name this row
   and accept the propagation that prompts you to get the schema from the
   tESBConsumer component.
5. Right-click the tESBConsumer component,
   select Row > Response from the contextual menu and click the third
   tXMLMap component.
6. Right-click the third tXMLMap component,
   select Row > \*New
   Output\* (Main) from the contextual menu and click one of the
   tLogRow components. Enter
   *response* in the popup dialog box to name this
   row.
7. Right-click the tESBConsumer component
   again, select Row > Fault from the contextual menu and click the
   other tLogRow component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-executing-job-standard-component-click -->
# Executing the Job

Last updated: 9/30/2026

Click the Run view to display it and click the
Run button to launch the execution of your Job.
You can also press F6 to execute it.

As shown in the execution log, the email address nomatter@gmail.com is
returned as false. The input and output SOAP messages in XML is also
shown in the console. The SOAP header is sent with the request to the
service.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-configuring-components-standard-component-esb -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFileInputDelimited to
   open its Basic settings view.
2. In the File name/stream field, enter
   the context variable for the file that has the country codes, *context.filepath*.
3. Click the [...] button to open the
   schema editor.
4. Click the [+] button to add a column,
   *country\_code*, for example, with
   the type of string.

   Click OK to close the editor.
5. Double-click tXMLMap to open its Map
   editor.
6. In the *request* table of the output
   flow side, right-click the column name *payload* and from the contextual menu, select Import from Repository. Then the Metadata wizard is opened. 

   Select the schema of the request message and click OK to validate this selection. In this
   example, the schema is *getAirportInformationByISOCountryCode*.
7. Drop the *country\_code* column in the
   main flow onto the Expression area next
   to the *tns:CountryAbbreviation* node
   in the *request* output flow. 

   Click OK to close the editor and
   validate this configuration.
8. Double-click tESBConsumer to open its
   service configuration wizard:
9. Click the Services button
   and select the `airport` service. The Port name and Operation are automatically filled up once the WSDL file is
   selected.

   Click OK to close the
   wizard.
10. Double-click response to open its
    Basic settings view:
11. Select Vertical (each row is a key/value
    list) and then Print
    label for a better view of the results.

    Do the same to the other tLogRow,
    fault\_message.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-dropping-and-linking-components-standard-component-esb-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop a tFileInputDelimited, a
   tXMLMap, a tESBConsumer and two tLogRow from the Palette to the workspace.
2. Rename one tLogRow as response and the other as fault\_message.
3. Link tFileInputDelimited to tXMLMap using a Row > Main
   connection.
4. Link tXMLMap to tESBConsumer using a Row > \*New
   Output\*(Main) connection.

   In the new Output name pop-up window,
   enter the output table name, for example *request*.

   Click OK in the pop-up window that
   asks whether to get the schema of the target component.
5. Link tESBConsumer to response using the Row > Response
   connection.
6. Link tESBConsumer to fault\_message using the Row > Fault
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-executing-job-standard-component-esb-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl +S to save the Job.
2. Press F6 to run this Job.

   As shown above, two messages are returned, one giving the airport name
   that matches the country code *CN* and
   the other giving the error details caused by the country code *CC*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-adding-components-to-arrange-data-flow-standard-component-esb-drop -->
# Adding components to arrange the data flow

Last updated: 9/30/2026

## Procedure

1. Drop tXMLMap and tMysqlInput from the Palette to the workspace.
2. Link tESBProviderRequest to tXMLMap using a Row > Main
   connection.
3. Link tMysqlInput to tXMLMap using a Row > Main
   connection.
4. Link tXMLMap to tESBProviderResponse using a Row > \*New
   Output\*(Main) connection.

   In the new Output name pop-up window,
   enter the output table name, *airport\_response*.

   Click OK in the pop-up window that
   asks whether to get the schema of the target component.
5. Link tXMLMap to tESBProviderFault using a Row > \*New
   Output\*(Main) connection.

   In the new Output name pop-up window,
   enter the output table name, *fault\_message*.

   Click OK in the pop-up window that
   asks whether to get the schema of the target component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-assigning-job-to-defined-service-standard-component-esb -->
# Assigning a Job to the defined service

Last updated: 9/30/2026

## Procedure

1. Right-click *getAirportInformationByISOCountryCode* under the Web
   service *airport* and from the
   contextual menu, select Assign Job.
2. In the Operation Choice window,
   select Create a new Job and Assign it to this
   Service Operation.
3. Click Next to open the Job
   description window. The Job name *airportSoap\_getAirportInformationByISOCountryCode* is
   automatically filled in.
4. Click Finish to create the Job and
   open it in the workspace. Three components are already available.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-configuring-how-requests-are-processed-standard-component-esb -->
# Configuring how requests are processed

Last updated: 9/30/2026

## Procedure

1. Double-click tMysqlInput to display
   its Basic settings view.
2. Fill up the basic settings for the Mysql connection and database
   table.

   Click the [...] button to open the
   schema editor.
3. Click the [+] button to add two
   columns, *id* and *name*, with the type of string.

   Click OK to close the editor.

   Click Guess Query to retrieve the SQL
   query.
4. Double-click tXMLMap to open its
   mapper.
5. In the main : row1 table of the input
   flow side (left), right-click the column name *payload* and from the contextual menu, select Import from Repository. Then the Metadata wizard is opened. 

   Select the schema of the request message and click OK to validate this selection. In this
   example, the schema is *getAirportInformationByISOCountryCode*.
6. Do the same to import the hierarchical schemas for the response/fault
   messages (right). In this example, these schemas are *getAirportInformationByISOCountryCodeResponse* and
   *getAirportInformationByISOCountryCodeFault*
   respectively.
7. Then to create the join to the lookup data, drop the *CountryAbbrviation* node from the main flow
   onto the *id* column of the lookup
   flow.
8. On the lookup flow table, click the wrench icon on the upper right
   corner to open the setting panel.

   Set Lookup Model as Reload at each row, Match Model as All
   matches and Join Model
   as Inner join.
9. On the *airport\_response* output flow
   table, click the wrench icon on the upper right corner to open the
   setting panel.

   Set the All in one option as
   true. This ensures that only one
   response is returned for each request if multiple airport matches are
   found in the database.
10. On the *fault\_message* output flow
    table, click the wrench icon on the upper right corner to open the
    setting panel.

    Set the Catch Lookup Inner Join
    Reject option as true to
    monitor the mismatches between the country code in the request and the
    records in the database table. Once such a situation occurs, a fault
    message will be generated by tESBConsumer and outputted via its Row > Fault
    flow.

    Information noteNote:

    The Row > Fault flow of tESBConsumer has a predefined schema in which the
    *faultString* column is filled
    with the content of the field Fault
    title of tESBProviderFault.
11. Drop the *name* column in the lookup
    flow onto the Expression area next to
    the *tns:getAirportInformationByISOCountryCodeResult* node in
    the *airport\_response* output flow. 

    Drop the *tns:CountryAbbreviation*
    node in the main flow onto the Expression area next to the *tns:getAirportInformationByISOCountryCodeFaultString*
    node in the *fault\_message* output
    flow. This way, the incorrect country code in the request will be shown
    in the *faultDetail* column of the
    Row > Fault flow of tESBConsumer.

    Click OK to close the editor and
    validate this configuration.
12. Double-click tESBProviderFault to
    display its Basic settings view:
13. In the field Fault title, enter the
    context variable *context.fault\_message*.

    For how to define context variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-defining-the-web-service.dita -->
# Defining the Web service

Last updated: 9/30/2026

## Procedure

1. On the Repository tree view, right-click the
   Services node and from the contextual menu,
   select Create Service.
2. In the pop-up wizard, enter `airport` in the
   Name field and click Next.
3. Select the Create new WSDL option.
4. Click Finish to validate this creation. 

   The service opens in the design workspace.
5. Right-click the port `airportPort` in the WSDL skeleton and
   select Show properties. In the Address
   field, specify the address where you want the service to be published, for example,
   `http://localhost:8200/airport.service`.
6. Click the portType `airportPortType` in the WSDL skeleton.
   Change its name to `airportSoap`.
7. Click the operation `airportOperation` in the WSDL skeleton.
   Change its name to
   `getAirportInformationByISOCountryCode`.
8. Right-click the `getAirportInformationByISOCountryCode`
   operation and select Add Fault to add the fault element to the
   operation.
9. Save the WSDL file.

   The newly defined Web service displays under the Services
   node of the Repository view.
10. Under the Services node, right-click `airport
    0.1` and select Import WSDL Schemas.

    This option imports the WSDL metadata from the service into the
    Repository, under the Metadata >
    File XML, which allows you to share the operation details
    across services and other components.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-tesbproviderfault-tmap-publishing-service-to-listen-to-requests-standard-component-esb-press -->
# Publishing the service to listen to requests

Last updated: 9/30/2026

## Procedure

1. Press Ctrl +S to save the Job.
2. Press F6 to run this Job.

## Results

The data service is published and will listen to all the requests until you
click the Kill button to stop it as by default,
the Keep listening option of tESBProviderRequest is selected automatically.

Now is the time to configure the consumer Job that interacts with the data
service.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-tesbconsumer-component-standard-component-in-this -->
# Configuring the tESBConsumer component

Last updated: 9/30/2026

## About this task

In this scenario, a public web service which is available at <http://www.webservicex.net/ValidateEmail.asmx> will be called by the
tESBConsumer component to returns true or
false for an email address. You can view the WSDL definition of the service at
<http://www.webservicex.net/ValidateEmail.asmx?WSDL> for the service
description.

## Procedure

1. In the design workspace, double-click the tESBConsumer component to open its Basic settings view in the Component tab.
2. Click the [...] button next to Service configuration.
3. In the dialog box that appears, type in:
   *http://www.webservicex.net/ValidateEmail.asmx?WSDL*
   in the WSDL field and click the refresh
   button to retrieve port name and operation name. In the Port Name list, select the port you want to use,
   *ValidateEmailSoap* in this example. Click OK to validate your settings and close the dialog
   box.

   Select the Populate schema to repository on
   finish to retrieve the schema from the WSDL definition, which
   will be used by the tFixedFlowInput
   component. This option is only available to users of *Talend Studio* with ESB. If you don't have this option,
   please ignore it. The schema can be created manually in the tFixedFlowInput component, which will be shown
   later.

   Click Finish to validate your settings
   and close the dialog box.
4. In the Advanced settings view, select the
   Log messages check box to log the
   content of the messages.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-tfixedflowinput-components-standard-component -->
# Configuring the tFixedFlowInput components

Last updated: 9/30/2026

## Procedure

1. Double-click the first tFixedFlowInput
   component to open its Basic settings view
   in the Component tab.
2. For users of *Talend Studio* with
   ESB who have retrieved the schema from the service WSDL definition in the
   configuration of the tESBConsumer
   component, select Repository from the
   Schema list. Then click the [...] of the next field to show the Repository Content dialog box. Select the
   metadata under the *IsValidEmail* node to use it as the
   schema of the input message. Click OK to
   close the dialog box.

   For users of *Talend Studio*
   without ESB, please go to the next step.
3. For users of *Talend Studio*
   without ESB, the schema need to be created manually. Select Built-In from the Schema list. 

   Click the [...] button next to Edit Schema. In the schema dialog box, click the
   [+] button to add a new line of
   String type and name it
   *Email*. Click OK to
   close the dialog box.
4. In the Number of rows field, set the
   number of rows as *1*.
5. In the Mode area, select Use Single Table and enter
   "nomatter@gmail.com" into the Value field, which is the payload of the request
   message.
6. Configure the second tFixedFlowInput as
   the first one, except for its schema.

   Add two rows of String type to the schema
   and name them *id* and
   *company* respectively.

   Give the value *Hello world!* to
   *id* and *Talend* to
   *company*, which are the headers of the request
   message.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-tmap-component-standard-component-in -->
# Configuring the tMap component

Last updated: 9/30/2026

## Procedure

1. In the design workspace, double-click tMap to open the Map
   Editor.
2. On the lower right part of the map editor, click [+] to add two rows of Document type to the
   output table and name them *payload* and
   *headers* respectively.
3. Click the *payload* node in the input table and drop it
   to the Expression column in the row of the
   *payload* node in the output table.
4. Click the *header* node in the input table and drop it
   to the Expression column in the row of the
   *headers* node in the output table.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-txmlmap-component-in-output-flow-standard-component-the -->
# Configuring the tXMLMap component in the output flow

Last updated: 9/30/2026

## About this task

The tXMLMap in the output flow will convert
the response message from the XML format to the row/column structure.

## Procedure

1. In the design workspace, double-click the tXMLMap component in the output flow to open the Map Editor.
2. In the input table, right-click the root node and select Rename from the contextual menu. Enter
   *IsValidEmailResponse* in the dialog box that
   appears.
3. Right-click the *IsValidEmailResponse* node and select
   Set A Namespace from the contextual
   menu. Enter *http://www.webservicex.net* in the dialog
   box that appears.
4. Right-click the *IsValidEmailResponse* node again and
   select Create Sub-Element from the
   contextual menu. Enter *IsValidEmailResult* in the dialog
   box that appears.
5. Right-click the *IsValidEmailResult* node and select
   As loop element from the contextual
   menu.
6. On the lower right part of the map editor, click [+] to add a row of String type to the output
   table and name it *response*.
7. Click the *IsValidEmailResult* node in the input table
   and drop it to the Expression column in the
   row of the *response* node in the output table.
8. Click OK to validate the mapping and
   close the Map Editor.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/esb-soap/tesbconsumer-txmlmap-tfixedflowinput-tlogrow-configuring-txmlmap-components-in-input-flow-standard-component-data -->
# Configuring the tXMLMap components in the input flow

Last updated: 9/30/2026

## About this task

Talend
 data
integration uses schemas based on rows and columns since it has roots in
relational data warehouse integration. But SOAP messages uses the XML format.
XML is hierarchical and supports richer structure than rows or columns. So we
need the tXMLMap to convert from the relational
row/column structure to the schema expected by the SOAP service.

## Procedure

1. In the design workspace, double-click the first tXMLMap component to open the Map
   Editor.
2. In the output table, right-click the root node and select Rename from the contextual menu. Enter
   *IsValidEmail* in the dialog box that appears.
3. Right-click the *IsValidEmail* node and select
   Set A Namespace from the contextual
   menu. Enter *http://www.webservicex.net* in the dialog
   box that appears.
4. Right-click the *IsValidEmail* node again and select
   Create Sub-Element from the contextual
   menu. Enter *Email* in the dialog box that
   appears.
5. Right-click the *Email* node and select As loop element from the contextual menu.
6. Click the *Email* node in the input table and drop it
   to the Expression column in the row of the
   *Email* node in the output table.
7. Click OK to validate the mapping and
   close the Map Editor.
8. Configure the other tXMLMap in the same
   way. Add a row of Document type to the output table and name it
   *header*. Create two sub-elements to it,
   *id* and *company*. Map the
   *id* and the *company* nodes in
   the input table to the corresponding nodes in the output table.
