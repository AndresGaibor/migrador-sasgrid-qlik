<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/maxdb/tmaxdbrow · versión 8.0 -->
# tMaxDBRow

Last updated: 9/30/2026

Acts on the actual DB structure or on the data (although without handling data),
depending on the nature of the query and the database.

tMaxDBRow is the specific component
for this database query. It executes the SQL query stated onto the specified database.
The row suffix means the component implements a flow in the Job design although it
doesn't provide output.

The SQLBuilder tool helps you write easily your SQL statements.

## tMaxDBRow Standard properties

These properties are used to configure tMaxDBRow running in the Standard Job framework.

The Standard
tMaxDBRow component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table name | Type in the table name. |
| Query type | * The query can be Built-in for a particular Job, or for commonly used   query, it can be stored in the Repository to ease the query reuse. * Built-in: Fill in manually the query statement or build it graphically   using SQLBuilder. * Repository: Select the relevant query stored in the Repository. The   Query field gets accordingly filled in. |
| Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row > Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Propagate QUERY's recordset | Select this check box to insert the result of the query into a COLUMN of the current flow. Select this column from the use column list. |
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
| **Usage rule** | This component offers the flexibility benefit of the DB query and covers all possible SQL queries. |
| Limitation | This component requires installation of its related jar files. |
