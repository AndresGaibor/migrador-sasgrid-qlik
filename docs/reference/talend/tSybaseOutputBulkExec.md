<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybaseoutputbulkexec · versión 8.0 -->
# tSybaseOutputBulkExec

Last updated: 9/30/2026

Gains in performance during Insert operations to a Sybase database.

The tSybaseOutputBulk and tSybaseBulkExec components are generally used together as parts of a two
step process. In the first step, an output file is generated. In the second step, this
file is used in the INSERT operation used to feed a database. These two steps are fused
together in the tSybaseOutputBulkExec component.

## tSybaseOutputBulkExec Standard properties

These properties are used to configure tSybaseOutputBulkExec running in the Standard Job framework.

The Standard
tSybaseOutputBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| DB Version | Select the version of the Sybase database to be used from the drop-down list. |
| Server | Database server IP address  Currently, only *localhost*, *127.0.0.1* or the exact IP address of the local machine is allowed for proper functioning. In other words, the database server must be installed on the same machine where Talend Studio is installed or where the Job using tSybaseOutputBulkExec is deployed. |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Bcp utility | Name of the utility to be used to copy data over to the Sybase server. |
| Batch row number | Number of lines in each processed batch. |
| Table | Name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Clear a table: The table content is deleted. |
| File Name | Name of the file to be generated and loaded.  Information noteWarning: This file is generated on the machine specified by the URI in the Server field so it should be on the same machine as the database server. |
| Append | Select this check box to add the new rows at the end of the records. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use an interface file | Select this check box to specify an interface file in the field Interface file. |
| Additional JDBC parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters. |
| Action on data | On the data of the table defined, you can perform:  Bulk Insert: Add multiple entries to the table. If duplicates are found, job stops.  Bulk Update: Make simultaneous changes to multiple entries. |
| Field terminator | Character, string or regular expression to separate fields.  Information noteWarning: *As a combination of tSybaseOutputBulk and tSybaseBulkExec, this component does not allow the use of Sybase-oriented row/field separators, such as \x09. To achieve the desired effect (for example, displaying fields in the tabular form), you need to use tSybaseOutputBulk and tSybaseBulkExec together to replace tSybaseOutputBulkExec, with \t used in the former component and \x09 used in the latter.* |
| DB Row terminator | String (ex: "\n"on Unix) to distinguish rows in the DB. |
| First row NO. of file | Type in the number of the file row where the action should start at. |
| FILE Row terminator | Character, string or regular expression to separate fields in a file. |
| Include Head | Select this heck box to include the column header. |
| Encoding | Regarding the source data, select the appropriate encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| Sybase encoding type | Select the Sybase-specific encoding type for the data to be processed. This encoding type allows tSybaseOutputBulkExec to properly generate the Sybase Bulk command. |
| Output | Select the type of output for the standard output of the Sybase database:  to console,  to global variable. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | This component requires installation of its related jar files.  The database server/client must be installed on the same machine where Talend Studio is installed or where the Job using tSybaseOutputBulkExec is deployed, so that the component functions properly. |
