<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatptutility · versión 8.0 -->
# tTeradataTPTUtility

Last updated: 9/30/2026

Writes the incoming data to a file and then loads the data from the file to a
Teradata database.

As the combination of tTeradataFastLoad, tTeradataMultiLoad, tTeradataTPump, and tTeradataFastExport, tTeradataTPTUtility writes the incoming data to a
file and then loads the data from the file to a Teradata database.

## tTeradataTPTUtility Standard properties

These properties are used to configure
tTeradataTPTUtility running in the Standard Job framework.

The
Standard
tTeradataTPTUtility component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings Data file

| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The Filename field is completed automatically using   the data retrieved. |
| Filename | Specify the file to save the incoming data. |
| Append | Select this check box to append the incoming data in the file specified in the Filename field. |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The database connection related fields   that follow are completed automatically using the data retrieved. |
| Execution platform | Select the Operating System that will be used to run the Job, either Windows or Unix. |
| TDPID | Specify the Teradata director program identifier. It can be either the name or the IP address of the Teradata database system being accessed. |
| Database name | Specify the name of the Teradata database. |
| Username and Password | Specify the username and the password for the Teradata database authentication.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Information noteNote: Avoid using a Teradata database keyword as a Db Column name in the schema. If you have to, be sure to enclose the column name in a pair of *\"*. For example, when the keyword *id* is used as a database column name, the Db Column should be filled with *\"id\"*.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Consumer Operator | Select a consumer operator from the drop-down list.   * Load: writes data into an empty Teradata table   using the Teradata FastLoad utility protocol. * Inserter: inserts data into Teradata tables   with SQL sessions. * Update: performs Insert, Update, or Delete   operations using the Teradata MultiLoad utility   protocol. * Stream: loads data continuously into Teradata   tables using the Teradata TPump utility.   For more information about Teradata consumer operators, see [Teradata consumer operators](https://docs.teradata.com/reader/j9~8T4F8ZcLkW7Ke0mxgZQ/xK9jh89gpz2RRqnRwV5Deg). |
| Action On Data | Select an action to be performed on the data from the drop-down list.  * Insert: inserts new records to the table.   If duplicates are found, the Job stops. * Update: updates existing records in the   table. * InsertOrUpdate: inserts new records or   updates existing records based on the given reference   key. * Delete: removes records corresponding to   the input flow.  Information noteNote: You must specify at least one column as the primary key on which the Update or Delete operation is based. You can do that by clicking the [...] button next to Edit schema and selecting the check box(es) next to the column(s) you want to set as primary key(s).  This list field appears only when the Update or Stream operator is selected from the Consumer Operator drop-down list. |
| Producer Operator | Select a producer operator from the drop-down list. Currently, only the DataConnector operator is supported.  DataConnector: accesses files either directly or through an access module, and then writes it to the data stream.  For more information about Teradata producer operators, see [Teradata producer operators](https://docs.teradata.com/reader/j9~8T4F8ZcLkW7Ke0mxgZQ/hMTd8FATzhUyis_IGAVB2w). |
| Table | Specify the name of the table to be written into the Teradata database. Note that only one table can be written at a time. |
| Script generated folder | Specify the directory under which the Teradata Parallel Transporter script file will be created during the Job execution. This script file will be deleted at the end of the Job execution. |
| Error file | Specify the file in which log messages will be recorded. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Row separator | Character, string, or regular expression to separate rows. |
| Field separator | Character, string, or regular expression to separate fields. |
| Include header | Select this check box to include the column header to the file. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for database data handling. |
| Set Script Parameters | Select this check box to define script parameters, which will be used when generating a script during the Job execution. If you do not specify them manually, the system will use their default values. |
| Enforce database name on Log, Work, and Error tables | Select this option to use a database other than the default database for the work table, log table, and the error table.  With this option selected, provide the new database name for the work table, log table, and the error table in the Option attributes table under the Apply TPT consumer operator optional attributes option.  This option is available when `Inserter` is not selected from the Consumer Operator drop-down list in the Basic settings view. |
| Load Operator | Specify the load operator.  This field appears only when the Set Script Parameters check box is selected. |
| Data Connector | Specify the data connector.  This field appears only when the Set Script Parameters check box is selected. |
| Job Name | Specify the name of a Teradata Parallel Transporter Job which is defined using the Teradata *tbuild* command.  For further information about the *tbuild* command, see [tbuild](https://docs.teradata.com/r/yxBNqiK9WZh15WoRzMnBrw/pTFncWq01yte_hXC8TesYQ).  This field appears only when the Set Script Parameters check box is selected. |
| Layout Name (schema) | Specify a schema for the data to be loaded.  This field appears only when the Set Script Parameters check box is selected. |
| Define Log table | Select this check box to specify a log table so that log messages recorded in the log file will also be written into the log table.  This option is available when `Inserter` is not selected from the Consumer Operator drop-down list in the Basic settings view. |
| Return mload error | Select this check box to specify the exit code number to indicate the point at which an error message should display in the console. |
| Define character set | Select this check box to specify the character encoding to be used in your system. |
| Apply TPT consumer operator optional attributes | Select this check box to define optional attribute(s) for the consumer operator that you have selected.  For more information about optional attributes of each consumer operator, see [Teradata Parallel Transporter Reference](https://docs.teradata.com/r/yxBNqiK9WZh15WoRzMnBrw/root). |
| Optional attributes | Click the [+] button below the table to add as many rows as needed, each row for an optional attribute, and set the following two parameters for each attribute:   * Name: click the cell and select an optional   attribute from the drop-down list. The list of optional   attributes may vary depending on the consumer operator you have   selected. For details about supported optional attributes for   each consumer operator, see [Supported optional attributes for each consumer operator](/talend/en-US/components/8.0/teradata/supported-optional-attributes-for-each-consumer-operator). * Value: enter the value for the corresponding   optional attribute.   For more information about the attribute value definition, see [Teradata Parallel Transporter Reference](https://docs.teradata.com/r/yxBNqiK9WZh15WoRzMnBrw/root).  This table appears only when the Apply TPT consumer operator optional attributes check box is selected. |
| tStatCatcher Statistics | Select this check box to collect the log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | EXIT\_VALUE: the process exit code. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | Preceded by an input component, tTeradataTPTUtility writes the incoming data to a file and then loads the data from the file to the Teradata Database. High performance is provided during this process. For further information about the usage of this component, see [tbuild](https://docs.teradata.com/r/yxBNqiK9WZh15WoRzMnBrw/pTFncWq01yte_hXC8TesYQ). |
| Limitation | The Teradata client tool with the Teradata Parallel Transporter Base and Teradata Parallel Transporter Stream features needs to be installed on the machine where Jobs using this component are executed. |
