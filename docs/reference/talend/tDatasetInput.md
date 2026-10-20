<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetinput · versión 8.0 -->
# tDatasetInput

Last updated: 9/30/2026

Creates a flow with data from a Talend Data Preparation
dataset.

tDatasetInput fetches the content of the dataset with the specified ID
to use as input.

Information noteNote: This component is not shipped with your Talend Studio by
default. You need to install the Talend Data Preparation
components in the Data Integration > Components section of the Feature Manager before you can use it in your Talend Studio. For more
information, see [Installing features using the Feature
Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDatasetInput Standard properties

These properties are used to configure tDatasetInput running in the Standard Job framework.

The Standard
tDatasetInput component belongs to the Talend Data Preparation family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Information noteNote: The byte, byte[], char, short, float, and long data types are not supported. |
| URL | Type the URL of the Talend Data Preparation web application, between double quotes.  If you are working with Talend Cloud Data Preparation, use the URL for the corresponding data center to access the application, for example, `https://tdp.us.cloud.talend.com` for the AWS US data center.  For the URLs of available data centers, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Email | Type the email address that you use to log in the Talend Data Preparation web application, between double quotes. |
| Password | Click the [...] button and type your user password for the Talend Data Preparation web application, between double quotes.  If you are working with Talend Cloud Data Preparation and if:   * SSO is enabled, enter an access   token in the field. * SSO is not enabled, enter either   an access token or your password in the field. |
| Dataset Name | Click the Choose a dataset button to select a name from the list. |
| Fetch Schema | Click this button to retrieve the schema from the dataset defined in the Dataset Name field. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Dataset ID | Type the ID of the dataset to be used, between double quotes. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is used as a start component and requires an output link. |
| Limitation | * If the column headers of your dataset in Talend Data Preparation contain whitespaces or special characters, the schema fetched in Talend Studio will be considered invalid. * In Talend Studio, after fetching a schema from a dataset, you can add new columns but you must then give the exact same name (case sensitive) to the equivalent column in Talend Data Preparation. * Variations between the schema of your data in Talend Data Preparation and in Talend Studio may lead to errors. |
