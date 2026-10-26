<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutputbulkexec · versión 8.0 -->
# tMysqlOutputBulkExec

Last updated: 9/30/2026

Executes the Insert action in the specified MySQL or Aurora database.

As a dedicated component, tMysqlBulkExec improves performance when
performing Insert operations to a MySQL or Aurora database.

The tMysqlOutputBulk and
tMysqlBulkExec components are used together in a two step
process. In the first step, an output file is generated. In the second step, this file
is used in the INSERT statement used to feed a database. These two steps are fused
together in the tMysqlOutputBulkExec component.

## tMysqlOutputBulkExec Standard properties

These properties are used to configure tMysqlOutputBulkExec running in the Standard Job framework.

The Standard
tMysqlOutputBulkExec component belongs to the Databases family.

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
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not already exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted. |
| Table | Name of the table to be written.  Information noteNote: Note that only one table can be written at a time and that the table must already exist for the insert operation to succeed |
| Local FileName | Name of the file to be generated and loaded.  This file is generated on the same machine where Talend Studio is installed or where the Job using tMysqlOutputBulkExec is deployed. Then it is loaded to the database specified by Host field. |
| Append | Select the check box for this option to append new rows to the end of the file. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Row separator | String (ex: "\n"on Unix) to distinguish rows. |
| Field separator | Character, string or regular expression to separate fields. |
| Escape char | Character of the row to be escaped |
| Text enclosure | Character used to enclose the text. |
| Create directory if does not exist | This check box is selected by default. It creates a directory to hold the output table if required. |
| Custom the flush buffer size | Customize the amount of memory used to temporarily store output data. In the Row number field, enter the number of rows after which the memory is to be freed again. |
| Action on data | On the data of the table defined, you can carry out the following opertaions:  Insert records in table: Add new records to the table.  Update records in table: Make changes to existing records.  Replace records in table: Replace existing records with new one. Ignore records in table: Ignore existing records or insert the new ones. |
| Records contain NULL value | This check box is selected by default. It allows you to take account of NULL value fields. If you clear the check box, the NULL values will automatically be replaced with empty values. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. |

**Related concepts**  

* [Inserting data in bulk in MySQL database](tmysqloutputbulkexec-trowgenerator-inserting-data-in-bulk-in-mysql-database-standard-component-this)
* [Inserting transformed data in MySQL database](tmysqlbulkexec-tmysqloutputbulk-tmap-inserting-transformed-data-in-mysql-database-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mysql/tmysqloutputbulkexec-trowgenerator-inserting-data-in-bulk-in-mysql-database-standard-component-this -->
# Inserting data in bulk in MySQL database

Last updated: 9/30/2026

This scenario describes a two-component Job which carries out the same
operation as the one described for [tMysqlOutputBulk Standard properties](/talend/en-US/components/8.0/mysql/tmysqloutputbulk#tmysqloutputbulk-standard-properties)
and [tMysqlBulkExec Standard Properties](/talend/en-US/components/8.0/mysql/tmysqlbulkexec#tmysqlbulkexec-standard-properties), although no data is
transformed.

* Drop a tRowGenerator and a
  tMysqlOutputBulkExec component from
  the Palette to the design workspace.
* Connect the components using a link such as Row > Main.
* Set the tRowGenerator
  parameters the same way as in [Inserting transformed data in MySQL database](/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-inserting-transformed-data-in-mysql-database-standard-component-this). The schema is made of four columns including: *ID*, *First Name*, *Last Name*, *Address* and *City*.
* In the workspace, double-click the tMysqlOutputBulkExec to display the Component view and set the properties.

* Define the database connection details in the corresponding fields,
  if necessary. Consult the recommendations detailed in [Inserting transformed data in MySQL database](/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-inserting-transformed-data-in-mysql-database-standard-component-this), concerning the conservation of connection details in the Repository, under the Metadata node. In the component view, select Repository in the Property
  Type field and then select the appropriate connection in the adjacent
  field. The following fields will be filled in automatically.

* In the Action on table
  field, select the None option as you want
  to insert the data into a table which already exists.
* In the Table field, enter
  the name of the table you want to populate, the name being *clients* in this example.
* In the Local filename
  field, indicate the access path and the name of the file which contains the data
  to be added to the table. In this example, the file is *clients.txt*.
* Click on the Advanced
  settings tab to define the component's advanced parameters.

* In the Action on data
  list, select the Insert records in table
  to insert the new data in the table.
* Press F6 to run the
  Job.

The result should be pretty much the same as in [Inserting transformed data in MySQL database](/talend/en-US/components/8.0/mysql/tmysqlbulkexec-tmysqloutputbulk-tmap-inserting-transformed-data-in-mysql-database-standard-component-this), but the data might differ as these are regenerated randomly everytime the Job is
run.

**Related reference**  

* [tMysqlOutputBulkExec](tmysqloutputbulkexec "Executes the Insert action in the specified MySQL or Aurora database.")

**Related information**  

* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
