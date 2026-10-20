<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delta-lake/tdeltalakerow · versión 8.0 -->
# tDeltaLakeRow

Last updated: 9/30/2026

Acts on the actual DB structure or on the data (although without handling data) using the SQLBuilder tool to write easily your SQL statements.

tDeltaLakeRow is the component for any type database using a JDBC API. It executes the SQL query stated onto the specified database. The row suffix means the component implements a flow in the Job design although it doesn't provide output.

## tDeltaLakeRow Standard properties

These properties are used to configure tDeltaLakeRow running in the Standard Job framework.

The Standard
tDeltaLakeRow component belongs to the Databases family.

The component in this framework is available in all
subscription-based Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved.   This property is not available when a connection component is selected with the Use an existing connection option. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| JDBC URL | The JDBC URL of the Delta Lake database to be used, which begins with `jdbc:spark://` (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the JDBC URL of the Delta Lake database begins with `jdbc:databricks//` (already presented).  See section Configure JDBC URL at [JDBC and ODBC drivers and configuration parameters](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#id7) for related information.  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks//`. |
| Drivers | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. The driver JAR SparkJDBC42-2.6.14.1018.jar is used for the Delta Lake databases (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the `databricks-jdbc-{version_number}.jar` driver will be used (already presented).  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver).  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update the driver and other related settings manually for existing Jobs to make sure `databricks-jdbc-{version_number}.jar` is used. |
| Driver class | Enter the class name for the specified driver between double quotation marks. For the `SparkJDBC42-2.6.14.1018.jar` driver, the name to be entered is `com.simba.spark.jdbc.Driver` (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the `databricks-jdbc-{version_number}.jar` driver will be used and the driver class to be entered is `com.databricks.client.jdbc.Driver` (already presented).  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update driver class and other related settings manually for existing Jobs to make sure the driver class `com.databricks.client.jdbc.Driver` is used. |
| User Id and Password | The database user authentication data. See section Username and password authentication at [JDBC and ODBC drivers and configuration parameters](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#id7) for related information.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Table | Enter the name of the table to be processed. |
| Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.   * Built-In: Fill in the query statement in the Query field manually or click the [...] button next to the Query field to build the statement graphically using the SQLBuilder. * Repository: Select the relevant query stored in the Repository by clicking the [...] button next to it and in the pop-up Repository Content dialog box, select the query to be used, and the Query field will be automatically filled in.   If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected.  This component supports vector search capabilities, you can use this option to specify the query condition using the vector index previously created in Databricks.  For more information on vector searches in Databricks, see the corresponding [Databricks documentation](https://www.databricks.com/blog/introducing-databricks-vector-search-public-preview). |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Propagate record set | Select this check box to propagate the result of the query to the output flow. From the use column list displayed, you need to select a column into which the query result will be inserted.  This option allows the component to have a different schema from that of the preceding component. Moreover, the column that holds the query's recordset should be set to the Object type and this component is usually followed by a tParseRecordSet component. |
| Use PreparedStatement | Select this check box if you want to query the database using a prepared statement. In the Set PreparedStatement Parameters table displayed, specify the value for each parameter represented by a question mark `?` in the SQL statement defined in the Query field.   * Parameter Index: the position of the parameter in the SQL   statement. * Parameter Type: the data type of the parameter. * Parameter Value: the value of the parameter.   For a related use case of this property, see [Using PreparedStatement objects to query data](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this). |
| Commit every | Specify the number of rows to be processed before committing batches of rows together into the database.  This option ensures transaction quality (but not rollback) and, above all, better performance at executions. |
| Use query timeout | Select this check box to set a timeout period for the query in seconds. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | * tDeltaLakeRow covers all possible SQL queries for   any database using a Delta Lake connection. * tDeltaLakeRow supports query vector capabilities,   you can use it to perform actions on vector embeddings. For more information   on vector search, see the corresponding [Databricks documentation](https://www.databricks.com/blog/introducing-databricks-vector-search-public-preview). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
