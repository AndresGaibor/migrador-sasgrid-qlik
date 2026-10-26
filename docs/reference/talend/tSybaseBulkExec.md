<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybasebulkexec · versión 8.0 -->
# tSybaseBulkExec

Last updated: 9/30/2026

Gains in performance during Insert operations to a Sybase database.

The tSybaseOutputBulk and tSybaseBulkExec components are generally used together as
parts of a two step process. In the first step, an output file is generated. In the
second step, this file is used in the INSERT operation used to feed a database. These
two steps are fused together in the tSybaseOutputBulkExec component, detailed in a separate section. The
advantage of using two separate components is that the data can be transformed before it
is loaded in the database.

## tSybaseBulkExec Standard properties

These properties are used to configure tSybaseBulkExec running in the Standard Job framework.

The Standard
tSybaseBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| DB Version | Select the version of the Sybase database to be used from the drop-down list. |
| Server | Database server IP address  Available when you select Bulk Update from the Action on data list in the Advanced settings view of tSybaseBulkExec. |
| Port | Listening port number of DB server.  Available when you select Bulk Update from the Action on data list in the Advanced settings view of tSybaseBulkExec. |
| Database | Database name |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Sybase Schema | Name of the database schema you want to use. |
| Bcp Utility | Name of the utility to be used to copy data over to the Sybase server. |
| Server | IP address of the database server for the Bcp utility connection. |
| Batch size | Number of lines in each processed batch. |
| Table | Name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted.  Truncate table: The table content is deleted. You do not have the possibility to rollback the operation. |
| File Name | Name of the file to be loaded.  Information noteWarning: This file should be located on the same machine as the database server. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use an interface file | Select this check box to specify an interface file in the field Interface file. |
| Additional JDBC parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters. |
| Action on data | On the data of the table defined, you can perform:  Bulk Insert: Add multiple entries to the table. If duplicates are found, Job stops.  Bulk Update: Make simultaneous changes to multiple entries. |
| Field Terminator | Character, string or regular expression to separate fields.  Information noteWarning: *With the row/field separators compliant with the Sybase syntax, this component allows for the use of Sybase-orientated characters, such as \x09.* |
| Row Terminator | String (ex: "\n" in Unix) to separate lines. |
| Head row | Number of head lines to be ignored in the beginning of a file. |
| Encoding | Select the encoding from the list, or enter the encoding between double quotes if it does not exist in the list. This field is compulsory for database data handling. |
| Output | Select the type of output for the standard output of the Sybase database:  to console,  to global variable. |
| tStataCatcher statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_DATA: the number of rows read. This is an After variable and it returns an integer.  NB\_LINE\_BAD: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The database server/client must be installed on the same machine where Talend Studio is installed or where the Job using tSybaseBulkExec is deployed, so that the component functions properly.  As opposed to the Oracle dedicated bulk component, no action on data is possible using this Sybase dedicated component.  This component requires installation of its related jar files. |
