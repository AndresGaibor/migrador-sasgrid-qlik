<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput · versión 8.0 -->
# tGoogleDrivePut

Last updated: 9/30/2026

Uploads data from a data flow or a local file to Google Drive.

## tGoogleDrivePut Standard properties

These properties are used to configure tGoogleDrivePut running in the Standard Job framework.

The Standard
tGoogleDrivePut component belongs to the Cloud family.

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
| File Name | The name for the file after being uploaded. |
| Destination Folder | The name or ID of the folder in which uploaded data will be stored. |
| Access Method | Select the method by which the destination folder is specified, either `by Name` or `by Id`. |
| Replace if Existing | Select this check box to overwrite any existing file with the newly uploaded one. |
| Upload Mode | Select one of the following upload modes from the drop-down list:   * Upload Incoming content as File: Select this   option to upload data from an input flow of the preceding component. * Upload Local File: Select this option to upload   data from a local file. In the File field   displayed, specify the path to the file to be uploaded. * Expose As OutputStream: Select this option to   expose output stream of this component, which can be used by other   components to write the file content. For example, you can use the   Use Output Stream feature of the   tFileOutputDelimited component to feed a given   tGoogleDrivePut's exposed output stream. For   more information, see [tFileOutputDelimited](/talend/r/en-US/8.0/components/delimited/tfileoutputdelimited). |
| Schema and Edit schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.  The schema of this component is read-only. You can click the [...] button next to Edit schema to view the predefined schema which contains the following fields:   * content: The content of the uploaded data. * parentFolderId: The ID of the parent folder. * fileId: The ID of the file. |

## Advanced settings

| Properties | Description |
| --- | --- |
| DataStore Path | The path to the credential file that stores the refresh token.  Information noteNote: When your client ID, client secret, or any other configuration related to the Installed Application authentication changes, you need to delete this credential file manually before running your Job again.  This property is available only when `Installed Application (Id & Secret)` or `Installed Application (JSON)` is selected from the OAuth Method drop-down list. |
| Read Timeout | Enter the read timeout value in seconds. An exception will occur if the timeout expires before there is data available for read. The default value is 30 and `0` means an infinite time out. This option is available if the component does not use an existing connection. |
| Include shared folders/files | Select this check box to take into account files and folders that have been shared with you. |
| Include shared drives | Select this check box to take into account drives that have been shared with you.  It is recommended to use the `by Id` Access Method in Basic settings when you select this check box, as using the `by Name` Access Method can affect performance. |
| Corpora type | Select a type of Corpora to narrow the scope of file and folder searches:  * User to query files that you have accessed,   including both shared drive and My Drive files. * Drive to query all items in the specified   shared drive. Specify the drive ID in the Drive   ID field. * Domain to query files that are shared to the   domain, including both shared drive and My Drive files. * All drives to query files that you have   accessed and all shared drives in which you are a member. This   corpora type can affect performance as it has a broad scope.  By default, User is the selected value.  This property is available only when the Include shared drives check box is selected. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| PARENT\_FOLDER\_ID | The ID of the parent folder. This is an After variable and it returns a string. |
| FILE\_ID | The ID of the file. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a standalone component to upload a local file to Google Drive or an end component to upload data from an input flow of the preceding component to Google Drive. |

**Related concepts**  

* [Managing files with Google Drive](tgoogledriveput-tgoogledriveconnection-tfileinputraw-managing-files-with-google-drive-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-managing-files-with-google-drive-standard-component-this -->
# Managing files with Google Drive

Last updated: 9/30/2026

This scenario describes a Job that uploads two files to an empty folder
`Talend` in the root directory of Google Drive, then creates a new
folder `Talend Backup` in the root directory and copies one of the two
files to the new folder `Talend Backup`, and finally lists and
displays all files and folders in the root directory of Google Drive on the console.

### In this section

* [Creating a Job for managing files with Google Drive](/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-creating-job-for-managing-files-with-google-drive-standard-component-create)
* [Opening a connection to Google Drive](/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-opening-connection-to-google-drive-standard-component-the)
* [Uploading files to Google Drive](/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-uploading-files-to-google-drive-standard-component)
* [Creating a new folder in Google Drive](/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-creating-new-folder-in-google-drive-standard-component)
* [Copying a file to the newly created folder](/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-copying-file-to-newly-created-folder-standard-component)
* [Listing files and folders in Google Drive](/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-listing-files-and-folders-in-google-drive-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tGoogleDrivePut](tgoogledriveput "Uploads data from a data flow or a local file to Google Drive.")
* [tGoogleDriveConnection](tgoogledriveconnection "Opens a Google Drive connection that can be reused by other Google Drive components.")
* [tGoogleDriveCreate](tgoogledrivecreate "Creates a new folder in Google Drive.")
* [tGoogleDriveCopy](tgoogledrivecopy "Creates a copy of a file/folder in Google Drive.")
* [tGoogleDriveList](tgoogledrivelist "Lists all files, or folders, or both files and folders in a specified Google Drive folder, in the domain, including both Shared Drive and My Drive, and all shared drives.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFileInputRaw](/talend/en-US/components/8.0/raw/tfileinputraw)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-copying-file-to-newly-created-folder-standard-component -->
# Copying a file to the newly created folder

Last updated: 9/30/2026

## Procedure

1. Double-click the tGoogleDriveCopy component to open its Basic settings view in the Component tab.
2. Select the component that will create the Google Drive connection from the
   Connection Component drop-down list, `tGoogleDriveConnection_1`
   in this example.
3. Select `File` from the Copy Mode
   drop-down list.
4. In the Source field, enter
   the name of the file to be copied. In this example, it is `Talend
   Customers.csv`.
5. In the Destination Folder
   Name field, enter the name of the folder to which the file will be
   copied. In this example, it is `Talend Backup`.
6. Select the Rename (set new
   title) check box and in the Destination
   Name field, enter a new name for the file after being copied to the
   destination folder. In this example, it is `Talend Customers
   v1.0.csv.`
7. Double-click the fourth tLogRow component to open its Basic
   settings view in the Component
   tab.
8. In the Mode area, select
   Vertical (each row is a key/value list) for a better
   display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-creating-job-for-managing-files-with-google-drive-standard-component-create -->
# Creating a Job for managing files with Google Drive

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a
   tGoogleDriveConnection component, two
   tGoogleDrivePut components, a
   tFileInputRaw component, a
   tGoogleDriveCreate component, a
   tGoogleDriveCopy component, a
   tGoogleDriveList component, and five
   tLogRow components to the Job.
2. Link the first tGoogleDrivePut component to the first
   tLogRow component using a Row > Main connection.
3. Do the same to link the tFileInputRaw component to the
   second tGoogleDrivePut component, the second
   tGoogleDrivePut component to the second
   tLogRow component, the
   tGoogleDriveCreate component to the third
   tLogRow component, the
   tGoogleDriveCopy component to the fourth
   tLogRow component, the
   tGoogleDriveList component to the fifth
   tLogRow component.
4. Link the tGoogleDriveConnection component to the first tGoogleDrivePut component using a Trigger > On Subjob Ok connection.
5. Do the same to link the first tGoogleDrivePut component to the
   tFileInputRaw component, the
   tFileInputRaw component to the tGoogleDriveCreate component, the tGoogleDriveCreate component to the tGoogleDriveCopy component, and the tGoogleDriveCopy component to the tGoogleDriveList component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-creating-new-folder-in-google-drive-standard-component -->
# Creating a new folder in Google Drive

Last updated: 9/30/2026

## Procedure

1. Double-click tGoogleDriveCreate to open its Basic
   settings view in the Component
   tab.
2. Select the component that will create the Google Drive connection from the
   Connection Component drop-down list, `tGoogleDriveConnection_1`
   in this example.
3. In the Parent Folder field,
   enter the name of the folder in which a new folder will be created. In this example,
   it is `root`.
4. In the New Folder Name
   field, enter the name of the folder to be created. In this example, it is
   `Talend Backup`.
5. Double-click the third tLogRow component to open its Basic
   settings view in the Component
   tab.
6. In the Mode area, select
   Vertical (each row is a key/value list) for a better
   display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-listing-files-and-folders-in-google-drive-standard-component -->
# Listing files and folders in Google Drive

Last updated: 9/30/2026

## Procedure

1. Double-click the tGoogleDriveList component to open its Basic settings view in the Component tab.
2. Select the component that will create the Google Drive connection from the
   Connection Component drop-down list, `tGoogleDriveConnection_1`
   in this example.
3. In the Folder Name field,
   enter the name of the folder in which the files/folders will be listed. In this
   example, it is the root directory of Google Drive and you can use the alias
   `root` to refer to it.
4. Select Both from the
   FileList Type drop-down list to list both
   files and folders in the root directory.
5. Select the Include SubDirectories check box
   to list also the files/folders in the subdirectories.
6. Double-click the fifth tLogRow component to open its Basic
   settings view in the Component
   tab.
7. In the Mode area, select
   Vertical (each row is a key/value list) for a better
   display of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-opening-connection-to-google-drive-standard-component-the -->
# Opening a connection to Google Drive

Last updated: 9/30/2026

Configure the tGoogleDriveConnection component to connect to Google Drive using a
client secret JSON file.

## Before you begin

* The client secret JSON file has been downloaded into a local folder through Google
  API Console. For more information, see [How to access Google Drive using a client secret JSON file](/talend/en-US/components/8.0/google-drive/how-to-access-google-drive-using-client-secret-json-file-the).
* An empty folder `Talend` has been created in the root
  directory of Google Drive.

## Procedure

1. Double-click the tGoogleDriveConnection
   component to open its Basic settings view in the
   Component tab.
2. In the Application Name field, enter the application name
   required by Google Drive to get access to its API. In this example, it is
   `TalendProject`.
3. Select `Installed Application (JSON)` from the
   OAuth Method drop-down list.
4. In the Client Secret JSON field, specify the path to the
   client secret JSON file you have generated,
   `D:/client_secret.json` in this example.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the
   Job.
2. Execute the Job by pressing F6 or clicking Run on the
   Run tab.

   As shown above, two files `Talend Products.txt` and
   `Talend Customers.csv` were uploaded to the folder
   `Talend`, then a new folder `Talend
   Backup` was created in the root folder and the file
   `Talend Customers.csv` was copied to the new folder and
   renamed to `Talend Customers v1.0.csv`, and finally all files
   and folders in the root directory are listed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-drive/tgoogledriveput-tgoogledriveconnection-tfileinputraw-uploading-files-to-google-drive-standard-component -->
# Uploading files to Google Drive

Last updated: 9/30/2026

## Procedure

1. Double-click the first tGoogleDrivePut
   component to open its Basic settings view in
   the Component tab.
2. Select the component that will create the Google Drive connection from the
   Connection Component drop-down list,
   `tGoogleDriveConnection_1` in this example.
3. Select `by Name` from the Access Method
   drop-down list and in the Destination Folder field, enter the
   name of the folder in which the file will be uploaded, `Talend`
   in this example.

   Information noteNote: When accessing a Google Drive resource by its name, if the name matches more
   than one resource, an error will be thrown because the resource cannot be
   identified precisely. In this case, you can specify the Google Drive resource
   using a pseudo path hierarchy, like `/Talend/Documentation`.
   This example specifies a folder named `Documentation` under
   the folder `Talend` under the Google Drive
   `root` folder.
4. In the File Name field, enter the name for the file after
   being uploaded. In this example, it is `Talend
   Customers.csv`.
5. Select `Upload Local File` from the Upload Mode drop-down list and in the File field, browse to or enter the path to the file to
   be uploaded. In this example, it is `D:/Downloads/Talend
   Customers.csv`.
6. Double-click the tFileInputRaw component and on its
   Basic settings view, select `Read the file as a
   bytes array` in the Mode area and specify the
   path to the file whose content will be uploaded in the
   Filename field, `D:/Downloads/Talend
   Products.txt` in this example.
7. Double-click the second tGoogleDrivePut component to open
   its Basic settings view in the Component tab.
8. Repeat step [2](tgoogledriveput-tgoogledriveconnection-tfileinputraw-uploading-files-to-google-drive-standard-component) to step [3](tgoogledriveput-tgoogledriveconnection-tfileinputraw-uploading-files-to-google-drive-standard-component) to configure this component.
9. In the File Name field, enter the name for the file after
   being uploaded. In this example, it is `Talend
   Products.txt`.
10. Select `Upload Incoming content as File` from the
    Upload Mode drop-down list.
