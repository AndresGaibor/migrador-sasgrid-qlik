<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpget · versión 8.0 -->
# tFTPGet

Last updated: 9/30/2026

Downloads files to a local directory from an FTP directory.

## tFTPGet Standard properties

These properties are used to configure tFTPGet running in the Standard Job framework.

The Standard
tFTPGet component belongs to the Internet family.

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
| Local directory | The local directory in which downloaded files will be saved. |
| Remote directory | The FTP directory from which files will be downloaded. |
| Transfer mode | Select the transfer mode from the list, either ascii or binary. |
| Overwrite file | Select the action to be performed when the file already exists.   * never: Never   overwrite the file. * always:   Always overwrite the file. * size   different or: Overwrite the file when the file size   is different. * overwrite:   Overwrite the existing file. * resume:   Resume downloading the file from the point of interruption. * append: Add   data to the end of the file without overwriting data.   overwrite, resume, and append are available when the SFTP Support check box is selected. |
| Append | Select this check box to append data at the end of the file in order to avoid overwriting data. |
| SFTP Support | Select this check box to connect to the FTP server via an SFTP connection. Information noteWarning: This option does not work with an HTTPS proxy. If you need an HTTPS proxy, use the tSetProxy component. |
| Authentication method | Select the SFTP authentication method, Public key, Password, or Public key and password.   * Public key:   Enter the path to the private key and the passphrase for the key in   the Private key and   Key Passphrase fields   correspondingly. * Password:   Enter the password required. * Public key and   password: Select this option if the SFTP server requires   both a public key and a password for authentication. In this case, you   need to provide the password, the   private key file, and the   key passphrase in the   corresponding fields.   This property is available only when the SFTP Support check box is selected. |
| Filename encoding | Select this check box to set the encoding used to convert file names from Strings to bytes. It should be the same encoding used on the SFTP server. If the SFTP server's version is greater than 3, the encoding should be `UTF-8`, or else an error occurs.  This property is available only when the SFTP Support check box is selected. |
| FTPS Support | Select this check box to connect to the FTP server via an FTPS connection. If you are using an HTTP proxy, via a tSetProxy component for example, you need to select this check box and set the connection mode to `Passive`.  Information noteNote: If your FTPS server requires session resumption between data and control connections, the tFTP components support this only when the TLS version is set to TLSv1.2 and the following Java 17 JVM properties are configured: ``` -Djdk.tls.client.protocols=TLSv1.2  -Djdk.tls.allowLegacyResumption=true -Djdk.tls.useExtendedMasterSecret=false -Djdk.tls.client.enableSessionTicketExtension=false ```  This configuration is necessary to allow Java 17 to work with session resumption for FTPS connections. |
| Keystore File | The path to your keystore file, a password protected file containing several keys and certificates.  Depending on the FTPS server configuration, an FTPS server private key or a client certificate is needed to establish an FTPS connection. You can store the FTP server private key or your client certificate in the keystore file.  This property is available only when the FTPS Support check box is selected. |
| Keystore Password | The password for your keystore file.  This property is available only when the FTPS Support check box is selected. |
| Security Mode | Select the security mode from the list, either Implicit or Explicit.  This property is available only when the FTPS Support check box is selected. |
| Use Perl5 Regex Expression as Filemask | Select this check box to use Perl5 regular expressions in the or Files field as file filters. This is useful when the name of the file to be processed contains special characters such as parentheses.  For more information about Perl5 regular expression syntax, see [Perl5 Regular Expression Syntax](http://perldoc.perl.org/perlre.html#Regular-Expressions). |
| Files | The names of the files or the paths to the files to be downloaded. You can specify multiple files in a line by using wildcards or a regular expression. |
| Connection mode | Select the connection mode from the list, either Passive or Active. |
| Encoding | Specify the encoding type by selecting an encoding type from the list or selecting CUSTOM and enter the encoding type manually. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any error and continue the Job execution process. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use Socks Proxy | Select this check box if you are using a proxy, and in the Proxy host, Proxy port, Proxy user and Proxy password fields displayed, specify the proxy server settings information. |
| Connection timeout | Specify the timeout value (in ms) for the connection. A value of 0 or any negative values will be ignored. In this case, the default value (that is, 60000ms) will be used. |
| Ignore Failure At Quit (FTP) | Select this check box to ignore library closing errors or FTP closing errors. |
| Print message | Select this check box to display the list of files downloaded on the console. This option is not available if FTPS Support is selected in the Basic settings view. |
| Data Channel Protection Level | The data channel protection level with which data is transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Protection Buffer Size | The maximum size (in bytes) of the encoded data blocks to be transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Enable Remote Verification | Select this option to enable remote verification. This option solves FTPS server architecture compatibility issues. See [setRemoteVerificationEnabled](https://commons.apache.org/proper/commons-net/apidocs/org/apache/commons/net/ftp/FTPClient.html#setRemoteVerificationEnabled-boolean-) for related information.  This option is available when FTPS Support is selected in the Basic settings view. |
| Use strict reply parsing | Select this option to use strict reply parsing. |
| Config client | Select this option to set JSch encryption algorithm properties. To set an encryption algorithm property, add a row in the table that appears by clicking the plus button on the bottom of the table and enter property name and property value in the Client parameter and Value columns. See [Fork of JSch-0.1.55](https://github.com/mwiede/jsch) and the setConfig section at [Class JSch](http://epaul.github.io/jsch-documentation/javadoc/) for related information.  This option is available when the Use an existing connection option is not selected and the SFTP Support option is selected in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_FILE | The number of the files processed. This is an After variable and it returns an integer. |
| CURRENT\_STATUS | The execution result of the component. This is a Flow variable and it returns a string. |
| TRANSFER\_MESSAGES | The file transferred information. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is typically used as a single-component subJob but can also be used as output or end object. |

**Related concepts**  

* [Listing and getting files/folders on an FTP directory](tftpfilelist-tftpconnection-tlogrow-listing-and-getting-files-folders-on-ftp-directory-standard-component "Here is an example of using Talend FTP components to iterate and list all files and folders on an FTP server directory, and then get only text files on that directory to a local directory.")
