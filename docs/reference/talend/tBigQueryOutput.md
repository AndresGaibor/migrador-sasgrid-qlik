<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput · versión 8.0 -->
# tBigQueryOutput

Last updated: 9/30/2026

Transfers the data provided by its preceding component to Google
BigQuery.

This component writes the data it receives in a user-specified
directory and transfers the data to Google BigQuery via Google Cloud
Storage.

### In this section

* [tBigQueryOutput Standard properties](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-standard-properties)
* [tBigQueryOutput properties for Apache Spark Batch](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-properties-for-apache-spark-batch)
* [tBigQueryOutput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Writing data in Google BigQuery](tbigqueryoutput-trowgenerator-tmysqlinput-tmap-writing-data-in-google-bigquery-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-properties-for-apache-spark-batch -->
# tBigQueryOutput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tBigQueryOutput running in the Spark Batch Job framework.

The Spark Batch
tBigQueryOutput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Dataset | Enter the name of the dataset to which the table to be created or updated belongs.  When you use Google BigQuery with Dataproc, in Google Cloud Platform, select the same region for your BigQuery dataset as for the Dataproc cluster to be run. |
| Table | Enter the name of the table to be created or updated. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Table operations | Select the operation to be performed on the defined table:  * Create table if does not exist: The table is   created if it does not exist. * Truncate: The table content   is deleted. |
| Data operation | Select the operation to be performed on the incoming data:  * Append:   Append data to the table, whether the table is empty or not. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This is an input component. It sends data extracted from BigQuery to the component that follows it.  Place a tBigQueryConfiguration component in the same Job because it needs to use the BigQuery configuration information provided by tBigQueryConfiguration. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-standard-properties -->
# tBigQueryOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure tBigQueryOutput running in the Standard Job framework.

The Standard
tBigQueryOutput component belongs to the Big Data family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Property type | Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs. |
| Local filename | Browse to, or enter the path to the file you want to write the received data in. |
| Append | Select this checkbox to add rows to the existing data in the file specified in Local filename. |
| Authentication mode | Select the mode to be used to authenticate to your project.  * Service account: authenticate using a Google account   that is associated with your Google Cloud Platform project. When selecting   this mode, the credentials must be provided in the Service   account credentials file field. * Workload Identity Federation: authenticate   through a Google Workload Identity Pool, allowing integration with identity providers such as   AWS, Azure, or OIDC, without needing a service account key. When selecting   this mode, the identity federation configuration must be provided in the   Client library configuration file field. * Application Default Credentials: authenticate using   the Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based   on the application environment. * OAuth 2.0 - Authorization Code grant: authenticate   using OAuth credentials. The OAuth parameters must be provided in the   Client ID, Client secret,   Authorization code, and Redirect   URI fields. Only Desktop application credentials are   supported. For more information, read [Desktop apps](https://support.google.com/googleapi/answer/6158849#zippy=%2Cnative-applications%2Cdesktop-apps) and [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job."). * OAuth Access Token: authenticate using an OAuth   access token. When selecting this mode, the token must be provided in the   OAuth Access Token file.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Service account credentials file | Enter the path to the credentials file created for the service account to be used. This file must be stored in the machine in which your Talend Job is actually launched and executed. This property is only available when you authenticate using Service account. |
| Client ID and Client secret | Paste the client ID and the client secret, both created and viewable on the API Access tab view of the project hosting the Google BigQuery service and the Cloud Storage service you need to use.  To enter the client secret, click the [...] button next to the client secret field, and then in the pop-up dialog box enter the client secret between double quotes and click OK to save the settings.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit.  This property is only available when you authenticate using OAuth Access Token. |
| Redirect URI | Enter the redirect URI for your Google OAuth desktop application.  Use a loopback URI such as http://127.0.0.1:<port> or http://localhost:<port>.  This value must exactly match one of the redirect URIs configured in your Google OAuth client.  For more information, see [redirect\_uri parameter](https://developers.google.com/identity/protocols/oauth2/native-app#request-parameter-redirect_uri) and [loopback IP address](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_loopback) in Google documentation.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Authorization code | Paste the authorization code provided by Google for the access you are building.  To obtain the authorization code, you need to execute the Job using this component and when this Job pauses execution to print out an URL address, you navigate to this address to copy the authorization code displayed. For more information, read [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job.").  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Project ID | Paste the ID of the project hosting the Google BigQuery service you need to use.  The ID of your project can be found in the URL of the Google API Console, or by hovering your mouse pointer over the name of the project in the BigQuery Browser Tool. |
| Dataset | Enter the name of the dataset you need to transfer data to. |
| Table | Enter the name of the table you need to transfer data to.  If this table does not exist, select the Create the table if it doesn't exist checkbox. |
| Action on data | Select the action to be performed from the dropdown list when transferring data to the target table. The action may be:   * Truncate: it empties the   contents of the table and repopulates it with the transferred   data. * Append: it adds rows to the   existing data in the table. * Empty: it populates the empty   table. |
| Credential type | Select the type to be used to authenticate to your project.  * Service account: when selecting this credential type,   the parameter to be defined in the Basic settings view   is Service account key. * Application Default Credentials: when selecting this   credential type, the parameter to be defined in the Basic   settings view is Application Default   Credentials. * OAuth Access Token: when selecting this credential   type, the parameter to be defined in the Basic settings   view is OAuth Access Token.   By default, Service account is selected. The Credential type field is available only if you do not select the Bulk file already exists in Google storage check box. |
| Service account key | Click the [...] button next to the service account key field to browse for the JSON file that contains your service account key.  This property is only available when you authenticate using Service account. |
| Access key and Secret key | Paste the authentication information obtained from Google for making requests to Google Cloud Storage.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  These keys can be consulted on the Interoperable Access tab view under the Google Cloud Storage tab of the project. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit. This property is only available when you authenticate using OAuth Access Token. |
| Bucket | Enter the name of the bucket, the Google Cloud Storage container, which holds the data to be transferred to Google BigQuery. |
| File | Enter the directory of the data stored on Google Cloud Storage and to be transferred to Google BigQuery.  If the data is not on Google Cloud Storage, this directory is used as the intermediate destination before the data is transferred to Google BigQuery.  Note that this file name must be identical with the name of the file specified in the Local filename field. |
| Header | Set values to ignore the header of the transferred data. For example, enter *0* to ignore no rows for the data without header and set *1* for the data with header at the first row. |
| Die on error | This checkbox is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| *token properties File Name* | Enter the path to, or browse to the refresh token file you need to use.  At the first Job execution using the Authorization code you have obtained from Google BigQuery, the value in this field is the directory and the name of that refresh token file to be created and used; if that token file has been created and you need to reuse it, you have to specify its directory and file name in this field.  With only the token file name entered, Talend Studio considers the directory of that token file to be the root of the Talend Studio folder.  For further information about the refresh token, see the manual of Google BigQuery. |
| Field Separator | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Drop table if exists | Select the Drop table if exists checkbox to remove the table specified in the Table field, if this table already exists. |
| Create directory if not exists | Select this checkbox to create the directory you defined in the File field for Google Cloud Storage, if it does not exist. |
| Custom the flush buffer size | Enter the number of rows to be processed before the memory is freed. |
| Check disk space | Select this checkbox to throw an exception during execution if the disk is full. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| tStatCatcher Statistics | Select this checkbox to collect the log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |
| JOBID | The ID of the Job. This is an After variable and it returns a string. |
| STATISTICS | The statistics of the Job. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This is an output component used at the end of a Job. It receives data from its preceding component such as tFileInputDelimited, tMap or tMysqlInput.  This component automatically detects and supports both multi-regional locations and regional locations. When using the regional locations, the buckets and the datasets to be used must be in the same locations. |
| BigQuery data type limitations | * The Record type of BigQuery is not supported. * The columns for table metadata such as the   Description column or the Mode column cannot be retrieved. * The Timestamp data from your BigQuery system is formatted to be String   data. * The numeric data of BigQuery is converted to   BigDecimal. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-writing-data-in-google-bigquery-standard-component-this -->
# Writing data in Google BigQuery

Last updated: 9/30/2026

This scenario uses two components to write data in Google BigQuery.

### In this section

* [Linking the components](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-linking-components-standard-component-in)
* [Preparing the data to be transferred](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-preparing-data-to-be-transferred-standard-component)
* [Configuring the access to BigQuery and Cloud Storage](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-configuring-access-to-bigquery-and-cloud-storage-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-executing-job-standard-component-press)

**Related concepts**  

* [tBigQueryOutput](tbigqueryoutput "Transfers the data provided by its preceding component to Google BigQuery.")

**Related information**  

* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)
* [tMap](/talend/en-US/components/8.0/tmap/tmap)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-configuring-access-to-bigquery-and-cloud-storage-standard-component -->
# Configuring the access to BigQuery and Cloud Storage

Last updated: 9/30/2026

### In this section

* [Building access to Cloud Storage](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-building-access-to-cloud-storage-standard-component)
* [Building access to BigQuery](/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-building-access-to-bigquery-standard-component-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-executing-job-standard-component-press -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

Press F6.

## Results

Once done, the Run view is opened automatically,
where you can check the execution result.

The data is transferred to Google BigQuery.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-linking-components-standard-component-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the 
   Integration
    perspective
   of *Talend Studio*,
   create an empty Job, named WriteBigQuery for example, from the Job Designs node in the Repository tree view.

   For further information about how to create a Job, see [Creating a Job](/talend/r/en-US/8.0/studio-user-guide/creating-job).
2. Drop tRowGenerator and tBigQueryOutput onto the workspace.

   The tRowGenerator component generates the
   data to be transferred to Google BigQuery in this scenario. In the
   real-world case, you can use other components such as tMysqlInput or tMap in the
   place of tRowGenerator to design a
   sophisticated process to prepare your data to be transferred.
3. Connect them using the Row > Main
   link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-preparing-data-to-be-transferred-standard-component -->
# Preparing the data to be transferred

Last updated: 9/30/2026

## Procedure

1. Double-click tRowGenerator to open its
   Component view.
2. Click RowGenerator Editor to open the
   editor.
3. Click
   three times to add three rows in the Schema table.
4. In the Column column, enter the name of
   your choice for each of the new rows. For example, *fname*, *lname* and
   *States*.
5. In the Functions column, select *TalendDataGenerator.getFirstName* for the
   *fname* row, *TalendDataGenerator.getLastName* for the *lname* row and *TalendDataGenerator.getUsState* for the *States* row.
6. In the Number of Rows for RowGenerator
   field, enter, for example, *100* to define
   the number of rows to be generated.
7. Click OK to validate these
   changes.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-building-access-to-bigquery-standard-component-in -->
# Building access to BigQuery

Last updated: 9/30/2026

## Procedure

1. In the Dataset field of the
   Component view, enter the dataset you need to transfer data
   in. In this scenario, it is *documentation*.

   This dataset must exist in BigQuery. The following figure shows the
   dataset used by this scenario.
2. In the Table field, enter the
   name of the table you need to write data in, for example, *UScustomer*.
3. In the Action on data field,
   select the action. In this example, select Truncate to empty the contents, if there are any, of target table and
   to repopulate it with the transferred data.
4. In the Authentication area, add the authentication
   information to access your Google Cloud account. For more information on the
   available authentication modes, see [tBigQueryOutput Standard properties](/talend/r/en-US/8.0/components/google-bigquery/tbigqueryoutput-standard-properties).
5. If you have been using the OAuth 2.0 authentication mode, in
   the Action on data field, select the action to be performed on
   your data. In this example, select Truncate to empty the
   contents, if there are any, of target table and to repopulate it with the transferred
   data. If your are using Service account, ignore this
   step.

   If the table to be used does not exist in BigQuery, select Create the table if it doesn't exist.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryoutput-trowgenerator-tmysqlinput-tmap-building-access-to-cloud-storage-standard-component -->
# Building access to Cloud Storage

Last updated: 9/30/2026

## Procedure

1. Double-click tBigQueryOutput to
   open its Component view.
2. Click Sync columns to retrieve
   the schema from its preceding component.
3. In the Local filename field,
   enter the directory where you need to create the file to be transferred to
   BigQuery.
4. Navigate to the Google APIs Console in your web browser to access the
   Google project hosting the BigQuery and the Cloud Storage services you need to
   use.
5. Click Google Cloud Storage > Interoperable Access to open its
   view.
6. In Google storage configuration area of the
   Component view, paste Access key, Access
   secret from the Interoperable Access tab view to the corresponding fields,
   respectively.
7. In the Bucket field, enter the
   path to the bucket you want to store the transferred data in. In this example, it is
   *talend/documentation*

   This bucket must exist in the directory in Cloud Storage
8. In the File field, enter the
   directory where in Google Clould Storage you receive and create the file to be
   transferred to BigQuery. In this example, it is *gs://talend/documentation/biquery\_UScustomer.csv*. The file name must be the
   same as the one you defined in the Local
   filename field.

   Troubleshooting: if you encounter issues such as *Unable to read source URI* of the file stored in Google Cloud Storage,
   check whether you put the same file name in these two fields.
9. Enter *0* in the Header field to ignore no rows in the transferred data.
