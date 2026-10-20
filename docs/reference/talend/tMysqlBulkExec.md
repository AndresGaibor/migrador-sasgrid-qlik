<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlbulkexec · versión 8.0 -->
# tMysqlBulkExec

Last updated: 9/30/2026

Offers gains in performance while executing the Insert operations on a MySQL or
Aurora database.

The tMysqlOutputBulk and tMysqlBulkExec components are used together in a two step
process. In the first step, an output file is generated. In the second step, this file
is used in the INSERT statement used to feed a database. These two steps are fused
together in the tMysqlOutputBulkExec component,
detailed in a separate section. The advantage of using two separate steps is that the
data can be transformed before it is loaded in the database.

## tMysqlBulkExec Standard Properties

These properties are used to configure tMysqlBulkExec running in the Standard Job framework.

The Standard
tMysqlBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| DB Version | Select the version of the database that you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted. You have the possibility to rollback the operation.  Truncate table: The table content is deleted. You do not have the possibility to rollback the operation. |
| Table | Name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Local file Name | Name of the file to be loaded.  This file should be located on the same machine where Talend Studio is installed or where the Job using tMysqlBulkExec is deployed. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Lines terminated by | Character or sequence of characters used to separate lines. |
| Fields terminated by | Character, string or regular expression to separate fields. |
| Enclosed by | Character used to enclose text. |
| Action on data | On the data of the table defined, you can perform:  Insert records in table: Add new records to the table.  Update records in table: Make changes to existing records.  Replace records in table: Replace existing records with new ones. Ignore records in table: Ignore the existing records, or insert the new ones. |
| Records contain NULL value | Check this box if you want to retrieve the null values from the input data flow. If you do not check this box, the null values from the input data flow will be considered as empty fields in the output data flow. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is to be used along with tMysqlOutputBulk component. Used together, they can offer gains in performance while feeding a MySQL or Aurora database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Inserting transformed data in MySQL database](tmysqlbulkexec-tmysqloutputbulk-tmap-inserting-transformed-data-in-mysql-database-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-inserting-transformed-data-in-mysql-database-standard-component-this -->
# Inserting transformed data in MySQL database

Last updated: 9/30/2026

This scenario describes a four-component Job which aims at fueling a database
with data contained in a file, including transformed data. Two steps are required in this job,
first step is to create the file, that will then be used in the second step. The first step
includes a tranformation phase of the data included in the file.

### In this section

* [Dropping and linking components](/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-dropping-and-linking-components-standard-component-drag)
* [Configuring the components](/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-configuring-components-standard-component-a)
* [Saving and executing the Job](/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tMysqlOutputBulkExec](tmysqloutputbulkexec "Executes the Insert action in the specified MySQL or Aurora database.")
* [tMysqlBulkExec](tmysqlbulkexec "Offers gains in performance while executing the Insert operations on a MySQL or Aurora database.")
* [tMysqlOutputBulk](tmysqloutputbulk "Writes a file with columns based on the defined delimiter and the MySQL or Aurora standards.")

**Related information**  

* [tMap](/talend/en-US/components/8.0/tmap/tmap)
* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-configuring-components-standard-component-a -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. A tRowGenerator is used to generate
   random data. Double-click on the tRowGenerator
   component to launch the editor.
2. Define the schema of the rows to be generated and the nature of data to
   generate. In this example, the *clients* file to be
   produced will contain the following columns: *ID*,
   *First Name*, *Last Name*,
   *Address*, *City* which all are
   defined as string data but the ID that is of integer type.

   Some schema information don't necessarily need to be displayed. To hide
   them away, click on Columns list button
   next to the toolbar, and uncheck the relevant entries, such as Precision or Parameters.

   Use the plus button to add as many columns to your schema
   definition.

   Click the Refresh button to preview the first generated row of your
   output.
3. Then select the tMap component to set the
   transformation.
4. Drag and drop all columns from the input table to the output table.
5. Apply the transformation on the *LastName* column by
   adding .toUpperCase() in its expression field.

   Then, click OK to validate the
   transformation.
6. Double-click on the tMysqlOutputBulk
   component.
7. Define the name of the file to be produced in File
   Name field. If the delimited file information is stored in
   the Repository, select it in Property Type field, to retrieve relevant data.
   In this use case the file name is *clients.txt*.

   The schema is propagated from the tMap
   component, if you accepted it when prompted.
8. In this example, don't include the header information as the table should
   already contain it.
9. Click OK to validate the output.
10. Then double-click on the tMysqlBulkExec
    component to set the INSERT query to be executed.
11. Define the database connection details. We recommend you to store
    this type of information in the Repository, so that you can retrieve them at any time
    for any Job.
12. Set the table to be filled in with the collected data, in the Table field.
13. Fill in the column delimiters in the Field
    terminated by area.
14. Make sure the encoding corresponds to the data encoding.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-dropping-and-linking-components-standard-component-drag -->
# Dropping and linking components

Last updated: 9/30/2026

## Procedure

1. Drag and drop a tRowGenerator, a
   tMap, a tMysqlOutputBulk as well as a tMysqlBulkExec component.
2. Connect the main flow using row Main
   links.
3. And connect the start component (tRowgenerator in this example) to the tMysqlBulkExec using a trigger connection, of type OnComponentOk.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Press F6 or click Run on the Run tab to
   execute the Job.

   The *clients* database table is filled with data from
   the file including upper-case *last name* as transformed
   in the job.

## Results

For simple Insert operations that don't include any transformations, the use of
tMysqlOutputBulkExec allows you to skip a step
in the process and thus improves performance.

Related topic: [tMysqlOutputBulkExec Standard properties](/talend/en-US/components/8.0/mysql/tmysqloutputbulkexec#tmysqloutputbulkexec-standard-properties)
