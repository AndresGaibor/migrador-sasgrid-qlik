<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/greenplum/tgreenplumbulkexec · versión 8.0 -->
# tGreenplumBulkExec

Last updated: 9/30/2026

Improves performance when loading data in a Greenplum
database.

The tGreenplumOutputBulk and
tGreenplumBulkExec components are used
together in a two step process. In the first step, an output file is generated. In the
second step, this file is used in the INSERT statement used to feed a database. These
two steps are fused together in the tGreenplumOutputBulkExec component, detailed in a separate section. The
advantage of using a two step process is that it makes it possible to transform data
before it is loaded in the database.

tGreenplumBulkExec performs an Insert
action on the data.

## tGreenplumBulkExec Standard properties

These properties are used to configure tGreenplumBulkExec running in the Standard Job framework.

The Standard
tGreenplumBulkExec component belongs to the Databases family.

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
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Schema | Exact name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted. |
| Filename | Name of the file to be loaded.  Information noteWarning: When you select DataDirect as the DB driver, the Filename can use a path local to the client or Job runtime. For other drivers, the file must be on the machine specified in the Host field.  DataDirect does not provide native bulk-load support for Greenplum and loads data using standard batching. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. |
| DB driver | Select a database driver from the drop-down list: `PostgreSQL`, `Greenplum(Deprecated)`, or `DataDirect`. The default is `PostgreSQL`.  Information noteImportant: The `Greenplum(Deprecated)` driver is deprecated. Migrate to `DataDirect`, a third-party JDBC driver suggested by Greenplum.  This option is available when Use an existing connection is not selected in the Basic settings view. |
| Action on data | Select the operation you want to perform:  Bulk insert  Bulk update The details asked will be different according to the action chosen. |
| Copy the OID for each row | Retrieve the ID item for each row. |
| Contains a header line with the names of each column in the file | Specify that the table contains header. |
| File type | Select the file type to process. |
| Null string | String displayed to indicate that the value is null. |
| Fields terminated by | Character, string or regular expression to separate fields. |
| Escape char | Character of the row to be escaped |
| Text enclosure | Character used to enclose text. |
| Force not null for columns | Define the columns nullability  Force not null: Select the check box next to the column you want to define as not null. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with a tGreenplumOutputBulk component. Used together they offer gains in performance while feeding a Greenplum database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
