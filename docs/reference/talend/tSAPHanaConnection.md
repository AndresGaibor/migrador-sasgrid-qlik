<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsaphanaconnection · versión 8.0 -->
# tSAPHanaConnection

Last updated: 9/30/2026

Establishes a SAP HANA connection to be reused by other SAP HANA components in your
Job.

tSAPHanaConnection opens a connection to the database
for a current transaction.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSAPHanaConnection Standard properties

These properties are used to configure tSAPHanaConnection running in the Standard Job framework.

The Standard
tSAPHanaConnection component belongs to the Databases and the ELT families.

If you have installed the 8.0.1-R2023-01 Talend Studio Monthly
update or a later one delivered by Talend, this
component is available in all Talend
subscription-based products; otherwise it is only available in all Talend products
with Big Data and in Talend Data Fabric.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Host | Database server IP address. |
| Port | Listening port number of database server. |
| Schema | Name of the database schema. |
| Username and Password | Database authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings. |
| Additional JDBC Parameters | Specify additional connection properties in the database connection you are creating. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Auto Commit | Select this checkbox to commit any changes to the database automatically upon the transaction.  With this checkbox selected, you cannot use the corresponding commit component to commit changes to the database; likewise, when using the corresponding commit component, this checkbox has to be cleared. By default, the auto commit function is disabled and changes must be committed explicitly using the corresponding commit component.  Note that the auto commit function commits each SQL statement as a single transaction immediately after the statement is executed while the commit component does not commit only until all of the statements are executed. For this reason, if you need more room to manage your transactions in a Job, it is recommended to use the commit component. |
| tStatCatcher Statistics | Select this check box to gather the Job processing metadata at a Job level as well as at each component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tSAPHana\* components, especially with the tSAPHanaCommit and tSAPHanaRollback components. |
| **Support** | tSAPHanaConnection should be used to interact with the ERP part of SAP, including S4/HANA. |
