<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/change-data-capture/tpostgresqlcdc · versión 8.0 -->
# tPostgresqlCDC

Last updated: 9/30/2026

Addresses data extraction and transportation needs, only extracts the changes made
to the source operational data and makes them available to the target system(s) using
database CDC views.

The tPostgresqlCDC extracts source
system data that has changed since the last extraction and transports it to
another/other system(s).

Information noteNote: If batch processing is enabled in the Job, the component cannot capture the order of changes and the source and target databases will not be synchronized.

## tPostgresqlCDC Standard properties

These properties are used to configure tPostgresqlCDC running in the Standard Job framework.

The Standard
tPostgresqlCDC component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend
products.

This component supports PostgreSQL vector data types. Use the
VECTOR or Dynamic DB type in your schema
column definition to store and then query vector embeddings. For more information about
pgvector, read [the Amazon documentation](https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-rds-postgresql-pgvector-ml-model-integration/).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved.  Information noteWarning: Reset the DB type by clicking the   relevant button to select the CDC connection. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| DB Version | Select the database version in the dropdown list. |
| Host | Enter the database server IP address. |
| Port | Listening port number of DB server. |
| Database | Enter the name of the database. |
| Schema | Enter the name of the PostgreSQL schema. |
| Username and Password | Enter the database user authentication data. To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema using CDC and Edit Schema | A schema is a row description, it defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.  * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.  Information noteWarning: Reset the DB type by clicking the   relevant button to select the schema of the CDC connection.   This component supports PostgreSQL vector data types. Use the VECTOR or Dynamic DB type in your schema column definition to store and then query vector embeddings. For more information about pgvector, read [the Amazon documentation](https://aws.amazon.com/about-aws/whats-new/2023/05/amazon-rds-postgresql-pgvector-ml-model-integration/). |
| Table | Select the source table from which any changes made to data are to be captured. |
| Subscriber | Enter the name of the application that will use the change table. |
| Events to catch | Insert: Select this checkbox to catch the data inserted in the change table since the last extracion.  Update: Select this checkbox to catch the data updated in the change table since the last extracion.  Delete: Select this checkbox to catch the data deleted in the change table since the last extracion. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional JDBC parameters for the database connection created. This property is not available when the Use an existing connection check box in the Basic settings view is selected. |
| Keep data in CDC Table | Select this checkbox to retain changes in the CDC table, allowing one or more target systems to consult the data even after ingestion. When enabled, this option prevents deletion of the consulted CDC data; instead, it updates the value of the field CDC\_STATE to 'x'. This mechanism lets users recheck previously ingested data by filtering records where CDC\_STATE = 'x' (for example, using a tMysqlInput component), and manage deletion themselves if needed. This option is especially useful for users who need to audit or revisit ingested data without having to re-run Jobs or reverse-engineer the process to understand how the checkbox affects CDC\_STATE. |
| Use cursor | Select this checkbox to specify the number of rows you want to work with at at any given time. This option optimises performance. |
| Trim all the String/Char columns | Select this checkbox to delete any spaces found at the beginning or end of fields, in all of the columns containing character strings. |
| Trim column | Remove leading and trailing whitespace from defined columns. Information noteNote: Clear Trim all the String/Char columns to enable Trim columns in this field. |
| tStatCatcher Statistics | Select this checkbox to collect the log data at component level. |
| Enable parallel execution | Select this check box to perform high-speed data processing, by treating multiple data flows simultaneously. Note that this feature depends on the database or the application ability to handle multiple inserts in parallel as well as the number of CPU affected. In the Number of parallel executions field, either:  * Enter the number of parallel executions desired. * Press Ctrl+Space and select   the appropriate context variable from the list. For further information about context   variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Note that when parallel execution is enabled, it is not possible to use global variables to retrieve return values in a subJob.  * The Action on   table field is not available with the   parallelization function. Therefore, you must use a tCreateTable component if you   want to create a table. * When parallel execution is enabled, it is not   possible to use global variables to retrieve return values in a   subJob. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is used as a start component. It requires an output component and a row Main link. This component supports PostgreSQL vector data types. |
