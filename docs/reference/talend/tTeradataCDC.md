<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tteradatacdc · versión 8.0 -->
# tTeradataCDC

Last updated: 9/30/2026

Extracts source system data that has changed since the last extraction and
transports it to another system(s) using the CDC Trigger mode.

tTeradataCDC addresses data extraction and transportation
needs. It only extracts the changes done to the source operational data and makes them
available to the target system(s) using database CDC views.

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tTeradataCDC Standard properties

These properties are used to configure tTeradataCDC running in the Standard Job framework.

The Standard
tTeradataCDC component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property of the CDC connection | * Either Built-In or Repository. * Built-In: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The database connection related   fields that follow are completed automatically using the data   retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Type in the IP address or hostname of the database. |
| Database | Type in the name of the database you want to use. |
| Username and Password | Type in the database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema using CDC and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  The schema of this component is set by default. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table using CDC | Specify the name of the table from which data changes will be captured. |
| Subscriber | Specify the name of the application that will use the change table in Trigger mode. |
| Events to catch | Insert: Select this check box to catch the data inserted in the change table since the last extraction.  Update: Select this check box to catch the data updated in the change table since the last extraction.  Delete: Select this check box to catch the data deleted in the change table since the last extraction. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the database connection you are creating. This field is not visible when the Use an existing connection check box is selected. |
| Keep data in CDC Table | Select this check box to retain changes in the CDC table, allowing one or more target systems to consult the data even after ingestion. When enabled, this option prevents deletion of the consulted CDC data; instead, it updates the value of the field CDC\_STATE to 'x'. This mechanism lets users recheck previously ingested data by filtering records where CDC\_STATE = 'x' (for example, using a tMysqlInput component), and manage deletion themselves if needed. This option is especially useful for users who need to audit or revisit ingested data without having to re-run Jobs or reverse-engineer the process to understand how the checkbox affects CDC\_STATE. |
| Trim all the String/Char columns | Select this check box to remove the leading and trailing whitespaces from all the String/Char columns. |
| Trim column | Select the check box(es) in the Trim column to remove the leading and trailing whitespaces from the corresponding column(s). This table is not visible when the Trim all the String/Char columns check box is selected. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as a start component of a Job or subJob and it needs an output link. |
