<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatpump · versión 8.0 -->
# tTeradataTPump

Last updated: 9/30/2026

Inserts, updates, or deletes data in the Teradata database with the TPump loading
utility which allows near-real-time data to be achieved in the data warehouse.

Use this component particularly for environments where batch windows are
shrinking and warehouse maintenance overlaps normal working hours.

## tTeradataTPump Standard properties

These properties are used to configure tTeradataTPump running in the Standard Job framework.

The Standard
tTeradataTPump component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Execution platform | Select the Operating System type you use. |
| Host | Host name or IP address of the database server. |
| Database name | Database name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Script generated folder | Browse your directory and select the destination of the file which will be created. |
| Action to data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, job stops.  Update: Make changes to existing entries  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made.  Delete: Remove entries corresponding to the input flow.  Information noteWarning: *It is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s).* |
| Where condition in case Delete | Type in a condition, which, once verified, will delete the row.  This field appears only when Delete is selected from the Action to data drop-down list. |
| Load file | Browse your directory and select the file from which you want to load data. |
| Field separator | Character, string, or regular expression to separate fields. |
| Error file | Browse your directory and select the destination of the file where the error messages will be recorded. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Define Log table | This check box is selected to define a log table you want to use in place of the default one that is the database table you defined in Basic settings. The syntax required to define the log table is *databasename.logtablename*. |
| BEGIN LOAD | This field allows you to define your BEGIN LOAD command to initiate or restart a TPump task. You can specify the number of sessions to use, the error limit and any other parameters needed to execute the task. The default value is:  SESSIONS 8 PACK 600 ARRAYSUPPORT ON CHECKPOINT 60 TENACITY 2 ERRLIMIT 1000.  For more information, see *Teradata Parallel Data Pump Reference* documentation. |
| Return tpump error | Select this check box to specify the exit code number to indicate the point at which an error message should display in the console. |
| Define character set | Specify the character encoding you need use for your system |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | EXIT\_VALUE: the process exit code. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query and covers all possible SQL queries. |

**Related tasks**  

* [Inserting data into a Teradata database table](tteradatatpump-trowgenerator-tfileoutputdelimited-tfileoutputdelimited-inserting-data-into-teradata-database-table-standard-component-in-this "In this scenario, you create a Job using tTeradataTPump to insert customer data into a Teradata database table and specify the exit code to be displayed in the event of an exception error.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatpump-trowgenerator-tfileoutputdelimited-tfileoutputdelimited-inserting-data-into-teradata-database-table-standard-component-in-this -->
# Inserting data into a Teradata database table

Last updated: 9/30/2026

In this scenario, you create a Job using tTeradataTPump to
insert customer data into a Teradata database table and specify the exit code to be
displayed in the event of an exception error.

Three components are used in this Job:

* tRowGenerator: generates rows as required using
  random customer data taken from a list.
* tFileOutputDelimited: outputs the customer data
  into a delimited file.
* tTeradataTPump: inserts the customer data into
  the Teradata database table in the TPump mode.

## Dropping components

### Procedure

1. Place the following components from the Palette onto the design workspace:

   * tRowGenerator,
   * tFileOutputDelimited,
   * tTeradataTPump.
2. Link tRowGenerator to
   tFileOutputDelimited using a Row > Main
   connection.
3. Link tRowGenerator to
   tTeradataTPump using a Trigger > On
   SubjobOk connection.

## Configuring the components

### Procedure

1. Double-click tRowGenerator to open the tRowGenerator
   Editor window.

   In the tRowGenerator
   Editor window, define the data to be generated. For this Job, the
   schema is composed of two columns: *ID* and *Name*.

   Enter the Number of Rows for
   RowGenerator to generate.
2. Double-click tFileOutputDelimited to define its properties in the Component view.
3. Next to File Name, browse
   to the output file or enter a name for the output file to be created.
4. Between double quotation marks, enter the delimiters to be used
   next to Row Separator and Field Separator.

   Click Edit schema and
   check that the schema matches the input schema. If need be, click Sync Columns.
5. Double-click tTeradataTPump to open its Component view.

   In the Basic settings
   tab of the Component view, define the
   tTeradataTPump parameters.
6. Enter the Database name,
   User name and Password in accordance with your database authentication
   information.
7. Specify the Table into
   which you want to insert the customer data. In this scenario, it is called
   `mytable`.
8. In the Script generated
   folder field, browse to the folder in which you want to store the
   script files generated.
9. In the Load file field,
   browse to the file which contains the customer data.
10. In the Error file field,
    browse to the file in which you want to log the error information.
11. In the Action on data
    field, select Insert.

## Executing the Job

### Procedure

1. Press F6 to execute the
   Job.

   The Run view console reads as follows:
2. Double-click the tTeradataTPump component to go back to its Component view.
3. On the Advanced settings
   tab, select the Return tpump error check
   box and type in the exit code number to indicate the point at which an error
   message should be displayed in the console.

   In this example, enter the number `4` and use the default
   values for the other parameters.
4. Press F6 to run the
   Job.

   The Run view console reads as follows:

   An exception error occurs and TPump
   returned exit code 12 is displayed. If you need to view detailed
   information about the exception error, you can open the log file stored in the
   directory you specified in the Error file
   field in the Basic settings tab of the
   Component view.

**Related reference**  

* [tTeradataTPump](tteradatatpump "Inserts, updates, or deletes data in the Teradata database with the TPump loading utility which allows near-real-time data to be achieved in the data warehouse.")

**Related information**  

* [tRowGenerator](/talend/en-US/components/8.0/trowgenerator/trowgenerator)
* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
