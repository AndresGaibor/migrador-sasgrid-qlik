<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-internet/cftp · versión 8.0 -->
# cFtp

Last updated: 9/30/2026

Provides access to remote file systems over the FTP, FTPS and SFTP
protocols.

For more information, see the Apache camel documentation <https://camel.apache.org/components/latest/>.

## cFtp Standard properties

These properties are used to configure cFtp running in the Standard Job framework.

The Standard
cFtp component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Parameters/type | Select the file transfer protocol, ftp or sftp, ftps. |
| Parameters/server | Type in the remote server address to be accessed. |
| Parameters/port | Type in the port number to be accessed. |
| Parameters/username | Type in the user authentication information. |
| Parameters/password | Type in the user authentication information. To enter the password, click the [...] button next to the password field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings. |
| Parameters/directory | Enter the directory you want to access on the remote server. If not specified, the root directory will be accessed. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced | Set the optional arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Then click the corresponding Value field and enter a value. See the site <http://camel.apache.org/ftp.html> for available URI options. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cFtp can be a start, middle or end component in a Route. |
