<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/vertica/tverticaoutputbulkexec · versión 8.0 -->
# tVerticaOutputBulkExec

Last updated: 9/30/2026

Receives data from a preceding component, writes data into a local file, and
loads data into a Vertica database from the file using the Vertica COPY SQL
statement.

## tVerticaOutputBulkExec Standard properties

These properties are used to configure tVerticaOutputBulkExec running in the Standard Job framework.

The Standard
tVerticaOutputBulkExec component belongs to the Databases family.

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
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  When a Job contains the parent Job and the child Job, if you need to share an existing connection between the two levels, for example, to share the connection created by the parent Job with the child Job, you have to:   1. In the parent level, register the database connection to be shared    in the Basic settings view of the connection    component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the IP address or hostname of the database. |
| Port | Enter the listening port number of the database. |
| DB Name | Enter the name of the database. |
| Schema | Enter the schema of the database. |
| Username and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Action on data | Select an action that will be performed on the data of the table defined.   * Bulk insert: Insert multiple rows into the table at once   instead of doing single row inserts. If duplicates are found, the Job stops. * Bulk update: Make simultaneous updates to multiple rows. |
| Table | Enter the name of the table into which data will be written. |
| Action on table | Select an operation to be performed on the table defined.   * Default: No operation is carried out. * Drop and create table: The table is removed   and created again. * Create table: The table does not exist and   gets created. * Create table if does not exist: The table is   created if it does not exist. * Drop table if exist and create: The table is   removed if it already exists and created again. * Clear table: The table content is   deleted. You have the possibility to rollback the operation. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| File Name | The path to the file to be generated.  This file is generated on the same machine where Talend Studio is installed or where your Job using this component is deployed. |
| Append | Select this check box to add new rows at the end of the file. |
| Use schema columns for Copy | Select this check box to use the column option in the COPY statement so that you can restrict the load to one or more specified columns in the table. For more information, see [the Vertica COPY SQL Statement](https://my.vertica.com/docs/9.0.x/HTML/index.htm#Authoring/SQLReferenceManual/Statements/COPY/COPY.htm). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. This property is not available when the Use an existing connection check box in the Basic settings view is selected. |
| Stream name | The stream name of a load, which helps identify a particular load.  This property is available only when you are using Vertica 6.0 and later. |
| Write to ROS (Read Optimized Store) | Select this check box to store data in a physical storage area, in order to optimize the reading, as the data is compressed and pre-sorted. |
| Exit Job if no row was loaded | The Job automatically stops if no row has been loaded. |
| Missing columns as null | Select this check box to insert NULL values for the missing columns when there is insufficient data to match the columns specified in the schema.  This property is available only when you are using Vertica 6.0 and later. |
| Skip Header | Select this check box and in the field displayed next to it, specify the number of records to skip in the file.  This property is available only when you are using Vertica 6.0 and later. |
| Record terminator | Select this check box and in the field displayed next to it, specify the literal character string used to indicate the end of each record in the file.  This property is available only when you are using Vertica 6.0 and later. |
| Enclosed by character | Select this check box to set the character within which data is enclosed.  This property is available only when you are using Vertica 6.0 and later. |
| Field Separator | The character, string or regular expression to separate fields. |
| Null String | The string displayed to indicate that the value is null. |
| Include Header | Select the check box to include the column header to the file. |
| Encoding | Select an encoding method from the list, or select CUSTOM and define it manually. This field is compulsory for database data handling. |
| Reject not fitted values | Select this check box to reject data rows of type char, varchar, binary, and varbinary if they do not fit the target table.  This property is available only when you are using Vertica 6.0 and later. |
| Maximum number of rejected records | Select this check box and in the field displayed next to it, specify the maximum number of records that can be rejected before a load fails.  This property is available only when you are using Vertica 6.0 and later. |
| Stop and rollback if any row is rejected | Select this check box to stop and roll back a load without loading any data if any row is rejected.  This property is available only when you are using Vertica 6.0 and later. |
| Don't commit | Select this check box to perform a bulk load transaction without committing the results automatically. This is useful if you want to execute multiple bulk loads in a single transaction.  This property is available only when you are using Vertica 6.0 and later. |
| Rejected data file | Specify the file into which rejected rows will be written.  This property is available only when `Bulk insert` is selected from the Action on data drop-down list. |
| Exception log file | Specify the file into which the exception log will be written. This log explains why each rejected row was rejected.  This property is available only when `Bulk insert` is selected from the Action on data drop-down list. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ACCEPTED\_ROW\_NUMBER | The number of rows loaded into the database. This is an After variable and it returns an integer. |
| REJECTED\_ROW\_NUMBER | The number of rows rejected. This is an After variable and it returns an integer. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded into the database.  Talend Studio and the Vertica database create very fast and affordable data warehouse and data mart applications. For more information about how to configure *Talend Studio* to connect to Vertica, see [Talend and HP Vertica Tips and Techniques](https://www.vertica.com/kb/Vertica-Integration-with-Talend-Connection-Guide/Content/Partner/Vertica-Integration-with-Talend-Connection-Guide.htm). |
