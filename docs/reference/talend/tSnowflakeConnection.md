<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconnection · versión 8.0 -->
# tSnowflakeConnection

Last updated: 9/30/2026

Opens a connection to Snowflake that can then be reused by other Snowflake
components.

Information noteNote:

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSnowflakeConnection Standard properties

These properties are used to configure tSnowflakeConnection running in the Standard Job framework.

The Standard
tSnowflakeConnection component belongs to the Cloud family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Account | In the Account field, enter, in double quotation marks, the account name that has been assigned to you by Snowflake. |
| Authentication Type | Set the authentication type.   * Basic: Select this option if key pair   authentication is not enabled. * Key Pair: Select this option if key pair   authentication is enabled.  See [Using Key Pair Authentication](https://docs.snowflake.net/manuals/user-guide/jdbc-configure.html#using-key-pair-authentication) for related   information. * OAuth 2.0: Select this option to use external   OAuth for data accessing.  See [External OAuth Overview](https://docs.snowflake.com/en/user-guide/oauth-ext-overview.html) for related   information.   Information noteNote: Before selecting the Key Pair option, make sure you have set the key pair authentication data in the Basic settings view of the tSetKeystore component as follows.  1. Leave the TrustStore type field unchanged. 2. Set TrustStore file to    `""`. 3. Clear the TrustStore password field. 4. Select Need Client authentication. 5. Enter the path to the key store file in double quotation marks in the    KeyStore file field (or click the    […] button to the right of the    KeyStore file field and navigate to the key    store file). 6. Enter the key store file password in the KeyStore    password field. 7. Clear the Check server identity option. |
| OAuth token endpoint | Enter OAuth 2.0 token endpoint. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Client ID | Enter the client ID of your application. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Client Secret | Enter the client secret of your application. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| Grant type | Set the grant type for retrieving the access token. Two options are provided: Client Credentials and Password. Click [Client Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.4) and [Resource Owner Password Credentials](https://tools.ietf.org/html/rfc6749#section-1.3.3) for related information.  This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| OAuth username | Enter the OAuth username. This option is available when Password is selected from the Grant type dropdown list. |
| OAuth password | Enter the OAuth password. To enter the password, click the [...] button next to the password field, enter the password between double quotes in the pop-up dialog box, and then click OK to save the settings.  This option is available when Password is selected from the Grant type dropdown list.  Information noteNote: OAuth password does not support spaces. |
| Scope | Enter the scope. See [Scopes](https://docs.snowflake.com/en/user-guide/oauth-ext-overview.html#scopes) for related information. This option is available when OAuth 2.0 is selected from the Authentication Type dropdown list. |
| User Id | Enter your login name in double quotation marks. |
| Password | Click the [...] button next to the Password field, enter the password in double quotation marks in the pop-up dialog box, and click OK. This field is available if Basic is selected from the Authentication Type dropdown list. |
| Key Alias | Enter the key pair alias in double quotation marks. This field is available if Key Pair is selected from the Authentication Type dropdown list. |
| Warehouse | Enter, in double quotation marks, the name of the Snowflake warehouse to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Schema | Enter, within double quotation marks, the name of the database schema to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Database | Enter, in double quotation marks, the name of the Snowflake database to be used. This name is case-sensitive and is normally upper case in Snowflake. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail.  This checkbox is not available when the Specify a data source alias checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Auto Commit | Select this option to automatically commit the changes made to the current database when the connection to the database is terminated. This option is selected by default.  Information noteNote: This option has no effect on the tSnowflakeOutput and tSnowflakeRow components. |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| Login Timeout | Specify the timeout period (in minutes) of Snowflake login attempts. An error will be generated if no response is received in this period. |
| Role | Enter, in double quotation marks, the default access control role to use to initiate the Snowflake session.  This role must already exist and has been granted to the user ID you are using to connect to Snowflake. If this field is left empty, the PUBLIC role is automatically granted. For information about Snowflake access control model, see [Understanding the Access Control Model](https://docs.snowflake.net/manuals/user-guide/security-access-control.html). |
| URL suffix | Enter, in double quotation marks, the Snowflake custom domain URL of your choice. For more information about Snowflake URL formats, see [Standard account URLs](https://docs.snowflake.com/en/user-guide/organizations-connect#standard-account-urls). For Snowflake components other than tSnowflakeConnection, this field is available when you select Use This Component from the Connection Component drop-down list in the Basic settings view. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other Snowflake components. It creates a Snowflake connection and works with other subJobs that reuse this connection using a Trigger link. |
| Tracing Snowflake JDBC logs | If you wish to merge the Snowflake JDBC driver logs with the logs of the current Job, add this JVM argument, -Dnet.snowflake.jdbc.loggerImpl=net.snowflake.client.log.JDK14Logger, in the Run > Advanced settings tab of the Job you are running. |

**Related concepts**  

* [Aggregating Snowflake data using ELT components](teltinput-teltmap-tsnowflakeinput-tlogrow-aggregating-snowflake-data-using-context-variables-as-table-and-connection-names "This scenario shows you an example of aggregating Snowflake data from two source tables STUDENT and TEACHER to one target table FULLINFO using the ELT components.")
* [Writing data into and reading data from a Snowflake table](tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-writing-data-into-and-reading-data-from-snowflake-table-standard-component "Here is an example of using Talend Snowflake components to connect to Snowflake, create a Snowflake table, write data into the table, then read data from this table, finally close the connection to Snowflake.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-writing-data-into-and-reading-data-from-snowflake-table-standard-component -->
# Writing data into and reading data from a Snowflake table

Last updated: 9/30/2026

Here is an example of using Talend
Snowflake components to connect to Snowflake, create a Snowflake table, write data into the
table, then read data from this table, finally close the connection to
Snowflake.

### In this section

* [Creating a Job for writing and reading Snowflake data](/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-creating-job-for-writing-and-reading-snowflake-data-standard-component-the)
* [Connecting to Snowflake](/talend/en-US/components/8.0/snowflake/teltinput-teltmap-tsnowflakeinput-tlogrow-connecting-to-snowflake-standard-component?id=4670)
* [Creating a Snowflake table](/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-creating-snowflake-table)
* [Writing data into Snowflake](/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-writing-data-into-snowflake-standard-component)
* [Reading data from Snowflake](/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-reading-data-from-snowflake-standard-component)
* [Closing the Snowflake connection](/talend/en-US/components/8.0/snowflake/teltinput-teltmap-tsnowflakeinput-tlogrow-closing-snowflake-connection?id=4674)
* [Executing the Job to write and read data in Snowflake](/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-executing-job-to-write-and-read-data-in-snowflake-standard-component-press)

**Related concepts**  

* [tSnowflakeInput](tsnowflakeinput "Reads data from a Snowflake table into the data flow of your Job based on an SQL query.")
* [tSnowflakeOutput](tsnowflakeoutput "Uses the data incoming from its preceding component to insert, update, upsert or delete data in a Snowflake table.")

**Related reference**  

* [tSnowflakeConnection](tsnowflakeconnection "Opens a connection to Snowflake that can then be reused by other Snowflake components.")
* [tSnowflakeClose](tsnowflakeclose "Closes an active Snowflake connection to release the occupied resources.")
* [tSnowflakeRow](tsnowflakerow "Executes the SQL command stated onto a specified Snowflake database.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tSalesforceConnection](/talend/en-US/components/8.0/salesforce/tsalesforceconnection)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-creating-job-for-writing-and-reading-snowflake-data-standard-component-the -->
# Creating a Job for writing and reading Snowflake data

Last updated: 9/30/2026

Create a Job to connect to Snowflake, create a Snowflake table, write data into
the table and then read data from the table, finally close the connection to
Snowflake.

## Before you begin

* The Snowflake data warehouse to be used is started but not in the Suspended
  status.
* The Snowflake role assigned to you has read and write permissions to the
  database to be connected.

If you are not sure about these requirements, ask the administrator of your Snowflake
system.

## Procedure

1. In the Integration perspective of Talend Studio,
   create a new Job from the Job Designs node in
   the Repository tree view.
2. Add a tSnowflakeConnection component, a
   tSnowflakeRow component, a
   tFixedFlowInput component, a
   tSnowflakeOutput component, a
   tSnowflakeInput component, a
   tLogRow component, and a
   tSnowflakeClose component to the Job.
3. Connect the tFixedFlowInput component to the tSnowflakeOutput component using a Row > Main connection.
4. Do the same to connect the tSnowflakeInput component to
   the tLogRow component.
5. Connect the tSnowflakeConnection component to the tSnowflakeRow component using a Trigger >  On Subjob Ok connection.
6. Do the same to connect the tSnowflakeRow
   component to the tFixedFlowInput
   component, the tFixedFlowInput component to the
   tSnowflakeInput component, and the
   tSnowflakeInput component to the
   tSnowflakeClose component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-creating-snowflake-table -->
# Creating a Snowflake table

Last updated: 9/30/2026

Configure the tSnowflakeRow component to create a new
table.

## Procedure

1. Double-click the tSnowflakeRow component to open its
   Basic settings view on the
   Component tab.
2. From the Connection Component drop-down list, select the
   tSnowflakeConnection component to reuse the
   connection created by it. In this example, it is
   `tSnowflakeConnection_1`.
3. In the Query field, enter the SQL statement used to
   create a new table into which the data will be written.

   In this example, the following SQL statement is used to create or replace a
   table `EMPLOYEE` with four columns,
   `ID` of INT type, `NAME` of
   VARCHAR type, `ONBOARD` of DATE type, and
   `SALARY` of VARIANT type.

   ```
   "CREATE OR REPLACE TABLE EMPLOYEE (" +
   "ID INT NOT NULL primary key," +
   "NAME VARCHAR (50), " +
   "ONBOARD DATE," +
   "SALARY VARIANT" +
   ") COMMENT = 'Created By Doc Team'"
   ```


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-executing-job-to-write-and-read-data-in-snowflake-standard-component-press -->
# Executing the Job to write and read data in Snowflake

Last updated: 9/30/2026

After setting up the Job and configuring the components used in the Job for writing
and reading Snowflake data, you can then execute the Job and verify the Job execution
result.

## Procedure

1. Press Ctrl + S to save the
   Job.
2. Press F6 to run the Job.

   As shown below, the data is written into the table `EMPLOYEE`
   in Snowflake, then read from this table and outputted on the console in the
   Run view of Talend Studio.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-reading-data-from-snowflake-standard-component -->
# Reading data from Snowflake

Last updated: 9/30/2026

Configure the tSnowflakeInput component and the
tLogRow component to retrieve data from Snowflake and output
the data on the console.

## Procedure

1. Double-click the tSnowflakeInput component to open its Basic settings view.
2. From the Connection
   Component drop-down list, select the tSalesforceConnection component to reuse the connection created
   by it.
3. Click the [...] button next to the
   Table field and in the pop-up dialog box, select the
   Use custom object check box and enter the name of the
   table from which the data will be retrieved in the Object
   Name field. In this example, it is
   `EMPLOYEE`, the table created by the
   tSnowflakeRow component. When done, click
   OK to close the dialog box.
4. Click the [...] button
   next to Edit schema and in the pop-up
   schema dialog box, define the schema by adding four columns,
   `ID` of int type, `NAME` and
   `SALARY` of String type, and
   `ONBOARD` of Date type. This schema is the same as the
   schema of the tSnowflakeOutput component.
5. Click OK to validate
   these changes and accept the propagation prompted by the pop-up dialog
   box.
6. Double-click the tLogRow
   component to open its Component
   view.
7. In the Mode area, select
   Vertical (each row is a key/value
   list) for better readability of the results.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/snowflake/tsnowflakeconnection-tsnowflakerow-tsalesforceconnection-writing-data-into-snowflake-standard-component -->
# Writing data into Snowflake

Last updated: 9/30/2026

Configure the tFixedFlowInput component and the
tSnowflakeOutput component to write data into
Snowflake.

## Procedure

1. Double-click the tFixedFlowInput component to open its Basic settings view.
2. Click the [...] button next
   to Edit schema and in the pop-up schema dialog
   box, define the schema by adding four columns, `ID` of int type,
   `NAME` and `SALARY` of String type, and
   `ONBOARD` of Date type.
3. Click OK to validate these
   changes and accept the propagation prompted by the pop-up dialog box.
4. In the Number of rows field, enter the number of records to
   be generated, `5` in this example.
5. In the Mode area, select
   Use Single Table and specify the value for each
   column.

   * `ID`: the automatically incremented number generated by
     the routine `Numeric.sequence("id",1,1)`.
   * `NAME`: the random first name generated by the routine
     `TalendDataGenerator.getFirstName()`.
   * `ONBOARD`: the random date generated by the routine
     `TalendDate.getRandomDate("2007-09-01","2017-09-01")`.
   * `SALARY`: the semi-structured JSON data with the format
     `{"Salary": value}`, where the salary value is
     generated by the routine
     `Numeric.random(100000,200000)`.
6. Double-click the tSnowflakeOutput component to open its Basic settings view.
7. From the Connection
   Component drop-down list, select the tSnowflakeConnection component to reuse the connection created by
   it.
8. Click the [...] button next
   to the Table field and in the pop-up dialog
   box, select the Use custom object check box and enter the name
   of the table into which the data will be written in the Object
   Name field. In this example, it is `EMPLOYEE`,
   the table created by the tSnowflakeRow component. When done,
   click OK to close the dialog box.
9. From the Output action
   drop-down list, select Insert to write data to
   the table `EMPLOYEE`.
