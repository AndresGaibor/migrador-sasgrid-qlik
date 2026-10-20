<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqloutputbulk · versión 8.0 -->
# tMSSqlOutputBulk

Last updated: 9/30/2026

Prepares the file to be used as parameter in the INSERT query to
feed the MSSql database.

The tMSSqlOutputBulk and tMSSqlBulkExec components are used together in a two step process. In
the first step, an output file is generated. In the second step, this file is used in
the INSERT operation used to feed a database. These two steps are fused together in the
tMSSqlOutputBulkExec component, detailed in a
separate section. The advantage of using a two step process is that the data can be
transformed before it is loaded in the database.

tMSSqlOutputBulk writes a file with columns based on the
defined delimiter and the MSSql standards.

## tMSSqlOutputBulk Standard properties

These properties are used to configure tMSSqlOutputBulk running in the Standard Job framework.

The Standard
tMSSqlOutputBulk component belongs to the Databases family.

The component in this framework is available in all Talend
products.

Information noteNote: This component is a specific version of a dynamic database
connector. The properties related to database settings vary depending on your database
type selection. For more information about dynamic database connectors, see [DB Generic components](/talend/r/en-US/8.0/components/db-generic/db-generic-component).

Information noteNote: When building a Job as an OSGI Bundle for ESB, MS SQL Server
drivers jtds and mssql-jdbc used by the SQL Server components are not included in the build
artifact. To run the artifact in Talend Runtime, you need
to deploy the drivers manually by copying the drivers to the
<TalendRuntimePath>/lib folder and restart Talend Runtime.

## Basic settings

| Properties | Description |
| --- | --- |
| Database | Select the desired database type from the list and click Apply. |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| File Name | Enter the name of the file to be generated. Information noteNote: This file can be on the same machine as the database server resides or on another machine. If the file is on the same machine as the database server resides, fill the path to the file in the form prompted in the field; if the file is on another machine, fill the universal naming convention (UNC) name (that is, `\\{Servername}\{Sharename}\{Path}\{Filename}`) of the file in this field. In the second case, you need to have the permission to write the file. See [Bulk importing to SQL Server from a remote data file](https://docs.microsoft.com/en-us/sql/relational-databases/import-export/import-bulk-data-by-using-bulk-insert-or-openrowset-bulk-sql-server?view=sql-server-ver16#bulk-importing-to-sql-server-from-a-remote-data-file) for related information. |
| Append | Select this checkbox to add the new rows at the end of the records. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Authenticate using Azure Active Directory | When selected, this option allows you to pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   Read the Usage section of this document for information about Microsoft SQL Server/JDBC encryption requirements. |
| Row separator | String (ex: "\n"on Unix) to distinguish rows. |
| Field separator | Character, string, or regular expression to separate fields. |
| Include header | Select this check to include the column header. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStaCatcher statistics | Select this checkbox to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rules | This component is to be used along with tMSSqlBulkExec component. Used together they offer gains in performance while feeding an MSSql database. Information noteImportant: Microsoft SQL Server/JDBC encryption requirements Starting with recent versions of the Microsoft SQL Server JDBC driver, TLS encryption is enabled by default (encrypt=true;trustServerCertificate=false). This enhances security, but if your SQL Server does not support encrypted connections or does not require clients to use TLS, you must set encrypt=false in the JDBC parameters of this component to connect successfully.   * For production or cloud environments using certificates signed by a   trusted authority (e.g., Azure, AWS), no changes are needed, the   default settings will work. * For servers using self-signed certificates, use   encrypt=true;trustServerCertificate=true or   specify the trust store details   (encrypt=true;trustStore=<your\_trust\_store>;trustStorePassword=<your\_trust\_store\_password>). * For non-secure development or test servers, set   encrypt=false in the additional JDBC parameters.   For more information on how to use connections with encryption properties, see [Microsoft SQL JDBC documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-ver17). |
| Component family | Databases/MS SQL Server |
