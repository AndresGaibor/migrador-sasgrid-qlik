<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatafastexport · versión 8.0 -->
# tTeradataFastExport

Last updated: 9/30/2026

Exports data batches from a Teradata table to a customer system or to a smaller
database.

tTeradataFastExport exports rapidly
voluminous data batches from a Teradata table or view.

## tTeradataFastExport Standard properties

These properties are used to configure tTeradataFastExport running in the Standard
Job framework.

The Standard
tTeradataFastExport component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Use Commandline | Select this check box to enable the Talend CommandLine mode. |
| Use Java API | Select this check box to enable the Java API mode. |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Execution platform | Select the Operating System type you use.  Available in the Use Commandline mode. |
| Host | Server name or IP. |
| Database name | Database name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Use query | Select this check box to show the Query box where you can enter the SQL statement.  Available in the Use Commandline mode. |
| Query | Enter the SQL statement in the Query box. |
| Log database | Log database name.  Available in the Use Commandline mode. |
| Log table | Log table name.  Available in the Use Commandline mode. |
| Script generated folder | Browse your directory and select the destination of the file which will be created.  Available in the Use Commandline mode. |
| Exported file | Name and path to the file which will be created. |
| Field separator | Character, string, or regular expression to separate fields. |
| Row separator | String (e.g.: "\n"on Unix) to separate rows.  Available in the Use Java API mode. |
| Error file | Browse your directory and select the destination of the file where the error messages will be recorded.  Available in the Use Commandline mode. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Create directories if do not exist | Select this option to have the directories specified in the Basic settings view created before generating files in them if the directories do not exist. |
| Die When Unnormal Terminated | Select this option to stop the execution of the Job when the operation is terminated unexpectedly. |
| Advanced separator (for number) | Select this option to insert thousands separators and decimal separators for numbers. You can set thousands separator and decimal separator in the fields to the right.  This option is available when Use Java API is selected in the Basic settings view. |
| Include Header | Select this option to insert header line in the output data.  This option is available when Use Java API is selected in the Basic settings view. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all possible SQL queries. |
| Limitation | If you have selected the Use Commandline mode, you need to install the Teradata client on the machine where there is the Job that involves this component. |
