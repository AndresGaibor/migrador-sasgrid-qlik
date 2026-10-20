<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hsqldb/thsqldbrow · versión 8.0 -->
# tHSQLDbRow

Last updated: 9/30/2026

Acts on the actual DB structure or on the data (although without handling
data), depending on the nature of the query and the database.

The SQLBuilder
tool helps you write easily your SQL statements.

tHSQLDbRow is the specific component for this database query. It
executes the SQL query stated onto the specified database. The row suffix means the
component implements a flow in the Job design although it doesn't provide output.

## tHSQLDbRow Standard properties

These properties are used to configure tHSQLDbRow running in the Standard Job framework.

The Standard
tHSQLDbRow component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Running Mode | Select on the list the Server Mode corresponding to your DB setup among the four propositions :  HSQLDb Server, HSQLDb WebServer, HSQLDb In Process Persistent, HSQLDb In Memory. |
| Use TLS/SSL sockets | Select this check box to enable the secured mode if required. |
| Host | Database server IP address |
| Port | Listening port number of DB server. |
| Database Alias | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| DB path | Specify the directory to the database you want to connect to. This field is available only to the HSQLDb In Process Persistent running mode.    Information noteNote: By default, if the database you specify in this field does not exist, it will be created automatically. If you want to change this default setting, modify the connection parameter set in the Additional JDBC parameter field in the Advanced settings view |
| Database | Enter the database name that you want to connect to. This field is available only to the HSQLDb In Process Persistent running mode and the HSQLDb In Memory running mode. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Query type | * Either Built-in or   Repository   . * Built-in: Fill in manually the   query statement or build it graphically using SQLBuilder * Repository: Select the relevant   query stored in the Repository. The Query field gets accordingly   filled in. |
| Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition. |
| Die on error | This check box is selected by default. Clear the check box to skip the row on error and complete the process for error-free rows. If needed, you can retrieve the rows on error via a Row > Rejects link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. When the running mode is HSQLDb In Process Persistent , you can set the connection property ifexists=true to allow connection to an existing database only and avoid creating a new database. |
| Propagate QUERY's recordset | Select this check box to insert the result of the query into a COLUMN of the current flow. Select this column from the use column list. |
| Commit every | Number of rows to be completed before committing batches of rows together into the DB. This option ensures transaction quality (but not rollback) and above all better performance on executions. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | QUERY: Indicates the query to be processed. This is a Flow variable and it returns a string.  For further information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteNote: A Flow variable means it functions during the execution of a component while an After variable means it functions after the execution of a component. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query and covers all possible SQL queries. |
| Connections | Outgoing links (from this component to another):  Row: Main; Reject; Iterate  Trigger: Run if; On Component Ok; On Component Error; On Subjob Ok; On Subjob Error.    Incoming links (from one component to this one):  Row: Main; Iterate  Trigger: Run if; On Component Ok; On Component Error; On Subjob Ok; On Subjob Error.    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
