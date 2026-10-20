<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/postgresql/tpostgresqloutputbulkexec · versión 8.0 -->
# tPostgresqlOutputBulkExec

Last updated: 9/30/2026

Improves performance during Insert operations to a Postgresql database.

The tPostgresqlOutputBulkExec executes the Insert
action on the data provided.

The tPostgresqlOutputBulk and tPostgresqlBulkExec components are generally used together as part of a
two step process. In the first step, an output file is generated. In the second step,
this file is used in the INSERT operation used to feed a database. These two steps are
fused together in the tPostgresqlOutputBulkExec
component.

## tPostgresqlOutputBulkExec Standard properties

These properties are used to configure tPostgresqlOutputBulkExec running in the Standard Job framework.

The Standard
tPostgresqlOutputBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

This component supports PostgreSQL vector data types. Use the
VECTOR or Dynamic DB type in your schema
column definition to store and then query vector embeddings. For more information about
pgvector, read [the Amazon documentation](https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-rds-postgresql-pgvector-ml-model-integration/).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| DB Version | Select the database version in the dropdown list. |
| Host | Enter the database server IP address. |
| Port | Listening port number of DB server. |
| Database | Enter the name of the database. |
| Schema | Enter the name of the PostgreSQL schema. |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Enter the name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | Select the operation to be performed on the defined table: None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if already exists and created again.  Clear a table: The table content is deleted. |
| File Name | Enter the name of the file to be generated and loaded. Information noteWarning: This file is generated on the machine specified by the URI in the Host field and it should be on the same machine as the database server. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository. Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component supports PostgreSQL vector data types. Use the VECTOR or Dynamic DB type in your schema column definition to store and then query vector embeddings. For more information about pgvector, read [the Amazon documentation](https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-rds-postgresql-pgvector-ml-model-integration/). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| Action on data | Select the action to be performed on the table data: * Bulk Insert: Add multiple entries   to the table. If duplicates are found, the Job stops. * Bulk Update: Make simultaneous   changes to multiple entries. |
| Copy the OID for each row | Retrieve the ID item for each row. |
| Contains a header line with the names of each column in the file | Specify that the table contains header. |
| Use local file for copy (for DB server 8.2 or newer) | (Enabled by default) Select this check box to copy files from the PostgreSQL client machine. |
| Encoding | Select the encoding standard from the list, or select CUSTOM and define it manually. This field is compulsory for DB data handling. |
| File type | Select the type of file being handled. |
| Null string | String displayed to indicate that the value is null. |
| Row separator | String (ex: "\n"on Unix) to distinguish rows. |
| Fields terminated by | Character, string, or regular expression to separate fields. |
| Escape char | Character of the row to be escaped. |
| Text enclosure | Character used to enclose text. |
| Activate standard\_conforming\_string | Activate the variable. |
| Force not null for columns | Define the column nullability. Force not null: Select the checkbox next to the column you want to define as not null. |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. This component supports PostgreSQL vector data types. |
| Limitation | The database server must be installed on the same machine where Talend Studio is installed or where the Job using tPostgresqlOutputBulkExec is deployed, so that the component functions correctly. |
