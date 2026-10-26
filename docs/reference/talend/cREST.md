<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest · versión 8.0 -->
# cREST

Last updated: 9/30/2026

Provides integration with Apache CXF for connecting to JAX-RS
services.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cREST Standard properties

These properties are used to configure cREST running in the Standard Job framework.

The Standard
cREST component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| API Definition / Definition | Select the way the API definition will be set.   * Built-In: The API definition will be set locally   for this component. You need to specify the values for all related   connection properties manually. * Repository: The API definition stored centrally in Repository > REST API Definitions will be reused by this component.  You need to click the [...] button next to it and   in the pop-up Repository Content dialog box, select   the API definition to be reused, and all related properties will be   automatically filled in.   If you have installed the R2023-05 Talend Studio Monthly update or a later one delivered by Talend, you can drag and drop a REST API Definition from the Metadata node of the Repository tree view to the design workspace to create a cREST component. |
| Endpoint | Fill this field with the service path where the REST service is provided. For Data Service deployments in Talend Runtime Container (ESB Runtime), do not include hostname:port in this field.  The default endpoint value for a new component is "/restservice/v1". This value is meant as an example. Replace it with your own path value. You can define the endpoint path using context variables. |
| Type | Select which type you want to use to provide the REST service. Either Manual or resourceClass.  Manual: Determine the REST API mapping manually in the table if cREST is used as a service provider, or set HTTP Method and other parameters if the component is used as a service consumer.  resourceClass: Select this type to provide the resource class which you want to export as the REST service. |
| REST API Mapping | This table appears when the Manual service type is selected and cREST is used as a service provider.  Click [+] under the table to add as many rows as needed to specify the HTTP request:  Output Flow: Specify the name of an output flow.  HTTP Verb: Select a HTTP method from GET, POST, PUT, DELETE, OPTIONS, HEAD, and PATCH in the list.  URI pattern: Fill this field with the REST URI that describes the resource.  Consumes: Select the format type of the consume content that the component will use from XML or JSON, XML, JSON, Form, Multipart, and Any when HTTP Verb is POST, PUT, or PATCH.  Produces: Select the format type of the produce content that the component will use from XML or JSON, XML, JSON, HTML, Any when HTTP Verb is GET, POST, PUT, DELETE, or PATCH.  Bean class: Set the bean class when the HTTP Verb is POST, PUT, or PATCH and the consume content format is XML or JSON, XML or JSON. |
| Resource Class | This field appears when the resourceClass service type is selected. Enter the name of the resource class which you want to export as the REST service. |
| Operation | This field appears when the resourceClass service type is selected and cREST is used as the service consumer. Enter the name of the operation. |
| Relative Path | This field appears when the Manual service type is selected and cREST is used as the service consumer. Enter the relative path of the REST server to be invoked. |
| HTTP Method | This option appears when the Manual service type is selected and cREST is used as the service consumer. Select a HTTP method from GET, POST, PUT, DELETE, PATCH, HEAD, and OPTIONS in the list. Information noteWarning: When using the POST method to create an object, by default, the created object ID will not be get back from the header. By default, the cREST filters any header except system headers. To get the created object ID, you need to set javax.ws.rs.core.Response as the response class. |
| Content Type | This option appears when the Manual service type is selected and cREST is used as the service consumer.  Select XML, JSON, or FORM according to the media type of the content to be uploaded to the server end. This list appears only when you select the POST, PUT, or PATCH in the HTTP Method list. |
| Accept Type | This field appears when the Manual service type is selected and cREST is used as the service consumer.  Select the media type the client end is prepared to accept for the response from the server end. Available options are XML, JSON, and ANY. When ANY is selected, the response message can be of any type and will be transformed into a string. This list does not appear when you select the DELETE method. |
| Response Class | This field appears when the Manual service type is selected and the cREST is used as the service consumer. Enter the name of the response class. |
| Skip incoming data unmarshalling | Select this check box to skip the unmarshalling of the server response data. This option is used when the server already provides the data that the Route can work on, and the need for type conversion can be avoided. |
| Use Service Locator | Select this check box to enable the Service Locator. Specify the service namespace and the service name in the corresponding fields. |
| Enable the Service Activity Monitoring | Select this check box to enable the Service Activity Monitor.  Note that this option works in Runtime only. When running the Route in Talend Studio, it is recommended to clear this check box. Otherwise warnings will be thrown in the execution console. |
| Security | Select this check box to enable the security option. Select the security scheme from:   * HTTP Basic: The simplest technique for enforcing access controls to web resources using standard fields in the HTTP header. * JWT Bearer Token: The open and standardized method   for storing and exchanging data in JSON format. * SAML Token (Runtime Only): An XML-based,   open-standard data format for exchanging authentication and authorization   data between an identity provider and a service provider. * Open ID Connect: An extension for OAuth2 which allows   Clients to verify the identity of the End-User based on the authentication   performed by an Authorization Server, as well as to obtain basic profile   information about the End-User in an interoperable and REST-like manner. For   more information, see [Talend Identity and Access Management](/talend/r/en-US/8.0/esb-infra-services-configuration-guide/talend-identity-and-access-management) and [Managing ESB Resources and authorizations](/talend/r/en-US/8.0/administration-center-user-guide/managing-esb-resources-and-authorizations).   When the cREST component is used as consumer, enter a username and a password in the corresponding fields as required. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| JWT configuration | JWT configuration options appear when JWT Bearer Token is selected in the Security list. In the Keystore Type list, select:  * Java Keystore (\*.jks) to provide a local Java   keystore file, * PKCS12 Keystore (\*.p12, \*.pfx) to provide a local   keystore file in PKCS12 format, * JSON Web Key Sets (JWKS) to provide the URL of   the online key sets.  For the Java Keystore (\*.jks) or PKCS12 Keystore (\*.p12, \*.pfx) keystore type, you need to enter the location of the keystore file and the associated password in the Keystore File and Keystore Password field respectively. You can also set the Keystore Alias and Audience as needed.  For the JSON Web Key Sets (JWKS) keystore type, you need to specify the URL of the online key sets in the JWKS URL field. You can also set the Audience as needed. |
| Use Authorization | This option is only available if you subscribed to Talend Enterprise ESB solutions. It appears when SAML Token (Runtime Only) is selected in the Security list.  When the cREST component is used as the service provider, select this check box to enable authorization.  When the cREST component is used as the service consumer, select this check box to invoke authorized call and specify the client's role in the Role field. |
| Use Business Correlation | Select this check box to create a correlation ID in this component.  You can specify a correlation ID in the Correlation Value field. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Log messages | Select this check box to log the message exchanges in the Route. |
| Expose OpenAPI documentation | Select this checkbox to activate documentation of an API implementation. When this option is enabled, deployed REST service offers the following endpoints to access API documentation:  * http://host:port/[component\_endpoint]/openapi.json: API   documentation as raw text (JSON file as OpenAPI 3.0.1 format). * http://host:port/[component\_endpoint]/api-docs: A UI with   API documentation and opportunity to test API operations.   If this option is enabled and the REST service is built as a Microservice, you can activate or deactivated API documentation by adding the exposeOpenApi=[true/false] parameter in the application.properties configuration file inside the Microservice JAR, or using the -DexposeOpenApi=[true/false] parameter in the command when running the Microservice.  Information noteNote: This option is available only if you have installed the R2025-10 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  To use this feature in Talend Runtime, you need to install Talend Runtime 8.0.1-R2025-10 patch or a later one. |
| Arguments | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/cxfrs.html> for available URI options. |
| JAXRS properties | This option appears when JWT Bearer Token is selected in the Security list in the Basic settings tab. Click [+] to add as many properties as needed to the table. In the Property Name field, you can either select the property from the drop-down list, or enter a property name that is not available in the list. Enter the value of the property in the Property Value field. For more information on the JAXRS properties, see the [Apache CXF documentation](https://cxf.apache.org/docs/jax-rs-jose.html#JAXRSJOSE-Configuration). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cREST can be a start component in a Route as the service provider, or middle or end component as the service consumer. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Making an HTTP POST call to a REST service using cREST](crest-clog-csetheader-ctimer-making-http-post-call-to-rest-service-using-crest)
* [Providing and consuming a REST service using cREST](crest-clog-cbeanregister-ctimer-providing-and-consuming-rest-service-using-crest)
* [Securing REST service with JWT validation using Keycloak](securing-rest-service-with-jwt-validation-using-keycloak)
* [Securing REST service with JWT validation using Microsoft Entra ID](securing-rest-service-with-jwt-validation-using-microsoft-entra-id)
* [Securing REST service with JWT validation using Talend Cloud IAM](securing-rest-service-with-jwt-validation-using-talend-cloud-iam)
* [Securing REST service with JWT validation using Talend STS](securing-rest-service-with-jwt-validation-using-talend-sts)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-providing-and-consuming-rest-service-using-crest -->
# Providing and consuming a REST service using cREST

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario demonstrates how to use the cREST component to provide and consume a REST service. To do so, two Routes are
built, a service provider Route and a consumer Route. The service provider Route will be
accessible for requests and respond with some predefined customer information. The consumer
Route will send a request to the REST service.

### In this section

* [Building the service provider Route](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-building-service-provider-route)
* [Building the service consumer Route](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-building-service-consumer-route)

**Related reference**  

* [cREST](crest "Provides integration with Apache CXF for connecting to JAX-RS services.")

**Related information**  

* [cLog](/talend/en-US/components/8.0/mediation-logs-and-errors/clog)
* [cSetBody](/talend/en-US/components/8.0/mediation-setbody/csetbody)
* [cTimer](/talend/en-US/components/8.0/mediation-orchestration/ctimer)
* [cBeanRegister](/talend/en-US/components/8.0/mediation-bean/cbeanregister)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-csetheader-ctimer-making-http-post-call-to-rest-service-using-crest -->
# Making an HTTP POST call to a REST service using cREST

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

This scenario demonstrates a simple Route using the cREST component to make an HTTP POST call to a REST
service.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-csetheader-ctimer-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-csetheader-ctimer-configuring-components)
* [Executing the Route](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-csetheader-ctimer-executing-route)

**Related reference**  

* [cREST](crest "Provides integration with Apache CXF for connecting to JAX-RS services.")

**Related information**  

* [cLog](/talend/en-US/components/8.0/mediation-logs-and-errors/clog)
* [cSetHeader](/talend/en-US/components/8.0/mediation-setheader/csetheader)
* [cSetBody](/talend/en-US/components/8.0/mediation-setbody/csetbody)
* [cTimer](/talend/en-US/components/8.0/mediation-orchestration/ctimer)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-building-service-consumer-route -->
# Building the service consumer Route

Last updated: 9/30/2026

This Route will consume the REST service that is built in the provider
Route.

### In this section

* [Arranging the flow of the message](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-arranging-flow-of-message)
* [Configuring how the message is processed](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-configuring-how-message-is-processed)
* [Executing the Route](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-building-service-provider-route -->
# Building the service provider Route

Last updated: 9/30/2026

This Route provides a REST Web service using the cREST component. In this Route, a cBeanRegister component is used to set the customer information in a Java bean.
The bean is then called by a cSetBody as the response of
the service.

### In this section

* [Creating Beans](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-creating-beans)
* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-viewing-code-and-executing-route)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-csetheader-ctimer-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. In the Basic settings view of the cTimer component, enter `1` in the
   Repeat field to trigger the message exchange
   one time.
2. In the Basic settings view
   of the cSetHeader component, click the
   [+] button to add two headers in the
   Headers table, and then give each header a name and a
   value. 

   In this example, name the first header `"Authorization"` and give its value an email address.

   The other header is
   `org.apache.camel.component.cxf.common.message.CxfConstants.CAMEL_CXF_RS_RESPONSE_CLASS`.
   Set it value to `String.class` to turn the response object
   to string.
3. In the Basic settings view of the
   cSetBody component:
   1. Select SIMPLE from the Language list to trigger
      a simple text message exchange in this example.
   2. In the Expression field, enter
      `{\"user\":\"test\",\"password\":\"t@l3nd\}"` in double
      quotation marks as the content of the message.
4. In the Basic settings view of the first
   cLog component, click Specify output log
   message in the Options area and enter
   `"Test.cLog_1 HEADER ${in.headers} BODY ${in.body} "` in the
   message field to log the message header and body.
5. In the Basic settings view
   of the cREST component:
   1. Fill the Endpoint field with the URL of the Web service you are
      going to invoke.
   2. From the Type list, select
      Manual to determine the REST
      API mapping manually.
   3. In the Relative Path field, enter
      `constant("")`.
   4. Select POST in the HTTP
      Method list.
   5. Select JSON in the Content
      Type and Accept Type lists.
   6. In the Response Class field, enter
      `javax.ws.rs.core.Response`.
6. In the Basic settings view of the second
   cLog component, select Specify output log
   messge in the Options area and enter
   `"Test.cLog_2 HEADER ${in.headers} BODY ${in.body} Exception
   ${exception.message}"` in the message field to log the header and body
   of the response message and the exception.
7. Press Ctrl+S to save your
   Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-csetheader-ctimer-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cTimer, a cSetHeader, a cSetBody, a cREST, and two
   cLog components onto the design
   workspace.
2. Link the components using the Row
   > Route connection as shown in the
   screenshot.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-csetheader-ctimer-executing-route -->
# Executing the Route

Last updated: 9/30/2026

## Procedure

Click the Run view to display it
and click the Run button to launch the execution
of your Route. You can also press F6 to execute
it. 

RESULT: The request and response messages as well as the exception
is printed in the execution console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-arranging-flow-of-message -->
# Arranging the flow of the message

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop
   a cTimer, a cREST, and a cLog component onto
   the design workspace.
2. Link the cTimer, cREST and cLog
   using the Row > Route connection.
3. Label the components for better identification of their roles.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-configuring-how-message-is-processed -->
# Configuring how the message is processed

Last updated: 9/30/2026

## Procedure

1. Double-click the cTimer
   component to display its Basic settings
   view in the Component tab.
2. In the Repeat field, enter
   *1* to generate the message exchange one time. Keep the
   default settings of the other options.
3. Double-click the cREST
   component to display its Basic settings
   view in the Component tab.
4. This cREST component will
   consume the REST service built in the provider Route.

   In the Endpoint field, type in
   the URL of the service,
   `"http://localhost:8040/services/customers"` in this
   example.

   Select Manual from the
   Type list. In the Relative Path field, enter `constant("")`.
   Select GET in the HTTP
   Method list. Keep the default settings of the other options.
5. Keep the default settings of the cLog component to log the message exchanges.
6. Press Ctrl+S to save your
   Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-executing-route -->
# Executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to have a look at the generated code.

   As shown in the code, the Route is built from
   cTimer\_1. The HTTP\_PATH, HTTP\_METHOD, and ACCEPT\_CONTENT\_TYPE are set in cREST\_1. The message is then routed to cLog\_1.
2. Click the Run view to display it
   and click the Run button to launch the execution
   of your Route. You can also press F6 to execute
   it. 

   RESULT: The customers information is displayed in the
   console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the cBeanRegister component to display its Basic settings view in the Component tab.
2. The cBeanRegister component
   registers a Java bean, in which the customer information is set with the firstName, lastName,
   city, and id
   values.

   In the Id field, enter
   `"customers"` to name the bean.

   Select the Customized option
   and enter the following code in the Code box to
   create two customers and set the firstName, lastName, city, and id values for each of
   them:

   ```
   beans.Customers customers = new beans.Customers();

   beans.Customer customer = new beans.Customer();
   customer.setFirstName(TalendDataGenerator.getFirstName());
   customer.setLastName(TalendDataGenerator.getLastName());
   customer.setCity(TalendDataGenerator.getUsCity());
   customers.addCustomer(customer);

   customer = new beans.Customer();
   customer.setFirstName(TalendDataGenerator.getFirstName());
   customer.setLastName(TalendDataGenerator.getLastName());
   customer.setCity(TalendDataGenerator.getUsCity());
   customers.addCustomer(customer);

   beanInstance = customers;
   ```
3. Double-click the cREST
   component to display its Basic settings
   view in the Component tab.
4. The cREST component is used
   to provide the REST service.

   In the Endpoint field, type in
   the endpoint URL where the Web service will be provided,
   `"http://localhost:8040/services/customers"` in this
   example.

   From the Type list, select
   Manual to determine the REST API
   mapping manually.

   In the REST API mapping table,
   click [+] to add a row in the table. In the
   Output Flow field, enter
   `getAllCustomers` as the name of it. Select GET in the HTTP
   Verb list. Keep the default settings in the other columns.
5. Double-click the cSetBody
   component to display its Basic settings
   view in the Component tab.
6. Select SIMPLE from the
   Dataformat list. In the Expression field, enter
   `"${ref:customers}"` to refer to the bean defined in the
   cBeanRegister component as the message body
   of the service response.
7. Keep the default settings of the cLog component to log the message exchanges.
8. Press Ctrl+S to save your
   Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-creating-beans -->
# Creating Beans

Last updated: 9/30/2026

## Procedure

1. From the repository tree view, expand Code > Global Beans and right-click the Beans node. In
   the contextual menu, select Create Bean.
2. The New Bean wizard opens. In the
   Name field, type in a name for the Bean,
   `Customer` in this use case.
3. Enter the following code in the design workspace.

   ```
   package beans;

   import javax.xml.bind.annotation.XmlAccessType;
   import javax.xml.bind.annotation.XmlAccessorType;
   import javax.xml.bind.annotation.XmlElement;
   import javax.xml.bind.annotation.XmlRootElement;
   import javax.xml.bind.annotation.XmlType;

   /**
    * <p>Java class for customer complex type.
    * 
    * <p>The following schema fragment specifies the expected content contained within this class.
    * 
    * <pre>
    * &lt;complexType name="customer">
    *   &lt;complexContent>
    *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
    *       &lt;sequence>
    *         &lt;element name="firstName" type="{http://www.w3.org/2001/XMLSchema}string"/>
    *         &lt;element name="lastName" type="{http://www.w3.org/2001/XMLSchema}string"/>
    *         &lt;element name="city" type="{http://www.w3.org/2001/XMLSchema}string"/>
    *       &lt;/sequence>
    *     &lt;/restriction>
    *   &lt;/complexContent>
    * &lt;/complexType>
    * </pre>
    * 
    * 
    */
   @XmlAccessorType(XmlAccessType.FIELD)
   @XmlType(name = "customer", propOrder = {
       "firstName",
       "lastName",
       "city"
   })
   @XmlRootElement(name = "customer")
   public class Customer {

       @XmlElement(required = true)
       protected String firstName;
       @XmlElement(required = true)
       protected String lastName;
       @XmlElement(required = true)
       protected String city;

       /**
        * Gets the value of the firstName property.
        * 
        * @return
        *     possible object is
        *     {@link String }
        *     
        */
       public String getFirstName() {
           return firstName;
       }

       /**
        * Sets the value of the firstName property.
        * 
        * @param value
        *     allowed object is
        *     {@link String }
        *     
        */
       public void setFirstName(String value) {
           this.firstName = value;
       }

       /**
        * Gets the value of the lastName property.
        * 
        * @return
        *     possible object is
        *     {@link String }
        *     
        */
       public String getLastName() {
           return lastName;
       }

       /**
        * Sets the value of the lastName property.
        * 
        * @param value
        *     allowed object is
        *     {@link String }
        *     
        */
       public void setLastName(String value) {
           this.lastName = value;
       }

       /**
        * Gets the value of the city property.
        * 
        * @return
        *     possible object is
        *     {@link String }
        *     
        */
       public String getCity() {
           return city;
       }

       /**
        * Sets the value of the city property.
        * 
        * @param value
        *     allowed object is
        *     {@link String }
        *     
        */
       public void setCity(String value) {
           this.city = value;
       }

   }
   ```
4. Press Ctrl+S to save your
   Bean.
5. Repeat this operation to create another Bean named `Customers`
   using the following code:

   ```
   package beans;

   import java.util.ArrayList;
   import java.util.HashMap;
   import java.util.List;
   import java.util.Map;

   import javax.xml.bind.annotation.XmlAccessType;
   import javax.xml.bind.annotation.XmlAccessorType;
   import javax.xml.bind.annotation.XmlElement;
   import javax.xml.bind.annotation.XmlRootElement;

   /**
    * <p>Java class for anonymous complex type.
    * 
    * <p>The following schema fragment specifies the expected content contained within this class.
    * 
    * <pre>
    * &lt;complexType>
    *   &lt;complexContent>
    *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
    *       &lt;sequence>
    *         &lt;element name="customer" type="{http://talend.org//services/esb/registry/soap/2012/09}customer" maxOccurs="unbounded" minOccurs="0"/>
    *       &lt;/sequence>
    *     &lt;/restriction>
    *   &lt;/complexContent>
    * &lt;/complexType>
    * </pre>
    * 
    * 
    */
   @XmlAccessorType(XmlAccessType.PROPERTY)
   @XmlRootElement(name = "customers")
   public class Customers {

   	private Map<Long, Customer> customers = new HashMap<Long, Customer>();
   	private long currentId = 1;
   	
       public static class Entry extends Customer {
           public Long id;
       }

       public Customers() {
       };

       /**
        * Gets the value of the customer property.
        * 
        * <p>
        * This accessor method returns a reference to the live list,
        * not a snapshot. Therefore any modification you make to the
        * returned list will be present inside the JAXB object.
        * This is why there is not a <CODE>set</CODE> method for the customer property.
        * 
        * <p>
        * For example, to add a new item, do as follows:
        * <pre>
        *    getCustomer().add(newItem);
        * </pre>
        * 
        * 
        * <p>
        * Objects of the following type(s) are allowed in the list
        * {@link Customer }
        * 
        * 
        */
       @XmlElement(name="customer")
       public List<Entry> getCustomers() {
       	List<Entry> adaptedMap = new ArrayList<Entry>();
           for(Map.Entry<Long, Customer> mapEntry : customers.entrySet()) {
               Entry entry = new Entry();
               entry.id = mapEntry.getKey();
               entry.setFirstName(mapEntry.getValue().getFirstName());
               entry.setLastName(mapEntry.getValue().getLastName());
               entry.setCity(mapEntry.getValue().getCity());
               adaptedMap.add(entry);
           }
           return adaptedMap;
       }
       
       public void setCustomers(List<Entry> adaptedMap) {
           for(Entry entry : adaptedMap) {
               customers.put(entry.id, entry);
           }
       }

       public Customer getCustomer(long id) {
       	return customers.get(id);
       }

       public long addCustomer(Customer customer) {
       	customers.put(currentId, customer);
       	return currentId++;
       }
       
       public void updateCustomer(Long id, Customer customer) {
      		customers.put(id, customer);
       }
       
       public void deleteCustomer(long id) {
   		customers.remove(id);
       }
       
   }
   ```

   For more information about creating and using Java Beans, see [Using Beans](/talend/r/en-US/8.0/studio-user-guide/using-beans).


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

## Procedure

1. From the Palette, drag and drop a
   cREST, a cSetBody, a cLog and a cBeanRegister component onto the design workspace.
2. Link the cREST, cSetBody and cLog
   using the Row > Route connection.
3. Label the components for better identification of their roles.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-apache-cxf/crest-clog-cbeanregister-ctimer-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the
   bottom of the design workspace to have a look at the generated code.

   As shown in the code, the Route is built from
   cREST\_1, set message body in cSetBody\_1 and then to cLog\_1.
2. Click the Run view to display it
   and click the Run button to launch the execution
   of your Route. You can also press F6 to execute
   it. 

   RESULT: The service is successfully started. You can access it from
   a Web browser using the service endpoint URL. The customer information is shown in
   the browser.
