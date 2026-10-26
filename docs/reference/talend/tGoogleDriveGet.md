<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveget · versión 8.0 -->
# tGoogleDriveGet

Last updated: 9/30/2026

Gets a file's content and downloads the file to a local directory.

## tGoogleDriveGet Standard properties

These properties are used to configure tGoogleDriveGet running in the Standard Job framework.

The Standard
tGoogleDriveGet component belongs to the Cloud family.

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
| File | The name or ID of the file to be downloaded. |
| Access Method | Select the method by which the file to be downloaded is specified, either `by Name` or `by Id`. |
| Save as File | Select this check box to save the file to a local directory. In the Save to field displayed, browse to or enter the path where you want to save the file to be downloaded. |
| Schema and Edit schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.  The schema of this component is read-only. You can click the [...] button next to Edit schema to view the predefined schema with only one field named content which describes the content of the file to be downloaded. |

## Advanced settings

| Properties | Description |
| --- | --- |
| DataStore Path | The path to the credential file that stores the refresh token.  Information noteNote: When your client ID, client secret, or any other configuration related to the Installed Application authentication changes, you need to delete this credential file manually before running your Job again.  This property is available only when `Installed Application (Id & Secret)` or `Installed Application (JSON)` is selected from the OAuth Method drop-down list. |
| Read Timeout | Enter the read timeout value in seconds. An exception will occur if the timeout expires before there is data available for read. The default value is 30 and `0` means an infinite time out. This option is available if the component does not use an existing connection. |
| Include shared folders/files | Select this check box to take into account files and folders that have been shared with you. |
| Include shared drives | Select this check box to take into account drives that have been shared with you.  It is recommended to use the `by Id` Access Method in Basic settings when you select this check box, as using the `by Name` Access Method can affect performance. |
| Corpora type | Select a type of Corpora to narrow the scope of file and folder searches:  * User to query files that you have accessed,   including both shared drive and My Drive files. * Drive to query all items in the specified   shared drive. Specify the drive ID in the Drive   ID field. * Domain to query files that are shared to the   domain, including both shared drive and My Drive files. * All drives to query files that you have   accessed and all shared drives in which you are a member. This   corpora type can affect performance as it has a broad scope.  By default, User is the selected value.  This property is available only when the Include shared drives check box is selected. |
| Export Google Doc as | Select the type for the Google Doc to be exported. |
| Export Google Draw as | Select the type for the Google Draw to be exported. |
| Export Google Presentation as | Select the type for the Google Presentation to be exported. |
| Export Google Spreadsheet as | Select the type for the Google Spreadsheet to be exported. |
| Add extension | Select this check box to add extension to the exported file. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| FILE\_ID | The ID of the file. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component or as a start component of a Job or subJob.  If you use this component as a standalone component:  * When you select the Save as File checkbox, the   file is saved to disk, and can be larger than 2 GB. * When you leave the Save as File checkbox cleared,   the file is cached in the memory, and cannot be larger than 2 GB   otherwise you encounter the OutOfMemoryError error.  If you use this component as a start component of a Job or subJob:  * When you select the Save as File checkbox, the   file is cached in the memory first, then saved to disk, and streamed to   Talend Studio. The file cannot be larger than 2 GB otherwise you encounter the   OutOfMemoryError error. * When you leave the Save as File checkbox cleared,   the file is cached in the memory, and then streamed to Talend Studio. The file cannot be larger than 2 GB otherwise you encounter the   OutOfMemoryError error. |
