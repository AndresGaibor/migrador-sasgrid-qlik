<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/exasol/texasolrow · versión 8.0 -->
# tExasolRow

Last updated: 9/30/2026

Executes SQL queries on an Exasol database.

Depending on the nature of the query and the database,
tExasolRow acts on the actual structure of the
database, or indeed the data, although without modifying them. The Row suffix indicates
that it is used to channel a flow in a Job although it does not produce any output
data.

## tExasolRow Standard properties

These properties are used to configure tExasolRow running in the Standard Job
framework.

The Standard
tExasolRow component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Either Built-In or Repository.   * Built-In: No property data   stored centrally. * Repository: Select the   repository file in which the properties are stored. The database   connection fields that follow are completed automatically using   the data retrieved. |
| Use an existing connection | Select this check box and from the list displayed select the relevant connection component to reuse the connection details you have already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the host or host list of the Exasol database servers. Exasol can run in a cluster environment. The valid value can be a simple IP address (for example, *172.16.173.128*), an IP range list (for example, *172.16.173.128..130* that represents three servers *172.16.173.128*, *172.16.173.129*, and *172.16.173.130*), or a comma-separated host list (for example, *server1,server2,server3*) of the Exasol database cluster. |
| Port | Enter the listening port number of the Exasol database cluster. |
| Schema name | Enter the name of the schema you want to use. |
| Username and Password | Enter the user authentication data to access the Exasol database.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | * A schema is a row description. It defines the number of fields   (columns) to be processed and passed on to the next component. When you create a Spark   Job, avoid the reserved word `line` when naming the   fields.    + Built-In: You create and store the schema locally for this component     only.   + Repository: You have already created the schema and stored it in the     Repository. You can reuse it in various projects and Job designs. * Click Edit   schema to make changes to the schema. If the current schema is of the Repository type, three options are available:    + View schema: choose this     option to view the schema only.   + Change to built-in property:     choose this option to change the schema to Built-in for local changes.   + Update repository connection:     choose this option to change the schema stored in the repository and decide whether     to propagate the changes to all the Jobs upon completion.  If you just want to     propagate the changes to the current Job, you can select No upon completion and choose this schema metadata     again in the Repository Content     window. |
| Table Name | Enter the name of the table to be processed. |
| Query Type | Either Built-In or Repository .   * Built-In: Enter the query   manually or with the help of the SQLBuilder. * Repository: Select the   appropriate query from the Repository. The Query field is   then completed automatically. |
| Guess Query | Click the Guess Query button to generate the query that corresponds to the table schema in the Query field. |
| Query | Enter the database query paying particularly attention to the proper sequence of the fields in order to match the schema definition. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows. When errors are skipped, you can collect the rows on error using a Row > Reject link. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair, for example, *encryption=1;clientname=Talend*.  This field is not available if the Use an existing connection check box is selected. |
| Propagate QUERY's recordset | Select this check box to insert the query results in one of the flow columns. Select the particular column from the use column list. |
| Use PreparedStatement | Select this check box to use prepared statements and in the Set PreparedStatement Parameters table displayed, add as many parameters as needed and set the following attributes for each parameter:   * Parameter Index: enter the   index of the prepared statement parameter. * Parameter Type: click in the   cell and select the type of the parameter from the list. * Parameter Value: enter the   value of the parameter. |
| Commit every | Enter the number of rows to be included in each batch before the data is written. This option guarantees the quality of the transaction (although there is no rollback option) and improves performance. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers query flexibility as it covers all possible SQL query requirements. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
