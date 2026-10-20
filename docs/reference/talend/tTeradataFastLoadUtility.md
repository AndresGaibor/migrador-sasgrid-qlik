<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatafastloadutility · versión 8.0 -->
# tTeradataFastLoadUtility

Last updated: 9/30/2026

Executes a database query according to a strict order which must be the same as the
one in the schema.

tTeradataFastLoad
Utility reads a database and extracts fields using
queries. The retrieve list of fields is then transferred to the next component, using a
connection flow (Main row).

## tTeradataFastLoadUtility Standard properties

These properties are used to configure tTeradataFastLoadUtility running in the Standard Job framework.

The Standard
tTeradataFastLoadUtility component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-In or Repository.  * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Execution platform | Select the Operating System type you use. |
| Host | Host name or IP address of the database server. |
| Database name | Database name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Script generated folder | Browse your directory and select the destination of the file which will be created. |
| Load file | Browse your directory and select the file from which you want to load data. |
| Field separator | Character, string, or regular expression to separate fields. |
| Error file | Browse your directory and select the destination of the file where the error messages will be recorded. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Define character set | Specify the character encoding you need use for your system. |
| Check point | Enter the check point value. |
| Error files | Enter the file name where the error messages are stored. By default, the code ERRORFILES table\_ERR1, table\_ERR2 is entered, meaning that the two tables *table\_ERR1* and *table\_ERR2* are used to record the error messages. |
| Return fastload error | Select this check box to specify the exit code number to indicate the point at which an error message should display in the console. |
| ERRLIMIT | Enter the limit number of errors detected during the loading phase. Processing stops when the limit is reached.  The default error limit value is 1000000.  For more information, see *Teradata FastLoad Reference* documentation. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query and covers all possible SQL queries. |
