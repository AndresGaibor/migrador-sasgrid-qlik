<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/postgresql/tpostgresqlbulkexec · versión 8.0 -->
# tPostgresqlBulkExec

Last updated: 9/30/2026

Improves performance while carrying out the Insert operations to a Postgresql
database.

The tPostgresqlBulkExec executes the Insert action on
the data provided.

The tPostgresqlOutputBulk and
tPostgresqlBulkExec components are used
together to first output the file that will be then used as parameter to execute the SQL
query stated. These two steps compose the tPostgresqlOutputBulkExec component, detailed in a separate section.
The interest in having two separate elements lies in the fact that it allows
transformations to be carried out before the data loading in the database.

## tPostgresqlBulkExec Standard properties

These properties are used to configure tPostgresqlBulkExec running in the Standard Job framework.

The Standard
tPostgresqlBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| DB Version | Select the database version in the dropdown list. |
| Host | Enter the database server IP address. |
| Port | Listening port number of DB server. |
| Database | Enter the name of the database. |
| Schema | Enter the name of the PostgreSQL schema. |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Enter the name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | Select the operation to be performed on the defined table: None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted.  Truncate table: The table content is deleted. You don not have the possibility to rollback the operation. |
| File Name | Enter the name of the file to be loaded. Information noteWarning: This file is located on the machine specified by the URI in the Host field so it should be on the same machine as the database server. |
| Schema and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component supports PostgreSQL vector data types. Use the VECTOR or Dynamic DB type in your schema column definition to store and then query vector embeddings. For more information about pgvector, read [the Amazon documentation](https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-rds-postgresql-pgvector-ml-model-integration/). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. This property is not available when the Use an existing connection check box in the Basic settings view is selected. |
| Action on data | Select the action to be performed on the table data: * Bulk Insert: Add multiple entries   to the table. If duplicates are found, the Job stops. * Bulk Update: Make simultaneous   changes to multiple entries. |
| Copy the OID for each row | Retrieve the ID item for each row. |
| Contains a header line with the names of each column in the file | Specify that the table contains header. |
| Use local file for copy (for DB server 8.2 or newer) | (Enabled by default) Select this checkbox to copy files from the PostgreSQL client machine. |
| Set encoding and Encoding | Select the option to set a specific encoding. Select the encoding standard from the list, or select CUSTOM and define it manually. |
| File type | Select the type of file being handled. |
| Null string | String displayed to indicate that the value is null. |
| Fields terminated by | Character, string, or regular expression to separate fields. |
| Escape char | Character of the row to be escaped. |
| Text enclosure | Character used to enclose text. |
| Activate standard\_conforming\_string | Activate the variable. |
| Force not null for columns | Define the columns nullability. Force not null: Select the checkbox next to the column you want to define as not null. |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is to be used along with tPostgresqlOutputBulk component. Used together, they can offer gains in performance while feeding a PostgreSQL database. This component supports PostgreSQL vector data types. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
