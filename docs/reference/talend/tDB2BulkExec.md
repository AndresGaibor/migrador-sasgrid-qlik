<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/db2/tdb2bulkexec · versión 8.0 -->
# tDB2BulkExec

Last updated: 9/30/2026

Executes the Insert action on the provided data and gains in performance during
Insert operations to a DB2 database.

## tDB2BulkExec Standard properties

These properties are used to configure tDB2BulkExec running in the Standard Job framework.

The Standard
tDB2BulkExec component belongs to the Databases family.

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
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Table Schema | Name of the DB schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-in: You create the schema   and store it locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository, hence can reuse   it. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Use Ingest Command | Select this check box to populate data into DB2 using the INGEST command. For more information about the INGEST command, see <http://www.ibm.com/developerworks/data/library/techarticle/dm-1304ingestcmd> and <https://www-01.ibm.com/support/knowledgecenter/SSEPGG_10.1.0/com.ibm.db2.luw.admin.cmd.doc/doc/r0057198.html?cp=SSEPGG_10.1.0%2F3-5-2-4-59>. |
| Load From | Select the source of the data to be populated.   * FILE: loads data from a   file. * PIPE: loads data from a   pipe. * FOLDER: loads data from   multiple files in a folder.   This list is available only when the Use Ingest Command check box is selected. |
| Data File | Name of the file to be loaded. Information noteNote: This file is located on the machine specified by the URI in the Host field so it should be on the same machine as the database server.  This field is not visible when PIPE or FOLDER is selected from the Load From drop-down list. |
| Data File/Named Pipe | Name of the file or the named pipe to load data from. This component supports data file and named pipe when loading data into DB2 tables. It loads data using the LOAD command by calling the DB2 system procedure SYSPROC.ADMIN\_CMD. For more information, see [LOAD command using the ADMIN\_CMD procedure](https://www.ibm.com/docs/en/db2/10.5?topic=commands-load-using-admin-cmd#:~:text=LOAD%20command%20using%20the%20ADMIN_CMD%20procedure%20Efficiently%20loads,the%20data%20is%20loaded%20into%20the%20DB2%20table).  Information noteNote:  * The file is located on the machine specified by the URI in the Host field so it should be on the same   machine as the database server. * Make sure the named pipe is a server-side named pipe. That is, it needs to   be configured on the target server.  This field is not visible when Use Ingest Command is selected. |
| Pipe Name | Enter the name of the pipe.  This field is available only when PIPE is selected from the Load From drop-down list. |
| Folder | Specify the path to the folder holding the files to be loaded.  This field is available only when FOLDER is selected from the Load From drop-down list. |
| Action on Data | On the data of the table defined, you can perform one of the following operations:  * Insert: Add new   records to the table. If duplicates are found, Job   stops. * Replace: Add new   records to the table. If an old record in the table has   the same value as a new record for a PRIMARY KEY or a   UNIQUE index, the old record is deleted before the new   record is inserted. * Update: Make changes   to existing records. * Delete: Remove the   records that match the input data. * Merge: Merge the   input data to the table.  Delete and Merge are available only when the Use Ingest Command check box is selected. |
| File Glob Pattern | Specify the global expression for the files to be loaded.  This field is available only when FOLDER is selected from the Load From drop-down list. |
| Where Clause | Enter the WHERE clause to filter the data to be processed.  This field is available only when update or delete is selected from the Action on Data drop-down list. |
| Custom Insert Values Clause | Select this check box and in the Insert Values Clause field displayed enter the VALUES clause for the insert operation.  This check box is available only when the Use Ingest Command check box is selected and insert is selected from the Action on Data drop-down list. |
| Custom Update Set Clause | Select this check box and specify the SET clause for the update operation by completing the Set Mapping table.  This check box is available only when the Use Ingest Command check box is selected and update is selected from the Action on Data drop-down list. |
| Set Mapping | Complete this table to specify the SET clause for the update operation.   * Column: the name of the   column. By default, the fields in the Column column are same as what they are in   the schema. * Expression: the   expression for the corresponding column.   This table is available only when the Custom Update Set Clause check box is selected. |
| Merge Clause | Specify the MERGE clause for the merge operation.  This table is available only when the Use Ingest Command check box is selected and merge is selected from the Action on Data drop-down list. |
| Content Format | Select the format of the input file, either Delimited or Positional.  This list is available only when the Use Ingest Command check box is selected. |
| Delimited By | Enter the character that separates the fields in the delimited file.  This field is available only when Delimited is selected from the Content Format drop-down list. |
| Optionally Enclosed By | Enter the character that encloses the string in the delimited file.  This field is available only when Delimited is selected from the Content Format drop-down list. |
| Fixed Length | Enter the length (in bytes) of the record in the positional file.  This field is available only when Positional is selected from the Content Format drop-down list. |
| Mapping | Complete this table to specify the mapping relationship between the source column and the DB2 table column.   * Column: the name of the   column. By default, the fields in the Column column are same as what they are in   the schema. * Is Table Column: select   the check box if the corresponding column is a table   column. * Start Position: the   starting position of the corresponding column. * End Position: the ending   position of the corresponding column.  The Start Position and   End Position columns   are available only when Positional is selected from the Content Format drop-down   list.   This table is available only when the Use Ingest Command check box is selected. |
| Script Generated Folder | Specify the directory under which the script file will be created.  This field is available only when the Use Ingest Command check box is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating.  Information noteNote: You can set the encoding parameters through this field. |
| Field terminated by | Character, string or regular expression to separate fields. |
| Date Format | Use this field to define the way months and days are ordered. |
| Time Format | Use this field to define the way hours, minutes and seconds are ordered. |
| Timestamp Format | Use this field to define the way date and time are ordered. |
| Remove load pending | When the box is ticked, tables blocked in "pending" status following a bulk load are de-blocked. |
| Load options | Click + to add data loading options:  Parameter: select a loading parameter from the list.  Value: enter a value for the parameter selected. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_DELETED: the number of rows deleted. This is an After variable and it returns an integer.  QUERY: the query statement processed. This is an After variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This dedicated component offers performance and flexibility of DB2 query handling. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
