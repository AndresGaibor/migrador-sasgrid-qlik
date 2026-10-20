<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/netsuite/tnetsuiteoutput · versión 8.0 -->
# tNetSuiteOutput

Last updated: 9/30/2026

Invokes the NetSuite SOAP service and inserts, updates, or removes data on the
NetSuite SOAP server.

Information noteNote:

* This component works with two tNetSuiteOutput components: one for NetSuite version
  2019 databases and the other for NetSuite version 2019/2021/2025 databases.
* This component is available only when you have installed
  the 8.0.1-R2023-02 Talend Studio monthly
  update or a later one delivered by Talend. For
  more information, check with your administrator.

## tNetSuiteOutput Standard properties

These properties are used to configure tNetsuiteOutput running
in the Standard Job framework.

The Standard
tNetsuiteOutput component belongs to the Business
and the Cloud families.

## Basic settings

This component serves as an entry point for the NetSuite version 2019 databases and
NetSuite version 2019/2021 databases. To configure this component, select a NetSuite
database version from the Version drop-down list and click
Apply on its Basic settings view.

* Select NetSuite Deprecated from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite version 2019
  database. See [tNetSuiteOutput (v2019)](/talend/en-US/components/8.0/netsuite/tnetsuiteoutput-deprecated)
  for information about the component options.
* Select NetSuite SOAP from the
  Version drop-down list in the Basic
  settings view if you are using a NetSuite database that is of
  version 2019, 2021 or 2025. See [tNetSuiteOutput (v2019/2021/2025)](/talend/en-US/components/8.0/netsuite/tnetsuitev2019output) for information about the component
  options.

Information noteNote:

* For Jobs that contain tNetsuiteV2019Connection, tNetsuiteV2019Input, and
  tNetsuiteV2019Output components, the NetSuite components will be replaced by the
  corresponding NetSuite SOAP components when the Jobs are migrated, with the
  options set.
* For Jobs that contain NetSuite components that marked as deprecated,
  the NetSuite components will be replaced with legacy NetSuite components when the
  Jobs are migrated. In such Jobs, legacy NetSuite components can be switched to the
  new NetSuite components where some options will be pre-filled to aid the
  migration.
