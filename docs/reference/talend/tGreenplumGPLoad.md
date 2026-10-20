<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/greenplum/tgreenplumgpload · versión 8.0 -->
# tGreenplumGPLoad

Last updated: 9/30/2026

Bulk loads data into a Greenplum table either from an existing data file, an input
flow, or directly from a data flow in streaming mode through a named-pipe.

tGreenplumGPLoad inserts data
into a Greenplum database table using Greenplum's gpload
utility.

## tGreenplumGPLoad Standard properties

These properties are used to configure tGreenplumGPLoad running in the Standard Job framework.

The Standard
tGreenplumGPLoad component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | Either Built-in or Repository .   * Built-in: No property data stored centrally. * Repository: Select the repository file in which the properties are stored. The fields that follow are completed automatically using the data retrieved. |
| Host | Database server IP address. |
| Port | Listening port number of the DB server. |
| Database | Name of the Greenplum database. |
| Schema | Exact name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table into which the data is to be inserted. |
| Action on table | On the table defined, you can perform one of the following operations before loading the data:  None: No operation is carried out.  Clear table: The table content is deleted before the data is loaded.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop and create table: The table is removed and created again.  Drop table if exists and create: The table is removed if it already exists and created again.  Truncate table: The table content is deleted. You do not have the possibility to rollback the operation. |
| Action on data | On the data of the table defined, you can perform:  Insert: Add new entries to the table. If duplicates are found, Job stops.  Update: Make changes to existing entries.  Merge: Updates or adds data to the table.  Information noteWarning: *It is necessary to specify at least one column as a primary key on which the Update and Merge operations are based. You can do that by clicking Edit Schema and selecting the check box(es) next to the column(s) you want to set as primary key(s). To define the Update/Merge options, select in the Match Column column the check boxes corresponding to the column names that you want to use as a base for the Update and Merge operations, and select in the Update Column column the check boxes corresponding to the column names that you want to update. To define the Update condition, type in the condition that will be used to update the data.* |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Data file | Full path to the data file to be used. If this component is used in standalone mode, this is the name of an existing data file to be loaded into the database. If this component is connected with an input flow, this is the name of the file to be generated and written with the incoming data to later be used with gpload to load into the database. This field is hidden when the Use named-pipe check box is selected. |
| Populate column list based on the schema | Select this option to add the columns defined in the schema to the YAML file. This is extremely useful if the target table has extra columns (for example, to load only the primary keys to a staging table.) Selecting this option generates the COLUMNS: section in the YAML file. |
| Use named-pipe | Select this check box to use a named-pipe. This option is only applicable when the component is connected with an input flow. When this check box is selected, no data file is generated and the data is transferred to gpload through a named-pipe. This option greatly improves performance in both Linux and Windows.  Information noteNote: This component on named-pipe mode uses a JNI interface to create and write to a named-pipe on any Windows platform. There­fore the path to the associated JNI DLL must be con­figured inside the java library path. The component comes with two DLLs for both 32 and 64 bit operating systems that are automatically provided in Talend Studio with the component. |
| Named-pipe name | Specify a name for the named-pipe to be used. Ensure that the name entered is valid. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row>Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| DB driver | Select a database driver from the drop-down list: `PostgreSQL`, `Greenplum(Deprecated)`, or `DataDirect`. The default is `PostgreSQL`.  Information noteImportant: The `Greenplum(Deprecated)` driver is deprecated. Migrate to `DataDirect`, a third-party JDBC driver suggested by Greenplum. |
| Additional Parameters | Specify additional parameters for the database connection. |
| Use existing control file (YAML formatted) | Select this check box to provide a control file to be used with the gpload utility instead of specifying all the options explicitly in the component. When this check box is selected, Data file and the other gpload related options no longer apply. Refer to Greenplum's gpload manual for details on creating a control file. |
| Control file | Enter the path to the control file to be used, between double quotation marks, or click [...] and browse to the control file. This option is passed on to the gpload utility via the *-f* argument. |
| CSV mode | Select this check box to include CSV specific parameters such as Escape char and Text enclosure. |
| Field separator | Character, string, or regular expression used to separate fields.  Information noteWarning: *This is gpload's delim argument. The default value is |. To improve performance, use the default value.* |
| Escape char | Character of the row to be escaped. |
| Text enclosure | Character used to enclose text. |
| Header (skips the first row of data file) | Select this check box to skip the first row of the data file. |
| Additional options | Set the gpload arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Click the Parameter field and choose among the arguments from the list. Then click the corresponding Value field and enter a value between quotation marks.   * LOCAL\_HOSTNAME: The host name or IP address of the local machine on which gpload is running. If this machine is configured with multiple network interface cards (NICs), you can specify the host name or IP of each individual NIC to allow network traffic to use all NICs simultaneously. By default, the local machine's primary host name or IP is used. * PORT (gpfdist port): The specific port number that the gpfdist file distribution program should use. You can also specify a PORT\_RANGE to select an available port from the specified range. If both PORT and PORT\_RANGE are defined, then PORT takes precedence. If neither PORT or PORT\_RANGE is defined, an available port between 8000 and 9000 is selected by default. If multiple host names are declared in LOCAL\_HOSTNAME, this port number is used for all hosts. This configuration is desired if you want to use all NICs to load the same file or set of files in a given directory location. * PORT\_RANGE: Can be used instead of PORT (gpfdist port) to specify a range of port numbers from which gpload can choose an available port for this instance of the gpfdist file distribution program. * NULL\_AS: The string that represents a null value. The default is \N (backslash-N) in TEXT mode, and an empty value with no quotation marks in CSV mode. Any source data item that matches this string will be considered a null value. * FORCE\_NOT\_NULL: In CSV mode, processes each specified column as though it were quoted and hence not a NULL value. For the default null string in CSV mode (nothing between two delimiters), this causes missing values to be evaluated as zero-length strings. * ERROR\_LIMIT (2 or higher): Enables single row error isolation mode for this load operation. When enabled and the error limit count is not reached on any Greenplum segment instance during input processing, all good rows will be loaded and input rows that have format errors will be discarded or logged to the table specified in ERROR\_TABLE if available. When the error limit is reached, input rows that have format errors will cause the load operation to abort. Note that single row error isolation only applies to data rows with format errors, for example, extra or missing attributes, attributes of a wrong data type, or invalid client encoding sequences. Constraint errors, such as primary key violations, will still cause the load operation to abort if encountered. When this option is not enabled, the load operation will abort on the first error encountered. * ERROR\_TABLE: When ERROR\_LIMIT is declared, specifies an error table where rows with formatting errors will be logged when running in single row error isolation mode. You can then examine this error table to see error rows that were not loaded (if any). * LOG\_ERRORS: True or False and defaults to `False`. A value of True logs rows with formatting errors internally. See Control File Format > GPLOAD > LOG\_ERRORS section of [gpload](https://gpdb.docs.pivotal.io/6-12/utility_guide/ref/gpload.html) for more information. * MAX\_LINE\_LENGTH: an integer that specifies the maximum length of a line in the XML transformation data passed to gpload. * EXTERNAL\_SCHEMA (\_ext\_stg\_objects): specifies the schema of the external table database objects created by gpload. Enter the name of the schema of the external table in the Value field. See Control File Format > GPLOAD > EXTERNAL section of [gpload](https://gpdb.docs.pivotal.io/6-12/utility_guide/ref/gpload.html) for more information. * PRELOAD\_TRUNCATE, PRELOAD\_REUSE\_TABLES, PRELOAD\_STAGING\_TABLE, and PRELOAD\_FAST\_MATCH: specifies the operations to carry out prior to the load operation. See Control File Format > PRELOAD section of [gpload](https://gpdb.docs.pivotal.io/6-12/utility_guide/ref/gpload.html) for more information. * SQL\_BEFORE LOAD and SQL\_AFTER LOAD: sets the SQL commands to run before and/or after the load operation. See Control File Format > SQL section of [gpload](https://gpdb.docs.pivotal.io/6-12/utility_guide/ref/gpload.html) for more information. |
| Log file | Browse to or enter the access path to the log file in your directory. |
| Encoding | Define the encoding type manually in the field. |
| Specify gpload path | Select this check box to specify the full path to the gpload executable. You must check this option if the gpload path is not specified in the PATH environment variable. |
| Full path to gpload executable | Full path to the gpload executable on the machine in use. It is advisable to specify the gpload path in the PATH environment variable instead of selecting this option. |
| Remove datafile on successful execution | Select this option to remove the datafile generated if the operation completes successfuly. |
| Gzip compress the datafile | Select this option to compress the datafile using Gzip, which saves the disk space by up to 50-90% the original size. However, it increases CPU usage. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  GPLOAD\_OUTPUT: the output information when the gpload utility is the executed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  NB\_LINE\_INSERTED: the number of rows successfully inserted. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows successfully updated. This is an After variable and it returns an integer.  NB\_DATA\_ERRORS: the number of errors occurred. This is an After variable and it returns an integer.  GPLOAD\_STATUS: the status of the load operation. This is an After variable and it returns a string.  GPLOAD\_RUNTIME: the time (in ms) cost by the load operation. This is an After variable of type long.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded on to the database.  This component can be used as a standalone or an output component. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
