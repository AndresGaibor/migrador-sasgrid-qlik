<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/sap/tsaphanaclose · versión 8.0 -->
# tSAPHanaClose

Last updated: 9/30/2026

Closes a connection to a SAP HANA database.

This component is not shipped with your Talend Studio by
default. You need to install it using the Feature Manager. For more information, see [Installing features using the Feature Manager](/talend/r/en-US/8.0/studio-user-guide/install-features-to-talend-studio).

## tSAPHanaClose Standard properties

These properties are used to configure tSAPHanaClose running in the Standard Job framework.

The Standard
tSAPHanaClose component belongs to the Databases family.

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

## Advanced settings

| Properties | Description |
| --- | --- |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is to be used along with SAP HANA components, especially with tSAPHanaConnection and tSAPHanaCommit. |
| **Support** | tSAPHanaClose should be used to interact with the ERP part of SAP, including S4/HANA. |
