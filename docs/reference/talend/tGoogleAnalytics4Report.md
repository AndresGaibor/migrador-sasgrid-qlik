<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/google-analytics/tgoogleanalytics4report · versión 8.0 -->
# tGoogleAnalytics4Report

Last updated: 9/30/2026

Establishes a connection to Google Analytics 4 to retrieve data reports.

## tGoogleAnalytics4Report Standard properties

These properties are used to configure tGoogleAnalytics4Report
running in the Standard Job framework.

The Standard
tGoogleAnalytics4Report component belongs to the Business family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Schema and Edit schema | A schema is a row description, and it defines the fields to be processed and passed on to the next component.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Authentication method | Select the mode to be used to authenticate to your project.  * Service account key: authenticate using a Google   account that is associated with your Google Cloud Platform project. When   selecting this mode, the parameter to be defined is Google   credentials. * Application Default Credentials: authenticate using   the Application Default Credentials. When selecting this mode, no additional   parameters need to be defined as credentials are automatically found based   on the application environment.   To know more about the Google Cloud authentication process, read [the Google Cloud documentation](https://cloud.google.com/docs/authentication/). |
| Google credentials | Paste the content of the JSON file that contains your service account key.  This property is only available when you authenticate using Service account key. |
| Property ID | Select or enter the unique property ID for retrieving Analytics data. For more information, read [the Google Analytics 4 documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id). Information noteTip: To visualize all available property IDs, click the [...] button next to the corresponding field to bring out the Retrieve values dialog box, and click Run in background. A new dialog box opens with all the retrieved property identifiers you can select. |
| Start date/End date | Select or enter the start and end dates corresponding to the report you want to retrieve. |
| Dimensions | Select or enter the name of the dimensions you want to use.  Example: `Page title(PageTitle)`  Fore more information, read [the Google Analytics 4 API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/Dimension).  This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after setting the dimensions in the table. |
| Metrics | Select or enter the name of the metrics you want to use.  Example: `Sessions (sessions)`  Fore more information, read [the Google Analytics 4 API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/Metric).  This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after setting the metrics in the table. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Read timeout | Enter the read timeout value in milliseconds. An exception will occur if the waiting time expires before there is data available to read. |
| Advanced metrics | * Expression: Select or enter the expression   corresponding to the metrics you want to use. Example:   `eventCount/sessions` * Name: Specify a name for the previously defined   expression. The name will help you reuse this expression in a filter   clause. Example: `eventCountPerSession`  For more information, read [the Google Analytics 4 API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/Metric).  This option impacts the schema of the output flow of this component. It is recommended to update the schema by clicking the Guess schema button after setting the metrics in the table. |
| Dimension filter clauses | Define your custom filter clause in JSON format. You can use the expression name defined previously in this clause.  For more information, read [the Google Analytics 4 API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/FilterExpression). |
| Metric filter clauses | Define your custom metric clause in JSON format. You can use the expression name defined previously in this clause.  For more information, read [the Google Analytics 4 API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/FilterExpression). |
| Keep empty rows | Enable this option to include in the response the rows where all metric values are zero. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component or as a start component of a Job or subJob. |
