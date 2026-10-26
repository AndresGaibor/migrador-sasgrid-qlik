<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/as400/tas400connection · versión 8.0 -->
# tAS400Connection

Last updated: 9/30/2026

Opens a connection to the specified database that can then be reused in the
subsequent subJob or subJobs.

tAS400Connection opens a connection to
the database for a current transaction.

## tAS400Connection Standard properties

These properties are used to configure tAS400Connection running in the Standard Job framework.

The Standard
tAS400Connection component belongs to the Databases and the ELT families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository.   * Built-in: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The fields that follow are completed   automatically using the data retrieved. |
| DB Version | Select the AS/400 version in use |
| Host | Database server IP address |
| Database | Name of the database |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings. |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tAS400\* components, especially with the tAS400Commit and tAS400Rollback components. |
