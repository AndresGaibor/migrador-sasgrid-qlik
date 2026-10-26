<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/access/taccessconnection · versión 8.0 -->
# tAccessConnection

Last updated: 9/30/2026

Opens a connection to the specified database that can then be reused in the
subsequent subJob or subJobs.

tAccessConnection opens a connection to the database for
a current transaction.

## tAccessConnection Standard properties

These properties are used to configure tAccessConnection running in the Standard Job framework.

The Standard
tAccessConnection component belongs to the Databases and the ELT families.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .   * Built-in: No property data stored   centrally. * Repository: Select the repository file   in which the properties are stored. The fields that follow are completed   automatically using the data retrieved. |
| Database | Name of the database. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Use or register a shared DB Connection | Select this checkbox to share your database connection or fetch a database connection shared by a parent or child Job, and in the Shared DB connection name field displayed, enter the name for the shared database connection. This allows you to share one single database connection (except the database schema setting) among several database connection components from different Job levels that can be either parent or child.  This option is incompatible with the Use dynamic Job and Use an independent process to run subJob options of the tRunJob component. Using a shared connection together with a tRunJob component with either of these two options enabled will cause your Job to fail. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the DB connection you are creating. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tAccess\* components, especially with the tAccessCommit and tAccessRollback components. |
| Limitation | If you are using an ODBC driver, you need to work with Java 7, and make sure that your JVM and ODBC versions match up: both 64-bit or 32-bit.  When working with Java 8, this component supports only the General collation mode of Access.  From 8.0.1-R2022-11 monthly release onward, this component uses hsql.2.7.1.jar, a module built in JDK 11, only Java 11 and higher versions are supported. |

**Related concepts**  

* [Inserting data in parent/child tables](taccessinput-taccessconnection-tlogrow-inserting-data-in-parent-child-tables-standard-component-the)
