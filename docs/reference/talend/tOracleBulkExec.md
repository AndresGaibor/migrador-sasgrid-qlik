<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toraclebulkexec · versión 8.0 -->
# tOracleBulkExec

Last updated: 9/30/2026

Offers gains in performance during operations performed on data of an Oracle
database.

tOracleBulkExec inserts, appends,
replaces or truncate data in an Oracle database.

The tOracleOutputBulk and tOracleBulkExec components are used together in a two
step process. In the first step, an output file is generated. In the second step, this
file is used in the INSERT operation used to feed a database. These two steps are fused
together in the tOracleOutputBulkExec component,
detailed in a separate section. The advantage of using two separate steps is that the
data can be transformed before it is loaded in the database.

## tOracleBulkExec Standard properties

These properties are used to configure tOracleBulkExec running in the Standard Job framework.

The Standard
tOracleBulkExec component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: The database server/client must be installed on the same machine where Talend Studio is
installed or where the Job using tOracleBulkExec is deployed, so
that the component functions properly.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Make sure that the connection selected is not of the WALLET type to prevent possible errors.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers:  Oracle OCI: Select this connection type to use Oracle Call Interface with a set of C-language software APIs that provide an interface to the Oracle database.  Oracle Service Name: Select this connection type to use the TNS alias that you give when you connect to the remote database.  Oracle SID: Select this connection type to uniquely identify a particular database on a system.  Oracle Custom: Select this connection type to access a clustered database. |
| DB Version | Select the Oracle version in use. |
| Host | IP address of the database server. |
| Port | Port number listening the database server. |
| Database | Database name. |
| Schema | Schema name. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:  None: No operation is carried out.  Drop and create table: The table is removed and created again.  Create table: The table does not exist and gets created.  Create table if not exists: The table is created if it does not exist.  Drop table if exists and create: The table is removed if it already exists and created again.  Clear table: The table content is deleted.  Truncate table: The table content is deleted. You do not have the possibility to rollback the operation. |
| Data file name | Name of the file to be loaded.  Information noteWarning: This file should be located on the same machine as the Talend JobServer. |
| Action on data | On the data of the table defined, you can perform:  Insert: Insert data to an empty table. If the table already contains data, the Job stops and the existing data remains in the table.  Update: Update the existing data. You have to set the key on the schema if this option is selected.  Append: Append data to the table, whether the table is empty or not.  Replace: if the table already contains data, delete all the existing data and insert the new data. If the table is empty, insert the new data.  Truncate: If the table already contains data, truncate all the existing data and insert the new data. If the table is empty, insert the new data. |
| Schema and Edit Schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are   integers or functions, ensure that these default values are not enclosed within   quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg). |

## Advanced settings

| Properties | Description |
| --- | --- |
| Advanced separator (for number) | Select this check box to change the separator used for the numbers. |
| Use existing control file | Select this check box if you use a control file (.ctl) and specify its path in the .ctl file name field. |
| Record format | Define the record format:  Default: format parameters are set by default.  Stream: set Record terminator.  Fixed: set the Record length.  Variable: set the Field size of the record length. |
| Specify .ctl file's INTO TABLE clause manually | Select this check box to manually fill in the INTO TABLE clause of the control file. |
| Fields terminated by | Character, string or regular expression to separate fields:  None: no separator is used.  Whitespace: the separator used is a space.  EOF (used for loading LOBs from lobfile): the separator used is an EOF character (End Of File).  Other terminator: Set another terminator in the Field terminator field. |
| Use fields enclosure | Select this check box if you want to use enclosing characters for the text:  Fields enclosure (left part): character delimiting the left of the field.  Field enclosure (right part): character delimiting the right of the field. |
| Use schema's Date Pattern to load Date field | Select this check box to use the date pattern of the schema in the date field. |
| Specify field condition | Select this check box to define data loading condition. |
| Preserve blanks | Select this check box to preserve the blanks. |
| Trailing null columns | Select this check box to load null columns. |
| Load options | Click + to add data loading options:  Parameter: select a loading parameter from the list.  Value: enter a value for the parameter selected. |
| NLS Language | In the list, select the language used for the data that are not used in Unicode. |
| Set Parameter NLS\_TERRITORY | Select this check box to modify the territory conventions used for day and weeks numbering. Your OS value is the default value used. |
| Encoding | Select the encoding from the list, or enter the encoding between double quotes if it does not exist in the list. This field is compulsory for database data handling. |
| Output | Select the type of output for the standard output of the Oracle database:  to console,  to global variable. |
| Convert columns and table names to uppercase | Select this check box to uppercase the names of the columns and the name of the table. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_DATA: the number of rows read. This is an After variable and it returns an integer.  NB\_LINE\_BAD: the number of rows rejected. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  RETURN\_CODE: the return code indicating the result of processing. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This dedicated component offers performance and flexibility of Oracle DB query handling. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Truncating and inserting file data into an Oracle database](toracleinput-toraclebulkexec-tfileoutputdelimited-toraclebulkexec-tfileoutputdelimited-truncating-and-inserting-file-data-into-oracle-database-standard-component-this)
