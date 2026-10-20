<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scdelt/tteradatascdelt · versión 8.0 -->
# tTeradataSCDELT

Last updated: 9/30/2026

Addresses Slowly Changing Dimension needs through SQL queries (server-side
processing mode), and logs the changes into a dedicated Teradata SCD table.

tTeradataSCDELT
reflects and tracks changes in a dedicated Teradata SCD table.

## tTeradataSCDELT Standard properties

These properties are used to configure tTeradataSCDELT running in the Standard Job
framework.

The Standard
tTeradataSCDELT component belongs to the Business Intelligence and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Either Built-In or Repository.   * Built-In: No   property data stored centrally. * Repository: Select   the repository file in which the properties are stored. The database   connection fields that follow are completed automatically using the data   retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the IP address or hostname of the database server. |
| Database | Enter the name of the database you want to use. |
| Username and Password | Enter the user authentication data to access the database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Source table | Enter the name of the input Teradata SCD table. |
| Table | Enter the name of the table to be written. Note that only one table can be written at a time. |
| Action on table | Select one of the following operations to be performed on the table defined:   * None: No action   carried out on the table. * Create table: A   new table gets created. * Drop and create   table: The table is removed and created again. * Create table if not   exists: A table gets created if it does not exist. * Drop table if exists and   create: The table is removed if it already exists and   created again. * Clear table: The   table content is deleted. You have the possibility to rollback the   operation. * Truncate table:   The table content is deleted. You don not have the possibility to   rollback the operation. |
| Create | Select the type of the table to be created:   * SET TABLE: creates   a SET table that does not allow duplicate rows to be inserted. * MULTISET TABLE:   creates a MULTISET table that allows duplicate rows to be inserted.   This list is available only when Create table, Drop and create table, Create table if not exists, or Drop table if exists and create is selected from the Action on table drop-down list. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: The     schema is created and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).   + Repository: The     schema already exists and is stored in the Repository, hence can be     reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Surrogate key | Select the surrogate key column from the list. |
| Creation | Select the method to be used for the surrogate key generation.  For more information about the creation methods, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology). |
| Source Keys | Select one or more columns to be used as keys, to ensure the unicity of the incoming data. |
| Use SCD type 1 fields | Select this check box to use SCD Type 1 if tracking changes is not necessary. SCD Type 1 should be used for typos corrections for example. |
| SCD type 1 fields | Click the [+] button to add as many rows as needed, and in each row select an input schema column that will be checked for Type 1 changes.  This table is available only when the Use SCD type 1 fields check box is selected. |
| Use SCD type 2 fields | Select this check box to use SCD Type 2 if changes need to be tracked down. SCD Type 2 should be used to trace updates for example. |
| SCD type 2 fields | Click the [+] button to add as many rows as needed, each row for a column. Click the arrow on the right side of the cell and select the column whose value changes will be tracked using Type 2 SCD from the drop-down list displayed .  This table is available only when the Use SCD type 2 fields option is selected. |
| Start date | Specify the column that holds the start date for type 2 SCD.  This list is available only when the Use SCD type 2 fields option is selected. |
| End date | Specify the column that holds the end date for type 2 SCD.  This list is available only when the Use SCD type 2 fields option is selected.  Information noteNote: To avoid duplicated change records, it is recommended to select a column that can identify each change for this field. |
| Log active status | Select this check box and from the Active field drop-down list displayed, select the column that holds the true or false status value, which helps to spot the active record for type 2 SCD.  This option is available only when the Use SCD type 2 fields option is selected. |
| Log versions | Select this check box and from the Version field drop-down list displayed, select the column that holds the version number of the record for type 2 SCD.  This option is available only when the Use SCD type 2 fields option is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the database connection you are creating.  This field is not available if the Use an existing connection check box is selected. |
| Source fields value include Null | Select this check box to allow the source columns to have Null values. The source columns here refer to the fields defined in the SCD type 1 fields and SCD type 2 fields tables. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an output component and it always needs an incoming link. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | This component requires installation of its related jar files. |
