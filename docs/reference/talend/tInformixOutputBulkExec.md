<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/informix/tinformixoutputbulkexec · versión 8.0 -->
# tInformixOutputBulkExec

Last updated: 9/30/2026

Carries out Insert operations in Informix databases using the data
provided.

tInformixOutputBulk and
tInformixBulkExec are generally used together in a two step process.
In the first step, an output file is generated. In the second step, this file is used in
the INSERT operation used to feed a database. These two steps are fused together in the
tInformixOutputBulkExec component.

## tInformixOutputBulkExec Standard properties

These properties are used to configure tInformixOutputBulkExec running in the Standard Job framework.

The Standard
tInformixOutputBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | * Either Built-in or   Repository   . * No properties stored centrally * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Execution platform | Select the operating system you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. |
| Port | DB server listening port. |
| Database | Name of the database. |
| Schema | Name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Instance | Name of the Informix instance to be used. This information can generally be found in the *SQL hosts* file. |
| Table | Name of the table to be written. Note that only one table can be written at a time and the table must already exist for the insert operation to be authorised. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create a table: The table is removed and created again.  Create a table: The table does not exist and gets created.  Create a table if not exists: The table is created if it does not exist.  Drop a table if exists and create: The table is removed if it already exists and created again.  Clear a table: The table content is deleted. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Informix Directory | Informix installation directory, e.g. *" C:\Program Files\IBM\IBM Informix Dynamic Server\11.50\"*. |
| Data file | Name of the file to be generated and loaded. |
| Append | Select this check box to add rows to the end of the file. |
| Action on data | Select the operation you want to perform:  Bulk insert  Bulk update The details asked will be different according to the action chosen. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Row separator | String (ex: "\n"on Unix) to distinguish rows. |
| Fields terminated by | Character, string or regular expression used to separate the fields |
| Set DBMONEY | Select this check box to define the decimal separator used in the corresponding field. |
| Set DBDATE | Select the date format you want to apply. |
| Rows Before Commit | Enter the number of rows to be processed before the commit. |
| Bad Rows Before Abort | Enter the number of rows in error at which point the Job should stop. |
| Create directory if not exists | This check box is selected by default. It creates a directory to hold the output table if required. |
| Custom the flush buffer size | Select this box in order to customize the memory size used to store the data temporarily. In the Row number field enter the number of rows at which point the memory should be freed. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |
| Output | Where the output should go. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used when no particular transformation is required on the data to be inserted in the database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The database server/client must be installed on the same machine where Talend Studio is installed or where the Job using tInformixOutputBulkExec is deployed, so that the component functions properly. |
