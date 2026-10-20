<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/greenplum/tgreenplumoutputbulkexec · versión 8.0 -->
# tGreenplumOutputBulkExec

Last updated: 9/30/2026

Provides performance gains during Insert operations to a Greenplum
database.

The tGreenplumOutputBulk and tGreenplumBulkExec components are used together in a two step process.
In the first step, an output file is generated. In the second step, this file is used in
the INSERT operation used to feed a database. These two steps are fused together in the
tGreenplumOutputBulkExec component.

tGreenplumOutputBulkExec executes the
action on the data provided.

## tGreenplumOutputBulkExec Standard properties

These properties are used to configure tGreenplumOutputBulkExec running in the Standard Job framework.

The Standard
tGreenplumOutputBulkExec component belongs to the Databases family.

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
| Host | Database server IP address.  Currently, only *localhost*, *127.0.0.1* or the exact IP address of the local machine is allowed for proper functioning. In other words, the database server must be installed on the same machine where Talend Studio is installed or where the Job using tGreenplumOutputBulkExec is deployed. |
| Port | Listening port number of DB server. |
| Database name | Name of the database. |
| Schema | Exact name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written.  Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted. You have the possibility to rollback the operation. |
| File Name | Name of the file to be generated and loaded.  Information noteWarning: This file is generated on the machine specified by the URI in the Host field so it should be on the same machine as the database server. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| DB driver | Select a database driver from the drop-down list: `PostgreSQL`, `Greenplum(Deprecated)`, or `DataDirect`. The default is `PostgreSQL`.  Information noteImportant: The `Greenplum(Deprecated)` driver is deprecated. Migrate to `DataDirect`, a third-party JDBC driver suggested by Greenplum. |
| Action on data | Select the operation you want to perform:  Bulk insert  Bulk update The details asked will be different according to the action chosen. |
| Copy the OID for each row | Retrieve the ID item for each row. |
| Contains a header line with the names of each column in the file | Specify that the table contains header. |
| File type | Select the file type to process. |
| Null string | String displayed to indicate that the value is null. |
| Row separator | String (ex: "\n"on Unix) to distinguish rows. |
| Fields terminated by | Character, string or regular expression to separate fields. |
| Escape char | Character of the row to be escaped |
| Text enclosure | Character used to enclose text. |
| Force not null for columns | Define the columns nullability  Force not null: Select the check box next to the column you want to define as not null. |
| tStatCatcherStatistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. |
| Limitation | The database server must be installed on the same machine where Talend Studio is installed or where the Job using tGreenplumOutputBulkExec is deployed, so that the component functions properly. |
