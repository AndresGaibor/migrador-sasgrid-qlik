<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/oracle/toracleinvalidrows · versión 8.0 -->
# tOracleInvalidRows

Last updated: 9/30/2026

Checks Oracle database rows against specific Data Quality patterns (regular
expression) or Data Quality rules (business rule).

tOracleInvalidRows extracts database rows that do not match
a given data quality pattern or rule. You can then implement any required correction.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tOracleInvalidRows Standard properties

These properties are used to configure tOracleInvalidRows running in the Standard Job framework.

The Standard
tOracleInvalidRows component belongs to the Data Quality and the Databases families.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Validation type | * Either Regex pattern validation   or DQ rule validation. * Regex pattern validation:   Validate data in the database against regex patterns. * DQ rule validation: Validate data   in the database against DQ rules. |
| Property type | * Either Built-in or Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository   file where Properties are stored. The fields that come after are   pre-filled in using the fetched data. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Note that connections that are of WALLET type are for the tCreateTable component, the tOracleInput component, and the tOracleOutput component only. Make sure that the connection selected is not of the WALLET type to prevent possible errors.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Connection Type | Drop-down list of available drivers. |
| DB Version | Select the Oracle version you are using. |
| Host | Database server IP address. |
| Port | Listening port number of DB server. |
| Database | Name of the database. |
| Oracle schema | Name of the Oracle schema. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | * A schema is a row description, it defines the number of fields to   be processed and passed on to the next component. The schema is   either Built-in or stored remotely   in the Repository. * Built-in: You create and store   the schema locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). * Repository: You have already   created the schema and stored it in the Repository and thus reuse it   when needed. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| Table Name | Enter the name of the table to be read. |
| Where clause | Enter a WHERE clause to define a row filter on the table.  You can use the WHERE clause to filter the rows you want to analyze in the table. This WHERE clause enables you then to retrieve valid and invalid data that match certain specified criteria or conditions. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Convert XML type to Java Type | Select this check box and then use the table to convert the types of the defined columns to Java types. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |
| Use cursor | Select this check box to specify the number of rows you want to work with at at a given time. This option optimises performance. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from the defined columns.  This check box is not visible if Trim all the String/Char columns is selected. Clear Trim all the String/Char columns to enable Trim column. |
| No null values | Select this check box to improve the performance if there are no null values. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows read by an input component or transferred to an output component. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component can be used as a start or intermediary step. It requires an output flow. |
| Information noteNote: Available only for Regex pattern validation. | Analyzed column |
| Information noteNote: Available only for Regex pattern validation. | Custom pattern |
| Information noteNote: Available only for Regex pattern validation. | Patterns list |
| Information noteNote: Available only for DQ rule validation. | DQ rule list |
| Information noteNote: Available only for DQ rule validation. | * Query type |
| Information noteNote: Available only for DQ rule validation. | Guess Query |
| Information noteNote: Available only for DQ rule validation. | Guess schema |
| Information noteNote: Available only for DQ rule validation. | Query |
