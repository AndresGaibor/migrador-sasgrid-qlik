<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/databricks/tdatabricksserverlesssqlwarehouseinput-standard-properties · versión 8.0 -->
# tDatabricksServerlessSQLWarehouseInput Standard properties

Last updated: 9/30/2026

These properties are used to configure tDatabricksServerlessSQLWarehouseInput running in the Standard Job framework.

The Standard
tDatabricksServerlessSQLWarehouseInput component belongs to the Databases family.

This component supports Databricks serverless SQL warehouse by using Databricks JDBC connectivity.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in.   This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined. |
| Component list | Select the component that opens the database connection to be reused by this component. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables. |
| Guess Schema | Click this button to generate schema columns based on the query defined in the Query field. |
| JDBC URL | The JDBC URL of the database to be used.  Information noteNote: There will be no migration operation for Databricks components when the 8.0.1-R2026-07 Talend Studio [Modules] monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks://`. |
| **Drivers** | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver).  Information noteNote: There will be no migration operation for Databricks components when the 8.0.1-R2026-07 Talend Studio [Modules] monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks://`. |
| **Driver Class** | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`.  Information noteNote: There will be no migration operation for Databricks components when the 8.0.1-R2026-07 Talend Studio [Modules] monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks://`. |
| User Id and Password | The database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Table | Enter the name of the table from which data will be retrieved. |
| Query Type and Query | Specify the database query statement paying particularly attention to the sequence of the fields which must correspond to the schema definition.   * Built-In: Fill in the query statement in the Query field manually or click the [...] button next to the Query field to build the statement graphically using the SQLBuilder. * Repository: Select the relevant query stored in the Repository by clicking the [...] button next to it and in the pop-up Repository Content dialog box, select the query to be used, and the Query field will be automatically filled in.   If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Use cursor | Select this check box to specify the number of rows you want to work with at any given time. This option optimises performance. |
| Trim all the string/CHAR columns | Select this check box to remove leading whitespace and trailing whitespace from all String/Char columns. |
| Enable mapping file for dynamic | Select this checkbox to use the specified metadata mapping file when reading data from a dynamic type column. This checkbox is cleared by default.  With this checkbox selected, you can specify the metadata mapping file to use in the Mapping File dropdown list. |
| Allow special character in dynamic table name | Select this option to use the actual column names of the input table in the dynamic column. This option prevents special characters (for example, `$`) in the input table column names from being converted into `_` in the dynamic column.  This option is selected by default. |
| Use PreparedStatement | Select this check box if you want to query the database using a prepared statement. In the Set PreparedStatement Parameters table displayed, specify the value for each parameter represented by a question mark `?` in the SQL statement defined in the Query field.   * Parameter Index: the position of the parameter in the SQL   statement. * Parameter Type: the data type of the parameter. * Parameter Value: the value of the parameter.   For a related use case of this property, see [Using PreparedStatement objects to query data](/talend/en-US/components/8.0/mysql/tmysqlrow-tparserecordset-tfileinputdelimited-tfileoutputdelimited-using-preparedstatement-objects-to-query-data-standard-component-this). |
| Query timeout | Select this option to set a timeout period for queries or batch queries. The Job is terminated if a query times out. You can set the timeout period in seconds in the Timeout field. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is a start component of a data flow in your Job. It sends data to other components through a Row > Main link. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
