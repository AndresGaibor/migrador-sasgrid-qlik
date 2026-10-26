<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput · versión 8.0 -->
# tAmazonAuroraInput

Last updated: 9/30/2026

Reads an Amazon Aurora database and extracts fields based on a query.

tAmazonAuroraInput executes a database query with a strictly defined
order which must correspond to the schema definition. Then it passes on the field list
to the next component via a Row >Main
link.

## tAmazonAuroraInput Standard properties

These properties are used to configure tAmazonAuroraInput
running in the Standard Job framework.

The Standard
tAmazonAuroraInput component belongs to the Cloud and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | * Either Built-In or   Repository. * Built-In: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The database connection fields that follow   are completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Type in the IP address or hostname of the Amazon Aurora database. |
| Port | Type in the listening port number of the Amazon Aurora database. |
| Database | Type in the name of the database you want to use. |
| Username and Password | Type in the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Type in the name of the table to be read. |
| Query Type and Query | Enter the database query paying particularly attention to the proper sequence of the fields in order to match the schema definition.  *If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected.* |
| Guess Query | Click the button to generate the query which corresponds to the table schema in the Query field. |
| Guess schema | Click the button to retrieve the schema from the table. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  This check box disappears when the Use an existing connection check box is selected. |
| Data source alias | Type in the alias of the data source created on the *Talend Runtime* side.  This field appears only when the Specify a data source alias check box is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. When you need to handle data of the time-stamp type *0000-00-00 00:00:00* using this component, set the parameter to noDatetimeStringSync=true&zeroDa­teTimeBehavior=convertToNull.  This field disappears when the Use an existing connection check box in the Basic settings view is selected. |
| Enable stream | Select this check box to enable streaming over buffering which allows the code to read from a large table without consuming a large amount of memory in order to optimize the performance. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Select the check box(es) in the Trim column to remove leading and trailing whitespace from the corresponding column(s).  This option disappears when the Trim all the String/Char columns check box is selected. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component of a Job or subJob and it needs an output link. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Handling data with Amazon Aurora](tamazonaurorainput-tamazonauroracommit-tlogrow-handling-data-with-amazon-aurora-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-handling-data-with-amazon-aurora-standard-component-this -->
# Handling data with Amazon Aurora

Last updated: 9/30/2026

This scenario describes a Job that writes the user information into Amazon Aurora, and then
reads the information in Amazon Aurora and displays it on the console.

The scenario requires the following seven components:

* tAmazonAuroraConnection: opens a connection
  to Amazon Aurora.
* tFixedFlowInput: defines the user information
  data structure, and sends the data to the next component.
* tAmazonAuroraOutput: writes the data it
  receives from the preceding component into Amazon Aurora.
* tAmazonAuroraCommit: commits in one go the
  data processed to Amazon Aurora.
* tAmazonAuroraInput: reads the data from
  Amazon Aurora.
* tLogRow: displays the data it receives from
  the preceding component on the console.
* tAmazonAuroraClose: closes the connection to
  Amazon Aurora.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tAmazonAuroraInput](tamazonaurorainput "Reads an Amazon Aurora database and extracts fields based on a query.")
* [tAmazonAuroraCommit](tamazonauroracommit "Commits in one go a global transaction instead of doing that on every row or every batch, and provides gain in performance, using a unique connection.")
* [tAmazonAuroraConnection](tamazonauroraconnection "Opens a connection to an Amazon Aurora database instance that can then be reused by other Amazon Aurora components.")
* [tAmazonAuroraOutput](tamazonauroraoutput "Writes, updates, makes changes or suppresses entries in an Amazon Aurora database.")
* [tAmazonAuroraClose](tamazonauroraclose "Closes an active connection to an Amazon Aurora database instance to release the occupied resources.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-adding-and-linking-components-standard-component-create -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add seven components listed previously by typing their names in the
   design workspace or dropping them from the Palette.
2. Connect tFixedFlowInput to tAmazonAuroraOutput using a Row
   > Main connection.
3. Do the same to connect tAmazonAuroraInput to
   tLogRow.
4. Connect tAmazonAuroraConnection to tFixedFlowInput using a Trigger
   > OnSubjobOk connection.
5. Do the same to connect tFixedFlowInput to tAmazonAuroraCommit, tAmazonAuroraCommit to tAmazonAuroraInput, and tAmazonAuroraInput to tAmazonAuroraClose.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Opening a connection to Amazon Aurora](/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-opening-connection-to-amazon-aurora-standard-component)
* [Writing the data into Amazon Aurora](/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-writing-data-into-amazon-aurora-standard-component)
* [Retrieving the data from Amazon Aurora](/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-retrieving-data-from-amazon-aurora-standard-component)
* [Closing the connection to Amazon Aurora](/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-closing-connection-to-amazon-aurora-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 or click Run on the Run tab to run the
   Job.

   As shown above, the user information is written into Amazon Aurora, and then the data is
   retrieved from Amazon Aurora and displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-closing-connection-to-amazon-aurora-standard-component -->
# Closing the connection to Amazon Aurora

Last updated: 9/30/2026

## Procedure

1. Double-click tAmazonAuroraClose to open its Basic settings view.
2. In the Component List, select the connection
   component you have configured.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-opening-connection-to-amazon-aurora-standard-component -->
# Opening a connection to Amazon Aurora

Last updated: 9/30/2026

## Procedure

1. Double-click tAmazonAuroraConnection to open its
   Basic settings view.
2. In the Host, Port,
   Database, Username and Password fields,
   enter the information required for the connection to Amazon Aurora.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-retrieving-data-from-amazon-aurora-standard-component -->
# Retrieving the data from Amazon Aurora

Last updated: 9/30/2026

## Procedure

1. Double-click tAmazonAuroraInput to open its
   Basic settings view.
2. Select the Use an existing connection check
   box and in the Component List that appears,
   select the connection component you have configured.
3. Click the [...] button next to Edit schema and in the pop-up window define the
   schema by adding three columns: *id* of Integer
   type, and *name* and *city* of String type. The data structure is same as the structure
   you have defined for tFixedFlowInput.
4. In the Table Name field, enter or browse to
   the table into which you write the data. In this example, it is *TalendUser*.
5. Click the Guess Query button to generate the
   query. The Query field will be filled with the
   automatically generated query.
6. Double-click tLogRow to open its Basic settings view.
7. In the Mode area, select Table (print values in cells of a table) for better
   readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainput-tamazonauroracommit-tlogrow-writing-data-into-amazon-aurora-standard-component -->
# Writing the data into Amazon Aurora

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit
   schema and in the pop-up window define the schema by adding three
   columns: *id* of Integer type, and *name* and *city* of
   String type.

   Click OK to validate the changes and accept
   the propagation prompted by the pop-up dialog box.
3. In the Mode area, select Use Inline Content (delimited file) and enter the
   following user information in the Content
   field.

   ```
   1;George;Bismarck
   2;Abraham;Boise
   3;Taylor;Nashville
   4;William;Jefferson City
   5;Alexander;Jackson
   6;James;Boise
   7;Gerald;Little Rock
   8;Tony;Richmond
   9;Thomas;Springfield
   10;Andre;Nashville
   ```
4. Double-click tAmazonAuroraOutput to open its
   Basic settings view.
5. Select the Use an existing connection check
   box and in the Component List that appears,
   select the connection component you have configured.
6. In the Table field, enter or browse to the
   table into which you want to write the data. In this example, it is *TalendUser*.
7. Select Drop table if exists and create from
   the Action on table drop-down list, and select
   Insert from the Action on data drop-down list.
8. Double-click tAmazonAuroraCommit to open its
   Basic settings view.
9. Clear the Close Connection check box if it is
   selected.
