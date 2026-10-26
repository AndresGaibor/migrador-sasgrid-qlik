<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsaphanarow · versión 8.0 -->
# tSAPHanaRow

Last updated: 9/30/2026

Acts on the actual database structure or on the data (although without handling
data).

tSAPHanaRow is the specific
component for this database query. It executes the SQL query stated onto the specified
database. The row suffix means the component implements a flow in the Job design
although it does not provide output.

The SQLBuilder tool helps you write easily your SQL statements.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSAPHanaRow Standard properties

These properties are used to configure tSAPHanaRow running in the Standard Job framework.

The Standard
tSAPHanaRow component belongs to the Databases family.

If you have installed the 8.0.1-R2023-01 Talend Studio Monthly
update or a later one delivered by Talend, this
component is available in all Talend
subscription-based products; otherwise it is only available in all Talend products
with Big Data and in Talend Data Fabric.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Property type | * Either Built-in or Repository   . * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Host | Database server IP address. |
| Port | Listening port number of database server. |
| Username and Password | Database authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit Schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields. * Built-in: The schema is created   and stored locally for this component only. * Repository: The schema already   exists and is stored in the Repository, hence can be reused. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Name of the table to be written. Note that only one table can be written at a time. |
| Query Type | * Either Built-in or Repository. * Built-in: Fill in manually the   query statement or build it graphically using SQLBuilder. * Repository: Select the relevant   query stored in the Repository. The Query field gets accordingly   filled in. |
| Guess Query | Click the Guess Query button to generate the query which corresponds to your table schema in the Query field. |
| Query | Enter your database query paying particularly attention to properly sequence the fields in order to match the schema definition. |
| Die on error | This check box is cleared by default. This means that Die on error skips the row when an error is encountered and completes the process for rows without errors. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties in the database connection you are creating. This option is not available if you have selected Use an existing connection check box in the Basic settings. |
| Propagate QUERY's recordset | Select this check box to insert the result of the query into a column of the current flow. Select this column from the use column list.  Information noteNote: This option allows the component to have a different schema from that of the preceding component. Moreover, the column that holds the QUERY's recordset should be set to the type of *Object* and this component is usually followed by tParseRecordSet. |
| Commit every | Number of rows to be completed before committing batches of rows together into the database. This option ensures transaction quality (but not rollback) and above all better performance on executions. |
| Use PreparedStatement | Select this check box if you want to query the database using a PreparedStatement. In the Set PreparedStatement Parameter table, define the parameters represented by "?" in the SQL instruction of the Query field in the Basic Settings tab.  Parameter Index: Enter the parameter position in the SQL instruction.  Parameter Type: Enter the parameter type.  Parameter Value: Enter the parameter value.    Information noteNote: This option is very useful if you need to execute the same query several times. Performance levels are increased. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the database query and covers all possible SQL queries. |
| **Support** | tSAPHanaRow should be used to interact with the ERP part of SAP, including S4/HANA. |
