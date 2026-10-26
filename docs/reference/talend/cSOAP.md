<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap · versión 8.0 -->
# cSOAP

Last updated: 9/30/2026

Provides integration with Apache CXF for connecting to JAX-WS
services.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cSOAP Standard properties

These properties are used to configure cSOAP running in the
Standard Job framework.

The Standard
cSOAP component belongs to the
Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Address | The service endpoint URL where the Web service is provided.  In case cSOAP is used to consume a Web service and the endpoint lookup shall use the Service Locator (the Use Service Locator  check box is selected), the URL needs to be `"locator://anyAddress/"`. |
| Type | Select which type you want to use to provide Web service. Either wsdlURL or serviceClass.  wsdlURL: Select this type to provide the Web service from a WSDL file. Choose Repository or File to provide the Web service from a Route Resource or the file system.  serviceClass: Select this type to provide the Web service from an SEI (Service Endpoint Interface) Java class. |
| WSDL File | This field appears when the wsdlURL service type is selected. If the WSDL file is from the file system, browse to or enter the path to the WSDL file. If the WSDL file is from a Route Resource, click [...] and select the one you want from the Resources tree view. The Version list appears allowing you to choose from all the versions of the Route Resource. |
| Service configuration | This option appears when wsdlURL is selected in the Type list. It allows you to configure the service endpoint information conveniently. Click [...] to open the service configuration wizard.  The WSDL field in the wizard is filled in with the WSDL file defined in the WSDL File field automatically. You can also set the WSDL file directly in the service configuration wizard in one of the following ways:   * Click Browse... to browse to or enter the path to the   WSDL file in the file system. * Click Services   to select a service under the Services. * Click Resources to select a service under the   Resources node.   After setting the WSDL file, click  to show the port(s) and operation(s) available in the Port Name and Operation boxes respectively. Select the one you want to use and click Finish. The Operation box only shows when the cSOAP component is used to consume a Web service. |
| Service Class | This field appears when the serviceClass service type is selected. Enter the name of the service class to be used to provide the Web service. |
| Dataformat | The exchange data style. POJO, PAYLOAD, RAW, or CXF\_MESSAGE.  POJOs (Plain Old Java Objects) are the Java parameters to the method being invoked on the target server.  PAYLOAD is the message payload, the contents of the soap:body.  RAW is the raw message that is received from the transport layer without SAM (Service Activity Monitor) support.  CXF\_MESSAGE is the raw message that is received from the transport layer with SAM support. |
| Use GZip Compress | Select this check box to compress the incoming messages into GZip format before sending. |
| Service Name | The service name this service is implementing. It maps to the wsdl:service@name in the format of ns:SERVICE\_NAME where ns is a namespace prefix valid at this scope. This field gets filled in automatically upon completion of the Service configuration. |
| Port Name | The endpoint name this service is implementing. It maps to the wsdl:port@name, in the format of ns:PORT\_NAME where ns is a namespace prefix valid at this scope. This field gets filled in automatically upon completion of the Service configuration. |
| Allow Streaming | This option appears when PAYLOAD is selected in the Dataformat list. Select this check box to keep the payload as a javax.xml.transform.Source object that would allow streaming over buffering. If this option is disabled, the cSOAP component will parse the incoming messages into DOM elements. |
| Operation Name | The operation name this service is implementing. It maps to the wsdl:operation@name, in the format of ns:OPERATION\_NAME where ns is a namespace prefix valid at this scope. This option appears when the cSOAP component is used consume a Web service. This field gets filled in automatically upon completion of the Service configuration. |
| Use Service Registry | This option is only available if you subscribed to Talend Enterprise ESB solutions.  Select this check box to enable the Service Registry. It provides dynamic endpoint lookup and allows services to be redirected based upon information retrieved from the registry. It works in Runtime only.  When the cSOAP component is used to provide a Web service, the service deployed in Talend Runtime will work with the Security Token Service.  When the cSOAP component is used to consume a Web service:  In the Correlation Value field, specify a correlation ID or leave this field empty. For more information, see the Use Business Correlation option.  In the Username and the Password fields, enter the authentication credentials. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  If SAML token is registered in the Service Registry, you need to specify the client's role in the Role field. You can also select the Propagate Credentials check box to make the call on behalf of an already authenticated user by propagating the existing credentials. You can enter the username and the password to authenticate with STS to propagate credentials using username and password, or provide the alias, username and the password to propagate using certificate. For more information, see the Use Authentication option.  For more information about how to set up and use the Service Registry, see [Setting up Service Registry](/talend/r/en-US/8.0/administration-center-user-guide/setting-up-esb-service-registry) and [Service Registry](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/service-registry). |
| Use Service Locator | Provides service consumers with a mechanism to discover service endpoints at runtime without specifying the physical location of the endpoint. Additionally, it allows service providers to automatically register and unregister their service endpoints at the Service Locator.  Information noteNote: For service consumers, the URL additionally needs to be set to "locator://anyAddress/" in the CXF Configuration / Address field.  The Custom Properties table appears when the Use Service Locator  check box is selected. Click  to add as many properties as needed to the table. Enter the name and the value of each property in the Property Name field and the Property Value field respectively to identify the service. For more information about Service Locator, see [Installing Service Locator](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/installing-service-locator). |
| Use Service Activity Monitor | Captures events and stores this information to facilitate in-depth analysis of service activity and track-and-trace of messages throughout a business transaction. This can be used to analyze service response times, identify traffic patterns, perform root cause analysis and more.  This feature is not supported when MESSAGE is used as the processing mode. When MESSAGE is selected in the Dataformat field, the Use Service Activity Monitor check box is disabled.  This option is also disabled when the Use Service Registry  check box is selected if you subscribed to Talend Enterprise ESB solutions. |
| Use Authentication | Select this check box to enable the authentication option. Select from Username Token, SAML Token (ESB runtime only), HTTP Basic, and HTTP Digest.  When the cSOAP component is used to produce a Web service, authentication with the Username Token, SAML token, and HTTP Basic work in runtime only. HTTP Digest is not supported. When SAML Token (ESB runtime only) is selected, cSOAP will get the SAML Token from the request header for further use in the message routing.  When the cSOAP component is used to consume a Web service, authentication with the Username Token, HTTP Basic, and HTTP Digest work in both Talend Studio and Talend Runtime. Authentication with the SAML token works in runtime only. Enter a username and a password in the corresponding fields as required. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  When SAML Token (ESB runtime only) is selected, you can either provide the user credentials to send the request or make the call on behalf of an already authenticated user by propagating the existing credentials. Select from:  -: Enter the username and the password in the corresponding fields to access the service.  Propagate using U/P: Enter the username and the password used to authenticate using STS.  Propagate using Certificate: Enter the alias and the password used to authenticate using STS.  This check box disappears when the Use Service Registry  check box is selected. |
| Use Authorization | This option is only available if you subscribed to Talend Enterprise ESB solutions. It appears when SAML Token (ESB runtime only) is selected in the Use Authentication list.  When the cSOAP component is used to provide a Web service, select this check box to enable authorization.  When the cSOAP component is used to consume a Web service, select this check box to invoke authorized call and specify the client's role in the Role field.  For more information about the management of user roles and rights, see [Managing ESB Resources and authorizations](/talend/r/en-US/8.0/administration-center-user-guide/managing-esb-resources-and-authorizations) and [Talend Identity and Access Management](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/talend-identity-and-access-management). |
| Use Business Correlation | Select this check box to enable the correlation option so that chained service calls will be grouped under the same correlation ID.  When cSOAP is used to provide a Web service:  cSOAP will extract the correlation ID from the request message.  If the request message does not contain a correlation ID, the provider will create a correlation ID automatically in the SOAP header.  When cSOAP is used to consume a Web service:  You can specify a correlation ID in the Correlation Value field using a string or a simple expression. If you leave this field empty, this value will be generated automatically at runtime. The correlation ID will be created in the custom SOAP header of the request message and passed on to the service it calls.  This check box disappears when the Use Service Registry  check box is selected or RAW is selected in the Dataformat list. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Arguments | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/cxf.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSOAP can be a start, middle, or end component in a Route. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules).   Multiple cSOAP components with the same label in a Route is not supported.  When cSOAP is used to consume a Web service, if you use the CXF\_MESSAGE data format, the request body type needs to be javax.xml.transform.Source.class, or the request body will be empty.  For simple proxy use cases, for example, from cSOAP to cProcessor to cSOAP, if you use the RAW data format, the request body will be reset. If it is printed by cProcessor, the output request body will be empty.  When cSOAP is used to consume a Web service and the data format is POJO, PAYLOAD, or CXF\_MESSAGE, if fault response is returned the message routing will stop. In this case, it is recommended to use the cErrorHandler component to catch the fault message. For more information about cErrorHandler, see [cErrorHandler](/talend/en-US/components/8.0/mediation-logs-and-errors/cerrorhandler). |

**Related concepts**  

* [Providing a Web service from a Route Resource](csoap-cprocessor-providing-web-service-from-route-resource)
* [Providing a Web service using cSOAP from a Java class](csoap-cprocessor-providing-web-service-using-csoap-from-java-class)
* [Providing a Web service using cSOAP from a WSDL file](csoap-cprocessor-providing-web-service-using-csoap-from-wsdl-file)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-providing-web-service-from-route-resource -->
# Providing a Web service from a Route Resource

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a Web service is provided from a Route Resource using a
cSOAP component.

### In this section

* [Creating a Route Resource](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-creating-route-resource)
* [Setting up a Route for the Web service](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-setting-up-route-for-web-service)
* [Configuring the cSOAP component to provide the Web Service](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-configuring-csoap-component-to-provide-web-service)
* [Checking the results](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-checking-results)

**Related reference**  

* [cSOAP](csoap "Provides integration with Apache CXF for connecting to JAX-WS services.")

**Related information**  

* [cProcessor](/talend/en-US/components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-providing-web-service-using-csoap-from-java-class -->
# Providing a Web service using cSOAP from a Java class

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a Web service is provided from a Java class file using a
cSOAP component.

### In this section

* [Creating a Java class](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-creating-java-class)
* [Setting up the Route](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-setting-up-route)
* [Configuring the cSOAP component](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-configuring-csoap-component)
* [Executing the Route to provide the service](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-executing-route-to-provide-service)

**Related reference**  

* [cSOAP](csoap "Provides integration with Apache CXF for connecting to JAX-WS services.")

**Related information**  

* [cProcessor](/talend/en-US/components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-providing-web-service-using-csoap-from-wsdl-file -->
# Providing a Web service using cSOAP from a WSDL file

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a Web service is produced by a cSOAP component using a WSDL file.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cSOAP](csoap "Provides integration with Apache CXF for connecting to JAX-WS services.")

**Related information**  

* [cProcessor](/talend/en-US/components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-checking-results -->
# Checking the results

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, the cSOAP
   component produces the Web service from an predefined Route Resource DemoServiceWsdl\_0.1 using the endpoint URL http://localhost:8000/service.endpoint.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: The service is successfully started. You can access it from a Web
   browser using the service endpoint URL followed by ?wsdl.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-configuring-csoap-component-to-provide-web-service -->
# Configuring the cSOAP component to provide the Web Service

Last updated: 9/30/2026

## About this task

In this scenario, the cProcessor
component is used only to enable the cSOAP
component to function as a service producer. Therefore, it does not need any
configuration.

## Procedure

1. Double-click the cSOAP
   component to display its Basic settings
   view in the Component tab.
2. In the Address field, type in the service
   endpoint URL for the Web service to be provided, *http://localhost:8000/service.endpoint* in this
   example.
3. From the Type list, select wsdlURl and use the Repository property type to start the Web service from the
   Route Resource that we have created.
4. In the WSDL File field, click the
   [...] button and select *DemoServiceWsdl* from the Resources tree view.
   Click OK to close the wizard.
5. Click [...] next to Service Configuration to open the service configuration
   wizard. The WSDL field has been filled in
   with the selected WSDL file. Click
   to show the available port in the Port Name box. Select the DemoServicePort port
   and click Finish to close the wizard. The
   Service Name and Port Name fields in the Basic
   settings view are filled in automatically.
6. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-creating-route-resource -->
# Creating a Route Resource

Last updated: 9/30/2026

## Procedure

1. From the Repository tree view, right-click the
   Resources node and select Create Resource from the context menu.
2. The New Route Resource wizard opens. In the Name field, type in a name for the Resource, for
   example, *DemoServiceWsdl*. Click Finish to close the wizard.
3. Browse to an existing WSDL file from the local file system and click Finish.
4. Press Ctrl+S to save your Route Resource.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-setting-up-route-for-web-service -->
# Setting up a Route for the Web service

Last updated: 9/30/2026

## About this task

This use case requires a cSOAP and a
cProcessor component.

## Procedure

1. From the Palette, expand the
   Connectivity/Services folder, and drop
   a cSOAP component onto the design
   workspace.
2. Expand the Custom folder, and drop a cProcessor component onto the design
   workspace.
3. Right-click the cSOAP
   component, select Row > Route from the contextual menu and click the
   cProcessor component.
4. Label the cSOAP component
   for better identification of its functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-configuring-csoap-component -->
# Configuring the cSOAP component

Last updated: 9/30/2026

## About this task

In this scenario, the cProcessor
component is used only to enable the cSOAP
component to function as a service producer. Therefore, it does not need any
configuration.

## Procedure

1. Double-click the cSOAP
   component to display its Basic settings
   view in the Component tab.
2. In the Address field, type in the service
   endpoint URL for the Web service to be provided, *http://192.168.0.212:8001/service.endpoint* in this
   example.
3. From the Type from, select serviceClass to start the Web service from a Java
   class.
4. In the Service Class field, specify the
   predefined bean class, *CXFdemobean* in
   this example.
5. From the Dataformat list, select
   POJO as the serviceClass service data format.
6. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-creating-java-class -->
# Creating a Java class

Last updated: 9/30/2026

## Procedure

1. From the repository tree view, expand the Code node and right click the Beans node. In the contextual menu, select Create Bean.
2. The New Bean wizard opens. In the Name field, type in a name for the bean, for
   example, *CXFdemobean*. Click Finish to close the wizard.
3. Change the class type to interface, change the return type
   to string and remove the message body.

   ```
   package beans;

   public interface CXFdemobean {
       public String helloExample(String message) ;
   }
   ```
4. Press Ctrl+S to save your bean.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-executing-route-to-provide-service -->
# Executing the Route to provide the service

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, the cSOAP
   component produces the Web service from an predefined bean beans.CXFdemobean using the endpoint URL http://192.168.0.212:8001/service.endpoint.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: The service is successfully started. You can access it from a Web
   browser using the service endpoint URL followed by ?wsdl.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-setting-up-route -->
# Setting up the Route

Last updated: 9/30/2026

## About this task

This use case requires one cSOAP
component and one cProcessor component.

## Procedure

1. From the Palette, expand the
   Connectivity/Services folder, select
   the cSOAP component and drop it onto the
   design workspace.
2. Expand the Custom folder,
   select the cProcessor component and drop it
   onto the design workspace.
3. Right-click the cSOAP
   component, select Row > Route in the contextual menu and click the
   cProcessor component.
4. Label the components for better identification of their
   functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## About this task

In this scenario, the cProcessor
component is used only to enable the cSOAP
component to function as a service producer. Therefore, it does not need any
configuration.

## Procedure

1. Double-click the cSOAP
   component to display its Basic settings
   view in the Component tab.
2. In the Address field, type in the service
   endpoint URL for the Web service to be provided, *http://192.168.0.212:8000/service.endpoint* in this
   example.
3. From the Type list, select wsdlURL to enable producing the Web service from
   a WSDL file.
4. In the Wsdl File field, browse to or type
   in the path to the WSDL file to be used.
5. Click [...] next to Service Configuration to open the service configuration
   wizard. The WSDL field has been filled in
   with the selected WSDL file. Click
   to show the available port in the Port Name box. Select the airportSoap port and
   click Finish to close the wizard. The
   Service Name and Port Name fields in the Basic
   settings view are filled in automatically.
6. From the Dataformat list, select
   PAYLOAD mode for the wsdlURL data format.
7. Press Ctrl+S to save your route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

This use case requires one cSOAP
component and one cProcessor component.

## Procedure

1. From the Palette, expand the
   Connectivity/Services folder, and drop a
   cSOAP component onto the design
   workspace.
2. Expand the Custom folder, and drop a cProcessor component onto the design
   workspace.
3. Right-click the cSOAP
   component, select Row > Route from the contextual menu and click the
   cProcessor component.
4. Label the cSOAP component for
   better identification of its functionality.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to have a look at the generated code.

   As shown in the code, the cSOAP
   component produces the Web service from an input file airport\_soap\_route.wsdl using the endpoint URL http://192.168.0.212:8000/service.endpoint.
2. Click the Run view to display it and
   click the Run button to launch the
   execution of your Route. You can also press F6 to execute it. 

   RESULT: The service is successfully started. You can access it from a Web
   browser using the service endpoint URL followed by ?wsdl.
