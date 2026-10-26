<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinvalidrows · versión 8.0 -->
# tMySQLInvalidRows

Last updated: 9/30/2026

Checks MySQL database rows against specific Data Quality patterns (regular
expression) or Data Quality rules (business rule).

tMySQLInvalidRows extracts DB rows that do not match a given data quality
pattern or rule. You can then implement any required correction.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tMySQLInvalidRows Standard properties

These properties are used to configure tMySQLInvalidRows running in the Standard Job framework.

The Standard
tMySQLInvalidRows component belongs to the Data Quality and the Databases families.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Validation type | Either Regex pattern validation or DQ rule validation.  Regex pattern validation: Validate data in the database against regex patterns.  DQ rule validation: Validate data in the database against DQ rules. |
| Property type | Either Built-in or Repository.  Built-in: No property data stored centrally.  Repository: Select the repository file where Properties are stored. The fields that come after are pre-filled in using the fetched data. |
| DB Version | Select the MySQL version you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository. * Built-in: You create and store   the schema locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository and thus reuse it   when needed. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Table Name | Enter the name of the table to be read. |
| Where clause | Enter a WHERE clause to define a row filter on the table.  You can use the WHERE clause to filter the rows you want to analyze in the table. This WHERE clause enables you then to retrieve valid and invalid data that match certain specified criteria or conditions. |
| Analyzed column | This field is available when Regex pattern validation is selected as Validation type. |
| Custom pattern | Select this check box to enter a custom pattern. This check box is available when Regex pattern validation is selected as Validation type. |
| Patterns list | Select a pattern against which you want to check the DB rows. This field is available when Regex pattern validation is selected as Validation type. |
| DQ rule list | Select from the list the rule against which you want to check the DB rows. This field is available when DQ rule validation is selected as Validation type. |
| Query type | Built-in: Fill in manually the query statement or build it graphically using SQLBuilder. Repository: Select the relevant query stored in the Repository. The Query field is filled in accordingly. This field is available when DQ rule validation is selected as Validation type. |
| Guess Query | Click to generate the query which corresponds to your table schema. You can edit the query in the Query field.  This button is available when DQ rule validation is selected as Validation type. |
| Guess schema | Click to retrieve the schema from the table.  This button is available when DQ rule validation is selected as Validation type. |
| Query | Enter the query between double quotes or click Guess Query. This field is available when DQ rule validation is selected as Validation type. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteTip: You can press Ctrl+Space to access a list of predefined global variables. |
| Enable stream | Select this check box to enable streaming over buffering. This allows reading from large tables without consuming large amount of memory in order to optimize the performance. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Select this check box to remove leading and trailing whitespace from the defined columns. This check box is not visible if Trim all the String/Char columns is selected. To enable Trim column, clear Trim all the String/Char columns. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a start or intermediary step, and requires an output flow. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Checking customer table against a given DQ rule to select customer records](tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-checking-customer-table-against-given-dq-rule-to-select-customer-records-standard-component-enterprise-this)
* [Reading email addresses from a DB table and retrieving specific data](tmysqlinvalidrows-tlogrow-reading-email-addresses-from-db-table-and-retrieving-specific-data-standard-component-enterprise-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinvalidrows-tlogrow-reading-email-addresses-from-db-table-and-retrieving-specific-data-standard-component-enterprise-this -->
# Reading email addresses from a DB table and retrieving specific data

Last updated: 9/30/2026

This scenario applies only to Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform, and
Talend Data Fabric.

This example is a two-component Job created in Talend Studio. In this example, tMySQLInvalidRows:

1. Reads the email addresses for people from a specific country from a MySQL database
   table.
2. Filters data using a WHERE clause to narrow down the validation process.
3. Checks the email values against the given Talend Studio email pattern.
4. Extracts filtered data including the invalid rows and displays them on the
   console.

Below is the database table used in this example, some customers are from
the USA and others are from Canada. The `email` column contains some
invalid addresses. The tMySQLInvalidRows component
filters data in the `email` column to read only the emails for the
customers from the USA, and then validates these email addresses against the email address
pattern.

In this example, you have already stored the schemas of the input table in
the Repository. For more information about storing schema metadata in the Repository tree view, see [Using centralized metadata in a Job](/talend/r/en-US/8.0/studio-user-guide/using-centralized-metadata-in-job).

### In this section

* [Setting up your Job](/talend/en-US/components/8.0/mysql/tmysqlinvalidrows-tlogrow-setting-up-your-job-standard-component-enterprise-in?id=3576)
* [Setting up the schema](/talend/en-US/components/8.0/mysql/tmysqlinvalidrows-tlogrow-setting-up-schema-standard-component-enterprise?id=3577)
* [Executing the Job](/talend/en-US/components/8.0/mysql/tmysqlinvalidrows-tlogrow-executing-job-standard-component-enterprise-save?id=3578)

**Related reference**  

* [tMySQLInvalidRows](tmysqlinvalidrows "Checks MySQL database rows against specific Data Quality patterns (regular expression) or Data Quality rules (business rule).")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinvalidrows-tlogrow-executing-job-standard-component-enterprise-save -->
# Executing the Job

Last updated: 9/30/2026

## Procedure

1. Save your Job.
2. Press F6 to execute it.

   The tMySQLInvalidRows component analyzed the
   email addresses only for customers from the USA in the database table against
   the selected SQL pattern (*Email Address*), and then it
   extracted all filtered data including the invalid email addresses.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinvalidrows-tlogrow-setting-up-schema-standard-component-enterprise -->
# Setting up the schema

Last updated: 9/30/2026

## Procedure

1. Double-click tDBInvalidRows
   to display its Basic settings view and define
   its properties.

   All database connection fields are automatically filled in. If you
   do not define your input files in the Repository, fill in the details manually after
   selecting Built-in in the Property Type field
2. From the Validation type
   list, select Regex pattern validation.

   This will validate data in the selected rows against a regex
   pattern. For an example about validating data against DQ rule, see [Checking customer table against a given DQ rule to select customer
   records](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlinvalidrows-tlogrow-tmysqlinvalidrows-tlogrow-checking-customer-table-against-given-dq-rule-to-select-customer-records-standard-component-enterprise-this).
3. In the Table Name field, type in the name of
   the database table on which you want to run the Job,
   *customer1* in this example.
4. In the Where clause field, type in the WHERE
   clause that will restrict the number of the analyzed rows.

   In this example, you want to examine only the emails of the
   customers from the USA.
5. In the Analyzed column list, select the
   column you want to analyze, *Email* in this example.
6. In the Patterns list, select
   the 
   Talend Studio
    database pattern against which you want to check addresses from the
   `Email` column, `Email Address` in this
   example.

   If you select the Custom
   pattern check box, you can customize the regular expression against
   which you want to check the data.
7. Double-click tLogRow to open its Basic settings view and define its properties as
   needed.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlinvalidrows-tlogrow-setting-up-your-job-standard-component-enterprise-in -->
# Setting up your Job

Last updated: 9/30/2026

## Procedure

1. In the Repository tree view,
   expand Metadata > DB Connections where you have stored the input schemas and drag and drop the relevant
   connection onto the design workspace.

   The Components dialog box
   displays.
2. Select tDBInvalidRows (MySQL)
   from the list and click OK to close the dialog
   box.

   The tDBInvalidRows
   component displays on the workspace and is named after the connection name. The MySQL
   table used in this example is called *customers* and holds the
   customers' *customer\_id, account\_num, Iname, fname, country* and
   *Email* columns.

   Information noteRemember: The connection components, including
   tMysqlConnection and tMySQLInvalidRows, have been regrouped into the
   tDBConnection component. They are automatically converted into
   this component when you place them on the workspace.
3. Drop tLogRow from the Palette onto the design workspace.
4. Connect the two components together using the Main link.
