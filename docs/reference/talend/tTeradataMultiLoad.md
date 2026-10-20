<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatamultiload · versión 8.0 -->
# tTeradataMultiLoad

Last updated: 9/30/2026

Executes a database query according to a strict order which must be the same as the
one in the schema.

tTeradataMultiLoad reads a database
and extracts fields using queries. The retrieved list of fields is then transferred to the
next component, using a connection flow (Main row).

## tTeradataMultiLoad Standard properties

These properties are used to configure tTeradataMultiLoad running in the Standard Job framework.

The Standard
tTeradataMultiLoad component belongs to the Databases family.

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
| Action to data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, Job stops.  Update: Make changes to existing entries  Insert or update: Insert a new record. If the record with the given reference already exists, an update would be made.  Delete: Remove entries corresponding to the input flow.  Information noteWarning: *It is necessary to specify at least one column as a primary key on which the Update and Delete operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s).* |
| Where condition in case Delete | Type in a condition, which, once verified, will delete the row.  This field appears only when Delete is selected from the Action to data drop-down list. |
| Load file | Browse your directory and select the file from which you want to load data. |
| Field separator | Character, string, or regular expression to separate fields. |
| Error file | Browse your directory and select the destination of the file where the error messages will be recorded. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Define Log table | This check box is selected to define a log table you want to use in place of the default one that is the database table you defined in Basic settings. The syntax required to define the log table is *databasename.logtablename*. |
| BEGIN LOAD | This field allows you to define your BEGIN LOAD command to initiate or restart a load task. You can specify the number of sessions to use, the error limit, any other parameters needed to execute the task.  For more information, see *Teradata MultiLoad Reference* documentation. |
| Return mload error | Select this check box to specify the exit code number to indicate the point at which an error message should display in the console. |
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
