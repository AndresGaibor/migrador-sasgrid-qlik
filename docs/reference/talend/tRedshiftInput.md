<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput · versión 8.0 -->
# tRedshiftInput

Last updated: 9/30/2026

Reads data from a database and extracts fields based on a query so that you may
apply changes to the extracted data.

tRedshiftInput executes a DB query
with a strictly defined order which must correspond to the schema
definition. Then it passes on the field list to the next component
through a Main row link.

### In this section

* [tRedshiftInput Standard properties](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-standard-properties)
* [tRedshiftInput properties for Apache Spark Batch](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-properties-for-apache-spark-batch)

**Related concepts**  

* [Handling data with Redshift](tredshiftconnection-tredshiftinput-tlogrow-handling-data-with-redshift-standard-component-this)
* [Loading/unloading data to/from Amazon S3](tredshiftinput-tredshiftbulkexec-ts3get-loading-unloading-data-to-from-amazon-s3-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-properties-for-apache-spark-batch -->
# tRedshiftInput properties for Apache Spark Batch

Last updated: 9/30/2026

These properties are used to configure tRedshiftInput running in the Spark Batch Job framework.

The Spark Batch
tRedshiftInput component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend products
with Big Data and Talend Data Fabric.

This component is not supported with Spark 4.0.x.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  Built-In: No property data stored centrally.  Repository: Select the repository file where the properties are stored. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Driver version | Select the Redshift driver version to be used between Driver v1 or Driver v2.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-06 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Host | Enter the endpoint of the database you need to connect to in Redshift. |
| Port | Enter the port number of the database you need to connect to in Redshift.  The related information can be found in the Cluster Database Properties area in the Web console of your Redshift.  For further information, see [Managing clusters console](http://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html). |
| Username and Password | Enter the authentication information to the Redshift database you need to connect to.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Database | Enter the name of the database you need to connect to in Redshift.  The related information can be found in the Cluster Database Properties area in the Web console of your Redshift.  For further information, see [Managing clusters console](http://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html). |
| Schema | Enter the name of the database schema to be used in Redshift. The default schema is called *PUBLIC*.  A schema in terms of Redshift is similar to a operating system directory. For further information about a Redshift schema, see [Schemas](http://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables.html). |
| Use String JDBC parameters | Set JDBC properties in a string. If you select this option, enter your JDBC parameter string in the Additional JDBC Parameters field; otherwise, enter JDBC properties and property values in the Additional JDBC Parameters table.  This option is only available when you select Driver v2 from the Driver version drop-down list. |
| Additional JDBC Parameters (field) | Specify additional JDBC properties for the connection you are creating. The properties are separated by ampersand & and each property is a key-value pair. For example, *ssl=true & sslfactory=com.amazon.redshift.ssl.NonValidatingFactory*, which means the connection will be created using SSL.  This option is only available when you select Driver v1 from the Driver version drop-down list or when you select Driver v2 from the Driver version drop-down list with Use String JDBC parameters selected. |
| Additional JDBC Parameters (table) | Specify JDBC properties in table rows.  To specify a JDBC property, add a row in the table by clicking the plus button on the bottom of this table, enter the property name in the Key column, and then enter the property value in the Value column.  This table is available when you select Driver v2 from the Driver version drop-down list and clear Use String JDBC parameters option.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-03 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| S3 configuration | Select the tS3Configuration component from which you want Spark to use the configuration details to connect to S3.  You need drop the tS3Configuration component to be used alongside tRedshiftConfiguration in the same Job so that this tS3Configuration is displayed on the S3 configuration list. |
| S3 temp path | Enter the location in S3 in which the data to be transferred from or to Redshift is temporarily stored.  This path is independent of the temporary path you need to set in the Basic settings tab of tS3Configuration. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table name | Enter the name of the table from which the data will be read.  This field is only available when you select Table from the Read from drop-down list. |
| Read from | Select the type of the source of the data to be read.  * Table: tRedshiftInput reads the data of the table you   specify in the Table name   field. * Query: tRedshiftInput reads the result of the query you   write in the Query   field. |
| Query Type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.  You can use pushdown predicate in the query to filter the data from the database. Spark supports the following operators:  * `Filter` * `Limit`  These fields are only available when you select Query from the Read from drop-down list. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Trim all the String/Char columns | Select this check box to remove leading whitespace and trailing whitespace from all String/Char columns. |
| Trim column | This table is filled automatically with the schema being used. Select the check box(es) corresponding to the column(s) to be trimmed. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component and requires an output link.  This component should use a tRedshiftConfiguration component present in the same Job to connect to Redshift. You need to drop a tRedshiftConfiguration component alongside this component and configure the Basic settings of this component to use tRedshiftConfiguration.  This component, along with the Spark Batch component Palette it belongs to, appears only when you are creating a Spark Batch Job.  Note that in this documentation, unless otherwise explicitly stated, a scenario presents only Standard Jobs, that is to say traditional  Talend  data integration Jobs. |
| Spark Connection | In the Spark Configuration tab in the Run view, define the connection to a given Spark cluster for the whole Job. In addition, since the Job expects its dependent jar files for execution, you must specify the directory in the file system to which these jar files are transferred so that Spark can access these files:  * Yarn mode (Yarn client or Yarn cluster):   + When using Google Dataproc, specify a bucket in the     Google Storage staging bucket     field in the Spark configuration     tab.   + When using HDInsight, specify the blob to be used for Job     deployment in the Windows Azure Storage     configuration area in the Spark     configuration tab.   + When using Altus, specify the S3 bucket or the Azure     Data Lake Storage for Job deployment in the Spark     configuration tab.   + When using on-premises distributions, use     the configuration component corresponding to the file system     your cluster is using. Typically, this system is HDFS and so     use [tHDFSConfiguration](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration). * Standalone mode: use the   configuration component corresponding to the file system your cluster is   using, such as [tHDFSConfiguration Apache Spark Batch](/talend/r/en-US/8.0/components/hdfs/thdfsconfiguration-properties-for-apache-spark-batch) or [tS3Configuration Apache Spark Batch](/talend/r/en-US/8.0/components/amazon-s3/ts3configuration-properties-for-apache-spark-batch).  If you are using Databricks without any configuration component present   in your Job, your business data is written directly in DBFS (Databricks   Filesystem).  This connection is effective on a per-Job basis. |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-standard-properties -->
# tRedshiftInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tRedshiftInput running in the Standard Job framework.

The Standard
tRedshiftInput component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .   * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Driver version | Select the Redshift driver version to be used: Driver v1 or Driver v2.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Hostname or IP address of the database server. |
| Port | Listening port number of the database server. |
| Database | Name of the database. |
| Schema | Exact name of the schema. |
| Username and Password | Database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use String JDBC parameters | Set JDBC properties in a string. If you select this option, enter your JDBC parameter string in the Additional JDBC Parameters field; otherwise, enter JDBC properties and property values in the Additional JDBC Parameters table.  This option is not available if Driver v1 is selected from the Driver version drop-down list.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Additional JDBC Parameters | Specify additional JDBC properties for the connection you are creating. The properties are separated by ampersand & and each property is a key-value pair. For example, *ssl=true & sslfactory=com.amazon.redshift.ssl.NonValidatingFactory*, which means the connection will be created using SSL.  This field is not available if Driver v2 is selected from the Driver version drop-down list and the Use String JDBC parameters option is not selected. |
| Additional JDBC Parameters (table) | Specify JDBC properties in table rows.  To specify a JDBC property, add a row in the table by clicking the plus button on the bottom of this table, enter the property name in the Key column, and then enter the property value in the Value column.  This table is available when Driver v2 is selected from the Driver version drop-down list and the Use String JDBC parameters option is not selected.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Table Name | Name of the table from which the data will be read. |
| Query Type and Query | Enter your database query paying particularly attention to sequence the fields properly in order to match the schema definition.  If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Guess schema | Click the Guess schema button to retrieve the table schema. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Log file | Specify the path to the log file to be generated during the data retrieval process.  Note that if the logging information needs to be saved and this component reuses the connection created by a tRedshiftConnection component, you must specify the property *loglevel=1/2/3* in the Additional JDBC Parameters field of the tRedshiftConnection component.  There is no limitation on the size of the log file. If the specified log file already exists, it will be overwritten. |
| Logging level | Select a logging level from the drop-down list to specify which kind of events will be logged in the log file. |
| Use cursor | Select this check box to help to decide the row set to work with at a time and thus optimize performance. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| JDBC url | Select a way to access to an Amazon Redshift database from the JDBC url drop-down list.  * Standard: Use the   standard way to access the Redshift database. * SSO: Use the IAM   Single Sign-ON (SSO) authentication way to access the Redshift Database. Before selecting   this option, ensure that the IAM role added to your Redshift cluster has appropriate   access rights and permissions to this cluster. You can ask the administrator of your AWS   services for more details. This option is available only when Use an existing connection check box is not selected from   the Basic settings. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for Amazon Redshift databases. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-loading-unloading-data-to-from-amazon-s3-standard-component-this -->
# Loading/unloading data to/from Amazon S3

Last updated: 9/30/2026

This scenario describes a Job that generates a delimited file and uploads the file to S3,
loads data from the file on S3 to Redshift and displays the data on the console, then
unloads the data from Redshift to files on S3 per slice of the Redshift cluster, and
finally lists and gets the unloaded files on S3.

Prerequisites:

The following context variables have been created and saved in the Repository tree view. For more information about context
variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).

* *redshift\_host*: the connection endpoint URL of the
  Redshift cluster.
* *redshift\_port*: the listening port number of the
  database server.
* *redshift\_database*: the name of the database.
* *redshift\_username*: the username for the database
  authentication.
* *redshift\_password*: the password for the database
  authentication.
* *redshift\_schema*: the name of the schema.
* *s3\_accesskey*: the access key for accessing Amazon
  S3.
* *s3\_secretkey*: the secret key for accessing Amazon
  S3.
* *s3\_bucket*: the name of the Amazon S3 bucket.

Note that all context values in the above screenshot are for demonstration purposes
only.

### In this section

* [Adding and linking components](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tRedshiftInput](tredshiftinput "Reads data from a database and extracts fields based on a query so that you may apply changes to the extracted data.")

**Related reference**  

* [tRedshiftBulkExec](tredshiftbulkexec "Loads data into Amazon Redshift from Amazon S3, Amazon EMR cluster, Amazon DynamoDB, or remote hosts.")
* [tRedshiftUnload](tredshiftunload "Unloads data on Amazon Redshift to files on Amazon S3.")
* [tRedshiftOutputBulk](tredshiftoutputbulk "Prepares a delimited/CSV file that can be used by tRedshiftBulkExec to feed Amazon Redshift.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tS3List](/talend/en-US/components/8.0/amazon-s3/ts3list)
* [tS3Get](/talend/en-US/components/8.0/amazon-s3/ts3get)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-adding-and-linking-components-standard-component-create -->
# Adding and linking components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and apply all context variables listed above to the new
   Job.
2. Add the following components by typing their names in the design workspace or dropping
   them from the Palette: a tRowGenerator component, a tRedshiftOutputBulk component, a tRedshiftBulkExec component, a tRedshiftInput component, a tLogRow component, a tRedshiftUnload component, a tS3List component, and a tS3Get component.
3. Link tRowGenerator to tRedshiftOutputBulk using a Row > Main
   connection.
4. Do the same to link tRedshiftInput to
   tLogRow.
5. Link tS3List to tS3Get using a Row >
   Iterate connection.
6. Link tRowGenerator to tRedshiftBulkExec using a Trigger > On Subjob Ok
   connection.
7. Do the same to link tRedshiftBulkExec to
   tRedshiftInput, link tRedshiftInput to tRedshiftUnload, link tRedshiftUnload to tS3List.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Preparing a file and uploading the file to S3](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-preparing-file-and-uploading-file-to-s3-standard-component)
* [Loading data from the file on S3 to Redshift](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-loading-data-from-file-on-s3-to-redshift-standard-component)
* [Retrieving data from the table on Redshift](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-retrieving-data-from-table-on-redshift-standard-component)
* [Unloading data from Redshift to file(s) on S3](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-unloading-data-from-redshift-to-file-s-on-s3-standard-component)
* [Retrieving files unloaded to Amazon S3](/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-retrieving-files-unloaded-to-amazon-s3-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Execute the Job by pressing F6 or
   clicking Run on the Run tab.

   As shown above, the generated data is written into the local file *redshift\_bulk.txt*, the file is uploaded on S3 with the new
   name *person\_load*, and then the data is
   loaded from the file on S3 to the table *person* in Redshift and displayed on the console. After that,
   the data is unloaded from the table *person* in Redshift to two files *person\_unload\_0000\_part\_00* and *person\_unload\_0001\_part\_00* on S3 per slice of the Redshift
   cluster, and finally the unloaded files on S3 are listed and retrieved in
   the local folder.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-loading-data-from-file-on-s3-to-redshift-standard-component -->
# Loading data from the file on S3 to Redshift

Last updated: 9/30/2026

## Procedure

1. Double-click tRedshiftBulkExec to open its Basic settings view on the Component tab.
2. In the Host field, press Ctrl + Space and from the list select *context.redshift\_host* to fill in this
   field.

   Do the same to fill:

   * the Port field with *context.redshift\_port*,
   * the Database field with *context.redshift\_database*,
   * the Schema field with *context.redshift\_schema*,
   * the Username field with *context.redshift\_username*,
   * the Password field with *context.redshift\_password*,
   * the Access Key field with
     *context.s3\_accesskey*,
   * the Secret Key field with *context.s3\_secretkey*, and
   * the Bucket field with *context.s3\_bucket*.
3. In the Table Name field, enter the name
   of the table to be written. In this example, it is *person*.
4. From the Action on table list, select
   Drop table if exists and create.
5. In the Key field, enter the name of the file on Amazon
   S3 to be loaded. In this example, it is *person\_load*.
6. Click the [...] button next to Edit schema and in the pop-up window define the schema by
   adding two columns: *ID* of Integer type
   and *Name* of String type.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-preparing-file-and-uploading-file-to-s3-standard-component -->
# Preparing a file and uploading the file to S3

Last updated: 9/30/2026

## Procedure

1. Double-click tRowGenerator to open its
   RowGenerator Editor.
2. Click the [+] button to add two columns: *ID* of Integer type and *Name* of String type.
3. Click the cell in the Functions column and select a
   function from the list for each column. In this example, select Numeric.sequence to generate sequence numbers for
   the *ID* column and select TalendDataGenerator.getFirstName to generate
   random first names for the *Name*
   column.
4. In the Number of Rows for RowGenerator field, enter the
   number of data rows to generate. In this example, it is *20*.
5. Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
6. Double-click tRedshiftOutputBulk to open its Basic settings view on the Component tab.
7. In the Data file path at local field,
   specify the local path for the file to be generated. In this example, it is
   *E:/Redshift/redshift\_bulk.txt*.
8. In the Access Key field, press Ctrl + Space and from the list select *context.s3\_accesskey* to fill in this
   field.

   Do the same to fill the Secret Key field
   with *context.s3\_accesskey* and the
   Bucket field with *context.s3\_bucket*.
9. In the Key field, enter a new name for the file to be
   generated after being uploaded on Amazon S3. In this example, it is
   *person\_load*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-retrieving-data-from-table-on-redshift-standard-component -->
# Retrieving data from the table on Redshift

Last updated: 9/30/2026

## Procedure

1. Double-click tRedshiftInput to open its
   Basic settings view on the Component tab.
2. Fill the Host, Port, Database, Schema, Username, and Password fields
   with their corresponding context variables.
3. In the Table Name field, enter the name
   of the table to be read. In this example, it is *person*.
4. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding two columns: *ID* of
   Integer type and *Name* of String
   type.
5. In the Query field, enter the following
   SQL statement based on which the data are retrieved.

   ```
   "SELECT * FROM" + context.redshift_schema + "person ORDER BY \"ID\""
   ```
6. Double-click tLogRow to open its
   Basic settings view on the Component tab.
7. In the Mode area, select Table (print values in cells of a table) for a
   better display of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-retrieving-files-unloaded-to-amazon-s3-standard-component -->
# Retrieving files unloaded to Amazon S3

Last updated: 9/30/2026

## Procedure

1. Double-click tS3List to open its
   Basic settings view on the Component tab.
2. Fill the Access Key and Secret
   Key fields with their corresponding context variables.
3. From the Region list, select the AWS
   region where the unload files are created. In this example, it is *US Standard*.
4. Clear the List all buckets objects check
   box, and click the [+] button under the
   table displayed to add one row.

   Fill in the Bucket name column with the name of the
   bucket in which the unload files are created. In this example, it is the
   context variable *context.s3\_bucket*.

   Fill in the Key prefix column with the name prefix for
   the unload files. In this example, it is *person\_unload\_*.
5. Double-click tS3Get to open its Basic settings view on the Component tab.
6. Fill the Access Key field and Secret Key field with their corresponding context
   variables.
7. From the Region list, select the AWS
   region where the unload files are created. In this example, it is *US Standard*.
8. In the Bucket field, enter the name of
   the bucket in which the unload files are created. In this example, it is the
   context variable *context.s3\_bucket*.

   In the Key field, enter the name of the
   unload files by pressing Ctrl + Space and
   from the list selecting the global variable *((String)globalMap.get("tS3List\_1\_CURRENT\_KEY"))*.
9. In the File field, enter the local path
   where the unload files are saved. In this example, it is *"E:/Redshift/" +
   ((String)globalMap.get("tS3List\_1\_CURRENT\_KEY"))*.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftinput-tredshiftbulkexec-ts3get-unloading-data-from-redshift-to-file-s-on-s3-standard-component -->
# Unloading data from Redshift to file(s) on S3

Last updated: 9/30/2026

## Procedure

1. Double-click tRedshiftUnload to open its
   Basic settings view on the Component tab.
2. Fill the Host, Port, Database, Schema, Username, and Password fields
   with their corresponding context variables.

   Fill the Access Key, Secret Key, and Bucket fields also with their corresponding context
   variables.
3. In the Table Name field, enter the name
   of the table from which the data will be read. In this example, it is
   *person*.
4. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding two columns: *ID* of
   Integer type and *Name* of String
   type.
5. In the Query field, enter the following
   SQL statement based on which the result will be unloaded.

   ```
   "SELECT * FROM person"
   ```
6. In the Key prefix field, enter the name
   prefix for the unload files. In this example, it is *person\_unload\_*.
