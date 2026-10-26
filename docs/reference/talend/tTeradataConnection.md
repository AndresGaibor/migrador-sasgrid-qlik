<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/teradata/tteradataconnection · versión 8.0 -->
# tTeradataConnection

Last updated: 9/30/2026

Opens a connection to the specified database that can then be reused in the
subsequent subJob or subJobs.

tTeradataConnection opens a
connection to the database for a current transaction.

## tTeradataConnection Standard properties

These properties are used to configure tTeradataConnection running in the Standard Job framework.

The Standard
tTeradataConnection component belongs to the Databases and the ELT families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-In or Repository.   * Built-In: No property data stored centrally. * Repository: Select the repository file where the   properties are stored. The fields that follow are completed automatically using the data   retrieved. |
| Host | Database server IP address. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Additional JDBC parameters | Specify additional connection properties in the existing DB connection, to allow specific character set support. E.G.: CHARSET=KANJISJIS\_OS to get support of Japanese characters.  Information noteNote: You can set the encoding parameters through this field. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Query band | Select this check box to use the Teradata Query Banding feature to add metadata to the query to be processed, such as the user running the query. This can help you, for example, identify the origin of this query.  Once selecting the check box, the Query Band parameters table is displayed, in which you need to enter the metadata information to be added. This information takes the form of key/value pairs, for example, *DpID* in the Key column and *Finance* in the Value column.  This check box actually generates the SET QUERY\_BAND FOR SESSION statement with the key/value pairs declared in the Query Band parameters table. For further information about this statement, see the [Teradata documentation](https://docs.teradata.com/search/all?query=End+logging+syntax). |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tTeradata\* components, especially with the tTeradataCommit and tTeradataRollback components. |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |
