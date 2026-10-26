<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern · versión 8.0 -->
# cExchangePattern

Last updated: 9/30/2026

Sets the message exchange mode in a Route.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cExchangePattern Standard properties

These properties are used to configure cExchangePattern running in the Standard Job framework.

The Standard
cExchangePattern component belongs to the Core family.

## Basic settings

| Properties | Description |
| --- | --- |
| Exchange Patterns | Select the message exchange mode from InOnly or InOptionalOut, InOut, OutIn, OutOptionalIn, RobustInOnly, RobustOutOnly. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | As a middle component in a Route, cExchangePattern allows you to set the message exchange mode. |
| Limitation |  |

**Related concepts**  

* [Enabling the InOut exchange pattern to get replies](cexchangepattern-csoap-cprocessor-cprocessor-enabling-inout-exchange-pattern-to-get-replies)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-enabling-inout-exchange-pattern-to-get-replies -->
# Enabling the InOut exchange pattern to get replies

Last updated: 9/30/2026

This scenario applies only to Talend ESB, Talend Data Services Platform, Talend Real-Time Big Data Platform, and
Talend Data Fabric.

In this scenario, a cExchangePattern component is
used to enable the request/reply exchange pattern in the Route, so that the client can
get a reply from the server.

To send requests to the server side, a SoapUI is needed and its configuration
will be briefed in the following contents.

To build the Route, do the following.

### In this section

* [Dropping and linking the components](/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-dropping-and-linking-components)
* [Configuring the components](/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-configuring-components)
* [Viewing code and executing the Route](/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-viewing-code-and-executing-route)
* [Creating and sending a request to the server Route and getting a reply](/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-creating-and-sending-request-to-server-route-and-getting-reply)

**Related reference**  

* [cExchangePattern](cexchangepattern "Sets the message exchange mode in a Route.")

**Related information**  

* [cSOAP](/talend/en-US/mediation-components/8.0/mediation-apache-cxf/csoap)
* [cProcessor](/talend/en-US/mediation-components/8.0/mediation-custom-code/cprocessor)


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-configuring-components -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click cSOAP to open
   its Basic settings view in the Component tab.
2. In the Address field, leave
   the default setting unchanged.
3. In the Type list, select
   wsdlURL.
4. In the WSDL File field, enter
   the URL of the WSDL file. You can also click the [...] button
   to browse for it.
5. Click [...] next to Service
   Configuration to open the service configuration wizard. The
   WSDL field has been filled in with the selected WSDL
   file. Click  to show the available port in the Port
   Name box. Select the airportSoap port and click
   Finish to close the wizard. The Service
   Name and Port Name fields in the
   Basic settings view are filled in
   automatically.
6. In the Dataformat list,
   select PAYLOAD.
7. Double-click cExchangePattern to open its Basic
   settings view in the Component tab.
8. In the Exchange Patterns
   list, select InOut to enable the
   request/reply message exchange mode.
9. Double-click cProcessor to
   open its Basic settings view in the
   Component tab.
10. In the Code box, enter the
    code below.

    ```
    StringBuilder sb = new StringBuilder();
    sb.append("<tns:getAirportInformationByISOCountryCodeResponse xmlns:tns=\"http://airportsoap.sopera.de\">");
    sb.append("<tns:getAirportInformationByISOCountryCodeResult>This is a response</tns:getAirportInformationByISOCountryCodeResult>");
    sb.append("</tns:getAirportInformationByISOCountryCodeResponse>");
    exchange.getOut().setBody(sb.toString());
    ```

    As shown above, a string is built here and is used as a reply
    message of the Route. It is in line with the message definition of the above WSDL
    file.
11. Press Ctrl+S to save your
    Route.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-creating-and-sending-request-to-server-route-and-getting-reply -->
# Creating and sending a request to the server Route and getting a reply

Last updated: 9/30/2026

## Procedure

1. In the SoapUI, create a Test project and edit a request, as
   illustrated below:

   Note that the wsdl file must be same as that configured for
   cSOAP, so that the request can be in line
   with the definition of the web service.
2. Send the request to the server Route and you can get the reply, as
   illustrated below:


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-dropping-and-linking-components -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. From the Palette, drag and
   drop a cSOAP, a cExchangePattern and a cProcessor onto the workspace, and label them *WebService\_producer*, *Set\_exchange\_mode* and *Build\_reply\_message* respectively to better identify their
   roles in the Route.
2. Link cSOAP to cExchangePattern using a Row > Route
   connection.
3. Link cExchangePattern to cProcessor using a Row > Route
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-exchange/cexchangepattern-csoap-cprocessor-cprocessor-viewing-code-and-executing-route -->
# Viewing code and executing the Route

Last updated: 9/30/2026

## Procedure

1. Click the Code tab at the bottom of the
   design workspace to check the generated code.

   As shown above, the route has its message exchange pattern set as
   InOut using the method
   .setExchangePattern(org.apache.camel.ExchangePattern.InOut).
   In the meantime, a string is created using StringBuilder sb = new
   StringBuilder() at cProcessor\_1 and is used as the
   reply message via the method exchange.getOut().setBody(
   sb.toString()).
2. Press F6 to execute the Route.

   The server Route gets started.
