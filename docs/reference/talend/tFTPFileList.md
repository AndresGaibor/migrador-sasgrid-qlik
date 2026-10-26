<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist · versión 8.0 -->
# tFTPFileList

Last updated: 9/30/2026

Lists all files and folders directly under a specified directory based on a
filemask pattern.

## tFTPFileList Standard properties

These properties are used to configure tFTPFileList running in the Standard Job framework.

The Standard
tFTPFileList component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Host | The IP address or hostname of the FTP server. |
| Port | The listening port number of the FTP server. |
| Logon type | Select the authentication type to access the FTP server:  * Password: Enter the username and password used to   access the server. * Password and account: Enter the username,   password, as well as the associated user account name.   To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Remote directory | The remote directory where the files and folders to be listed are located. |
| File detail | Select this check box to list the details of each file/folder. The informative details include the file/folder permissions, the name of the author, the name of the group of users that have read/write permissions, the file size, and the last modification date. |
| Files | The names of the files/folders to be listed. You can specify multiple files/folders in a line by using wildcards or a regular expression. |
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
| Ignore Failure At Quit (FTP) | Select this check box to ignore library closing errors or FTP closing errors. |
| Data Channel Protection Level | The data channel protection level with which data is transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Protection Buffer Size | The maximum size (in bytes) of the encoded data blocks to be transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Enable Remote Verification | Select this option to enable remote verification. This option solves FTPS server architecture compatibility issues. See [setRemoteVerificationEnabled](https://commons.apache.org/proper/commons-net/apidocs/org/apache/commons/net/ftp/FTPClient.html#setRemoteVerificationEnabled-boolean-) for related information.  This option is available when FTPS Support is selected in the Basic settings view. |
| Connection timeout | Specify the timeout value (in ms) for the connection. A value of 0 or any negative values will be ignored. In this case, the default value (that is, 60000ms) will be used. |
| Use strict reply parsing | Select this option to use strict reply parsing. |
| Config client | Select this option to set JSch encryption algorithm properties. To set an encryption algorithm property, add a row in the table that appears by clicking the plus button on the bottom of the table and enter property name and property value in the Client parameter and Value columns. See [Fork of JSch-0.1.55](https://github.com/mwiede/jsch) and the setConfig section at [Class JSch](http://epaul.github.io/jsch-documentation/javadoc/) for related information.  This option is available when the Use an existing connection option is not selected and the SFTP Support option is selected in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| CURRENT\_FILE | The current file name. This is a Flow variable and it returns a string. |
| CURRENT\_FILEPATH | The current file path. This is a Flow variable and it returns a string. |
| NB\_FILE | The number of the files processed. This is an After variable and it returns an integer. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is typically used as a single-component subJob but can also be used with other components. |

**Related concepts**  

* [Listing and getting files/folders on an FTP directory](tftpfilelist-tftpconnection-tlogrow-listing-and-getting-files-folders-on-ftp-directory-standard-component "Here is an example of using Talend FTP components to iterate and list all files and folders on an FTP server directory, and then get only text files on that directory to a local directory.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-listing-and-getting-files-folders-on-ftp-directory-standard-component -->
# Listing and getting files/folders on an FTP directory

Last updated: 9/30/2026

Here is an example of using Talend FTP
components to iterate and list all files and folders on an FTP server directory, and then
get only text files on that directory to a local directory.

### In this section

* [Creating a Job for listing and getting files/folders on an FTP directory](/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-creating-job-for-listing-and-getting-files-folders-on-ftp-directory-standard-component)
* [Opening a connection to the FTP server](/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-opening-connection-to-ftp-server-standard-component)
* [Listing all files/folders on the FTP root directory](/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-listing-all-files-folders-on-ftp-root-directory-standard-component)
* [Getting files on the FTP server directory to a local directory](/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-getting-files-on-ftp-server-directory-to-local-directory-standard-component)
* [Closing the connection to the FTP server](/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-closing-connection-to-ftp-server-standard-component)
* [Executing the Job to list and get files/folders on the FTP directory](/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-executing-job-to-list-and-get-files-folders-on-ftp-directory-standard-component-press)

**Related reference**  

* [tFTPFileList](tftpfilelist "Lists all files and folders directly under a specified directory based on a filemask pattern.")
* [tFTPConnection](tftpconnection "Opens an FTP connection to transfer files in a single transaction.")
* [tFTPGet](tftpget "Downloads files to a local directory from an FTP directory.")
* [tFTPClose](tftpclose "Closes an active FTP connection to release the occupied resources.")

**Related information**  

* [tIterateToFlow](/talend/en-US/components/8.0/orchestration/titeratetoflow)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-closing-connection-to-ftp-server-standard-component -->
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
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-creating-job-for-listing-and-getting-files-folders-on-ftp-directory-standard-component -->
# Creating a Job for listing and getting files/folders on an FTP directory

Last updated: 9/30/2026

Create a Job to connect to an FTP server, iterate and list all files
and folders on an FTP root directory, then get only text files on the FTP root directory to
a local directory, finally close the connection to the server.

## Before you begin

Prerequisites: To replicate this
scenario, an FTP server must be started and a couple of files/folders must be put onto
the root directory of the FTP server.

## Procedure

1. Create a new Job and add a tFTPConnection component, a tFTPFileList component, a tIterateToFlow component, a tLogRow
   component, a tFTPGet component, and a tFTPClose component by typing their names in the design
   workspace or dropping them from the Palette.
2. Link the tFTPFileList component to the
   tIterateToFlow component using a Row > Iterate
   connection.
3. Link the tIterateToFlow component to
   the tLogRow component using a Row > Main connection.
4. Link the tFTPConnection component to
   the tFTPFileList component using a Trigger > OnSubjobOk
   connection.
5. Do the same to link the tFTPFileList
   component to the tFTPGet component, and the
   tFTPGet component to the tFTPClose component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-executing-job-to-list-and-get-files-folders-on-ftp-directory-standard-component-press -->
# Executing the Job to list and get files/folders on the FTP directory

Last updated: 9/30/2026

After setting up the Job and configuring the components used in
the Job for listing and getting files/folders on the FTP directory, you can then execute
the Job and verify the Job execution result.

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

   As shown above, the names and paths of the files and folders on the FTP server
   root directory are displayed on the console, and only the text files are downloaded
   to the specified local directory.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-getting-files-on-ftp-server-directory-to-local-directory-standard-component -->
# Getting files on the FTP server directory to a local directory

Last updated: 9/30/2026

Configure the tFTPGet
component to get only the text files on the FTP root directory to a local
directory.

## Procedure

1. Double-click the tFTPGet component to
   open its Basic settings view.
2. Specify the connection details required to access the FTP server. In
   this example, select the Use an existing connection
   check box and from the Component list drop-down
   list displayed, select the connection component to reuse its connection details you
   have already defined.
3. In the Local directory field, specify
   the local directory to which the files and folders will be downloaded. In this
   example, it is *D:/FtpDownloads*.
4. In the Remote directory field, specify
   the FTP server directory under which the files and folders will be downloaded. In
   this example, it is */*, which means the root
   directory of the FTP server.
5. In the Files table, click the
   [+] button to add a line and in the Filemask column field, enter *\*.txt* between double quotation marks to get only the text files on
   the FTP directory to the local directory.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-listing-all-files-folders-on-ftp-root-directory-standard-component -->
# Listing all files/folders on the FTP root directory

Last updated: 9/30/2026

Configure the tFTPFileList component, the tIterateToFlow component, and the tLogRow component to iterate all files and folders on the FTP root directory and display the names and paths of these files and folders on the console of *Talend Studio*.

## Procedure

1. Double-click the tFTPFileList component to open its Basic settings view.
2. Specify the connection details required to access the FTP server. In this example, select the Use an existing connection check box and from the Component list drop-down list displayed, select the connection component to reuse its connection details you have already defined.
3. In the Remote directory field, specify the FTP server directory on which the files and folders will be iterated. In this example, it is */*, which means the root directory of the FTP server.
4. Double-click the tIterateToFlow component to open its Basic settings view.
5. Click the  button next to Edit schema to open the schema dialog box.
6. Click the  button to add two String type columns *filename* and *filepath* that will hold the names and paths of the files to be iterated respectively. When done, click OK to close the dialog box.
7. In the Mapping table, set the values for the *filename* and *filepath* columns. In this example, the global variable *((String)globalMap.get("tFTPFileList\_1\_CURRENT\_FILE"))* for *filename* and the global variable *((String)globalMap.get("tFTPFileList\_1\_CURRENT\_FILEPATH"))* for *filepath*.

   Note that you can fill the values by pressing Ctrl + Space to access the global variables list and then selecting *tFTPFileList\_1\_CURRENT\_FILE* and *tFTPFileList\_1\_CURRENT\_FILEPATH* from the list.
8. Double-click the tLogRow component to open its Basic settings view, and then select Table (print values in cells of a table) in the Mode area for better readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfilelist-tftpconnection-tlogrow-opening-connection-to-ftp-server-standard-component -->
# Opening a connection to the FTP server

Last updated: 9/30/2026

Configure the tFTPConnection component to open a connection to the FTP
server.

## Procedure

1. Double-click the tFTPConnection
   component to open its Basic settings view.
2. In the Host and Port fields, enter the FTP server IP address and the listening port
   number respectively.
3. In the Username and Password fields, enter the authentication details.
