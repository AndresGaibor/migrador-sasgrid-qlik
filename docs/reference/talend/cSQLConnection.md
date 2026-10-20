<!-- fuente: https://help.qlik.com/talend/en-US/mediation-components/8.0/mediation-database/csqlconnection · versión 8.0 -->
# cSQLConnection

Last updated: 9/30/2026

Opens a connection to the specified database that can then be reused in the
subsequent subRoute.

Information noteNote: This component is available only if you have installed the R2022-11 Talend Studio Monthly
update or a later one delivered by Talend. For
more information, check with your administrator.

## cSQLConnection Standard properties

These properties are used to configure cSQLConnection running in
the Standard Route framework.

The Standard
cSQLConnection component belongs to the Connectivity family.

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   You can drag and drop a JDBC connection from the Metadata node of the Repository tree view to the design workspace to create a cSQLConnection component.  Information noteNote: This option is available only if you have installed the R2023-05 Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Driver Class | Enter the class name for the specified driver between double quotation marks. |
| Driver JAR | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/jdbc/importing-database-driver). |
| JDBC URL | The JDBC URL of the database to be used. |
| Authentication | Select this check box to enter the database user authentication data. The User Id and Password fields appear when this check box is selected.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Specify a data source alias | Select this check box and in the Data source alias field displayed, specify the alias of a data source created on the Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Route in Talend Runtime. |
| Use Transaction | Select this check box to enable local transaction for the connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Initial Connections | Specify the maximum number of initial connections. |
| Max Connections | Specify the maximum number of connections. |
| Min Idle Connections | Specify the minimum number of idle connections (connections not used). |
| Max Idle Connections | Specify the maximum number of idle connections (connections not used). |
| Set Timeouts | Select this check box to set the timeout options.  * Query Timeout (sec): Set a timeout period for the   query in seconds. A value of -1 means that no timeout is   set. * Max Connection duration (sec): Set a maximum   duration of the connection in seconds. A value of -1   means that no timeout is set. |
| Use validation query | Select this check box to validate the database connection using a query.  * Validation Query Timeout (sec): Set a timeout period   for the validation query in seconds. A value of -1 means   that no timeout is set. * Validation query: Enter an SQL SELECT statement to   validate the connection. |
| Use SQL Initialization | Select this check box to initialize the database server by entering a query in the Init Query box. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | cSQLConnection can be added directly in a Route without any input or output component linked. |
| Limitation | n/a |

**Related concepts**  

* [Writing and reading data in an H2 database with an SQL statement](csql-writing-and-reading-data-in-an-h2-database-with-an-sql-statement)
