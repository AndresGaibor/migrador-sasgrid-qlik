<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqloutputbulkexec · versión 8.0 -->
# tMSSqlOutputBulkExec

Last updated: 9/30/2026

Gains in performance during Insert operations to a Microsoft SQL Server
database.

The tMSSqlOutputBulk and tMSSqlBulkExec components are used together in a two step
process. In the first step, an output file is generated. In the second step, this file
is used in the INSERT operation used to feed a database. These two steps are fused
together in the tMSSqlOutputBulkExec
component.

## tMSSqlOutputBulkExec Standard properties

These properties are used to configure tMSSqlOutputBulkExec running in the Standard Job framework.

The Standard
tMSSqlOutputBulkExec component belongs to the Databases family.

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
| Action | Select the action to be carried out Bulk insert  Bulk update |
| Property type | Either Built-in or Repository .  * Built-in: No property data stored   centrally. * Repository: Select the repository   file in which the properties are stored. The fields that follow are   completed automatically using the data retrieved. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| JDBC Provider | Select the provider of the JDBC driver to be used, either Microsoft (the default, recommended) or Open source JTDS.  When Microsoft is selected, you need to download the Microsoft JDBC Driver for SQL Server on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774), unpack the downloaded zip file, choose a jar in the unzipped folder based on your JRE version, rename the jar to *mssql-jdbc.jar* and install it manually. For more information about choosing the jar, see the System Requirements information on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774).  Note that OSGi builds will not include any open source jTDS JDBC driver. If you need to build your Job containing this component as an OSGi bundle, use the official Microsoft JDBC driver; otherwise, this component will work only with Datasource with the jTDS JDBC driver properly installed in Talend Runtime. |
| Host | Enter the IP address or the hostname of the database server or the Azure Synapse Analytics to be used. If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in this field in the format of `{host_name}\{instance_name}`. In this case, you can leave the Port field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information.  Currently, only *localhost*, *127.0.0.1* or the exact IP address of the local machine is allowed for proper functioning. In other words, the database server must be installed on the same machine where Talend Studio is installed or where the Job using tMSSqlOutputBulkExec is deployed. |
| Port | Enter the listening port number of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in the Host field and leave this field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| DB name | Enter the name of the database |
| Schema | Enter the name of the database schema. |
| Username and Password | Enter the authentication data. To enter the password, click the [...] button next to the Password field, enter the password in double quotes in the pop-up dialog box, and then click OK.  You can use Type 2 integrated authentication on Windows by adding `integratedSecurity=true` in the Additional JDBC Parameters field and leave these two fields empty. See section Connecting with integrated authentication On Windows at [Building the connection URL](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?redirectedfrom=MSDN) for related information. |
| Table | Name of the table to be written. Note that only one table can be written at a time and that the table must exist for the insert operation to succeed. |
| Action on table | On the table defined, you can perform one of the following operations:  * None: No operation is carried   out. * Drop and create a table: The table is   removed and created again. * Create a table: The table does not   exist and gets created. * Create a table if not exists: The   table is created if it does not exist. * Truncate table: The table content is   deleted. You do not have the possibility to rollback the operation. * Clear a table: The table content is   deleted. You have the possibility to rollback the operation. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| File Name | Enter the name of the file to be generated and loaded. Information noteNote: This file can be on the same machine as the database server resides or on another machine. If the file is on the same machine as the database server resides, fill the path to the file in the form prompted in the field; if the file is on another machine, fill the universal naming convention (UNC) name (that is, `\\{Servername}\{Sharename}\{Path}\{Filename}`) of the file in this field. In the second case, you need to have the permission to read and write the file. See [Bulk importing to SQL Server from a remote data file](https://docs.microsoft.com/en-us/sql/relational-databases/import-export/import-bulk-data-by-using-bulk-insert-or-openrowset-bulk-sql-server?view=sql-server-ver16#bulk-importing-to-sql-server-from-a-remote-data-file) for related information. |
| Append | Select this checkbox to add the new rows at the end of the records |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair. For example, *encrypt=true;trustServerCertificate=false;* *hostNameInCertificate=\*.database.windows.net;loginTimeout=30;* for Azure SQL database connection.  This field is not available if the Use an existing connection check box is selected. |
| Authenticate using Azure Active Directory | When selected, this option allows you to pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   Read the Usage section of this document for information about Microsoft SQL Server/JDBC encryption requirements.  This option is only available when Microsoft is selected from the JDBC Provider dropdown list in the Basic settings view. |
| Enable always encrypted (Column encryption) | Select this option to use the Microsoft [Always encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15) feature to encrypt and protect your data. To use this option, you need to have previously stored your secrets with [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts):  * Application Client ID: Enter the client ID for the   registered application. This information can be found in the details of your   app under Azure Active Directory > App registrations > Essentials. * Application Client Secret: Enter the client password   for the registered application. This information can be found in the details   of your app under Azure Active Directory > App registrations > Certificates and secrets.   Some limitations regarding query operations and statements apply to this feature. For the exhaustive list of limitations, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15#limitations). |
| Field separator | Character, string, or regular expression to separate fields. |
| Row separator | String (ex: "\n"on Unix) to distinguish rows. |
| First row | Type in the number of the row where the action should start. |
| Include header | Select this checkbox to include the column header. |
| Code page | OEM code pages used to map a specific set of characters to numerical code point values. |
| Data file type | Select the type of data being handled. |
| Encoding | Select the encoding from the list or select Custom and define it manually. This field is compulsory for DB data handling. |
| tStatCatcher statistics | Select this checkbox to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rules | This component is mainly used when no particular transformation is required on the data to be loaded onto the database. Information noteImportant: Microsoft SQL Server/JDBC encryption requirements Starting with recent versions of the Microsoft SQL Server JDBC driver, TLS encryption is enabled by default (encrypt=true;trustServerCertificate=false). This enhances security, but if your SQL Server does not support encrypted connections or does not require clients to use TLS, you must set encrypt=false in the JDBC parameters of this component to connect successfully.   * For production or cloud environments using certificates signed by a   trusted authority (e.g., Azure, AWS), no changes are needed, the   default settings will work. * For servers using self-signed certificates, use   encrypt=true;trustServerCertificate=true or   specify the trust store details   (encrypt=true;trustStore=<your\_trust\_store>;trustStorePassword=<your\_trust\_store\_password>). * For non-secure development or test servers, set   encrypt=false in the additional JDBC parameters.   For more information on how to use connections with encryption properties, see [Microsoft SQL JDBC documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-ver17). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The database server must be installed on the same machine where Talend Studio is installed or where the Job using tMSSqlOutputBulkExec is deployed, so that the component functions properly. |
