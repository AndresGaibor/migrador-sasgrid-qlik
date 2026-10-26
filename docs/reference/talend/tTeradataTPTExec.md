<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatptexec · versión 8.0 -->
# tTeradataTPTExec

Last updated: 9/30/2026

Offers high performance in inserting data from an existing file to a table in a
Teradata database.

As the combination of tTeradataFastLoad, tTeradataMultiLoad, tTeradataTPump,
and tTeradataFastExport, tTeradataTPTExec loads the data from an existing file to a Teradata
database.

## tTeradataTPTExec Standard properties

These properties are used to configure
tTeradataTPTExec running in the Standard Job framework.

The
Standard
tTeradataTPTExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property Type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The database connection related fields that follow are completed   automatically using the data retrieved. |
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
| Load file | Specify the file holding the data to be loaded into the Teradata database. |
| Error file | Specify the file in which log messages will be recorded.  Make sure that the path to the file exists and is accessible to TPT tools. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Custom script | Select this check box to use the customized Teradata TPT script in the directory specified in Path to custom script. * Path to custom   script: Path to the folder where you store the   customized Teradata TPT script. |
| Field separator | Character, string, or regular expression to separate fields. |
| Define Log table | Select this check box to specify a log table so that log messages recorded in the log file will also be written into the log table.  This option is available when `Inserter` is not selected from the Consumer Operator drop-down list in the Basic settings view. |
| Set Script Parameters | Select this check box to define script parameters, which will be used when generating a script during the Job execution. If you do not specify them manually, the system will use their default values.  This field is not available when Custom script is selected. |
| Enforce database name on Log, Work, and Error tables | Select this option to use a database other than the default database for the work table, log table, and the error table.  With this option selected, provide the new database name for the work table, log table, and the error table in the Option attributes table under the Apply TPT consumer operator optional attributes option.  This option is available when `Inserter` is not selected from the Consumer Operator drop-down list in the Basic settings view. |
| Load Operator | Specify the load operator.  This field appears only when the Set Script Parameters check box is selected. |
| Data Connector | Specify the data connector.  This field appears only when the Set Script Parameters check box is selected. |
| Job Name | Specify the name of a Teradata Parallel Transporter Job which is defined using the Teradata *tbuild* command.  For further information about the *tbuild* command, see [tbuild](https://docs.teradata.com/r/yxBNqiK9WZh15WoRzMnBrw/pTFncWq01yte_hXC8TesYQ).  This field appears only when the Set Script Parameters check box is selected. |
| Layout Name (schema) | Specify a schema for the data to be loaded.  This field appears only when the Set Script Parameters check box is selected. |
| Return mload error | Select this check box to specify the exit code number to indicate the point at which an error message should display in the console. |
| Character set encoding of the script | This check box is selected by default, allowing you to specify the encoding to be used in the Teradata TPT script. |
| Character set encoding of the data | Select this check box to specify the encoding to be used for the Teradata TPT data. This field is not available when Custom script is selected. |
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
| **Usage rule** | Used as a single-component Job or subJob, this component offers high performance in inserting data from an existing file to a table in the Teradata database. For further information about the usage of this component, see [tbuild](https://docs.teradata.com/r/yxBNqiK9WZh15WoRzMnBrw/pTFncWq01yte_hXC8TesYQ). |
| Limitation | The Teradata client tool with the Teradata Parallel Transporter Base and Teradata Parallel Transporter Stream features needs to be installed on the machine where Jobs using this component are executed. |

**Related concepts**  

* [Loading data into a Teradata database](tteradatatptexec-tteradatainput-tlogrow-loading-data-into-teradata-database-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatptexec-tteradatainput-tlogrow-loading-data-into-teradata-database-standard-component-this -->
# Loading data into a Teradata database

Last updated: 9/30/2026

This scenario describes a Job that creates a new Teradata database table, writes data
into a delimited file, then loads the data from the file into this table, and finally
retrieves the data from the table and displays it on the console.

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/teradata/tteradatatptexec-tteradatainput-tlogrow-dropping-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/teradata/tteradatatptexec-tteradatainput-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/teradata/tteradatatptexec-tteradatainput-tlogrow-saving-and-executing-job-standard-component-press)

**Related concepts**  

* [tTeradataInput](tteradatainput "Executes a DB query with a strictly defined order which must correspond to the schema definition.")

**Related reference**  

* [tTeradataTPTExec](tteradatatptexec "Offers high performance in inserting data from an existing file to a table in a Teradata database.")
* [tTeradataRow](tteradatarow "Acts on the actual DB structure or on the data (although without handling data).")

**Related information**  

* [tFileOutputDelimited](/talend/en-US/components/8.0/delimited/tfileoutputdelimited)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatptexec-tteradatainput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

## Creating a new Teradata database table

### Procedure

1. Double-click tTeradataRow to open its
   Basic settings view.
2. Fill in the Host, Database, Username, and
   Password fields with your Teradata
   database connection details.
3. In the Query field, enter the
   following SQL statement to create a new table named `person` with
   three columns `id`, `name`,
   `sex`.

   ```
   CREATE SET TABLE samples.person,
                 FALLBACK,
                 NO BEFORE JOURNAL,
                 NO AFTER JOURNAL
                 (
                 id INTEGER NOT NULL,
                 name VARCHAR(50),
                 sex VARCHAR(20)
                 )
                 UNIQUE PRIMARY INDEX (id)
   ```

## Preparing the source data

### Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit schema to open the schema editor.
3. Click the [+] button to add
   three columns: `id` of the integer type,
   `name` and `sex` of the string type.
4. Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
5. In the Mode area, select Use Inline Content (delimited file) and enter the
   input data in the Content field.

   ```
   1;Ford;Male
                 2;Rose;Female
                 3;Sabrina;Female
                 4;Teddy;Male
                 5;Kate;Male
   ```
6. Double-click tFileOutputDelimited to open
   its Basic settings view.
7. In the File Name field,
   specify the file into which the input data will be written. In this example, it is
   E:/person.csv.

## Loading the source data into an empty table

### Procedure

1. Double-click tTeradataTPTExec to open its Basic settings view.
2. Fill in the TDPID, Database name, Username,
   and Password fields with your Teradata
   database connection details.
3. In the Table field, enter the
   name of the table into which the source data will be loaded. In this example, it is
   `person`.
4. In the Script generated folder
   field, browse to the directory under which the Teradata Parallel Transporter script file
   will be created during the Job execution. 

   In this example, it is E:/.
5. In the Load file field, browse
   to the file that contains the source data. In this example, it is
   E:/person.csv.
6. In the Error file field,
   specify the file in which log messages will be recorded. In this example, it is
   E:/error.log.
7. Click the [...] button next to Edit schema to open the schema editor.

   Click the [+] button to add
   three columns: `id` of the integer type,
   `name` and `sex` of the string type. Note
   that `id` and `name` in Db Column are enclosed in a pair of *\"* since they are Teradata database keywords.

   Click OK to validate these changes and
   close the schema editor.
8. Click Advanced settings to open its view,
   and then select the Apply TPT consumer operator
   optional attributes check box and click the [+] button below the Optional attributes table to add the following attributes
   needed: ErrorLimit, ErrorTable1, QueryBandSessInfo, and TraceLevel.

   Information noteNote:

   For VARCHAR attributes, enter their values between double quotation
   marks.

## Retrieving data from the Teradata database table

### Procedure

1. Double-click tTeradataInput to open its
   Basic settings view.
2. In the Table Name field, enter
   the name of the table to read data from. In this example, it is
   `person`.
3. In the Query field, enter the following
   SQL statement to retrieve data from the table *person*.

   ```
   SELECT * FROM samples.person ORDER BY id
   ```
4. Click the [...] button next to Edit schema to open the schema editor.
5. Click the [+] button to add
   three columns: `id` of the integer type,
   `name` and `sex` of the string type. Note
   that `id` and `name` in Db Column are enclosed in a pair of *\"* since they are Teradata database keywords.
6. Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
7. Double-click tLogRow to open its
   Basic settings view.
8. In the Mode area, select the Table (print values in cells of a table) option
   for a better display of the result.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatptexec-tteradatainput-tlogrow-dropping-and-linking-components-standard-component-create -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their
   names in the design workspace or dropping them from the Palette:

   * a tTeradataRow component,
   * a tFixedFlowInput component,
   * a tFileOutputDelimited component,
   * a tTeradataTPTExec component,
   * a tTeradataInput component,
   * and a tLogRow component.
2. Connect tFixedFlowInput to tFileOutputDelimited using a Row > Main
   connection.
3. Do the same to connect tTeradataInput to
   tLogRow.
4. Connect tTeradataRow to tFixedFlowInput using a Trigger > On Subjob Ok
   connection.
5. Do the same to connect tFixedFlowInput to tTeradataTPTExec and tTeradataTPTExec to tTeradataInput.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradatatptexec-tteradatainput-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save the
   Job.
2. Press F6 to execute the Job.

   The data written into the specified Teradata database table is displayed
   on the console.
