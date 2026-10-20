<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection · versión 8.0 -->
# tRedshiftConnection

Last updated: 9/30/2026

Opens a connection to the specified database that can then be reused in the
subsequent subJob or subJobs.

tRedshiftConnection opens a
connection to the database for a current transaction.

## tRedshiftConnection Standard properties

These properties are used to configure tRedshiftConnection running in the Standard Job framework.

The Standard
tRedshiftConnection component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository.   * Built-in: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The fields that follow are completed   automatically using the data retrieved. |
| Driver version | Select the Redshift driver version to be used: Driver v1 or Driver v2.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Host | Host name or IP address of DB server. |
| Port | Listening port number of DB server. |
| Database | Name of the database.  The bucket and the Redshift database to be used must be in the same region on Amazon. This could avoid the S3ServiceException errors known to Amazon. For further information about these errors, see [S3ServiceException Errors](https://docs.aws.amazon.com/redshift/latest/dg/s3serviceexception-error.html). |
| Schema | Name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use String JDBC parameters | Set JDBC properties in a string. If you select this option, enter your JDBC parameter string in the Additional JDBC Parameters field; otherwise, enter JDBC properties and property values in the Additional JDBC Parameters table.  This option is not available if Driver v1 is selected from the Driver version drop-down list.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Additional JDBC Parameters | Specify additional JDBC properties for the connection you are creating. The properties are separated by ampersand & and each property is a key-value pair. For example, *ssl=true & sslfactory=com.amazon.redshift.ssl.NonValidatingFactory*, which means the connection will be created using SSL.  This field is not available if Driver v2 is selected from the Driver version drop-down list and the Use String JDBC parameters option is not selected. |
| Additional JDBC Parameters (table) | Specify JDBC properties in table rows.  To specify a JDBC property, add a row in the table by clicking the plus button on the bottom of this table, enter the property name in the Key column, and then enter the property value in the Value column.  This table is available when Driver v2 is selected from the Driver version drop-down list and the Use String JDBC parameters option is not selected.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-04 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Log file | Specify the path to the log file to be generated during the data retrieval process.  Note that if the logging information needs to be saved and this component reuses the connection created by a tRedshiftConnection component, you must specify the property *loglevel=1/2/3* in the Additional JDBC Parameters field of the tRedshiftConnection component.  There is no limitation on the size of the log file. If the specified log file already exists, it will be overwritten. |
| Logging level | Select a logging level from the drop-down list to specify which kind of events will be logged in the log file. |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| JDBC url | Select a way to access to an Amazon Redshift database from the JDBC url drop-down list.  * Standard: Use the   standard way to access the Redshift database. * SSO: Use the IAM   Single Sign-ON (SSO) authentication way to access the Redshift Database. Before selecting   this option, ensure that the IAM role added to your Redshift cluster has appropriate   access rights and permissions to this cluster. You can ask the administrator of your AWS   services for more details. This option is available only when Use an existing connection check box is not selected from   the Basic settings. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tRedshift\* components, especially with the tRedshiftCommit and tRedshiftRollback components. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Handling data with Redshift](tredshiftconnection-tredshiftinput-tlogrow-handling-data-with-redshift-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-handling-data-with-redshift-standard-component-this -->
# Handling data with Redshift

Last updated: 9/30/2026

This scenario describes a Job that writes the personal information into Redshift, then
retrieves the information in Redshift and displays it on the console.

The scenario requires the following six components:

* tRedshiftConnection: opens a connection to
  Redshift.
* tFixedFlowInput: defines the personal
  information data structure, and sends the data to the next component.
* tRedshiftOutput: writes the data it receives
  from the preceding component into Redshift.
* tRedshiftInput: reads the data from
  Redshift.
* tLogRow: displays the data it receives from
  the preceding component on the console.
* tRedshiftClose: closes the connection to
  Redshift.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-dropping-and-linking-components-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tRedshiftInput](tredshiftinput "Reads data from a database and extracts fields based on a query so that you may apply changes to the extracted data.")
* [tRedshiftOutput](tredshiftoutput "Writes, updates, modifies or deletes the data in a database.")

**Related reference**  

* [tRedshiftConnection](tredshiftconnection "Opens a connection to the specified database that can then be reused in the subsequent subJob or subJobs.")
* [tRedshiftClose](tredshiftclose "Closes the transaction committed in the connected DB.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Opening a connection to Redshift](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-opening-connection-to-redshift-standard-component)
* [Defining the input data](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-defining-input-data-standard-component)
* [Writing the data into Redshift](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-writing-data-into-redshift-standard-component)
* [Retrieving the data from Redshift](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-retrieving-data-from-redshift-standard-component)
* [Displaying the defined information](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-displaying-defined-information-standard-component)
* [Closing the connection to Redshift](/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-closing-connection-to-redshift-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-dropping-and-linking-components-standard-component-drop -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Drop the six components listed previously from the Palette onto the design workspace.
2. Connect tFixedFlowInput to tRedshiftOutput using a Row > Main
   connection.
3. Connect tRedshiftInput to tLogRow also using a Row > Main
   connection.
4. Connect tRedshiftConnection to tFixedFlowInput using a Trigger > OnSubjobOk
   connection.
5. Connect tFixedFlowInput to tRedshiftInput and tRedshiftInput to tRedshiftClose also using a Trigger > OnSubjobOk
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to execute the Job.

   The personal information is written to the specified target Redshift
   database, and then the data is retrieved from the database and displayed on
   the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-closing-connection-to-redshift-standard-component -->
# Closing the connection to Redshift

Last updated: 9/30/2026

## Procedure

1. Double-click tRedshiftClose to open its
   Basic settings view.
2. From Component List, select the
   connection you have already configured for tRedshiftConnection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-defining-input-data-standard-component -->
# Defining the input data

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit schema to open the schema editor.
3. In the schema editor, click the [+]
   button to add three columns: *id* of the
   interger type, *name* of the string type,
   and *age* of the integer type.
4. Click OK to validate the changes and
   accept the propagation prompted by the pop-up [Propagate] dialog box.
5. In the Mode area, select Use Inline Content (delimited file) and enter the
   following personal information in the Content field.

   ```
   1;Arthur;16
   2;Ford;18
   3;Jackson;17
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-displaying-defined-information-standard-component -->
# Displaying the defined information

Last updated: 9/30/2026

## Procedure

1. Double-click tLogRow to open its
   Basic settings view.
2. In the Mode area, select Table (print values in cells of a table) for a
   better view of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-opening-connection-to-redshift-standard-component -->
# Opening a connection to Redshift

Last updated: 9/30/2026

## Procedure

1. Double-click tRedshiftConnection to open
   its Basic settings view.
2. Select Built-In from the Property Type drop-down list.

   In the Host, Port, Database, Schema, Username, and Password fields,
   enter the information required for the connection to Redshift.
3. In Advanced settings view, select
   Auto Commit check box to commit any
   changes to Redshift upon each transaction.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-retrieving-data-from-redshift-standard-component -->
# Retrieving the data from Redshift

Last updated: 9/30/2026

## Procedure

1. Double-click tRedshiftInput to open its
   Basic settings view.
2. Select the Use an existing connection
   check box, and then select the connection you have already configured for
   tRedshiftConnection from the Component List drop-down list.
3. Click the [...] button next to Edit schema to open the schema editor.
4. In the schema editor, click the [+]
   button to add three columns: *id* of the
   interger type, *name* of the string type,
   and *age* of the integer type. The data
   structure is same as the structure you have defined for tFixedFlowInput.
5. Click OK to validate the changes and
   accept the propagation prompted by the pop-up [Propagate] dialog box.
6. In the Table Name field, enter or browse
   to the table into which you write the data, *redshiftexample* in this scenario.
7. Click the Guess Query button to generate
   the query. The Query field will be filled
   with the automatically generated query.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-redshift/tredshiftconnection-tredshiftinput-tlogrow-writing-data-into-redshift-standard-component -->
# Writing the data into Redshift

Last updated: 9/30/2026

## Procedure

1. Double-click tRedshiftOutput to open its
   Basic settings view.
2. Select the Use an existing connection
   check box, and then select the connection you have already configured for
   tRedshiftConnection from the Component List drop-down list.
3. In the Table field, enter or browse to
   the table into which you want to write the data, *redshiftexample* in this scenario.
4. Select Drop table if exists and create
   from the Action on table drop-down list,
   and select Insert from the Action on data drop-down list.
5. Click Sync columns to retrieve the schema
   from the preceding component tFixedFlowInput.
