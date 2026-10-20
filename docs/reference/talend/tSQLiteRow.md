<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sqlite/tsqliterow · versión 8.0 -->
# tSQLiteRow

Last updated: 9/30/2026

Executes the defined query onto the specified database and uses the parameters
bound with the column.

A prepared statement uses the input flow to replace the placeholders with
the values for each parameters defined. This component can be very useful for updates.

## tSQLiteRow Standard properties

These properties are used to configure tSQLiteRow running in the Standard Job framework.

The Standard
tSQLiteRow component belongs to the Databases family.

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
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Query type | * Either Built-in or Repository   . * Built-in: Fill in manually the   query statement or build it graphically using SQLBuilder * Repository: Select the relevant   query stored in the Repository. The Query field gets accordingly   filled in. |
| Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition. |
| Die on error | Clear this check box to skip the row on error and complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Propagate QUERY's recordset | Select this check box to insert the result of the query into a COLUMN of the current flow. Select this column from the use column list.  Information noteNote: This option allows the component to have a different schema from that of the preceding component. Moreover, the column that holds the QUERY's recordset should be set to the type of *Object* and this component is usually followed by tParseRecordSet. |
| Use PreparedStatement | Select this check box if you want to query the database using a PreparedStatement. In the Set PreparedStatement Parameter table, define the parameters represented by "?" in the SQL instruction of the Query field in the Basic Settings tab.  Parameter Index: Enter the parameter position in the SQL instruction.  Parameter Type: Enter the parameter type.  Parameter Value: Enter the parameter value.    Information noteNote: This option is very useful if you need to execute the same query several times. Performance levels are increased |
| Commit every | Number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and above all better performance on executions. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query and covers all possible SQL queries. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |

**Related concepts**  

* [Updating SQLite rows](tsqliterow-tfileinputdelimited-updating-sqlite-rows-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sqlite/tsqliterow-tfileinputdelimited-updating-sqlite-rows-standard-component-this -->
# Updating SQLite rows

Last updated: 9/30/2026

This scenario describes a Job which updates an SQLite database file based on a
prepared statement and using a delimited file.

* Drop a tFileInputDelimited and a tSQLiteRow component from the Palette to the design workspace.
* On the tFileInputDelimited
  Basic settings panel, browse to the input file
  that will be used to update rows in the database.

* There is no Header nor Footer. The Row separator is a
  carriage return and the Field separator is a
  semi-colon.
* Click the [...] button next to Edit schema and define the schema structure in case it is not stored in the Repository.

* Make sure the length and type are respectively correct and large enough to
  define the columns.
* Then in the tSQLiteRow
  Basic settings panel, set the Database filepath to the file to be updated.

* The schema is read-only as it is required to match the input schema.
* Type in the query or retrieve it from the
  Repository. In this use case, we updated the
  *type\_os* for the *id* defined in the
  Input flow. The statement is as follows: "Update download set type\_os=?
  where id=?".
* Then select the Use PreparedStatement check
  box to display the placeholders' parameter table.

* In the Input parameters table, add as many lines as necessary to cover all
  placeholders. In this scenario, *type\_os* and
  *id* are to be defined.
* Set the Commit every field.
* Save the Job and press F6 to run it.

The *download* table from the SQLite database is thus updated with
new *type\_os* code according to the delimited input file.

**Related reference**  

* [tSQLiteRow](tsqliterow "Executes the defined query onto the specified database and uses the parameters bound with the column.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
