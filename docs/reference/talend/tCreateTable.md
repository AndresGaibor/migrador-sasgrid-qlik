<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/database-utility/tcreatetable · versión 8.0 -->
# tCreateTable

Last updated: 9/30/2026

Creates a table for a specific type of database.

## tCreateTable Standard properties

These properties are used to configure tCreateTable running in the Standard Job framework.

The Standard
tCreateTable component belongs to the Databases family.

The component in this framework is available in all Talend
products.

## Basic settings

| Properties | Description |
| --- | --- |
| Database Type | Select the type of the database. The connection properties may differ slightly according to the database type selected. |
| Property Type | Select the way the connection details will be set.   * Built-In: The connection details will be set   locally for this component. You need to specify the values for all   related connection properties manually. * Repository: The connection details stored   centrally in Repository > Metadata will be reused by this component.  You need to click   the [...] button next to it and in the pop-up   Repository Content dialog box, select the   connection details to be reused, and all related connection   properties will be automatically filled in. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  When a Job contains the parent Job and the child Job, if you need to share an existing connection between the two levels, for example, to share the connection created by the parent Job with the child Job, you have to:   1. In the parent level, register the database connection to be shared    in the Basic settings view of the connection    component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| JDBC Provider | Select the provider of the JDBC driver to be used, either Microsoft (the default, recommended) or Open source JTDS.  When Microsoft is selected, you need to download the Microsoft JDBC Driver for SQL Server on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774), unpack the downloaded zip file, choose a jar in the unzipped folder based on your JRE version, rename the jar to *mssql-jdbc.jar* and install it manually. For more information about choosing the jar, see the System Requirements information on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774).  When using this component with Datasource in Talend Runtime, you need to use the Open source JTDS driver.  This option is available when MSSQLServer is selected from the Database Type drop-down list. |
| DB Version | Select the version of the database. |
| Host | Enter the IP address or the hostname of the database. If you select MSSQLServer from the Database Type dropdown list, enter the IP address or the hostname of the database server or the Azure Synapse Analytics to be used in this field. If the SQL Server Browser service is running on the machine where the MSSQL server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in this field in the format of `{host_name}\{instance_name}`. In this case, you can leave the Port field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Port | Enter the listening port number of the database. If you select MSSQLServer from the Database Type dropdown list, enter the listening port number of the database server or the Azure Synapse Analytics to be used in this field. If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in the Host field and leave this field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Database name | Enter the name of the database. |
| Schema | Enter the name of the database schema. This property is available for DB2, Exasol, Greenplum, Informix, MS SQL Server, Oracle, PostgreSQL, Redshift, Sybase, and Vertica database types. |
| Access File | Enter the path to the Access database file. |
| Firebird File | Enter the path to the Firebird database file. |
| Interbase File | Enter the path to the Interbase database file. |
| SQLite File | Enter the path to the SQLite database file. |
| Running Mode | Select the Server Mode that corresponds to your database setup.  This property is available only for the HSQLDb database type. |
| Use TLS/SSL Sockets | Select this checkbox to enable the security mode if required.  This property is available only for the HSQLDb database type. |
| DB Alias | Enter the name of the database.  This property is available only for the HSQLDb database type. |
| Framework Type | Select the framework type for your database.  This property is available only for the JavaDb database type. |
| DB Root Path | Browse to your database root.  This property is available only for the JavaDb database type. |
| ODBC Name | Enter the name of the ODBC database. |
| Connection Type | Select the Oracle database connection type.   * Oracle SID: select this connection type to uniquely   identify a particular database on a system. * Oracle Service: select this connection type to use the TNS   alias that you give when you connect to the remote database. * Oracle OCI: select this connection type to use Oracle Call   Interface with a set of C-language software APIs that provide an interface to the   Oracle database. * Oracle Custom: select this connection type to access a   clustered database. * WALLET: select this connection type to store credentials   in an Oracle wallet. |
| Account | In the Account field, enter, in double quotation marks, the account name that has been assigned to you by Snowflake.  This property is available only for the Snowflake database type. |
| UserName and Password | Enter the database user authentication data.  To enter the password, click the [...] button next to the Password field, enter the password in double quotes in the pop-up dialog box, and then click OK.  If you select MSSQLServer from the Database Type dropdown list, you can use Type 2 integrated authentication on Windows by adding `integratedSecurity=true` in the Additional JDBC Parameters field and leave these two fields empty. See section Connecting with integrated authentication On Windows at [Building the connection URL](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?redirectedfrom=MSDN) for related information. |
| Role | Enter, in double quotation marks, the default access control role to use to initiate the Snowflake session.  This role must already exist and has been granted to the user ID you are using to connect to Snowflake. If this field is left empty, the PUBLIC role is automatically granted. For information about Snowflake access control model, see [Understanding the Access Control Model](https://docs.snowflake.net/manuals/user-guide/security-access-control.html).  This property is available only for the Snowflake database type. |
| Table name | Enter the name of the table to be created. |
| Table Action | Select the action to be carried out on the table.   * Create table: the specified table doesn't exist and gets created. * Create table if not exists: the specified table is created if it does not exist. * Drop table if exits and create: the table is removed if it already exists and gets created again. |
| Temporary Table | Select this checkbox to create a temporary table during an operation, which is automatically dropped at the end of the operation. Since temporary tables exist in a special schema, you cannot specify a schema name when creating a temporary table, and the name of the temporary table must be distinct from the name of any other table, sequence, index, and view in the same schema. Note that once you select to create a temporary table, you should empty the values when you edit schema.  This field is available only when Postgresql is selected from the Database Type dropdown list. |
| Unlogged Table | Select this checkbox to create an unlogged table during an operation. This way, data is loaded considerably faster than an ordinary table where the data is logged and then written. However, the data in an unlogged table is not crash-safe. This field is available only when Postgresql is selected from the Database Type dropdown list and Temporary Table is not selected. |
| Case Sensitive | Select this checkbox to make the table/column name case sensitive.  This property is available only for the HSQLDb database type. |
| Temporary Table | Select this checkbox if you want to save the created table temporarily.  This property is available only for the MySQL database type. |
| Create | Select the type of the table to be created.   * SET TABLE: the table that does not allow duplicate rows. * MULTISET TABLE: the table that allows duplicate rows.   This property is available only for the Teradata database type. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.   * Built-In: You create and store the schema locally for this component   only. * Repository: You have already created the schema and stored it in the   Repository. You can reuse it in various projects and Job designs.   When the schema to be reused has default values that are integers or functions, ensure that these default values are not enclosed within quotation marks. If they are, you must remove the quotation marks manually.  For more information, see [Retrieving table schemas](/talend/r/en-US/8.0/studio-user-guide/retrieving-table-schemas?tocId=_C1%7EeFOlN%7EGM_JR2qkBYZg).  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC Parameters | Specify additional connection properties for the DB connection you are creating. This option is not available if you have selected the Use an existing connection checkbox in the Basic settings. This property is available for the AS/400 and MSSQL Server database types. |
| Authenticate using Azure Active Directory | When selected, this option allows you pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   This option is available when MSSQLServer is selected from the Database Type dropdown list and Microsoft is selected from the JDBC Provider dropdown list in the Basic settings view. |
| Create projection | Select this checkbox to create a projection. This property is available only for the Vertica database type. |
| Enforce database delimited identifiers | Select this checkbox to enable delimited identifiers. This property is available only for the Snowflake database type.  For more information on delimited identifiers, see <https://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GSQL_identifiers>.  Information noteNote: If you use special characters in your column names, select this checkbox to avoid possible errors or Job execution failure. |
| tStatCatcher Statistics | Select this checkbox to gather the Job processing metadata at the Job level as well as at each component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| QUERY | The query statement being processed. This is a Flow variable and it returns a string. |
| ERROR\_MESSAGE | The error message generated by the component when an error occurs. This is an After variable and it returns a string. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rule | This component can be used as a standalone component of a Job or subJob. |

**Related concepts**  

* [Creating new table in a Mysql Database](tcreatetable-creating-new-table-in-mysql-database-standard-component "The Job described below aims at creating a table in a database, made of a placeholder schema taken from a delimited file schema stored in the Repository. This Job is composed of a single component.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/database-utility/tcreatetable-creating-new-table-in-mysql-database-standard-component -->
# Creating new table in a Mysql Database

Last updated: 9/30/2026

The Job described below aims at creating a table in a database, made of a placeholder schema taken from a delimited file schema
stored in the Repository. This Job is composed of a single
component.

### In this section

* [Procedure](/talend/en-US/components/8.0/database-utility/tcreatetable-procedure-standard-component-drop)

**Related reference**  

* [tCreateTable](tcreatetable "Creates a table for a specific type of database.")


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/database-utility/tcreatetable-procedure-standard-component-drop -->
# Procedure

Last updated: 9/30/2026

## Procedure

1. Drop a tCreateTable component from the
   Databases family in the Palette to the design workspace.
2. In the Basic settings view, and from the
   Database Type list, select Mysql for this
   scenario.
3. From the Table Action list, select Create table.
4. Select the Use Existing Connection check box
   only if you are using a dedicated DB connection component [tMysqlConnection](/talend/en-US/components/8.0/mysql/tmysqlconnection). In this example, we won't use this
   option.
5. In the Property type field, select Repository so that the connection fields that
   follow are automatically filled in. If you have not defined your DB
   connection metadata in the DB connection
   directory under the Metadata node, fill in
   the details manually as Built-in
   .
6. In the Table Name field, fill in a name for
   the table to be created.
7. If you want to retrieve the Schema from the
   Metadata (it doesn't need to be a DB connection Schema metadata), select
   Repository then the relevant entry.
8. In any case (Built-in or Repository)
   click Edit Schema to check the data type
   mappingClick Edit Schema
   to define the data structure.
9. Click the Reset DB Types button in case the
   DB type column is empty or shows discrepancies (marked in orange). This allows
   you to map any data type to the relevant DB data type. Then, click OK to validate your changes and close the dialog
   box.
10. Save your Job and press F6 to execute
    it.

## Results

The table is created empty but with all columns defined in the Schema.
