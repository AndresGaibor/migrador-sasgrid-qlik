<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tingresscd · versión 8.0 -->
# tIngresSCD

Last updated: 9/30/2026

Reflects and tracks changes in a dedicated Ingres SCD table.

tIngresSCD addresses Slowly Changing Dimension needs,
reading regularly a source of data and logging the changes into a dedicated SCD table.

Information noteNote:

* This component is available only when you have installed the 8.0.1-R2023-02 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator.
* If you plan to upgrade from an earlier version of Talend Studio
  that has Ingres components, please make sure you apply the 8.0.1-R2023-02 Talend Studio
  Monthly update before starting the upgrade process.

## tIngresSCD Standard properties

These properties are used to configure tIngresSCD running in the Standard Job framework.

The Standard
tIngresSCD component belongs to the Business Intelligence and the Databases families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the Repository   file where properties are stored. The fields to follow are   pre-filled in using fetched data. |
| Server | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Table | Name of the table to be written. Note that only one table can be written at a time. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| SCD Editor | The SCD editor helps to build and configure the data flow for slowly changing dimension outputs.  For more information, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology). |
| Use memory saving Mode | Select this check box to maximize system performance. |
| Source keys include Null | Select this check box to allow the source key columns to have Null values.  Information noteWarning: Special attention should be paid to the uniqueness of the source key(s) values when this option is selected. |
| Die on error | This check box is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. This property is not available when the Use an existing connection check box in the Basic settings view is selected. |
| End date time details | Specify the time value of the SCD end date time setting in the format of *HH:mm:ss*. The default value for this field is *12:00:00*.  This field appears only when SCD Type 2 is used and Fixed year value is selected for creating the SCD end date. |
| Debug mode | Select this check box to display each step during processing entries in a database. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as Output component. It requires an Input component and Row main link as input. |
| Limitation | This component does not support using SCD type 0 together with other SCD types. |
