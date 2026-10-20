<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/delta-lake/tdeltalakeconnection · versión 8.0 -->
# tDeltaLakeConnection

Last updated: 9/30/2026

Opens a connection to the specified database that can then be reused in the subsequent subJob or
subJobs.

## tDeltaLakeConnection Standard properties

These properties are used to configure tDeltaLakeConnection running in the Standard Job framework.

The Standard
tDeltaLakeConnection component belongs to the Databases and the ELT families.

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
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| JDBC URL | The JDBC URL of the Delta Lake database to be used, which begins with `jdbc:spark://` (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the JDBC URL of the Delta Lake database begins with `jdbc:databricks//` (already presented).  See section Configure JDBC URL at [JDBC and ODBC drivers and configuration parameters](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#id7) for related information.  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update the JDBC URL and other related settings manually for existing Jobs to make sure the JDBC URL begins with `jdbc:databricks//`. |
| Drivers | Complete this table to load the driver JARs needed. To do this, click the [+] button under the table to add as many rows as needed, each row for a driver JAR, then select the cell and click the [...] button at the right side of the cell to open the Module dialog box from which you can select the driver JAR to be used. The driver JAR SparkJDBC42-2.6.14.1018.jar is used for the Delta Lake databases (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the `databricks-jdbc-{version_number}.jar` driver will be used (already presented).  For more information, see [Importing a database driver](/talend/r/en-US/8.0/components/jdbc/importing-database-driver).  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update the driver and other related settings manually for existing Jobs to make sure `databricks-jdbc-{version_number}.jar` is used. |
| Driver class | Enter the class name for the specified driver between double quotation marks. For the `SparkJDBC42-2.6.14.1018.jar` driver, the name to be entered is `com.simba.spark.jdbc.Driver` (already presented). If you have installed the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend, the `databricks-jdbc-{version_number}.jar` driver will be used and the driver class to be entered is `com.databricks.client.jdbc.Driver` (already presented).  Information noteNote: There will be no migration operation for Delta Lake components when the 8.0.1-R2023-05 Talend Studio Monthly update or a later one delivered by Talend is installed. In this case, you may need to update driver class and other related settings manually for existing Jobs to make sure the driver class `com.databricks.client.jdbc.Driver` is used. |
| User Id and Password | The database user authentication data. See section Username and password authentication at [JDBC and ODBC drivers and configuration parameters](https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#id7) for related information.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail.  This checkbox is not available when the Specify a data source alias checkbox is selected. |
| Specify a data source alias | Select this checkbox and in the Data source alias field displayed, specify the alias of a data source created on Talend Runtime side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in Talend Runtime.  This checkbox is not available when the Use or register a shared DB Connection checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use Auto-Commit | Select this checkbox to activate the auto commit mode. |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tDeltaLake\* components. |
