<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-bigquery/tbigquerysqlrow · versión 8.0 -->
# tBigQuerySQLRow

Last updated: 9/30/2026

Connects to Google BigQuery and performs queries to select data from tables row by row or create or delete tables in Google BigQuery.

## tBigQuerySQLRow Standard properties

These properties are used to configure tBigQuerySQLRow running in the Standard Job framework.

The Standard
tBigQueryInput component belongs to the Big Data family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. |
| Authentication mode | Select the mode to be used to authenticate to your project.  * Service account: authenticate using a Google account   that is associated with your Google Cloud Platform project. When selecting   this mode, the credentials must be provided in the Service   account credentials file field. * Workload Identity Federation: authenticate   through a Google Workload Identity Pool, allowing integration with identity providers such as   AWS, Azure, or OIDC, without needing a service account key. When selecting   this mode, the identity federation configuration must be provided in the   Client library configuration file field. * Application Default Credentials: authenticate using   the Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based   on the application environment. * OAuth 2.0 - Authorization Code grant: authenticate   using OAuth credentials. The OAuth parameters must be provided in the   Client ID, Client secret,   Authorization code, and Redirect   URI fields. Only Desktop application credentials are   supported. For more information, read [Desktop apps](https://support.google.com/googleapi/answer/6158849#zippy=%2Cnative-applications%2Cdesktop-apps) and [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job."). * OAuth Access Token: authenticate using an OAuth   access token. When selecting this mode, the token must be provided in the   OAuth Access Token file.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Service account credentials file | Enter the path to the credentials file created for the service account to be used. This file must be stored in the machine in which your Talend Job is actually launched and executed. This property is only available when you authenticate using Service account. |
| Client ID and Client secret | Paste the client ID and the client secret, both created and viewable on the API Access tab view of the project hosting the Google BigQuery service and the Cloud Storage service you need to use.  To enter the client secret, click the [...] button next to the client secret field, and then in the pop-up dialog box enter the client secret between double quotes and click OK to save the settings.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| OAuth Access Token | Enter an access token. The lifetime of the token is one hour. The component does not perform the token refresh operation but will fetch the new access token to operate beyond the one-hour limit.  This property is only available when you authenticate using OAuth Access Token. |
| Redirect URI | Enter the redirect URI for your Google OAuth desktop application.  Use a loopback URI such as http://127.0.0.1:<port> or http://localhost:<port>.  This value must exactly match one of the redirect URIs configured in your Google OAuth client.  For more information, see [redirect\_uri parameter](https://developers.google.com/identity/protocols/oauth2/native-app#request-parameter-redirect_uri) and [loopback IP address](https://developers.google.com/identity/protocols/oauth2/native-app#redirect-uri_loopback) in Google documentation.  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Authorization code | Paste the authorization code provided by Google for the access you are building.  To obtain the authorization code, you need to execute the Job using this component and when this Job pauses execution to print out an URL address, you navigate to this address to copy the authorization code displayed. For more information, read [Accessing BigQuery using OAuth 2.0 authentication mode](accessing-bigquery-using-oauth-2-0-authentication-mode "Use OAuth 2.0 - Authorization Code grant to connect BigQuery components to Google BigQuery in a Standard Job.").  This property is only available when you authenticate using OAuth 2.0 - Authorization Code grant. |
| Project ID | Paste the ID of the project hosting the Google BigQuery service you need to use.  The ID of your project can be found in the URL of the Google API Console, or by hovering your mouse pointer over the name of the project in the BigQuery Browser Tool. |
| Use legacy SQL and Query | Enter the query you need to use. If the query to be used is the legacy SQL of BigQuery, select this Use legacy SQL checkbox. For further information about this legacy SQL, see [Legacy SQL query reference](https://cloud.google.com/bigquery/docs/reference/legacy-sql) in the Google Cloud documentation. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use a custom endpoint | Select this check box to use a private endpoint rather than the default one. When selected, enter the URL in the Google BigQuery Private API URL property, by respecting the following format: "https://bigquery.googleapis.com".  For more information, see [Access Google APIs through endpoints](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis) in the Google Cloud documentation.  This property is only available when you authenticate using Service account. |
| *token properties File Name* | Enter the path to, or browse to the refresh token file you need to use.  At the first Job execution using the Authorization code you have obtained from Google BigQuery, the value in this field is the directory and the name of that refresh token file to be created and used; if that token file has been created and you need to reuse it, you have to specify its directory and file name in this field.  With only the token file name entered, Talend Studio considers the directory of that token file to be the root of the Talend Studio folder.  For further information about the refresh token, see the manual of Google BigQuery. |
| Advanced Separator for numbers | Select this check box to change the separator used for the numbers. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. The supported encodings depend on the JVM that you are using. For more information, see <https://docs.oracle.com>. |
| Force single query execution | Select this check box to let the component return the result of the whole query. If you clear this check box, the component executes each sub-query separately and returns the result of each query sequentially. |
| Result size | Select the option depending on the volume of the query result.  By default, the `Small` option is used, but when the query result is larger than the [maximum response size](https://cloud.google.com/bigquery/quota-policy#queries), you need to select the `Large` option.  If the volume of the result is not certain, select `Auto`. |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

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
| **Usage rule** | It can be a starting or an end component. When starting a Job, it sends the extracted data to the component that follows it; When ending a Job, it deletes a given table.  This component automatically detects and supports both multi-regional locations and regional locations. When using the regional locations, the buckets and the datasets to be used must be in the same locations. |
