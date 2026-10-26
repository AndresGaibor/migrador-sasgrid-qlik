<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-athena/tathenarow · versión 8.0 -->
# tAthenaRow

Last updated: 9/30/2026

Acts on the actual DB structure or on the data (although without handling data)
using the SQLBuilder tool to write easily your SQL statements.

tAthenaRow is the component for any type database using a
JDBC API. It executes the SQL query stated onto the specified database. The row suffix
means the component implements a flow in the Job design although it doesn't provide
output.

## tAthenaRow Standard properties

These properties are used to configure tAthenaRow running in the Standard Job
framework.

The Standard
tAthenaRow component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select Athena in the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Component list | Select the component that opens the database connection to be reused by this component. |
| JDBC URL | The JDBC URL of the database. For example, the Athena JDBC URL should start with `jdbc:athena://`. |
| Drivers | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver JAR `athena-jdbc-uber-3.7.0.jar` for the Athena database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver). |
| Driver Class | Enter the class name for the driver between double quotation marks. For example, for the `athena-jdbc-uber-3.7.0.jar` driver, the name to be entered is `com.amazon.athena.jdbc.AthenaDriver`. |
| User Id and Password | The database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Table | Enter the name of the table to be processed. |
| Query Type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.   * Built-In: Fill in the query statement in the Query field manually or click the [...] button next to the Query field to build the statement graphically using the SQLBuilder. * Repository: Select the relevant query stored in the Repository by clicking the [...] button next to it and in the pop-up Repository Content dialog box, select the query to be used, and the Query field will be automatically filled in. |
| Guess Query | Click this button to generate query in the Query field based on the defined table and schema. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Propagate record set | Select this check box to propagate the result of the query to the output flow. From the use column list displayed, you need to select a column into which the query result will be inserted.  This option allows the component to have a different schema from that of the preceding component. Moreover, the column that holds the query's recordset should be set to the Object type and this component is usually followed by a tParseRecordSet component. |
| Use PreparedStatement | Select this check box if you want to query the database using a prepared statement. In the Set PreparedStatement Parameters table displayed, specify the value for each parameter represented by a question mark `?` in the SQL statement defined in the Query field.   * Parameter Index: the position of the parameter in the SQL   statement. * Parameter Type: the data type of the parameter. * Parameter Value: the value of the parameter.   For a related use case of this property, see [Using PreparedStatement objects to query data](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this). |
| Use query timeout | Select this option to set a timeout period for the query or the batch query. The Job will be terminated if the query or the batch query is timed out. You can set the timeout period (in seconds) in the Timeout field. Information noteNote:  * It varies with the driver implementations whether this option applies to   an individual SQL statement or a set of SQL statements (that is, a batch   query). Refer to your driver vendor documentation for details. * This option is available only when you have installed the R2021-12   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| Detect error on multiple statements | Select this option to detect errors that occur when executing the SQL query statements. With this option selected, an error caused by a SQL query statement stops the Job execution and will be prompted. |
| Commit every | Specify the number of rows to be processed before committing batches of rows together into the database.  This option ensures transaction quality (but not rollback) and, above all, better performance at executions.  When used with an existing JDBC connection, tJDBCRow ignores this option at runtime. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component offers the flexibility of the DB query for any database using a JDBC connection and covers all possible SQL queries. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
