<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch · versión 8.0 -->
# tFileFetch

Last updated: 9/30/2026

Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

This content is deprecated.

Information noteImportant: This component has been removed from Talend Studio 8.0
R2025-04 onwards. Use tHTTPClient instead.

Retrieves a file through the given protocol (HTTP, HTTPS, FTP, or SMB).

## tFileFetch Standard properties

These properties are used to configure
tFileFetch running in the Standard Job framework.

The Standard
tFileFetch
component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Protocol | Select the protocol you want to use from the list and fill in the corresponding fields: http, https, ftp, smb.  The properties differ slightly depending on the type of protocol selected. The additional fields are defined in this table, after the basic settings.  Information noteDeprecation: The support for SMBv1 (the smb option) is deprecated. |
| URI | Type in the URI of the site from which the file is to be fetched. |
| Use cache to save resource | Select this check box to save the data in the cache.  This option allows you to process the file data flow (in streaming mode) without saving it on your drive. This is faster and improves performance. |
| Domain | Enter the Microsoft server domain name.  Available for the smb protocol. |
| Username and Password | Enter the authentication information required to access the server.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available for the smb protocol. |
| Destination Directory | Browse to the destination folder where the file fetched is to be placed.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Destination Filename | Enter a new name for the file fetched.  If the Upload file option in the Advanced settings view is selected, the upload response will be saved in this file.  Information noteWarning: Use absolute path (instead of relative path) for this field to avoid possible errors. |
| Create full path according to URI | It allows you to reproduce the URI directory path. To save the file at the root of your destination directory, clear the check box.  Available for the http, https and ftp protocols. |
| Add header | Select this check box if you want to add one or more HTTP request headers as fetch conditions. In the Headers table, enter the name(s) of the HTTP header parameter(s) in the Name field and the corresponding value(s) in the Value field.  Available for the http and https protocols. |
| POST method | This check box is selected by default. It allows you to use the POST method. In the Parameters table, enter the name of the variable(s) in the Name field and the corresponding value in the Value field.  Clear the check box if you want to use the GET method.  Available for the http and https protocols. |
| Die on error | Clear this check box to skip the rows in error and to complete the process for the error free rows  Available for the http, https and ftp protocols. |
| Read Cookie | Select this check box for tFileFetch to load a web authentication cookie.  Available for the http, https, ftp and smb protocols. |
| Save Cookie | Select this check box to save the web page authentication cookie. This means you will not have to log on to the same web site in the future.  Available for the http, https, ftp and smb protocols. |
| Cookie file | Type in the full path to the file which you want to use to save the cookie or click [...] and browse to the desired file to save the cookie.  Available for the http, https, ftp and smb protocols. |
| Cookie policy | Choose a cookie policy from this drop-down list. Four options are available, BROWSER\_COMPATIBILITY, DEFAULT, NETSCAPE and RFC\_2109.  Available for the http, https, ftp and smb protocols. |
| Single cookie header | Check this box to put all cookies into one request header for maximum compatibility among different servers.  Available for the http, https, ftp and smb protocols. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at each component level. |
| Timeout | Enter the number of milliseconds after which the protocol connection should close.  Available for the http and https protocols. |
| Encoding for parameters | Select the character encoding for the POST method parameters: `US-ASCII`, `UTF-8`, or `Windows-1252`.  This option is available when POST method is selected in the Basic settings view. |
| Print response to console | Select this check box to print the server response in the console.  Available for the http and https protocols. |
| Upload file | Select this check box to upload one or more files to the server. For each file to be uploaded, click the [+] button beneath the table displayed and set the following fields:   * Name: the value of the name attribute of the <input type="file">   field in the original HTML form. * File: the full path of the file to upload, e.g.   `"D:/filefetch.txt"`. * Content-Type: the content type of the file to   upload. The default value is `"application/octet-stream"`. * Charset: the character set of the file to   upload. The default value is `"ISO-8859-1"`.   This option is available for the http and https protocols, with the POST method option in the Basic settings view selected.  With this option selected, the upload response will be saved in the file specified in the Destination filename field in the Basic settings view. |
| Enable proxy server | Select this check box if you are connecting via a proxy and complete the fields which follow with the relevant information.  Available for the http, https and ftp protocols. |
| Enable NTLM Credentials | Select this check box if you are using an NTLM authentication protocol.  Domain: The client domain name.  Host: The client's IP address.  Available for the http and https protocols. |
| Need authentication | Select this check box and enter the username and password in the relevant fields, if they are required to access the protocol.  Available for the http and https protocols. |
| Support redirection | Select this check box to repeat the redirection request until redirection is successful and the file can be retrieved.  Force Get method for 302 redirection: Select this check box to send the redirection request with the Get method if the redirection code is 302.  Available for the http, https and ftp protocols. |
| Trust all servers | Select this option to trust any servers. With this option selected, the component does not validate the server certificates. Not selected by default.  This option is available when `https` is selected from the Protocol drop-down list in the Basic settings view. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  INPUT\_STREAM: the content of the file being fetched. This is a Flow variable and it returns an InputStream.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used as a start component to feed the input flow of a Job and is often connected to the Job using an OnSubjobOk or OnComponentOk link, depending on the context. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Fetching data through HTTP](tfilefetch-tfileinputdelimited-tlogrow-tlogrow-fetching-data-through-http-standard-component-this)
* [Reusing stored cookie to fetch files through HTTP](tfilefetch-reusing-stored-cookie-to-fetch-files-through-http-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-reusing-stored-cookie-to-fetch-files-through-http-standard-component-this -->
# Reusing stored cookie to fetch files through HTTP

Last updated: 9/30/2026

This scenario describes a two-component Job which logs in a given HTTP website and
then using cookie stored in a user-defined local directory, fetches data from this
website.

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/internet/tfilefetch-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/internet/tfilefetch-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/internet/tfilefetch-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tFileFetch](tfilefetch "Retrieves a file through the given protocol (HTTP, HTTPS, FTP, or SMB).")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-tfileinputdelimited-tlogrow-tlogrow-fetching-data-through-http-standard-component-this -->
# Fetching data through HTTP

Last updated: 9/30/2026

This scenario describes a three-component Job which retrieves a file from an HTTP
website, reads data from the fetched file and displays the data on the console.

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/internet/tfilefetch-tfileinputdelimited-tlogrow-tlogrow-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/internet/tfilefetch-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/internet/tfilefetch-tfileinputdelimited-tlogrow-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tFileFetch](tfilefetch "Retrieves a file through the given protocol (HTTP, HTTPS, FTP, or SMB).")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Configuring the first subJob](/talend/en-US/components/8.0/internet/tfilefetch-configuring-first-subjob-standard-component)
* [Configuring the second subJob](/talend/en-US/components/8.0/internet/tfilefetch-configuring-second-subjob-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. Drop two tFileFetch components onto your
   design workspace.
2. Link the two components as subJobs using a Trigger > On Subjob Ok
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   Then, go to the local directory *D:/download* to check the downloaded file.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-tfileinputdelimited-tlogrow-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click tFileFetch to open its
   Basic settings view.
2. Select the protocol you want to use from the list. Here, http is selected.
3. In the URI field, type in the URI where
   the file to be fetched can be retrieved from. You can paste the URI directly
   in your browser to view the data in the file.
4. In the Destination directory field,
   browse to the folder where the fetched file is to be stored. In this
   example, it is *D:/Output*.
5. In the Destination filename field, type
   in a new name for the file if you want it to be changed. In this example,
   *new.txt*.
6. If needed, select the Add header check
   box and define one or more HTTP request headers as fetch conditions. For
   example, to fetch the file only if it has been modified since 19:43:31 GMT,
   October 29, 1994, fill in the Name and
   Value fields with "If-Modified-Since"
   and "Sat, 29 Oct 1994 19:43:31 GMT" respectively in the Headers table. For details about HTTP request
   header definitions, see [Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14).
7. Double-click tFileInputDelimited to open
   its Basic settings view.
8. In the File name field, type in the full
   path to the fetched file which had been stored locally.
9. Click the [...] button next to Edit schema to open the Schema dialog box. In this example, add one column
   *output* to store the data from the
   fetched file.
10. Leave other settings as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-tfileinputdelimited-tlogrow-tlogrow-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. Drop a tFileFetch, a tFileInputDelimited and a tLogRow onto your design workspace.
2. Link tFileFetch to tFileInputDelimited using a Trigger > On Subjob Ok or
   On Component Ok connection.
3. Link tFileInputDelimited to tLogRow using a Row > Main
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-tfileinputdelimited-tlogrow-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The data of the fetched file is displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-configuring-first-subjob-standard-component -->
# Configuring the first subJob

Last updated: 9/30/2026

## Procedure

1. Double-click tFileFetch\_1 to
   open its component view.
2. Select the protocol you want to use from the Protocol list. Here, we use the https protocol.
3. In the URI field, type in the
   URI through which you can log in the website and fetch the web page accordingly. In
   this example, the URI is https://www.codeproject.com/script/Membership/LogOn.aspx?download=true.
4. In the Destination directory
   field, browse to the folder where the fetched web page is to be stored. This folder
   will be created on the fly if it does not exist. In this example, type in *D:/download*.
5. In the Destination Filename
   field, type in a new name for the file if you want it to be changed. In this example,
   *codeproject.html*.
6. Under the Parameters table,
   click the plus button to add two rows and fill in the credentials for accessing the
   desired website.

   In the Name column, type in
   a new name respectively for the two rows. In this example, they are *Email* and *Password*, which are required
   by the website you are logging in.

   In the Value column, type
   in the authentication information.
7. Select the Save cookie check
   box.
8. In the Cookie directory
   field, type in the full path to the file which you want to use to save the cookie. In
   this example, it is *D:/download/cookie*.
9. Click Advanced settings to
   open its view.
10. Select the Support
    redirection check box so that the redirection request will be repeated
    until the redirection is successful.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/internet/tfilefetch-configuring-second-subjob-standard-component -->
# Configuring the second subJob

Last updated: 9/30/2026

## Procedure

1. Double-click tFileFetch\_2 to open its
   Component view.
2. From the Protocol list, select http.
3. In the URI field, type in the address
   from which you fetch the files of your interest. In this example, the
   address is
   http://www.codeproject.com/script/articles/download.aspx?file=/KB/DLL/File\_List\_Downloader/FLD02June2011\_Source.zip&rp=http://www.codeproject.com/Articles/203991/File-List-Downloader.
4. In the Destination directory field, type
   in the directory or browse to the folder where you want to store the fetched
   files. This folder can be automatically created if it does not exist yet
   during the execution process. In this example, type in
   *D:/download*.
5. In the Destination Filename field, type
   in a new name for the file if you want it to be changed. In this example,
   *source.zip*.
6. Clear the POST method check box to
   deactivate the Parameters table.
7. Select the Read cookie check box.
8. In the Cookie directory
   field, browse to the file which is used to save the cookie. In this example, it is *D:/download/cookie*.
