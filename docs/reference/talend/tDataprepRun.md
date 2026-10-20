<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun · versión 8.0 -->
# tDataprepRun

Last updated: 9/30/2026

Applies a preparation made using Talend Data Preparation in a
standard Data Integration Job.

tDataprepRun fetches a preparation made using Talend Data Preparation and
applies it to a set of data.

Using the Deployment drop-down list in the Basic
settings of the tDataprepRun component, you can select one of the two
versions of the component:

* The [Cloud deployment](tdatapreprun-standard-properties-cloud "These properties are used to configure the cloud version of tDataprepRun running in the Standard Job framework."),
  that runs the execution on the same engine as the Job. Your data does not leave your
  infrastructure. The only exchange happening is to retrieve the preparation information
  from Talend Cloud Data Preparation.
* The [On-Premises
  deployment](tdatapreprun-standard-properties "These properties are used to configure the on-premises version of tDataprepRun running in the Standard Job framework."), that runs the preparation on the Talend Data Preparation
  server.

Information noteNote: This component is not shipped with your Talend Studio by
default. You need to install the Talend Data Preparation
components in the Data Integration > Components section of the Feature Manager before you can use it in your Talend Studio. For more
information, see [Installing features using the Feature
Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

Information noteNote: For reference, tDataprepRun can process datasets of up to 10 million rows and 100 columns (7GB) at a speed of around 200 rows per second (150kB/s) for a 60-step preparation (these figures are indicative and may vary).
For better performance or datasets beyond 10 million rows, consider using Spark Jobs.

### In this section

* [tDataprepRun Standard properties for a cloud deployment](/talend/en-US/components/8.0/data-preparation/tdatapreprun-standard-properties-cloud)
* [tDataprepRun Standard properties for an on-premises deployment](/talend/en-US/components/8.0/data-preparation/tdatapreprun-standard-properties)
* [tDataprepRun properties for Apache Spark Batch](/talend/en-US/components/8.0/data-preparation/tdatapreprun-properties-for-apache-spark-batch)
* [tDataprepRun properties for Apache Spark Streaming (deprecated)](/talend/en-US/components/8.0/data-preparation/tdatapreprun-properties-for-apache-spark-streaming)

**Related concepts**  

* [Applying a preparation to a data sample in an Apache Spark Batch Job](tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-applying-preparation-to-data-sample-in-apache-spark-batch-job-spark-batch-component-the)
* [Applying a preparation to a data sample in an Apache Spark Streaming Job](tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-applying-preparation-to-data-sample-in-apache-spark-streaming-job-spark-stream-component-the)
* [Dynamically selecting a preparation at runtime according to the input](tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-dynamically-selecting-preparation-at-runtime-according-to-input-standard-component-enterprise-the)
* [Preparing data from a database in a Talend Job](tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-preparing-data-from-database-in-talend-job-standard-component-enterprise-the)
* [Promoting a Job leveraging a preparation across environments](tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-promoting-job-leveraging-preparation-across-environments-standard-component-enterprise-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-properties-for-apache-spark-batch -->
# tDataprepRun properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tDataprepRun running in
the Spark Batch Job framework.

The Spark Batch
tDataprepRun component belongs to the
Talend Data Preparation family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

## Basic settings

| Properties | Description |
| --- | --- |
| URL | Type the URL to the Talend Data Preparation web application, between double quotes.  If you are working with Talend Cloud Data Preparation, use the URL for the corresponding data center to access the application, for example, `https://tdp.us.cloud.talend.com` for the AWS US data center.  For the URLs of available data centers, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Email | Type the email address that you use to log in the Talend Data Preparation web application, between double quotes. |
| Password | Click the [...] button and type your user password for the Talend Data Preparation web application, between double quotes.  If you are working with Talend Cloud Data Preparation and if:   * SSO is enabled, enter an access   token in the field. * SSO is not enabled, enter either   an access token or your password in the field. |

When using the default preparation selection properties:

| Properties | Description |
| --- | --- |
| Preparation | * To complete the Preparation field, click Choose   an existing preparation and select one of the previously created   preparations in a pop-up dialog box. This dialog box shows the name, path, author, and   last modification date of each preparation. * Click this button to edit the preparation in Talend Data Preparation that corresponds to the ID defined   in the Preparation field. |
| Version | If you have created several versions of your preparation, you can choose which one you want to use in the Job. To complete the Version field, click Choose a Version to select from the list of existing versions, including the current version of the preparation. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Fetch Schema | Click this button to retrieve the schema from the preparation defined in the Preparation field. |

When using the Dynamic preparation selection:

| Properties | Description |
| --- | --- |
| Dynamic preparation selection | Select this checkbox to define a preparation path and version using context variables. The preparation will be dynamically selected at runtime. |
| Preparation path | Use a context variable to define a preparation path. Paths with or without the initial / are supported. |
| Preparation version | Use a context variable to define the version of the preparation to use. Preparation versions are referenced by their number. As a consequence, to execute the version #2 of a preparation for example, the expected value is "2". To use the current version of the preparation, the expected value is "Current state". |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Fetch Schema | Click this button to dynamically retrieve the schema from the preparations defined by the context variable in the Preparation path field. If the fetch is successful, any previously configured schema will be overwritten. If the fetch fails, the current schema is kept. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Encoding | Select an encoding mode from this list. You can select Custom from the list to enter an encoding method in the field that appears. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is an intermediary step. It requires an input flow as well as an output. |
| Limitations | * If the dataset is updated after the tDataprepRun component has been configured, the   schema needs to be fetched again. * If a context variable was used in the URL of the   dataset, you cannot use the  button to edit the preparation   directly in Talend Data Preparation. * The Make as header and Delete   row functions, as well as any modification of a single   cell, are ignored by the tDataprepRun component. These   functions only affect a single row or cell and are thus not compatible   with a big data context. In the list of existing preparations to choose   from, a warning is displayed next to preparations that include   incompatible actions. |
| Yarn cluster mode | When the Yarn cluster mode is selected, the Job driver is not executed on a local machine, but rather on a machine from the Hadoop Cluster. As it is not possible to know in advance which node of the cluster the Job will be executed on, verify that all the cluster nodes are accessible by the Talend Data Preparation server. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-standard-properties -->
# tDataprepRun Standard properties for an on-premises deployment

Last updated: 9/30/2026

These properties are used to configure the on-premises version of
tDataprepRun running in the Standard Job
framework.

The Standard
tDataprepRun component belongs to the Talend Data Preparation family.

To use the on-premises deployment version of the tDataprepRun component, select
On-premises from the Deployment drop-down
list of the component's basic settings.

The component in this framework is available in all
subscription-based Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| URL | Type the URL to the Talend Data Preparation web application, between double quotes.  If you are working with Talend Cloud Data Preparation, use the URL for the corresponding data center to access the application, for example, `https://tdp.us.cloud.talend.com` for the AWS US data center.  For the URLs of available data centers, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
| Username | Type the email address that you use to log in the Talend Data Preparation web application, between double quotes. |
| Password | Click the [...] button and type your user password for the Talend Data Preparation web application, between double quotes.  If you are working with Talend Cloud Data Preparation and if:   * SSO is enabled, enter an access   token in the field. * SSO is not enabled, enter either   an access token or your password in the field. |

When using the default preparation selection properties:

| Properties | Description |
| --- | --- |
| Preparation | To complete the Preparation field, do one of the following:  * click Choose an existing preparation and select   one of the previously created preparations in a pop-up dialog box. This   dialog box shows the name, path, author, and last modification date of each   preparation. * click Or create a new one and create a new   preparation based on your input data. |
|  | Click this button to edit the preparation in Talend Data Preparation that corresponds to the ID defined in the Preparation field. |
| Version | If you have created several versions of your preparation, you can choose which one you want to use in the Job. To complete the Version field, click Choose a Version to select from the list of existing versions, including the current version of the preparation. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job.  tDataprepRun offers the advantage of the dynamic schema feature. This feature allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schema, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  Information noteNote: The dynamic schema feature is not supported when creating a new preparation. It is designed for the purpose of retrieving unknown columns and is recommended to be used for this purpose only. |
| Fetch Schema | Click this button to retrieve the schema from the preparation defined in the Preparation field. |

When using the Dynamic preparation selection:

| Properties | Description |
| --- | --- |
| Dynamic preparation selection | Select this checkbox to define a preparation path and version using context variables. The preparation will be dynamically selected at runtime. |
| Preparation path | Use a context variable to define a preparation path. Paths with or without the initial / are supported. |
| Preparation version | Use a context variable to define the version of the preparation to use. Preparation versions are referenced by their number. As a consequence, to execute the version #2 of a preparation for example, the expected value is "2". To use the current version of the preparation, the expected value is "Current state". |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Fetch Schema | Click this button to dynamically retrieve the schema from the preparations defined by the context variable in the Preparation path field. If the fetch is successful, any previously configured schema will be overwritten. If the fetch fails, the current schema is kept. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Limit Preview | Specify the number of rows to which you want to limit the preview. This option works only when creating a new preparation. |
| Exclude technical columns (for dynamic) | If you are using a dynamic schema for this component, this option removes the extra technical columns that are automatically added to the output results.  This option is selected by default. |
| Use column labels for dynamic schema | If you are using a dynamic schema for this component, this option uses the column labels as shown in your preparation rather than the technical ones. It allows you to retrieve the actual data, using a tExtractDynamicFields component for example.  This option is selected by default. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component is an intermediary step. It requires an input flow as well as an output. |
| Limitations | * If the dataset is updated after the tDataprepRun component has been   configured, the schema needs to be fetched again. * If a context variable was used in the URL of the   dataset, you cannot use the  button to edit the   preparation directly in Talend Data Preparation. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-standard-properties-cloud -->
# tDataprepRun Standard properties for a cloud deployment

Last updated: 9/30/2026

These properties are used to configure the cloud version of
tDataprepRun running in the Standard Job
framework.

The Standard
tDataprepRun component belongs to the Talend Data Preparation family.

To use the cloud deployment version of the tDataprepRun component, select
Cloud from the Deployment drop-down
list of the component's basic settings.

The component in this framework is available in all
subscription-based Talend
products.

Information noteWarning: The cloud version of tDataprepRun has a large amount of dependencies.
When using this component in ESB cases, if the build type of the Job is set to
Talend Runtime (OSGi), you need to increase the memory size
by specifying `-Xmx2048m` or bigger in the
.ini file under the Talend Studio
installation directory according to your operating system. Otherwise the execution of
the Job might fail with the OutOfMemoryError exception.

## Basic settings

| Deployment | From the drop-down list, select your current deployment type, Cloud in this case, and click Apply.  With this setting, your data will not transit in Talend Cloud, and the preparation will be run locally. |
| Property Type | Either Built-in or Repository.   * Built-In: You create and store the schema   locally for this component only. * Repository: You have already created the   schema and stored it in the Repository. You can reuse it in various   projects and Job designs. |
| Data Preparation server | From the drop-down list, select the data center that corresponds to your region:   * EU * US * US-West * AU * AP * Custom (to enter the endpoint manually) |
| Authentication type | * Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated) This content is deprecated. Basic, to log in to   your Talend Cloud Data Preparation instance using your login and password information. * PAT, to log in to your Talend Cloud Data Preparation instance using a Personal Access Token. |
| Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated) This content is deprecated.  Login | Type the email address that you use to log in the Talend Cloud Data Preparation application.  This field is only available if you select Basic from the Authentication type drop-down list. |
| Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated) This content is deprecated.  Password | Click the [...] button and type your user password for the Talend Cloud Data Preparation application, between double quotes.  This field is only available if you select Basic from the Authentication type drop-down list. |
| PAT | Click the [...] and enter your Personal Access Token between double quotes. A PAT can be retrieved from the Profile preferences page of Talend Cloud. See [Generating a Personal Access Token](https://help.qlik.com/talend/r/en-US/Cloud/management-console-user-guide/cloud-access-token) for more information.  This field is only available if you select PAT from the Authentication type drop-down list. |
| Dynamic preparation selection | Select this check box to define a preparation path and version using context variables or manually entered values. The preparation will be dynamically selected at runtime. |
| Preparation path | Use a context variable to define a preparation path. Paths with or without the initial / are supported.  This field is only available if you select the Dynamic preparation selection check box. |
| Preparation version | Use a context variable to define the version of the preparation to use. Preparation versions are referenced by their number. As a consequence, to execute the version #2 of a preparation for example, the expected value is "2". To use the current version of the preparation, the expected value is "Current state".  This field is only available if you select the Dynamic preparation selection check box. |
| Preparation identifier | Use the [...] button to select a preparation from the list. |
| Preparation version | Use the [...] button to select a version from the list.  Preparation versions are referenced by their number, starting from the oldest in ascending order. After selecting a version, the corresponding preparation ID will display in the Preparation version field. If you select the current version, it will show as HEAD in the field. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Click Sync columns to retrieve the schema from the previous component connected in the Job. |
| Guess Schema | Click this button to retrieve the schema from the preparation defined in the Preparation identifier field. |

## Advanced settings

| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |
| Use Dictionary | Select this check box if your preparation includes steps that modify the semantic types of the columns or functions that use semantic types. When selected, you need to configure the following parameters:   * Personal access token: Use the [...] button   to enter a personal access token, that you can retrieve in the   Profile preferences page of Talend Cloud, between double quotes. This field is only available If you   have selected Basic as   Authentication type. * Dictionary version: Click the [...] button to   select the latest version from the list. |

## Usage

| Usage rule | This component is an intermediary step. It requires an input flow as well as an output. |
| Best practice | When using dynamic mode, any potential lookup dataset called as dependency of the Job has to be from the same technology as the source dataset of the preparation, or the Job will fail. A good practice to work around this is to directly specify the dependencies in advance using a tLibraryLoad component for example and connect it to the Job using the tDataprepRun with an On Subjob Ok link. |
| Limitations | * If the dataset is updated after the   tDataprepRun component has been   configured, the schema needs to be fetched again. * Preparations that use a Join/Lookup   transformation do not support lookup datasets from local file   storage (localstorage). If a recipe depends on   localstorage for the lookup dataset, the Job   can fail at runtime. Workaround: Upload the lookup file to a supported storage   technology and update the preparation to use that dataset. * The cloud deployment mode will not work when using a Talend Runtime or a Cloud Engine for Design. * Preparations created prior to the R2024-12 monthly release need to   be opened at least once in the Talend Cloud Data Preparation interface. This ensures that the preparations are persisted in   the Talend Cloud Data Preparation database, and can be used in Talend Studio Jobs regardless of the state of the Remote Engine Gen2. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-promoting-job-leveraging-preparation-across-environments-standard-component-enterprise-the -->
# Promoting a Job leveraging a preparation across environments

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

The tDataprepRun component allows you to reuse an existing preparation made in Talend Data Preparation, directly in a data integration, Spark Batch
or Spark Streaming Job. In other words, you can operationalize the process of applying a
preparation to input data with the same model.

A good practice when using Talend Data Preparation is to set up at least two environments to
work with: a development one, and a production one for example. When a preparation is ready on
the development environment, you can use the Import/Export
Preparation feature to promote it to the production environment, that has a
different URL. For more information, see the section about promoting a preparation across
environments.

Following this logic, you will likely find yourself with a preparation that has the same name
on different environments. The thing is that preparations are not actually identified by their
name, but rather by a technical id, such as
prepid=faf4fe3e-3cec-4550-ae0b-f1ce108f83d5. As a consequence, what you
really have is two dinstinct preparations, each with its specific id.

In case you wanted to operationalize this recipe in a Talend Job using the regular preparation selection
properties, you would actually need two Jobs: one for the preparation on the development
environment, with a specific url and id, and a second one for the production environment, with
different parameters.

Through the use the Dynamic preparation selection checkbox and some
context variables, you will be able to use a single Job to run your preparation, regardless of
the environment. Indeed, the dynamic preparation selection relies on the preparation path in
Talend Data Preparation, and not on the preparation id.

You will be able to use a single Job definition to later deploy on your development or
production environment

The following scenario creates a simple Job that:

* Receives data from a local CSV file containing customers data
* Dynamically retrieves an existing preparation based on its path and
  environment
* Applies the preparation on the input data
* Outputs the prepared data into a MySQL database.

In this example, the Customers\_leads preparation has
been created beforehand in Talend Data Preparation. This
simple preparation was created on a dataset that has the same schema as the CSV file used
as input for this Job, and its purpose is to remove invalid values from your customers
data.

### In this section

* [Designing the Job](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-designing-job-standard-component-enterprise-in)
* [Creating contexts for your different environments](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-creating-contexts-for-your-different-environments-standard-component-enterprise-click)
* [Configuring the components](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-configuring-components-standard-component-enterprise)
* [Deploying the Job to production](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-deploying-job-to-production-standard-component-enterprise-save)

**Related concepts**  

* [tDataprepRun](tdatapreprun "Applies a preparation made using Talend Data Preparation in a standard Data Integration Job.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tMysqlOutput](/talend/en-US/components/8.0/mysql/tmysqloutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-dynamically-selecting-preparation-at-runtime-according-to-input-standard-component-enterprise-the -->
# Dynamically selecting a preparation at runtime according to the input

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

The tDataprepRun component allows you to reuse an existing preparation
made in Talend Data Preparation, directly in a data
integration, Spark Batch or Spark Streaming Job. In other words, you can operationalize the
process of applying a preparation to input data with the same model.

By default, the tDataprepRun component retrieves
preparations using their technical id. However, the dynamic preparation selection feature
allows you to call a preparation via its path in Talend Data Preparation. Through the use of the Dynamic
preparation selection check box and some variables, it is then possible to
dynamically select a preparation at runtime, according to runtime data or metadata.

In case you wanted to operationalize preparations in a Talend Job using the regular preparation selection
properties, you would actually need several Jobs: one for each preparation to apply on a
specific dataset. By retrieving the correct preparation according to the input file name, you
will be able to dynamically run more than one preparation on your source data, in a single
Job.

The following scenario creates a Job that:

* Scans the content of a folder containing several datasets
* Creates a dynamic path to your CSV files
* Dynamically retrieves the preparations according to the input file name and
  applies them on the data
* Outputs the prepared data into a Redshift database

In this example, .csv datasets with data from two of your
clients are locally stored in a folder called customers\_files. Each of
your clients datasets have their specific naming convention and are stored in dedicated sub
folders. All the datasets in the customers\_files folder have identical
schemas, or data model.

A customers folder has also been created in Talend Data Preparation, containing two preparations. These two
distinct preparation are each aimed at cleaning data from your two different customers.

The purpose of customer\_1\_preparation for example is to isolate a
certain type of email addresses, while customer\_2\_preparation aims at
cleansing invalid values and formatting the data. In this example, the preparations names are
based on the two sub folders names customer\_1 and
customer\_2, with `_preparation` as suffix.

Just like the input schema that all four dataset have in common, all of your output data must
also share the same model. For this reason, you cannot have one preparation that modifies the
schema by adding a column for example, while the other does not.

By following this scenario, a single Job will allow you to use the appropriate preparation,
depending on whether the dataset extracted from the local customers\_files
folder belongs to customer 1 or customer 2.

### In this section

* [Designing the Job](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-designing-job-standard-component-enterprise-in)
* [Configuring the components](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-configuring-components-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-saving-and-executing-job-standard-component-enterprise-save)

**Related concepts**  

* [tDataprepRun](tdatapreprun "Applies a preparation made using Talend Data Preparation in a standard Data Integration Job.")

**Related information**  

* [tFileList](/talend/en-US/components/8.0/tfilelist/tfilelist)
* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tRedshiftOutput](/talend/en-US/components/8.0/amazon-redshift/tredshiftoutput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-applying-preparation-to-data-sample-in-apache-spark-batch-job-spark-batch-component-the -->
# Applying a preparation to a data sample in an Apache Spark Batch Job

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend products
with Big Data.

The tDataprepRun component allows you to reuse an existing
preparation made in Talend Data Preparation or
Talend Cloud Data Preparation, directly in a big data Job. In other words, you can operationalize the process of
applying a preparation to input data with the same model.

The following scenario creates a simple Job that :

* Reads a small sample of customer data,
* applies an existing preparation on this data,
* shows the result of the execution in the console.

This assumes that a preparation has been created beforehand,
on a dataset with the same schema as your input data for the Job. In this case, the
existing preparation is called datapreprun\_spark.

Information noteNote: Having the same schema on both ends ensures a coherent result, but the Job will still
run even if the schema is different.

This simple preparation puts the customer last names into upper case and
applies a filter to isolate the customers from California, Texas and Florida.

Note that if a preparation contains actions that only affect a single row, or cells, they
will be skipped by the tDataprepRun component during the job. The Make as
header or Delete Row functions for example, do not
work in a big data context.

The sample data reads as
follows:

```
James;Butt;California
Daniel;Fox;Connecticut
Donna;Coleman;Alabama
Thomas;Webb;Illinois
William;Wells;Florida
Ann;Bradley;California
Sean;Wagner;Florida
Elizabeth;Hall;Minnesota
Kenneth;Jacobs;Florida
Kathleen;Crawford;Texas
Antonio;Reynolds;California
Pamela;Bailey;Texas
Patricia;Knight;Texas
Todd;Lane;New Jersey
Dorothy;Patterson;Virginia
```

Information noteNote: The sample data is created for demonstration purposes only.

tHDFSConfiguration is used in this scenario by Spark to connect
to the HDFS system where the jar files dependent on the Job are transferred.

In the Spark
Configuration tab in the Run
view, define the connection to a given Spark cluster for the whole Job. In
addition, since the Job expects its dependent jar files for execution, you must
specify the directory in the file system to which these jar files are
transferred so that Spark can access these files:

* Yarn mode (Yarn client or Yarn cluster):
  + When using Google Dataproc, specify a bucket in the
    Google Storage staging bucket
    field in the Spark configuration
    tab.
  + When using HDInsight, specify the blob to be used for Job
    deployment in the Windows Azure Storage
    configuration area in the Spark
    configuration tab.
  + When using Altus, specify the S3 bucket or the Azure
    Data Lake Storage for Job deployment in the Spark
    configuration tab.
  + When using on-premises distributions, use
    the configuration component corresponding to the file system
    your cluster is using. Typically, this system is HDFS and so
    use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
* Standalone mode: use the
  configuration component corresponding to the file system your cluster is
  using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

  If you are using Databricks without any configuration component present
  in your Job, your business data is written directly in DBFS (Databricks
  Filesystem).

Prerequisite: ensure that the Spark
cluster has been properly installed and is running.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-adding-and-linking-components-spark-batch-component-in)
* [Selecting the Spark mode](/talend/en-US/components/8.0/data-preparation/selecting-spark-mode-spark-batch?id=819)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/data-preparation/configuring-connection-to-file-system-to-be-used-by-spark?id=820)
* [Configuring the input data and the preparation](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-configuring-input-data-and-preparation-spark-batch-component)
* [Executing the Job](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-executing-job-spark-batch-component-in)

**Related concepts**  

* [tDataprepRun](tdatapreprun "Applies a preparation made using Talend Data Preparation in a standard Data Integration Job.")

**Related information**  

* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tS3Configuration](/talend/en-US/components/8.0/amazon-s3/ts3configuration)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-applying-preparation-to-data-sample-in-apache-spark-streaming-job-spark-stream-component-the -->
# Applying a preparation to a data sample in an Apache Spark Streaming Job

Last updated: 9/30/2026

This scenario applies only to Talend Real-Time Big Data Platform and
Talend Data Fabric.

The tDataprepRun component allows you to reuse an existing preparation
made in Talend Data Preparation or
Talend Cloud Data Preparation, directly in a big data Job. In other words, you can operationalize the process of
applying a preparation to input data with the same model.

The following scenario creates a simple Job that :

* Reads a small sample of customer data,
* applies an existing preparation on this data,
* shows the result of the execution in the console.

This assumes that a preparation has been created beforehand, on a dataset
with the same schema as your input data for the Job. In this case, the existing preparation
is called datapreprun\_spark.

Information noteNote: Having the same schema on both ends ensures a coherent result, but the Job will still
run even if the schema is different.

This simple preparation puts the customer last names into upper case and
applies a filter to isolate the customers from California, Texas and Florida.

Note that if a preparation contains actions that only affect a single row, or cells, they
will be skipped by the tDataprepRun component during the job. The
Make as header or Delete Row functions for
example, do not work in a big data context.

The sample data reads as
follows:

```
James;Butt;California
Daniel;Fox;Connecticut
Donna;Coleman;Alabama
Thomas;Webb;Illinois
William;Wells;Florida
Ann;Bradley;California
Sean;Wagner;Florida
Elizabeth;Hall;Minnesota
Kenneth;Jacobs;Florida
Kathleen;Crawford;Texas
Antonio;Reynolds;California
Pamela;Bailey;Texas
Patricia;Knight;Texas
Todd;Lane;New Jersey
Dorothy;Patterson;Virginia
```

Information noteNote: The sample data is created for demonstration purposes only.

tHDFSConfiguration is used in this scenario by Spark to connect
to the HDFS system where the jar files dependent on the Job are transferred.

In the Spark
Configuration tab in the Run
view, define the connection to a given Spark cluster for the whole Job. In
addition, since the Job expects its dependent jar files for execution, you must
specify the directory in the file system to which these jar files are
transferred so that Spark can access these files:

* Yarn mode (Yarn client or Yarn cluster):
  + When using Google Dataproc, specify a bucket in the
    Google Storage staging bucket
    field in the Spark configuration
    tab.
  + When using HDInsight, specify the blob to be used for Job
    deployment in the Windows Azure Storage
    configuration area in the Spark
    configuration tab.
  + When using Altus, specify the S3 bucket or the Azure
    Data Lake Storage for Job deployment in the Spark
    configuration tab.
  + When using on-premises distributions, use
    the configuration component corresponding to the file system
    your cluster is using. Typically, this system is HDFS and so
    use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration).
* Standalone mode: use the
  configuration component corresponding to the file system your cluster is
  using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).

  If you are using Databricks without any configuration component present
  in your Job, your business data is written directly in DBFS (Databricks
  Filesystem).

Prerequisite: ensure that the Spark cluster has been properly
installed and is running.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-adding-and-linking-components-spark-stream-component-in)
* [Selecting the Spark mode](/talend/en-US/components/8.0/data-preparation/selecting-spark-mode-spark-batch?id=827)
* [Configuring the connection to the file system to be used by Spark](/talend/en-US/components/8.0/data-preparation/configuring-connection-to-file-system-to-be-used-by-spark?id=829)
* [Configuring the input data and the preparation](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-configuring-input-data-and-preparation-spark-stream-component)
* [Executing the Job](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-executing-job-spark-stream-component-in)

**Related concepts**  

* [tDataprepRun](tdatapreprun "Applies a preparation made using Talend Data Preparation in a standard Data Integration Job.")

**Related information**  

* [tHDFSConfiguration](/talend/en-US/components/8.0/hdfs/thdfsconfiguration)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tS3Configuration](/talend/en-US/components/8.0/amazon-s3/ts3configuration)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-preparing-data-from-database-in-talend-job-standard-component-enterprise-the -->
# Preparing data from a database in a Talend Job

Last updated: 9/30/2026

This scenario applies only to subscription-based Talend
products.

The tDataprepRun component allows you to reuse an existing
preparation made in Talend Data Preparation or Talend Cloud Data Preparation, directly in a data integration Job. In
other words, you can operationalize the process of applying a preparation to input data with
the same model.

The following scenario creates a simple Job
that :

* retrieves a table from a MySQL database, that holds some employee-related
  data,
* applies an existing preparation on this data,
* outputs the prepared data into an Excel file.

This assumes that a preparation has been created beforehand,
on a dataset with the same schema as your input data for the Job. In this case, the existing
preparation is called datapreprun\_scenario.

Information noteNote: Having the same schema on both ends ensures
a coherent result, but the Job will still run even if the schema is different.

This simple preparation puts the employees last names into upper case and
isolate the employees with a salary greater than 1500$.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-adding-and-linking-components-standard-component-enterprise-in)
* [Configuring the components](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-configuring-components-standard-component-enterprise)
* [Saving and executing the Job](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-saving-and-executing-job-standard-component-enterprise-save)

**Related concepts**  

* [tDataprepRun](tdatapreprun "Applies a preparation made using Talend Data Preparation in a standard Data Integration Job.")

**Related information**  

* [tMysqlInput](/talend/en-US/components/8.0/mysql/tmysqlinput)
* [tFileOutputExcel](/talend/en-US/components/8.0/excel/tfileoutputexcel)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Retrieving the data from a CSV file](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-retrieving-data-from-csv-file-standard-component-enterprise-in)
* [Dynamically selecting the preparation from Talend Data Preparation](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-dynamically-selecting-preparation-from-talend-data-preparation-standard-component-enterprise-in)
* [Outputting the result of the preparation into a database](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-outputting-result-of-preparation-into-database-standard-component-enterprise-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-creating-contexts-for-your-different-environments-standard-component-enterprise-click -->
# Creating contexts for your different environments

Last updated: 9/30/2026

For your Job to be usable in differents situations, you will create two distincts
contexts.

Talend Studio allows you to create a set of
variables that you can regroup in a context. In this example, you will create a context
called Development and another one called
Production. Each of these contexts will contain the variables to
be used for the tDataprepRun configuration, according to the
target environment.

## Procedure

1. Click the Context view of your
   Job.
2. Click the + button on the top right of the variables
   table to create a new context.
3. Select the Default context and click
   Edit... to rename it
   `Development`.
4. Click New... to create a new context called
   `Production`.
5. Click the + button on the bottom left of the variables
   table to create a new variable called
   `parameter_URL`.

   The parameter\_ prefix is mandatory, in order for the
   variable to be retrievable in Talend Management Console, if you use the Cloud
   version of Talend Data Preparation.
6. On the newly created URL line, enter the URLs of your
   development and production instances of Talend Data Preparation in the corresponding
   columns.
7. Repeat the last two steps in order to create the
   parameter\_USERNAME and
   parameter\_PASSWORD variables, that will store your
   Talend Data Preparation credentials depending
   on the environment.

   If Multi Factor Authentication is activated, use your authentication token
   instead of your password when creating the
   parameter\_PASSWORD variable.

## Results

These two different contexts will be available at execution time, when deploying your
Job.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-deploying-job-to-production-standard-component-enterprise-save -->
# Deploying the Job to production

Last updated: 9/30/2026

Now that the Job has been designed, you can deploy it to production and use it to
operationalize your preparation on real data.

## Procedure

1. Save your Job.
2. To promote your Job to production, export it to Talend Administration Center.
3. Create an execution task with the production context variables and configure
   your preferred schedule.

   For more information on how to create an execution task
   with the appropriate context variables, see [Working with Job execution tasks](/talend/r/en-US/8.0/administration-center-user-guide/working-with-job-execution-tasks).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-designing-job-standard-component-enterprise-in -->
# Designing the Job

Last updated: 9/30/2026

## Procedure

1. In the 
   Integration
    perspective of Talend Studio, create an empty Standard Job
   from the Job Designs node in the
   Repository tree view.
2. Drop the following components from the Palette onto the design workspace: tFileInputDelimited, tDataprepRun and tMysqlOutput.
3. Connect the three components using Row > Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Reading the input files from your local folder](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-reading-input-files-from-your-local-folder-standard-component-enterprise-in)
* [Dynamically selecting the preparation from Talend Data Preparation](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-dynamically-selecting-preparation-from-talend-data-preparation-standard-component-enterprise-in)
* [Outputting the result of the preparation into a database](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-outputting-result-of-preparation-into-database-standard-component-enterprise-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-designing-job-standard-component-enterprise-in -->
# Designing the Job

Last updated: 9/30/2026

## Procedure

1. In the Integration
   perspective of Talend Studio,
   create an empty Standard, Spark Batch or Spark Streaming Job from the Job
   Designs node in the Repository tree view.
2. Drop the following components from the palette onto the
   design workspace: two tFileList, a
   tFileInputDelimited, a tDataprepRun and a
   tRedshiftOutput.
3. Connect the two tFileList and the
   tFileInputDelimited components using Row > Iterate links.
4. Connect the tFileInputDelimited,
   tDataprepRun and tRedshiftOutput
   components using Row > Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-saving-and-executing-job-standard-component-enterprise-save -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Save your Job.
2. Press F6 to execute it.

## Results

The four datasets have been dynamically prepared with a single Job, using the
preparation dedicated to each of your customers and the output of those four
preparations has been sent to a Redshift database, in four new tables.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-adding-and-linking-components-spark-batch-component-in -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. In the 
   Integration
    perspective of Talend Studio, create an empty Spark Batch
   Job from the Job Designs node in the
   Repository tree view.

   For further information about how to create a Spark Batch Job, see [Creating a Spark Job](/talend/r/en-US/8.0/studio-user-guide/creating-spark-job).
2. Drop the following components from the Palette onto the design workspace:
   tHDFSConfiguration, tFixedFlowInput, tDataprepRun and tLogRow.
3. Connect the last three components using Row > Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-configuring-input-data-and-preparation-spark-batch-component -->
# Configuring the input data and the preparation

Last updated: 9/30/2026

### In this section

* [Loading the sample data](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-loading-sample-data-spark-batch-component-in)
* [Accessing the preparation from Talend Data Preparation](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-accessing-preparation-from-talend-data-preparation-spark-batch-component-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-executing-job-spark-batch-component-in -->
# Executing the Job

Last updated: 9/30/2026

The tLogRow component is used to present the
execution result of the Job.

## Procedure

1. In the design workspace, select the tLogRow
   component and click the Component tab to define
   its basic settings.
2. Select the Table radio button to present the
   result in a table.
3. Save your Job and press 
   F6
    to execute it.
4. You can now check the execution result in the console of the Run view.

## Results

The preparation made in Talend Data Preparation or Talend Cloud Data Preparation has been applied to the sample
data and only the customer from California, Florida and Texas remain.

For the sake of this example, we used a small data sample, but the Spark
Batch version of the tDataprepRun component can be used with high
volume of data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-adding-and-linking-components-spark-stream-component-in -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. In the 
   Integration
    perspective of Talend Studio, create an empty Spark
   Streaming Job from the Job Designs node in the
   Repository tree view.

   For further information about how to create a Spark Streaming Job, see [Creating a Spark Job](/talend/r/en-US/8.0/studio-user-guide/creating-spark-job).
2. Drop the following components from the Palette onto the
   design workspace: tHDFSConfiguration,
   tFixedFlowInput, tDataprepRun and tLogRow.
3. Connect the last three components using Row > Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-configuring-input-data-and-preparation-spark-stream-component -->
# Configuring the input data and the preparation

Last updated: 9/30/2026

### In this section

* [Loading the sample data](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-loading-sample-data-spark-stream-component-in)
* [Accessing the preparation from Talend Data Preparation](/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-accessing-preparation-from-talend-data-preparation-spark-stream-component-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-executing-job-spark-stream-component-in -->
# Executing the Job

Last updated: 9/30/2026

The tLogRow component is used to present the execution result of the
Job.

## Procedure

1. In the design workspace, select the tLogRow
   component and click the Component tab to define
   its basic settings.
2. Select the Table radio button to present the
   result in a table.
3. Save your Job and press 
   F6
    to
   execute it.
4. You can now check the execution result in the console of the Run view.

## Results

The preparation made in Talend Data Preparation or
Talend Cloud Data Preparation has been applied to the
sample data and only the customer from California, Florida and Texas remain.

For the sake of this example, we used a small data sample, but the Spark
Batch version of the tDataprepRun component can be used with high
volume of data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-adding-and-linking-components-standard-component-enterprise-in -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. In the Integration perspective of Talend Studio,
   create an empty Standard Job from the Job
   Designs node in the Repository
   tree view.
2. Drop the following components from the Palette onto the design workspace: tMysqlInput, tDataprepRun and
   tFileOutputExcel.
3. Connect the three components using Row > Main links.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-configuring-components-standard-component-enterprise -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Retrieving the data from the database](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-retrieving-data-from-database-standard-component-enterprise-in)
* [Accessing the preparation from Talend Data Preparation](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-accessing-preparation-from-talend-data-preparation-standard-component-enterprise-in)
* [Outputting the preparation into an Excel file](/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-outputting-preparation-into-excel-file-standard-component-enterprise-in)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-saving-and-executing-job-standard-component-enterprise-save -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Save your Job and press 
   F6
    to execute it.
2. You can now open the Excel file containing the result of the preparation
   applied on your data from the MySQL database.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-dynamically-selecting-preparation-from-talend-data-preparation-standard-component-enterprise-in -->
# Dynamically selecting the preparation from Talend Data Preparation

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tDataprepRun
   and click the Component tab to define its
   basic settings.
2. In the URL field, enter
   `context.parameter_URL` to reuse one of the values
   previously set for the URL context variable.
3. In the Username and
   Password fields, respectively enter
   `context.parameter_USERNAME` and
   `context.parameter_PASSWORD` to reuse one of the values
   previously set for the USERNAME and PASSWORD
   context variables.
4. Select the Dynamic preparation selection checkbox to
   define a preparation with its path in Talend Data Preparation rather than its technical
   id.
5. In the Preparation path field, enter the path to the
   customers\_leads preparation you want to apply on the
   .csv file.

   Your preparation must have the same path on your Talend Data Preparation development environment
   and production environment.
6. In the Preparation version field, type
   `Current state` between double quotes, in order to use the
   current version of the preparation.
7. Click Fetch Schema to
   retrieve the schema of the preparation.

   The output schema of the tDataprepRun component now
   reflects the changes made with each preparation step. The schema takes into
   account columns that were added or removed for example. By default, the output
   schema will use the String type for all the columns, in order
   not to overwrite any formatting operations performed on dates or numeric values
   during the preparation.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-outputting-result-of-preparation-into-database-standard-component-enterprise-in -->
# Outputting the result of the preparation into a database

Last updated: 9/30/2026

The result of the preparation will be exported to a MySQL database.

## Procedure

1. In the design workspace, select tDataprepRun and click the
   Component tab to define its basic
   settings.
2. In the Property Type list, select Built-in to set the
   database connection details manually.
3. In the DB Version list, select the version of MySQL you are
   using, MySQL 5 in this
   example.

   Information noteNote: MySQL 5 has been removed from Talend Studio 8.0 R2026-04. Use MySQL 8.0 or later.
4. In the Host, Port,
   Database, Username and
   Password fields, enter the MySQL connection details and the
   user authentication data for the database, between double quotes.
5. In the Table Name field, type the name of the table to be
   write in, between double quotes.
6. From the Action on table drop-down list, select
   Create table if does not exist.
7. From the Action on data drop-down list, select
   Insert.
8. Click Sync columns to retrieve the new output schema,
   inherited from the tDataprepRun component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfileinputdelimited-tmysqloutput-tmysqloutput-retrieving-data-from-csv-file-standard-component-enterprise-in -->
# Retrieving the data from a CSV file

Last updated: 9/30/2026

The input data retrieved by the component must have same model as the dataset on
wich the preparation to operationalize was created.

## Procedure

1. In the design workspace, select the
   tFileInputDelimited component, and click the
   Component tab to define its basic settings.

   Fields marked with a \* are mandatory.
2. In the Property Type list, select
   Built-in.
3. In the File name/Stream field, enter the path to the
   file containing the input data on which you want to apply the preparation.
4. Define the characters to be used as Row Separator and
   Field Separator.
5. Cick the Edit schema button to define the columns of the
   source dataset and their data type.

   Make sure that the schema of the tFileInputDelimited
   component matches the schema expected by the
   tDataprepRun component. In other words, the input
   schema must be the same as the dataset upon which the preparation was made
   in the first place.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-dynamically-selecting-preparation-from-talend-data-preparation-standard-component-enterprise-in -->
# Dynamically selecting the preparation from Talend Data Preparation

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tDataprepRun and click the
   Component tab to define its basic settings.
2. In the URL field, type the URL of the Talend Data Preparation web application, between
   double quotes. Port 9999 is the default port for Talend Data Preparation.
3. In the Username and Password fields,
   enter your Talend Data Preparation
   connection information, between double quotes.

   If you are using Talend Data Preparation
   Cloud, you need to use your Talend Data Preparation
   Cloud login instead of your Talend Data Preparation
   email.

   If you are working with Talend Cloud Data Preparation
   and if:

   * SSO is enabled, enter an access
     token in the field.
   * SSO is not enabled, enter either
     an access token or your password in the field.
4. Select the Dynamic preparation selection check box to
   dynamically define the preparations with their paths in Talend Data Preparation rather than their technical
   ids.
5. In the Preparation path field, enter
   `"customers/"+((String)globalMap.get("tFileList_2_CURRENT_FILE"))+"_preparation"`.

   This expression is made of three distinct parts. In the path,
   customers is the folder in Talend Data Preparation where the preparations are
   kept. As for the preparations names, because they are partly reused from the
   local sub folders names, you will use this expression to retrieve those sub
   folders name from the tFileList\_1, and attach the
   `_preparation` suffix.
6. In the Preparation version field, type
   `Current state` between double quotes, in order to use the
   current version of the preparation.
7. Click Fetch Schema to
   retrieve the schema of the preparation.

   The output schema of the tDataprepRun component now
   reflects the changes made with each preparation step. The schema takes into
   account columns that were added or removed for example. By default, the output
   schema will use the String type for all the columns, in order
   not to overwrite any formatting operations performed on dates or numeric values
   during the preparation.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-outputting-result-of-preparation-into-database-standard-component-enterprise-in -->
# Outputting the result of the preparation into a database

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tRedshiftOutput and click the
   Component tab to define its basic settings.
2. In the Property Type list, select
   Built-in to set the database connection details
   manually.
3. In the Host, Port,
   Database, Schema,
   Username and Password fields, enter the
   Redshift connection details and the user authentication data for the database,
   between double quotes
4. To fill the Table field, with the expression that will
   dynamically reuse the input file name and give it to the table, drag it from the
   tFileList\_2 list of expressions in the
   Outline panel.
5. From the Action on table drop-down list, select
   Create table if does not exist.
6. From the Action on data drop-down list, select
   Insert.
7. Click Sync columns to retrieve the new output schema,
   inherited from the tDataprepRun component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tfilelist-tfileinputdelimited-tredshiftoutput-reading-input-files-from-your-local-folder-standard-component-enterprise-in -->
# Reading the input files from your local folder

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select
   tFileList\_1 and click the
   Component tab to define its basic settings.

   This first tFileList will read the
   customers\_files folder, and retrieve the path of the
   two sub folders so that they can be reused later.
2. In the Directory field, enter the path to the
   customers\_files folder, containing the customers datasets,
   in their respective sub folders.
3. Click the + button in the
   Filemask table to add a new line and rename it
   `*`, between double quotes.
4. In the design workspace, select tFileList\_2 and click
   the Component tab to define its basic settings.

   This second tFileList will read the four
   .csv datasets contained in the two sub folders and
   retrieve their file paths.
5. To fill the Directory field with the expression that
   will dynamically retrieve the input files paths, drag it from the
   tFileList\_1 list of expressions in the
   Outline panel.
6. Check the Includes subdirectories check box.
7. Click the + button in the
   Filemask table to add a new line and rename it
   `*.csv`, between double quotes.
8. In the design workspace, select the tFileInputDelimited and
   click the Component tab to define its basic
   settings.
9. To fill the File name/Stream field with the expression
   that will dynamically retrieve the input files paths, drag it from the
   tFileList\_2 list of expressions in the
   Outline panel.
10. Enter the Row Separator and Field
    Separator that correspond to your datasets, between double
    quotes.
11. Click the Edit schema button to define the columns of
    the source datasets and their data type.

    The schema is the same for all the datasets from the
    customers\_files folder. Make sure that this schema
    matches the schema expected by the tDataprepRun
    component. In other words, the input schema must be the same as the datasets
    upon which the preparations were made in the first place.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-accessing-preparation-from-talend-data-preparation-spark-batch-component-in -->
# Accessing the preparation from Talend Data Preparation

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tDataprepRun
   and click the Component tab to define its
   basic settings.
2. In the URL field, type
   the URL of the Talend Data Preparation or
   Talend Cloud Data Preparation web application,
   between double quotes. Port 9999 is the default
   port for Talend Data Preparation.
3. In the Username and
   Password fields, enter your Talend Data Preparation or Talend Cloud Data Preparation connection information,
   between double quotes.

   If you are working with Talend Cloud Data Preparation and if:
   * SSO is enabled, enter an access
     token in the field.
   * SSO is not enabled, enter either
     an access token or your password in the field.
4. Click Choose an existing
   preparation to display a list of the prepations available in
   Talend Data Preparation or Talend Cloud Data Preparation, and select datapreprun\_spark.

   This scenario assumes that a preparation with a compatible schema has been
   created beforehand.

   A warning is displayed next to preparations containing incompatible actions,
   that only affect a single row or cell.
5. Click Fetch Schema to retrieve the schema of
   the preparation.

   The output schema of the tDataprepRun component now
   reflects the changes made with each preparation step. The schema takes into
   account columns that were added or removed for example. By default, the output
   schema will use the String type for all the columns, in order
   not to overwrite any formatting operations performed on dates or numeric values
   during the preparation.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-loading-sample-data-spark-batch-component-in -->
# Loading the sample data

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select the
   tFixedFlowInput component and click the Component tab to define its basic settings.
2. Click the [...] button next to Edit schema to open the schema editor.
3. Click the [+] button to add the schema
   columns as shown in this image.

   This schema is the same as the dataset originally used to create the
   datapreprun\_spark preparation in
   Talend Data Preparation or Talend Cloud Data Preparation.
4. Click OK to validate these changes and accept
   the propagation prompted by the pop-up dialog box.
5. In the Mode area, select the Use Inline Content radio button and paste the
   above-mentioned sample data about customers into the Content field that is displayed.
6. In the Field separator
   field, enter a semicolon (;).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-accessing-preparation-from-talend-data-preparation-spark-stream-component-in -->
# Accessing the preparation from Talend Data Preparation

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tDataprepRun and click
   the Component tab to define its basic settings.
2. In the URL field, type the URL of the Talend Data Preparation or Talend Cloud Data Preparation web application, between
   double quotes. Port 9999 is the default port for Talend Data Preparation.
3. In the Username and
   Password fields, enter your Talend Data Preparation or Talend Cloud Data Preparation connection information,
   between double quotes.

   If you are working with Talend Cloud Data Preparation and if:
   * SSO is enabled, enter an access
     token in the field.
   * SSO is not enabled, enter either
     an access token or your password in the field.
4. Click Choose an existing
   preparation to display a list of the prepations available in
   Talend Data Preparation, and select
   datapreprun\_spark.

   This scenario assumes that a preparation with a compatible schema has been
   created beforehand.

   A warning is displayed next to preparations containing incompatible actions,
   that only affect a single row or cell.
5. Click Fetch Schema to retrieve the schema of
   the preparation.

   The output schema of the tDataprepRun component now
   reflects the changes made with each preparation step. The schema takes into
   account columns that were added or removed for example. By default, the output
   schema will use the String type for all the columns, in order
   not to overwrite any formatting operations performed on dates or numeric values
   during the preparation.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-thdfsconfiguration-tlogrow-ts3configuration-loading-sample-data-spark-stream-component-in -->
# Loading the sample data

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select the tFixedFlowInput
   component and click the Component tab to define its basic
   settings.
2. Click the [...] button next to Edit schema to open the schema editor.
3. Click the [+] button to add the schema
   columns as shown in this image.

   This schema is the same as the dataset originally used to create the
   datapreprun\_spark preparation in Talend Data Preparation or Talend Cloud Data Preparation.
4. Click OK to validate these changes and accept
   the propagation prompted by the pop-up dialog box.
5. In the Streaming area, enter your preferred value for
   the Input repetition interval (ms) field. In this
   example, the default value, `5000` is used.
6. In the Mode area, select the Use Inline Content radio button and paste the
   above-mentioned sample data about customers into the Content field that is displayed.
7. In the Field separator
   field, enter a semicolon (;).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-accessing-preparation-from-talend-data-preparation-standard-component-enterprise-in -->
# Accessing the preparation from Talend Data Preparation

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tDataprepRun
   and click the Component tab to define its
   basic settings.
2. In the URL field, type
   the URL of the Talend Data Preparation or
   Talend Cloud Data Preparation web application,
   between double quotes. Port 9999 is the default
   port for Talend Data Preparation.
3. In the Username and
   Password fields, enter your Talend Data Preparation or Talend Cloud Data Preparation connection information,
   between double quotes.

   If you are working with Talend Cloud Data Preparation and if:
   * SSO is enabled, enter an access
     token in the field.
   * SSO is not enabled, enter either
     an access token or your password in the field.
4. Click Choose an existing
   preparation to display a list of the preparations available in
   Talend Data Preparation or Talend Cloud Data Preparation, and select datapreprun\_scenario.

   This scenario assumes that a preparation with a compatible schema has been
   created beforehand.
5. Click Fetch Schema to
   retrieve the schema of the preparation,
   datapreprun\_preparation in this case.

   The output schema of the tDataprepRun component now
   reflects the changes made with each preparation step. The schema takes into
   account columns that were added or removed for example. By default, the output
   schema will use the String type for all the columns, in order
   not to overwrite any formatting operations performed on dates or numeric values
   during the preparation.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-outputting-preparation-into-excel-file-standard-component-enterprise-in -->
# Outputting the preparation into an Excel file

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tFileOutputExcel and click the Component tab to define its basic settings.
2. In the File Name field, enter the location
   where you want to save the result of the preparation.
3. Click Sync columns to
   retrieve the new output schema, inherited from the tDataprepRun
   component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/data-preparation/tdatapreprun-tmysqlinput-tfileoutputexcel-tfileoutputexcel-retrieving-data-from-database-standard-component-enterprise-in -->
# Retrieving the data from the database

Last updated: 9/30/2026

## Procedure

1. In the design workspace, select tMysqlInput
   and click the Component tab to define its
   basic settings.
2. In the Property Type list, select Built-in to set the database connection details
   manually.
3. In the DB Version list, select the version of
   MySQL you are using, MySQL 5 in this example.

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

   Make sure that the schema of the tMysqlInput component matches the schema expected by the
   tDataprepRun  component. In other
   words, the input schema must be the same as the dataset upon which the
   preparation was made in the first place.
