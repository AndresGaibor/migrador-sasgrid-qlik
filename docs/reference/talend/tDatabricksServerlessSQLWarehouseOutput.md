<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/databricks/tdatabricksserverlesssqlwarehouseoutput-standard-properties · versión 8.0 -->
# tDatabricksServerlessSQLWarehouseOutput Standard properties

Last updated: 9/30/2026

These properties are used to configure tDatabricksServerlessSQLWarehouseOutput running in the Standard Job framework.

The Standard
tDatabricksServerlessSQLWarehouseOutput component belongs to the Databases family.

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
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If you make changes, the schema automatically becomes built-in.   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Guess Schema | Click this button to generate schema columns based on the settings of database table columns. |
| JDBC URL | The JDBC URL of the database to be used.  Information noteNote: There will be no migration operation for Databricks components when the 8.0.1-R2026-07 Talend Studio [Modules] monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks://`. |
| **Drivers** | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. For example, the driver jar `RedshiftJDBC41-1.1.13.1013.jar` for the Redshift database.  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver).  Information noteNote: There will be no migration operation for Databricks components when the 8.0.1-R2026-07 Talend Studio [Modules] monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks://`. |
| **Driver Class** | Enter the class name for the specified driver between double quotation marks. For example, for the `RedshiftJDBC41-1.1.13.1013.jar` driver, the name to be entered is `com.amazon.redshift.jdbc41.Driver`.  Information noteNote: There will be no migration operation for Databricks components when the 8.0.1-R2026-07 Talend Studio [Modules] monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks://`. |
| User Id and Password | The database user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  If you use the component's own DB configuration, your data source connection will be closed at the end of the component. To prevent this from happening, use a shared DB connection with the data source alias specified.  This property is not available when other connection component is selected from the Connection Component dropdown list. |
| Table | Enter the name of the table into which data will be written. |
| Data Action | Select an action to be performed on data of the table defined.   * Insert: Add   new entries to the table. If duplicates are found, the Job stops. * Update:   Make changes to existing entries. * Insert or   update: Insert a new record in the index pool. If the record with the   given reference already exists, an update would be made. * Update or   insert: Update the record with the given reference. If the record does   not exist in the index pool, a new record would be inserted. * Delete:   Remove entries corresponding to the input flow. |
| Clear data in table | Select this checkbox to clear data in the table before performing the selected action. |
| Die on error | Select the checkbox to stop the execution of the Job when an error occurs.  Clear the checkbox to skip any rows on error and complete the process for error-free rows.  When errors are skipped, you can collect the rows on error using a Row > Reject connection. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |
| Commit every | Specify the number of rows to be processed before committing batches of rows together into the database. |
| Additional Columns | This option allows you to call SQL functions to perform actions on columns, which are not insert, update or delete actions, or actions that require particular preprocessing. It is not offered if you create (with or without drop) the database table.   * Name: The name of the schema column to be inserted, or the   name of the schema column used to replace an existing column. * SQL expression: The SQL statement to be executed in order to   insert or replace relevant column. * Position: Select `Before`,   `After`, or `Replace` according to the   action to be performed on the reference column. * Reference column: The name of the reference column that can   be used to locate the new column to be inserted or that will be replaced. |
| Use field options | Select this check box and in the Fields options table displayed, select the check box for the corresponding column to customize a request, particularly if multiple actions are being carried out on the data.   * Key in update: Select the check box for the   corresponding column based on which data is updated. * Key in delete: Select the check box for the   corresponding column based on which data is deleted. * Updatable: Select the check box if data in the   corresponding column can be updated. * Insertable: Select the check box if data in   the corresponding column can be inserted. |
| Debug query mode | Select this check box to display each step during processing entries in a database. |
| Use batch | Select this check box to activate the batch mode for data processing, and in the Batch Size field displayed, specify the number of records to be processed in each batch. |
| Query timeout | Select this option to set a timeout period for queries or batch queries. The Job is terminated if a query times out. You can set the timeout period in seconds in the Timeout field. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |
| NB\_LINE | The number of rows processed. This is an After variable and it returns an integer. |
| NB\_LINE\_INSERTED | The number of rows inserted. This is an After variable and it returns an integer. |
| NB\_LINE\_UPDATED | The number of rows updated. This is an After variable and it returns an integer. |
| NB\_LINE\_DELETED | The number of rows deleted. This is an After variable and it returns an integer. |
| NB\_LINE\_REJECTED | The number of rows rejected. This is an After variable and it returns an integer. |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component must be used as an output component. It supports writing data to Databricks serverless SQL warehouse tables and can create a reject flow using a Row > Rejects link. |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
