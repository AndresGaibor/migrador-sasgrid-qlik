<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec · versión 8.0 -->
# tExasolBulkExec

Last updated: 9/30/2026

Imports data into an Exasol database table using the IMPORT command provided by the Exasol database in a fast way.

The import will be cancelled after a configurable number of records fail to import. Erroneous records can be sent to a log table in the same database or to a local log file.

## tExasolBulkExec Standard properties

These properties are used to configure
tExasolBulkExec running in the Standard Job framework.

The
Standard
tExasolBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use an existing connection | Select this check box and from the list displayed select the relevant connection component to reuse the connection details you have already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored   centrally. * Repository: Select the repository file in which   the properties are stored. The database connection fields that   follow are completed automatically using the data   retrieved. |
| Host | Enter the host or host list of the Exasol database servers. Exasol can run in a cluster environment. The valid value can be a simple IP address (for example, *172.16.173.128*), an IP range list (for example, *172.16.173.128..130* that represents three servers *172.16.173.128*, *172.16.173.129*, and *172.16.173.130*), or a comma-separated host list (for example, *server1,server2,server3*) of the Exasol database cluster. |
| Port | Enter the listening port number of the Exasol database cluster. |
| Schema | Enter the name of the schema you want to use. |
| User and Password | Enter the user authentication data to access the Exasol database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Enter the name of the table to be written.  Information noteNote: Typically the table names are stored in upper case. If you need mixed case identifiers, you have to enter the name in double quotes. For example, "\"TEST\_data\_LOAD\"". |
| Action on table | On the table defined, you can perform one of the following operations before running the import:   * None: No operation is carried out. * Drop and create   table: The table is removed and created   again. * Create   table: The table does not exist and gets   created. * Create table if   not exists: The table is created if it does not   exist. * Truncate   table: The table content is deleted. You do not   have the possibility to rollback the operation. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. Information noteNote: The columns in the schema must be in the same order as they   are in the CSV file. It is not necessary to fill all columns of the defined   table unless the use case or table definition expects that. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Column Formats | Specify the format for Date and numeric columns if the default can not be applied.   * Column: The cells in this column are   automatically filled with the defined schema column   names. * Has Thousand   Delimiters: Select this check box if the value   of the corresponding numeric column (only for numeric column) in   the file contains thousand separators. * Alternative   Format: Specify the necessary format as String   value if a special format is expected. The necessary format will   be created from the schema column length and precision. For more   information about format models, see [Exasol User Manual](https://www.exasol.com/support/secure/attachment/35839/EXASolution_User_Manual-5.0.11-en.pdf). |
| Source table columns | If the source is a database, configure the mapping between the source columns and the target columns in this table.  Specifically configuring the mapping is optional. If you set nothing here, it is assumed that the source table has the same structure as the target table.  * Column: The schema column in the target   table. * Source column name: The name of the column   in the source table. |
| Column Separator | Enter the separator for the columns of a row in the local file. |
| Column Delimiter | Enter the delimiter that encapsulates the field content in the local file. |
| Row Separator | Enter the char used to separate the rows in the local file. |
| Null representation | Enter the string that represents a NULL value in the local file. If not specified, NULL values are represented as the empty string. |
| Skip rows | Enter the number of rows (for example, header or any other prefix rows) to be omitted. |
| Encoding | Enter the character set used in the local file. By default, it is *UTF8*. |
| Trim column values | Specify whether spaces are deleted at the border of CSV columns.   * No   trim: no spaces are trimmed. * Trim: spaces from both left and right sides are   trimmed. * Trim only   left: spaces from only the left side are   trimmed. * Trim only   right: spaces from only the right side are   trimmed. |
| Default Date Format | Specify the format for datetime values. By default, it is *YYYY-MM-DD*. |
| Default Timestamp Format | Specify the timestamp format used. By default, it is *YYYY-MM-DD HH24:MI:SS.FF3*. |
| Thousands Separator | Specify the character used to separate thousand groups in a numeric text value. In the numeric format, the character will be applied to the placeholder *G*. If the text values contain this char, you have to configure it also in the Column Formats table.  Note that this setting affects the connection property *NLS\_NUMERIC\_CHARACTERS* that defines the decimal and group characters used for representing numbers. |
| Decimal Separator | Specify the character used to separate the integer part of a number from the fraction. In the numeric format, the character will be applied to the placeholder *D*.  Note that this setting affects the connection property *NLS\_NUMERIC\_CHARACTERS* that defines the decimal and group characters used for representing numbers. |
| Minimal number errors to reject the transfer | Specify the maximum number of invalid rows allowed during the data loading process. For example, the value *2* means the loading process will stop if the third error occurs. |
| Log Error Destination | Specify the location where error messages will be stored.   * No   Logging: error messages will not be   saved. * Local Log   File: error messages will be stored in a   specified local file.    + Local Error Log File:     specify the path to the local file that stores error     messages.   + Add current timestamp to log file     name (before extension): select this     check box to add the current timestamp before the     extension of the file name for identification reasons in     case you use the same file multiple times. * Logging   Table: error messages will be stored in a   specified table. The table will be created if it does not   exist.    + Error Log Table: enter     the name of the table that stores error     messages.   + Use current timestamp to build log     table: select this check box to use the     current timestamp to build the log table for     identification reasons in case you use the same table     multiple times. |
| Transfer files secure | Select this check box to transfer the file over HTTPS instead of HTTP. |
| Test mode (no statements are executed) | Select this check box to have the component running in test mode, where no statements are executed. |
| Use precision and length from schema | Select this check box to check column values that are of numeric types (that is, Double, Float, BigDecimal, Integer, Long, and Short) against the Length setting (which sets the number of integer digits) and the Precision setting (which sets the number of decimal digits) in the schema. Only the values with neither their number of integer digits nor number of decimal digits larger than the Length setting and the Precision setting are loaded.  For example, with Length set to `4` and Precision set to `3`, the values `8888.8888` and `88888.888` will be dropped; the values `8888.88` and `888.888` will be loaded. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  FILENAME: the name of the file processed. This is an After variable and it returns a string.  ERROR\_LOG\_FILE: the path to the local log file. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a standalone component. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Importing data into an Exasol database table from a local CSV file](texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-importing-data-into-exasolution-database-table-from-local-csv-file-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-importing-data-into-exasolution-database-table-from-local-csv-file-standard-component-this -->
# Importing data into an Exasol database table from a local CSV file

Last updated: 9/30/2026

This scenario describes a Job that writes employee information into a CSV file, then loads the data from this local file into a newly created Exasol database table using the tExasolBulkExec component, and finally retrieves the data from the table and displays it on the console.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-dropping-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tExasolBulkExec](texasolbulkexec "Imports data into an Exasol database table using the IMPORT command provided by the Exasol database in a fast way.")
* [tExasolInput](texasolinput "Retrieves data from an Exasol database based on a query with a strictly defined order which corresponds to the schema definition, and passes the data to the next component.")

**Related information**  

* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Preparing the source data](/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-preparing-source-data-standard-component)
* [Loading the source data into a newly created Exasol database table](/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-loading-source-data-into-newly-created-exasolution-database-table-standard-component)
* [Retrieving data from the Exasol database table](/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-retrieving-data-from-exasolution-database-table-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-dropping-and-linking-components-standard-component-create -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in the design workspace or dropping them from the Palette: a tFixedFlowInput component, a tFileOutputDelimited component, a tExasolBulkExec component, a tExasolInput component, and a tLogRow component.
2. Connect the tFixedFlowInput component to the tFileOutputDelimited component using a Row>Main connection.
3. Do the same to connect the tExasolInput component to the tLogRow component.
4. Connect the tFixedFlowInput component to the tExasolBulkExec component using a Trigger>On Subjob Ok connection.
5. Do the same to connect the tExasolBulkExec component to the tExasolInput component.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to execute the Job.

   As shown above, the employee data is written into the specified Exasol
   database table and is then retrieved and displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-loading-source-data-into-newly-created-exasolution-database-table-standard-component -->
# Loading the source data into a newly created Exasol database table

Last updated: 9/30/2026

## Procedure

1. Double-click the tExasolBulkExec component to open its Basic settings view.
2. Fill in the Host, Port, Schema, User and Password fields with your Exasol database connection details.
3. In the Table field, enter the name of the table into which the source data will be written. In this example, the target database table is named *"employee"* and it does not exist.
4. Select Create table from the Action on table list to create the specified table.
5. In the Source area, select Local file as the source for the input data, and then specify the file that contains the source data. In this example, it is *"E:/employee.csv"*.
6. Click the [...] button next to Edit schema to open the Schema dialog box and define the schema, which should be the same as that of the tFixedFlowInput component.

   Then click OK to validate these changes and close the dialog box.
7. Click Advanced settings to open the Advanced settings view of the tExasolBulkExec component.
8. In the Column Formats table, for the two numeric fields *EmployeeID* and *MonthSalary*, select the corresponding check boxes in the Has Thousand Delimiters column, and then define their format model strings in the corresponding fields of the Alternative Format column. In this example, *"99G999"* for *EmployeeID* and *"99G999D99"* for *MonthSalary*.
9. Make sure that the Thousands Separator and Decimal Separator fields have values identical to those of the tFileOutputDelimited component and keep the default settings for the other options.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-preparing-source-data-standard-component -->
# Preparing the source data

Last updated: 9/30/2026

## Procedure

1. Double-click the tFixedFlowInput component to
   open its Basic settings view.
2. Click the [...] button next to Edit schema to open the Schema dialog box.
3. Click the [+] button to add six columns:
   *EmployeeID* of the Integer type, *EmployeeName*,
   *OrgTeam* and *JobTitle* of the String type,
   *OnboardDate* of the Data type with the *yyyy-MM-dd*
   date pattern, and *MonthSalary* of the
   Double type.
4. Click OK to close the dialog box and accept
   schema propagation to the next component.
5. In the Mode area, select Use Inline Content (delimited file) and enter the
   following employee data in the Content
   field.

   ```
   12000;James;Dev Team;Developer;2008-01-01;15000.01
   12001;Jimmy;Dev Team;Developer;2008-11-22;13000.11
   12002;Herbert;QA Team;Tester;2008-05-12;12000.22
   12003;Harry;Doc Team;Technical Writer;2009-03-10;12000.33
   12004;Ronald;QA Team;Tester;2009-06-20;12500.44
   12005;Mike;Dev Team;Developer;2009-10-15;14000.55
   12006;Jack;QA Team;Tester;2009-03-25;13500.66
   12007;Thomas;Dev Team;Developer;2010-02-20;16000.77
   12008;Michael;Dev Team;Developer;2010-07-15;14000.88
   12009;Peter;Doc Team;Technical Writer;2011-02-10;12500.99
   ```
6. Double-click the tFileOutputDelimited
   component to open its Basic settings
   view.
7. In the File Name field, specify the file into
   which the input data will be written. In this example, it is *"E:/employee.csv"*.
8. Click Advanced settings to open the Advanced settings view of the tFileOutputDelimited component.
9. Select the Advanced separator (for numbers)
   check box and in the Thousands separator and
   Decimal separator fields displayed, specify
   the separators for thousands and decimal. In this example, the default values
   *","* and *"."* are used.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolbulkexec-texasolinput-tfixedflowinput-tlogrow-retrieving-data-from-exasolution-database-table-standard-component -->
# Retrieving data from the Exasol database table

Last updated: 9/30/2026

## Procedure

1. Double-click the tExasolInput component to open its Basic settings view.
2. Fill in the Host name, Port, Schema name, Username and Password fields with your Exasol database connection details.
3. In the Table Name field, enter the name of the table from which the data will be retrieved. In this example, it is *"employee"*.
4. Click the [...] button next to Edit schema to open the Schema dialog box and define the schema, which should be the same as that of the tFixedFlowInput component.

   Then click OK to close the dialog box and accept schema propagation to the next component.
5. Click the Guess Query button to fill the Query field with the following auto-generated SQL statement that will be executed on the specified table.

   ```
   SELECT employee.EmployeeID,
   		employee.EmployeeName,
   		employee.OrgTeam,
   		employee.JobTitle,
   		employee.OnboardDate,
   		employee.MonthSalary
   FROM	employee
   ```
6. Double-click the tLogRow component to open its Basic settings view.
7. In the Mode area, select the Table (print values in cells of a table) option for better readability of the output.
