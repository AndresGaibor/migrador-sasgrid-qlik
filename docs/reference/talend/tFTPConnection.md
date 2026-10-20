<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection · versión 8.0 -->
# tFTPConnection

Last updated: 9/30/2026

Opens an FTP connection to transfer files in a single transaction.

## tFTPConnection Standard properties

These properties are used to configure tFTPConnection running in the Standard Job framework.

The Standard
tFTPConnection component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Host | The IP address or hostname of the FTP server. |
| Port | The listening port number of the FTP server. |
| Logon type | Select the authentication type to access the FTP server:  * Password: Enter the username and password used to   access the server. * Password and account: Enter the username,   password, as well as the associated user account name.   To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| SFTP Support | Select this check box to connect to the FTP server via an SFTP connection. Information noteWarning: This option does not work with an HTTPS proxy. If you need an HTTPS proxy, use the tSetProxy component. |
| Authentication method | Select the SFTP authentication method, Public key, Password, or Public key and password.   * Public key:   Enter the path to the private key and the passphrase for the key in   the Private key and   Key Passphrase fields   correspondingly. * Password:   Enter the password required. * Public key and   password: Select this option if the SFTP server requires   both a public key and a password for authentication. In this case, you   need to provide the password, the   private key file, and the   key passphrase in the   corresponding fields.   This property is available only when the SFTP Support check box is selected. |
| Filename encoding | Select this check box to set the encoding used to convert file names from Strings to bytes. It should be the same encoding used on the SFTP server. If the SFTP server's version is greater than 3, the encoding should be `UTF-8`, or else an error occurs.  This property is available only when the SFTP Support check box is selected. |
| FTPS Support | Select this check box to connect to the FTP server via an FTPS connection. If you are using an HTTP proxy, via a tSetProxy component for example, you need to select this check box and set the connection mode to `Passive`.  Information noteNote: If your FTPS server requires session resumption between data and control connections, the tFTP components support this only when the TLS version is set to TLSv1.2 and the following Java 17 JVM properties are configured: ``` -Djdk.tls.client.protocols=TLSv1.2  -Djdk.tls.allowLegacyResumption=true -Djdk.tls.useExtendedMasterSecret=false -Djdk.tls.client.enableSessionTicketExtension=false ```  This configuration is necessary to allow Java 17 to work with session resumption for FTPS connections. |
| Keystore File | The path to your keystore file, a password protected file containing several keys and certificates.  Depending on the FTPS server configuration, an FTPS server private key or a client certificate is needed to establish an FTPS connection. You can store the FTP server private key or your client certificate in the keystore file.  This property is available only when the FTPS Support check box is selected. |
| Keystore Password | The password for your keystore file.  This property is available only when the FTPS Support check box is selected. |
| Security Mode | Select the security mode from the list, either Implicit or Explicit.  This property is available only when the FTPS Support check box is selected. |
| Connection mode | Select the connection mode from the list, either Passive or Active. |
| Encoding | Specify the encoding type by selecting an encoding type from the list or selecting CUSTOM and enter the encoding type manually. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use Socks Proxy | Select this check box if you are using a proxy, and in the Proxy host, Proxy port, Proxy user and Proxy password fields displayed, specify the proxy server settings information. |
| Data Channel Protection Level | The data channel protection level with which data is transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Protection Buffer Size | The maximum size (in bytes) of the encoded data blocks to be transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Enable Remote Verification | Select this option to enable remote verification. This option solves FTPS server architecture compatibility issues. See [setRemoteVerificationEnabled](https://commons.apache.org/proper/commons-net/apidocs/org/apache/commons/net/ftp/FTPClient.html#setRemoteVerificationEnabled-boolean-) for related information.  This option is available when FTPS Support is selected in the Basic settings view. |
| Connection timeout | Specify the timeout value (in ms) for the connection. A value of 0 or any negative values will be ignored. In this case, the default value (that is, infinite) will be used. |
| Use strict reply parsing | Select this option to use strict reply parsing. |
| Config client | Select this option to set JSch encryption algorithm properties. To set an encryption algorithm property, add a row in the table that appears by clicking the plus button on the bottom of the table and enter property name and property value in the Client parameter and Value columns. See [Fork of JSch-0.1.55](https://github.com/mwiede/jsch) and the setConfig section at [Class JSch](http://epaul.github.io/jsch-documentation/javadoc/) for related information.  This option is available when the SFTP Support option is selected in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is typically used as a single-component subJob. It is used along with other FTP components. |

**Related concepts**  

* [Listing and getting files/folders on an FTP directory](tftpfilelist-tftpconnection-tlogrow-listing-and-getting-files-folders-on-ftp-directory-standard-component "Here is an example of using Talend FTP components to iterate and list all files and folders on an FTP server directory, and then get only text files on that directory to a local directory.")
* [Putting files onto an FTP server](tftpconnection-tftpput-tftpclose-putting-files-onto-ftp-server-standard-component "Here is an example of using Talend FTP components to put several files in a local directory onto an FTP server.")
* [Renaming a file located on an FTP server](tftpconnection-tftprename-tftpclose-renaming-file-located-on-ftp-server-standard-component "Here is an example of using Talend FTP components to rename a file located on an FTP server.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-putting-files-onto-ftp-server-standard-component -->
# Putting files onto an FTP server

Last updated: 9/30/2026

Here is an example of using Talend FTP
components to put several files in a local directory onto an FTP server.

### In this section

* [Creating a Job for putting files onto an FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-creating-job-for-putting-files-onto-ftp-server-standard-component-create)
* [Opening a connection to the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-opening-connection-to-ftp-server-standard-component)
* [Putting files onto the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-putting-files-onto-ftp-server-standard-component?id=2298)
* [Closing the connection to the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-closing-connection-to-ftp-server-standard-component)
* [Executing the Job to put files on the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-executing-job-to-put-files-on-ftp-server-standard-component-press)

**Related reference**  

* [tFTPConnection](tftpconnection "Opens an FTP connection to transfer files in a single transaction.")
* [tFTPClose](tftpclose "Closes an active FTP connection to release the occupied resources.")
* [tFTPPut](tftpput "Uploads files from a local directory to an FTP directory.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-renaming-file-located-on-ftp-server-standard-component -->
# Renaming a file located on an FTP server

Last updated: 9/30/2026

Here is an example of using Talend FTP
components to rename a file located on an FTP server.

### In this section

* [Creating a Job for renaming a file on an FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-creating-job-for-renaming-file-on-ftp-server-standard-component)
* [Opening a connection to the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-opening-connection-to-ftp-server-standard-component)
* [Renaming the file on the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-renaming-file-on-ftp-server-standard-component)
* [Closing the connection to the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-closing-connection-to-ftp-server-standard-component)
* [Executing the Job to rename the file on the FTP server](/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-executing-job-to-rename-file-on-ftp-server-standard-component-press)

**Related reference**  

* [tFTPConnection](tftpconnection "Opens an FTP connection to transfer files in a single transaction.")
* [tFTPClose](tftpclose "Closes an active FTP connection to release the occupied resources.")
* [tFTPRename](tftprename "Renames files in an FTP directory.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-closing-connection-to-ftp-server-standard-component -->
# Closing the connection to the FTP server

Last updated: 9/30/2026

Configure the tFTPClose
component to close the connection to the FTP server.

## Procedure

1. Double-click the tFTPClose component
   to open its Basic settings view.
2. From the Component list drop-down
   list, select the tFTPConnection component that
   opens the connection you need to close. In this example, only one tFTPConnection component is used and it is selected by
   default.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-creating-job-for-putting-files-onto-ftp-server-standard-component-create -->
# Creating a Job for putting files onto an FTP server

Last updated: 9/30/2026

Create a Job to connect to an FTP server, then put several local files
onto the server, finally close the connection to the server.

## Procedure

1. Create a new Job and add a tFTPConnection component, a tFTPPut
   component, and a tFTPClose component by typing
   their names in the design workspace or dropping them from the Palette.
2. Link the tFTPConnection component to
   the tFTPPut component using a Trigger > OnSubjobOk
   connection.
3. Link the tFTPPut component to the
   tFTPClose component using a Trigger > OnSubjobOk
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-executing-job-to-put-files-on-ftp-server-standard-component-press -->
# Executing the Job to put files on the FTP server

Last updated: 9/30/2026

After setting up the Job and configuring the components used in
the Job for putting files onto the FTP server, you can then execute the Job and verify
the Job execution result.

## Procedure

1. Press Ctrl + S to save the Job and
   then F6 to execute the Job.
2. Connect to the FTP server to verify the result.

   As shown above, only the text and png files in the local directory are put onto
   the FTP server.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftpput-tftpclose-opening-connection-to-ftp-server-standard-component -->
# Opening a connection to the FTP server

Last updated: 9/30/2026

Configure the tFTPConnection
component to open a connection to the FTP server.

## Procedure

1. Double-click the tFTPConnection
   component to open its Basic settings view.
2. In the Host and Port fields, enter the FTP server IP address and the listening port
   number respectively.
3. In the Username and Password fields, enter the authentication details.
4. From the Connection Mode drop-down
   list, select the FTP connection mode you want to use, *Active* in this example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-closing-connection-to-ftp-server-standard-component -->
# Closing the connection to the FTP server

Last updated: 9/30/2026

Configure the tFTPClose
component to close the connection to the FTP server.

## Procedure

1. Double-click the tFTPClose component
   to open its Basic settings view.
2. From the Component list drop-down
   list, select the tFTPConnection component that
   opens the connection you need to close. In this example, only one tFTPConnection component is used and it is selected by
   default.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-creating-job-for-renaming-file-on-ftp-server-standard-component -->
# Creating a Job for renaming a file on an FTP server

Last updated: 9/30/2026

Create a Job to connect to an FTP server, then rename a file on the
server, finally close the connection to the server.

## Before you begin

Prerequisites: To replicate this
scenario, an FTP server must be started and a file must be put onto the server. In this
example, the file *movies.json* has been put into the folder *movies* under the root directory of the FTP server.

## Procedure

1. Create a new Job and add a tFTPConnection component, a tFTPRename component, and a tFTPClose component by typing their names in the design workspace or
   dropping them from the Palette.
2. Link the tFTPConnection component to
   the tFTPRename component using a Trigger > OnSubjobOk
   connection.
3. Link the tFTPRename component to the
   tFTPClose component using a Trigger > OnSubjobOk
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-executing-job-to-rename-file-on-ftp-server-standard-component-press -->
# Executing the Job to rename the file on the FTP server

Last updated: 9/30/2026

After setting up the Job and configuring the components used in
the Job for renaming the file on the FTP server, you can then execute the Job and verify
the Job execution result.

## Procedure

1. Press Ctrl + S to save the Job and
   then F6 to execute the Job.
2. Connect to the FTP server to verify the result.

   As shown above, the file on the FTP server has been renamed from *movies.json* to *action\_movies.json*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-opening-connection-to-ftp-server-standard-component -->
# Opening a connection to the FTP server

Last updated: 9/30/2026

Configure the tFTPConnection
component to open a connection to the FTP server.

## Procedure

1. Double-click the tFTPConnection component to open its Basic
   settings view.
2. In the Host and Port fields, enter the FTP server IP address and the listening port
   number respectively.
3. In the Username and Password fields, enter the authentication details.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpconnection-tftprename-tftpclose-renaming-file-on-ftp-server-standard-component -->
# Renaming the file on the FTP server

Last updated: 9/30/2026

Configure the tFTPRename component to rename the file on the FTP server.

## Procedure

1. Double-click the tFTPRename component to open its Basic settings view.
2. Specify the connection details required to access the FTP server. In this example, select the Use an existing connection check box and from the Component list drop-down list displayed, select the connection component to reuse its connection details you have already defined.
3. In the Remote directory field, enter the directory on the FTP server where the file to be renamed exists. In this example, it is */movies*.
4. In the Files table, click the [+] button to add a line, and then enter the existing file name in the Filemask column field and the new file name in the New name column field. In this example, they are *movies.json* and *action\_movies.json* respectively.
