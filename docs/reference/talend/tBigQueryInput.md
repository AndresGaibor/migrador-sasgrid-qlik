<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput · versión 8.0 -->
# tBigQueryInput

Last updated: 9/30/2026

Performs the queries supported by Google BigQuery.

This component connects to Google BigQuery and performs queries in
it.

### In this section

* [tBigQueryInput Standard properties](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-standard-properties)
* [tBigQueryInput properties for Apache Spark Batch](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-properties-for-apache-spark-batch)
* [tBigQueryInput properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-properties-for-apache-spark-streaming)

**Related concepts**  

* [Performing a query in Google BigQuery](tbigqueryinput-tlogrow-performing-query-in-google-bigquery-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-properties-for-apache-spark-batch -->
# tBigQueryInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tBigQueryInput running in the Spark Batch Job framework.

The Spark Batch
tBigQueryInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Source type | Select the way you want tBigQueryInput to read data from Google BigQuery:  * `Table`: copy the whole table. * `Query`: write a query to select data. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |

When the Source type is `Table`:

| Properties | Description |
| --- | --- |
| Project ID | If your Google BigQuery service uses the Google Cloud Platform project ID, keep this checkbox clear to allow tBigQueryInput to read this ID from the Spark configuration tab or the tBigQueryConfiguration component.  If the Google BigQuery service uses a custom ID, select this checkbox and enter the ID.  The ID of your project can be found in the URL of the Google API Console, or by hovering your mouse pointer over the name of the project in the BigQuery Browser Tool. |
| Dataset | Enter the name of the dataset to which the table to be copied belongs.  When you use Google BigQuery with Dataproc, in Google Cloud Platform, select the same region for your BigQuery dataset as for the Dataproc cluster to be run. |
| Table | Enter the name of the table to be copied. |

When the Source type is `Query`:

| Properties | Description |
| --- | --- |
| Query | Enter the query to be used.  When you use Google BigQuery with Dataproc, in Google Cloud Platform, select the same region for your BigQuery dataset as for the Dataproc cluster to be run.  If the query to be used is the legacy SQL of BigQuery, select this Use legacy SQL checkbox. For further information about this legacy SQL, see [Legacy SQL query reference](https://cloud.google.com/bigquery/docs/reference/legacy-sql) in the Google Cloud documentation. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This is an input component. It sends data extracted from BigQuery to the component that follows it.  Place a tBigQueryConfiguration component in the same Job because it needs to use the BigQuery configuration information provided by tBigQueryConfiguration. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-standard-properties -->
# tBigQueryInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tBigQueryInput running in the Standard Job framework.

The Standard
tBigQueryInput component belongs to the Big Data family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Guess schema | Click the button to retrieve the schema from the table. Note that Date type data will be returned as String type when clicking Guess schema.  This option is available when you have installed the R2023-02 Talend Studio monthly update or a later one delivered by Talend. |
| Authentication mode | Select the mode to be used to authenticate to your project.  * Service account: authenticate using a Google account   that is associated with your Google Cloud Platform project. When selecting   this mode, the credentials must be provided in the Service   account credentials file field. * Workload Identity Federation: authenticate   through a Google Workload Identity Pool, allowing integration with identity providers such as   AWS, Azure, or OIDC, without needing a service account key. When selecting   this mode, the identity federation configuration must be provided in the   Client library configuration file field. * Application Default Credentials: authenticate using   the Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based   on the application environment. * OAuth 2.0 - Authorization Code grant: authenticate   using OAuth credentials. The OAuth parameters must be provided in the   Client ID, Client secret,   Authorization code, and Redirect   URI fields. Only Desktop application credentials are   supported. For more information, read [Desktop apps](https://support.google.com/googleapi/answer/6158849#zippy=%2Cnative-applications%2Cdesktop-apps) and [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job."). * OAuth Access Token: authenticate using an OAuth   access token. When selecting this mode, the token must be provided in the   OAuth Access Token file.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Service account credentials file | Enter the path to the credentials file created for the service account to be used. This file must be stored in the machine in which your Talend Job is actually launched and executed. This property is only available when you authenticate using Service account. |
| Client ID and Client secret | Paste the client ID and the client secret, both created and viewable on the API Access tab view of the project hosting the Google BigQuery service and the Cloud Storage service you need to use.  To enter the client secret, click the [...] button next to the client secret field, and then in the pop-up dialog box enter the client secret between double quotes and click OK to save the settings.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit.  This property is only available when you authenticate using OAuth Access Token. |
| Redirect URI | Enter the redirect URI for your Google OAuth desktop application.  Use a loopback URI such as http://127.0.0.1:<port> or http://localhost:<port>.  This value must exactly match one of the redirect URIs configured in your Google OAuth client.  For more information, see [redirect\_uri parameter](https://developers.google.com/identity/protocols/oauth2/native-app#request-parameter-redirect_uri) and [loopback IP address](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_loopback) in Google documentation.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Authorization code | Paste the authorization code provided by Google for the access you are building.  To obtain the authorization code, you need to execute the Job using this component and when this Job pauses execution to print out an URL address, you navigate to this address to copy the authorization code displayed. For more information, read [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job.").  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Project ID | Paste the ID of the project hosting the Google BigQuery service you need to use.  The ID of your project can be found in the URL of the Google API Console, or by hovering your mouse pointer over the name of the project in the BigQuery Browser Tool. |
| Use legacy SQL and Query | Enter the query you need to use. If the query to be used is the legacy SQL of BigQuery, select this Use legacy SQL checkbox. For further information about this legacy SQL, see [Legacy SQL query reference](https://cloud.google.com/bigquery/docs/reference/legacy-sql) in the Google Cloud documentation. |
| Result size | Select the option depending on the volume of the query result.  By default, the `Small` option is used, but when the query result is larger than the [maximum response size](https://cloud.google.com/bigquery/quota-policy#queries), you need to select the `Large` option.  If the volume of the result is not certain, select `Auto`. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use a custom endpoint | Select this check box to use a private endpoint rather than the default one. When selected, enter the URL in the Google BigQuery Private API URL property, by respecting the following format: "https://bigquery.googleapis.com".  For more information, see [Access Google APIs through endpoints](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis) in the Google Cloud documentation.  This property is only available when you authenticate using Service account. |
| *token properties File Name* | Enter the path to, or browse to the refresh token file you need to use.  At the first Job execution using the Authorization code you have obtained from Google BigQuery, the value in this field is the directory and the name of that refresh token file to be created and used; if that token file has been created and you need to reuse it, you have to specify its directory and file name in this field.  With only the token file name entered, Talend Studio considers the directory of that token file to be the root of the Talend Studio folder.  For further information about the refresh token, see the manual of Google BigQuery. |
| Advanced Separator for numbers | Select this checkbox to change the separator used for the numbers. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Force single query execution | Select this checkbox to let the component return the result of the whole query. If you clear this checkbox, the component executes each sub-query separately and returns the result of each query sequentially. |
| Use custom temporary Dataset name | Select this checkbox to use an existing dataset to which you have access, instead of creating one, and in the field that is displayed, enter the name of this dataset. This way, you avoid rights and permissions issues related to dataset creation.  This checkbox is available only when you have selected `Large` from the Result size dropdown list in the Basic settings tab. |
| tStatCatcher Statistics | Select this checkbox to collect the log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error check box is selected. |
| JOBID | The ID of the Job. This is an After variable and it returns a string. |
| STATISTICS | The statistics of the Job. This is an After variable and it returns a string. |
| STATISTICS\_CHILD | The statistics of the child Job. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This is an input component. It sends the extracted data to the component that follows it.  This component automatically detects and supports both multi-regional locations and regional locations. When using the regional locations, the buckets and the datasets to be used must be in the same locations. |
| BigQuery data type limitations | * The Record type of BigQuery is not supported. * The columns for table metadata such as the   Description column or the Mode column cannot be retrieved. * The Timestamp data from your BigQuery system is formatted to be String   data. * The numeric data of BigQuery is converted to   BigDecimal. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-performing-query-in-google-bigquery-standard-component-this -->
# Performing a query in Google BigQuery

Last updated: 9/30/2026

This scenario uses two components to perform the SELECT query in BigQuery and
present the result in Talend Studio.

The following figure shows the schema of the table, *UScustomer*, we use as example to perform the SELECT query in.

We will select the State records and count the occurrence of each State among those
records.

### In this section

* [Linking the components](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-linking-components-standard-component-in)
* [Creating the query](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-creating-query-standard-component)
* [Executing the Job](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-executing-job-standard-component-the)

**Related concepts**  

* [tBigQueryInput](tbigqueryinput "Performs the queries supported by Google BigQuery.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-creating-query-standard-component -->
# Creating the query

Last updated: 9/30/2026

### In this section

* [Building access to BigQuery](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-building-access-to-bigquery-standard-component)
* [Writing the query](/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-writing-query-standard-component-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-executing-job-standard-component-the -->
# Executing the Job

Last updated: 9/30/2026

## About this task

The tLogRow component presents the execution
result of the Job. You can configure the presentation mode on its Component view.

To do this, double-click tLogRow to open the
Component view and in the Mode area, select the Table (print values in
cells of a table) option.

## Procedure

To execute this Job, press F6.

## Results

Once done, the Run view is opened automatically,
where you can check the execution result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-linking-components-standard-component-in -->
# Linking the components

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective of Talend Studio,
   create an empty Job, named *BigQueryInput* for example, from
   the Job Designs node in the Repository tree view.

   For further information about how to create a Job, see [Creating a Job](/talend/r/en-US/8.0/studio-user-guide/creating-job).
2. Drop tBigQueryInput and tLogRow onto the workspace.
3. Connect them using the Row > Main
   link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-building-access-to-bigquery-standard-component -->
# Building access to BigQuery

Last updated: 9/30/2026

## Procedure

1. Double-click tBigQueryInput to open its
   Component view.
2. Click Edit schema to open the
   editor
3. Click the
   button twice to add two rows and enter the names of
   your choice for each of them in the Column
   column. In this scenario, they are: *States* and *Count*.
4. Click OK to validate these changes and
   accept the propagation prompted by the pop-up dialog box.
5. In the Authentication area, add the authentication
   information to access your Google Cloud account. For more information on the
   available authentication modes, see [tBigQueryInput Standard properties](/talend/r/en-US/8.0/components/google-bigquery/tbigqueryinput-standard-properties).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigqueryinput-tlogrow-writing-query-standard-component-in -->
# Writing the query

Last updated: 9/30/2026

## Procedure

In the Query field, enter
select States, count (\*) as Count from documentation.UScustomer group by States
