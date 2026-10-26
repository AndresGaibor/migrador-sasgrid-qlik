<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tsybasecdc · versión 8.0 -->
# tSybaseCDC

Last updated: 9/30/2026

Extracts source system data that has changed since the last extraction and
transports it to another/other system(s).

tSybaseCDC addresses data extraction
and transportation needs. It only extracts the changes made to the source operational data and
makes them available to the target system(s) using database CDC views.

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tSybaseCDC Standard properties

These properties are used to configure tSybaseCDC running in the Standard Job framework.

The Standard
tSybaseCDC component belongs to the Databases family.

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
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved.  Information noteWarning: *Reset the DB type by clicking the relevant button to   select the CDC connection.* |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Server | Database server IP address. |
| Port | DB server listeing port number. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema using CDC and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Information noteWarning: *Reset the DB type by clicking the relevant button to   select the schema of the CDC connection.* * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table name | Select the source table from which changes made to data are to be captured. |
| Schema | Name of the DB schema. |
| Subscriber | Enter the name of the application that will use the change table. |
| Events to catch | Insert: Select this check box to catch the data inserted in the change table since the last extraction.  Update: Select this check box to catch the data updated in the change table since the last extraction.  Delete: select this check box to catch the data deleted in the change table since the last extraction. |
| Limit | Maximum number of consumed rows a subscriber can recover from the change table, per execution. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Keep data in CDC Table | Select this check box to retain changes in the CDC table, allowing one or more target systems to consult the data even after ingestion. When enabled, this option prevents deletion of the consulted CDC data; instead, it updates the value of the field CDC\_STATE to 'x'. This mechanism lets users recheck previously ingested data by filtering records where CDC\_STATE = 'x' (for example, using a tMysqlInput component), and manage deletion themselves if needed. This option is especially useful for users who need to audit or revisit ingested data without having to re-run Jobs or reverse-engineer the process to understand how the checkbox affects CDC\_STATE. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns.  Information noteNote: Clear Trim all the String/Char columns to enable Trim columns in this field. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component. It requires an output component and row Main link. |
| Limitation | This component requires installation of its related jar files. |
