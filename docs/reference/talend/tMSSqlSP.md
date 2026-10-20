<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp · versión 8.0 -->
# tMSSqlSP

Last updated: 9/30/2026

Offers a convenient way to centralize multiple or complex queries in a database and
calls them easily.

tMSSqlSP calls the stored procedure in
a Microsoft SQL Server or Azure SQL database.

## tMSSqlSP Standard properties

These properties are used to configure tMSSqlSP running in the Standard Job
framework.

The Standard
tMSSqlSP component belongs to the Databases family.

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
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| JDBC Provider | Select the provider of the JDBC driver to be used, either Microsoft (the default, recommended) or Open source JTDS.  When Microsoft is selected, you need to download the Microsoft JDBC Driver for SQL Server on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774), unpack the downloaded zip file, choose a jar in the unzipped folder based on your JRE version, rename the jar to *mssql-jdbc.jar* and install it manually. For more information about choosing the jar, see the System Requirements information on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774).  Note that OSGi builds will not include any open source jTDS JDBC driver. If you need to build your Job containing this component as an OSGi bundle, use the official Microsoft JDBC driver; otherwise, this component will work only with Datasource with the jTDS JDBC driver properly installed in Talend Runtime. |
| Host | Enter the IP address or the hostname of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in this field in the format of `{host_name}\{instance_name}`. In this case, you can leave the Port field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Port | Enter the listening port number of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in the Host field and leave this field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Database | Enter the name of the database. |
| Schema | Enter the name of the database schema. |
| Username and Password | Enter the authentication data. To enter the password, click the [...] button next to the Password field, enter the password in double quotes in the pop-up dialog box, and then click OK.  You can use Type 2 integrated authentication on Windows by adding `integratedSecurity=true` in the Additional JDBC Parameters field and leave these two fields empty. See section Connecting with integrated authentication On Windows at [Building the connection URL](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?redirectedfrom=MSDN) for related information. |
| Schema and Edit Schema | In SP principle, the schema is an input parameter. A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| SP Name | Type in the exact name of the Stored Procedure |
| Is Function / Return result in | Select this checkbox, if only a value is to be returned. Select on the list the schema column, the value to be returned is based on. |
| Parameters | Click the Plus button and select the various Schema Columns that will be required by the procedures. Note that the SP schema can hold more columns than there are parameters used in the procedure. Select the Type of parameter:  IN: Input parameter  OUT: Output parameter/return value  IN OUT: Input parameter is to be returned as value, likely after modification through the procedure (function).  RECORDSET: Input parameter is to be returned as a set of values, rather than single value.  Information noteNote: Check [Inserting data in mother/daughter tables](/talend/en-US/components/8.0/mysql/tmysqlconnection-tmysqlrollback-tfileinputdelimited-inserting-data-in-mother-daughter-tables-standard-component-the), if you want to analyze a set of records from a database table or DB query and return single records. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  This checkbox is not available when the Use an existing connection checkbox is selected. |
| Data source alias | Enter the alias of the data source created on the *Talend Runtime* side.  This field is available only when the Specify a data source alias checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair. For example, *encrypt=true;trustServerCertificate=false;* *hostNameInCertificate=\*.database.windows.net;loginTimeout=30;* for Azure SQL database connection.  This field is not available if the Use an existing connection check box is selected. |
| Authenticate using Azure Active Directory | When selected, this option allows you to pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   Read the Usage section of this document for information about Microsoft SQL Server/JDBC encryption requirements.  This option is only available when Microsoft is selected from the JDBC Provider dropdown list in the Basic settings view. |
| Enable always encrypted (Column encryption) | Select this option to use the Microsoft [Always encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15) feature to encrypt and protect your data. To use this option, you need to have previously stored your secrets with [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts):  * Application Client ID: Enter the client ID for the   registered application. This information can be found in the details of your   app under Azure Active Directory > App registrations > Essentials. * Application Client Secret: Enter the client password   for the registered application. This information can be found in the details   of your app under Azure Active Directory > App registrations > Certificates and secrets.   Some limitations regarding query operations and statements apply to this feature. For the exhaustive list of limitations, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15#limitations). |
| tStatCatcher Statistics | Select this checkbox to collect log data at the component level. |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rules | This component is used as intermediary component. It can be used as start component but only input parameters are thus allowed. Information noteImportant: Microsoft SQL Server/JDBC encryption requirements Starting with recent versions of the Microsoft SQL Server JDBC driver, TLS encryption is enabled by default (encrypt=true;trustServerCertificate=false). This enhances security, but if your SQL Server does not support encrypted connections or does not require clients to use TLS, you must set encrypt=false in the JDBC parameters of this component to connect successfully.   * For production or cloud environments using certificates signed by a   trusted authority (e.g., Azure, AWS), no changes are needed, the   default settings will work. * For servers using self-signed certificates, use   encrypt=true;trustServerCertificate=true or   specify the trust store details   (encrypt=true;trustStore=<your\_trust\_store>;trustStorePassword=<your\_trust\_store\_password>). * For non-secure development or test servers, set   encrypt=false in the additional JDBC parameters.   For more information on how to use connections with encryption properties, see [Microsoft SQL JDBC documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-ver17). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | The Stored Procedures syntax should match the Database syntax. Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Retrieving personal information using a stored procedure](tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-retrieving-personal-information-using-stored-procedure-standard-component-this)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-retrieving-personal-information-using-stored-procedure-standard-component-this -->
# Retrieving personal information using a stored procedure

Last updated: 9/30/2026

This scenario describes a Job that retrieves a personal information record from a
specified table using a stored procedure according to the *id* value defined in the input flow.

In this scenario, the table to retrieve data from contains the personal information.
To reproduce this scenario, you can write the data into the table from a CSV file like
the following. For how to write data into a MS SQL table, see [Inserting data into a database table and extracting useful information from
it](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-inserting-data-into-database-table-and-extracting-useful-information-from-it-standard-component-the).

```
id;name;sex;age
1;Ford;Male;25
2;Rose;Female;30
3;Sabrina;Female;28
4;Teddy;Male;32
5;Kate;Male;35
```

In this scenario, the stored procedure used to retrieve the personal information is as
follows:

```
CREATE PROCEDURE [dbo].[QueryPerson]
@id int,
@name varchar(50)
AS
BEGIN
SET NOCOUNT ON
SELECT * FROM dbo.person where id=@id
END
```

### In this section

* [Dropping and linking the components](/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-dropping-and-linking-components-standard-component-create)
* [Configuring the components](/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tMSSqlSP](tmssqlsp "Offers a convenient way to centralize multiple or complex queries in a database and calls them easily.")

**Related information**  

* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)
* [tParseRecordSet](/talend/en-US/components/8.0/db-generic/tparserecordset)
* [tFixedFlowInput](/talend/en-US/components/8.0/tfixedflowinput/tfixedflowinput)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Configuring the input component](/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-input-component-standard-component)
* [Configuring the tMSSqlSP component](/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-tmssqlsp-component-standard-component)
* [Configuring the tParseRecordSet component](/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-tparserecordset-component-standard-component)
* [Configuring the output components](/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-output-components-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-dropping-and-linking-components-standard-component-create -->
# Dropping and linking the components

Last updated: 9/30/2026

## Procedure

1. Create a new Job and add the following components by typing their names in
   the design workspace or dropping them from the Palette: a tFixedFlowInput
   component, a tMSSqlSP component, a
   tParseRecordSet component, and two
   tLogRow components.
2. Connect tFixedFlowInput to tMSSqlSP using a Row > Main link.
3. Do the same to connect tMSSqlSP to the
   first tLogRow, the first tLogRow to tParseRecordSet, and tParseRecordSet to the second tLogRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl + S to save the Job.
2. Press F6 to run the Job.

   The personal information with the id of *4* in the MS SQL table is displayed in the lower table on the
   console. Note that the values of the *id*
   and *name* columns shown in the upper table
   are the input data.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-input-component-standard-component -->
# Configuring the input component

Last updated: 9/30/2026

## Procedure

1. Double-click tFixedFlowInput to open its
   Basic settings view.
2. Click the [...] button next to Edit schema to open the schema editor.

   Click the [+] button to add two columns:
   *id* of the integer type and *name* of the string type.

   Click OK to close the schema
   editor.
3. In the Mode area, fill each column with
   respective value. In this example, the *id*
   value is set to *4*, and the *name* value is null since it is not used in the
   select SQL statement in the stored procedure.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-output-components-standard-component -->
# Configuring the output components

Last updated: 9/30/2026

## Procedure

1. Double-click the first tLogRow to open
   its Basic settings view.

   In the Mode area, select Vertical (each row is a key/value list) for a
   better display of the result.
2. Do the same to configure the second tLogRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-tmssqlsp-component-standard-component -->
# Configuring the tMSSqlSP component

Last updated: 9/30/2026

## Procedure

1. Double-click tMSSqlSP to open its
   Basic settings view.
2. Fill in the Host, Port, Schema, Database, Username, and Password
   fields with your MS SQL Server connection details.
3. In the SP Name field, enter the name of
   the stored procedure to be used. In this example, it is *QueryPerson*.
4. Click the [...] button next to Edit schema to open the schema editor.

   Click the
   button to copy all columns from the input schema to the
   output schema, and then click the [+]
   button in the right panel to add a new column *person* of the object type to hold the personal information
   to be retrieved from the database.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
5. In the Parameters area, click the
   [+] button to add three rows and select
   a schema column and its type for each row. In this example, the *id* and *name*
   columns are of type IN, and the *person* column is of type RECORD SET.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlsp-tlogrow-tparserecordset-tfixedflowinput-configuring-tparserecordset-component-standard-component -->
# Configuring the tParseRecordSet component

Last updated: 9/30/2026

## Procedure

1. Double-click tParseRecordSet to open its
   Basic settings view.
2. From the Prev. Comp. Column list
   drop-down list, select the column that holds the personal information to be
   parsed. In this example, it is *person*.
3. Click the [...] button next to Edit schema to open the schema editor.

   Click the [+] button in the right panel
   to add four columns: *id* and *age* of the integer type, and *name* and *sex*
   of the string type.

   Click OK to close the schema editor and
   accept the propagation prompted by the pop-up dialog box.
4. In the Attribute table area, fill in each
   Value column with the corresponding
   column name in the MS SQL Server table that holds the personal
   information.
