<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/webservice/twebserviceinput · versión 8.0 -->
# tWebServiceInput

Last updated: 9/30/2026

Invokes a Method through a Web service.

This component calls the defined method from the
invoked Web service, and returns the class as defined, based on the given parameters.

## tWebServiceInput Standard properties

These properties are used to configure tWebServiceInput running in the Standard Job framework.

The Standard
tWebServiceInput component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the Repository   file where the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
|  | Click this icon to open a WSDL schema wizard and store your WSDL connection in the Repository tree view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: You create the schema   and store it locally for the relevant component. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository. You can reuse it   in various projects and Job flowcharts. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| WSDL | Description of Web service bindings and configuration. |
| Need authentication / Username and Password | Select this check box and:  -enter a username and a password in the corresponding fields if this is necessary to access the service. Or,  -select the Windows authentication check box and enter the windows domain in the corresponding field if this is necessary to access the service.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use http proxy | Select this check box if you are using a proxy server and fill in the necessary information. |
| Trust server with SSL | Select this check box to validate the server certificate to the client via an SSL protocol and fill in the corresponding fields:  TrustStore file: enter the path (including filename) to the certificate TrustStore file that contains the list of certificates that the client trusts.  TrustStore password: enter the password used to check the integrity of the TrustStore data. |
| Time out (second) | Set a value in seconds for Web service connection time out. |
| Method Name | Enter the exact name of the Method to be invoked.  The Method name MUST match the corresponding method described in the Web Service. The Method name is also case-sensitive. |
| Parameters | Enter the parameters expected and the sought values to be returned. Make sure that the parameters entered fully match the names and the case of the parameters described in the method. |

## Advanced Settings

| Properties | Description |
| --- | --- |
| API | Select the framework for invoking the Web service method: `AXIS` or `CXF`. See [Web Services - Axis](http://axis.apache.org/axis/) and [Apache AXF](http://cxf.apache.org/) for related information. |
| Advanced Use | Select this check box to display the fields dedicated for the advanced use of tWebServiceInput:  WSDL2java: click the [...] button to generate  Talend  routines that hold the Java code necessary to connect and query the Web service.  Code: replace the generated model Java code with the code necessary to connect and query the specified Web service using the code in the generated  Talend  routines.  Match Brackets: select the number of brackets to be used to close the for loop based on the number of open brackets.  Information noteNote: The Advanced Use option is available when `AXIS` is selected from the API drop-down list. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used as a Start component. It must be linked to an output component. |

**Related concepts**  

* [Getting the sum of two numbers using tWebServiceInput](getting-sum-of-two-numbers-using-twebserviceinput-standard-component "This scenario describes a two-component Job which uses a Web service method to obtain the sum of two numbers and displays the output on the Run console view.")
