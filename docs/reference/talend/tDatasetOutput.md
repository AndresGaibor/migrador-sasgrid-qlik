<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetoutput · versión 8.0 -->
# tDatasetOutput

Last updated: 9/30/2026

Creates a dataset in Talend Data Preparation.

tDatasetOutput receives input data from the preceding components and
outputs it as a dataset that you can use in Talend Data Preparation.

Information noteNote: This component is not shipped with your Talend Studio by
default. You need to install the Talend Data Preparation
components in the Data Integration > Components section of the Feature Manager before you can use it in your Talend Studio. For more
information, see [Installing features using the Feature
Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tDataSetOutput Standard properties

These properties are used to configure tDataSetOutput running in the Standard Job framework.

The Standard
tDataSetOutput component belongs to the Talend Data Preparation family.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Information noteNote: The date pattern is ignored when using the Date type. |
| Url | Type the URL of the Talend Data Preparation web application, between double quotes.  If you are working with Talend Cloud Data Preparation, use the URL for the corresponding data center to access the application, for example, `https://tdp.us.cloud.talend.com` for the AWS US data center.  For the URLs of available data centers, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Email | Type the email address that you use to log in the Talend Data Preparation web application, between double quotes. This field is only available in Create or Update mode. |
| Password | Click the [...] button and type your user password for the Talend Data Preparation web application, between double quotes. This field is only available in Create or Update mode.  If you are working with Talend Cloud Data Preparation and if:   * SSO is enabled, enter an access   token in the field. * SSO is not enabled, enter either   an access token or your password in the field. |
| Mode | * Create: Creates a new dataset from your input data in Talend Data Preparation . * Update: Uses your input data to update the dataset defined in the Dataset Name field. * Create or update: Creates a new dataset if the dataset defined in Dataset Name does not exist, or updates it if it exists. |
| Dataset Name | Type the name you want to give the new dataset, between double quotes. This field is only available in Create, Update, or Create or update mode. |
| Limit | Specifiy the number of rows to be processed. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component needs incoming data from the preceding component for creating or updating datasets. |
| Limitation | The dataset generated as output of the Job will always be a .csv file, regardless of the type of the input data. |

**Related concepts**  

* [Creating a dataset from a Job](tdatasetoutput-tmysqlinput-creating-dataset-from-job-standard-component-enterprise-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-creating-dataset-from-job-standard-component-enterprise-the -->
# Creating a dataset from a Job

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

The tDatasetOutput is a component that receives input data
from the preceding components and outputs it as a dataset that you can use in Talend Data Preparation or Talend Cloud Data Preparation. To create a dataset via Talend Studio, you must set the
tDatasetOutput component to Create mode.

The following scenario creates a simple Job that :

* extracts information from a database table that holds some
  client-related data,
* outputs this data in the form of a dataset that you can open and prepare
  in the Talend Data Preparation or Talend Cloud Data Preparation.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-adding-and-linking-components-standard-component-enterprise-drop)
* [Configuring the components](/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-configuring-components-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-saving-and-executing-job-standard-component-enterprise-save)

**Related reference**  

* [tDatasetOutput](tdatasetoutput "Creates a dataset in Talend Data Preparation.")

**Related information**  

* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-adding-and-linking-components-standard-component-enterprise-drop -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design
   workspace: tMysqlInput and tDatasetOutput.
2. Connect tMysqlInput and
   tDatasetOutput using a Row > Main link.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Retrieving the data from the database](/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-retrieving-data-from-database-standard-component-enterprise-in)
* [Creating the dataset in Talend Data Preparation](/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-creating-dataset-in-talend-data-preparation-standard-component-enterprise-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-saving-and-executing-job-standard-component-enterprise-save -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Save your Job and press 
   F6
    to execute it.
2. You can now log in the Talend Data Preparation or Talend Cloud Data Preparation web application, where the
   new dataset is available in the Datasets
   view.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-creating-dataset-in-talend-data-preparation-standard-component-enterprise-in -->
# Creating the dataset in Talend Data Preparation

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tDatasetOutput and click
   the Component tab to define its basic settings.
2. Click the Sync columns button to retrieve the schema from the previous
   component, or configure the schema manually by selecting Built-in from the
   Schema list and clicking the [...] button next to
   Edit
   schema.
3. In the URL field, type the
   URL of the Talend Data Preparation or Talend Cloud Data Preparation web application, between double
   quotes. Port 9999 is the default port for Talend Data Preparation.
4. In the Email field, type the
   email address that you use to log in the Talend Data Preparation or Talend Cloud Data Preparation web application, between double
   quotes.
5. In the Password field, type your password for the Talend Data Preparation or Talend Cloud Data Preparation web application, between double
   quotes.

   If you are working with Talend Cloud Data Preparation and if:
   * SSO is enabled, enter an access
     token in the field.
   * SSO is not enabled, enter either
     an access token or your password in the field.

   The user those credentials belong to, will be the owner of the newly created
   dataset. He will also be the one to have the possibility to share this dataset to
   other users.
6. Select the Create mode from the Mode drop-down list.

   Setting the mode to Update allows you to use the input to
   update the dataset defined in the Dataset Name field.
7. In the Dataset Name
   field, enter a name for your dataset, between double quotes,
   `tDatasetOutput_test` in this example.
8. In the Limit field, enter a number that is at
   least equal to the number of rows of your input file. In this example, the limit
   is 500 because the input table has 500 rows.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatasetoutput-tmysqlinput-retrieving-data-from-database-standard-component-enterprise-in -->
# Retrieving the data from the database

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tMysqlInput and click the Component tab to define its basic settings.
2. In the Property Type list, select Built-in to set the database connection details
   manually.
3. In the DB Version list, select the version of
   MySQL you are using, MySQL 5 in this
   example.

   Information noteNote: MySQL 5 has been removed from Talend Studio 8.0 R2026-04. Use MySQL 8.0 or later.
4. In the Host, Port, Database, Username and Password
   fields, enter the MySQL connection details and the user authentication data for
   the database, between double quotes.
5. In the Table Name field, type the name of the
   table to be read, between double quotes.
6. In the Query field,
   enter your database query between double quotes. In this example, the query is
   select \* from employees to retrieve all of the
   information from the table employees, in the
   test database.
7. Click Guess schema to automatically retrieve
   the schema from the database table or enter the schema manually by clicking the
   [...] button next to Edit
   schema.
