<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/ftp/tftpfileproperties · versión 8.0 -->
# tFTPFileProperties

Last updated: 9/30/2026

Retrieves the properties of a specified file on an FTP server.

## tFTPFileProperties Standard properties

These properties are used to configure tFTPFileProperties running in the Standard Job framework.

The Standard
tFTPFileProperties component belongs to the Internet family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Schema and Edit schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.   * abs\_path: the absolute   path of the file. * dirname: the directory   of the file. * basename: the name of   the file. * size: the file size   in bytes. * mtime: the timestamp   indicating the period between the Unix epoch (00:00:00 UTC, Jan 1, 1970) and   the time the file was last modified, measured in milliseconds in the   FTP/FTPS mode and in seconds in the SFTP mode (that is, the SFTP   Support option is selected in the Basic   settings view). * mtime\_string: the   date and time the file was last modified. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Host | The IP address or hostname of the FTP server. |
| Port | The listening port number of the FTP server. |
| Logon type | Select the authentication type to access the FTP server:  * Password: Enter the username and password used to   access the server. * Password and account: Enter the username,   password, as well as the associated user account name.   To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Remote directory | The path to the directory where the file is available. |
| File | The name of the file or the path to the file whose properties will be retrieved. |
| Transfer mode | Select the transfer mode from the list, either ascii or binary. |
| SFTP Support | Select this check box to connect to the FTP server via an SFTP connection. Information noteWarning: This option does not work with an HTTPS proxy. If you need an HTTPS proxy, use the tSetProxy component. |
| Authentication method | Select the SFTP authentication method, Public key, Password, or Public key and password.   * Public key:   Enter the path to the private key and the passphrase for the key in   the Private key and   Key Passphrase fields   correspondingly. * Password:   Enter the password required. * Public key and   password: Select this option if the SFTP server requires   both a public key and a password for authentication. In this case, you   need to provide the password, the   private key file, and the   key passphrase in the   corresponding fields.   This property is available only when the SFTP Support check box is selected. |
| Filename encoding | Select this check box to set the encoding used to convert file names from Strings to bytes. It should be the same encoding used on the SFTP server. If the SFTP server's version is greater than 3, the encoding should be `UTF-8`, or else an error occurs.  This property is available only when the SFTP Support check box is selected. |
| FTPS Support | Select this check box to connect to the FTP server via an FTPS connection. If you are using an HTTP proxy, via a tSetProxy component for example, you need to select this check box and set the connection mode to `Passive`.  Information noteNote: If your FTPS server requires session resumption between data and control connections, the tFTP components support this only when the TLS version is set to TLSv1.2 and the following Java 17 JVM properties are configured: ``` -Djdk.tls.client.protocols=TLSv1.2  -Djdk.tls.allowLegacyResumption=true -Djdk.tls.useExtendedMasterSecret=false -Djdk.tls.client.enableSessionTicketExtension=false ```  This configuration is necessary to allow Java 17 to work with session resumption for FTPS connections. |
| Keystore File | The path to your keystore file, a password protected file containing several keys and certificates.  Depending on the FTPS server configuration, an FTPS server private key or a client certificate is needed to establish an FTPS connection. You can store the FTP server private key or your client certificate in the keystore file.  This property is available only when the FTPS Support check box is selected. |
| Keystore Password | The password for your keystore file.  This property is available only when the FTPS Support check box is selected. |
| Security Mode | Select the security mode from the list, either Implicit or Explicit.  This property is available only when the FTPS Support check box is selected. |
| Connection mode | Select the connection mode from the list, either Passive or Active. |
| Encoding | Specify the encoding type by selecting an encoding type from the list or selecting CUSTOM and enter the encoding type manually. |
| Calculate MD5 Hash | Select this check box to check the file's MD5. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use Socks Proxy | Select this check box if you are using a proxy, and in the Proxy host, Proxy port, Proxy user and Proxy password fields displayed, specify the proxy server settings information. |
| Ignore Failure At Quit (FTP) | Select this check box to ignore library closing errors or FTP closing errors. |
| Data Channel Protection Level | The data channel protection level with which data is transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Protection Buffer Size | The maximum size (in bytes) of the encoded data blocks to be transferred between the client and the server. For more information, see [RFC 2228: FTP Security Extensions](https://www.rfc-editor.org/rfc/rfc2228.txt).  This property is available only when the FTPS Support check box is selected. |
| Connection timeout | Specify the timeout value (in ms) for the connection. A value of 0 or any negative values will be ignored. In this case, the default value (that is, 60000ms) will be used. |
| Enable Remote Verification | Select this option to enable remote verification. This option solves FTPS server architecture compatibility issues. See [setRemoteVerificationEnabled](https://commons.apache.org/proper/commons-net/apidocs/org/apache/commons/net/ftp/FTPClient.html#setRemoteVerificationEnabled-boolean-) for related information.  This option is available when FTPS Support is selected in the Basic settings view. |
| Use strict reply parsing | Select this option to use strict reply parsing. |
| Config client | Select this option to set JSch encryption algorithm properties. To set an encryption algorithm property, add a row in the table that appears by clicking the plus button on the bottom of the table and enter property name and property value in the Client parameter and Value columns. See [Fork of JSch-0.1.55](https://github.com/mwiede/jsch) and the setConfig section at [Class JSch](http://epaul.github.io/jsch-documentation/javadoc/) for related information.  This option is available when the Use an existing connection option is not selected and the SFTP Support option is selected in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-07 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as standalone component. |
