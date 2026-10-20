<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist · versión 8.0 -->
# tMongoDBGridFSList

Last updated: 9/30/2026

Retrieves a list of files based on a query.

tMongoDBGridFSList iterates on files
of a bucket in MongoDB GridFS.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMongoDBGridFSList Standard properties

These properties are used to configure tMongoDBGridFSList running in the Standard Job framework.

The Standard
tMongoDBGridFSList component belongs to the Big Data and the Databases NoSQL families.

The component in this framework is available in all Talend products
with Big Data and in Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
| Use existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that when a Job contains the parent Job and the child Job, Component List presents only the connection components in the same Job level. |
| DB Version | List of the database versions.  Available when the Use existing connection check box is not selected. |
| Use connection string | Select this option to establish a connection using a MongoDB Atlas URI. Enter the URI in the field to the right. See [Connection String URI Format](https://docs.mongodb.com/manual/reference/connection-string/) for related information.  This option is available when you select `MongoDB 4.4.X and later` from the DB Version drop-down list.  Information noteNote: This option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use replica set address or multiple query routers | Select this check box to show the Server addresses table.  In the Server addresses table, define the shared MongoDB databases or the MongoDB replica sets you want to connect to. |
| Server and Port | IP address and listening port of the database server.  Available when the Use replica set address check box is not selected.  Note that if you use the authentication mechanisms to connect to this MongoDB database, you must enter the name, rather than the IP address, of the host of the database server. |
| Database | Name of the database. |
| Use SSL connection (Configure the SSL authentication in tSetKeystore or in Studio preferences) | Select this checkbox to enable the SSL or TLS encrypted connection.  Then you need to use the tSetKeystore component in the same Job to specify the encryption information.  Note that the SSL connection is available only for the version 2.4 + of MongoDB. |
| Set read preference | Select this check box and from the Read preference drop-down list that is displayed, select the member to which you need to direct the read operations.  If you leave this check box clear, the Job uses the default Read preference, that is to say, uses the primary member in a replica set.  For further information, see MongoDB's documentation about Replication and its Read preferences. |
| Use authentication | Select this check box to enable the database authentication.  Among the mechanisms listed on the Authentication mechanism drop-down list, the NEGOTIATE one is recommended if you are not using Kerberos, because it automatically select the authentication mechanism the most adapted to the MongoDB version you are using.  Because the SCRAM-SHA-256 authentication mechanism is only supported by MongoDB 4.x and later versions, `SCRAM-SHA-256 SASL` option is available only when `MongoDB 4.4.X and later` is selected from the DB Version drop-down list.  Information noteNote: The `X509` option is available only when you have installed the R2021-12 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.  For details about the other mechanisms in this list, see [MongoDB Authentication](https://docs.mongodb.org/manual/reference/parameters/#param.authenticationMechanisms) from the MongoDB documentation. |
| Set Authentication database | If the username to be used to connect to MongoDB has been created in a specific Authentication database of MongoDB, select this check box to enter the name of this Authentication database in the Authentication database field that is displayed.  For further information about the MongoDB Authentication database, see [User Authentication database](https://docs.mongodb.org/manual/core/security-users/#user-authentication-database). |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  Available when the Required authentication check box is selected.  If the security system you have selected from the Authentication mechanism dropdown list is Kerberos, you need to enter the User principal, the Realm and the KDC server fields instead of the Username and the Password fields. |
| Bucket | Enter the name of the bucket in which the files to be listed are stored. A bucket of GridFS is similar to a folder. |
| Query | Enter the query to be used to select the files to be listed. You need to define how these files are sorted in the list by selecting:   * Sort by: these files can be   sorted by their *filename*   attributes, *uploadDate*   attributes or *length* (the   File Size option)   attributes. * Sort order: these files can   be sorted in the Ascending or   Descending order. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| No query timeout | Select this check box to prevent MongoDB servers from stopping idle cursors at the end of 10-minute inactivity of these cursors. In this situation, an idle cursor will stay open until either the results of this cursor are exhausted or you manually close it using the cursor.close() method.  A cursor for MongoDB is a pointer to the result set of a query. By default, that is to say, with this check box being clear, a MongoDB server automatically stops idle cursors after a given inactivity period to avoid excess memory use. For further information about MongoDB cursors, see <https://docs.mongodb.org/manual/core/cursors/>. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_FILE: the number of files processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  CURRENT\_FILEID: the value of the *ObjectId* (the file ID) attribute of the current file. This is an Flow variable and it returns a string.  CURRENT\_FILENAME: the value of the *filename* attribute of the current file. This is an Flow variable and it returns a string.  CURRENT\_FILEUPLOADDATE: the value of the *uploadDate* attribute of the current file. This is an Flow variable and it returns a date.  CURRENT\_FILELENGTH: the value of the *length* (the size) attribute of the current file. This is an Flow variable and it returns a length.  CURRENT\_FILEMD5: the value of the *md5* attribute of the current file. This is an Flow variable and it returns a string.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component combines MongoDB GridFS connection and data iteration, thus usually used as a single-component subJob to list files stored in a given bucket in MongoDB GridFS.  Different lists are returned, each representing an attribute of these files and being stored in a specific global variable as explained above regarding the global variables provided by tMongoDBGridFSList.  It is often connected to the Job using OnSubjobOk or OnComponentOk link, depending on the context. |

**Related concepts**  

* [Managing files using MongoDB GridFS](tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-managing-files-using-mongodb-gridfs-standard-component-bigdata-in-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-managing-files-using-mongodb-gridfs-standard-component-bigdata-in-this -->
# Managing files using MongoDB GridFS

Last updated: 9/30/2026

This scenario applies only to Talend products
with Big Data.

In this scenario, the MongoDB GridFS components are used to create a Job to manage video
files in MongoDB GridFS.

For further information about the GridFS system of MongoDB, see [When to use GridFS](https://docs.mongodb.org/manual/core/gridfs/#faq-developers-when-to-use-gridfs).

For demonstration purposes, only one video file, called *custom\_hadoop.mp4*, is used; you can use any of your own video files to replicate
this scenario.

### In this section

* [Linking the components](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-linking-components-standard-component-bigdata-in)
* [Connecting to MongoDB](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-connecting-to-mongodb-standard-component-bigdata)
* [Copying data to MongoDB GridFS](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-copying-data-to-mongodb-gridfs-standard-component-bigdata)
* [Listing files stored in MongoDB GridFS](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-listing-files-stored-in-mongodb-gridfs-standard-component-bigdata)
* [Downloading files from MongoDB GridFS](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-downloading-files-from-mongodb-gridfs-standard-component-bigdata)
* [Remove files from MongoDB GridFS](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-remove-files-from-mongodb-gridfs-standard-component-bigdata)
* [Executing the Job](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-executing-job-standard-component-bigdata-then-you)

**Related reference**  

* [tMongoDBConnection](tmongodbconnection "Creates a connection to a MongoDB database and reuse that connection in other components.")
* [tMongoDBGridFSList](tmongodbgridfslist "Retrieves a list of files based on a query.")
* [tMongoDBGridFSProperties](tmongodbgridfsproperties "Obtains information about the properties of given files selected based on a query.")
* [tMongoDBGridFSPut](tmongodbgridfsput "Connects to a MongoDB GridFS system to load files into it.")
* [tMongoDBGridFSGet](tmongodbgridfsget "Connects to a MongoDB GridFS system to copy files from it.")
* [tMongoDBGridFSDelete](tmongodbgridfsdelete "Automates the delete action over specific files in MongoDB GridFS.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFilterColumns](/talend/en-US/components/8.0/processing/tfiltercolumns)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-connecting-to-mongodb-standard-component-bigdata -->
# Connecting to MongoDB

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBConnection to open its
   Component view.
2. From the DB version list, select the MongoDB
   version you are using.
3. In the Server and Port
   fields, enter the authentication information required for the connection to
   MongoDB. 

   If you use the host name of the MongoDB server, ensure that you have added the
   mapping between this host name and its IP address in the *hosts* file of the operating system in which the current Job is
   executed.
4. In the Database field, enter the name of the database
   hosting GridFS. This database is created on the fly if it dose not exist.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-copying-data-to-mongodb-gridfs-standard-component-bigdata -->
# Copying data to MongoDB GridFS

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBGridFSPut to open its
   Component view.
2. Select the Use existing connection check box
   and from the Connection list, select the
   component in which the MongoDB connection to be used is defined.
3. In the Bucket field, enter the bucket to be
   used to store files in GridFS. In this example, it is *talend\_channel/61*.
4. In the Local folder field, enter the path, or
   browse to the folder where the files to be uploaded to GridFS are stored. As
   explained previously, it is a video file called *custom\_hadoop.mp4*.
5. In the Files table, add one row by clicking
   the [+] button and in the Filemask column, enter *\*.mp4*
   within the double quotation marks. This allows tMongoDBGridFSPut to copy all the files with the *.mp4* extension from the local folder you have specified
   to the bucket to be used in GridFS.
6. Leave the New name column empty, that is to
   say, leave the double quotation marks in this column as is, so as to keep the
   name of this video unchanged after being copied to GridFS.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-downloading-files-from-mongodb-gridfs-standard-component-bigdata -->
# Downloading files from MongoDB GridFS

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBGridFSGet to open its
   Component view.
2. Select the Use existing connection check box
   and from the Connection list, select the
   component in which the MongoDB connection to be used is defined.
3. In the Bucket field, enter the bucket in
   which the files to be retrieved are stored. In this example, it is *talend\_channel/61*.
4. In the Local folder field, enter the path to
   the local folder in which you want to store the downloaded files. In this
   scenario, it is *C:/tmp/output*.
5. Select the Use Document ID as output filename
   check box to rename each downloaded file using the value of its *ObjectID* attribute.

   Since a file in GridFS is distinct by ID rather than by name, it is possible
   that several files are using the same file name. For this reason, when
   downloading this kind of files into the same directory without renaming them
   differently, an exception is returned to alert that the file being downloaded
   already exists. In order to avoid this error, you can either select the
   Overwrite local files check box to replace the
   existing one with the latest downloaded file or rename these files on the fly
   using their IDs. In this example, the strategy of renaming these files is
   adopted.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-executing-job-standard-component-bigdata-then-you -->
# Executing the Job

Last updated: 9/30/2026

## About this task

Then you can run this Job.

The tLogRow component is used to present the execution
result of the
Job.

## Procedure

1. If you want to configure the presentation mode on its Component view, double-click the tLogRow component to open the Component view and in the Mode
   area, then, select the Table (print values in cells of a
   table) radio box.
2. Press
   F6
   to run this
   Job.

## Results

Once done, the Run view is opened automatically, where
the metadata of the video *custom\_hadoop.mp4* in GridFS
is displayed.

The downloaded file can be found in the directory *C:/tmp/output*, using its ID as its file name.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-linking-components-standard-component-bigdata-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective of Talend Studio,
   create an empty Job, named *FS\_video* for example, from
   the Job Designs node in the Repository tree view.

   For further information about how to create a Job, see [Creating a Job](/talend/r/en-US/8.0/studio-user-guide/creating-job).
2. In the workspace, enter the name of the component to be used and select this
   component from the list that appears. In this scenario, the components are
   tMongoDBConnection, tMongoDBGridFSPut, tMongoDBGridFSList, tMongoDBGridFSProperties, tFilterColumns, tLogRow, tMongoDBGridFSGet and tMongoDBGridFSDelete.
3. Connect tMongoDBConnection to tMongoDBGridFSPut using the Trigger
   > On Subjob Ok link.
4. Repeat this operation to connect tMongoDBGridFSPut to tMongoDBGridFSList, tMongoDBGridFSList to tMongoDBGridFSGet, and then tMongoDBGridFSGet to tMongoDBGridFSDelete.
5. Connect tMongoDBGridFSList to tMongoDBGridFSProperties using the Row > Iterate link. This link allows tMongoDBGridFSList to send data to tMongoDBGridFSProperties iteratively.
6. Connect tMongoDBGridFSProperties to tFilterColumns using the Row >
   Main link.
7. Do the same to connect tFilterColumns to
   tLogRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-listing-files-stored-in-mongodb-gridfs-standard-component-bigdata -->
# Listing files stored in MongoDB GridFS

Last updated: 9/30/2026

### In this section

* [Iterating on the files](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-iterating-on-files-standard-component-bigdata)
* [Extracting file metadata](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-extracting-file-metadata-standard-component-bigdata)
* [Filtering attributes](/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-filtering-attributes-standard-component-bigdata)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-remove-files-from-mongodb-gridfs-standard-component-bigdata -->
# Remove files from MongoDB GridFS

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBGridFSDelete to open its
   Component view.
2. Select the Use existing connection check box
   and from the Connection list, select the
   component in which the MongoDB connection to be used is defined.
3. In the Bucket field, enter the bucket in
   which the files to be deleted are stored. In this example, it is *talend\_channel/61*.
4. From the Query type list, select the approach
   you want to use to select the files to be deleted. In this example, select
   Filename to use the *filename* attribute of each GridFS file for query.
5. In the Filename field, enter the name of the
   file to be deleted.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-extracting-file-metadata-standard-component-bigdata -->
# Extracting file metadata

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBGridFSProperties to open its
   Component view.
2. Select the Use existing connection check box
   and from the Connection list, select the
   component in which the MongoDB connection to be used is defined.
3. In the Bucket field, enter the bucket in
   which the files to be used are stored. In this example, it is *talend\_channel/61*.
4. From the Query type list, select the approach
   you want to use to select the files about which you need to extract the
   metadata. In this example, select Filename to
   use the *filename* attribute of each GridFS
   file for query.
5. In the Filename field, press Ctrl + Space to display the variable list and choose the
   variable to be used. In this example, select *tMongoDBGridFSList.CURRENT\_FILENAME* from the list. Then the
   expression to use the *CURRENT\_FILENAME*
   variable is automatically added.

   This allows tMongoDBGridFSProperties to read
   each file name returned by tMongoDBGridFSList.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-filtering-attributes-standard-component-bigdata -->
# Filtering attributes

Last updated: 9/30/2026

## Procedure

1. Double-click tFilterColumns to open its
   Component view.
2. Click the [...] button next to Edit schema to open the schema editor.
3. On the left side (the input side), select the column to be used and click the
   button to move this column to the right side (the output
   side). In this example, move every column to the right side except the *contentType* column.

   Each column represents a file attribute and the pre-defined schema of tMongoDBGridFSProperties automatically contains these
   columns.
4. Click OK to validate these changes and accept the
   propagation prompted by the pop-up dialog box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mongodb/tmongodbgridfslist-tmongodbgridfsproperties-tlogrow-iterating-on-files-standard-component-bigdata -->
# Iterating on the files

Last updated: 9/30/2026

## Procedure

1. Double-click tMongoDBGridFSList to open its
   Component view.
2. Select the Use existing connection check box
   and from the Connection list, select the
   component in which the MongoDB connection to be used is defined.
3. In the Bucket field, enter the bucket in
   which the files to be listed are stored. In this example, it is *talend\_channel/61*.
4. In the Query field, enter the query to select
   the files you want tMongoDBGridFSList to
   iterate on to generate different file lists. In this example, leave the default
   one in order to iterate on all of the files stored in this *talend\_channel/61* bucket.

   As explained previously, only one file, *custom\_hadoop.mp4*, is expected.
