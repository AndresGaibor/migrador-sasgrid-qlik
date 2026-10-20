<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp · versión 8.0 -->
# cHttp

Last updated: 9/30/2026

Provides HTTP-based endpoints for consuming and producing HTTP
resources.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cHttp Standard properties

These properties are used to configure cHttp running in the Standard Job framework.

The Standard
cHttp component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Uri | The URI of the Http resource to call. |
| Client | Select this option to use cHttp as a client to call external servers. |
| Server | Select this option to use cHttp as a server to produce Web services. |
| Client Configuration / Method | * Select an HTTP request method from GET, POST, PUT, DELETE,   HEAD, OPTIONS, TRACE, and PATCH in the list. * GET: Retrieve the information   identified by the request URI.  Parameters: click the [+] button to add lines as needed and   define the key and value in the table.  Encoder Charset: enter the   encoder charset in the field. * POST: Request that the origin   server accept the entity enclosed in the request as a new   subordinate of the resource identified by the request URI.  Plain Text: select the Content-Type from *text/plain*, *text/html*, *text/xml*, *application/x-www-form-urlencoded*, *application/xml*, *application/JSON*, or *other...* (specify the Content-Type in   the next field that appears when *other...* is selected), and type in the text in the   Content box as the request   message.  Form Style: click the [+] button to add lines as needed and   define the key and value in the Parameters table. Also, enter the encoder charset in   the Encoder Charset field.  Use Message Body: use the incoming message body as the   Http request. Select the Content-Type from *text/plain*, *text/html*, *text/xml*, *application/x-www-form-urlencoded*, *application/xml*, *application/JSON*, or *other...* (specify the Content-Type in   the next field that appears when *other...* is selected), * PUT: Request that the   enclosed entity be stored under the supplied request URI.  Plain Text: select the Content-Type from *text/plain*, *text/html*, *text/xml*, *application/x-www-form-urlencoded*, *application/xml*, *application/JSON*, or *other...* (specify the Content-Type in   the next field that appears when *other...* is selected), and type in the text in the   Content box as the request   message.  Form Style: click the [+] button to add lines as needed and   define the key and value in the Parameters table. Also, enter the encoder charset in   the Encoder Charset field.  Use Message Body: use the incoming message body as the   Http request. Select the Content-Type from *text/plain*, *text/html*, *text/xml*, *application/x-www-form-urlencoded*, *application/xml*, *application/JSON*, or *other...* (specify the Content-Type in   the next field that appears when *other...* is selected), * DELETE: Request that the origin   server delete the resource identified by the request URI.  Parameters: click the [+] button to add lines as needed and   define the key and value in the table.  Encoder Charset: enter the   encoder charset in the field. * HEAD: Identical to GET except   that the server MUST NOT return a message body in the   response.  Parameters: click the [+] button to add lines as needed and   define the key and value in the table.  Encoder Charset: enter the   encoder charset in the field. * OPTIONS: Represent a request for   information about the communication options available on the   request/response chain identified by the request URI. * TRACE: Invoke a remote,   application-layer loop-back of the request message. * PATCH: Modify data partially based on the given   parameters.  Plain Text: select the   Content-Type from *text/plain*,   *text/html*, *text/xml*, *application/x-www-form-urlencoded*,   *application/xml*, *application/JSON*, or *other...*. Specify   the Content-Type in the next field that appears when *other...* is   selected.  Form Style: click the [+] button   to add lines as needed and define the key and value in the   Parameters table.  Use Message Body: use the incoming message body as the   HTTP request. Select the Content-Type from   *text/plain*, *text/html*, *text/xml*,   *application/x-www-form-urlencoded*, *application/xml*,   *application/JSON*, or *other...*. Specify the Content-Type in the   next field that appears when *other...* is selected. |
| Server Configuration / Disable Stream Cache | DefaultHttpBinding will copy the request input stream into a stream cache and put it into message body. When this check box is selected, DefaultHttpBinding will set the request input stream directly into the message body. |
| Server Configuration / Session Support | Select this check box to enable the session manager on the server side of Jetty. |
| Server Configuration / Use Transfer-Encoding | This option is enabled by default. If this check box is cleared, Jetty servlet will disable the HTTP streaming and set the content-length header on the response. |
| Server Configuration / Enable JMX | Select this option to enable Jetty JMX support for this endpoint. For more information about this option, see the site<http://camel.apache.org/jetty.html#Jetty-JettyJMXsupport>. |
| Server Configuration / Match on URI Prefix | Select this check box to use the CamelServlet to find a target consumer by matching the URI prefix if no exact match is found. For more information about this option, see the site <http://camel.apache.org/how-do-i-let-jetty-match-wildcards.html>. |
| Server Configuration / Use Jetty Continuation | Select this check box to use Jetty continuations for the Jetty Server. For more information about this option, see the site <http://wiki.eclipse.org/Jetty/Feature/Continuations>. |
| Server Configuration / Enable HTTP TRACE | Select this option to enable the HTTP TRACE method. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Headers | Click the [+] button to add lines as needed and define the key and value for headers. See the site <https://camel.apache.org/components/latest/http-component.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cHttp provides Http based endpoints for consuming external Http resources, that is to say as a client to call external servers using Http. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Retrieving the content of a remote file](chttp-csetbody-cprocessor-cmessagingendpoint-retrieving-content-of-remote-file)
* [Using cHttp to produce a Web service](chttp-cprocessor-using-chttp-to-produce-web-service)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-cprocessor-using-chttp-to-produce-web-service -->
# Using cHttp to produce a Web service

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, cHttp is used to as a server to
start a Web service. A cProcessor component is used to
request the service.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-internet/chttp-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-internet/chttp-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-internet/chttp-cprocessor-viewing-code-and-executing-route)

**Related reference**  

* [cHttp](chttp "Provides HTTP-based endpoints for consuming and producing HTTP resources.")

**Related information**  

* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-csetbody-cprocessor-cmessagingendpoint-retrieving-content-of-remote-file -->
# Retrieving the content of a remote file

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, cHttp is used to request the body
of a weather condition definition file that is available at 
<http://wsf.cdyne.com/WeatherWS/Weather.asmx>
.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-internet/chttp-csetbody-cprocessor-cmessagingendpoint-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-internet/chttp-csetbody-cprocessor-cmessagingendpoint-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-internet/chttp-csetbody-cprocessor-cmessagingendpoint-viewing-code-and-executing-route)

**Related reference**  

* [cHttp](chttp "Provides HTTP-based endpoints for consuming and producing HTTP resources.")

**Related information**  

* [cSetBody](/talend/en-US/mediation-components/8.0/mediation-setbody/csetbody)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)
* [cMessagingEndpoint](/talend/en-US/mediation-components/8.0/mediation-messaging-endpoint/cmessagingendpoint)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click cHttp to open its Basic settings view in the Component tab.
2. In the URI field, enter
   `"http://localhost:8088/user"` where the service will be
   accessible for requests.
3. Click the Server radio button to use this
   cHttp component as a server. Keep the
   default settings of the other options.
4. Double-click cProcessor to
   open its Basic settings view in the
   Component tab.
5. In the Code area, enter the
   following code to get the header `id` of the exchange
   message:

   ```
   System.out.println(exchange.getIn().getHeader("id"));
   ```
6. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drag and drop a cHttp and a cProcessor from the Palette onto the design workspace.
2. Link the components using a Row >
   Route connection.
3. Label the components for better identification of their roles.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the route is built from the endpoint
   server\_cHttp\_1 and the message header id is
   printed out by cProcessor\_1.
2. Press F6 to execute the Route.
3. Start a Web browser. In the address bar, type in
   http://localhost:8088/user?id=1 and click Enter. A blank page opens up.
4. Switch back to Talend Studio.
   The ID 1 is printed in the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-csetbody-cprocessor-cmessagingendpoint-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click cMessagingEndpoint to open
   its Basic settings view in the Component tab.
2. In the URI field, enter
   `timer:go?repeatCount=1` to define a timer for starting
   message exchanges. In this example, only one message exchange will be carried out due
   to the setting of repeatCount=1.
3. Double-click cSetBody to open its
   Basic settings view in the Component tab.
4. In the Language field, select
   Constant.
5. In the Expression field, enter the
   following as the body of the request message:

   ```
   <soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:weat=\"http://ws.cdyne.com
   /WeatherWS/\"><soapenv:Header/><soapenv:Body><weat:GetWeatherDefinitionInformation/></soapenv:Body></soapenv:Envelope>
   ```
6. Double-click cHttp to open
   its Basic settings view in the Component tab.
7. In the Uri field, enter the
   location of the file to fetch,
   `http://wsf.cdyne.com/WeatherWS/Weather.asmx` in this
   example.
8. Click the Client radio button to use this
   cHttp component as a client.
9. Select POST in the Method list and then the Use Message
   Body radio button. Select text/xml in the
   Content-Type list.
10. Click Advanced settings for further setup.
11. Click the [+] button to add a line in the
    Headers table. 

    Type in `SOAPAction` and
    `http://ws.cdyne.com/WeatherWS/GetWeatherInformation` for the
    Key and Value fields.
12. Double-click cProcessor to open its
    Basic settings view in the Component tab.
13. In the Code area, enter the following to print the
    response from the remote website, the body of the desired file:

    ```
    System.out.println("--------------------RESPONSE--------------------");
    System.out.println(exchange.getIn().getBody(String.class));
    System.out.println("--------------------END--------------------");
    ```
14. Press Ctrl+S to save your Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-csetbody-cprocessor-cmessagingendpoint-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the workspace: cMessagingEndpoint, cSetBody, cHttp and
   cProcessor, labeled as STARTER, HTTP\_REQUEST\_BODY, GET\_WEATHER\_DESCRIPTION and PRINT\_RESPONSE respectively.
2. Link the components using a Row >
   Route connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/chttp-csetbody-cprocessor-cmessagingendpoint-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the message exchange starts from the endpoint STARTER, gets its body
   set to <soapenv:Envelope
   xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"xmlns:weat=\"http://ws.cdyne.com/WeatherWS/\"><soapenv:Header/><soapenv:Body><weat:GetWeatherDefinitionInformation/></soapenv:Body></soapenv:Envelope>
   at cSetBody\_1, and then is sent out to the specified
   website by cHttp\_1. Finally, the response is printed
   out in cProcessor\_1.
2. Press F6 to execute the Route.

   As shown above, the retrieved file defines up to 37 weather conditions
   with detailed description.
