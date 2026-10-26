<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sybase/tsybaseiqbulkexec · versión 8.0 -->
# tSybaseIQBulkExec

Last updated: 9/30/2026

Information noteImportant: Support for Sybase 12 through 15 is removed from 8.0.1-R2024-12 onwards. Use Sybase 16 instead.

Loads data into a Sybase database table from a flat file or other database
table.

## tSybaseIQBulkExec Standard properties

These properties are used to configure tSybaseIQBulkExec
running in the Standard Job framework.

The Standard
tSybaseIQBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  When reusing an existing Sybase 16 (SQL Anywhere) connection created by a tSybaseConnection component and loading data from a file located on the client side, you need to select Sybase 16 (SQL Anywhere) from the DB Version drop-down list to display the Is client file check box before selecting this check box.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection).  This property is not available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| DB Version | Select the version of the Sybase database to be used from the drop-down list.   * For Sybase IQ 12 and Sybase IQ 16, the file to be bulk-loaded must be located on   the same machine as the Sybase IQ server. * For Sybase IQ 15, the file to be bulk-loaded can be located on the client side,   however, this means certain setup on the Sybase IQ server. For more information, see   [Sybase IQ client-side load support   enhancements](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc00787.0480/html/etl_nfg/CHDEIAJG.htm). * For Sybase 16 (SQL Anywhere), the file to be bulk-loaded can be located on both the   server side and the client side.  Before loading data into Sybase 16 (SQL Anywhere), SQL Anywhere 17 must be   installed. You can download it [here](https://archive.sap.com/documents/docs/DOC-35857). Once the installation is done, you need to check the system   variable `Path` to make sure the installation path of   SQL Anywhere 17 has been added to it, and then restart Talend Studio (in certain case restart the computer) to have the new   `Path` variable take effect. |
| Host | The IP address or hostname of the database.  This property is not available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| Port | The listening port number of the database.  This property is not available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| Data Source | Select the type of the data source to be used and complete the corresponding DSN information in the field alongside. The available types are `DSN` and `FILEDSN`.  When `FILEDSN` is selected, a [...] button is available next to the Data Source field to allow you to browse to the data source file of interest.  This property is available when `Sybase IQ 15` is selected from the DB Version drop-down list. |
| Database | Enter the name of the database. |
| Sybase Schema | The schema of the database. |
| Username and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | The name of the table to be written. |
| Action on table | On the table defined, you can perform one of the following operations:   * Default:   No operation is carried out. * Drop and create   table: The table is removed and created   again. * Create   table: The table does not exist and gets   created. * Create table if does   not exist: The table is created if it does not   exist. * Drop table if exists   and create: The table is removed if it already   exists and created again. * Clear   table: The table content is deleted. * Truncate   table: The table content is deleted. You do not   have the possibility to rollback the operation. |
| Local filename | The path to the file to be loaded. |
| Is client file | Select this check box if you need to load data from the client side.  This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Use Insert-Location | Select this check box and specify the source database table from which data will be imported into the Sybase table.  This option is not supported for Sybase v16.x (Sybase SQL Anywhere) and above. |
| Server | The name of the server that stores data to be imported.  This property is available only when the Use Insert-Location check box is selected. |
| Database | The name of the database that stores data to be imported.  This property is available only when the Use Insert-Location check box is selected. |
| Schema | The name of the source schema.  This property is available only when the Use Insert-Location check box is selected. |
| Table | The name of the source table.  This property is available only when the Use Insert-Location check box is selected. |
| Use Source Filter | Select this check box and specify the row filter on the source table.  This property is available only when the Use Insert-Location check box is selected. |
| Where Clause | The where clause to filter the rows you want to import into the Sybase table.  This property is available only when the Use Source Filter check box is selected. |
| Columns Mapping | Complete this table to specify the mapping relationship between the source table columns and the Sybase table columns.   * Column:   the name of the Sybase table column. By default, the fields in   the Column column are   same as what they are in the schema. * Columns in Source   Table: the name of the corresponding column in   the table from which the data will be imported.   This property is available only when the Use Insert-Location check box is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| Lines terminated by | The character or sequence of characters used to separate lines.  This property is not available when the Use Insert-Location check box is selected. |
| Fields terminated by | The character, string or regular expression used to separate fields.  With the row/field separators compliant with the Sybase syntax, this component allows the use of Sybase-oriented separators, such as *\x09*.  This property is not available when the Use Insert-Location or Use fixed length check box is selected. |
| Use enclosed quotes | Select this check box to use data enclosure characters.  This property is not available when the Use Insert-Location or Use fixed length check box is selected. |
| Use fixed length | Select this check box to set a fixed width for data lines.  This property is not available when the Use Insert-Location check box is selected. |
| Include Header | Select this check box if the file that will be loaded includes header.  This property is not available when the Use Insert-Location check box is selected. |
| Blank as null | Select this check box to store the input zero-length varchars as NULLs instead of blanks in the database during the load operation.  This property is not available when the Use Insert-Location or Use fixed length check box is selected. |
| On file error | Select the action Sybase performs when an error occurs:   * Rollback (default): rolls back the entire transaction. * Finish: finishes the insertions already completed and ends   the load operation. * Continue: skips the error and continues the load   operation.   This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Message log file | The path to the MESSAGE LOG file that saves the log information about integrity constraint violations, the types of violations, etc. It must be specified together with the Row log file property.  This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Row log file | The path to the ROW LOG file that saves the log information about reject data, the timestamps of the start and completion of the load, etc. It must be specified together with the Message log file property.  This property is available when `Sybase 16 (SQL Anywhere)` is selected from the DB Version drop-down list. |
| Location Options | Select this check box to display the location options. For more information about the location options, see <http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc00801.1510/html/iqrefso/X315746.htm>.  This property is available only when the Use Insert-Location check box is selected. |
| Encrypted Password | Select this check box to specify the use of Open Client Library default password encryption when connecting to the remote source server.  This property is available only when the Location Options check box is selected. |
| Use TDS Packet Size | Select this check box and in the Packet Size field displayed specify the TDS packet size in bytes.  This property is available only when the Location Options check box is selected. |
| Quoted Identifier | Select this check box and from the Status drop-down list displayed specify the setting of the QUOTED\_IDENTIFIER option on the remote server.  This property is available only when the Location Options check box is selected. |
| Set Isolation Level | Select this check box and from the Isolation Level drop-down list displayed select the isolation level for the connection to the remote server.  This property is available only when the Location Options check box is selected. |
| Insert Load Options | Select this check box to display the insert load options. For more information about the insert load options, see <http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc00801.1510/html/iqrefso/X315746.htm>.  This property is available only when the Use Insert-Location check box is selected. |
| Limit Number | Specify the maximum number of rows to be inserted into the Sybase IQ table.  This property is available only when the Insert Load Options check box is selected. |
| Notify Number | Specify that you will be notified with a message each time the number of rows are successfully inserted into the Sybase IQ table.  This property is available only when the Insert Load Options check box is selected. |
| Skip Number | Specify the number of rows to be skiped at the beginning of the source table.  This property is available only when the Insert Load Options check box is selected. |
| Start Row ID | Specify the ID of the row in the Sybase IQ table where you want to start the insert.  Information noteNote: Sybase IQ 16 doesn't support this parameter.  This property is available only when the Insert Load Options check box is selected. |
| Insert Select Load Options | Select this check box to display the insert select load options. For more information about the insert select load options, see <http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc00801.1510/html/iqrefso/X315750.htm>.  This property is available only when the Use Insert-Location check box is selected. |
| Word Skip Number | Enter the number of times the error *Words exceeding the maximum permitted word length not supported* is ignored when loading data into the Sybase IQ table.  This property is available only when the Insert Select Load Options check box is selected. |
| Ignore Constraint | Select this check box and in the table displayed you can specify the integrity constraint violation to ignore when loading data into the Sybase IQ table by clicking the [+] button to add as many rows as needed, each row for a constraint violation, and setting the value of the following columns for each constraint violation:   * Constraint Type: Click   the cell and from the drop-down list displayed select the type   of the constraint violation to ignore. * Number: Enter the   maximum number of the constraint violation to ignore before   initiating a rollback during a load.   This property is available only when the Insert Select Load Options check box is selected. |
| Log In File | Select this check box if you want to log the constraint violation information in files.  This property is available only when the Insert Select Load Options check box is selected. |
| Message Log | Specify the path to the MESSAGE LOG file.  This property is available only when the Log In File check box is selected. |
| Row Log | Specify the path to the ROW LOG file.  This property is available only when the Log In File check box is selected. |
| Log Delimited By | Specify the separator between data values in the ROW LOG file.  This property is available only when the Log In File check box is selected. |
| Log Filter | Select this check box and from the Only Log drop-down list displayed select the type of the constraint violation information to be logged.  This property is available only when the Log In File check box is selected. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
