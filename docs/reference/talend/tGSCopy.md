<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy · versión 8.0 -->
# tGSCopy

Last updated: 9/30/2026

Copies or moves objects within a bucket or between buckets in Google Cloud
Storage.

tGSCopy streamlines processes by automating the copy tasks..

## tGSCopy Standard properties

These properties are used to configure tGSCopy running in the Standard Job framework.

The Standard
tGSCopy component belongs to the Big Data and the Cloud families.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and in the Component List click the relevant connection component to reuse the connection details you already defined. |
| Credential type | Select the mode to be used to authenticate to your project.  * Service account: authenticate using a Google account   that is associated with your Google Cloud Platform project. When selecting this   mode, the access key must be provided in the Service account   key field. * Workload Identity Federation: authenticate using an   external identity provider, such as AWS, Azure, or OIDC, without needing a   service account key. When selecting this mode, the identity federation   configuration must be provided in the Client library configuration   file field. * Application Default Credentials: authenticate using the   Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based on   the application environment. * OAuth Access Token: authenticate using an OAuth access   token. When selecting this mode, the token must be provided in the   OAuth Access Token field.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Service account key | Click the [...] button next to the service account key field to browse for the JSON file that contains your service account key.  This property is only available when you authenticate using Service account. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit. This property is only available when you authenticate using OAuth Access Token. |
| Source bucket name | Specify the name of the bucket from which you want to copy or move objects. |
| Project ID | When the credential type is set to OAuth Access Token, specify the project ID from which you want to copy or move objects. |
| Source object key | Specify the key of the object to be copied. |
| Source is folder | Select this check box if the source object is a folder. |
| Target bucket name | Specify the name of the bucket to which you want to copy or move objects. |
| Target folder | Specify the target folder to which the objects will be copied or moved. |
| Action | Select the action that you want to perform on objects from the list.   * Copy: copies objects from the   source bucket or folder to the target bucket or folder. * Move: moves objects from the   source bucket or folder to the target bucket or folder. |
| Rename | Select this check box and in the New name field enter a new name for the object to be copied or moved.  The Rename check box will not be available if you select the Source is folder check box. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use a custom endpoint | Select this check box to use a private endpoint rather than the default one. When selected, enter the URL in the Google Storage Private API URL property, by respecting the following format: "https://storage.goggleapis.com".  For more information, see [Access Google APIs through endpoints](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis) from Google documentation.  This property is only available when you authenticate using Service account and Application Default Credentials. |
| Use source path | Select this check box to add paths while copying or moving items in the same bucket or several ones.  When you select the Rename check box from the Basic settings view, the Use source path option does not work. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | SOURCE\_BUCKET: the source bucket name. This is an After variable and it returns a string.  SOURCE\_OBJECTKEY: the key of a source object. This is an After variable and it returns a string.  DESTINATION\_BUCKETNAME: the destination bucket name. This is an After variable and it returns a string.  DESTINATION\_FOLDER: the destination folder. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a standalone component. |

**Related concepts**  

* [Managing files with Google Cloud Storage](tgscopy-tgslist-tlogrow-managing-files-with-google-cloud-storage-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-managing-files-with-google-cloud-storage-standard-component-the -->
# Managing files with Google Cloud Storage

Last updated: 9/30/2026

The scenario describes a Job which uploads files from the local directory to a
bucket in Google Cloud Storage, then performs copy, move and delete operations on those
files, and finally lists and displays the files in relevant buckets on the console.

Prerequisites: You have purchased a Google Cloud
Storage account and created three buckets under the same Google Storage directory. In this
example, the buckets created are bighouse, bed\_room, and study\_room.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-dropping-and-linking-components-standard-component-to)
* [Configuring the components](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tGSCopy](tgscopy "Copies or moves objects within a bucket or between buckets in Google Cloud Storage.")
* [tGSList](tgslist "Retrieves a list of objects from Google Cloud Storage one by one.")
* [tGSPut](tgsput "Uploads files from a local directory to Google Cloud Storage so that you can manage them with Google Cloud Storage.")
* [tGSDelete](tgsdelete "Deletes the objects which match the specified criteria in Google Cloud Storage so as to release the occupied resources.")
* [tGSConnection](tgsconnection "Provides the authentication information for making requests to the Google Cloud Storage system and enables the reuse of the connection it creates to Google Cloud Storage.")
* [tGSClose](tgsclose "Closes an active connection to Google Cloud Storage in order to release the occupied resources.")

**Related information**  

* [tIterateToFlow](/talend/en-US/components/8.0/orchestration/titeratetoflow)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Opening a connection to Google Cloud Storage](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-opening-connection-to-google-cloud-storage-standard-component)
* [Uploading files to Google Cloud Storage](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-uploading-files-to-google-cloud-storage-standard-component)
* [Copying all files from one bucket to another bucket](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-copying-all-files-from-one-bucket-to-another-bucket-standard-component)
* [Moving a file from one bucket to another bucket and renaming it](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-moving-file-from-one-bucket-to-another-bucket-and-renaming-it-standard-component)
* [Deleting a file in one bucket](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-deleting-file-in-one-bucket-standard-component)
* [Listing all files in the three buckets](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-listing-all-files-in-three-buckets-standard-component)
* [Closing the connection to Google Cloud Storage](/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-closing-connection-to-google-cloud-storage-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-dropping-and-linking-components-standard-component-to -->
# Dropping and linking the components

Last updated: 9/30/2026

## About this task

To design the Job, proceed as follows:

## Procedure

1. Drop the following components from the Palatte to design the workspace: one tGSConnection component, one tGSPut component, two tGSCopy components, one tGSDelete component, one tGSList component, one tIterateToFlow component, one tLogRow component and one tGSClose component.
2. Connect tGSConnection to tGSPut using a Trigger > On
   Subjob Ok link.
3. Connect tGSPut to the first tGSCopy using a Trigger >
   On Subjob Ok link.
4. Do the same to connect the first tGSCopy
   to the second tGSCopy, connect the second
   tGSCopy to tGSDelete, connect tGSDelete to tGSList, and
   connect tGSList to tGSClose.
5. Connect tGSList to tIterateToFlow using a Row >
   Iterate link.
6. Connect tIterateToFlow to tLogRow using a Row >
   Main link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Execute the Job by pressing F6 or
   clicking Run on the Run tab.

   The files in the three buckets are displayed. As expected, at first, the
   files from the bucket *bighouse* are copied
   to the bucket *bed\_room*, then the file
   *computer\_01.txt* from the bucket
   *bighouse* is moved to the bucket
   *study\_room* and renamed to be
   *laptop.txt*, finally the file
   *computer\_03.csv* is deleted from the
   bucket *bed\_room*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-closing-connection-to-google-cloud-storage-standard-component -->
# Closing the connection to Google Cloud Storage

Last updated: 9/30/2026

## Procedure

1. Double-click the tGSClose component to
   open its Basic settings view in the
   Component tab.
2. Select the connection you want to close from the Component List.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-copying-all-files-from-one-bucket-to-another-bucket-standard-component -->
# Copying all files from one bucket to another bucket

Last updated: 9/30/2026

## Procedure

1. Double-click the first tGSCopy component
   to open its Basic settings view in the
   Component tab.
2. Select the Use an existing connection
   check box and then select the connection you have configured earlier.
3. In the Source bucket name field, enter
   the name of the bucket from which you want to copy files, *bighouse* in this example.
4. Select the Source is a folder check box.
   All files from the bucket *bighouse* will
   be copied.
5. In the Target bucket name field, enter
   the name of the bucket into which you want to copy files, *bed\_room* in this example.
6. Select Copy from the Action list.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-deleting-file-in-one-bucket-standard-component -->
# Deleting a file in one bucket

Last updated: 9/30/2026

## Procedure

1. Double-click the tGSDelete component to
   open its Basic settings view in the
   Component tab.
2. Select the Use an existing connection
   check box and then select the connection you have configured earlier.
3. Select the Delete object from bucket list
   check box. Fill in the Bucket table with
   the file information that you want to delete. 

   In this example, the file *computer\_03.csv* will be deleted from the bucket *bed\_room* whose files are copied from the bucket
   *bighouse*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-listing-all-files-in-three-buckets-standard-component -->
# Listing all files in the three buckets

Last updated: 9/30/2026

## Procedure

1. Double-click the tGSList component to
   open its Basic settings view in the
   Component tab.
2. Select the Use an existing connection
   check box and then select the connection you have configured earlier.
3. Select the List objects in bucket list
   check box. In the Bucket table, enter the
   name of the three buckets in the *Bucket
   name* column, *bighouse*,
   *study\_room*, and *bed\_room*.
4. Double-click the tIterateToFlow component
   to open its Basic settings view in the
   Component tab.
5. Click Edit schema to define the data to
   pass on to tLogRow.

   In this example, add two columns *bucketName* and *key*, and
   set their types to Object.
6. The Mapping table will be populated with
   the defined columns automatically.

   In the *Value* column, enter *globalMap.get("tGSList\_2\_CURRENT\_BUCKET")* for
   the *bucketName* column and *globalMap.get("tGSList\_2\_CURRENT\_KEY")* for the
   *key* column. You can also press
   Ctrl + Space and then choose the
   appopriate variable.
7. Double-click the tLogRow component to
   open its Basic settings view in the
   Component tab.
8. Select Table (print values in cells of a
   table) for a better view of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-moving-file-from-one-bucket-to-another-bucket-and-renaming-it-standard-component -->
# Moving a file from one bucket to another bucket and renaming it

Last updated: 9/30/2026

## Procedure

1. Double-click the second tGSCopy component
   to open its Basic settings view in the
   Component tab.
2. Select the Use an existing connection
   check box and then select the connection you have configured earlier.
3. In the Source bucket name field, enter
   the name of the bucket from which you want to move files, *bighouse* in this example.
4. In the Source object key field, enter the
   key of the object to be moved, *computer\_01.txt* in this example.
5. In the Target bucket name field, enter
   the name of the bucket into which you want to move files, *study\_room* in this example.
6. Select Move from the Action list. The specified source file *computer\_01.txt* will be moved from the bucket
   *bighouse* to *study\_room*.
7. Select the Rename check box. In the
   New name field, enter a new name for
   the moved file. In this example, the new name is *laptop.txt*.
8. Leave other settings as they are.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-opening-connection-to-google-cloud-storage-standard-component -->
# Opening a connection to Google Cloud Storage

Last updated: 9/30/2026

## Procedure

1. Double-click the tGSConnection component
   to open its Basic settings view in the
   Component tab.
2. In the Credential type list,
   select Application Default Credentials. When selecting this
   mode, no additional parameters need to be defined as credentials are automatically
   found based on the application environment.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/gs/tgscopy-tgslist-tlogrow-uploading-files-to-google-cloud-storage-standard-component -->
# Uploading files to Google Cloud Storage

Last updated: 9/30/2026

## Procedure

1. Double-click the tGSPut component to open
   its Basic settings view in the Component tab.
2. Select the Use an existing connection
   check box and then select the connection you have configured earlier.
3. In the Bucket name field, enter the name
   of the bucket into which you want to upload files. In this example,
   *bighouse*.
4. In the Local directory field, browse to
   the directory from which the files will be uploaded, *D:/Input/House* in this example.

   The files under this directory are shown below:
5. Leave other settings as they are.
