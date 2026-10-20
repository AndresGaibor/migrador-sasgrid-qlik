<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/scd/tmssqlscd · versión 8.0 -->
# tMSSqlSCD

Last updated: 9/30/2026

Tracks and reflects changes in a dedicated SCD table in a Microsoft SQL Server or
Azure SQL database.

tMSSqlSCD addresses Slowly Changing Dimension needs,
reading regularly a source of data and logging the changes into a dedicated SCD table.

## tMSSqlSCD Standard properties

These properties are used to configure tMSSqlSCD running in the Standard Job
framework.

The Standard
tMSSqlSCD component belongs to the Business Intelligence and the Databases families.

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
| Property type | Either Built-in or Repository.  * Built-in: No property data stored   centrally. * Repository: Select the Repository   file where Properties are stored. The following fields are pre-filled in   using fetched data. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| JDBC Provider | Select the provider of the JDBC driver to be used, either Microsoft (the default, recommended) or Open source JTDS.  When Microsoft is selected, you need to download the Microsoft JDBC Driver for SQL Server on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774), unpack the downloaded zip file, choose a jar in the unzipped folder based on your JRE version, rename the jar to *mssql-jdbc.jar* and install it manually. For more information about choosing the jar, see the System Requirements information on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774).  When using this component with Datasource in Talend Runtime, you need to use the Open source JTDS driver. |
| Server | Enter the IP address or hostname of the database server or the Azure SQL Data Warehouse to be used. If SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing host name and instance name in this field in the format of `{host_name}\{instance_name}`. In this case, you can leave the Port field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Port | Enter the listening port number of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in the Host field and leave this field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Schema | Enter the name of the DB schema. |
| Database | Enter the name of the database. |
| Username and Password | Enter the authentication data. To enter the password, click the [...] button next to the Password field, enter the password in double quotes in the pop-up dialog box, and then click OK.  You can use Type 2 integrated authentication on Windows by adding `integratedSecurity=true` in the Additional JDBC Parameters field and leave these two fields empty. See section Connecting with integrated authentication On Windows at [Building the connection URL](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?redirectedfrom=MSDN) for related information. |
| Table | Enter the name of the table to be written. Note that only one table can be written at a time. |
| Schema and Edit schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window.   Built-in: The schema is created and stored locally for this component only. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab).  Repository: The schema already exists and is stored in the Repository, hence can be reused. For more information about a component schema in its Basic settings tab, see [Basic settings tab](/talend/r/en-US/8.0/studio-user-guide/basic-settings-tab). |
| SCD Editor | The SCD editor helps to build and configure the data flow for slowly changing dimension outputs. For more information, see [SCD management methodology](/talend/en-US/components/8.0/scd/scd-management-methodology). |
| Use memory saving Mode | Select this checkbox to maximize system performance. |
| Source keys include Null | Select this checkbox to allow the source key columns to have Null values. Information noteWarning: Special attention should be paid to the uniqueness of the source key(s) values when this option is selected. |
| Die on error | This checkbox is cleared by default, meaning to skip the row on error and to complete the process for error-free rows. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair. For example, *encrypt=true;trustServerCertificate=false;* *hostNameInCertificate=\*.database.windows.net;loginTimeout=30;* for Azure SQL database connection.  This field is not available if the Use an existing connection check box is selected. |
| Authenticate using Azure Active Directory | When selected, this option allows you to pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   Read the Usage section of this document for information about Microsoft SQL Server/JDBC encryption requirements.  This option is only available when Microsoft is selected from the JDBC Provider dropdown list in the Basic settings view. |
| Enable always encrypted (Column encryption) | Select this option to use the Microsoft [Always encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15) feature to encrypt and protect your data. To use this option, you need to have previously stored your secrets with [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts):  * Application Client ID: Enter the client ID for the   registered application. This information can be found in the details of your   app under Azure Active Directory > App registrations > Essentials. * Application Client Secret: Enter the client password   for the registered application. This information can be found in the details   of your app under Azure Active Directory > App registrations > Certificates and secrets.   Some limitations regarding query operations and statements apply to this feature. For the exhaustive list of limitations, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15#limitations). |
| End date time details | Specify the time value of the SCD end date time setting in the format of *HH:mm:ss*. The default value for this field is *12:00:00*.  This field appears only when SCD Type 2 is used and Fixed year value is selected for creating the SCD end date. |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |
| Debug mode | Select this checkbox to display each step during processing entries in a database. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE\_UPDATED: the number of rows updated. This is an After variable and it returns an integer.  NB\_LINE\_INSERTED: the number of rows inserted. This is an After variable and it returns an integer.  NB\_LINE\_REJECTED: the number of rows rejected. This is an After variable and it returns an integer.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rules | This component is used as Output component. It requires an Input component and Row main link as input. Information noteImportant: Microsoft SQL Server/JDBC encryption requirements Starting with recent versions of the Microsoft SQL Server JDBC driver, TLS encryption is enabled by default (encrypt=true;trustServerCertificate=false). This enhances security, but if your SQL Server does not support encrypted connections or does not require clients to use TLS, you must set encrypt=false in the JDBC parameters of this component to connect successfully.   * For production or cloud environments using certificates signed by a   trusted authority (e.g., Azure, AWS), no changes are needed, the   default settings will work. * For servers using self-signed certificates, use   encrypt=true;trustServerCertificate=true or   specify the trust store details   (encrypt=true;trustStore=<your\_trust\_store>;trustStorePassword=<your\_trust\_store\_password>). * For non-secure development or test servers, set   encrypt=false in the additional JDBC parameters.   For more information on how to use connections with encryption properties, see [Microsoft SQL JDBC documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-ver17). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | This component does not support using SCD type 0 together with other SCD types. |
