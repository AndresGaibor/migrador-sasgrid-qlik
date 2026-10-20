<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigquerybulkexec · versión 8.0 -->
# tBigQueryBulkExec

Last updated: 9/30/2026

Transfers given data to Google BigQuery.

The tBigQueryOutputBulk and tBigQueryBulkExec components are generally used together as parts of a two step
process. In the first step, an output file is generated. In the second step, this file is
used to feed a dataset. These two steps are fused together in the tBigQueryOutput component, detailed in a separate section. The advantage of
using two separate components is that the data can be transformed before it is loaded in the
dataset.

This component transfers a given file from Google Cloud Storage to
Google BigQuery, or uploads a given file into Google Cloud Storage
and then transfers it to Google BigQuery.

## tBigQueryBulkExec Standard properties

These properties are used to configure tBigQueryBulkExec running in the Standard Job framework.

The Standard
tBigQueryBulkExec component belongs to the Big Data family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Authentication mode | Select the mode to be used to authenticate to your project.  * Service account: authenticate using a Google account   that is associated with your Google Cloud Platform project. When selecting   this mode, the credentials must be provided in the Service   account credentials file field. * Workload Identity Federation: authenticate   through a Google Workload Identity Pool, allowing integration with identity providers such as   AWS, Azure, or OIDC, without needing a service account key. When selecting   this mode, the identity federation configuration must be provided in the   Client library configuration file field. * Application Default Credentials: authenticate using   the Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based   on the application environment. * OAuth 2.0 - Authorization Code grant: authenticate   using OAuth credentials. The OAuth parameters must be provided in the   Client ID, Client secret,   Authorization code, and Redirect   URI fields. Only Desktop application credentials are   supported. For more information, read [Desktop apps](https://support.google.com/googleapi/answer/6158849#zippy=%2Cnative-applications%2Cdesktop-apps) and [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job."). * OAuth Access Token: authenticate using an OAuth   access token. When selecting this mode, the token must be provided in the   OAuth Access Token file.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Service account credentials file | Enter the path to the credentials file created for the service account to be used. This file must be stored in the machine in which your Talend Job is actually launched and executed. This property is only available when you authenticate using Service account. |
| Client ID and Client secret | Paste the client ID and the client secret, both created and viewable on the API Access tab view of the project hosting the Google BigQuery service and the Cloud Storage service you need to use.  To enter the client secret, click the [...] button next to the client secret field, and then in the pop-up dialog box enter the client secret between double quotes and click OK to save the settings.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit.  This property is only available when you authenticate using OAuth Access Token. |
| Redirect URI | Enter the redirect URI for your Google OAuth desktop application.  Use a loopback URI such as http://127.0.0.1:<port> or http://localhost:<port>.  This value must exactly match one of the redirect URIs configured in your Google OAuth client.  For more information, see [redirect\_uri parameter](https://developers.google.com/identity/protocols/oauth2/native-app#request-parameter-redirect_uri) and [loopback IP address](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_loopback) in Google documentation.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Authorization code | Paste the authorization code provided by Google for the access you are building.  To obtain the authorization code, you need to execute the Job using this component and when this Job pauses execution to print out an URL address, you navigate to this address to copy the authorization code displayed. For more information, read [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job.").  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Project ID | Paste the ID of the project hosting the Google BigQuery service you need to use.  The ID of your project can be found in the URL of the Google API Console, or by hovering your mouse pointer over the name of the project in the BigQuery Browser Tool. |
| Dataset | Enter the name of the dataset you need to transfer data to. |
| Table | Enter the name of the table you need to transfer data to. If this table does not exist, select the Create the table if it doesn't exist checkbox. |
| Action on data | Select the action to be performed from the dropdown list when transferring data to the target table. The action may be:  * Truncate: it empties the contents of   the table and repopulates it with the transferred data. * Append: it adds rows to the existing   data in the table. * Empty: it populates the empty table. |
| Credential type | Select the type to be used to authenticate to your project.  * Service account: when selecting this credential type,   the parameter to be defined in the Basic settings view   is Service account key. * Application Default Credentials: when selecting this   credential type, the parameter to be defined in the Basic   settings view is Application Default   Credentials. * OAuth Access Token: when selecting this credential   type, the parameter to be defined in the Basic settings   view is OAuth Access Token.   By default, Service account is selected. The Credential type field is available only if you do not select the Bulk file already exists in Google storage check box. |
| Bulk file already exists in Google storage | Select this checkbox to reuse the authentication information for Google Cloud Storage connection, then, complete the File and the Header fields. |
| Service account key | Click the [...] button next to the service account key field to browse for the JSON file that contains your service account key. This property is only available when you authenticate using Service account. |
| Access key and Secret key | Paste the authentication information obtained from Google for making requests to Google Cloud Storage.  To enter the secret key, click the [...] button next to the secret key field, and then in the pop-up dialog box enter the password between double quotes and click OK to save the settings.  These keys can be consulted on the Interoperable Access tab view under the Google Cloud Storage tab of the project. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit. This property is only available when you authenticate using OAuth Access Token. |
| File to upload | When the data to be transferred to Google BigQuery is not stored on Google Cloud Storage, browse to, or enter the path to it. |
| Bucket | Enter the name of the bucket, the Google Cloud Storage container, which holds the data to be transferred to Google BigQuery. |
| File | Enter the directory of the data stored on Google Cloud Storage and to be transferred to Google BigQuery.  If the data is not on Google Cloud Storage, this directory is used as the intermediate destination before the data is transferred to Google BigQuery. |
| Header | Set values to ignore the header of the transferred data. For example, enter *0* to ignore no rows for the data without header. |
| Die on error | This checkbox is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use a custom endpoint | Select this check box to use a private endpoint rather than the default one. When selected, enter the URL in the following properties:  * Google Storage Private API URL by respecting the   "https://storage.googleapis.com" format. * Google BigQuery Private API URL by respecting the   "https://bigquery.googleapis.com" format.  For more information, see [Access Google APIs through endpoints](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis) in the Google Cloud documentation.  This property is only available when you authenticate using Service account and Application Default Credentials. |
| *token properties File Name* | Enter the path to, or browse to the refresh token file you need to use.  At the first Job execution using the Authorization code you have obtained from Google BigQuery, the value in this field is the directory and the name of that refresh token file to be created and used; if that token file has been created and you need to reuse it, you have to specify its directory and file name in this field.  With only the token file name entered, Talend Studio considers the directory of that token file to be the root of the Talend Studio folder.  For further information about the refresh token, see the manual of Google BigQuery. |
| Set the field delimiter | Enter a character, a string, or a regular expression to separate fields for the transferred data. |
| Use custom null marker | Select this option to use a specific character as the null marker. You can specify the null marker in double quotation markers in the text frame to the right.  This option prevents errors caused by fields with null values. |
| Drop table if exists | Select the Drop table if exists checkbox to remove the table specified in the Table field, if this table already exists. |
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
| Usage rules | This is a standalone component. This component automatically detects and supports both multi-regional locations and regional locations. When using the regional locations, the buckets and the datasets to be used must be in the same locations. |
| BigQuery data type limitations | * The Record type of BigQuery is not supported. * The columns for table metadata such as the   Description column or the Mode column cannot be retrieved. * The Timestamp data from your BigQuery system is formatted to be String   data. * The numeric data of BigQuery is converted to   BigDecimal. |
