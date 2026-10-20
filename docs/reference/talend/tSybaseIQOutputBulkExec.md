<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec · versión 8.0 -->
# tSybaseIQOutputBulkExec

Last updated: 9/30/2026

Information noteImportant: Support for Sybase 12 through 15
is removed from 8.0.1-R2024-12 onwards. Use Sybase 16 instead.

Gains in performance during Insert operations to a Sybase IQ database.

tSybaseIQOutputBulkExec executes the
Insert action on the data provided.

## tSybaseIQOutputBulkExec Standard properties

These properties are used to configure tSybaseIQOutputBulkExec
running in the Standard Job framework.

The Standard
tSybaseIQOutputBulkExec component belongs to the
Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  When reusing an existing Sybase 16 (SQL Anywhere) connection created by a tSybaseConnection component and loading data from a file located on the client side, you need to select Sybase 16 (SQL Anywhere) from the DB Version drop-down list to display the Is client file check box before selecting this check box.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection).  This property is not available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| DB Version | Select the version of the Sybase database to be used from the drop-down list.   * For Sybase IQ 12 and Sybase IQ 16, the file to be bulk-loaded must be located on   the same machine as the Sybase IQ server. * For Sybase IQ 15, the file to be bulk-loaded can be located on the client side,   however, this means certain setup on the Sybase IQ server. For more information, see   [Sybase IQ client-side load support   enhancements](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc00787.0480/html/etl_nfg/CHDEIAJG.htm). * For Sybase 16 (SQL Anywhere), the file to be bulk-loaded can be located on both the   server side and the client side.  Before loading data into Sybase 16 (SQL Anywhere), SQL Anywhere 17 must be   installed. You can download it [here](https://archive.sap.com/documents/docs/DOC-35857). Once the installation is done, you need to check the system   variable `Path` to make sure the installation path of   SQL Anywhere 17 has been added to it, and then restart Talend Studio (in certain case restart the computer) to have the new   `Path` variable take effect. |
| Host | The IP address or hostname of the database.  This property is not available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| Port | The listening port number of the database.  This property is not available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| Data Source | Select the type of the data source to be used and complete the corresponding DSN information in the field alongside. The available types are `DSN` and `FILEDSN`.  When `FILEDSN` is selected, a [...] button is available next to the Data Source field to allow you to browse to the data source file of interest.  This property is available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| Database | Enter the name of the database. |
| Sybase Schema | The schema of the database. |
| Username and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | The name of the table to be written. |
| Action on table | On the table defined, you can perform one of the following operations:   * Default: No operation is   carried out. * Drop and create table:   The table is removed and created again. * Create table: The table   does not exist and gets created. * Create table if does not   exist: The table is created if it does not   exist. * Drop table if exists and   create: The table is removed if it already   exists and created again. * Clear table: The table   content is deleted. |
| Filename | Enter the name of the file to be generated and loaded. |
| Is client file | Select this check box if you need to load data from the client side.  This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Append the file | Select this check box to add the new rows at the end of the records. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. |
| Fields terminated by | Enter the character, string or regular expression used to separate fields.  Information noteWarning: As a combination of tSybaseOutputBulk and tSybaseIQBulkExec, this component does not allow the use of Sybase-oriented row/field separators, such as \x09. To achieve the desired effect (for example, displaying fields in the tabular form), you need to use tSybaseOutputBulk and tSybaseIQBulkExec together to replace tSybaseIQOutputBulkExec, with \t used in the former component and \x09 used in the latter. |
| Lines terminated by | Enter the character or sequence of characters used to separate lines. |
| Use enclosed quotes | Select this check box to use data enclosure characters. |
| Include Head | Select this heck box to include the column header. |
| Blank as null | Select this check box to store the input zero-length varchars as NULLs instead of blanks in the database during the load operation. |
| On file error | Select the action Sybase performs when an error occurs:   * Rollback (default): rolls back the entire transaction. * Finish: finishes the insertions already completed and ends   the load operation. * Continue: skips the error and continues the load   operation.   This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Message log file | The path to the MESSAGE LOG file that saves the log information about integrity constraint violations, the types of violations, etc. It must be specified together with the Row log file property.  This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Row log file | The path to the ROW LOG file that saves the log information about reject data, the timestamps of the start and completion of the load, etc. It must be specified together with the Message log file property.  This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Encoding | Select the encoding type from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. |

**Related concepts**  

* [Bulk-loading data to a Sybase IQ 12 database](tsybaseiqoutputbulkexec-trowgenerator-bulk-loading-data-to-sybase-iq-12-database-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec-trowgenerator-bulk-loading-data-to-sybase-iq-12-database-standard-component-this -->
# Bulk-loading data to a Sybase IQ 12 database

Last updated: 9/30/2026

This scenario describes a Job that writes data generated by a tRowGenerator component into a file and then bulk-loads the data
from the file to a Sybase IQ 12 database.

### In this section

* [Adding and linking the components](/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec-trowgenerator-adding-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec-trowgenerator-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec-trowgenerator-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tSybaseIQOutputBulkExec](tsybaseiqoutputbulkexec "Gains in performance during Insert operations to a Sybase IQ database.")

**Related information**  

* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec-trowgenerator-adding-and-linking-components-standard-component-create -->
# Adding and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add a tRowGenerator
   component and a tSybaseIQOutputBulkExec
   component by typing their names in the design workspace or dropping them from
   the Palette.
2. Link the tRowGenerator component to the
   tSybaseIQOutputBulkExec component using a
   Row > Main connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec-trowgenerator-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Procedure

1. Double-click the tRowGenerator component to
   open its RowGenerator Editor.
2. Click the [+] button to add two columns and
   set their properties:
   * *id*, Integer type, using Numeric.sequence(String,int,int) from the
     Functions list to generate sequence
     numbers.
   * *name*, String type, using TalendDataGenerator.getFirstName() from the
     Functions list to generate random
     first names.
3. In the Number of Rows for RowGenerator field,
   enter the number of rows to be generated. In this example, keep the default
   value *100*.
4. Click OK to close the editor and in the
   pop-up dialog box click Yes to propagate the
   schema to the next component.
5. Double-click the tSybaseIQOutputBulkExec
   component to open its Basic settings
   view.
6. In the Host, Port, Database, Username and Password fields, enter the information required to access the
   Sybase IQ 12 database.
7. In the Table field, enter the name of the
   table into which the data will be writen. In this example, it is *staff*.
8. In the Action on table list, select Create table if not exists.
9. In the Filename field, enter the full path of
   the file to hold the data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybaseiqoutputbulkexec-trowgenerator-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the Job.
2. Press F6 to run the Job.
3. In the Sybase Central console, open the table *staff* to check the data:

   As shown above, the table is created with data inserted.
