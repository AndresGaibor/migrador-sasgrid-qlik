<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400input · versión 8.0 -->
# tAS400Input

Last updated: 9/30/2026

Reads a database and extracts fields based on a query.

tAS400Input executes a DB query with a strictly defined order which
must correspond to the schema definition. Then it passes on the field list to the next
component via a Row > Main link.

## tAS400Input Standard properties

These properties are used to configure tAS400Input running in the Standard Job framework.

The Standard
tAS400Input component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Property type | Either Built-in or Repository .   * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| DB Version | Select the AS 400 version in use |
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.   * Built-in: The schema is created and   stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already exists   and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Set Query Timeout | Select this option to set a timeout period for the query or the batch query. The Job will be terminated if the query or the batch query is timed out. You can set the timeout period (in seconds) in the Timeout field.  Information noteNote:  * It varies with the driver implementations whether this option applies to an   individual SQL statement or a set of SQL statements (that is, a batch   query). Refer to your driver vendor documentation for details. * This option is available only when you have installed the R2021-12   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query and covers all possible SQL queries. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Handling data with AS/400](tas400input-tas400output-tfixedflowinput-tlogrow-handling-data-with-as-400-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-handling-data-with-as-400-standard-component-this -->
# Handling data with AS/400

Last updated: 9/30/2026

This scenario describes a Job that writes the user information into AS/400, and then reads
the information in AS/400 and displays it on the console.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tAS400Input](tas400input "Reads a database and extracts fields based on a query.")
* [tAS400Output](tas400output "Writes, updates, makes changes or suppresses entries in a database.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-adding-and-linking-components-standard-component-create -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tFixedFlowInput component, a
   tAS400Output component, a tAS400Input component, and a tLogRow component by typing their names in the design workspace
   or dropping them from the Palette.
2. Connect tFixedFlowInput to tAS400Output using a Row >
   Main connection.
3. Do the same to connect tAS400Input to tLogRow.
4. Connect tFixedFlowInput to tAS400Input using a Trigger
   > OnSubjobOk connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Writing the data into AS/400](/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-writing-data-into-as-400-standard-component)
* [Retrieving the data from AS/400](/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-retrieving-data-from-as-400-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 or click Run on the Run tab to run the
   Job.

   As shown above, the user information is written into AS/400, and then the data is
   retrieved from AS/400 and displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-retrieving-data-from-as-400-standard-component -->
# Retrieving the data from AS/400

Last updated: 9/30/2026

## Procedure

1. Double-click tAS400Input to open its Basic settings view.
2. In the Host, Database, Username and
   Password fields, enter the information
   required for the connection to AS/400.
3. Click the [...] button next to Edit
   schema and in the Schema
   dialog box define the schema by adding three columns: *id* of Integer type, and *name*
   and *city* of String type. The data structure
   is same as the structure you have defined for tFixedFlowInput.
4. In the Table Name field, enter or browse to the table
   into which you write the data. In this example, it is *doct1018*.
5. In the Query field, enter the SQL query sentence to be
   used to retrieve the user data from AS/400. In this example, it is *SELECT \* FROM doct1018*.
6. Double-click tLogRow to open its Basic settings view.
7. In the Mode area, select Table (print values in cells of a table) for better
   readability of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400input-tas400output-tfixedflowinput-tlogrow-writing-data-into-as-400-standard-component -->
# Writing the data into AS/400

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit
   schema and in the Schema
   dialog box define the schema by adding three columns: *id* of Integer type, and *name*
   and *city* of String type.

   Click OK to close the Schema dialog box and accept the propagation prompted by the
   pop-up dialog box.
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
4. Double-click tAS400Output to open its Basic settings view.
5. In the Host, Database, Username and
   Password fields, enter the information
   required for the connection to AS/400.
6. In the Table field, specify the table into which you want
   to write the data. In this example, it is *doct1018*.
7. Select Drop table if exists and create from
   the Action on table drop-down list, and select
   Insert from the Action on data drop-down list.
