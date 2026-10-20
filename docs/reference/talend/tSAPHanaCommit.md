<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsaphanacommit · versión 8.0 -->
# tSAPHanaCommit

Last updated: 9/30/2026

Commits in one go, using a unique connection, a global transaction instead of doing
that on every row or every batch and thus provides gain in performance.

tSAPHanaCommit validates the data
processed through the Job into the connected database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSAPHanaCommit Standard properties

These properties are used to configure tSAPHanaCommit running in the Standard Job framework.

The Standard
tSAPHanaCommit component belongs to the Databases family.

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
| Component list | Select the tSAPHanaConnection component in the list if more than one connection is planned for the current Job. |
| Close Connection | This check box is selected by default. It allows you to close the database connection once the commit is done. Clear this check box to continue to use the selected connection once the component has performed its task.  Information noteWarning: If you want to use a Row  *>* Main connection to link tSAPHanaCommit to your Job, your data will be committed row by row. In this case, do not select the Close connection check box or your connection will be closed before the end of your first row commit. |

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is more commonly used with other tSAPHana\* components, especially with the tSAPHanaConnection and tSAPHanaRollback components.  Use this component if the Auto Commit option of the tSAPHanaConnection component is cleared. |
