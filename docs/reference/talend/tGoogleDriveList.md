<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledrivelist · versión 8.0 -->
# tGoogleDriveList

Last updated: 9/30/2026

Lists all files, or folders, or both files and folders in a specified Google Drive
folder, in the domain, including both Shared Drive and My Drive, and all shared
drives.

## tGoogleDriveList Standard properties

These properties are used to configure tGoogleDriveList running in the Standard Job framework.

The Standard
tGoogleDriveList component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Component list | Select the component that opens the database connection to be reused by this component. |
| Application Name | The application name required by Google Drive to get access to its APIs. |
| OAuth Method | Select an OAuth method used to access Google Drive from the drop-down list.   * Installed Application (Id   & Secret): uses the client ID and client secret   created through Google API Console to access Google Drive. For more   information about this method, see [Google Identity Platform >   Installed applications](https://developers.google.com/identity/protocols/OAuth2#installed) . * Installed Application   (JSON): uses the client secret JSON file that is   created through Google API Console and contains the client ID,   client secret, and other OAuth 2.0 parameters to access Google   Drive. * Service   Account: uses a service account JSON file created   through Google API Console to access Google Drive. For more   information about this method, see [Google Identity Platform >   Service accounts](https://developers.google.com/identity/protocols/OAuth2#serviceaccount).   For more information about how to access Google Drive using each method, see [OAuth methods for accessing Google Drive](/talend/r/en-US/8.0/components/google-drive/oauth-methods-for-accessing-google-drive). |
| Client ID and Client Secret | The client ID and client secret.  These two properties are available only when `Installed Application (Id & Secret)` is selected from the OAuth Method drop-down list. |
| Client Secret JSON | The path to the client secret JSON file.  This property is available only when `Installed Application (JSON)` is selected from the OAuth Method drop-down list. |
| Service Account JSON | The path to the service account JSON file.  This property is available only when `Service Account` is selected from the OAuth Method drop-down list. |
| Use Proxy | Select this check box when you are working behind a proxy. With this check box selected, you need to specify the value for the following parameters:   * Host: The IP   address of the HTTP proxy server. * Port: The port   number of the HTTP proxy server. |
| Use SSL | Select this check box if an SSL connection is used to access Google Drive. With this check box selected, you need to specify the value for the following parameters:   * Algorithm: The   name of the SSL cryptography algorithm. * Keystore File:   The path to the certificate TrustStore file that contains the list   of certificates the client trusts. * Password: The   password used to check the integrity of the TrustStore data. |
| Folder Name | The name or ID of the folder in which the files/folders will be listed. |
| Access Method | Select the method by which the folder is specified, either `by Name` or `by Id`. |
| FileList Type | Select the type of data you want to list.   * Files: Only   files. * Directories: Only   folders. * Both: Both files   and folders. |
| Include SubDirectories | Select this check box to list also the files/folders in the subdirectories. |
| Schema and Edit schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.  The schema of this component is read-only. You can click the [...] button next to Edit schema to view the predefined schema which contains the following fields:   * id: The ID of the   file/folder. * name: The name of   the file/folder. * mimeType: The MIME type of the file/folder. * modifiedTime: The last modification date of the   file/folder. * size: The file size in bytes. * kind: The kind of the resource. * trashed: Whether the file has been trashed. * parents: The ID of the parent folder. * webViewLink: A link for opening the file in a   Google editor or viewer in a browser. |

## Advanced settings

| Properties | Description |
| --- | --- |
| DataStore Path | The path to the credential file that stores the refresh token.  Information noteNote: When your client ID, client secret, or any other configuration related to the Installed Application authentication changes, you need to delete this credential file manually before running your Job again.  This property is available only when `Installed Application (Id & Secret)` or `Installed Application (JSON)` is selected from the OAuth Method drop-down list. |
| Read Timeout | Enter the read timeout value in seconds. An exception will occur if the timeout expires before there is data available for read. The default value is 30 and `0` means an infinite time out. This option is available if the component does not use an existing connection. |
| Use query | Select this check box to customize your searches.  If you select this check box, trashed files are included by default.  If you select this check box, the Include trashed files option is hidden in Advanced settings and the Include SubDirectories option is hidden in Basic settings. |
| Query | Type in a query to search for specific files and folders. For more information about the query syntax, see <https://developers.google.com/drive/api/v3/search-files#query_string_examples>.  This property is available only when the Use query check box is selected. |
| Include shared folders/files | Select this check box to take into account files and folders that have been shared with you. |
| Include trashed files | Select this check box to also take into account files and folders that have been removed from the specified path. |
| Include shared drives | Select this check box to take into account drives that have been shared with you.  It is recommended to use the `by Id` Access Method in Basic settings when you select this check box, as using the `by Name` Access Method can affect performance. |
| Corpora type | Select a type of Corpora to narrow the scope of file and folder searches:  * User to query files that you have accessed,   including both shared drive and My Drive files. * Drive to query all items in the specified   shared drive. Specify the drive ID in the Drive   ID field. * Domain to query files that are shared to the   domain, including both shared drive and My Drive files. * All drives to query files that you have   accessed and all shared drives in which you are a member. This   corpora type can affect performance as it has a broad scope.  By default, User is the selected value.  This property is available only when the Include shared drives check box is selected. |
| Page size | Set the maximum number of files to return per page. You can set a value between 1 and 1000 included. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is usually used as a start component of a Job or subJob and it always needs an output link. |

**Related concepts**  

* [Managing files with Google Drive](tgoogledriveput-tgoogledriveconnection-tfileinputraw-managing-files-with-google-drive-standard-component-this)
