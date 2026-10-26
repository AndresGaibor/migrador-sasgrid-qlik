<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttprequest · versión 8.0 -->
# tHttpRequest

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Information noteImportant: This component has been removed from Talend Studio 8.0
R2025-04 onwards. Use tHTTPClient instead.

Sends an HTTP request to the server and outputs the response information
locally.

tHttpRequest sends an HTTP request to the server end and
gets the corresponding response information from the server end.

## tHttpRequest Standard properties

These properties are used to configure tHttpRequest running in the Standard Job framework.

The Standard
tHttpRequest component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to be   processed and passed on to the next component. The schema is either   Built-in or stored remotely in the   Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: You create and store the   schema locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already created   the schema and stored it in the Repository. You can reuse it in various projects and Job   designs. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Sync columns | Click this button to retrieve the schema from the preceding component. |
| URI | Type in the Uniform Resource Identifier (URI) that identifies the data resource on the server. A URI is similar to a URL, but more general. |
| Method | Select an HTTP method to define the action to be performed:  Post: Sends data (for example HTML form data) to the server end.  Get: Retrieves data from the server end. |
| Post parameters from file | Browse to, or enter the path to the file that is used to provide parameters (request body) to the POST method. |
| Write response content to file | Select this check box to save the HTTP response to a local file. You can either type in the file path in the input field or click the [...] button to browse to the file path. |
| Create directory if not exists | Select this check box to create the directory defined in the Write response content to file field if it does not exist.  This check box appears only when the Write response content to file check box is selected and is cleared by default. |
| Headers | Type in the name-value pair(s) for HTTP headers to define the parameters of the requested HTTP operation.  Key: Fill in the name of the header field of an HTTP header.  Value: Fill in the content of the header field of an HTTP header.  The following gives an example for a Basic authentication implementation.   * Key: `Authentication` * Value: `"Basic   "+java.util.Base64.getEncoder().encodeToString("{your_username}:{your_password}".getBytes())`   For more information about definition of HTTP headers, please refer to:  [en.wikipedia.org/wiki/List\_of\_HTTP\_headers](http://en.wikipedia.org/wiki/List_of_HTTP_headers). |
| Need authentication | Select this check box to fill in a user name and a password in the corresponding fields if authentication is needed:  user: Fill in the user name for the authentication.  password: Fill in the password for the authentication.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Information noteNote: This component supports all the authentication schemas described in [Http Authentication](https://docs.oracle.com/javase/7/docs/technotes/guides/net/http-auth.html). If an authentication schema that requires user and password is enabled on the server side (for example, HTTP Digest authentication, NTLM, HTTP Negotiate (SPNEGO), or Kerberos 5), you need to select this option and provide username and password in the corresponding fields. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Set timeout | Select this check box to specify the connect and read timeout values in the following two fields:  * Connect timeout(s): Enter   the connect timeout value in seconds. An exception will   occur if the timeout expires before the connection can be   established. The value of *0* indicates an infinite time out. By   default, the connect timeout value is *30*. * Read timeout(s): Enter   the read timeout value in seconds. An exception will occur   if the timeout expires before there is data available for   read. By default, the read timeout value is *0*, which indicates an infinite   time out. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level and at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  CONNECTED: the result of whether a connection to the server established. This is an After variable and it returns a Boolean.  RESPONSE\_CODE: the response code returned by the remote HTTP server. This is an After variable and it returns an integer.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used in sending HTTP requests to server and saving the response information. This component can be used as a standalone component. |

**Related concepts**  

* [Sending a HTTP request to the server and saving the response information to a local file](thttprequest-tlogrow-sending-http-request-to-server-and-saving-response-information-to-local-file-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttprequest-tlogrow-sending-http-request-to-server-and-saving-response-information-to-local-file-standard-component-this -->
# Sending a HTTP request to the server and saving the response information to a local file

Last updated: 9/30/2026

This scenario describes a two-component Job that uses the GET method to retrieve information from the server end and writes the
response to a local file as well as to the console.

### In this section

* [Linking the components](/talend/en-US/components/8.0/http/thttprequest-tlogrow-linking-components-standard-component-in)
* [Configuring the GET request](/talend/en-US/components/8.0/http/thttprequest-tlogrow-configuring-get-request-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/http/thttprequest-tlogrow-executing-job-standard-component-then-you)

**Related reference**  

* [tHttpRequest](thttprequest "Sends an HTTP request to the server and outputs the response information locally.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttprequest-tlogrow-configuring-get-request-standard-component -->
# Configuring the GET request

Last updated: 9/30/2026

## Procedure

1. Double-click the tHttpRequest component
   to open its Basic settings view and define
   the component properties.
2. Fill in the URI field with
   *"http://192.168.0.63:8081/testHttpRequest/build.xml".*
   Note that this URI is for demonstration purposes only and it is not a live
   address.
3. From the Method list, select GET.
4. Select the Write response content to
   file check box and fill in the input field on the right with
   the file path by manual entry, *D:/test.txt* for this use
   case.
5. Select the Need authentication check box
   and fill in the user and password, both *tomcat* in this
   use case.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttprequest-tlogrow-executing-job-standard-component-then-you -->
# Executing the Job

Last updated: 9/30/2026

## About this task

Then you can run this Job.

The tLogRow component is used to present the
execution result of the Job.

## Procedure

1. If you want to configure how the result is presented by tLogRow, double-click the component to open its
   Component view and in the Mode area, select the Table
   (print values in cells of a table) check box.
2. Press F6 to run this Job.

## Results

Once done, the response information from the server is saved and displayed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/http/thttprequest-tlogrow-linking-components-standard-component-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective of Talend Studio,
   create a Job from the Job Designs node in the
   Repository tree view.

   For further information about how to create a Job, see [Creating a Job](/talend/r/en-US/8.0/studio-user-guide/creating-job).
2. Drop the following components from the Palette onto the design workspace: tHttpRequest and tLogRow.
3. Connect the tHttpRequest component to
   the tLogRow component using a Row > Main
   connection.
