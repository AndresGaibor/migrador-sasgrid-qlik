<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/netezza/tnetezzanzload · versión 8.0 -->
# tNetezzaNzLoad

Last updated: 9/30/2026

Inserts data into a Netezza database table using Netezza's nzload
utility.

tNetezzaNzLoad bulk loads data into a Netezza table
either from an existing data file, an input flow, or directly from a data flow in streaming
mode through a named-pipe.

## tNetezzaNzLoad Standard properties

These properties are used to configure tNetezzaNzLoad running in the Standard Job framework.

The Standard
tNetezzaNzLoad component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Host | Database server IP address. |
| Port | Listening port number of the DB server. |
| Database | Name of the Netezza database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table into which the data is to be inserted. |
| Action on table | On the table defined, you can perform one of the following operations before loading the data:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted before the data is loaded.  Truncate table: executes a truncate statement prior to loading the data to clear the entire content of the table. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Data file | Full path to the data file to be used. If this component is used on its own (not connected to another component with input flow) then this is the name of an existing data file to be loaded into the database. If it is connected, with an input flow to another component; this is the name of the file to be generated and written with the incoming data to later be used with nzload to load into the database. |
| Use named-pipe | Select this check box to use a named-pipe instead of a data file. This option can only be used when the component is connected with an input flow to another component. When the check box is selected, no data file is generated and the data is transferred to nzload through a named-pipe. This option greatly improves performance in both Linux and Windows.    Information noteNote: This component on named-pipe mode uses a JNI interface to create and write to a named-pipe on any Windows platform. Therefore the path to the associated JNI DLL must be configured inside the java library path. The component comes with two DLLs for both 32 and 64 bit operating systems that are automatically provided in Talend Studio with the component. |
| Named-pipe name | Specify a name for the named-pipe to be used. Ensure that the name entered is valid. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| Use existing control file | Select this check box to provide a control file to be used with the nzload utility instead of specifying all the options explicitly in the component. When this check box is selected, Data file and the other nzload related options no longer apply. Please refer to Netezza's nzload manual for details on creating a control file.  Information noteNote: The global variable `NB_LINE` is not supported when any control file is being used. |
| Control file | Enter the path to the control file to be used, between double quotation marks, or click [...] and browse to the control file. This option is passed on to the nzload utility via the *-cf* argument. |
| Field separator | Character, string or regular expression used to separate fields.  Information noteWarning: *This is nzload's delim argument. If you do not use the Wrap quotes around fields option, you must make sure that the delimiter is not included in the data that's inserted to the database. The default value is \t or TAB. To improve performance, use the default value.* |
| Wrap quotes around fields | This option is only applied to columns of *String*, *Byte*, *Byte[]*, *Char*, and *Object* types. Select either:  None: do not wrap column values in quotation marks.  Single quote: wrap column values in single quotation marks.  Double quote: wrap column values in double quotation marks.  Information noteWarning: *If using the Single quote or Double quoteoption, it is necessary to use \ as the Escape char.* |
| Advanced options | Set the nzload arguments in the corresponding table. Click [+] as many times as required to add arguments to the table. Click the Parameter field and choose among the arguments from the list. Then click the corresponding Value field and enter a value between quotation marks.  For details about the available parameters, see [Parameters](tnetezzanzload). |
| Encoding | Select the encoding type from the list. |
| Specify nzload path | Select this check box to specify the full path to the nzload executable. You must check this option if the nzload path is not specified in the PATH environment variable. |
| Full path to nzload executable | Full path to the nzload executable on the machine in use. It is advisable to specify the nzload path in the PATH environment variable instead of selecting this option. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  Information noteWarning: * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when non particular transformation is required on the data to be loaded ont to the database.  This component can be used as a standalone or an output component. |

## Parameters

The following table lists the parameters you can use in the Advanced options table in the Advanced settings tab.

| -If | Name of the log file to generate. The logs will be appended if the log file already exists. If the parameter is not specified, the default name for the log file is '*<table\_name>.<db\_name>.nzlog*'. And it's generated under the current working directory where the job is running. |
| -bf | Name of the bad file to generate. The bad file contains all the records that could not be loaded due to an internal Netezza error. The records will be appended if the bad file already exists. If the parameter is not specified, the default name for the bad file is '*<table\_name>.<db\_name>.nzbad*'. And it's generated under the current working directory where the job is running. |
| -ouputDir | Directory path to where the log and the bad file are generated. If the parameter is not specified the files are generated under the current directory where the Job is currently running. |
| -logFileSize | Maximum size for the log file. The value is in MB. The default value is 2000 or 2GB. To save hard disk space, specify a smaller amount if your Job runs often. |
| -compress | Specify this option if the data file is compressed. Valid values are "`TRUE`" or "`FALSE`". Default value if "`FALSE`".  This option is only valid if this component is used by itself and not connected to another component via an input flow. |
| -skipRows <n> | Number of rows to skip from the beginning of the data file. Set the value to "1" if you like to skip the header row from the data file. The default value is "0".  This option should only be used if this component is used by itself and not connected to another component via an input flow. |
| -maxRows <n> | Maximum number of rows to load from the data file.  This option should only be used if this component is used by itself and not connected to another component via an input flow. |
| -maxErrors | Maximum number of error records to allow before terminating the load process. The default value is "1". |
| -ignoreZero | Binary zero bytes in the input data will generate errors. Set this option to "NO" to generate error or to "YES" to ignore zero bytes. The default value is "NO". |
| -requireQuotes | This option requires all the values to be wrapped in quotes. The default value is "FALSE".  This option currently does not work with input flow. Use this option only in standalone mode with an existing file. |
| -nullValue <token> | Specify the token to indicate a null value in the data file. The default value is "NULL". To improve slightly performance you can set this value to an empty field by specifying the value as single quotes: "\'\'". |
| -fillRecord | Treat missing trailing input fields as null. You do not need to specify a value for this option in the value field of the table. This option is not turned on by default, therefore input fields must match exactly all the columns of the table by default.  Trailing input fields must be nullable in the database. |
| -ctrlChar | Accept control chars in char/varchar fields (must escape NUL, CR and LF). You do not need to specify a value for this option in the value field of the table. This option is turned off by default. |
| -ctInString | Accept un-escaped CR in char/varchar fields (LF becomes only end of row). You do not need to specify a value for this option in the value field of the table. This option is turned off by default. |
| -truncString | Truncate any string value that exceeds its declared char/varchar storage. You do not need to specify a value for this option in the value field of the table. This option is turned off by default. |
| -dateStyle | Specify the date format in which the input data is written in. Valid values are: "YMD", "Y2MD", "DMY", "DMY2", "MDY", "MDY2", "MONDY", "MONDY2". The default value is "YMD".  The date format of the column in the component's schema must match the value specified here. For example if you want to load a DATE column, specify the date format in the component schema as "yyyy-MM-dd" and the -dateStyle option as "YMD".  For more description on loading date and time fields, see [Loading DATE, TIME and TIMESTAMP columns](tnetezzanzload). |
| -dateDelim | Delimiter character between date parts. The default value is "-" for all date styles except for "MONDY[2]" which is " " (empty space).  The date format of the column in the component's schema must match the value specified here. |
| -y2Base | First year expressible using two digit year (Y2) dateStyle. |
| -timeStyle | Specify the time format in which the input data is written in. Valid values are: "24HOUR" and "12HOUR". The default value is "24HOUR". For slightly better performance you should keep the default value.  The time format of the column in the component's schema must match the value specified here. For example if you want to load a TIME column, specify the date format in the component schema as "HH:mm:ss" and the -timeStyle option as "24HOUR".  For more description on loading date and time fields, see [Loading DATE, TIME and TIMESTAMP columns](tnetezzanzload). |
| -timeDelim | Delimiter character between time parts. The default value is ":".  Information noteNote: The time format of the column in the component's schema must match the value specified here. |
| -timeRoundNanos | Allow but round non-zero digits with smaller than microsecond resolution. |
| -boolStyle | Specify the format in which Boolean data is written in the data. The valid values are: "1\_0", "T\_F", "Y\_N", "TRUE\_FALSE", "YES". The default value is "1\_0". For slightly better performance keep the default value. |
| -allowRelay | Allow load to continue after one or more SPU reset or failed over. The default behaviour is not allowed. |
| -allowRelay <n> | Specify number of allowable continuation of a load. Default value is "1". |

## Loading DATE, TIME and TIMESTAMP columns

When this component is used with an input flow, the date format specified inside
the component's schema must match the value specified for -dateStyle, -dateDelim,
-timeStyle, and -timeDelim options.

| DB Type | Schema date format | -dateStyle | -dateDelim | -timeStyle | -timeDelim |
| --- | --- | --- | --- | --- | --- |
| DATE | "yyyy-MM-dd" | "YMD" | "-" | n/a | n/a |
| TIME | "HH:mm:ss" | n/a | n/a | "24HOUR" | ":" |
| TIMESTAMP | "yyyy-MM-dd HH:mm:ss" | "YMD" | "-" | "24HOUR" | ":" |
