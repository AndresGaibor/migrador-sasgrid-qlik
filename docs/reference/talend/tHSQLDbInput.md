<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/hsqldb/thsqldbinput · versión 8.0 -->
# tHSQLDbInput

Last updated: 9/30/2026

Executes a DB query with a strictly defined order which must correspond to the
schema definition and then it passes on the field list to the next component via a Main row
link.

tHSQLDbInput reads a database and
extracts fields based on a query.

## tHSQLDbInput Standard properties

These properties are used to configure tHSQLDbInput running in the Standard Job framework.

The Standard
tHSQLDbInput component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Property type | * Either Built-in or   Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view.  For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| Running Mode | Select on the list the Server Mode corresponding to your DB setup among the four propositions :  HSQLDb Server, HSQLDb WebServer, HSQLDb In Process Persistent, HSQLDb In Memory. |
| Use TLS/SSL sockets | Select this check box to enable the secured mode if required. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database Alias | Alias name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| DB path | Specify the directory to the database you want to connect to. This field is available only to the HSQLDb In Process Persistent running mode.    Information noteNote: By default, if the database you specify in this field does not exist, it will be created automatically. If you want to change this default set­ting, modify the connection parameter set in the Additional JDBC parameter field in the Advanced settings view |
| Db name | Enter the database name that you want to connect to. This field is available only to the HSQLDb In Process Persistent running mode and the HSQLDb In Memory running mode. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.  This component offers the advantage of the   dynamic schema feature. This allows you to retrieve unknown columns from source   files or to copy batches of columns from a source without mapping each column   individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This   dynamic schema feature is designed for the purpose of retrieving unknown columns of a   table and is recommended to be used for this purpose only; it is not recommended for the   use of creating tables. * Built-in: The schema is created   and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: The schema already   exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  *If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected.* |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. When the running mode is HSQLDb In Process Persistent , you can set the connection property ifexists=true to allow connection to an existing database only and avoid creating a new database. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| tStat Catcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: Indicates the number of lines processed. This is an After variable and it returns an integer.  QUERY: Indicates the query to be processed. This is a Flow variable and it returns a string.  For further information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables).  Information noteNote: A Flow variable means it functions during the execution of a component while an After variable means it functions after the execution of a component. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component covers all possible SQL queries for HSQLDb databases. |
| Connections | Outgoing links (from this component to another):  Row: Main; Iterate  Trigger: Run if; On Component Ok; On Component Error; On Subjob Ok; On Subjob Error.    Incoming links (from one component to this one):  Row: Iterate;  Trigger: Run if; On Component Ok; On Component Error; On Subjob Ok; On Subjob Error.    For further information regarding connections, see [Using connections in a Job](/talend/r/en-US/8.0/studio-user-guide/using-connections-in-job). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
