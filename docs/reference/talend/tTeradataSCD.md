<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tteradatascd · versión 8.0 -->
# tTeradataSCD

Last updated: 9/30/2026

Addresses Slowly Changing Dimension needs, reading regularly a source of data and
logging the changes into a dedicated SCD table.

tTeradataSCD reflects and tracks changes in a dedicated
Teradata SCD table.

## tTeradataSCD Standard properties

These properties are used to configure tTeradataSCD running in the Standard Job framework.

The Standard
tTeradataSCD component belongs to the Business Intelligence and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | * Either Built-In or Repository. * Built-In: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The database connection related   fields that follow are completed automatically using the data   retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Type in the IP address or hostname of the database. |
| Database | Type in the name of the database you want to use. |
| Username and Password | Type in the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Type in the name of the table to be written. Note that only one table can be written at a time. |
| Action on table | On the table defined, you can perform one of the following operations:  * None: No operation is   carried out. * Create table: The table does not exist and gets   created. * Create table if not exists: The table is created if   it does not exist. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| SCD Editor | The SCD editor helps to build and configure the data flow for slowly changing dimension outputs.  For more information, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology). |
| Use memory saving mode | Select this check box to maximize system performance. |
| Source keys include Null | Select this check box to allow the source key columns to have Null values.  Information noteWarning: Special attention should be paid to the uniqueness of the source key(s) values when this option is selected. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the database connection you are creating.  This field is not visible when the Use an existing connection check box is selected. |
| Debug mode | Select this check box to display each step during processing entries in a database. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as an Output component. It requires an Input component and a Row > Main link as input. |
| Limitation | This component does not support using SCD type 0 together with other SCD types. |
