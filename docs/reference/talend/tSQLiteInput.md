<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sqlite/tsqliteinput · versión 8.0 -->
# tSQLiteInput

Last updated: 9/30/2026

Executes a DB query with a defined command which must correspond to the schema
definition. It passes on rows to the next component via a Main row link.

tSQLiteInput reads a database file
and extracts fields based on an SQL query. As it embeds the SQLite engine, no need of
connecting to any database server.

## tSQLiteInput Standard properties

These properties are used to configure tSQLiteInput running in the Standard Job framework.

The Standard
tSQLiteInput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Database | Filepath to the SQLite database file. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Query type | Either Built-in or Repository . |
| Query | If your query is not stored in the Repository, type in your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  *If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected.* |

## Advanced settings

| Properties | Description |
| --- | --- |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is standalone as it includes the SQLite engine. This is a startable component that can iniate a data flow processing. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Filtering SQlite data](tsqliteinput-tsqliteoutput-tsqliteoutput-filtering-sqlite-data-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sqlite/tsqliteinput-tsqliteoutput-tsqliteoutput-filtering-sqlite-data-standard-component-this -->
# Filtering SQlite data

Last updated: 9/30/2026

This scenario describes a rather simple Job which uses a select statement based on a
filter to extract rows from a source SQLite Database and feed an output SQLite table.

* Drop from the Palette, a tSQLiteInput and a tSQLiteOutput component from the Palette to the design workspace.
* Connect the input to the output using a row main link.
* On the tSQLiteInput Basic settings, type in
  or browse to the SQLite Database input file.

* The file contains hundreds of lines and includes an ip column which the select statement will based on
* On the tSQLite Basic settings, edit the
  schema for it to match the table structure.

* In the Query field, type in your select
  statement based on the *ip* column.
* On the tSQLiteOutput component Basic settings panel, select the Database filepath.

* Type in the Table to be fed with the
  selected data.
* Select the Action on table and Action on Data. In this use case, the action on table
  is *Drop and create* and the action on data is
  *Insert*.
* The schema should be synchronized with the input schema.
* Save the Job and run it.

The data queried is returned in the defined SQLite file.

For an example of how to use dynamic schemas
with Input components, see [Writing dynamic columns from a database to an output file](/talend/en-US/components/8.0/dynamic-schema/tmysqlinput-tfileoutputdelimited-tmap-tfileoutputdelimited-tmap-writing-dynamic-columns-from-database-to-output-file-standard-component-enterprise-in-this).

**Related reference**  

* [tSQLiteInput](tsqliteinput "Executes a DB query with a defined command which must correspond to the schema definition. It passes on rows to the next component via a Main row link.")
* [tSQLiteOutput](tsqliteoutput "Executes the action defined on the table and/or on the data contained in the table, based on the flow incoming from the preceding component in the job.")
