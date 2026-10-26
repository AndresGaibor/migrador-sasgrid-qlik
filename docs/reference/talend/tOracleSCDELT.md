<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/toraclescdelt · versión 8.0 -->
# tOracleSCDELT

Last updated: 9/30/2026

Reflects and tracks changes in a dedicated Oracle SCD table through SQL
queries.

tOracleSCDELT addresses Slowly Changing
Dimension needs through SQL queries (server-side processing mode), and logs the changes into a
dedicated Oracle SCD table.

## tOracleSCDELT Standard properties

These properties are used to configure tOracleSCDELT running in the Standard Job framework.

The Standard
tOracleSCDELT component belongs to the Business Intelligence and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. Enter properties manually. * Repository: Select the repository   file where Properties are stored. The fields that come after are   pre-filled in using the fetched data. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Make sure that the connection selected is not of the WALLET type to prevent possible errors.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection type | Drop-down list of available drivers:  Oracle OCI: Select this connection type to use Oracle Call Interface with a set of C-language software APIs that provide an interface to the Oracle database.  Oracle Service Name: Select this connection type to use the TNS alias that you give when you connect to the remote database.  Oracle SID: Select this connection type to uniquely identify a particular database on a system.  Oracle Custom: Select this connection type to access a clustered database. |
| DB Version | Select the Oracle version you are using. |
| Host | The IP address of the database server. |
| Port | Listening port number of database server. |
| Database | Name of the database |
| Username and Password | User authentication data for a dedicated database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Source table | Name of the input DB2 SCD table. |
| Table | Name of the table to be written. Note that only one table can be written at a time |
| Action on table | Select to perform one of the following operations on the table defined:  None: No action carried out on the table.  Drop and create table: The table is removed and created again  Create table: A new table gets created.  Create table if not exists: A table gets created if it does not exist.  Clear table: The table content is deleted. You have the possibility to rollback the operation.  Truncate table: The table content is deleted. You don not have the possibility to rollback the operation. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Surrogate Key | Select the surrogate key column from the list. |
| Creation | Select the method to be used for the surrogate key generation.  For more information regarding the creation methods, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology). |
| Source Keys | Select one or more columns to be used as keys, to ensure the unicity of incoming data. |
| Source fields value include Null | Select this check box to allow the source columns to have Null values.  Information noteNote: The source columns here refer to the fields defined in the SCD type 1 fields and SCD type 2 fields tables. |
| Use SCD Type 1 fields | Use type 1 if tracking changes is not necessary. SCD Type 1 should be used for typos corrections for example. Select the columns of the schema that will be checked for changes. |
| Use SCD Type 2 fields | Use type 2 if changes need to be tracked down. SCD Type 2 should be used to trace updates for example. Select the columns of the schema that will be checked for changes.  Start date: Adds a column to your SCD schema to hold the start date value. You can select one of the input schema columns as Start Date in the SCD table.  End Date: Adds a column to your SCD schema to hold the end date value for the record. When the record is currently active, the End Date column shows a null value, or you can select Fixed Year value and fill it in with a fictive year to avoid having a null value in the End Date field.  Information noteNote: To avoid duplicated change records, it is recommended to select a column that can identify each change for this field.  Log Active Status: Adds a column to your SCD schema to hold the true or false status value. This column helps to easily spot the active record.  Log versions: Adds a column to your SCD schema to hold the version number of the record. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Debug mode | Select this check box to display each step during processing entries in a database. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Support NLS | Select this option to enable globalization support. See [Overview of Globalization Support](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/overview-of-globalization-support.html) for related information.  This option is available when the Use an existing connection option is cleared and Oracle 18 and above is selected from the DB Version drop-down list in the Basic settings view.  Information noteNote: This option is available only when you have installed the 8.0.1-R2022-09 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an output component. It requires an input component and Row main link as input. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
