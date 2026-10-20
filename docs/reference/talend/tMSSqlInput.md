<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput · versión 8.0 -->
# tMSSqlInput

Last updated: 9/30/2026

Executes a DB query with a strictly defined order which must correspond to the
schema definition.

tMSSqlInput reads data and extracts
fields based on a query from a Microsoft SQL Server database or a Microsoft Azure SQL
database. Then it passes on the field list to the next component via a Main row link.

## tMSSqlInput Standard properties

These properties are used to configure tMSSqlInput running in the Standard Job
framework.

The Standard
tMSSqlInput component belongs to the Databases family.

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
|  | Click this icon to open a database connection wizard and store the database connection parameters you set in the component Basic settings view. For more information about setting up and storing database connection parameters, see [Centralizing database metadata](/talend/r/en-US/8.0/studio-user-guide/centralizing-database-metadata). |
| JDBC Provider | Select the provider of the JDBC driver to be used, either Microsoft (the default, recommended) or Open source JTDS.  When Microsoft is selected, you need to download the Microsoft JDBC Driver for SQL Server on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774), unpack the downloaded zip file, choose a jar in the unzipped folder based on your JRE version, rename the jar to *mssql-jdbc.jar* and install it manually. For more information about choosing the jar, see the System Requirements information on [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=11774).  Note that OSGi builds will not include any open source jTDS JDBC driver. If you need to build your Job containing this component as an OSGi bundle, use the official Microsoft JDBC driver; otherwise, this component will work only with Datasource with the jTDS JDBC driver properly installed in Talend Runtime. |
| Use an existing connection | Select this check box and in the Component List drop-down list, select the desired connection component to reuse the connection details you already defined.  Information noteNote: When a Job contains the parent Job and the child Job, do the following if you want to share an existing connection between the parent Job and the child Job (for example, to share the connection created by the parent Job with the child Job).  1. In the parent level, register the database connection to be shared    in the Basic settings view of the    connection component which creates that very database connection. 2. In the child level, use a dedicated connection component to read    that registered database connection.   For an example about how to share a database connection across Job levels, see [Sharing a database connection](/talend/r/en-US/7.3/studio-user-guide/sharing-database-connection). |
| Host | Enter the IP address or the hostname of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in this field in the format of `{host_name}\{instance_name}`. In this case, you can leave the Port field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Port | Enter the listening port number of the database server or the Azure Synapse Analytics to be used.  If the SQL Server Browser service is running on the machine where the server resides, you can connect to a named instance through a TCP dynamic port by providing the host name and the instance name in the Host field and leave this field empty. See [SQL Server Browser service](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) for related information. |
| Database | Enter the name of the database. |
| Schema | Enter the name of the database schema. |
| Username and Password | Enter the authentication data. To enter the password, click the [...] button next to the Password field, enter the password in double quotes in the pop-up dialog box, and then click OK.  You can use Type 2 integrated authentication on Windows by adding `integratedSecurity=true` in the Additional JDBC Parameters field and leave these two fields empty. See section Connecting with integrated authentication On Windows at [Building the connection URL](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?redirectedfrom=MSDN) for related information. |
| Schema and Edit Schema | A schema is a row description. It defines the number of fields (columns) to be processed and passed on to the next component. When you create a Spark Job, avoid the reserved word `line` when naming the fields.  This component offers the advantage of the dynamic schema feature. This allows you to retrieve unknown columns from source files or to copy batches of columns from a source without mapping each column individually. For further information about dynamic schemas, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema).  This dynamic schema feature is designed for the purpose of retrieving unknown columns of a table and is recommended to be used for this purpose only; it is not recommended for the use of creating tables.  Built-In: You create and store the schema locally for this component only.  Repository: You have already created the schema and stored it in the Repository. You can reuse it in various projects and Job designs.  Click Edit schema to make changes to the schema. If the current schema is of the Repository type, three options are available:   * View schema: choose this   option to view the schema only. * Change to built-in property:   choose this option to change the schema to Built-in for local changes. * Update repository connection:   choose this option to change the schema stored in the repository and decide whether   to propagate the changes to all the Jobs upon completion.  If you just want to   propagate the changes to the current Job, you can select No upon completion and choose this schema metadata   again in the Repository Content   window. |
| Query type and Query | Enter your DB query paying particularly attention to properly sequence the fields in order to match the schema definition.  If using the dynamic schema feature, the SELECT query must include the \* wildcard, to retrieve all of the columns from the table selected. |
| Specify a data source alias | Select this checkbox and specify the alias of a data source created on the *Talend Runtime* side to use the shared connection pool defined in the data source configuration. This option works only when you deploy and run your Job in *Talend Runtime*.  This checkbox is not available when the Use an existing connection checkbox is selected. |
| Data source alias | Enter the alias of the data source created on the *Talend Runtime* side.  This field is available only when the Specify a data source alias checkbox is selected. |

## Advanced settings

| Properties | Description |
| --- | --- |
| Additional JDBC parameters | Specify additional connection properties for the database connection you are creating. The properties are separated by semicolon and each property is a key-value pair. For example, *encrypt=true;trustServerCertificate=false;* *hostNameInCertificate=\*.database.windows.net;loginTimeout=30;* for Azure SQL database connection.  This field is not available if the Use an existing connection check box is selected. |
| Authenticate using Azure Active Directory | When selected, this option allows you to pick the authentication mode to use from the Azure Active Directory authentication mode dropdown list:  * Service principal (client secret): use the service   principal credentials (client ID and client secret) to authenticate. * User password: use the Azure Active Directory user   credentials (username and password) to authenticate.   Read the Usage section of this document for information about Microsoft SQL Server/JDBC encryption requirements.  This option is only available when Microsoft is selected from the JDBC Provider dropdown list in the Basic settings view. |
| Enable always encrypted (Column encryption) | Select this option to use the Microsoft [Always encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15) feature to encrypt and protect your data. To use this option, you need to have previously stored your secrets with [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/basic-concepts):  * Application Client ID: Enter the client ID for the   registered application. This information can be found in the details of your   app under Azure Active Directory > App registrations > Essentials. * Application Client Secret: Enter the client password   for the registered application. This information can be found in the details   of your app under Azure Active Directory > App registrations > Certificates and secrets.   Some limitations regarding query operations and statements apply to this feature. For the exhaustive list of limitations, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15#limitations). |
| Trim all the String/Char columns | Select this checkbox to remove leading and trailing whitespace from all the String/Char columns. |
| Trim column | Remove leading and trailing whitespace from defined columns. |
| Set Query Timeout | Select this option to set a timeout period for the query or the batch query. The Job will be terminated if the query or the batch query is timed out. You can set the timeout period (in seconds) in the Timeout field. Information noteNote:  * This option applies to batch queries if you use the JDBC driver provided   by Microsoft (that is, select `Microsoft` from the   JDBC Provider drop-down list). It applies to   individual queries if you use the JTDS driver (that is, select   `Open source JTDS` from the JDBC   Provider drop-down list). * This option is available only when you have installed the R2021-12   Talend Studio Monthly update or a later one delivered by Talend. For more information, check with your administrator. |
| tStat Catcher Statistics | Select this checkbox to collect log data at the component level. |

## Global Variables

| Variables | Description |
| --- | --- |
| Global Variables | NB\_LINE: the number of rows processed. This is an After variable and it returns an integer.  QUERY: the query statement being processed. This is a Flow variable and it returns a string.  ERROR\_MESSAGE: the error message generated by the component when an error occurs. This is an After variable and it returns a string. This variable functions only if the Die on error checkbox is cleared, if the component has this checkbox.  A Flow variable functions during the execution of a component while an After variable functions after the execution of the component.  To fill up a field or expression with a variable, press Ctrl+Space to access the variable list and choose the variable to use from it.  For more information about variables, see [Using contexts and variables](/talend/r/en-US/8.0/studio-user-guide/contexts-and-variables). |

## Usage

| Usage guidance | Description |
| --- | --- |
| Usage rules | This component covers all possible SQL queries for MS SQL server databases. Information noteImportant: Microsoft SQL Server/JDBC encryption requirements Starting with recent versions of the Microsoft SQL Server JDBC driver, TLS encryption is enabled by default (encrypt=true;trustServerCertificate=false). This enhances security, but if your SQL Server does not support encrypted connections or does not require clients to use TLS, you must set encrypt=false in the JDBC parameters of this component to connect successfully.   * For production or cloud environments using certificates signed by a   trusted authority (e.g., Azure, AWS), no changes are needed, the   default settings will work. * For servers using self-signed certificates, use   encrypt=true;trustServerCertificate=true or   specify the trust store details   (encrypt=true;trustStore=<your\_trust\_store>;trustStorePassword=<your\_trust\_store\_password>). * For non-secure development or test servers, set   encrypt=false in the additional JDBC parameters.   For more information on how to use connections with encryption properties, see [Microsoft SQL JDBC documentation](https://learn.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-ver17). |
| Dynamic settings | Click the [+] button to add a row in the table and fill the Code field with a context variable to choose your database connection dynamically from multiple connections planned in your Job. This feature is useful when you need to access database tables having the same data structure but in different databases, especially when you are working in an environment where you cannot change your Job settings, for example, when your Job has to be deployed and executed independent of Talend Studio.  The Dynamic settings table is available only when the Use an existing connection check box is selected in the Basic settings view. Once a dynamic parameter is defined, the Component List box in the Basic settings view becomes unusable.  For examples on using dynamic parameters, see [Reading data from databases through context-based dynamic connections](/talend/r/en-US/8.0/components/defining-context-groups/reading-data-from-databases-through-context-based-dynamic-connections) and [Reading data from different MySQL databases using dynamically loaded connection parameters](/talend/r/en-US/8.0/components/context/reading-data-from-different-mysql-databases-using-dynamically-loaded-connection-parameters). For more information on Dynamic settings and context variables, see [Dynamic schema](/talend/r/en-US/8.0/studio-user-guide/dynamic-schema) and [Creating a context group and define context variables in it](/talend/r/en-US/8.0/studio-user-guide/creating-context-group-and-define-context-variables-in-it). |
| Limitation | Due to license incompatibility, one or more JARs required to use this component are not provided. You can install the missing JARs for this particular component by clicking the Install button on the Component tab view. You can also find out and add all missing JARs easily on the Modules tab in the Integration perspective of Talend Studio. For details, see [Installing external modules](/talend/r/en-US/8.0/studio-user-guide/installing-external-modules). |

**Related concepts**  

* [Inserting data into a database table and extracting useful information from it](tmssqlinput-tmssqloutput-tlogrow-inserting-data-into-database-table-and-extracting-useful-information-from-it-standard-component-the)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-inserting-data-into-database-table-and-extracting-useful-information-from-it-standard-component-the -->
# Inserting data into a database table and extracting useful information from it

Last updated: 9/30/2026

The scenario describes a Job that reads the employee data from a text file, inserts the
data into a table of an MSSQL database, then extracts useful data from the table, and
displays the information on the console.

This scenario involves the following components:

* tMSSqlConnection: establishes a connection to the
  MSSQL server.
* tFileInputDelimited: reads the input file,
  defines the data structure and sends it to the next component.
* tMSSqlOutput: writes data it receives from the
  preceding component into a table of an MSSQL database.
* tMSSqlInput: extracts data from the table based
  on an SQL query.
* tLogRow: displays the information it receives
  from the preceding component on the console.
* tMSSqlCommit: commits the transaction in the
  connected MSSQL server.

### In this section

* [Setting up the Job](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-setting-up-job-standard-component-drop)
* [Configuring the components](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-configuring-components-standard-component)
* [Saving and executing the Job](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-saving-and-executing-job-standard-component-press)

**Related reference**  

* [tMSSqlInput](tmssqlinput "Executes a DB query with a strictly defined order which must correspond to the schema definition.")
* [tMSSqlOutput](tmssqloutput "Executes the action defined on the table and/or on the data contained in the table, based on the flow incoming from the preceding component in the Job.")
* [tMSSqlConnection](tmssqlconnection "Opens a connection to the specified database that can then be reused in the subsequent subJob or subJobs.")
* [tMSSqlCommit](tmssqlcommit "Commits in one go, using a unique connection, a global transaction instead of doing that on every row or every batch and thus provides gain in performance.")

**Related information**  

* [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited)
* [tLogRow](/talend/en-US/components/8.0/logs-and-errors/tlogrow)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-configuring-components-standard-component -->
# Configuring the components

Last updated: 9/30/2026

### In this section

* [Opening a connection to the MSSQL server](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-opening-connection-to-mssql-server-standard-component)
* [Reading the input data](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-reading-input-data-standard-component)
* [Writing the data into the database table](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-writing-data-into-database-table-standard-component)
* [Extracting useful information from the table](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-extracting-useful-information-from-table-standard-component)
* [Displaying information on the console](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-displaying-information-on-console-standard-component)
* [Committing the transaction and closing the connection](/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-committing-transaction-and-closing-connection-standard-component)


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-saving-and-executing-job-standard-component-press -->
# Saving and executing the Job

Last updated: 9/30/2026

## Procedure

1. Press Ctrl+S to save your Job.
2. Execute the Job by pressing F6 or clicking
   Run on the Run tab.

   The information of employees whose wages are above the average value ordered
   by id is displayed on the console.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-setting-up-job-standard-component-drop -->
# Setting up the Job

Last updated: 9/30/2026

## Procedure

1. Drop the following components from the Palette onto the design workspace: tMSSqlConnection, tFileInputDelimited, tMSSqlOutput, tMSSqlInput,
   tLogRow, and tMSSqlCommit.
2. Connect tMSSqlConnection to tFileInputDelimited using a Trigger > OnSubjobOk
   link.
3. Do the same to connect tFileInputDelimited to
   tMSSqlInput and tMSSqlInput to tMSSqlCommit.
4. Connect tFileInputDelimited to tMSSqlOutput using a Row > Main link.
5. Do the same to connect tMSSqlInput to
   tLogRow.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-committing-transaction-and-closing-connection-standard-component -->
# Committing the transaction and closing the connection

Last updated: 9/30/2026

## Procedure

1. Double-click the tMSSqlCommit component to
   open its Basic settings view.
2. Select the Close Connection check box.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-displaying-information-on-console-standard-component -->
# Displaying information on the console

Last updated: 9/30/2026

## Procedure

1. Double-click the tLogRow component to open
   its Basic settings view.
2. In the Mode area, select Table (print values in cells of a table).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-extracting-useful-information-from-table-standard-component -->
# Extracting useful information from the table

Last updated: 9/30/2026

## Procedure

1. Double-click the tMSSqlInput component to
   open its Basic settings view in the Component tab.
2. Select the Use an existing connection check
   box. If multiple connections are available, select the connection you want to
   use from the Component List drop-down
   list.
3. Click Edit schema to define the data
   structure to be read from the table. In this example, we need to read all three
   columns from the table.
4. In the Table Name field, type in the name of
   the table you want to read the data from: *Wage\_Info* in this example.
5. In the Query field, fill in the SQL query to
   be executed on the table specified. To obtain the data of employees whose wages
   are above the average value and order them by id, enter the SQL query as
   follows:SELECT \*
   FROM Wage\_Info
   WHERE wage >
   (SELECT avg(wage)
   FROM Wage\_Info)
   ORDER BY id


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-opening-connection-to-mssql-server-standard-component -->
# Opening a connection to the MSSQL server

Last updated: 9/30/2026

## Procedure

1. Double-click the tMSSqlConnection component
   to open its Basic settings view in theComponent tab.
2. In the Host field, type in the IP address or
   hostname of the MSSQL server, *192.168.30.47*
   in this example.
3. In the Port field, type in the port number of
   the database server, *1433* in this
   example.
4. In the Schema field, type in the schema name,
   *dbo* in this example.
5. In the Database field, type in the database
   name, *talend* in this example.
6. In the Username and Password fields, enter the credentials for the MSSQL
   connection.


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-reading-input-data-standard-component -->
# Reading the input data

Last updated: 9/30/2026

## Procedure

1. Double-click the tFileInputDelimited
   component to open its Component view.
2. Click the [...] button next to the File Name/Stream field to browse to the input file.
   In this example, it is *D:/Input/Employee\_Wage.txt*. This text file holds three columns:
   *id*, *name* and *wage*.
   id;name;wage
   51;Harry;2300
   40;Ronald;3796
   17;Theodore;2174
   21;James;1986
   2;George;2591
   89;Calvin;2362
   84;Ulysses;3383
   4;Lyndon;2264
   17;Franklin;1780
   86;Lyndon;3999
3. In the Header field, type in *1* to skip the first row of the input file.
4. Click Edit schema to define the data to pass
   on to the tMSSqlOutput component. In this
   example, we define *id* as the key, and specify
   the length and precision for each column respectively.

   Click OK to close the schema editor. A dialog
   box opens, and you can choose to propagate the schema to the next
   component.

   Related topic: [tFileInputDelimited](/talend/en-US/components/8.0/delimited/tfileinputdelimited).


---
<!-- fuente: https://help.qlik.com/talend/en-US/components/8.0/mssql/tmssqlinput-tmssqloutput-tlogrow-writing-data-into-database-table-standard-component -->
# Writing the data into the database table

Last updated: 9/30/2026

## Procedure

1. Double-click the tMSSqlOutput component to
   open its Basic settings view in the Component tab.
2. Type in required information for the connection or use the existing connection
   you have configured before. In this example, we select the Use an existing connection check box. If multiple connections
   are available, select the connection you want to use from the Component List drop-down list.
3. In the Table field, type in the name of the
   table you want to write the data to: *Wage\_Info* in this example. You can also click the [...] button next to the Table field to open a dialog box and select a proper
   table.
4. Select Create table if does not
   exist from the Action on table
   drop-down list.
5. Select Insert if not exist
   from the Action on data drop-down list.
6. Click Sync columns to retrieve the schema
   from the preceding component.
