<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleoutputbulkexec · versión 8.0 -->
# tOracleOutputBulkExec

Last updated: 9/30/2026

Executes the Insert action in the specified Oracle database.

As a dedicated component, it allows gains in performance during Insert operations to an
Oracle database.

The tOracleOutputBulk and tOracleBulkExec components are used together in a two
step process. In the first step, an output file is generated. In the second step, this
file is used in the INSERT operation used to feed a database. These two steps are fused
together in the tOracleOutputBulkExec
component.

## tOracleOutputBulkExec Standard properties

These properties are used to configure tOracleOutputBulkExec running in the Standard Job framework.

The Standard
tOracleOutputBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: The database server/client must be installed on the same machine where Talend Studio is
installed or where the Job using tOracleOutputBulkExec is deployed, so that the component functions
properly.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Make sure that the connection selected is not of the WALLET type to prevent possible errors.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers:  Oracle OCI: Select this connection type to use Oracle Call Interface with a set of C-language software APIs that provide an interface to the Oracle database.  Oracle Service Name: Select this connection type to use the TNS alias that you give when you connect to the remote database.  Oracle SID: Select this connection type to uniquely identify a particular database on a system.  Oracle Custom: Select this connection type to access a clustered database. |
| DB Version | Select the Oracle version in use |
| Host | Database server IP address.  Currently, only *localhost*, *127.0.0.1* or the exact IP address of the local machine is allowed for proper functioning. In other words, the database server must be installed on the same machine where Talend Studio is installed or where the Job using tOracleOutputBulkExec is deployed. |
| Port | Listening port number of DB server. |
| Database | Name of the database |
| Schema | Name of the schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operations is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted.  Truncate table: The table content is deleted. You do not have the possibility to rollback the operation. |
| File Name | Name of the file to be generated and loaded.  Information noteWarning: This file is generated on the machine specified by the URI in the Host field so it should be on the same machine as the database server. |
| Create directory if not exists | This check box is selected by default. It creates a directory to hold the output table if required. |
| Append | Select this check box to add the new rows at the end of the file. |
| Action on data | On the data of the table defined, you can perform:  Insert: Insert data to an empty table. If the table already contains data, the Job stops and the existing data remains in the table.  Update: Update the existing data. You have to set the key on the schema if this option is selected.  Append: Append data to the table, whether the table is empty or not.  Replace: if the table already contains data, delete all the existing data and insert the new data. If the table is empty, insert the new data.  Truncate: If the table already contains data, truncate all the existing data and insert the new data. If the table is empty, insert the new data. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to be   processed and passed on to the next component. The schema is either   Built-in or stored remotely in the   Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |
| Field separator | Character, string or regular expression to separate fields. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change data separators for numbers:  Thousands separator: define separators you want to use for thousands.  Decimal separator: define separators you want to use for decimals. |
| Use existing control file | Select this check box and browse to the .ctl control file you want to use. |
| Field separator | Character, string or regular expression to separate fields. |
| Row separator | String (ex: "\n"on Unix) to separate rows. |
| Specify .ctl file's INTO TABLE clause manually | Select this check box to enter manually the INTO TABLE clause of the control file directly into the code. |
| Use schema's Date Pattern to load Date field | Select this check box to use the date model indicated in the schema for dates. |
| Specify field condition | Select this check box to define a condition for loading data. |
| Preserve blanks | Select this check box to preserve blank spaces. |
| Trailing null columns | Select this check box to load data with all empty columns. |
| Load options | Click + to add data loading options:  Parameter: select a loading parameter from the list.  Value: enter a value for the parameter selected. |
| NLS Language | From the drop-down list, select the language for your data if the data is not in Unicode. |
| Set Parameter NLS\_TERRITORY | Select this check box to modify the conventions used for date and time formats. The default value is that of the operating system. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| Oracle encoding type | Select the Oracle-specific encoding type for the data to be processed. This encoding type allows tOracleOutputBulkExec to properly generate the Sybase Bulk command. |
| Output | Select the type of output for the standard output of the Oracle database:  to console,  to global variable. |
| Convert columns and table names to uppercase | Select this check box to put columns and table names in upper case. |
| Bulk file parameters | Set the parameters Buffer Size and StringBuilder Size for a performance gain according to the memory size. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a job level as well as at each component level. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
