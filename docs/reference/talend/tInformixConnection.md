<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/informix/tinformixconnection · versión 8.0 -->
# tInformixConnection

Last updated: 9/30/2026

Opens a connection to the specified database that can then be reused in the
subsequent subJob or subJobs.

tInformixConnection is closely related to
tInformixCommit and tInformixRollback. They are
generally used along with tInformixConnection, with
tInformixConnection opening the connection for the transaction.

## tInformixConnection Standard properties

These properties are used to configure tInformixConnection running in the Standard Job framework.

The Standard
tInformixConnection component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | * Either Built-in or   Repository. * Built-in: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The fields that follow are completed   automatically using the data retrieved. |
| Host | Database server IP address. |
| Port | DB server listening port. |
| Database | Name of the database. |
| Schema | Name of the schema |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Instance | Name of the Informix instance to be used. This information can generally be found in the SQL hosts file. |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Use Transaction | Clear this check box when the database is configured in NO\_LOG. mode. If the check box is selected, you can choose whether to activate the Auto Commit option. |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| tStatCatcher Statistics | Select this check box to collect the log data at a component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is generally used with other Informix components, particularly tInformixCommit and tInformixRollback. |
| Database Family | Databases/Informix |
| Limitation | This component requires installation of its related jar files. |
