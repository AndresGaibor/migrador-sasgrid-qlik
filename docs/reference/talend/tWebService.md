<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice · versión 8.0 -->
# tWebService

Last updated: 9/30/2026

Calls a method via a Web service in order to retrieve the values of the parameters
defined in the component editor.

Information noteWarning: This component requires a JDK to be functional. It should
be noted that tWebservice will not run in Talend Cloud.

tWebservice calls the defined method
from the invoked Web service and returns the class as defined, based on the given
parameters.

## tWebService Standard properties

These properties are used to configure tWebService running in the Standard Job framework.

The Standard
tWebService component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. Enter properties manually * Repository: Select the repository   file where properties are stored. The fields that come after are   pre-filled in using the fetched data. |
| Service configuration | Click the [...] button next to the field to open the component editor.  In this editor, you can:  -select the Web service you want to use,  -configure the input parameters of the Web service,  -configure the output parameters of the Web service. These parameters will be used to retrieve and output specific data. |
| Mapping links display as | Auto: By default, the links between the input and output schemas and the Web service parameters are in the form of curves.  Curves: Links between the schema and the Web service parameters are in the form of curve.  Lines: Links between the schema and the Web service parameters are in the form of straight lines. This option slightly optimizes performance. |
| Connection Time out | Set a value in seconds for Web service connection time out. |
| Receive Time out | Set a value in seconds for server answer. |
| Input schema | A schema is a row description. It defines the number of fields that will be processed and passed on to the next component. The schema is either built-in or remote in the Repository. This field is used to process the input schema. The option for this schema may be:  - Built-in: No property data stored centrally.  - Repository: Select the Repository file where properties are stored. The following fields are pre-filled in using fetched data. |
| Edit Schema | Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Sync columns | This button is available when an input link has been created. Click this button to retrieve the schema from the previous component connected in the Job. |
| Output schema | This field is used to process the output schema. The schema is either built-in or remote in the Repository and is configured the same way as the input schema is.    Information noteWarning: *The input schema is not necessarily identical with the output schema.* |
| Use NTLM | Select this check box if you want to use the NTLM authentication protocol.  Domain: Name of the client domain,  Host: Client IP address. |
| Need authentication | Select this check box and enter a username and a password in the corresponding fields if this is necessary to access the service.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use http proxy | Select this check box if you are using a proxy server and fill in the necessary information. |
| Trust server with SSL | Select this check box to validate the server certificate to the client via an SSL protocol and fill in the corresponding fields:  TrustStore file: enter the path (including filename) to the certificate TrustStore file that contains the list of certificates that the client trusts.  TrustStore password: enter the password used to check the integrity of the TrustStore data. |
| Die on error | Clear this check box to skip the rows in error and to complete the process for the error free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Temporary folder (for wsdl2java) | Set or browse to a temporary folder that you configured in order to store the wsdl files. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as an input or as an intermediate component. It must be linked to an output component. |
| Limitation | A JDK is required for this component to operate. |

**Related concepts**  

* [Getting country names using tWebService](twebservice-tfixedflowinput-tlogrow-tlogrow-getting-country-names-using-twebservice-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-getting-country-names-using-twebservice-standard-component-this -->
# Getting country names using tWebService

Last updated: 9/30/2026

This scenario describes a three-component Job that uses a Web service to retrieve the
country name corresponding to a given country code.

### In this section

* [Linking components](/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-linking-components-standard-component-drop)
* [Configuring the input data](/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configuring-input-data-standard-component)
* [Configuring the Web service](/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configuring-web-service-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-executing-job-standard-component-save)

**Related reference**  

* [tWebService](twebservice "Calls a method via a Web service in order to retrieve the values of the parameters defined in the component editor.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configuring-input-data-standard-component -->
# Configuring the input data

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view and define the
   component properties.
2. Click the [...] button next to the Edit
   schema field to open a dialog box where you can define the
   input schema.
3. In the open dialog box, click the plus button to add a column to the
   schema.
4. Click in the column and type in a name, *CountryCode*
   in this example.
5. Click OK to close the schema definition
   dialog box. The *CountryCode* column displays in the
   Values table in the component Basic settings view.
6. In the Values table, click in the
   Value column and enter the value of the
   *CountryCode* column, *cn* in this
   example. This country code will be passed to the tWebService component to retrieve the country name
   corresponding to it.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configuring-web-service-standard-component -->
# Configuring the Web service

Last updated: 9/30/2026

### In this section

* [Selecting the WSDL](/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-selecting-wsdl-standard-component)
* [Configure the input mapping](/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configure-input-mapping-standard-component-click)
* [Configuring the output mapping](/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configuring-output-mapping-standard-component-click)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-executing-job-standard-component-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Save your Job and press F6 to execute
it.

## Results

The country name corresponding to the specified country code is returned from the
Web service.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-linking-components-standard-component-drop -->
# Linking components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tFixedFlowInput, tWebService, and tLogRow.
2. Connect the components together using Main
   Row links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configure-input-mapping-standard-component-click -->
# Configure the input mapping

Last updated: 9/30/2026

## Procedure

1. Click Next to open a new view in the
   editor.
2. In the panel to the right of the Input
   mapping view, select [+]
   parameters and then click the plus button on top to display
   the Parameter Tree dialog box where you
   can select any of the listed parameters. 

   The Web service in this example has only one input parameter, *CountryCode*.

   Information noteNote:

   If available, use the Auto map!
   button, located at the bottom left of the interface, to carry out the
   mapping operation automatically.

   You now need to create a connection between the input schema and the input
   parameter of the defined Web service.
3. In the Column list, drag the column in
   the input schema you want to link to the input parameter of the Web service
   to the corresponding parameter in the panel to the right.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-configuring-output-mapping-standard-component-click -->
# Configuring the output mapping

Last updated: 9/30/2026

## Procedure

1. Click Next to open a new view in the
   editor.

   In the Element list to the left of the
   view, the output parameter of the web service displays automatically.
   However, you can add other parameters if you select [+] parameters and then click the plus button on top to
   display the Parameter Tree dialog box
   where you can select any of the parameters listed.

   The Web service in this example has only one output parameter: *GetCountryByCountryCodeResult*.
2. In the panel to the right of the view, click the [...] button next to
   Edit Schema to open a dialog box in
   which you can define the output schema.
3. In the Output list to the right of the
   dialog box, click the plus button to add a column to the output
   schema.
4. Click in the column and type in a name, *Result* in
   this example. This will retrieve the names of the country.
5. Click OK to validate your changes and to
   close the schema definition dialog box.

   You now need to create a connection between the output parameter of the
   defined Web service and the schema of the output component.
6. In the Element list to the right of the
   editor, drag *parameters.GetCountryByCountryCodeResult* to the field that
   corresponds to the *Result* column to the
   right of the editor.

   Information noteNote:

   If available, use the Auto map!
   button, located at the bottom left of the interface, to carry out the
   mapping operation automatically.
7. Click OK to validate your changes and to
   close the editor.
8. Click the [...] button to open the
   Schema dialog box, and add a column
   to the output schema, *Result* in this
   example. Then click OK to validate the
   schema setting and close the dialog box.
9. Double-click the tLogRow component to
   open its Basic settings view, and click
   Sync columns to retrieve the schema
   from the proceeding component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebservice-tfixedflowinput-tlogrow-tlogrow-selecting-wsdl-standard-component -->
# Selecting the WSDL

Last updated: 9/30/2026

## Procedure

1. Double-click tWebService to open the
   component editor, or select the component in the design workspace and in the
   Basic settings view, click the
   [...] button next to Service
   configuration.
2. In the WSDL field, enter the Web service
   address or browse to it, if the WSDL is locally stored, by clicking the
   Browse... button. In this example,
   the WSDL URL is *http://www.webservicex.net/
   country.asmx?WSDL*.
3. Click the refresh button next to the WSDL
   filed to retrieve the WSDL description and display it in the fields that
   follow.
4. In the Port Name list, select the port
   you want to use, *countrySoap* in this
   example.
5. In the Operation list, select the service
   you want to use. In this example the selected service is *GetCountryByCountryCode(parameters):string*.
