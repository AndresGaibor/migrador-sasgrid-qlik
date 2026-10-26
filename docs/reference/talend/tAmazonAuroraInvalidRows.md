<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/amazon-aurora/tamazonaurorainvalidrows · versión 8.0 -->
# tAmazonAuroraInvalidRows

Last updated: 9/30/2026

Checks Amazon Aurora database rows against specific Data Quality patterns (regular
expression) or Data Quality rules (business rule). Only MySQL is supported.

tAmazonAuroraInvalidRows extracts database rows that do not match
a given data quality pattern or rule. You can then implement any required correction.

## tAmazonAuroraInvalidRows Standard properties

These properties are used to configure tAmazonAuroraInvalidRows
running in the Standard Job framework.

The Standard
tAmazonAuroraInvalidRows component belongs to the Cloud and the Databases families.

This component is available in Talend Data Management Platform, Talend Big Data Platform, Talend Real-Time Big Data Platform, Talend Data Services Platform and in
Talend Data Fabric.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

## Basic settings

| Properties | Description |
| --- | --- |
| Validation type | Either Regexp pattern validation or DQ rule validation.  Regex pattern validation: Validate data in the database against regex patterns.  DQ rule validation: Validate data in the database against data quality rules. |
| Property type | Either Built-in or Repository. Built-in: No property data stored centrally.  Repository: Select the repository file where Properties are stored. The fields that come after are pre-filled in using the fetched data. |
| DB Version | Select the MySQL version you are using. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Database server IP address. This field is available when Use an existing connection is cleared. |
| Port | Listening port number of DB server.  This field is available when Use an existing connection is cleared. |
| Database | Name of the database.  This field is available when Use an existing connection is cleared. |
| Username and Password | DB user authentication data.  To enter the password, click the [...] button next to the password field, enter the password in double quotes in the pop-up dialog box, and click OK to save the settings.  These fields are available when Use an existing connection is cleared. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields to be processed and passed on to the next component. The schema is either Built-in or stored remotely in the Repository.  Built-in: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in projects and Job designs. |
| Table Name | Enter the name of the table to be read. |
| Where clause | Enter a WHERE clause to define a row filter on the table. You can use the WHERE clause to filter the rows you want to analyze in the table. This WHERE clause enables you then to retrieve valid and invalid data that match certain specified criteria or conditions. |
| Analyzed column | Select from the schema list the column to analyze. |
| Custom pattern | Select this check box to define manually your own customized regular expression against which you want to check the database rows. |
| Patterns list | Select from the pattern list the pattern against which you want to check the DB rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection check box in the Basic settings.  Information noteNote: You can press Ctrl+Space to access a list of predefined global variables. |
| Enable stream | Select this check box to enable streaming over buffering. This allows reading from large tables without consuming large amount of memory in order to optimize the performance. |
| Trim all the String/Char columns | Select this check box to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from the defined columns.  This check box is not visible if Trim all the String/Char columns is selected. Clear Trim all the String/Char columns to enable Trim column. |
| tStatCatcher Statistics | Select this check box to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| **Usage rule** | This component is usually used as an intermediate component, and it requires an input component and an output component. |
